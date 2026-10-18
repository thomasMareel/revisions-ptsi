// Mesures typographiques sur les maquettes : signes par ligne, corps, début du texte au téléphone.
const path = require('path'); const { chromium } = require('playwright');
const M = path.join(__dirname, '..', 'maquettes');
(async () => {
  const b = await chromium.launch({ env: Object.assign({}, process.env, { FONTCONFIG_FILE: '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/ptspe/fonts-sans-lm.conf' }) });
  for (const [f, w, h] of [['01-chapitre-ordinateur.html', 1440, 900], ['02-chapitre-telephone.html', 390, 844]]) {
    const p = await (await b.newContext({ viewport: { width: w, height: h } })).newPage();
    await p.goto('file://' + path.join(M, f)); await p.waitForFunction(() => window.MathJax && MathJax.startup && MathJax.startup.promise); await p.evaluate(() => MathJax.startup.promise); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
    const r = await p.evaluate(() => {
      const ps = [...document.querySelectorAll('.panel p')].filter(e => !e.closest('.def-box,.prop-box,.notice,.reveal,.method-box'));
      let lines = 0, chars = 0, full = [];
      for (const e of ps) {
        const n = Math.round(e.getBoundingClientRect().height / parseFloat(getComputedStyle(e).lineHeight));
        if (n >= 3) { const t = e.textContent.replace(/\s+/g, ' ').trim().length; full.push(t / (n - 0.5)); }   // dernière ligne comptée pour moitié
        lines += n; chars += e.textContent.replace(/\s+/g, ' ').trim().length;
      }
      const sec = document.querySelector('.panel .sec-t');
      const p0 = document.querySelector('.panel p');
      return { corps: getComputedStyle(p0).fontSize, interligne: getComputedStyle(p0).lineHeight, largeurColonne: Math.round(p0.getBoundingClientRect().width),
        signesParLigne: Math.round(full.reduce((a, x) => a + x, 0) / full.length), debutTexte: Math.round((sec || p0).getBoundingClientRect().top),
        h1: getComputedStyle(document.querySelector('.chap-h1, .mbar-h')).fontSize };
    });
    console.log(f, JSON.stringify(r));
  }
  await b.close();
})();
