# Contrôle des contrastes sur les JETONS (tokens.css), thème clair et sombre.
# 1) vérifie que le bloc « Auto + système sombre » est identique au bloc sombre ;
# 2) résout les var() et calcule le ratio WCAG 2.x de chaque paire réellement
#    employée par les composants (texte 4,5:1 ; éléments graphiques 3:1) ;
# 3) calcule les écarts OKLab entre encres (matières et états) — information.
#   python3 -I contrastes-jetons.py ../tokens.css [sortie.json]
import re, sys, json, os, itertools
sys.path.insert(0, os.path.dirname(__file__))
from couleur import dist
src = open(sys.argv[1], encoding='utf-8').read()
nc = re.sub(r'/\*.*?\*/', '', src, flags=re.S)
def body_after(pattern, text):
    m = re.search(pattern + r'\s*\{', text); i = m.end(); d = 1; j = i
    while d:
        d += {'{': 1, '}': -1}.get(text[j], 0); j += 1
    return text[i:j - 1]
decls = lambda b: dict(re.findall(r'(--[\w-]+)\s*:\s*([^;]+);', b))
light = {}
for m in re.finditer(r'(?m)^:root\s*\{', nc):
    light.update(decls(body_after(r'(?m)^:root', nc[m.start():])))
dark_over = decls(body_after(r':root\[data-theme="dark"\]', nc))
media = body_after(r'@media \(prefers-color-scheme: dark\)', nc)
auto_over = decls(body_after(r':root:not\(\[data-theme-pref\]\):not\(\[data-theme\]\)', media))
same = dark_over == auto_over
dark = dict(light); dark.update(dark_over)
def resolve(env, v, d=0):
    v = v.strip(); m = re.fullmatch(r'var\((--[\w-]+)\)', v)
    return resolve(env, env[m.group(1)], d + 1) if m and d < 10 else v
def rgba(c):
    c = c.strip()
    if c.startswith('#'):
        h = c[1:]; h = ''.join(x * 2 for x in h) if len(h) == 3 else h
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (1.0,)
    p = [float(x) for x in re.split(r'[ ,/]+', re.match(r'rgba?\(([^)]+)\)', c).group(1).strip()) if x]
    return (p[0], p[1], p[2], p[3] if len(p) > 3 else 1.0)
over = lambda fg, bg: tuple(fg[i] * fg[3] + bg[i] * (1 - fg[3]) for i in range(3)) + (1.0,)
def lum(c):
    v = [(x / 255) / 12.92 if x / 255 <= 0.04045 else (((x / 255) + 0.055) / 1.055) ** 2.4 for x in c[:3]]
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]
ratio = lambda a, b: (max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05)
def col(env, name):
    if '@' in name:
        a, b = name.split('@', 1); return over(rgba(resolve(env, env[a])), col(env, b))
    return rgba(resolve(env, env[name]))
hexof = lambda env, n: '#%02x%02x%02x' % tuple(int(round(x)) for x in col(env, n)[:3])
MATS = ['physique', 'maths', 'si', 'info', 'anglais']; SEM = ['rouge', 'ambre', 'vert']
BGS = ['--sheet', '--desk', '--sunk', '--raise', '--bristol']
P = []
for t in ['--text', '--text-2', '--text-3']:
    for b in BGS: P.append((t, b, 4.5, 'texte'))
    P.append((t, '--hover@--sheet', 4.5, 'texte sur survol'))
# NB : l'anneau de focus est toujours décalé de 2 px (outline-offset) : il touche le FOND,
# jamais le bouton ; d'où les paires focus/fonds ci-dessous et aucune paire focus/bouton.
P += [('--on-primary', '--primary', 4.5, 'bouton principal'), ('--on-primary', '--primary-hover', 4.5, 'bouton principal survolé'),
      ('--on-rouge-plein', '--rouge-plein', 4.5, 'compteur plein « 37 »'),
      ('--link', '--sheet', 4.5, 'lien'), ('--link', '--sunk', 4.5, 'lien dans un creux'),
      ('--field', '--sheet', 3, 'contour de champ'), ('--field', '--raise', 3, 'contour de champ (menu)'), ('--field', '--sunk', 3, 'segment choisi / champ en creux'), ('--field', '--desk', 3, 'champ sur le bureau'),
      ('--focus', '--sheet', 3, 'anneau de focus'), ('--focus', '--raise', 3, 'anneau de focus'), ('--focus', '--desk', 3, 'anneau de focus'), ('--focus', '--sunk', 3, 'anneau de focus'),
      ('--text', '--selection@--sheet', 4.5, 'texte sélectionné'), ('--text-3', '--selection@--sheet', 4.5, 'texte 3 sélectionné'),
      ('--text-3', '--note-nv', 1, 'information : jamais vue (barre, pas de texte)')]
