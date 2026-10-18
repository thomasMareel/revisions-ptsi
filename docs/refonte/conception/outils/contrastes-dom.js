// Contrôle des contrastes dans les MAQUETTES RENDUES : pour chaque élément visible
// portant du texte (formules MathJax comprises) ou une icône, couleur réelle contre le
// fond réel (premier fond opaque des ancêtres, transparences composées), seuil WCAG AA
// (4,5:1 ; 3:1 pour le grand texte ≥ 24 px ou ≥ 18,66 px gras, et pour les icônes).
// Chaque maquette est contrôlée dans le thème clair ET dans le thème sombre.
const path = require('path'), fs = require('fs');
const { chromium } = require('playwright');
const ROOT = path.join(__dirname, '..'), M = path.join(ROOT, 'maquettes');
const PAGES = fs.readdirSync(M).filter(f => f.endsWith('.html')).sort();
(async () => {
  const b = await chromium.launch({ env: Object.assign({}, process.env, { FONTCONFIG_FILE: '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/ptspe/fonts-sans-lm.conf' }) });
  const out = []; let fails = 0, total = 0;
  for (const f of PAGES) for (const theme of ['light', 'dark']) {
    const mob = /telephone/.test(f);  // 390 × 844 ; ordinateur 1440 × 900
    const ctx = await b.newContext({ viewport: { width: mob ? 390 : 1440, height: mob ? 844 : 900 }, deviceScaleFactor: 1, colorScheme: theme });
    const p = await ctx.newPage();
    await p.goto('file://' + path.join(M, f));
    await p.waitForFunction(() => window.MathJax && MathJax.startup && MathJax.startup.promise);
    await p.evaluate(() => MathJax.startup.promise); await p.evaluate(() => document.fonts.ready);
    // Thème tel que le pose le JS publié : data-theme="dark" (effectif) + data-theme-pref
    await p.evaluate(t => { const r = document.documentElement; if (t === 'dark') { r.setAttribute('data-theme', 'dark'); r.setAttribute('data-theme-pref', 'dark'); } else { r.removeAttribute('data-theme'); r.setAttribute('data-theme-pref', 'light'); } }, theme);
    await p.waitForTimeout(250);
    const r = await p.evaluate(() => {
      const parse = s => {
        let m = s.match(/^rgba?\(([^)]+)\)/);
        if (m) { const v = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return [v[0], v[1], v[2], v.length > 3 ? v[3] : 1]; }
        m = s.match(/^color\(srgb ([^)]+)\)/);
        if (m) { const v = m[1].split(/[ /]+/).filter(Boolean).map(Number); return [v[0] * 255, v[1] * 255, v[2] * 255, v.length > 3 ? v[3] : 1]; }
        return null;
      };
      const comp = (fg, bg) => [0, 1, 2].map(i => fg[i] * fg[3] + bg[i] * (1 - fg[3])).concat(1);
      const lum = c => c.slice(0, 3).map(v => { v /= 255; return v <= .04045 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }).reduce((a, v, i) => a + v * [.2126, .7152, .0722][i], 0);
      const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); };
      function bgOf(el) {
        const stack = [];
        for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
          const c = parse(getComputedStyle(e).backgroundColor);
          if (c && c[3] > 0) { stack.push(c); if (c[3] >= 1) break; }
        }
        let bg = [255, 255, 255, 1];
        for (let i = stack.length - 1; i >= 0; i--) bg = comp(stack[i], bg);
        return bg;
      }
      const hidden = el => { for (let e = el; e && e.nodeType === 1; e = e.parentElement) { const s = getComputedStyle(e); if (s.display === 'none' || s.visibility === 'hidden' || +s.opacity === 0) return true; } return false; };
      const scrim = document.querySelector('.scrim');
      const rows = [];
      const els = [...document.querySelectorAll('body *')];
      for (const el of els) {
        if (el.closest('script,style,svg defs,.sr,mjx-assistive-mml')) continue;
        if (scrim && !el.closest('.bsheet')) continue;          // contenu volontairement voilé
        const isIcon = el.matches('svg.ic');
        const isDot = el.matches('.dot');           // pastille de matière : élément graphique (3:1)
        if (isDot) { const r0 = el.getBoundingClientRect(); if (r0.width < 1 || hidden(el)) continue;
          const fgd = parse(getComputedStyle(el).backgroundColor); const bgd = bgOf(el.parentElement); const rr0 = ratio(fgd[3] < 1 ? comp(fgd, bgd) : fgd, bgd);
          rows.push({ txt: '[pastille ' + (el.closest('[data-mat]') || {}).dataset?.mat + ']', ratio: Math.round(rr0 * 100) / 100, seuil: 3, ok: rr0 >= 2.995, size: 0, cls: 'dot' }); continue; }
        const hasText = !isIcon && [...el.childNodes].some(n => n.nodeType === 3 && n.data.trim()) || el.matches('mjx-c');
        if (!isIcon && !hasText) continue;
        const rect = el.getBoundingClientRect(); if (rect.width < 1 || rect.height < 1 || hidden(el)) continue;
        const cs = getComputedStyle(el);
        let fg = parse(isIcon ? cs.color : cs.color); if (!fg) continue;
        const bg = bgOf(el); if (fg[3] < 1) fg = comp(fg, bg);
        const size = parseFloat(cs.fontSize), w = +cs.fontWeight;
        const large = size >= 24 || (size >= 18.66 && w >= 700);
        const th = isIcon || large ? 3 : 4.5;
        const rr = ratio(fg, bg);
        const txt = isIcon ? '[icône ' + ((el.querySelector('use') || {}).getAttribute ? el.querySelector('use').getAttribute('href') : '') + ']' : (el.matches('mjx-c') ? '[formule]' : el.textContent.trim().slice(0, 50));
        rows.push({ txt, ratio: Math.round(rr * 100) / 100, seuil: th, ok: rr >= th - 0.005, size: Math.round(size * 10) / 10, cls: (el.className && el.className.baseVal === undefined ? el.className : (el.className.baseVal || '')).toString().slice(0, 40) });
      }
      return rows;
    });
    const bad = r.filter(x => !x.ok); fails += bad.length; total += r.length;
    const min = r.reduce((a, x) => (!a || x.ratio / x.seuil < a.ratio / a.seuil) ? x : a, null);
    out.push({ page: f, theme, mesures: r.length, echecs: bad.length, plusFaible: min, detailEchecs: bad.slice(0, 30) });
    console.log(`${f.padEnd(40)} ${theme.padEnd(5)} ${String(r.length).padStart(5)} éléments  échecs ${bad.length}  plus faible ${min ? min.ratio + ':1 (seuil ' + min.seuil + ') « ' + min.txt + ' »' : '-'}`);
    for (const x of bad.slice(0, 8)) console.log('    ÉCHEC', JSON.stringify(x));
    await ctx.close();
  }
  fs.mkdirSync(path.join(ROOT, 'controles'), { recursive: true });
  fs.writeFileSync(path.join(ROOT, 'controles', 'contrastes-maquettes.json'), JSON.stringify({ total, echecs: fails, pages: out }, null, 1));
  console.log(`TOTAL ${total} mesures, ${fails} échecs`);
  await b.close(); process.exit(fails ? 1 : 0);
})();
