#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Étiquetage automatique conservateur des flashcards-formules (cat:'form').

Ajoute `, cat:'form'` aux cartes dont la RÉPONSE est sans ambiguïté une formule :
contient '=', contient au moins un symbole mathématique, est courte (<= 60 car.)
et ne contient aucun mot de liaison français (sinon = prose / définition).
N'altère jamais q/a ; ne touche pas les cartes déjà étiquetées (elles finissent
par 'form'} ou 'val'} et non par "}). Précision privilégiée sur le rappel.
"""
import re, sys

PATH = 'index.html'

STOP = [' le ', ' la ', ' les ', ' est ', ' sont ', ' une ', ' un ', ' des ', ' du ',
        ' de ', ' pour ', ' quand ', ' donc ', ' avec ', ' où ', ' qui ', ' que ',
        ' ou ', ' et ', ' on ', ' se ', ' au ', ' aux ', ' par ', ' dans ', ' sur ',
        ' si ', ' plus ', ' moins ', ' entre ', ' selon ', ' chaque ', ' tout ',
        ' toute ', ' alors ', ' car ', ' mais ', ' puis ', ' soit ', ' vers ', ' sans ',
        ' leur ', ' cette ', ' ce ', ' il ', ' elle ', ' on ', ' son ', ' sa ', ' ses ',
        ' nombre ', ' valeur ', ' unité ', ' axe ', ' point ', ' droite ', ' courbe ']
MATH = re.compile(r'[0-9√/·×÷^∑∏∫∂∇πθλμνωαβγδεζηξφϕψρστΩ²³⁰¹⁴⁵⁶⁷⁸⁹ⁿ₀₁₂₃₄₅₆₇₈₉±∓≤≥≠≈∝]')
CARD = re.compile(r'^\s*\{q:".*",\s*a:"(.*)"\}\s*,?\s*$')
OPEN = re.compile(r'const \w+Cards\s*=\s*\[')

def qualifies(ans):
    if '=' not in ans:
        return False
    if len(ans) > 60:
        return False
    if not MATH.search(ans):
        return False
    low = ' ' + ans.lower() + ' '
    if any(w in low for w in STOP):
        return False
    return True

def main():
    with open(PATH, encoding='utf-8') as f:
        lines = f.readlines()
    inblock = False
    tagged = 0
    samples = []
    for i, ln in enumerate(lines):
        s = ln.rstrip('\n')
        if OPEN.search(s):
            inblock = True
        if inblock and re.match(r'^\];', s):
            inblock = False
            continue
        if not inblock:
            continue
        m = CARD.match(s)
        if not m:
            continue
        ans = m.group(1)
        if not qualifies(ans):
            continue
        if s.endswith('"},'):
            new = s[:-3] + "\", cat:'form'},"
        elif s.endswith('"}'):
            new = s[:-2] + "\", cat:'form'}"
        else:
            continue
        lines[i] = new + '\n'
        tagged += 1
        if len(samples) < 12:
            samples.append(ans)
    with open(PATH, 'w', encoding='utf-8', newline='\n') as f:
        f.writelines(lines)
    # Affichage ASCII-safe (console Windows cp1252) : on évite d'imprimer les
    # symboles Unicode des réponses.
    print('cartes etiquetees form:', tagged)

if __name__ == '__main__':
    main()
