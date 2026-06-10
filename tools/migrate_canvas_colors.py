#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Migration des couleurs codees en dur des canvas vers le theme (__CV/__CVA).

Ne touche QUE les lignes contenant fillStyle / strokeStyle / addColorStop /
shadowColor (donc uniquement du code de dessin canvas). Sur ces lignes :
  - les hex de la palette claire ('#c8472e', "#2d5f8a", ...) deviennent
    __CV().accent / .accent2 / .green / .amber / .ink / .muted / .paper ;
  - les rgba(R,G,B,a) de ces memes couleurs deviennent __CVA('nom', a).
Les rgba(0,0,0,x) (ombres) sont laisses tels quels.
Affiche le compte de remplacements par motif + les couleurs quotees restantes
sur ces lignes (a traiter manuellement le cas echeant). Sortie ASCII-safe.
"""
import re

PATH = 'index.html'
LINE_FILTER = re.compile(r'fillStyle|strokeStyle|addColorStop|shadowColor')

# hex (insensible a la casse) -> expression theme
HEX_MAP = {
    '#c8472e': '__CV().accent',
    '#2d5f8a': '__CV().accent2',
    '#5a7a3a': '__CV().green',
    '#b8801a': '__CV().amber',
    '#1a1d24': '__CV().ink',
    '#1a1a1a': '__CV().ink',
    '#222':    '__CV().ink',
    '#222222': '__CV().ink',
    '#333':    '__CV().ink',
    '#333333': '__CV().ink',
    '#444':    '__CV().ink',
    '#444444': '__CV().ink',
    '#555':    '__CV().ink',
    '#555555': '__CV().ink',
    '#666':    '__CV().muted',
    '#666666': '__CV().muted',
    '#777':    '__CV().muted',
    '#777777': '__CV().muted',
    '#888':    '__CV().muted',
    '#888888': '__CV().muted',
    '#999':    '__CV().muted',
    '#999999': '__CV().muted',
    '#aaa':    "__CVA('ink',0.35)",
    '#aaaaaa': "__CVA('ink',0.35)",
    '#bbb':    "__CVA('ink',0.3)",
    '#bbbbbb': "__CVA('ink',0.3)",
    '#ccc':    "__CVA('ink',0.25)",
    '#cccccc': "__CVA('ink',0.25)",
    '#ddd':    "__CVA('ink',0.2)",
    '#dddddd': "__CVA('ink',0.2)",
    '#fff':    '__CV().paper',
    '#ffffff': '__CV().paper',
    '#f4f1e8': '__CV().paper',
}

# (R,G,B) -> nom de couleur theme pour les rgba(...)
RGBA_MAP = {
    (200, 71, 46):  'accent',
    (45, 95, 138):  'accent2',
    (90, 122, 58):  'green',
    (184, 128, 26): 'amber',
    (26, 29, 36):   'ink',
    (255, 255, 255): 'paper',
    (244, 241, 232): 'paper',
}

RGBA_RE = re.compile(r"(['\"])rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([0-9.]+)\s*\)\1")
QUOTED_COLOR_RE = re.compile(r"(['\"])(#[0-9a-fA-F]{3,8}|rgba?\([^'\"]*\))\1")


def main():
    with open(PATH, encoding='utf-8') as f:
        lines = f.readlines()

    counts = {}
    leftovers = []  # (numero de ligne, couleur restante)

    for i, line in enumerate(lines):
        if not LINE_FILTER.search(line):
            continue
        new = line

        # 1) hex quotes
        for hexa, repl in HEX_MAP.items():
            pat = re.compile(r"(['\"])" + re.escape(hexa) + r"\1", re.IGNORECASE)
            new, n = pat.subn(repl, new)
            if n:
                counts[hexa] = counts.get(hexa, 0) + n

        # 2) rgba quotes
        def rgba_sub(m):
            rgb = (int(m.group(2)), int(m.group(3)), int(m.group(4)))
            alpha = m.group(5)
            if rgb in RGBA_MAP:
                key = 'rgba' + str(rgb)
                counts[key] = counts.get(key, 0) + 1
                return "__CVA('" + RGBA_MAP[rgb] + "'," + alpha + ")"
            return m.group(0)  # rgba inconnu (ex. noir pur) : laisser

        new = RGBA_RE.sub(rgba_sub, new)

        # 3) recenser ce qui reste de quote-colore sur la ligne
        for m in QUOTED_COLOR_RE.finditer(new):
            col = m.group(2)
            if not col.startswith('rgba(0,'):  # ombres noires tolerees
                leftovers.append((i + 1, col))

        lines[i] = new

    with open(PATH, 'w', encoding='utf-8', newline='\n') as f:
        f.writelines(lines)

    total = sum(counts.values())
    print('remplacements totaux:', total)
    for k in sorted(counts):
        print('  ', k.encode('ascii', 'replace').decode(), '->', counts[k])
    print('couleurs quotees restantes sur lignes canvas:', len(leftovers))
    for ln, col in leftovers[:40]:
        print('   ligne', ln, ':', col.encode('ascii', 'replace').decode())


if __name__ == '__main__':
    main()
