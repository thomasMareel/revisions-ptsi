# Palette FINALE (source des valeurs de tokens.css). python3 -I palette.py
# Chaque teinte : (L, C, H) OKLCH de l'encre claire ; on en dérive la teinte de fond,
# le « vif » (traits, pastilles, barres) et les trois équivalents sombres.
import sys, itertools, json
sys.path.insert(0, '.')
from couleur import *
L_NEU = dict(desk='#f3f1ec', sheet='#fffdf9', sunk='#f6f3ed', raise_='#ffffff')
D_NEU = dict(desk='#111316', sheet='#191b20', sunk='#20232a', raise_='#24272e')
INK = {  # encre claire (texte) : L, C, H
    'physique': (0.500, 0.140, 266), 'maths': (0.480, 0.150, 350), 'si': (0.515, 0.095, 177),
    'info': (0.468, 0.094, 229), 'anglais': (0.475, 0.145, 304),
    'rouge': (0.510, 0.150, 27), 'ambre': (0.520, 0.108, 74), 'vert': (0.475, 0.133, 139),
}
def hx(L, C, H):
    lo, hi = 0, C
    h, ok = lch2hex(L, C, H)
    if ok: return h
    for _ in range(30):            # réduit la chroma jusqu'à entrer dans le gamut sRGB
        m = (lo + hi) / 2
        if lch2hex(L, m, H)[1]: lo = m
        else: hi = m
    return lch2hex(L, lo, H)[0]
# En sombre, deux teintes tournent un peu (info vers le cyan, SI vers le vert d'eau)
# pour garder des écarts OKLab >= 8 entre encres claires sur fond nuit.
H_SOMBRE = {'info': 221, 'si': 175}
def derive(k, L, C, H):
    Hs = H_SOMBRE.get(k, H)
    return {
        'clair': {'encre': hx(L, C, H), 'fond': hx(0.962, C * 0.17, H), 'vif': hx(0.60, C * 1.12, H)},
        'sombre': {'encre': hx(0.77, C * 1.10, Hs), 'fond': hx(0.285, C * 0.26, Hs), 'vif': hx(0.68, C * 1.0, Hs)},
    }
PAL = {k: derive(k, *v) for k, v in INK.items()}
if __name__ == '__main__':
    for k, d in PAL.items():
        c, s = d['clair'], d['sombre']
        print(f"{k:9s} clair {c['encre']} fond {c['fond']} vif {c['vif']} | "
              f"encre/feuille {cr(c['encre'], L_NEU['sheet']):.2f} /bureau {cr(c['encre'], L_NEU['desk']):.2f} /fond {cr(c['encre'], c['fond']):.2f} vif/feuille {cr(c['vif'], L_NEU['sheet']):.2f} vif/fond {cr(c['vif'], c['fond']):.2f} texte/fond {cr('#1c1d21', c['fond']):.2f}")
        print(f"{'':9s} sombre {s['encre']} fond {s['fond']} vif {s['vif']} | "
              f"encre/feuille {cr(s['encre'], D_NEU['sheet']):.2f} /bureau {cr(s['encre'], D_NEU['desk']):.2f} /fond {cr(s['encre'], s['fond']):.2f} /menu {cr(s['encre'], D_NEU['raise_']):.2f} vif/feuille {cr(s['vif'], D_NEU['sheet']):.2f} vif/fond {cr(s['vif'], s['fond']):.2f} texte/fond {cr('#e8e6e1', s['fond']):.2f}")
    for th in ('clair', 'sombre'):
        c = {k: PAL[k][th]['encre'] for k in PAL}
        print(th, 'distances OKLab les plus courtes :', ', '.join(f"{a}/{b} {dist(c[a], c[b]):.1f}" for a, b in sorted(itertools.combinations(c, 2), key=lambda ab: dist(c[ab[0]], c[ab[1]]))[:8]))
    json.dump(PAL, open('palette.json', 'w'), indent=1)
