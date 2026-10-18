// Captures Playwright des maquettes (fenêtre + page entière) et contrôles de base :
// débordement horizontal, polices réellement chargées, erreurs, requêtes externes.
// NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node outils/capture.js [filtre]
const path = require('path'), fs = require('fs');
const { chromium } = require('playwright');
const ROOT = path.join(__dirname, '..'), M = path.join(ROOT, 'maquettes'), C = path.join(ROOT, 'captures');
fs.mkdirSync(path.join(C, 'pleine'), { recursive: true });
const D = { w: 1440, h: 900, mob: false }, P = { w: 390, h: 844, mob: true };
const LIST = [
  ['01-chapitre-ordinateur', D], ['02-chapitre-telephone', P], ['02b-chapitre-telephone-defile', P],
  ['03a-navigation-ordinateur', D], ['03b-navigation-telephone', P], ['03c-navigation-telephone-filtre', P],
  ['04a-carte-recto-telephone', P], ['04b-carte-verso-telephone', P], ['05-aujourdhui-telephone', P],
  ['06a-chapitre-sombre-ordinateur', D], ['06b-chapitre-sombre-telephone', P],
  ['07a-theme-ordinateur', D], ['07b-theme-telephone', P, 'light'], ['07b-theme-telephone', P, 'dark'],
  ['08a-exercices-ordinateur', D], ['08b-simulateur-ordinateur', D], ['08c-simulateur-telephone', P],
  ['09-specimen-clair', { w: 1240, h: 900, mob: false }], ['09-specimen-sombre', { w: 1240, h: 900, mob: false }],
];
(async () => {
  const filt = process.argv[2];
  const b = await chromium.launch({ env: Object.assign({}, process.env, { FONTCONFIG_FILE: '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/ptspe/fonts-sans-lm.conf' }) });
  const report = [];
  for (const [name, v, scheme] of LIST) {
    if (filt && !name.includes(filt)) continue;
    const ctx = await b.newContext({ viewport: { width: v.w, height: v.h }, deviceScaleFactor: v.mob ? 2 : 1, isMobile: v.mob, hasTouch: v.mob, colorScheme: scheme || 'light' });
    const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', e => errs.push('JS ' + e.message)); p.on('requestfailed', r => errs.push('ÉCHEC ' + r.url()));
    p.on('request', r => { if (!r.url().startsWith('file:') && !r.url().startsWith('data:')) errs.push('EXTERNE ' + r.url()); });
    p.on('console', m => { if (m.type() === 'error') errs.push('console ' + m.text()); });
    await p.goto('file://' + path.join(M, name + '.html'));
    await p.waitForFunction(() => window.MathJax && MathJax.startup && MathJax.startup.promise, null, { timeout: 15000 });
    await p.evaluate(() => MathJax.startup.promise); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(700);
    const info = await p.evaluate(() => ({
      debordement: document.documentElement.scrollWidth - window.innerWidth,
      polices: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + (f.style === 'italic' ? ' it.' : '')).filter((x, i, a) => a.indexOf(x) === i),
      formules: document.querySelectorAll('mjx-container').length,
      hauteur: document.documentElement.scrollHeight,
      sous12: [...document.querySelectorAll('body *')].filter(e => [...e.childNodes].some(n => n.nodeType === 3 && n.data.trim()) && e.getBoundingClientRect().width > 0 && !e.closest('svg,mjx-container,.sr') && parseFloat(getComputedStyle(e).fontSize) < 11.95).map(e => e.textContent.trim().slice(0, 30) + ' (' + getComputedStyle(e).fontSize + ')').slice(0, 10),
    }));
    const tag = name + (scheme ? '-' + (scheme === 'dark' ? 'systeme-sombre' : 'systeme-clair') : '');
    await p.screenshot({ path: path.join(C, tag + '.png') });
    await p.screenshot({ path: path.join(C, 'pleine', tag + '-page.png'), fullPage: true });
    report.push({ tag, ...info, erreurs: errs });
    console.log(tag, JSON.stringify(info), errs.join(' | '));
    await ctx.close();
  }
  if (!filt) fs.writeFileSync(path.join(C, 'rapport-captures.json'), JSON.stringify(report, null, 1));
  await b.close();
})();
