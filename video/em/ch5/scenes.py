from base import *
import os
APERCU = os.environ.get("APERCU")   # contrôle d'une scène en image fixe (pas d'effacement final)

# ---------- outils communs (repris des chapitres précédents)
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
def crb(ax, f, a, b, col=ORANGE, sw=4, n=200):
    u = np.linspace(a, b, n)
    return VMobject(color=col, stroke_width=sw).set_points_smoothly([ax.c2p(s, f(s)) for s in u])
def zero(ax, a, b): return DashedLine(ax.c2p(a, 0), ax.c2p(b, 0), color=GRIS, stroke_width=1.5, dash_length=0.08)
def P(x, y): return np.array([x, y, 0.0])
def fleche(a, b, col=ROUGE, sw=4, tl=0.18):
    return Arrow(P(*a), P(*b), buff=0, color=col, stroke_width=sw, tip_length=tl, max_tip_length_to_length_ratio=0.5, max_stroke_width_to_length_ratio=20)
def coche(x, y, col=VERT):
    return VMobject(color=col, stroke_width=6).set_points_as_corners([P(x - 0.16, y), P(x - 0.04, y - 0.13), P(x + 0.18, y + 0.18)])
def odot(x, y, col=BLEU, r=0.14):
    """vecteur sortant du tableau"""
    return VGroup(Circle(radius=r, color=col, stroke_width=3).move_to(P(x, y)), Dot(P(x, y), radius=0.045, color=col))
def otimes(x, y, col=BLEU, r=0.14):
    """vecteur entrant dans le tableau"""
    d = r*0.68
    return VGroup(Circle(radius=r, color=col, stroke_width=3).move_to(P(x, y)),
                  Line(P(x - d, y - d), P(x + d, y + d), color=col, stroke_width=3), Line(P(x - d, y + d), P(x + d, y - d), color=col, stroke_width=3))
def hachures(x0, y0, x1, y1, pas=0.2, col=GRIS, sw=1.5):
    """traits obliques à 45° dans le rectangle [x0, x1] x [y0, y1]"""
    h = y1 - y0; g = VGroup(); u = x0 - h
    while u < x1:
        a = (max(u, x0), y0 + max(0, x0 - u)); b = (min(u + h, x1), y0 + min(h, x1 - u))
        if b[0] > a[0]: g.add(Line(P(*a), P(*b), color=col, stroke_width=sw))
        u += pas
    return g
def metal(x0, x1, y0, y1, face=None):
    """bloc métallique hachuré ; face = abscisse de la face éclairée (trait épais)"""
    g = VGroup(Rectangle(width=x1 - x0, height=y1 - y0, color=GRIS, stroke_width=2).set_fill(GRIS, 0.12).move_to(P((x0 + x1)/2, (y0 + y1)/2)),
               hachures(x0, y0, x1, y1, pas=0.22, sw=1.2))
    if face is not None: g.add(Line(P(face, y0), P(face, y1), color=CRAIE, stroke_width=6))
    return g
def onde(f, x0, x1, col=ORANGE, sw=4, n=220, tirets=False):
    xs = np.linspace(x0, x1, n)
    v = VMobject(color=col, stroke_width=sw).set_points_smoothly([P(x, f(x)) for x in xs])
    return DashedVMobject(v, num_dashes=int(abs(x1 - x0)*7), dashed_ratio=0.55) if tirets else v
def repere_zyx(x, y, l=0.5, col=GRIS, horiz="z", vert="x", sort="y", entrant=False):
    """repère du tableau : un vecteur vers la droite, un vers le haut, le troisième perpendiculaire (⊙ ou ⊗)"""
    a1 = fleche((x, y), (x + l, y), col=col, sw=3, tl=0.11); a2 = fleche((x, y), (x, y + l), col=col, sw=3, tl=0.11)
    l1 = M(r"\vec e_" + horiz, sc=0.48, color=col).next_to(a1.get_end(), RIGHT, buff=0.05)
    l2 = M(r"\vec e_" + vert, sc=0.48, color=col).next_to(a2.get_end(), UP, buff=0.04)
    o = (otimes if entrant else odot)(x, y, col=col, r=0.09); l3 = M(r"\vec e_" + sort, sc=0.48, color=col).next_to(o, DL, buff=0.02)
    return VGroup(a1, a2, l1, l2, o, l3)

