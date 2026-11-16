from base import *
import os
APERCU = os.environ.get("APERCU")   # contrôle d'une scène en image fixe (pas d'effacement final)

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
def crb(ax, f, a, b, col=ORANGE, sw=4, n=120):
    u = np.linspace(a, b, n)
    return VMobject(color=col, stroke_width=sw).set_points_smoothly([ax.c2p(s, f(s)) for s in u])
def aire(ax, f, a, b, col=ORANGE, op=0.18, n=80):
    u = np.linspace(a, b, n); pts = [ax.c2p(a, 0)] + [ax.c2p(s, f(s)) for s in u] + [ax.c2p(b, 0)]
    return Polygon(*pts, stroke_width=0, fill_color=col, fill_opacity=op)
def zero(ax, a, b): return DashedLine(ax.c2p(a, 0), ax.c2p(b, 0), color=GRIS, stroke_width=1.5, dash_length=0.08)

# --- dessins de poutres (symboles du cours)
def poutre(x0, x1, y, col=CRAIE, sw=8): return Line([x0, y, 0], [x1, y, 0], color=col, stroke_width=sw)
def hachures(x0, x1, y0, y1, n=6, col=GRIS, sw=2):
    """traits obliques à 45° dans le rectangle [x0, x1] x [y0, y1]"""
    w = x1 - x0; g = VGroup()
    for k in range(n + 1):
        b = y0 + k*(y1 - y0 - w)/n
        g.add(Line([x0, b, 0], [x1, b + w, 0], color=col, stroke_width=sw))
    return g
def encastrement(x, y, h=1.1, w=0.3, cote=-1, col=GRIS):
    """rectangle hachuré accolé à l'extrémité x de la poutre ; cote=-1 : à gauche, +1 : à droite"""
    x0, x1 = (x - w, x) if cote < 0 else (x, x + w)
    r = Rectangle(width=w, height=h, color=col, stroke_width=3).move_to([(x0 + x1)/2, y, 0])
    return VGroup(r, hachures(x0, x1, y - h/2, y + h/2, n=max(4, int(h/0.18)), col=col))
def sol(x, y, l=0.75, col=GRIS):
    g = VGroup(Line([x - l/2, y, 0], [x + l/2, y, 0], color=col, stroke_width=3))
    for k in range(6):
        a = x - l/2 + 0.06 + k*(l - 0.12)/5
        g.add(Line([a, y, 0], [a - 0.11, y - 0.13, 0], color=col, stroke_width=2))
    return g
def pivot(x, y, s=1.0, col=CRAIE):
    """articulation : petit triangle sous la poutre, pointe à l'axe, sur un sol hachuré"""
    tri = Polygon([x, y - 0.05*s, 0], [x - 0.24*s, y - 0.42*s, 0], [x + 0.24*s, y - 0.42*s, 0], color=col, stroke_width=3)
    return VGroup(tri, Dot([x, y - 0.05*s, 0], radius=0.05*s, color=col), sol(x, y - 0.42*s, 0.75*s))
def glissant(x, y, s=1.0, col=CRAIE):
    """appui simple : triangle posé sur deux petits rouleaux"""
    tri = Polygon([x, y - 0.05*s, 0], [x - 0.24*s, y - 0.36*s, 0], [x + 0.24*s, y - 0.36*s, 0], color=col, stroke_width=3)
    rr = VGroup(*[Circle(radius=0.055*s, color=col, stroke_width=2).move_to([x + d*s, y - 0.42*s, 0]) for d in (-0.12, 0.12)])
    return VGroup(tri, rr, sol(x, y - 0.48*s, 0.75*s))
def force(x, y, l=0.9, col=ROUGE, sw=5):
    return Arrow([x, y + l, 0], [x, y + 0.06, 0], buff=0, color=col, stroke_width=sw, max_tip_length_to_length_ratio=0.35, tip_length=0.2)
def repartie(x0, x1, y, h=0.65, n=9, col=ORANGE, sw=3):
    g = VGroup(Line([x0, y + h, 0], [x1, y + h, 0], color=col, stroke_width=sw))
    for a in np.linspace(x0, x1, n):
        g.add(Arrow([a, y + h, 0], [a, y + 0.06, 0], buff=0, color=col, stroke_width=sw, max_tip_length_to_length_ratio=0.4, tip_length=0.14))
    return g
def repere(x, y, l=0.7, col=GRIS, lx="x", ly="y"):
    ax_ = Arrow([x, y, 0], [x + l, y, 0], buff=0, color=col, stroke_width=3, max_tip_length_to_length_ratio=0.3, tip_length=0.14)
    ay = Arrow([x, y, 0], [x, y + l, 0], buff=0, color=col, stroke_width=3, max_tip_length_to_length_ratio=0.3, tip_length=0.14)
    tx = M(lx, sc=0.6, color=col).next_to(ax_.get_end(), DOWN, buff=0.08)
    ty = M(ly, sc=0.6, color=col).next_to(ay.get_end(), LEFT, buff=0.08)
    return VGroup(ax_, ay, tx, ty)
def cote(x0, x1, y, lab, col=GRIS, sc=0.6, dessous=True):
    d = DoubleArrow([x0, y, 0], [x1, y, 0], buff=0, color=col, stroke_width=2, tip_length=0.13, max_tip_length_to_length_ratio=0.2)
    t = T(lab, sc=sc, color=col).next_to(d, DOWN if dessous else UP, buff=0.08)
    return VGroup(d, t)
def courbe(f, x0, x1, col=BLEU, sw=4, n=80, tirets=True):
    c = VMobject(color=col, stroke_width=sw).set_points_smoothly([[a, f(a), 0] for a in np.linspace(x0, x1, n)])
    return DashedVMobject(c, num_dashes=int(1 + 9*(x1 - x0)), dashed_ratio=0.6) if tirets else c
def couple(x, y, r=0.5, sens=1, col=ORANGE):
    """moment autour de l'axe (horizontal) d'un arbre : arc d'ellipse fléché"""
    a = Arc(radius=r, start_angle=-0.55*PI*sens + (PI if sens < 0 else 0), angle=1.55*PI*sens, color=col, stroke_width=4)
    a.stretch(0.32, 0).move_to([x, y, 0])
    a.add_tip(tip_length=0.16, tip_width=0.16)
    return a
def tableau(lignes, xs, y0, dy, sc=0.62, col=CRAIE):
    """petit tableau : 1re ligne = en-tête (gris), filet sous l'en-tête"""
    g = VGroup()
    for i, l in enumerate(lignes):
        for x, c in zip(xs, l):
            g.add(T(c, sc=sc, color=GRIS if i == 0 else col).move_to([x, y0 - i*dy, 0]))
    w0, w1 = xs[0] - 0.85, xs[-1] + 0.75
    g.add(Line([w0, y0 - dy/2, 0], [w1, y0 - dy/2, 0], color=GRIS, stroke_width=2))
    return g

class C(Cours):
    def etape(self, k, col, y, m, t, rt=1.0, x=-6.35):
        ca = carte(k, col, x, y); mm = pos(m, x + 0.5, y)
        self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
        return mm
    def pause5(self, t, x, y):
        pa, arc = chrono(x, y)
        self.at(t, FadeIn(pa), Create(arc), run_time=0.5)
        self.play(Uncreate(arc), run_time=4.6); self.play(FadeOut(pa), run_time=0.2)
    def fin(self):
        if APERCU: self.wait(0.1); return
        super().fin()

