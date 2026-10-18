// Assemble les MAQUETTES FINALES (maquettes/*.html) à partir des extraits réels de
// index.html (src/*.html : DOM et classes du site), de la liste réelle des chapitres
// (donnees/chapitres.json), de tokens.css, composants.css et polices/polices.css.
// Aucune dépendance.   node outils/build.js
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..'), SRC = path.join(ROOT, 'src'), OUT = path.join(ROOT, 'maquettes');
fs.mkdirSync(OUT, { recursive: true });
const R = String.raw;
const rd = f => fs.readFileSync(path.join(SRC, f), 'utf8');
const CH = JSON.parse(fs.readFileSync(path.join(ROOT, 'donnees', 'chapitres.json'), 'utf8'));
const BY = {}; for (const m in CH) for (const s of CH[m]) for (const c of s.chapitres) BY[c.id] = Object.assign({ mat: m, part: s.label }, c);
const MATS = [['physique', 'Physique'], ['maths', 'Maths'], ['si', 'SI'], ['info', 'Info'], ['anglais', 'Anglais']];
const MATL = Object.fromEntries(MATS);
const inYear = (c, y) => c.annee === 0 || c.annee === y;
const effectif = (m, y) => CH[m].flatMap(s => s.chapitres).filter(c => inYear(c, y)).length;
const ic = (n, c = '') => `<svg class="ic ${c}" aria-hidden="true"><use href="#i-${n}"/></svg>`;
const sprite = `<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>\n${rd('sprite-site.svg')}\n${rd('sprite-extra.svg')}</defs></svg>`;
// État de démonstration plausible (cartes dues, épinglés, récents)
const DUE = { rlc: 3, filtres: 5, signaux: 2, premierordre: 1, cinept: 4, thermo2: 6, estat: 2, oxred: 3, maxwell: 4, slci: 2, cine: 1 };
const PINNED = ['filtres', 'maxwell'];
const RECENTS = [['rlc', 'Cours · §3'], ['cine', 'Exercices'], ['slci', 'Cartes']];

// Petits scripts proposés pour le site (SPEC §7) — appliqués ici au chargement :
// « §1 · LES BASES » → <span class="sec-n">§1</span><span class="sec-t">LES BASES</span>
const split = h => h.replace(/<div class="sec-num">(§\d+)\s*·\s*([^<]*)<\/div>/g,
  '<div class="sec-num"><span class="sec-n">$1</span><span class="sec-t">$2</span></div>');
// « ★ ☆ ☆ » → <span class="diff" data-niveau="1"><span class="bars"><i></i><i></i><i></i></span>Facile</span>
const diffHtml = n => `<span class="diff" data-niveau="${n}" title="Difficulté ${n} sur 3"><span class="bars" aria-hidden="true"><i></i><i></i><i></i></span>${['', 'Facile', 'Moyen', 'Difficile'][n]}</span>`;
const diff = h => h.replace(/<span class="diff">([★☆ ]+)<\/span>/g, (m, s) => diffHtml((s.match(/★/g) || []).length));

function page({ title, theme = 'light', body, bodyCls = '', extraHead = '' }) {
  // Attributs du thème tels que les pose le JS publié : data-theme="dark" = thème
  // effectif sombre ; data-theme-pref = préférence. « auto » : seul le CSS décide ici.
  const attrs = theme === 'dark' ? 'data-theme="dark" data-theme-pref="dark"' : theme === 'auto' ? 'data-theme-pref="auto"' : 'data-theme-pref="light"';
  return R`<!doctype html>
<html lang="fr" ${attrs}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title}</title>
<link rel="stylesheet" href="../polices/polices.css">
<link rel="stylesheet" href="../tokens.css">
<link rel="stylesheet" href="../composants.css">
<script>
window.MathJax = {
  tex: {inlineMath: [['\\(', '\\)']], displayMath: [['$$', '$$']]},
  options: {renderActions: {addMenu: []}},
  chtml: {scale: 1.07, minScale: 0.5, matchFontHeight: false, mtextInheritFont: true}
};
</script>
<script defer src="../mathjax/tex-mml-chtml.js"></script>
<script>
// (SPEC §7.3) Typographie française et ponctuation collée aux formules, lancée
// après le rendu MathJax d'un panneau : espace fine insécable avant ; ! ? et
// insécable avant : » / après « ; une ponctuation qui suit une formule en ligne
// ne part plus seule à la ligne ; formule en ligne trop large → .mj-large.
document.addEventListener('DOMContentLoaded', () => MathJax.startup.promise.then(() => {
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, { acceptNode: n =>
    n.parentElement.closest('script,style,mjx-container,code,pre,kbd') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT });
  const ns = []; while (w.nextNode()) ns.push(w.currentNode);
  ns.forEach(t => { t.data = t.data.replace(/ ([;!?])/g, ' $1').replace(/ ([:»])/g, ' $1').replace(/« /g, '« '); });
  document.querySelectorAll('mjx-container:not([display="true"])').forEach(m => {
    const t = m.nextSibling;
    if (t && t.nodeType === 3) {
      const k = t.data.match(/^[   ]?[.,;:!?)\]…»]+/);
      if (k) { const s = document.createElement('span'); s.style.whiteSpace = 'nowrap';
        m.parentNode.insertBefore(s, m); s.appendChild(m); s.appendChild(document.createTextNode(k[0])); t.data = t.data.slice(k[0].length); }
    }
    const box = m.closest('p,li,div'); if (box && m.getBoundingClientRect().width > box.clientWidth) m.classList.add('mj-large');
  });
  document.querySelectorAll('.control input[type=range]').forEach(r => { const f = () => r.style.setProperty('--p', ((r.value - r.min) / (r.max - r.min) * 100) + '%'); f(); r.addEventListener('input', f); });
}));
</script>
${extraHead}
</head>
<body class="${bodyCls}">
${sprite}
${body}
</body>
</html>
`;
}
const write = (f, html) => { fs.writeFileSync(path.join(OUT, f), html); console.log('écrit', f); };

