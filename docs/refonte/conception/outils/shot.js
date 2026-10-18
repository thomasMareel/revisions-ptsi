// node shot.js fichier.html sortie.png largeur hauteur [dpr]
const { chromium } = require('playwright');
(async () => {
  const [f, out, w, h, dpr] = process.argv.slice(2);
  const b = await chromium.launch({ env: Object.assign({}, process.env, { FONTCONFIG_FILE: '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/ptspe/fonts-sans-lm.conf' }) });
  const p = await (await b.newContext({ viewport: { width: +w, height: +h }, deviceScaleFactor: +(dpr || 1) })).newPage();
  await p.goto('file://' + f); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  await p.screenshot({ path: out, fullPage: true }); await b.close();
})();
