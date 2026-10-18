// Page « spécimen » : échelle typographique, couleurs, encadrés, boutons, badges,
// onglets, champs, menus, notation… générée en clair et en sombre.
const { page, ic, split, R, write, BY, diffHtml, matTabs } = require('./build.js');

const TYPE = [
  ['--fs-display', 'Grand nombre', '40 → 56', 'serif 600', 'font:var(--w-semi) var(--fs-display)/1 var(--font-text);letter-spacing:-.03em', '37'],
  ['--fs-h1', 'Titre de chapitre', '29 → 44', 'serif 600 · taille optique auto · −0,018 em', 'font:var(--w-semi) var(--fs-h1)/1.08 var(--font-text);letter-spacing:-.018em', 'Circuit RLC série'],
  ['--fs-h2', 'Titre de section', '24 → 32', 'serif 600', 'font:var(--w-semi) var(--fs-h2)/1.15 var(--font-text);letter-spacing:-.01em', 'Les trois dipôles élémentaires'],
  ['--fs-h3', 'Sous-titre', '20 → 23', 'serif 600', 'font:var(--w-semi) var(--fs-h3)/1.25 var(--font-text)', 'Le conducteur ohmique (résistance R)'],
  ['--fs-card-q', 'Question de carte', '22 → 26', 'serif 600', 'font:600 var(--fs-card-q)/1.45 var(--font-text)', R`Quelle est l'expression de \(\omega_0\) ?`],
  ['--fs-lead', 'Chapô (.intro)', '18,5 → 21,5', 'serif 400 romain · encre 2', 'font:400 var(--fs-lead)/1.5 var(--font-text);color:var(--text-2)', 'Avant d\'attaquer le RLC, on rappelle le comportement de chaque composant.'],
  ['--fs-body', 'Corps', '17,5 → 19', 'serif 400 · gras 650 · interligne 1,6', 'font:400 var(--fs-body)/1.6 var(--font-text)', R`La bobine s'oppose aux <strong>variations</strong> du courant : \(u_L = L\,\frac{di}{dt}\) ; ions Fe³⁺ et SO₄²⁻, H₂O → 2 H⁺ + ½ O₂ ≈ ≤ ≥ ⟹.`],
  ['--fs-sol', 'Correction', '16,5 → 17,5', 'serif 400', 'font:400 var(--fs-sol)/1.6 var(--font-text)', R`\(Q > 1/2\) : régime pseudo-périodique.`],
  ['--fs-small', 'Note, légende', '15,5 → 16,5', 'serif 400 / italique', 'font:italic 400 var(--fs-small)/1.45 var(--font-text);color:var(--text-2)', 'Loi d\'Ohm — nom de formule en marge'],
  ['--fs-ui-l', 'Interface grand', '17', 'sans 600', 'font:600 var(--fs-ui-l)/1.3 var(--font-ui)', 'Afficher la réponse'],
  ['--fs-ui', 'Interface', '15 → 16', 'sans 400–600', 'font:500 var(--fs-ui)/1.3 var(--font-ui)', 'Cours · Méthodes · Simulateur · Cartes 26'],
  ['--fs-ui-s', 'Interface petit', '14', 'sans 400–600', 'font:400 var(--fs-ui-s)/1.3 var(--font-ui);color:var(--text-2)', '7 sections · 26 cartes · 8 exercices · 1 414 rad/s'],
  ['--fs-ui-xs', 'Micro (plancher du texte)', '13', 'sans 500', 'font:500 var(--fs-ui-xs)/1.3 var(--font-ui);color:var(--text-3)', '10 acquises · 5 hésitantes · 1ʳᵉ année'],
  ['--fs-count', 'Compteur, pastille', '12', 'sans 700 (gras seulement)', 'font:700 var(--fs-count)/1.3 var(--font-ui);color:var(--text-2)', '37 · 2A · 1 2 3'],
  ['--fs-kicker', 'Surtitre', '12,5 → 13', 'sans 600 capitales +7,5 %', 'font:600 var(--fs-kicker)/1.2 var(--font-ui);letter-spacing:var(--track-kicker);text-transform:uppercase;color:var(--physique)', '§1 · Les bases'],
  ['--font-code', 'Code', '0,84 em', 'JetBrains Mono 400 · sans ligatures', 'font:400 15px/1.5 var(--font-code);font-variant-ligatures:none', 'def omega0(L, C): return 1 / sqrt(L * C) if C != 0 else None'],
];
const SW = (name, label) => `<div class="sw"><span class="chipc" style="background:var(${name})"></span><span class="swl"><b>${label}</b><code>${name}</code><span class="ratio" data-fg="${name}"></span></span></div>`;
const MATSW = ['physique', 'maths', 'si', 'info', 'anglais'].map(m => `<div class="msw" data-mat="${m}"><div class="mtop" style="background:var(--${m}-fond)"><span style="color:var(--${m});font:600 15px var(--font-ui)">${{ physique: 'Physique', maths: 'Maths', si: 'SI', info: 'Info', anglais: 'Anglais' }[m]}</span><span class="dotb" style="background:var(--${m}-vif)"></span></div><div class="mbot"><code>--${m}</code><span class="ratio" data-fg="--${m}" data-bg="--${m}-fond"></span></div></div>`).join('');
const SEMSW = [['rouge', 'À revoir · dû · alerte'], ['ambre', 'Hésitant · À noter'], ['vert', 'Acquis · correction']].map(([m, l]) => `<div class="msw"><div class="mtop" style="background:var(--${m}-fond)"><span style="color:var(--${m});font:600 15px var(--font-ui)">${l}</span><span class="dotb" style="background:var(--${m}-vif)"></span></div><div class="mbot"><code>--${m}</code><span class="ratio" data-fg="--${m}" data-bg="--${m}-fond"></span></div></div>`).join('');

