'use strict';
/* ============================================================
   Suite « site » — chargement bureau, chapitres, MathJax, simulateurs
   ============================================================
   - chargement sans erreur console / exception, AUCUNE requête externe ;
   - CHAPTERS cohérent avec le DOM (chapitres, onglets, panneaux, drawFn, decks) ;
   - chaque chapitre × chacun de ses onglets : panneau affiché, 0 mjx-merror,
     aucun délimiteur TeX resté en clair, flashcards injectées ;
   - flashcards : flashPretty + MathJax sur toutes les cartes (0 erreur) ;
   - tous les simulateurs (drawFn) exécutés, canvas peints en clair ET sombre
     (en --rapide : un seul thème). */
const { pause, attendreApp, fermerOverlays, naviguer, etatMathJax, problemesJournal } = require('../lib/outils');

/* Anomalies CONNUES (déjà recensées, à corriger avec l'accord de l'utilisateur) :
   elles ne font pas échouer la suite. Si l'une disparaît, un avertissement
   demande de la retirer de la liste. */
const TEX_EN_CLAIR_CONNUS = {
  // panneau : textes restés en clair tolérés (tout AUTRE reste dans ce panneau fait échouer)
  'stab-exos': { motif: /Tableau de Routh\s*:\s*\\\[|^\\\]$/, raison: 'tableau de Routh écrit en \\[ … \\] au lieu de $$ … $$' },
};
const ONGLETS_HORS_CHAPTERS_CONNUS = {
  'lor-simu': 'simulateur de Lorentz (SVG) non déclaré dans CHAPTERS.panels',
};

