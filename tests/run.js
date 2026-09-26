#!/usr/bin/env node
'use strict';
/* ============================================================
   Batterie de tests navigateur — Révisions PTSI
   ============================================================
   Point d'entrée UNIQUE, 100 % node (aucun bash, aucun http-server) :
     node tests/run.js                 → toutes les suites
     node tests/run.js --rapide        → échantillon (~10 chapitres, 5 matières)
     node tests/run.js --suite=site,mobile --chapitres=rlc,optgeo
     node tests/run.js --aide          → toutes les options
   Le script démarre son propre petit serveur (tests/lib/serveur.js) sur un
   port libre, pilote Chromium via Playwright, écrit captures + rapport JSON
   dans tests/sortie/ et se termine avec un code ≠ 0 si un test échoue.
   Mode d'emploi détaillé : tests/README.md */
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { demarrerServeur } = require('./lib/serveur');
const { suivreErreurs, pause } = require('./lib/outils');

const RACINE_DEPOT = path.resolve(__dirname, '..');
const SUITES = ['site', 'mobile', 'interactions', 'pwa', 'regressions'];

/* Échantillon du mode --rapide : une dizaine de chapitres couvrant les 5
   matières (dont le chapitre par défaut, des simulateurs, des formules longues).
   Un id absent de CHAPTERS est ignoré ; une matière absente de la liste est
   complétée par son premier chapitre. */
const ECHANTILLON_RAPIDE = ['rlc', 'optgeo', 'mecpt', 'complexes', 'polynomes', 'va', 'slci', 'ingsys', 'pyrepr', 'enusuels'];

/* Ctrl+C pendant un lancement : plus rien n'est affiché ni écrit (voir main()) */
let interrompu = false;

/* ---------- Couleurs du terminal (désactivées hors terminal ou avec NO_COLOR) ---------- */
const COULEUR = process.stdout.isTTY && !process.env.NO_COLOR;
const teinte = code => s => (COULEUR ? '\x1b[' + code + 'm' + s + '\x1b[0m' : s);
const vert = teinte('32'), rouge = teinte('31'), jaune = teinte('33'), gras = teinte('1'), gris = teinte('90');

/* ---------- Options de la ligne de commande ---------- */
function lireOptions(argv) {
  const o = { rapide: false, suites: SUITES.slice(), chapitres: null, racine: RACINE_DEPOT,
    sortie: path.join(__dirname, 'sortie'), visible: false, aide: false };
  for (const arg of argv) {
    const [cle, ...reste] = arg.replace(/^--?/, '').split('=');
    const val = reste.join('=');
    switch (cle) {
      case 'rapide': o.rapide = true; break;
      case 'suite': case 'suites':
        o.suites = val.split(',').map(s => s.trim()).filter(Boolean);
        if (!o.suites.length) throw new Error('--suite sans aucun nom (suites : ' + SUITES.join(', ') + ')');
        break;
      case 'chapitres': case 'chapitre':
        o.chapitres = val.split(',').map(s => s.trim()).filter(Boolean);
        if (!o.chapitres.length) throw new Error('--chapitres sans aucun id (ex. --chapitres=rlc,optgeo)');
        break;
      case 'racine': o.racine = path.resolve(val); break;
      case 'sortie': o.sortie = path.resolve(val); break;
      case 'visible': o.visible = true; break;
      case 'aide': case 'help': case 'h': o.aide = true; break;
      default: throw new Error('option inconnue : ' + arg + ' (voir --aide)');
    }
  }
  const inconnues = o.suites.filter(s => !SUITES.includes(s));
  if (inconnues.length) throw new Error('suite inconnue : ' + inconnues.join(', ') + ' (suites : ' + SUITES.join(', ') + ')');
  return o;
}

function afficherAide() {
  console.log(`
Batterie de tests navigateur — Révisions PTSI

Usage :  node tests/run.js [options]      (ou : npm test, npm run test:rapide)

Options :
  --rapide               échantillon d'une dizaine de chapitres (5 matières)
                         + tous les simulateurs dans un seul thème (clair)
  --suite=nom[,nom]      suites à lancer parmi : ${SUITES.join(', ')}
  --chapitres=id[,id]    limite les boucles de chapitres à ces ids (ex. rlc,optgeo) ;
                         un prefix est accepté (og = optgeo) ; nom inconnu → arrêt (code 2)
  --racine=dossier       dossier du site à tester (défaut : racine du dépôt)
  --sortie=dossier       captures + rapport.json (défaut : tests/sortie/)
  --visible              ouvre une vraie fenêtre Chromium (pour observer / déboguer)
  --aide                 affiche cette aide

Code de sortie : 0 si tout passe, 1 si au moins un test échoue, 2 si le
harnais lui-même ne peut pas démarrer (Playwright absent, site introuvable…),
130 si le lancement est interrompu par Ctrl+C (aucun rapport écrit).
`);
}

