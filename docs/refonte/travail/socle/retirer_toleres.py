#!/usr/bin/env python3
"""Retire de TOLERES (tests/suites/visuel.js) les sélecteurs que la suite signale
comme « plus constatés » (section de visuel.md). Rend la liste plus stricte."""
import re, sys
visuel_js, visuel_md = sys.argv[1:3]
md = open(visuel_md, encoding='utf-8').read()
sec = md.split('## Sélecteurs de TOLERES plus constatés (à retirer)', 1)[1].split('\n## ', 1)[0]
a_retirer = re.findall(r"- `([^`]+)` \((\w+), écrans ([^,]+), thèmes ([^,]+), appareils ([^)]+)\)", sec)
s = open(visuel_js, encoding='utf-8').read()
lignes = s.split('\n')
retires = 0
for sel, mesure, ecrans, themes, apps in a_retirer:
    trouve = False
    for i, l in enumerate(lignes):
        if l is None:
            continue
        m = re.match(r"(\s*)\['(\w+)', '([^']*)', '([^']*)', '([^']*)', \{(.*)\}\],\s*$", l)
        if not m or (m.group(2), m.group(3), m.group(4), m.group(5)) != (mesure, ecrans.strip(), themes.strip(), apps.strip()):
            continue
        entrees = re.findall(r"'((?:[^'\\]|\\.)*)': ([\d.]+)", m.group(6))
        neuves = [(k, v) for k, v in entrees if k != sel]
        if len(neuves) == len(entrees):
            continue
        trouve = True
        retires += 1
        if neuves:
            lignes[i] = "%s['%s', '%s', '%s', '%s', { %s }]," % (m.group(1), mesure, m.group(3), m.group(4), m.group(5),
                                                            ', '.join("'%s': %s" % (k, v) for k, v in neuves))
        else:
            lignes[i] = None
        break
    if not trouve:
        print('INTROUVABLE', sel, mesure, ecrans, themes, apps)
s = '\n'.join(l for l in lignes if l is not None)
open(visuel_js, 'w', encoding='utf-8').write(s)
print(retires, 'sélecteurs retirés sur', len(a_retirer))
