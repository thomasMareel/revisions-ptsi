'use strict';
/* ============================================================
   Suite « mobile » — téléphone 390×844 (tactile)
   ============================================================
   - en-tête mobile visible, sommaire masqué, écran « Aujourd'hui » NON ouvert au lancement ;
   - tiroir des chapitres : ouverture, changement de matière, filtre
     (résultats, aucun résultat, Entrée = 1er résultat) ;
   - débordement horizontal (scrollWidth > largeur d'écran) de CHAQUE panneau.
     Des panneaux débordent déjà (formules en ligne trop longues, voir
     tests/README.md §5) : ils sont listés dans DEBORDEMENTS_CONNUS. La suite n'échoue que
     pour un NOUVEAU débordement, et signale un panneau connu qui ne déborde plus. */
const { pause, attendreApp, fermerOverlays, naviguer, choisirTheme, etatMathJax } = require('../lib/outils');

/* Panneaux qui débordent à 390 px (mesurés avec cette suite, Chromium 141) : largeur de page
   mesurée (px) et formule en cause. Un panneau connu fait quand même échouer si sa largeur augmente
   de plus de MARGE px (nouvelle formule plus large). Quand un débordement est corrigé, la suite
   affiche un avertissement : retirer alors la ligne correspondante.
   Liste VIDE depuis la refonte du contenu (formules en bloc défilantes, formules en ligne trop
   larges en .mj-large, schémas élargis) : les 13 panneaux du commit a04c445 (rlc-cours 415 px,
   sig-meth, mp-exos, cpx-meth, pol-cours, suit-meth, cd-cours, dl-meth, asy-meth, prim-meth,
   va-cours, ensi-meth, repn-cours) ne débordent plus. Format d'une entrée :
   'rlc-cours': { largeur: 415, formule: '\\dot{u}_C(0) = 0 …' }, */
const DEBORDEMENTS_CONNUS = {};

const LARGEUR = 390;
const MARGE = 12;   // tolérance (px) sur la largeur des débordements connus (polices, système)