module.exports = {
  nom: 'site',
  description: 'chargement, chapitres × onglets, MathJax, flashcards, simulateurs',
  delaiMax: o => (o.rapide ? 10 : 40) * 60000,

  async executer(ctx, res) {
    const { page, journal } = await ctx.nouvellePage();

    /* ---------- 1) Chargement ---------- */
    journal.lieu = 'chargement';
    const t0 = Date.now();
    await page.goto(ctx.url(), { waitUntil: 'load', timeout: 60000 });
    await attendreApp(page);
    res.info('chargementMs', Date.now() - t0);
    ctx.log('chargement + initialisation : ' + (Date.now() - t0) + ' ms');
    await ctx.capture(page, 'accueil');
    await fermerOverlays(page);

    /* ---------- 2) Cohérence CHAPTERS ↔ DOM ---------- */
    const inv = await page.evaluate(() => {
      const chapitres = CHAPTERS.map(c => ({
        id: c.id, prefix: c.prefix, matiere: c.matiere, panels: c.panels.slice(), drawFn: c.drawFn || null,
        onglets: Array.from(document.querySelectorAll('#chap-' + c.id + ' .tab')).map(t => t.dataset.panel),
      }));
      const pb = [];
      for (const c of chapitres) {
        if (!document.getElementById('chap-' + c.id)) pb.push('div #chap-' + c.id + ' absente');
        if (!document.querySelector('.chap-btn[data-chap="' + c.id + '"]')) pb.push('bouton .chap-btn[data-chap=' + c.id + '] absent');
        for (const p of c.panels) {
          const pid = c.prefix + '-' + p;
          if (!document.getElementById(pid)) pb.push('panneau #' + pid + ' absent');
          if (!c.onglets.includes(pid)) pb.push('onglet .tab[data-panel=' + pid + '] absent');
        }
      }
      return {
        chapitres, pb,
        nbDiv: document.querySelectorAll('.chapter').length,
        drawFnManquants: chapitres.filter(c => c.drawFn && typeof window[c.drawFn] !== 'function').map(c => c.id + ' → ' + c.drawFn),
        simuSansDrawFn: chapitres.filter(c => c.panels.includes('simu') && !c.drawFn).map(c => c.id),
        decksManquants: chapitres.filter(c => c.panels.includes('flash') &&
          !(window.FLASH_REGISTRY && Array.isArray(FLASH_REGISTRY[c.prefix]) && FLASH_REGISTRY[c.prefix].length)).map(c => c.prefix),
        parMatiere: chapitres.reduce((a, c) => (a[c.matiere] = (a[c.matiere] || 0) + 1, a), {}),
      };
    });
    const tous = inv.chapitres;
    res.info('chapitres', tous.length);
    res.info('parMatiere', inv.parMatiere);
    ctx.log(tous.length + ' chapitres : ' + Object.entries(inv.parMatiere).map(([k, v]) => k + ' ' + v).join(', ')
      + ' · ' + tous.filter(c => c.drawFn).length + ' simulateurs');
    if (inv.nbDiv !== tous.length) inv.pb.unshift(inv.nbDiv + ' div.chapter dans le DOM pour ' + tous.length + ' entrées CHAPTERS');
    res.verifier('CHAPTERS cohérent avec le DOM (chapitres, onglets, panneaux)', !inv.pb.length, inv.pb);
    res.verifier('drawFn déclarés et existants', !inv.drawFnManquants.length && !inv.simuSansDrawFn.length,
      inv.drawFnManquants.map(x => 'fonction absente : ' + x).concat(inv.simuSansDrawFn.map(x => 'panneau simu sans drawFn : ' + x)));
    res.verifier('flashcards câblées (un deck makeFlash par chapitre avec « flash »)', !inv.decksManquants.length,
      inv.decksManquants.map(p => 'deck absent ou vide : ' + p));

    /* ---------- 3) Chaque chapitre × chacun de ses onglets ---------- */
    const selection = ctx.selectionner(tous);
    ctx.log('parcours de ' + selection.length + ' chapitre(s) × onglets');
    const pbChap = [];
    const texConnusVus = new Set(), ongletsConnusVus = new Set();
    let nbPanneaux = 0;
    for (let i = 0; i < selection.length; i++) {
      const c = selection[i];
      const avant = pbChap.length;
      const nbErr = journal.erreurs.length;
      try {
        journal.lieu = c.id + '/cours';
        await naviguer(page, c.id, c.panels.includes('cours') ? 'cours' : c.panels[0]);
        const nav = await page.evaluate(id => {
          const ch = document.getElementById('chap-' + id);
          return { actif: !!(ch && ch.classList.contains('active')), visible: !!(ch && ch.offsetParent !== null), hash: location.hash };
        }, c.id);
        if (!nav.actif || !nav.visible) pbChap.push(c.id + ' : chapitre non actif / non visible après navigateTo');
        if (!nav.hash.startsWith('#' + c.id + '/')) pbChap.push(c.id + ' : hash inattendu après navigation (' + nav.hash + ')');

        // Onglets hors CHAPTERS.panels
        for (const pid of c.onglets) {
          if (c.panels.includes(pid.slice(c.prefix.length + 1)) && pid.startsWith(c.prefix + '-')) continue;
          if (ONGLETS_HORS_CHAPTERS_CONNUS[pid]) ongletsConnusVus.add(pid);
          else pbChap.push(c.id + ' : onglet ' + pid + ' présent dans le DOM mais absent de CHAPTERS.panels');
        }

        for (const pid of c.onglets) {
          const suffixe = pid.split('-').pop();
          journal.lieu = c.id + '/' + suffixe;
          nbPanneaux++;
          const clic = await page.evaluate(pid => {
            const t = document.querySelector('.tab[data-panel="' + pid + '"]');
            if (!t) return false;
            t.click();
            return true;
          }, pid);
          if (!clic) { pbChap.push(pid + ' : onglet introuvable'); continue; }
          await pause(suffixe === 'simu' ? 300 : 80);
          const e = await etatMathJax(page, pid, 2500);
          if (!e) { pbChap.push(pid + ' : panneau introuvable'); continue; }
          const actif = await page.evaluate(pid => {
            const p = document.getElementById(pid);
            return !!(p && p.classList.contains('active') && p.offsetParent !== null);
          }, pid);
          if (!actif) pbChap.push(pid + ' : panneau non affiché après clic sur son onglet');
          if (e.merror.length) pbChap.push(pid + ' : ' + e.merror.length + ' erreur(s) MathJax (mjx-merror) : ' + e.merror.slice(0, 2).join(' | '));
          const connu = TEX_EN_CLAIR_CONNUS[pid];
          const restes = connu ? e.restes.filter(r => !connu.motif.test(r)) : e.restes;
          if (connu && restes.length < e.restes.length) texConnusVus.add(pid);
          if (restes.length) pbChap.push(pid + ' : délimiteur TeX resté en clair : « ' + restes.slice(0, 2).join(' » « ') + ' »');
          if (e.texte < 20) pbChap.push(pid + ' : panneau quasi vide (' + e.texte + ' caractères)');
          if (suffixe === 'flash') {
            const f = await page.evaluate(pre => {
              const el = document.getElementById(pre + '-flash-content');
              return el ? { longueur: el.innerHTML.length, chargement: /Chargement…/.test(el.textContent) } : null;
            }, c.prefix);
            if (!f || f.longueur < 50 || f.chargement) pbChap.push(pid + ' : flashcard non injectée (#' + c.prefix + '-flash-content)');
          }
        }
      } catch (err) {
        pbChap.push(c.id + ' : ' + String(err.message).split('\n')[0]);
      }
      // Erreurs JS apparues pendant ce chapitre
      journal.erreurs.slice(nbErr).forEach(er => pbChap.push(c.id + ' : ' + er.type + ' pendant « ' + er.lieu + ' » : ' + er.texte));
      ctx.progression(i, selection.length, pbChap.length > avant);
    }
    res.info('panneauxVisites', nbPanneaux);
    res.verifier('chapitres × onglets : affichage, MathJax (' + nbPanneaux + ' panneaux)', !pbChap.length, pbChap);
    for (const pid of Object.keys(TEX_EN_CLAIR_CONNUS)) {
      const c = selection.find(x => x.onglets.includes(pid));
      if (c && !texConnusVus.has(pid)) res.avertir('TeX en clair CONNU sur ' + pid + ' corrigé ? Retirer « ' + pid + ' » de TEX_EN_CLAIR_CONNUS (tests/suites/site.js).');
    }
    for (const pid of Object.keys(ONGLETS_HORS_CHAPTERS_CONNUS)) {
      const c = selection.find(x => pid.startsWith(x.prefix + '-'));
      if (c && !ongletsConnusVus.has(pid)) res.avertir('Onglet ' + pid + ' désormais déclaré dans CHAPTERS ? Le retirer de ONGLETS_HORS_CHAPTERS_CONNUS (tests/suites/site.js).');
    }
    res.info('anomaliesConnuesRencontrees', { texEnClair: Array.from(texConnusVus), ongletsHorsChapters: Array.from(ongletsConnusVus) });

    if (selection.some(c => c.id === 'rlc')) {
      await naviguer(page, 'rlc', 'cours');
      await page.evaluate(() => window.scrollTo(0, 0));
      await ctx.capture(page, 'rlc-cours');
    }

    /* ---------- 4) Flashcards : flashPretty + MathJax sur toutes les cartes ---------- */
    journal.lieu = 'flashcards (MathJax)';
    const prefixes = selection.filter(c => c.panels.includes('flash')).map(c => c.prefix);
    const fl = await page.evaluate(async prefixes => {
      const r = { decks: 0, cartes: 0, merror: [], exceptions: [] };
      const boite = document.createElement('div');
      boite.style.cssText = 'position:absolute;left:-99999px;top:0;width:800px';
      document.body.appendChild(boite);
      for (const pre of prefixes) {
        const cartes = (window.FLASH_REGISTRY || {})[pre];
        if (!Array.isArray(cartes)) continue;
        r.decks++;
        // Decks d'anglais : texte brut, pas de flashPretty (voir makeFlash / isPlainDeck)
        if (CHAPTERS_BY_PREFIX[pre] && CHAPTERS_BY_PREFIX[pre].matiere === 'anglais') { r.cartes += cartes.length; continue; }
        boite.innerHTML = '';
        cartes.forEach((c, i) => ['q', 'a'].forEach(f => {
          const d = document.createElement('div');
          d.dataset.k = pre + '#' + i + '.' + f;
          try { d.innerHTML = flashPretty(c[f]); } catch (e) { r.exceptions.push(pre + '#' + i + '.' + f + ' : ' + e.message); }
          boite.appendChild(d);
        }));
        r.cartes += cartes.length;
        try { await MathJax.typesetPromise([boite]); } catch (e) { r.merror.push(pre + ' : typesetPromise a échoué (' + e.message + ')'); }
        boite.querySelectorAll('mjx-merror').forEach(m => {
          const k = (m.closest('[data-k]') || {}).dataset;
          r.merror.push((k ? k.k : pre) + ' : ' + (m.getAttribute('data-mjx-error') || m.textContent).slice(0, 100));
        });
        if (MathJax.typesetClear) MathJax.typesetClear([boite]);
      }
      boite.remove();
      return r;
    }, prefixes);
    res.verifier('flashcards : flashPretty + MathJax (' + fl.cartes + ' cartes, ' + fl.decks + ' decks)',
      !fl.merror.length && !fl.exceptions.length, fl.exceptions.map(e => 'exception flashPretty ' + e).concat(fl.merror.map(e => 'mjx-merror ' + e)));

    /* ---------- 5) Simulateurs en clair puis en sombre ---------- */
    const simus = (ctx.options.chapitres ? selection : tous).filter(c => c.drawFn && c.panels.includes('simu'));
    const themes = ctx.options.rapide ? ['clair'] : ['clair', 'sombre'];
    for (const theme of themes) {
      journal.lieu = 'thème ' + theme;
      if (theme === 'sombre') {
        await page.click('#theme-btn');
        await pause(300);
        const t = await page.evaluate(() => ({ attr: document.documentElement.getAttribute('data-theme'), stocke: Store.get('theme') }));
        res.verifier('bascule en thème sombre (#theme-btn)', t.attr === 'dark' && t.stocke === 'dark',
          'data-theme = ' + t.attr + ', Store theme = ' + t.stocke);
      }
      const pbSim = [];
      ctx.log(simus.length + ' simulateur(s) en thème ' + theme);
      for (let i = 0; i < simus.length; i++) {
        const c = simus[i];
        const avant = pbSim.length, nbErr = journal.erreurs.length;
        journal.lieu = c.id + '/simu (' + theme + ')';
        try {
          await naviguer(page, c.id, 'simu');
          await pause(250);
          const s = await page.evaluate(([pid, fn]) => {
            const out = { appel: 'ok', canvas: [], svg: 0 };
            try { window[fn](); } catch (e) { out.appel = e.message; }
            const panneau = document.getElementById(pid);
            if (!panneau) { out.appel = 'panneau ' + pid + ' introuvable'; return out; }
            out.canvas = Array.from(panneau.querySelectorAll('canvas')).filter(cv => cv.offsetParent !== null).map(cv => {
              let peints = 0;
              try {
                const g = cv.getContext('2d');
                if (g && cv.width && cv.height) {
                  const d = g.getImageData(0, 0, cv.width, cv.height).data;
                  for (let k = 3; k < d.length; k += 4 * 97) if (d[k] !== 0) peints++;
                }
              } catch (e) { peints = -1; }
              return { id: cv.id, l: cv.width, h: cv.height, peints };
            });
            out.svg = panneau.querySelectorAll('svg').length;
            return out;
          }, [c.prefix + '-simu', c.drawFn]);
          if (s.appel !== 'ok') pbSim.push(c.id + ' : ' + c.drawFn + '() lève « ' + s.appel + ' »');
          if (s.canvas.length && !s.canvas.some(k => k.peints > 0)) pbSim.push(c.id + ' : canvas vide(s) après ' + c.drawFn + '() : ' + s.canvas.map(k => (k.id || '?') + ' ' + k.l + '×' + k.h).join(', '));
          if (!s.canvas.length && !s.svg) pbSim.push(c.id + ' : aucun canvas ni SVG visible dans ' + c.prefix + '-simu');
        } catch (err) {
          pbSim.push(c.id + ' : ' + String(err.message).split('\n')[0]);
        }
        journal.erreurs.slice(nbErr).forEach(er => pbSim.push(c.id + ' : ' + er.type + ' : ' + er.texte));
        ctx.progression(i, simus.length, pbSim.length > avant);
      }
      res.verifier('simulateurs exécutés et peints — thème ' + theme + ' (' + simus.length + ')', !pbSim.length, pbSim);
      if (simus.some(c => c.id === 'rlc')) {
        await naviguer(page, 'rlc', 'simu');
        await page.evaluate(() => { const p = document.getElementById('rlc-simu'); if (p) p.scrollIntoView(); });
        await pause(300);
        await ctx.capture(page, 'rlc-simu-' + theme);
      }
    }
    if (themes.includes('sombre')) { await page.click('#theme-btn'); await pause(200); }

    /* ---------- 6) Bilan du journal : erreurs JS, requêtes externes ---------- */
    const js = journal.erreurs.map(e => '[' + e.lieu + '] ' + e.type + ' : ' + e.texte + (e.source ? ' (' + e.source + ')' : ''));
    res.verifier('aucune erreur console ni exception JavaScript', !js.length, js);
    res.verifier('aucune requête externe (site 100 % autonome)', !journal.externes.length,
      journal.externes.map(e => '[' + e.lieu + '] ' + e.url));
    const reseau = problemesJournal(Object.assign({}, journal, { erreurs: [], externes: [] }));
    res.verifier('aucune requête en échec ni réponse HTTP ≥ 400', !reseau.length, reseau);
    if (journal.dialogues.length) res.avertir('boîte(s) de dialogue inattendue(s) : ' + journal.dialogues.map(d => d.type + ' « ' + d.message + ' »').join(' ; '));
  },
};