/* ---------------- Coquille ordinateur ---------------- */
const hdr = (opts = {}) => `
<header class="hdr">
  <button class="btn btn-ghost btn-icon" aria-label="Masquer la navigation">${ic('sidebar')}</button>
  <a class="brand" href="#"><span class="brand-mark" aria-hidden="true"></span><span class="brand-name">Mes cours de <em>prépa</em></span></a>
  <label class="field field-soft">${ic('search')}<input placeholder="Rechercher chapitre, formule, carte…"><span class="kbd kbd-hint">Ctrl K</span></label>
  <span class="spacer"></span>
  <button class="btn btn-ghost">${ic('calendar')}Aujourd'hui</button>
  <button class="btn btn-ghost">${ic('chart')}Bilan</button>
  <button class="btn btn-primary">${ic('refresh')}Réviser<span class="count">37</span>${ic('chev-down', 'ic-s')}</button>
  <span class="vsep"></span>
  <button class="btn btn-ghost btn-icon" aria-label="Thème : Auto (actuellement clair)" aria-haspopup="dialog" ${opts.themeOpen ? 'aria-expanded="true" style="background:var(--press);color:var(--text)"' : ''}>${ic('theme')}</button>
  <button class="btn btn-ghost btn-icon" aria-label="Plus">${ic('dots')}</button>
</header>`;

function navParts(mat, year, cur, openParts) {
  return CH[mat].map(s => {
    const items = s.chapitres.filter(c => inYear(c, year));
    if (!items.length) return '';
    const open = openParts.includes(s.label);
    const autres = year === 2 ? s.chapitres.filter(c => c.annee === 1).length : 0;
    const rows = open ? `<ul class="nav-list">${items.map(c => {
      const pin = PINNED.includes(c.id);
      return `<li><a class="nav-item${c.id === cur ? ' cur' : ''}" href="#" data-mat="${mat}"${c.id === cur ? ' aria-current="page"' : ''}>${c.court}<span class="end">${c.annee === 2 && year === 1 ? '<span class="tag2a">2A</span>' : ''}${DUE[c.id] ? `<span class="count count-soft" aria-label="${DUE[c.id]} cartes dues">${DUE[c.id]}</span>` : ''}${ic(pin ? 'star-fill' : 'star', 'ic-s pin' + (pin ? ' on' : ''))}</span></a></li>`;
    }).join('')}${autres ? `<li class="nav-more">${ic('book', 'ic-s')}+ ${autres} chapitres de 1ʳᵉ année</li>` : ''}</ul>` : '';
    return `<div class="nav-part"><button class="nav-part-h" aria-expanded="${open}">${ic('chev-down')}${s.label}<span class="n">${items.length}</span></button>${rows}</div>`;
  }).join('');
}
const matTabs = (cur, year = 1) => `<div class="mat-tabs" role="tablist" data-mat="${cur}">${MATS.map(([m, l]) => `<button class="mat-tab${m === cur ? ' on' : ''}" data-mat="${m}" role="tab" aria-selected="${m === cur}">${l}<span class="n">${effectif(m, year)}</span></button>`).join('')}</div>`;
const pinnedChips = () => PINNED.map(id => { const c = BY[id]; return `<a class="chip" href="#" data-mat="${c.mat}"><span class="dot"></span>${c.court}${c.annee === 2 ? '<span class="tag2a">2A</span>' : ''}</a>`; }).join('');
const recentRows = () => RECENTS.map(([id, w]) => { const c = BY[id]; return `<a class="recent-row" href="#" data-mat="${c.mat}"><span class="dot"></span>${c.court}<span class="where">${w}</span></a>`; }).join('');

function side({ mat = 'physique', year = 1, cur = 'rlc', open = ['Ondes & signaux'] } = {}) {
  return `
<aside class="side" aria-label="Chapitres">
  <div class="seg seg-block" role="group" aria-label="Année"><button aria-pressed="${year === 1}">1ʳᵉ&nbsp;année</button><button aria-pressed="${year === 2}">2ᵉ&nbsp;année</button></div>
  <label class="field field-soft" style="margin-top:.75rem">${ic('filter')}<input placeholder="Filtrer les 160 chapitres"></label>
  <div class="nav-block"><div class="kicker">Épinglés</div><div class="chips">${pinnedChips()}</div></div>
  <div class="nav-block"><div class="kicker">Récents</div>${recentRows()}</div>
  <div class="nav-block" style="margin-top:1.1rem">${matTabs(mat, year)}</div>
  <div data-mat="${mat}" style="margin-top:.5rem">${navParts(mat, year, cur, open)}</div>
</aside>`;
}

const TOC = ['Les bases', 'Mise en équation', 'Régime libre', 'Réponse à un échelon de tension', 'Régime sinusoïdal forcé', 'Résonance', 'Aspects énergétiques'];
const mesCartes = `
  <div class="card-mini" data-mat="physique">
    <div class="kicker">Mes cartes</div>
    <div style="margin-top:.6rem" class="big">10<small>acquises sur 26</small></div>
    <div class="stack" role="img" aria-label="10 acquises, 5 hésitantes, 3 à revoir, 8 jamais vues"><i class="s2" style="width:38.5%"></i><i class="s1" style="width:19.2%"></i><i class="s0" style="width:11.5%"></i></div>
    <div class="legend"><span><i style="background:var(--note-2-vif)"></i>10 acquises</span><span><i style="background:var(--note-1-vif)"></i>5 hésitantes</span><span><i style="background:var(--note-0-vif)"></i>3 à revoir</span><span><i style="background:var(--note-nv)"></i>8 jamais vues</span></div>
    <button class="btn btn-chap">${ic('refresh')}Réviser les 3 cartes dues</button>
  </div>`;
const rail = (on = 0) => `
<aside class="rail" aria-label="Dans ce chapitre" data-mat="physique">
  <div class="kicker toc-title">Dans ce chapitre</div>
  <ul class="toc-list">${TOC.map((t, i) => `<li><a href="#" class="${i === on ? 'on' : ''}"><span class="n">§${i + 1}</span>${t}</a></li>`).join('')}</ul>
  ${mesCartes}
</aside>`;
const EXOS = [['01', 1, 'Identification de régime'], ['02', 2, 'Réponse indicielle'], ['03', 2, 'Résonance en tension'], ['04', 2, 'Bande passante'], ['05', 3, 'Énergie et facteur de qualité'], ['06', 1, 'Lecture d\'un oscillogramme'], ['07', 3, 'Circuit bouchon'], ['PT', 3, 'Concours PT · RLC série']];
const railExos = `
<aside class="rail" aria-label="Exercices du chapitre" data-mat="physique">
  <div class="kicker toc-title">8 exercices</div>
  <ul class="exo-index">${EXOS.map(([n, d, t], i) => `<li><a href="#" class="${i === 0 ? 'on' : ''}"><span class="n">${n === 'PT' ? 'PT' : 'EXO ' + n}</span>${t}${diffHtml(d).replace(/>(Facile|Moyen|Difficile)</, '><span class="sr">$1</span><')}</a></li>`).join('')}</ul>
  ${mesCartes}
</aside>`;

