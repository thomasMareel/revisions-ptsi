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
def P(x, y): return np.array([x, y, 0.0])
def fleche(a, b, col=ROUGE, sw=4, tl=0.18):
    return Arrow(P(*a), P(*b), buff=0, color=col, stroke_width=sw, tip_length=tl, max_tip_length_to_length_ratio=0.5, max_stroke_width_to_length_ratio=20)
def sep(y): return Line([-6.6, y, 0], [6.6, y, 0], color=GRIS, stroke_width=1.5, stroke_opacity=0.5)
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
    h = y1 - y0; g = VGroup(); u = x0 - h
    while u < x1:
        a = (max(u, x0), y0 + max(0, x0 - u)); b = (min(u + h, x1), y0 + min(h, x1 - u))
        if b[0] > a[0]: g.add(Line(P(*a), P(*b), color=col, stroke_width=sw))
        u += pas
    return g

# ---------- couleurs des grandeurs de l'onde
CE, CB, CU = ROUGE, BLEU, VERT
DPROF = np.array([-0.42, -0.36, 0.0])   # direction « vers l'observateur » (perspective cavalière)

def onde3d(x0, x1, y0, A=0.8, lam=2.2, nfl=10, phase=0.0, ab=0.85):
    """instantané d'une OPP polarisée rectilignement, propagation vers la droite (u) :
    E vertical (dans le tableau), B = u ^ E / c dessiné en perspective (vers l'observateur), en phase"""
    k = 2*PI/lam
    zs = np.linspace(x0, x1, 240); e = A*np.cos(k*(zs - x0) + phase)
    axe = Line(P(x0, y0), P(x1, y0), color=GRIS, stroke_width=2)
    Ec = VMobject(color=CE, stroke_width=3.5).set_points_smoothly([P(z, y0 + v) for z, v in zip(zs, e)])
    Bc = VMobject(color=CB, stroke_width=3.5).set_points_smoothly([P(z, y0, ) + ab*v*DPROF for z, v in zip(zs, e)])
    pts = np.linspace(x0, x1, nfl + 1)[:-1] + (x1 - x0)/(2*nfl)
    Ef, Bf = VGroup(), VGroup()
    for z in pts:
        v = A*np.cos(k*(z - x0) + phase)
        if abs(v) < 0.18: continue
        Ef.add(Arrow(P(z, y0), P(z, y0 + v), buff=0, color=CE, stroke_width=2.5, tip_length=0.1, max_tip_length_to_length_ratio=0.35))
        Bf.add(Arrow(P(z, y0), P(z, y0) + ab*v*DPROF, buff=0, color=CB, stroke_width=2.5, tip_length=0.1, max_tip_length_to_length_ratio=0.35))
    return dict(axe=axe, Ec=Ec, Bc=Bc, Ef=Ef, Bf=Bf, k=k)

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
        ti = T(r"\textbf{Électromagnétisme -- Chapitre 4}", sc=1.1, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Ondes électromagnétiques dans le vide", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-5.4, 1.3, 0], [5.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        o = onde3d(2.0, 6.1, -0.55, A=0.75, lam=2.05, nfl=12)
        fu = fleche((6.1, -0.55), (6.75, -0.55), col=CU, sw=4, tl=0.16)
        lu = M(r"\vec u", sc=0.62, color=CU).next_to(fu.get_end(), UP, buff=0.1)
        lE = M(r"\vec E", sc=0.62, color=CE).move_to([2.25, 0.45, 0])
        lB = M(r"\vec B", sc=0.62, color=CB).move_to([1.6, -1.05, 0])
        self.at(self.a("a2", "la lumière"), Create(o["axe"]), Create(o["Ec"]), Create(o["Bc"]), run_time=1.2)
        self.play(*[GrowArrow(f) for f in o["Ef"]], *[GrowArrow(f) for f in o["Bf"]], GrowArrow(fu), FadeIn(lu), FadeIn(lE), FadeIn(lB), run_time=0.9)
        items = []
        for k, (txt, col) in enumerate([("De Maxwell à la structure de l'onde", BLEU), ("Polarisation, énergie, spectre", VERT),
                                         ("Exercice 1 : lire une onde plane", ORANGE), ("Exercice 2 : une impulsion laser", ROUGE),
                                         ("Exercice 3 : une onde partiellement réfléchie", JAUNE)]):
            yy = 0.65 - 0.68*k
            items.append(VGroup(carte(k+1, col, -6.2, yy), pos(T(txt, sc=0.7), -5.65, yy)))
        for it, (sid, fr_) in zip(items, [("a3", "un cours express"), ("a3", "la polarisation"), ("a4", "lire une onde"),
                                          ("a4", "une impulsion laser"), ("a4", "une onde partiellement réfléchie")]):
            self.jusqua(self.a(sid, fr_)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

# ---------------------------------------------------------------- S1
class S1(C):
    sid = "S1"
    def construct(self):
        self.entete(r"4.1 -- Des équations de Maxwell à d'Alembert", "Cours")
        v = pos(T(r"\textbf{vide local} : $\rho = 0$, \; $\vec j = \vec 0$ \quad (les sources sont ailleurs)", sc=0.68), -6.3, 2.25)
        self.ecr(self.t("b1"), v, rt=1.0)
        m1 = pos(M(r"\operatorname{div}\vec E = 0 \qquad \operatorname{div}\vec B = 0", sc=0.8), -6.3, 1.55)
        m2 = pos(M(r"\overrightarrow{\operatorname{rot}}\,\vec E = -\frac{\partial\vec B}{\partial t} \qquad \overrightarrow{\operatorname{rot}}\,\vec B = \frac{1}{c^2}\,\frac{\partial\vec E}{\partial t}", sc=0.8), -6.3, 0.72)
        self.ecr(self.a("b2", "deux divergences"), m1, rt=0.9)
        self.ecr(self.a("b2", "deux rotationnels"), m2, rt=1.0)
        # couplage E <-> B
        cE = VGroup(Circle(radius=0.36, color=CE, stroke_width=3).move_to(P(3.0, 1.45)), M(r"\vec E", sc=0.75, color=CE).move_to(P(3.0, 1.45)))
        cB = VGroup(Circle(radius=0.36, color=CB, stroke_width=3).move_to(P(5.7, 1.45)), M(r"\vec B", sc=0.75, color=CB).move_to(P(5.7, 1.45)))
        a1 = ArcBetweenPoints(P(3.2, 1.78), P(5.5, 1.78), angle=-PI/2.6, color=VERT, stroke_width=3).add_tip(tip_length=0.15, tip_width=0.15)
        a2 = ArcBetweenPoints(P(5.5, 1.12), P(3.2, 1.12), angle=-PI/2.6, color=ORANGE, stroke_width=3).add_tip(tip_length=0.15, tip_width=0.15)
        l1 = T(r"(MA) : $\partial_t\vec E$ crée $\vec B$", sc=0.55, color=VERT).move_to(P(4.35, 2.45))
        l2 = T(r"(MF) : $\partial_t\vec B$ crée $\vec E$", sc=0.55, color=ORANGE).move_to(P(4.35, 0.42))
        self.at(self.a("b2", "couplent les champs"), Create(cE[0]), FadeIn(cE[1]), Create(cB[0]), FadeIn(cB[1]), run_time=0.6)
        self.at(self.a("b2", "une variation de B"), Create(a2), FadeIn(l2), run_time=0.7)
        self.at(self.a("b2", "une variation de E"), Create(a1), FadeIn(l1), run_time=0.7)
        dem = pos(T(r"$\overrightarrow{\mathrm{rot}}$ de (MF), \; $\overrightarrow{\mathrm{rot}}\,\overrightarrow{\mathrm{rot}}\,\vec E = \overrightarrow{\mathrm{grad}}\,(\mathrm{div}\,\vec E) - \vec\Delta\vec E$, \; avec $\mathrm{div}\,\vec E = 0$", sc=0.56, color=GRIS), -6.3, -0.12)
        self.ecr(self.t("b4"), dem, rt=1.3)
        da = pos(M(r"\vec\Delta\vec E - \frac{1}{c^2}\,\frac{\partial^2\vec E}{\partial t^2} = \vec 0", sc=0.8, color=JAUNE), -6.3, -0.95)
        self.ecr(self.t("b5"), da, rt=1.1); self.play(Create(enc(da, col=JAUNE, buff=0.13)), run_time=0.4)
        idb = pos(T(r"idem pour $\vec B$", sc=0.6, color=GRIS), da.get_right()[0] + 0.45, -0.95)
        self.ecr(self.a("b5", "Et de même pour B"), idb, rt=0.6)
        cc = pos(M(r"c = \frac{1}{\sqrt{\varepsilon_0\,\mu_0}} \approx 3{,}00\times10^{8}\ \mathrm{m\,s^{-1}}", sc=0.75), -6.3, -2.02)
        self.ecr(self.t("b6"), cc, rt=1.1)
        so = pos(M(r"\xi(x,t) = f\Big(t - \frac{x}{c}\Big) + g\Big(t + \frac{x}{c}\Big)", sc=0.8, color=ORANGE), -6.3, -2.95)
        self.ecr(self.t("b7"), so, rt=1.1)
        # profil qui se translate en bloc
        ax, fr = cadre(4.75, -2.2, 3.5, 1.9, 0, 5, -0.3, 1.9)
        prof = lambda s, s0: np.exp(-((s - s0)/0.28)**2) if s > s0 else np.exp(-((s - s0)/0.85)**2)
        p1 = DashedVMobject(crb(ax, lambda s: prof(s, 1.35), 0.05, 4.95, col=GRIS, sw=3), num_dashes=40)
        p2 = crb(ax, lambda s: prof(s, 3.35), 0.05, 4.95, col=ORANGE, sw=4)
        t1 = M(r"t_1", sc=0.5, color=GRIS).move_to(ax.c2p(0.5, 0.95)); t2 = M(r"t_2", sc=0.5, color=ORANGE).move_to(ax.c2p(4.1, 0.75))
        fc = Arrow(ax.c2p(1.45, 1.3), ax.c2p(3.25, 1.3), buff=0, color=VERT, stroke_width=2.5, tip_length=0.12)
        lc = M(r"c\,(t_2 - t_1)", sc=0.48, color=VERT).move_to(ax.c2p(2.35, 1.62))
        lx = M(r"x", sc=0.5, color=GRIS).next_to(fr, RIGHT, buff=0.08).shift(0.6*DOWN)
        self.at(self.t("b8"), Create(fr), Create(p1), FadeIn(t1), FadeIn(lx), run_time=0.8)
        self.at(self.a("b8", "avance en bloc"), TransformFromCopy(p1, p2), FadeIn(t2), run_time=1.0)
        self.play(GrowArrow(fc), FadeIn(lc), run_time=0.5)
        lf = T(r"$f$ : progressive \quad $g$ : en sens inverse", sc=0.52, color=GRIS).next_to(fr, DOWN, buff=0.12)
        self.ecr(self.a("b8", "Le terme g"), lf, rt=0.8)
        pl = pos(T(r"onde \textbf{plane} : surfaces d'onde = plans $\perp$ à une direction $\vec u$", sc=0.62, color=JAUNE), -6.3, -3.72)
        self.ecr(self.t("b9"), pl, rt=1.1)
        self.fin()

# ---------------------------------------------------------------- S2
class S2(C):
    sid = "S2"
    def construct(self):
        self.entete(r"4.2 -- Structure de l'onde plane progressive", "Cours")
        t0 = pos(T(r"d'Alembert ne suffit pas : Maxwell impose la \textbf{structure}", sc=0.62, color=GRIS), -6.3, 2.38)
        self.ecr(self.t("c2"), t0, rt=0.9)
        o = onde3d(-6.3, -1.45, 0.95, A=0.72, lam=2.4, nfl=11)
        fu = fleche((-1.45, 0.95), (-0.7, 0.95), col=CU, sw=4, tl=0.16)
        lu = M(r"\vec u", sc=0.65, color=CU).next_to(fu.get_end(), UP, buff=0.1)
        lE = M(r"\vec E", sc=0.62, color=CE).move_to([-6.05, 1.9, 0])
        lB = M(r"\vec B", sc=0.62, color=CB).move_to([-6.75, 0.45, 0])
        self.at(self.a("c2", "pour une onde plane"), Create(o["axe"]), Create(o["Ec"]), Create(o["Bc"]), GrowArrow(fu), FadeIn(lu), run_time=1.0)
        self.play(*[GrowArrow(f) for f in o["Ef"]], *[GrowArrow(f) for f in o["Bf"]], FadeIn(lE), FadeIn(lB), run_time=0.6)
        tv = pos(T(r"\textbf{transverses} : $\vec E\cdot\vec u = 0$, \; $\vec B\cdot\vec u = 0$", sc=0.66), 0.3, 1.98)
        self.ecr(self.a("c2", "les deux champs sont transverses"), tv, rt=1.0)
        rs = pos(M(r"\vec B = \frac{\vec u\wedge\vec E}{c}", sc=0.9, color=JAUNE), 0.45, 1.0)
        self.ecr(self.t("c3"), rs, rt=0.9); self.play(Create(enc(rs, col=JAUNE, buff=0.14)), run_time=0.4)
        cq = pos(T(r"$\vec E \perp \vec B$, \; $(\vec u, \vec E, \vec B)$ direct, \; $B = E/c$", sc=0.64), 0.3, 0.1)
        self.at(self.t("c4"), Ecrire(cq, rt=1.0), Indicate(fu, color=JAUNE), Indicate(o["Ef"][0], color=JAUNE), Indicate(o["Bf"][0], color=JAUNE), run_time=1.0)
        og = pos(T(r"$E = 1$ kV/m $\Rightarrow$ $B = 3\ \mu$T : force magnétique $\ll$ force électrique ($v \ll c$)", sc=0.58, color=GRIS), -6.3, -0.3)
        self.ecr(self.t("c5"), og, rt=1.2)
        self.play(Create(sep(-0.72)), run_time=0.3)
        lo = pos(T(r"\textbf{OPPM}", sc=0.66, color=ORANGE), -6.3, -1.2)
        f1 = pos(M(r"\xi = \xi_0\cos(\omega t - \vec k\cdot\vec r + \varphi)", sc=0.8), -5.0, -1.2)
        self.at(self.a("c6", "Cas idéal"), Ecrire(lo, rt=0.5), run_time=0.5)
        self.ecr(self.a("c6", "chaque composante"), f1, rt=1.0)
        f2 = pos(M(r"\vec k = k\,\vec u, \quad k = \frac{\omega}{c}, \quad \lambda = c\,T", sc=0.8), -6.3, -2.1)
        self.ecr(self.t("c7"), f2, rt=1.1)
        f2b = pos(T(r"$v_\varphi = \omega/k = c$ : vide non dispersif", sc=0.56, color=GRIS), -6.3, -2.85)
        self.ecr(self.a("c7", "avec k égale"), f2b, rt=0.8)
        f3 = pos(M(r"\underline{\vec E} = \underline{\vec E}_0\,e^{\,i(\omega t - \vec k\cdot\vec r)}", sc=0.8), 0.7, -1.18)
        f4 = pos(M(r"\partial_t \to i\omega \qquad \vec\nabla \to -i\vec k", sc=0.8), 0.7, -1.92)
        self.ecr(self.t("c8"), f3, rt=0.9)
        self.ecr(self.a("c8", "dériver revient"), f4, rt=1.0)
        f5 = pos(M(r"\vec k\cdot\underline{\vec E} = 0 \qquad \underline{\vec B} = \frac{\vec k\wedge\underline{\vec E}}{\omega}", sc=0.8, color=JAUNE), 0.7, -2.78)
        self.ecr(self.a("c8", "Maxwell donne alors"), f5, rt=1.1); self.play(Create(enc(f5, col=JAUNE, buff=0.12)), run_time=0.4)
        at = T(r"\textbf{une seule} onde plane progressive ! \; Somme d'ondes : \textbf{onde par onde}", sc=0.64, color=ROUGE).move_to([0, -3.68, 0])
        self.ecr(self.t("c10"), at, rt=1.1)
        self.fin()

# ---------------------------------------------------------------- S3
class S3(C):
    sid = "S3"
    def construct(self):
        self.entete(r"4.3 -- Polarisation et énergie", "Cours")
        p1 = pos(T(r"$\vec E$ vibre dans le plan d'onde ; direction fixe : \textbf{rectiligne}", sc=0.66), -6.3, 2.25)
        self.ecr(self.t("d1"), p1, rt=1.0)
        p2 = pos(M(r"\vec E = E_0\cos(\omega t - kz)\,\vec e_x", sc=0.85, color=CE), -6.3, 1.5)
        p2b = pos(T(r"(seule exigible)", sc=0.55, color=GRIS), p2.get_right()[0] + 0.3, 1.5)
        self.ecr(self.t("d2"), p2, rt=0.9)
        self.ecr(self.a("d2", "le seul cas"), p2b, rt=0.5)
        # polariseur
        cx, cy, R, al = 4.4, 1.05, 1.15, 0.62
        disque = Circle(radius=R, color=GRIS, stroke_width=2).set_fill(GRIS, 0.08).move_to(P(cx, cy))
        ua = np.array([np.sin(al), np.cos(al), 0])
        axe = DashedLine(P(cx, cy) - 1.1*R*ua, P(cx, cy) + 1.1*R*ua, color=JAUNE, stroke_width=2.5, dash_length=0.1)
        la = T("axe", sc=0.52, color=JAUNE).move_to(P(cx, cy) + 1.28*R*ua + 0.12*RIGHT)
        A = 0.95
        fE = Arrow(P(cx, cy), P(cx, cy + A), buff=0, color=CE, stroke_width=4, tip_length=0.15)
        lE = M(r"\vec E", sc=0.6, color=CE).next_to(fE.get_end(), LEFT, buff=0.1)
        ft = Arrow(P(cx, cy), P(cx, cy) + A*np.cos(al)*ua, buff=0, color=VERT, stroke_width=4, tip_length=0.15)
        pr = DashedLine(P(cx, cy + A), P(cx, cy) + A*np.cos(al)*ua, color=GRIS, stroke_width=1.5, dash_length=0.06)
        lt = M(r"E_0\cos\alpha", sc=0.52, color=VERT).move_to(P(cx + 1.0, cy + 0.42))
        arc = Arc(radius=0.42, start_angle=PI/2, angle=-al, arc_center=P(cx, cy), color=GRIS, stroke_width=2)
        lal = M(r"\alpha", sc=0.52, color=GRIS).move_to(P(cx, cy) + 0.6*np.array([np.sin(al/2), np.cos(al/2), 0]))
        self.at(self.t("d3"), Create(disque), Create(axe), FadeIn(la), GrowArrow(fE), FadeIn(lE), run_time=0.9)
        self.at(self.a("d3", "parallèle à son axe"), Create(pr), GrowArrow(ft), FadeIn(lt), Create(arc), FadeIn(lal), run_time=0.8)
        ml = pos(M(r"I = I_0\cos^2\alpha", sc=0.9, color=JAUNE), -6.3, 0.62)
        mlt = pos(T(r"loi de Malus", sc=0.6, color=GRIS), -3.4, 0.62)
        self.at(self.a("d3", "la loi de Malus"), Ecrire(ml, rt=0.8), FadeIn(mlt), run_time=0.8); self.play(Create(enc(ml, col=JAUNE, buff=0.12)), run_time=0.4)
        p4 = pos(T(r"2 extinctions par tour : rectiligne \; ; \; lumière naturelle : $I = I_0/2$", sc=0.6), -6.3, -0.15)
        self.ecr(self.t("d4"), p4, rt=1.1)
        self.play(Create(sep(-0.52)), run_time=0.3)
        e1 = pos(M(r"u_{em} = \frac{\varepsilon_0E^2}{2} + \frac{B^2}{2\mu_0} \qquad \vec\Pi = \frac{\vec E\wedge\vec B}{\mu_0}", sc=0.8), -6.3, -1.03)
        self.ecr(self.t("d5"), e1, rt=1.2)
        e2 = pos(M(r"\text{OPP : } u_{em} = \varepsilon_0E^2, \qquad \vec\Pi = c\,u_{em}\,\vec u", sc=0.8), -6.3, -1.93)
        self.ecr(self.t("d6"), e2, rt=1.1)
        e2b = pos(T(r"équipartition ; l'énergie avance à $c$", sc=0.56, color=GRIS), 1.5, -1.93)
        self.ecr(self.a("d6", "l'énergie avance"), e2b, rt=0.7)
        e3 = pos(M(r"\langle\cos^2\rangle = \tfrac12 \;\Rightarrow\; I = \|\langle\vec\Pi\rangle\| = \frac{\varepsilon_0\,c\,E_0^2}{2}", sc=0.82, color=JAUNE), -6.3, -2.8)
        self.ecr(self.a("d7", "En moyenne"), e3, rt=1.2); self.play(Create(enc(e3, col=JAUNE, buff=0.12)), run_time=0.4)
        e4 = pos(T(r"$\mu_0 c \approx 377\ \Omega$ : \; $I = E_0^2/(2 \times 377\ \Omega)$", sc=0.64), -6.3, -3.7)
        self.ecr(self.t("d8"), e4, rt=1.0)
        e5 = pos(T(r"jamais de produit de champs complexes !", sc=0.6, color=ROUGE), 1.0, -3.7)
        self.ecr(self.a("d8", "Et jamais"), e5, rt=0.8)
        self.fin()

# ---------------------------------------------------------------- S4
class S4(C):
    sid = "S4"
    def construct(self):
        self.entete(r"4.4 -- Spectre électromagnétique et limites du modèle", "Cours")
        t1 = pos(T(r"une seule théorie, du réseau à 50 Hz aux rayons $\gamma$ : \quad $\nu\,\lambda = c$", sc=0.66), -6.3, 2.3)
        self.ecr(self.t("e1"), t1, rt=1.0)
        # bande du spectre : log10(lambda) de 4 (10 km) à -13, lambda décroissante vers la droite
        X = lambda L: -6.3 + (4 - L)*12.6/17.0
        yb, hb = 1.05, 0.5
        doms = [(4, 0, "radio", GRIS, 0.10, "radio, RFID"), (0, -3, "micro-ondes", BLEU, 0.12, "Wi-Fi, four, radar"),
                (-3, -6.125, "infrarouge", ROUGE, 0.12, "caméra thermique"), (-6.125, -6.4, "", JAUNE, 0.9, ""),
                (-6.4, -8, "UV", VERT, 0.12, "germicide"), (-8, -11, "rayons X", ORANGE, 0.12, "radiographie"), (-11, -13, r"$\gamma$", GRIS, 0.18, "radiothérapie")]
        rects, labs, apps = [], [], []
        for a, b, nom, col, op, app in doms:
            r = Rectangle(width=X(b) - X(a), height=hb, stroke_width=1.5, color=GRIS).set_fill(col, op).move_to(P((X(a) + X(b))/2, yb))
            rects.append(r)
            labs.append(T(nom, sc=0.52).move_to(r) if nom else VMobject())
            apps.append(T(app, sc=0.5, color=GRIS).move_to(P((X(a) + X(b))/2, yb - 1.05)) if app else VMobject())
        lvis = T(r"visible : 400 à 750 nm", sc=0.52, color=JAUNE).move_to(P(X(-6.26) + 0.2, yb + 0.68))
        tvis = Line(P(X(-6.26), yb + 0.27), P(X(-6.26), yb + 0.52), color=JAUNE, stroke_width=2)
        ticks = VGroup(); tl = VGroup()
        for L, s in [(3, "1 km"), (0, "1 m"), (-3, "1 mm"), (-6, r"1 $\mu$m"), (-9, "1 nm"), (-12, "1 pm")]:
            ticks.add(Line(P(X(L), yb - hb/2), P(X(L), yb - hb/2 - 0.12), color=CRAIE, stroke_width=2))
            tl.add(T(s, sc=0.5).move_to(P(X(L), yb - hb/2 - 0.3)))
        ll = M(r"\lambda", sc=0.55, color=GRIS).move_to(P(6.55, yb - hb/2 - 0.3))
        self.at(self.a("e1", "seule change la fréquence"), *[Create(r) for r in rects], Create(ticks), FadeIn(tl), FadeIn(ll), run_time=1.1)
        self.at(self.t("e2"), FadeIn(labs[0]), FadeIn(apps[0]), run_time=0.3)
        self.at(self.a("e2", "micro-ondes"), FadeIn(labs[1]), FadeIn(apps[1]), run_time=0.3)
        self.at(self.a("e2", "infrarouge"), FadeIn(labs[2]), FadeIn(apps[2]), run_time=0.3)
        self.at(self.a("e2", "l'étroite bande du visible"), Create(tvis), FadeIn(lvis), Indicate(rects[3], color=JAUNE), run_time=0.5)
        self.at(self.a("e2", "l'ultraviolet"), FadeIn(labs[4]), FadeIn(apps[4]), run_time=0.3)
        self.at(self.a("e2", "les rayons X"), FadeIn(labs[5]), FadeIn(apps[5]), run_time=0.3)
        self.at(self.a("e2", "et les gamma"), FadeIn(labs[6]), FadeIn(apps[6]), run_time=0.3)
        rp = pos(T(r"repères : \; 1 GHz $\leftrightarrow$ 30 cm \quad ; \quad 500 nm $\leftrightarrow$ $6\times10^{14}$ Hz", sc=0.64, color=JAUNE), -6.3, -0.55)
        self.ecr(self.t("e4"), rp, rt=1.0)
        self.play(Create(sep(-1.0)), run_time=0.3)
        l1 = pos(T(r"l'OPPM : un modèle \textbf{idéal} (tout l'espace, de tout temps : énergie infinie)", sc=0.62), -6.3, -1.45)
        self.ecr(self.t("e5"), l1, rt=1.1)
        ax, fr = cadre(4.75, -2.45, 3.4, 1.5, 0, 5, -1.75, 1.25)
        env = lambda s: np.exp(-((s - 2.5)/0.85)**2)
        pq = crb(ax, lambda s: env(s)*np.cos(2*PI*s/0.28), 0.05, 4.95, col=ORANGE, sw=2.5, n=500)
        en = DashedVMobject(crb(ax, env, 0.05, 4.95, col=GRIS, sw=2), num_dashes=30)
        dt = DoubleArrow(ax.c2p(1.65, -1.4), ax.c2p(3.35, -1.4), buff=0, color=VERT, stroke_width=2, tip_length=0.1, max_tip_length_to_length_ratio=0.2)
        ldt = M(r"\Delta t", sc=0.5, color=VERT).next_to(dt, RIGHT, buff=0.08)
        l2 = pos(T(r"onde réelle : \textbf{paquet d'ondes} de durée $\Delta t$", sc=0.62), -6.3, -2.25)
        l3 = pos(M(r"\Delta\nu\,\Delta t \sim 1", sc=0.85, color=JAUNE), -6.3, -2.95)
        self.at(self.a("e5", "Une onde réelle"), Create(fr), Create(pq), Create(en), Ecrire(l2, rt=1.0), run_time=1.0)
        self.at(self.a("e5", "de largeur spectrale"), Ecrire(l3, rt=0.7), GrowFromCenter(dt), FadeIn(ldt), run_time=0.7)
        self.play(Create(enc(l3, col=JAUNE, buff=0.1)), run_time=0.3)
        l4 = pos(T(r"loin d'une source : onde sphérique \textbf{localement plane}", sc=0.62), -6.3, -3.65)
        self.ecr(self.t("e7"), l4, rt=1.0)
        px = T(r"\textbf{Place aux exercices !}", sc=0.8, color=JAUNE).move_to([4.75, -3.65, 0])
        self.ecr(self.a("e7", "Place aux exercices"), px, rt=0.6)
        self.fin()

# ---------------------------------------------------------------- S5
def repere_yz(x, y, l=0.75, col=GRIS):
    """e_y vers la droite, e_z vers le haut, e_x sortant du tableau"""
    ay = fleche((x, y), (x + l, y), col=col, sw=3, tl=0.13); az = fleche((x, y), (x, y + l), col=col, sw=3, tl=0.13)
    ly = M(r"\vec e_y", sc=0.52, color=col).next_to(ay.get_end(), RIGHT, buff=0.06)
    lz = M(r"\vec e_z", sc=0.52, color=col).next_to(az.get_end(), UP, buff=0.05)
    ox = odot(x, y, col=col, r=0.11); lx = M(r"\vec e_x", sc=0.52, color=col).next_to(ox, DL, buff=0.04)
    return VGroup(ay, az, ly, lz, ox, lx)

class S5(C):
    sid = "S5"
    def construct(self):
        self.entete(r"Exercice 1 -- lire une onde plane", "Énoncé")
        d0 = pos(T(r"Dans le vide :", sc=0.7), -6.3, 2.2)
        self.ecr(self.t("f1"), d0, rt=0.6)
        rp = repere_yz(4.6, 1.2)
        self.at(self.a("f1", "le champ électrique"), FadeIn(rp), run_time=0.6)
        fo = pos(M(r"\vec E = E_0\cos(\omega t + kx)\,\big(\vec e_y + \vec e_z\big)", sc=1.0, color=JAUNE), -6.3, 1.45)
        self.ecr(self.t("f2"), fo, rt=1.2)
        da = pos(T(r"$E_0 = 50$ V/m, \quad $\nu = 2{,}0\times10^{14}$ Hz, \quad $c = 3{,}0\times10^{8}$ m/s", sc=0.66), -6.3, 0.6)
        self.ecr(self.a("f2", "Les données"), da, rt=1.1)
        q1 = pos(T(r"Q1. Direction et sens de propagation, $\lambda$, domaine du spectre ?", sc=0.66), -6.0, -0.25)
        q2 = pos(T(r"Q2. État de polarisation ?", sc=0.66), -6.0, -0.8)
        q3 = pos(T(r"Q3. Champ magnétique $\vec B$ ?", sc=0.66), -6.0, -1.35)
        q4 = pos(T(r"Q4. Vérifier (MG) et (MF).", sc=0.66), -6.0, -1.9)
        self.ecr(self.t("f3"), q1, rt=1.0)
        self.ecr(self.t("f4"), q2, rt=0.6)
        self.ecr(self.a("f4", "le champ magnétique"), q3, rt=0.6)
        self.ecr(self.a("f4", "vérifier deux équations"), q4, rt=0.6)
        bx = SurroundingRectangle(VGroup(q1, q2, q3, q4), color=ROUGE, buff=0.18, corner_radius=0.08)
        self.play(Create(bx), run_time=0.4)
        rf = pos(T(r"Réfléchissons : le \textbf{sens} se lit dans la phase, la \textbf{polarisation} sur le vecteur", sc=0.62, color=BLEU), -6.3, -2.72)
        self.ecr(self.t("f5"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-1.0, -3.5, 0])
        self.ecr(self.t("f6"), av, rt=0.7)
        self.pause5(self.PH["f6"]["fin"], 2.3, -3.5)
        self.fin()

# ---------------------------------------------------------------- S6
class S6(C):
    sid = "S6"
    def construct(self):
        self.entete(r"Exercice 1 -- la solution", "Solution")
        self.rappel(r"$\vec E = E_0\cos(\omega t + kx)(\vec e_y + \vec e_z)$, \; $E_0 = 50$ V/m, \; $\nu = 2\cdot10^{14}$ Hz")
        sc = 0.64
        O = (4.4, 1.12)
        self.etape(1, BLEU, 2.15, T(r"phase $\omega t + kx$ constante : $x$ diminue quand $t$ augmente", sc=sc), self.a("g1", "Quand t augmente"), rt=1.0)
        g2 = pos(T(r"$\Rightarrow \vec u = -\vec e_x$ \quad (attention au signe !)", sc=sc, color=CU), -5.85, 1.57)
        self.ecr(self.a("g1", "u égale moins e x"), g2, rt=0.8)
        # figure : plan (e_y, e_z), u entrant
        ay = fleche(O, (O[0] + 1.1, O[1]), col=GRIS, sw=2.5, tl=0.12); az = fleche(O, (O[0], O[1] + 1.0), col=GRIS, sw=2.5, tl=0.12)
        lay = M(r"\vec e_y", sc=0.5, color=GRIS).next_to(ay.get_end(), RIGHT, buff=0.05); laz = M(r"\vec e_z", sc=0.5, color=GRIS).next_to(az.get_end(), LEFT, buff=0.06)
        ou = otimes(*O, col=CU, r=0.15); lu = M(r"\vec u = -\vec e_x", sc=0.52, color=CU).move_to(P(O[0] - 1.0, O[1] - 0.32))
        self.at(self.a("g1", "Attention au signe"), Create(ay), Create(az), FadeIn(lay), FadeIn(laz), FadeIn(ou), FadeIn(lu), run_time=0.8)
        g3 = pos(T(r"$\lambda = c/\nu = 1{,}5\ \mu$m : infrarouge (fibres optiques)", sc=sc), -5.85, 0.99)
        self.ecr(self.t("g3"), g3, rt=1.0)
        self.etape(2, VERT, 0.3, T(r"$E_y = E_z$, en phase : polarisation \textbf{rectiligne}", sc=sc), self.t("g4"), rt=1.0)
        g5 = pos(T(r"selon $\vec e_y + \vec e_z$ ($45^\circ$),", sc=sc), -5.85, -0.28)
        self.ecr(self.a("g4", "La polarisation est rectiligne"), g5, rt=0.8)
        fE = fleche(O, (O[0] + 0.72, O[1] + 0.72), col=CE, sw=4, tl=0.15); lE = M(r"\vec E", sc=0.6, color=CE).next_to(fE.get_end(), RIGHT, buff=0.06)
        self.at(self.a("g4", "à quarante-cinq degrés"), GrowArrow(fE), FadeIn(lE), run_time=0.6)
        g6 = pos(T(r"amplitude $E_0\sqrt2 \approx 71$ V/m", sc=sc, color=JAUNE), g5.get_right()[0] + 0.2, -0.28)
        self.ecr(self.t("g6"), g6, rt=0.8)
        g7 = pos(T(r"$\vec E\cdot\vec u = 0$ : onde transverse", sc=sc), -5.85, -0.86)
        self.ecr(self.t("g7"), g7, rt=0.8)
        self.play(Create(coche(g7.get_right()[0] + 0.35, -0.86)), run_time=0.3)
        sc3 = 0.66
        self.etape(3, ORANGE, -1.62, M(r"\vec B = \frac{\vec u\wedge\vec E}{c}, \qquad \vec u = -\vec e_x", sc=sc3), self.t("g8"), rt=0.9)
        g9 = pos(M(r"-\vec e_x\wedge\vec e_y = -\vec e_z, \qquad -\vec e_x\wedge\vec e_z = +\vec e_y", sc=sc3), -5.85, -2.38)
        self.ecr(self.t("g9"), g9, rt=1.1)
        g10 = pos(M(r"\vec B = \frac{E_0}{c}\cos(\omega t + kx)\,\big(\vec e_y - \vec e_z\big)", sc=0.7, color=VERT), -5.85, -3.2)
        self.ecr(self.t("g10"), g10, rt=1.1); self.play(Create(enc(g10, col=VERT, buff=0.12)), run_time=0.4)
        fB = fleche(O, (O[0] + 0.72, O[1] - 0.72), col=CB, sw=4, tl=0.15); lB = M(r"\vec B", sc=0.6, color=CB).next_to(fB.get_end(), RIGHT, buff=0.06)
        bm = T(r"$B_m = \sqrt2\,E_0/c \approx 0{,}24\ \mu$T", sc=0.58, color=CB).move_to(P(4.4, -0.05))
        self.at(self.a("g10", "d'amplitude"), GrowArrow(fB), FadeIn(lB), FadeIn(bm), run_time=0.7)
        rot = Arc(radius=0.45, start_angle=PI/4, angle=-PI/2, arc_center=P(*O), color=JAUNE, stroke_width=3).add_tip(tip_length=0.12, tip_width=0.12)
        self.at(self.t("g11"), Indicate(fE, color=JAUNE), run_time=0.5)
        self.at(self.a("g11", "B sur l'autre"), Indicate(fB, color=JAUNE), run_time=0.5)
        self.at(self.a("g11", "et u qui entre"), Indicate(ou, color=JAUNE, scale_factor=1.6), Create(rot), run_time=0.6)
        self.at(self.a("g11", "Il est bien direct"), Create(coche(6.0, 1.55)), run_time=0.4)
        # étape 4 : Maxwell (colonne droite)
        xr = 1.0; scr = 0.6
        self.etape(4, ROUGE, -0.8, T(r"(MG) : $\partial_y E_y + \partial_z E_z = 0$", sc=scr), self.t("g12"), rt=0.9, x=xr)
        self.play(Create(coche(5.15, -0.8)), run_time=0.3)
        r1 = pos(M(r"\overrightarrow{\operatorname{rot}}\,\vec E = k E_0\sin(\omega t + kx)\,\big(\vec e_y - \vec e_z\big)", sc=scr), xr + 0.5, -1.5)
        self.ecr(self.t("g13"), r1, rt=1.1)
        r2 = pos(M(r"= -\frac{\partial\vec B}{\partial t} \quad \text{car } \omega = kc \;:\; \text{(MF)}", sc=scr), xr + 0.85, -2.25)
        self.ecr(self.a("g13", "puisque oméga"), r2, rt=1.0)
        self.play(Create(coche(r2.get_right()[0] + 0.3, -2.25)), run_time=0.3)
        bl = VGroup(T(r"phase $\to$ sens \; ; \; vecteur $\to$ polarisation", sc=0.58, color=JAUNE),
                    T(r"structure $\to$ $\vec B$", sc=0.58, color=JAUNE)).arrange(DOWN, buff=0.12).move_to(P(3.95, -3.2))
        self.ecr(self.a("g14", "Bilan"), bl, rt=1.0); self.play(Create(enc(bl, col=JAUNE, buff=0.14)), run_time=0.4)
        self.fin()

# ---------------------------------------------------------------- S7
def paquet(x0, x1, y, a=0.17, per=0.16, col=ORANGE, sw=2.5):
    xs = np.linspace(x0, x1, 600); m = (x0 + x1)/2; s = (x1 - x0)/4.2
    return VMobject(color=col, stroke_width=sw).set_points_smoothly([P(x, y + a*np.exp(-((x - m)/s)**2)*np.cos(2*PI*(x - m)/per)) for x in xs])

class S7(C):
    sid = "S7"
    def construct(self):
        self.entete(r"Exercice 2 -- une impulsion laser", "Énoncé")
        yb = 1.6
        las = Rectangle(width=1.4, height=0.75, color=CRAIE, stroke_width=3).set_fill(CRAIE, 0.1).move_to(P(-5.6, yb)); ll = T("laser", sc=0.55).move_to(las)
        fx = VGroup(Line(P(-4.9, yb + 0.22), P(0.8, yb + 0.22), color=CE, stroke_width=2), Line(P(-4.9, yb - 0.22), P(0.8, yb - 0.22), color=CE, stroke_width=2))
        fond = Rectangle(width=5.7, height=0.44, stroke_width=0).set_fill(CE, 0.08).move_to(P(-2.05, yb))
        self.at(self.a("h1", "un laser impulsionnel"), Create(las), FadeIn(ll), Create(fx), FadeIn(fond), run_time=0.9)
        pk = paquet(-3.3, -0.5, yb)
        fc = fleche((0.85, yb), (1.55, yb), col=CU, sw=3, tl=0.14); lc = M(r"c", sc=0.6, color=CU).next_to(fc, UP, buff=0.06)
        self.at(self.t("h2"), Create(pk), GrowArrow(fc), FadeIn(lc), run_time=0.9)
        X = 2.4
        d1 = pos(T(r"$W = 10$ mJ", sc=0.68), X, 2.3); d2 = pos(T(r"$\tau = 10$ ns", sc=0.68), X, 1.75)
        d3 = pos(T(r"$\lambda = 1\,064$ nm", sc=0.68), X, 1.2)
        self.ecr(self.a("h2", "une énergie W"), d1, rt=0.5); self.ecr(self.a("h2", "une durée tau"), d2, rt=0.5)
        self.ecr(self.a("h2", "à la longueur d'onde"), d3, rt=0.5)
        cd = DoubleArrow(P(-4.4, yb - 0.22), P(-4.4, yb + 0.22), buff=0, color=GRIS, stroke_width=2, tip_length=0.08, max_tip_length_to_length_ratio=0.4)
        lcd = M(r"d", sc=0.52, color=GRIS).next_to(cd, LEFT, buff=0.05).shift(0.45*DOWN)
        d4 = pos(T(r"diamètre $d = 2{,}0$ mm", sc=0.68), X, 0.65)
        self.at(self.t("h3"), Create(cd), FadeIn(lcd), Ecrire(d4, rt=0.7), run_time=0.7)
        d5 = pos(T(r"faisceau assimilé à une OPPM polarisée rectilignement", sc=0.6, color=GRIS), -6.3, 0.65)
        d6 = pos(T(r"$\mu_0 c \approx 377\ \Omega$", sc=0.68), X, 0.1)
        self.at(self.a("h3", "est assimilé"), Ecrire(d5, rt=1.0), FadeIn(d6), run_time=1.0)
        q1 = pos(T(r"Q1. Éclairement $I$ pendant l'impulsion ?", sc=0.66), -6.0, -0.55)
        q2 = pos(T(r"Q2. Amplitudes $E_0$ et $B_0$ ?", sc=0.66), -6.0, -1.1)
        q3 = pos(T(r"Q3. $\langle u_{em}\rangle$, longueur de l'impulsion ; le modèle de l'OPPM est-il raisonnable ?", sc=0.66), -6.0, -1.65)
        self.ecr(self.t("h4"), q1, rt=0.7); self.ecr(self.a("h4", "Question deux"), q2, rt=0.6)
        self.ecr(self.t("h5"), q3, rt=1.2)
        bx = SurroundingRectangle(VGroup(q1, q2, q3), color=ROUGE, buff=0.18, corner_radius=0.08)
        self.play(Create(bx), run_time=0.4)
        rf = pos(T(r"Réfléchissons : puissance $\to$ éclairement (par la section) $\to$ $E_0$", sc=0.64, color=BLEU), -6.3, -2.6)
        self.ecr(self.t("h6"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-1.0, -3.45, 0])
        self.ecr(self.t("h7"), av, rt=0.7)
        self.pause5(self.PH["h7"]["fin"], 2.3, -3.45)
        self.fin()

# ---------------------------------------------------------------- S8
class S8(C):
    sid = "S8"
    def construct(self):
        self.entete(r"Exercice 2 -- la solution", "Solution")
        self.rappel(r"$W = 10$ mJ, \; $\tau = 10$ ns, \; $d = 2$ mm, \; $\lambda = 1\,064$ nm")
        sc = 0.66
        self.etape(1, BLEU, 2.15, M(r"P = \frac{W}{\tau} = \frac{10^{-2}}{10^{-8}} = 10^{6}\ \mathrm{W}", sc=sc), self.a("i1", "P égale W sur tau"), rt=1.0)
        self.etape(2, VERT, 1.25, M(r"S = \frac{\pi d^2}{4} \approx 3{,}1\ \mathrm{mm^2} = 3{,}1\times10^{-6}\ \mathrm{m^2}", sc=sc), self.a("i2", "on divise"), rt=1.1)
        i3 = pos(M(r"I = \frac{P}{S} \approx 3{,}2\times10^{11}\ \mathrm{W\,m^{-2}}", sc=sc, color=JAUNE), -5.85, 0.4)
        self.ecr(self.t("i3"), i3, rt=1.0); self.play(Create(enc(i3, col=JAUNE, buff=0.1)), run_time=0.3)
        i3b = pos(T(r"$\approx 2\times10^{8}$ fois le Soleil", sc=0.56, color=GRIS), i3.get_right()[0] + 0.3, 0.4)
        self.ecr(self.a("i3", "deux cents millions"), i3b, rt=0.7)
        self.etape(3, ORANGE, -0.45, M(r"E_0 = \sqrt{2\,\mu_0 c\, I}", sc=sc), self.a("i4", "on inverse"), rt=0.8)
        i5 = pos(M(r"E_0 \approx 1{,}5\times10^{7}\ \mathrm{V\,m^{-1}}", sc=0.7, color=VERT), -3.0, -0.45)
        self.ecr(self.t("i5"), i5, rt=0.9); self.play(Create(enc(i5, col=VERT, buff=0.1)), run_time=0.3)
        i6 = pos(T(r"piège : sans le 2 de la moyenne, $E_0$ serait $\sqrt2$ fois trop petit", sc=0.56, color=ROUGE), -5.85, -1.15)
        self.ecr(self.t("i6"), i6, rt=1.1)
        i7 = pos(M(r"B_0 = \frac{E_0}{c} \approx 0{,}05\ \mathrm{T} \approx 10^{3}\,B_{\text{terre}}", sc=sc, color=VERT), -5.85, -1.95)
        self.ecr(self.t("i7"), i7, rt=1.0)
        i8 = pos(T(r"$E_0 \ll E_{\text{atome}} \approx 5\times10^{11}$ V/m \; (30\,000 fois moins)", sc=0.58, color=GRIS), -5.85, -2.75)
        self.ecr(self.a("i8", "trente mille fois"), i8, rt=1.0)
        # colonne droite : énergie et bâton de lumière
        xr = 1.3
        self.etape(4, ROUGE, -0.3, M(r"\langle u_{em}\rangle = \frac{I}{c} \approx 1{,}1\times10^{3}\ \mathrm{J\,m^{-3}}", sc=0.62), self.a("i9", "la densité d'énergie"), rt=1.0, x=xr)
        y0 = 1.75; xa, xb = 2.0, 6.0
        bt = Rectangle(width=xb - xa, height=0.5, color=CE, stroke_width=2.5).set_fill(CE, 0.1).move_to(P((xa + xb)/2, y0))
        el = Ellipse(width=0.2, height=0.5, color=CE, stroke_width=2.5).move_to(P(xa, y0))
        osc = paquet(xa + 0.1, xb - 0.1, y0, a=0.17, per=0.2)
        fc = fleche((xb + 0.05, y0), (xb + 0.6, y0), col=CU, sw=3, tl=0.13); lc = M(r"c", sc=0.55, color=CU).next_to(fc, UP, buff=0.05)
        ls = M(r"S", sc=0.55, color=CE).next_to(el, LEFT, buff=0.08)
        cl = DoubleArrow(P(xa, y0 - 0.45), P(xb, y0 - 0.45), buff=0, color=GRIS, stroke_width=2, tip_length=0.1, max_tip_length_to_length_ratio=0.1)
        lcl = M(r"L = c\,\tau = 3\ \mathrm{m}", sc=0.55, color=GRIS).next_to(cl, DOWN, buff=0.06)
        self.at(self.t("i10"), Create(bt), Create(el), FadeIn(ls), Create(osc), GrowArrow(fc), FadeIn(lc), run_time=1.0)
        self.at(self.a("i10", "un bâton de lumière"), GrowFromCenter(cl), FadeIn(lcl), run_time=0.6)
        i11 = pos(M(r"\langle u_{em}\rangle\, S\, L \approx 10\ \mathrm{mJ} = W", sc=0.64, color=VERT), xr + 0.5, -1.05)
        self.ecr(self.t("i11"), i11, rt=1.2)
        i11b = pos(T(r"on retrouve l'énergie de l'impulsion", sc=0.56, color=GRIS), xr + 0.5, -1.65)
        self.ecr(self.a("i11", "On retrouve"), i11b, rt=0.9)
        self.play(Create(coche(i11b.get_right()[0] + 0.3, -1.65)), run_time=0.3)
        self.etape(5, JAUNE, -2.55, M(r"\frac{c\,\tau}{\lambda} \approx 3\times10^{6}\ \text{périodes}", sc=0.62), self.a("i12", "l'impulsion contient"), rt=1.0, x=xr)
        i12b = pos(T(r"quasi monochromatique : OPPM légitime", sc=0.54, color=VERT), xr + 0.5, -3.3)
        self.ecr(self.a("i12", "un paquet quasi"), i12b, rt=1.0)
        self.fin()

# ---------------------------------------------------------------- S9
E1, E2, LAM = 10.0, 5.0, 3.0   # V/m, V/m, cm
def amplE(z): return np.sqrt(E1**2 + E2**2 + 2*E1*E2*np.cos(4*PI*z/LAM))
def amplB(z): return np.sqrt(E1**2 + E2**2 - 2*E1*E2*np.cos(4*PI*z/LAM))
def cornet(x, y, col=CRAIE):
    return VGroup(Polygon(P(x - 0.45, y - 0.13), P(x + 0.25, y - 0.42), P(x + 0.25, y + 0.42), P(x - 0.45, y + 0.13), color=col, stroke_width=3).set_fill(col, 0.1),
                  Rectangle(width=0.35, height=0.26, color=col, stroke_width=3).move_to(P(x - 0.62, y)))
def ecran(x, y, h=1.3):
    return VGroup(Line(P(x, y - h/2), P(x, y + h/2), color=CRAIE, stroke_width=6), hachures(x, y - h/2, x + 0.25, y + h/2, pas=0.16))
def repere_zx(x, y, l=0.6, col=GRIS):
    """e_z vers la droite, e_x vers le haut, e_y sortant"""
    az = fleche((x, y), (x + l, y), col=col, sw=3, tl=0.12); ax_ = fleche((x, y), (x, y + l), col=col, sw=3, tl=0.12)
    lz = M(r"\vec e_z", sc=0.5, color=col).next_to(az.get_end(), RIGHT, buff=0.05); lx = M(r"\vec e_x", sc=0.5, color=col).next_to(ax_.get_end(), UP, buff=0.04)
    oy = odot(x, y, col=col, r=0.1); ly = M(r"\vec e_y", sc=0.5, color=col).next_to(oy, DL, buff=0.03)
    return VGroup(az, ax_, lz, lx, oy, ly)

class S9(C):
    sid = "S9"
    def construct(self):
        self.entete(r"Exercice 3 -- une onde partiellement réfléchie", "Énoncé")
        yc = 1.5
        em = cornet(-5.6, yc); ec = ecran(0.7, yc)
        lem = T("émetteur", sc=0.5, color=GRIS).move_to(P(-5.75, yc - 0.7)); lec = T("écran", sc=0.5, color=GRIS).move_to(P(0.8, yc - 0.85))
        axz = DashedLine(P(-5.25, yc), P(0.65, yc), color=GRIS, stroke_width=1.5, dash_length=0.08)
        rp = repere_zx(-6.4, 0.35)
        self.at(self.t("j1"), FadeIn(rp), run_time=0.5)
        self.at(self.a("j2", "Un émetteur"), Create(em), FadeIn(lem), Create(axz), run_time=0.8)
        fa = fleche((-4.6, yc + 0.42), (-0.6, yc + 0.42), col=CE, sw=4, tl=0.16)
        self.at(self.a("j2", "vers un écran"), Create(ec), FadeIn(lec), GrowArrow(fa), run_time=0.8)
        fr_ = fleche((0.3, yc - 0.42), (-2.2, yc - 0.42), col=ORANGE, sw=3, tl=0.15)
        self.at(self.a("j2", "qui en réfléchit"), GrowArrow(fr_), run_time=0.6)
        la = M(r"\text{aller : } E_1", sc=0.55, color=CE).next_to(fa, UP, buff=0.06)
        lr = M(r"\text{retour : } E_2 < E_1", sc=0.55, color=ORANGE).next_to(fr_, DOWN, buff=0.06)
        d1 = pos(T(r"somme de deux OPPM polarisées selon $\vec e_x$", sc=0.64), -4.9, 0.15)
        self.at(self.t("j3"), Ecrire(d1, rt=1.0), run_time=1.0)
        self.at(self.a("j3", "l'aller"), FadeIn(la), run_time=0.4)
        self.at(self.a("j3", "le retour"), FadeIn(lr), run_time=0.4)
        # mesures de la sonde
        ax, fr = cadre(4.25, 1.3, 4.3, 2.1, 0, 4.5, 0, 18)
        cu = crb(ax, amplE, 0, 4.5, col=CE, sw=3.5)
        h15 = DashedLine(ax.c2p(0, 15), ax.c2p(4.5, 15), color=GRIS, stroke_width=1.5, dash_length=0.07)
        h5 = DashedLine(ax.c2p(0, 5), ax.c2p(4.5, 5), color=GRIS, stroke_width=1.5, dash_length=0.07)
        l15 = T("15", sc=0.48, color=GRIS).next_to(ax.c2p(0, 15), LEFT, buff=0.08); l5 = T("5", sc=0.48, color=GRIS).next_to(ax.c2p(0, 5), LEFT, buff=0.08)
        lv = T(r"amplitude (V/m)", sc=0.45, color=GRIS).next_to(fr, UP, buff=0.06).align_to(fr, LEFT)
        lz = M(r"z", sc=0.5, color=GRIS).next_to(fr, RIGHT, buff=0.08).shift(0.8*DOWN)
        dm = DoubleArrow(ax.c2p(0.75, 2.2), ax.c2p(2.25, 2.2), buff=0, color=VERT, stroke_width=2, tip_length=0.1, max_tip_length_to_length_ratio=0.2)
        ldm = T(r"1,5 cm", sc=0.48, color=VERT).next_to(dm, UP, buff=0.04)
        d2 = pos(T(r"sonde : amplitude de $\vec E$ entre 15 et 5 V/m", sc=0.64), -4.9, -0.42)
        self.at(self.t("j4"), Create(fr), Create(cu), FadeIn(lv), FadeIn(lz), Ecrire(d2, rt=1.0), run_time=1.1)
        self.at(self.a("j4", "entre quinze et cinq"), Create(h15), Create(h5), FadeIn(l15), FadeIn(l5), run_time=0.6)
        d3 = pos(T(r"deux minima consécutifs distants de 1,5 cm", sc=0.64), -4.9, -0.97)
        self.at(self.a("j4", "avec des minima"), Ecrire(d3, rt=0.9), GrowFromCenter(dm), FadeIn(ldm), run_time=0.9)
        q1 = pos(T(r"Q1. L'onde est-elle plane ? progressive ? Champ $\vec B$ total ?", sc=0.64), -5.9, -1.65)
        q2 = pos(T(r"Q2. $\lambda$, $\nu$, $E_1$, $E_2$ ? \qquad Q3. Puissance moyenne surfacique $\langle\Pi\rangle$ ?", sc=0.64), -5.9, -2.2)
        self.ecr(self.t("j5"), q1, rt=1.0); self.ecr(self.t("j6"), q2, rt=1.1)
        bx = SurroundingRectangle(VGroup(q1, q2), color=ROUGE, buff=0.16, corner_radius=0.08)
        self.play(Create(bx), run_time=0.4)
        rf = pos(T(r"Réfléchissons : structure \textbf{onde par onde} ; maximum = ondes \textbf{en phase}", sc=0.62, color=BLEU), -6.3, -2.95)
        self.ecr(self.t("j7"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-1.0, -3.6, 0])
        self.ecr(self.t("j8"), av, rt=0.7)
        self.pause5(self.PH["j8"]["fin"], 2.3, -3.6)
        self.fin()

# ---------------------------------------------------------------- S10
class S10(C):
    sid = "S10"
    def construct(self):
        self.entete(r"Exercice 3 -- structure de l'onde", "Solution")
        self.rappel(r"aller $E_1$, retour $E_2$, polarisation $\vec e_x$")
        self.etape(1, BLEU, 2.1, M(r"\vec E = \big[E_1\cos(\omega t - kz) + E_2\cos(\omega t + kz)\big]\,\vec e_x", sc=0.64), self.a("k1", "le champ total"), rt=1.2)
        k2a = pos(T(r"fonction de $z$ et $t$ seulement : \textbf{plane}", sc=0.62), -5.85, 1.48)
        k2b = pos(T(r"amplitude fonction de $z$ : \textbf{pas progressive}", sc=0.62, color=ROUGE), -5.85, 0.95)
        self.ecr(self.t("k2"), k2a, rt=0.9)
        self.ecr(self.a("k2", "Mais son amplitude"), k2b, rt=0.9)
        self.etape(2, VERT, 0.2, T(r"relation de structure : \textbf{onde par onde} !", sc=0.62, color=ROUGE), self.a("k3", "Piège"), rt=0.9)
        k4 = pos(M(r"\text{aller : } \vec u = \vec e_z, \quad \vec B_1 = \frac{E_1}{c}\cos(\omega t - kz)\,\vec e_y", sc=0.62), -5.85, -0.5)
        self.ecr(self.t("k4"), k4, rt=1.2)
        k5 = pos(M(r"\text{retour : } \vec u = -\vec e_z, \quad \vec B_2 = -\frac{E_2}{c}\cos(\omega t + kz)\,\vec e_y", sc=0.62), -5.85, -1.3)
        self.ecr(self.t("k5"), k5, rt=1.2)
        k6 = pos(M(r"\vec B = \frac{E_1\cos(\omega t - kz) - E_2\cos(\omega t + kz)}{c}\,\vec e_y \;\neq\; \frac{\vec e_z\wedge\vec E}{c}", sc=0.64, color=VERT), -5.85, -2.2)
        self.ecr(self.t("k6"), k6, rt=1.3); self.play(Create(enc(k6, col=VERT, buff=0.12)), run_time=0.4)
        # colonne droite : Maxwell-Faraday et amplitudes
        xr = 1.25
        self.etape(3, ORANGE, -0.45, M(r"\text{(MF) : } \frac{\partial E_x}{\partial z} = -\frac{\partial B_y}{\partial t}", sc=0.62), self.a("k7", "Maxwell-Faraday le confirme"), rt=1.0, x=xr)
        k7b = pos(M(r"\text{les deux : } k\,\big[E_1\sin(\omega t - kz) - E_2\sin(\omega t + kz)\big]", sc=0.48, color=GRIS), xr + 0.4, -1.2)
        self.ecr(self.a("k7", "vaut bien moins"), k7b, rt=1.0)
        self.play(Create(coche(5.65, -0.45)), run_time=0.3)
        ax, fr = cadre(4.3, 1.25, 4.2, 1.95, 0, 4.5, 0, 17)
        cE = crb(ax, amplE, 0, 4.5, col=CE, sw=3.5); cB = crb(ax, amplB, 0, 4.5, col=CB, sw=3.5)
        lE = M(r"E_m(z)", sc=0.48, color=CE).next_to(fr, UP, buff=0.06).align_to(fr, LEFT)
        lB = M(r"c\,B_m(z)", sc=0.48, color=CB).next_to(lE, RIGHT, buff=0.35)
        vl = DashedLine(ax.c2p(1.5, 0), ax.c2p(1.5, 17), color=JAUNE, stroke_width=1.8, dash_length=0.07)
        lz = M(r"z", sc=0.5, color=GRIS).next_to(fr, RIGHT, buff=0.08).shift(0.75*DOWN)
        self.at(self.t("k8"), Create(fr), Create(cE), FadeIn(lE), FadeIn(lz), run_time=0.9)
        self.at(self.a("k8", "elles se retranchent pour B"), Create(cB), FadeIn(lB), run_time=0.9)
        self.at(self.a("k8", "Les maxima de E"), Create(vl), run_time=0.5)
        self.etape(4, JAUNE, -3.4, T(r"cas limites : \; $E_2 = 0$ : progressive \; ; \; $E_2 = E_1$ : stationnaire", sc=0.62), self.t("k9"), rt=1.2)
        self.fin()

# ---------------------------------------------------------------- S11
class S11(C):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice 3 -- mesures et énergie", "Solution")
        self.rappel(r"amplitude entre 15 et 5 V/m, \; minima distants de 1,5 cm")
        sc = 0.62
        # amplitude mesurée (colonne droite)
        ax, fr = cadre(4.45, 1.25, 3.9, 2.0, 0, 4.5, -5, 20)
        cu = crb(ax, amplE, 0, 4.5, col=CE, sw=3.5)
        lE = M(r"E_m(z)", sc=0.48, color=CE).next_to(fr, UP, buff=0.06).align_to(fr, LEFT)
        lz = M(r"z", sc=0.5, color=GRIS).next_to(fr, RIGHT, buff=0.08).shift(0.75*DOWN)
        self.play(Create(fr), Create(cu), FadeIn(lE), FadeIn(lz), run_time=0.7)
        mx = Dot(ax.c2p(1.5, 15), color=JAUNE, radius=0.06); lmx = M(r"E_1 + E_2", sc=0.45, color=JAUNE).next_to(ax.c2p(1.5, 15), UP, buff=0.08)
        mn = Dot(ax.c2p(0.75, 5), color=JAUNE, radius=0.06); lmn = M(r"E_1 - E_2", sc=0.45, color=JAUNE).next_to(ax.c2p(0.75, 5), DOWN, buff=0.1)
        dm = DoubleArrow(ax.c2p(2.25, -2.6), ax.c2p(3.75, -2.6), buff=0, color=VERT, stroke_width=2, tip_length=0.1, max_tip_length_to_length_ratio=0.2)
        ldm = M(r"\lambda/2", sc=0.48, color=VERT).next_to(dm, LEFT, buff=0.08)
        gm = VGroup(*[DashedLine(ax.c2p(z, 5), ax.c2p(z, -2.6), color=VERT, stroke_width=1.5, dash_length=0.06) for z in (2.25, 3.75)])
        self.etape(3, ORANGE, 2.15, T(r"maximum : en phase, \; $E_1 + E_2 = 15$ V/m", sc=sc), self.a("l1", "Au maximum"), rt=0.9)
        self.at(self.a("l1", "quinze volts"), FadeIn(mx), FadeIn(lmx), run_time=0.5)
        l2 = pos(T(r"minimum : en opposition, \; $E_1 - E_2 = 5$ V/m", sc=sc), -5.85, 1.6)
        self.ecr(self.t("l2"), l2, rt=0.9)
        self.at(self.a("l2", "cinq volts"), FadeIn(mn), FadeIn(lmn), run_time=0.5)
        l2b = pos(M(r"E_1 = 10\ \mathrm{V\,m^{-1}}, \qquad E_2 = 5\ \mathrm{V\,m^{-1}}", sc=0.66, color=VERT), -5.85, 1.0)
        self.ecr(self.a("l2", "D'où"), l2b, rt=0.9); self.play(Create(enc(l2b, col=VERT, buff=0.1)), run_time=0.3)
        l3 = pos(T(r"déphasage $2kz$ : un tour quand $z$ avance de $\lambda/2$", sc=sc), -5.85, 0.32)
        self.ecr(self.t("l3"), l3, rt=1.0)
        l4 = pos(T(r"minima séparés de $\lambda/2$ (pas $\lambda$ !) : \; $\lambda = 3{,}0$ cm", sc=sc, color=ROUGE), -5.85, -0.25)
        self.at(self.t("l4"), Ecrire(l4, rt=1.0), Create(gm), GrowFromCenter(dm), FadeIn(ldm), run_time=1.0)
        l5 = pos(M(r"\nu = c/\lambda = 10\ \mathrm{GHz}", sc=0.66, color=VERT), -5.85, -0.85)
        l5b = pos(T(r"ondes centimétriques", sc=0.56, color=GRIS), -2.35, -0.85)
        self.ecr(self.t("l5"), l5, rt=0.8); self.play(Create(enc(l5, col=VERT, buff=0.1)), FadeIn(l5b), run_time=0.4)
        # énergie
        self.etape(4, ROUGE, -1.52, T(r"$\vec\Pi = \vec E\wedge\vec B/\mu_0$, avec les champs \textbf{réels}", sc=sc), self.t("l6"), rt=1.0)
        l7 = pos(M(r"\vec\Pi = \frac{E_1^2\cos^2(\omega t - kz) - E_2^2\cos^2(\omega t + kz)}{\mu_0 c}\,\vec e_z", sc=0.58), -5.85, -2.3)
        l7a = pos(T(r"termes croisés : nuls !", sc=0.55, color=JAUNE), -5.85, -2.3)
        self.at(self.a("l7", "les termes croisés"), FadeIn(l7a), run_time=0.4)
        self.at(self.a("l7", "Il reste"), FadeOut(l7a), Ecrire(l7, rt=1.2), run_time=1.2)
        l8 = pos(M(r"\langle\vec\Pi\rangle = \frac{E_1^2 - E_2^2}{2\mu_0 c}\,\vec e_z \approx 0{,}10\ \mathrm{W\,m^{-2}}", sc=0.6, color=VERT), -5.85, -3.32)
        self.ecr(self.t("l8"), l8, rt=1.2); self.play(Create(enc(l8, col=VERT, buff=0.1)), run_time=0.3)
        # colonne droite : interprétation et vérifications
        xr = 2.4
        f1 = fleche((xr, -0.45), (xr + 1.6, -0.45), col=CE, sw=4, tl=0.15); f2 = fleche((xr + 4.0, -0.95), (xr + 3.0, -0.95), col=ORANGE, sw=3, tl=0.14)
        lf1 = M(r"\langle\Pi_1\rangle", sc=0.5, color=CE).next_to(f1, RIGHT, buff=0.08); lf2 = M(r"\langle\Pi_2\rangle", sc=0.5, color=ORANGE).next_to(f2, LEFT, buff=0.08)
        l9 = pos(M(r"\langle\Pi\rangle = \langle\Pi_1\rangle - \langle\Pi_2\rangle", sc=0.6), xr, -1.6)
        self.at(self.t("l9"), GrowArrow(f1), FadeIn(lf1), GrowArrow(f2), FadeIn(lf2), run_time=0.8)
        self.ecr(self.a("l9", "moins celle"), l9, rt=0.9)
        l10 = pos(T(r"renvoyé : $(E_2/E_1)^2 = 25\,\%$", sc=0.6), xr + 0.15, -2.25)
        self.ecr(self.t("l10"), l10, rt=0.9)
        ca = carte(5, JAUNE, xr + 0.95, -2.95)
        v1 = pos(T(r"$E_2 = 0$ : onde seule", sc=0.56), xr + 1.45, -2.95)
        v2 = pos(T(r"$E_2 = E_1$ : $\langle\Pi\rangle = 0$", sc=0.56), xr + 1.45, -3.5)
        self.at(self.t("l11"), Create(ca[0]), FadeIn(ca[1]), Ecrire(v1, rt=0.7), run_time=0.7)
        self.play(Create(coche(v1.get_right()[0] + 0.3, -2.95)), run_time=0.3)
        self.at(self.a("l11", "Et avec E deux égale E un"), Ecrire(v2, rt=0.8), run_time=0.8)
        self.play(Create(coche(v2.get_right()[0] + 0.3, -3.5)), run_time=0.3)
        self.fin()

# ---------------------------------------------------------------- S12
class S12(C):
    sid = "S12"
    def construct(self):
        self.entete(r"Ce qu'il faut retenir", "Méthode")
        t0 = pos(T(r"la méthode pour étudier \textbf{une onde dans le vide}", sc=0.74, color=GRIS), -6.3, 2.2)
        self.ecr(self.t("m1"), t0, rt=0.9)
        pts = [("m2", r"lire la \textbf{phase} : direction et sens de $\vec u$ ; vérifier $\omega/k = c$", BLEU),
               ("m3", r"lire le \textbf{vecteur} devant le cosinus : polarisation, $\perp \vec u$", VERT),
               ("m4", r"$\vec B = \vec u\wedge\vec E/c$ \textbf{onde par onde} ; trièdre direct, $B = E/c$", ORANGE),
               ("m5", r"énergie : champs \textbf{réels}, $\langle\cos^2\rangle = \frac12$, \; $I = \varepsilon_0 c E_0^2/2$", ROUGE),
               ("m6", r"\textbf{vérifier} : Maxwell, unités, ordre de grandeur, cas limite", JAUNE)]
        for k, (ph_, txt, c) in enumerate(pts):
            yy = [1.35, 0.45, -0.45, -1.35, -2.25][k]
            ca = carte(k+1, c, -5.9, yy); tx = pos(T(txt, sc=0.7), -5.35, yy)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        nx = T(r"Prochaine vidéo : ondes électromagnétiques et conducteurs", sc=0.64, color=GRIS).move_to([0, -3.35, 0])
        self.ecr(self.t("m7"), nx, rt=1.2)
        self.fin()