# ---------------------------------------------------------------- S0
class S0(C):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PT", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Résistance des matériaux -- Chapitre 3}", sc=1.1, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Déformations, flèches et dimensionnement en rigidité", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-5.4, 1.3, 0], [5.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        y0, x0, x1 = -0.35, 2.3, 6.2
        fig = VGroup(encastrement(x0, y0), poutre(x0, x1, y0), force(x1, y0, 0.95))
        dv = courbe(lambda a: y0 - 1.05*((a - x0)/(x1 - x0))**2*(3 - (a - x0)/(x1 - x0))/2, x0, x1)
        fl = DoubleArrow([x1 + 0.4, y0, 0], [x1 + 0.4, y0 - 1.05, 0], buff=0, color=BLEU, stroke_width=2, tip_length=0.12, max_tip_length_to_length_ratio=0.25)
        ft = M(r"f", sc=0.7, color=BLEU).next_to(fl, RIGHT, buff=0.08)
        self.at(self.a("a2", "Mais une pièce"), Create(fig[0]), Create(fig[1]), GrowArrow(fig[2]), run_time=0.8)
        self.play(Create(dv), GrowFromCenter(fl), FadeIn(ft), run_time=1.0)
        items = []
        for k, (txt, col) in enumerate([("Déplacements et loi de Hooke", BLEU), ("Traction et torsion", VERT), ("La déformée en flexion", ORANGE),
                                         ("Flèches de référence et rigidité", ROUGE), ("Exercice 1 : la console", BLEU),
                                         ("Exercice 2 : la poutre sur deux appuis", VERT), ("Exercice 3 : l'arbre de transmission", JAUNE)]):
            yy = 0.75 - 0.58*k
            items.append(VGroup(carte(k+1, col, -6.2, yy), pos(T(txt, sc=0.72), -5.65, yy)))
        for it, (sid, fr_) in zip(items, [("a3", "les déplacements"), ("a3", "la traction"), ("a3", "la déformée"), ("a3", "ses cas de référence"),
                                          ("a4", "une console"), ("a4", "une poutre sur deux appuis"), ("a4", "un arbre de transmission")]):
            self.jusqua(self.a(sid, fr_)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

# ---------------------------------------------------------------- S1
class S1(C):
    sid = "S1"
    def construct(self):
        self.entete(r"3.1 -- Déplacements et loi de Hooke", "Déformations")
        l1 = pos(T(r"section droite $=$ \textbf{plaque rigide}", sc=0.74, color=JAUNE), -6.3, 2.15)
        self.ecr(self.t("b1"), l1, rt=0.9)
        # figure : une section translatée et tournée
        xa, xb, y0, A = 1.3, 6.5, 2.1, 1.45
        yd = lambda a: y0 - A*((a - xa)/(xb - xa))**2
        ax0 = DashedLine([xa, y0, 0], [xb, y0, 0], color=GRIS, stroke_width=2, dash_length=0.1)
        dfo = courbe(yd, xa, xb, col=CRAIE, sw=6, tirets=False)
        rp = repere(1.35, 0.5)
        self.at(self.a("b1", "Elle translate"), Create(ax0), Create(dfo), FadeIn(rp), run_time=1.0)
        X0 = 4.9; s0 = (X0 - xa)/(xb - xa); pente = -2*A*s0/(xb - xa); th = np.arctan(pente)
        sec0 = DashedLine([X0, y0 - 0.38, 0], [X0, y0 + 0.38, 0], color=GRIS, stroke_width=3, dash_length=0.07)
        c0 = np.array([X0, yd(X0), 0]); dirn = np.array([-np.sin(th), np.cos(th), 0])
        sec1 = Line(c0 - 0.4*dirn, c0 + 0.4*dirn, color=BLEU, stroke_width=5)
        X1 = 2.9; va = Arrow([X1, y0, 0], [X1, yd(X1) + 0.03, 0], buff=0, color=ORANGE, stroke_width=4, tip_length=0.14, max_tip_length_to_length_ratio=0.3)
        vt = M(r"v(x)", sc=0.62, color=ORANGE).next_to(va, LEFT, buff=0.1).shift(0.25*UP)
        l2 = pos(T(r"translation : $u$ (axiale), \; $v$ (\textbf{flèche})", sc=0.72), -6.3, 1.45)
        self.at(self.t("b2"), Ecrire(l2, rt=1.0), FadeIn(sec0), GrowArrow(va), FadeIn(vt), run_time=1.0)
        l3 = pos(T(r"rotations : $\theta_x$ (torsion), \; $\theta_z$ (flexion)", sc=0.72), -6.3, 0.8)
        vr = DashedLine(c0, c0 + 0.62*UP, color=GRIS, stroke_width=2, dash_length=0.06)
        arc = Arc(radius=0.48, start_angle=PI/2, angle=th, arc_center=c0, color=BLEU, stroke_width=3)
        tht = M(r"\theta_z", sc=0.62, color=BLEU).move_to(c0 + 0.62*UP + 0.42*RIGHT)
        self.at(self.t("b3"), Ecrire(l3, rt=1.0), Create(sec1), Create(vr), Create(arc), FadeIn(tht), run_time=1.0)
        f4 = pos(M(r"\theta_z = \frac{dv}{dx}", sc=0.85, color=JAUNE), -6.1, 0.0)
        n4 = T(r"(Navier-Bernoulli)", sc=0.6, color=GRIS).next_to(f4, RIGHT, buff=0.45)
        self.ecr(self.a("b4", "Donc"), f4, rt=0.8); self.play(Create(enc(f4, col=JAUNE, buff=0.15)), FadeIn(n4), run_time=0.5)
        tg = Line(c0 - 0.8*np.array([np.cos(th), np.sin(th), 0]), c0 + 0.8*np.array([np.cos(th), np.sin(th), 0]), color=JAUNE, stroke_width=2)
        self.at(self.a("b4", "la pente"), Create(tg), run_time=0.6)
        # loi de comportement : courbe de traction
        axs = Axes(x_range=[0, 10, 2], y_range=[0, 10, 2], x_length=4.2, y_length=2.4, axis_config={"color": CRAIE, "stroke_width": 2, "include_ticks": False, "tip_width": 0.13, "tip_height": 0.13}).move_to([4.15, -1.95, 0])
        el = Line(axs.c2p(0, 0), axs.c2p(1.6, 6.0), color=VERT, stroke_width=5)
        pl = VMobject(color=VERT, stroke_width=5).set_points_smoothly([axs.c2p(a, b) for a, b in [(1.6, 6.0), (2.6, 7.2), (4.5, 8.3), (6.5, 8.6), (8.3, 8.1)]])
        ex, sy = M(r"\varepsilon", sc=0.65).next_to(axs.x_axis.get_end(), DOWN, buff=0.1), M(r"\sigma", sc=0.65).next_to(axs.y_axis.get_end(), LEFT, buff=0.1)
        re_ = DashedLine(axs.c2p(0, 6.0), axs.c2p(1.6, 6.0), color=GRIS, stroke_width=1.5, dash_length=0.07)
        ret = M(r"R_e", sc=0.6, color=GRIS).next_to(axs.c2p(0, 6.0), LEFT, buff=0.1)
        pe = T(r"pente $E$", sc=0.6, color=VERT).move_to(axs.c2p(2.6, 3.0))
        f5 = pos(M(r"\sigma = E\,\varepsilon \qquad \varepsilon = \frac{\Delta L}{L_0}", sc=0.85, color=VERT), -6.3, -1.2)
        self.at(self.t("b5"), Ecrire(f5, rt=1.0), Create(axs), FadeIn(ex), FadeIn(sy), run_time=1.0)
        self.at(self.a("b5", "La contrainte est proportionnelle"), Create(el), FadeIn(pe), run_time=0.8)
        self.play(Create(pl), Create(re_), FadeIn(ret), run_time=0.8)
        f6 = pos(M(r"\tau = G\,\gamma \qquad G = \frac{E}{2\,(1 + \nu)}", sc=0.85, color=VERT), -6.3, -2.1)
        self.ecr(self.t("b6"), f6, rt=1.0)
        ac = pos(T(r"acier : $E = 210$ GPa, \; $G \approx 81$ GPa", sc=0.66), -6.3, -2.85)
        self.ecr(self.a("b6", "Pour l'acier"), ac, rt=0.9)
        l7 = pos(T(r"rigidité : $E$ et $G$, \textbf{pas} $R_e$ !", sc=0.74, color=ROUGE), -6.3, -3.55)
        self.ecr(self.t("b7"), l7, rt=0.9)
        self.fin()

# ---------------------------------------------------------------- S2
class S2(C):
    sid = "S2"
    def construct(self):
        self.entete(r"3.2 -- Traction et torsion : allongement et angle", "Déformations")
        h1 = pos(T(r"\textbf{Traction}", sc=0.78, color=BLEU), -6.3, 2.2)
        f1 = pos(M(r"\varepsilon = \frac{du}{dx} = \frac{N}{E\,S}", sc=0.88), -6.3, 1.35)
        yb = 1.45; wall = encastrement(1.7, yb, h=1.0)
        bar = Rectangle(width=3.2, height=0.42, color=CRAIE, stroke_width=3).move_to([3.3, yb, 0])
        bar2 = DashedVMobject(Rectangle(width=3.85, height=0.38, color=BLEU, stroke_width=3).move_to([1.7 + 3.85/2, yb, 0]), num_dashes=40)
        fN = Arrow([5.55, yb, 0], [6.6, yb, 0], buff=0, color=ROUGE, stroke_width=5, tip_length=0.2)
        tN = M("N", sc=0.7, color=ROUGE).next_to(fN, UP, buff=0.08)
        self.at(self.t("c1"), Ecrire(h1, rt=0.5), Create(wall), Create(bar), run_time=0.8)
        self.ecr(self.a("c1", "epsilon"), f1, rt=0.9)
        self.play(GrowArrow(fN), FadeIn(tN), Create(bar2), run_time=0.8)
        cL = cote(1.7, 4.9, 0.85, r"$L$"); cD = cote(4.9, 5.55, 0.85, r"$\Delta L$", col=BLEU)
        f2 = pos(M(r"\Delta L = \frac{N\,L}{E\,S} \qquad k = \frac{E\,S}{L}", sc=0.9, color=JAUNE), -6.3, 0.2)
        self.at(self.t("c2"), Ecrire(f2, rt=1.1), FadeIn(cL), FadeIn(cD), run_time=1.1)
        self.play(Create(enc(f2, col=JAUNE, buff=0.15)), run_time=0.4)
        h3 = pos(T(r"\textbf{Torsion} d'un arbre circulaire", sc=0.78, color=VERT), -6.3, -0.85)
        ys = -1.75; wall2 = encastrement(1.8, ys, h=1.0)
        arb = Rectangle(width=3.9, height=0.62, color=CRAIE, stroke_width=3).move_to([1.8 + 1.95, ys, 0])
        g0 = DashedLine([1.8, ys + 0.16, 0], [5.7, ys + 0.16, 0], color=GRIS, stroke_width=2, dash_length=0.08)
        g1 = Line([1.8, ys + 0.16, 0], [5.7, ys - 0.2, 0], color=BLEU, stroke_width=3)
        cp = couple(6.05, ys, r=0.55, col=ORANGE); tM = M(r"M_t", sc=0.68, color=ORANGE).next_to(cp, UP, buff=0.05)
        tt = M(r"\theta_x", sc=0.62, color=BLEU).move_to([5.25, ys - 0.62, 0])
        self.at(self.t("c3"), Ecrire(h3, rt=0.7), Create(wall2), Create(arb), Create(g0), run_time=0.9)
        self.at(self.a("c3", "tourne en bloc"), Create(cp), FadeIn(tM), Transform(g0.copy(), g1), FadeIn(tt), run_time=1.0)
        f4 = pos(M(r"\theta' = \frac{d\theta_x}{dx} = \frac{M_t}{G\,I_0}", sc=0.9, color=JAUNE), -6.3, -1.72)
        self.ecr(self.t("c4"), f4, rt=1.0); self.play(Create(enc(f4, col=JAUNE, buff=0.15)), run_time=0.4)
        f5 = pos(M(r"I_0 = \frac{\pi D^4}{32} \qquad \Delta\theta = \frac{M_t\,L}{G\,I_0}", sc=0.88), -6.3, -3.2)
        self.ecr(self.t("c5"), f5, rt=1.1)
        r6 = T(r"rappel :", sc=0.62, color=GRIS); f6 = M(r"\tau_{max} = \frac{16\,M_t}{\pi D^3}", sc=0.82, color=GRIS)
        g6 = VGroup(r6, f6).arrange(RIGHT, buff=0.25).move_to([4.0, -3.2, 0])
        self.ecr(self.t("c6"), g6, rt=1.0)
        self.fin()

# ---------------------------------------------------------------- S3
class S3(C):
    sid = "S3"
    def construct(self):
        self.entete(r"3.3 -- La déformée en flexion", "Flexion")
        l1 = pos(T(r"déformée : la courbe $v(x)$ de la ligne moyenne", sc=0.72), -6.3, 2.2)
        x0, x1, y1 = 2.0, 6.1, 1.75
        fig1 = VGroup(encastrement(x0, y1, h=1.0), poutre(x0, x1, y1))
        F1 = force(x1, y1, 0.8)
        d1 = lambda a: y1 - 0.85*((a - x0)/(x1 - x0))**2*(3 - (a - x0)/(x1 - x0))/2
        cv1 = courbe(d1, x0, x1)
        va = Arrow([5.3, y1, 0], [5.3, d1(5.3) + 0.03, 0], buff=0, color=ORANGE, stroke_width=3, tip_length=0.12, max_tip_length_to_length_ratio=0.35)
        vt = M(r"v(x)", sc=0.58, color=ORANGE).next_to(va, RIGHT, buff=0.08)
        self.at(self.t("d1"), Ecrire(l1, rt=1.0), Create(fig1[0]), Create(fig1[1]), GrowArrow(F1), run_time=1.0)
        self.at(self.a("d1", "que prend"), Create(cv1), GrowArrow(va), FadeIn(vt), run_time=1.0)
        f2 = pos(M(r"E\,I_{Gz}\,v'' = M_{fz}(x)", sc=1.05, color=JAUNE), -6.0, 1.3)
        self.ecr(self.a("d2", "E I G z"), f2, rt=1.0); self.play(Create(enc(f2, col=JAUNE, buff=0.18)), run_time=0.4)
        l3 = pos(T(r"convention : cohésion $=$ action de II (aval) sur I (amont)", sc=0.6, color=GRIS), -6.3, 0.35)
        self.ecr(self.t("d3"), l3, rt=1.1)
        l4 = pos(T(r"$E\,I_{Gz}$ : la \textbf{rigidité en flexion}", sc=0.68), -6.3, -0.3)
        self.ecr(self.t("d4"), l4, rt=0.8)
        l5 = pos(T(r"\textbf{Méthode} : intégrer deux fois, tronçon par tronçon", sc=0.7, color=BLEU), -6.3, -1.15)
        self.ecr(self.t("d5"), l5, rt=1.1)
        l6 = pos(T(r"encastrement : \; $v = 0$ \; et \; $v' = 0$", sc=0.7), -6.3, -1.9)
        c1 = T(r"$v = 0,\; v' = 0$", sc=0.55, color=VERT).move_to([x0 + 0.1, y1 - 0.85, 0])
        self.at(self.a("d6", "À un encastrement"), Ecrire(l6, rt=0.9), Indicate(fig1[0], color=VERT), FadeIn(c1), run_time=1.0)
        y2, a2, b2 = -1.45, 2.0, 6.1
        fig2 = VGroup(poutre(a2, b2, y2), pivot(a2, y2), glissant(b2, y2), repartie(a2, b2, y2, h=0.55, n=9))
        d2 = lambda a: y2 - 0.55*16/5*((a - a2)/(b2 - a2))*(1 - 2*((a - a2)/(b2 - a2))**2 + ((a - a2)/(b2 - a2))**3)
        cv2 = courbe(d2, a2, b2)
        z1 = T(r"$v = 0$", sc=0.55, color=VERT).move_to([a2, y2 - 0.85, 0]); z2 = T(r"$v = 0$", sc=0.55, color=VERT).move_to([b2, y2 - 0.85, 0])
        l7 = pos(T(r"appui : $v = 0$ \; ; \; entre tronçons : $v$, $v'$ continus", sc=0.7), -6.3, -2.6)
        self.at(self.t("d7"), Create(fig2[0]), FadeIn(fig2[1]), FadeIn(fig2[2]), FadeIn(fig2[3]), run_time=0.8)
        self.play(Ecrire(l7, rt=1.0), Create(cv2), FadeIn(z1), FadeIn(z2), run_time=1.0)
        l8 = pos(T(r"flèche $f = \max|v|$ \; ; \; charge vers le bas $\Rightarrow v < 0$", sc=0.7, color=ROUGE), -6.3, -3.4)
        fa = DoubleArrow([4.05, y2, 0], [4.05, d2(4.05), 0], buff=0, color=ROUGE, stroke_width=2, tip_length=0.1, max_tip_length_to_length_ratio=0.3)
        ftx = M("f", sc=0.62, color=ROUGE).next_to(fa, RIGHT, buff=0.06).shift(0.12*DOWN)
        self.at(self.t("d8"), Ecrire(l8, rt=1.1), GrowFromCenter(fa), FadeIn(ftx), run_time=1.1)
        self.fin()

# ---------------------------------------------------------------- S4
class S4(C):
    sid = "S4"
    def construct(self):
        self.entete(r"3.4 -- Flèches de référence et rigidité", "Rigidité")
        y = 1.75; cas = []
        for k, cx in enumerate([-5.2, -1.75, 1.75, 5.2]):
            a, b = cx - 1.2, cx + 1.2
            if k < 2: sup = encastrement(a, y, h=0.8, w=0.22)
            else: sup = VGroup(pivot(a, y, 0.85), glissant(b, y, 0.85))
            ch_ = force(b if k == 0 else cx, y, 0.7) if k in (0, 2) else repartie(a + (0.05 if k == 1 else 0), b, y, h=0.5, n=7)
            cas.append(VGroup(sup, poutre(a, b, y, sw=6), ch_))
        noms = [r"console, $F$ en bout", r"console, charge $p$", r"deux appuis, $F$ au milieu", r"deux appuis, charge $p$"]
        fs = [r"f = \frac{F L^3}{3\,E I}", r"f = \frac{p L^4}{8\,E I}", r"f = \frac{F L^3}{48\,E I}", r"f = \frac{5\,p L^4}{384\,E I}"]
        cols = [BLEU, VERT, ORANGE, ROUGE]
        lab = [T(n, sc=0.55, color=GRIS).move_to([cx, 0.92, 0]) for n, cx in zip(noms, [-5.2, -1.75, 1.75, 5.2])]
        frm = [M(f, sc=0.82, color=c).move_to([cx, 0.2, 0]) for f, c, cx in zip(fs, cols, [-5.2, -1.75, 1.75, 5.2])]
        self.at(self.t("e1"), *[Create(c[1]) for c in cas], run_time=0.8)
        for k, (ph_, fr_) in enumerate([("e2", "Console chargée"), ("e2", "Console sous"), ("e3", "Deux appuis, force"), ("e3", "Deux appuis, charge")]):
            self.at(self.a(ph_, fr_), FadeIn(cas[k][0]), FadeIn(cas[k][2]), FadeIn(lab[k]), Ecrire(frm[k], rt=0.8), run_time=0.9)
        l4 = T(r"petites perturbations : les flèches \textbf{se superposent}", sc=0.72, color=BLEU).move_to([0, -0.7, 0])
        self.ecr(self.t("e4"), l4, rt=1.1)
        g5 = VGroup(M(r"f \le f_{adm}", sc=0.85, color=JAUNE), T(r"charpente : de $L/200$ à $L/500$", sc=0.66, color=GRIS)).arrange(RIGHT, buff=0.4)
        pos(g5, -6.3, -1.45); self.ecr(self.t("e5"), g5, rt=1.1)
        g6 = VGroup(M(r"\theta' \le \theta'_{adm}", sc=0.85, color=JAUNE), T(r"long arbre : $\approx 0{,}25^\circ$/m", sc=0.66, color=GRIS)).arrange(RIGHT, buff=0.4)
        pos(g6, -6.3, -2.1); self.ecr(self.t("e6"), g6, rt=1.1)
        l7 = pos(T(r"piège : contrainte en $1/d^3$, \; flèche et angle en $1/d^4$", sc=0.72, color=ROUGE), -6.3, -2.75)
        self.ecr(self.t("e7"), l7, rt=1.1)
        l8 = T(r"calculer les \textbf{deux} dimensions minimales, garder la plus grande", sc=0.74, color=JAUNE).move_to([0, -3.45, 0])
        self.ecr(self.t("e8"), l8, rt=1.2); self.play(Create(enc(l8, col=JAUNE, buff=0.14)), run_time=0.4)
        self.fin()

# ---------------------------------------------------------------- S5
class S5(C):
    sid = "S5"
    def construct(self):
        self.entete(r"Exercice 1 -- La console : l'énoncé", "Exercice 1")
        y, x0, x1 = 1.45, -4.4, 1.4
        wall = encastrement(x0, y, h=1.4, w=0.32); be = poutre(x0, x1, y)
        tO = M("O", sc=0.65).move_to([x0 + 0.25, y - 0.32, 0]); tA = M("A", sc=0.65).move_to([x1 + 0.3, y - 0.3, 0])
        F = force(x1, y, 1.05); tF = M(r"F", sc=0.7, color=ROUGE).next_to(F, RIGHT, buff=0.1)
        rp = repere(-6.4, 0.25)
        self.at(self.t("f1"), Create(wall), Create(be), FadeIn(tO), run_time=0.9)
        self.at(self.a("f1", "porte un palan"), GrowArrow(F), FadeIn(tF), FadeIn(tA), FadeIn(rp), run_time=0.8)
        cL = cote(x0, x1, 0.55, r"$L = 1{,}2$ m")
        d1 = pos(T(r"$F = 1{,}5$ kN vers le bas \qquad poids propre négligé", sc=0.7), -6.3, -0.4)
        self.at(self.t("f2"), FadeIn(cL), Ecrire(d1, rt=1.2), run_time=1.2)
        sx, sy = 4.6, 1.4
        sec = Rectangle(width=0.55, height=1.1, color=CRAIE, stroke_width=3).set_fill(GRIS, 0.25).move_to([sx, sy, 0])
        ts = T("section", sc=0.58, color=GRIS).next_to(sec, UP, buff=0.15)
        cb = cote(sx - 0.275, sx + 0.275, sy - 0.75, r"$40$", sc=0.55)
        ch_ = DoubleArrow([sx + 0.5, sy - 0.55, 0], [sx + 0.5, sy + 0.55, 0], buff=0, color=GRIS, stroke_width=2, tip_length=0.13, max_tip_length_to_length_ratio=0.2)
        th_ = T(r"$80$", sc=0.55, color=GRIS).next_to(ch_, RIGHT, buff=0.08)
        yy = Arrow([sx - 0.75, sy - 0.4, 0], [sx - 0.75, sy + 0.4, 0], buff=0, color=GRIS, stroke_width=2, tip_length=0.12); ty = M(r"y", sc=0.55, color=GRIS).next_to(yy, LEFT, buff=0.06)
        d2 = pos(T(r"section $40 \times 80$ mm ($h = 80$ mm selon $\vec y$) \qquad acier : $E = 210$ GPa", sc=0.7), -6.3, -1.05)
        self.at(self.t("f3"), Create(sec), FadeIn(ts), FadeIn(cb), GrowFromCenter(ch_), FadeIn(th_), GrowArrow(yy), FadeIn(ty), run_time=0.9)
        self.ecr(self.a("f3", "Acier"), d2, rt=1.2)
        q = T(r"Déformée $v(x)$, flèche et rotation en A \; ; \; a-t-on $f \le L/400$ ?", sc=0.76, color=ROUGE).move_to([0, -2.0, 0])
        self.ecr(self.t("f4"), q, rt=1.3); self.play(Create(enc(q, buff=0.18)), run_time=0.4)
        rf = T(r"Réfléchissons : $M_{fz}(x)$, puis double intégration, conditions de l'encastrement", sc=0.66, color=BLEU).move_to([0, -2.95, 0])
        self.ecr(self.t("f5"), rf, rt=1.3)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.72, color=JAUNE).move_to([-0.6, -3.6, 0])
        self.ecr(self.t("f6"), av, rt=0.7)
        self.pause5(self.a("f6", "Mettez"), 2.4, -3.6)
        self.fin()