const TABS = [['cours', 'Cours'], ['meth', 'Méthodes'], ['simu', 'Simulateur'], ['flash', 'Cartes'], ['exos', 'Exercices']];
const tabsDesk = (on) => `<nav class="tabs" role="tablist">${TABS.map(([k, l], i) => `<button class="tab${k === on ? ' active' : ''}" data-panel="rlc-${k}" role="tab" aria-selected="${k === on}"><span class="num">0${i + 1}</span>${l}${k === 'flash' ? ' <span class="cnt">26</span><span class="count" aria-label="3 cartes dues">3</span>' : k === 'exos' ? ' <span class="cnt">8</span>' : k === 'meth' ? ' <span class="cnt">4</span>' : ''}</button>`).join('')}</nav>`;
const chapHead = (on) => `
<header class="chap-head">
  <div class="crumb"><span class="dot"></span><a href="#"><b>Physique</b></a>${ic('chev-right')}<a href="#">Ondes &amp; signaux</a><span class="sep" style="color:var(--text-3)">·</span>Électrocinétique</div>
  <div class="chap-title-row"><h1 class="chap-h1">Circuit RLC série</h1>
    <div class="chap-actions"><button class="btn">${ic('function')}Formulaire</button><button class="btn btn-icon" aria-label="Imprimer le chapitre">${ic('printer')}</button><button class="btn btn-icon" aria-label="Épingler le chapitre">${ic('star')}</button></div></div>
  <div class="chap-meta"><span class="badge badge-out">1ʳᵉ&nbsp;année</span><span>7 sections</span><span class="sep">·</span><span>26 cartes</span><span class="sep">·</span><span>8 exercices</span><span class="sep">·</span><span>1 simulateur</span></div>
  ${tabsDesk(on)}
</header>`;

// Tableau de synthèse du §3 : balisage et styles inline identiques aux tableaux du site
const TABLE = R`<h3>En résumé : les trois régimes</h3>
  <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.82rem;margin:.5rem 0">
    <tr style="background:var(--surface)"><th style="padding:.3rem;border:1px solid var(--border)">Régime</th><th style="padding:.3rem;border:1px solid var(--border)">Condition</th><th style="padding:.3rem;border:1px solid var(--border)">Racines</th><th style="padding:.3rem;border:1px solid var(--border)">Solution homogène</th></tr>
    <tr><td style="padding:.3rem;border:1px solid var(--grid)">Pseudo-périodique</td><td style="border:1px solid var(--grid)">\(Q > 1/2\)</td><td style="border:1px solid var(--grid)">complexes conjuguées</td><td style="border:1px solid var(--grid)">\(e^{-t/\tau}(A\cos\omega t + B\sin\omega t)\)</td></tr>
    <tr><td style="padding:.3rem;border:1px solid var(--grid)">Critique</td><td style="border:1px solid var(--grid)">\(Q = 1/2\)</td><td style="border:1px solid var(--grid)">double, \(r = -\omega_0\)</td><td style="border:1px solid var(--grid)">\((A + Bt)\,e^{-\omega_0 t}\)</td></tr>
    <tr><td style="padding:.3rem;border:1px solid var(--grid)">Apériodique</td><td style="border:1px solid var(--grid)">\(Q \lt 1/2\)</td><td style="border:1px solid var(--grid)">réelles négatives \(r_1, r_2\)</td><td style="border:1px solid var(--grid)">\(A\,e^{r_1 t} + B\,e^{r_2 t}\)</td></tr>
  </table></div>`;
const s3 = () => split(rd('rlc-s3.html')).replace(/<\/div>\s*$/, TABLE + '\n</div>');
const noms = h => [['$$u_R(t)', "Loi d'Ohm"], ['$$u_L(t)', 'Loi de la bobine'], ['$$i(t) = C', 'Loi du condensateur']]
  .reduce((acc, [f, n]) => acc.split('<div class="formula">' + f).join('<div class="formula" data-nom="' + n + '">' + f), h);
const pager = `<nav class="pager" aria-label="Chapitres voisins"><a href="#" class="prev"><span class="k">${ic('chev-left', 'ic-s')}Chapitre précédent</span><span class="t">Circuit du 1er ordre</span></a><a href="#" class="next"><span class="k">Chapitre suivant${ic('chev-right', 'ic-s')}</span><span class="t">Signaux périodiques et Fourier</span></a></nav>`;
const coursDesk = () => `<section class="panel active" id="rlc-cours"><div class="panel-body marge">${noms(split(rd('rlc-s1.html')))}${split(rd('rlc-s2.html'))}${s3()}${split(rd('rlc-s6.html'))}${pager}</div></section>`;

/* ---------------- (1) et (6a) Chapitre, ordinateur ---------------- */
function chapDesk(theme, f, extra = '') {
  write(f, page({ title: 'Chapitre — ordinateur', theme, bodyCls: 'desk', body: `
${hdr({ themeOpen: !!extra })}
<div class="app">
  ${side()}
  <main class="main"><article class="sheet chapter" id="chap-rlc" data-mat="physique">${chapHead('cours')}${coursDesk()}</article></main>
  ${rail(0)}
</div>${extra}` }));
}
chapDesk('light', '01-chapitre-ordinateur.html');
chapDesk('dark', '06a-chapitre-sombre-ordinateur.html');

