#!/usr/bin/env python3
"""Résumé des constats d'un visuel.json : python3 constats.py <dossier-sortie-visuel>"""
import json, collections, sys
d = json.load(open(sys.argv[1] + '/visuel.json'))
cs = d['constats'] if isinstance(d, dict) and 'constats' in d else d
if isinstance(d, dict) and 'constats' not in d:
    print('clés :', list(d.keys())); sys.exit()
g = collections.defaultdict(lambda: {'n': 0, 'ecrans': set(), 'pire': None})
for c in cs:
    k = (c['mesure'], c['selecteur'])
    x = g[k]; x['n'] += 1; x['ecrans'].add(c['ecran'] + '/' + c['theme'][0] + c['appareil'][0])
    v = c['valeur']; x['pire'] = v if x['pire'] is None else min(x['pire'], v)
for (m, s), x in sorted(g.items()):
    print(m, '|', s, '|', x['pire'], '|', ' '.join(sorted(x['ecrans']))[:160])