# ---------------------------------------------------------------- S6
class S6(C):
    sid = "S6"
    def construct(self):
        self.entete(r"Exercice 1 -- La résolution", "Exercice 1")
        y, x0, x1 = 2.15, 1.7, 5.9
        wall = encastrement(x0, y, h=0.9, w=0.25); be = poutre(x0, x1, y, sw=7); F = force(x1, y, 0.7)
        tO = M("O", sc=0.58).move_to([x0 + 0.2, y - 0.28, 0]); tA = M("A", sc=0.58).move_to([x1 + 0.3, y + 0.22, 0]); tF = M("F", sc=0.62, color=ROUGE).next_to(F, LEFT, buff=0.08)
        self.add(wall, be, F, tO, tA, tF)
        xg = 3.3; dG = Dot([xg, y, 0], radius=0.07, color=JAUNE); tG = M("G", sc=0.58, color=JAUNE).move_to([xg, y + 0.3, 0])
        seg = Line([xg, y, 0], [x1, y, 0], color=ORANGE, stroke_width=11)
        self.at(self.a("g1", "On isole"), FadeIn(dG), FadeIn(tG), Create(seg), run_time=0.8)
        m1 = self.etape(1, BLEU, 2.3, M(r"T_y = -F, \qquad M_{fz} = -F\,(L - x)", sc=0.74), self.t("g2"), 1.1)
        ax, fr = cadre(3.8, 0.45, 4.2, 1.05, 0, 1, -1.15, 0.2)
        mf = crb(ax, lambda s: -(1 - s), 0, 1); ar = aire(ax, lambda s: -(1 - s), 0, 1)
        tm = M(r"M_{fz}(x)", sc=0.55, color=ORANGE).move_to(ax.c2p(0.8, -0.75)); tfl = M(r"-FL", sc=0.55, color=ORANGE).move_to(ax.c2p(0.12, -0.55))
        self.at(self.a("g2", "M f z égale"), FadeOut(seg), Create(fr), Create(zero(ax, 0, 1)), Create(mf), FadeIn(ar), FadeIn(tm), FadeIn(tfl), run_time=1.0)
        self.etape(2, VERT, 1.55, M(r"E I_{Gz}\,v'' = -F\,(L - x)", sc=0.74), self.t("g3"), 0.9)
        l4 = pos(M(r"E I_{Gz}\,v' = -F\,(Lx - x^2/2) + C_1", sc=0.72), -5.85, 0.85)
        self.ecr(self.a("g4", "E I v prime"), l4, rt=1.0)
        c4 = pos(M(r"v'(0) = 0 \;\Rightarrow\; C_1 = 0", sc=0.68, color=GRIS), -5.3, 0.22)
        self.ecr(self.a("g4", "la pente est nulle"), c4, rt=0.8)
        l5 = pos(M(r"E I_{Gz}\,v = -F\,(Lx^2/2 - x^3/6) + C_2", sc=0.72), -5.85, -0.45)
        self.ecr(self.t("g5"), l5, rt=1.0)
        c5 = pos(M(r"v(0) = 0 \;\Rightarrow\; C_2 = 0", sc=0.68, color=GRIS), -5.3, -1.08)
        self.ecr(self.t("g5b"), c5, rt=0.8)
        r6 = self.etape(3, ORANGE, -1.95, M(r"v(L) = -\frac{F L^3}{3\,E I_{Gz}}", sc=0.74, color=JAUNE), self.t("g6"), 1.0)
        dv = courbe(lambda a: y - 0.6*((a - x0)/(x1 - x0))**2*(3 - (a - x0)/(x1 - x0))/2, x0, x1)
        fa = DoubleArrow([x1 + 0.35, y, 0], [x1 + 0.35, y - 0.6, 0], buff=0, color=BLEU, stroke_width=2, tip_length=0.1, max_tip_length_to_length_ratio=0.3)
        ft = M("f", sc=0.62, color=BLEU).next_to(fa, RIGHT, buff=0.06)
        self.at(self.a("g6", "Elle est maximale"), Create(dv), GrowFromCenter(fa), FadeIn(ft), run_time=1.0)
        self.at(self.a("g6", "On retrouve"), Create(enc(r6, col=JAUNE, buff=0.12)), run_time=0.4)
        r7 = M(r"v'(L) = -\frac{F L^2}{2\,E I_{Gz}}", sc=0.74, color=JAUNE).next_to(r6, RIGHT, buff=0.7)
        self.ecr(self.t("g7"), r7, rt=0.9)
        l8 = pos(T(r"$v < 0$ : il descend \; ; \; $FL^3/(EI)$ en mètres \checkmark", sc=0.64, color=VERT), -5.85, -2.95)
        self.ecr(self.t("g8"), l8, rt=1.2)
        self.etape(4, ROUGE, -0.55, M(r"I_{Gz} = \frac{b h^3}{12} \approx 1{,}71\cdot10^{6}\ \mathrm{mm^4}", sc=0.66), self.a("g9", "I G z"), 1.0, x=1.55)
        n1 = pos(M(r"f \approx 2{,}4\ \mathrm{mm}", sc=0.8, color=JAUNE), 2.05, -1.6)
        n2 = pos(M(r"|\theta_z(A)| \approx 3{,}0\cdot10^{-3}\ \mathrm{rad} \approx 0{,}17^\circ", sc=0.64), 2.05, -2.25)
        self.ecr(self.t("g10"), n1, rt=0.7); self.play(Create(enc(n1, col=JAUNE, buff=0.12)), run_time=0.3)
        self.ecr(self.a("g10", "et une rotation"), n2, rt=1.0)
        n3 = pos(T(r"$L/400 = 3$ mm : \textbf{respecté} !", sc=0.7, color=VERT), 2.05, -2.9)
        self.ecr(self.t("g11"), n3, rt=0.8)
        n4 = pos(T(r"$f \propto L^3$ : \; $L \times 2 \;\Rightarrow\; f \times 8$ !", sc=0.7, color=ROUGE), 2.05, -3.5)
        self.ecr(self.a("g12", "Avec un bras"), n4, rt=0.9)
        self.fin()