const css = `<style>
body{ background:var(--desk); }
.spec{ width:1180px; margin:0 auto; padding:28px 0 60px; }
.spec-h{ display:flex; align-items:baseline; gap:16px; margin:0 0 18px; }
.spec-h h1{ margin:0; font:600 34px/1.1 var(--font-text); letter-spacing:-.02em; }
.spec-h span{ font:500 15px var(--font-ui); color:var(--text-3); }
.blk{ background:var(--sheet); border-radius:var(--r-l); box-shadow:var(--sh-sheet); padding:22px 26px 24px; margin-bottom:18px; }
.blk > h2{ margin:0 0 14px; font:700 var(--fs-kicker)/1 var(--font-ui); letter-spacing:var(--track-kicker); text-transform:uppercase; color:var(--text-3); }
.trow{ display:grid; grid-template-columns:170px 1fr; gap:18px; align-items:baseline; padding:10px 0; border-top:1px solid var(--line); }
.trow:first-of-type{ border-top:0; }
.tmeta{ font:400 13px/1.35 var(--font-ui); color:var(--text-3); }
.tmeta b{ display:block; font:600 14px var(--font-ui); color:var(--text); }
.tmeta code{ font:500 12.5px var(--font-code); color:var(--text-2); }
.grid2{ display:grid; grid-template-columns:1fr 1fr; gap:22px; }
.grid3{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; }
.sws{ display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }
.sw{ display:flex; gap:10px; align-items:center; }
.chipc{ width:40px; height:40px; border-radius:10px; box-shadow:inset 0 0 0 1px var(--line-2); flex:none; }
.swl{ display:flex; flex-direction:column; font:400 13px/1.3 var(--font-ui); color:var(--text-3); }
.swl b{ font:600 14px var(--font-ui); color:var(--text); }
.swl code, .mbot code{ font:500 12px var(--font-code); }
.ratio{ font:600 12.5px var(--font-ui); color:var(--text-2); }
.mats{ display:grid; grid-template-columns:repeat(5,1fr); gap:10px; }
.msw{ border-radius:12px; overflow:hidden; border:1px solid var(--line); }
.mtop{ height:64px; display:flex; align-items:center; justify-content:space-between; padding:0 14px; }
.dotb{ width:22px; height:22px; border-radius:50%; }
.mbot{ display:flex; justify-content:space-between; align-items:center; padding:8px 12px; background:var(--sheet); color:var(--text-3); }
.row{ display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin:8px 0; }
.lab{ font:600 13px var(--font-ui); color:var(--text-3); min-width:110px; }
.demo .panel{ font-size:var(--fs-body); }
.demo .course-section{ display:block; }
.demo .tabs{ margin-top:0; }
.phtabs{ width:390px; border:1px solid var(--line); border-radius:12px; overflow:hidden; }
.phtabs .mtabs{ position:static; }
.incont{ display:grid; grid-template-columns:repeat(5,1fr); gap:12px; }
.minisheet{ border:1px solid var(--line); border-top:4px solid var(--chap-vif); border-radius:12px; padding:12px 14px 14px; background:var(--sheet); }
.minisheet .crumb{ white-space:nowrap; overflow:hidden; text-overflow:ellipsis; font-size:13px; }
.minisheet .mt{ margin-top:.45rem; font:600 19px/1.2 var(--font-text); min-height:2.4em; }
.minisheet .tabs .tab{ height:2.25rem; padding:0 .5rem; font-size:14px; }
.minisheet .tabs .tab.active::after{ left:.5rem; right:.5rem; }
</style>`;

