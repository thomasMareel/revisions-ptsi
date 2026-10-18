/* Capture chaque panneau (simulateurs par défaut) : une image par panneau, puis planche.
   Usage : node sims.js <racine> <sortie> <largeur> <hauteur> <clair|sombre> [ids séparés par des virgules] [onglet=simu] [plein] */
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');
const [racine, sortie, w, h, theme, idsArg, ongletArg, pleinArg] = process.argv.slice(2);
const { demarrerServeur } = require(path.join(racine, 'tests/lib/serveur.js'));
const pause = ms => new Promise(r => setTimeout(r, ms));
fs.mkdirSync(sortie, { recursive: true });
(async () => {
  const srv = await demarrerServeur(racine);
  const nav = await chromium.launch();
  const mobile = +w < 768;
  const ctx = await nav.newContext({ viewport: { width: +w, height: +h }, serviceWorkers: 'block', deviceScaleFactor: 1, isMobile: mobile, hasTouch: mobile });
  await ctx.addInitScript(t => { try { localStorage.setItem('theme', t); } catch (e) {} }, theme === 'sombre' ? 'dark' : 'light');
  const page = await ctx.newPage();
  const erreurs = [];
  page.on('pageerror', e => erreurs.push(String(e.message) + ' @ ' + String(e.stack).split('\n').slice(1, 3).join(' / ')));
  page.on('console', m => { if (m.type() === 'error') erreurs.push('console: ' + m.text().slice(0, 200)); });
  await page.goto(srv.url + 'index.html#rlc/cours');
  await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_INSTANCES && window.MathJax && MathJax.typesetPromise, null, { timeout: 60000 });
  await pause(1500);
  const onglet = ongletArg || 'simu';
  let ids = idsArg && idsArg !== '-' ? idsArg.split(',') : await page.evaluate(o => CHAPTERS.filter(c => c.panels.includes(o) && (o !== 'simu' || c.drawFn)).map(c => c.id), onglet);
  console.log('ordre', ids.join(' '));
  const res = [];
  for (const id of ids) {
    const avant = erreurs.length;
    await page.evaluate(([id, o]) => { location.hash = '#' + id + '/' + o; }, [id, onglet]);
    await pause(900);
    const info = await page.evaluate(([id, o]) => {
      const c = CHAPTERS_BY_ID[id];
      const p = document.getElementById(c.prefix + '-' + o);
      if (!p) return { ok: false };
      p.scrollIntoView({ block: 'start' });
      const W = document.documentElement.clientWidth;
      return { ok: true, sw: document.documentElement.scrollWidth, W, h: p.getBoundingClientRect().height };
    }, [id, onglet]);
    await pause(250);
    const f = path.join(sortie, id + '.png');
    try {
      const prefix = await page.evaluate(id => CHAPTERS_BY_ID[id].prefix, id);
      const el = await page.$('#' + prefix + '-' + onglet);
      if (pleinArg) await el.screenshot({ path: f });
      else await page.screenshot({ path: f });
    } catch (e) { erreurs.push(id + ' capture : ' + e.message); }
    res.push({ id, ...info, erreurs: erreurs.slice(avant) });
  }
  console.log(JSON.stringify(res.filter(r => r.erreurs.length || (r.sw > r.W + 1)), null, 1));
  console.log('panneaux :', res.length, '| erreurs JS :', erreurs.length);
  await nav.close(); await srv.fermer();
})().catch(e => { console.error(e); process.exit(1); });
