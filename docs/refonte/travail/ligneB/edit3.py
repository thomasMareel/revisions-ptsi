#!/usr/bin/env python3
"""Ponctuation collée : la formule trop large garde sa ponctuation (largeur max réduite)."""
import os
os.chdir('/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/ligneB')
p = 'module.js'
s = open(p).read()
old = """      var large = m.classList.contains('mj-large');
      var nat = large ? m.scrollWidth : m.getBoundingClientRect().width;
      decisions.push([m, dispo > 0 && nat > dispo + 1]);
    });
    decisions.forEach(function(x){
      x[0].classList.toggle('mj-large', x[1]);
      var p = x[0].parentNode;
      if(p && p.classList && p.classList.contains('mj-colle')) p.classList.toggle('libre', x[1]);
    });"""
new = """      var large = m.classList.contains('mj-large');
      var l = m.getBoundingClientRect().width;
      var nat = large ? m.scrollWidth : l;
      // ponctuation collée (.mj-colle, insécable) : elle doit tenir sur la même ligne que la formule
      var p = m.parentNode, colle = 0;
      if(p && p.classList && p.classList.contains('mj-colle')) colle = Math.max(0, p.getBoundingClientRect().width - l);
      decisions.push([m, dispo > 0 && nat + colle > dispo + 1]);
    });
    decisions.forEach(function(x){ x[0].classList.toggle('mj-large', x[1]); });"""
assert s.count(old) == 1; s = s.replace(old, new)
open(p, 'w').write(s)
p = 'contenu.css'
s = open(p).read()
old = """/* Formule suivie de sa ponctuation (« … \\(x\\). ») : jamais séparées en fin de ligne (sauf formule
   plus large que sa ligne : .libre) */
.mj-colle{ white-space:nowrap; }
.mj-colle.libre{ white-space:normal; }"""
new = """/* Formule suivie de sa ponctuation (« … \\(x\\). ») : jamais séparées en fin de ligne ; une formule
   trop large y laisse la place de sa ponctuation */
.mj-colle{ white-space:nowrap; }
.mj-colle > mjx-container.mj-large:not([display="true"]){ max-width:calc(100% - 1em); }"""
assert s.count(old) == 1, 'css'; s = s.replace(old, new)
open(p, 'w').write(s)
print('ok')