const body = (theme) => `
<div class="spec chapter" data-mat="physique">
  <div class="spec-h"><h1>Spécimen du système</h1><span>Source Serif 4 · Source Sans 3 · JetBrains Mono — thème ${theme === 'dark' ? 'sombre' : 'clair'} — tailles en px : téléphone 390 → ordinateur 1280+</span></div>

  <section class="blk"><h2>Échelle typographique</h2>
    ${TYPE.map(([v, n, px, f, st, s]) => `<div class="trow"><div class="tmeta"><b>${n}</b>${px} px · ${f}<br><code>${v}</code></div><div style="${st}">${s}</div></div>`).join('')}
  </section>

  <section class="blk"><h2>Couleurs — neutres (ratio de contraste sur la feuille)</h2>
    <div class="sws">${SW('--desk', 'Bureau')}${SW('--sheet', 'Feuille')}${SW('--sunk', 'Creux')}${SW('--raise', 'Surface haute')}${SW('--text', 'Encre')}${SW('--text-2', 'Encre 2')}${SW('--text-3', 'Encre 3')}${SW('--field', 'Contour de champ')}${SW('--line', 'Filet')}${SW('--line-2', 'Filet 2 / tableau')}${SW('--primary', 'Action principale')}${SW('--focus', 'Focus')}${SW('--marge', 'Filet de marge (décor)')}${SW('--reglure', 'Réglure bristol (décor)')}</div>
    <h2 style="margin-top:22px">Matières — encre sur teinte, pastille vive</h2>
    <div class="mats">${MATSW}</div>
    <h2 style="margin-top:22px">Sémantique — notation et encadrés</h2>
    <div class="mats" style="grid-template-columns:repeat(3,1fr)">${SEMSW}</div>
  </section>


  <section class="blk"><h2>Les cinq encres de matière en situation (même gabarit, une encre par chapitre)</h2>
    <div class="incont">${[['rlc','Ondes & signaux'],['serient','Analyse'],['slci','Automatique'],['pyrec','Programmation'],['envocsci','Vocabulaire thématique']].map(([id, part]) => { const c = BY[id]; return `<div class="minisheet" data-mat="${c.mat}">
      <div class="crumb"><span class="dot"></span><b>${{ physique: 'Physique', maths: 'Maths', si: 'SI', info: 'Info', anglais: 'Anglais' }[c.mat]}</b>${ic('chev-right')}${part}</div>
      <div class="mt">${c.nom}</div>
      <div class="row" style="margin:.5rem 0 .2rem"><span class="badge badge-out">${c.annee === 2 ? '2ᵉ année' : c.annee === 0 ? '1ʳᵉ et 2ᵉ année' : '1ʳᵉ année'}</span></div>
      <nav class="tabs" style="margin-top:.4rem"><button class="tab active">Cours</button><button class="tab">Cartes<span class="count count-soft">2</span></button></nav>
      <div class="sec-t" style="margin-top:.9rem;display:block">§1 · Les bases</div>
      <div class="def-box" style="font:400 15px/1.5 var(--font-text);margin:.5rem 0 0">Encadré « Définition » teinté de l'encre du chapitre.</div>
    </div>`; }).join('')}</div>
  </section>
  <section class="blk demo"><h2>Encadrés du cours (classes existantes)</h2>
    <div class="panel"><div class="course-section">
      <div class="formula" style="margin-left:0">$$u_R(t) = R\\,i(t)$$</div><div class="formula" style="margin-left:0">$$P = u_R\\,i = R\\,i^2 \\geq 0$$</div>
      <div class="grid2">
        <div>
          <div class="def-box"><p><strong>Pulsation propre</strong> : \\(\\omega_0 = \\dfrac{1}{\\sqrt{LC}}\\) (rad/s). C'est la pulsation à laquelle le circuit oscillerait en l'absence de toute résistance.</p></div>
          <div class="prop-box"><strong>Continuité du courant.</strong> Dans une bobine idéale, l'intensité \\(i_L(t)\\) est <em>continue</em> : \\(i_L(0^+) = i_L(0^-)\\).</div>
          <div class="notice"><strong>Programme PTSI :</strong> on doit savoir reconnaître la résonance en tension et déterminer \\(\\omega_0\\) et \\(Q\\) <em>à partir d'un graphe</em>.</div>
        </div>
        <div>
          <div class="method-box"><strong>Méthode 1 — Identifier le régime d'un circuit</strong><ol style="margin-top:0.4rem"><li><span class="step">Étape 1.</span> Calculer \\(\\omega_0 = 1/\\sqrt{LC}\\).</li><li><span class="step">Étape 2.</span> Calculer \\(Q\\) avec la formule la plus directe.</li><li><span class="step">Étape 3.</span> Comparer Q à 1/2.</li></ol></div>
          <div class="reveal"><span class="label">Mémo — Les continuités</span><span class="prompt">Quelles grandeurs sont continues ?</span><div class="content"><p>…</p></div></div>
          <div class="reveal open"><span class="label">Application numérique</span><span class="prompt">Calculer \\(\\omega_0\\) pour \\(L = 10\\) mH, \\(C = 1\\) µF.</span><div class="content"><p>\\(\\omega_0 = 1/\\sqrt{10^{-8}} = 10^4\\) rad/s.</p></div></div>
        </div>
      </div>
      <div class="solution shown" style="margin-top:6px"><h4>Correction</h4><p><strong>Q2.</strong> \\(Q > 1/2\\) → <strong>régime pseudo-périodique</strong>.</p></div>
    </div></div>
  </section>

  <div class="grid2">
    <section class="blk"><h2>Boutons</h2>
      <div class="row"><button class="btn btn-primary">${ic('refresh')}Réviser<span class="count">37</span></button><button class="btn">${ic('function')}Formulaire</button><button class="btn btn-chap">${ic('refresh')}Réviser ce chapitre</button></div>
      <div class="row"><button class="btn btn-ghost">${ic('calendar')}Aujourd'hui</button><button class="btn btn-icon" aria-label="Imprimer">${ic('printer')}</button><button class="btn btn-ghost btn-icon" aria-label="Plus">${ic('dots')}</button><button class="toggle-sol">Voir la solution</button></div>
      <div class="row"><button class="btn btn-primary btn-lg">${ic('play')}Commencer la révision</button></div>
      <h2 style="margin-top:18px">Badges, compteurs, puces, touches</h2>
      <div class="row"><span class="badge badge-out">1ʳᵉ&nbsp;année</span><span class="badge badge-2a">2ᵉ&nbsp;année</span><span class="badge badge-chap"><span class="dot"></span>Physique</span><span class="badge">Formule</span><span class="badge badge-strong">Concours PT</span></div>
      <div class="row"><span class="count">37</span><span class="count count-soft">3</span><span class="count count-quiet">26</span><span class="chip" data-mat="physique"><span class="dot"></span>Filtres</span><span class="chip" data-mat="maths"><span class="dot"></span>Séries entières<span class="tag2a">2A</span></span><kbd>Ctrl</kbd><kbd>K</kbd></div>
      <div class="row"><span class="regime-badge pseudo">Pseudo-périodique</span><span class="regime-badge critique">Critique</span><span class="regime-badge aperiodique">Apériodique</span></div>
    </section>
    <section class="blk"><h2>Onglets</h2>
      <nav class="tabs"><button class="tab active">Cours</button><button class="tab">Méthodes</button><button class="tab">Simulateur</button><button class="tab">Cartes <span class="cnt">26</span><span class="count">3</span></button><button class="tab">Exercices <span class="cnt">8</span></button></nav>
      <div class="phtabs" style="margin-top:14px"><nav class="mtabs"><button class="tab active">Cours</button><button class="tab">Méthodes</button><button class="tab">Simu</button><button class="tab">Cartes<span class="count">3</span></button><button class="tab">Exos</button></nav></div>
      <h2 style="margin-top:18px">Champs et contrôles segmentés</h2>
      <label class="field">${ic('search')}<input placeholder="Rechercher un chapitre, une formule…"><span class="kbd">Ctrl K</span></label>
      <div class="row" style="margin-top:12px"><div class="seg"><button aria-pressed="true">1ʳᵉ&nbsp;année</button><button aria-pressed="false">2ᵉ&nbsp;année</button></div><div class="seg"><button aria-pressed="false">${ic('sun', 'ic-s')}Clair</button><button aria-pressed="false">${ic('moon', 'ic-s')}Sombre</button><button aria-pressed="true">${ic('auto', 'ic-s')}Auto</button></div></div>
      <div style="margin-top:12px">${matTabs('si')}</div>
    </section>
  </div>

  <div class="grid3">
    <section class="blk"><h2>Menu « Plus »</h2>
      <div class="menu" style="box-shadow:var(--sh-2)">
        <button class="menu-item">${ic('function')}Formulaire</button><button class="menu-item">${ic('printer')}Imprimer le chapitre</button><button class="menu-item hl">${ic('download')}Sauvegarde</button><button class="menu-item">${ic('keyboard')}Raccourcis<span class="end"><kbd>?</kbd></span></button><button class="menu-item">${ic('flag')}Cartes signalées<span class="end">2</span></button>
        <div class="menu-sep"></div><div class="menu-label">Taille du texte</div>
        <div class="seg seg-block" style="margin:0 .25rem .25rem;width:calc(100% - .5rem)"><button aria-pressed="false">A−</button><button aria-pressed="true">A</button><button aria-pressed="false">A+</button></div>
      </div>
    </section>
    <section class="blk"><h2>Notation des cartes</h2>
      <div class="flash-controls"><button class="hard">${ic('undo')}À revoir<small>aujourd'hui</small></button><button class="ok">${ic('wave')}Hésitant<small>dans 3 j</small></button><button class="easy">${ic('check')}Acquis<small>dans 7 j</small></button></div>
      <h2 style="margin-top:18px">Difficulté des exercices</h2>
      <div class="row" data-mat="physique">${diffHtml(1)}${diffHtml(2)}${diffHtml(3)}</div>
      <h2 style="margin-top:18px">Progression</h2>
      <div class="stack"><i class="s2" style="width:38%"></i><i class="s1" style="width:19%"></i><i class="s0" style="width:12%"></i></div>
      <div class="legend" style="margin-top:8px"><span><i style="background:var(--note-2-vif)"></i>acquises</span><span><i style="background:var(--note-1-vif)"></i>hésitantes</span><span><i style="background:var(--note-0-vif)"></i>à revoir</span><span><i style="background:var(--note-nv)"></i>jamais vues</span></div>
    </section>
    <section class="blk"><h2>Lignes de navigation</h2>
      <ul class="nav-list" style="margin-left:.5rem" data-mat="physique">
        <li><a class="nav-item" href="#">Circuit du 1er ordre<span class="end"><span class="count count-soft">1</span></span></a></li>
        <li><a class="nav-item cur" href="#" data-mat="physique">Circuit RLC série<span class="end"><span class="count count-soft">3</span></span></a></li>
        <li><a class="nav-item" href="#">Filtres<span class="end"><span class="count count-soft">5</span>${ic('star-fill', 'ic-s pin on')}</span></a></li>
        <li><a class="nav-item" href="#">ALI &amp; rétroaction<span class="end"><span class="tag2a">2A</span></span></a></li>
      </ul>
      <div class="nav-results" data-mat="physique" style="margin-top:10px"><div class="grp-h"><span class="dot"></span>Physique<span class="n">2</span></div><a class="nav-item" href="#"><mark>Onde</mark>s mécaniques<span class="sub">Ondes &amp; signaux · 1ʳᵉ année</span></a></div>
    </section>
  </div>
</div>
<script>
// Ratios de contraste affichés (calculés dans la page, sur les couleurs résolues)
(function(){
  function rgb(c){ const m=c.match(/[\\d.]+/g).map(Number); return m.slice(0,3); }
  function L(c){ return rgb(c).map(v=>{v/=255;return v<=.04045?v/12.92:Math.pow((v+.055)/1.055,2.4);}).reduce((a,v,i)=>a+v*[.2126,.7152,.0722][i],0); }
  function res(name, el){ const p=document.createElement('span'); p.style.color='var('+name+')'; (el||document.body).appendChild(p); const c=getComputedStyle(p).color; p.remove(); return c; }
  document.querySelectorAll('.ratio').forEach(s=>{ const host=s.closest('[data-mat]')||document.body;
    const fg=res(s.dataset.fg, host), bg=res(s.dataset.bg||'--sheet', host);
    const a=L(fg), b=L(bg), r=(Math.max(a,b)+.05)/(Math.min(a,b)+.05); s.textContent=r.toFixed(1)+':1'; });
})();
</script>`;

write('09-specimen-clair.html', page({ title: 'Spécimen — clair', theme: 'light', body: body('light'), extraHead: css }));
write('09-specimen-sombre.html', page({ title: 'Spécimen — sombre', theme: 'dark', body: body('dark'), extraHead: css }));
