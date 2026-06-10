#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verification syntaxique de tous les blocs <script> inline d'index.html.

Extrait chaque bloc <script> (sans src=), le passe a `node --check`, et
rapporte les erreurs avec la ligne approximative dans index.html.
Sortie ASCII-safe. Exit 0 si tout est bon, 1 sinon.
"""
import re
import subprocess
import tempfile
import os
import sys

PATH = 'index.html'


def main():
    with open(PATH, encoding='utf-8') as f:
        html = f.read()

    blocks = []
    for m in re.finditer(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', html, re.S | re.I):
        start_line = html[:m.start(1)].count('\n') + 1
        blocks.append((start_line, m.group(1)))

    print('blocs script inline:', len(blocks))
    errors = 0
    tmpdir = tempfile.mkdtemp()
    for i, (line0, code) in enumerate(blocks):
        p = os.path.join(tmpdir, 'b%d.js' % i)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(code)
        r = subprocess.run(['node', '--check', p], capture_output=True, text=True)
        if r.returncode != 0:
            errors += 1
            msg = (r.stderr or '').strip().splitlines()
            loc = ''
            for ln in msg:
                mm = re.search(r'b%d\.js:(\d+)' % i, ln)
                if mm:
                    loc = 'ligne index.html ~' + str(line0 + int(mm.group(1)) - 1)
                    break
            print('[ERREUR] bloc %d (debut l.%d) %s' % (i, line0, loc))
            for ln in msg[:6]:
                print('   ', ln.encode('ascii', 'replace').decode())
    print('blocs en erreur:', errors)
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
