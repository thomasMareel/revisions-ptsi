/* Évalue une expression dans la page. Usage : node eval.js <racine> <largeur> <hash> <fichier-expression.js> [sombre] */
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');
const [racine, w, hash, fichier, theme] = process.argv.slice(2);
const { demarrerServeur } = require(path.join(racine, 'tests/lib/serveur.js'));
const pause = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const srv = await demarrerServeur(racine);
  const nav = await chromium.launch();
  const mobile = +w < 768;
  const ctx = await nav.newContext({ viewport: { width: +w, height: 844 }, serviceWorkers: 'block', isMobile: mobile, hasTouch: mobile });
  await ctx.addInitScript(t => { try { localStorage.setItem('theme', t); } catch (e) {} }, theme === 'sombre' ? 'dark' : 'light');
  const page = await ctx.newPage();
  page.on('pageerror', e => console.log('ERREUR', e.message));
  await page.goto(srv.url + 'index.html#' + hash);
  await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_INSTANCES && window.MathJax && MathJax.typesetPromise, null, { timeout: 60000 });
  await pause(2500);
  const expr = fs.readFileSync(fichier, 'utf8');
  const r = await page.evaluate(expr);
  console.log(typeof r === 'string' ? r : JSON.stringify(r, null, 1));
  await nav.close(); await srv.fermer();
})().catch(e => { console.error(e); process.exit(1); });
