/* Contrôle sur le DOM réel des couples de sélecteurs candidats (conflits.py) :
   un élément peut-il porter les deux sélecteurs ? On parcourt plusieurs états
   (fenêtres ouvertes, tiroir, menus, carte retournée, solution dépliée,
   téléphone) et on fait l'union.
   Usage : node conflits-dom.js <racine-site> <candidats.json> <sortie.json> */
const path = require('path');
const fs = require('fs');
const racine = process.argv[2];
const cands = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
const sortie = process.argv[4];
const { chromium } = require('playwright');
const { demarrerServeur } = require(path.join(racine, 'tests/lib/serveur.js'));

const pause = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const srv = await demarrerServeur(racine);
  const nav = await chromium.launch();
  const paires = [];
  const vu = new Map();
  cands.forEach(c => { const k = c.a + '\u0001' + c.b; if (!vu.has(k)) { vu.set(k, paires.length); paires.push([c.a, c.b]); } });
  const touche = new Set();
  const erreurs = [];

  async function releve(page, etiquette) {
    const r = await page.evaluate(paires => {
      const nettoie = s => {
        s = s.replace(/:root\[data-theme="dark"\]/g, ':root');
        s = s.replace(/::[\w-]+(\([^)]*\))?/g, '');
        s = s.replace(/:not\(:(hover|disabled|focus|active|checked|focus-visible)\)/g, '');
        s = s.replace(/:(hover|active|focus-visible|focus-within|focus|visited|checked|disabled|placeholder-shown)(?![\w-])/g, '');
        s = s.trim();
        if (!s || /[\s>+~]$/.test(s)) s = s + '*';
        return s;
      };
      const cache = new Map();
      const tous = sel => {
        if (!cache.has(sel)) { try { cache.set(sel, Array.from(document.querySelectorAll(sel))); } catch (e) { cache.set(sel, null); } }
        return cache.get(sel);
      };
      const res = [], err = [];
      paires.forEach(([a, b], i) => {
        const na = nettoie(a), nb = nettoie(b);
        const la = tous(na);
        if (la === null) { err.push(na); return; }
        if (!la.length) return;
        try { if (la.some(el => el.matches(nb))) res.push(i); } catch (e) { err.push(nb); }
      });
      return { res, err };
    }, paires);
    r.res.forEach(i => touche.add(i));
    r.err.forEach(e => erreurs.push(etiquette + ' : ' + e));
    console.log(etiquette, '→', r.res.length, 'couples avec élément commun (cumul', touche.size + ')');
  }

  async function ouvrir(page, etiquette, fn) {
    try { await page.evaluate(fn); await pause(400); await releve(page, etiquette); }
    catch (e) { console.log('état', etiquette, 'impossible :', String(e.message).split('\n')[0]); }
    try { await page.keyboard.press('Escape'); await pause(150); } catch (e) {}
  }

  for (const vp of [{ width: 1280, height: 900, nom: 'ordinateur' }, { width: 390, height: 844, nom: 'téléphone' }]) {
    const ctx = await nav.newContext({ viewport: { width: vp.width, height: vp.height }, serviceWorkers: 'block' });
    const page = await ctx.newPage();
    await page.goto(srv.url + 'index.html#rlc/cours');
    await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_INSTANCES, null, { timeout: 60000 });
    await pause(1500);
    await releve(page, vp.nom + ' chargement');
    await ouvrir(page, vp.nom + ' tiroir', () => { const b = document.getElementById('nav-toggle-btn') || document.getElementById('mob-menu-btn'); b && b.click(); });
    await ouvrir(page, vp.nom + ' menu plus', () => { const b = document.getElementById(innerWidth < 768 ? 'mob-more-btn' : 'more-btn'); b && b.click(); });
    await ouvrir(page, vp.nom + ' menu réviser', () => { const b = document.getElementById('study-btn'); b && b.click(); });
    await ouvrir(page, vp.nom + ' aujourd\'hui', () => window.todayOpen && window.todayOpen());
    await ouvrir(page, vp.nom + ' bilan', () => document.getElementById('dash-btn').click());
    await ouvrir(page, vp.nom + ' recherche', async () => { document.getElementById('search-btn').click(); const i = document.getElementById('search-input'); i.value = 'résonance'; i.dispatchEvent(new Event('input', { bubbles: true })); await new Promise(r => setTimeout(r, 600)); });
    await ouvrir(page, vp.nom + ' formulaire', () => document.getElementById('formula-btn').click());
    await ouvrir(page, vp.nom + ' sauvegarde', () => document.getElementById('backup-btn').click());
    await ouvrir(page, vp.nom + ' signalées', () => document.getElementById('flag-btn').click());
    await ouvrir(page, vp.nom + ' calcul', () => document.getElementById('drill-btn').click());
    await ouvrir(page, vp.nom + ' raccourcis', () => document.dispatchEvent(new KeyboardEvent('keydown', { key: '?', bubbles: true })));
    await ouvrir(page, vp.nom + ' quiz config', () => document.getElementById('quiz-btn').click());
    await ouvrir(page, vp.nom + ' quiz question', async () => { document.getElementById('quiz-btn').click(); await new Promise(r => setTimeout(r, 200)); document.getElementById('quiz-start-btn').click(); await new Promise(r => setTimeout(r, 300)); const b = document.getElementById('quiz-reveal-btn'); b && b.click(); });
    // flashcards + exos + simu
    await ouvrir(page, vp.nom + ' flashcards', async () => { location.hash = '#rlc/flash'; await new Promise(r => setTimeout(r, 500)); window.FLASH_INSTANCES.rlc.flip(); await new Promise(r => setTimeout(r, 500)); });
    await ouvrir(page, vp.nom + ' exos', async () => { location.hash = '#rlc/exos'; await new Promise(r => setTimeout(r, 500)); document.querySelectorAll('.chapter.active .toggle-sol').forEach(b => b.click()); document.querySelectorAll('.reveal').forEach(r => r.classList.add('open')); });
    await ouvrir(page, vp.nom + ' simu', async () => { location.hash = '#rlc/simu'; await new Promise(r => setTimeout(r, 500)); });
    await ouvrir(page, vp.nom + ' anglais', async () => { location.hash = '#' + CHAPTERS.find(c => c.matiere === 'anglais').id + '/flash'; await new Promise(r => setTimeout(r, 500)); });
    await ouvrir(page, vp.nom + ' SI', async () => { location.hash = '#slci/cours'; await new Promise(r => setTimeout(r, 500)); });
    await ouvrir(page, vp.nom + ' sombre', async () => { window.__setTheme('dark'); await new Promise(r => setTimeout(r, 300)); });
    await ctx.close();
  }
  const out = cands.filter(c => touche.has(vu.get(c.a + '\u0001' + c.b)));
  fs.writeFileSync(sortie, JSON.stringify({ conflits: out, erreurs: [...new Set(erreurs)] }, null, 1));
  console.log('conflits avérés :', out.length, '— erreurs de sélecteur :', new Set(erreurs).size);
  await nav.close();
  await srv.fermer();
})().catch(e => { console.error(e); process.exit(1); });
