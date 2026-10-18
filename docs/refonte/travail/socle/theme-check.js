/* Vérifie le thème : préférence × système → data-theme, --sheet, metas theme-color,
   y compris AVANT le grand script (DOMContentLoaded non attendu). */
const path = require('path');
const { chromium } = require('playwright');
const racine = process.argv[2];
const { demarrerServeur } = require(path.join(racine, 'tests/lib/serveur.js'));
(async () => {
  const srv = await demarrerServeur(racine);
  const nav = await chromium.launch();
  for (const sys of ['light', 'dark']) for (const pref of ['light', 'dark', 'auto', null]) {
    const ctx = await nav.newContext({ colorScheme: sys, serviceWorkers: 'block' });
    await ctx.addInitScript(p => { try { if (p) localStorage.setItem('theme', p); else localStorage.removeItem('theme'); } catch (e) {} }, pref);
    const page = await ctx.newPage();
    // état très tôt : dès que <body> existe
    await page.goto(srv.url + 'index.html', { waitUntil: 'commit' });
    await page.waitForFunction(() => !!document.body, null, { timeout: 30000 });
    const tot = await page.evaluate(() => ({ theme: document.documentElement.getAttribute('data-theme'), pref: document.documentElement.getAttribute('data-theme-pref'), sheet: getComputedStyle(document.documentElement).getPropertyValue('--sheet').trim() }));
    await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.__themePref, null, { timeout: 60000 });
    const tard = await page.evaluate(() => ({ theme: document.documentElement.getAttribute('data-theme'), pref: document.documentElement.getAttribute('data-theme-pref'), sheet: getComputedStyle(document.documentElement).getPropertyValue('--sheet').trim(),
      metas: Array.from(document.querySelectorAll('meta[name="theme-color"]')).map(m => m.getAttribute('media').replace(/\(prefers-color-scheme: |\)/g, '') + '=' + m.content).join(' '),
      cv: (() => { const c = getCanvasColors(); return c.muted + ' ' + c.grid + ' ' + c.ink; })() }));
    const attendu = (pref === 'dark' || ((pref === 'auto' || !pref) && sys === 'dark')) ? '#191b20' : '#fffdf9';
    const ok = tot.sheet === attendu && tard.sheet === attendu;
    console.log((ok ? 'ok ' : 'KO ') + 'système ' + sys + ', préférence ' + pref + ' → tôt ' + JSON.stringify(tot) + ' | tard ' + JSON.stringify(tard));
    await ctx.close();
  }
  await nav.close(); await srv.fermer();
})().catch(e => { console.error(e); process.exit(1); });
