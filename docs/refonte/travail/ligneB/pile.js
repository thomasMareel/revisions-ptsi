/* Pile d'une erreur JS sur un panneau. Usage : node pile.js <racine> <largeur> <hauteur> <hash…> */
const path = require('path');
const { chromium } = require('playwright');
const [racine, w, h, ...hashes] = process.argv.slice(2);
const { demarrerServeur } = require(path.join(racine, 'tests/lib/serveur.js'));
const pause = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const srv = await demarrerServeur(racine);
  const nav = await chromium.launch();
  const mobile = +w < 768;
  const ctx = await nav.newContext({ viewport: { width: +w, height: +h }, serviceWorkers: 'block', isMobile: mobile, hasTouch: mobile });
  const page = await ctx.newPage();
  page.on('pageerror', e => console.log('ERREUR', e.message, '\n', String(e.stack).split('\n').slice(0, 6).join('\n')));
  await page.goto(srv.url + 'index.html#rlc/cours');
  await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_INSTANCES && window.MathJax && MathJax.typesetPromise, null, { timeout: 60000 });
  await pause(1000);
  for (const hsh of hashes) {
    console.log('→', hsh);
    await page.evaluate(x => { location.hash = '#' + x; }, hsh);
    await pause(1200);
    if (process.env.ELT) { const pid = await page.evaluate(x => CHAPTERS_BY_ID[x.split('/')[0]].prefix + '-' + x.split('/')[1], hsh); const el = await page.$('#' + pid); await el.screenshot({ path: '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/ligneB/pile.png' }); await pause(500); }
  }
  await nav.close(); await srv.fermer();
})().catch(e => { console.error(e); process.exit(1); });
