from base import *
from manim.mobject.geometry.boolean_ops import Difference, Intersection
# ---------- outils communs (repris des chapitres de RdM) ----------
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
def P(x, y): return np.array([x, y, 0.0])
def fleche(a, b, col=ROUGE, sw=4, tl=0.18):
    return Arrow(P(*a), P(*b), buff=0, color=col, stroke_width=sw, tip_length=tl, max_tip_length_to_length_ratio=0.6, max_stroke_width_to_length_ratio=20)
# ---------- dessins d'électromagnétisme ----------
def sortant(x, y, r=0.1, col=CRAIE, sw=2.5):
    """courant (ou vecteur) qui sort du tableau : ⊙"""
    return VGroup(Circle(radius=r, color=col, stroke_width=sw).move_to(P(x, y)), Dot(P(x, y), radius=0.3*r, color=col))
def entrant(x, y, r=0.1, col=CRAIE, sw=2.5):
    """courant (ou vecteur) qui entre dans le tableau : ⊗"""
    d = 0.62*r
    return VGroup(Circle(radius=r, color=col, stroke_width=sw).move_to(P(x, y)),
                  Line(P(x - d, y - d), P(x + d, y + d), color=col, stroke_width=sw), Line(P(x - d, y + d), P(x + d, y - d), color=col, stroke_width=sw))
def pointe(x, y, ang, col, s=0.2):
    u = np.array([np.cos(ang), np.sin(ang), 0.0]); v = np.array([-u[1], u[0], 0.0]); c = P(x, y)
    return Polygon(c + 0.6*s*u, c - 0.4*s*u + 0.45*s*v, c - 0.4*s*u - 0.45*s*v, color=col, stroke_width=0).set_fill(col, 1)
def cercle_or(cx, cy, R, col=BLEU, angs=(0.0, PI), sw=3, tir=False, s=0.2):
    """cercle parcouru dans le sens trigonométrique, avec des pointes aux angles donnés"""
    c = Circle(radius=R, color=col, stroke_width=sw).move_to(P(cx, cy))
    if tir: c = DashedVMobject(c, num_dashes=max(12, int(R*14)))
    return VGroup(c, *[pointe(cx + R*np.cos(a), cy + R*np.sin(a), a + PI/2, col, s) for a in angs])
def vec(a, b, nom, col, cote=RIGHT, sc=0.62, buff=0.08, sw=4, tl=0.16):
    f = fleche(a, b, col=col, sw=sw, tl=tl); l = M(nom, sc=sc, color=col).next_to(f.get_end(), cote, buff=buff)
    return f, l
def anneau_symboles(cx, cy, R, n, f, a0=0.0, r=0.09, col=CRAIE):
    return VGroup(*[f(cx + R*np.cos(a0 + 2*PI*k/n), cy + R*np.sin(a0 + 2*PI*k/n), r=r, col=col) for k in range(n)])
def cote(xa, xb, y, txt, col=GRIS, sc=0.52, dessous=True):
    l = DoubleArrow(P(xa, y), P(xb, y), buff=0, color=col, stroke_width=2, tip_length=0.11, max_tip_length_to_length_ratio=0.3)
    t = T(txt, sc=sc, color=col).next_to(l, DOWN if dessous else UP, buff=0.06)
    return VGroup(l, t)
