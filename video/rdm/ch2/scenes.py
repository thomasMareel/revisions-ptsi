from base import *
# ---------- outils communs (repris des chapitres SLCI) ----------
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)
def chrono(x, y):
    pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([x, y, 0])
    arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
    return pa, arc
def cadre(x, y, w, h, l0, l1, g0, g1):
    ax = Axes(x_range=[l0, l1, 1], y_range=[g0, g1, 1], x_length=w, y_length=h, tips=False,
              axis_config={"stroke_opacity": 0, "include_ticks": False}).move_to([x, y, 0])
    fr = Rectangle(width=w, height=h, color=GRIS, stroke_width=2).move_to([x, y, 0])
    return ax, fr
def lig(ax, pts, col=ORANGE, sw=4):
    return VMobject(color=col, stroke_width=sw).set_points_as_corners([ax.c2p(a, b) for a, b in pts])
def P(x, y): return np.array([x, y, 0.0])
def fleche(a, b, col=ROUGE, sw=4, tl=0.18):
    return Arrow(P(*a), P(*b), buff=0, color=col, stroke_width=sw, tip_length=tl, max_tip_length_to_length_ratio=0.6, max_stroke_width_to_length_ratio=20)
# ---------- dessins de RdM ----------
def hachures(x0, y0, x1, y1, pas=0.2, col=GRIS, sw=1.5):
    """traits obliques à 45° dans le rectangle [x0, x1] x [y0, y1]"""
    h = y1 - y0; g = VGroup()
    u = x0 - h
    while u < x1:
        a = (max(u, x0), y0 + max(0, x0 - u)); b = (min(u + h, x1), y0 + min(h, x1 - u))
        if b[0] > a[0]: g.add(Line(P(*a), P(*b), color=col, stroke_width=sw))
        u += pas
    return g
def bati(x0, x1, y0, y1):
    return VGroup(Rectangle(width=x1 - x0, height=y1 - y0, color=GRIS, stroke_width=2).move_to(P((x0 + x1)/2, (y0 + y1)/2)), hachures(x0, y0, x1, y1))
def poutre(xa, xb, y, col=CRAIE, sw=9): return Line(P(xa, y), P(xb, y), color=col, stroke_width=sw)
def pivot(x, y, col=CRAIE):
    tri = Polygon(P(x, y), P(x - 0.25, y - 0.42), P(x + 0.25, y - 0.42), color=col, stroke_width=3)
    sol = Line(P(x - 0.38, y - 0.42), P(x + 0.38, y - 0.42), color=col, stroke_width=3)
    return VGroup(tri, sol, hachures(x - 0.38, y - 0.58, x + 0.38, y - 0.42, pas=0.14))
def glissant(x, y, col=CRAIE):
    tri = Polygon(P(x, y), P(x - 0.25, y - 0.36), P(x + 0.25, y - 0.36), color=col, stroke_width=3)
    rl = VGroup(*[Circle(radius=0.065, color=col, stroke_width=2.5).move_to(P(x + d, y - 0.43)) for d in (-0.13, 0.13)])
    sol = Line(P(x - 0.38, y - 0.5), P(x + 0.38, y - 0.5), color=col, stroke_width=3)
    return VGroup(tri, rl, sol, hachures(x - 0.38, y - 0.66, x + 0.38, y - 0.5, pas=0.14))
def cote(xa, xb, y, txt, col=GRIS, sc=0.55):
    l = DoubleArrow(P(xa, y), P(xb, y), buff=0, color=col, stroke_width=2, tip_length=0.12, max_tip_length_to_length_ratio=0.3)
    t = T(txt, sc=sc, color=col).next_to(l, DOWN, buff=0.08)
    return VGroup(l, t)
def repere(x, y, L=0.6, col=GRIS):
    ax = fleche((x, y), (x + L, y), col=col, sw=3, tl=0.13); ay = fleche((x, y), (x, y + L), col=col, sw=3, tl=0.13)
    lx = M(r"x", sc=0.6, color=col).next_to(ax.get_end(), RIGHT, buff=0.06); ly = M(r"y", sc=0.6, color=col).next_to(ay.get_end(), UP, buff=0.06)
    return VGroup(ax, ay, lx, ly)
def coche(x, y, col=VERT):
    return VMobject(color=col, stroke_width=6).set_points_as_corners([P(x - 0.18, y), P(x - 0.05, y - 0.15), P(x + 0.2, y + 0.2)])
def croix(x, y, col=ROUGE, r=0.15):
    return VGroup(Line(P(x - r, y - r), P(x + r, y + r), color=col, stroke_width=6), Line(P(x - r, y + r), P(x + r, y - r), color=col, stroke_width=6))
def couple(cx, cy, r, a0, da, col=ORANGE, sw=3):
    return Arc(radius=r, start_angle=a0, angle=da, arc_center=P(cx, cy), color=col, stroke_width=sw).add_tip(tip_length=0.16, tip_width=0.16)
def ipe(x, y, h=0.85, b=0.5, e=0.09, col=CRAIE):
    sv = Rectangle(width=b, height=e).move_to(P(x, y + h/2 - e/2)); si = Rectangle(width=b, height=e).move_to(P(x, y - h/2 + e/2))
    am = Rectangle(width=e*0.7, height=h - 2*e).move_to(P(x, y))
    return VGroup(sv, si, am).set_stroke(col, 2).set_fill(col, 0.35)
