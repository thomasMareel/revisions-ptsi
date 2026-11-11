"""Contrôle AVANT le rendu : chaque self.t("id") et self.a("id", "fragment") de scenes.py doit viser
une phrase de segments.py, et le fragment doit figurer tel quel dans sa forme prononcée (« dit »).
À lancer DEPUIS le dossier du chapitre :  python3 ../../commun/ancres.py"""
import re, sys, os
sys.path.insert(0, os.getcwd())
from segments import SCENES
dit = {p[0]: (p[2] or p[1]) for s in SCENES for p in s[2]}
src = open("scenes.py", encoding="utf-8").read()
ko = 0
for m in re.finditer(r'self\.t\(\s*"([^"]+)"', src):
    if m.group(1) not in dit: print("phrase inconnue :", m.group(1)); ko += 1
n = 0
for m in re.finditer(r'self\.a\(\s*"([^"]+)"\s*,\s*r?"((?:[^"\\]|\\.)*)"', src):
    n += 1; i, frag = m.group(1), m.group(2)
    if i not in dit: print("phrase inconnue :", i); ko += 1
    elif frag not in dit[i]: print(f"fragment absent de {i} : « {frag} »\n      dit : {dit[i]}"); ko += 1
ids = [p[0] for s in SCENES for p in s[2]]
if len(ids) != len(set(ids)): print("identifiants de phrase en double :", sorted({i for i in ids if ids.count(i) > 1})); ko += 1
dyn = len(re.findall(r"self\.a\(", src)) - n
print(f"{n} ancres vérifiées, {ko} erreur(s)" + (f" ; {dyn} ancre(s) à fragment calculé, non vérifiée(s)" if dyn else ""))
sys.exit(1 if ko else 0)
