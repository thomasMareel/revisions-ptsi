'use strict';
/* ============================================================
   Suite « mobile » — téléphone 390×844 (tactile)
   ============================================================
   - en-tête mobile visible, sommaire masqué, écran « Aujourd'hui » au lancement ;
   - tiroir des chapitres : ouverture, changement de matière, filtre
     (résultats, aucun résultat, Entrée = 1er résultat) ;
   - débordement horizontal (scrollWidth > largeur d'écran) de CHAQUE panneau.
     Des panneaux débordent déjà (formules en ligne trop longues, voir
     tests/README.md §5) : ils sont listés dans DEBORDEMENTS_CONNUS. La suite n'échoue que
     pour un NOUVEAU débordement, et signale un panneau connu qui ne déborde plus. */
const { pause, attendreApp, fermerOverlays, naviguer, etatMathJax } = require('../lib/outils');

/* Panneaux qui débordent à 390 px au commit a04c445 (mesurés avec cette suite,
   Chromium 141) : largeur de page mesurée (px) et formule en cause. Un panneau
   connu fait quand même échouer si sa largeur augmente de plus de MARGE px
   (nouvelle formule plus large). Quand un débordement est corrigé, la suite
   affiche un avertissement : retirer alors la ligne correspondante. */
const DEBORDEMENTS_CONNUS = {
  'rlc-cours': { largeur: 415, formule: '\\dot{u}_C(0) = 0 \\Rightarrow -A/\\tau + B\\omega = 0 …' },
  'sig-meth': { largeur: 413, formule: 's(t) = \\sum_n |H(jn\\omega_0)|\\,E_n\\cos(…)' },
  'mp-exos': { largeur: 399, formule: 'N(\\theta) = \\dfrac{mv^2}{R} - mg\\cos\\theta = …' },
  'cpx-meth': { largeur: 668, formule: '\\cos^3\\theta = \\big(\\dfrac{e^{i\\theta}+e^{-i\\theta}}{2}\\big)^3 = …' },
  'pol-cours': { largeur: 506, formule: 'P = X^n - s_1 X^{n-1} + … = \\prod_{i=1}^n (X - r_i)' },
  'suit-meth': { largeur: 486, formule: '\\sqrt{n^2+n} - n = \\dfrac{…}{…}' },
  'cd-cours': { largeur: 405, formule: '\\forall \\varepsilon > 0,\\;\\exists \\eta > 0 …' },
  'dl-meth': { largeur: 613, formule: '\\dfrac{1}{1 + u} = 1 - u + u^2 + o(u^2) = …' },
  'asy-meth': { largeur: 515, formule: 'e^{\\sin x} = 1 + x + x^2/2 - … + o(x^3)' },
  'prim-meth': { largeur: 450, formule: '\\int \\dfrac{2\\,du}{4u^2 + 4} = …' },
  'va-cours': { largeur: 444, formule: '\\mathrm{Cov}(X,Y) = E(XY) - E(X)E(Y) = …' },
  'ensi-meth': { largeur: 400, formule: 'J_{eq,\\text{ramené}} = J_{moteur} + …' },
  's1-cours': { largeur: 405, formule: '-20\\ \\text{dB/décade}' },
  'repn-cours': { largeur: 607, formule: '2^0=1,\\ 2^1=2,\\ … 2^{10}=1024' },
};

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
    res.verifier("écran « Aujourd'hui » affiché au lancement", lancement.aujourdhui, '#today-overlay non ouvert au lancement (sans #hash)');
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

    /* ---------- 3) Thème via le bouton mobile ---------- */
    journal.lieu = 'thème mobile';
    await page.tap('#mob-theme-btn');
    await pause(300);
    const th = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
    await page.tap('#mob-theme-btn');
    await pause(200);
    const th2 = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
    res.verifier('bouton thème mobile (sombre puis clair)', th === 'dark' && th2 !== 'dark', 'data-theme après 1 clic = ' + th + ', après 2 clics = ' + th2);

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
