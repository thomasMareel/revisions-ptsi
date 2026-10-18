// Capture zoomée (×3) d'une zone d'une maquette : node zoom.js maquette.html x y l h sortie.png [largeur fenêtre]
const path = require('path'); const { chromium } = require('playwright');
(async () => {
  const [f, x, y, w, h, out, vw] = process.argv.slice(2);
  const b = await chromium.launch({ env: Object.assign({}, process.env, { FONTCONFIG_FILE: '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/ptspe/fonts-sans-lm.conf' }) });
  const p = await (await b.newContext({ viewport: { width: +(vw || 1440), height: 900 }, deviceScaleFactor: 3 })).newPage();
  await p.goto('file://' + path.resolve(f)); await p.waitForFunction(() => window.MathJax && MathJax.startup && MathJax.startup.promise); await p.evaluate(() => MathJax.startup.promise); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  await p.screenshot({ path: out, clip: { x: +x, y: +y, width: +w, height: +h } }); await b.close();
})();
