#!/usr/bin/env python3
"""Retouches des sources (schémas lisibles, MathML d'accessibilité, cinématique, Lorentz)."""
import os
os.chdir('/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/ligneB')
p = 'module.js'
s = open(p).read()
old_start = s.index('  /* ---------- 6. Schémas SVG : aucun libellé sous 12 px ---------- */')
old_end = s.index('  /* ---------- 7. Simulateurs')
new = '''  /* ---------- 6. Schémas SVG : aucun libellé sous 12 px ----------
     Mesure à l'état naturel ; s'il faut agrandir : .lisible (largeur minimale --svg-min, figure
     élargie jusqu'à la colonne, et au téléphone jusque dans la gouttière), puis .defile (la
     figure défile en largeur) seulement si cela ne suffit pas. */
  function schemasLisibles(root){
    var cadres = Array.prototype.slice.call(root.querySelectorAll('figure.schema, .cine-svg-wrap'))
      .filter(function(c){ return c.querySelector('svg text') && visible(c); });
    if(!cadres.length) return;
    cadres.forEach(function(c){ c.classList.remove('lisible', 'defile'); c.style.removeProperty('--svg-min'); });
    var besoins = cadres.map(function(c){
      var svg = c.querySelector('svg');
      var l = svg.getBoundingClientRect().width;
      if(!l) return 0;
      var mini = Infinity;
      svg.querySelectorAll('text, tspan').forEach(function(t){
        if(!t.firstChild || !t.getClientRects().length) return;
        var fs = parseFloat(getComputedStyle(t).fontSize) || 0, m = t.getScreenCTM && t.getScreenCTM();
        if(!fs || !m) return;
        var px = fs * Math.sqrt(Math.abs(m.a * m.d - m.b * m.c));
        if(px > 0 && px < mini) mini = px;
      });
      return (isFinite(mini) && mini < 12) ? Math.ceil(l * 12.1 / mini) : 0;
    });
    cadres.forEach(function(c, i){
      if(!besoins[i]) return;
      c.classList.add('lisible');
      c.style.setProperty('--svg-min', besoins[i] + 'px');
    });
    var trop = cadres.map(function(c, i){ return besoins[i] && besoins[i] > c.clientWidth + 1; });
    cadres.forEach(function(c, i){ if(trop[i]) c.classList.add('defile'); });
  }

'''
s = s[:old_start] + new + s[old_end:]
open(p, 'w').write(s)

p = 'contenu.css'
s = open(p).read()
old = s[s.index('/* Schéma dont un libellé passerait sous 12 px'):s.index('/* Code (informatique)')]
new = '''/* Schéma dont un libellé passerait sous 12 px : le script lui donne une largeur minimale
   (--svg-min, .lisible) ; la figure s'élargit jusqu'à la colonne (au téléphone, jusque dans la
   gouttière), puis défile en largeur si cela ne suffit pas (.defile). */
figure.schema.lisible{ max-width:max(540px, var(--svg-min, 0px)); }
figure.schema.lisible svg, .cine-svg-wrap.lisible svg{ min-width:var(--svg-min, 0px); }
figure.schema.defile, .cine-svg-wrap.defile{ overflow-x:auto; overflow-y:hidden; padding-block:.25rem; scrollbar-width:thin; }
.cine-svg-wrap.defile{ justify-content:safe center; }
/* Libellés blancs posés sur une pastille colorée (molécules, ions) : couleur de la feuille, lisible
   dans les deux thèmes (la pastille s'éclaircit en sombre) */
.schema text[style*="fill:#fff"]{ fill:var(--sheet) !important; }

'''
s = s.replace(old, new)
old = "/* Formule suivie de sa ponctuation"
new = """/* MathML d'accessibilité (masqué par clip mais aussi large que la formule native) : il ne doit
   pas élargir la page quand une formule en ligne finit près du bord droit */
mjx-container.MathJax[jax] > mjx-assistive-mml:not([display="block"]){ width:1px !important; }
/* Formule suivie de sa ponctuation"""
assert s.count(old) == 1; s = s.replace(old, new)
old = "  .exo{ padding:1.1rem 1rem 1.2rem; }"
new = """  figure.schema.lisible{ max-width:none; margin-left:calc(var(--gutter) * -1 + 4px); margin-right:calc(var(--gutter) * -1 + 4px); }
  .exo{ padding:1.1rem 1rem 1.2rem; }"""
assert s.count(old) == 1; s = s.replace(old, new)
old = ".cine-svg-wrap svg{ max-width:100%; height:auto; border:1px solid var(--line); background:var(--sheet); border-radius:var(--r-s); }"
new = old + "\n.cine-svg-wrap text[opacity]{ opacity:1; fill:var(--text-3); }   /* libellé estompé : encre 3 (≥ 4,5:1) plutôt qu'une opacité */"
assert s.count(old) == 1; s = s.replace(old, new)
open(p, 'w').write(s)

p = 'simu.css'
s = open(p).read()
old = "#lor-params{ color:var(--text-2) !important; opacity:1 !important; }"
new = old + """
/* Libellés du tracé (couleurs et opacités en attributs, posés par lorDraw) : encres du thème */
#lor-svg text{ opacity:1 !important; }
#lor-svg text[fill="var(--ink)"]{ fill:var(--text-3); }
#lor-svg [fill="#e74c3c"]{ fill:var(--rouge); } #lor-svg [stroke="#e74c3c"]{ stroke:var(--rouge-vif); }
#lor-svg [fill="#2ecc71"]{ fill:var(--vert); } #lor-svg [stroke="#2ecc71"]{ stroke:var(--vert-vif); }
#lor-svg [fill="#3498db"]{ fill:var(--physique); } #lor-svg [stroke="#3498db"]{ stroke:var(--physique-vif); }"""
assert s.count(old) == 1; s = s.replace(old, new)
old = """  .sim-controls{ padding:1rem; }
}"""
new = """  .sim-controls{ padding:1rem; }
  #lor-svg text{ font-size:17px; }   /* tracé réduit à ~70 % : libellés ≥ 12 px à l'écran */
}"""
assert s.count(old) == 1; s = s.replace(old, new)
open(p, 'w').write(s)
print('sources modifiées')
