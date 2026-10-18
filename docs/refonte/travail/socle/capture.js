/* Captures rapides du site (copie de travail) + bilan polices / erreurs / requêtes.
   Usage : node capture.js <racine> <dossier-sortie> [hash=rlc/cours] */
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');
const [racine, sortie, hashArg] = process.argv.slice(2);
const hash = hashArg || 'rlc/cours';
const { demarrerServeur } = require(path.join(racine, 'tests/lib/serveur.js'));
const pause = ms => new Promise(r => setTimeout(r, ms));
fs.mkdirSync(sortie, { recursive: true });

(async () => {
  const srv = await demarrerServeur(racine);
  const nav = await chromium.launch();
  const bilan = [];
  for (const [nom, w, h, theme] of [['ordi-clair', 1280, 900, 'light'], ['ordi-sombre', 1280, 900, 'dark'], ['tel-clair', 390, 844, 'light'], ['tel-sombre', 390, 844, 'dark']]) {
    const ctx = await nav.newContext({ viewport: { width: w, height: h }, serviceWorkers: 'block', deviceScaleFactor: 1 });
    await ctx.addInitScript(t => { try { localStorage.setItem('theme', t); } catch (e) {} }, theme);
    const page = await ctx.newPage();
    const erreurs = [], externes = [];
    page.on('pageerror', e => erreurs.push(String(e.message)));
    page.on('console', m => { if (m.type() === 'error') erreurs.push('console: ' + m.text()); });
    page.on('request', r => { if (!r.url().startsWith(srv.url) && !r.url().startsWith('data:') && !r.url().startsWith('about:')) externes.push(r.url()); });
    await page.goto(srv.url + 'index.html#' + hash);
    await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_INSTANCES && window.MathJax && MathJax.typesetPromise, null, { timeout: 60000 });
    await pause(2500);
    const info = await page.evaluate(async () => {
      await document.fonts.ready;
      const chargees = new Set();
      document.fonts.forEach(f => { if (f.status === 'loaded') chargees.add(f.family.replace(/"/g, '') + ' ' + f.style + ' ' + f.weight); });
      const p = document.querySelector('.chapter.active .panel.active p') || document.body;
      const cs = getComputedStyle(p);
      return { polices: [...chargees].sort(), pFont: cs.fontFamily, pSize: cs.fontSize, theme: document.documentElement.getAttribute('data-theme'), pref: document.documentElement.getAttribute('data-theme-pref'),
        debord: document.documentElement.scrollWidth > innerWidth, mjx: document.querySelectorAll('.chapter.active .panel.active mjx-container').length };
    });
    await page.screenshot({ path: path.join(sortie, nom + '.png') });
    bilan.push({ nom, ...info, erreurs, externes });
    await ctx.close();
  }
  console.log(JSON.stringify(bilan, null, 1));
  await nav.close();
  await srv.fermer();
})().catch(e => { console.error(e); process.exit(1); });