class C(Cours):
    def etape(self, k, col, y, m, t, rt=1.0, x=-6.35):
        ca = carte(k, col, x, y); mm = pos(m, x + 0.5, y)
        self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
        return mm
    def pause5(self, t, x, y):
        pa, arc = chrono(x, y)
        self.at(t, FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
    def rappel(self, txt):
        r = pos(T(txt, sc=0.54, color=GRIS), 6.6, 2.72, bord=RIGHT)
        self.play(FadeIn(r), run_time=0.4)
    def fin(self):
        if APERCU: self.wait(0.1); return
        super().fin()

# ---------------------------------------------------------------- S0
class S0(C):
    sid = "S0"
    def construct(self):
        sur = T(r"PHYSIQUE \;·\; PT", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Électromagnétisme -- Chapitre 5}", sc=1.1, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Ondes électromagnétiques et conducteurs", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-5.4, 1.3, 0], [5.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        # une onde arrive sur un métal : une partie s'éteint dedans, le reste rebondit
        xs, y0, y1, A, lam = 4.75, -0.35, -1.6, 0.4, 1.15
        bloc = metal(xs, 6.5, -2.3, 0.45, face=xs)
        inc = onde(lambda x: y0 + A*np.cos(2*PI*(x - xs)/lam + 0.9), 1.55, xs, col=ORANGE)
        ki = fleche((1.8, 0.3), (2.9, 0.3), col=ROUGE, sw=4, tl=0.15)
        dedans = onde(lambda x: y0 + 0.3*np.exp(-(x - xs)/0.22)*np.cos(2*PI*(x - xs)/0.5 + 0.9), xs, xs + 0.95, col=ROUGE, sw=3)
        ref = onde(lambda x: y1 - A*np.cos(2*PI*(xs - x)/lam - 0.9), 1.55, xs, col=BLEU, sw=3, tirets=True)
        kr = fleche((2.9, -2.3), (1.8, -2.3), col=BLEU, sw=4, tl=0.15)
        ld = M(r"\delta", sc=0.6, color=ROUGE).move_to(P(xs - 0.25, y0 + 0.62))
        self.at(self.a("a2", "qui rencontre un métal"), Create(bloc), Create(inc), GrowArrow(ki), run_time=1.0)
        self.at(self.a("a2", "Elle s'éteint"), Create(dedans), FadeIn(ld), run_time=0.6)
        self.at(self.a("a2", "ou elle rebondit"), Create(ref), GrowArrow(kr), run_time=0.8)
        items = []
        for k, (txt, col) in enumerate([("Conducteur ohmique et effet de peau", BLEU), ("Conducteur parfait, réflexion et cavité", VERT),
                                         ("Exercice 1 : le blindage d'une salle d'IRM", ORANGE), ("Exercice 2 : une antenne devant un réflecteur", ROUGE),
                                         ("Exercice 3 : la cavité d'un four à micro-ondes", JAUNE)]):
            yy = 0.65 - 0.64*k
            items.append(VGroup(carte(k+1, col, -6.2, yy), pos(T(txt, sc=0.66), -5.65, yy)))
        for it, (sid, fr_) in zip(items, [("a3", "l'effet de peau"), ("a3", "le conducteur parfait"), ("a4", "un blindage"),
                                          ("a4", "une antenne"), ("a4", "un four")]):
            self.jusqua(self.a(sid, fr_)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

# ---------------------------------------------------------------- S1
class S1(C):
    sid = "S1"
    def construct(self):
        self.entete(r"5.1 -- Le conducteur ohmique", "Cours")
        l1 = pos(T(r"\textbf{Loi d'Ohm locale} :", sc=0.72, color=BLEU), -6.3, 2.2)
        ohm = M(r"\vec j = \sigma\,\vec E", sc=1.0).next_to(l1, RIGHT, buff=0.4)
        self.at(self.a("b1", "Il suit la loi"), Ecrire(l1, rt=0.6), run_time=0.6)
        self.at(self.a("b1", "j égale sigma E"), Ecrire(ohm, rt=0.6), run_time=0.6)
        self.play(Create(enc(ohm, col=JAUNE, buff=0.12)), run_time=0.4)
        cu = pos(T(r"$\sigma$ : conductivité \quad (cuivre : $6{,}0\cdot10^{7}$ S$\cdot$m$^{-1}$)", sc=0.62, color=GRIS), -6.3, 1.5)
        self.ecr(self.a("b1", "où sigma est la conductivité"), cu, rt=1.0)
        self.etape(1, BLEU, 0.72, T(r"\textbf{Neutralité} : \; $\dfrac{\partial\rho}{\partial t} + \dfrac{\sigma}{\varepsilon_0}\,\rho = 0$", sc=0.68), self.t("b3"), rt=1.0)
        n1 = pos(T(r"$\rho = 0$ en volume, en $\varepsilon_0/\sigma \approx 10^{-19}$ s", sc=0.62, color=GRIS), -5.85, 0.0)
        self.ecr(self.a("b3", "Une charge en volume"), n1, rt=0.9)
        self.etape(2, VERT, -0.8, T(r"\textbf{Courant de déplacement} : \; $\dfrac{\varepsilon_0\,\omega}{\sigma}$", sc=0.68), self.a("b4", "comparer"), rt=1.0)
        n2 = pos(T(r"cuivre, 10 GHz : $\approx 10^{-8} \ll 1$ \;$\Rightarrow$\; \textbf{ARQS magnétique}", sc=0.62, color=VERT), -5.85, -1.52)
        self.ecr(self.t("b5"), n2, rt=1.1)
        # Maxwell dans le métal
        tm = T(r"Maxwell dans le métal", sc=0.66, color=GRIS).move_to([4.35, 2.25, 0])
        eqs = VGroup(M(r"\operatorname{div}\vec E = 0", sc=0.78), M(r"\overrightarrow{\operatorname{rot}}\,\vec E = -\frac{\partial\vec B}{\partial t}", sc=0.78),
                     M(r"\operatorname{div}\vec B = 0", sc=0.78), M(r"\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\sigma\,\vec E", sc=0.78, color=JAUNE))
        eqs.arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([4.35, 0.3, 0])
        bx = SurroundingRectangle(eqs, color=GRIS, buff=0.25, corner_radius=0.08)
        tm.next_to(bx, UP, buff=0.15)
        self.at(self.a("b5", "On néglige donc"), FadeIn(tm), Create(bx), Ecrire(eqs[0], rt=0.4), Ecrire(eqs[1], rt=0.6), Ecrire(eqs[2], rt=0.4), run_time=0.8)
        self.at(self.a("b6", "rotationnel de B"), Ecrire(eqs[3], rt=0.8), run_time=0.8)
        jl = T(r"\textbf{Effet Joule} : \; $\vec j\cdot\vec E = \sigma E^2 > 0$ \;$\Rightarrow$\; le métal \textbf{absorbe} l'onde", sc=0.72, color=ORANGE).move_to([0, -2.85, 0])
        self.ecr(self.t("b7"), jl, rt=1.2); self.play(Create(enc(jl, col=ORANGE, buff=0.16)), run_time=0.4)
        self.fin()

# ---------------------------------------------------------------- S2
class S2(C):
    sid = "S2"
    def construct(self):
        self.entete(r"5.2 -- Diffusion et effet de peau", "Cours")
        c1 = pos(T(r"$\overrightarrow{\mathrm{rot}}$ de (MF), avec $\overrightarrow{\mathrm{rot}}\,\vec B = \mu_0\sigma\vec E$ :", sc=0.62, color=GRIS), -6.3, 2.28)
        self.ecr(self.t("c2"), c1, rt=1.0)
        dif = pos(M(r"\Delta\vec E = \mu_0\sigma\,\frac{\partial\vec E}{\partial t}", sc=0.8, color=JAUNE), -6.1, 1.45)
        self.ecr(self.a("c2", "une équation de diffusion"), dif, rt=1.0); self.play(Create(enc(dif, col=JAUNE, buff=0.14)), run_time=0.4)
        ld = T(r"équation de \textbf{diffusion}", sc=0.62, color=JAUNE).next_to(dif, RIGHT, buff=0.45)
        self.play(FadeIn(ld), run_time=0.3)
        c3 = pos(T(r"ordre 1 en $t$ : \textbf{irréversible} (effet Joule)", sc=0.62, color=GRIS), -6.3, 0.6)
        self.ecr(self.a("c2", "Le phénomène est irréversible"), c3, rt=0.9)
        c4 = pos(M(r"\underline{\vec E} = E_0\,e^{i(\omega t - \underline{k}z)}\,\vec e_x \;\Rightarrow\; \underline{k}^2 = -i\,\mu_0\sigma\omega", sc=0.7), -6.3, -0.05)
        self.ecr(self.a("c4", "pseudo-onde plane"), c4, rt=1.3)
        c5 = pos(M(r"\underline{k} = (1-i)/\delta", sc=0.75), -6.3, -0.72)
        c5b = T(r"l'onde entre et s'atténue", sc=0.58, color=GRIS).next_to(c5, RIGHT, buff=0.35)
        self.ecr(self.t("c5"), c5, rt=0.7)
        self.ecr(self.a("c5", "On garde le signe plus"), c5b, rt=0.7)
        c6 = pos(M(r"\delta = \sqrt{\frac{2}{\mu_0\sigma\omega}}", sc=0.82, color=JAUNE), -6.1, -1.8)
        c6b = T(r"\textbf{épaisseur de peau}", sc=0.66, color=JAUNE).next_to(c6, RIGHT, buff=0.5)
        self.ecr(self.t("c6"), c6, rt=0.8); self.play(Create(enc(c6, col=JAUNE, buff=0.14)), FadeIn(c6b), run_time=0.4)
        # le champ dans le métal (z en unités de delta)
        ax, fr = cadre(3.85, 1.25, 5.3, 2.1, 0, 5, -1.15, 1.15)
        env = VGroup(crb(ax, lambda u: np.exp(-u), 0, 5, col=GRIS, sw=2), crb(ax, lambda u: -np.exp(-u), 0, 5, col=GRIS, sw=2))
        env = VGroup(*[DashedVMobject(e, num_dashes=28) for e in env])
        e1 = crb(ax, lambda u: np.exp(-u)*np.cos(u), 0, 5, col=ORANGE)
        e2 = crb(ax, lambda u: np.exp(-u)*np.sin(u), 0, 5, col=BLEU, sw=3)
        z0 = zero(ax, 0, 5)
        tk = DashedLine(ax.c2p(1, -1.15), ax.c2p(1, 1.15), color=GRIS, stroke_width=1.5, dash_length=0.07)
        lt = M(r"\delta", sc=0.6, color=CRAIE).next_to(ax.c2p(1, -1.15), DOWN, buff=0.08)
        lz = M(r"z", sc=0.6, color=GRIS).next_to(ax.c2p(5, -1.15), DOWN, buff=0.08).shift(0.15*LEFT)
        lm = T(r"métal ($z > 0$)", sc=0.52, color=GRIS).move_to(ax.c2p(3.75, 0.82))
        le = M(r"E_0\,e^{-z/\delta}", sc=0.55, color=GRIS).move_to(ax.c2p(2.3, 0.45))
        self.at(self.t("c7"), Create(fr), Create(z0), FadeIn(lm), run_time=0.5)
        self.play(Create(env), FadeIn(le), run_time=0.6)
        self.at(self.a("c7", "exponentielle"), Create(e1), Create(e2), Create(tk), FadeIn(lt), FadeIn(lz), run_time=1.0)
        cr = M(r"\vec E = E_0\,e^{-z/\delta}\cos(\omega t - z/\delta)\,\vec e_x", sc=0.7, color=ORANGE).move_to([3.85, -0.5, 0])
        self.ecr(self.a("c7", "l'onde s'éteint"), cr, rt=1.0)
        # ordres de grandeur
        X = [1.95, 3.55, 4.95, 6.2]; R = [-1.25, -1.88]
        hd = [T(r"$f$", sc=0.6, color=GRIS).move_to([X[0], R[0], 0]), T(r"$\delta$ (cuivre)", sc=0.6, color=GRIS).move_to([X[0], R[1], 0])]
        fs = [T(t, sc=0.6).move_to([x, R[0], 0]) for t, x in zip(["50 Hz", "1 MHz", "10 GHz"], X[1:])]
        ds = [T(t, sc=0.62, color=VERT).move_to([x, R[1], 0]) for t, x in zip([r"$9{,}2$ mm", r"$65$ $\mu$m", r"$0{,}65$ $\mu$m"], X[1:])]
        sp = Line([1.2, -1.57, 0], [6.7, -1.57, 0], color=GRIS, stroke_width=1.5, stroke_opacity=0.6)
        self.at(self.t("c8"), *[FadeIn(h) for h in hd], Create(sp), *[FadeIn(f) for f in fs], run_time=0.6)
        for d, fr_ in zip(ds, ["neuf millimètres", "soixante-cinq microns", "moins d'un micron"]):
            self.at(self.a("c8", fr_), Ecrire(d, rt=0.5), run_time=0.5)
        r1 = T(r"$\delta \propto 1/\sqrt{f}$", sc=0.8, color=JAUNE).move_to([3.85, -2.65, 0])
        self.ecr(self.t("c9"), r1, rt=0.6)
        r2 = T(r"attention : amplitude $\div\,e$ sur $\delta$, \; puissance $\div\,e$ sur $\delta/2$", sc=0.66, color=ROUGE).move_to([0, -3.4, 0])
        self.ecr(self.a("c9", "Et attention"), r2, rt=1.1)
        self.fin()

# ---------------------------------------------------------------- S3
class S3(C):
    sid = "S3"
    def construct(self):
        self.entete(r"5.3 -- Conducteur parfait et réflexion", "Cours")
        xs, ya = 4.7, 1.4
        bloc = metal(xs, 6.4, 0.25, 2.55, face=xs)
        lb = T(r"métal parfait", sc=0.55, color=GRIS).move_to([5.55, 0.0, 0])
        d1 = pos(T(r"\textbf{Conducteur parfait} : $\sigma \to \infty$, \; $\delta \to 0$", sc=0.7, color=BLEU), -6.3, 2.2)
        self.at(self.t("d1"), Ecrire(d1, rt=1.0), Create(bloc), FadeIn(lb), run_time=1.0)
        d2 = pos(M(r"\vec E_{\text{int}} = \vec 0, \qquad \vec B_{\text{int}} = \vec 0", sc=0.75), -6.3, 1.55)
        self.ecr(self.t("d2"), d2, rt=0.9)
        d2b = pos(T(r"sources en surface : $\sigma_s$ (C$\cdot$m$^{-2}$), $\vec j_s$ (A$\cdot$m$^{-1}$)", sc=0.6, color=GRIS), -6.3, 0.95)
        self.ecr(self.a("d2", "qu'en surface"), d2b, rt=0.9)
        d3 = pos(T(r"relations de passage (\textbf{fournies}), $\vec n$ \textbf{sortante} :", sc=0.62, color=GRIS), -6.3, 0.3)
        self.ecr(self.t("d3"), d3, rt=0.9)
        d3b = pos(M(r"\vec E = \frac{\sigma_s}{\varepsilon_0}\,\vec n \qquad \vec B = \mu_0\,\vec j_s \wedge \vec n", sc=0.8), -6.1, -0.5)
        fn = fleche((xs, 2.25), (xs - 0.75, 2.25), col=CRAIE, sw=3, tl=0.13); ln = M(r"\vec n", sc=0.6).next_to(fn.get_end(), DOWN, buff=0.05)
        self.ecr(self.a("d3", "avec n la normale"), d3b, rt=1.1)
        self.play(Create(enc(d3b, col=VERT, buff=0.14)), GrowArrow(fn), FadeIn(ln), run_time=0.5)
        d4 = pos(T(r"au contact : $\vec E$ \textbf{normal}, \; $\vec B$ \textbf{tangent}", sc=0.68, color=VERT), -6.3, -1.3)
        self.ecr(self.t("d4"), d4, rt=0.9)
        # onde incidente et onde réfléchie
        A, lam, ph = 0.5, 1.25, PI/3
        k = 2*PI/lam
        inc = onde(lambda x: ya + A*np.cos(ph - k*(x - xs)), 1.25, xs, col=ORANGE)
        ref = onde(lambda x: ya - A*np.cos(ph + k*(x - xs)), 1.25, xs, col=ORANGE, sw=3, tirets=True)
        ki = fleche((1.45, 2.35), (2.45, 2.35), col=ROUGE, sw=3, tl=0.13); lki = M(r"\vec k_i", sc=0.55, color=ROUGE).next_to(ki, RIGHT, buff=0.08)
        kr = fleche((3.55, 0.42), (2.55, 0.42), col=ROUGE, sw=3, tl=0.13); lkr = M(r"\vec k_r", sc=0.55, color=ROUGE).next_to(kr, LEFT, buff=0.08)
        rp = repere_zyx(0.75, 0.25, l=0.42, horiz="z", vert="x", sort="y")
        self.at(self.t("d5"), Create(inc), GrowArrow(ki), FadeIn(lki), FadeIn(rp), run_time=1.0)
        self.at(self.a("d6", "Il faut une onde réfléchie"), Create(ref), GrowArrow(kr), FadeIn(lkr), run_time=0.9)
        rr = M(r"\underline{r} = -1", sc=0.75, color=JAUNE).move_to([3.4, -0.4, 0])
        self.at(self.a("d6", "r égale moins un"), Ecrire(rr, rt=0.5), run_time=0.5); self.play(Create(enc(rr, col=JAUNE, buff=0.1)), run_time=0.3)
        es = M(r"\vec E = 2E_0\sin(kz)\sin(\omega t)\,\vec e_x", sc=0.75, color=ORANGE).move_to([-3.4, -2.05, 0])
        bs = M(r"\vec B = \frac{2E_0}{c}\cos(kz)\cos(\omega t)\,\vec e_y", sc=0.75, color=BLEU).move_to([3.3, -2.05, 0])
        self.ecr(self.a("d7", "E en sinus"), es, rt=1.0)
        self.ecr(self.a("d7", "B en cosinus"), bs, rt=1.0)
        st = T(r"\textbf{onde stationnaire} : rien ne se propage", sc=0.66, color=JAUNE).move_to([0, -2.85, 0])
        self.ecr(self.a("d7", "Rien ne se propage"), st, rt=0.8)
        jsf = fleche((xs - 0.12, 0.75), (xs - 0.12, 1.95), col=VERT, sw=4, tl=0.15); ljs = M(r"\vec j_s", sc=0.6, color=VERT).move_to([xs - 0.45, 0.75, 0])
        bm = odot(xs - 0.45, 1.75, col=BLEU, r=0.12)
        d9 = T(r"sur le miroir : $\vec B$ double, porté par $\vec j_s \parallel \vec E_i$, qui rayonne l'onde réfléchie", sc=0.62, color=VERT).move_to([0, -3.5, 0])
        self.at(self.t("d9"), GrowArrow(jsf), FadeIn(ljs), FadeIn(bm), Ecrire(d9, rt=1.3), run_time=1.3)
        self.fin()

# ---------------------------------------------------------------- S4
class S4(C):
    sid = "S4"
    def construct(self):
        self.entete(r"5.4 -- Onde stationnaire et cavité", "Cours")
        ax, fr = cadre(-2.55, 1.35, 7.3, 1.85, -1.0, 0.0, -0.12, 1.18)
        xr = ax.c2p(0, 0)[0]
        bloc = metal(xr, xr + 0.45, 0.42, 2.28, face=xr)
        cE = crb(ax, lambda u: abs(np.sin(2*PI*u)), -1, 0, col=ORANGE)
        cB = crb(ax, lambda u: abs(np.cos(2*PI*u)), -1, 0, col=BLEU, sw=3)
        lE = M(r"|E|", sc=0.55, color=ORANGE).move_to(ax.c2p(-0.75, 1.18) + np.array([0, 0.25, 0]))
        lB = M(r"c|B|", sc=0.55, color=BLEU).move_to(ax.c2p(-0.5, 1.18) + np.array([0, 0.25, 0]))
        nE = VGroup(*[Dot(ax.c2p(u, 0), radius=0.07, color=ORANGE) for u in (0, -0.5, -1)])
        tks = VGroup(*[T(t, sc=0.5, color=GRIS).next_to(ax.c2p(u, -0.12), DOWN, buff=0.08) for t, u in
                       [("$0$", 0), (r"$-\lambda/4$", -0.25), (r"$-\lambda/2$", -0.5), (r"$-3\lambda/4$", -0.75), (r"$-\lambda$", -1)]])
        t1 = pos(T(r"nœuds de $\vec E$ : tous les $\lambda/2$", sc=0.62, color=ORANGE), 2.05, 2.0)
        t2 = pos(T(r"ventres de $\vec E$ = nœuds de $\vec B$", sc=0.62, color=BLEU), 2.05, 1.4)
        self.at(self.t("e1"), Create(fr), Create(bloc), Create(cE), FadeIn(lE), FadeIn(tks), Ecrire(t1, rt=0.8), run_time=0.8)
        self.at(self.a("e1", "le premier sur le miroir"), FadeIn(nE), run_time=0.5)
        self.at(self.a("e1", "Les ventres de E"), Create(cB), FadeIn(lB), run_time=0.8)
        self.ecr(self.a("e1", "ce sont les nœuds de B"), t2, rt=0.8)
        t3 = pos(M(r"\langle\vec\Pi\rangle = \vec 0", sc=0.8, color=JAUNE), 2.05, 0.65)
        t3b = T(r"aucun transport d'énergie", sc=0.58, color=GRIS).next_to(t3, RIGHT, buff=0.3)
        self.ecr(self.t("e2"), t3, rt=0.6); self.play(Create(enc(t3, col=JAUNE, buff=0.1)), FadeIn(t3b), run_time=0.4)
        # cavité
        x0, x1, yc = -6.0, -1.55, -1.95
        mg = metal(x0 - 0.35, x0, yc - 1.0, yc + 1.0, face=x0); md = metal(x1, x1 + 0.35, yc - 1.0, yc + 1.0, face=x1)
        Lb = x1 - x0
        l0 = T(r"$0$", sc=0.55, color=GRIS).move_to([x0, yc - 1.22, 0]); lL = T(r"$L$", sc=0.55, color=GRIS).move_to([x1, yc - 1.22, 0])
        self.at(self.t("e3"), Create(mg), Create(md), FadeIn(l0), FadeIn(lL), run_time=0.8)
        s3 = pos(M(r"\sin(kL) = 0", sc=0.8), 0.4, -0.85)
        self.ecr(self.a("e3", "E doit aussi"), s3, rt=0.7)
        modes = [onde(lambda x, n=n: yc + 0.8*np.sin(n*PI*(x - x0)/Lb), x0, x1, col=c, sw=3) for n, c in ((1, ORANGE), (2, BLEU), (3, VERT))]
        lm = [T(r"$n = %d$" % n, sc=0.5, color=c).move_to([x, yc + y, 0]) for n, c, x, y in ((1, ORANGE, -3.78, 0.98), (2, BLEU, -4.9, 0.98), (3, VERT, -2.3, 0.98))]
        kn = pos(M(r"k_n = \frac{n\pi}{L}", sc=0.8), 0.4, -1.75)
        fn = M(r"f_n = n\,\frac{c}{2L}", sc=0.9, color=JAUNE).next_to(kn, RIGHT, buff=0.7)
        self.at(self.t("e4"), *[Create(m) for m in modes], *[FadeIn(l) for l in lm], Ecrire(kn, rt=0.7), run_time=1.0)
        self.ecr(self.a("e4", "f n égale"), fn, rt=0.7); self.play(Create(enc(fn, col=JAUNE, buff=0.12)), run_time=0.4)
        ln_ = pos(M(r"\lambda_n = \frac{2L}{n}, \quad n \in \mathbb{N}^*", sc=0.75), 0.4, -2.65)
        self.ecr(self.a("e4", "avec n entier"), ln_, rt=0.8)
        me = pos(T(r"$L$ = un nombre entier de $\lambda/2$ \; (corde de Melde)", sc=0.6, color=GRIS), 0.4, -3.4)
        self.ecr(self.t("e5"), me, rt=1.0)
        go = T(r"\textbf{Place aux exercices !}", sc=0.75, color=JAUNE).move_to([3.4, 2.45, 0]).shift(0.0*UP)
        self.at(self.t("e6"), Indicate(fn, color=JAUNE), run_time=0.6)
        self.fin()

# ---------------------------------------------------------------- S5
class S5(C):
    sid = "S5"
    def construct(self):
        self.entete(r"Exercice 1 -- le blindage d'une salle d'IRM", "Énoncé")
        xf0, xf1 = -3.35, -2.95
        ext = T(r"extérieur", sc=0.55, color=GRIS).move_to([-5.3, 2.45, 0])
        sal = T(r"salle d'IRM", sc=0.55, color=GRIS).move_to([-1.6, 2.45, 0])
        ou = onde(lambda x: 1.5 + 0.42*np.sin(2*PI*(x + 6.3)/0.95), -6.35, xf0, col=ORANGE)
        fk = fleche((-6.25, 0.72), (-5.3, 0.72), col=ROUGE, sw=3, tl=0.13); lk = T(r"ondes radio", sc=0.5, color=ROUGE).next_to(fk, RIGHT, buff=0.12)
        feu = Rectangle(width=xf1 - xf0, height=1.8, color=ORANGE, stroke_width=3).set_fill(ORANGE, 0.55).move_to([(xf0 + xf1)/2, 1.55, 0])
        lf = T(r"cuivre, épaisseur $d$ ?", sc=0.52, color=ORANGE).move_to([(xf0 + xf1)/2, 0.38, 0])
        irm = VGroup(Annulus(inner_radius=0.32, outer_radius=0.62, color=GRIS, stroke_width=2, fill_opacity=0.25).move_to([-1.6, 1.45, 0]),
                     Circle(radius=0.62, color=CRAIE, stroke_width=2.5).move_to([-1.6, 1.45, 0]), Circle(radius=0.32, color=CRAIE, stroke_width=2.5).move_to([-1.6, 1.45, 0]))
        self.at(self.t("f1"), FadeIn(ext), FadeIn(sal), Create(feu), Create(irm), run_time=1.0)
        self.at(self.a("f2", "des signaux"), Create(ou), GrowArrow(fk), FadeIn(lk), run_time=0.6)
        d1 = pos(T(r"$f = 64$ MHz", sc=0.7), 0.6, 2.25)
        d2 = pos(T(r"$\sigma = 6{,}0\cdot10^{7}$ S$\cdot$m$^{-1}$", sc=0.7), 0.6, 1.65)
        d3 = pos(T(r"$\mu_0 = 4\pi\cdot10^{-7}$ H$\cdot$m$^{-1}$, \; $\varepsilon_0 = 8{,}85\cdot10^{-12}$ F$\cdot$m$^{-1}$", sc=0.56, color=GRIS), 0.6, 1.05)
        self.ecr(self.a("f2", "soixante-quatre"), d1, rt=0.5)
        self.at(self.a("f2", "on tapisse"), Ecrire(d2, rt=0.7), Ecrire(d3, rt=0.9), run_time=0.9)
        self.at(self.a("f2", "feuille de cuivre"), FadeIn(lf), run_time=0.4)
        q1 = pos(T(r"Q1. Épaisseur de peau $\delta$ du cuivre à 64 MHz ?", sc=0.7), -6.2, -0.4)
        q2 = pos(T(r"Q2. Épaisseur $d$ de la feuille pour diviser l'amplitude par $10^5$ ?", sc=0.7), -6.2, -1.0)
        q3 = pos(T(r"Q3. Ce blindage arrête-t-il le champ à 50 Hz du réseau ?", sc=0.7), -6.2, -1.6)
        self.ecr(self.t("f3"), q1, rt=0.9); self.ecr(self.t("f4"), q2, rt=1.1); self.ecr(self.t("f5"), q3, rt=1.0)
        bx = SurroundingRectangle(VGroup(q1, q2, q3), color=ROUGE, buff=0.18, corner_radius=0.08)
        self.play(Create(bx), run_time=0.4)
        rf = pos(T(r"Réfléchissons : ARQS valable ? \; Puis la loi de décroissance de l'amplitude", sc=0.66, color=BLEU), -6.2, -2.5)
        self.ecr(self.t("f6"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-1.0, -3.25, 0])
        self.ecr(self.t("f7"), av, rt=0.7)
        self.pause5(self.PH["f7"]["fin"], 2.3, -3.25)
        self.fin()

# ---------------------------------------------------------------- S6
class S6(C):
    sid = "S6"
    def construct(self):
        self.entete(r"Exercice 1 -- la solution", "Solution")
        self.rappel(r"$f = 64$ MHz, \; $\sigma = 6{,}0\cdot10^{7}$ S$\cdot$m$^{-1}$")
        self.etape(1, BLEU, 2.2, M(r"\frac{\varepsilon_0\,\omega}{\sigma} \approx 6\cdot10^{-11} \ll 1 \;\Rightarrow\; \text{ARQS}", sc=0.68), self.a("g1", "Epsilon zéro oméga"), rt=1.0)
        self.etape(2, VERT, 1.5, T(r"piège : la \textbf{pulsation} $\omega = 2\pi f$, pas $f$ !", sc=0.64, color=ROUGE), self.a("g2", "Piège"), rt=0.9)
        g2 = pos(M(r"\delta = \sqrt{\frac{2}{\mu_0\sigma\omega}} = \frac{1}{\sqrt{\pi\mu_0\sigma f}}", sc=0.7), -5.85, 0.78)
        self.ecr(self.a("g2", "Avec la fréquence"), g2, rt=1.0)
        g3 = pos(M(r"\delta \approx 8{,}1\ \mu\mathrm{m}", sc=0.8, color=VERT), -5.85, 0.0)
        g3b = T(r"10 fois moins qu'un cheveu", sc=0.56, color=GRIS).next_to(g3, RIGHT, buff=0.45)
        self.ecr(self.t("g3"), g3, rt=0.6); self.play(Create(enc(g3, col=VERT, buff=0.1)), FadeIn(g3b), run_time=0.4)
        # amplitude en échelle logarithmique dans la feuille
        ax, fr = cadre(4.0, 1.15, 4.9, 2.2, 0, 120, -6, 0.6)
        l64 = Line(ax.c2p(0, 0), ax.c2p(112.2, -6), color=ORANGE, stroke_width=4)
        l50 = Line(ax.c2p(0, 0), ax.c2p(120, -120/(9188.8*np.log(10))), color=BLEU, stroke_width=4)
        h5 = DashedLine(ax.c2p(0, -5), ax.c2p(120, -5), color=GRIS, stroke_width=1.5, dash_length=0.07)
        v94 = DashedLine(ax.c2p(93.5, -6), ax.c2p(93.5, 0.6), color=VERT, stroke_width=2, dash_length=0.07)
        ty = T(r"$\log_{10}(E/E_0)$", sc=0.48, color=GRIS).move_to(ax.c2p(22, -4.3))
        tx = VGroup(*[T(t, sc=0.48, color=GRIS).next_to(ax.c2p(u, -6), DOWN, buff=0.07) for t, u in (("$0$", 0), ("$50$", 50), ("$100$", 100))])
        tz = T(r"$z$ ($\mu$m)", sc=0.48, color=GRIS).next_to(ax.c2p(120, -6), DOWN, buff=0.07).shift(0.1*LEFT)
        t5 = T(r"$-5$", sc=0.48, color=GRIS).next_to(ax.c2p(0, -5), LEFT, buff=0.08)
        t0 = T(r"$0$", sc=0.48, color=GRIS).next_to(ax.c2p(0, 0), LEFT, buff=0.08)
        a64 = T(r"64 MHz", sc=0.5, color=ORANGE).move_to(ax.c2p(70, -2.4))
        a50 = T(r"50 Hz", sc=0.5, color=BLEU).move_to(ax.c2p(60, -0.75))
        l94 = T(r"$94$ $\mu$m", sc=0.5, color=VERT).move_to(ax.c2p(107, -2.6))
        self.at(self.t("g4"), Create(fr), FadeIn(tx), FadeIn(tz), FadeIn(t0), FadeIn(ty), run_time=0.6)
        self.etape(3, ORANGE, -0.75, M(r"e^{-d/\delta} \le 10^{-5}", sc=0.75), self.a("g4", "On veut que"), rt=0.7)
        self.play(Create(l64), FadeIn(a64), run_time=0.8)
        g5 = pos(M(r"d \ge \delta\,\ln(10^5) \approx 11{,}5\,\delta", sc=0.75), -5.85, -1.42)
        self.at(self.t("g5"), Ecrire(g5, rt=0.9), Create(h5), FadeIn(t5), run_time=0.9)
        g6 = pos(M(r"d \ge 94\ \mu\mathrm{m} \;\to\; 0{,}1\ \mathrm{mm}", sc=0.8, color=VERT), -5.85, -2.15)
        self.at(self.t("g6"), Ecrire(g6, rt=0.8), Create(v94), FadeIn(l94), run_time=0.8); self.play(Create(enc(g6, col=VERT, buff=0.1)), run_time=0.4)
        # 50 Hz
        self.etape(4, ROUGE, -0.6, M(r"50\ \mathrm{Hz} : \ \delta \times \sqrt{64\cdot10^6/50} \approx \delta \times 1130", sc=0.58), self.a("g8", "Delta varie"), rt=1.0, x=1.05)
        g9 = pos(T(r"$\delta = 9{,}2$ mm : la feuille n'atténue que de $1\,\%$", sc=0.58), 1.55, -1.22)
        self.at(self.t("g9"), Ecrire(g9, rt=0.9), Create(l50), FadeIn(a50), run_time=0.9)
        g10 = pos(T(r"il faudrait $11{,}5 \times 9{,}2$ mm $\approx 10$ cm !", sc=0.6, color=ROUGE), 1.55, -1.84)
        self.ecr(self.t("g10"), g10, rt=0.9)
        self.etape(5, JAUNE, -2.55, T(r"$9{,}2$ mm à 50 Hz : la valeur du cours", sc=0.6), self.t("g11"), rt=1.0, x=1.05)
        cc = T(r"l'effet de peau arrête les \textbf{hautes} fréquences, pas les basses", sc=0.7, color=JAUNE).move_to([0.3, -3.45, 0])
        self.ecr(self.t("g12"), cc, rt=1.1); self.play(Create(enc(cc, col=JAUNE, buff=0.12)), run_time=0.4)
        self.fin()

# ---------------------------------------------------------------- S7
class S7(C):
    sid = "S7"
    def construct(self):
        self.entete(r"Exercice 2 -- une antenne devant un réflecteur", "Énoncé")
        xs = -1.55
        bloc = metal(xs, -0.75, 0.45, 2.55, face=xs)
        lp = T(r"plaque", sc=0.5, color=GRIS).move_to([-1.15, 0.2, 0])
        fk = fleche((-5.9, 2.3), (-4.8, 2.3), col=ROUGE, sw=3, tl=0.13); lk = M(r"\vec k", sc=0.6, color=ROUGE).next_to(fk, RIGHT, buff=0.08)
        fe = fleche((-4.3, 1.1), (-4.3, 2.05), col=ORANGE, sw=4, tl=0.15); le = M(r"\vec E_i", sc=0.6, color=ORANGE).next_to(fe, RIGHT, buff=0.08)
        ou = onde(lambda x: 1.45 + 0.35*np.cos(2*PI*(x + 3.6)/1.1), -3.6, xs, col=ORANGE, sw=3)
        rp = repere_zyx(-6.25, 0.7, l=0.42, horiz="z", vert="y", sort="x", entrant=True)
        an = VGroup(Line(P(-2.35, 1.1), P(-2.35, 1.42), color=JAUNE, stroke_width=5), Line(P(-2.35, 1.5), P(-2.35, 1.82), color=JAUNE, stroke_width=5))
        la = T(r"antenne", sc=0.5, color=JAUNE).move_to([-2.35, 2.15, 0])
        cd = DoubleArrow(P(-2.35, 0.75), P(xs, 0.75), buff=0, color=GRIS, stroke_width=2, tip_length=0.1, max_tip_length_to_length_ratio=0.3)
        lcd = T(r"$d$ ?", sc=0.55, color=GRIS).next_to(cd, DOWN, buff=0.06)
        self.at(self.t("h1"), Create(bloc), FadeIn(lp), Create(an), FadeIn(la), run_time=1.0)
        self.at(self.a("h1", "réflecteur"), Create(cd), FadeIn(lcd), run_time=0.5)
        d1 = pos(T(r"$f = 2{,}4$ GHz, \; incidence normale", sc=0.66), 0.25, 2.25)
        d2 = pos(T(r"plaque : conducteur parfait en $z > 0$", sc=0.62, color=GRIS), 0.25, 1.68)
        self.at(self.t("h2"), Ecrire(d1, rt=0.8), GrowArrow(fk), FadeIn(lk), FadeIn(rp), run_time=0.8)
        self.ecr(self.a("h2", "une plaque conductrice parfaite"), d2, rt=0.8)
        d3 = pos(M(r"\vec E_i = E_0\cos(\omega t - kz)\,\vec e_y, \quad E_0 = 2{,}0\ \mathrm{V\cdot m^{-1}}", sc=0.66), 0.25, 1.1)
        self.at(self.t("h3"), Ecrire(d3, rt=1.1), GrowArrow(fe), FadeIn(le), Create(ou), run_time=1.1)
        d4 = pos(T(r"fournies : $\vec E = \dfrac{\sigma_s}{\varepsilon_0}\,\vec n$, \; $\vec B = \mu_0\,\vec j_s\wedge\vec n$ \; ($\vec n$ sortante)", sc=0.58, color=GRIS), 0.25, 0.45)
        self.play(Ecrire(d4, rt=1.0))
        q1 = pos(T(r"Q1. Onde réfléchie, puis champs $\vec E$ et $\vec B$ totaux ?", sc=0.7), -6.2, -0.4)
        q2 = pos(T(r"Q2. Nœuds de $\vec E$ et de $\vec B$ ? Où placer l'antenne (sensible à $\vec E$) ?", sc=0.7), -6.2, -1.0)
        q3 = pos(T(r"Q3. Courant surfacique $\vec j_s$ ? Vecteur de Poynting moyen ?", sc=0.7), -6.2, -1.6)
        self.ecr(self.t("h4"), q1, rt=1.0); self.ecr(self.t("h5"), q2, rt=1.2); self.ecr(self.t("h6"), q3, rt=1.0)
        bx = SurroundingRectangle(VGroup(q1, q2, q3), color=ROUGE, buff=0.18, corner_radius=0.08)
        self.play(Create(bx), run_time=0.4)
        rf = pos(T(r"Réfléchissons : condition aux limites sur la plaque, et attention au \textbf{trièdre} !", sc=0.64, color=BLEU), -6.2, -2.55)
        self.ecr(self.t("h7"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-1.0, -3.35, 0])
        self.ecr(self.t("h8"), av, rt=0.7)
        self.pause5(self.PH["h8"]["fin"], 2.3, -3.35)
        self.fin()

# ---------------------------------------------------------------- S8
class S8(C):
    sid = "S8"
    def construct(self):
        self.entete(r"Exercice 2 -- l'onde stationnaire", "Solution")
        self.rappel(r"$\vec E_i = E_0\cos(\omega t - kz)\,\vec e_y$, \; $2{,}4$ GHz, \; métal en $z > 0$")
        m1 = self.etape(1, BLEU, 2.25, M(r"\vec B_i = (\vec e_z \wedge \vec E_i)/c", sc=0.7), self.a("i1", "e z vectoriel E i"), rt=0.8)
        m1b = M(r"= -\tfrac{E_0}{c}\cos(\omega t - kz)\,\vec e_x", sc=0.7).next_to(m1, RIGHT, buff=0.12)
        self.ecr(self.a("i2", "d'où un signe moins"), m1b, rt=0.9)
        n2 = pos(T(r"$\vec e_z\wedge\vec e_y = -\vec e_x$ \; : \; trièdre $(\vec E, \vec B, \vec k)$ direct", sc=0.6, color=GRIS), -5.85, 1.65)
        self.ecr(self.a("i2", "Pas d'erreur"), n2, rt=0.9)
        self.etape(2, VERT, 1.05, T(r"sur la plaque : $\vec E$ tangent \textbf{nul}, à tout instant", sc=0.64), self.t("i4"), rt=0.9)
        m4 = pos(M(r"\vec E_r = E_{r0}\cos(\omega t + kz)\,\vec e_y, \quad E_0 + E_{r0} = 0", sc=0.66), -5.85, 0.48)
        self.ecr(self.a("i4", "L'onde réfléchie"), m4, rt=1.1)
        m4b = pos(M(r"\Rightarrow\; E_{r0} = -E_0", sc=0.66, color=VERT), -5.85, -0.08)
        self.ecr(self.a("i4", "y vaut donc"), m4b, rt=0.6)
        # fuseaux devant la plaque
        ax, fr = cadre(4.3, 0.2, 4.3, 2.3, -1.0, 0.0, -0.12, 1.25)
        xr = ax.c2p(0, 0)[0]
        bloc = metal(xr, xr + 0.38, -0.95, 1.35, face=xr)
        cE = crb(ax, lambda u: abs(np.sin(2*PI*u)), -1, 0, col=ORANGE)
        cB = crb(ax, lambda u: abs(np.cos(2*PI*u)), -1, 0, col=BLEU, sw=3)
        lE = M(r"|E|", sc=0.52, color=ORANGE).move_to(ax.c2p(-0.75, 1.25) + np.array([0, 0.22, 0]))
        lB = M(r"c|B|", sc=0.52, color=BLEU).move_to(ax.c2p(-0.5, 1.25) + np.array([0, 0.22, 0]))
        tks = VGroup(*[T(t, sc=0.48, color=GRIS).next_to(ax.c2p(u, -0.12), DOWN, buff=0.07) for t, u in
                       [("$0$", 0), (r"$-3{,}1$", -0.25), (r"$-6{,}25$", -0.5), (r"$-9{,}4$", -0.75), (r"$-12{,}5$", -1)]])
        tz = T(r"$z$ (cm)", sc=0.48, color=GRIS).next_to(ax.c2p(0, -0.12), DOWN, buff=0.07).shift(0.45*DOWN + 0.1*LEFT)
        self.at(self.a("i5", "on additionne"), Create(fr), Create(bloc), run_time=0.6)
        m5 = self.etape(3, ORANGE, -0.72, M(r"\vec E = 2E_0\sin(kz)\sin(\omega t)\,\vec e_y", sc=0.72, color=ORANGE), self.a("i5", "Il vient"), rt=1.0)
        self.play(Create(enc(m5, col=ORANGE, buff=0.1)), Create(cE), FadeIn(lE), run_time=0.8)
        m6 = pos(M(r"\vec k_r = -k\,\vec e_z \;\Rightarrow\; \vec B_r = -\tfrac{E_0}{c}\cos(\omega t + kz)\,\vec e_x", sc=0.64), -5.85, -1.38)
        self.ecr(self.t("i6"), m6, rt=1.1)
        ns = pos(T(r"sur le miroir, $\vec B$ \textbf{double} !", sc=0.58, color=BLEU), 2.15, -1.85)
        self.ecr(self.a("i6", "sur le miroir"), ns, rt=0.7)
        self.at(self.a("i6", "Le champ magnétique double"), Create(cB), FadeIn(lB), run_time=0.8)
        m7 = pos(M(r"\vec B = -\tfrac{2E_0}{c}\cos(kz)\cos(\omega t)\,\vec e_x", sc=0.72, color=BLEU), -5.85, -2.05)
        self.ecr(self.t("i7"), m7, rt=1.0); self.play(Create(enc(m7, col=BLEU, buff=0.1)), run_time=0.4)
        nE = VGroup(*[Dot(ax.c2p(u, 0), radius=0.07, color=ORANGE) for u in (0, -0.5, -1)])
        nB = VGroup(*[Dot(ax.c2p(u, 0), radius=0.07, color=BLEU) for u in (-0.25, -0.75)])
        self.etape(4, ROUGE, -2.8, T(r"$\lambda = c/f = 12{,}5$ cm : nœuds de $\vec E$ en $z = 0$, puis tous les $6{,}25$ cm", sc=0.6), self.t("i8"), rt=1.1)
        self.at(self.a("i8", "sur la plaque"), FadeIn(tks), FadeIn(tz), FadeIn(nE), run_time=0.6)
        n9 = pos(T(r"nœuds de $\vec B$ : à $3{,}1$ cm, puis tous les $6{,}25$ cm (ventres de $\vec E$)", sc=0.6), -5.85, -3.42)
        self.at(self.t("i9"), Ecrire(n9, rt=1.1), FadeIn(nB), run_time=1.1)
        an = VGroup(Line(ax.c2p(-0.25, 0.38), ax.c2p(-0.25, 0.6), color=JAUNE, stroke_width=6), Line(ax.c2p(-0.25, 0.68), ax.c2p(-0.25, 0.9), color=JAUNE, stroke_width=6))
        r10 = pos(T(r"antenne à $\lambda/4 = 3{,}1$ cm", sc=0.66, color=JAUNE), 3.3, -2.45)
        self.at(self.t("i10"), Create(an), Ecrire(r10, rt=0.8), run_time=0.8); self.play(Create(enc(r10, col=JAUNE, buff=0.1)), run_time=0.4)
        r11 = T(r"amplitude $2E_0 = 4{,}0$ V$\cdot$m$^{-1}$", sc=0.6, color=VERT).next_to(r10, DOWN, buff=0.28, aligned_edge=LEFT)
        self.ecr(self.t("i11"), r11, rt=0.8)
        self.fin()

# ---------------------------------------------------------------- S9
class S9(C):
    sid = "S9"
    def construct(self):
        self.entete(r"Exercice 2 -- courants et énergie", "Solution")
        self.rappel(r"$\vec E = 2E_0\sin(kz)\sin(\omega t)\,\vec e_y$, \; $\vec B = -(2E_0/c)\cos(kz)\cos(\omega t)\,\vec e_x$")
        xs = 5.3
        bloc = metal(xs, 6.4, 0.05, 2.35, face=xs)
        fn = fleche((xs, 2.0), (xs - 0.95, 2.0), col=CRAIE, sw=3, tl=0.13); ln = M(r"\vec n = -\vec e_z", sc=0.55).next_to(fn.get_end(), LEFT, buff=0.08)
        bm = odot(xs - 0.5, 1.2, col=BLEU, r=0.13); lbm = M(r"\vec B(0)", sc=0.55, color=BLEU).next_to(bm, LEFT, buff=0.1)
        js = fleche((xs - 0.13, 0.25), (xs - 0.13, 0.95), col=VERT, sw=4, tl=0.14); ljs = M(r"\vec j_s", sc=0.58, color=VERT).next_to(js, LEFT, buff=0.1)
        rp = repere_zyx(2.55, 0.35, l=0.42, horiz="z", vert="y", sort="x", entrant=True)
        m1 = self.etape(5, BLEU, 2.2, M(r"\vec n = -\vec e_z", sc=0.75), self.a("j1", "On oriente"), rt=0.6)
        m1b = T(r"(sortante du métal, vers le vide)", sc=0.58, color=GRIS).next_to(m1, RIGHT, buff=0.3)
        self.at(self.a("j1", "moins e z"), FadeIn(m1b), Create(bloc), GrowArrow(fn), FadeIn(ln), FadeIn(rp), run_time=0.8)
        m2 = pos(M(r"\vec j_s = \vec n \wedge \vec B(0)/\mu_0", sc=0.74), -5.85, 1.52)
        self.at(self.a("j2", "j s égale"), Ecrire(m2, rt=0.9), FadeIn(bm), FadeIn(lbm), run_time=0.9)
        m3 = pos(M(r"\vec j_s = \tfrac{2E_0}{\mu_0 c}\cos(\omega t)\,\vec e_y", sc=0.76, color=VERT), -5.85, 0.82)
        self.at(self.a("j3", "j s est selon e y"), Ecrire(m3, rt=1.0), GrowArrow(js), FadeIn(ljs), run_time=1.0)
        self.play(Create(enc(m3, col=VERT, buff=0.1)), run_time=0.4)
        m4 = pos(T(r"$\vec j_s \parallel \vec E_i$ \; ; \; amplitude $2\varepsilon_0 c E_0 \approx 11$ mA$\cdot$m$^{-1}$", sc=0.62), -5.85, 0.02)
        self.ecr(self.t("j4"), m4, rt=1.1)
        m5 = pos(M(r"\vec E(0) = \vec 0 \;\Rightarrow\; \sigma_s = 0", sc=0.7), -5.85, -0.65)
        self.ecr(self.t("j5"), m5, rt=0.8)
        self.etape(6, ORANGE, -1.4, M(r"\vec\Pi = \vec E\wedge\vec B/\mu_0 = \tfrac{E_0^2}{\mu_0 c}\sin(2kz)\sin(2\omega t)\,\vec e_z", sc=0.68), self.a("j6", "Avec les champs réels"), rt=1.3)
        m7 = pos(M(r"\langle\vec\Pi\rangle = \vec 0", sc=0.8, color=JAUNE), -5.85, -2.12)
        m7b = T(r"aucun transport d'énergie en moyenne", sc=0.58, color=GRIS).next_to(m7, RIGHT, buff=0.45)
        self.ecr(self.a("j6", "sa moyenne est nulle"), m7, rt=0.6); self.play(Create(enc(m7, col=JAUNE, buff=0.1)), FadeIn(m7b), run_time=0.4)
        self.etape(7, JAUNE, -2.85, M(r"\langle\Pi_i\rangle = \langle\Pi_r\rangle = \varepsilon_0 c E_0^2/2 \approx 5{,}3\ \mathrm{mW\cdot m^{-2}}", sc=0.66), self.a("j8", "l'onde incidente"), rt=1.2)
        m9 = pos(T(r"miroir parfait : rien d'absorbé \; ; \; $\vec\Pi$ instantané $\neq \vec 0$ : va-et-vient", sc=0.6, color=GRIS), -5.85, -3.52)
        self.ecr(self.t("j9"), m9, rt=1.1)
        self.fin()

# ---------------------------------------------------------------- S10
class S10(C):
    sid = "S10"
    def construct(self):
        self.entete(r"Exercice 3 -- la cavité d'un four à micro-ondes", "Énoncé")
        x0, x1 = -5.55, -1.65
        mg = metal(x0 - 0.35, x0, 0.85, 2.55, face=x0); md = metal(x1, x1 + 0.35, 0.85, 2.55, face=x1)
        axz = DashedLine(P(x0, 1.1), P(x1 + 0.75, 1.1), color=GRIS, stroke_width=1.5, dash_length=0.08)
        lzz = M(r"z", sc=0.55, color=GRIS).move_to([x1 + 0.9, 1.3, 0])
        l0 = T(r"$0$", sc=0.55, color=GRIS).move_to([x0, 0.62, 0]); lL = T(r"$L$", sc=0.55, color=GRIS).move_to([x1, 0.62, 0])
        mag = Rectangle(width=1.6, height=0.42, color=CRAIE, stroke_width=2.5).move_to([(x0 + x1)/2, 2.15, 0])
        lmag = T(r"magnétron", sc=0.48).move_to(mag)
        cd = DoubleArrow(P(x0, 0.3), P(x1, 0.3), buff=0, color=GRIS, stroke_width=2, tip_length=0.1, max_tip_length_to_length_ratio=0.2)
        lcd = T(r"$L$ ?", sc=0.55, color=GRIS).next_to(cd, DOWN, buff=0.06)
        self.at(self.t("k1"), Create(mg), Create(md), Create(axz), FadeIn(lzz), run_time=1.0)
        self.at(self.a("k2", "Deux parois"), FadeIn(l0), FadeIn(lL), run_time=0.5)
        d1 = pos(T(r"$f = 2{,}45$ GHz, \; $c = 3{,}00\cdot10^{8}$ m$\cdot$s$^{-1}$", sc=0.66), 0.0, 2.25)
        self.at(self.a("k2", "Le magnétron"), Create(mag), FadeIn(lmag), Ecrire(d1, rt=0.9), run_time=0.9)
        d2 = pos(M(r"\vec E = E_m\sin(kz)\cos(\omega t)\,\vec e_x, \quad \omega = kc", sc=0.68), 0.0, 1.62)
        self.ecr(self.t("k3"), d2, rt=1.0)
        q1 = pos(T(r"Q1. Fréquences propres $f_n$ de la cavité ?", sc=0.66), -6.2, -0.72)
        q2 = pos(T(r"Q2. $L$ entre 28 et 32 cm pour accorder la cavité ? Ordre $n$ du mode ?", sc=0.66), -6.2, -1.24)
        q3 = pos(T(r"Q3. Où sont les points chauds ? Pourquoi le plateau tourne-t-il ?", sc=0.66), -6.2, -1.76)
        q4 = pos(T(r"Q4. Parois réelles : modèle parfait justifié ? Le four fuit-il ?", sc=0.66), -6.2, -2.28)
        self.ecr(self.t("k4"), q1, rt=0.9)
        self.at(self.t("k5"), Ecrire(q2, rt=1.1), Create(cd), FadeIn(lcd), run_time=1.1)
        self.ecr(self.t("k6"), q3, rt=1.0)
        d3 = pos(T(r"parois en inox : $\sigma = 1{,}4\cdot10^{6}$ S$\cdot$m$^{-1}$, épaisseur $0{,}5$ mm", sc=0.6, color=GRIS), 0.0, 1.0)
        self.at(self.t("k7"), Ecrire(d3, rt=1.0), run_time=1.0)
        self.ecr(self.a("k7", "Le modèle parfait"), q4, rt=1.0)
        bx = SurroundingRectangle(VGroup(q1, q2, q3, q4), color=ROUGE, buff=0.16, corner_radius=0.08)
        self.play(Create(bx), run_time=0.4)
        rf = pos(T(r"Réfléchissons : \textbf{deux} conditions aux limites ; point chaud = ventre de $\vec E$", sc=0.62, color=BLEU), -6.2, -3.0)
        self.ecr(self.t("k8"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-1.0, -3.6, 0])
        self.ecr(self.t("k9"), av, rt=0.7)
        self.pause5(self.PH["k9"]["fin"], 2.3, -3.6)
        self.fin()

# ---------------------------------------------------------------- S11
class S11(C):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice 3 -- modes et points chauds", "Solution")
        self.rappel(r"$f = 2{,}45$ GHz, \; $L$ entre 28 et 32 cm")
        x0, x1, yc = 1.75, 6.25, 1.25
        Lb = x1 - x0
        mg = metal(x0 - 0.32, x0, yc - 1.0, yc + 1.0, face=x0); md = metal(x1, x1 + 0.32, yc - 1.0, yc + 1.0, face=x1)
        l0 = T(r"$0$", sc=0.52, color=GRIS).move_to([x0, yc - 1.2, 0]); lL = T(r"$L$", sc=0.52, color=GRIS).move_to([x1, yc - 1.2, 0])
        axz = DashedLine(P(x0, yc), P(x1, yc), color=GRIS, stroke_width=1.5, dash_length=0.08)
        self.etape(1, BLEU, 2.2, T(r"$\vec E$ tangent aux parois : nul en $z = 0$ et en $z = L$", sc=0.62), self.t("l1"), rt=1.0)
        self.at(self.a("l1", "il doit s'y annuler"), Create(mg), Create(md), Create(axz), FadeIn(l0), FadeIn(lL), run_time=0.8)
        a2 = pos(T(r"$z = 0$ : automatique \; ; \; $z = L$ :", sc=0.62, color=GRIS), -5.85, 1.55)
        a2b = M(r"\sin(kL) = 0", sc=0.75).next_to(a2, RIGHT, buff=0.25)
        self.ecr(self.a("l1", "En z égale zéro"), a2, rt=0.8)
        self.ecr(self.a("l1", "il faut sinus"), a2b, rt=0.6)
        a3 = pos(M(r"k_n L = n\pi, \quad n \in \mathbb{N}^*", sc=0.72), -5.85, 0.92)
        a3b = T(r"($n = 0$ : champ nul)", sc=0.56, color=GRIS).next_to(a3, RIGHT, buff=0.35)
        self.ecr(self.t("l3"), a3, rt=0.8); self.ecr(self.a("l3", "Le cas n égale zéro"), a3b, rt=0.6)
        a4 = pos(M(r"f_n = n\,\frac{c}{2L}", sc=0.85, color=JAUNE), -5.85, 0.22)
        a4b = T(r"écart constant $c/(2L)$", sc=0.56, color=GRIS).next_to(a4, RIGHT, buff=0.45)
        self.ecr(self.a("l4", "f n égale"), a4, rt=0.7); self.play(Create(enc(a4, col=JAUNE, buff=0.1)), FadeIn(a4b), run_time=0.4)
        self.etape(2, VERT, -0.55, M(r"L = n\,\lambda/2, \quad \lambda = c/f = 12{,}24\ \mathrm{cm}", sc=0.7), self.a("l5", "L doit valoir"), rt=1.0)
        alt = pos(T(r"$n = 4$ : $24{,}5$ cm \; ; \; $n = 6$ : $36{,}7$ cm", sc=0.56, color=GRIS), 1.85, -0.55)
        self.ecr(self.a("l6", "un seul multiple"), alt, rt=0.8)
        a6 = pos(M(r"n = 5 \;\Rightarrow\; L = 30{,}6\ \mathrm{cm}", sc=0.78, color=VERT), -5.85, -1.25)
        mode = onde(lambda x: yc + 0.8*np.sin(5*PI*(x - x0)/Lb), x0, x1, col=ORANGE)
        mode2 = onde(lambda x: yc - 0.8*np.sin(5*PI*(x - x0)/Lb), x0, x1, col=ORANGE, sw=2, tirets=True)
        lmo = T(r"mode $n = 5$", sc=0.52, color=ORANGE).move_to([(x0 + x1)/2, yc - 1.2, 0])
        self.at(self.a("l6", "n égale cinq"), Ecrire(a6, rt=0.8), Create(mode), Create(mode2), FadeIn(lmo), run_time=1.0)
        self.play(Create(enc(a6, col=VERT, buff=0.1)), run_time=0.4)
        a7 = pos(M(r"f_5 = 5c/(2L) \approx 2{,}45\ \mathrm{GHz}", sc=0.72), -5.85, -1.98)
        ok = coche(-1.1, -1.98)
        self.ecr(self.t("l7"), a7, rt=0.8)
        self.at(self.a("l7", "redonne bien"), Create(ok), run_time=0.4)
        self.etape(3, ORANGE, -2.7, T(r"points chauds = \textbf{ventres} de $\vec E$ : $\sin(kz) = \pm 1$", sc=0.62), self.t("l8"), rt=1.0)
        a9 = pos(T(r"$z = 3{,}1$ ; $9{,}2$ ; $15{,}3$ ; $21{,}4$ ; $27{,}6$ cm : \textbf{cinq} ventres", sc=0.62, color=ROUGE), -5.85, -3.35)
        vs = VGroup(*[Dot(P(x0 + (2*p + 1)*Lb/10, yc + 0.8*(-1)**p), radius=0.1, color=ROUGE) for p in range(5)])
        self.at(self.t("l9"), Ecrire(a9, rt=1.3), FadeIn(vs), run_time=1.3)
        nn = VGroup(*[Dot(P(x0 + p*Lb/5, yc), radius=0.07, color=GRIS) for p in range(6)])
        t10 = VGroup(T(r"nœuds (tous les $6{,}1$ cm) : froid", sc=0.6, color=GRIS),
                     T(r"plateau tournant :", sc=0.6, color=JAUNE), T(r"ventres $\leftrightarrow$ nœuds", sc=0.6, color=JAUNE)).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        pos(t10, 2.1, -1.75)
        self.at(self.t("l10"), FadeIn(nn), Ecrire(t10[0], rt=0.9), run_time=0.9)
        self.at(self.a("l10", "d'où le plateau"), Ecrire(t10[1], rt=0.5), Ecrire(t10[2], rt=0.6), run_time=0.9)
        self.fin()

# ---------------------------------------------------------------- S12
class S12(C):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice 3 -- des parois réelles", "Solution")
        self.rappel(r"inox : $\sigma = 1{,}4\cdot10^{6}$ S$\cdot$m$^{-1}$, \; paroi de $0{,}5$ mm, \; $L = 30{,}6$ cm")
        self.etape(4, BLEU, 2.2, M(r"\delta = 1/\sqrt{\pi\mu_0\sigma f}", sc=0.74), self.a("m1", "Quatrième étape"), rt=0.8)
        b2 = pos(M(r"\delta \approx 8{,}6\ \mu\mathrm{m}", sc=0.8, color=VERT), -5.85, 1.45)
        self.ecr(self.a("m1", "vaut huit virgule six"), b2, rt=0.6); self.play(Create(enc(b2, col=VERT, buff=0.1)), run_time=0.4)
        b3 = pos(M(r"\frac{\lambda}{\delta} \approx 14\,000", sc=0.72), -5.85, 0.68)
        b3b = T(r"conducteur parfait : justifié", sc=0.6, color=VERT).next_to(b3, RIGHT, buff=0.4)
        self.ecr(self.t("m3"), b3, rt=0.7); self.ecr(self.a("m3", "Vue de l'onde"), b3b, rt=0.8)
        b4 = pos(T(r"paroi : $0{,}5$ mm $\approx 58\,\delta$", sc=0.66), -5.85, -0.05)
        self.ecr(self.t("m4"), b4, rt=0.8)
        # la paroi vue de près : amplitude en e^{-z/delta}
        xw, xe = 3.2, 6.45; yb, A = 0.45, 1.55
        sl = metal(xw, xe, yb - 0.25, yb + 1.95, face=xw)
        dec = onde(lambda x: yb + A*np.exp(-(x - xw)/0.3), xw, xw + 2.3, col=ROUGE, sw=4)
        cav = onde(lambda x: yb + A*abs(np.cos(2*PI*(x - xw)/2.4)), 1.35, xw, col=BLEU, sw=3)
        ld = T(r"$\propto e^{-z/\delta}$", sc=0.56, color=ROUGE).move_to([xw + 1.25, yb + 1.0, 0])
        ld = VGroup(BackgroundRectangle(ld, color="#1F2A24", fill_opacity=0.92, buff=0.06), ld)
        lc = T(r"cavité : $c|B|$", sc=0.52, color=BLEU).move_to([2.3, yb + 1.85, 0])
        le = T(r"après $58\,\delta$ : $\approx 0$", sc=0.52, color=CRAIE).move_to([5.45, yb + 0.25, 0])
        le = VGroup(BackgroundRectangle(le, color="#1F2A24", fill_opacity=0.92, buff=0.06), le)
        self.at(self.a("m4", "La paroi fait"), Create(sl), Create(cav), FadeIn(lc), run_time=0.8)
        self.play(Create(dec), FadeIn(ld), run_time=0.7)
        self.at(self.a("m4", "cinquante-huit"), FadeIn(le), run_time=0.4)
        b5 = pos(M(r"e^{-58} \approx 10^{-25}", sc=0.8, color=JAUNE), -5.85, -0.78)
        b5b = T(r"rien ne sort !", sc=0.66, color=JAUNE).next_to(b5, RIGHT, buff=0.4)
        self.ecr(self.t("m5"), b5, rt=0.7)
        self.at(self.a("m5", "Rien ne sort"), FadeIn(b5b), Create(enc(b5, col=JAUNE, buff=0.1)), run_time=0.4)
        # peigne des modes
        ax, fr = cadre(4.15, -1.65, 4.6, 0.9, 0, 3.3, 0, 1)
        base = Line(ax.c2p(0, 0.2), ax.c2p(3.3, 0.2), color=GRIS, stroke_width=2)
        df = 0.4902
        tk = VGroup(*[Line(ax.c2p(n*df, 0.2), ax.c2p(n*df, 0.75), color=(VERT if n == 5 else CRAIE), stroke_width=(5 if n == 5 else 3)) for n in range(1, 7)])
        tl = VGroup(*[T(t, sc=0.46, color=GRIS).next_to(ax.c2p(n*df, 0.2), DOWN, buff=0.08) for t, n in ((r"$1{,}96$", 4), (r"$2{,}45$", 5), (r"$2{,}94$", 6))])
        tf = T(r"$f$ (GHz)", sc=0.46, color=GRIS).next_to(ax.c2p(1.0, 0.2), DOWN, buff=0.08)
        fm = fleche((ax.c2p(5*df, 1.35)[0], ax.c2p(5*df, 1.35)[1]), (ax.c2p(5*df, 0.82)[0], ax.c2p(5*df, 0.82)[1]), col=JAUNE, sw=4, tl=0.13)
        lfm = T(r"magnétron", sc=0.48, color=JAUNE).next_to(fm.get_start(), LEFT, buff=0.1)
        self.etape(5, JAUNE, -1.55, T(r"modes espacés de $c/(2L) \approx 490$ MHz", sc=0.64), self.t("m6"), rt=0.9)
        self.at(self.a("m6", "les modes voisins"), Create(base), Create(tk), FadeIn(tf), run_time=0.8)
        b6 = pos(T(r"voisins à $1{,}96$ et $2{,}94$ GHz : loin du magnétron", sc=0.6), -5.85, -2.2)
        self.at(self.a("m6", "sont loin"), Ecrire(b6, rt=1.0), FadeIn(tl), GrowArrow(fm), FadeIn(lfm), run_time=1.0)
        cc = T(r"un four = une \textbf{cavité accordée}, gardée par l'\textbf{effet de peau}", sc=0.7, color=JAUNE).move_to([0, -3.55, 0])
        self.ecr(self.t("m8"), cc, rt=1.1)
        self.play(Create(enc(cc, col=JAUNE, buff=0.12)), run_time=0.4)
        self.fin()

# ---------------------------------------------------------------- S13
class S13(C):
    sid = "S13"
    def construct(self):
        self.entete(r"Ce qu'il faut retenir", "Méthode")
        t0 = pos(T(r"la méthode : une onde face à un \textbf{conducteur}", sc=0.74, color=GRIS), -6.3, 2.2)
        self.ecr(self.t("n1"), t0, rt=0.9)
        pts = [("n2", r"\textbf{le modèle} : ohmique (ARQS, $\varepsilon_0\omega \ll \sigma$) ou parfait ($\delta \ll$ les autres longueurs)", BLEU, 1.4),
               ("n3", r"ohmique : $\delta = \sqrt{2/(\mu_0\sigma\omega)}$, amplitude en $e^{-z/\delta}$ \; (piège : $\omega$, pas $f$)", VERT, 0.5),
               ("n4", r"parfait : $\vec E$ tangent \textbf{nul} $\Rightarrow$ onde réfléchie ($r = -1$), somme en onde stationnaire", ORANGE, -0.4),
               ("n5", r"$\vec B$ onde par onde (relation de structure), puis $\sigma_s$ et $\vec j_s$ avec $\vec n$ \textbf{sortante}", ROUGE, -1.3),
               ("n6", r"cavité : un nœud de $\vec E$ sur chaque paroi $\Rightarrow$ $L = n\,\lambda/2$", JAUNE, -2.2)]
        for k, (ph_, txt, c, yy) in enumerate(pts):
            ca = carte(k+1, c, -5.9, yy); tx = pos(T(txt, sc=0.64), -5.35, yy)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.1), run_time=1.0)
        vf = pos(T(r"et toujours \textbf{vérifier} : unités, signes, ordres de grandeur", sc=0.66, color=JAUNE), -5.35, -2.8)
        self.ecr(self.a("n6", "Et toujours vérifier"), vf, rt=1.0)
        self.fin()