def chape(cx, cy, k=1.0, axe_col=BLEU):
    """vue de côté d'une chape : deux joues pendues au bâti, l'œil de la tige, l'axe qui traverse le tout"""
    jw, jh, ew, eh, aw, ah = 0.2*k, 0.95*k, 0.44*k, 0.62*k, 1.4*k, 0.2*k
    top = cy + 0.62*k*0.45 + 0.4*k
    joues = VGroup(*[Rectangle(width=jw, height=jh, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.12).move_to(P(cx + s*0.45*k, top - jh/2)) for s in (-1, 1)])
    oeil = RoundedRectangle(corner_radius=0.14*k, width=ew, height=eh, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.12).move_to(P(cx, cy))
    axe = Rectangle(width=aw, height=ah, color=axe_col, stroke_width=3).set_fill(axe_col, 0.45).move_to(P(cx, cy))
    return joues, oeil, axe, top

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PT", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Résistance des matériaux -- Chapitre 2}", sc=1.1, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Contraintes et dimensionnement en résistance", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-5.4, 1.3, 0], [5.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        # petite poutre fléchie : la question du jour
        xa, xb, y = 1.9, 6.1, -0.55
        pt = poutre(xa, xb, y); pa = pivot(xa, y - 0.05); pb = glissant(xb, y - 0.05)
        fs = [fleche((x, y + 1.0), (x, y + 0.07)) for x in (3.0, 5.0)]
        q = M(r"\sigma_{max} \le R_{pe}\;?", sc=0.85, color=JAUNE).move_to([4.0, -1.75, 0])
        self.at(self.a("a2", "la pièce va-t-elle tenir"), Create(pt), Create(pa), Create(pb), *[GrowArrow(f) for f in fs], run_time=1.0)
        self.play(Ecrire(q, rt=0.6))
        items = []
        for k, (txt, col) in enumerate([("Contraintes et sections", BLEU), ("Le critère de résistance", VERT), ("Exercice 1 : une suspente et son axe", ORANGE),
                                         ("Exercice 2 : un arbre en torsion", ROUGE), ("Exercice 3 : une poutre en flexion", JAUNE)]):
            yy = 0.65 - 0.68*k
            items.append(VGroup(carte(k+1, col, -6.2, yy), pos(T(txt, sc=0.74), -5.65, yy)))
        for it, (sid, fr_) in zip(items, [("a3", "un cours express"), ("a3", "le critère de résistance"), ("a4", "une suspente"),
                                          ("a4", "un arbre en torsion"), ("a4", "une poutre en flexion")]):
            self.jusqua(self.a(sid, fr_)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"2.1 -- Contraintes et caractéristiques des sections", "Cours")
        # vecteur contrainte sur la section
        tr = Rectangle(width=1.1, height=1.2, color=GRIS, stroke_width=2).set_fill(GRIS, 0.12).move_to([-5.95, 1.85, 0])
        lI = T("I", sc=0.6, color=GRIS).move_to([-6.2, 1.85, 0])
        sec = Line([-5.4, 1.25, 0], [-5.4, 2.45, 0], color=JAUNE, stroke_width=5)
        mp = Dot([-5.4, 1.7, 0], color=CRAIE, radius=0.06)
        fs = fleche((-5.4, 1.7), (-4.65, 1.7), col=ROUGE, tl=0.15); ft = fleche((-5.4, 1.7), (-5.4, 2.4), col=BLEU, tl=0.15)
        ls = M(r"\sigma", sc=0.7, color=ROUGE).next_to(fs.get_end(), DOWN, buff=0.1); lt = M(r"\tau", sc=0.7, color=BLEU).next_to(ft.get_end(), RIGHT, buff=0.1)
        self.at(self.t("b1"), Create(tr), FadeIn(lI), Create(sec), run_time=0.7)
        fc = pos(M(r"\vec C(M,\vec x) = \sigma\,\vec x + \vec\tau", sc=0.8), -4.2, 2.15)
        self.at(self.a("b1", "un vecteur contrainte"), FadeIn(mp), GrowArrow(fs), GrowArrow(ft), Ecrire(fc, rt=1.0), run_time=1.0)
        self.at(self.a("b2", "normale"), FadeIn(ls), Indicate(fs, color=ROUGE), run_time=0.6)
        self.at(self.a("b2", "tangentielle"), FadeIn(lt), Indicate(ft, color=BLEU), run_time=0.6)
        de = pos(T(r"$\sigma$ : traction ou compression \;;\; $\tau$ : cisaillement", sc=0.55, color=GRIS), -4.2, 1.5)
        self.play(Ecrire(de, rt=0.9))
        un = pos(T(r"unité : $1\ \mathrm{MPa} = 1\ \mathrm{N/mm^2}$", sc=0.68, color=JAUNE), 1.85, 2.15)
        self.ecr(self.t("b3"), un, rt=0.9)
        ho = pos(T(r"Hooke : $\sigma = E\,\varepsilon$ \; (si $\sigma < R_e$)", sc=0.68), 1.85, 1.5)
        self.ecr(self.a("b4", "la loi de Hooke"), ho, rt=1.0)
        # tableau des sections
        sep = Line([-6.6, 0.98, 0], [6.6, 0.98, 0], color=GRIS, stroke_width=1.5, stroke_opacity=0.5)
        X = [-4.5, 0.0, 4.5]; yd = 0.5
        r1 = Rectangle(width=0.42, height=0.72, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.2).move_to([X[0], yd, 0])
        d1 = Circle(radius=0.36, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.2).move_to([X[1], yd, 0])
        t1 = Annulus(inner_radius=0.21, outer_radius=0.36, color=CRAIE, stroke_width=3, fill_opacity=0.2).move_to([X[2], yd, 0])
        axz = [DashedLine([x - 0.6, yd, 0], [x + 0.6, yd, 0], color=GRIS, stroke_width=1.5) for x in X]
        lz = [M(r"z", sc=0.5, color=GRIS).next_to(a, RIGHT, buff=0.06) for a in axz]
        lb = [T(r"$b$", sc=0.55).next_to(r1, DOWN, buff=0.06), T(r"$h$", sc=0.55).next_to(r1, LEFT, buff=0.08).shift(0.22*UP),
              T(r"$D$", sc=0.55).next_to(d1, DOWN, buff=0.06), T(r"$D,\ d$", sc=0.55).next_to(t1, DOWN, buff=0.06)]
        self.at(self.a("b5", "La section intervient"), Create(sep), Create(r1), Create(d1), Create(t1), *[Create(a) for a in axz], *[FadeIn(l) for l in lz + lb], run_time=1.0)
        R = [-0.64, -1.4, -2.16, -2.92]; sc = 0.55
        def cell(i, j, tex, col): return M(tex, sc=sc, color=col).move_to([X[i], R[j], 0])
        S_ = [cell(0, 0, r"S = bh", CRAIE), cell(1, 0, r"S = \dfrac{\pi D^2}{4}", CRAIE), cell(2, 0, r"S = \dfrac{\pi (D^2 - d^2)}{4}", CRAIE)]
        self.at(self.a("b5", "l'aire S"), *[Ecrire(c, rt=0.6) for c in S_], run_time=0.8)
        ir = cell(0, 1, r"I_{Gz} = \dfrac{b\,h^3}{12}", BLEU)
        self.ecr(self.t("b6"), ir, rt=0.8)
        idq = cell(1, 1, r"I_{Gz} = \dfrac{\pi D^4}{64}", BLEU); i0d = cell(1, 2, r"I_0 = \dfrac{\pi D^4}{32}", ORANGE)
        self.ecr(self.a("b7", "Pour un disque"), idq, rt=0.8)
        i0r = M(r"\text{---}", sc=sc, color=GRIS).move_to([X[0], R[2], 0])
        self.at(self.a("b7", "le moment polaire"), Ecrire(i0d, rt=0.8), FadeIn(i0r), run_time=0.8)
        it = cell(2, 1, r"I_{Gz} = \dfrac{\pi (D^4 - d^4)}{64}", BLEU); i0t = cell(2, 2, r"I_0 = \dfrac{\pi (D^4 - d^4)}{32}", ORANGE)
        self.at(self.a("b7", "Pour un tube"), Ecrire(it, rt=0.9), Ecrire(i0t, rt=0.9), run_time=0.9)
        wd = cell(1, 3, r"\dfrac{I_{Gz}}{v} = \dfrac{\pi D^3}{32}", VERT); wt = cell(2, 3, r"\dfrac{I_{Gz}}{v} = \dfrac{\pi (D^4 - d^4)}{32\,D}", VERT)
        self.at(self.a("b8", "le module de flexion"), Ecrire(wd, rt=0.9), Ecrire(wt, rt=0.9), run_time=0.9)
        wr = cell(0, 3, r"\dfrac{I_{Gz}}{v} = \dfrac{b\,h^2}{6}", VERT)
        self.ecr(self.t("b8b"), wr, rt=0.8); self.play(Create(enc(wr, col=VERT, buff=0.1)), run_time=0.4)
        idee = T(r"la matière compte avec le \textbf{carré} de sa distance à l'axe", sc=0.68, color=JAUNE).move_to([0, -3.62, 0])
        self.ecr(self.t("b9"), idee, rt=1.1)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"2.2 -- Traction, cisaillement et torsion", "Cours")
        X = [-4.6, 0.0, 4.6]; yd = 1.2
        hd = [T(r"\textbf{" + t + "}", sc=0.78, color=c).move_to([x, 2.5, 0]) for t, c, x in [("Traction", BLEU, X[0]), ("Cisaillement", VERT, X[1]), ("Torsion", ORANGE, X[2])]]
        # traction
        bar = Rectangle(width=2.0, height=0.42, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.15).move_to([X[0], yd, 0])
        fa = fleche((X[0] - 1.0, yd), (X[0] - 1.75, yd), col=ROUGE); fb = fleche((X[0] + 1.0, yd), (X[0] + 1.75, yd), col=ROUGE)
        la = M(r"N", sc=0.65, color=ROUGE).next_to(fa, UP, buff=0.08); lb_ = M(r"N", sc=0.65, color=ROUGE).next_to(fb, UP, buff=0.08)
        s1 = M(r"\sigma = \dfrac{N}{S}", sc=0.9, color=BLEU).move_to([X[0], -0.35, 0])
        u1 = T(r"contrainte uniforme", sc=0.6, color=GRIS).move_to([X[0], -1.25, 0])
        self.at(self.t("c1"), Ecrire(hd[0], rt=0.5), Create(bar), GrowArrow(fa), GrowArrow(fb), FadeIn(la), FadeIn(lb_), run_time=0.9)
        self.ecr(self.a("c1", "la contrainte est uniforme"), u1, rt=0.6)
        self.ecr(self.a("c1", "sigma égale"), s1, rt=0.6)
        # cisaillement : axe dans une chape
        jo = VGroup(*[Rectangle(width=0.28, height=1.0, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.12).move_to([s*0.62, yd, 0]) for s in (-1, 1)])
        oe = Rectangle(width=0.36, height=1.0, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.12).move_to([0, yd, 0])
        ax_ = Rectangle(width=1.9, height=0.26, color=BLEU, stroke_width=3).set_fill(BLEU, 0.45).move_to([0, yd, 0])
        fF = fleche((0, yd - 0.5), (0, yd - 1.0), col=ROUGE, tl=0.15); lF = M(r"F", sc=0.6, color=ROUGE).next_to(fF, RIGHT, buff=0.08)
        fu = [fleche((s*0.62, yd + 0.5), (s*0.62, yd + 0.9), col=ROUGE, tl=0.14) for s in (-1, 1)]
        lu = [M(r"F/2", sc=0.55, color=ROUGE).next_to(fu[0], LEFT, buff=0.08), M(r"F/2", sc=0.55, color=ROUGE).next_to(fu[1], RIGHT, buff=0.08)]
        s2 = M(r"\tau_{moy} = \dfrac{T}{S}", sc=0.9, color=VERT).move_to([X[1], -0.35, 0])
        self.at(self.t("c2"), Ecrire(hd[1], rt=0.5), Create(jo), Create(oe), Create(ax_), run_time=0.9)
        self.ecr(self.a("c2", "une contrainte moyenne"), s2, rt=0.7)
        pl = [DashedLine([s*0.33, yd - 0.3, 0], [s*0.33, yd + 0.3, 0], color=ROUGE, stroke_width=4) for s in (-1, 1)]
        d2 = T(r"chape : \textbf{deux} sections", sc=0.62, color=ROUGE).move_to([X[1], -1.25, 0])
        d3 = M(r"T = F/2", sc=0.8, color=ROUGE).move_to([X[1], -1.9, 0])
        self.at(self.t("c3"), GrowArrow(fF), FadeIn(lF), *[GrowArrow(f) for f in fu], *[FadeIn(l) for l in lu], run_time=0.8)
        self.at(self.a("c3", "coupé en deux sections"), *[Create(p) for p in pl], Ecrire(d2, rt=0.6), run_time=0.7)
        self.ecr(self.a("c3", "la moitié"), d3, rt=0.5)
        # torsion
        cx = X[2]; R_ = 0.75
        dq = Circle(radius=R_, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.12).move_to([cx, yd, 0])
        ry = Line([cx, yd, 0], [cx + R_, yd, 0], color=GRIS, stroke_width=2)
        ft_ = [fleche((cx + r, yd), (cx + r, yd + 0.95*r), col=ORANGE, sw=3, tl=0.12) for r in (0.25, 0.5, 0.75)]
        env = DashedLine([cx, yd, 0], [cx + R_, yd + 0.95*R_, 0], color=ORANGE, stroke_width=2)
        cp = couple(cx, yd, 0.98, 2.4, 1.5, col=ORANGE); lc = M(r"M_t", sc=0.6, color=ORANGE).move_to([cx - 1.35, yd + 0.6, 0])
        s3 = M(r"\tau(r) = \dfrac{M_t\,r}{I_0}", sc=0.9, color=ORANGE).move_to([X[2], -0.35, 0])
        self.at(self.t("c4"), Ecrire(hd[2], rt=0.5), Create(dq), Create(cp), FadeIn(lc), run_time=0.9)
        self.at(self.a("c4", "croît linéairement"), Create(ry), *[GrowArrow(f) for f in ft_], Create(env), run_time=1.0)
        self.ecr(self.a("c4", "tau égale"), s3, rt=0.8)
        tm = M(r"\tau_{max} = \dfrac{16\,M_t}{\pi D^3}", sc=0.85, color=JAUNE).move_to([X[2], -1.62, 0])
        lm = M(r"\tau_{max}", sc=0.55, color=ORANGE).next_to(ft_[2].get_end(), RIGHT, buff=0.08)
        self.at(self.t("c5"), FadeIn(lm), Indicate(ft_[2], color=JAUNE), run_time=0.6)
        self.ecr(self.a("c5", "Pour un arbre plein"), tm, rt=0.9); self.play(Create(enc(tm, col=JAUNE, buff=0.12)), run_time=0.4)
        pw = M(r"M_t = \dfrac{P}{\omega}", sc=0.8).move_to([X[2], -2.82, 0])
        pu = T(r"$\omega$ en rad/s", sc=0.58, color=GRIS).move_to([X[2], -3.55, 0])
        self.ecr(self.t("c6"), pw, rt=0.7); self.ecr(self.a("c6", "avec oméga"), pu, rt=0.5)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"2.3 -- La flexion", "Cours")
        xs, h, k = -4.2, 1.4, 0.9
        sec = Line([xs, -h, 0], [xs, h, 0], color=CRAIE, stroke_width=5)
        ay = fleche((xs, h), (xs, h + 0.6), col=GRIS, sw=3, tl=0.13); ly = M(r"y", sc=0.6, color=GRIS).next_to(ay.get_end(), RIGHT, buff=0.08)
        ys = np.linspace(-h, h, 8)
        fl_ = VGroup(*[fleche((xs, y), (xs - k*y, y), col=(BLEU if y > 0 else ROUGE), sw=3, tl=0.12) for y in ys])
        env = Line([xs - k*h, h, 0], [xs + k*h, -h, 0], color=GRIS, stroke_width=2)
        self.at(self.t("d1"), Create(sec), GrowArrow(ay), FadeIn(ly), run_time=0.6)
        self.at(self.a("d1", "varie linéairement"), *[GrowArrow(f) for f in fl_], Create(env), run_time=1.2)
        fo = pos(M(r"\sigma = -\,\frac{M_{fz}}{I_{Gz}}\;y", sc=1.0, color=JAUNE), -0.9, 2.05)
        self.ecr(self.t("d2"), fo, rt=1.0); self.play(Create(enc(fo, col=JAUNE, buff=0.15)), run_time=0.4)
        an = DashedLine([xs - 1.8, 0, 0], [xs + 1.5, 0, 0], color=GRIS, stroke_width=2)
        g = Dot([xs, 0, 0], color=JAUNE, radius=0.07); lg = M(r"G", sc=0.6, color=JAUNE).move_to([xs - 0.32, -0.26, 0])
        la = T(r"axe neutre", sc=0.55, color=GRIS).move_to([xs - 1.25, -0.26, 0])
        t1 = pos(T(r"nulle sur l'\textbf{axe neutre}, qui passe par $G$", sc=0.7), -0.9, 0.95)
        self.at(self.a("d2", "Elle s'annule"), Create(an), FadeIn(g), FadeIn(lg), FadeIn(la), Ecrire(t1, rt=1.0), run_time=1.0)
        cp = couple(-2.2, 0.35, 0.42, -1.6, 3.4, col=VERT); lc = M(r"M_{fz} > 0", sc=0.6, color=VERT).move_to([-2.2, 1.12, 0])
        lco = T(r"compression", sc=0.58, color=BLEU).move_to([xs - 1.0, h + 0.36, 0])
        ltr = T(r"traction", sc=0.58, color=ROUGE).move_to([xs + 0.75, -h - 0.38, 0])
        t2 = pos(T(r"$M_{fz} > 0$ : côté $y > 0$ \textbf{comprimé}, l'autre \textbf{tendu}", sc=0.7), -0.9, 0.3)
        self.at(self.t("d3"), Create(cp), FadeIn(lc), run_time=0.6)
        self.at(self.a("d3", "comprime le côté"), FadeIn(lco), FadeIn(ltr), Ecrire(t2, rt=1.1), run_time=1.1)
        # poutre fléchie
        hb = 0.32
        f_haut = ArcBetweenPoints(P(1.0, -0.62), P(4.8, -0.62), angle=-0.35, color=BLEU, stroke_width=4)
        f_bas = ArcBetweenPoints(P(1.0, -0.62 - hb), P(4.8, -0.62 - hb), angle=-0.35, color=ROUGE, stroke_width=4)
        bo = VGroup(Line(P(1.0, -0.62), P(1.0, -0.62 - hb), color=CRAIE, stroke_width=3), Line(P(4.8, -0.62), P(4.8, -0.62 - hb), color=CRAIE, stroke_width=3))
        l1 = T(r"raccourcie", sc=0.55, color=BLEU).move_to([5.75, -0.55, 0]); l2 = T(r"allongée", sc=0.55, color=ROUGE).move_to([5.7, -0.97, 0])
        self.at(self.a("d4", "une poutre qui fléchit"), Create(f_haut), Create(f_bas), Create(bo), run_time=0.9)
        self.at(self.a("d4", "raccourcit"), FadeIn(l1), run_time=0.4)
        self.at(self.a("d4", "s'allonge"), FadeIn(l2), run_time=0.4)
        vv = DoubleArrow([xs + 0.45, 0, 0], [xs + 0.45, h, 0], buff=0, color=VERT, stroke_width=2.5, tip_length=0.13, max_tip_length_to_length_ratio=0.2)
        lv = M(r"v", sc=0.65, color=VERT).next_to(vv, RIGHT, buff=0.08)
        sm = pos(M(r"\sigma_{max} = \frac{|M_{fz}|\,v}{I_{Gz}} = \frac{|M_{fz}|}{I_{Gz}/v}", sc=0.95, color=VERT), -0.9, -2.2)
        self.at(self.t("d5"), Create(vv), FadeIn(lv), run_time=0.6)
        self.ecr(self.a("d5", "sigma max"), sm, rt=1.2); self.play(Create(enc(sm, col=VERT, buff=0.15)), run_time=0.4)
        pc = pos(T(r"point critique : la fibre la plus éloignée", sc=0.7, color=ROUGE), -0.9, -3.4)
        self.at(self.t("d6"), Indicate(fl_[0], color=ROUGE, scale_factor=1.3), Indicate(fl_[-1], color=ROUGE, scale_factor=1.3), Ecrire(pc, rt=0.9), run_time=1.0)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"2.4 -- Le critère de résistance", "Cours")
        t1 = pos(T(r"jamais à $R_e$ : un coefficient de sécurité $s > 1$", sc=0.72), -6.3, 2.1)
        self.ecr(self.t("e1"), t1, rt=1.0)
        # courbe de traction
        ax, fr = cadre(4.05, 0.75, 4.6, 3.0, 0, 1, 0, 1.25)
        eps = np.linspace(0, 1, 120); sig = np.where(eps < 0.15, eps/0.15*0.75, 0.75 + 0.27*(1 - np.exp(-(eps - 0.15)/0.3)))
        cb = VMobject(color=BLEU, stroke_width=4).set_points_as_corners([ax.c2p(a, b) for a, b in zip(eps, sig)])
        le = DashedLine(ax.c2p(0, 0.75), ax.c2p(1, 0.75), color=ROUGE, stroke_width=2); lre = M(r"R_e", sc=0.6, color=ROUGE).next_to(ax.c2p(1, 0.75), DOWN, buff=0.08).shift(0.35*LEFT)
        lsg = M(r"\sigma", sc=0.6, color=GRIS).move_to(ax.c2p(0.06, 1.13)); lep = M(r"\varepsilon", sc=0.6, color=GRIS).move_to(ax.c2p(0.95, 0.09))
        self.at(self.a("e1", "On ne travaille jamais"), Create(fr), Create(cb), Create(le), FadeIn(lre), FadeIn(lsg), FadeIn(lep), run_time=1.2)
        zp = Polygon(ax.c2p(0, 0), ax.c2p(1, 0), ax.c2p(1, 0.42), ax.c2p(0, 0.42), stroke_width=0).set_fill(VERT, 0.18)
        lp = DashedLine(ax.c2p(0, 0.42), ax.c2p(1, 0.42), color=VERT, stroke_width=2.5)
        lrp = M(r"R_{pe} = R_e/s", sc=0.6, color=VERT).next_to(ax.c2p(1, 0.42), DOWN, buff=0.1).shift(0.95*LEFT)
        f2 = pos(M(r"R_{pe} = \frac{R_e}{s} \qquad \sigma_{max} \le R_{pe}", sc=0.95, color=JAUNE), -6.3, 1.0)
        self.at(self.t("e2"), FadeIn(zp), Create(lp), FadeIn(lrp), Ecrire(f2, rt=1.2), run_time=1.2)
        self.play(Create(enc(f2, col=JAUNE, buff=0.15)), run_time=0.4)
        f3 = pos(M(r"\tau_{max} \le R_{pg} \qquad R_{pg} \approx 0{,}5 \text{ à } 0{,}6\,R_{pe}", sc=0.85, color=VERT), -6.3, -0.25)
        self.ecr(self.t("e3"), f3, rt=1.2)
        f4 = pos(T(r"$s \approx 1{,}5$ : pièce bien connue \;;\; $s \geq 5$ : levage", sc=0.7), -6.3, -1.2)
        self.ecr(self.t("e4"), f4, rt=1.0)
        hp = pos(T(r"\textit{Hors programme} : près d'une gorge, d'un épaulement,", sc=0.64, color=GRIS), -6.3, -2.1)
        hp2 = pos(M(r"\sigma_{\text{réelle}} = K_t\,\sigma_{\text{nom}} \quad (K_t \approx 1{,}5 \text{ à } 3, \text{ fourni par le sujet})", sc=0.66, color=GRIS), -6.3, -2.7)
        self.ecr(self.t("e5"), hp, rt=1.0); self.ecr(self.a("e5", "multipliée par"), hp2, rt=1.1)
        ex = T(r"\textbf{Place aux exercices !}", sc=0.85, color=JAUNE).move_to([0, -3.5, 0])
        self.ecr(self.a("e6", "place aux exercices"), ex, rt=0.6)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"Exercice 1 -- une suspente et son axe", "Énoncé")
        cx = -4.8
        ch = bati(cx - 1.5, cx + 1.5, 2.2, 2.55)
        jo, oe, axe, top = chape(cx, 1.55, k=1.0)
        tg = Line([cx, 1.24, 0], [cx, -2.3, 0], color=CRAIE, stroke_width=10)
        fN = fleche((cx, -2.3), (cx, -3.2)); lN = T(r"$N = 30$ kN", sc=0.62, color=ROUGE).next_to(fN, RIGHT, buff=0.12)
        lch = T("chape", sc=0.55, color=GRIS).next_to(jo[0], LEFT, buff=0.22); lax = T("axe", sc=0.55, color=BLEU).next_to(axe, RIGHT, buff=0.1)
        ltg = T("tige", sc=0.55, color=GRIS).move_to([cx + 0.55, 0.1, 0])
        self.at(self.t("f1"), Create(ch), Create(tg), FadeIn(ltg), run_time=1.0)
        d1 = pos(T(r"trémie suspendue par \textbf{4 tiges rondes} en acier", sc=0.72), -2.4, 2.25)
        self.ecr(self.a("f1", "Une trémie"), d1, rt=1.0)
        d2 = pos(T(r"chaque tige tendue : $N = 30$ kN", sc=0.72), -2.4, 1.6)
        self.at(self.t("f2"), GrowArrow(fN), FadeIn(lN), Ecrire(d2, rt=0.9), run_time=0.9)
        self.at(self.a("f2", "son œil est articulé"), Create(jo), Create(oe), FadeIn(lch), run_time=0.8)
        self.at(self.a("f2", "par un axe"), Create(axe), FadeIn(lax), run_time=0.5)
        d3 = pos(T(r"acier : $R_e = 355$ MPa, \; $s = 2{,}5$, \; $R_{pg} = R_{pe}/2$", sc=0.72), -2.4, 0.95)
        self.ecr(self.t("f3"), d3, rt=1.2)
        d4 = pos(T(r"diamètres normalisés : 16, 18, 20, 22, 25 mm", sc=0.66, color=GRIS), -2.4, 0.3)
        q = T(r"Diamètre de la tige ? \quad Diamètre de l'axe ?", sc=0.8, color=ROUGE).move_to([1.7, -0.75, 0])
        self.ecr(self.a("f4", "Question"), d4, rt=0.8)
        self.ecr(self.a("f4", "quels diamètres"), q, rt=1.0); self.play(Create(enc(q)), run_time=0.4)
        rf = pos(T(r"Réfléchissons : tige \textbf{tendue} ; axe \textbf{cisaillé}, sur combien de sections ?", sc=0.6, color=BLEU), -2.4, -1.95)
        self.ecr(self.t("f5"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([1.0, -3.05, 0])
        self.ecr(self.t("f6"), av, rt=0.7)
        pa, arc = chrono(4.3, -3.05)
        self.at(self.PH["f6"]["fin"], FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"Exercice 1 -- la solution", "Solution")
        rap = pos(T(r"$N = 30$ kN \; ; \; $R_e = 355$ MPa, \; $s = 2{,}5$", sc=0.56, color=GRIS), 6.6, 2.72, bord=RIGHT)
        self.play(FadeIn(rap), run_time=0.4)
        def etape(k, c, y, m, t, rt=1.0):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        m1 = etape(1, BLEU, 2.25, M(r"R_{pe} = 355/2{,}5 = 142\ \mathrm{MPa}", sc=0.72), self.a("g1", "R p e égale"))
        m1b = M(r"R_{pg} = 71\ \mathrm{MPa}", sc=0.72).next_to(m1, RIGHT, buff=0.5)
        self.ecr(self.t("g1b"), m1b, rt=0.6)
        etape(2, VERT, 1.4, M(r"\text{tige : } N/S \le R_{pe}", sc=0.72), self.a("g2", "la tige"), rt=0.8)
        m3 = pos(M(r"S \ge 30\,000/142 \approx 211\ \mathrm{mm^2} \;\Rightarrow\; d \ge 16{,}4\ \mathrm{mm}", sc=0.72), -5.85, 0.78)
        self.ecr(self.t("g3"), m3, rt=1.3)
        m4 = pos(T(r"$16$ mm : $\sigma \approx 149$ MPa $> R_{pe}$ : refusé", sc=0.62, color=ROUGE), -5.85, 0.2)
        self.ecr(self.a("g4", "Avec seize"), m4, rt=0.9)
        m5 = pos(M(r"\text{tige : } d = 18\ \mathrm{mm}, \;\; \sigma \approx 118\ \mathrm{MPa}", sc=0.75, color=VERT), -5.85, -0.42)
        self.ecr(self.t("g5"), m5, rt=0.9); self.play(Create(enc(m5, col=VERT, buff=0.12)), run_time=0.4)
        # chape agrandie : deux sections cisaillées
        cx = 4.5
        cy = 1.1
        jo, oe, axe, top = chape(cx, cy, k=1.45)
        ch = bati(cx - 1.55, cx + 1.55, top, top + 0.3)
        tg = Line([cx, cy - 0.45, 0], [cx, 0.25, 0], color=CRAIE, stroke_width=10)
        fN = fleche((cx, 0.25), (cx, -0.3), tl=0.15); lN = M(r"N", sc=0.6, color=ROUGE).next_to(fN, RIGHT, buff=0.08)
        self.at(self.t("g6"), Create(ch), Create(jo), Create(oe), Create(tg), GrowArrow(fN), FadeIn(lN), run_time=1.0)
        self.at(self.a("g6", "l'axe traverse"), Create(axe), run_time=0.6)
        pl = [DashedLine([cx + s*0.5*(0.35*1.45 + 0.22*1.45), cy - 0.3, 0], [cx + s*0.5*(0.35*1.45 + 0.22*1.45), cy + 0.3, 0], color=ROUGE, stroke_width=5) for s in (-1, 1)]
        lpl = T(r"2 sections cisaillées", sc=0.58, color=ROUGE).move_to([cx, -0.62, 0])
        self.at(self.t("g7"), *[Create(p) for p in pl], FadeIn(lpl), run_time=0.7)
        m6 = etape(3, ORANGE, -1.22, M(r"\text{axe : double cisaillement, } T = N/2 = 15\ \mathrm{kN}", sc=0.72), self.a("g7", "C'est du double cisaillement"), rt=1.2)
        m7 = pos(M(r"T/S \le R_{pg} \;\Rightarrow\; S \ge 15\,000/71 \approx 211\ \mathrm{mm^2}", sc=0.72), -5.85, -1.85)
        self.ecr(self.t("g8"), m7, rt=1.2)
        m7b = pos(T(r"même section que la tige !", sc=0.6, color=GRIS), -5.85, -2.42)
        self.ecr(self.t("g8b"), m7b, rt=0.7)
        m8 = pos(M(r"\text{axe : } d = 18\ \mathrm{mm}, \;\; \tau \approx 59\ \mathrm{MPa}", sc=0.75, color=VERT), -5.85, -3.1)
        self.ecr(self.t("g9"), m8, rt=0.9); self.play(Create(enc(m8, col=VERT, buff=0.12)), run_time=0.4)
        # vérifications
        ca4 = carte(4, JAUNE, 2.3, -1.2)
        v1 = pos(T(r"porte-à-faux : $T = 30$ kN", sc=0.6), 2.8, -1.2)
        self.at(self.t("g10"), Create(ca4[0]), FadeIn(ca4[1]), Ecrire(v1, rt=0.9), run_time=0.9)
        v2 = pos(M(r"d \ge 23{,}2\ \mathrm{mm} \;\to\; 25\ \mathrm{mm}", sc=0.7), 2.8, -1.8)
        self.ecr(self.a("g10", "il faudrait"), v2, rt=0.8)
        v3 = pos(T(r"chape : diamètre divisé par $\sqrt{2}$", sc=0.6, color=JAUNE), 2.8, -2.4)
        self.ecr(self.t("g11"), v3, rt=0.8)
        v4 = pos(T(r"$118$ MPa $\approx R_e/3$ : raisonnable", sc=0.6, color=VERT), 2.8, -3.1)
        self.ecr(self.t("g12"), v4, rt=0.8)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"Exercice 2 -- un arbre en torsion", "Énoncé")
        y = 1.75
        mo = Rectangle(width=1.4, height=1.0, color=CRAIE, stroke_width=3).move_to([-5.6, y, 0]); lmo = T("moteur", sc=0.5).move_to(mo)
        ar = Rectangle(width=4.8, height=0.32, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.15).move_to([-2.5, y, 0])
        re_ = Rectangle(width=1.4, height=1.0, color=CRAIE, stroke_width=3).move_to([0.6, y, 0]); lre = T("récepteur", sc=0.46).move_to(re_)
        el = Arc(radius=0.42, start_angle=0.6, angle=4.6, color=ORANGE, stroke_width=3).add_tip(tip_length=0.15, tip_width=0.15).stretch(0.35, 0).move_to([-2.5, y, 0])
        lmt = M(r"M_t", sc=0.65, color=ORANGE).move_to([-2.5, y + 0.75, 0])
        self.at(self.t("h1"), Create(mo), FadeIn(lmo), Create(ar), Create(re_), FadeIn(lre), run_time=1.0)
        self.at(self.a("h1", "la torsion"), Create(el), FadeIn(lmt), run_time=0.7)
        d1 = pos(T(r"$P = 12$ kW", sc=0.72), 2.4, 2.3); d2 = pos(T(r"$955$ tr/min", sc=0.72), 2.4, 1.7)
        d3 = pos(T(r"$R_{pg} = 50$ MPa", sc=0.72), 2.4, 1.1)
        self.ecr(self.a("h2", "une puissance"), d1, rt=0.6); self.ecr(self.a("h2", "tours par minute"), d2, rt=0.6)
        self.ecr(self.a("h2", "La résistance pratique"), d3, rt=0.6)
        q1 = pos(T(r"Q1. Diamètre minimal $D$ d'un arbre plein (au mm supérieur) ?", sc=0.7), -6.2, 0.0)
        self.ecr(self.t("h3"), q1, rt=1.1)
        q2 = pos(T(r"Q2. Tube $30/18$ mm, de même masse : $\tau_{max}$ ?", sc=0.7), -6.2, -0.75)
        dp = Circle(radius=0.44, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.2).move_to([4.55, -0.4, 0])
        tb = Annulus(inner_radius=0.33, outer_radius=0.55, color=CRAIE, stroke_width=3, fill_opacity=0.2).move_to([6.0, -0.4, 0])
        ldp = T(r"$D$ ?", sc=0.55).next_to(dp, DOWN, buff=0.1); ltb = T(r"$30/18$", sc=0.55).next_to(tb, DOWN, buff=0.1)
        self.at(self.t("h4"), Ecrire(q2, rt=1.0), Create(dp), FadeIn(ldp), run_time=1.0)
        self.at(self.a("h4", "de même masse"), Create(tb), FadeIn(ltb), run_time=0.6)
        bx = SurroundingRectangle(VGroup(q1, q2), color=ROUGE, buff=0.18, corner_radius=0.08)
        self.play(Create(bx), run_time=0.4)
        rf = pos(T(r"Réfléchissons : le \textbf{couple} d'abord, puis $\tau$ à la \textbf{périphérie}", sc=0.68, color=BLEU), -6.2, -1.95)
        self.ecr(self.t("h5"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-1.0, -3.05, 0])
        self.ecr(self.t("h6"), av, rt=0.7)
        pa, arc = chrono(2.3, -3.05)
        self.at(self.PH["h6"]["fin"], FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"Exercice 2 -- la solution", "Solution")
        rap = pos(T(r"$P = 12$ kW, \; $955$ tr/min, \; $R_{pg} = 50$ MPa", sc=0.56, color=GRIS), 6.6, 2.72, bord=RIGHT)
        self.play(FadeIn(rap), run_time=0.4)
        def etape(k, c, y, m, t, rt=1.0):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        etape(1, BLEU, 2.25, M(r"\omega = \pi \times 955/30 \approx 100\ \mathrm{rad/s}", sc=0.72), self.a("i1", "On convertit"), rt=1.0)
        m2 = pos(M(r"M_t = P/\omega = 120\ \mathrm{N\,m} = 1{,}2\cdot 10^5\ \mathrm{N\,mm}", sc=0.72), -5.85, 1.62)
        self.ecr(self.t("i2"), m2, rt=1.2)
        etape(2, VERT, 0.82, M(r"\text{plein : } \frac{16\,M_t}{\pi D^3} \le R_{pg}", sc=0.72), self.a("i3", "On écrit le critère"), rt=1.0)
        m4 = pos(M(r"D^3 \ge 12\,200\ \mathrm{mm^3} \;\Rightarrow\; D \ge 23{,}0\ \mathrm{mm}", sc=0.72), -5.85, 0.08)
        self.ecr(self.t("i4"), m4, rt=1.1)
        m5 = pos(M(r"D = 24\ \mathrm{mm}, \;\; \tau_{max} \approx 44\ \mathrm{MPa}", sc=0.75, color=VERT), -5.85, -0.55)
        self.ecr(self.t("i5"), m5, rt=0.9); self.play(Create(enc(m5, col=VERT, buff=0.12)), run_time=0.4)
        # tube : contrainte linéaire en r
        cx, cy, Re_, Ri = 4.4, 1.0, 1.0, 0.6
        tb = Annulus(inner_radius=Ri, outer_radius=Re_, color=CRAIE, stroke_width=3, fill_opacity=0.2).move_to([cx, cy, 0])
        self.at(self.a("i6", "le tube"), Create(tb), run_time=0.7)
        etape(3, ORANGE, -1.42, M(r"\text{tube : } I_0 = \frac{\pi(30^4 - 18^4)}{32} \approx 69\,200\ \mathrm{mm^4}", sc=0.72), self.a("i6", "Son moment polaire"), rt=1.3)
        m7 = pos(T(r"piège : $R = 15$ mm, le rayon extérieur (pas $30$ !)", sc=0.62, color=ROUGE), -5.85, -2.2)
        self.ecr(self.a("i7", "R est le rayon"), m7, rt=1.0)
        rs = np.linspace(Ri, Re_, 4); kk = 1.0
        ft_ = VGroup(*[fleche((cx + r, cy), (cx + r, cy + kk*r), col=ORANGE, sw=3, tl=0.1) for r in rs])
        en = DashedLine([cx, cy, 0], [cx + Re_, cy + kk*Re_, 0], color=GRIS, stroke_width=2)
        l26 = T(r"$26$ MPa", sc=0.55, color=VERT).next_to(ft_[-1].get_end(), RIGHT, buff=0.08)
        m8 = pos(M(r"\tau_{max} = \frac{M_t\,R}{I_0} = \frac{1{,}2\cdot10^5 \times 15}{69\,200} \approx 26\ \mathrm{MPa}", sc=0.72, color=VERT), -5.85, -2.98)
        self.at(self.t("i8"), *[GrowArrow(f) for f in ft_], Create(en), Ecrire(m8, rt=1.3), run_time=1.3)
        self.play(Create(enc(m8, col=VERT, buff=0.12)), FadeIn(l26), run_time=0.4)
        l16 = T(r"bord du trou : $16$ MPa", sc=0.55, color=GRIS).move_to([cx, cy - Re_ - 0.22, 0])
        self.at(self.t("i9"), Indicate(ft_[0], color=JAUNE, scale_factor=1.4), FadeIn(l16), run_time=0.7)
        ca4 = carte(4, JAUNE, 1.75, -0.72)
        v1 = pos(M(r"30^2 - 18^2 = 576 = 24^2", sc=0.72), 2.25, -0.72)
        self.at(self.t("i10"), Create(ca4[0]), FadeIn(ca4[1]), Ecrire(v1, rt=1.0), run_time=1.0)
        v2 = pos(T(r"même section, même masse", sc=0.62, color=GRIS), 2.25, -1.32)
        self.ecr(self.a("i10", "Même section"), v2, rt=0.7)
        cc = VGroup(T(r"à masse égale :", sc=0.66, color=JAUNE), T(r"\textbf{1,7 fois} moins de contrainte", sc=0.66, color=JAUNE)).arrange(DOWN, buff=0.12).move_to([4.4, -2.35, 0])
        self.ecr(self.t("i11"), cc, rt=1.0); self.play(Create(enc(cc, col=JAUNE, buff=0.14)), run_time=0.4)
        self.fin()

def poutre3(self, xa, xb, y, sc_lab=0.6, avec_cotes=True, fy=1.0):
    """poutre AB sur pivot et appui simple, deux forces en C et D (à L/4 des appuis)"""
    L = xb - xa; xc, xd = xa + L/4, xb - L/4
    pt = poutre(xa, xb, y); pa = pivot(xa, y - 0.06); pb = glissant(xb, y - 0.06)
    fs = [fleche((x, y + fy), (x, y + 0.08), tl=0.17) for x in (xc, xd)]
    lf = [T(r"$6$ kN", sc=sc_lab, color=ROUGE).next_to(f, RIGHT, buff=0.08).shift(0.15*UP) for f in fs]
    lab = [T(r"$%s$" % n, sc=sc_lab).move_to([x, y + 0.32, 0]) for n, x in (("A", xa - 0.22), ("B", xb + 0.22))]
    lab += [T(r"$%s$" % n, sc=sc_lab).move_to([x - 0.25, y + 0.3, 0]) for n, x in (("C", xc), ("D", xd))]
    cotes = VGroup(cote(xa, xc, y - 0.95, r"$0{,}5$ m"), cote(xc, xd, y - 0.95, r"$1$ m"), cote(xd, xb, y - 0.95, r"$0{,}5$ m")) if avec_cotes else VGroup()
    return dict(pt=pt, pa=pa, pb=pb, fs=fs, lf=lf, lab=lab, cotes=cotes, xc=xc, xd=xd)

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"Exercice 3 -- une poutre en flexion", "Énoncé")
        xa, xb, y = -5.0, 1.4, 1.45
        p = poutre3(self, xa, xb, y)
        rp = repere(-6.55, 0.35)
        self.at(self.t("j1"), Create(p["pt"]), FadeIn(rp), run_time=0.8)
        self.at(self.a("j2", "un pivot en A"), Create(p["pa"]), FadeIn(p["lab"][0]), run_time=0.6)
        self.at(self.a("j2", "un appui simple"), Create(p["pb"]), FadeIn(p["lab"][1]), run_time=0.6)
        self.at(self.t("j3"), *[GrowArrow(f) for f in p["fs"]], *[FadeIn(l) for l in p["lf"] + p["lab"][2:]], run_time=0.9)
        self.at(self.a("j3", "à cinquante centimètres"), Create(p["cotes"]), run_time=0.8)
        # sections possibles
        de = Rectangle(width=0.34, height=0.9, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.2).move_to([3.4, 1.45, 0])
        co = Rectangle(width=0.9, height=0.34, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.2).move_to([5.4, 1.45, 0])
        lde = T("debout", sc=0.55).move_to([3.4, 0.68, 0]); lco = T("couché", sc=0.55).move_to([5.4, 0.68, 0])
        fy_ = [fleche((x, 2.55), (x, 2.05), col=GRIS, sw=3, tl=0.12) for x in (3.4, 5.4)]
        d1 = pos(T(r"plat d'acier $30 \times 80$ mm \; (poids propre négligé)", sc=0.7), -6.2, -0.4)
        self.at(self.t("j4"), Create(de), Create(co), FadeIn(lde), FadeIn(lco), *[GrowArrow(f) for f in fy_], Ecrire(d1, rt=1.0), run_time=1.0)
        d2 = pos(T(r"acier : $R_e = 235$ MPa, \; $s = 1{,}5$", sc=0.7), -6.2, -1.0)
        self.ecr(self.t("j4b"), d2, rt=0.9)
        q = T(r"Plat debout ou couché ? \quad Critère de résistance vérifié ?", sc=0.78, color=ROUGE).move_to([0, -1.95, 0])
        self.ecr(self.t("j5"), q, rt=1.1); self.play(Create(enc(q)), run_time=0.4)
        rf = T(r"Réfléchissons : diagrammes $\to |M_{fz}|_{max}$, puis $\sigma$ sur la fibre la plus éloignée", sc=0.64, color=BLEU).move_to([0, -2.9, 0])
        self.ecr(self.t("j6"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-1.0, -3.6, 0])
        self.ecr(self.t("j7"), av, rt=0.7)
        pa, arc = chrono(2.3, -3.6)
        self.at(self.PH["j7"]["fin"], FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"Exercice 3 -- les diagrammes", "Solution")
        xa, xb, yb = -0.4, 6.0, 2.2
        p = poutre3(self, xa, xb, yb, sc_lab=0.55, avec_cotes=False, fy=0.62)
        self.play(Create(p["pt"]), Create(p["pa"]), Create(p["pb"]), *[GrowArrow(f) for f in p["fs"]], *[FadeIn(l) for l in p["lf"] + p["lab"]], run_time=0.8)
        def etape(k, c, y, m, t, rt=0.9):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        ya = [T(r"$Y_A$", sc=0.55, color=VERT).move_to([xa - 0.62, yb - 0.3, 0]), T(r"$Y_B$", sc=0.55, color=VERT).move_to([xb + 0.62, yb - 0.3, 0])]
        etape(1, BLEU, 2.3, M(r"Y_A = Y_B = 6\ \mathrm{kN} \;\; (\text{symétrie})", sc=0.66), self.a("k1", "Tout est symétrique"))
        self.play(*[FadeIn(l) for l in ya], run_time=0.4)
        k2 = pos(T(r"section critique : $|M_{fz}|$ maximal", sc=0.6, color=GRIS), -5.85, 1.72)
        self.ecr(self.t("k2"), k2, rt=0.8)
        # cadres alignés sur la poutre (x en m : A = 0, B = 2)
        sx = (xb - xa)/2.0; x0 = xa - 0.4; x1 = xb + 0.4; w = x1 - x0; xm = (x0 + x1)/2
        l0, l1 = (x0 - xa)/sx, (x1 - xa)/sx
        aT, fT = cadre(xm, 0.42, w, 1.7, l0, l1, -8.5, 8.5); aM, fM = cadre(xm, -1.85, w, 2.0, l0, l1, -0.6, 4.0)
        zT = DashedLine(aT.c2p(l0, 0), aT.c2p(l1, 0), color=GRIS, stroke_width=1.5); zM = DashedLine(aM.c2p(l0, 0), aM.c2p(l1, 0), color=GRIS, stroke_width=1.5)
        gT = M(r"T_y\ (\mathrm{kN})", sc=0.55, color=ORANGE).move_to(aT.c2p(l0, 0) + np.array([0.75, 0.55, 0]))
        gM = M(r"M_{fz}\ (\mathrm{kN\,m})", sc=0.55, color=BLEU).move_to(aM.c2p(l0, 3.3) + np.array([0.9, 0, 0]))
        gu = [DashedLine([x, yb - 0.1, 0], [x, -2.85, 0], color=GRIS, stroke_width=1.2, stroke_opacity=0.6) for x in (p["xc"], p["xd"])]
        self.at(self.t("k3"), Create(fT), Create(fM), Create(zT), Create(zM), FadeIn(gT), FadeIn(gM), *[Create(g) for g in gu], run_time=0.9)
        etape(2, ORANGE, 1.0, M(r"\text{AC : } T_y = -Y_A = -6\ \mathrm{kN}", sc=0.66), self.a("k3", "on isole la partie gauche"))
        t1 = lig(aT, [(0, 0), (0, -6), (0.5, -6)], col=ORANGE)
        lt1 = T(r"$-6$", sc=0.55, color=ORANGE).move_to(aT.c2p(0.25, -3.3))
        self.at(self.a("k3", "moins six"), Create(t1), FadeIn(lt1), run_time=0.6)
        k4 = pos(M(r"\text{en C : saut de } +6\ \mathrm{kN}", sc=0.66), -5.85, 0.42)
        k4b = pos(M(r"\text{CD : } T_y = 0", sc=0.66), -5.85, -0.12)
        t2 = lig(aT, [(0.5, -6), (0.5, 0), (1.5, 0)], col=ORANGE)
        self.at(self.t("k4"), Ecrire(k4, rt=0.8), Create(t2), run_time=0.9)
        self.ecr(self.a("k4", "Entre C et D"), k4b, rt=0.6)
        k5 = pos(M(r"\text{DB : } T_y = +6\ \mathrm{kN}", sc=0.66), -5.85, -0.66)
        t3 = lig(aT, [(1.5, 0), (1.5, 6), (2, 6), (2, 0)], col=ORANGE)
        lt3 = T(r"$+6$", sc=0.55, color=ORANGE).move_to(aT.c2p(1.75, 3.3))
        self.at(self.t("k5"), Ecrire(k5, rt=0.7), Create(t3), FadeIn(lt3), run_time=0.9)
        etape(3, BLEU, -1.45, M(r"\text{AC : } M_{fz} = Y_A\,x", sc=0.66), self.a("k6", "Entre A et C"))
        m1 = lig(aM, [(0, 0), (0.5, 3)], col=BLEU)
        self.at(self.a("k6", "il croît"), Create(m1), run_time=0.7)
        k7 = pos(M(r"\text{CD : } M_{fz} \text{ constant}", sc=0.66), -5.85, -2.0)
        m2 = lig(aM, [(0.5, 3), (1.5, 3)], col=BLEU); m3 = lig(aM, [(1.5, 3), (2, 0)], col=BLEU)
        fp = T(r"flexion pure", sc=0.55, color=JAUNE).move_to(aM.c2p(1.0, 1.4))
        self.at(self.t("k7"), Ecrire(k7, rt=0.7), Create(m2), Create(m3), run_time=0.9)
        self.at(self.a("k7", "flexion pure"), FadeIn(fp), run_time=0.4)
        k7b = pos(M(r"M_{fz,max} = 6 \times 0{,}5 = 3\ \mathrm{kN\,m}", sc=0.66, color=JAUNE), -5.85, -2.6)
        l3 = T(r"$3$", sc=0.55, color=BLEU).move_to(aM.c2p(1.0, 3.7))
        self.at(self.t("k7b"), Ecrire(k7b, rt=0.9), FadeIn(l3), run_time=0.9); self.play(Create(enc(k7b, col=JAUNE, buff=0.1)), run_time=0.4)
        etape(4, VERT, -3.45, M(r"M_{fz}' = -T_y, \;\; M_{fz}(A) = M_{fz}(B) = 0", sc=0.62, color=VERT), self.a("k8", "la pente"), rt=1.0)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice 3 -- debout ou couché ?", "Solution")
        rap = pos(T(r"$M_{fz,max} = 3$ kN$\,$m \; ; \; plat $30 \times 80$ mm", sc=0.56, color=GRIS), 6.6, 2.72, bord=RIGHT)
        self.play(FadeIn(rap), run_time=0.4)
        def etape(k, c, y, m, t, rt=0.9):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        etape(4, BLEU, 2.25, M(r"R_{pe} = 235/1{,}5 \approx 157\ \mathrm{MPa}", sc=0.72), self.a("l1", "R p e égale"))
        de = Rectangle(width=0.34, height=0.9, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.2).move_to([3.1, 1.15, 0])
        co = Rectangle(width=0.9, height=0.34, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.2).move_to([3.1, -0.75, 0])
        etape(5, VERT, 1.6, T(r"\textbf{Debout} : $h = 80$ mm", sc=0.7), self.t("l2"))
        self.play(Create(de), run_time=0.4)
        l2b = pos(M(r"I_{Gz} = \frac{30 \times 80^3}{12} = 1{,}28\cdot10^6\ \mathrm{mm^4}", sc=0.68), -5.85, 0.95)
        self.ecr(self.t("l2b"), l2b, rt=1.1)
        l3 = pos(M(r"\sigma_{max} = \frac{3\cdot10^6 \times 40}{1{,}28\cdot10^6} \approx 94\ \mathrm{MPa} \le 157", sc=0.68, color=VERT), -5.85, 0.05)
        self.ecr(self.a("l3", "Avec v égale"), l3, rt=1.3); self.play(Create(enc(l3, col=VERT, buff=0.1)), run_time=0.4)
        ok = coche(4.0, 1.15)
        self.at(self.a("l3", "ça tient"), Create(ok), run_time=0.4)
        etape(6, ROUGE, -0.95, T(r"\textbf{Couché} : $h = 30$ mm", sc=0.7), self.t("l4"))
        self.play(Create(co), run_time=0.4)
        l4b = pos(M(r"I_{Gz} = \frac{80 \times 30^3}{12} = 1{,}8\cdot10^5\ \mathrm{mm^4}, \;\; v = 15", sc=0.68), -5.85, -1.6)
        self.ecr(self.t("l4b"), l4b, rt=1.1)
        l5 = pos(M(r"\sigma_{max} = 250\ \mathrm{MPa} > R_e", sc=0.75, color=ROUGE), -5.85, -2.4)
        no = croix(4.0, -0.75)
        self.at(self.t("l5"), Ecrire(l5, rt=0.8), Create(no), run_time=0.8); self.play(Create(enc(l5, col=ROUGE, buff=0.1)), run_time=0.4)
        l6 = pos(T(r"même masse, $80/30 \approx 2{,}7$ fois plus de contrainte", sc=0.62, color=GRIS), -5.85, -3.08)
        self.ecr(self.t("l6"), l6, rt=1.0)
        lcp = T(r"comprimée", sc=0.52, color=BLEU).move_to([4.45, 1.75, 0]); ltd = T(r"tendue", sc=0.52, color=ROUGE).move_to([4.25, 0.5, 0])
        fcp = Line([3.27, 1.6, 0], [3.65, 1.7, 0], color=BLEU, stroke_width=2); ftd = Line([3.27, 0.7, 0], [3.7, 0.58, 0], color=ROUGE, stroke_width=2)
        self.at(self.t("l7"), Indicate(de, color=JAUNE), run_time=0.6)
        self.at(self.a("l7", "fibre du dessous"), Create(ftd), FadeIn(ltd), run_time=0.4)
        self.at(self.a("l7", "celle du dessus"), Create(fcp), FadeIn(lcp), run_time=0.4)
        v1 = pos(T(r"$\tau_{moy} = 6000/2400 = 2{,}5$ MPa", sc=0.58), 2.3, -1.6)
        self.ecr(self.t("l8"), v1, rt=0.9)
        v2 = pos(T(r"poids propre : $\approx 3\,\%$ du moment", sc=0.58), 2.3, -2.15)
        self.ecr(self.t("l9"), v2, rt=0.9)
        ip = ipe(2.6, -3.2)
        v3 = pos(T(r"IPE 80 : $I_{Gz}/v = 20$ cm$^3$", sc=0.54), 3.05, -2.95)
        v4 = pos(T(r"$\sigma = 150$ MPa, 3 fois plus léger", sc=0.54, color=JAUNE), 3.05, -3.5)
        self.at(self.t("l10"), Create(ip), Ecrire(v3, rt=0.9), run_time=0.9)
        self.ecr(self.t("l10b"), v4, rt=0.9)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Ce qu'il faut retenir", "Méthode")
        t0 = pos(T(r"la méthode pour \textbf{dimensionner en résistance}", sc=0.74, color=GRIS), -6.3, 2.2)
        self.ecr(self.t("m1"), t0, rt=0.9)
        pts = [("m2", r"sollicitation, puis \textbf{section critique} (diagrammes)", BLEU),
               ("m3", r"\textbf{point critique} : fibre la plus éloignée (flexion), périphérie (torsion)", VERT),
               ("m4", r"contrainte maximale : la bonne formule, en N, mm et MPa", ORANGE),
               ("m5", r"$\sigma_{max} \le R_{pe}$ \; ou \; $\tau_{max} \le R_{pg}$ $\Rightarrow$ dimension minimale", ROUGE),
               ("m6", r"\textbf{vérifier} : unités, ordre de grandeur, cas limite", JAUNE)]
        for k, (ph_, txt, c) in enumerate(pts):
            yy = [1.4, 0.5, -0.4, -1.3, -2.45][k]
            ca = carte(k+1, c, -5.9, yy); tx = pos(T(txt, sc=0.7), -5.35, yy)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
            if ph_ == "m5":
                ar = pos(T(r"arrondie à la valeur normalisée \textbf{supérieure}", sc=0.62, color=ROUGE), -5.35, yy - 0.5)
                self.ecr(self.t("m5b"), ar, rt=0.8)
        nx = T(r"Prochaine vidéo : déformations, flèches et dimensionnement en rigidité", sc=0.62, color=GRIS).move_to([0, -3.4, 0])
        self.ecr(self.t("m7"), nx, rt=1.2)
        self.fin()
