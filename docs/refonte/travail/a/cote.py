#!/usr/bin/env python3
"""Côte à côte : même zone de la cible (maquette) et du rendu réel, agrandie.
Usage : python3 -I cote.py cible.png reel.png x y l h sortie.png [echelle]"""
import sys
from PIL import Image
cible, reel, x, y, l, h, out = sys.argv[1:8]
k = float(sys.argv[8]) if len(sys.argv) > 8 else 2
x, y, l, h = map(int, (x, y, l, h))
a, b = Image.open(cible), Image.open(reel)
# les captures téléphone sont en ×2 : coordonnées données en px CSS
fa, fb = a.width / (390 if a.width < 1000 else a.width), b.width / (390 if b.width < 1000 else b.width)
def zone(im, f):
    return im.crop((int(x * f), int(y * f), int((x + l) * f), int((y + h) * f))).resize((int(l * k), int(h * k)))
za, zb = zone(a, fa), zone(b, fb)
o = Image.new('RGB', (za.width * 2 + 10, za.height), 'white')
o.paste(za, (0, 0)); o.paste(zb, (za.width + 10, 0))
o.save(out)
