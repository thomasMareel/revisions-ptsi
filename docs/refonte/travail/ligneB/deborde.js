/* Qui fait déborder la page ? Usage : node deborde.js <racine> <largeur> <hash> [sol] */
const path = require('path');
const { chromium } = require('playwright');
const [racine, w, hash, sol] = process.argv.slice(2);
const { demarrerServeur } = require(path.join(racine, 'tests/lib/serveur.js'));
const pause = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const srv = await demarrerServeur(racine);
  const nav = await chromium.launch();
  const mobile = +w < 768;
  const ctx = await nav.newContext({ viewport: { width: +w, height: 844 }, serviceWorkers: 'block', isMobile: mobile, hasTouch: mobile });
  const page = await ctx.newPage();
  await page.goto(srv.url + 'index.html#' + hash);
  await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_INSTANCES && window.MathJax && MathJax.typesetPromise, null, { timeout: 60000 });
  await pause(2500);
  if (sol) await page.evaluate(() => { const p = Array.from(document.querySelectorAll('.chapter.active .panel.active')).find(x => x.offsetParent);
    p.querySelectorAll('.toggle-sol').forEach(b => b.click()); p.querySelectorAll('.reveal:not(.open)').forEach(r => r.click()); });
  await pause(1200);
  const r = await page.evaluate(() => {
    const W = document.documentElement.clientWidth, out = [];
    document.querySelectorAll('body *').forEach(e => {
      const b = e.getBoundingClientRect();
      if (b.right > W + 0.5 && b.width > 0 && b.height > 0 && getComputedStyle(e).visibility !== 'hidden') {
        if (e.parentElement && e.parentElement.getBoundingClientRect().right > W + 0.5) return;
        out.push(e.tagName.toLowerCase() + '.' + String(e.className).slice(0, 40) + ' #' + e.id + ' → ' + Math.round(b.right) + ' (l=' + Math.round(b.left) + ', w=' + Math.round(b.width) + ') parent ' + e.parentElement.tagName + '.' + String(e.parentElement.className).slice(0, 30) + ' ov=' + getComputedStyle(e.parentElement).overflowX);
      }
    });
    return { sw: document.documentElement.scrollWidth, bsw: document.body.scrollWidth, W, out: out.slice(0, 25) };
  });
  console.log(JSON.stringify(r, null, 1));
  await nav.close(); await srv.fermer();
})().catch(e => { console.error(e); process.exit(1); });