# ---------------------------------------------------------------- S14
class S14(C):
    sid = "S14"
    def construct(self):
        self.entete(r"Conclusion du cours", "Bilan")
        t0 = pos(T(r"l'électromagnétisme en \textbf{cinq vidéos}", sc=0.74, color=GRIS), -6.3, 2.2)
        self.ecr(self.t("o1"), t0, rt=0.9)
        vids = [(r"\textbf{Électrostatique} : les charges créent $\vec E$ \; -- \; théorème de Gauss", BLEU, ("o2", "Les charges créent")),
                (r"\textbf{Magnétostatique} : les courants créent $\vec B$ \; -- \; théorème d'Ampère", VERT, ("o2", "Les courants créent")),
                (r"\textbf{Maxwell} : $\vec E$ et $\vec B$ couplés \; -- \; ARQS et énergie", ORANGE, ("o3", "Les équations de Maxwell")),
                (r"\textbf{Ondes dans le vide} : propagation à la vitesse $c$", ROUGE, ("o3", "Et elles prédisent")),
                (r"\textbf{Ondes et conducteurs} : effet de peau, réflexion, cavités", JAUNE, ("o4", "Enfin"))]
        ys = [1.35, 0.5, -0.35, -1.2, -2.05]
        prev = None
        for k, ((txt, c, (ph_, fr_)), yy) in enumerate(zip(vids, ys)):
            ca = carte(k+1, c, -5.9, yy); tx = pos(T(txt, sc=0.66), -5.35, yy)
            an = [Line(P(-5.9, ys[k-1] - 0.29), P(-5.9, yy + 0.29), color=GRIS, stroke_width=2)] if k else []
            self.at(self.a(ph_, fr_), *[Create(a) for a in an], Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=0.9), run_time=0.9)
        br = T(r"\textbf{Bonnes révisions, et à bientôt !}", sc=0.95, color=JAUNE).move_to([0, -3.2, 0])
        self.ecr(self.t("o5"), br, rt=0.8)
        self.fin()