/* ---------------- (2) et (6b) Chapitre, téléphone ---------------- */
const mbar = ({ k = '<b>Physique</b>·<span class="part">Ondes &amp; signaux</span>·<span>1ʳᵉ</span>', h = 'Circuit RLC série', dot = true } = {}) => `
<header class="mbar" data-mat="physique">
  <button class="btn btn-ghost btn-icon" aria-label="Chapitres">${ic('menu')}</button>
  <div class="mbar-t"><div class="mbar-k">${dot ? '<span class="dot"></span>' : ''}${k}</div><div class="mbar-h">${h}</div></div>
  <button class="btn btn-ghost btn-icon" aria-label="Rechercher">${ic('search')}</button>
  <button class="btn btn-ghost btn-icon" aria-label="Réviser : 37 cartes dues">${ic('refresh')}<span class="count">37</span></button>
  <button class="btn btn-ghost btn-icon" aria-label="Plus">${ic('dots')}</button>
</header>`;
const MT = [['cours', 'Cours'], ['meth', 'Méthodes'], ['simu', 'Simu'], ['flash', 'Cartes'], ['exos', 'Exos']];
const mtabs = (on, cls = '') => `<nav class="mtabs ${cls}" data-mat="physique" role="tablist">${MT.map(([k, l]) => `<button class="tab${k === on ? ' active' : ''}" role="tab" aria-selected="${k === on}">${l}${k === 'flash' ? '<span class="count" aria-label="3 cartes dues">3</span>' : ''}</button>`).join('')}</nav>`;
function chapPhone(theme, f, extra = '') {
  write(f, page({ title: 'Chapitre — téléphone', theme, body: `
<div class="phone chapter" data-mat="physique">
  ${mbar()}${mtabs('cours')}
  <section class="panel active mcontent">${noms(split(rd('rlc-s1.html')))}${split(rd('rlc-s2.html'))}${s3()}${pager}</section>
  ${extra}
</div>` }));
}
chapPhone('light', '02-chapitre-telephone.html');
chapPhone('dark', '06b-chapitre-sombre-telephone.html');
// (2b) Défilé : la barre est revenue (petit geste vers le haut) et montre la section courante
write('02b-chapitre-telephone-defile.html', page({ title: 'Chapitre — téléphone, défilé', body: `
<div class="phone chapter" data-mat="physique">
  ${mbar({ k: 'Circuit RLC série · Cours', h: '<span class="sn">§2</span>Mise en équation', dot: true })}${mtabs('cours')}
  <section class="panel active mcontent" style="padding-top:.25rem">${split(rd('rlc-s2.html')).replace(/^[\s\S]*?(<h3>Établissement)/, '<div class="course-section">$1')}${s3()}</section>
</div>` }));

/* ---------------- (3a) Navigation, ordinateur : « Sommaire de la matière » ---------------- */
function partCard(s, year) {
  const items = s.chapitres.filter(c => inYear(c, year));
  if (!items.length) return '';
  const due = items.reduce((a, c) => a + (DUE[c.id] || 0), 0);
  const acq = { 'Ondes & signaux': 41, 'Mécanique': 63, 'Thermodynamique': 22, 'Électromagnétisme': 8, 'Chimie': 35, 'Référence': 70 }[s.label] || 0;
  return `<section class="pcard">
    <div class="pcard-h"><h3>${s.label}</h3><span class="pcard-n">${items.length} chapitres</span></div>
    <div class="pcard-p"><div class="stack" role="img" aria-label="${acq} % acquis"><i class="s2" style="width:${acq}%"></i></div><span>${acq} % acquis${due ? ` · <b>${due} dues</b>` : ''}</span></div>
    <ol class="pcard-list">${items.map(c => `<li><a href="#" class="${c.id === 'rlc' ? 'cur' : ''}">${c.nom}</a>${c.simu ? `<span class="simu" title="Simulateur">${ic('wave', 'ic-s')}</span>` : ''}${DUE[c.id] ? `<span class="count count-soft">${DUE[c.id]}</span>` : ''}</li>`).join('')}</ol>
  </section>`;
}
write('03a-navigation-ordinateur.html', page({
  title: 'Navigation — ordinateur', bodyCls: 'desk', extraHead: `<style>
.overview{ padding:0 2.5rem 2.5rem; }
.ov-head{ margin:0 -2.5rem; padding:2rem 2.5rem 1.5rem; position:relative; background:var(--chap-fond); border-bottom:1px solid var(--line); }
.ov-head::before{ content:""; position:absolute; inset:0; pointer-events:none;
  background-image:linear-gradient(var(--mill-cm) 1px, transparent 1px), linear-gradient(90deg, var(--mill-cm) 1px, transparent 1px), linear-gradient(var(--mill-fin) 1px, transparent 1px), linear-gradient(90deg, var(--mill-fin) 1px, transparent 1px);
  background-size:40px 40px, 40px 40px, 8px 8px, 8px 8px; -webkit-mask-image:linear-gradient(180deg,#000,transparent); mask-image:linear-gradient(180deg,#000,transparent); }
.ov-head > *{ position:relative; }
.ov-h{ margin:.4rem 0 0; font:italic var(--w-semi) var(--fs-h1)/1.05 var(--font-text); letter-spacing:var(--track-h1); color:var(--chap); }
.ov-meta{ margin-top:.6rem; font:var(--w-regular) var(--fs-ui)/1.4 var(--font-ui); color:var(--text-2); }
.ov-resume{ display:flex; align-items:center; gap:.9rem; margin-top:1.1rem; padding:.75rem 1rem; max-width:34rem; border-radius:var(--r-m); background:var(--raise); border:1px solid var(--line); text-decoration:none; color:var(--text); }
.ov-resume .pic{ width:2.5rem; height:2.5rem; border-radius:10px; display:grid; place-items:center; background:var(--chap-fond); color:var(--chap); font:italic 600 1.15rem/1 var(--font-text); }
.ov-resume .t{ font:600 1.0625rem/1.2 var(--font-text); } .ov-resume .s{ font:400 var(--fs-ui-s)/1.3 var(--font-ui); color:var(--text-2); }
.ov-resume > .ic{ margin-left:auto; color:var(--text-3); }
.ov-grid{ columns:2; column-gap:1rem; margin-top:1.5rem; }
.ov-grid .pcard{ break-inside:avoid; margin-bottom:1rem; }
.pcard{ border:1px solid var(--line); border-radius:var(--r-l); padding:1rem 1rem .5rem; background:var(--sheet); }
.pcard-h{ display:flex; align-items:baseline; gap:.5rem; }
.pcard-h h3{ margin:0; font:var(--w-semi) 1.1875rem/1.2 var(--font-text); }
.pcard-n{ margin-left:auto; font:var(--w-medium) var(--fs-ui-xs)/1 var(--font-ui); color:var(--text-2); }
.pcard-p{ display:grid; grid-template-columns:4.5rem 1fr; align-items:center; gap:.6rem; margin:.65rem 0 .5rem; font:var(--w-regular) var(--fs-ui-xs)/1.2 var(--font-ui); color:var(--text-2); }
.pcard-p b{ color:var(--rouge); font-weight:var(--w-semi); }
.pcard-p .stack{ height:.375rem; }
.pcard-list{ list-style:none; margin:0; padding:0; counter-reset:c; }
.pcard-list li{ display:flex; align-items:center; gap:.5rem; border-top:1px solid var(--line); counter-increment:c; }
.pcard-list a{ flex:1; display:flex; gap:.6rem; padding:.5rem 0; font:var(--w-regular) var(--fs-ui)/1.25 var(--font-ui); color:var(--text); text-decoration:none; }
.pcard-list a::before{ content:counter(c); min-width:1.1rem; font:italic var(--w-semi) 1rem/1.25 var(--font-text); color:var(--chap); }
.pcard-list a.cur{ font-weight:var(--w-semi); color:var(--chap); }
.pcard-list .simu{ color:var(--text-3); display:inline-flex; }
.ov-2a{ display:flex; align-items:center; gap:.75rem; margin-top:.5rem; padding:.85rem 1rem; border-radius:var(--r-m); background:var(--sunk); font:var(--w-regular) var(--fs-ui-s)/1.35 var(--font-ui); color:var(--text-2); }
.ov-2a .btn{ margin-left:auto; }
</style>`, body: `
${hdr()}
<div class="app no-rail">
  ${side({ open: ['Ondes & signaux', 'Mécanique'] })}
  <main class="main"><article class="sheet" data-mat="physique" style="max-width:none">
    <div class="overview">
      <div class="ov-head">
        <div class="crumb"><span class="dot"></span><b>Sommaire de la matière</b><span class="sep" style="color:var(--text-3)">·</span>1ʳᵉ année</div>
        <h1 class="ov-h">Physique</h1>
        <div class="ov-meta">6 parties · 37 chapitres · <b style="color:var(--rouge)">${CH.physique.flatMap(s => s.chapitres).filter(c => inYear(c, 1)).reduce((a, c) => a + (DUE[c.id] || 0), 0)} cartes dues</b> · 34 % des cartes acquises</div>
        <a class="ov-resume" href="#"><span class="pic">§3</span><span><span class="t">Reprendre : Circuit RLC série</span><br><span class="s">Cours · §3 Régime libre · hier, 21 h 40</span></span>${ic('chev-right')}</a>
      </div>
      <div class="ov-grid">${CH.physique.map(s => partCard(s, 1)).join('')}</div>
      <div class="ov-2a">${ic('book')}<span>14 chapitres de 2ᵉ année en physique (Maxwell, interférences, diffusion thermique…).</span><button class="btn">Voir la 2ᵉ&nbsp;année</button></div>
    </div>
  </article></main>
</div>` }));

