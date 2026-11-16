from base import *
FOND = "#1F2A24"
# ---------------------------------------------------------------- outils communs
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)
def chrono(x, y):
    pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([x, y, 0])
    arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
    return pa, arc
def lim(m, w):
    if m.width > w: m.scale_to_fit_width(w)
    return m
def P(x, y): return np.array([x, y, 0.0])

# ---------------------------------------------------------------- dessin des poutres
def poutre(x0, x1, y, col=CRAIE, sw=9): return Line(P(x0, y), P(x1, y), color=col, stroke_width=sw)
def hach(x0, x1, y, col=GRIS, pas=0.13, h=0.12):
    g = VGroup(Line(P(x0, y), P(x1, y), color=col, stroke_width=2.5))
    for k in range(int((x1 - x0)/pas)):
        xa = x0 + (k + 1)*pas; g.add(Line(P(xa, y), P(xa - h, y - h), color=col, stroke_width=1.5))
    return g
def pivot(x, y, s=0.24, col=CRAIE):          # articulation : triangle, petit cercle au sommet
    top = y - 0.07; yb = top - 1.6*s
    tri = Polygon(P(x, top), P(x - s, yb), P(x + s, yb), color=col, stroke_width=3)
    c = Circle(radius=0.06, color=col, stroke_width=3).set_fill(FOND, 1).move_to(P(x, top))
    return VGroup(tri, hach(x - 1.5*s, x + 1.5*s, yb), c)
def appui(x, y, s=0.24, col=CRAIE):          # appui simple : triangle sur deux rouleaux
    top = y - 0.07; yb = top - 1.6*s; r = 0.07
    tri = Polygon(P(x, top), P(x - s, yb), P(x + s, yb), color=col, stroke_width=3)
    rou = VGroup(*[Circle(radius=r, color=col, stroke_width=2.5).move_to(P(x + d, yb - r)) for d in (-0.55*s, 0.55*s)])
    return VGroup(tri, rou, hach(x - 1.5*s, x + 1.5*s, yb - 2*r))
def encas(x, y, h=1.0, w=0.3, col=GRIS):    # encastrement : rectangle hachuré, à gauche de x
    r = Rectangle(width=w, height=h, color=col, stroke_width=2.5).move_to(P(x - w/2, y))
    g = VGroup(r)
    yy = y - h/2 + 0.04
    while yy + w <= y + h/2 - 0.02:
        g.add(Line(P(x - w, yy), P(x, yy + w), color=col, stroke_width=1.5)); yy += 0.14
    return g
def force(x, y0, y1, col=ROUGE, sw=5, tl=0.2):
    return Arrow(P(x, y0), P(x, y1), buff=0, color=col, stroke_width=sw, max_tip_length_to_length_ratio=0.35, tip_length=tl)
def repartie(x0, x1, y, h=0.55, col=ROUGE, pas=0.3):
    n = max(3, int(round((x1 - x0)/pas)) + 1)
    g = VGroup(Line(P(x0, y + h), P(x1, y + h), color=col, stroke_width=3))
    for xx in np.linspace(x0, x1, n):
        g.add(Arrow(P(xx, y + h), P(xx, y + 0.07), buff=0, color=col, stroke_width=3, max_tip_length_to_length_ratio=0.4, tip_length=0.13))
    return g
def repere(x, y, l=0.55, col=GRIS):
    ax = Arrow(P(x, y), P(x + l, y), buff=0, color=col, stroke_width=3, tip_length=0.14, max_tip_length_to_length_ratio=0.35)
    ay = Arrow(P(x, y), P(x, y + l), buff=0, color=col, stroke_width=3, tip_length=0.14, max_tip_length_to_length_ratio=0.35)
    lx = M(r"\vec x", sc=0.6, color=col).next_to(ax.get_end(), RIGHT, buff=0.06)
    ly = M(r"\vec y", sc=0.6, color=col).next_to(ay.get_end(), UP, buff=0.04)
    return VGroup(ax, ay, lx, ly)
def cote(x0, x1, y, txt, col=GRIS, haut=False, sc=0.56):
    a = DoubleArrow(P(x0, y), P(x1, y), buff=0, color=col, stroke_width=2, tip_length=0.12, max_tip_length_to_length_ratio=0.25)
    tk = VGroup(Line(P(x0, y - 0.1), P(x0, y + 0.1), color=col, stroke_width=2), Line(P(x1, y - 0.1), P(x1, y + 0.1), color=col, stroke_width=2))
    t = M(txt, sc=sc, color=col).next_to(a, UP if haut else DOWN, buff=0.07)
    return VGroup(a, tk, t)
def lettre(s, x, y, col=CRAIE, sc=0.62): return M(s, sc=sc, color=col).move_to(P(x, y))

# ---------------------------------------------------------------- diagrammes dans un cadre (même échelle en x que la poutre)
class Diag:
    def __init__(self, X0, X1, L, yc, h, v0, v1, nom, unite, marge=0.3, xn=None):
        self.X0, self.X1, self.L, self.v0, self.v1 = X0, X1, L, v0, v1
        self.ya, self.yz = yc - h/2 + 0.1, yc + h/2 - 0.1
        self.fr = Rectangle(width=X1 - X0 + 2*marge, height=h, color=GRIS, stroke_width=2).move_to(P((X0 + X1)/2, yc))
        self.zero = DashedLine(P(X0 - marge, self.p(0, 0)[1]), P(X1 + marge, self.p(0, 0)[1]), color=GRIS, stroke_width=1.5, dash_length=0.08)
        xn = X0 - marge - 0.5 if xn is None else xn
        self.nom = VGroup(M(nom, sc=0.62, color=GRIS), T(unite, sc=0.48, color=GRIS)).arrange(DOWN, buff=0.06).move_to(P(xn, yc))
    def p(self, x, v): return P(self.X0 + x*(self.X1 - self.X0)/self.L, self.ya + (v - self.v0)/(self.v1 - self.v0)*(self.yz - self.ya))
    def trace(self, pts, col, sw=5): return VMobject(color=col, stroke_width=sw).set_points_as_corners([self.p(a, b) for a, b in pts])
    def courbe(self, f, a, b, col, sw=5, n=60): return self.trace([(t, f(t)) for t in np.linspace(a, b, n)], col, sw)
    def aire(self, pts, col, op=0.18):
        q = [self.p(pts[0][0], 0)] + [self.p(a, b) for a, b in pts] + [self.p(pts[-1][0], 0)]
        return Polygon(*q, stroke_width=0, fill_color=col, fill_opacity=op)
    def tirets(self, pts, col, sw=3.5): return DashedVMobject(self.trace(pts, col, sw), num_dashes=40)
    def cadre(self): return VGroup(self.fr, self.zero, self.nom)

class Cours2(Cours):
    def minuteur(self, x, y, ph, frag):
        pa, arc = chrono(x, y)
        self.at(self.a(ph, frag), FadeIn(pa), Create(arc), run_time=0.5)
        self.play(Uncreate(arc), run_time=max(1.0, self.PH[ph]["fin"] + 4.2 - self.renderer.time))
        self.play(FadeOut(pa), run_time=0.2)
    def etape(self, k, col, x, y, m, t, rt=1.0, w=None):
        ca = carte(k, col, x, y); mm = pos(m, x + 0.5, y)
        if w: lim(mm, w); pos(mm, x + 0.5, y)
        self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
        return VGroup(ca, mm)

