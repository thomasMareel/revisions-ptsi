from base import *
from scipy import signal
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)
def chrono(x, y):
    pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([x, y, 0])
    arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
    return pa, arc
def axes(x, y, w, h, xr, yr, col=CRAIE, sw=2):
    return Axes(x_range=xr, y_range=yr, x_length=w, y_length=h,
                axis_config={"color": col, "stroke_width": sw, "include_ticks": False, "tip_width": 0.14, "tip_height": 0.14}).move_to([x, y, 0])
def croix(p, col=ROUGE, r=0.12):
    return VGroup(Line(p + np.array([-r, -r, 0]), p + np.array([r, r, 0]), color=col, stroke_width=5),
                  Line(p + np.array([-r, r, 0]), p + np.array([r, -r, 0]), color=col, stroke_width=5))
def blk(lab, x, y, w=1.6, h=0.75, col=CRAIE, sc=0.7):
    r = Rectangle(width=w, height=h, color=col, stroke_width=3).move_to([x, y, 0])
    t = M(lab, sc=sc, color=col).move_to(r)
    if t.width > w - 0.15: t.scale_to_fit_width(w - 0.2)
    return VGroup(r, t)
def som(x, y, r=0.24, col=CRAIE):
    d = r*0.7
    return VGroup(Circle(radius=r, color=col, stroke_width=3).move_to([x, y, 0]), Line([x-d, y-d, 0], [x+d, y+d, 0], color=col, stroke_width=2), Line([x-d, y+d, 0], [x+d, y-d, 0], color=col, stroke_width=2))
def fl(*pts, col=CRAIE, sw=3):
    pts = [np.array([p[0], p[1], 0]) for p in pts]
    g = VGroup(*[Line(pts[i], pts[i+1], color=col, stroke_width=sw) for i in range(len(pts) - 2)])
    g.add(Arrow(pts[-2], pts[-1], buff=0, color=col, stroke_width=sw, max_tip_length_to_length_ratio=0.5, tip_length=0.18))
    return g
def indic(z, t):
    _, y = signal.step(signal.lti([1], [1, 2*z, 1]), T=t)
    return y
def courbe(ax, t, y, col, sw=4):
    return VMobject(color=col, stroke_width=sw).set_points_smoothly([ax.c2p(a, b) for a, b in zip(t, y)])
def t5(z):
    t = np.linspace(0, 60*max(1, z*z) if z >= 0.1 else 400, 60000)
    y = indic(z, t); out = np.where(np.abs(y - 1) > 0.05)[0]
    return t[out[-1]+1]

