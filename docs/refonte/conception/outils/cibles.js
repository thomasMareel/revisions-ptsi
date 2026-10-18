// Cibles tactiles des maquettes TÉLÉPHONE (pointer: coarse émulé) : chaque élément
// interactif visible doit mesurer ≥ 44 × 44 px (règle du projet) — au minimum 24 px
// (WCAG 2.5.8). Exceptions documentées : liens dans une phrase (WCAG 2.5.8, exception « inline »).
const path = require('path'), fs = require('fs');
const { chromium } = require('playwright');
const ROOT = path.join(__dirname, '..'), M = path.join(ROOT, 'maquettes');
const PAGES = fs.readdirSync(M).filter(f => /telephone/.test(f) && f.endsWith('.html')).sort();
(async () => {
  const b = await chromium.launch({ env: Object.assign({}, process.env, { FONTCONFIG_FILE: '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/ptspe/fonts-sans-lm.conf' }) });
  const out = [];
  for (const f of PAGES) {
    const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
    const p = await ctx.newPage(); await p.goto('file://' + path.join(M, f));
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    const r = await p.evaluate(() => [...document.querySelectorAll('button, a, input, [role=button], .reveal, .mat-tab')].filter(e => {
      const s = getComputedStyle(e), q = e.getBoundingClientRect();
      if (q.width < 1 || s.visibility === 'hidden' || e.closest('.scrim') ) return false;
      if (document.querySelector('.scrim') && !e.closest('.bsheet')) return false;
      if (e.tagName === 'A' && e.closest('p, .statement, .exo-source')) return false;   // lien dans une phrase
      return true;
    }).map(e => { const q = e.getBoundingClientRect(); return { t: (e.getAttribute('aria-label') || e.textContent || e.placeholder || '').trim().replace(/\s+/g, ' ').slice(0, 30), w: Math.round(q.width), h: Math.round(q.height) }; }));
    const bad44 = r.filter(x => x.w < 44 || x.h < 44), bad24 = r.filter(x => x.w < 24 || x.h < 24);
    out.push({ page: f, cibles: r.length, sous44: bad44, sous24: bad24.length });
    console.log(f.padEnd(40), r.length, 'cibles ; < 44 px :', bad44.length, bad44.slice(0, 6).map(x => `« ${x.t} » ${x.w}×${x.h}`).join(' ; '), '; < 24 px :', bad24.length);
    await ctx.close();
  }
  fs.writeFileSync(path.join(ROOT, 'controles', 'cibles-tactiles.json'), JSON.stringify(out, null, 1));
  await b.close();
})();