/* ---------------- (3b) Navigation, téléphone : page « Chapitres » plein écran ---------------- */
const drawerHead = (filtre = '') => `
  <div class="dr-top"><h1>Chapitres</h1><button class="btn btn-ghost btn-icon" aria-label="Fermer">${ic('x')}</button></div>
  <div class="dr-rich"><a href="#"><span class="t">${ic('calendar')}Aujourd'hui<span class="count">37</span></span><span class="s">37 cartes dues · ≈ 12 min</span></a><a href="#"><span class="t">${ic('chart')}Bilan</span><span class="s">34 % des cartes acquises</span></a></div>
  <div class="dr-row"><div class="seg" role="group" aria-label="Année"><button aria-pressed="true">1ʳᵉ</button><button aria-pressed="false">2ᵉ</button></div><label class="field">${ic('filter')}<input placeholder="Filtrer les 160 chapitres" value="${filtre}"></label></div>`;
write('03b-navigation-telephone.html', page({ title: 'Navigation — téléphone', body: `
<div class="phone drawer">
  ${drawerHead()}
  <div class="dr-sec">
    <div class="kicker">Épinglés · Récents</div><div class="chips">${PINNED.map(id => { const c = BY[id]; return `<a class="chip" href="#" data-mat="${c.mat}">${ic('star-fill', 'on')}${c.court}${c.annee === 2 ? '<span class="tag2a">2A</span>' : ''}</a>`; }).join('')}${RECENTS.map(([id]) => { const c = BY[id]; return `<a class="chip" href="#" data-mat="${c.mat}">${ic('clock')}${c.court}</a>`; }).join('')}</div>
    <div style="margin-top:1rem">${matTabs('physique')}</div>
    <div data-mat="physique" style="margin-top:.35rem">${navParts('physique', 1, 'rlc', ['Ondes & signaux'])}</div>
  </div>
</div>` }));
// (3c) Filtre : résultats groupés par matière, toutes années, correspondance surlignée
const hl = (s, q) => s.replace(new RegExp('(' + q + ')', 'i'), '<mark>$1</mark>');
const RES = Object.entries(CH).map(([m, parts]) => [m, parts.flatMap(p => p.chapitres.map(c => Object.assign({ part: p.label }, c))).filter(c => /onde/i.test(c.nom))]).filter(([, l]) => l.length);
write('03c-navigation-telephone-filtre.html', page({ title: 'Navigation — téléphone, filtre', body: `
<div class="phone drawer">
  ${drawerHead('onde')}
  <div class="dr-sec nav-results">
    <div class="kicker" style="margin-top:1rem">${RES.reduce((a, [, l]) => a + l.length, 0)} chapitres · toutes matières, les deux années</div>
    ${RES.map(([m, l]) => `<div class="grp" data-mat="${m}"><div class="grp-h"><span class="dot"></span>${MATL[m]}<span class="n">${l.length}</span></div><ul class="nav-list" style="border:0;margin-left:0;padding-left:0">${l.map(c => `<li><a class="nav-item" href="#" data-mat="${m}"><span class="nm">${hl(c.nom, 'onde')}</span><span class="end">${c.annee === 2 ? '<span class="badge badge-2a" style="height:1.25rem">2ᵉ</span>' : ''}${ic('chev-right', 'ic-s')}</span><span class="sub">${c.part}${c.annee ? ' · ' + (c.annee === 1 ? '1ʳᵉ' : '2ᵉ') + ' année' : ''}</span></a></li>`).join('')}</ul></div>`).join('')}
  </div>
</div>` }));

