#!/usr/bin/env python3
"""Remplace l'IIFE urlRouting (sommaire de matière + retour Android) et ajoute
l'horodatage t à lastPos. Usage : python3 etape_routage.py index.html routage.js"""
import sys
p, frag = sys.argv[1:3]
s = open(p, encoding='utf-8').read()
deb = s.index("(function urlRouting(){\n  let lastChap = null;")
marq = "  window.__navFromHash = navFromHash;\n})();"
fin = s.index(marq, deb) + len(marq)
neuf = open(frag, encoding='utf-8').read().rstrip('\n')
s = s[:deb] + neuf + s[fin:]
a = "      Store.setJSON('lastPos', {chap:chapId, panel: activePanel?activePanel.id:null});"
b = "      if(chap) Store.setJSON('lastPos', {chap:chap.id, panel:t.dataset.panel});"
c = "    Store.setJSON('lastPos', {chap:chapId, panel:panelId||null});"
for x in (a, b, c):
    assert s.count(x) == 1, x
s = s.replace(a, "      Store.setJSON('lastPos', {chap:chapId, panel: activePanel?activePanel.id:null, t:Date.now()});")
s = s.replace(b, "      if(chap) Store.setJSON('lastPos', {chap:chap.id, panel:t.dataset.panel, t:Date.now()});")
s = s.replace(c, "    Store.setJSON('lastPos', {chap:chapId, panel:panelId||null, t:Date.now()});")
open(p, 'w', encoding='utf-8').write(s)
print('routage remplacé')