# ================================================================ S0 : introduction
class S0(Cours2):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PT", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Résistance des matériaux -- Chapitre 1}", sc=1.1, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Torseur de cohésion et diagrammes des efforts", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-5.2, 1.3, 0], [5.2, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        X0, X1, y = 2.2, 5.8, 0.35
        po = poutre(X0, X1, y); s1 = pivot(X0, y); s2 = appui(X1, y); ch_ = repartie(X0, X1, y, h=0.45)
        d = Diag(X0, X1, 1.0, -1.45, 1.5, -0.01, 0.13, r"M_{fz}", "", marge=0.3)
        c = d.courbe(lambda u: u*(1 - u)/2, 0, 1, VERT); ai = d.aire([(u, u*(1 - u)/2) for u in np.linspace(0, 1, 40)], VERT)
        nm = M(r"M_{fz}", sc=0.6, color=VERT).next_to(d.fr, LEFT, buff=0.15)
        self.at(self.a("a2", "L'outil"), Create(po), FadeIn(s1), FadeIn(s2), run_time=0.8)
        self.play(FadeIn(ch_, shift=0.15*DOWN), run_time=0.5)
        self.at(self.a("a2", "son portrait"), Create(d.fr), Create(d.zero), FadeIn(nm), Create(c), FadeIn(ai), run_time=1.2)
        items = []
        for k, (txt, col) in enumerate([("Le modèle poutre", BLEU), ("Coupure et torseur de cohésion", VERT), ("Composantes et sollicitations", ORANGE),
                                         ("Équations locales et diagrammes", ROUGE), ("Trois exercices résolus", JAUNE)]):
            yy = 0.75 - 0.6*k
            items.append(VGroup(carte(k+1, col, -6.2, yy), pos(T(txt, sc=0.74), -5.65, yy)))
        for it, (sid, fr_) in zip(items, [("a3", "le modèle poutre"), ("a3", "la coupure"), ("a3", "les sollicitations"),
                                          ("a3", "les équations locales"), ("a4", "trois exercices")]):
            self.jusqua(self.a(sid, fr_)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

# ================================================================ S1 : le modèle poutre
class S1(Cours2):
    sid = "S1"
    def construct(self):
        self.entete(r"1.1 -- Le modèle poutre", "Modèle")
        xa, xb, yc, hb = -5.6, 3.6, 1.7, 0.7
        bord = VGroup(Line(P(xa, yc + hb/2), P(xb, yc + hb/2), color=CRAIE, stroke_width=3), Line(P(xa, yc - hb/2), P(xb, yc - hb/2), color=CRAIE, stroke_width=3),
                      Ellipse(width=0.3, height=hb, color=CRAIE, stroke_width=3).move_to(P(xa, yc)), Ellipse(width=0.3, height=hb, color=CRAIE, stroke_width=3).move_to(P(xb, yc)))
        lm = DashedLine(P(xa, yc), P(xb + 0.35, yc), color=JAUNE, stroke_width=3, dash_length=0.12)
        llm = pos(T("ligne moyenne", sc=0.6, color=JAUNE), xb + 0.5, yc)
        xg = 0.4
        sec = Ellipse(width=0.32, height=hb, color=BLEU, stroke_width=4).set_fill(BLEU, 0.25).move_to(P(xg, yc))
        g = Dot(P(xg, yc), radius=0.06, color=BLEU); lg = lettre("G", xg + 0.28, yc - 0.2, col=BLEU, sc=0.58)
        ls = T(r"section droite $\Sigma$", sc=0.6, color=BLEU).move_to(P(xg, yc - hb/2 - 0.32))
        self.at(self.t("b1"), Create(bord), run_time=0.8)
        self.at(self.a("b1", "une section droite"), FadeIn(sec), FadeIn(ls), run_time=0.6)
        self.at(self.a("b1", "dont le centre G"), FadeIn(g, scale=2), FadeIn(lg), run_time=0.5)
        self.at(self.a("b1", "la ligne moyenne"), Create(lm), FadeIn(llm), run_time=0.8)
        el = T(r"poutre \textbf{élancée} : longueur $\geq 5$ à $10\times$ la plus grande dimension transversale", sc=0.66).move_to(P(-0.6, 0.55))
        self.ecr(self.a("b2", "la poutre est élancée"), el, rt=1.3)
        o = Dot(P(xa, yc), radius=0.06, color=CRAIE); lo = lettre("O", xa - 0.3, yc, sc=0.58)
        cx = cote(xa, xg, yc + hb/2 + 0.3, "x", col=CRAIE, haut=True)
        vx = Arrow(P(xg, yc), P(xg + 0.85, yc), buff=0, color=BLEU, stroke_width=4, tip_length=0.15, max_tip_length_to_length_ratio=0.3)
        vy = Arrow(P(xg, yc), P(xg, yc + 0.95), buff=0, color=BLEU, stroke_width=4, tip_length=0.15, max_tip_length_to_length_ratio=0.3)
        lvx = M(r"\vec x", sc=0.6, color=BLEU).next_to(vx.get_end(), DOWN, buff=0.12).shift(0.1*RIGHT)
        lvy = M(r"\vec y", sc=0.6, color=BLEU).next_to(vy.get_end(), RIGHT, buff=0.08)
        self.at(self.a("b3", "son abscisse x"), FadeIn(o), FadeIn(lo), FadeIn(cx), run_time=0.6)
        self.at(self.a("b3", "L'axe x"), GrowArrow(vx), FadeIn(lvx), run_time=0.5)
        self.at(self.a("b3", "l'axe i grec"), GrowArrow(vy), FadeIn(lvy), run_time=0.5)
        h = [(r"$\bullet$ matériau homogène, isotrope, élastique linéaire", "b4", "Les hypothèses"),
             (r"$\bullet$ petites perturbations : les effets des charges s'additionnent", "b4", "et petites perturbations"),
             (r"$\bullet$ Navier-Bernoulli : sections planes \; ; \; Saint-Venant : loin des charges", "b5", "Navier")]
        for k, (txt, ph, fr) in enumerate(h):
            m = pos(T(txt, sc=0.64), -6.4, -0.2 - 0.55*k); self.ecr(self.a(ph, fr), m, rt=1.0)
        ys = -2.15
        st1 = VGroup(encas(-5.1, ys, h=0.8), poutre(-5.1, -3.7, ys))
        st2 = VGroup(poutre(-0.7, 0.7, ys), pivot(0, ys))
        st3 = VGroup(poutre(3.7, 5.1, ys), appui(4.4, ys))
        cap = [T(r"encastrement : $X,\ Y,\ M_z$", sc=0.6, color=GRIS).move_to(P(-4.4, -3.3)),
               T(r"articulation : $X,\ Y$", sc=0.6, color=GRIS).move_to(P(0, -3.3)),
               T(r"appui simple : $Y$", sc=0.6, color=GRIS).move_to(P(4.4, -3.3))]
        for st, cp, fr in zip([st1, st2, st3], cap, ["L'encastrement", "L'articulation", "l'appui simple"]):
            self.at(self.a("b6", fr), FadeIn(st), FadeIn(cp), run_time=0.6)
        self.fin()

# ================================================================ S2 : coupure et torseur de cohésion
class S2(Cours2):
    sid = "S2"
    def construct(self):
        self.entete(r"1.2 -- Coupure et torseur de cohésion", "Cohésion")
        y, xa, xb, xg = 1.75, -5.5, 5.5, 0.3
        p1 = poutre(xa, xg, y); p2 = poutre(xg, xb, y); sA = pivot(xa, y); sB = appui(xb, y)
        fF = force(-2.6, 2.75, y + 0.07); ch_ = repartie(1.9, 4.6, y, h=0.5)
        self.at(self.t("c1"), Create(p1), Create(p2), FadeIn(sA), FadeIn(sB), GrowArrow(fF), FadeIn(ch_), run_time=1.0)
        cut = DashedLine(P(xg, y - 0.6), P(xg, y + 0.75), color=JAUNE, stroke_width=3, dash_length=0.1)
        lg = lettre("G", xg - 0.25, y + 0.3, col=JAUNE, sc=0.58)
        self.at(self.a("c1", "on coupe la poutre"), Create(cut), FadeIn(lg), run_time=0.6)
        pI = poutre(xa, xg, y, col=BLEU); pII = poutre(xg, xb, y, col=ORANGE)
        lI = T(r"tronçon I", sc=0.62, color=BLEU).move_to(P(-2.6, y - 0.55)); lII = T(r"tronçon II", sc=0.62, color=ORANGE).move_to(P(3.1, y - 0.55))
        self.at(self.a("c2", "le tronçon un"), Create(pI), FadeIn(lI), run_time=0.5)
        self.at(self.a("c2", "le tronçon deux"), Create(pII), FadeIn(lII), run_time=0.5)
        gI = VGroup(p1, pI, sA, fF, lI); gII = VGroup(p2, pII, sB, ch_, lII)
        self.at(self.a("c3", "Le torseur de cohésion"), FadeOut(cut), lg.animate.shift(0.5*LEFT), gI.animate.shift(0.5*LEFT), gII.animate.shift(0.5*RIGHT), run_time=0.8)
        xe = xg - 0.5
        aN = Arrow(P(xe, y), P(xe + 0.75, y), buff=0, color=VERT, stroke_width=5, tip_length=0.16, max_tip_length_to_length_ratio=0.3)
        aT = Arrow(P(xe, y), P(xe, y + 0.8), buff=0, color=VERT, stroke_width=5, tip_length=0.16, max_tip_length_to_length_ratio=0.3)
        aM = Arc(radius=0.45, start_angle=1.12*PI, angle=0.76*PI, arc_center=P(xe, y), color=VERT, stroke_width=4).add_tip(tip_length=0.14)
        lN = M(r"N", sc=0.6, color=VERT).move_to(P(xe + 0.6, y + 0.27)); lT = M(r"T_y", sc=0.6, color=VERT).move_to(P(xe + 0.3, y + 0.85))
        lM = M(r"M_{fz}", sc=0.6, color=VERT).move_to(P(xe - 0.7, y - 0.6))
        self.at(self.a("c3", "l'action du tronçon deux"), GrowArrow(aN), GrowArrow(aT), Create(aM), FadeIn(lN), FadeIn(lT), FadeIn(lM), run_time=0.9)
        d = T(r"torseur de cohésion $=$ actions de \textbf{II sur I}, réduites en $G$", sc=0.74).move_to(P(0, 0.35))
        self.ecr(self.a("c3", "réduite au point G"), d, rt=1.1)
        e = T(r"on isole I : \; $\{\mathrm{II}\to\mathrm{I}\} + \{\bar E\to\mathrm{I}\} = \{0\}$", sc=0.68, color=GRIS).move_to(P(0, -0.45))
        self.ecr(self.a("c4", "On isole le tronçon un"), e, rt=1.1)
        f = M(r"\{\mathcal{T}_{coh}\} = -\{\bar E\to \mathrm{I}\} = +\{\bar E\to \mathrm{II}\}", sc=1.0, color=JAUNE).move_to(P(0, -1.4))
        self.ecr(self.a("c5", "la formule clé"), f, rt=1.4); self.play(Create(enc(f, col=JAUNE, buff=0.18)), run_time=0.4)
        g = T(r"on isole le tronçon qui porte le \textbf{moins} d'actions", sc=0.74, color=VERT).move_to(P(0, -2.45))
        self.ecr(self.a("c6", "Alors on isole"), g, rt=1.0)
        h = T(r"piège : convention « I sur II » $\Rightarrow$ tous les signes s'inversent", sc=0.7, color=ROUGE).move_to(P(0, -3.25))
        self.ecr(self.t("c7"), h, rt=1.1)
        self.fin()

# ================================================================ S3 : composantes et sollicitations
class S3(Cours2):
    sid = "S3"
    def construct(self):
        self.entete(r"1.3 -- Composantes et sollicitations", "Cohésion")
        tz = M(r"\{\mathcal{T}_{coh}\}_G = \begin{Bmatrix} N & M_t \\ T_y & M_{fy} \\ T_z & M_{fz} \end{Bmatrix}_{G,\,(\vec x,\,\vec y,\,\vec z)}", sc=0.95).move_to(P(-3.3, 1.35))
        self.ecr(self.t("d2"), tz, rt=1.4)
        lb = [(r"$N$ : effort normal", BLEU, "d2", "l'effort normal"), (r"$T_y,\ T_z$ : efforts tranchants", BLEU, "d2", "les efforts tranchants"),
              (r"$M_t$ : moment de torsion", ORANGE, "d3", "le moment de torsion"), (r"$M_{fy},\ M_{fz}$ : moments fléchissants", ORANGE, "d3", "les moments fléchissants")]
        for k, (txt, c, ph, fr) in enumerate(lb):
            m = pos(T(txt, sc=0.68, color=c), 0.6, 2.1 - 0.5*k); self.ecr(self.a(ph, fr), m, rt=0.7)
        hd = VGroup(pos(T("sollicitation", sc=0.58, color=GRIS), -6.2, 0.0), pos(T("composantes non nulles", sc=0.58, color=GRIS), -2.2, 0.0), pos(T("exemple", sc=0.58, color=GRIS), 1.8, 0.0))
        fil = Line(P(-6.2, -0.25), P(5.6, -0.25), color=GRIS, stroke_width=1.5)
        self.at(self.t("d4"), FadeIn(hd), Create(fil), run_time=0.6)
        rows = [("Traction / compression", r"$N$", "tirant, câble", "d4", "N seul"), ("Cisaillement", r"$T_y$", "goupille, axe de chape", "d4", "cisaillement"),
                ("Torsion", r"$M_t$", "arbre de transmission", "d4", "torsion"), ("Flexion pure", r"$M_{fz}$", "essieu entre deux roues", "d5", "flexion pure"),
                ("Flexion simple", r"$T_y,\ M_{fz}$", "poutre, console", "d5", "la flexion simple")]
        for k, (a, b, c, ph, fr) in enumerate(rows):
            yy = -0.6 - 0.55*k; col = JAUNE if k == 4 else CRAIE
            r = VGroup(pos(T(a, sc=0.66, color=col), -6.2, yy), pos(T(b, sc=0.68, color=col), -2.2, yy), pos(T(c, sc=0.62, color=GRIS), 1.8, yy))
            self.ecr(self.a(ph, fr), r, rt=0.7)
        pl = T(r"problème plan : \; $N,\ T_y,\ M_{fz}$", sc=0.8, color=JAUNE).move_to(P(0, -3.4))
        self.ecr(self.a("d6", "Dans un problème plan"), pl, rt=0.8); self.play(Create(enc(pl, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

# ================================================================ S4 : équations locales et diagrammes
class S4(Cours2):
    sid = "S4"
    def construct(self):
        self.entete(r"1.4 -- Équations locales et diagrammes", "Équilibre local")
        t1 = pos(T(r"équilibre d'une tranche $dx$, charge linéique $q$ (N/m)", sc=0.64, color=GRIS), -6.4, 2.4)
        self.ecr(self.t("e1"), t1, rt=1.0)
        eq = pos(M(r"\frac{dT_y}{dx} + q_y = 0 \qquad \frac{dM_{fz}}{dx} + T_y = 0", sc=0.85, color=JAUNE), -6.2, 1.5)
        self.ecr(self.a("e2", "Dé T i grec"), eq, rt=1.4); self.play(Create(enc(eq, col=JAUNE, buff=0.15)), run_time=0.4)
        rg = [(r"sans charge répartie : $T_y$ constant, $M_{fz}$ affine", CRAIE, "e3", "Sans charge"),
              (r"charge uniforme : $T_y$ affine, $M_{fz}$ parabolique", CRAIE, "e4", "Sous une charge"),
              (r"force $F\,\vec y$ : $T_y$ saute de $-F$, $M_{fz}$ anguleux", CRAIE, "e5", "Une force concentrée"),
              (r"$M_{fz}$ extrémal là où $T_y$ s'annule", JAUNE, "e6", "Et surtout"),
              (r"$M_{fz} = 0$ en bout libre ou articulé, sans couple", CRAIE, "e6", "Il est nul")]
        for k, (txt, c, ph, fr) in enumerate(rg):
            m = lim(pos(T(txt, sc=0.64, color=c), -6.4, 0.45 - 0.65*k), 6.3); pos(m, -6.4, 0.45 - 0.65*k); self.ecr(self.a(ph, fr), m, rt=0.9)
        X0, X1, y = 1.6, 6.0, 2.0
        po = poutre(X0, X1, y); s1 = pivot(X0, y); s2 = appui(X1, y); ch_ = repartie(X0, X1, y, h=0.45)
        lp = M("p", sc=0.62, color=ROUGE).move_to(P(X1 + 0.35, y + 0.55))
        dT = Diag(X0, X1, 1.0, 0.45, 1.35, -0.9, 0.9, r"T_y", "")
        dM = Diag(X0, X1, 1.0, -1.65, 1.7, -0.02, 0.15, r"M_{fz}", "")
        cT = dT.trace([(0, -0.5), (1, 0.5)], BLEU); aT = dT.aire([(0, -0.5), (1, 0.5)], BLEU)
        f = lambda u: u*(1 - u)/2
        cM = dM.courbe(f, 0, 1, VERT); aM = dM.aire([(u, f(u)) for u in np.linspace(0, 1, 40)], VERT)
        vT = [M(r"-pL/2", sc=0.56, color=BLEU).move_to(dT.p(0.2, -0.72)), M(r"+pL/2", sc=0.56, color=BLEU).move_to(dT.p(0.8, 0.72))]
        vM = M(r"pL^2/8", sc=0.6, color=JAUNE).next_to(dM.p(0.5, 0.125), RIGHT, buff=0.3).shift(0.1*UP)
        self.at(self.t("e7"), Create(po), FadeIn(s1), FadeIn(s2), FadeIn(ch_), FadeIn(lp), Create(dT.fr), Create(dT.zero), FadeIn(dT.nom), Create(dM.fr), Create(dM.zero), FadeIn(dM.nom), run_time=1.0)
        r = pos(T(r"référence : $M_{fz,max} = pL^2/8$, au milieu", sc=0.66, color=VERT), -6.4, -2.85)
        lim(r, 6.4); pos(r, -6.4, -2.85)
        self.ecr(self.a("e7", "charge uniforme p"), r, rt=1.0)
        self.at(self.a("e7", "L'effort tranchant s'annule"), Create(cT), FadeIn(aT), *[FadeIn(v) for v in vT], run_time=0.9)
        vl = DashedLine(dT.p(0.5, 0), dM.p(0.5, 0.125), color=JAUNE, stroke_width=2)
        self.at(self.a("e7", "atteint"), Create(cM), FadeIn(aM), Create(vl), FadeIn(vM), run_time=1.0)
        self.fin()

# ================================================================ Exercice 1 : palan sur deux appuis (L = 5 m, F = 10 kN en x = 2 m)
class S5(Cours2):
    sid = "S5"
    def construct(self):
        self.entete(r"Exercice 1 -- l'énoncé", "Exercice 1")
        y, k = 1.45, 2.0
        X = lambda x: -5.0 + k*x
        po = poutre(X(0), X(5), y); sA = pivot(X(0), y); sB = appui(X(5), y)
        lA = lettre("A", X(0) - 0.35, y + 0.3); lB = lettre("B", X(5) + 0.35, y + 0.3)
        rp = repere(-6.6, 0.45)
        self.at(self.t("f1"), Create(po), FadeIn(lA), FadeIn(lB), FadeIn(rp), run_time=0.8)
        self.at(self.a("f1", "articulée en A"), FadeIn(sA), run_time=0.4)
        self.at(self.a("f1", "en appui simple"), FadeIn(sB), run_time=0.4)
        fF = force(X(2), 2.65, y + 0.07); lF = M(r"F = 10\ \mathrm{kN}", sc=0.62, color=ROUGE).next_to(fF, RIGHT, buff=0.12).shift(0.3*UP)
        lC = lettre("C", X(2) - 0.3, y + 0.3)
        c1 = cote(X(0), X(2), 0.5, r"2\ \mathrm{m}"); c2 = cote(X(2), X(5), 0.5, r"3\ \mathrm{m}")
        self.at(self.a("f2", "au point C"), GrowArrow(fF), FadeIn(lF), FadeIn(lC), run_time=0.6)
        self.at(self.a("f2", "à deux mètres"), FadeIn(c1), FadeIn(c2), run_time=0.6)
        dn = T(r"$L = 5$ m, \; $F = 10$ kN en $C$ ($x = 2$ m), \; poids de la poutre négligé", sc=0.68).move_to(P(0, -0.45))
        self.ecr(self.a("f2", "On néglige"), dn, rt=1.0)
        q = T(r"Diagrammes de $T_y$ et de $M_{fz}$ ? \; Section la plus sollicitée ?", sc=0.78, color=ROUGE).move_to(P(0, -1.4))
        self.ecr(self.t("f3"), q, rt=1.1); self.play(Create(enc(q, buff=0.18)), run_time=0.4)
        rf = T(r"Réfléchissons : forces ponctuelles $\to$ réactions, puis une coupure par intervalle", sc=0.68, color=BLEU).move_to(P(0, -2.4))
        self.ecr(self.a("f4", "quelle méthode"), rf, rt=1.2)
        av = T(r"À vous : mettez la vidéo en pause !", sc=0.75, color=JAUNE).move_to(P(-0.8, -3.25))
        self.ecr(self.t("f5"), av, rt=0.8)
        self.minuteur(2.9, -3.25, "f5", "Mettez la vidéo")
        self.fin()

class S6(Cours2):
    sid = "S6"
    def construct(self):
        self.entete(r"Exercice 1 -- réactions et coupures", "Exercice 1")
        y, k = 1.75, 2.0
        X = lambda x: -5.0 + k*x
        po = poutre(X(0), X(5), y); sA = pivot(X(0), y); sB = appui(X(5), y)
        fF = force(X(2), 2.7, y + 0.07); lF = M(r"10\ \mathrm{kN}", sc=0.6, color=ROUGE).next_to(fF, RIGHT, buff=0.1).shift(0.3*UP)
        lA = lettre("A", X(0) - 0.35, y + 0.3); lB = lettre("B", X(5) + 0.35, y + 0.3); lC = lettre("C", X(2) - 0.3, y + 0.3)
        self.add(po, sA, sB, fF, lF, lA, lB, lC)
        rA = force(X(0), 0.75, y - 0.07, col=VERT); rB = force(X(5), 0.75, y - 0.07, col=VERT)
        lrA = M("Y_A", sc=0.6, color=VERT).next_to(rA, LEFT, buff=0.1); lrB = M("Y_B", sc=0.6, color=VERT).next_to(rB, RIGHT, buff=0.1)
        self.at(self.a("g1", "On isole toute la poutre"), FadeOut(sA), FadeOut(sB), GrowArrow(rA), GrowArrow(rB), FadeIn(lrA), FadeIn(lrB), run_time=0.8)
        x0 = -6.4
        self.etape(1, BLEU, x0, 0.25, M(r"5\,Y_B - 10\times 2 = 0 \;\Rightarrow\; Y_B = 4\ \mathrm{kN}", sc=0.74), self.t("g2"), rt=1.2)
        r2 = pos(M(r"Y_A = 6\ \mathrm{kN}, \quad X_A = 0", sc=0.74, color=VERT), 1.6, 0.25)
        self.ecr(self.t("g3"), r2, rt=0.8)
        self.etape(2, VERT, x0, -0.55, T(r"deux intervalles : $AC$ \; $(0 < x < 2)$ \; et \; $CB$ \; $(2 < x < 5)$", sc=0.7), self.t("g4"), rt=1.1)
        # coupure sur AC
        xg = 1.0
        cut = DashedLine(P(X(xg), y - 0.45), P(X(xg), y + 0.6), color=JAUNE, stroke_width=3, dash_length=0.1)
        pI = poutre(X(0), X(xg), y, col=BLEU); lI = T("I", sc=0.62, color=BLEU).move_to(P((X(0) + X(xg))/2 + 0.4, y - 0.35))
        cx = cote(X(0), X(xg), y + 0.55, "x", col=GRIS, haut=True)
        self.at(self.a("g5", "coupure sur A C"), Create(cut), Create(pI), FadeIn(lI), FadeIn(cx), run_time=0.7)
        self.etape(3, ORANGE, x0, -1.35, M(r"AC,\ \text{tronçon I} : \; T_y = -Y_A = -6\ \mathrm{kN}", sc=0.72), self.t("g6"), rt=1.1)
        m3 = pos(M(r"M_{fz} = -(-6x) = 6x", sc=0.72, color=ORANGE), 1.6, -1.35)
        self.ecr(self.a("g7", "Donc le moment fléchissant"), m3, rt=1.0)
        # coupure sur CB
        xg2 = 3.5
        cut2 = DashedLine(P(X(xg2), y - 0.45), P(X(xg2), y + 0.6), color=JAUNE, stroke_width=3, dash_length=0.1)
        pII = poutre(X(xg2), X(5), y, col=ORANGE); lII = T("II", sc=0.62, color=ORANGE).move_to(P((X(xg2) + X(5))/2 - 0.3, y - 0.35))
        self.at(self.a("g8", "coupure sur C B"), FadeOut(cut), FadeOut(pI), FadeOut(lI), FadeOut(cx), Create(cut2), Create(pII), FadeIn(lII), run_time=0.7)
        self.etape(4, ROUGE, x0, -2.15, M(r"CB,\ \text{tronçon II} : \; T_y = +Y_B = 4\ \mathrm{kN}, \quad M_{fz} = 4\,(5 - x)", sc=0.72), self.t("g9"), rt=1.4)
        ok = pos(T(r"en $C$ : \; $6\times 2 = 4\times 3 = 12$ kN$\cdot$m \; : \; $M_{fz}$ continu \checkmark", sc=0.72, color=VERT), -5.9, -3.0)
        self.ecr(self.t("g10"), ok, rt=1.2)
        self.fin()

class S7(Cours2):
    sid = "S7"
    def construct(self):
        self.entete(r"Exercice 1 -- les diagrammes", "Exercice 1")
        X0, X1, L, y = 1.6, 6.3, 5.0, 2.0
        X = lambda x: X0 + (X1 - X0)*x/L
        po = poutre(X0, X1, y); sA = pivot(X0, y); sB = appui(X1, y)
        fF = force(X(2), 2.7, y + 0.07); lF = M(r"10", sc=0.58, color=ROUGE).next_to(fF, RIGHT, buff=0.08).shift(0.25*UP)
        lA = lettre("A", X0 - 0.3, y + 0.3, sc=0.56); lB = lettre("B", X1 + 0.3, y + 0.3, sc=0.56); lC = lettre("C", X(2) - 0.25, y + 0.3, sc=0.56)
        dT = Diag(X0, X1, L, 0.42, 1.4, -7.5, 5.5, r"T_y", "(kN)", xn=0.85)
        dM = Diag(X0, X1, L, -1.62, 2.0, -1.5, 14, r"M_{fz}", r"(kN$\cdot$m)", xn=0.85)
        self.at(self.t("h1"), Create(po), FadeIn(sA), FadeIn(sB), GrowArrow(fF), FadeIn(lF), FadeIn(lA), FadeIn(lB), FadeIn(lC),
                Create(dT.fr), Create(dT.zero), FadeIn(dT.nom), Create(dM.fr), Create(dM.zero), FadeIn(dM.nom), run_time=1.0)
        vC = DashedLine(P(X(2), y - 0.15), P(X(2), dM.fr.get_bottom()[1]), color=GRIS, stroke_width=1.5, dash_length=0.08)
        x0 = -6.5
        self.etape(5, BLEU, x0, 2.1, T(r"diagrammes alignés sous la poutre", sc=0.7), self.a("h1", "les diagrammes"), rt=0.8)
        pT = [(0, -6), (2, -6), (2, 4), (5, 4)]
        cT = dT.trace(pT, BLEU); aT = dT.aire(pT, BLEU)
        vT = [M("-6", sc=0.58, color=BLEU).next_to(dT.p(1, -6), UP, buff=0.08), M("+4", sc=0.58, color=BLEU).next_to(dT.p(3.5, 4), DOWN, buff=0.08)]
        sj = M(r"+10", sc=0.58, color=JAUNE).next_to(dT.p(2, 1.6), LEFT, buff=0.1)
        self.at(self.t("h2"), Create(cT), FadeIn(aT), *[FadeIn(v) for v in vT], Create(vC), run_time=1.0)
        t2 = pos(T(r"$T_y$ : $-6$ puis $+4$ ; saut de $+10 = -(-F)$ en $C$", sc=0.66), x0 + 0.5, 1.3)
        self.at(self.a("h2", "un saut de plus dix"), FadeIn(sj), Ecrire(t2, rt=1.0), run_time=1.0)
        pM = [(0, 0), (2, 12), (5, 0)]
        cM = dM.trace(pM, VERT); aM = dM.aire(pM, VERT)
        vM = M("12", sc=0.62, color=VERT).next_to(dM.p(2, 12), UP, buff=0.06).shift(0.25*RIGHT)
        self.at(self.t("h3"), Create(cM), FadeIn(aM), run_time=1.2)
        t3 = pos(T(r"$M_{fz}$ : $0 \to 12 \to 0$, affine par morceaux", sc=0.66), x0 + 0.5, 0.55)
        self.at(self.a("h3", "monte jusqu'à douze"), FadeIn(vM), Ecrire(t3, rt=0.9), run_time=0.9)
        t4 = pos(T(r"pentes : $6$ sur $AC$, $-4$ sur $CB$ : c'est $-T_y$ \checkmark", sc=0.66), x0 + 0.5, -0.2)
        self.ecr(self.t("h4"), t4, rt=1.1)
        dot = Dot(dM.p(2, 12), radius=0.09, color=JAUNE)
        t5 = pos(T(r"maximum en $C$, où $T_y$ change de signe", sc=0.66), x0 + 0.5, -0.95)
        self.at(self.t("h5"), FadeIn(dot, scale=2), Ecrire(t5, rt=0.9), run_time=0.9)
        e6 = self.etape(6, JAUNE, x0, -1.85, T(r"section critique : $C$, \; $M_{fz} = 12$ kN$\cdot$m", sc=0.68, color=JAUNE), self.t("h6"), rt=1.0, w=6.0)
        self.play(Create(enc(e6[1], col=JAUNE, buff=0.12)), run_time=0.4)
        t7 = pos(M(r"\frac{Fab}{L} = \frac{10\times 2\times 3}{5} = 12 \;\checkmark", sc=0.72, color=VERT), x0 + 0.5, -2.8)
        self.ecr(self.t("h7"), t7, rt=1.0)
        t8 = pos(T(r"$M_{fz} > 0$ : fibre inférieure tendue", sc=0.64, color=GRIS), x0 + 0.5, -3.55)
        self.ecr(self.t("h8"), t8, rt=0.8)
        self.fin()

# ================================================================ Exercice 2 : console (L = 2 m, p = 3 kN/m, F = 4 kN en bout)
class S8(Cours2):
    sid = "S8"
    def construct(self):
        self.entete(r"Exercice 2 -- l'énoncé", "Exercice 2")
        y, X0, X1 = 1.45, -3.6, 1.4
        en = encas(X0, y, h=1.0); po = poutre(X0, X1, y)
        lO = lettre("O", X0 + 0.25, y - 0.32); lA = lettre("A", X1 + 0.3, y - 0.3)
        rp = repere(3.6, 0.55)
        self.at(self.t("i1"), FadeIn(en), Create(po), FadeIn(rp), run_time=0.8)
        self.at(self.a("i1", "encastrée au point O"), FadeIn(lO), Indicate(en, color=JAUNE), run_time=0.6)
        self.at(self.a("i1", "libre en A"), FadeIn(lA), run_time=0.4)
        ch_ = repartie(X0 + 0.05, X1, y, h=0.5); lp = M(r"p = 3\ \mathrm{kN/m}", sc=0.6, color=ROUGE).move_to(P(-1.1, y + 0.82))
        fF = force(X1, 2.65, y + 0.07); lF = M(r"F = 4\ \mathrm{kN}", sc=0.6, color=ROUGE).next_to(fF, RIGHT, buff=0.12).shift(0.3*UP)
        cL = cote(X0, X1, 0.55, r"L = 2\ \mathrm{m}")
        self.at(self.a("i2", "trois kilonewtons par mètre"), FadeIn(ch_, shift=0.15*DOWN), FadeIn(lp), FadeIn(cL), run_time=0.8)
        dn = T(r"$L = 2$ m, \; $p = 3$ kN/m ($q_y = -3$), \; $F = 4$ kN en $A$", sc=0.68).move_to(P(0, -0.35))
        self.at(self.a("i2", "une force de quatre"), GrowArrow(fF), FadeIn(lF), Ecrire(dn, rt=1.0), run_time=1.0)
        q = T(r"$T_y(x)$ et $M_{fz}(x)$, diagrammes, section critique ?", sc=0.78, color=ROUGE).move_to(P(0, -1.3))
        self.ecr(self.t("i3"), q, rt=1.1); self.play(Create(enc(q, buff=0.18)), run_time=0.4)
        rf = T(r"Réfléchissons : l'encastrement cache 3 inconnues. Couper côté libre ?", sc=0.68, color=BLEU).move_to(P(0, -2.3))
        self.ecr(self.a("i4", "quelle méthode"), rf, rt=1.2)
        av = T(r"À vous : mettez la vidéo en pause !", sc=0.75, color=JAUNE).move_to(P(-0.8, -3.2))
        self.ecr(self.t("i5"), av, rt=0.8)
        self.minuteur(2.9, -3.2, "i5", "Mettez la vidéo")
        self.fin()

class S9(Cours2):
    sid = "S9"
    def construct(self):
        self.entete(r"Exercice 2 -- la coupure côté libre", "Exercice 2")
        y, X0, X1, L = 1.75, -4.6, 2.4, 2.0
        X = lambda x: X0 + (X1 - X0)*x/L
        en = encas(X0, y, h=1.0); po = poutre(X0, X1, y)
        ch_ = repartie(X0 + 0.05, X1, y, h=0.5); lp = M(r"3\ \mathrm{kN/m}", sc=0.58, color=ROUGE).move_to(P(X(0.25), y + 0.78))
        fF = force(X1, 2.75, y + 0.07); lF = M(r"4\ \mathrm{kN}", sc=0.58, color=ROUGE).next_to(fF, RIGHT, buff=0.1).shift(0.3*UP)
        lO = lettre("O", X0 + 0.25, y - 0.3, sc=0.56); lA = lettre("A", X1 + 0.3, y - 0.3, sc=0.56)
        self.add(en, po, ch_, lp, fF, lF, lO, lA)
        xg = 0.8; XG = X(xg)
        cut = DashedLine(P(XG, y - 0.5), P(XG, y + 0.7), color=JAUNE, stroke_width=3, dash_length=0.1)
        pII = poutre(XG, X1, y, col=ORANGE); lII = T(r"tronçon II", sc=0.6, color=ORANGE).move_to(P(X1 + 1.75, y - 0.3))
        lG = lettre("G", XG - 0.25, y - 0.3, col=JAUNE, sc=0.56)
        x0 = -6.4
        self.etape(1, BLEU, x0, -0.15, T(r"tronçon II (côté libre) : charges connues, \textbf{pas besoin} de l'encastrement", sc=0.68), self.t("j1"), rt=1.2, w=12.4)
        self.at(self.a("j1", "On isole le tronçon deux"), Create(cut), Create(pII), FadeIn(lII), FadeIn(lG), run_time=0.7)
        flo = [a for a in ch_[1:] if a.get_center()[0] > XG + 0.02]
        Xm = (XG + X1)/2
        R = force(Xm, 2.85, y + 0.07, col=VERT, sw=6, tl=0.22); lR = M(r"3\,(2 - x)", sc=0.58, color=VERT).next_to(R, LEFT, buff=0.1).shift(0.35*UP)
        self.etape(2, VERT, x0, -0.85, T(r"charge répartie : résultante $3\,(2 - x)$, au milieu du tronçon", sc=0.68), self.t("j3"), rt=1.1)
        self.at(self.a("j3", "sa résultante"), *[a.animate.set_opacity(0.25) for a in flo], GrowArrow(R), FadeIn(lR), run_time=0.8)
        self.etape(3, ORANGE, x0, -1.6, M(r"T_y = +\textstyle\sum F_y = -3\,(2 - x) - 4", sc=0.74), self.t("j4"), rt=1.1)
        t5 = pos(T(r"de $-10$ (en $O$) à $-4$ (en $A$)", sc=0.66, color=GRIS), 1.6, -1.6)
        self.ecr(self.a("j5", "de moins dix"), t5, rt=0.8)
        c1 = cote(XG, Xm, y - 0.55, r"(2 - x)/2", col=VERT, sc=0.6); c2 = cote(XG, X1, y - 1.25, r"2 - x", col=CRAIE, sc=0.6)
        self.at(self.a("j6", "Bras de levier"), FadeIn(c1), run_time=0.5)
        self.at(self.a("j6", "pour la force"), FadeIn(c2), run_time=0.5)
        m4 = M(r"M_{fz} = -3\,(2 - x)\cdot\frac{2 - x}{2} - 4\,(2 - x)", sc=0.72)
        self.etape(4, ROUGE, x0, -2.45, m4, self.t("j7"), rt=1.3)
        m4b = pos(M(r"= -1{,}5\,(2 - x)^2 - 4\,(2 - x)", sc=0.72, color=ROUGE), m4.get_right()[0] + 0.15, -2.45)
        self.ecr(self.t("j7b"), m4b, rt=1.1)
        m5 = pos(M(r"M_{fz}(0) = -6 - 8 = -14\ \mathrm{kN\cdot m}, \qquad M_{fz}(2) = 0", sc=0.74, color=JAUNE), x0 + 0.5, -3.3)
        self.ecr(self.t("j8"), m5, rt=1.2)
        self.fin()

class S10(Cours2):
    sid = "S10"
    def construct(self):
        self.entete(r"Exercice 2 -- diagrammes et contrôles", "Exercice 2")
        X0, X1, L, y = 1.6, 6.3, 2.0, 2.0
        X = lambda x: X0 + (X1 - X0)*x/L
        en = encas(X0, y, h=0.9); po = poutre(X0, X1, y); ch_ = repartie(X0 + 0.05, X1, y, h=0.42, pas=0.32)
        fF = force(X1, 2.75, y + 0.07); lO = lettre("O", X0 + 0.22, y - 0.3, sc=0.54); lA = lettre("A", X1 + 0.28, y - 0.3, sc=0.54)
        dT = Diag(X0, X1, L, 0.45, 1.35, -11, 1.5, r"T_y", "(kN)", xn=0.85)
        dM = Diag(X0, X1, L, -1.6, 2.0, -15.5, 1.8, r"M_{fz}", r"(kN$\cdot$m)", xn=0.85)
        Tf = lambda x: -3*(2 - x) - 4; Mf = lambda x: -1.5*(2 - x)**2 - 4*(2 - x)
        cT = dT.trace([(0, Tf(0)), (2, Tf(2))], BLEU); aT = dT.aire([(0, Tf(0)), (2, Tf(2))], BLEU)
        cM = dM.courbe(Mf, 0, 2, VERT); aM = dM.aire([(u, Mf(u)) for u in np.linspace(0, 2, 40)], VERT)
        vT = [M("-10", sc=0.56, color=BLEU).move_to(dT.p(0.25, -7.0)), M("-4", sc=0.56, color=BLEU).move_to(dT.p(1.8, -2.2))]
        vM = M("-14", sc=0.58, color=VERT).move_to(dM.p(0.4, -14.3))
        self.at(self.t("k1"), FadeIn(en), Create(po), FadeIn(ch_), GrowArrow(fF), FadeIn(lO), FadeIn(lA),
                Create(dT.fr), Create(dT.zero), FadeIn(dT.nom), Create(dM.fr), Create(dM.zero), FadeIn(dM.nom), run_time=1.0)
        x0 = -6.5
        self.etape(5, BLEU, x0, 2.1, T(r"$T_y$ affine, \; $M_{fz}$ parabolique", sc=0.7), self.a("k1", "les diagrammes"), rt=0.8)
        self.at(self.a("k1", "L'effort tranchant est une droite"), Create(cT), FadeIn(aT), *[FadeIn(v) for v in vT], run_time=0.8)
        self.at(self.a("k1", "le moment une parabole"), Create(cM), FadeIn(aM), FadeIn(vM), run_time=1.0)
        k2 = pos(M(r"\frac{dT_y}{dx} = 3 = -q_y \;\checkmark", sc=0.74, color=VERT), x0 + 0.5, 1.2)
        self.ecr(self.t("k2"), k2, rt=0.9)
        k3 = pos(M(r"\frac{dM_{fz}}{dx} = 3\,(2 - x) + 4 = -T_y \;\checkmark", sc=0.74, color=VERT), x0 + 0.5, 0.2)
        self.ecr(self.t("k3"), k3, rt=1.1)
        k4 = pos(T(r"piège : $T_y \neq 0$ partout $\Rightarrow$ $|M_{fz}|_{max}$ au bord", sc=0.66, color=ROUGE), x0 + 0.5, -0.7)
        dot = Dot(dM.p(0, -14), radius=0.09, color=ROUGE)
        self.at(self.t("k4"), Ecrire(k4, rt=1.0), FadeIn(dot, scale=2), run_time=1.0)
        e6 = self.etape(6, JAUNE, x0, -1.55, T(r"section critique : $O$ \; ($14$ kN$\cdot$m ; $10$ kN)", sc=0.68, color=JAUNE), self.t("k5"), rt=1.1, w=5.9)
        self.play(Create(enc(e6[1], col=JAUNE, buff=0.12)), run_time=0.4)
        k6 = pos(T(r"encastrement : \; $Y_O = 10$ kN, \; $M_O = 14$ kN$\cdot$m", sc=0.66), x0 + 0.5, -2.4)
        self.ecr(self.a("k6", "l'encastrement retient"), k6, rt=1.0)
        k7 = pos(M(r"pL + F = 6 + 4, \qquad pL^2/2 + FL = 6 + 8 \;\checkmark", sc=0.7, color=VERT), x0 + 0.5, -3.0)
        self.ecr(self.t("k7"), k7, rt=1.1)
        k8 = pos(T(r"$M_{fz} < 0$ : fibre supérieure tendue", sc=0.64, color=GRIS), x0 + 0.5, -3.6)
        self.ecr(self.t("k8"), k8, rt=0.8)
        self.fin()

# ================================================================ Exercice 3 : charge sur la moitié gauche (L = 4 m, p = 5 kN/m sur [0, 2])
class S11(Cours2):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice 3 -- l'énoncé", "Exercice 3")
        y, k = 1.55, 2.2
        X = lambda x: -4.4 + k*x
        po = poutre(X(0), X(4), y); sA = pivot(X(0), y); sB = appui(X(4), y)
        lA = lettre("A", X(0) - 0.35, y + 0.3); lB = lettre("B", X(4) + 0.35, y + 0.3)
        rp = repere(-6.6, 0.5)
        self.at(self.t("l1"), Create(po), FadeIn(sA), FadeIn(sB), FadeIn(lA), FadeIn(lB), FadeIn(rp), run_time=0.9)
        ch_ = repartie(X(0) + 0.05, X(2), y, h=0.5); lp = M(r"p = 5\ \mathrm{kN/m}", sc=0.6, color=ROUGE).move_to(P(X(1), y + 0.85))
        tk = Line(P(X(2), y - 0.15), P(X(2), y + 0.15), color=CRAIE, stroke_width=3); lC = lettre("C", X(2) + 0.3, y + 0.3)
        c1 = cote(X(0), X(2), 0.6, r"2\ \mathrm{m}"); c2 = cote(X(2), X(4), 0.6, r"2\ \mathrm{m}")
        self.at(self.t("l2"), FadeIn(ch_, shift=0.15*DOWN), FadeIn(lp), run_time=0.7)
        dn = T(r"$L = 4$ m, \; $p = 5$ kN/m de $A$ à $C$ (milieu), \; soit $q_y = -5$", sc=0.68).move_to(P(0, -0.2))
        self.ecr(self.a("l2", "couvre seulement"), dn, rt=1.0)
        self.at(self.a("l2", "jusqu'au milieu C"), Create(tk), FadeIn(lC), FadeIn(c1), FadeIn(c2), run_time=0.6)
        q = T(r"Où $M_{fz}$ est-il maximal ? Combien vaut-il ?", sc=0.8, color=ROUGE).move_to(P(0, -1.1))
        self.ecr(self.t("l3"), q, rt=1.0); self.play(Create(enc(q, buff=0.18)), run_time=0.4)
        rf = T(r"Réfléchissons : réactions, puis intégrer $T_y' = -q_y$ et $M_{fz}' = -T_y$", sc=0.68, color=BLEU).move_to(P(0, -2.0))
        lim(rf, 13.0)
        self.ecr(self.a("l4", "quelle méthode"), rf, rt=1.2)
        ind = T(r"Indice : cherchez où $T_y$ s'annule", sc=0.68, color=VERT).move_to(P(0, -2.7))
        self.ecr(self.t("l5"), ind, rt=0.8)
        av = T(r"À vous : mettez la vidéo en pause !", sc=0.75, color=JAUNE).move_to(P(-0.8, -3.4))
        self.ecr(self.a("l5", "À vous"), av, rt=0.8)
        self.minuteur(2.9, -3.4, "l5", "Mettez la vidéo")
        self.fin()

def fig3(X0, X1, y, h=0.45):
    L = 4.0; X = lambda x: X0 + (X1 - X0)*x/L
    po = poutre(X0, X1, y); sA = pivot(X0, y); sB = appui(X1, y); ch_ = repartie(X0 + 0.05, X(2), y, h=h, pas=0.3)
    lA = lettre("A", X0 - 0.3, y + 0.3, sc=0.54); lB = lettre("B", X1 + 0.3, y + 0.3, sc=0.54)
    tk = Line(P(X(2), y - 0.13), P(X(2), y + 0.13), color=CRAIE, stroke_width=3); lC = lettre("C", X(2) + 0.25, y - 0.3, sc=0.54)
    return VGroup(po, sA, sB, ch_, lA, lB, tk, lC), ch_, X

class S12(Cours2):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice 3 -- réactions et effort tranchant", "Exercice 3")
        X0, X1, y = 1.6, 6.3, 2.0
        fg, ch_, X = fig3(X0, X1, y)
        dT = Diag(X0, X1, 4.0, 0.3, 1.8, -11.0, 5.5, r"T_y", "(kN)", xn=0.85)
        self.at(self.t("m1"), FadeIn(fg), Create(dT.fr), Create(dT.zero), FadeIn(dT.nom), run_time=0.9)
        R = force(X(1), 2.85, y + 0.07, col=VERT, sw=6, tl=0.22); lR = M(r"10\ \mathrm{kN}", sc=0.56, color=VERT).next_to(R, LEFT, buff=0.08).shift(0.3*UP)
        x0 = -6.5
        self.etape(1, BLEU, x0, 2.1, T(r"charge totale : $5\times 2 = 10$ kN, en $x = 1$", sc=0.68), self.a("m1", "La charge totale"), rt=1.0)
        self.at(self.a("m1", "vaut dix kilonewtons"), ch_.animate.set_opacity(0.25), GrowArrow(R), FadeIn(lR), run_time=0.8)
        m2 = pos(M(r"4\,Y_B = 10\times 1 \;\Rightarrow\; Y_B = 2{,}5\ \mathrm{kN}, \; Y_A = 7{,}5\ \mathrm{kN}", sc=0.7), x0 + 0.5, 1.3)
        lim(m2, 6.0); pos(m2, x0 + 0.5, 1.3)
        self.ecr(self.t("m2"), m2, rt=1.2)
        m3 = pos(T(r"charge à gauche : $A$ porte la plus grosse part", sc=0.62, color=GRIS), x0 + 0.5, 0.6)
        self.ecr(self.t("m3"), m3, rt=0.8)
        self.etape(2, VERT, x0, -0.2, M(r"AC : \; q_y = -5 \;\Rightarrow\; \frac{dT_y}{dx} = 5", sc=0.74), self.t("m4"), rt=1.0)
        self.at(self.a("m4", "Il est affine"), FadeOut(R), FadeOut(lR), ch_.animate.set_opacity(1), run_time=0.5)
        m5 = pos(M(r"T_y(0^+) = -Y_A = -7{,}5", sc=0.72), x0 + 0.5, -1.1)
        self.ecr(self.t("m5"), m5, rt=0.9)
        T1 = lambda x: 5*x - 7.5
        cT1 = dT.trace([(0, T1(0)), (2, T1(2))], BLEU); aT1 = dT.aire([(0, T1(0)), (1.5, 0)], BLEU); aT1b = dT.aire([(1.5, 0), (2, T1(2))], BLEU)
        v0 = M(r"-7{,}5", sc=0.56, color=BLEU).next_to(dT.p(0, -7.5), DOWN, buff=0.08).shift(0.3*RIGHT)
        m6 = pos(M(r"T_y = 5x - 7{,}5", sc=0.76, color=BLEU), x0 + 0.5, -1.85)
        self.at(self.t("m6"), Ecrire(m6, rt=0.8), Create(cT1), FadeIn(aT1), FadeIn(aT1b), FadeIn(v0), run_time=1.0)
        self.play(Create(enc(m6, col=BLEU, buff=0.12)), run_time=0.4)
        cT2 = dT.trace([(2, 2.5), (4, 2.5)], BLEU); aT2 = dT.aire([(2, 2.5), (4, 2.5)], BLEU)
        v2 = M(r"2{,}5", sc=0.56, color=BLEU).next_to(dT.p(3, 2.5), UP, buff=0.08)
        m7 = pos(T(r"$CB$ : $T_y = 2{,}5 = +Y_B$ \checkmark", sc=0.68, color=VERT), x0 + 0.5, -2.65)
        self.at(self.t("m7"), Create(cT2), FadeIn(aT2), FadeIn(v2), Ecrire(m7, rt=0.9), run_time=0.9)
        z = Dot(dT.p(1.5, 0), radius=0.09, color=JAUNE)
        box = M(r"T_y = 0 \;\text{ en }\; x = 1{,}5\ \mathrm{m}", sc=0.78, color=JAUNE).move_to(P(3.8, -1.55))
        vl = DashedLine(dT.p(1.5, 0), P(X(1.5), box.get_top()[1] + 0.25), color=JAUNE, stroke_width=2)
        ca = carte(3, JAUNE, box.get_left()[0] - 0.55, -1.55)
        self.at(self.t("m8"), FadeIn(z, scale=2), Create(vl), Create(ca[0]), FadeIn(ca[1]), Ecrire(box, rt=0.9), run_time=1.0)
        self.play(Create(enc(box, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

class S13(Cours2):
    sid = "S13"
    def construct(self):
        self.entete(r"Exercice 3 -- le moment maximal", "Exercice 3")
        X0, X1, y = 1.6, 6.3, 2.1
        fg, ch_, X = fig3(X0, X1, y, h=0.4)
        dT = Diag(X0, X1, 4.0, 0.72, 1.25, -11.0, 4.0, r"T_y", "(kN)", xn=0.85)
        dM = Diag(X0, X1, 4.0, -1.45, 2.5, -0.6, 11.0, r"M_{fz}", r"(kN$\cdot$m)", xn=0.85)
        T1 = lambda x: 5*x - 7.5
        pT = [(0, -7.5), (2, 2.5), (4, 2.5)]
        cT = dT.trace(pT, BLEU); aT = VGroup(dT.aire([(0, -7.5), (1.5, 0)], BLEU), dT.aire([(1.5, 0), (2, 2.5), (4, 2.5)], BLEU))
        self.play(FadeIn(fg), Create(dT.fr), Create(dT.zero), FadeIn(dT.nom), Create(cT), FadeIn(aT), Create(dM.fr), Create(dM.zero), FadeIn(dM.nom), run_time=0.4)
        x0 = -6.5
        self.etape(4, ORANGE, x0, 2.1, M(r"\frac{dM_{fz}}{dx} = -T_y, \qquad M_{fz}(0) = 0", sc=0.74), self.t("n1"), rt=1.0)
        M1 = lambda x: 7.5*x - 2.5*x**2
        cM1 = dM.courbe(M1, 0, 2, VERT); aM1 = dM.aire([(u, M1(u)) for u in np.linspace(0, 2, 40)], VERT)
        n2 = pos(M(r"AC : \; M_{fz} = 7{,}5\,x - 2{,}5\,x^2", sc=0.74), x0 + 0.5, 1.15)
        self.at(self.t("n2"), Ecrire(n2, rt=1.0), Create(cM1), FadeIn(aM1), run_time=1.1)
        n3 = pos(M(r"M_{fz}(1{,}5) = 11{,}25 - 5{,}625 = 5{,}625\ \mathrm{kN\cdot m}", sc=0.7, color=JAUNE), x0 + 0.5, 0.3)
        lim(n3, 5.9); pos(n3, x0 + 0.5, 0.3)
        dmx = Dot(dM.p(1.5, 5.625), radius=0.09, color=JAUNE); vl = DashedLine(dT.p(1.5, 0), dM.p(1.5, 5.625), color=JAUNE, stroke_width=2)
        lmx = VGroup(DashedLine(dM.p(0, 5.625), dM.p(1.5, 5.625), color=JAUNE, stroke_width=1.5, dash_length=0.06), M(r"5{,}625", sc=0.56, color=JAUNE).move_to(dM.p(0.3, 6.5)))
        self.at(self.t("n3"), Ecrire(n3, rt=1.2), Create(vl), FadeIn(dmx, scale=2), FadeIn(lmx), run_time=1.2)
        self.play(Create(enc(n3, col=JAUNE, buff=0.12)), run_time=0.4)
        M2 = lambda x: 2.5*(4 - x)
        cM2 = dM.trace([(2, 5), (4, 0)], VERT); aM2 = dM.aire([(2, 5), (4, 0)], VERT)
        n4 = pos(M(r"CB : \; M_{fz} = 2{,}5\,(4 - x), \quad M_{fz}(2) = 5", sc=0.72), x0 + 0.5, -0.55)
        l5 = M(r"5", sc=0.56, color=VERT).move_to(dM.p(2.3, 3.45))
        self.at(self.t("n4"), Ecrire(n4, rt=1.1), Create(cM2), FadeIn(aM2), FadeIn(l5), run_time=1.1)
        n5 = pos(T(r"continuité en $C$ : \; $15 - 10 = 5$ \checkmark", sc=0.68, color=VERT), x0 + 0.5, -1.3)
        self.ecr(self.t("n5"), n5, rt=0.9)
        n6 = pos(T(r"max à $1{,}5$ m : ni en $x = 1$, ni en $x = 2$ !", sc=0.68, color=ROUGE), x0 + 0.5, -2.05)
        self.at(self.t("n6"), Ecrire(n6, rt=1.0), Indicate(dmx, color=ROUGE, scale_factor=1.8), run_time=1.0)
        Ms = lambda x: M1(4 - x) if x > 2 else M2(4 - x)
        cS = dM.tirets([(u, Ms(u)) for u in np.linspace(0, 4, 80)], BLEU)
        n7 = pos(M(r"\text{symétrie : } 5 + 5 = 10", sc=0.72, color=VERT), x0 + 0.5, -2.95)
        self.at(self.t("n7"), Create(cS), Ecrire(n7, rt=0.9), run_time=1.0)
        cP = dM.tirets([(u, 5*u*(4 - u)/2) for u in np.linspace(0, 4, 80)], JAUNE)
        lP = M(r"10", sc=0.56, color=JAUNE).next_to(dM.p(2, 10), UP, buff=0.06).shift(0.3*RIGHT)
        n8 = pos(M(r"= \frac{pL^2}{8} \;\checkmark", sc=0.72, color=VERT), n7.get_right()[0] + 0.12, -2.95)
        self.at(self.a("n8", "la poutre chargée partout"), Create(cP), FadeIn(lP), run_time=1.0)
        self.ecr(self.a("n8", "C'est bien"), n8, rt=0.8)
        self.fin()

# ================================================================ S14 : la méthode
class S14(Cours2):
    sid = "S14"
    def construct(self):
        self.entete(r"Ce qu'il faut retenir : la méthode", "Bilan")
        pts = [("o2", r"\textbf{Modéliser} : liaisons, charges signées ($q_y = -p$), réactions si besoin", BLEU),
               ("o3", r"\textbf{Découper} : un intervalle entre deux événements (appui, force, couple, charge)", VERT),
               ("o4", r"\textbf{Couper} le tronçon le plus simple : $-\{\bar E\to\mathrm{I}\}$ ou $+\{\bar E\to\mathrm{II}\}$", ORANGE),
               ("o5", r"\textbf{Tracer} $T_y$ puis $M_{fz}$, alignés sous la poutre", ROUGE),
               ("o6", r"\textbf{Contrôler} : $M_{fz}' = -T_y$, sauts, continuité, zéros, max où $T_y = 0$", JAUNE)]
        for k, (ph_, txt, c) in enumerate(pts):
            yy = 2.0 - 0.95*k
            ca = carte(k+1, c, -6.1, yy); tx = lim(pos(T(txt, sc=0.68), -5.55, yy), 12.0); pos(tx, -5.55, yy)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.1), run_time=1.0)
        nx = T(r"Prochaine vidéo : des efforts aux \textbf{contraintes}, dimensionner en résistance", sc=0.66, color=GRIS).move_to(P(0, -3.0))
        self.ecr(self.t("o7"), nx, rt=1.1)
        self.fin()
