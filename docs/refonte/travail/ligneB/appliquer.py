#!/usr/bin/env python3
"""Applique les sources de la ligne B à index.html : régions CONTENU et SIMU (contenu.css,
simu.css) et module « CONTENU » (module.js, remplacé en place)."""
import re
D = '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/ligneB/'
P = '/home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-3/index.html'
src = open(P, encoding='utf-8').read()

def region(src, nom, fichier):
    neuf = open(D + fichier, encoding='utf-8').read().strip('\n')
    debut = '/* ===== RÉGION %s ===== */\n' % nom
    fin = '/* ===== FIN RÉGION %s ===== */' % nom
    i = src.index(debut)
    j = src.index('*/', i + len(debut)) + 2
    k = src.index(fin, j)
    return src[:j] + '\n\n' + neuf + '\n\n' + src[k:]

src = region(src, 'CONTENU', 'contenu.css')
src = region(src, 'SIMU', 'simu.css')
mod = open(D + 'module.js', encoding='utf-8').read().strip('\n')
a = src.index('<script>\n/* ===== CONTENU : enrichissements')
b = src.index('</script>', a) + len('</script>')
src = src[:a] + mod + src[b:]
open(P, 'w', encoding='utf-8').write(src)
print('CONTENU, SIMU et module appliqués')
