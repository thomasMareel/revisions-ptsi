p = '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/socle/cssparse.py'
s = open(p).read()
old = '''        end = _match_brace(s, j)
        text = s[start:end]'''
new = '''        end = _match_brace(s, j)
        # commentaire sur la même ligne, juste après l'accolade : il appartient à la règle
        m = re.match(r'[ \\t]*/\\*.*?\\*/', s[end:], re.S)
        if m and '\\n' not in m.group(0):
            end += m.end()
        text = s[start:end]'''
assert old in s
s = s.replace(old, new)
open(p, 'w').write(s)

p = '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/socle/regions.py'
s = open(p).read()
rep = [
('''    def ajouter(reg, rang, texte):
        if reg in attente:
            texte = attente.pop(reg) + '\\n' + texte
        frags[reg].append((rang, texte))''', '''    def ajouter(reg, rang, texte, sep='\\n\\n'):
        if reg in attente:
            texte = attente.pop(reg) + '\\n' + texte
        frags[reg].append((rang, sep, texte))'''),
('''        rang += 1
        lead = lead_propre(it['lead'])''', '''        rang += 1
        lead = lead_propre(it['lead'])
        blancs = re.match(r'\\s*', it['lead']).group(0)
        sep = '\\n\\n' if (blancs.count('\\n') >= 2 or lead) else '\\n\''''),
("            ajouter(reg, rang, (lead + '\\n' if lead else '') + it['text'])",
 "            ajouter(reg, rang, (lead + '\\n' if lead else '') + it['text'], sep)"),
("                ajouter(reg, rang, ((lead + '\\n') if (lead and k == 0) else '') + txt)",
 "                ajouter(reg, rang, ((lead + '\\n') if (lead and k == 0) else '') + txt, sep)"),
("            ajouter(reg, rang, ((lead + '\\n') if (lead and k == 0) else '') + bloc)",
 "            ajouter(reg, rang, ((lead + '\\n') if (lead and k == 0) else '') + bloc, sep)"),
('''            out.append('\\n\\n'.join(t for _, t in sorted(frags[reg], key=lambda x: x[0])))''', '''            liste = sorted(frags[reg], key=lambda x: x[0])
            morceaux = []
            for k, (_, sep, t) in enumerate(liste):
                morceaux.append(('' if k == 0 else sep) + t)
            out.append(''.join(morceaux))'''),
]
for a, b in rep:
    assert a in s, a
    s = s.replace(a, b)
open(p, 'w').write(s)
print('ok')
