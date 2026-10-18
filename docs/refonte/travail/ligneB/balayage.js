/* Balayage du contenu : mesurerEcran (suite visuel) appliqué aux PANNEAUX de chapitres choisis,
   clair/sombre × ordinateur/téléphone, solutions et mémos dépliés.
   Usage : node balayage.js <racine> <sortie> <chap/onglet,chap/onglet,…> [captures] */
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');
const [racine, sortie, listeArg, capturesArg] = process.argv.slice(2);
fs.mkdirSync(sortie, { recursive: true });
// mesurerEcran recopié de la suite visuel (fonction autonome, sérialisée par page.evaluate)
const src = fs.readFileSync(path.join(racine, 'tests/suites/visuel.js'), 'utf8');
const i0 = src.indexOf('function mesurerEcran(o) {');
let prof = 0, i1 = src.indexOf('{', i0);
for (let k = i1; k < src.length; k++) { if (src[k] === '{') prof++; else if (src[k] === '}') { prof--; if (!prof) { i1 = k + 1; break; } } }
const mesurerEcran = new Function('return (' + src.slice(i0, i1) + ')')();
const { demarrerServeur } = require(path.join(racine, 'tests/lib/serveur.js'));
const pause = ms => new Promise(r => setTimeout(r, ms));
const APP = [{ nom: 'ordi', w: 1440, h: 900, mobile: false }, { nom: 'tel', w: 390, h: 844, mobile: true }];
(async () => {
  const srv = await demarrerServeur(racine);
  const nav = await chromium.launch();
  const liste = listeArg.split(',');
  const tous = [], erreurs = [];
  for (const app of APP) for (const theme of ['clair', 'sombre']) {
    const ctx = await nav.newContext({ viewport: { width: app.w, height: app.h }, serviceWorkers: 'block', isMobile: app.mobile, hasTouch: app.mobile });
    await ctx.addInitScript(t => { try { localStorage.setItem('theme', t); } catch (e) {} }, theme === 'sombre' ? 'dark' : 'light');
    const page = await ctx.newPage();
    let lieu = '';
    page.on('pageerror', e => erreurs.push(app.nom + '/' + theme + ' ' + lieu + ' : ' + String(e.message).slice(0, 200)));
    page.on('console', m => { if (m.type() === 'error' && !/Service Worker/.test(m.text())) erreurs.push(app.nom + '/' + theme + ' ' + lieu + ' console : ' + m.text().slice(0, 200)); });
    await page.goto(srv.url + 'index.html#rlc/cours');
    await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_INSTANCES && window.MathJax && MathJax.typesetPromise, null, { timeout: 60000 });
    await pause(1200);
    for (const item of liste) {
      lieu = item;
      const [chap, onglet] = item.split('/');
      await page.evaluate(h => { location.hash = '#' + h; }, item);
      await pause(500);
      const pid = await page.evaluate(([c, o]) => CHAPTERS_BY_ID[c] ? CHAPTERS_BY_ID[c].prefix + '-' + o : null, [chap, onglet]);
      if (!pid) { erreurs.push('chapitre inconnu ' + item); continue; }
      // rendu MathJax du panneau
      await page.waitForFunction(id => { const p = document.getElementById(id); return p && (p.querySelector('mjx-container') || !/\\\(|\$\$/.test(p.textContent)); }, pid, { timeout: 8000 }).catch(() => {});
      await page.evaluate(id => {
        const p = document.getElementById(id);
        p.querySelectorAll('.toggle-sol').forEach(b => { const s = b.nextElementSibling; if (s && !s.classList.contains('shown')) b.click(); });
        p.querySelectorAll('.reveal:not(.open)').forEach(r => r.click());
      }, pid);
      await pause(900);
      await page.evaluate(async () => { await document.fonts.ready; });
      const m = await page.evaluate(mesurerEcran, { racines: ['#' + pid], mobile: app.mobile });
      for (const c of m.constats) tous.push(Object.assign({ item, theme, app: app.nom }, c));
      if (m.scrollWidth > m.W + 1) tous.push({ item, theme, app: app.nom, mesure: 'page', selecteur: 'scrollWidth', valeur: m.scrollWidth });
      if (capturesArg) {
        const el = await page.$('#' + pid);
        try { await el.screenshot({ path: path.join(sortie, app.nom + '-' + theme + '-' + item.replace('/', '-') + '.png') }); } catch (e) { erreurs.push('capture ' + item + ' ' + e.message.slice(0, 80)); }
      }
    }
    await ctx.close();
  }
  fs.writeFileSync(path.join(sortie, 'balayage.json'), JSON.stringify({ tous, erreurs }, null, 1));
  // Résumé par (mesure, sélecteur)
  const g = new Map();
  for (const c of tous) {
    const k = c.mesure + ' | ' + c.selecteur;
    const x = g.get(k) || { n: 0, pire: c.valeur, ou: new Set(), ex: c.exemples ? c.exemples[0] : null };
    x.n++; x.ou.add(c.item + ' ' + c.app + '/' + c.theme);
    if ((c.mesure === 'debordement' || c.mesure === 'page') ? c.valeur > x.pire : c.valeur < x.pire) x.pire = c.valeur;
    g.set(k, x);
  }
  for (const [k, x] of g) console.log(k, '→ pire', x.pire, '×' + x.n, '|', Array.from(x.ou).slice(0, 4).join(' ; '), x.ex ? '| ex : ' + JSON.stringify(x.ex).slice(0, 160) : '');
  console.log('constats :', tous.length, '| erreurs JS :', erreurs.length);
  erreurs.slice(0, 10).forEach(e => console.log('  ' + e));
  await nav.close(); await srv.fermer();
})().catch(e => { console.error(e); process.exit(1); });