# ---------------------------------------------------------------- S7
IPE = [[r"profilé", r"$I_{Gz}$ (cm$^4$)", r"$h$ (mm)"], ["IPE 140", "541", "140"], ["IPE 160", "869", "160"], ["IPE 180", "1317", "180"], ["IPE 200", "1943", "200"]]
class S7(C):
    sid = "S7"
    def construct(self):
        self.entete(r"Exercice 2 -- La poutre sur deux appuis : l'énoncé", "Exercice 2")
        y, xa, xb = 1.25, -5.0, 0.9
        be = poutre(xa, xb, y); pA = pivot(xa, y); pB = glissant(xb, y)
        tA = M("A", sc=0.65).move_to([xa - 0.5, y - 0.2, 0]); tB = M("B", sc=0.65).move_to([xb + 0.5, y - 0.2, 0])
        rp = repere(-6.6, 0.1)
        self.at(self.t("h1"), Create(be), FadeIn(rp), run_time=0.7)
        self.at(self.a("h1", "articulation"), FadeIn(pA), FadeIn(tA), run_time=0.5)
        self.at(self.a("h1", "appui simple"), FadeIn(pB), FadeIn(tB), run_time=0.5)
        q = repartie(xa, xb, y, h=0.75, n=12); tq = T(r"$p = 5$ kN/m", sc=0.66, color=ORANGE).move_to([(xa + xb)/2, y + 1.05, 0])
        cL = cote(xa, xb, 0.3, r"$L = 4$ m")
        self.at(self.t("h2"), FadeIn(q, shift=0.2*DOWN), FadeIn(tq), FadeIn(cL), run_time=1.0)
        d1 = pos(T(r"profilé IPE en acier : \; $E = 210$ GPa, \; $R_{pe} = 157$ MPa", sc=0.7), -6.3, -0.6)
        self.ecr(self.t("h3"), d1, rt=1.2)
        tb = tableau(IPE, [2.75, 4.55, 6.15], 2.25, 0.52)
        self.at(self.a("h4", "dans ce tableau"), FadeIn(tb), run_time=0.8)
        qq = T(r"Flèche au milieu ? \; Plus petit IPE tel que $f \le L/300$ ?", sc=0.76, color=ROUGE).move_to([0, -1.5, 0])
        self.ecr(self.t("h4"), qq, rt=1.2); self.play(Create(enc(qq, buff=0.18)), run_time=0.4)
        rf = VGroup(T(r"Réfléchissons : double intégration, mais \textbf{autres} conditions aux limites,", sc=0.64, color=BLEU),
                    T(r"puis le critère de rigidité donne $I_{Gz}$ minimal", sc=0.64, color=BLEU)).arrange(DOWN, buff=0.1).move_to([0, -2.55, 0])
        self.ecr(self.t("h5"), rf, rt=1.4)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.72, color=JAUNE).move_to([-0.6, -3.5, 0])
        self.ecr(self.t("h6"), av, rt=0.7)
        self.pause5(self.a("h6", "Mettez"), 2.4, -3.5)
        self.fin()

