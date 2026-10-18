/* Analyse du DOM du contenu (structure réelle des 160 chapitres). Usage : node analyse.js <racine> */
const path = require('path');
const { chromium } = require('playwright');
const [racine] = process.argv.slice(2);
const { demarrerServeur } = require(path.join(racine, 'tests/lib/serveur.js'));
(async () => {
  const srv = await demarrerServeur(racine);
  const nav = await chromium.launch();
  const ctx = await nav.newContext({ viewport: { width: 1440, height: 900 }, serviceWorkers: 'block' });
  const page = await ctx.newPage();
  await page.goto(srv.url + 'index.html#rlc/cours');
  await page.waitForFunction(() => typeof CHAPTERS !== 'undefined' && window.FLASH_INSTANCES, null, { timeout: 60000 });
  const r = await page.evaluate(() => {
    const cnt = (m, k) => { m[k] = (m[k] || 0) + 1; };
    const desc = e => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).join('.') : '');
    const out = {};
    // Enfants des .sim-wrapper
    out.sim = {};
    document.querySelectorAll('.sim-wrapper').forEach(w => cnt(out.sim, Array.from(w.children).map(desc).join(' > ')));
    // Enfants directs des .course-section (tags), texte direct
    out.csChild = {}; out.csTexte = [];
    document.querySelectorAll('.course-section').forEach(cs => {
      Array.from(cs.children).forEach(c => cnt(out.csChild, desc(c).split('.').slice(0, 2).join('.')));
      Array.from(cs.childNodes).forEach(n => { if (n.nodeType === 3 && n.textContent.trim()) out.csTexte.push((cs.closest('.panel') || {}).id + ' : ' + n.textContent.trim().slice(0, 60)); });
    });
    out.csTexte = out.csTexte.slice(0, 30);
    // Premier enfant des course-section
    out.csPremier = {};
    document.querySelectorAll('.course-section').forEach(cs => cnt(out.csPremier, cs.firstElementChild ? desc(cs.firstElementChild).split('.').slice(0, 2).join('.') : '(vide)'));
    // Enfants directs des panneaux (hors flash/simu), après le sommaire
    out.panelChild = {};
    document.querySelectorAll('section.panel').forEach(p => {
      if (/-(flash|simu)$/.test(p.id)) return;
      const root = p.querySelector(':scope > .toc-wrapper > .toc-content') || p;
      Array.from(root.children).forEach(c => cnt(out.panelChild, desc(c).split('.').slice(0, 2).join('.')));
    });
    // Panneaux simu sans sim-wrapper
    out.simuSansWrapper = Array.from(document.querySelectorAll('section.panel[id$="-simu"]')).filter(p => !p.querySelector('.sim-wrapper')).map(p => p.id + ' : ' + Array.from(p.children).map(desc).join(' > ').slice(0, 200));
    // Tables : parent
    out.tableParent = {};
    document.querySelectorAll('section.panel table').forEach(t => cnt(out.tableParent, desc(t.parentElement).split('.').slice(0, 2).join('.') + (t.parentElement.getAttribute('style') ? '[style]' : '')));
    out.nbTables = document.querySelectorAll('section.panel table').length;
    // SVG : parent
    out.svgParent = {};
    document.querySelectorAll('section.panel svg').forEach(s => { if (s.closest('mjx-container') || s.closest('button')) return; cnt(out.svgParent, desc(s.parentElement).split('.').slice(0, 2).join('.')); });
    // pre / code / codeblock
    out.pre = document.querySelectorAll('section.panel pre').length;
    out.codeblock = document.querySelectorAll('section.panel .codeblock').length;
    out.codeTags = {}; document.querySelectorAll('section.panel .codeblock').forEach(c => cnt(out.codeTags, c.tagName));
    out.code = document.querySelectorAll('section.panel code').length;
    out.codeInline = document.querySelectorAll('section.panel .code-inline').length;
    // Exercices
    out.exo = document.querySelectorAll('.exo').length;
    out.exoHorsWrapper = Array.from(document.querySelectorAll('.exo')).filter(e => !e.closest('.exo-wrapper')).length;
    out.diffTxt = {}; document.querySelectorAll('.exo .diff').forEach(d => cnt(out.diffTxt, d.textContent.trim()));
    out.exoSansDiff = Array.from(document.querySelectorAll('.exo')).filter(e => !e.querySelector(':scope > .diff')).length;
    out.numConcours = {}; document.querySelectorAll('.exo.concours > .num').forEach(d => cnt(out.numConcours, d.textContent.trim()));
    out.numAutres = {}; document.querySelectorAll('.exo:not(.concours) > .num').forEach(d => cnt(out.numAutres, d.textContent.trim().replace(/\d+/, 'n')));
    out.exoEnfants = {}; document.querySelectorAll('.exo').forEach(e => Array.from(e.children).forEach(c => cnt(out.exoEnfants, desc(c).split('.').slice(0, 2).join('.'))));
    out.qPremier = {}; document.querySelectorAll('.exo .q').forEach(q => cnt(out.qPremier, q.firstElementChild ? desc(q.firstElementChild) + (q.firstChild === q.firstElementChild ? '' : '(texte avant)') : '(aucun)'));
    out.toggleTxt = {}; document.querySelectorAll('.toggle-sol').forEach(b => cnt(out.toggleTxt, b.textContent.trim()));
    out.toggleSuivant = {}; document.querySelectorAll('.toggle-sol').forEach(b => cnt(out.toggleSuivant, b.nextElementSibling ? desc(b.nextElementSibling) : '(rien)'));
    out.solH4 = {}; document.querySelectorAll('.solution').forEach(s => cnt(out.solH4, s.firstElementChild ? desc(s.firstElementChild) + ' ' + s.firstElementChild.textContent.trim().slice(0, 20) : '(vide)'));
    // Encadrés
    ['def-box', 'prop-box', 'method-box', 'notice', 'reveal', 'formula', 'hors-prog', 'video-resources', 'exo-source', 'exo-part', 'intro'].forEach(k => out['n_' + k] = document.querySelectorAll('.' + k).length);
    out.propPremier = {}; document.querySelectorAll('.prop-box').forEach(b => cnt(out.propPremier, b.firstElementChild ? desc(b.firstElementChild) + (b.firstChild === b.firstElementChild || !b.firstChild.textContent.trim() ? '' : '(texte avant)') : '(texte)'));
    out.methPremier = {}; document.querySelectorAll('.method-box').forEach(b => cnt(out.methPremier, b.firstElementChild ? desc(b.firstElementChild) + (b.firstChild === b.firstElementChild || !b.firstChild.textContent.trim() ? '' : '(texte avant)') : '(texte)'));
    out.step = document.querySelectorAll('.step').length;
    out.stepParent = {}; document.querySelectorAll('.step').forEach(s => cnt(out.stepParent, desc(s.parentElement) + ' < ' + desc(s.parentElement.parentElement) + (s.parentElement.firstChild === s ? '' : ' (pas 1er)')));
    out.revealEnfants = {}; document.querySelectorAll('.reveal').forEach(r => cnt(out.revealEnfants, Array.from(r.children).map(desc).join(' ')));
    out.revealAttr = {}; document.querySelectorAll('.reveal').forEach(r => cnt(out.revealAttr, (r.getAttribute('onclick') || '') + ' tab=' + r.getAttribute('tabindex') + ' role=' + r.getAttribute('role')));
    out.formulaConsec = document.querySelectorAll('.formula + .formula').length;
    out.formulaParent = {}; document.querySelectorAll('.formula').forEach(f => cnt(out.formulaParent, desc(f.parentElement).split('.').slice(0, 2).join('.')));
    // Couleurs codées en dur dans les styles inline du contenu ?
    out.styleInlineColor = 0; document.querySelectorAll('section.panel [style*="#"]').forEach(() => out.styleInlineColor++);
    // figure / figcaption
    out.figure = {}; document.querySelectorAll('section.panel figure').forEach(f => cnt(out.figure, desc(f)));
    out.figcaption = document.querySelectorAll('section.panel figcaption').length;
    out.img = document.querySelectorAll('section.panel img').length;
    // Lorentz
    out.lor = document.querySelectorAll('[id^="lor-"]').length;
    out.lorSimu = (document.getElementById('lor-simu') || {}).outerHTML ? document.getElementById('lor-simu').outerHTML.slice(0, 1500) : null;
    // inputs range hors sim-controls
    out.rangeHors = Array.from(document.querySelectorAll('input[type=range]')).filter(i => !i.closest('.sim-controls')).map(i => i.id + ' < ' + desc(i.parentElement) + ' < ' + desc(i.parentElement.parentElement));
    out.controlEnfants = {}; document.querySelectorAll('.sim-controls .control').forEach(c => cnt(out.controlEnfants, Array.from(c.children).map(desc).join(' ')));
    out.simControlsEnfants = {}; document.querySelectorAll('.sim-controls').forEach(c => Array.from(c.children).forEach(x => cnt(out.simControlsEnfants, desc(x))));
    out.simInfoEnfants = {}; document.querySelectorAll('.sim-info').forEach(c => Array.from(c.children).forEach(x => cnt(out.simInfoEnfants, Array.from(x.children).map(desc).join(' '))));
    out.regime = {}; document.querySelectorAll('.regime-badge').forEach(b => cnt(out.regime, b.id + ' ' + b.className));
    out.buttonsInSim = {}; document.querySelectorAll('.sim-wrapper button').forEach(b => { if (!b.closest('.mode-switch')) cnt(out.buttonsInSim, desc(b) + ' « ' + b.textContent.trim().slice(0, 30) + ' » < ' + desc(b.parentElement)); });
    return out;
  });
  console.log(JSON.stringify(r, null, 1));
  await nav.close(); await srv.fermer();
})().catch(e => { console.error(e); process.exit(1); });
