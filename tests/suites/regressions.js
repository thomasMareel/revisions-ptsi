'use strict';
/* ============================================================
   Suite « regressions » — un test par correctif (contrat B1 à B4)
   ============================================================
   B1  Synchronisation quiz → flashcards : les notes données dans le quiz
       (« Réviser ») ne doivent pas être écrasées par l'onglet Flashcards ;
       B1b : idem quand localStorage refuse les écritures (quota plein), puis
       les accepte de nouveau ; B1c : quiz dans un AUTRE onglet (même stockage).
   B2  État des flashcards indexé par position. B2a (un état distinct pour
       CHAQUE carte, contrôlé carte par carte) : insertion / retrait /
       réordonnancement d'un deck, question reformulée (sur place, suivie d'une
       insertion, après retrait de la précédente, à côté d'une carte déplacée,
       entre une carte retirée et une carte ajoutée), ambiguïté (deux entrées
       candidates de même réponse → vierge), question ET réponse retouchées sur
       place ou deck entier réécrit (état conservé), carte remplacée sur place
       (hérite de l'état de l'ancienne) ; état « hérité » de longueur différente
       (B2b), quizRate sans exception, y compris sur un état hérité non migré
       (B2c), tableau 'flash:<prefix>' toujours aligné ; import d'une sauvegarde
       sans table d'identifiants (B2d) ; réalignement des cartes signalées, aussi
       sur une question en double, signalement introuvable rendu orphelin si son
       index est pris (B2e) ; question en double : réponses
       différentes ou doublon exact (B2f).
   B3  Simulateur SLCI, 2e ordre apériodique (ξ > 1) : s(0) = 0, t₅% exact et
       palier atteint dans la fenêtre tracée (pôle lent) ; t₅% pseudo-périodique
       exact même au-delà de la fenêtre tracée (80 s).
   B4  getCanvasColors() : couleurs muted / grid du thème sombre.
   Tests en boîte noire autant que possible (vrais boutons, vrai Store). Pour
   B2, le serveur de test sert une VARIANTE d'index.html où le deck rlcCards
   est modifié (le fichier sur le disque n'est jamais touché). */
const fs = require('fs');
const path = require('path');
const { pause, attendreApp, fermerOverlays, naviguer, extraireDeck, remplacerDeck, suivreErreurs } = require('../lib/outils');

const DECK = 'rlcCards';   // deck utilisé pour B1/B2 (chapitre rlc, prefix rlc)
const JOUR = 86400000;

/* État normalisé d'une carte (null / absent → carte vierge) */
const norm = s => (s && typeof s === 'object')
  ? { h: s.h | 0, o: s.o | 0, e: s.e | 0, last: s.last == null ? null : s.last, box: s.box == null ? null : s.box, due: s.due == null ? null : s.due }
  : { h: 0, o: 0, e: 0, last: null, box: null, due: null };
const vierge = s => { const n = norm(s); return n.last === null && !n.h && !n.o && !n.e; };
const memeEtat = (a, b) => JSON.stringify(norm(a)) === JSON.stringify(norm(b));
const nbEvals = arr => (Array.isArray(arr) ? arr : []).reduce((t, s) => { const n = norm(s); return t + n.h + n.o + n.e; }, 0);
const court = q => '« ' + String(q).slice(0, 45) + (String(q).length > 45 ? '…' : '') + ' »';
const aff = s => { const n = norm(s); return '{h:' + n.h + ',o:' + n.o + ',e:' + n.e + ',last:' + n.last + ',box:' + n.box + '}'; };

/* Variante B2 du HTML : deck rlcCards modifié selon
   ?op=<op>[,<op>…]&i=<index>. Opérations :
   insertion    carte nouvelle insérée à l'index (texte unique à chaque insertion) ;
   retrait      carte retirée ;
   inversion    deck entier inversé ;
   edition      question reformulée (réponse inchangée), comme une faute corrigée ;
   retouche     question ET réponse retouchées sur place (rechercher/remplacer…) ;
   reecriture   question ET réponse de TOUTES les cartes réécrites ;
   remplacement carte remplacée par une carte nouvelle (question ET réponse) ;
   memereponse  la carte suivante reçoit la même réponse que la carte index ;
   doublon      copie de la carte ajoutée en fin de deck : même question, autre réponse ;
   doublonexact copie EXACTE (même question, même réponse) ajoutée en fin de deck ;
   echange      la carte index et la dernière carte du deck échangent leur place ;
   deplacement  la carte index est retirée puis réinsérée à l'index d, compté après
                le retrait (« deplacement@k>d » : carte k déplacée à l'index d).
   Les opérations s'appliquent dans l'ordre, à l'index i (ex. op=retrait,edition :
   carte i retirée, puis la suivante reformulée), sauf « op@k » qui vise l'index k
   (ex. op=edition,insertion@8&i=7). */
function varianteB2(html, params) {
  const nom = params.get('deck') || DECK;
  const { cartes } = extraireDeck(html, nom);
  const i0 = parseInt(params.get('i') || '0', 10);
  const c = cartes.slice();
  let nIns = 0;
  for (const jeton of String(params.get('op')).split(',')) {
    const [op, arg] = jeton.split('@');
    const [k, dest] = (arg === undefined ? '' : arg).split('>');
    const i = arg === undefined ? i0 : parseInt(k, 10);
    switch (op) {
      case 'insertion': c.splice(i, 0, { q: 'Question ajoutée par le test B2 (n° ' + (++nIns) + ', position ' + i + ') ?', a: 'Réponse de test B2 n° ' + nIns + '.' }); break;
      case 'retrait': c.splice(i, 1); break;
      case 'inversion': c.reverse(); break;
      case 'edition': c[i] = Object.assign({}, c[i], { q: c[i].q + ' (reformulée par le test B2)' }); break;
      case 'retouche': c[i] = Object.assign({}, c[i], { q: c[i].q + ' (retouchée par le test B2)', a: c[i].a + ' (retouchée)' }); break;
      case 'reecriture': c.forEach((x, j) => { c[j] = Object.assign({}, x, { q: 'Question réécrite par le test B2 n° ' + j + ' ?', a: 'Réponse réécrite n° ' + j + '.' }); }); break;
      case 'remplacement': c[i] = { q: 'Question de remplacement du test B2 (position ' + i + ') ?', a: 'Réponse de remplacement du test B2.' }; break;
      case 'memereponse': c[i + 1] = Object.assign({}, c[i + 1], { a: c[i].a }); break;
      case 'doublon': c.push(Object.assign({}, c[i], { a: c[i].a + ' (copie du test B2)' })); break;
      case 'doublonexact': c.push(Object.assign({}, c[i])); break;
      case 'echange': { const d = c.length - 1, x = c[i]; c[i] = c[d]; c[d] = x; break; }
      case 'deplacement': {
        const d = parseInt(dest, 10);
        if (isNaN(d)) throw new Error('deplacement : destination manquante (deplacement@k>d)');
        c.splice(d, 0, c.splice(i, 1)[0]);
        break;
      }
      default: throw new Error('op inconnue : ' + op);
    }
  }
  return remplacerDeck(html, nom, c);
}

