#!/usr/bin/env python3
"""Petit analyseur CSS (niveau bloc) pour ranger le grand <style> d'index.html.
Items : {'kind': 'rule'|'at'|'group', 'prelude', 'text', 'lead' (commentaires et
blancs qui précèdent), 'line', 'children' (pour @media/@supports)}."""
import re

GROUP_AT = ('@media', '@supports', '@container', '@layer')


def _skip_string(s, i):
    q = s[i]
    i += 1
    while i < len(s):
        if s[i] == '\\':
            i += 2
            continue
        if s[i] == q:
            return i + 1
        i += 1
    return i


def _match_brace(s, i):
    """s[i] == '{' ; renvoie l'indice juste après l'accolade fermante."""
    depth = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c == '/' and s.startswith('/*', i):
            j = s.find('*/', i + 2)
            i = n if j < 0 else j + 2
            continue
        if c in '"\'':
            i = _skip_string(s, i)
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError('accolade non fermée')


def parse(s, base_line=1, offset=0):
    """Analyse s (contenu d'un bloc) ; renvoie (items, trailing)."""
    items = []
    i = 0
    n = len(s)
    lead_start = 0
    while True:
        # avancer sur blancs et commentaires (ils forment le « lead »)
        while i < n:
            if s[i].isspace():
                i += 1
            elif s.startswith('/*', i):
                j = s.find('*/', i + 2)
                i = n if j < 0 else j + 2
            else:
                break
        if i >= n:
            break
        lead = s[lead_start:i]
        start = i
        # prélude jusqu'à { ou ;
        j = i
        while j < n and s[j] not in '{;':
            if s[j] in '"\'':
                j = _skip_string(s, j)
                continue
            if s.startswith('/*', j):
                k = s.find('*/', j + 2)
                j = n if k < 0 else k + 2
                continue
            j += 1
        if j >= n:
            raise ValueError('prélude sans bloc : %r' % s[start:start + 80])
        prelude = s[start:j].strip()
        line = base_line + s.count('\n', 0, start)
        if s[j] == ';':
            items.append({'kind': 'at', 'prelude': prelude, 'text': s[start:j + 1], 'lead': lead, 'line': line})
            i = j + 1
            lead_start = i
            continue
        end = bend = _match_brace(s, j)
        # commentaire sur la même ligne, juste après l'accolade : il appartient à la règle
        m = re.match(r'[ \t]*/\*.*?\*/', s[end:], re.S)
        if m and '\n' not in m.group(0):
            end += m.end()
        text = s[start:end]
        if prelude.lower().startswith(GROUP_AT):
            inner = s[j + 1:bend - 1]
            inner_line = base_line + s.count('\n', 0, j + 1)
            children, trailing = parse(inner, inner_line)
            items.append({'kind': 'group', 'prelude': prelude, 'text': text, 'lead': lead,
                          'line': line, 'children': children, 'trailing': trailing})
        elif prelude.startswith('@'):
            items.append({'kind': 'at', 'prelude': prelude, 'text': text, 'lead': lead, 'line': line})
        else:
            items.append({'kind': 'rule', 'prelude': prelude, 'text': text, 'lead': lead, 'line': line})
        i = end
        lead_start = i
    trailing = s[lead_start:]
    return items, trailing


def split_selectors(prelude):
    """Découpe une liste de sélecteurs sur les virgules de premier niveau."""
    out, depth, cur = [], 0, ''
    for c in prelude:
        if c in '([':
            depth += 1
        elif c in ')]':
            depth -= 1
        if c == ',' and depth == 0:
            out.append(cur.strip())
            cur = ''
        else:
            cur += c
    if cur.strip():
        out.append(cur.strip())
    return out


def strip_comments(t):
    return re.sub(r'/\*.*?\*/', '', t, flags=re.S)