# ---------------------------------------------------------------- S8
class S8(C):
    sid = "S8"
    def construct(self):
        self.entete(r"Exercice 2 -- La déformée", "Exercice 2")
        y, xa, xb = 1.95, 1.7, 6.1
        fig = VGroup(poutre(xa, xb, y, sw=7), pivot(xa, y, 0.85), glissant(xb, y, 0.85), repartie(xa, xb, y, h=0.6, n=10))
        tA = M("A", sc=0.58).move_to([xa - 0.42, y - 0.15, 0]); tB = M("B", sc=0.58).move_to([xb + 0.42, y - 0.15, 0])
        self.add(fig, tA, tB)
        self.etape(1, BLEU, 2.3, M(r"Y_A = Y_B = \frac{pL}{2}", sc=0.74), self.t("i1"), 0.8)
        l2 = pos(M(r"M_{fz} = \frac{p\,x\,(L - x)}{2}, \qquad M_{max} = \frac{pL^2}{8}", sc=0.72), -5.85, 1.5)
        ax, fr = cadre(3.9, 0.55, 4.4, 1.05, 0, 1, -0.15, 1.15)
        par = lambda s: 4*s*(1 - s)
        cm = crb(ax, par, 0, 1); am = aire(ax, par, 0, 1)
        tm = M(r"M_{fz}(x)", sc=0.52, color=ORANGE).move_to(ax.c2p(0.13, 0.85)); tmx = M(r"\frac{pL^2}{8}", sc=0.52, color=ORANGE).move_to(ax.c2p(0.5, 0.42))
        self.ecr(self.a("i2", "M f z égale"), l2, rt=1.1)
        self.at(self.a("i2", "Une parabole"), Create(fr), Create(zero(ax, 0, 1)), Create(cm), FadeIn(am), FadeIn(tm), FadeIn(tmx), run_time=1.0)
        self.etape(2, VERT, 0.7, M(r"E I_{Gz}\,v'' = \frac{p}{2}\,(Lx - x^2)", sc=0.74), self.t("i3"), 1.0)
        l4 = pos(M(r"E I_{Gz}\,v' = \frac{pLx^2}{4} - \frac{px^3}{6} + C_1", sc=0.72), -5.85, -0.08)
        self.ecr(self.t("i4"), l4, rt=1.1)
        l4b = pos(M(r"E I_{Gz}\,v = \frac{pLx^3}{12} - \frac{px^4}{24} + C_1 x + C_2", sc=0.72), -5.85, -0.88)
        self.ecr(self.t("i4b"), l4b, rt=1.2)
        self.etape(3, ORANGE, -1.7, T(r"pas d'encastrement : seulement $v(0) = 0$ et $v(L) = 0$", sc=0.64, color=ROUGE), self.t("i5"), 1.1)
        self.play(Indicate(fig[1], color=ROUGE), Indicate(fig[2], color=ROUGE), run_time=0.8)
        c6 = pos(M(r"C_2 = 0", sc=0.74), -5.85, -2.45)
        self.ecr(self.a("i6", "En A"), c6, rt=0.5)
        c7 = M(r"C_1 = -\frac{pL^3}{24}", sc=0.74).next_to(c6, RIGHT, buff=0.7)
        self.ecr(self.a("i7", "Donc C un"), c7, rt=0.8)
        l8 = pos(T(r"contrôle : $v'(L/2) = 0$ (symétrie) \checkmark", sc=0.66, color=VERT), -5.85, -3.3)
        self.ecr(self.a("i8", "Et v prime"), l8, rt=0.9)
        av, fv = cadre(3.9, -0.95, 4.4, 1.05, 0, 1, -1.15, 0.15)
        vn = lambda s: -s*(1 - 2*s**2 + s**3)/0.3125
        cvv = crb(av, vn, 0, 1, col=BLEU); avv = aire(av, vn, 0, 1, col=BLEU, op=0.15)
        tv = M(r"v(x)", sc=0.52, color=BLEU).move_to(av.c2p(0.12, -0.75))
        self.at(self.t("i9"), Create(fv), Create(zero(av, 0, 1)), Create(cvv), FadeIn(avv), FadeIn(tv), run_time=1.0)
        r9 = M(r"f = \left|v\!\left(\frac{L}{2}\right)\right| = \frac{5\,pL^4}{384\,E I_{Gz}}", sc=0.78, color=JAUNE).move_to([3.95, -2.45, 0])
        ca = carte(4, ROUGE, 1.55, -2.45)
        self.at(self.a("i9", "v de L sur deux"), Create(ca[0]), FadeIn(ca[1]), Ecrire(r9, rt=1.1), run_time=1.1)
        self.play(Create(enc(r9, col=JAUNE, buff=0.12)), run_time=0.4)
        l10 = T(r"le fameux $5/384$ \; ; \; $v < 0$ : elle descend", sc=0.64, color=VERT).move_to([4.15, -3.35, 0])
        self.ecr(self.t("i10"), l10, rt=0.9)
        self.fin()