/* ---------------- (4) Cartes, téléphone (onglet Cartes du chapitre : recto, verso) ---------------- */
const Q = R`Quelle est l'expression de la pseudo-pulsation \(\omega\) en régime pseudo-périodique ?`;
function carte(verso, theme = 'light') {
  const bottom = verso
    ? `<div class="flash-controls">
        <button class="hard">${ic('undo')}À revoir<small>aujourd'hui</small><span class="kbd">1</span></button>
        <button class="ok">${ic('wave')}Hésitant<small>dans 3 jours</small><span class="kbd">2</span></button>
        <button class="easy">${ic('check')}Acquis<small>dans 7 jours</small><span class="kbd">3</span></button></div>`
    : `<button class="btn btn-primary btn-lg btn-block" style="height:4rem">${ic('flip')}Afficher la réponse</button>`;
  const side = verso
    ? R`<div class="flash-side verso"><span class="tag">Question</span><p class="fc-q">${Q}</p>
        <div class="fc-sep"><span class="kicker">Réponse</span></div>
        <div class="fc-a"><div class="formula">$$\omega = \omega_0\sqrt{1 - \frac{1}{4Q^2}}$$</div><p style="margin:0">Toujours inférieure à \(\omega_0\) ; l'écart devient négligeable quand \(Q\) est grand.</p></div></div>`
    : `<div class="flash-side"><span class="tag">Question</span><p class="fc-q">${Q}</p></div>`;
  return page({ title: 'Cartes — téléphone', theme, extraHead: `<style>
.cards-tab{ display:flex; flex-direction:column; gap:.65rem; padding:.75rem var(--gutter) calc(.75rem + env(safe-area-inset-bottom)); min-height:calc(844px - var(--bar-h) - var(--tabs-h)); }
.cards-tab .flash-wrapper{ flex:1; max-width:none; }
.cards-tab .flash-card{ flex:1; min-height:0; }
</style>`, body: `
<div class="phone chapter" data-mat="physique">
  ${mbar()}${mtabs('flash')}
  <section class="panel active cards-tab" id="rlc-flash">
    <div class="flash-wrapper">
      <div class="flash-progress" id="rlc-flash-prog">Carte 12 / 26<span class="bar" role="img" aria-label="5 acquises, 3 hésitantes, 2 à revoir"><i style="width:19%;background:var(--note-2-vif)"></i><i style="width:12%;background:var(--note-1-vif)"></i><i style="width:8%;background:var(--note-0-vif)"></i></span><span style="font-weight:500">3 dues</span></div>
      <div class="flash-card flash-mat-physique" role="button" aria-label="${verso ? 'Carte retournée' : 'Retourner la carte'}">
        <div class="fc-head"><span class="badge badge-chap"><span class="dot"></span>Physique</span><span class="badge">Formule</span><span class="end"><span class="badge badge-out"><span class="dot" style="background:var(--note-0-vif)"></span>Dernière note : à revoir</span></span></div>
        ${side}
        <div class="${verso ? 'fc-foot' : 'flash-hint'}">${verso ? `<a class="flash-course-link" href="#">${ic('book', 'ic-s')}Voir dans le cours · §3</a><button class="flash-flag-btn">${ic('flag', 'ic-s')}Signaler</button>` : `${ic('clock', 'ic-s')}Formule la réponse de tête, puis touche la carte.`}</div>
      </div>
    </div>
    <div class="review-nav"><button class="btn btn-ghost">${ic('chev-left')}Précédente</button><button class="btn btn-ghost">Passer${ic('skip')}</button></div>
    ${bottom}
  </section>
</div>` });
}
write('04a-carte-recto-telephone.html', carte(false));
write('04b-carte-verso-telephone.html', carte(true));

/* ---------------- (5) Aujourd'hui, téléphone (ouvert à la main, jamais au lancement) ---------------- */
const WEEK = [['sa', 37, 1], ['di', 14], ['lu', 22], ['ma', 9], ['me', 17], ['je', 6], ['ve', 11]];
const DUEM = [['physique', 21], ['maths', 12], ['si', 4]];
write('05-aujourdhui-telephone.html', page({ title: "Aujourd'hui — téléphone", body: `
<div class="phone today" role="dialog" aria-label="Aujourd'hui">
  <div class="today-top"><span class="date">Samedi 18 octobre</span><span style="flex:1"></span><button class="btn btn-ghost btn-icon" aria-label="Fermer">${ic('x')}</button></div>
  <h1 class="today-h">Aujourd'hui<small>Bonjour ! On révise ?</small></h1>
  <div class="today-body">
    <section class="tcard">
      <div class="tcard-h"><span class="kicker">Révisions du jour</span><span class="end">toutes matières</span></div>
      <div class="due-big"><span class="n">37</span><span class="l">cartes à revoir</span></div>
      <div class="due-sub">≈ 12 min · répétition espacée</div>
      <div class="due-bars">${DUEM.map(([m, v]) => `<span class="m" data-mat="${m}"><span class="dot"></span>${MATL[m]}</span><span class="b" data-mat="${m}"><i style="width:${Math.round(v / 21 * 100)}%"></i></span><span class="v">${v}</span>`).join('')}</div>
      <button class="btn btn-primary btn-lg btn-block">${ic('play')}Commencer la révision</button>
      <div class="row2"><button class="btn">${ic('bolt')}Quiz</button><button class="btn">${ic('calc')}Calcul mental</button></div>
    </section>
    <section class="tcard">
      <div class="tcard-h"><span class="kicker">Reprendre</span><span class="end">hier, 21 h 40</span></div>
      <a class="resume" href="#" data-mat="physique"><span class="pic">§3</span><div><div class="t">Circuit RLC série</div><div class="s">Physique · Cours · Régime libre</div></div>${ic('chev-right')}</a>
      <div class="recents-mini">${RECENTS.slice(1).map(([id, w]) => { const c = BY[id]; return `<a class="recent-row" href="#" data-mat="${c.mat}"><span class="dot"></span>${c.court}<span class="where">${MATL[c.mat]} · ${w}</span></a>`; }).join('')}</div>
    </section>
    <section class="tcard">
      <div class="tcard-h"><span class="kicker">7 prochains jours</span><span class="end">cartes dues par jour</span></div>
      <div class="week" role="img" aria-label="Cartes dues : samedi 37, dimanche 14, lundi 22, mardi 9, mercredi 17, jeudi 6, vendredi 11">${WEEK.map(([w, v, now]) => `<div class="d${now ? ' now' : ''}"><span class="v">${v}</span><span class="b" style="height:${Math.round(v / 37 * 52) + 4}px"></span><span class="w">${w}</span></div>`).join('')}</div>
    </section>
    <section class="tcard" style="padding:.75rem">
      <div class="quick"><a href="#">${ic('chart')}Bilan</a><a href="#">${ic('function')}Formulaire</a><a href="#">${ic('flag')}Signalées</a><a href="#">${ic('download')}Sauvegarde</a></div>
    </section>
  </div>
</div>` }));