for m in MATS:
    P += [(f'--{m}', '--sheet', 4.5, f'encre {m}'), (f'--{m}', '--desk', 4.5, f'encre {m} sur le bureau'), (f'--{m}', '--raise', 4.5, f'encre {m} sur menu'),
          (f'--{m}', '--sunk', 4.5, f'encre {m} dans un creux'), (f'--{m}', f'--{m}-fond', 4.5, f'encre {m} sur sa teinte (onglet, intercalaire, Définition)'),
          ('--text', f'--{m}-fond', 4.5, f'texte sur teinte {m}'), ('--text-2', f'--{m}-fond', 4.5, f'texte 2 sur teinte {m} (méta de l\'intercalaire)'),
          ('--text-3', f'--{m}-fond', 4.5, f'texte 3 sur teinte {m}'),
          (f'--{m}-vif', '--sheet', 3, f'trait/pastille {m}'), (f'--{m}-vif', f'--{m}-fond', 3, f'trait {m} sur sa teinte'), (f'--{m}-vif', '--desk', 3, f'pastille {m} sur le bureau'), (f'--{m}-vif', '--raise', 3, f'pastille {m} sur menu')]
for s in SEM:
    P += [(f'--{s}', '--sheet', 4.5, s), (f'--{s}', '--raise', 4.5, f'{s} sur carte'), (f'--{s}', '--sunk', 4.5, f'{s} dans un creux'), (f'--{s}', f'--{s}-fond', 4.5, f'{s} sur sa teinte (notation, À noter, Correction)'),
          ('--text', f'--{s}-fond', 4.5, f'texte sur teinte {s}'), (f'--{s}-vif', '--sheet', 3, f'barre {s}'), (f'--{s}-vif', f'--{s}-fond', 3, f'trait {s} sur sa teinte'), (f'--{s}-vif', '--raise', 3, f'barre {s} sur carte')]
for legacy in ['--ink', '--accent', '--accent2', '--green', '--amber', '--muted']:
    for b in ['--paper', '--paper-dark']: P.append((legacy, b, 4.5, f'{legacy} (contenu inline) sur {b}'))
res = {'auto_identique_au_sombre': same}; bad = 0
for theme, env in [('clair', light), ('sombre', dark)]:
    rows = []
    for fg, bg, th, use in P:
        r = ratio(col(env, fg), col(env, bg)); ok = r >= th; bad += not ok
        rows.append({'avant': fg, 'fond': bg, 'couleurs': f'{hexof(env, fg)} / {hexof(env, bg)}', 'ratio': round(r, 2), 'seuil': th, 'ok': ok, 'usage': use})
    res[theme] = rows
    enc = {k: hexof(env, '--' + k) for k in MATS + SEM}
    res[theme + '_ecarts_oklab'] = {f'{a}/{b}': round(dist(enc[a], enc[b]), 1) for a, b in itertools.combinations(enc, 2)}
print(f"Bloc « Auto + système sombre » identique au bloc sombre : {'oui' if same else 'NON'}")
for theme in ('clair', 'sombre'):
    rows = [r for r in res[theme] if r['seuil'] > 1]; mn = min(rows, key=lambda x: x['ratio'] / x['seuil'])
    mt = min([r for r in rows if r['seuil'] == 4.5], key=lambda x: x['ratio']); mg = min([r for r in rows if r['seuil'] == 3], key=lambda x: x['ratio'])
    print(f"{theme:7s}: {sum(r['ok'] for r in rows)}/{len(rows)} paires conformes ; texte min {mt['ratio']}:1 ({mt['avant']} sur {mt['fond']}) ; graphique min {mg['ratio']}:1 ({mg['avant']} sur {mg['fond']})")
    for r in rows:
        if not r['ok']: print('   ÉCHEC', r)
    e = res[theme + '_ecarts_oklab']; low = sorted(e.items(), key=lambda kv: kv[1])[:5]
    print('         écarts OKLab les plus courts :', ', '.join(f'{k} {v}' for k, v in low))
res['echecs'] = bad
if len(sys.argv) > 2: json.dump(res, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
sys.exit(1 if bad or not same else 0)