# ---------------------------------------------------------------- S9
class S9(C):
    sid = "S9"
    def construct(self):
        self.entete(r"Exercice 2 -- Choisir le profilé", "Exercice 2")
        tb = tableau(IPE, [2.85, 4.6, 6.15], 2.3, 0.52); self.add(tb)
        self.etape(5, BLEU, 2.3, M(r"f_{adm} = \frac{L}{300} \approx 13{,}3\ \mathrm{mm}", sc=0.74), self.t("j1"), 0.9)
        l2 = pos(M(r"\frac{5\,pL^4}{384\,E I_{Gz}} \le \frac{L}{300} \;\Rightarrow\; I_{Gz} \ge \frac{1500\,pL^3}{384\,E}", sc=0.72), -5.85, 1.4)
        self.ecr(self.t("j2"), l2, rt=1.3)
        l3 = pos(M(r"p = 5\ \mathrm{N/mm}, \qquad L = 4000\ \mathrm{mm}", sc=0.7, color=GRIS), -5.85, 0.55)
        self.ecr(self.t("j3"), l3, rt=0.9)
        l3b = pos(M(r"I_{Gz} \ge 5{,}95\cdot10^6\ \mathrm{mm^4} = 595\ \mathrm{cm^4}", sc=0.76, color=JAUNE), -5.85, -0.2)
        self.ecr(self.t("j3b"), l3b, rt=1.0); self.play(Create(enc(l3b, col=JAUNE, buff=0.12)), run_time=0.3)
        r140 = VGroup(*tb[3:6]); r160 = VGroup(*tb[6:9])
        bar = Line(r140.get_left() + 0.15*LEFT, r140.get_right() + 0.15*RIGHT, color=ROUGE, stroke_width=4)
        no = T(r"trop juste", sc=0.52, color=ROUGE).next_to(bar, DOWN, buff=0.04).align_to(bar, RIGHT)
        bx = SurroundingRectangle(r160, color=VERT, buff=0.1, corner_radius=0.06)
        self.at(self.a("j4", "n'a que"), Create(bar), run_time=0.5)
        self.at(self.a("j4", "raté"), FadeIn(no), run_time=0.4)
        self.at(self.a("j4", "convient"), Create(bx), run_time=0.5)
        l5 = pos(M(r"\text{IPE 160} : \; f \approx 9{,}1\ \mathrm{mm} \le 13{,}3\ \mathrm{mm}", sc=0.72, color=VERT), -5.85, -1.05)
        self.ecr(self.t("j5"), l5, rt=1.1)
        self.etape(6, ORANGE, -1.9, M(r"M_{max} = \frac{pL^2}{8} = 10\ \mathrm{kN\cdot m}", sc=0.74), self.t("j6"), 1.0)
        l7 = pos(M(r"\sigma_{max} = \frac{M_{max}\,h/2}{I_{Gz}} \approx 92\ \mathrm{MPa} \le 157\ \mathrm{MPa}", sc=0.72), -5.85, -2.75)
        self.ecr(self.t("j7"), l7, rt=1.2)
        l8 = pos(T(r"IPE 140 : $129$ MPa, il résistait : la \textbf{rigidité} dimensionne", sc=0.64, color=ROUGE), -5.85, -3.5)
        self.ecr(self.t("j8"), l8, rt=1.1)
        mo = VGroup(T(r"Moralité : une grande portée", sc=0.68, color=JAUNE), T(r"se dimensionne par sa \textbf{flèche}", sc=0.68, color=JAUNE)).arrange(DOWN, buff=0.1).move_to([4.5, -0.6, 0])
        self.ecr(self.t("j9"), mo, rt=1.0); self.play(Create(enc(mo, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

# ---------------------------------------------------------------- S10
class S10(C):
    sid = "S10"
    def construct(self):
        self.entete(r"Exercice 3 -- L'arbre de transmission : l'énoncé", "Exercice 3")
        y = 1.6
        mo = VGroup(Rectangle(width=1.7, height=1.15, color=BLEU, stroke_width=3).move_to([-5.3, y, 0]), T("moteur", sc=0.6, color=BLEU).move_to([-5.3, y, 0]))
        pm = VGroup(Rectangle(width=1.7, height=1.15, color=VERT, stroke_width=3).move_to([2.9, y, 0]), T("pompe", sc=0.6, color=VERT).move_to([2.9, y, 0]))
        ar = Rectangle(width=5.6, height=0.3, color=CRAIE, stroke_width=3).set_fill(GRIS, 0.2).move_to([-1.2, y, 0])
        c1 = couple(-3.65, y, r=0.5, sens=1); c2 = couple(1.25, y, r=0.5, sens=-1)
        t1 = M(r"M_t", sc=0.65, color=ORANGE).next_to(c1, UP, buff=0.05); t2 = M(r"-M_t", sc=0.65, color=ORANGE).next_to(c2, UP, buff=0.05)
        rx = Arrow([-1.9, y - 0.75, 0], [-1.0, y - 0.75, 0], buff=0, color=GRIS, stroke_width=3, tip_length=0.14); tx = M("x", sc=0.6, color=GRIS).next_to(rx, RIGHT, buff=0.08)
        self.at(self.t("k1"), Create(mo[0]), FadeIn(mo[1]), run_time=0.6)
        self.at(self.a("k1", "entraîne une pompe"), Create(pm[0]), FadeIn(pm[1]), Create(ar), run_time=0.8)
        self.at(self.a("k1", "un long arbre"), Create(c1), Create(c2), FadeIn(t1), FadeIn(t2), GrowArrow(rx), FadeIn(tx), run_time=0.8)
        d1 = pos(T(r"$P = 11$ kW \qquad $N = 1\,500$ tr/min \qquad arbre plein en acier", sc=0.72), -6.3, 0.2)
        self.ecr(self.a("k1", "Un moteur"), d1, rt=1.2)
        d2 = pos(T(r"$G = 81$ GPa \qquad $R_{pg} = 50$ MPa", sc=0.72), -6.3, -0.45)
        self.ecr(self.t("k2"), d2, rt=0.9)
        d3 = pos(T(r"angle unitaire : \; $\theta' \le \theta'_{adm} = 0{,}25^\circ$/m", sc=0.72), -6.3, -1.1)
        self.ecr(self.t("k3"), d3, rt=1.0)
        q = VGroup(T(r"$d_{min}$ en résistance, puis en rigidité : lequel l'emporte ?", sc=0.74, color=ROUGE),
                   T(r"diamètres normalisés : 20, 25, 30, 35, 40, 45 mm", sc=0.6, color=GRIS)).arrange(DOWN, buff=0.12).move_to([0, -2.05, 0])
        self.ecr(self.t("k4"), q, rt=1.4); self.play(Create(enc(q, buff=0.16)), run_time=0.4)
        q2 = T(r"Et un acier allié $3$ fois plus résistant : bonne idée ?", sc=0.72, color=ROUGE).move_to([0, -3.0, 0])
        self.ecr(self.t("k5"), q2, rt=1.1)
        rf = T(r"Réfléchissons : le couple, puis une inégalité par critère ; attention aux unités !", sc=0.62, color=BLEU).move_to([0, -3.65, 0])
        self.ecr(self.t("k6"), rf, rt=1.2)
        av = T(r"\textbf{À vous !}", sc=0.72, color=JAUNE).move_to([5.0, -0.45, 0])
        self.ecr(self.t("k7"), av, rt=0.5)
        self.pause5(self.a("k7", "Mettez"), 6.2, -0.45)
        self.fin()

# ---------------------------------------------------------------- S11
class S11(C):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice 3 -- Résistance ou rigidité ?", "Exercice 3")
        self.etape(1, BLEU, 2.3, M(r"\omega = \frac{\pi N}{30} \approx 157\ \mathrm{rad/s}", sc=0.74), self.a("l1", "Oméga"), 1.0)
        l2 = pos(M(r"M_t = \frac{P}{\omega} \approx 70\ \mathrm{N\cdot m} = 7{,}0\cdot10^4\ \mathrm{N\cdot mm}", sc=0.72), -5.85, 1.5)
        self.ecr(self.t("l2"), l2, rt=1.2)
        self.etape(2, ORANGE, 0.7, M(r"\tau_{max} = \frac{16\,M_t}{\pi d^3} \le R_{pg}", sc=0.74), self.t("l3"), 1.0)
        l4 = pos(M(r"d \ge \sqrt[3]{\frac{16\,M_t}{\pi R_{pg}}} \approx 19{,}3\ \mathrm{mm}", sc=0.74, color=ORANGE), -5.85, -0.12)
        self.ecr(self.t("l4"), l4, rt=1.1)
        # barres : diamètres minimaux (échelle 45 mm -> 4,1)
        k_, xb0 = 4.1/45, 2.15
        tt = T(r"diamètre minimal (mm)", sc=0.56, color=GRIS).move_to([4.2, 2.45, 0])
        def barre(d, yy, col): return Rectangle(width=d*k_, height=0.32, color=col, stroke_width=0).set_fill(col, 0.85).move_to([xb0 + d*k_/2, yy, 0])
        b1 = barre(19.25, 1.6, ORANGE); n1 = T(r"résistance", sc=0.56, color=ORANGE).next_to(b1, UP, buff=0.06).align_to(b1, LEFT)
        v1 = T(r"$19{,}3$", sc=0.58, color=ORANGE).next_to(b1, RIGHT, buff=0.1)
        self.at(self.a("l4", "D'où d"), FadeIn(tt), GrowFromEdge(b1, LEFT), FadeIn(n1), FadeIn(v1), run_time=0.8)
        self.etape(3, VERT, -0.95, T(r"rigidité : l'angle en \textbf{rad/mm} !", sc=0.66, color=ROUGE), self.t("l5"), 0.9)
        l6 = pos(M(r"\theta'_{adm} = 0{,}25^\circ/\mathrm{m} = 4{,}36\cdot10^{-6}\ \mathrm{rad/mm}", sc=0.72), -5.85, -1.7)
        self.ecr(self.t("l6"), l6, rt=1.2)
        l7 = pos(M(r"\frac{M_t}{G\,I_0} \le \theta'_{adm} \;\Rightarrow\; I_0 \ge \frac{M_t}{G\,\theta'_{adm}}", sc=0.72), -5.85, -2.5)
        self.ecr(self.t("l7"), l7, rt=1.2)
        l8 = pos(M(r"I_0 \ge 1{,}98\cdot10^5\ \mathrm{mm^4} \;\Rightarrow\; d \ge 37{,}7\ \mathrm{mm}", sc=0.74, color=VERT), -5.85, -3.35)
        self.ecr(self.t("l8"), l8, rt=1.2)
        b2 = barre(37.69, 0.8, VERT); n2 = T(r"rigidité", sc=0.56, color=VERT).next_to(b2, UP, buff=0.06).align_to(b2, LEFT)
        v2 = T(r"$37{,}7$", sc=0.58, color=VERT).next_to(b2, RIGHT, buff=0.1)
        self.at(self.a("l8", "d dépasse"), GrowFromEdge(b2, LEFT), FadeIn(n2), FadeIn(v2), run_time=0.8)
        x40 = xb0 + 40*k_
        lim = DashedLine([x40, 2.05, 0], [x40, 0.45, 0], color=JAUNE, stroke_width=3, dash_length=0.08)
        t40 = T(r"$d = 40$ mm", sc=0.62, color=JAUNE).move_to([x40, 0.15, 0])
        ca = carte(4, JAUNE, 2.35, -0.45)
        r9 = pos(T(r"la \textbf{rigidité} l'emporte", sc=0.66, color=JAUNE), 2.85, -0.45)
        self.at(self.t("l9"), Create(ca[0]), FadeIn(ca[1]), Ecrire(r9, rt=0.8), run_time=0.8)
        self.at(self.a("l9", "on choisit"), Create(lim), FadeIn(t40), run_time=0.6)
        self.play(Create(enc(t40, col=JAUNE, buff=0.08)), run_time=0.3)
        v10 = T(r"à 40 mm : $\theta' \approx 0{,}20^\circ$/m, \; $\tau_{max} \approx 5{,}6$ MPa", sc=0.58, color=VERT).move_to([4.45, -1.15, 0])
        self.ecr(self.t("l10"), v10, rt=1.1)
        t11 = T(r"acier allié ($R_{pg} \times 3$) :", sc=0.6, color=ROUGE).move_to([4.45, -1.85, 0])
        f11 = M(r"d \ge \frac{19{,}3}{\sqrt[3]{3}} \approx 13{,}4\ \mathrm{mm}", sc=0.68, color=ROUGE).move_to([4.45, -2.5, 0])
        self.ecr(self.t("l11"), t11, rt=0.7)
        b1n = barre(13.35, 1.6, ORANGE); v1n = T(r"$13{,}4$", sc=0.58, color=ORANGE).next_to(b1n, RIGHT, buff=0.1)
        self.at(self.a("l11", "dix-neuf"), Ecrire(f11, rt=1.0), Transform(b1, b1n), Transform(v1, v1n), run_time=1.0)
        t12 = T(r"même $G$ : \; $d = 40$ mm \textbf{inchangé}", sc=0.62, color=VERT).move_to([4.45, -3.1, 0])
        self.ecr(self.t("l12"), t12, rt=0.9)
        self.at(self.a("l12", "Le diamètre"), Indicate(b2, color=JAUNE, scale_factor=1.05), run_time=0.7)
        t13 = T(r"fausse bonne idée $\Rightarrow$ arbre creux", sc=0.62, color=JAUNE).move_to([4.45, -3.65, 0])
        self.ecr(self.a("l13", "Pour alléger"), t13, rt=0.9)
        self.fin()

# ---------------------------------------------------------------- S12
class S12(C):
    sid = "S12"
    def construct(self):
        self.entete(r"Ce qu'il faut retenir : la méthode", "Bilan")
        pts = [("m2", [r"\textbf{Modèle} : liaisons, charges, repère, convention du torseur de cohésion"], BLEU),
               ("m3", [r"\textbf{Efforts intérieurs} : $M_{fz}(x)$, $M_t$, tronçon par tronçon"], VERT),
               ("m4", [r"\textbf{Déformée} : $E I_{Gz}\,v'' = M_{fz}$, deux intégrations, conditions aux limites", r"(ou cas de référence superposés)"], ORANGE),
               ("m5", [r"\textbf{Contrôles} : signe, unités (N, mm, MPa ; radians), ordre de grandeur"], ROUGE),
               ("m6", [r"\textbf{Deux critères}, résistance et rigidité : garder la plus grande dimension"], JAUNE)]
        ys = [2.15, 1.3, 0.35, -0.6, -1.45]
        for k, ((ph_, txt, c), yy) in enumerate(zip(pts, ys)):
            ca = carte(k+1, c, -6.0, yy)
            tx = VGroup(*[T(t_, sc=0.7 if i == 0 else 0.62, color=CRAIE if i == 0 else GRIS) for i, t_ in enumerate(txt)]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            pos(tx, -5.45, yy)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.9)
        if True:
            tr = Line([-5.0, -2.25, 0], [5.0, -2.25, 0], color=JAUNE, stroke_width=1.5, stroke_opacity=0.5)
            c1 = T(r"torseur de cohésion \; $\to$ \; contraintes \; $\to$ \; déformations", sc=0.7, color=GRIS).move_to([0, -2.75, 0])
            self.at(self.t("m7"), Create(tr), Ecrire(c1, rt=1.1), run_time=1.1)
            c2 = T(r"Une pièce doit \textbf{tenir}, et rester assez \textbf{rigide} pour sa fonction.", sc=0.76, color=JAUNE).move_to([0, -3.45, 0])
            self.ecr(self.t("m8"), c2, rt=1.2)
        self.fin()