/* ---------------- (7) Sélecteur de thème : Clair / Sombre / Auto ---------------- */
const prev = (kind) => {
  const L = (top, w, cl, cd) => `<span class="ln" style="top:${top}%;width:${w}%;background:${cd ? `linear-gradient(135deg, ${cl} 0 55%, ${cd} 55%)` : cl}"></span>`;
  if (kind === 'light') return `<span class="theme-prev"><span class="pl"></span>${L(18, 52, '#1c1d21')}${L(36, 72, '#d6cfc3')}${L(50, 64, '#d6cfc3')}${L(66, 40, '#547add')}</span>`;
  if (kind === 'dark') return `<span class="theme-prev"><span class="pd"></span>${L(18, 52, '#e8e6e1')}${L(36, 72, '#3a3e47')}${L(50, 64, '#3a3e47')}${L(66, 40, '#6f94ee')}</span>`;
  return `<span class="theme-prev"><span class="layer"><span class="pl"></span>${L(18, 52, '#1c1d21')}${L(36, 72, '#d6cfc3')}${L(50, 64, '#d6cfc3')}${L(66, 40, '#547add')}</span><span class="layer diag"><span class="pd"></span>${L(18, 52, '#e8e6e1')}${L(36, 72, '#3a3e47')}${L(50, 64, '#3a3e47')}${L(66, 40, '#6f94ee')}</span></span>`;
};
const themePop = (sel) => `
<div class="menu theme-pop" role="dialog" aria-label="Thème" style="position:absolute; top:3.3rem; right:3.2rem; z-index:var(--z-menu)">
  <h3>Thème</h3>
  <p class="theme-now"><b>Auto</b> suit le réglage clair/sombre de ton appareil, en continu, même site ouvert — actuellement : <b>clair</b>.</p>
  <div class="theme-opts" role="radiogroup" aria-label="Thème">
    <button class="theme-opt" role="radio" aria-checked="${sel === 'light'}">${prev('light')}<span class="nm">${ic('sun', 'ic-s')}Clair</span></button>
    <button class="theme-opt" role="radio" aria-checked="${sel === 'dark'}">${prev('dark')}<span class="nm">${ic('moon', 'ic-s')}Sombre</span></button>
    <button class="theme-opt" role="radio" aria-checked="${sel === 'auto'}">${prev('auto')}<span class="nm">${ic('auto', 'ic-s')}Auto</span></button>
  </div>
  <div class="theme-sub"><span class="lab">Taille du texte<small>cours et cartes</small></span><div class="seg" role="radiogroup" aria-label="Taille du texte"><button aria-checked="false" aria-label="Plus petit">A−</button><button aria-checked="true">A</button><button aria-checked="false" aria-label="Plus grand">A+</button></div></div>
</div>`;
chapDesk('light', '07a-theme-ordinateur.html', themePop('auto'));
const bsheet = `
<div class="scrim"></div>
<div class="bsheet" role="dialog" aria-label="Plus d'options">
  <div class="grab"></div>
  <button class="menu-item">${ic('calendar')}Aujourd'hui<span class="count">37</span></button>
  <button class="menu-item">${ic('chart')}Bilan</button>
  <button class="menu-item">${ic('bolt')}Quiz</button>
  <button class="menu-item">${ic('calc')}Calcul mental</button>
  <button class="menu-item">${ic('function')}Formulaire du chapitre</button>
  <button class="menu-item">${ic('star')}Épingler ce chapitre</button>
  <button class="menu-item">${ic('flag')}Cartes signalées<span class="end">2</span></button>
  <button class="menu-item">${ic('download')}Sauvegarde<span class="end">exporter, importer</span></button>
  <div class="bsheet-theme">
    <div class="row"><span class="lab">Thème</span><div class="seg" role="radiogroup" aria-label="Thème"><button aria-checked="false">${ic('sun', 'ic-s')}Clair</button><button aria-checked="false">${ic('moon', 'ic-s')}Sombre</button><button aria-checked="true">${ic('auto', 'ic-s')}Auto</button></div></div>
    <p class="help">Auto suit le réglage de ton téléphone — actuellement : <b class="now-l">clair</b><b class="now-d">sombre</b>.</p>
    <div class="row"><span class="lab">Texte</span><div class="seg" role="radiogroup" aria-label="Taille du texte"><button aria-checked="false">A−</button><button aria-checked="true">A</button><button aria-checked="false">A+</button></div></div>
  </div>
</div>`;
write('07b-theme-telephone.html', page({ title: 'Thème — téléphone (Auto)', theme: 'auto', extraHead: `<style>
.now-d{ display:none; } @media (prefers-color-scheme: dark){ .now-l{ display:none; } .now-d{ display:inline; } }
</style>`, body: `
<div class="phone chapter" data-mat="physique">
  ${mbar()}${mtabs('cours')}
  <section class="panel active mcontent">${noms(split(rd('rlc-s1.html')))}</section>
  ${bsheet}
</div>` }));

/* ---------------- (8a) Exercices et (8b) Simulateur, ordinateur ---------------- */
const exo1 = diff(rd('rlc-exo1.html')).replace('<button class="toggle-sol" onclick="toggleSol(this)">Voir la solution</button>', '<button class="toggle-sol open" onclick="toggleSol(this)">Masquer la solution</button>').replace('<div class="solution">', '<div class="solution shown">');
const exosPanel = `<section class="panel active" id="rlc-exos"><div class="panel-body" style="padding-left:2.5rem">
  <div class="exo-tools"><div class="seg" role="group" aria-label="Difficulté"><button aria-pressed="true">Tous</button><button aria-pressed="false">Facile</button><button aria-pressed="false">Moyen</button><button aria-pressed="false">Difficile</button></div><button class="chip">Concours PT · 1</button><span class="info">8 exercices corrigés</span></div>
  <div class="exo-wrapper">${exo1}${diff(rd('rlc-exo2.html'))}${diff(rd('rlc-exo-concours.html'))}</div></div></section>`;
write('08a-exercices-ordinateur.html', page({ title: 'Exercices — ordinateur', bodyCls: 'desk', extraHead: `<style>.chap-head{ grid-template-columns:2.5rem minmax(0,1fr) 0; }</style>`, body: `
${hdr()}
<div class="app">${side()}<main class="main"><article class="sheet chapter" data-mat="physique">${chapHead('exos')}${exosPanel}</article></main>${railExos}</div>` }));

