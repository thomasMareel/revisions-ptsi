# Planches de synthèse (captures réduites côte à côte).  python3 -I planche.py
import os
from PIL import Image, ImageDraw
C = os.path.join(os.path.dirname(__file__), '..', 'captures')
def planche(noms, sortie, h_cible, cols, fond=(214, 210, 202)):
    ims = [Image.open(os.path.join(C, n + '.png')).convert('RGB') for n in noms]
    ims = [im.resize((round(im.width * h_cible / im.height), h_cible)) for im in ims]
    w = max(im.width for im in ims); g = 24
    rows = [ims[i:i + cols] for i in range(0, len(ims), cols)]
    W = cols * w + (cols + 1) * g; H = len(rows) * h_cible + (len(rows) + 1) * g
    out = Image.new('RGB', (W, H), fond)
    for r, row in enumerate(rows):
        for c, im in enumerate(row):
            out.paste(im, (g + c * (w + g), g + r * (h_cible + g)))
    out.save(os.path.join(C, sortie)); print(sortie, out.size)
planche(['01-chapitre-ordinateur', '03a-navigation-ordinateur', '06a-chapitre-sombre-ordinateur', '07a-theme-ordinateur', '08a-exercices-ordinateur', '08b-simulateur-ordinateur'], 'planche-ordinateur.png', 600, 2)
planche(['02-chapitre-telephone', '02b-chapitre-telephone-defile', '03b-navigation-telephone', '03c-navigation-telephone-filtre', '04a-carte-recto-telephone', '04b-carte-verso-telephone'], 'planche-telephone-a.png', 1000, 6)
planche(['05-aujourdhui-telephone', '06b-chapitre-sombre-telephone', '07b-theme-telephone-systeme-clair', '07b-theme-telephone-systeme-sombre', '08c-simulateur-telephone'], 'planche-telephone-b.png', 1000, 5)
