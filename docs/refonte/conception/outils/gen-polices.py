# Génère ../polices/polices.css (plages unicode-range des fichiers npm @fontsource-variable,
# + fichiers « symboles » construits par construire-symboles.py).   python3 -I gen-polices.py
import os
D = os.path.join(os.path.dirname(__file__), '..', 'polices')
pl = dict(l.split(' ', 1) for l in open(os.path.join(D, 'symboles-plages.txt')).read().strip().split('\n'))
LAT = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
# latin-ext de fontsource MOINS ʳ (02B3), ˢ (02E2), ᵈ (1D48), ᵉ (1D49), ᵒ (1D52), servis par « symboles »
EXT = "U+0100-02B2,U+02B4-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02E1,U+02E3-02FF,U+0304,U+0308,U+0329,U+1D00-1D47,U+1D4A-1D51,U+1D53-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C4,U+2113,U+2C60-2C7F,U+A720-A7FF"
GRK = "U+0370-0377,U+037A-037F,U+0384-038A,U+038C,U+038E-03A1,U+03A3-03FF"
def ff(fam, style, w, f, rng, fmt='woff2'):
    return "@font-face{font-family:'%s';font-style:%s;font-weight:%s;font-display:swap;src:url(%s) format('%s');unicode-range:%s}" % (fam, style, w, f, fmt, rng)
H = open(os.path.join(os.path.dirname(__file__), 'polices-entete.txt'), encoding='utf-8').read()
L = [H, '/* --- Source Serif 4, romain (taille optique automatique) --- */']
for s, r in (('latin', LAT), ('latin-ext', EXT), ('greek', GRK)):
    L.append(ff('Source Serif 4', 'normal', '200 900', 'source-serif-4-%s-opsz-normal.woff2' % s, r))
L.append(ff('Source Serif 4', 'normal', '200 900', 'source-serif-4-symboles-opsz-normal.woff2', pl['serif']))
L.append("/* --- Source Serif 4, italique (emphase, « § » de marge, noms de formules) ---\n   Symboles et lettres en exposant droits en italique (comme en mathématiques) : même fichier. */")
for s, r in (('latin', LAT), ('latin-ext', EXT), ('greek', GRK)):
    L.append(ff('Source Serif 4', 'italic', '200 900', 'source-serif-4-%s-wght-italic.woff2' % s, r))
L.append(ff('Source Serif 4', 'italic', '200 900', 'source-serif-4-symboles-opsz-normal.woff2', pl['serif']))
L.append("/* --- Source Sans 3 (interface ; pas d'italique dans l'interface) --- */")
for s, r in (('latin', LAT), ('latin-ext', EXT), ('greek', GRK)):
    L.append(ff('Source Sans 3', 'normal', '200 900', 'source-sans-3-%s-wght-normal.woff2' % s, r))
L.append(ff('Source Sans 3', 'normal', '200 900', 'source-sans-3-symboles-wght-normal.woff2', pl['sans']))
L.append("/* --- JetBrains Mono (code, <kbd>, canvas ; ligatures coupées par composants.css) --- */")
for s, r in (('latin', LAT), ('latin-ext', EXT), ('greek', GRK)):
    L.append(ff('JetBrains Mono', 'normal', '100 800', 'jetbrains-mono-%s-wght-normal.woff2' % s, r))
L.append("/* --- Symboles TeX : fontes MathJax (woff, déjà en cache dès qu'une formule est rendue) --- */")
for st in ('normal', 'italic'):
    L.append(ff('Symboles TeX', st, '400 700', '../mathjax/output/chtml/fonts/woff-v2/MathJax_Main-Regular.woff', 'U+2190-21B9,U+21BB-21FF,U+2200-22FF,U+27E8-27E9,U+27F5-27FF', 'woff'))
    L.append(ff('Symboles TeX', st, '400 700', '../mathjax/output/chtml/fonts/woff-v2/MathJax_AMS-Regular.woff', 'U+21BA,U+2605', 'woff'))
open(os.path.join(D, 'polices.css'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('écrit polices.css')
