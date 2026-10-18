# Construit les deux petits fichiers « symboles » (indices, exposants, flèches,
# opérateurs) que les sous-ensembles npm @fontsource-variable n'incluent pas.
# Source : paquets npm OFFICIELS d'Adobe (licence OFL) — reproductible :
#   npm pack source-serif@4.5.1 source-sans@3.52.0 && tar -xzf …
#   python3 -I construire-symboles.py <dossier source-serif/package> <dossier source-sans/package> <sortie>
# Le texte du site contient ≈ 1 300 indices/exposants Unicode (H₂O, SO₄²⁻, Fe³⁺, ω₀),
# 1 600 flèches → et ≈ 400 ≈ ≤ ≥ ≠ hors formules : sans ces fichiers ils tombent sur
# une police système (dessin, graisse et hauteur différents).
import sys, os
from fontTools import subset
from fontTools.ttLib import TTFont
serif_pkg, sans_pkg, out = sys.argv[1:4]
WANT = list(range(0x2070, 0x20A0)) + list(range(0x2190, 0x2200)) + list(range(0x2200, 0x2300)) \
     + [0x2016, 0x2713, 0x25CF, 0x25CB] \
     + [0x02B3, 0x02E2, 0x1D48, 0x1D49, 0x1D52]   # ʳ ˢ ᵈ ᵉ ᵒ (1ʳᵉ, 2ᵉ, 1ᵉʳ…) : retirés des plages latin-ext
# (sans cela, chaque « 1ʳᵉ année » de l'interface ferait télécharger 60–100 Ko de latin-ext).
# déjà dans le sous-ensemble « latin » de fontsource (U+2000-206F, 2191, 2193, 2212, 2215) :
# on ne les reprend pas, pour que ce fichier ne soit téléchargé que si un VRAI symbole apparaît.
DEJA = set(range(0x2000, 0x2070)) | {0x2191, 0x2193, 0x2212, 0x2215}
WANT = [u for u in WANT if u not in DEJA]
def build(src, dst):
    f = TTFont(src); cmap = f.getBestCmap()
    have = sorted(u for u in WANT if u in cmap)
    opts = subset.Options(); opts.flavor = 'woff2'; opts.layout_features = ['*']; opts.notdef_outline = False
    opts.name_IDs = ['*']; opts.name_languages = ['*']; opts.drop_tables += ['DSIG']
    s = subset.Subsetter(options=opts); s.populate(unicodes=have); s.subset(f)
    f.flavor = 'woff2'; f.save(dst)
    # plages compactes pour unicode-range
    rng, a = [], None
    for i, u in enumerate(have):
        if a is None: a = b = u
        elif u == b + 1: b = u
        else: rng.append((a, b)); a = b = u
    rng.append((a, b))
    txt = ','.join(f'U+{x:04X}' if x == y else f'U+{x:04X}-{y:04X}' for x, y in rng)
    print(os.path.basename(dst), os.path.getsize(dst), 'octets,', len(have), 'caractères :', ''.join(chr(u) for u in have))
    print('   unicode-range:', txt)
    return txt
r1 = build(os.path.join(serif_pkg, 'WOFF2/VAR/SourceSerif4Variable-Roman.ttf.woff2'), os.path.join(out, 'source-serif-4-symboles-opsz-normal.woff2'))
r2 = build(os.path.join(sans_pkg, 'WOFF2/VF/SourceSans3VF-Upright.ttf.woff2'), os.path.join(out, 'source-sans-3-symboles-wght-normal.woff2'))
open(os.path.join(out, 'symboles-plages.txt'), 'w').write('serif ' + r1 + '\nsans ' + r2 + '\n')
