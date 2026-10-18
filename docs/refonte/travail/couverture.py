#!/usr/bin/env python3
"""Couverture CSS : classes/ids utilisés par le HTML et le JS d'index.html vs
sélecteurs des blocs <style> (hors template d'impression). Usage :
  python3 couverture.py index.html [sortie.json]
Sortie : classes utilisées sans aucune règle CSS (à vérifier), classes stylées
jamais utilisées (CSS mort probable), comptes par classe."""
import re, sys, json, collections
src = open(sys.argv[1], encoding='utf-8').read()
# blocs <style> de la page (le template d'impression est dans une chaîne JS ${CSS})
styles = re.findall(r'<style>(.*?)</style>', src, re.S)
css = '\n'.join(s for s in styles if '${' not in s)
css_nc = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
sel_txt = ' '.join(re.findall(r'([^{}]+)\{', css_nc))
css_classes = set(re.findall(r'\.(-?[A-Za-z_][\w-]*)', sel_txt))
css_ids = set(re.findall(r'#(-?[A-Za-z_][\w-]*)', sel_txt))
# HTML hors <script>/<style>
html = re.sub(r'<script\b.*?</script>', ' ', src, flags=re.S)
html = re.sub(r'<style>.*?</style>', ' ', html, flags=re.S)
used = collections.Counter()
for m in re.finditer(r'\bclass\s*=\s*"([^"]*)"', html):
    for c in m.group(1).split():
        if '${' not in c: used[c] += 1
ids_html = collections.Counter(re.findall(r'\bid\s*=\s*"([^"$]+)"', html))
# JS : class="…" dans les chaînes, classList.add/toggle/contains, className =
scripts = '\n'.join(re.findall(r'<script\b[^>]*>(.*?)</script>', src, re.S))
js_used = collections.Counter()
for m in re.finditer(r'class\s*=\s*\\?["\']([^"\'$]*)', scripts):
    for c in m.group(1).split():
        if re.fullmatch(r'[A-Za-z_][\w-]*', c): js_used[c] += 1
for m in re.finditer(r'classList\.(?:add|toggle|remove|contains|replace)\(([^)]*)\)', scripts):
    for c in re.findall(r'["\']([A-Za-z_][\w-]*)["\']', m.group(1)): js_used[c] += 1
for m in re.finditer(r'className\s*[+]?=\s*[`"\']([^`"\']*)', scripts):
    for c in m.group(1).split():
        if re.fullmatch(r'[A-Za-z_][\w-]*', c): js_used[c] += 1
for m in re.finditer(r'querySelector(?:All)?\(\s*[`"\']([^`"\']*)', scripts):
    for c in re.findall(r'\.([A-Za-z_][\w-]*)', m.group(1)): js_used[c] += 1
tous = used + js_used
non_styles = sorted(c for c in tous if c not in css_classes)
morts = sorted(c for c in css_classes if c not in tous)
res = {
  'nb_classes_utilisees': len(tous), 'nb_classes_css': len(css_classes),
  'utilisees_sans_regle': non_styles, 'css_sans_usage_detecte': morts,
  'compte_html': dict(used.most_common()), 'compte_js': dict(js_used.most_common()),
  'ids_css': sorted(css_ids), 'ids_css_absents_html': sorted(i for i in css_ids if i not in ids_html and i not in scripts),
}
if len(sys.argv) > 2: json.dump(res, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
print('classes utilisées :', len(tous), '| classes du CSS :', len(css_classes))
print('utilisées sans règle CSS :', len(non_styles))
print('CSS sans usage détecté :', len(morts))