// Simulateur : DOM RÉEL de rlc-simu (src/rlc-simu.html), seulement placé par la grille CSS
const simDom = rd('rlc-simu.html')
  .replace('<section class="panel" id="rlc-simu">', '<section class="panel active" id="rlc-simu"><div class="panel-body" style="padding-left:2.5rem">')
  .replace(/<\/div>\s*<\/section>[\s\S]*$/, '</div></div></section>')
  .replace('id="regime-display" class="regime-badge">—', 'id="regime-display" class="regime-badge pseudo">Pseudo-périodique · Q &gt; 1/2')
  .replace('<span class="lbl">ω₀</span><span id="info-w0">—</span>', R`<span class="lbl">Pulsation propre \(\omega_0\)</span><span id="info-w0">1 414 rad/s</span>`)
  .replace('<span class="lbl">f₀</span><span id="info-f0">—</span>', R`<span class="lbl">Fréquence propre \(f_0\)</span><span id="info-f0">225 Hz</span>`)
  .replace('<span class="lbl">Q</span><span id="info-Q">—</span>', R`<span class="lbl">Facteur de qualité \(Q\)</span><span id="info-Q">3,54</span>`)
  .replace('<span class="lbl">τ ou Δω</span><span id="info-tau">—</span>', R`<span class="lbl">Constante de temps \(\tau\)</span><span id="info-tau">5,0 ms</span>`)
  .replace('<label>R (Ω)</label>', '<label>R — résistance (Ω)</label>').replace('<label>L (mH)</label>', '<label>L — inductance (mH)</label>').replace('<label>C (µF)</label>', '<label>C — capacité (µF)</label>')
  .replace(/<\/div>\s*<canvas id="sim-canvas"><\/canvas>/, `<button class="btn btn-ghost sim-reset">↺ Valeurs par défaut</button></div>\n  <canvas id="sim-canvas" aria-label="Tension aux bornes du condensateur en fonction du temps"></canvas>`);
const simScript = R`<script>
// Canvas dessiné avec les jetons (même principe que __CV() dans le site)
(function(){
  const cv=document.getElementById('sim-canvas'), g=cv.getContext('2d'), cs=getComputedStyle(cv);
  const v=n=>cs.getPropertyValue(n).trim();
  const dpr=window.devicePixelRatio||1, cw=cv.clientWidth, chh=Math.round(cw*(cw<500?0.62:0.5)); cv.width=cw*dpr; cv.height=chh*dpr; cv.style.height=chh+'px'; g.scale(dpr,dpr);
  const W=cw, H=chh, L=44, Rr=24, T=34, B=34, x0=L, x1=W-Rr, yc=T+(H-T-B)/2, A=(H-T-B)/2-10;
  g.lineWidth=1; g.strokeStyle=v('--line'); g.beginPath();
  for(let i=0;i<=10;i++){const x=x0+(x1-x0)*i/10; g.moveTo(x,T); g.lineTo(x,H-B);} for(let j=-2;j<=2;j++){const y=yc-j*A/2; g.moveTo(x0,y); g.lineTo(x1,y);} g.stroke();
  g.strokeStyle=v('--text-3'); g.lineWidth=1.25; g.beginPath(); g.moveTo(x0,yc); g.lineTo(x1,yc); g.moveTo(x0,T); g.lineTo(x0,H-B); g.stroke();
  g.font='500 12px "JetBrains Mono", monospace'; g.fillStyle=v('--text-2'); g.textAlign='right'; g.textBaseline='middle';
  [['1',yc-A],['0',yc],['−1',yc+A]].forEach(([t,y])=>g.fillText(t,x0-8,y));
  g.textAlign='center'; g.textBaseline='top';
  for(let i=1;i<=5;i++){ if(cw<500 && i%2===0) continue; g.fillText((i*5)+' ms', x0+(x1-x0)*i/5 - (i===5?16:0), H-B+8); }
  const tau=5, w=1414*Math.sqrt(1-1/(4*3.54*3.54))/1000, tmax=25, X=t=>x0+(x1-x0)*t/tmax, Y=u=>yc-u*A;
  g.setLineDash([4,4]); g.strokeStyle=v('--text-3'); g.lineWidth=1; g.beginPath();
  for(let t=0;t<=tmax;t+=.1){ const e=Math.exp(-t/tau); t?g.lineTo(X(t),Y(e)):g.moveTo(X(t),Y(e)); } g.stroke();
  g.beginPath(); for(let t=0;t<=tmax;t+=.1){ const e=-Math.exp(-t/tau); t?g.lineTo(X(t),Y(e)):g.moveTo(X(t),Y(e)); } g.stroke(); g.setLineDash([]);
  g.strokeStyle=v('--chap-vif'); g.lineWidth=2.25; g.lineJoin='round'; g.beginPath();
  for(let t=0;t<=tmax;t+=.02){ const u=Math.exp(-t/tau)*(Math.cos(w*t)+Math.sin(w*t)/(w*tau)); t?g.lineTo(X(t),Y(u)):g.moveTo(X(t),Y(u)); } g.stroke();
  g.fillStyle=v('--text'); g.textAlign='left'; g.textBaseline='alphabetic';
  g.font='italic 500 16px "Source Serif 4", serif'; g.fillText('u', x0+10, T-12); g.font='italic 500 11px "Source Serif 4", serif'; g.fillText('C', x0+19, T-8);
  g.font='500 15px "Source Serif 4", serif'; g.fillText('/', x0+28, T-12); g.font='italic 500 16px "Source Serif 4", serif'; g.fillText('U', x0+35, T-12);
  g.font='500 11px "Source Serif 4", serif'; g.fillText('0', x0+47, T-8);
  g.font='500 13px "Source Sans 3", sans-serif'; g.fillStyle=v('--text-2'); g.textAlign='right'; g.fillText('– – enveloppe e^(−t/τ)', x1, T-12);
})();
</script>`;
const simBoot = `<script>document.fonts.ready.then(()=>{const s=document.createElement('script');s.textContent=${JSON.stringify(simScript.replace(/<\/?script>/g, ''))};document.body.appendChild(s);});</script>`;
write('08b-simulateur-ordinateur.html', page({ title: 'Simulateur — ordinateur', bodyCls: 'desk', extraHead: `<style>.chap-head{ grid-template-columns:2.5rem minmax(0,1fr) 0; }</style>`, body: `
${hdr()}
<div class="app no-rail">${side()}<main class="main"><article class="sheet chapter" data-mat="physique" style="max-width:66rem">${chapHead('simu')}${simDom}</article></main></div>
${simBoot}` }));
write('08c-simulateur-telephone.html', page({ title: 'Simulateur — téléphone', body: `
<div class="phone chapter" data-mat="physique">
  ${mbar()}${mtabs('simu')}
  <div class="mcontent">${simDom.replace('<div class="panel-body" style="padding-left:2.5rem">', '<div>')}</div>
</div>
${simBoot}` }));

module.exports = { page, ic, split, diff, diffHtml, rd, R, write, MATS, MATL, CH, BY, matTabs, mbar, mtabs };
if (require.main === module) require('./build-specimen.js');