def cadre(x, y, w, h, l0, l1, g0, g1):
    ax = Axes(x_range=[l0, l1, 1], y_range=[g0, g1, 1], x_length=w, y_length=h, tips=False,
              axis_config={"stroke_opacity": 0, "include_ticks": False}).move_to([x, y, 0])
    fr = Rectangle(width=w, height=h, color=GRIS, stroke_width=2).move_to([x, y, 0])
    return ax, fr

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PTSI", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Automatique -- Chapitre 4}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Systèmes du deuxième ordre", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        ax = axes(3.6, -1.0, 4.4, 2.6, [0, 12, 2], [0, 1.6, 1])
        t = np.linspace(0, 11.8, 200); cb = courbe(ax, t, indic(0.25, t), BLEU, 5)
        self.at(self.a("a1", "la caisse monte"), Create(ax), run_time=0.5); self.play(Create(cb), run_time=2.0)
        items = []
        for k, (txt, c) in enumerate([("Le modèle et ses pôles", BLEU), ("Le dépassement", VERT), ("Le temps de réponse", ORANGE),
                                       ("La résonance", ROUGE), ("Identifier un deuxième ordre", BLEU), ("Exercice résolu : régler un gain", JAUNE)]):
            yy = 0.75 - 0.6*k
            items.append(VGroup(carte(k+1, c, -6.2, yy), pos(T(txt, sc=0.74), -5.65, yy)))
        for it, (sid, fr) in zip(items, [("a3", "le modèle et ses pôles"), ("a3", "le dépassement"), ("a3", "le temps de réponse"),
                                         ("a3", "la résonance"), ("a3", "et l'identification"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"4.1 -- Le modèle du deuxième ordre", "Deuxième ordre")
        h = M(r"H(p) = \frac{K}{1 + \frac{2\xi}{\omega_0}\,p + \frac{p^2}{\omega_0^2}}", sc=1.1, color=JAUNE).move_to([0, 1.75, 0])
        self.ecr(self.a("b1", "La forme canonique"), h, rt=1.3); self.play(Create(enc(h, col=JAUNE)), run_time=0.4)
        ps = [(r"$K$ : gain statique", "K, le gain", -4.6), (r"$\omega_0$ : pulsation propre", "la pulsation propre", -0.6), (r"$\xi$ : amortissement", "le coefficient", 3.4)]
        for txt, fr, x in ps:
            m = T(txt, sc=0.72, color=BLEU).move_to([x, 0.45, 0]); self.ecr(self.a("b2", fr), m, rt=0.7)
        e = pos(M(r"m\,x'' + f\,x' + k\,x = F", sc=0.9), -6.3, -0.75)
        self.ecr(self.a("b3", "une masse"), e, rt=0.9)
        # petit dessin : masse, ressort, amortisseur
        sol = Line([1.5, -3.0, 0], [5.5, -3.0, 0], color=GRIS, stroke_width=3)
        mas = Rectangle(width=1.5, height=0.7, color=CRAIE, stroke_width=3).move_to([3.5, -0.8, 0]); lm = M("m", sc=0.7).move_to(mas)
        zz = [np.array([2.8, -3.0, 0])] + [np.array([2.8 + (0.18 if i % 2 else -0.18), -3.0 + 0.25*(i+1), 0]) for i in range(7)] + [np.array([2.8, -1.15, 0])]
        res = VMobject(color=BLEU, stroke_width=3).set_points_as_corners(zz)
        am = VGroup(Line([4.2, -3.0, 0], [4.2, -2.3, 0], color=ORANGE, stroke_width=3), Rectangle(width=0.4, height=0.6, color=ORANGE, stroke_width=3).move_to([4.2, -2.0, 0]),
                    Line([4.2, -2.15, 0], [4.2, -1.15, 0], color=ORANGE, stroke_width=3))
        lk = M("k", sc=0.6, color=BLEU).next_to(res, LEFT, buff=0.15); lf = M("f", sc=0.6, color=ORANGE).next_to(am, RIGHT, buff=0.15)
        self.at(self.a("b3", "un ressort"), Create(sol), Create(mas), FadeIn(lm), Create(res), Create(am), FadeIn(lk), FadeIn(lf), run_time=1.0)
        idf = pos(M(r"\omega_0 = \sqrt{\frac{k}{m}}, \qquad \xi = \frac{f}{2\sqrt{km}}", sc=0.95, color=VERT), -6.3, -2.0)
        self.ecr(self.a("b4", "On divise"), idf, rt=1.2)
        lo = T(r"amortisseur fort $\Rightarrow$ $\xi$ grand", sc=0.68, color=ORANGE).move_to([3.5, -3.45, 0])
        self.ecr(self.t("b5"), lo, rt=0.8)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"4.2 -- Les pôles selon $\xi$", "Deuxième ordre")
        eq = M(r"p^2 + 2\xi\omega_0\,p + \omega_0^2 = 0", sc=0.95, color=JAUNE).move_to([-2.9, 2.05, 0])
        self.ecr(self.a("c1", "Les pôles sont"), eq, rt=1.0)
        ax = axes(-3.0, -0.75, 6.2, 4.4, [-2.9, 0.8, 1], [-1.4, 1.4, 1], col=GRIS)
        lr = M(r"\mathrm{Re}", sc=0.55, color=GRIS).next_to(ax.x_axis.get_end(), DOWN, buff=0.1); li = M(r"\mathrm{Im}", sc=0.55, color=GRIS).next_to(ax.y_axis.get_end(), LEFT, buff=0.1)
        self.at(self.a("c1", "Tout dépend"), Create(ax), FadeIn(lr), FadeIn(li), run_time=0.6)
        z = 1.5; r1, r2 = -(z - np.sqrt(z*z - 1)), -(z + np.sqrt(z*z - 1))
        a = VGroup(croix(ax.c2p(r1, 0), col=VERT), croix(ax.c2p(r2, 0), col=VERT))
        ta = pos(T(r"$\xi > 1$ : deux pôles réels \;$\to$\; \textbf{apériodique}", sc=0.6, color=VERT), 0.5, 0.9)
        self.at(self.t("c2"), FadeIn(a, scale=2), Ecrire(ta, rt=0.9), run_time=0.9)
        b = croix(ax.c2p(-1, 0), col=ORANGE, r=0.16)
        tb = pos(T(r"$\xi = 1$ : pôle double \;$\to$\; \textbf{critique}", sc=0.6, color=ORANGE), 0.5, 0.05)
        self.at(self.t("c3"), FadeIn(b, scale=2), Ecrire(tb, rt=0.8), run_time=0.8)
        th = np.arccos(0.5)
        c = VGroup(croix(ax.c2p(-0.5, np.sin(th))), croix(ax.c2p(-0.5, -np.sin(th))))
        tc = pos(T(r"$\xi < 1$ : complexes \;$\to$\; \textbf{pseudo-périodique}", sc=0.6, color=ROUGE), 0.5, -0.8)
        self.at(self.t("c4"), FadeIn(c, scale=2), Ecrire(tc, rt=0.9), run_time=0.9)
        o = ax.c2p(0, 0); rr = ax.c2p(1, 0)[0] - o[0]
        cer = DashedVMobject(Arc(radius=rr, start_angle=PI/2, angle=PI, arc_center=o, color=JAUNE, stroke_width=3), num_dashes=30)
        ray = Line(o, ax.c2p(-0.5, np.sin(th)), color=JAUNE, stroke_width=3)
        ang = Arc(radius=0.45, start_angle=PI - th, angle=th, arc_center=o, color=JAUNE, stroke_width=3)
        lth = M(r"\theta", sc=0.6, color=JAUNE).move_to(o + 0.7*np.array([np.cos(PI - th/2), np.sin(PI - th/2), 0]))
        tw = pos(M(r"|p| = \omega_0, \qquad \cos\theta = \xi", sc=0.9, color=JAUNE), 0.5, -2.0)
        self.at(self.a("c5", "sur un cercle"), Create(cer), Create(ray), run_time=0.8)
        self.at(self.a("c5", "le cosinus"), Create(ang), FadeIn(lth), Ecrire(tw, rt=0.9), run_time=0.9)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"4.3 -- Les réponses indicielles", "Deuxième ordre")
        ax = axes(-0.6, -0.55, 10.0, 4.8, [0, 12, 2], [0, 1.65, 0.5])
        lt = M(r"\omega_0 t", sc=0.7).next_to(ax.x_axis.get_end(), DOWN, buff=0.12); ls = M(r"s/KE_0", sc=0.7).next_to(ax.y_axis.get_end(), LEFT, buff=0.12)
        fin = DashedLine(ax.c2p(0, 1), ax.c2p(12, 1), color=GRIS, stroke_width=3); l1 = M("1", sc=0.65, color=GRIS).next_to(ax.c2p(0, 1), LEFT, buff=0.1)
        self.at(self.t("d1"), Create(ax), FadeIn(lt), FadeIn(ls), Create(fin), FadeIn(l1), run_time=0.7)
        t = np.linspace(0, 11.9, 220)
        cas = [(0.7, ROUGE, "d1", "pour plusieurs"), (0.2, ORANGE, "d3", "Ksi égale"), (1.0, VERT, "d5", "Ksi égale un"), (2.0, BLEU, "d5", "de plus en plus lent")]
        cbs = {}
        for z, col, ph, fr in cas:
            cbs[z] = courbe(ax, t, indic(z, t), col, 5)
        self.at(self.a("d1", "pour plusieurs"), Create(cbs[0.7]), run_time=1.2)
        tg = Line(ax.c2p(0, 0), ax.c2p(1.6, 0), color=JAUNE, stroke_width=5)
        lh = T(r"tangente horizontale", sc=0.62, color=JAUNE).move_to(ax.c2p(2.7, 0.07))
        self.at(self.a("d2", "tangente horizontale"), Create(tg), FadeIn(lh), run_time=0.6)
        self.at(self.a("d2", "tendent vers"), Indicate(fin, color=JAUNE), run_time=0.6)
        self.at(self.a("d3", "Ksi égale"), Create(cbs[0.2]), run_time=1.3)
        l02 = VGroup(Line(ORIGIN, 0.4*RIGHT, color=ORANGE, stroke_width=5), M(r"\xi = 0{,}2", sc=0.6, color=ORANGE)).arrange(RIGHT, buff=0.12).move_to(ax.c2p(7.6, 1.6))
        self.play(FadeIn(l02), run_time=0.3)
        l07 = VGroup(Line(ORIGIN, 0.4*RIGHT, color=ROUGE, stroke_width=5), M(r"\xi = 0{,}7", sc=0.6, color=ROUGE)).arrange(RIGHT, buff=0.12).move_to(ax.c2p(10.4, 1.6))
        self.at(self.t("d4"), Indicate(cbs[0.7], color=ROUGE, scale_factor=1.02), FadeIn(l07), run_time=0.8)
        self.at(self.t("d5"), Create(cbs[1.0]), run_time=1.0)
        self.play(Create(cbs[2.0]), run_time=1.0)
        l1v = VGroup(Line(ORIGIN, 0.4*RIGHT, color=VERT, stroke_width=5), M(r"\xi = 1", sc=0.6, color=VERT)).arrange(RIGHT, buff=0.12).move_to(ax.c2p(7.4, 1.43)); l2v = VGroup(Line(ORIGIN, 0.4*RIGHT, color=BLEU, stroke_width=5), M(r"\xi = 2", sc=0.6, color=BLEU)).arrange(RIGHT, buff=0.12).move_to(ax.c2p(10.2, 1.43))
        self.play(FadeIn(l1v), FadeIn(l2v), run_time=0.4)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"4.4 -- Le dépassement", "Deuxième ordre")
        ax = axes(3.6, 0.6, 5.2, 3.2, [0, 12, 2], [0, 1.5, 0.5])
        t = np.linspace(0, 11.9, 200); z = 0.3; y = indic(z, t)
        cb = courbe(ax, t, y, BLEU, 4); fin = DashedLine(ax.c2p(0, 1), ax.c2p(12, 1), color=GRIS, stroke_width=2)
        self.at(self.a("e1", "En régime pseudo-périodique"), Create(ax), Create(fin), Create(cb), run_time=1.2)
        w = pos(M(r"\omega_p = \omega_0\sqrt{1 - \xi^2}", sc=0.85), -6.3, 2.1)
        self.ecr(self.a("e1", "la pseudo-pulsation"), w, rt=0.9)
        wp = np.sqrt(1 - z*z); tm = np.pi/wp; ym = 1 + np.exp(-np.pi*z/wp)
        tk = DashedLine(ax.c2p(tm, 0), ax.c2p(tm, 1), color=ORANGE, stroke_width=2); lt = M("t_1", sc=0.6, color=ORANGE).next_to(ax.c2p(tm, 0), DOWN, buff=0.12)
        t1 = pos(M(r"t_1 = \frac{\pi}{\omega_p}", sc=0.85), -6.3, 1.15)
        self.at(self.t("e2"), Ecrire(t1, rt=0.7), Create(tk), FadeIn(lt), run_time=0.8)
        v = Line(ax.c2p(tm, 1), ax.c2p(tm, ym), color=JAUNE, stroke_width=4); lv = M("D_1", sc=0.65, color=JAUNE).next_to(v, RIGHT, buff=0.1)
        d = pos(M(r"D_1 = \exp\!\left(-\frac{\pi\,\xi}{\sqrt{1 - \xi^2}}\right)", sc=0.85, color=JAUNE), -6.3, -0.2)
        self.at(self.a("e3", "Et le dépassement"), Ecrire(d, rt=1.2), Create(v), FadeIn(lv), run_time=1.2)
        self.play(Create(enc(d, col=JAUNE)), run_time=0.4)
        on = T(r"ne dépend que de $\xi$ !", sc=0.7, color=JAUNE).next_to(d, DOWN, buff=0.35).align_to(d, LEFT)
        self.ecr(self.a("e3", "Il ne dépend"), on, rt=0.7)
        vals = T(r"$\xi = 0{,}3$ : $37\,\%$ \quad $\xi = 0{,}5$ : $16\,\%$ \quad $\xi = 0{,}69$ : $5\,\%$", sc=0.7, color=BLEU)
        pos(vals, -6.3, -2.0)
        self.ecr(self.t("e4"), vals, rt=1.4)
        dk = pos(M(r"D_k = D_1^{\,k}", sc=0.85, color=VERT), -6.3, -2.85)
        self.ecr(self.t("e5"), dk, rt=0.6)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"4.5 -- Le temps de réponse à 5\,\%", "Deuxième ordre")
        ax, fr = cadre(0.2, -0.45, 10.0, 4.6, -1, 1, 0, 2)
        lx = M(r"\xi", sc=0.75).next_to(fr, DOWN, buff=0.45).align_to(fr, RIGHT)
        ly = M(r"t_{5\%}\,\omega_0", sc=0.7).next_to(fr, UP, buff=0.12).align_to(fr, LEFT)
        grad = VGroup(*[M(l, sc=0.55, color=GRIS).next_to(ax.c2p(np.log10(v), 0), DOWN, buff=0.12) for v, l in [(0.1, "0{,}1"), (0.3, "0{,}3"), (0.7, "0{,}7"), (1, "1"), (3, "3"), (10, "10")]])
        grady = VGroup(*[M(l, sc=0.55, color=GRIS).next_to(ax.c2p(-1, np.log10(v)), LEFT, buff=0.12) for v, l in [(1, "1"), (3, "3"), (10, "10"), (30, "30"), (100, "100")]])
        self.at(self.t("f1"), Create(fr), FadeIn(lx), FadeIn(ly), FadeIn(grad), FadeIn(grady), run_time=0.8)
        zs = np.concatenate([np.logspace(-1, np.log10(0.69), 70), np.linspace(0.69, 0.71, 12), np.logspace(np.log10(0.71), 1, 70)])
        pts = [ax.c2p(np.log10(z), np.log10(max(t5(z), 1))) for z in zs]
        cb = VMobject(color=BLEU, stroke_width=5).set_points_as_corners(pts)
        self.play(Create(cb), run_time=2.0)
        mn = Dot(ax.c2p(np.log10(0.7), np.log10(2.9)), color=JAUNE, radius=0.1)
        lmn = T(r"minimum $\approx 3$ pour $\xi \approx 0{,}7$", sc=0.68, color=JAUNE).move_to(ax.c2p(-0.2, 0.13))
        self.at(self.a("f2", "Regardez le minimum"), FadeIn(mn, scale=2), Ecrire(lmn, rt=0.9), run_time=0.9)
        f3 = T(r"moins amorti : oscille longtemps", sc=0.64, color=ORANGE).move_to(ax.c2p(-0.5, 1.82))
        self.ecr(self.t("f3"), f3, rt=0.9)
        cr = Dot(ax.c2p(0, np.log10(4.75)), color=VERT, radius=0.09)
        f4 = T(r"plus amorti : montée paresseuse", sc=0.64, color=VERT).move_to(ax.c2p(0.45, 0.32))
        lcr = T(r"critique : $4{,}75$", sc=0.6, color=VERT).next_to(cr, RIGHT, buff=0.2)
        self.ecr(self.t("f4"), f4, rt=0.9)
        self.at(self.a("f4", "Au régime critique"), FadeIn(cr, scale=2), FadeIn(lcr), run_time=0.6)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"4.6 -- La réponse fréquentielle", "Deuxième ordre")
        ax, fr = cadre(0.2, 0.25, 10.0, 4.0, -1, 1, -42, 16)
        lx = VGroup(*[M(t, sc=0.6, color=GRIS).next_to(ax.c2p(k, -42), DOWN, buff=0.1) for k, t in [(-1, r"0{,}1\,\omega_0"), (0, r"\omega_0"), (1, r"10\,\omega_0")]])
        ly = T(r"gain (dB)", sc=0.58, color=GRIS).next_to(fr, LEFT, buff=0.12).align_to(fr, UP)
        z0 = DashedLine(ax.c2p(-1, 0), ax.c2p(1, 0), color=GRIS, stroke_width=1.5)
        self.at(self.t("g1"), Create(fr), FadeIn(lx), FadeIn(ly), Create(z0), run_time=0.6)
        a1 = Line(ax.c2p(-1, 0), ax.c2p(0, 0), color=ORANGE, stroke_width=4); a2 = Line(ax.c2p(0, 0), ax.c2p(1, -40), color=ORANGE, stroke_width=4)
        l2 = T(r"$-40$ dB/déc", sc=0.62, color=ORANGE).move_to(ax.c2p(0.42, -31))
        self.at(self.a("g1", "un plateau"), Create(a1), run_time=0.5)
        self.at(self.a("g1", "puis une chute"), Create(a2), FadeIn(l2), run_time=0.6)
        u = np.linspace(-1, 1, 240); w = 10**u
        cbs = {}
        for z, col in [(0.7, VERT), (0.3, BLEU), (0.1, ROUGE)]:
            g = 20*np.log10(1/np.abs(1 - w**2 + 2j*z*w))
            cbs[z] = VMobject(color=col, stroke_width=4).set_points_smoothly([ax.c2p(a, max(b, -42)) for a, b in zip(u, g)])
        v0 = DashedLine(ax.c2p(0, -42), ax.c2p(0, 16), color=GRIS, stroke_width=2)
        k2 = M(r"|H(j\omega_0)| = \frac{K}{2\xi}, \quad \varphi(\omega_0) = -90^\circ", sc=0.8, color=JAUNE).move_to([-2.4, -2.55, 0])
        self.at(self.t("g2"), Create(v0), Create(cbs[0.7]), run_time=0.8)
        self.ecr(self.a("g2", "le gain vaut"), k2, rt=1.1)
        self.at(self.a("g3", "une bosse"), Create(cbs[0.3]), Create(cbs[0.1]), run_time=1.2)
        lb = VGroup(M(r"\xi = 0{,}1", sc=0.58, color=ROUGE), M(r"\xi = 0{,}3", sc=0.58, color=BLEU), M(r"\xi = 0{,}7", sc=0.58, color=VERT)).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(ax.c2p(-0.8, -26))
        rs = T(r"résonance si $\xi < 1/\sqrt{2} \approx 0{,}71$", sc=0.62, color=ROUGE).move_to(ax.c2p(-0.52, 11))
        self.play(FadeIn(lb), run_time=0.3)
        self.ecr(self.a("g3", "Elle existe"), rs, rt=1.0)
        mal = T(r"forte résonance $=$ fort dépassement : amortissement trop faible", sc=0.64, color=JAUNE).move_to([0.2, -3.35, 0])
        self.ecr(self.t("g4"), mal, rt=1.2)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"4.7 -- Identifier un deuxième ordre", "Deuxième ordre")
        ax = axes(3.5, 0.0, 5.6, 3.8, [0, 12, 2], [0, 1.5, 0.5])
        t = np.linspace(0, 11.9, 200); z = 0.35; y = indic(z, t); cb = courbe(ax, t, y, BLEU, 4)
        fin = DashedLine(ax.c2p(0, 1), ax.c2p(12, 1), color=GRIS, stroke_width=2)
        self.at(self.t("h1"), Create(ax), Create(fin), Create(cb), run_time=1.2)
        wp = np.sqrt(1 - z*z); t1 = np.pi/wp; t2 = 3*np.pi/wp; ym = 1 + np.exp(-np.pi*z/wp)
        k = pos(M(r"K = \frac{\Delta s_\infty}{\Delta e}", sc=0.9, color=ORANGE), -6.3, 1.9)
        self.ecr(self.t("h2"), k, rt=0.8)
        v = Line(ax.c2p(t1, 1), ax.c2p(t1, ym), color=JAUNE, stroke_width=4); lv = M("D_1", sc=0.6, color=JAUNE).next_to(v, RIGHT, buff=0.08)
        x = pos(M(r"\xi = \frac{-\ln D_1}{\sqrt{\pi^2 + \ln^2 D_1}}", sc=0.9, color=JAUNE), -6.3, 0.35)
        self.at(self.t("h3"), Create(v), FadeIn(lv), run_time=0.5); self.ecr(self.a("h3", "Le dépassement D un"), x, rt=1.1)
        y2 = 1 + np.exp(-3*np.pi*z/wp)
        tp = DoubleArrow(ax.c2p(t1, 1.42), ax.c2p(t2, 1.42), color=VERT, buff=0, stroke_width=3, tip_length=0.14); lp = M("T_p", sc=0.6, color=VERT).next_to(tp, UP, buff=0.05)
        w0 = pos(M(r"\omega_0 = \frac{2\pi}{T_p\sqrt{1 - \xi^2}}", sc=0.9, color=VERT), -6.3, -1.4)
        self.at(self.t("h4"), GrowFromCenter(tp), FadeIn(lp), run_time=0.6); self.ecr(self.a("h4", "la pseudo-période donne"), w0, rt=1.1)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"4.8 -- À vous de jouer", "Exercice")
        h = M(r"H(p) = \frac{100}{p^2 + 6p + 100}", sc=1.05, color=JAUNE).move_to([-0.8, 1.9, 0])
        q = T(r"$K$ ? \; $\omega_0$ ? \; $\xi$ ? \; dépassement ?", sc=0.75, color=BLEU).next_to(h, DOWN, buff=0.3)
        self.ecr(self.a("i1", "H de p"), h, rt=1.1); self.ecr(self.a("i1", "Que valent"), q, rt=0.8)
        pa, arc = chrono(4.3, 1.9)
        self.at(self.a("i1", "Mettez sur pause"), FadeIn(pa), Create(arc), run_time=0.5)
        self.play(Uncreate(arc), run_time=2.6); self.play(FadeOut(pa), run_time=0.2)
        a = pos(M(r"\omega_0^2 = 100 \;\Rightarrow\; \omega_0 = 10\ \mathrm{rad/s}, \qquad K = \frac{100}{100} = 1", sc=0.85), -6.3, -0.15)
        self.ecr(self.t("i2"), a, rt=1.3)
        b = pos(M(r"2\xi\omega_0 = 6 \;\Rightarrow\; \xi = 0{,}3", sc=0.85), -6.3, -1.2)
        self.ecr(self.t("i3"), b, rt=1.0)
        c = M(r"D_1 \approx 37\,\%, \qquad t_1 = \frac{\pi}{\omega_p} \approx 0{,}33\ \mathrm{s}", sc=0.95, color=JAUNE).move_to([-0.8, -2.5, 0])
        self.ecr(self.t("i4"), c, rt=1.2); self.play(Create(enc(c, col=JAUNE)), run_time=0.4)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"4.9 -- Le compromis du gain", "Deuxième ordre")
        y = 1.6
        s = som(-4.6, y); g = blk(r"\frac{K}{p\,(1 + \tau p)}", -2.4, y, w=2.4, h=0.9)
        fs = [fl((-6.2, y), (-4.84, y)), fl((-4.36, y), (-3.6, y)), fl((-1.2, y), (0.6, y))]
        r = fl((-0.1, y), (-0.1, y - 1.05), (-4.6, y - 1.05), (-4.6, y - 0.24), col=BLEU)
        self.at(self.t("j1"), *[Create(f) for f in fs], Create(s), Create(g[0]), FadeIn(g[1]), Create(r), run_time=1.0)
        f = pos(M(r"\omega_0 = \sqrt{\frac{K}{\tau}}, \qquad \xi = \frac{1}{2\sqrt{K\tau}}", sc=0.85, color=JAUNE), 1.2, 1.6)
        self.ecr(self.t("j2"), f, rt=1.2); self.play(Create(enc(f, col=JAUNE)), run_time=0.4)
        u = T(r"$K \nearrow$ \;$\Rightarrow$\; $\omega_0 \nearrow$ : plus vif", sc=0.8, color=VERT).move_to([-3.0, -0.75, 0])
        d = T(r"mais $\xi \searrow$ : plus oscillant !", sc=0.8, color=ROUGE).move_to([2.6, -0.75, 0])
        self.ecr(self.a("j3", "Augmenter K"), u, rt=0.9); self.ecr(self.a("j3", "Mais ksi"), d, rt=0.8)
        c = T(r"compromis \textbf{rapidité} \;/\; \textbf{amortissement}", sc=0.85, color=JAUNE).move_to([0, -2.1, 0])
        self.ecr(self.t("j4"), c, rt=1.0); self.play(Create(enc(c, col=JAUNE)), run_time=0.4)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"À retenir", "Bilan")
        pts = [("k1", r"Trois paramètres $K$, $\omega_0$, $\xi$ : c'est $\xi$ qui fixe l'allure", BLEU),
               ("k2", r"$\xi < 1$ : oscillations, $D_1 = e^{-\pi\xi/\sqrt{1 - \xi^2}}$ (ne dépend que de $\xi$)", VERT),
               ("k3", r"Le plus rapide : $\xi \approx 0{,}7$, \; $t_{r5\%} \approx 3/\omega_0$", ORANGE),
               ("k4", r"Fréquence : $-40$ dB/décade, résonance si $\xi < 0{,}71$", JAUNE)]
        for k, (ph, txt, c) in enumerate(pts):
            yy = 1.8 - 1.3*k
            ca = carte(k+1, c, -5.9, yy); tx = pos(T(txt, sc=0.74), -5.35, yy)
            self.at(self.t(ph), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice résolu -- l'énoncé", "Application")
        y = 1.55
        s = som(-4.6, y); g = blk(r"\frac{K}{p\,(1 + 0{,}1\,p)}", -2.3, y, w=2.6, h=0.9)
        fs = [fl((-6.2, y), (-4.84, y)), fl((-4.36, y), (-3.6, y)), fl((-1.0, y), (0.8, y))]
        r = fl((0.1, y), (0.1, y - 1.05), (-4.6, y - 1.05), (-4.6, y - 0.24), col=BLEU)
        self.at(self.a("l1", "Une boucle de position"), *[Create(f) for f in fs], Create(s), Create(g[0]), FadeIn(g[1]), Create(r), run_time=1.0)
        ob = T(r"objectif : le plus rapide sans dépassement notable \;$\Rightarrow$\; $\xi = 0{,}7$", sc=0.72, color=BLEU).move_to([0, -0.15, 0])
        self.ecr(self.t("l2"), ob, rt=1.3)
        qs = [(r"quel gain $K$ ?", "quel gain"), (r"quel temps de réponse ?", "Quel temps"), (r"et si l'on double $K$ ?", "Et que se passe")]
        for k, (q, fr) in enumerate(qs):
            m = pos(T(q, sc=0.75, color=ROUGE), -5.4, -1.05 - 0.6*k)
            self.at(self.a("l3", fr), Create(carte(k+1, ROUGE, -6.0, -1.05 - 0.6*k)), Ecrire(m, rt=0.7), run_time=0.7)
        rf = pos(T(r"Réfléchissons : FTBF $\to$ deuxième ordre $\to$ abaque", sc=0.72, color=BLEU), -6.3, -3.1)
        self.ecr(self.t("l4"), rf, rt=1.1)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- la solution", "Application")
        def etape(k, c, y, m, ph, fr, rt=1.0):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(self.a(ph, fr), Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        etape(1, BLEU, 2.2, M(r"H_{BF} = \frac{1}{1 + \frac{p}{K} + \frac{0{,}1\,p^2}{K}}", sc=0.78), "m1", "Première étape", 1.2)
        etape(2, VERT, 1.05, M(r"\omega_0 = \sqrt{10K}, \qquad \xi = \frac{1}{2\sqrt{0{,}1K}}", sc=0.78), "m2", "Deuxième étape", 1.2)
        k = pos(M(r"\xi = 0{,}7 \;\Rightarrow\; K \approx 5{,}1\ \mathrm{s^{-1}}", sc=0.8, color=JAUNE), -5.85, 0.05)
        self.ecr(self.a("m3", "On impose"), k, rt=1.0); self.play(Create(enc(k, col=JAUNE, buff=0.12)), run_time=0.4)
        etape(3, ORANGE, -1.0, M(r"\omega_0 \approx 7{,}1\ \mathrm{rad/s}, \quad t_{r5\%} \approx \frac{3}{\omega_0} \approx 0{,}42\ \mathrm{s}", sc=0.78), "m4", "Troisième étape", 1.2)
        ax = axes(4.0, 0.9, 4.6, 3.0, [0, 1.2, 0.5], [0, 1.4, 0.5])
        lt = M("t", sc=0.6).next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        fin = DashedLine(ax.c2p(0, 1), ax.c2p(1.2, 1), color=GRIS, stroke_width=2)
        t = np.linspace(0, 1.19, 200)
        def rep(K):
            _, y = signal.step(signal.lti([K], [0.1, 1, K]), T=t); return y
        c1 = courbe(ax, t, rep(5.1), VERT, 4); c2 = courbe(ax, t, rep(10.2), ROUGE, 4)
        l1 = M(r"K = 5{,}1", sc=0.55, color=VERT).move_to(ax.c2p(0.95, 0.82)); l2 = M(r"K = 10{,}2", sc=0.55, color=ROUGE).move_to(ax.c2p(0.42, 1.3))
        self.at(self.a("m4", "Et l'abaque"), Create(ax), FadeIn(lt), Create(fin), Create(c1), FadeIn(l1), run_time=1.0)
        d1 = pos(T(r"dépassement : $4{,}6\,\%$ \;$\checkmark$", sc=0.7, color=VERT), -5.85, -1.85)
        self.ecr(self.t("m5"), d1, rt=0.8)
        db = pos(M(r"2K : \;\xi \approx 0{,}5, \quad D_1 \approx 17\,\%", sc=0.78, color=ROUGE), -5.85, -2.65)
        self.at(self.a("m6", "Et si l'on double"), Create(c2), FadeIn(l2), run_time=0.9)
        self.ecr(self.a("m6", "Ksi est divisé"), db, rt=1.0)
        tr = pos(M(r"\omega_0 = 10, \;\; t_{r5\%} \approx \frac{5{,}3}{10} = 0{,}52\ \mathrm{s}", sc=0.78, color=ROUGE), -5.85, -3.4)
        self.ecr(self.t("m7"), tr, rt=1.1)
        su = T(r"plus de gain \ldots{} et plus lent !", sc=0.72, color=JAUNE).move_to([4.0, -1.1, 0])
        self.ecr(self.t("m8"), su, rt=0.8); self.play(Create(enc(su, col=JAUNE, buff=0.15)), run_time=0.4)
        nx = T(r"Prochain chapitre : les diagrammes de Bode", sc=0.62, color=GRIS).move_to([4.0, -2.1, 0])
        self.at(self.t("m9"), FadeIn(nx), run_time=0.6)
        self.fin()
