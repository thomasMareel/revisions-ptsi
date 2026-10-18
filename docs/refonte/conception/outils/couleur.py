# Outils couleur : sRGB <-> OKLab/OKLCH, contraste WCAG 2.x, distance OKLab (x100).
import math
def hex2rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
def rgb2hex(c):
    return '#' + ''.join('%02x' % max(0, min(255, round(v * 255))) for v in c)
def lin(v): return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
def delin(v): return 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055
def lum(h):
    r, g, b = (lin(v) for v in hex2rgb(h)); return 0.2126 * r + 0.7152 * g + 0.0722 * b
def cr(a, b):
    x, y = lum(a), lum(b); return (max(x, y) + 0.05) / (min(x, y) + 0.05)
def oklab(h):
    r, g, b = (lin(v) for v in hex2rgb(h))
    l = 0.4122214708*r + 0.5363325363*g + 0.0514459929*b
    m = 0.2119034982*r + 0.6806995451*g + 0.1073969566*b
    s = 0.0883024619*r + 0.2817188376*g + 0.6299787005*b
    l, m, s = (math.copysign(abs(v) ** (1/3), v) for v in (l, m, s))
    return (0.2104542553*l + 0.7936177850*m - 0.0040720468*s,
            1.9779984951*l - 2.4285922050*m + 0.4505937099*s,
            0.0259040371*l + 0.7827717662*m - 0.8086757660*s)
def lab2hex(L, a, b):
    l = L + 0.3963377774*a + 0.2158037573*b
    m = L - 0.1055613458*a - 0.0638541728*b
    s = L - 0.0894841775*a - 1.2914855480*b
    l, m, s = l**3, m**3, s**3
    r = 4.0767416621*l - 3.3077115913*m + 0.2309699292*s
    g = -1.2684380046*l + 2.6097574011*m - 0.3413193965*s
    bb = -0.0041960863*l - 0.7034186147*m + 1.7076147010*s
    out = (r, g, bb)
    ok = all(-0.0005 <= v <= 1.0005 for v in out)
    return rgb2hex([delin(min(1, max(0, v))) for v in out]), ok
def oklch(h):
    L, a, b = oklab(h); return L, math.hypot(a, b), (math.degrees(math.atan2(b, a)) % 360)
def lch2hex(L, C, H):
    return lab2hex(L, C * math.cos(math.radians(H)), C * math.sin(math.radians(H)))
def dist(a, b):
    x, y = oklab(a), oklab(b); return 100 * math.dist(x, y)
