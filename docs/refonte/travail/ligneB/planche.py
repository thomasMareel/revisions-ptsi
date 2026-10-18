#!/usr/bin/env python3
"""Planches de captures : python3 planche.py <dossier> <colonnes> <par_planche> <largeur_vignette> [hauteur_max]"""
import sys, os
from PIL import Image, ImageDraw
d, cols, per, lw = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
hmax = int(sys.argv[5]) if len(sys.argv) > 5 else 10**6
fs = sorted(f for f in os.listdir(d) if f.endswith('.png') and not f.startswith('planche'))
for k in range(0, len(fs), per):
    lot = fs[k:k + per]
    ims = []
    for f in lot:
        im = Image.open(os.path.join(d, f)).convert('RGB')
        r = lw / im.width
        im = im.resize((lw, int(im.height * r)))
        if im.height > hmax: im = im.crop((0, 0, lw, hmax))
        ims.append((f, im))
    rows = (len(ims) + cols - 1) // cols
    hs = [max(im.height for _, im in ims[i * cols:(i + 1) * cols]) + 18 for i in range(rows)]
    out = Image.new('RGB', (cols * lw + (cols - 1) * 6, sum(hs)), 'white')
    dr = ImageDraw.Draw(out)
    y = 0
    for i in range(rows):
        for j, (f, im) in enumerate(ims[i * cols:(i + 1) * cols]):
            x = j * (lw + 6)
            dr.text((x + 2, y + 2), f, fill=(200, 0, 0))
            out.paste(im, (x, y + 16))
        y += hs[i]
    out.save(os.path.join(d, 'planche%02d.png' % (k // per)))
print('ok', len(fs))
