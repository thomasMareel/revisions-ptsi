#!/usr/bin/env python3
"""Étape 1 : classement + candidats de conflit (sans écrire index.html)."""
import os, sys, json, subprocess
S = os.path.dirname(os.path.abspath(__file__))
IDX = sys.argv[1] if len(sys.argv) > 1 else '/home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-1/index.html'
subprocess.run([sys.executable, os.path.join(S, 'regions.py'), IDX, '--json', os.path.join(S, 'meta.json')], check=True)
subprocess.run([sys.executable, os.path.join(S, 'conflits.py'), os.path.join(S, 'meta.json'), os.path.join(S, 'candidats.json')], check=True)
c = json.load(open(os.path.join(S, 'candidats.json')))
for x in c:
    print(x['regA'], x['lineA'], repr(x['a']), '|', x['regB'], x['lineB'], repr(x['b']), x['props'][:4], x['mediaA'] or '', x['mediaB'] or '')
