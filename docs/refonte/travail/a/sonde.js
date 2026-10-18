// Sonde : ouvre le site (copie de travail) et évalue une expression JS.
// node sonde.js <racine> <largeur> <hauteur> <mobile 0|1> <hash> "<expression JS>" [actions JS avant]
const path = require('path'), fs = require('fs'), http = require('http');
const { chromium } = require('playwright');
const [racineArg, L, H, mob, hash, expr, avant] = process.argv.slice(2);
const RACINE = path.resolve(racineArg);
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.woff2': 'font/woff2', '.json': 'application/json', '.webmanifest': 'application/manifest+json', '.png': 'image/png', '.svg': 'image/svg+xml' };
const serveur = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
  const f = path.join(RACINE, p);
  if (!f.startsWith(RACINE) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});
(async () => {
  await new Promise(r => serveur.listen(0, r));
  const base = 'http://127.0.0.1:' + serveur.address().port + '/';
  const b = await chromium.launch();
  const m = mob === '1';
  const ctx = await b.newContext({ viewport: { width: +L, height: +H }, isMobile: m, hasTouch: m, serviceWorkers: 'block' });
  const p = await ctx.newPage(); const errs = [];
  p.on('pageerror', e => errs.push('JS ' + e.message + ' ' + (e.stack || '').split('\n').slice(1, 3).join(' '))); p.on('console', msg => { if (msg.type() === 'error' || msg.type() === 'warning') errs.push('console ' + msg.text()); });
  await p.goto(base + 'index.html' + (hash || ''), { waitUntil: 'load' });
  await p.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_REGISTRY, null, { timeout: 30000 });
  await new Promise(r => setTimeout(r, 1200));
  if (avant) { await p.evaluate(avant); await new Promise(r => setTimeout(r, 800)); }
  const r = await p.evaluate(expr);
  console.log(JSON.stringify(r, null, 1));
  if (errs.length) console.log('ERREURS', errs);
  await b.close(); serveur.close();
})();