module.exports = {
  nom: 'mobile',
  description: 'téléphone 390 px : tiroir, filtre, débordements horizontaux',
  delaiMax: o => (o.rapide ? 8 : 30) * 60000,

  async executer(ctx, res) {
    const { page, journal } = await ctx.nouvellePage({ mobile: true, largeur: LARGEUR, hauteur: 844 });

    /* ---------- 1) Lancement ---------- */
    journal.lieu = 'chargement mobile';
    await page.goto(ctx.url(), { waitUntil: 'load', timeout: 60000 });
    await attendreApp(page);
    const lancement = await page.evaluate(() => {
      const vis = el => !!el && getComputedStyle(el).display !== 'none' && el.getBoundingClientRect().width > 0;
      const toc = document.querySelector('.toc');
      const today = document.getElementById('today-overlay');
      return {
        entete: vis(document.getElementById('mob-header')),
        tocMasque: !toc || getComputedStyle(toc).display === 'none',
        aujourdhui: !!(today && today.classList.contains('open')),
      };
    });
    await ctx.capture(page, 'accueil');
    res.verifier('en-tête mobile visible et sommaire (.toc) masqué', lancement.entete && lancement.tocMasque,
      [!lancement.entete && '#mob-header invisible', !lancement.tocMasque && 'le sommaire .toc est affiché en mobile (il doit être masqué)']);
    res.verifier("écran « Aujourd'hui » non ouvert au lancement", !lancement.aujourdhui, "#today-overlay ouvert au lancement : le site doit s'ouvrir sur le dernier chapitre consulté");
    await fermerOverlays(page);

    /* ---------- 2) Tiroir des chapitres ---------- */
    journal.lieu = 'tiroir';
    const pbTiroir = [];
    try {
      await page.tap('#mob-menu-btn');
      await pause(450);
      const t = await page.evaluate(() => ({
        ouvert: document.getElementById('mob-drawer').classList.contains('open'),
        aria: document.getElementById('mob-menu-btn').getAttribute('aria-expanded'),
        rangees: document.querySelectorAll('#mob-chap-list .mob-chap-row').length,
      }));
      if (!t.ouvert) pbTiroir.push('le tiroir ne s\'ouvre pas (#mob-drawer sans .open)');
      if (t.aria !== 'true') pbTiroir.push('aria-expanded du bouton menu = ' + t.aria);
      if (!t.rangees) pbTiroir.push('aucune rangée de chapitre dans le tiroir');
      await ctx.capture(page, 'tiroir');

      await page.tap('.mob-mat-btn[data-mat="maths"]');
      await pause(300);
      const nbMaths = await page.evaluate(() => document.querySelectorAll('#mob-chap-list .mob-chap-item').length);
      if (!nbMaths) pbTiroir.push('matière « maths » : aucun chapitre listé');

      await page.fill('#mob-filter', 'electro');
      await pause(300);
      const f1 = await page.evaluate(() => Array.from(document.querySelectorAll('#mob-chap-list .mob-chap-item')).map(b => b.innerText.replace(/\s+/g, ' ').trim()));
      if (!f1.some(x => /lectrostatique/i.test(x))) pbTiroir.push('filtre « electro » : « Électrostatique » absent des résultats (' + f1.slice(0, 5).join(' | ') + ')');
      await ctx.capture(page, 'filtre');

      await page.fill('#mob-filter', 'zzzqqq');
      await pause(250);
      const f2 = await page.evaluate(() => ({ n: document.querySelectorAll('#mob-chap-list .mob-chap-item').length, vide: !!document.querySelector('#mob-chap-list .mob-filter-empty') }));
      if (f2.n || !f2.vide) pbTiroir.push('filtre sans résultat : ' + f2.n + ' chapitre(s) listé(s), message « aucun résultat » ' + (f2.vide ? 'présent' : 'absent'));

      await page.fill('#mob-filter', 'rlc');
      await pause(300);
      await page.press('#mob-filter', 'Enter');
      await pause(900);
      const apres = await page.evaluate(() => ({
        hash: location.hash,
        ouvert: document.getElementById('mob-drawer').classList.contains('open'),
        titre: (document.getElementById('mob-chapter-title') || {}).textContent || '',
      }));
      if (!/^#rlc\//.test(apres.hash)) pbTiroir.push('Entrée dans le filtre « rlc » : hash ' + apres.hash + ' au lieu de #rlc/…');
      if (apres.ouvert) pbTiroir.push('le tiroir reste ouvert après la sélection d\'un chapitre');
      if (!/RLC/i.test(apres.titre)) pbTiroir.push('titre mobile inattendu : « ' + apres.titre + ' »');
      await page.evaluate(() => window.scrollTo(0, 0));
      await ctx.capture(page, 'chapitre');
    } catch (e) {
      pbTiroir.push('interaction impossible : ' + String(e.message).split('\n')[0]);
    }
    res.verifier('tiroir : ouverture, matières, filtre, Entrée', !pbTiroir.length, pbTiroir);

    /* ---------- 2b) Bouton retour (Android) : ferme la page Chapitres / la feuille ⋯ ---------- */
    journal.lieu = 'retour Android';
    const pbRetour = [];
    try {
      // Au-dessus de rlc/meth, qui ne déborde pas à 390 px : un panneau qui déborde élargit la zone
      // d'affichage du téléphone, et avec elle les pages plein écran (voir DEBORDEMENTS_CONNUS)
      await naviguer(page, 'rlc', 'meth');
      await pause(300);
      const avant = await page.evaluate(() => location.hash);
      for (const [nom, bouton, page_] of [['page Chapitres', '#mob-menu-btn', 'mob-drawer'], ['feuille ⋯', '#mob-more-btn', 'mob-more-menu']]) {
        await page.tap(bouton);
        await pause(500);
        if (!(await page.evaluate(id => document.getElementById(id).classList.contains('open'), page_))) { pbRetour.push(nom + ' : ne s\'ouvre pas'); continue; }
        await page.goBack();
        await pause(500);
        const s = await page.evaluate(id => ({ ouvert: document.getElementById(id).classList.contains('open'), hash: location.hash }), page_);
        if (s.ouvert) pbRetour.push(nom + ' : le bouton retour ne la ferme pas');
        if (s.hash !== avant) pbRetour.push(nom + ' : le bouton retour a quitté le chapitre (hash ' + s.hash + ' au lieu de ' + avant + ')');
      }
      // fermée par ×, puis retour : on revient bien au chapitre PRÉCÉDENT (l'entrée fictive a été retirée)
      await page.tap('#mob-menu-btn');
      await pause(500);
      await page.tap('#mob-drawer-close');
      await pause(500);
      const s2 = await page.evaluate(() => ({ ouvert: document.getElementById('mob-drawer').classList.contains('open'), hash: location.hash }));
      if (s2.ouvert) pbRetour.push('× ne ferme pas la page Chapitres');
      if (s2.hash !== avant) pbRetour.push('après ×, hash ' + s2.hash + ' au lieu de ' + avant);
    } catch (e) { pbRetour.push('interaction impossible : ' + String(e.message).split('\n').slice(0, 8).join(' | ')); }
    res.verifier('bouton retour (Android) : ferme la page Chapitres et la feuille ⋯ sans quitter le chapitre', !pbRetour.length, pbRetour);

    /* ---------- 3) Thème via la feuille ⋯ du téléphone (segmenté Clair / Sombre / Auto) ---------- */
    journal.lieu = 'thème mobile';
    let th = {}, th2 = {};
    try {
      await naviguer(page, 'rlc', 'meth');   // panneau sans débordement (voir ci-dessus)
      th = await choisirTheme(page, 'dark', true);
      th2 = await choisirTheme(page, 'light', true);
    } catch (e) { th.erreur = String(e.message).split('\n')[0]; }
    res.verifier('thème au téléphone par la feuille ⋯ (sombre puis clair, mémorisé)',
      th.attr === 'dark' && th.store === 'dark' && th2.attr !== 'dark' && th2.store === 'light' && !th2.feuille,
      th.erreur || ('« Sombre » : data-theme = ' + th.attr + ', Store = ' + th.store + ' ; « Clair » : data-theme = ' + th2.attr
        + ', Store = ' + th2.store + (th2.feuille ? ' ; la feuille ⋯ reste ouverte après Échap' : '')));

    /* ---------- 3b) Focus au clavier : feuille ⋯ piégée, fenêtres ouvertes depuis la feuille ----------
       (relecture accessibilité, tour 1) Tab depuis le dernier élément de la feuille y reste ; une
       fenêtre ouverte depuis la feuille rend le focus au bouton ⋯ à sa fermeture (l'élément d'origine
       est dans la feuille refermée : il refuse le focus). */
    journal.lieu = 'focus mobile';
    const pbFocus = [];
    try {
      await naviguer(page, 'rlc', 'meth');
      await page.focus('#mob-more-btn'); await page.keyboard.press('Enter'); await pause(500);
      await page.evaluate(() => {
        const m = document.getElementById('mob-more-menu');
        const f = Array.from(m.querySelectorAll('a[href], button, input, select, [tabindex]'))
          .filter(e => e.tabIndex >= 0 && !e.disabled && e.getClientRects().length && getComputedStyle(e).visibility !== 'hidden');
        if (f.length) f[f.length - 1].focus();
      });
      await page.keyboard.press('Tab'); await pause(80);
      if (!(await page.evaluate(() => document.getElementById('mob-more-menu').contains(document.activeElement)))) pbFocus.push('feuille ⋯ : Tab depuis le dernier élément sort de la feuille');
      await page.keyboard.press('Escape'); await pause(400);
      for (const [nom, bouton, fenetre] of [['Bilan', '#mob-dash-btn', 'dash-overlay'], ['Aujourd\'hui', '#mob-today-btn', 'today-overlay']]) {
        await page.focus('#mob-more-btn'); await page.keyboard.press('Enter'); await pause(500);
        await page.focus(bouton); await page.keyboard.press('Enter'); await pause(700);
        if (!(await page.evaluate(id => document.getElementById(id).classList.contains('open'), fenetre))) { pbFocus.push(nom + ' : la fenêtre ne s\'ouvre pas'); await fermerOverlays(page).catch(() => {}); continue; }
        await page.keyboard.press('Escape'); await pause(500);
        const a = await page.evaluate(() => document.activeElement && document.activeElement !== document.body ? document.activeElement.id || document.activeElement.className : 'BODY');
        if (a !== 'mob-more-btn') pbFocus.push(nom + ' (depuis la feuille ⋯) : focus rendu à ' + a + ' au lieu du bouton ⋯');
      }
    } catch (e) { pbFocus.push('interaction impossible : ' + String(e.message).split('\n')[0]); }
    res.verifier('focus au clavier : feuille ⋯ piégée, retour au bouton ⋯ après une fenêtre ouverte depuis la feuille', !pbFocus.length, pbFocus);

    /* ---------- 3c) Fenêtres de révision plein écran : fond sous TOUT le contenu (relecture téléphone, tour 2)
       Étirée à la hauteur de l'écran, la boîte laissait la suite du Bilan, le bas d'Aujourd'hui ou une
       longue réponse du quiz se dessiner sans fond, sur le chapitre. On fait défiler la fenêtre jusqu'en
       bas : le bas de la boîte ([role=dialog]) doit couvrir le bas de son dernier descendant visible. */
    journal.lieu = 'fenêtres plein écran';
    const pbFen = [];
    try {
      await naviguer(page, 'rlc', 'cours');
      // une longue réponse au quiz : toutes les cartes d'ecr dues
      await page.evaluate(() => { const c = FLASH_REGISTRY.ecr; if (c) flashSaveState('ecr', c, c.map(() => ({ h: 1, o: 0, e: 0, last: 0, box: 0, due: Date.now() - 86400000 }))); if (window.__updateReviseBadge) __updateReviseBadge(); });
      for (const [nom, id, ouvrir] of [
        ['Aujourd\'hui', 'today-overlay', () => window.todayOpen()],
        ['Bilan', 'dash-overlay', () => document.getElementById('mob-dash-btn').click()],
        ['quiz (carte longue)', 'quiz-overlay', () => { window.quizStartDue('ecr'); }],
      ]) {
        await page.evaluate(ouvrir); await pause(900);
        if (id === 'quiz-overlay') { await page.evaluate(() => window.quizReveal()); await pause(500); }
        const r = await page.evaluate(id => {
          const ov = document.getElementById(id);
          if (!ov || !ov.classList.contains('open')) return { err: 'fenêtre non ouverte' };
          ov.scrollTop = ov.scrollHeight;
          const box = ov.querySelector('[role="dialog"]') || ov.firstElementChild;
          const b = box.getBoundingClientRect();
          const bas = Math.max(...Array.from(box.querySelectorAll('*')).filter(x => x.getClientRects().length && getComputedStyle(x).visibility !== 'hidden').map(x => x.getBoundingClientRect().bottom));
          return { boite: Math.round(b.bottom), contenu: Math.round(bas), vh: innerHeight };
        }, id);
        if (r.err) pbFen.push(nom + ' : ' + r.err);
        else if (r.contenu > r.boite + 1) pbFen.push(nom + ' : contenu jusqu\'à ' + r.contenu + ' px, fond de la boîte jusqu\'à ' + r.boite + ' px (le reste se dessine sans fond)');
        if (id === 'quiz-overlay' && !r.err) {
          const n = await page.evaluate(() => { const c = document.getElementById('quiz-actions-rate'); return c && c.getClientRects().length ? Math.round(c.getBoundingClientRect().bottom) : null; });
          if (n === null || n > r.vh) pbFen.push('quiz (carte longue) : notation ' + (n === null ? 'absente' : 'sous le pli (' + n + ' px pour ' + r.vh + ')'));
        }
        await fermerOverlays(page).catch(() => {}); await pause(300);
      }
    } catch (e) { pbFen.push('interaction impossible : ' + String(e.message).split('\n')[0]); }
    res.verifier('fenêtres plein écran (Aujourd\'hui, Bilan, quiz à longue réponse) : fond sous tout le contenu, notation du quiz visible', !pbFen.length, pbFen);

    /* ---------- 3d) Changement d'onglet depuis le bas d'un panneau (onglets collés) ---------- */
    journal.lieu = 'onglet depuis le bas';
    const pbOng = [];
    try {
      await naviguer(page, 'rlc', 'cours');
      await page.evaluate(() => { document.documentElement.style.scrollBehavior = 'auto'; window.scrollTo(0, Math.round((document.documentElement.scrollHeight - innerHeight) * 0.7)); });
      await pause(400);
      await page.locator('#chap-rlc .tab[data-panel="rlc-flash"]').tap(); await pause(900);
      const r = await page.evaluate(() => {
        const c = document.querySelector('#rlc-flash .flash-card').getBoundingClientRect();
        const t = document.querySelector('#chap-rlc > nav.tabs').getBoundingClientRect();
        return { haut: Math.round(c.top), bas: Math.round(c.bottom), onglets: Math.round(t.bottom), vh: innerHeight };
      });
      if (r.haut < r.onglets - 1 || r.bas > r.vh) pbOng.push('Cours (fond) → Cartes : fiche [' + r.haut + ', ' + r.bas + '] pour des onglets finissant à ' + r.onglets + ' et un écran de ' + r.vh + ' px');
      await page.locator('#chap-rlc .tab[data-panel="rlc-exos"]').tap(); await pause(900);
      const e = await page.evaluate(() => { const x = document.querySelector('#rlc-exos .exo'); const t = document.querySelector('#chap-rlc > nav.tabs').getBoundingClientRect(); return { haut: Math.round(x.getBoundingClientRect().top), onglets: Math.round(t.bottom), vh: innerHeight }; });
      if (e.haut < e.onglets - 1 || e.haut > e.vh) pbOng.push('Cartes → Exercices : 1er exercice à ' + e.haut + ' px (onglets jusqu\'à ' + e.onglets + ')');
      await page.evaluate(() => window.scrollTo(0, 0));
    } catch (e) { pbOng.push('interaction impossible : ' + String(e.message).split('\n')[0]); }
    res.verifier('changement d\'onglet depuis le bas d\'un panneau : le nouveau panneau commence sous les onglets (fiche entière)', !pbOng.length, pbOng);

    /* ---------- 3e) Zone défilante à fondu : anneau de focus visible (masque retiré) ---------- */
    journal.lieu = 'focus des zones défilantes';
    let pbAnneau = [];
    try {
      await naviguer(page, 'rlc', 'cours'); await pause(800);
      const r = await page.evaluate(() => {
        const e = Array.from(document.querySelectorAll('#rlc-cours mjx-container.a-defiler')).find(x => x.classList.contains('suite-d') || x.classList.contains('suite-g'));
        if (!e) return { err: 'aucune formule défilante à fondu dans rlc-cours' };
        document.documentElement.style.scrollBehavior = 'auto';
        e.scrollIntoView({ block: 'center' });
        e.setAttribute('data-test-anneau', '1');
        return {};
      });
      if (r.err) pbAnneau.push(r.err);
      else {
        // focus CLAVIER (Maj+Tab puis Tab, comme un élève) pour obtenir :focus-visible
        await page.focus('[data-test-anneau]'); await page.keyboard.press('Shift+Tab'); await page.keyboard.press('Tab'); await pause(150);
        const m = await page.evaluate(() => { const a = document.activeElement; return { cible: a && a.hasAttribute('data-test-anneau'), fv: a && a.matches(':focus-visible'), masque: a ? getComputedStyle(a).maskImage || getComputedStyle(a).webkitMaskImage : '' }; });
        if (!m.cible) pbAnneau.push('la formule défilante ne reçoit pas le focus au clavier');
        else if (m.fv && m.masque && m.masque !== 'none') pbAnneau.push('formule défilante focalisée : le masque du fondu reste posé (« ' + String(m.masque).slice(0, 40) + ' ») et efface l\'anneau');
      }
    } catch (e) { pbAnneau.push('interaction impossible : ' + String(e.message).split('\n')[0]); }
    res.verifier('zone défilante à fondu focalisée au clavier : masque retiré, anneau visible', !pbAnneau.length, pbAnneau);

    /* ---------- 4) Débordement horizontal de chaque panneau ---------- */
    const tous = await page.evaluate(() => CHAPTERS.map(c => ({ id: c.id, prefix: c.prefix, matiere: c.matiere,
      onglets: Array.from(document.querySelectorAll('#chap-' + c.id + ' .tab')).map(t => t.dataset.panel) })));
    const selection = ctx.selectionner(tous);
    ctx.log('balayage de ' + selection.length + ' chapitre(s) × onglets à ' + LARGEUR + ' px');
    const deborde = {};        // pid → { largeur, coupables }
    const erreursNav = [];
    for (let i = 0; i < selection.length; i++) {
      const c = selection[i];
      const avant = Object.keys(deborde).length + erreursNav.length;
      try {
        journal.lieu = 'mobile ' + c.id;
        await naviguer(page, c.id, null);
        for (const pid of c.onglets) {
          journal.lieu = 'mobile ' + pid;
          await page.evaluate(pid => { const t = document.querySelector('.tab[data-panel="' + pid + '"]'); if (t) t.click(); }, pid);
          await pause(pid.endsWith('-simu') ? 250 : 60);
          await etatMathJax(page, pid, 2000);   // les formules rendues changent la largeur
          const m = await page.evaluate(pid => {
            const W = document.documentElement.clientWidth;
            const sw = document.documentElement.scrollWidth;
            if (sw <= W + 2) return { sw, W };
            // Coupables : éléments du panneau qui dépassent à droite (le plus profond)
            const panneau = document.getElementById(pid);
            const coupables = [];
            if (panneau) panneau.querySelectorAll('*').forEach(e => {
              if (e.offsetParent === null || coupables.length >= 3) return;
              const r = e.getBoundingClientRect();
              if (r.right <= W + 2 || e.parentElement.getBoundingClientRect().right > W + 2) return;
              let tex = null;
              const mc = e.closest('mjx-container');
              if (mc && window.MathJax && MathJax.startup && MathJax.startup.document) {
                try { const it = MathJax.startup.document.getMathItemsWithin(mc.parentElement).find(x => x.typesetRoot === mc); tex = it ? it.math : null; } catch (x) { /* ignoré */ }
              }
              const k = (tex ? 'formule ' + tex : e.tagName.toLowerCase() + ' « ' + (e.textContent || '').trim() + ' »').slice(0, 110);
              if (!coupables.includes(k)) coupables.push(k);
            });
            return { sw, W, coupables };
          }, pid);
          if (m.sw > m.W + 2) deborde[pid] = { largeur: m.sw, coupables: m.coupables || [] };
        }
      } catch (e) {
        erreursNav.push(c.id + ' : ' + String(e.message).split('\n')[0]);
      }
      ctx.progression(i, selection.length, Object.keys(deborde).length + erreursNav.length > avant);
    }
    const visites = new Set(selection.flatMap(c => c.onglets));
    const nouveaux = Object.keys(deborde).filter(pid => !DEBORDEMENTS_CONNUS[pid]);
    const aggraves = Object.keys(deborde).filter(pid => DEBORDEMENTS_CONNUS[pid] && deborde[pid].largeur > DEBORDEMENTS_CONNUS[pid].largeur + MARGE);
    const resolus = Object.keys(DEBORDEMENTS_CONNUS).filter(pid => visites.has(pid) && !deborde[pid]);
    res.info('debordements', deborde);
    res.info('debordementsConnusToujoursPresents', Object.keys(deborde).filter(pid => DEBORDEMENTS_CONNUS[pid]));
    res.verifier('aucun NOUVEAU débordement horizontal à ' + LARGEUR + ' px (' + visites.size + ' panneaux, '
      + Object.keys(deborde).length + ' débordent dont ' + (Object.keys(deborde).length - nouveaux.length) + ' connus)',
      !nouveaux.length && !aggraves.length && !erreursNav.length,
      nouveaux.map(pid => pid + ' : largeur de page ' + deborde[pid].largeur + ' px > ' + LARGEUR
        + (deborde[pid].coupables.length ? ' — ' + deborde[pid].coupables.join(' ; ') : ''))
        .concat(aggraves.map(pid => pid + ' : débordement connu AGGRAVÉ, ' + DEBORDEMENTS_CONNUS[pid].largeur + ' → ' + deborde[pid].largeur
          + ' px' + (deborde[pid].coupables.length ? ' — ' + deborde[pid].coupables.join(' ; ') : '')))
        .concat(erreursNav));
    resolus.forEach(pid => res.avertir('le panneau ' + pid + ' ne déborde plus : le retirer de DEBORDEMENTS_CONNUS (tests/suites/mobile.js)'));

    /* ---------- 5) Erreurs JavaScript ---------- */
    const js = journal.erreurs.map(e => '[' + e.lieu + '] ' + e.type + ' : ' + e.texte);
    res.verifier('aucune erreur console ni exception JavaScript (mobile)', !js.length, js);
    res.verifier('aucune requête externe (mobile)', !journal.externes.length, journal.externes.map(e => '[' + e.lieu + '] ' + e.url));
  },
};
