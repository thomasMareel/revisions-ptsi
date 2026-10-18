// Captures du site réel (copie de travail) pour comparaison aux maquettes.
// node capt.js <racine du site> <dossier de sortie> [filtre]
const path = require('path'), fs = require('fs'), http = require('http');
const { chromium } = require('playwright');
const RACINE = path.resolve(process.argv[2] || '.');
const SORTIE = path.resolve(process.argv[3] || './cap');
const FILTRE = process.argv[4] || '';
fs.mkdirSync(SORTIE, { recursive: true });
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.woff2': 'font/woff2', '.json': 'application/json', '.webmanifest': 'application/manifest+json', '.png': 'image/png', '.svg': 'image/svg+xml' };
const serveur = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
  const f = path.join(RACINE, p);
  if (!f.startsWith(RACINE) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});
const D = { w: 1440, h: 900, mob: false }, P = { w: 390, h: 844, mob: true };
const pause = ms => new Promise(r => setTimeout(r, ms));
// Défilement instantané par pas de 100 px (une image entre deux pas), comme un doigt
async function defiler(p, dy) {
  await p.evaluate(async d => { const pas = d > 0 ? 100 : -20; for (let f = 0; Math.abs(f) < Math.abs(d); f += pas) {
    window.scrollBy({ top: pas, behavior: 'instant' }); await new Promise(r => requestAnimationFrame(() => setTimeout(r, 16))); } }, dy);
  await pause(400);
}
// Semis : progression de quelques decks (cartes dues), épinglés
async function semer(p) {
  await p.evaluate(() => {
    const jour = 86400000, t = Date.now();
    ['rlc', 'cpx', 'og', 'slci', 'mxw', 'ond', 'fil', 'sig'].forEach(pr => {
      const cartes = window.FLASH_REGISTRY && FLASH_REGISTRY[pr]; if (!cartes) return;
      const etat = cartes.map((_, i) => { const k = i % 5; if (k === 4) return { h: 0, o: 0, e: 0, last: null };
        const last = [2, 1, 0, 2][k]; return { h: last === 0 ? 1 : 0, o: last === 1 ? 1 : 0, e: last === 2 ? 2 : 0, last, box: last === 2 ? 2 : (last === 1 ? 1 : 0), due: t + (k === 2 || i % 7 === 0 ? -jour : 3 * jour) }; });
      flashSaveState(pr, cartes, etat);
      if (window.FLASH_INSTANCES && FLASH_INSTANCES[pr] && FLASH_INSTANCES[pr].reload) FLASH_INSTANCES[pr].reload();
    });
    const id = n => { const c = CHAPTERS.find(x => x.id === n || x.mobLabel === n); return c ? 'chap-' + c.id : null; };
    Store.setJSON('pinned', [id('Filtres'), id('maxwell')].filter(Boolean));
    if (window.__updateReviseBadge) window.__updateReviseBadge();
  });
}
const SCEN = [
  ['01-chapitre-ordinateur', D, 'light', '#rlc/cours'],
  ['06a-chapitre-sombre-ordinateur', D, 'dark', '#rlc/cours'],
  ['02-chapitre-telephone', P, 'light', '#rlc/cours'],
  ['06b-chapitre-sombre-telephone', P, 'dark', '#rlc/cours'],
  ['02b-chapitre-telephone-defile', P, 'light', '#rlc/cours', async p => { await defiler(p, 1400); await defiler(p, -60); }],
  ['02c-chapitre-telephone-cachee', P, 'light', '#rlc/cours', async p => { await defiler(p, 1400); }],
  ['03a-navigation-ordinateur', D, 'light', '#sommaire/physique'],
  ['03a-navigation-ordinateur-sombre', D, 'dark', '#sommaire/physique'],
  ['03b-navigation-telephone', P, 'light', '#rlc/meth', async p => { await p.tap('#mob-menu-btn'); await pause(600); }],
  ['03b-navigation-telephone-sombre', P, 'dark', '#rlc/meth', async p => { await p.tap('#mob-menu-btn'); await pause(600); }],
  ['03c-navigation-telephone-filtre', P, 'light', '#rlc/meth', async p => { await p.tap('#mob-menu-btn'); await pause(500); await p.fill('#mob-filter', 'onde'); await pause(400); }],
  ['03d-sommaire-telephone', P, 'light', '#sommaire/physique'],
  ['07a-theme-ordinateur', D, 'light', '#rlc/cours', async p => { await p.click('#theme-btn'); await pause(400); }],
  ['07a-theme-ordinateur-sombre', D, 'dark', '#rlc/cours', async p => { await p.click('#theme-btn'); await pause(400); }],
  ['07b-theme-telephone-systeme-sombre', P, 'auto-dark', '#rlc/meth', async p => { await p.tap('#mob-more-btn'); await pause(600); }],
  ['07b-theme-telephone-systeme-clair', P, 'auto-light', '#rlc/meth', async p => { await p.tap('#mob-more-btn'); await pause(600); }],
  ['tablette-1024', { w: 1024, h: 768, mob: false }, 'light', '#rlc/cours'],
  ['tablette-1024-tiroir', { w: 1024, h: 768, mob: false }, 'light', '#rlc/cours', async p => { await p.click('#nav-toggle-btn'); await pause(500); }],
  ['tablette-800', { w: 800, h: 1000, mob: false }, 'light', '#rlc/cours'],
  ['ordi-1280', { w: 1280, h: 800, mob: false }, 'light', '#rlc/cours'],
  ['ordi-1280-plus', { w: 1280, h: 800, mob: false }, 'light', '#rlc/cours', async p => { await p.click('#more-btn'); await pause(300); }],
  ['menu-plus', D, 'light', '#rlc/cours', async p => { await p.click('#more-btn'); await pause(300); }],
  ['menu-reviser', D, 'light', '#rlc/cours', async p => { await p.click('#study-btn'); await pause(300); }],
  ['menu-reviser-sombre', D, 'dark', '#rlc/cours', async p => { await p.click('#study-btn'); await pause(300); }],
  ['filtre-ordinateur', D, 'light', '#rlc/cours', async p => { await p.fill('#mob-filter', 'onde'); await pause(400); }],
  ['ordi-2a', D, 'light', '#maxwell/cours'],
  ['tablette-768', { w: 768, h: 1000, mob: false }, 'light', '#rlc/cours'],
  ['ordi-1150', { w: 1150, h: 800, mob: false }, 'light', '#rlc/cours'],
  ['ordi-1150-sombre', { w: 1150, h: 800, mob: false }, 'dark', '#rlc/cours'],
];
(async () => {
  await new Promise(r => serveur.listen(0, r));
  const base = 'http://127.0.0.1:' + serveur.address().port + '/';
  const b = await chromium.launch();
  for (const [nom, v, theme, hash, action] of SCEN) {
    if (FILTRE && !new RegExp(FILTRE).test(nom)) continue;
    const scheme = theme === 'auto-dark' ? 'dark' : 'light';
    const ctx = await b.newContext({ viewport: { width: v.w, height: v.h }, deviceScaleFactor: v.mob ? 2 : 1, isMobile: v.mob, hasTouch: v.mob, colorScheme: scheme, serviceWorkers: 'block' });
    const pref = theme.startsWith('auto') ? 'auto' : theme;
    await ctx.addInitScript(t => { try { if (!sessionStorage.getItem('capt')) { localStorage.setItem('theme', t); sessionStorage.setItem('capt', '1'); } } catch (e) {} }, pref);
    const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', e => errs.push('JS ' + e.message)); p.on('console', m => { if (m.type() === 'error') errs.push('console ' + m.text()); });
    await p.goto(base + 'index.html#cine/cours', { waitUntil: 'load' });
    await p.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_REGISTRY, null, { timeout: 30000 });
    await pause(500);
    await semer(p);
    for (const h of ['#slci/flash', '#cine/exos', '#rlc/cours']) { await p.evaluate(x => { location.hash = x; }, h); await pause(450); }
    await p.evaluate(x => { location.hash = x; }, hash); await pause(900);
    await p.evaluate(async () => { try { await MathJax.startup.promise; } catch (e) {} await document.fonts.ready; });
    await pause(500);
    if (action) await action(p);
    await pause(300);
    const info = await p.evaluate(() => ({ deb: document.documentElement.scrollWidth - window.innerWidth }));
    await p.screenshot({ path: path.join(SORTIE, nom + '.png') });
    console.log(nom, JSON.stringify(info), errs.join(' | '));
    await ctx.close();
  }
  await b.close(); serveur.close();
})();