# ---------- lignes de champ d'un solénoïde fini (calculées : fonction de flux, intégrales elliptiques) ----------
def lignes_solenoide(cx, cy, s, a=1.0, L=4.0, Z=4.4, Rm=2.9, fr=(0.2, 0.4, 0.56, 0.7), col=BLEU):
    from scipy.special import ellipk, ellipe
    import contourpy
    def psi(r, z):
        r = np.maximum(np.abs(r), 1e-9)
        m = np.clip(4*a*r/((a + r)**2 + z**2), 0, 1 - 1e-12); k = np.sqrt(m)
        return r/(np.pi*k)*np.sqrt(a/r)*((1 - m/2)*ellipk(m) - ellipe(m))
    z0 = np.linspace(-L/2, L/2, 120)
    zs = np.linspace(-Z, Z, 640); rs = np.linspace(0, Rm, 300); ZZ, RR = np.meshgrid(zs, rs)
    PS = sum(psi(RR, ZZ - z) for z in z0)/len(z0)
    pc = sum(psi(np.array([0.3]), np.array([-z])) for z in z0)[0]/len(z0)/0.09   # psi ≈ pc r² au centre
    gen = contourpy.contour_generator(zs, rs, PS)
    lignes, pts = VGroup(), VGroup()
    for kf, f in enumerate(fr):
        zin = (-1.6, -0.7)[kf % 2]
        for seg in gen.lines(pc*f*f):
            seg = seg[::3] if len(seg) > 60 else seg
            for sg in (1, -1):
                lignes.add(VMobject(color=col, stroke_width=2.6).set_points_as_corners([P(cx + s*z, cy + sg*s*r) for z, r in seg]))
                sens = 0
                for i in range(len(seg) - 1):
                    if seg[i][1] < a and (seg[i][0] < zin <= seg[i + 1][0] or seg[i + 1][0] < zin <= seg[i][0]):
                        sens = 1 if seg[i + 1][0] > seg[i][0] else -1
                if sens and kf % 2 == 1:   # retour à l'extérieur : pointes tangentes, sens donné par le parcours intérieur
                    for i in range(len(seg) - 1):
                        if (seg[i][1] - 2.1)*(seg[i + 1][1] - 2.1) < 0:
                            dz, dr = sens*(seg[i + 1][0] - seg[i][0]), sens*(seg[i + 1][1] - seg[i][1])
                            pts.add(pointe(cx + s*0.5*(seg[i][0] + seg[i + 1][0]), cy + sg*s*2.1, np.arctan2(sg*dr, dz), col, 0.2))
                for i in range(len(seg) - 1):
                    for zt, dedans in ((zin, True), (0.0, False)):
                        if seg[i][0] < zt <= seg[i + 1][0] or seg[i + 1][0] < zt <= seg[i][0]:
                            r_ = 0.5*(seg[i][1] + seg[i + 1][1])
                            if (r_ < a) == dedans: pts.add(pointe(cx + s*zt, cy + sg*s*r_, 0.0 if dedans else PI, col, 0.17 if dedans else 0.2))
    axe = Line(P(cx - s*Z, cy), P(cx + s*Z, cy), color=col, stroke_width=2.6)
    lignes.add(axe); pts.add(pointe(cx - 1.15*s, cy, 0.0, col, 0.17))
    bob = VGroup(*[sortant(cx + s*z, cy + s*a, r=0.075) for z in np.linspace(-L/2, L/2, 9)],
                 *[entrant(cx + s*z, cy - s*a, r=0.075) for z in np.linspace(-L/2, L/2, 9)])
    fr_ = Rectangle(width=2*Z*s, height=2*Rm*s, color=GRIS, stroke_width=1.5).move_to(P(cx, cy))
    return lignes, pts, bob, fr_

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"PHYSIQUE \;·\; PT", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Électromagnétisme -- Chapitre 2}", sc=1.1, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Magnétostatique : théorème d'Ampère", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-5.4, 1.3, 0], [5.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        cx, cy = 4.4, -0.7
        fil = sortant(cx, cy, r=0.14, col=ORANGE); lI = M(r"I", sc=0.6, color=ORANGE).move_to([cx + 0.3, cy - 0.25, 0])
        cs = [cercle_or(cx, cy, R, angs=(a0, a0 + PI)) for R, a0 in ((0.55, 0.3), (0.95, 0.9), (1.35, 1.5))]
        fo = M(r"\oint_{\mathcal C} \vec B\cdot\mathrm{d}\vec\ell = \mu_0\, I_{\text{enlacé}}", sc=0.72, color=JAUNE).move_to([cx, -2.75, 0])
        self.at(self.a("a2", "place au champ magnétique"), FadeIn(fil), FadeIn(lI), *[Create(c) for c in cs], run_time=1.2)
        self.ecr(self.a("a2", "la magnétostatique"), fo, rt=0.9)
        items = []
        for k, (txt, col) in enumerate([("Courants et symétries", BLEU), ("Flux et théorème d'Ampère", VERT), ("Exercice 1 : un câble coaxial", ORANGE),
                                         ("Exercice 2 : une bobine torique", ROUGE), ("Exercice 3 : l'aimant d'un accélérateur", JAUNE)]):
            yy = 0.65 - 0.68*k
            items.append(VGroup(carte(k+1, col, -6.2, yy), pos(T(txt, sc=0.74), -5.65, yy)))
        for it, (sid, fr_) in zip(items, [("a3", "les symétries"), ("a3", "le théorème d'Ampère"), ("a4", "un câble coaxial"),
                                          ("a4", "une bobine torique"), ("a4", "l'aimant")]):
            self.jusqua(self.a(sid, fr_)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"2.1 -- Courants et symétries", "Cours")
        f1 = pos(M(r"\vec j = n\,q\,\vec v \qquad (\mathrm{A\cdot m^{-2}})", sc=0.8), -6.3, 2.15)
        self.ecr(self.a("b1", "le vecteur densité"), f1, rt=1.0)
        f2 = pos(M(r"I = \iint_S \vec j\cdot\vec n\,\mathrm{d}S", sc=0.8), -6.3, 1.4)
        self.ecr(self.t("b2"), f2, rt=1.0)
        f3 = pos(T(r"fil domestique : $j \approx 10\ \mathrm{A/mm^2}$", sc=0.6, color=GRIS), -6.3, 0.75)
        self.ecr(self.t("b3"), f3, rt=0.8)
        # tableau E / B
        h0 = pos(T(r"en $M$ d'un plan\dots", sc=0.6, color=GRIS), -6.3, 0.0)
        hE = M(r"\vec E", sc=0.7, color=GRIS).move_to([-2.6, 0.02, 0]); hB = M(r"\vec B", sc=0.7, color=JAUNE).move_to([-0.5, 0.02, 0])
        sp = Line([-6.4, -0.3, 0], [0.6, -0.3, 0], color=GRIS, stroke_width=1.5, stroke_opacity=0.6)
        self.at(self.a("b4", "Attention au piège"), FadeIn(h0), FadeIn(hE), FadeIn(hB), Create(sp), run_time=0.7)
        r1 = [pos(T(r"de symétrie", sc=0.62), -6.3, -0.65), T(r"contenu", sc=0.62, color=GRIS).move_to([-2.6, -0.65, 0]),
              T(r"\textbf{orthogonal}", sc=0.62, color=ROUGE).move_to([-0.5, -0.65, 0])]
        r2 = [pos(T(r"d'antisymétrie", sc=0.62), -6.3, -1.3), T(r"orthogonal", sc=0.62, color=GRIS).move_to([-2.6, -1.3, 0]),
              T(r"\textbf{contenu}", sc=0.62, color=ROUGE).move_to([-0.5, -1.3, 0])]
        self.at(self.a("b5", "plan de symétrie"), Ecrire(r1[0], rt=0.5), Ecrire(r1[1], rt=0.5), run_time=0.6)
        self.ecr(self.a("b5", "B est perpendiculaire"), r1[2], rt=0.6)
        inv = pos(T(r"règles \textbf{inversées} par rapport à $\vec E$ !", sc=0.6, color=ROUGE), -6.3, -2.0)
        self.ecr(self.a("b5", "C'est l'inverse"), inv, rt=0.8)
        self.at(self.t("b6"), Ecrire(r2[0], rt=0.5), Ecrire(r2[1], rt=0.5), run_time=0.6)
        self.ecr(self.a("b6", "B est contenu"), r2[2], rt=0.6)
        # le fil rectiligne
        cx, cy, R = 3.9, 0.95, 1.6
        fil = sortant(cx, cy, r=0.15, col=ORANGE); lI = M(r"I", sc=0.6, color=ORANGE).move_to([cx - 0.12, cy - 0.38, 0])
        pl = DashedLine(P(1.85, cy), P(6.6, cy), color=GRIS, stroke_width=2)
        lpl = M(r"\Pi", sc=0.6, color=GRIS).move_to([1.98, cy - 0.3, 0])
        mM = Dot(P(cx + R, cy), color=CRAIE, radius=0.06); lM = M(r"M", sc=0.6).move_to([cx + R + 0.3, cy - 0.3, 0])
        lr = M(r"r", sc=0.55, color=GRIS).move_to([cx + 0.8, cy + 0.22, 0])
        self.at(self.a("b7", "le fil rectiligne"), FadeIn(fil), FadeIn(lI), run_time=0.5)
        self.at(self.a("b7", "Le plan qui contient"), Create(pl), FadeIn(lpl), FadeIn(mM), FadeIn(lM), FadeIn(lr), run_time=0.8)
        cl = cercle_or(cx, cy, R, angs=(PI/2, 3*PI/2 - 0.3, PI + 0.6))
        fB, lB = vec((cx + R, cy), (cx + R, cy + 1.05), r"\vec B", ORANGE)
        self.at(self.a("b8", "perpendiculaire"), GrowArrow(fB), FadeIn(lB), run_time=0.6)
        self.at(self.a("b8", "il tourne"), Create(cl), run_time=1.0)
        iv = T(r"invariances : translation, rotation", sc=0.58, color=GRIS).move_to([4.2, -1.1, 0])
        self.ecr(self.t("b9"), iv, rt=0.8)
        fo = M(r"\vec B = B_\theta(r)\,\vec e_\theta", sc=0.85, color=JAUNE).move_to([4.2, -1.85, 0])
        self.ecr(self.a("b9", "Donc B égale"), fo, rt=0.8); self.play(Create(enc(fo, col=JAUNE, buff=0.14)), run_time=0.4)
        md = VGroup(T(r"sens : main droite", sc=0.6), T(r"(pouce : $I$ \; ; \; doigts : $\vec B$)", sc=0.56, color=GRIS)).arrange(DOWN, buff=0.12).move_to([4.2, -3.05, 0])
        self.ecr(self.t("b10"), md, rt=1.0)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"2.2 -- Flux conservatif et lignes de champ", "Cours")
        f1 = pos(M(r"\oint_\Sigma \vec B\cdot\vec n\,\mathrm{d}S = 0", sc=0.9, color=JAUNE), -6.3, 2.05)
        t1 = pos(T(r"$\Sigma$ fermée \; ; \; pas de charge magnétique", sc=0.56, color=GRIS), -6.3, 1.12)
        self.ecr(self.a("c1", "Le flux de B"), f1, rt=0.9); self.play(Create(enc(f1, col=JAUNE, buff=0.14)), FadeIn(t1), run_time=0.5)
        t2 = VGroup(T(r"lignes de champ \textbf{fermées},", sc=0.62), T(r"autour des courants", sc=0.62)).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        pos(t2, -6.3, 0.35)
        self.ecr(self.t("c2"), t2, rt=1.0)
        lignes, pts, bob, fr_ = lignes_solenoide(3.65, 0.35, 0.66)
        self.at(self.t("c3"), Create(fr_), FadeIn(bob), run_time=0.7)
        self.at(self.a("c3", "calculée"), Create(lignes), run_time=1.6)
        self.play(FadeIn(pts), run_time=0.4)
        t3 = pos(T(r"dedans : serrées, parallèles $\Rightarrow$ intense, uniforme", sc=0.56), -6.3, -0.75)
        self.ecr(self.a("c3", "Dedans"), t3, rt=1.0)
        t4 = pos(T(r"dehors : elles s'écartent $\Rightarrow$ champ faible", sc=0.56), -6.3, -1.35)
        t4b = pos(T(r"(flux conservé dans un tube de champ)", sc=0.52, color=GRIS), -6.3, -1.85)
        self.ecr(self.t("c4"), t4, rt=0.9); self.ecr(self.a("c4", "le flux se conserve"), t4b, rt=0.8)
        pm = DashedLine(P(3.65, -1.6), P(3.65, 2.3), color=JAUNE, stroke_width=3)
        t5 = T(r"plan médian : plan de symétrie, lignes $\perp$", sc=0.56, color=JAUNE).move_to([3.65, -2.05, 0])
        self.at(self.a("c5", "le plan médian"), Create(pm), Ecrire(t5, rt=0.9), run_time=0.9)
        t6 = T(r"en 3D : onglet \textbf{Simulateur} du chapitre, sur le site", sc=0.62, color=VERT).move_to([0, -3.3, 0])
        self.ecr(self.t("c6"), t6, rt=1.0); self.play(Create(enc(t6, col=VERT, buff=0.14)), run_time=0.4)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"2.3 -- Le théorème d'Ampère", "Cours")
        fo = pos(M(r"\oint_{\mathcal C} \vec B\cdot\mathrm{d}\vec\ell = \mu_0\, I_{\text{enlacé}}", sc=1.0, color=JAUNE), -6.3, 2.0)
        self.ecr(self.a("d1", "La circulation"), fo, rt=1.1); self.play(Create(enc(fo, col=JAUNE, buff=0.16)), run_time=0.4)
        mu = pos(T(r"$\mu_0 = 4\pi\times10^{-7}$ H$\cdot$m$^{-1}$ : perméabilité du vide", sc=0.6, color=GRIS), -6.3, 1.05)
        self.ecr(self.t("d2"), mu, rt=1.0)
        # contour vu en perspective, normale, fils
        ex, ey = 4.2, 0.0
        el = Ellipse(width=3.8, height=1.3, color=VERT, stroke_width=3).set_fill(CRAIE, 0.07).move_to(P(ex, ey))
        o1 = pointe(ex, ey - 0.65, 0.0, VERT, 0.24); o2 = pointe(ex, ey + 0.65, PI, VERT, 0.24)
        lC = M(r"\mathcal C", sc=0.65, color=VERT).move_to([ex - 2.15, ey + 0.4, 0])
        fn, ln = vec((5.3, 0.0), (5.3, 1.15), r"\vec n", VERT)
        self.at(self.t("d3"), Create(el), FadeIn(o1), FadeIn(o2), FadeIn(lC), run_time=0.9)
        t3 = pos(T(r"contour \textbf{orienté} $\Rightarrow$ $\vec n$ par la main droite", sc=0.62), -6.3, 0.3)
        self.at(self.a("d3", "la normale"), GrowArrow(fn), FadeIn(ln), Ecrire(t3, rt=0.9), run_time=0.9)
        t4 = pos(T(r"compté $+$ s'il traverse dans le sens de $\vec n$, $-$ sinon", sc=0.62), -6.3, -0.35)
        self.ecr(self.t("d4"), t4, rt=1.0)
        w1 = VGroup(Line(P(3.2, -1.9), P(3.2, 1.9), color=BLEU, stroke_width=4), pointe(3.2, 1.45, PI/2, BLEU, 0.24), Dot(P(3.2, 0), radius=0.06, color=BLEU))
        w2 = VGroup(Line(P(4.4, -1.9), P(4.4, 1.9), color=ORANGE, stroke_width=4), pointe(4.4, -1.45, -PI/2, ORANGE, 0.24), Dot(P(4.4, 0), radius=0.06, color=ORANGE))
        w3 = VGroup(Line(P(6.45, -1.9), P(6.45, 1.9), color=GRIS, stroke_width=4), pointe(6.45, 1.45, PI/2, GRIS, 0.24))
        l1 = pos(T(r"$I_1 = 4$ A", sc=0.56, color=BLEU), 3.05, 1.75, bord=RIGHT)
        l2 = pos(T(r"$I_2 = 6$ A", sc=0.56, color=ORANGE), 4.55, -1.7)
        l3 = M(r"I_3", sc=0.6, color=GRIS).move_to([6.45, 2.15, 0])
        self.at(self.a("d5", "quatre ampères"), Create(w1), FadeIn(l1), run_time=0.6)
        self.at(self.a("d5", "six ampères"), Create(w2), FadeIn(l2), run_time=0.6)
        t5 = pos(M(r"I_{\text{enlacé}} = I_1 - I_2 = 4 - 6 = -2\ \mathrm{A}", sc=0.75), -6.3, -1.1)
        self.ecr(self.a("d5", "Le courant enlacé"), t5, rt=1.0); self.play(Create(enc(t5, col=VERT, buff=0.12)), run_time=0.4)
        t6 = pos(T(r"$I_3$ : non enlacé, il ne compte pas", sc=0.6, color=GRIS), -6.3, -1.85)
        self.at(self.t("d6"), Create(w3), FadeIn(l3), run_time=0.6)
        self.ecr(self.a("d6", "Il n'est pas enlacé"), t6, rt=0.8)
        t7 = pos(T(r"bobine : fil traversant $N$ fois la surface $\Rightarrow$ $N\,I$", sc=0.62), -6.3, -2.5)
        self.ecr(self.t("d7"), t7, rt=1.0)
        t8 = T(r"toujours vrai, mais \textbf{utile} seulement si les symétries sortent $B$ de l'intégrale", sc=0.62, color=JAUNE).move_to([0, -3.4, 0])
        self.ecr(self.t("d8"), t8, rt=1.2)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"2.4 -- Les champs de référence", "Cours")
        X = [-4.6, 0.0, 4.6]; yf = 1.2
        hd = [T(r"\textbf{" + t + "}", sc=0.72, color=c).move_to([x, 2.45, 0]) for t, c, x in [("Fil épais", BLEU, X[0]), ("Solénoïde infini", VERT, X[1]), ("Bobine torique", ORANGE, X[2])]]
        # fil épais
        dq = Circle(radius=0.5, color=CRAIE, stroke_width=2.5).set_fill(BLEU, 0.3).move_to(P(X[0], yf))
        sI = sortant(X[0], yf, r=0.1)
        ra = Line(P(X[0], yf), P(X[0] + 0.5*np.cos(-0.5), yf + 0.5*np.sin(-0.5)), color=CRAIE, stroke_width=2)
        la = M(r"a", sc=0.55).move_to([X[0] + 0.32, yf - 0.48, 0])
        ca = cercle_or(X[0], yf, 0.88, col=VERT, angs=(PI/2,), tir=True, s=0.18)
        self.at(self.t("e1"), Ecrire(hd[0], rt=0.5), Create(dq), FadeIn(sI), run_time=0.8)
        self.at(self.a("e1", "de rayon a"), Create(ra), FadeIn(la), run_time=0.4)
        b1 = M(r"r \le a :\ B_\theta = \frac{\mu_0 I\, r}{2\pi a^2}", sc=0.66, color=BLEU).move_to([X[0], -0.25, 0])
        self.at(self.a("e2", "Sur un cercle"), Create(ca), run_time=0.7)
        self.ecr(self.a("e2", "Donc B croît"), b1, rt=0.9)
        b2 = M(r"r \ge a :\ B_\theta = \frac{\mu_0 I}{2\pi r}", sc=0.66, color=BLEU).move_to([X[0], -1.15, 0])
        self.ecr(self.a("e3", "tout le courant"), b2, rt=0.9)
        b3 = T(r"continu en $r = a$, maximal", sc=0.52, color=GRIS).move_to([X[0], -1.85, 0])
        self.ecr(self.a("e3", "Le champ est continu"), b3, rt=0.7)
        # solénoïde
        xs = np.linspace(-1.2, 1.2, 7)
        hau = VGroup(*[sortant(x, yf + 0.5) for x in xs]); bas = VGroup(*[entrant(x, yf - 0.5) for x in xs])
        fB, lB = vec((-0.7, yf), (0.7, yf), r"\vec B", VERT)
        s1 = M(r"B = \mu_0\, n\, I", sc=0.82, color=VERT).move_to([X[1], -0.25, 0])
        s2 = T(r"uniforme dedans, nul dehors", sc=0.55, color=GRIS).move_to([X[1], -1.05, 0])
        self.at(self.t("e4"), Ecrire(hd[1], rt=0.5), FadeIn(hau), FadeIn(bas), run_time=0.8)
        self.at(self.a("e4", "axial"), GrowArrow(fB), FadeIn(lB), run_time=0.5)
        self.ecr(self.a("e4", "B égale"), s1, rt=0.7); self.play(Create(enc(s1, col=VERT, buff=0.12)), run_time=0.3)
        self.ecr(self.a("e4", "Dehors"), s2, rt=0.7)
        # bobine torique
        cx = X[2]
        an = Annulus(inner_radius=0.45, outer_radius=0.95, color=ORANGE, fill_opacity=0.15, stroke_width=0).move_to(P(cx, yf))
        sin_ = anneau_symboles(cx, yf, 0.45, 6, sortant, r=0.08); sout = anneau_symboles(cx, yf, 0.95, 10, entrant, r=0.08, a0=0.3)
        ct = cercle_or(cx, yf, 0.7, col=VERT, angs=(PI/2, 3*PI/2), tir=True, s=0.17)
        t1 = M(r"B_\theta = \frac{\mu_0 N I}{2\pi r}", sc=0.72, color=ORANGE).move_to([cx, -0.25, 0])
        t2 = T(r"dans le tore \; ; \; nul dehors", sc=0.55, color=GRIS).move_to([cx, -1.05, 0])
        self.at(self.t("e5"), Ecrire(hd[2], rt=0.5), FadeIn(an), FadeIn(sin_), FadeIn(sout), run_time=0.8)
        self.at(self.a("e5", "orthoradial"), Create(ct), run_time=0.6)
        self.ecr(self.a("e5", "mu zéro N I"), t1, rt=0.8); self.ecr(self.a("e5", "et zéro"), t2, rt=0.6)
        o1 = T(r"$1$ A à $1$ cm : $20\ \mu$T \quad (Terre : $\approx 50\ \mu$T)", sc=0.62).move_to([0, -2.55, 0])
        self.ecr(self.t("e6"), o1, rt=1.0)
        o2 = T(r"solénoïde de TP : quelques mT \quad IRM : $1{,}5$ à $3$ T", sc=0.62).move_to([0, -3.1, 0])
        self.ecr(self.t("e7"), o2, rt=1.0)
        ex = T(r"\textbf{Place aux exercices !}", sc=0.75, color=JAUNE).move_to([0, -3.68, 0])
        self.ecr(self.a("e8", "place aux exercices"), ex, rt=0.6)
        self.fin()

