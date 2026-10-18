/* Compare les styles calculés de deux versions du site (même DOM, CSS rangé
   différemment) : chapitres choisis (tous leurs panneaux), coquille, fenêtres
   ouvertes, en clair / sombre / téléphone.
   Usage : node compare-styles.js <racineA> <racineB> [sortie.json] */
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');
const [racA, racB, sortie] = process.argv.slice(2);
const { demarrerServeur } = require(path.join(racB, 'tests/lib/serveur.js'));
const pause = ms => new Promise(r => setTimeout(r, ms));

const ETATS = [
  { nom: 'ordi-clair', vp: [1280, 900], theme: 'light' },
  { nom: 'ordi-sombre', vp: [1280, 900], theme: 'dark' },
  { nom: 'tel-clair', vp: [390, 844], theme: 'light' },
];
const CHAPS = ['rlc', 'slci', 'optgeo'];

async function releve(url, etat) {
  const nav = await chromium.launch();
  const ctx = await nav.newContext({ viewport: { width: etat.vp[0], height: etat.vp[1] }, serviceWorkers: 'block', reducedMotion: 'reduce' });
  await ctx.addInitScript(t => { try { localStorage.setItem('theme', t); } catch (e) {} }, etat.theme);
  const page = await ctx.newPage();
  await page.goto(url + 'index.html#rlc/cours');
  await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_INSTANCES, null, { timeout: 60000 });
  await pause(1500);
  const res = {};
  const prendre = async (etiquette) => {
    res[etiquette] = await page.evaluate((CHAPS) => {
      const props = Array.from(getComputedStyle(document.body)).filter(p => !/^(transition|animation)/.test(p));
      const out = {};
      const chemin = el => { const p = []; while (el && el !== document.body) { let i = 0, s = el; while ((s = s.previousElementSibling)) i++; p.unshift(el.tagName + ':' + i + (el.id ? '#' + el.id : '')); el = el.parentElement; } return p.join('/'); };
      const garder = el => { const ch = el.closest('.chapter'); return !ch || CHAPS.includes(ch.id.replace('chap-', '')); };
      const els = Array.from(document.body.querySelectorAll('*')).filter(el => !el.closest('mjx-container') && garder(el));
      for (const el of els) {
        const cs = getComputedStyle(el);
        const v = {};
        for (const p of props) v[p] = cs.getPropertyValue(p);
        for (const pe of ['::before', '::after']) { const c = getComputedStyle(el, pe); if (c.content && c.content !== 'none') { v[pe + 'content'] = c.content; v[pe + 'color'] = c.color; v[pe + 'display'] = c.display; } }
        out[chemin(el)] = v;
      }
      return out;
    }, CHAPS);
  };
  await prendre('chargement');
  const actions = [
    ['tiroir', () => { (document.getElementById(innerWidth < 768 ? 'mob-menu-btn' : 'nav-toggle-btn')).click(); }],
    ['quiz', async () => { document.getElementById('quiz-btn').click(); await new Promise(r => setTimeout(r, 200)); document.getElementById('quiz-start-btn').click(); await new Promise(r => setTimeout(r, 300)); document.getElementById('quiz-reveal-btn').click(); }],
    ['aujourdhui', () => window.todayOpen()],
    ['bilan', () => document.getElementById('dash-btn').click()],
    ['recherche', async () => { document.getElementById('search-btn').click(); const i = document.getElementById('search-input'); i.value = 'résonance'; i.dispatchEvent(new Event('input', { bubbles: true })); await new Promise(r => setTimeout(r, 600)); }],
    ['flash', async () => { location.hash = '#rlc/flash'; await new Promise(r => setTimeout(r, 600)); window.FLASH_INSTANCES.rlc.flip(); await new Promise(r => setTimeout(r, 600)); }],
    ['exos', async () => { location.hash = '#slci/exos'; await new Promise(r => setTimeout(r, 600)); document.querySelectorAll('#chap-slci .toggle-sol').forEach(b => b.click()); }],
  ];
  for (const [n, f] of actions) {
    try { await page.evaluate(f); await pause(500); await prendre(n); } catch (e) { res[n] = { erreur: String(e.message).split('\n')[0] }; }
    await page.keyboard.press('Escape').catch(() => {}); await pause(200);
    await page.evaluate(() => { document.querySelectorAll('.open').forEach(o => { if (/overlay|modal/.test(o.className)) o.classList.remove('open'); }); if (window.quizClose) try { window.quizClose(); } catch (e) {} }).catch(() => {});
  }
  await nav.close();
  return res;
}

(async () => {
  const srvA = await demarrerServeur(racA), srvB = await demarrerServeur(racB);
  const rapport = [];
  for (const etat of ETATS) {
    const A = await releve(srvA.url, etat), B = await releve(srvB.url, etat);
    for (const k of Object.keys(A)) {
      const a = A[k], b = B[k] || {};
      let n = 0, diffs = [];
      for (const el of Object.keys(a)) {
        if (!b[el]) { diffs.push({ el, manque: true }); continue; }
        for (const p of Object.keys(a[el])) if (a[el][p] !== b[el][p]) { n++; if (diffs.length < 40) diffs.push({ el, p, a: a[el][p], b: b[el][p] }); }
      }
      console.log(etat.nom, k, Object.keys(a).length, 'éléments,', n, 'différences');
      if (n || diffs.length) rapport.push({ etat: etat.nom, etape: k, n, diffs });
    }
  }
  if (sortie) fs.writeFileSync(sortie, JSON.stringify(rapport, null, 1));
  await srvA.fermer(); await srvB.fermer();
})().catch(e => { console.error(e); process.exit(1); });
