#!/usr/bin/env python3
"""Affiche des plages de lignes d'index.html. Usage : python3 lignes.py A,B [C,D …]"""
import sys
L = open('/home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-3/index.html', encoding='utf-8').read().split('\n')
for r in sys.argv[1:]:
    a, b = map(int, r.split(','))
    print('==', r)
    for i in range(a, b + 1):
        print(i, L[i - 1][:170])
