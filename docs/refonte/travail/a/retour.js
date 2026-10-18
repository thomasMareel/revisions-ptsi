// Débogage : bouton retour Android sur la page Chapitres / la feuille ⋯ (téléphone)
const path = require('path'), fs = require('fs'), http = require('http');
const { chromium } = require('playwright');
const RACINE = path.resolve(process.argv[2] || '.');
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.woff2': 'font/woff2', '.json': 'application/json', '.webmanifest': 'application/manifest+json', '.png': 'image/png', '.svg': 'image/svg+xml' };
const serveur = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
  const f = path.join(RACINE, p);
  if (!f.startsWith(RACINE) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});
const pause = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  await new Promise(r => serveur.listen(0, r));
  const base = 'http://127.0.0.1:' + serveur.address().port + '/';
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2, locale: 'fr-FR', serviceWorkers: 'block' });
  const p = await ctx.newPage();
  p.on('pageerror', e => console.log('JS', e.message));
  p.on('framenavigated', f => { if (f === p.mainFrame()) console.log('NAV', f.url()); });
  await p.goto(base + 'index.html', { waitUntil: 'load' });
  await p.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_REGISTRY, null, { timeout: 30000 });
  await pause(1500);
  const etat = async t => console.log(t, JSON.stringify(await p.evaluate(() => ({ h: location.hash, len: history.length, st: history.state,
    dr: document.getElementById('mob-drawer').classList.contains('open'), fe: document.getElementById('mob-more-menu').classList.contains('open') }))));
  await etat('départ');
  await p.tap('#mob-menu-btn'); await pause(500); await etat('tiroir ouvert');
  await p.tap('.mob-mat-btn[data-mat="maths"]'); await pause(300); await etat('maths');
  await p.fill('#mob-filter', 'electro'); await pause(300); await p.screenshot({ path: '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/a/dbg1.png' });
  await p.fill('#mob-filter', 'zzzqqq'); await pause(250);
  await p.fill('#mob-filter', 'rlc'); await pause(300); await p.press('#mob-filter', 'Enter'); await pause(900); await etat('après Entrée');
  await p.evaluate(() => window.scrollTo(0, 0)); await p.screenshot({ path: '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/a/dbg2.png' });
  await p.tap('#mob-menu-btn', { timeout: 5000 }).catch(e => console.log('ÉCHEC tap', e.message));
  await pause(500); await etat('tiroir rouvert');
  await p.goBack({ timeout: 5000 }).catch(e => console.log('goBack', e.message.split('\n')[0])); await pause(500); await etat('après retour');
  await p.tap('#mob-more-btn', { timeout: 5000 }).catch(e => console.log('ÉCHEC tap ⋯', e.message.split('\n')[0]));
  await pause(500); await etat('feuille ouverte');
  await p.goBack({ timeout: 5000 }).catch(e => console.log('goBack', e.message.split('\n')[0])); await pause(500); await etat('après retour 2');
  await b.close(); serveur.close();
})();
