# Recherche de la palette claire : 5 matières + 3 sémantiques, distances OKLab maximales
# sous contraintes de contraste (texte >= 4,6:1 sur bureau #f3f1ec et >= 4,5:1 sur sa teinte).
import sys, random, itertools, math
sys.path.insert(0, '.')
from couleur import *
DESK, SHEET = '#f3f1ec', '#fffdf9'
WIN = {'physique': (255, 270), 'maths': (345, 362), 'anglais': (298, 312), 'info': (214, 236),
       'si': (170, 192), 'rouge': (20, 32), 'ambre': (66, 80), 'vert': (128, 150)}
def maxC(L, H):
    lo, hi = 0, 0.3
    for _ in range(30):
        m = (lo + hi) / 2
        if lch2hex(L, m, H)[1]: lo = m
        else: hi = m
    return lo
def make(p):
    out = {}
    for k, (L, cf, H) in p.items():
        C = maxC(L, H) * cf
        out[k] = lch2hex(L, C, H % 360)[0]
    return out
def score(cols):
    for k, v in cols.items():
        if cr(v, DESK) < 4.6: return -1
    ks = list(cols)
    return min(dist(cols[a], cols[b]) for a, b in itertools.combinations(ks, 2))
random.seed(1)
best = None
for it in range(60000):
    p = {k: (random.uniform(0.44, 0.52), random.uniform(0.85, 1.0), random.uniform(*w)) for k, w in WIN.items()}
    if best and random.random() < 0.7:
        p = {k: (min(0.52, max(0.44, v[0] + random.gauss(0, 0.01))), min(1, max(0.8, v[1] + random.gauss(0, 0.03))),
                 min(WIN[k][1], max(WIN[k][0], v[2] + random.gauss(0, 2)))) for k, v in best[1].items()}
    c = make(p); s = score(c)
    if best is None or s > best[0]: best = (s, p, c)
print('min dist %.2f' % best[0])
for k, v in best[2].items():
    print(k, v, ['%.3f' % x for x in oklch(v)], 'desk %.2f sheet %.2f' % (cr(v, DESK), cr(v, SHEET)))
ks = list(best[2])
for a, b in sorted(itertools.combinations(ks, 2), key=lambda ab: dist(best[2][ab[0]], best[2][ab[1]]))[:10]:
    print(a, b, '%.1f' % dist(best[2][a], best[2][b]))
