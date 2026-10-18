#!/usr/bin/env python3
"""Remplace dans PRECACHE (sw.js) les entrées vendor/fonts/… par polices.css et
les 14 woff2 présents dans vendor/fonts/ (ordre alphabétique)."""
import os, re, sys
racine = sys.argv[1]
p = os.path.join(racine, 'sw.js')
s = open(p, encoding='utf-8').read()
lignes = s.split('\n')
fontes = sorted(f for f in os.listdir(os.path.join(racine, 'vendor/fonts')) if f.endswith('.woff2'))
neuves = ["  'vendor/fonts/polices.css',"] + ["  'vendor/fonts/%s'," % f for f in fontes]
out, insere = [], False
for l in lignes:
    if re.match(r"\s*'vendor/fonts/", l):
        if not insere:
            out.extend(neuves)
            insere = True
        continue
    out.append(l)
assert insere
open(p, 'w', encoding='utf-8').write('\n'.join(out))
print(len(fontes), 'polices')
