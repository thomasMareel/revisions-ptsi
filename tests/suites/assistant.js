'use strict';
/* ============================================================
   Suite « assistant » — assistant IA, phase 0 (docs/assistant-ia.md)
   ============================================================
   - Hors activation : aucun bouton, module non chargé ; activation par
     ?assistant=1 (paramètre retiré de l'adresse), retrait par ?assistant=0.
   - Collecte du contexte (window.__contexteAssistant, schéma 1) sur les
     chapitres × onglets : chapitre, matière, onglet, section (Cours, Méthodes),
     exercice, carte, simulateur ; contenu du chapitre (formules en TeX, aucun
     reste de MathJax).
   - Section suivie au défilement ; sélection avec formule relue en TeX.
   - Vidéo lancée : instant de lecture, partie, scène et phrase (timeline.json).
   - Panneau : touche « a », focus, Échap et focus rendu, colonne de lecture
     décalée et rail masqué (≥ 1 200 px), fiche de modification ; téléphone :
     feuille ⋯ → page plein écran modale, refermée par le bouton retour.
   - Aucune requête externe (hors lecteur YouTube, au clic), aucune erreur JS ;
     hors connexion avant chargement : message, pas d'erreur. */
const { pause, attendreApp, fermerOverlays, naviguer, problemesJournal, marqueJournal } = require('../lib/outils');