/* Solution exacte du 2e ordre apériodique (ξ > 1) : t tel que s(t) = 0,95·K */
function t5Exact(K, w0, z) {
  const rac = Math.sqrt(z * z - 1), r1 = -w0 * (z - rac), r2 = -w0 * (z + rac);
  const s = t => K * (1 + (r2 * Math.exp(r1 * t) - r1 * Math.exp(r2 * t)) / (r1 - r2));
  let a = 0, b = 1;
  while (s(b) < 0.95 * K) b *= 2;
  for (let k = 0; k < 200; k++) { const m = (a + b) / 2; if (s(m) < 0.95 * K) a = m; else b = m; }
  return (a + b) / 2;
}

/* 2e ordre pseudo-périodique (ξ < 1) : dernier instant où |s(t) − K| > 5 %·K.
   Au-delà de ln(20/√(1−ξ²))/(ξω0), l'enveloppe garantit un écart < 5 %. */
function t5PseudoExact(K, w0, z) {
  const wp = w0 * Math.sqrt(1 - z * z), a = w0 * z;
  const s = t => K * (1 - Math.exp(-a * t) * (Math.cos(wp * t) + (a / wp) * Math.sin(wp * t)));
  const T = Math.log(20 / Math.sqrt(1 - z * z)) / a * 1.01, M = 400000;
  for (let i = M; i >= 0; i--) { const t = (i / M) * T; if (Math.abs(s(t) - K) > 0.05 * K) return t; }
  return 0;
}

