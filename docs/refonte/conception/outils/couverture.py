# Couverture des caractères du site par les polices retenues (cmap ∩ unicode-range).
# python3 -I couverture.py /home/user/revisions-ptsi/index.html
import sys, re, glob, collections, os
from fontTools.ttLib import TTFont
html = open(sys.argv[1], encoding='utf-8').read()
# texte hors <script>/<style> et hors formules TeX \( \) $$ $$ (rendues par MathJax)
body = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', ' ', html, flags=re.S)
body = re.sub(r'\$\$.*?\$\$|\\\(.*?\\\)', ' ', body, flags=re.S)
body = re.sub(r'<[^>]+>', ' ', body)
# + le texte des cartes (dans le JS : chaînes q:/a:), hors \( \)
cards = ' '.join(re.findall(r'\b[qa]\s*:\s*"((?:[^"\\]|\\.)*)"', html))
cards = re.sub(r'\\\\\(.*?\\\\\)', ' ', cards)
cnt = collections.Counter(c for c in body + cards if ord(c) > 127)
POL = os.path.join(os.path.dirname(__file__), '..', 'polices')
def faces(css):
    out = []
    for m in re.finditer(r"@font-face\{([^}]*)\}", css):
        d = m.group(1)
        fam = re.search(r"font-family:'([^']+)'", d).group(1)
        style = re.search(r"font-style:(\w+)", d).group(1)
        src = re.search(r"url\(([^)]+)\)", d).group(1)
        ur = re.search(r"unicode-range:([^;}]+)", d)
        rng = []
        if ur:
            for part in ur.group(1).split(','):
                part = part.strip()[2:]
                a, _, b = part.partition('-'); rng.append((int(a, 16), int(b or a, 16)))
        out.append((fam, style, src, rng))
    return out
css = open(os.path.join(POL, 'polices.css'), encoding='utf-8').read()
FACES = faces(css)
cmaps = {}
def covered(fam, style, ch):
    o = ord(ch)
    for f, s, src, rng in FACES:
        if f != fam or s != style: continue
        if rng and not any(a <= o <= b for a, b in rng): continue
        p = os.path.normpath(os.path.join(POL, src))
        if p not in cmaps: cmaps[p] = TTFont(p).getBestCmap() or {}
        if o in cmaps[p]: return True
    return False
for fam in ['Source Serif 4', 'Source Sans 3']:
    miss = [(c, n) for c, n in cnt.most_common() if not covered(fam, 'normal', c) and not covered('Symboles TeX', 'normal', c) and not covered('Source Sans 3', 'normal', c)]
    tot = sum(n for _, n in miss)
    print(f"{fam} (+ Symboles TeX) : {len(miss)} caractères non couverts, {tot} occurrences")
    print('   ', ' '.join(f"{c}U+{ord(c):04X}×{n}" for c, n in miss[:60]))
print('caractères non ASCII distincts :', len(cnt), ' occurrences :', sum(cnt.values()))
