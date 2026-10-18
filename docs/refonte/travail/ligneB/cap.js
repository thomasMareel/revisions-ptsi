/* Captures de travail de la ligne B (contenu).
   Usage : node cap.js <racine> <sortie> <spec> [<spec>…]
   spec = nom:hash:largeur:hauteur:theme[:plein][:sol][:scroll=N][:sel=CSS]
     theme = clair|sombre ; plein = page entière ; sol = déplier toutes les solutions et .reveal
     scroll=N : défiler de N px ; sel=CSS : faire défiler jusqu'à l'élément CSS puis capturer l'écran */
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');
const [racine, sortie, ...specs] = process.argv.slice(2);
const { demarrerServeur } = require(path.join(racine, 'tests/lib/serveur.js'));
const pause = ms => new Promise(r => setTimeout(r, ms));
fs.mkdirSync(sortie, { recursive: true });

(async () => {
  const srv = await demarrerServeur(racine);
  const nav = await chromium.launch();
  const bilan = [];
  for (const spec of specs) {
    const [nom, hash, w, h, theme, ...opts] = spec.split('|');
    const o = {};
    opts.forEach(x => { const [k, v] = x.split('='); o[k] = v === undefined ? true : v; });
    const mobile = +w < 768;
    const ctx = await nav.newContext({ viewport: { width: +w, height: +h }, serviceWorkers: 'block', deviceScaleFactor: o.dpr ? +o.dpr : 1, isMobile: mobile, hasTouch: mobile });
    await ctx.addInitScript(t => { try { localStorage.setItem('theme', t); } catch (e) {} }, theme === 'sombre' ? 'dark' : 'light');
    const page = await ctx.newPage();
    const erreurs = [];
    page.on('pageerror', e => erreurs.push(String(e.message)));
    page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') erreurs.push('console: ' + m.text().slice(0, 300)); });
    await page.goto(srv.url + 'index.html#' + hash);
    await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_INSTANCES && window.MathJax && MathJax.typesetPromise, null, { timeout: 60000 });
    await pause(1800);
    if (o.apercu) {
      // Aperçu de la feuille cible (région PAGE, ligne 3) : PAS dans le dépôt, seulement pour comparer aux maquettes
      await page.addStyleTag({ content: `
        @media (min-width:768px){
          main, main#si-content{ max-width:none !important; padding:1.5rem 1.5rem 3rem !important; }
          .chapter.active{ max-width:56rem; margin:0 auto; background:var(--sheet); border-radius:16px; box-shadow:var(--sh-sheet); border-top:4px solid var(--chap-vif); overflow:clip; }
          .toc{ display:none !important; } .toc-wrapper{ display:block !important; }
          section.panel{ padding:2.25rem 2.5rem 3rem 0; position:relative; }
          section.panel:not([id$="-cours"]):not([id$="-meth"]){ padding-left:2.5rem; }
          section.panel[id$="-cours"]::before, section.panel[id$="-meth"]::before{ content:""; position:absolute; top:0; bottom:0; left:calc(var(--margin-col) - 1.25rem); width:1px; background:var(--marge); }
          nav.tabs, .chap-title-banner{ background:var(--chap-fond) !important; }
        }
        @media (max-width:767px){ main, main#si-content{ padding:1rem 1rem 3rem !important; background:var(--sheet); } body{ background:var(--sheet); } }
      ` });
      await pause(300);
    }
    if (o.sol) {
      await page.evaluate(() => {
        const p = Array.from(document.querySelectorAll('.chapter.active .panel.active')).find(x => x.offsetParent);
        if (!p) return;
        p.querySelectorAll('.toggle-sol').forEach(b => { const s = b.nextElementSibling; if (s && !s.classList.contains('shown')) b.click(); });
        p.querySelectorAll('.reveal').forEach(r => r.classList.add('open'));
      });
      await pause(1500);
    }
    if (o.js) { await page.evaluate(o.js); await pause(600); }
    if (o.sel) { await page.evaluate(s => { const e = Array.from(document.querySelectorAll(s)).find(x => x.offsetParent); if (e) e.scrollIntoView({ block: 'start' }); }, o.sel.replace(/~/g, ' ')); await pause(500); }
    if (o.scroll) { await page.evaluate(n => window.scrollTo(0, n), +o.scroll); await pause(500); }
    const info = await page.evaluate(() => {
      const W = document.documentElement.clientWidth;
      const p = Array.from(document.querySelectorAll('.chapter.active .panel.active')).find(x => x.offsetParent);
      const debords = [];
      if (p) p.querySelectorAll('*').forEach(e => {
        if (e.offsetParent === null || debords.length >= 5) return;
        const r = e.getBoundingClientRect();
        if (r.right <= W + 1 || e.parentElement.getBoundingClientRect().right > W + 1) return;
        debords.push(e.tagName.toLowerCase() + '.' + e.className + ' → ' + Math.round(r.right));
      });
      return { sw: document.documentElement.scrollWidth, W, debords };
    });
    await page.screenshot({ path: path.join(sortie, nom + '.png'), fullPage: !!o.plein });
    bilan.push({ nom, ...info, erreurs });
    await ctx.close();
  }
  console.log(JSON.stringify(bilan, null, 1));
  await nav.close();
  await srv.fermer();
})().catch(e => { console.error(e); process.exit(1); });
