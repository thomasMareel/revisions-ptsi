#!/usr/bin/env python3
"""Trie les constats de visuel.json : périmètre de la coquille (ligne A, étape 1) ou hors périmètre.
Usage : python3 constats.py visuel.json"""
import json, re, sys, collections
d = json.load(open(sys.argv[1], encoding='utf-8'))
MOI = re.compile(r'(^|[ .#])(hdr|brand|#search-btn|search-btn|today-btn|dash-btn|study-btn|study-menu|rev-badge|theme-|more-|hdr-more|menu-item|mob-|mat-tab|nav-|chip|recent-row|dr-|mbar|bsheet|grab|skip-link|back-to-top|pied|ov-|pcard|sommaire|maj-|kicker|tag2a|count|keys-btn|flag-btn|formula-btn|print-btn|backup-btn|quiz-btn|drill-btn|revise-btn|nav-toggle|read-size)|mark$|^page \(|mob-header|mob-drawer')
ecr_moi = {'tiroir', 'menu-plus'}
moi, autres = collections.defaultdict(list), collections.defaultdict(list)
for c in d['constats']:
    sel = c['selecteur']
    cle = (c['mesure'], sel)
    lieu = c['ecran'] + ' ' + c['theme'] + ' ' + c['appareil']
    dest = moi if (MOI.search(sel) or c['ecran'] in ecr_moi) else autres
    dest[cle].append((lieu, c['valeur'], (c.get('exemples') or [{}])[0].get('texte', ''), (c.get('exemples') or [{}])[0]))
def montrer(t, g):
    print('=====', t, len(g))
    for (m, sel), l in sorted(g.items()):
        pire = min(x[1] for x in l) if m != 'debordement' else max(x[1] for x in l)
        ex = l[0][3]
        print(' %-10s %-50s %6s  %s | %s' % (m, sel[:50], pire, '; '.join(sorted(set(x[0] for x in l)))[:110], (ex.get('texte') or '')[:40] + (' ' + str(ex.get('couleur','')) + ' / ' + str(ex.get('fond','')) if ex.get('couleur') else '')))
montrer('PÉRIMÈTRE COQUILLE', moi)
montrer('HORS PÉRIMÈTRE', autres)
