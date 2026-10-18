#!/usr/bin/env python3
"""Contrôle de cascade du rangement en régions : liste les paires de règles dont
l'ordre relatif s'inverse (A avant B à l'origine, B avant A après rangement),
qui déclarent une même propriété (longhands), avec la même importance, une même
spécificité pour au moins un couple de sélecteurs, un même pseudo-élément et des
media compatibles. Sortie JSON : couples de sélecteurs à tester sur le DOM réel
(conflits-dom.js), qui dira si un élément peut porter les deux.
Usage : python3 conflits.py meta.json candidats.json"""
import re, sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cssparse import split_selectors, strip_comments
from regions import REGIONS

LONG = {
    'margin': ['margin-top', 'margin-right', 'margin-bottom', 'margin-left'],
    'padding': ['padding-top', 'padding-right', 'padding-bottom', 'padding-left'],
    'inset': ['top', 'right', 'bottom', 'left'],
    'border-width': ['border-%s-width' % s for s in ('top', 'right', 'bottom', 'left')],
    'border-style': ['border-%s-style' % s for s in ('top', 'right', 'bottom', 'left')],
    'border-color': ['border-%s-color' % s for s in ('top', 'right', 'bottom', 'left')],
    'border-radius': ['border-top-left-radius', 'border-top-right-radius', 'border-bottom-right-radius', 'border-bottom-left-radius'],
    'background': ['background-color', 'background-image', 'background-position', 'background-size', 'background-repeat', 'background-attachment', 'background-origin', 'background-clip'],
    'font': ['font-style', 'font-variant', 'font-weight', 'font-stretch', 'font-size', 'line-height', 'font-family'],
    'flex': ['flex-grow', 'flex-shrink', 'flex-basis'],
    'flex-flow': ['flex-direction', 'flex-wrap'],
    'transition': ['transition-property', 'transition-duration', 'transition-timing-function', 'transition-delay'],
    'animation': ['animation-name', 'animation-duration', 'animation-timing-function', 'animation-delay', 'animation-iteration-count', 'animation-direction', 'animation-fill-mode', 'animation-play-state'],
    'outline': ['outline-width', 'outline-style', 'outline-color'],
    'overflow': ['overflow-x', 'overflow-y'],
    'list-style': ['list-style-type', 'list-style-position', 'list-style-image'],
    'text-decoration': ['text-decoration-line', 'text-decoration-color', 'text-decoration-style', 'text-decoration-thickness'],
    'gap': ['row-gap', 'column-gap'],
    'grid-gap': ['row-gap', 'column-gap'],
    'place-items': ['align-items', 'justify-items'],
    'place-content': ['align-content', 'justify-content'],
    'columns': ['column-width', 'column-count'],
    'grid-template': ['grid-template-rows', 'grid-template-columns', 'grid-template-areas'],
    'grid-area': ['grid-row-start', 'grid-column-start', 'grid-row-end', 'grid-column-end'],
    'grid-row': ['grid-row-start', 'grid-row-end'], 'grid-column': ['grid-column-start', 'grid-column-end'],
    'scroll-margin': ['scroll-margin-top', 'scroll-margin-right', 'scroll-margin-bottom', 'scroll-margin-left'],
}
for side in ('top', 'right', 'bottom', 'left'):
    LONG['border-' + side] = ['border-%s-%s' % (side, k) for k in ('width', 'style', 'color')]
LONG['border'] = sum((LONG['border-' + s] for s in ('top', 'right', 'bottom', 'left')), [])


def longhands(p):
    p = p.strip().lower()
    if p in LONG:
        out = []
        for q in LONG[p]:
            out += longhands(q) if q in LONG else [q]
        return out
    return [p]


def declarations(body):
    out = {}
    for d in strip_comments(body).split(';'):
        if ':' not in d:
            continue
        nom, val = d.split(':', 1)
        nom = nom.strip()
        if not nom or nom.startswith('--'):
            # variables : comparées telles quelles
            if nom:
                out[nom] = '!important' in val
            continue
        imp = '!important' in val.replace(' ', '')
        for l in longhands(nom):
            out[l] = imp
    return out


def specificite(sel):
    s = sel
    a = b = c = 0
    # :not(...) : spécificité de l'argument
    while True:
        m = re.search(r':not\(([^()]*)\)', s)
        if not m:
            break
        x, y, z = specificite(m.group(1))
        a += x; b += y; c += z
        s = s[:m.start()] + s[m.end():]
    c += len(re.findall(r'::[\w-]+', s))
    s = re.sub(r'::[\w-]+', '', s)
    a += len(re.findall(r'#[\w-]+', s))
    s = re.sub(r'#[\w-]+', '', s)
    b += len(re.findall(r'\[[^\]]*\]', s))
    s = re.sub(r'\[[^\]]*\]', '', s)
    b += len(re.findall(r'\.[\w-]+', s))
    s = re.sub(r'\.[\w-]+', '', s)
    b += len(re.findall(r':[\w-]+(\([^)]*\))?', s))
    s = re.sub(r':[\w-]+(\([^)]*\))?', '', s)
    c += len(re.findall(r'(?:^|[\s>+~])([a-zA-Z][\w-]*)', s))
    return (a, b, c)


def pseudo_elt(sel):
    m = re.findall(r'::([\w-]+)', sel)
    return m[-1] if m else ''


def media_type(m):
    if not m:
        return 'tout'
    if 'print' in m:
        return 'print'
    if 'max-width' in m:
        return 'mobile'
    if 'min-width' in m:
        return 'desktop'
    return 'tout'   # prefers-*


def compatibles(m1, m2):
    t1, t2 = media_type(m1), media_type(m2)
    if 'tout' in (t1, t2):
        return True
    if t1 == t2:
        return True
    return False   # mobile/desktop/print exclusifs entre eux


def main():
    meta = json.load(open(sys.argv[1]))
    for m in meta:
        m['new'] = (REGIONS.index(m['region']), m['rang'], m['sub'])
        m['decl'] = declarations(m['body'])
        m['sels'] = split_selectors(m['prelude'])
    cands = []
    n = len(meta)
    for i in range(n):
        A = meta[i]
        for j in range(n):
            B = meta[j]
            if not (A['orig'] < B['orig'] and A['new'] > B['new']):
                continue
            if not compatibles(A['media'], B['media']):
                continue
            props = [p for p in A['decl'] if p in B['decl'] and A['decl'][p] == B['decl'][p]]
            if not props:
                continue
            for sa in A['sels']:
                for sb in B['sels']:
                    if specificite(sa) != specificite(sb) or pseudo_elt(sa) != pseudo_elt(sb):
                        continue
                    cands.append({'a': sa, 'b': sb, 'regA': A['region'], 'regB': B['region'],
                                  'lineA': A['line'], 'lineB': B['line'], 'props': props,
                                  'mediaA': A['media'], 'mediaB': B['media']})
    json.dump(cands, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
    print(len(cands), 'couples candidats')


if __name__ == '__main__':
    main()