module.exports = {
  nom: 'regressions',
  description: 'correctifs B1 (quiz→flashcards), B2 (état des decks), B3 (SLCI ξ>1), B4 (couleurs canvas)',
  delaiMax: () => 8 * 60000,

  async executer(ctx, res) {
    ctx.serveur.variantes.set('b2', varianteB2);

    /* ---- petits outils ---- */
    const lireEtat = page => page.evaluate(() => ({
      etat: Store.getJSON('flash:rlc', null),
      ids: Store.getJSON('flashids:rlc', null),
      questions: FLASH_REGISTRY.rlc.map(c => c.q),
    }));
    const noter = async (page, niveaux) => {
      for (const n of niveaux) {
        await page.click('#rlc-flash .flash-controls .' + ['hard', 'ok', 'easy'][n]);
        await pause(120);
      }
      await pause(200);
    };
    // Pré-remplit le localStorage (même origine) AVANT de charger le site
    const preremplir = async (page, donnees) => {
      await page.goto(ctx.base + '__tests__/vide.html');
      await page.evaluate(d => { for (const [k, v] of Object.entries(d)) { if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } }, donnees);
    };
    const charger = async (page, hash, params) => {
      await page.goto(ctx.url(hash, params), { waitUntil: 'load', timeout: 60000 });
      await attendreApp(page);
      await fermerOverlays(page);
    };
    // Nombre de cartes du deck d'origine (lu dans le HTML servi, sans navigateur)
    const html = fs.readFileSync(path.join(ctx.options.racine, 'index.html'), 'utf8');
    const n = extraireDeck(html, DECK).cartes.length;
    const exceptions = journal => journal.erreurs.filter(e => e.type === 'exception').map(e => e.texte);
    // Enregistre (comme la version corrigée : état + identifiants, via flashSaveState) un
    // état DISTINCT et non vierge pour CHAQUE carte du deck rlc servi (h = index + 1), puis
    // le relit. Rend les contrôles B2 déterministes : une carte qui reprend l'état d'une
    // autre, ou aucun, se voit toujours (au lieu de dépendre des cartes tirées au hasard).
    const etatsDistincts = async page => {
      await page.evaluate(J => {
        const c = FLASH_REGISTRY.rlc, t = Date.now();
        flashSaveState('rlc', c, c.map((_, k) => ({ h: k + 1, o: k % 3, e: 1, last: k % 3, box: 1 + k % 5, due: t + (k + 1) * J })));
      }, JOUR);
      return lireEtat(page);
    };
    // Réécrit dans le Store un état relu plus tôt (s = résultat de lireEtat / etatsDistincts)
    const restaurer = (page, s) => page.evaluate(s => { Store.setJSON('flash:rlc', s.etat); Store.setJSON('flashids:rlc', s.ids); }, s);
    // Compare CHAQUE carte du deck relu (s2) à l'état attendu : origine(j, q) = index, dans
    // s1, de la carte dont elle doit avoir l'état, ou −1 si elle doit être vierge
    const comparer = (s1, s2, origine, quoi, pb) => {
      if (!Array.isArray(s2.etat) || s2.etat.length !== s2.questions.length) {
        pb.push(quoi + ' : (d) flash:rlc non aligné sur le deck (' + (Array.isArray(s2.etat) ? s2.etat.length : typeof s2.etat) + ' états pour ' + s2.questions.length + ' cartes)');
        return;
      }
      if (!Array.isArray(s2.ids) || s2.ids.length !== s2.questions.length) pb.push(quoi + ' : flashids:rlc absent ou non aligné sur le deck');
      const faux = [];
      s2.questions.forEach((q, j) => {
        const k = origine(j, q), e = s2.etat[j];
        if (k < 0) { if (!vierge(e)) faux.push('carte ' + court(q) + ' (index ' + j + ') : ' + aff(e) + ' au lieu d\'un état vierge'); }
        else if (!memeEtat(e, s1.etat[k])) faux.push('carte ' + court(q) + ' (index ' + k + ' → ' + j + ') : ' + aff(e) + ' au lieu de ' + aff(s1.etat[k]));
      });
      if (faux.length) pb.push(quoi + ' : ' + faux.length + ' carte(s) sans le bon état : ' + faux.slice(0, 3).join(' ; ') + (faux.length > 3 ? ' ; …' : ''));
    };

    /* =====================================================================
       B1 — quiz « Réviser » puis onglet Flashcards du même chapitre
       ===================================================================== */
    await (async () => {
      const nom = 'B1 — notes du quiz conservées par l\'onglet Flashcards';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        // 5 cartes de rlc « à revoir », dues depuis hier (le reste jamais vu)
        const N = 5;
        const depart = Array.from({ length: n }, (_, i) => i < N
          ? { h: 1, o: 0, e: 0, last: 0, box: 0, due: Date.now() - JOUR } : { h: 0, o: 0, e: 0, last: null });
        await preremplir(page, { 'flash:rlc': JSON.stringify(depart), 'flashids:rlc': null });
        await charger(page, '#rlc/cours');
        // Vrai bouton « Réviser » → « Révisions du jour »
        await page.click('#study-btn');
        await pause(200);
        await page.click('#revise-btn');
        await pause(500);
        const prog = await page.evaluate(() => document.getElementById('quiz-progress-text').textContent);
        if (!new RegExp('^\\s*1\\s*/\\s*' + N + '\\b').test(prog)) throw new Error('préparation : la session « Réviser » devrait compter ' + N + ' cartes (progression « ' + prog + ' »)');
        for (let k = 0; k < N; k++) {
          await page.click('#quiz-reveal-btn');
          await pause(150);
          await page.click('#quiz-actions-rate .rate-acq');
          await pause(200);
        }
        const apresQuiz = (await lireEtat(page)).etat;
        const quizOk = apresQuiz && apresQuiz.slice(0, N).every(s => s && s.last === 2 && s.e === 1 && s.box === 1);
        if (!quizOk) throw new Error('préparation : le quiz n\'a pas enregistré les ' + N + ' notes « acquis » (' + (apresQuiz || []).slice(0, N).map(aff).join(' ') + ')');
        await page.keyboard.press('Escape');
        await pause(200);
        // Onglet Flashcards du même chapitre
        await naviguer(page, 'rlc', 'flash');
        await pause(300);
        const statsAvant = await page.evaluate(() => document.getElementById('rlc-stats').textContent);
        if (!new RegExp('Acquis\\s*:\\s*' + N + '\\s*/').test(statsAvant))
          pb.push('statistiques affichées à l\'ouverture de l\'onglet : « ' + statsAvant + ' » (attendu « Acquis: ' + N + '/' + n + ' … » : les notes du quiz sont ignorées)');
        await noter(page, [2]);   // une notation dans l'onglet Flashcards
        const fin = (await lireEtat(page)).etat;
        const attendu = nbEvals(depart) + N + 1;
        if (nbEvals(fin) !== attendu)
          pb.push(nbEvals(fin) + ' évaluation(s) dans le Store au lieu de ' + attendu + ' (' + nbEvals(depart) + ' initiales + ' + N + ' du quiz + 1 flashcard) : les notes du quiz ont été écrasées');
        const intactes = apresQuiz.slice(0, N).filter((s, i) => fin && memeEtat(fin[i], s)).length;
        const toutes = (fin || []).slice(0, N).every(s => s && s.last === 2 && s.e >= 1 && s.box >= 1 && s.due > Date.now());
        if (intactes < N - 1 || !toutes)
          pb.push('état (box/due) des cartes notées dans le quiz non conservé : ' + (fin || []).slice(0, N).map(aff).join(' ') + ' (attendu last:2, box ≥ 1, révision future)');
        const statsApres = await page.evaluate(() => document.getElementById('rlc-stats').textContent);
        const acq = /Acquis\s*:\s*(\d+)\s*\//.exec(statsApres);
        if (!acq || +acq[1] < N) pb.push('statistiques après la notation : « ' + statsApres + ' » (attendu au moins ' + N + ' acquises)');
        exceptions(journal).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B1b — localStorage plein en cours de session : Store.get doit relire
             l'écriture de repli (mémoire), sinon rate() → sync() repartirait
             de l'ancienne valeur et chaque notation effacerait la précédente ;
             puis retour à la normale (écritures de nouveau acceptées) : Store.set
             doit oublier la valeur de repli, devenue périmée
       ===================================================================== */
    await (async () => {
      const nom = 'B1b — localStorage plein en cours de session, puis de nouveau disponible : les notes s\'accumulent';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        await charger(page, '#rlc/flash');
        // À partir d'ici, toute écriture 'flash…' dans localStorage échoue (quota plein simulé)
        await page.evaluate(() => {
          const origine = window.__setItemOrigine = Storage.prototype.setItem;
          Storage.prototype.setItem = function (k, v) {
            if (String(k).indexOf('flash') === 0) throw new DOMException('quota dépassé (simulé par le test)', 'QuotaExceededError');
            return origine.call(this, k, v);
          };
        });
        const suite = [];
        for (let k = 0; k < 3; k++) {
          await noter(page, [2]);
          const st = await page.evaluate(() => document.getElementById('rlc-stats').textContent);
          const m = /Acquis\s*:\s*(\d+)\s*\//.exec(st);
          suite.push(m ? +m[1] : NaN);
        }
        if (suite.join(',') !== '1,2,3')
          pb.push('« Acquis » après 3 notations « acquis » : ' + suite.join(', ') + ' (attendu 1, 2, 3 : chaque notation efface la précédente)');
        const etat = (await lireEtat(page)).etat;
        if (nbEvals(etat) !== 3)
          pb.push('Store.getJSON(\'flash:rlc\') : ' + nbEvals(etat) + ' évaluation(s) au lieu de 3 (la lecture ignore l\'écriture de repli en mémoire)');
        // Retour à la normale : localStorage accepte de nouveau les écritures. La 1re
        // notation y écrit tout l'état (repli compris) ; si Store.set gardait la valeur
        // de repli, get() la relirait (périmée) et chaque notation effacerait la précédente
        await page.evaluate(() => { Storage.prototype.setItem = window.__setItemOrigine; });
        const suite2 = [];
        for (let k = 0; k < 2; k++) {
          await noter(page, [2]);
          const st = await page.evaluate(() => document.getElementById('rlc-stats').textContent);
          const m = /Acquis\s*:\s*(\d+)\s*\//.exec(st);
          suite2.push(m ? +m[1] : NaN);
        }
        if (suite2.join(',') !== '4,5')
          pb.push('quota de nouveau disponible : « Acquis » après 2 notations de plus : ' + suite2.join(', ') + ' (attendu 4, 5 : la valeur de repli, périmée, est relue)');
        await charger(page, '#rlc/flash');   // rechargement : seul localStorage compte
        const relu = (await lireEtat(page)).etat;
        if (nbEvals(relu) !== 5)
          pb.push('après rechargement : ' + nbEvals(relu) + ' évaluation(s) relues dans localStorage au lieu de 5 (3 sous quota plein + 2 ensuite)');
        exceptions(journal).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B1c — quiz dans un AUTRE onglet (même localStorage) : l'onglet des
             flashcards, ouvert avant, ne doit pas réécrire son état périmé par
             dessus (c'est le sync() de rate() qui l'en empêche : dans un même
             onglet, quizRate → reload() suffirait à masquer son absence)
       ===================================================================== */
    await (async () => {
      const nom = 'B1c — quiz dans un autre onglet : ses notes survivent à une notation dans l\'onglet Flashcards';
      const pb = [];
      try {
        const { contexte, page: A, journal } = await ctx.nouvellePage();
        await charger(A, '#rlc/flash');
        const B = await contexte.newPage();   // même contexte → même localStorage
        B.setDefaultTimeout(20000);
        const journalB = suivreErreurs(B, ctx.base);
        await charger(B, '#rlc/cours');
        const N = 5;
        await B.evaluate(N => {
          const c = CHAPTERS_BY_ID.rlc;
          window.quizOpen();
          window.quizStart(Array.from({ length: N }, (_, k) => ({ card: FLASH_REGISTRY.rlc[k], prefix: 'rlc', idx: k, lastEval: null,
            meta: { name: c.name, mat: c.matiere, chapId: 'chap-rlc', panelId: 'rlc-flash' } })));
        }, N);
        await pause(300);
        for (let k = 0; k < N; k++) {
          await B.click('#quiz-reveal-btn');
          await pause(150);
          await B.click('#quiz-actions-rate .rate-acq');
          await pause(200);
        }
        const apresQuiz = (await lireEtat(B)).etat;
        if (nbEvals(apresQuiz) !== N) throw new Error('préparation : le quiz de l\'onglet B a enregistré ' + nbEvals(apresQuiz) + ' évaluation(s) au lieu de ' + N);
        await A.bringToFront();
        await noter(A, [2]);   // une notation dans l'onglet A, chargé AVANT le quiz
        const fin = (await lireEtat(A)).etat;
        if (nbEvals(fin) !== N + 1)
          pb.push(nbEvals(fin) + ' évaluation(s) dans le Store au lieu de ' + (N + 1) + ' (' + N + ' du quiz de l\'onglet B + 1 flashcard dans l\'onglet A) : l\'onglet A a réécrit son état périmé');
        exceptions(journal).concat(exceptions(journalB)).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B2a — état enregistré par la version corrigée (un état distinct pour
             CHAQUE carte), puis deck modifié : chaque carte doit avoir l'état
             attendu (le sien, ou vierge pour une carte nouvelle)
       ===================================================================== */
    // reprend : {index dans le deck modifié: index d'origine} pour les cartes dont le texte
    // a changé ('identite' : toutes) ; vierges : index qui doivent repartir vierges ; les
    // autres cartes sont retrouvées par leur question (carte nouvelle → vierge).
    const scenarios = [
      { op: 'insertion', i: 0, titre: 'carte insérée au début', noterEnsuite: true },
      { op: 'insertion', i: 13, titre: 'carte insérée au milieu' },
      { op: 'retrait', i: 5, titre: 'carte retirée' },
      { op: 'inversion', i: 0, titre: 'deck réordonné (inversé)' },
      // Question reformulée sur place (réponse inchangée), puis retour au libellé d'origine
      { op: 'edition', i: 7, titre: 'question reformulée sur place', reprend: { 7: 7 }, retour: true },
      // Passe 3 b, candidat compté depuis la voisine précédente (lo + j − p) : une carte
      // insérée juste après la carte reformulée (plus autant de cartes que d'entrées)
      { op: 'edition,insertion@8', i: 7, titre: 'question reformulée + carte insérée juste après', reprend: { 7: 7 } },
      // Passe 3 b, candidat compté depuis la voisine suivante (hi − (n − j)) : la carte
      // reformulée garde SON état, pas celui de la carte retirée qui occupait sa place
      { op: 'retrait,edition', i: 5, titre: 'carte retirée + la suivante reformulée', reprend: { 5: 6 } },
      // Passe 3 b, voisines dans le désordre (lo > hi) : une carte déplacée juste à côté de la
      // carte reformulée, qui garde son rang compté depuis son AUTRE voisine (candidat compté
      // depuis n, cherché en deçà de hi ; puis candidat compté depuis p, au-delà de lo)
      { op: 'edition@5,deplacement@10>5', i: 0, titre: 'carte déplacée juste avant une question reformulée', reprend: { 6: 5 } },
      { op: 'edition@4,deplacement@1>4', i: 0, titre: 'carte déplacée juste après une question reformulée', reprend: { 3: 4 } },
      // Passe 3 a, réponse univoque : entre les voisines, une carte retirée et une ajoutée
      // (autant de cartes que d'entrées) ; la carte reformulée garde SON état (pas celui de
      // la carte retirée) et la carte nouvelle part vierge (au lieu de prendre le sien)
      { op: 'retrait,edition,insertion@8', i: 7, titre: 'carte retirée juste avant une question reformulée + carte insérée juste après', reprend: { 7: 8 } },
      { op: 'retrait@8,insertion@7,edition@8', i: 7, titre: 'carte insérée juste avant une question reformulée + carte suivante retirée', reprend: { 8: 7 } },
      // Passe 3 b, ambiguïté : les deux entrées candidates ont la même réponse que la carte
      // (cas réel : deck dl, deux cartes de réponse « x. ») → rien n'est repris
      { base: 'memereponse', op: 'retrait,edition', i: 5, titre: 'carte retirée + la suivante (même réponse) reformulée : ambigu, vierge', vierges: [5] },
      // Passe 3 a (règle positionnelle) : question ET réponse retouchées sur place
      { op: 'retouche@2,retouche@3,retouche@11,retouche@' + (n - 1), i: 0, titre: 'question ET réponse retouchées sur place (4 cartes, dont la dernière)',
        reprend: { 2: 2, 3: 3, 11: 11, [n - 1]: n - 1 } },
      { op: 'reecriture', i: 0, titre: 'deck entier réécrit (même longueur)', reprend: 'identite' },
      // Contrepartie de la règle positionnelle (comme l'ancien appariement par position) :
      // une carte remplacée sur place par une autre lui lègue son état
      { op: 'remplacement', i: 9, titre: 'carte remplacée sur place par une nouvelle : hérite de l\'état de l\'ancienne', reprend: { 9: 9 } },
    ];
    for (const sc of scenarios) {
      const nom = 'B2a — ' + sc.titre + ' : chaque carte a l\'état attendu';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        const avant = sc.base ? { variante: 'b2', op: sc.base, i: String(sc.i) } : undefined;
        await charger(page, '#rlc/flash', avant);
        const s1 = await etatsDistincts(page);
        if (!Array.isArray(s1.ids) || s1.ids.length !== s1.questions.length || nbEvals(s1.etat) === 0)
          throw new Error('préparation : état de départ non enregistré (flash:rlc / flashids:rlc)');
        // 2e chargement, MÊME contexte (même localStorage), deck modifié
        await charger(page, '#rlc/flash', { variante: 'b2', op: (sc.base ? sc.base + ',' : '') + sc.op, i: String(sc.i) });
        await pause(300);
        const s2 = await lireEtat(page);
        if (JSON.stringify(s2.questions) === JSON.stringify(s1.questions)) throw new Error('préparation : la variante du deck n\'a pas été servie');
        const origine = (j, q) => sc.reprend === 'identite' ? j
          : (sc.reprend && j in sc.reprend) ? sc.reprend[j]
          : (sc.vierges || []).includes(j) ? -1 : s1.questions.indexOf(q);
        comparer(s1, s2, origine, 'après modification du deck', pb);
        if (sc.noterEnsuite) {
          // Une notation dans le deck modifié ne doit rien effacer
          await noter(page, [2]);
          const s3 = await lireEtat(page);
          if (nbEvals(s3.etat) !== nbEvals(s1.etat) + 1)
            pb.push('après une notation dans le deck modifié : ' + nbEvals(s3.etat) + ' évaluation(s) au lieu de ' + (nbEvals(s1.etat) + 1) + ' (progression du chapitre effacée)');
        }
        if (sc.retour) {
          // 3e chargement : deck d'origine (libellé rétabli) → rien ne doit s'être perdu en route
          await charger(page, '#rlc/flash', avant);
          await pause(300);
          comparer(s1, await lireEtat(page), j => j, 'après retour au libellé d\'origine', pb);
        }
        exceptions(journal).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    }

    /* =====================================================================
       B2b — état « hérité » (sans flashids) PLUS LONG que le deck
       ===================================================================== */
    await (async () => {
      const nom = 'B2b — état hérité plus long que le deck : conservé par position, rien d\'effacé';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        const base = Date.now() + 2 * JOUR;
        const herite = Array.from({ length: n + 2 }, (_, i) => ({ h: i % 3, o: 1, e: i, last: i % 3, box: i % 5, due: base + i * 3600e3 }));
        await preremplir(page, { 'flash:rlc': JSON.stringify(herite), 'flashids:rlc': null });
        await charger(page, '#rlc/flash');
        await pause(300);
        const s = await lireEtat(page);
        if (!Array.isArray(s.etat) || s.etat.length !== n)
          pb.push('(d) après chargement, flash:rlc n\'est pas aligné sur le deck : ' + (Array.isArray(s.etat) ? s.etat.length : typeof s.etat) + ' états pour ' + n + ' cartes');
        const diff0 = herite.slice(0, n).filter((h, i) => !(s.etat && memeEtat(s.etat[i], h))).length;
        if (diff0) pb.push('après chargement, ' + diff0 + ' carte(s) sur ' + n + ' ont perdu leur état hérité (conservation par position attendue)');
        await noter(page, [2]);
        const s2 = await lireEtat(page);
        const change = herite.slice(0, n).map((h, i) => (s2.etat && memeEtat(s2.etat[i], h) ? -1 : i)).filter(i => i >= 0);
        const ok1 = change.length === 1 && s2.etat && nbEvals([s2.etat[change[0]]]) === nbEvals([herite[change[0]]]) + 1;
        if (!ok1) pb.push('après UNE notation : ' + change.length + ' carte(s) modifiée(s) au lieu de 1'
          + (change.length > 1 ? ' — progression héritée effacée (' + nbEvals(s2.etat) + ' évaluations au lieu de ' + (nbEvals(herite.slice(0, n)) + 1) + ')' : ''));
        exceptions(journal).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B2c — état « hérité » PLUS COURT que le deck + quizRate sur une carte
             au-delà de l'état stocké
       ===================================================================== */
    await (async () => {
      const nom = 'B2c — état hérité plus court : quizRate sans exception, état conservé';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        const base = Date.now() + 3 * JOUR;
        const herite = Array.from({ length: n - 3 }, (_, i) => ({ h: 1, o: i % 2, e: 2, last: 2, box: 2, due: base + i * 60000 }));
        await preremplir(page, { 'flash:rlc': JSON.stringify(herite), 'flashids:rlc': null });
        await charger(page, '#rlc/cours');
        // Quiz sur la DERNIÈRE carte du deck (au-delà de l'état stocké)
        await page.evaluate(k => {
          const c = CHAPTERS_BY_ID.rlc;
          window.quizOpen();
          window.quizStart([{ card: FLASH_REGISTRY.rlc[k], prefix: 'rlc', idx: k, lastEval: null,
            meta: { name: c.name, mat: c.matiere, chapId: 'chap-rlc', panelId: 'rlc-flash' } }]);
        }, n - 1);
        await pause(300);
        await page.click('#quiz-reveal-btn');
        await pause(150);
        await page.click('#quiz-actions-rate .rate-acq');
        await pause(400);
        const exc = exceptions(journal);
        if (exc.length) pb.push('quizRate lève une exception : ' + exc[0]);
        const s = await lireEtat(page);
        const der = Array.isArray(s.etat) ? s.etat[n - 1] : null;
        if (!der || der.last !== 2) pb.push('la note du quiz sur la carte ' + (n - 1) + ' n\'est pas enregistrée (' + aff(der) + ')');
        const diff = herite.filter((h, i) => !(s.etat && memeEtat(s.etat[i], h))).length;
        if (diff) pb.push(diff + ' carte(s) sur ' + herite.length + ' ont perdu leur état hérité');
        if (!Array.isArray(s.etat) || s.etat.length !== n) pb.push('(d) flash:rlc non aligné : ' + (Array.isArray(s.etat) ? s.etat.length : typeof s.etat) + ' états pour ' + n + ' cartes');
        await page.keyboard.press('Escape');
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B2c (suite) — état hérité court écrit APRÈS le chargement (makeFlash ne
             l'a donc pas migré) : quizRate doit lui-même le relire réaligné
             (flashLoadState) et ne rien noter sur une carte absente
       ===================================================================== */
    await (async () => {
      const nom = 'B2c — état hérité court écrit après le chargement : quizRate le réaligne, sans exception';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        await charger(page, '#rlc/cours');
        const base = Date.now() + 4 * JOUR;
        const herite = Array.from({ length: n - 3 }, (_, i) => ({ h: 2, o: i % 3, e: 1, last: 1, box: 3, due: base + i * 60000 }));
        await page.evaluate(h => { localStorage.setItem('flash:rlc', JSON.stringify(h)); localStorage.removeItem('flashids:rlc'); }, herite);
        await page.evaluate(k => {
          const c = CHAPTERS_BY_ID.rlc;
          window.quizOpen();
          window.quizStart([{ card: FLASH_REGISTRY.rlc[k], prefix: 'rlc', idx: k, lastEval: null,
            meta: { name: c.name, mat: c.matiere, chapId: 'chap-rlc', panelId: 'rlc-flash' } }]);
        }, n - 1);
        await pause(300);
        await page.click('#quiz-reveal-btn');
        await pause(150);
        await page.click('#quiz-actions-rate .rate-acq');
        await pause(400);
        const exc = exceptions(journal);
        if (exc.length) pb.push('quizRate lève une exception : ' + exc[0]);
        const s = await lireEtat(page);
        const der = Array.isArray(s.etat) ? s.etat[n - 1] : null;
        if (!der || der.last !== 2) pb.push('la note du quiz sur la carte ' + (n - 1) + ' (au-delà de l\'état stocké) n\'est pas enregistrée (' + aff(der) + ')');
        const diff = herite.filter((h, i) => !(s.etat && memeEtat(s.etat[i], h))).length;
        if (diff) pb.push(diff + ' carte(s) sur ' + herite.length + ' ont perdu leur état hérité');
        if (!Array.isArray(s.etat) || s.etat.length !== n) pb.push('(d) flash:rlc non aligné : ' + (Array.isArray(s.etat) ? s.etat.length : typeof s.etat) + ' états pour ' + n + ' cartes');
        if (!Array.isArray(s.ids) || s.ids.length !== n) pb.push('flashids:rlc absent ou non aligné après la note du quiz');
        await page.keyboard.press('Escape');
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B2d — import d'une sauvegarde contenant 'flash:rlc' SANS 'flashids:rlc'
             (version antérieure) : la table locale doit être retirée, et
             l'état importé relu par position au rechargement
       ===================================================================== */
    await (async () => {
      const nom = 'B2d — import sans table d\'identifiants : état relu par position, table locale retirée';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        await charger(page, '#rlc/cours');
        // Table locale d'un deck INVERSÉ : si l'import la gardait, l'état importé
        // serait réaligné à l'envers au rechargement.
        await page.evaluate(() => {
          const cartes = FLASH_REGISTRY.rlc;
          Store.setJSON('flash:rlc', cartes.map(() => ({ h: 0, o: 1, e: 0, last: 1, box: 0, due: Date.now() })));
          Store.setJSON('flashids:rlc', flashCardIds(cartes.slice().reverse()));
        });
        const importe = Array.from({ length: n }, (_, i) => (i < 4
          ? { h: i, o: 0, e: 1, last: 2, box: i + 1, due: Date.now() + (i + 1) * JOUR } : { h: 0, o: 0, e: 0, last: null }));
        const f = ctx.fichierSortie('b2d-sauvegarde.json');
        fs.writeFileSync(f, JSON.stringify({ app: 'revisions-ptsi', version: 1, exportedAt: new Date().toISOString(),
          data: { 'flash:rlc': JSON.stringify(importe) } }, null, 1));
        journal.dialogue = d => d.accept();   // confirmation « Importer cette sauvegarde ? »
        await page.click('#more-btn');
        await pause(200);
        await page.click('#backup-btn');
        await pause(300);
        const recharge = page.waitForEvent('load', { timeout: 15000 });
        await page.setInputFiles('#backup-file-input', f);
        await recharge;
        await attendreApp(page);
        await fermerOverlays(page);
        await pause(300);
        const s = await lireEtat(page);
        const decales = importe.map((e, i) => (s.etat && memeEtat(s.etat[i], e) ? -1 : i)).filter(i => i >= 0);
        if (decales.length)
          pb.push(decales.length + ' carte(s) sur ' + n + ' sans l\'état importé à leur position (ex. index ' + decales[0] + ' : '
            + aff(s.etat && s.etat[decales[0]]) + ' au lieu de ' + aff(importe[decales[0]]) + ') : table locale d\'identifiants appliquée à tort ?');
        const idsDeck = await page.evaluate(() => flashCardIds(FLASH_REGISTRY.rlc));
        if (JSON.stringify(s.ids) !== JSON.stringify(idsDeck))
          pb.push('après rechargement, flashids:rlc ne décrit pas le deck actuel');
        exceptions(journal).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B2e — cartes signalées ('flagged' = {p, i, q…}) : après insertion d'une
             carte en tête du deck, l'index i suit la question
       ===================================================================== */
    await (async () => {
      const nom = 'B2e — cartes signalées : index réaligné après insertion d\'une carte';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        const cartes = extraireDeck(html, DECK).cartes;
        const K = [3, 7];
        await preremplir(page, { flagged: JSON.stringify(K.map(k => ({ p: 'rlc', i: k, q: cartes[k].q, a: cartes[k].a, t: Date.now() }))) });
        await charger(page, '#rlc/flash', { variante: 'b2', op: 'insertion', i: '0' });
        await pause(300);
        const r = await page.evaluate(() => ({ liste: Store.getJSON('flagged', []), questions: FLASH_REGISTRY.rlc.map(c => c.q) }));
        for (const k of K) {
          const x = (Array.isArray(r.liste) ? r.liste : []).find(e => e && e.q === cartes[k].q);
          if (!x) pb.push('carte signalée ' + court(cartes[k].q) + ' absente de la liste « flagged »');
          else if (+x.i !== k + 1 || r.questions[+x.i] !== cartes[k].q)
            pb.push('carte signalée ' + court(cartes[k].q) + ' : index ' + x.i + ' au lieu de ' + (k + 1) + ' après insertion d\'une carte en tête');
        }
        exceptions(journal).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B2e (suite) — cartes signalées, question en double (cas du doublon
             « Torricelli » de flu) : chaque signalement suit la copie de même
             question ET même réponse, pas la 1re copie venue
       ===================================================================== */
    await (async () => {
      const nom = 'B2e — cartes signalées, question en double : chaque signalement suit SA copie';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        const cartes = extraireDeck(html, DECK).cartes, K = 3;
        const q = cartes[K].q, a1 = cartes[K].a, a2 = a1 + ' (copie du test B2)';   // réponses des 2 copies (op « doublon »)
        const lireFlags = () => page.evaluate(() => Store.getJSON('flagged', []));
        const index = (liste, a) => { const x = (Array.isArray(liste) ? liste : []).find(e => e && e.q === q && e.a === a); return x ? +x.i : null; };
        // 1) copies échangées (1re copie en fin de deck, 2e à l'index K) : chaque signalement suit SA copie
        await preremplir(page, { flagged: JSON.stringify([{ p: 'rlc', i: K, q, a: a1, t: 1 }, { p: 'rlc', i: n, q, a: a2, t: 2 }]) });
        await charger(page, '#rlc/flash', { variante: 'b2', op: 'doublon,echange', i: String(K) });
        let l = await lireFlags();
        if (index(l, a1) !== n || index(l, a2) !== K)
          pb.push('copies échangées : signalement de la 1re copie à l\'index ' + index(l, a1) + ' (attendu ' + n + '), de la 2e à l\'index ' + index(l, a2) + ' (attendu ' + K + ')');
        // 2) carte insérée en tête : le signalement de la 2e copie la suit (n + 1), pas la 1re (K + 1)
        await preremplir(page, { flagged: JSON.stringify([{ p: 'rlc', i: n, q, a: a2, t: 2 }]) });
        await charger(page, '#rlc/flash', { variante: 'b2', op: 'doublon,insertion@0', i: String(K) });
        l = await lireFlags();
        if (index(l, a2) !== n + 1)
          pb.push('carte insérée en tête : signalement de la 2e copie à l\'index ' + index(l, a2) + ' au lieu de ' + (n + 1) + (index(l, a2) === K + 1 ? ' (rattaché à la 1re copie)' : ''));
        exceptions(journal).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B2e (fin) — signalement dont la question a été corrigée depuis
             (introuvable) : il garde son index, sauf si un autre signalement,
             déplacé, s'y trouve désormais → orphelin (i = −1). Sinon deux
             signalements marquent la même carte et un clic sur 🚩 retire
             l'autre (la carte reste « Signalée »)
       ===================================================================== */
    await (async () => {
      const nom = 'B2e — cartes signalées : question corrigée + carte déplacée sur son index → orphelin, un clic retire le drapeau';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        const cartes = extraireDeck(html, DECK).cartes;
        const signal = k => ({ p: 'rlc', i: k, q: cartes[k].q, a: cartes[k].a, t: k });
        // 1) question de la carte 5 corrigée sur place : son signalement reste sur elle
        await preremplir(page, { flagged: JSON.stringify([signal(5), signal(3)]) });
        await charger(page, '#rlc/flash', { variante: 'b2', op: 'edition', i: '5' });
        let l = await page.evaluate(() => Store.getJSON('flagged', []));
        const trouver = (liste, k) => (Array.isArray(liste) ? liste : []).find(e => e && e.q === cartes[k].q);
        if (!trouver(l, 5) || +trouver(l, 5).i !== 5) pb.push('question corrigée sur place : signalement à l\'index ' + (trouver(l, 5) || {}).i + ' au lieu de 5');
        // 2) même correction + 2 cartes insérées en tête : la carte 3 arrive à l'index 5
        await preremplir(page, { flagged: JSON.stringify([signal(5), signal(3)]) });
        await charger(page, '#rlc/flash', { variante: 'b2', op: 'edition@5,insertion@0,insertion@0', i: '0' });
        l = await page.evaluate(() => Store.getJSON('flagged', []));
        const s3 = trouver(l, 3), s5 = trouver(l, 5);
        if (!s3 || +s3.i !== 5) pb.push('signalement de la carte ' + court(cartes[3].q) + ' à l\'index ' + (s3 || {}).i + ' au lieu de 5');
        if (!s5) pb.push('signalement de la carte à question corrigée disparu de la liste (il doit rester listé)');
        else if (+s5.i !== -1) pb.push('signalement de la carte à question corrigée à l\'index ' + s5.i + ' au lieu de −1 (orphelin)' + (+s5.i === 5 ? ' : deux signalements sur la carte 5' : ''));
        // Un clic sur 🚩 (carte 5 affichée, « Signalée ») doit retirer SON drapeau
        const clic = await page.evaluate(() => { window.flagToggle('rlc', 5); return { marquee: window.flagIsFlagged('rlc', 5), liste: Store.getJSON('flagged', []) }; });
        if (clic.marquee) pb.push('après un clic sur 🚩, la carte 5 reste « Signalée »');
        if (!trouver(clic.liste, 5)) pb.push('un clic sur 🚩 de la carte 5 a retiré le signalement orphelin au lieu du sien');
        exceptions(journal).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B2f — question en double dans un deck (cas du doublon « Torricelli » de
             flu), un état distinct pour CHAQUE carte :
             • copies à réponses différentes : 1re copie reformulée (puis retour),
               1re copie retirée, copies échangées (la réponse départage : passe 2,
               « même réponse d'abord ») ;
             • doublon EXACT (même question, même réponse : seule la position
               départage) : 1re copie retirée (passe 2, écart à la position
               attendue), 3 cartes insérées en tête (décalage lu sur les voisines
               appariées en passe 1)
       ===================================================================== */
    await (async () => {
      const nom = 'B2f — question en double : chaque copie garde SON état (reformulée, retirée, échangée, doublon exact)';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        // Charge la variante `op` (index i) à partir de l'état s1 (réécrit d'abord, sauf
        // garder = on repart de l'état laissé par le chargement précédent) et compare
        const verif = async (s1, op, i, origine, quoi, garder) => {
          if (!garder) await restaurer(page, s1);
          await charger(page, '#rlc/flash', { variante: 'b2', op, i: String(i) });
          await pause(300);
          comparer(s1, await lireEtat(page), origine, quoi, pb);
        };
        // Copies de la carte K aux index K et n (fin du deck), réponses différentes
        const K = 3;
        await charger(page, '#rlc/cours', { variante: 'b2', op: 'doublon', i: String(K) });
        const s1 = await etatsDistincts(page);
        if (s1.questions.length !== n + 1 || s1.questions[K] !== s1.questions[n]) throw new Error('préparation : la variante « doublon » n\'a pas été servie');
        await verif(s1, 'doublon,edition', K, j => j, '1re copie reformulée');
        await verif(s1, 'doublon', K, j => j, 'retour au libellé d\'origine', true);
        await verif(s1, 'doublon,retrait', K, j => (j < K ? j : j + 1), '1re copie retirée');
        await verif(s1, 'doublon,echange', K, j => (j === K ? n : j === n ? K : j), 'copies échangées (la réponse départage)');
        // Doublon EXACT de l'avant-dernière carte, ajouté en fin : copies aux index n − 2 et n
        const K2 = n - 2;
        await charger(page, '#rlc/cours', { variante: 'b2', op: 'doublonexact', i: String(K2) });
        const s1x = await etatsDistincts(page);
        if (s1x.questions.length !== n + 1 || s1x.questions[K2] !== s1x.questions[n]) throw new Error('préparation : la variante « doublonexact » n\'a pas été servie');
        await verif(s1x, 'doublonexact,retrait', K2, j => (j < K2 ? j : j + 1), 'doublon exact, 1re copie retirée');
        await verif(s1x, 'doublonexact,insertion@0,insertion@0,insertion@0', K2, j => (j < 3 ? -1 : j - 3), 'doublon exact, 3 cartes insérées en tête');
        exceptions(journal).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B3 — SLCI, 2e ordre apériodique : t₅% affiché et départ de la courbe
       ===================================================================== */
    await (async () => {
      const nom = 'B3 — SLCI 2e ordre : s(0) = 0, palier dans la fenêtre et t₅% exact (ξ > 1), t₅% exact hors fenêtre (ξ = 0,05)';
      const pb = [];
      try {
        const { page, journal } = await ctx.nouvellePage();
        await charger(page, '#slci/simu');
        await page.click('[data-slci-mode="t2"]');
        await pause(200);
        const regler = (K, w0, z) => page.evaluate(([K, w0, z]) => {
          for (const [id, v] of [['slci-K', K], ['slci-w0', w0], ['slci-z', z]]) {
            const el = document.getElementById(id);
            el.value = String(v);
            el.dispatchEvent(new Event('input', { bubbles: true }));
          }
        }, [K, w0, z]);
        const lireT5 = () => page.evaluate(() => {
          const lignes = Array.from(document.querySelectorAll('#slci-simu .sim-info > div'));
          const l = lignes.find(d => /t\s*[₅5]\s*%/.test((d.querySelector('.lbl') || {}).textContent || ''));
          if (!l) return null;
          const spans = Array.from(l.querySelectorAll('span')).filter(s => !s.classList.contains('lbl'));
          return spans.map(s => s.textContent).join(' ').trim();
        });
        // 3 réglages apériodiques (B3) + 2 pseudo-périodiques très peu amortis, dont le
        // t₅% dépasse la fenêtre tracée (bornée à 80 s) : il était tronqué à ≈ 80 s.
        for (const [K, w0, z] of [[2, 2, 2], [1, 4, 1.5], [1.5, 2, 1.2], [1, 0.5, 0.05], [1, 0.7, 0.05]]) {
          await regler(K, w0, z);
          await pause(250);
          const texte = await lireT5();
          const exact = z > 1 ? t5Exact(K, w0, z) : t5PseudoExact(K, w0, z);
          const m = texte && /(\d+(?:[.,]\d+)?)/.exec(texte);
          const lu = m ? parseFloat(m[1].replace(',', '.')) : NaN;
          if (!(Math.abs(lu - exact) <= 0.02 * exact))
            pb.push('K=' + K + ', ω₀=' + w0 + ', ξ=' + z + ' : t₅% affiché « ' + texte + ' », valeur exacte ' + exact.toFixed(2) + ' s (tolérance ±2 %)');
        }
        // Départ de la courbe : au niveau de l'axe des temps (s = 0), pas au-dessus
        await regler(2, 2, 2);
        await pause(250);
        const px = await page.evaluate(() => {
          const cv = document.getElementById('slci-canvas');
          const W = cv.width, H = cv.height, dpr = window.devicePixelRatio || 1;
          const d = cv.getContext('2d').getImageData(0, 0, W, H).data;
          const col = getCanvasColors();
          const rgb = h => { h = String(h).trim().replace('#', ''); if (h.length === 3) h = h.split('').map(x => x + x).join(''); return [0, 2, 4].map(k => parseInt(h.substr(k, 2), 16)); };
          const acc = rgb(col.accent), ink = rgb(col.ink);
          const proche = (i, c, tol) => d[i + 3] > 180 && Math.abs(d[i] - c[0]) + Math.abs(d[i + 1] - c[1]) + Math.abs(d[i + 2] - c[2]) < tol;
          let xmin = Infinity; const pts = [];
          for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) if (proche((y * W + x) * 4, acc, 60)) { pts.push([x, y]); if (x < xmin) xmin = x; }
          let yAxe = -1, meilleur = 0;
          for (let y = Math.floor(H / 2); y < H; y++) {
            let k = 0; for (let x = 0; x < W; x++) if (proche((y * W + x) * 4, ink, 90)) k++;
            if (k > meilleur) { meilleur = k; yAxe = y; }
          }
          if (!pts.length) return { courbe: false, H, yAxe };
          const debut = pts.filter(p => p[0] <= xmin + 3 * dpr);
          // Palier : y moyen de la courbe par colonne, à droite (xmax) et 10 % plus à gauche
          const cols = new Map();
          pts.forEach(([x, y]) => { if (!cols.has(x)) cols.set(x, []); cols.get(x).push(y); });
          const xs = [...cols.keys()].sort((a, b) => a - b), xmax = xs[xs.length - 1];
          const yMoy = x => { const k = xs.reduce((m, c) => (Math.abs(c - x) < Math.abs(m - x) ? c : m), xs[0]); const l = cols.get(k); return l.reduce((t, y) => t + y, 0) / l.length; };
          return { courbe: true, H, dpr, yAxe, axeLong: meilleur / W, yDebut: debut.reduce((t, p) => t + p[1], 0) / debut.length, xmin,
            yFin: yMoy(xmax), y10: yMoy(xmax - 0.1 * (xmax - xmin)) };
        });
        if (!px.courbe) pb.push('K=2, ω₀=2, ξ=2 : aucun pixel de la courbe dans le cadre (s(t) hors échelle, ex. s(0) = 2K)');
        else if (px.yAxe < 0 || px.axeLong < 0.3) pb.push('axe des temps introuvable sur le canvas (test à adapter ?)');
        else if (Math.abs(px.yDebut - px.yAxe) > Math.max(4 * px.dpr, 0.03 * px.H))
          pb.push('K=2, ω₀=2, ξ=2 : la courbe démarre à ' + Math.round(px.yAxe - px.yDebut) + ' px au-dessus de l\'axe des temps (s(0) ≠ 0)');
        // Fenêtre de temps fixée par le pôle lent : la courbe doit avoir atteint son palier
        // (sur les 10 % de droite, elle varie de moins de 2 % de sa montée totale)
        if (px.courbe) {
          const montee = px.yDebut - px.yFin, variation = Math.abs(px.y10 - px.yFin);
          if (!(montee > 0) || variation > 0.02 * montee)
            pb.push('K=2, ω₀=2, ξ=2 : la courbe n\'atteint pas son palier dans la fenêtre tracée (elle monte encore de ' + Math.round(variation)
              + ' px sur les 10 % de droite, pour une montée totale de ' + Math.round(montee) + ' px) : fenêtre de temps trop courte (pôle lent ignoré ?)');
        }
        await ctx.capture(page, 'b3-slci-aperiodique', { selecteur: '#slci-canvas' });
        exceptions(journal).forEach(e => pb.push('exception JavaScript : ' + e));
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();

    /* =====================================================================
       B4 — getCanvasColors() / __CV() en clair et en sombre
       ===================================================================== */
    await (async () => {
      const nom = 'B4 — getCanvasColors() et __CV() : muted / grid suivent le thème';
      const pb = [];
      const compact = s => String(s).replace(/\s+/g, '').toLowerCase();
      const attendu = { clair: { muted: '#666666', grid: 'rgba(45,95,138,0.08)' }, sombre: { muted: '#a8a496', grid: 'rgba(200,200,180,0.12)' } };
      try {
        const { page } = await ctx.nouvellePage();
        await charger(page, '#rlc/simu');
        const lire = () => page.evaluate(() => {
          const a = getCanvasColors(), b = __CV();
          return { theme: document.documentElement.getAttribute('data-theme'), gc: { muted: a.muted, grid: a.grid }, cv: { muted: b.muted, grid: b.grid } };
        });
        const controler = (etiquette, v, att) => {
          for (const src of ['gc', 'cv']) for (const k of ['muted', 'grid']) {
            if (compact(v[src][k]) !== compact(att[k]))
              pb.push(etiquette + ' : ' + (src === 'gc' ? 'getCanvasColors()' : '__CV()') + '.' + k + ' = ' + v[src][k] + ' (attendu ' + att[k] + ')');
          }
        };
        const v1 = await lire();
        if (v1.theme === 'dark') throw new Error('préparation : le site démarre en thème sombre');
        controler('thème clair', v1, attendu.clair);
        await page.click('#theme-btn');
        await pause(300);
        const v2 = await lire();
        if (v2.theme !== 'dark') throw new Error('préparation : #theme-btn n\'a pas activé le thème sombre');
        controler('thème sombre', v2, attendu.sombre);
        await page.click('#theme-btn');
        await pause(300);
        controler('retour au clair', await lire(), attendu.clair);
      } catch (e) { pb.push(String(e.message).split('\n')[0]); }
      res.verifier(nom, !pb.length, pb);
    })();
  },
};