def coax(cx, cy, s):
    """coupe du câble coaxial (a = 1, b = 4, c = 5 mm ; s unités par mm)"""
    ame = Circle(radius=1*s, color=BLEU, stroke_width=2.5).set_fill(BLEU, 0.35).move_to(P(cx, cy))
    gai = Annulus(inner_radius=4*s, outer_radius=5*s, color=ORANGE, fill_opacity=0.3, stroke_width=2.5).move_to(P(cx, cy))
    sym = anneau_symboles(cx, cy, 4.5*s, 8, entrant, a0=PI/8, r=0.1)
    so = sortant(cx, cy, r=0.12)
    return ame, gai, sym, so

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"Exercice 1 -- un câble coaxial", "Énoncé")
        cx, cy, s = -4.45, -0.25, 0.42
        ame, gai, sym, so = coax(cx, cy, s)
        lam = T(r"âme", sc=0.5, color=BLEU).move_to([cx, cy - 0.78, 0]); lga = T(r"gaine", sc=0.55, color=ORANGE).move_to([cx, cy - 2.42, 0])
        rb = Line(P(cx, cy), P(cx + 4*s*np.cos(3*PI/4), cy + 4*s*np.sin(3*PI/4)), color=CRAIE, stroke_width=2)
        rc = Line(P(cx, cy), P(cx - 5*s, cy), color=CRAIE, stroke_width=2)
        ra = Line(P(cx, cy), P(cx + s*np.cos(PI/4), cy + s*np.sin(PI/4)), color=CRAIE, stroke_width=2)
        lb = M(r"b", sc=0.55).move_to([cx - 0.95, cy + 0.6, 0]); lc = M(r"c", sc=0.55).move_to([cx - 1.4, cy - 0.22, 0])
        la = M(r"a", sc=0.55).move_to([cx + 0.48, cy + 0.42, 0])
        self.at(self.t("f1"), Create(gai), Create(ame), run_time=0.9)
        d1 = pos(T(r"âme : $a = 1$ mm, \; $I = 5$ A selon $\vec e_z$ (vers vous)", sc=0.66), -1.7, 2.2)
        self.at(self.t("f2"), FadeIn(so), Create(ra), FadeIn(la), FadeIn(lam), Ecrire(d1, rt=1.1), run_time=1.1)
        d2 = pos(T(r"gaine : $b = 4$ mm, \; $c = 5$ mm, \; courant $-I$", sc=0.66), -1.7, 1.55)
        self.at(self.t("f3"), Create(rb), Create(rc), FadeIn(lb), FadeIn(lc), FadeIn(lga), Ecrire(d2, rt=1.0), run_time=1.0)
        self.at(self.a("f3", "porte le courant de retour"), FadeIn(sym), run_time=0.5)
        d3 = pos(T(r"courants uniformes dans chaque conducteur", sc=0.6, color=GRIS), -1.7, 0.9)
        self.ecr(self.a("f3", "Dans chaque conducteur"), d3, rt=0.9)
        q = T(r"Champ $\vec B$ en tout point ? \quad Tracer $B(r)$.", sc=0.8, color=ROUGE).move_to([2.35, -0.3, 0])
        self.ecr(self.a("f4", "que vaut le champ"), q, rt=1.0); self.play(Create(enc(q)), run_time=0.4)
        rf = VGroup(T(r"Réfléchissons : symétries, cercle d'Ampère,", sc=0.62, color=BLEU), T(r"puis $I_{\text{enlacé}}$ zone par zone", sc=0.62, color=BLEU)).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        pos(rf, -1.7, -1.75)
        self.ecr(self.t("f5"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([1.6, -3.1, 0])
        self.ecr(self.t("f6"), av, rt=0.7)
        pa, arc = chrono(4.9, -3.1)
        self.at(self.PH["f6"]["fin"], FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"Exercice 1 -- la solution", "Solution")
        rap = pos(T(r"$a = 1$ mm, \; $b = 4$ mm, \; $c = 5$ mm, \; $I = 5$ A", sc=0.56, color=GRIS), 6.6, 2.72, bord=RIGHT)
        self.play(FadeIn(rap), run_time=0.4)
        def etape(k, c, y, m, t, rt=0.9):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        etape(1, BLEU, 2.15, T(r"plan $(M, Oz)$ : symétrie $\Rightarrow$ $\vec B \perp$ ce plan", sc=0.62), self.a("g1", "Première étape"))
        g2 = pos(M(r"\vec B = B_\theta(r)\,\vec e_\theta", sc=0.72), -5.85, 1.55)
        self.ecr(self.a("g2", "B égale"), g2, rt=0.8)
        etape(2, VERT, 0.85, T(r"cercle d'axe $Oz$, de rayon $r$, selon $\vec e_\theta$ ; \; $\vec n = \vec e_z$", sc=0.6), self.a("g3", "Un cercle"), rt=1.0)
        g4 = pos(M(r"\oint \vec B\cdot\mathrm{d}\vec\ell = 2\pi r\,B_\theta(r)", sc=0.7), -5.85, 0.25)
        self.ecr(self.a("g4", "la circulation"), g4, rt=0.9)
        etape(3, ORANGE, -0.35, M(r"I_{\text{enlacé}} :", sc=0.66), self.a("g5", "Troisième étape"), rt=0.5)
        z1 = pos(M(r"r \le a :\ I\,r^2/a^2", sc=0.62), -5.3, -0.85)
        z2 = pos(M(r"a \le r \le b :\ I", sc=0.62), -5.3, -1.35)
        z3 = pos(M(r"b \le r \le c :\ I\,\frac{c^2 - r^2}{c^2 - b^2}", sc=0.62, color=ROUGE), -5.3, -1.9)
        z4 = pos(M(r"r \ge c :\ I - I = 0", sc=0.62), -5.3, -2.45)
        self.ecr(self.a("g5", "Dans l'âme"), z1, rt=0.7)
        self.ecr(self.t("g6"), z2, rt=0.6)
        pg = pos(T(r"piège : le retour compte $-$", sc=0.52, color=ROUGE), -1.95, -1.9)
        self.at(self.a("g6", "attention au piège"), FadeIn(pg), run_time=0.4)
        self.ecr(self.a("g7", "Il reste"), z3, rt=1.0)
        self.ecr(self.t("g8"), z4, rt=0.7)
        # graphe B(r)
        ax, fr = cadre(4.15, 0.9, 4.4, 2.7, 0, 6, 0, 1.2)
        gB = T(r"$B$ (mT)", sc=0.52, color=GRIS).move_to(ax.c2p(5.3, 1.05)); gr = M(r"r", sc=0.55, color=GRIS).move_to(ax.c2p(6, 0) + np.array([0.22, 0, 0]))
        gu = VGroup(*[DashedLine(ax.c2p(x, 0), ax.c2p(x, 1.2), color=GRIS, stroke_width=1.3, stroke_opacity=0.6) for x in (1, 4, 5)])
        lt = VGroup(*[M(n, sc=0.55, color=GRIS).move_to(ax.c2p(x, 0) + np.array([0, -0.24, 0])) for n, x in (("a", 1), ("b", 4), ("c", 5))])
        b4 = etape(4, JAUNE, -3.2, M(r"B_\theta(r) = \frac{\mu_0\, I_{\text{enlacé}}(r)}{2\pi r}", sc=0.72), self.a("g9", "Quatrième étape"), rt=0.9)
        self.play(Create(enc(b4, col=JAUNE, buff=0.1)), Create(fr), Create(gu), FadeIn(gB), FadeIn(gr), FadeIn(lt), run_time=0.6)
        rr2 = np.linspace(1, 4, 60); rr3 = np.linspace(4, 5, 30)
        c1 = lig(ax, [(0, 0), (1, 1.0)], col=BLEU); c2 = lig(ax, list(zip(rr2, 1.0/rr2)), col=BLEU)
        c3 = lig(ax, list(zip(rr3, (25 - rr3**2)/(9*rr3))), col=BLEU); c4 = lig(ax, [(5, 0), (6, 0)], col=BLEU)
        v1 = T(r"$1$ mT", sc=0.52, color=BLEU).move_to(ax.c2p(1.0, 1.0) + np.array([0.55, 0.12, 0]))
        v2 = T(r"$0{,}25$", sc=0.52, color=BLEU).move_to(ax.c2p(4.0, 0.25) + np.array([0.12, 0.3, 0]))
        self.at(self.a("g9", "croît linéairement"), Create(c1), FadeIn(v1), run_time=0.8)
        self.at(self.a("g10", "il décroît"), Create(c2), run_time=1.0)
        self.at(self.a("g10", "virgule vingt-cinq"), FadeIn(v2), run_time=0.4)
        self.at(self.a("g10", "dans la gaine"), Create(c3), run_time=0.7)
        self.at(self.a("g10", "en r égale c"), Create(c4), run_time=0.4)
        ca5 = carte(5, VERT, 0.6, -1.15)
        v3 = VGroup(T(r"continu en $a$, $b$, $c$", sc=0.58), T(r"$B = 0$ sur l'axe", sc=0.58)).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        pos(v3, 1.1, -1.35)
        self.at(self.t("g11"), Create(ca5[0]), FadeIn(ca5[1]), Ecrire(v3, rt=1.0), *[Indicate(m, color=JAUNE, scale_factor=1.3) for m in lt], run_time=1.0)
        cc = VGroup(T(r"dehors : $\vec B = \vec 0$", sc=0.62, color=JAUNE), T(r"le câble ne perturbe pas son environnement", sc=0.56, color=JAUNE)).arrange(DOWN, buff=0.12).move_to([3.75, -2.85, 0])
        self.ecr(self.t("g13"), cc, rt=1.0); self.play(Create(enc(cc, col=JAUNE, buff=0.14)), run_time=0.4)
        self.fin()

def lig(ax, pts, col=ORANGE, sw=4):
    return VMobject(color=col, stroke_width=sw).set_points_as_corners([ax.c2p(a, b) for a, b in pts])

def tore_dessus(cx, cy, R1, R2, nin=12, nout=16, r=0.09):
    an = Annulus(inner_radius=R1, outer_radius=R2, color=ORANGE, fill_opacity=0.14, stroke_width=0).move_to(P(cx, cy))
    bords = VGroup(Circle(radius=R1, color=ORANGE, stroke_width=2).move_to(P(cx, cy)), Circle(radius=R2, color=ORANGE, stroke_width=2).move_to(P(cx, cy)))
    sin_ = anneau_symboles(cx, cy, R1, nin, sortant, r=r); sout = anneau_symboles(cx, cy, R2, nout, entrant, r=r, a0=PI/nout)
    return an, bords, sin_, sout

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"Exercice 2 -- une bobine torique", "Énoncé")
        cx, cy, R1, R2 = -4.55, 0.45, 1.15, 1.61
        an = Annulus(inner_radius=R1, outer_radius=R2, color=ORANGE, fill_opacity=0.18, stroke_width=2.5).move_to(P(cx, cy))
        sp = VGroup(*[Line(P(cx + R1*np.cos(t), cy + R1*np.sin(t)), P(cx + R2*np.cos(t), cy + R2*np.sin(t)), color=CRAIE, stroke_width=1.6)
                      for t in np.linspace(0, 2*PI, 28, endpoint=False) + 0.06])
        oz = sortant(cx, cy, r=0.1, col=GRIS); loz = M(r"Oz", sc=0.5, color=GRIS).move_to([cx + 0.38, cy - 0.12, 0])
        r1 = Line(P(cx, cy), P(cx + R1*np.cos(7*PI/6), cy + R1*np.sin(7*PI/6)), color=CRAIE, stroke_width=2)
        r2 = Line(P(cx, cy), P(cx + R2*np.cos(-PI/3), cy + R2*np.sin(-PI/3)), color=CRAIE, stroke_width=2)
        l1 = M(r"R_1", sc=0.52).move_to([cx - 0.62, cy - 0.05, 0]); l2 = M(r"R_2", sc=0.52).move_to([cx + 0.6, cy - 0.75, 0])
        lN = T(r"$N$ spires", sc=0.55, color=GRIS).move_to([cx, cy - 2.0, 0])
        self.at(self.t("h1"), Create(an), FadeIn(oz), FadeIn(loz), run_time=0.9)
        self.at(self.a("h1", "section rectangulaire"), Create(sp), run_time=0.8)
        d0 = pos(T(r"tore d'axe $Oz$, section rectangulaire", sc=0.66), -1.9, 2.2)
        self.play(Ecrire(d0, rt=0.9))
        d1 = pos(T(r"$R_1 = 5$ cm, \; $R_2 = 7$ cm, \; hauteur $h = 3$ cm", sc=0.66), -1.9, 1.6)
        self.at(self.t("h2"), Create(r1), Create(r2), FadeIn(l1), FadeIn(l2), Ecrire(d1, rt=1.1), run_time=1.1)
        # petite coupe pour la hauteur h
        xa, sc_, yc = -6.3, 0.3, -2.95
        axe = DashedLine(P(xa, yc - 0.8), P(xa, yc + 0.8), color=GRIS, stroke_width=2); lz = M(r"z", sc=0.5, color=GRIS).move_to([xa - 0.2, yc + 0.75, 0])
        rc = Rectangle(width=2*sc_, height=3*sc_, color=ORANGE, stroke_width=2.5).set_fill(ORANGE, 0.18).move_to(P(xa + 6*sc_, yc))
        lh = M(r"h", sc=0.5).move_to([xa + 5*sc_ - 0.22, yc, 0]); lco = T(r"coupe", sc=0.48, color=GRIS).move_to([xa + 6*sc_ + 0.85, yc, 0])
        self.at(self.a("h2", "hauteur"), Create(axe), FadeIn(lz), Create(rc), FadeIn(lh), FadeIn(lco), run_time=0.7)
        d2 = pos(T(r"$N = 800$ spires jointives, \; $I = 2$ A", sc=0.66), -1.9, 1.0)
        self.at(self.t("h3"), FadeIn(lN), Ecrire(d2, rt=1.0), run_time=1.0)
        q = VGroup(T(r"$\vec B$ en tout point ? \quad flux propre $\Phi$ ? \quad inductance $L$ ?", sc=0.72, color=ROUGE),
                   T(r"approximation du tore mince : bonne ?", sc=0.72, color=ROUGE)).arrange(DOWN, buff=0.15).move_to([2.35, -0.3, 0])
        self.ecr(self.t("h4"), q[0], rt=1.0)
        self.ecr(self.a("h4", "tore mince"), q[1], rt=0.8); self.play(Create(enc(q)), run_time=0.4)
        rf = VGroup(T(r"Réfléchissons : Ampère pour $\vec B$ ;", sc=0.62, color=BLEU), T(r"mais $B$ est-il uniforme dans la section ?", sc=0.62, color=BLEU)).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        pos(rf, -1.9, -1.85)
        self.ecr(self.t("h5"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([1.6, -3.2, 0])
        self.ecr(self.t("h6"), av, rt=0.7)
        pa, arc = chrono(4.9, -3.2)
        self.at(self.PH["h6"]["fin"], FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"Exercice 2 -- le champ dans le tore", "Solution")
        rap = pos(T(r"$N = 800$, \; $I = 2$ A, \; $R_1 = 5$ cm, \; $R_2 = 7$ cm", sc=0.56, color=GRIS), 6.6, 2.72, bord=RIGHT)
        self.play(FadeIn(rap), run_time=0.4)
        def etape(k, c, y, m, t, rt=0.9):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        cx, cy, R1, R2 = 4.45, 0.1, 1.5, 2.1
        an, bords, sin_, sout = tore_dessus(cx, cy, R1, R2)
        self.at(self.t("i1"), FadeIn(an), Create(bords), run_time=0.7)
        etape(1, BLEU, 2.15, T(r"chaque spire dans un plan contenant l'axe : \textbf{symétrie}", sc=0.6), self.a("i1", "chaque spire"), rt=1.0)
        self.at(self.a("i1", "C'est un plan"), FadeIn(sin_), FadeIn(sout), run_time=0.6)
        i2 = pos(M(r"\Rightarrow\ \vec B = B_\theta(r, z)\,\vec e_\theta", sc=0.72), -5.85, 1.55)
        self.ecr(self.a("i2", "orthoradial"), i2, rt=0.8)
        ca = cercle_or(cx, cy, 1.8, col=VERT, angs=(PI/4, 5*PI/4), tir=True, s=0.2)
        etape(2, VERT, 0.8, M(r"\text{cercle } (r,\ \vec e_\theta) :\ \oint \vec B\cdot\mathrm{d}\vec\ell = 2\pi r\,B_\theta", sc=0.64), self.a("i3", "un cercle"), rt=1.0)
        self.at(self.a("i3", "Circulation"), Create(ca), run_time=0.8)
        i4 = pos(T(r"dans le tore : $N$ traversées, $I_{\text{enlacé}} = N I$", sc=0.6), -5.85, 0.12)
        self.at(self.t("i4"), Ecrire(i4, rt=1.0), Indicate(sin_, color=JAUNE, scale_factor=1.05), run_time=1.0)
        i4b = pos(M(r"B_\theta = \frac{\mu_0 N I}{2\pi r}", sc=0.9, color=VERT), -5.85, -0.75)
        self.ecr(self.a("i4", "D'où"), i4b, rt=0.8); self.play(Create(enc(i4b, col=VERT, buff=0.12)), run_time=0.4)
        fBs = [vec((cx + 1.8, cy - 0.32), (cx + 1.8, cy + 0.32), r"\vec B", ORANGE, cote=RIGHT, sc=0.58, buff=0.42),
               vec((cx - 1.8, cy + 0.32), (cx - 1.8, cy - 0.32), r"\vec B", ORANGE, cote=LEFT, sc=0.58, buff=0.42)]
        self.play(*[GrowArrow(f) for f, l in fBs], *[FadeIn(l) for f, l in fBs], run_time=0.5)
        cint = DashedVMobject(Circle(radius=0.85, color=GRIS, stroke_width=2).move_to(P(cx, cy)), num_dashes=16)
        lint = M(r"I_{\text{enlacé}} = 0", sc=0.48, color=GRIS).move_to([cx, cy, 0])
        i5 = pos(T(r"dehors : $I_{\text{enlacé}} = 0$ ou $NI - NI$ $\Rightarrow$ $\vec B = \vec 0$", sc=0.6), -5.85, -1.6)
        i5b = pos(T(r"(sans hypothèse admise, contrairement au solénoïde)", sc=0.52, color=GRIS), -5.85, -2.12)
        self.at(self.t("i5"), Create(cint), FadeIn(lint), Ecrire(i5, rt=1.0), run_time=1.0)
        self.ecr(self.a("i5", "sans aucune hypothèse"), i5b, rt=0.9)
        i6 = pos(M(r"B(R_1) = 6{,}4\ \mathrm{mT}, \qquad B(R_2) = 4{,}6\ \mathrm{mT}", sc=0.72), -5.85, -3.05)
        self.ecr(self.t("i6"), i6, rt=1.0)
        nu = T(r"$\Rightarrow$ \textbf{non uniforme} !", sc=0.66, color=ROUGE).next_to(i6, RIGHT, buff=0.35)
        self.ecr(self.a("i6", "Le champ n'est pas"), nu, rt=0.6)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"Exercice 2 -- flux propre et inductance", "Solution")
        rap = pos(T(r"$N = 800$, \; $I = 2$ A, \; $R_1 = 5$ cm, \; $R_2 = 7$ cm, \; $h = 3$ cm", sc=0.56, color=GRIS), 6.6, 2.72, bord=RIGHT)
        self.play(FadeIn(rap), run_time=0.4)
        def etape(k, c, y, m, t, rt=0.9):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        # coupe méridienne : section rectangulaire, bande dr
        xa, k = 2.3, 0.58
        axe = DashedLine(P(xa, -0.05), P(xa, 2.3), color=GRIS, stroke_width=2); lz = M(r"z", sc=0.5, color=GRIS).move_to([xa - 0.22, 2.15, 0])
        rc = Rectangle(width=2*k, height=3*k, color=ORANGE, stroke_width=2.5).set_fill(ORANGE, 0.16).move_to(P(xa + 6*k, 1.15))
        bd = Rectangle(width=0.13, height=3*k, color=VERT, stroke_width=1.5).set_fill(VERT, 0.7).move_to(P(xa + 6*k, 1.15))
        lh = M(r"h", sc=0.52).move_to([xa + 5*k - 0.25, 1.15, 0]); ldr = M(r"\mathrm{d}r", sc=0.5, color=VERT).move_to([xa + 6*k, 2.2, 0])
        sB = entrant(xa + 6.6*k, 1.65, r=0.1, col=ORANGE); lB = M(r"\vec B", sc=0.5, color=ORANGE).move_to([xa + 6.6*k, 1.25, 0])
        c1 = cote(xa, xa + 5*k, 0.0, r"$R_1$"); c2 = cote(xa, xa + 7*k, -0.62, r"$R_2$")
        etape(3, ORANGE, 2.15, T(r"flux à travers \textbf{une} spire :", sc=0.62), self.a("i7", "le flux"), rt=0.8)
        self.at(self.a("i7", "à travers une spire"), Create(axe), FadeIn(lz), Create(rc), FadeIn(lh), FadeIn(sB), FadeIn(lB), Create(c1), Create(c2), run_time=0.9)
        pg = pos(T(r"$\Phi_1 \neq B\,S$ !", sc=0.66, color=ROUGE), -1.65, 2.15)
        self.ecr(self.a("i7", "Piège classique"), pg, rt=0.6)
        i8 = pos(M(r"\Phi_1 = \int_{R_1}^{R_2} \frac{\mu_0 N I}{2\pi r}\; h\,\mathrm{d}r", sc=0.72), -5.85, 1.3)
        self.at(self.t("i8"), FadeIn(bd), FadeIn(ldr), run_time=0.6)
        self.ecr(self.a("i8", "et on intègre"), i8, rt=1.0)
        i9 = pos(M(r"\Phi_1 = \frac{\mu_0 N I h}{2\pi}\,\ln\frac{R_2}{R_1} \approx 3{,}2\ \mu\mathrm{Wb}", sc=0.72), -5.85, 0.3)
        self.ecr(self.t("i9"), i9, rt=1.1); self.play(Create(enc(i9, col=ORANGE, buff=0.1)), run_time=0.4)
        etape(4, JAUNE, -0.65, M(r"\Phi = N\,\Phi_1, \qquad L = \frac{\Phi}{I}", sc=0.72), self.a("i10", "Quatrième étape"), rt=0.9)
        i11 = pos(M(r"L = \frac{\mu_0 N^2 h}{2\pi}\,\ln\frac{R_2}{R_1} \approx 1{,}3\ \mathrm{mH}", sc=0.75, color=VERT), -5.85, -1.65)
        self.ecr(self.t("i11"), i11, rt=1.1); self.play(Create(enc(i11, col=VERT, buff=0.1)), run_time=0.4)
        i12 = pos(T(r"$L \propto N^2$ : chaque spire voit le champ des $N$ spires", sc=0.56, color=GRIS), -5.85, -2.4)
        self.ecr(self.t("i12"), i12, rt=0.9)
        i13 = etape(5, VERT, -3.2, M(r"\text{tore mince : } L \approx \frac{\mu_0 N^2 h\,(R_2 - R_1)}{2\pi R_{\text{moy}}} = 1{,}28\ \mathrm{mH}", sc=0.62), self.a("i13", "Vérification"), rt=1.1)
        i14 = T(r"écart $< 1\,\%$", sc=0.62, color=VERT).next_to(i13, RIGHT, buff=0.35)
        self.ecr(self.t("i14"), i14, rt=0.6)
        i15 = VGroup(T(r"champ confiné dans le tore :", sc=0.58, color=JAUNE), T(r"pas de fuite, idéal pour un transformateur", sc=0.56, color=JAUNE)).arrange(DOWN, buff=0.12).move_to([4.35, -1.75, 0])
        self.ecr(self.t("i15"), i15, rt=1.0); self.play(Create(enc(i15, col=JAUNE, buff=0.14)), run_time=0.4)
        self.fin()

def aimant(o1x, o2x, oy, R, nsym=3, ang=(PI*0.72, PI, PI*1.28), rs=0.75):
    """deux cylindres qui se chevauchent : croissant +j (gauche, ⊙), croissant -j (droite, ⊗), zone commune vide"""
    c1 = Circle(radius=R).move_to(P(o1x, oy)); c2 = Circle(radius=R).move_to(P(o2x, oy))
    g = Difference(c1, c2).set_fill(BLEU, 0.35).set_stroke(width=0); d = Difference(c2, c1).set_fill(ORANGE, 0.35).set_stroke(width=0)
    bords = VGroup(c1.copy().set_stroke(CRAIE, 2.5).set_fill(opacity=0), c2.copy().set_stroke(CRAIE, 2.5).set_fill(opacity=0))
    sg = VGroup(*[sortant(o1x + rs*R*np.cos(a), oy + rs*R*np.sin(a), r=0.1) for a in ang])
    sd = VGroup(*[entrant(o2x - rs*R*np.cos(a), oy + rs*R*np.sin(a), r=0.1) for a in ang])
    return g, d, bords, sg, sd

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"Exercice 3 -- l'aimant d'un accélérateur", "Énoncé")
        o1, o2, oy, R = -4.85, -3.95, 0.3, 1.8
        g, d, bords, sg, sd = aimant(o1, o2, oy, R)
        p1 = Dot(P(o1, oy), radius=0.05); p2 = Dot(P(o2, oy), radius=0.05)
        l1 = M(r"O_1", sc=0.52).move_to([o1, oy - 0.27, 0]); l2 = M(r"O_2", sc=0.52).move_to([o2, oy - 0.27, 0])
        cd = cote(o1, o2, oy - 0.62, r"$d$")
        rR = Line(P(o1, oy), P(o1, oy + R), color=CRAIE, stroke_width=2); lR = M(r"R", sc=0.52).move_to([o1 - 0.2, oy + 0.95, 0])
        self.at(self.t("j1"), Create(bords), run_time=0.9)
        d0 = pos(T(r"deux cylindres infinis de rayon $R$, d'axes $\parallel Oz$", sc=0.64), -1.7, 2.2)
        self.at(self.t("j2"), Ecrire(d0, rt=1.0), Create(rR), FadeIn(lR), run_time=1.0)
        self.at(self.a("j2", "passent par"), FadeIn(p1), FadeIn(p2), FadeIn(l1), FadeIn(l2), run_time=0.5)
        self.at(self.a("j2", "à la distance d"), Create(cd), run_time=0.5)
        lg = M(r"+j\,\vec e_z", sc=0.58, color=BLEU).move_to([-6.45, 2.25, 0]); ld = M(r"-j\,\vec e_z", sc=0.58, color=ORANGE).move_to([-2.4, 2.25, 0])
        d1 = pos(T(r"en $O_1$ : $+j\,\vec e_z$ \quad en $O_2$ : $-j\,\vec e_z$ \quad $\overrightarrow{O_1O_2} = d\,\vec e_x$", sc=0.64), -1.7, 1.6)
        self.at(self.a("j3", "Le premier"), FadeIn(g), FadeIn(sg), FadeIn(lg), run_time=0.6)
        self.at(self.a("j3", "le second"), FadeIn(d), FadeIn(sd), FadeIn(ld), Ecrire(d1, rt=1.0), run_time=1.0)
        lz = T(r"sans courant", sc=0.45, color=GRIS).move_to([(o1 + o2)/2, oy - 1.2, 0])
        d2 = pos(T(r"zone commune : $j - j = 0$, le faisceau y passe", sc=0.6, color=GRIS), -1.7, 1.0)
        self.at(self.t("j4"), FadeIn(lz), Ecrire(d2, rt=1.0), run_time=1.0)
        rp = VGroup(fleche((-6.55, -2.25), (-5.95, -2.25), col=GRIS, sw=3, tl=0.13), fleche((-6.55, -2.25), (-6.55, -1.65), col=GRIS, sw=3, tl=0.13),
                    M(r"x", sc=0.5, color=GRIS).move_to([-5.8, -2.25, 0]), M(r"y", sc=0.5, color=GRIS).move_to([-6.55, -1.5, 0]),
                    sortant(-6.55, -2.25, r=0.07, col=GRIS), M(r"z", sc=0.5, color=GRIS).move_to([-6.8, -2.45, 0]))
        self.play(FadeIn(rp), run_time=0.4)
        q = VGroup(T(r"$\vec B$ dans la zone commune ?", sc=0.74, color=ROUGE), T(r"$j$ pour $B = 8{,}3$ T, avec $d = 2$ cm ?", sc=0.74, color=ROUGE)).arrange(DOWN, buff=0.15).move_to([2.4, -0.35, 0])
        self.ecr(self.a("j5", "que vaut le champ"), q[0], rt=0.8)
        self.ecr(self.a("j5", "quelle densité"), q[1], rt=0.9); self.play(Create(enc(q)), run_time=0.4)
        rf = VGroup(T(r"Réfléchissons : plus de symétrie de révolution,", sc=0.62, color=BLEU), T(r"pas d'Ampère direct. Quelle astuce ?", sc=0.62, color=BLEU)).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        pos(rf, -1.7, -1.85)
        self.ecr(self.t("j6"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([1.6, -3.25, 0])
        self.ecr(self.t("j7"), av, rt=0.7)
        pa, arc = chrono(4.9, -3.25)
        self.at(self.PH["j7"]["fin"], FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice 3 -- un cylindre plein", "Solution")
        def etape(k, c, y, m, t, rt=0.9):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        k1 = pos(M(r"\text{distribution} = \text{cylindre}\,(O_1,\, +\vec j\,) + \text{cylindre}\,(O_2,\, -\vec j\,)", sc=0.62, color=JAUNE), -6.35, 2.2)
        self.ecr(self.a("k1", "Ce sont deux cylindres"), k1, rt=1.2)
        # un cylindre plein
        ox, oy, R, rm, am = 4.6, 0.65, 1.7, 1.0, 0.6
        dq = Circle(radius=R, color=BLEU, stroke_width=2.5).set_fill(BLEU, 0.18).move_to(P(ox, oy))
        sj = VGroup(*[sortant(ox + 1.3*np.cos(a), oy + 1.3*np.sin(a), r=0.09) for a in (2.4, 3.3, 4.2, 5.1)])
        lj = M(r"\vec j", sc=0.55, color=BLEU).move_to([ox + 1.3*np.cos(4.2) - 0.33, oy + 1.3*np.sin(4.2) - 0.05, 0])
        po = Dot(P(ox, oy), radius=0.05); lo = M(r"O", sc=0.55).move_to([ox - 0.25, oy - 0.2, 0])
        mx, my = ox + rm*np.cos(am), oy + rm*np.sin(am)
        pm = Dot(P(mx, my), radius=0.06); lm = M(r"M", sc=0.55).move_to([mx + 0.28, my - 0.12, 0])
        fom = fleche((ox, oy), (mx, my), col=CRAIE, sw=3, tl=0.14); lom = M(r"\overrightarrow{OM}", sc=0.5).move_to([ox + 0.2, oy + 0.62, 0])
        ca = cercle_or(ox, oy, rm, col=VERT, angs=(PI + 0.4,), tir=True, s=0.18)
        u = np.array([-np.sin(am), np.cos(am)])
        fB, lB = vec((mx, my), (mx + 0.85*u[0], my + 0.85*u[1]), r"\vec B", ORANGE, cote=UP, sc=0.58)
        etape(1, BLEU, 1.4, T(r"un cylindre plein, d'axe $O$, et $M$ intérieur :", sc=0.62), self.a("k2", "Première étape"), rt=1.0)
        self.at(self.a("k2", "d'axe passant"), Create(dq), FadeIn(sj), FadeIn(lj), FadeIn(po), FadeIn(lo), run_time=0.7)
        self.at(self.a("k2", "en un point M"), FadeIn(pm), FadeIn(lm), run_time=0.4)
        k3 = pos(M(r"\vec B = B_\theta(r)\,\vec e_\theta, \quad \text{cercle de rayon } r", sc=0.66), -5.85, 0.8)
        self.ecr(self.t("k3"), k3, rt=1.0)
        self.at(self.a("k3", "un cercle d'Ampère"), Create(ca), run_time=0.7)
        k4 = pos(M(r"2\pi r\,B_\theta = \mu_0\, j\,\pi r^2 \;\Rightarrow\; B_\theta = \frac{\mu_0\, j\, r}{2}", sc=0.66), -5.85, 0.1)
        self.ecr(self.t("k4"), k4, rt=1.1)
        self.at(self.a("k4", "On en déduit"), GrowArrow(fB), FadeIn(lB), run_time=0.5)
        etape(2, VERT, -0.75, T(r"forme \textbf{vectorielle}, sans repère lié à l'axe :", sc=0.62), self.a("k5", "Deuxième étape"), rt=1.0)
        k6 = pos(M(r"\vec e_z \wedge \vec e_r = \vec e_\theta", sc=0.66, color=GRIS), -5.85, -1.4)
        self.ecr(self.t("k6"), k6, rt=0.7)
        k6b = pos(M(r"\vec B = \frac{\mu_0}{2}\,\vec j \wedge \overrightarrow{OM}", sc=0.95, color=JAUNE), -5.85, -2.2)
        self.at(self.a("k6", "Donc B égale"), Ecrire(k6b, rt=0.9), GrowArrow(fom), FadeIn(lom), run_time=0.9)
        self.play(Create(enc(k6b, col=JAUNE, buff=0.14)), run_time=0.4)
        k6c = T(r"($\overrightarrow{OM} \perp$ axe)", sc=0.55, color=GRIS).next_to(k6b, RIGHT, buff=0.45)
        self.ecr(self.a("k6", "part de l'axe"), k6c, rt=0.6)
        k7 = pos(T(r"$\Rightarrow$ on peut additionner des cylindres d'axes différents", sc=0.58, color=GRIS), -5.85, -3.0)
        self.ecr(self.t("k7"), k7, rt=1.0)
        k8 = pos(T(r"contrôle : sur l'axe, $\overrightarrow{OM} = \vec 0$ $\Rightarrow$ $\vec B = \vec 0$", sc=0.58, color=VERT), -5.85, -3.6)
        self.ecr(self.t("k8"), k8, rt=1.0)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice 3 -- un champ uniforme", "Solution")
        def etape(k, c, y, m, t, rt=0.9):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        o1, o2, oy, R = 3.75, 4.5, 0.85, 1.5
        g, d, bords, sg, sd = aimant(o1, o2, oy, R, ang=(PI*5/6, PI, PI*7/6), rs=0.75)
        p1 = Dot(P(o1, oy), radius=0.05); p2 = Dot(P(o2, oy), radius=0.05)
        l1 = M(r"O_1", sc=0.5).move_to([o1 - 0.05, oy - 0.27, 0]); l2 = M(r"O_2", sc=0.5).move_to([o2 + 0.05, oy - 0.27, 0])
        mx, my = 4.35, 1.75
        pm = Dot(P(mx, my), radius=0.06); lm = M(r"M", sc=0.5).move_to([mx + 0.22, my + 0.15, 0])
        f1 = fleche((o1, oy), (mx, my), col=BLEU, sw=3, tl=0.13); f2 = fleche((o2, oy), (mx, my), col=ORANGE, sw=3, tl=0.13)
        etape(3, BLEU, 2.15, T(r"superposition en $M$, dans la zone commune :", sc=0.62), self.a("l1", "Troisième étape"), rt=1.0)
        self.play(FadeIn(g), FadeIn(d), Create(bords), FadeIn(sg), FadeIn(sd), FadeIn(p1), FadeIn(p2), FadeIn(l1), FadeIn(l2), run_time=0.7)
        self.at(self.a("l1", "En un point M"), FadeIn(pm), FadeIn(lm), GrowArrow(f1), GrowArrow(f2), run_time=0.7)
        l2_ = pos(M(r"\vec B = \frac{\mu_0}{2}\,\vec j\wedge\overrightarrow{O_1M} - \frac{\mu_0}{2}\,\vec j\wedge\overrightarrow{O_2M}", sc=0.68), -5.85, 1.45)
        self.ecr(self.t("l2"), l2_, rt=1.3)
        l3 = pos(M(r"\overrightarrow{O_1M} - \overrightarrow{O_2M} = \overrightarrow{O_1O_2} \quad (\text{Chasles})", sc=0.66), -5.85, 0.65)
        f12 = fleche((o1, oy), (o2, oy), col=JAUNE, sw=4, tl=0.14)
        self.at(self.a("l3", "la relation de Chasles"), Ecrire(l3, rt=1.0), GrowArrow(f12), run_time=1.0)
        l4 = pos(M(r"\vec B = \frac{\mu_0}{2}\,\vec j \wedge \overrightarrow{O_1O_2}", sc=0.9, color=JAUNE), -5.85, -0.2)
        self.ecr(self.a("l4", "Résultat"), l4, rt=0.9); self.play(Create(enc(l4, col=JAUNE, buff=0.12)), run_time=0.4)
        un = T(r"\textbf{uniforme} !", sc=0.7, color=JAUNE).next_to(l4, RIGHT, buff=0.45)
        fl = VGroup(*[fleche((x, y - 0.24), (x, y + 0.24), col=VERT, sw=4, tl=0.14) for x in (3.5, 4.125, 4.75) for y in (0.0, 1.72)])
        self.at(self.a("l4", "le champ est uniforme"), FadeOut(f1), FadeOut(f2), FadeOut(pm), FadeOut(lm), Ecrire(un, rt=0.6), *[GrowArrow(f) for f in fl], run_time=0.8)
        l5 = pos(M(r"\vec B = \frac{\mu_0\, j\, d}{2}\;\vec e_y \;\perp\; (O_1O_2)", sc=0.72), -5.85, -1.2)
        lB = M(r"\vec B", sc=0.6, color=VERT).move_to([4.125, -0.62, 0])
        self.at(self.a("l5", "il est porté par e y"), Ecrire(l5, rt=1.0), FadeIn(lB), run_time=1.0)
        ca5 = carte(5, VERT, 1.65, -1.5)
        l6 = pos(T(r"main droite : $\odot$ à gauche, $\otimes$ à droite", sc=0.56), 2.15, -1.38)
        l6b = pos(T(r"$\Rightarrow$ $\vec B$ vers le haut : cohérent", sc=0.56, color=VERT), 2.15, -1.88)
        self.at(self.t("l6"), Create(ca5[0]), FadeIn(ca5[1]), Ecrire(l6, rt=1.0), Indicate(sg, color=JAUNE), Indicate(sd, color=JAUNE), run_time=1.0)
        self.ecr(self.a("l6", "B monte"), l6b, rt=0.7)
        etape(4, ORANGE, -2.05, M(r"j = \frac{2B}{\mu_0\, d} \approx 6{,}6\cdot10^{8}\ \mathrm{A\cdot m^{-2}}", sc=0.68), self.a("l7", "Quatrième étape"), rt=1.0)
        l8 = pos(T(r"$= 660$ A/mm$^2$ : soixante fois le cuivre domestique !", sc=0.58, color=ROUGE), -5.85, -2.78)
        self.ecr(self.t("l8"), l8, rt=1.0)
        l9 = pos(T(r"$\Rightarrow$ supraconducteurs refroidis à l'hélium (LHC)", sc=0.58), -5.85, -3.35)
        self.ecr(self.t("l9"), l9, rt=1.0)
        l10 = pos(T(r"cas limite : $d \to 0$ $\Rightarrow$ $\vec B \to \vec 0$", sc=0.58, color=VERT), 2.15, -2.6)
        self.ecr(self.t("l10"), l10, rt=0.9)
        self.fin()

class S13(Cours):
    sid = "S13"
    def construct(self):
        self.entete(r"Ce qu'il faut retenir", "Méthode")
        t0 = pos(T(r"la méthode pour calculer $\vec B$ avec le \textbf{théorème d'Ampère}", sc=0.74, color=GRIS), -6.3, 2.2)
        self.ecr(self.t("m1"), t0, rt=0.9)
        pts = [("m2", r"\textbf{symétries} et invariances : $\vec B \perp$ plan de symétrie des courants", BLEU),
               ("m3", r"\textbf{contour} par $M$ : $\vec B$ tangent et constant, $\perp$, ou nul \; ; \textbf{l'orienter}", VERT),
               ("m4", r"$I_{\text{enlacé}}$ \textbf{algébrique}, zone par zone \; ($N I$, ou une fraction)", ORANGE),
               ("m5", r"$\oint_{\mathcal C} \vec B\cdot\mathrm{d}\vec\ell = \mu_0\, I_{\text{enlacé}}$", ROUGE),
               ("m6", r"symétrie insuffisante : \textbf{superposer}, avec $\vec B$ vectoriel", CRAIE),
               ("m7", r"\textbf{vérifier} : continuité, axe, cas limite, unités, ordre de grandeur", JAUNE)]
        for k, (ph_, txt, c) in enumerate(pts):
            yy = 1.45 - 0.75*k
            ca = carte(k+1, c, -5.9, yy); tx = pos(T(txt, sc=0.68), -5.35, yy)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        nx = T(r"Prochaine vidéo : équations de Maxwell, ARQS et énergie électromagnétique", sc=0.62, color=GRIS).move_to([0, -3.4, 0])
        self.ecr(self.t("m8"), nx, rt=1.2)
        self.fin()