/* ---------- Chargement de Playwright ----------
   1) installation locale du dépôt (npm install) ou NODE_PATH ;
   2) sinon installation globale (npm root -g), cas du conteneur Claude Code. */
function chargerPlaywright() {
  try { return require('playwright'); } catch (e) { /* essai suivant */ }
  let racineGlobale = null;
  try {
    racineGlobale = execSync('npm root -g', { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'], timeout: 30000 }).trim();
  } catch (e) { /* npm introuvable */ }
  if (racineGlobale) {
    for (const nom of ['playwright', '@playwright/test']) {
      const p = path.join(racineGlobale, nom);
      if (fs.existsSync(p)) { try { return require(p); } catch (e) { /* essai suivant */ } }
    }
  }
  console.error(rouge(gras('\nPlaywright est introuvable.')) + `
Il sert à piloter le navigateur Chromium pendant les tests. Pour l'installer,
ouvrez un terminal DANS le dossier du dépôt (revisions-ptsi) et tapez :

    npm install
    npx playwright install chromium

(il faut Node.js 18 ou plus récent : https://nodejs.org). Voir tests/README.md.
`);
  process.exit(2);
}

/* Erreur d'utilisation détectée pendant une suite (ex. --chapitres inconnu) :
   le harnais s'arrête avec le code 2 au lieu de compter un simple échec. */
function erreurHarnais(message) { const e = new Error(message); e.harnais = true; return e; }

/* ---------- Résultats d'une suite ---------- */
class ResultatSuite {
  constructor(nom) {
    this.nom = nom; this.controles = []; this.avertissements = []; this.infos = {};
    this.debut = Date.now(); this.duree = 0;
  }
  _ajouter(nom, statut, messages, detail) {
    if (interrompu) return;   // navigateur fermé par Ctrl+C : faux échecs, rien à afficher
    const msgs = (Array.isArray(messages) ? messages : [messages]).filter(m => m != null && m !== '').map(String);
    this.controles.push({ nom, statut, messages: msgs, detail: detail === undefined ? null : detail });
    const marque = statut === 'ok' ? vert('  ok  ') : rouge('ÉCHEC ');
    console.log('   ' + marque + ' ' + nom);
    if (statut !== 'ok') msgs.slice(0, 8).forEach(m => console.log('          ' + rouge('x ') + m));
    if (statut !== 'ok' && msgs.length > 8) console.log('          ' + gris('… et ' + (msgs.length - 8) + ' autre(s) (voir rapport.json)'));
  }
  ok(nom, detail) { this._ajouter(nom, 'ok', [], detail); }
  echec(nom, messages, detail) { this._ajouter(nom, 'echec', messages, detail); }
  /* condition vraie → ok ; sinon échec avec le(s) message(s) */
  verifier(nom, condition, messages, detail) {
    if (condition) this.ok(nom, detail); else this.echec(nom, messages, detail);
    return !!condition;
  }
  avertir(message) {
    if (interrompu) return;
    this.avertissements.push(String(message));
    console.log('   ' + jaune('  !   ') + ' ' + message);
  }
  info(cle, valeur) { this.infos[cle] = valeur; }
  get enEchec() { return this.controles.filter(c => c.statut !== 'ok'); }
}

const duree = ms => {
  const s = Math.round(ms / 1000);
  return s < 60 ? s + ' s' : Math.floor(s / 60) + ' min ' + String(s % 60).padStart(2, '0') + ' s';
};

/* Exécute une promesse avec un délai maximal */
function avecDelai(promesse, ms, quoi) {
  let t;
  return Promise.race([
    promesse,
    new Promise((_, rej) => { t = setTimeout(() => rej(new Error(quoi + ' : délai maximal dépassé (' + duree(ms) + ')')), ms); }),
  ]).finally(() => clearTimeout(t));
}

/* ---------- Contexte fourni à chaque suite ---------- */
function creerContexte({ pw, navigateur, serveur, options, nomSuite }) {
  const contextes = [], journaux = [];
  const ctx = {
    journaux,   // journaux de toutes les pages de la suite (erreurs JS…)
    pw, navigateur, serveur, options,
    base: serveur.url,
    /* URL du site : ctx.url('#rlc/cours') ou ctx.url('#rlc/flash', { variante: 'b2', op: 'inversion' }) */
    url(hash, params) {
      let u = serveur.url;
      if (params && Object.keys(params).length) u += '?' + new URLSearchParams(params).toString();
      if (hash) u += (hash.startsWith('#') ? '' : '#') + hash;
      return u;
    },
    /* Nouveau contexte Chromium isolé (stockage vierge) + une page + son journal.
       Par défaut : bureau 1400×900, service workers BLOQUÉS, thème clair. */
    async nouvellePage(o) {
      o = o || {};
      const opts = {
        viewport: { width: o.largeur || (o.mobile ? 390 : 1400), height: o.hauteur || (o.mobile ? 844 : 900) },
        serviceWorkers: o.sw ? 'allow' : 'block',
        colorScheme: 'light', locale: 'fr-FR', acceptDownloads: true,
      };
      if (o.mobile) Object.assign(opts, { isMobile: true, hasTouch: true, deviceScaleFactor: o.dpr || 2 });
      const contexte = await navigateur.newContext(opts);
      contextes.push(contexte);
      // Toute requête vers un autre serveur est bloquée (le test ne dépend pas du réseau) ;
      // le journal la signale quand même comme « requête EXTERNE ».
      const origine = new URL(serveur.url).origin;
      await contexte.route(u => u.origin !== origine, r => r.abort('blockedbyclient'));
      const page = await contexte.newPage();
      page.setDefaultTimeout(20000);
      const journal = suivreErreurs(page, serveur.url);
      journaux.push(journal);
      return { contexte, page, journal };
    },
    async fermerContextes() {
      while (contextes.length) { const c = contextes.pop(); await c.close().catch(() => {}); }
    },
    /* Capture d'écran dans le dossier de sortie (jamais bloquante).
       ctx.capture(page, 'nom') → page visible ; { selecteur: '#id' } → un seul élément. */
    async capture(page, nom, o) {
      const f = path.join(options.sortie, nomSuite + '-' + nom + '.png');
      try {
        if (o && o.selecteur) await page.locator(o.selecteur).first().screenshot({ path: f });
        else await page.screenshot(Object.assign({ path: f }, o || {}));
        return f;
      } catch (e) { return null; }
    },
    fichierSortie(nom) { return path.join(options.sortie, nomSuite + '-' + nom); },
    /* Chapitres à parcourir selon --chapitres / --rapide.
       `tous` : [{id, prefix, matiere, …}] lus dans CHAPTERS. Avec --chapitres,
       un prefix est accepté comme alias de l'id (les messages d'échec citent des
       panneaux « <prefix>-<onglet> », ex. og-cours pour optgeo) ; un nom qui ne
       correspond à aucun chapitre ARRÊTE le lancement (sinon la suite passerait
       « OK » sans avoir rien vérifié). */
    selectionner(tous) {
      if (options.chapitres) {
        const trouver = nom => tous.find(c => c.id === nom) || tous.find(c => c.prefix === nom);
        const inconnus = options.chapitres.filter(nom => !trouver(nom));
        if (inconnus.length) {
          throw erreurHarnais('--chapitres : chapitre(s) inconnu(s) : ' + inconnus.join(', ')
            + '\n  ids valides (CHAPTERS) : ' + tous.map(c => c.id).join(', '));
        }
        const voulus = new Set(options.chapitres.map(trouver));
        return tous.filter(c => voulus.has(c));
      }
      if (!options.rapide) return tous;
      const sel = tous.filter(c => ECHANTILLON_RAPIDE.includes(c.id));
      for (const mat of new Set(tous.map(c => c.matiere))) {
        if (!sel.some(c => c.matiere === mat)) { const c = tous.find(x => x.matiere === mat); if (c) sel.push(c); }
      }
      return sel;
    },
    /* Progression compacte sur une ligne : un point par élément */
    progression(i, n, echec) {
      if (interrompu) return;
      if (i === 0) process.stdout.write('         ');
      process.stdout.write(echec ? rouge('x') : gris('.'));
      if ((i + 1) % 60 === 0 && i + 1 < n) process.stdout.write('\n         ');
      if (i + 1 === n) process.stdout.write(' ' + gris(n + '/' + n) + '\n');
    },
    log(msg) { if (!interrompu) console.log('         ' + gris(msg)); },
    pause,
  };
  return ctx;
}

/* ---------- Programme principal ---------- */
async function main() {
  let options;
  try { options = lireOptions(process.argv.slice(2)); }
  catch (e) { console.error(rouge('Erreur : ') + e.message); process.exit(2); }
  if (options.aide) { afficherAide(); return; }

  if (!fs.existsSync(path.join(options.racine, 'index.html'))) {
    console.error(rouge('Erreur : ') + 'index.html introuvable dans ' + options.racine + ' (option --racine ?)');
    process.exit(2);
  }
  // --chapitres : noms vérifiés ici, pour TOUTES les suites (même celles qui
  // n'utilisent pas l'option) — ids et prefix lus dans le tableau CHAPTERS du site.
  // (ctx.selectionner revérifie d'après le CHAPTERS réel de la page.)
  if (options.chapitres) {
    const html = fs.readFileSync(path.join(options.racine, 'index.html'), 'utf8');
    const d = html.indexOf('const CHAPTERS = [');
    const chap = d < 0 ? [] : [...html.slice(d, html.indexOf('\n];', d)).matchAll(/\{\s*id:'([^']+)',\s*prefix:'([^']+)'/g)];
    const inconnus = chap.length ? options.chapitres.filter(nom => !chap.some(m => m[1] === nom || m[2] === nom)) : [];
    if (inconnus.length) {
      console.error(rouge('Erreur : ') + '--chapitres : chapitre(s) inconnu(s) : ' + inconnus.join(', ')
        + '\n  ids valides (CHAPTERS) : ' + chap.map(m => m[1]).join(', '));
      process.exit(2);
    }
  }
  const pw = chargerPlaywright();
  fs.mkdirSync(options.sortie, { recursive: true });
  // On efface les fichiers d'un run précédent (uniquement ceux que le harnais produit)
  const produits = new RegExp('^((' + SUITES.join('|') + ')-[\\w.-]+\\.(png|json)|rapport\\.json)$', 'i');
  for (const f of fs.readdirSync(options.sortie)) {
    if (produits.test(f)) { try { fs.unlinkSync(path.join(options.sortie, f)); } catch (e) { /* ignoré */ } }
  }

  const serveur = await demarrerServeur(options.racine);
  let navigateur;
  try {
    // handleSIGINT: false → Ctrl+C est géré ci-dessous (et non par Playwright)
    navigateur = await pw.chromium.launch({ headless: !options.visible, handleSIGINT: false });
  } catch (e) {
    await serveur.fermer();
    console.error(rouge(gras('\nImpossible de lancer Chromium.')) + '\n' + String(e.message).split('\n').slice(0, 4).join('\n') + `

Le navigateur de test n'est probablement pas installé pour cette version de
Playwright. Dans le dossier du dépôt, tapez :

    npx playwright install chromium

(Dans le conteneur Claude Code : NE PAS lancer cette commande ; vérifier que
PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers et ne pas faire « npm install ».)
`);
    process.exit(2);
  }

  // Ctrl+C : le gestionnaire de Playwright fermait le navigateur pendant que la suite
  // en cours continuait → cascade de faux « ÉCHEC », résumé « RÉSULTAT : ÉCHEC » et
  // rapport.json réécrit. Ici : on se tait, on ferme navigateur et serveur, code 130.
  process.once('SIGINT', async () => {
    interrompu = true;
    console.error('\n' + jaune('Interrompu (Ctrl+C) : aucun rapport écrit.'));
    await navigateur.close().catch(() => {});
    await Promise.resolve().then(() => serveur.fermer()).catch(() => {});
    process.exit(130);
  });

  const t0 = Date.now();
  // Chemin affiché : relatif s'il est sous le dossier courant, absolu sinon
  const rel = p => { const r = path.relative(process.cwd(), p); return !r ? '.' : (r.startsWith('..') || path.isAbsolute(r) ? p : r); };
  console.log(gras('\nTests navigateur — Révisions PTSI'));
  console.log(gris('  site     : ' + rel(options.racine) + '  (servi sur ' + serveur.url + ')'));
  console.log(gris('  Chromium : ' + navigateur.version() + (options.rapide ? '   · mode RAPIDE' : '')
    + (options.chapitres ? '   · chapitres : ' + options.chapitres.join(',') : '')));

  const resultats = [];
  let arretHarnais = null;   // erreur d'utilisation (code 2)
  for (const nom of options.suites) {
    const suite = require('./suites/' + nom + '.js');
    const res = new ResultatSuite(nom);
    console.log('\n' + gras('== Suite « ' + nom + ' »') + gris(' — ' + suite.description));
    const ctx = creerContexte({ pw, navigateur, serveur, options, nomSuite: nom });
    const execution = Promise.resolve().then(() => suite.executer(ctx, res));
    execution.catch(() => {});   // après un dépassement de délai, la suite abandonnée peut encore échouer : ignoré
    try {
      await avecDelai(execution, suite.delaiMax ? suite.delaiMax(options) : 10 * 60000, 'suite ' + nom);
    } catch (e) {
      if (e && e.harnais) { arretHarnais = e; break; }   // le finally ferme les contextes
      // Message d'arrêt + erreurs JavaScript déjà relevées (souvent la vraie cause)
      const erreursJS = ctx.journaux.flatMap(j => j.erreurs).slice(0, 6)
        .map(er => 'erreur relevée [' + er.lieu + '] ' + er.type + ' : ' + er.texte + (er.source ? ' (' + er.source + ')' : ''));
      res.echec('exécution de la suite (arrêt prématuré)', [String(e && e.stack || e).split('\n').slice(0, 3).join(' | ')].concat(erreursJS));
    } finally {
      await ctx.fermerContextes();
    }
    if (interrompu) break;   // Ctrl+C : le gestionnaire SIGINT termine le programme
    if (!res.controles.length) res.echec('exécution de la suite', 'aucun contrôle effectué');
    res.duree = Date.now() - res.debut;
    resultats.push(res);
    console.log('   ' + gris('→ ' + (res.enEchec.length ? res.enEchec.length + ' échec(s)' : 'tout est OK') + ' en ' + duree(res.duree)));
  }

  if (interrompu) return;   // ni rapport ni résumé (sortie par le gestionnaire SIGINT)
  await navigateur.close().catch(() => {});
  await serveur.fermer();
  if (arretHarnais) {
    console.error('\n' + rouge('Erreur : ') + arretHarnais.message + '\n' + gris('Lancement arrêté (voir --aide).'));
    process.exit(2);
  }

  /* Rapport JSON détaillé */
  const rapport = {
    date: new Date().toISOString(), racine: options.racine, rapide: options.rapide, chapitres: options.chapitres,
    chromium: navigateur.version(), dureeMs: Date.now() - t0,
    suites: resultats.map(r => ({ nom: r.nom, ok: !r.enEchec.length, dureeMs: r.duree, controles: r.controles,
      avertissements: r.avertissements, infos: r.infos })),
  };
  const fichierRapport = path.join(options.sortie, 'rapport.json');
  fs.writeFileSync(fichierRapport, JSON.stringify(rapport, null, 1));

  /* Résumé lisible */
  const trait = '='.repeat(66);
  console.log('\n' + trait + '\n' + gras(' RÉSUMÉ') + gris('  (durée totale ' + duree(Date.now() - t0) + ')') + '\n' + trait);
  for (const r of resultats) {
    const echecs = r.enEchec;
    const etiquette = echecs.length ? rouge('[ÉCHEC]') : vert('[OK]   ');
    const compte = echecs.length ? echecs.length + ' échec(s) sur ' + r.controles.length + ' contrôles' : r.controles.length + ' contrôles';
    console.log(' ' + etiquette + ' ' + r.nom.padEnd(13) + compte.padEnd(34) + gris(duree(r.duree)));
    for (const c of echecs) {
      console.log('          ' + rouge('x ' + c.nom));
      c.messages.slice(0, 4).forEach(m => console.log('              ' + m));
      if (c.messages.length > 4) console.log('              ' + gris('… (' + (c.messages.length - 4) + ' de plus dans rapport.json)'));
    }
    r.avertissements.forEach(a => console.log('          ' + jaune('! ' + a)));
  }
  const nbEchec = resultats.filter(r => r.enEchec.length).length;
  console.log('-'.repeat(66));
  console.log(' Rapport détaillé : ' + rel(fichierRapport));
  console.log(' Captures d\'écran : ' + rel(options.sortie) + path.sep + '*.png');
  console.log(' RÉSULTAT : ' + (nbEchec ? rouge(gras('ÉCHEC')) + ' (' + nbEchec + ' suite(s) sur ' + resultats.length + ')' : vert(gras('TOUT EST OK'))));
  process.exitCode = nbEchec ? 1 : 0;
}

main().catch(e => {
  console.error(rouge('\nErreur inattendue du harnais de test :'), e && e.stack || e);
  process.exit(2);
});