module.exports = {
  nom: 'assistant',
  description: 'assistant IA (phase 0) : activation, collecte du contexte, panneau, téléphone',
  delaiMax: o => (o.rapide || o.chapitres ? 6 : 25) * 60000,

  async executer(ctx, res) {
    const charger = async (page, hash, params) => {
      await page.goto(ctx.url(hash, params), { waitUntil: 'load', timeout: 60000 });
      await attendreApp(page);
      await fermerOverlays(page);
    };

    /* ---------- 1. Activation par appareil ---------- */
    {
      const { page, journal } = await ctx.nouvellePage();
      const scripts = [];
      page.on('request', r => { if (/assistant\/assistant\.js/.test(r.url())) scripts.push(r.url()); });
      await charger(page, '#rlc/cours');
      const avant = await page.evaluate(() => ({
        visible: !!document.getElementById('assistant-btn').getClientRects().length,
        module: !!window.__assistant, amorce: typeof window.__ouvrirAssistant === 'function',
      }));
      res.verifier('hors activation : bouton absent, module non chargé, amorce présente',
        !avant.visible && !avant.module && avant.amorce && !scripts.length, JSON.stringify(avant) + ' ; scripts : ' + scripts.join(', '));
      await charger(page, '#rlc/cours', { assistant: '1' });
      const actif = await page.evaluate(() => ({ url: location.href, store: Store.get('assistant'),
        visible: !!document.getElementById('assistant-btn').getClientRects().length }));
      res.verifier('?assistant=1 : bouton visible, clé « assistant », paramètre retiré de l\'adresse',
        actif.visible && actif.store === '1' && !/assistant=/.test(actif.url) && /#rlc\/cours$/.test(actif.url), JSON.stringify(actif));
      await charger(page, '#rlc/cours', { assistant: '0' });
      const inactif = await page.evaluate(() => ({ store: Store.get('assistant'), visible: !!document.getElementById('assistant-btn').getClientRects().length }));
      res.verifier('?assistant=0 : bouton retiré', !inactif.visible && inactif.store === '0', JSON.stringify(inactif));
      const pb = problemesJournal(journal);
      res.verifier('activation : aucune erreur, aucune requête externe', !pb.length, pb);
    }

    /* ---------- 2. Collecte du contexte sur les chapitres × onglets ---------- */
    {
      const { page, journal } = await ctx.nouvellePage();
      await charger(page, '#rlc/cours', { assistant: '1' });
      await page.evaluate(() => window.__chargerAssistant());
      const tous = await page.evaluate(() => CHAPTERS.map(c => ({ id: c.id, prefix: c.prefix, matiere: c.matiere, panels: c.panels })));
      const chapitres = ctx.selectionner(tous);
      const pbs = [];
      let nOnglets = 0;
      for (let i = 0; i < chapitres.length; i++) {
        const c = chapitres[i];
        const avant = pbs.length;
        for (const onglet of c.panels) {
          nOnglets++;
          await page.evaluate(h => { location.hash = h; }, '#' + c.id + '/' + onglet);
          await pause(320);
          const x = await page.evaluate(([onglet, avecContenu]) => {
            const r = window.__contexteAssistant({ contenu: avecContenu });
            const pan = document.getElementById(CHAPTERS_BY_ID[r.chapitre ? r.chapitre.id : ''] ? CHAPTERS_BY_ID[r.chapitre.id].prefix + '-' + onglet : '');
            return {
              schema: r.schema, page: r.page, chap: r.chapitre && r.chapitre.id, mat: r.matiere && r.matiere.code, onglet: r.onglet,
              section: !!r.section, aSections: !!(pan && Array.from(pan.querySelectorAll('.sec-num')).some(s => !s.closest('.exo'))),
              exo: !!(r.exercice && r.exercice.num), aExos: !!(pan && pan.querySelector('.exo:not(.filtre-masque)')),
              carte: !!(r.carte && r.carte.question), aCarte: !!(pan && pan.querySelector('.flash-side')),
              simu: !!(r.simulateur && r.simulateur.titre), aSimu: !!(pan && pan.querySelector('.sim-wrapper')),
              contenu: r.contenu ? { signes: r.contenu.signes, mjx: /mjx-|\[object /.test(r.contenu.texte), emp: /^fnv1a:[0-9a-f]{8}$/.test(r.contenu.empreinte) } : null,
            };
          }, [onglet, onglet === c.panels[0]]);
          const ici = c.id + '/' + onglet;
          if (x.schema !== 1 || x.page !== 'chapitre' || x.chap !== c.id || x.mat !== c.matiere || x.onglet !== onglet) {
            pbs.push(ici + ' : contexte ' + JSON.stringify({ schema: x.schema, page: x.page, chap: x.chap, mat: x.mat, onglet: x.onglet }));
            continue;
          }
          if ((onglet === 'cours' || onglet === 'meth') && x.aSections && !x.section) pbs.push(ici + ' : section courante absente');
          if (onglet === 'exos' && x.aExos && !x.exo) pbs.push(ici + ' : exercice courant absent');
          if (onglet === 'flash' && x.aCarte && !x.carte) pbs.push(ici + ' : carte affichée absente');
          if (onglet === 'simu' && x.aSimu && !x.simu) pbs.push(ici + ' : simulateur absent');
          if (x.contenu && (x.contenu.signes < 200 || x.contenu.mjx || !x.contenu.emp)) pbs.push(ici + ' : contenu ' + JSON.stringify(x.contenu));
        }
        ctx.progression(i, chapitres.length, pbs.length > avant);
      }
      res.verifier('contexte complet sur ' + chapitres.length + ' chapitre(s), ' + nOnglets + ' onglet(s)', !pbs.length, pbs);

      // Section suivie au défilement, sélection avec formule
      await page.evaluate(() => { location.hash = '#maxwell/cours'; });
      await pause(1200);
      const s = await page.evaluate(() => {
        const secs = Array.from(document.querySelectorAll('#mxw-cours .course-section')).filter(x => /^§\s*3\b/.test((x.querySelector('.sec-num') || {}).textContent || ''));
        const sec = secs[0];
        window.scrollTo({ top: sec.getBoundingClientRect().top + scrollY - 120, behavior: 'instant' });
        return !!sec;
      });
      await pause(400);
      const sel = await page.evaluate(() => {
        const r0 = window.__contexteAssistant().section;
        const p = Array.from(document.querySelectorAll('#mxw-cours .course-section p')).find(x => x.querySelector('mjx-container') && x.textContent.length > 60);
        const r = document.createRange(); r.selectNodeContents(p);
        const g = getSelection(); g.removeAllRanges(); g.addRange(r);
        const c = window.__contexteAssistant({ selection: { range: r, t: Date.now() } });
        g.removeAllRanges();
        return { section: r0, texte: c.selection && c.selection.texte };
      });
      res.verifier('section suivie au défilement (§3 de maxwell)', s && sel.section && sel.section.num === '§3', JSON.stringify(sel.section));
      res.verifier('sélection avec formule relue en TeX', !!sel.texte && /\\\(.+\\\)/.test(sel.texte) && !/mjx/.test(sel.texte), String(sel.texte).slice(0, 200));
      const pb = problemesJournal(journal);
      res.verifier('collecte : aucune erreur, aucune requête externe', !pb.length, pb);
    }

    /* ---------- 3. Vidéo : instant, partie, scène, phrase ---------- */
    {
      const { page, journal } = await ctx.nouvellePage();
      await charger(page, '#maxwell/video', { assistant: '1' });
      await page.evaluate(() => window.__chargerAssistant());
      await pause(400);
      const saut = await page.evaluate(() => {
        const b = Array.from(document.querySelectorAll('#mxw-video .vid-saut')).find(x => +x.getAttribute('data-t') > 60);
        if (!b) return null;
        b.click();
        return +b.getAttribute('data-t');
      });
      await pause(400);
      await page.evaluate(() => window.__contexteAssistant());   // lance le chargement du timeline.json
      await pause(800);
      const { v, src } = await page.evaluate(() => ({ v: window.__contexteAssistant().video, src: (document.querySelector('#mxw-video iframe') || {}).src || '' }));
      const ok = v && saut != null && v.t >= saut && v.t < saut + 15 && v.partie && v.scene && v.scene.id && v.phrase && v.phrase.ecrit
        && v.src === 'video/em/ch3' && /enablejsapi=1/.test(src);
      res.verifier('vidéo lancée : instant, partie, scène et phrase du timeline.json', ok, JSON.stringify(v));
      const exc = journal.erreurs.filter(e => e.type === 'exception');
      res.verifier('vidéo : aucune exception', !exc.length, exc.map(e => e.texte));
    }

    /* ---------- 4. Panneau (ordinateur) ---------- */
    {
      const { page, journal } = await ctx.nouvellePage({ largeur: 1440, hauteur: 900 });
      await charger(page, '#rlc/cours', { assistant: '1' });
      const m0 = marqueJournal(journal);
      await page.focus('#search-btn');
      await page.keyboard.press('a');
      await page.waitForSelector('#assistant-panel.open', { timeout: 5000 }).catch(() => {});
      await pause(400);
      const o = await page.evaluate(() => ({
        ouvert: document.getElementById('assistant-panel').classList.contains('open'),
        focus: document.activeElement && document.activeElement.id,
        expanded: document.getElementById('assistant-btn').getAttribute('aria-expanded'),
        decalage: parseFloat(getComputedStyle(document.getElementById('app-main')).paddingRight) || 0,
        rail: getComputedStyle(document.getElementById('chap-rail')).display,
        chap: document.querySelector('#assistant-panel .assist-chap').textContent,
      }));
      res.verifier('touche « a » : panneau ouvert, focus dans le champ, aria-expanded', o.ouvert && o.focus === 'assistant-question' && o.expanded === 'true', JSON.stringify(o));
      res.verifier('panneau à 1 440 px : colonne de lecture décalée, rail masqué, chapitre affiché', o.decalage >= 300 && o.rail === 'none' && /RLC/.test(o.chap), JSON.stringify(o));
      await page.click('#assistant-panel [data-mode="modif"]');
      await page.fill('#assistant-question', 'Corrige la démonstration du §1.');
      await page.press('#assistant-question', 'Enter');
      await pause(500);
      const f = await page.evaluate(() => { const p = document.querySelectorAll('#assistant-panel .assist-msg.note pre'); return p.length ? p[p.length - 1].textContent : ''; });
      res.verifier('mode Modification : fiche de demande (demande, chapitre, panneau, consignes)',
        /Corrige la démonstration du §1\./.test(f) && /`rlc`/.test(f) && /`rlc-cours`/.test(f) && /CLAUDE\.md/.test(f), f.slice(0, 300));
      await page.keyboard.press('Escape');
      await pause(300);
      const fe = await page.evaluate(() => ({ ouvert: document.getElementById('assistant-panel').classList.contains('open'),
        focus: document.activeElement && document.activeElement.id, decalage: parseFloat(getComputedStyle(document.getElementById('app-main')).paddingRight) || 0 }));
      res.verifier('Échap : panneau fermé, focus rendu au bouton, colonne rétablie', !fe.ouvert && fe.focus === 'assistant-btn' && fe.decalage < 300, JSON.stringify(fe));
      const pb = problemesJournal(journal, m0);
      res.verifier('panneau : aucune erreur, aucune requête externe', !pb.length, pb);
    }

    /* ---------- 5. Téléphone : feuille ⋯ → page plein écran, retour Android ---------- */
    {
      const { page, journal } = await ctx.nouvellePage({ mobile: true });
      await charger(page, '#rlc/cours');
      await charger(page, '#rlc/cours', { assistant: '1' });
      await page.click('#mob-more-btn');
      await pause(500);
      await page.click('#mob-assistant-btn');
      await page.waitForSelector('#assistant-panel.open', { timeout: 5000 }).catch(() => {});
      await pause(400);
      const t = await page.evaluate(() => {
        const p = document.getElementById('assistant-panel'), r = p.getBoundingClientRect();
        return { ouvert: p.classList.contains('open'), modal: p.getAttribute('aria-modal'), feuille: document.getElementById('mob-more-menu').classList.contains('open'),
          plein: r.left === 0 && r.top === 0 && Math.round(r.width) === innerWidth, debordement: document.documentElement.scrollWidth > innerWidth };
      });
      res.verifier('téléphone : page plein écran modale, feuille ⋯ refermée', t.ouvert && t.modal === 'true' && !t.feuille && t.plein && !t.debordement, JSON.stringify(t));
      await page.goBack();
      await pause(700);
      const r = await page.evaluate(() => ({ ouvert: document.getElementById('assistant-panel').classList.contains('open'), hash: location.hash }));
      res.verifier('téléphone : le bouton retour referme le panneau sans quitter le chapitre', !r.ouvert && r.hash === '#rlc/cours', JSON.stringify(r));
      const pb = problemesJournal(journal);
      res.verifier('téléphone : aucune erreur, aucune requête externe', !pb.length, pb);
    }

    /* ---------- 6. Hors connexion avant le premier chargement ---------- */
    {
      const { contexte, page, journal } = await ctx.nouvellePage();
      await charger(page, '#rlc/cours', { assistant: '1' });
      await contexte.setOffline(true);
      await page.evaluate(() => window.__ouvrirAssistant());
      await pause(900);
      const h = await page.evaluate(() => ({ ouvert: document.getElementById('assistant-panel').classList.contains('open'),
        toast: Array.from(document.querySelectorAll('.toasts *')).map(e => e.textContent).join(' ') }));
      await contexte.setOffline(false);
      res.verifier('hors connexion : message clair, aucune exception', !h.ouvert && /connexion|charger/i.test(h.toast)
        && !journal.erreurs.some(e => e.type === 'exception'), JSON.stringify(h));
    }
  },
};
