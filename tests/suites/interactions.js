'use strict';
/* ============================================================
   Suite « interactions » — parcours d'un utilisateur sur ordinateur
   ============================================================
   Deep-link #hash, routage (précédent / suivant du navigateur), boutons
   ‹ › de chapitre, bascule vers la SI, recherche, flashcards + Leitner, quiz,
   « Réviser », Bilan, Aujourd'hui, formulaire, cartes signalées, calcul
   mental, impression, thème, sauvegarde (export PUIS import, qui recharge). */
const fs = require('fs');
const { pause, attendreApp, fermerOverlays, naviguer, marqueJournal, problemesJournal } = require('../lib/outils');

/* Chapitre réellement affiché (deux .chapter.active coexistent au chargement :
   un dans chaque <main> ; on garde celui qui est visible) */
const CHAP_VISIBLE = () => {
  const v = Array.from(document.querySelectorAll('.chapter.active')).find(c => c.offsetParent !== null);
  return v ? v.id : null;
};

module.exports = {
  nom: 'interactions',
  description: "quiz, recherche, Bilan, Aujourd'hui, sauvegarde, navigation, #hash",
  delaiMax: () => 8 * 60000,

  async executer(ctx, res) {
    const { page, journal } = await ctx.nouvellePage();

    /* Chaque étape : exceptions et erreurs JS de l'étape → échec de l'étape */
    async function etape(nom, fn) {
      journal.lieu = nom;
      const m = marqueJournal(journal);
      let pb = [];
      try { pb = (await fn()) || []; }
      catch (e) { pb = ['exception du test : ' + String(e.message).split('\n')[0]]; }
      pb = pb.filter(Boolean).concat(problemesJournal(journal, m));
      res.verifier(nom, !pb.length, pb);
      await fermerOverlays(page).catch(() => {});
    }
    const visible = () => page.evaluate(CHAP_VISIBLE);
    const ouvert = id => page.evaluate(id => { const o = document.getElementById(id); return !!(o && o.classList.contains('open')); }, id);

    /* ---------- Deep-link ---------- */
    await etape('deep-link #rlc/simu (sans écran Aujourd\'hui)', async () => {
      await page.goto(ctx.url('#rlc/simu'), { waitUntil: 'load', timeout: 60000 });
      await attendreApp(page);
      await pause(400);
      const s = await page.evaluate(() => ({
        aujourdhui: document.getElementById('today-overlay').classList.contains('open'),
        panneau: (document.querySelector('#chap-rlc .panel.active') || {}).id,
        hash: location.hash,
      }));
      s.chap = await visible();
      return [
        s.aujourdhui && "l'écran Aujourd'hui s'ouvre alors qu'un #hash est fourni",
        s.chap !== 'chap-rlc' && 'chapitre affiché : ' + s.chap + ' au lieu de chap-rlc',
        s.panneau !== 'rlc-simu' && 'onglet actif : ' + s.panneau + ' au lieu de rlc-simu',
        s.hash !== '#rlc/simu' && 'hash : ' + s.hash,
      ];
    });

    // Chapitre dont l'id diffère du prefix (cas le plus fréquent, source de bugs)
    const autre = await page.evaluate(() => {
      const c = CHAPTERS.find(x => x.id !== 'rlc' && x.id !== x.prefix && x.matiere !== 'si' && x.panels.includes('flash'));
      return { id: c.id, prefix: c.prefix };
    });

    /* ---------- Routage : hash, pushState / replaceState, précédent ---------- */
    await etape('routage #hash + bouton précédent/suivant du navigateur (' + autre.id + ')', async () => {
      const pb = [];
      await naviguer(page, autre.id, 'cours');
      let h = await page.evaluate(() => location.hash);
      if (h !== '#' + autre.id + '/cours') pb.push('après navigation : hash ' + h + ' au lieu de #' + autre.id + '/cours');
      const lg = await page.evaluate(() => history.length);
      await page.evaluate(pid => document.querySelector('.tab[data-panel="' + pid + '"]').click(), autre.prefix + '-flash');
      await pause(150);
      h = await page.evaluate(() => location.hash);
      if (h !== '#' + autre.id + '/flash') pb.push('après clic sur l\'onglet Flashcards : hash ' + h);
      if (await page.evaluate(() => history.length) !== lg) pb.push("un changement d'onglet ne doit pas créer d'entrée d'historique (replaceState)");
      await page.goBack();
      await pause(500);
      if (await visible() !== 'chap-rlc') pb.push('« précédent » : chapitre affiché ' + (await visible()) + ' au lieu de chap-rlc');
      h = await page.evaluate(() => location.hash);
      if (!h.startsWith('#rlc/')) pb.push('« précédent » : hash ' + h);
      await page.goForward();
      await pause(500);
      if (await visible() !== 'chap-' + autre.id) pb.push('« suivant » : chapitre affiché ' + (await visible()));
      return pb;
    });

    /* ---------- Bascule vers un chapitre SI (<main id="si-content">) ---------- */
    await etape('navigation vers un chapitre SI (bascule de <main>)', async () => {
      const si = await page.evaluate(() => CHAPTERS.find(c => c.matiere === 'si').id);
      await naviguer(page, si, 'cours');
      const s = await page.evaluate(id => ({
        siAffiche: getComputedStyle(document.getElementById('si-content')).display !== 'none',
        principalMasque: getComputedStyle(document.querySelector('main:not(#si-content)')).display === 'none',
        visible: !!document.getElementById('chap-' + id).offsetParent,
      }), si);
      const pb = [!s.siAffiche && '#si-content reste masqué', !s.principalMasque && 'le <main> principal reste affiché',
        !s.visible && 'chap-' + si + ' invisible'];
      await naviguer(page, 'rlc', 'cours');
      if (await visible() !== 'chap-rlc') pb.push('retour vers rlc impossible (chapitre affiché : ' + (await visible()) + ')');
      return pb;
    });

    /* ---------- Boutons ‹ › (chapitre précédent / suivant) ---------- */
    await etape('boutons chapitre précédent / suivant', async () => {
      const pb = [];
      const ids = await page.evaluate(() => CHAPTERS.map(c => c.id));
      const k = Math.min(5, ids.length - 2);
      await naviguer(page, ids[k], 'cours');
      await page.evaluate(() => document.getElementById('next-chap-btn').click());
      await pause(400);
      if (await visible() !== 'chap-' + ids[k + 1]) pb.push('› : chapitre affiché ' + (await visible()) + ' au lieu de chap-' + ids[k + 1]);
      await page.evaluate(() => document.getElementById('prev-chap-btn').click());
      await pause(400);
      if (await visible() !== 'chap-' + ids[k]) pb.push('‹ : chapitre affiché ' + (await visible()) + ' au lieu de chap-' + ids[k]);
      await naviguer(page, ids[0], 'cours');
      await pause(100);
      if (!(await page.evaluate(() => document.getElementById('prev-chap-btn').disabled))) pb.push('‹ devrait être désactivé sur le premier chapitre');
      return pb;
    });

    /* ---------- Recherche ---------- */
    await etape('recherche (Ctrl K / bouton) : résultats puis Entrée', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'cours');
      const avant = await page.evaluate(() => location.hash);
      await page.click('#search-btn');
      await pause(250);
      if (!(await ouvert('search-overlay'))) return ['la fenêtre de recherche ne s\'ouvre pas'];
      await page.fill('#search-input', 'fourier');
      await pause(500);
      const n = await page.evaluate(() => document.querySelectorAll('#search-results .search-result').length);
      if (!n) pb.push('aucun résultat pour « fourier »');
      await page.keyboard.press('Enter');
      await pause(500);
      if (await ouvert('search-overlay')) pb.push('la recherche reste ouverte après Entrée');
      const apres = await page.evaluate(() => location.hash);
      if (n && apres === avant) pb.push('Entrée n\'a pas navigué vers le 1er résultat (hash inchangé : ' + apres + ')');
      await page.keyboard.press('Control+k');
      await pause(200);
      if (!(await ouvert('search-overlay'))) pb.push('Ctrl+K n\'ouvre pas la recherche');
      await page.keyboard.press('Escape');
      await pause(150);
      if (await ouvert('search-overlay')) pb.push('Échap ne ferme pas la recherche');
      return pb;
    });

    /* ---------- Flashcards + répétition espacée ---------- */
    await etape('flashcards : retourner, noter, progression et Leitner', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'flash');
      const q = await page.evaluate(() => document.getElementById('rlc-flash-content').innerText);
      await page.click('#rlc-flash .flash-card');
      await pause(600);
      const a = await page.evaluate(() => document.getElementById('rlc-flash-content').innerText);
      if (a === q || !/R[ÉE]PONSE/i.test(a)) pb.push('la carte ne se retourne pas (face : ' + a.slice(0, 40) + ')');
      await page.click('#rlc-flash .flash-controls .easy');
      await pause(400);
      const s = await page.evaluate(() => {
        const st = Store.getJSON('flash:rlc', []) || [];
        const notees = st.filter(x => x && x.last !== null && x.last !== undefined);
        return { notees, n: FLASH_REGISTRY.rlc.length, prog: document.getElementById('rlc-flash-prog').textContent,
          stats: document.getElementById('rlc-stats').textContent };
      });
      if (s.notees.length !== 1) pb.push(s.notees.length + ' carte(s) notée(s) dans le Store au lieu de 1');
      else {
        const c = s.notees[0];
        if (c.last !== 2 || c.e !== 1) pb.push('état enregistré inattendu : ' + JSON.stringify(c));
        if (c.box !== 1 || !(c.due > Date.now() + 12 * 3600e3)) pb.push('Leitner : box=' + c.box + ', due=' + c.due + ' (attendu box 1, révision dans ~1 jour)');
      }
      if (!new RegExp('Carte 2 / ' + s.n).test(s.prog)) pb.push('progression : « ' + s.prog + ' »');
      if (!/Acquis\s*:\s*1\//.test(s.stats)) pb.push('statistiques : « ' + s.stats + ' »');
      // « Voir le cours » bascule sur l'onglet Cours
      await page.evaluate(() => document.querySelector('#rlc-flash .flash-course-link').click());
      await pause(500);
      const actif = await page.evaluate(() => (document.querySelector('#chap-rlc .panel.active') || {}).id);
      if (actif !== 'rlc-cours') pb.push('« Voir le cours » : onglet actif ' + actif);
      return pb;
    });

    /* ---------- Quiz global ---------- */
    await etape('quiz global : configuration, question, notation, fermeture', async () => {
      const pb = [];
      const compte = () => page.evaluate(() => Object.keys(FLASH_REGISTRY).reduce((n, p) =>
        n + ((Store.getJSON('flash:' + p, []) || []).filter(s => s && s.last !== null && s.last !== undefined).length), 0));
      const avant = await compte();
      await page.click('#study-btn');
      await pause(200);
      await page.click('#quiz-btn');
      await pause(500);
      if (!(await ouvert('quiz-overlay'))) return ['le quiz ne s\'ouvre pas'];
      const info = await page.evaluate(() => document.getElementById('quiz-config-info').textContent);
      if (!/carte/.test(info)) pb.push('configuration : « ' + info + ' »');
      await page.click('#quiz-start-btn');
      await pause(400);
      const q = await page.evaluate(() => ({
        ecran: getComputedStyle(document.getElementById('quiz-screen-question')).display !== 'none',
        texte: document.getElementById('quiz-question-text').textContent.trim(),
        prog: document.getElementById('quiz-progress-text').textContent,
      }));
      if (!q.ecran || !q.texte) return pb.concat(['l\'écran question ne s\'affiche pas']);
      await page.click('#quiz-reveal-btn');
      await pause(250);
      await page.click('#quiz-actions-rate .rate-acq');
      await pause(300);
      const prog2 = await page.evaluate(() => document.getElementById('quiz-progress-text').textContent);
      if (prog2.split('/')[0].trim() !== '2') pb.push('progression après notation : « ' + prog2 + ' » (avant : « ' + q.prog + ' »)');
      const apres = await compte();
      if (apres !== avant + 1) pb.push('cartes notées dans le Store : ' + avant + ' → ' + apres + ' (attendu +1)');
      await page.keyboard.press('Escape');
      await pause(200);
      if (await ouvert('quiz-overlay')) pb.push('Échap ne ferme pas le quiz');
      return pb;
    });

    /* ---------- « Révisions du jour » ---------- */
    await etape('« Réviser » (révisions du jour) sans carte due', async () => {
      await page.click('#study-btn');
      await pause(200);
      await page.click('#revise-btn');
      await pause(400);
      const s = await page.evaluate(() => ({
        ouvert: document.getElementById('quiz-overlay').classList.contains('open'),
        info: document.getElementById('quiz-config-info').textContent,
      }));
      await page.keyboard.press('Escape');
      return [!s.ouvert && 'la fenêtre du quiz ne s\'ouvre pas',
        s.ouvert && !/Aucune carte à réviser/.test(s.info) && 'message attendu « Aucune carte à réviser… », obtenu « ' + s.info + ' »'];
    });

    /* ---------- Bilan ---------- */
    await etape('Bilan : statistiques et clic vers un chapitre', async () => {
      const pb = [];
      await page.click('#dash-btn');
      await pause(400);
      if (!(await ouvert('dash-overlay'))) return ['le Bilan ne s\'ouvre pas'];
      const s = await page.evaluate(() => ({
        texte: document.getElementById('dash-overlay').innerText,
        rlc: !!document.querySelector('#dash-overlay .dash-chap[data-chap="rlc"]'),
      }));
      if (!/%/.test(s.texte) || !/acquises/.test(s.texte)) pb.push('contenu inattendu : ' + s.texte.slice(0, 80).replace(/\s+/g, ' '));
      if (!s.rlc) pb.push('la ligne du chapitre rlc (noté plus haut) est absente');
      else {
        await page.click('#dash-overlay .dash-chap[data-chap="rlc"]');
        await pause(500);
        const actif = await page.evaluate(() => (document.querySelector('#chap-rlc .panel.active') || {}).id);
        if (await ouvert('dash-overlay')) pb.push('le Bilan reste ouvert après le clic');
        if (actif !== 'rlc-flash') pb.push('clic sur rlc : onglet actif ' + actif + ' au lieu de rlc-flash');
      }
      return pb;
    });

    /* ---------- Aujourd'hui ---------- */
    await etape("écran « Aujourd'hui » (menu Plus)", async () => {
      await page.click('#more-btn');
      await pause(200);
      await page.click('#today-btn');
      await pause(400);
      const s = await page.evaluate(() => ({
        ouvert: document.getElementById('today-overlay').classList.contains('open'),
        date: document.getElementById('today-date').textContent,
        reprendre: !document.getElementById('today-resume-wrap').hidden,
      }));
      const pb = [!s.ouvert && "l'écran ne s'ouvre pas", s.ouvert && (s.date === '—' || !s.date) && 'date non renseignée',
        s.ouvert && !s.reprendre && 'section « Reprendre » absente alors qu\'un chapitre a été consulté'];
      await page.click('#today-close').catch(() => {});
      await pause(200);
      if (await ouvert('today-overlay')) pb.push('« Continuer » ne ferme pas l\'écran');
      return pb;
    });

    /* ---------- Fenêtres secondaires ---------- */
    for (const [nom, menu, bouton, fenetre] of [
      ['formulaire du chapitre', '#more-btn', '#formula-btn', 'formula-overlay'],
      ['cartes signalées', '#more-btn', '#flag-btn', 'flag-overlay'],
      ['calcul mental', '#study-btn', '#drill-btn', 'drill-overlay'],
    ]) {
      await etape('fenêtre « ' + nom + ' » : ouverture et Échap', async () => {
        await naviguer(page, 'rlc', 'cours');
        await page.click(menu);
        await pause(200);
        await page.click(bouton);
        await pause(500);
        const s = await page.evaluate(id => { const o = document.getElementById(id); return o ? { ouvert: o.classList.contains('open'), n: o.innerText.trim().length } : null; }, fenetre);
        if (!s) return ['#' + fenetre + ' absent'];
        await page.keyboard.press('Escape');
        await pause(200);
        return [!s.ouvert && 'la fenêtre ne s\'ouvre pas', s.ouvert && s.n < 20 && 'fenêtre vide',
          (await ouvert(fenetre)) && 'Échap ne ferme pas la fenêtre'];
      });
    }

    /* ---------- Impression (génération de l'iframe seulement) ---------- */
    await etape('impression du chapitre (document généré)', async () => {
      await naviguer(page, 'rlc', 'cours');
      await page.evaluate(() => { window.print = () => {}; printChapter(); });
      await pause(2500);
      const s = await page.evaluate(() => {
        const f = document.getElementById('print-iframe') || Array.from(document.querySelectorAll('iframe')).pop();
        try { const d = f && f.contentDocument; return d ? { titre: d.title, texte: d.body ? d.body.innerText.length : 0, base: !!d.querySelector('base') } : null; }
        catch (e) { return { erreur: e.message }; }
      });
      if (!s) return ['aucune iframe d\'impression générée'];
      return [s.erreur && s.erreur, !s.erreur && s.texte < 200 && 'document d\'impression quasi vide (' + s.texte + ' caractères)',
        !s.erreur && !s.base && 'balise <base> absente (les chemins vendor/… ne résoudraient pas)'];
    });

    /* ---------- Lecture audio des cartes d'anglais (présence du bouton) ---------- */
    await etape('bouton de lecture audio sur une flashcard d\'anglais', async () => {
      const ang = await page.evaluate(() => { const c = CHAPTERS.find(x => x.matiere === 'anglais' && x.panels.includes('flash')); return c && c.id; });
      if (!ang) return [];
      await naviguer(page, ang, 'flash');
      const s = await page.evaluate(id => ({ ok: !!(window.__TTS && window.__TTS.ok), btn: !!document.querySelector('#chap-' + id + ' .flash-tts-btn') }), ang);
      return [s.ok && !s.btn && 'bouton .flash-tts-btn absent alors que la synthèse vocale est disponible'];
    });

    /* ---------- Thème ---------- */
    await etape('thème sombre puis clair (#theme-btn, mémorisé)', async () => {
      await page.click('#theme-btn');
      await pause(250);
      const a = await page.evaluate(() => ({ t: document.documentElement.getAttribute('data-theme'), s: Store.get('theme') }));
      await page.click('#theme-btn');
      await pause(250);
      const b = await page.evaluate(() => ({ t: document.documentElement.getAttribute('data-theme'), s: Store.get('theme') }));
      return [(a.t !== 'dark' || a.s !== 'dark') && '1er clic : data-theme=' + a.t + ', Store=' + a.s,
        (b.t === 'dark' || b.s === 'dark') && '2e clic : data-theme=' + b.t + ', Store=' + b.s];
    });

    /* ---------- Sauvegarde : export ---------- */
    let exporte = null;
    await etape('sauvegarde : export JSON (téléchargement)', async () => {
      await page.click('#more-btn');
      await pause(200);
      await page.click('#backup-btn');
      await pause(300);
      if (!(await ouvert('backup-overlay'))) return ['la fenêtre Sauvegarde ne s\'ouvre pas'];
      const [dl] = await Promise.all([page.waitForEvent('download', { timeout: 8000 }), page.click('#backup-export-btn')]);
      const f = ctx.fichierSortie('sauvegarde-exportee.json');
      await dl.saveAs(f);
      exporte = JSON.parse(fs.readFileSync(f, 'utf8'));
      const fb = await page.evaluate(() => document.getElementById('backup-feedback').textContent);
      return [exporte.app !== 'revisions-ptsi' && 'champ app = ' + exporte.app, exporte.version !== 1 && 'champ version = ' + exporte.version,
        !(exporte.data && exporte.data['flash:rlc']) && 'la progression flash:rlc est absente de l\'export',
        !/Export réussi/.test(fb) && 'message de confirmation absent (« ' + fb + ' »)'];
    });

    /* ---------- Sauvegarde : import (recharge la page) ---------- */
    await etape('sauvegarde : import JSON puis rechargement', async () => {
      const n = await page.evaluate(p => FLASH_REGISTRY[p].length, autre.prefix);
      const etat = Array.from({ length: n }, (_, i) => i < 3
        ? { h: 0, o: 0, e: 1, last: 2, box: 1, due: Date.now() + 86400000 } : { h: 0, o: 0, e: 0, last: null });
      const donnees = { app: 'revisions-ptsi', version: 1, exportedAt: new Date().toISOString(),
        data: Object.assign({}, exporte ? exporte.data : {}, { ['flash:' + autre.prefix]: JSON.stringify(etat) }) };
      const f = ctx.fichierSortie('sauvegarde-a-importer.json');
      fs.writeFileSync(f, JSON.stringify(donnees, null, 1));
      let confirme = null;
      journal.dialogue = d => { confirme = d.message(); d.accept(); };
      const recharge = page.waitForEvent('load', { timeout: 15000 });
      await page.setInputFiles('#backup-file-input', f);
      await recharge;
      await attendreApp(page);
      const lu = await page.evaluate(p => Store.getJSON('flash:' + p, null), autre.prefix);
      await naviguer(page, autre.id, 'flash');
      const stats = await page.evaluate(p => document.getElementById(p + '-stats').textContent, autre.prefix);
      return [!confirme && 'aucune demande de confirmation avant l\'import',
        JSON.stringify(lu) !== JSON.stringify(etat) && 'la progression importée n\'a pas été réécrite dans le Store',
        !/Acquis\s*:\s*3\//.test(stats) && 'statistiques du chapitre après import : « ' + stats + ' »'];
    });

    if (journal.dialogues.length) res.avertir('boîte(s) de dialogue inattendue(s) : ' + journal.dialogues.map(d => d.type + ' « ' + d.message + ' »').join(' ; '));
  },
};
