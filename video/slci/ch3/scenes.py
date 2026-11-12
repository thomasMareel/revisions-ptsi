from base import *
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
def tick(ax, x, lab, col=GRIS, sc=0.6):
    l = Line(ax.c2p(x, 0) + 0.07*DOWN, ax.c2p(x, 0) + 0.07*UP, color=col, stroke_width=2)
    return VGroup(l, M(lab, sc=sc, color=col).next_to(ax.c2p(x, 0), DOWN, buff=0.15))

def cadre(x, y, w, h, l0, l1, g0, g1):
    ax = Axes(x_range=[l0, l1, 1], y_range=[g0, g1, 1], x_length=w, y_length=h, tips=False,
              axis_config={"stroke_opacity": 0, "include_ticks": False}).move_to([x, y, 0])
    fr = Rectangle(width=w, height=h, color=GRIS, stroke_width=2).move_to([x, y, 0])
    dec = VGroup(*[DashedLine(ax.c2p(k, g0), ax.c2p(k, g1), color=GRIS, stroke_width=1, dash_length=0.06) for k in range(int(np.ceil(l0)), int(np.floor(l1)) + 1)])
    return ax, VGroup(fr, dec)

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PTSI", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Automatique -- Chapitre 3}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Systèmes du premier ordre", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        ax = axes(3.6, -0.9, 4.2, 2.6, [0, 5, 1], [0, 1.15, 1])
        cb = ax.plot(lambda t: 1 - np.exp(-t), x_range=[0, 4.9, 0.02], color=BLEU, stroke_width=5)
        lb = M(r"H(p) = \frac{K}{1 + \tau p}", sc=0.85, color=JAUNE).move_to([3.6, 0.75, 0])
        self.at(self.a("a1", "Un four qui chauffe"), Create(ax), run_time=0.5)
        self.at(self.a("a2", "Une montée douce"), Create(cb), run_time=1.2)
        self.ecr(self.a("a2", "C'est le système"), lb, rt=0.9)
        items = []
        for k, (txt, c) in enumerate([("Le modèle", BLEU), ("Réponse à un échelon", VERT), ("Réponse à une rampe", ORANGE),
                                       ("Réponse fréquentielle", ROUGE), ("Identifier un premier ordre", BLEU), ("Exercice résolu : un moteur", JAUNE)]):
            yy = 0.75 - 0.6*k
            items.append(VGroup(carte(k+1, c, -6.2, yy), pos(T(txt, sc=0.74), -5.65, yy)))
        for it, (sid, fr) in zip(items, [("a3", "le modèle"), ("a3", "la réponse à un échelon"), ("a3", "à une rampe"),
                                         ("a3", "la réponse fréquentielle"), ("a3", "et l'identification"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"3.1 -- Le modèle du premier ordre", "Premier ordre")
        e = pos(M(r"\tau\, s' + s = K\, e", sc=1.0), -6.3, 2.05)
        self.ecr(self.t("b1"), e, rt=0.8)
        h = M(r"H(p) = \frac{K}{1 + \tau p}", sc=1.15, color=JAUNE).move_to([2.2, 2.0, 0])
        self.ecr(self.t("b2"), h, rt=0.9); self.play(Create(enc(h, col=JAUNE)), run_time=0.4)
        k = pos(T(r"$K$ : gain statique (sortie / entrée en régime permanent, avec unités)", sc=0.7, color=BLEU), -6.3, 0.75)
        tt = pos(T(r"$\tau$ : constante de temps, en secondes $\Rightarrow$ rapidité", sc=0.7, color=BLEU), -6.3, 0.1)
        po = pos(T(r"un pôle : $-1/\tau < 0$ \;$\Rightarrow$\; stable", sc=0.7, color=VERT), -6.3, -0.55)
        self.ecr(self.t("b3"), k, rt=1.2); self.ecr(self.t("b4"), tt, rt=1.1); self.ecr(self.t("b5"), po, rt=0.9)
        ex = [(r"circuit RC : \; $\tau = RC$, \; $K = 1$", "le circuit"), (r"enceinte chauffée : \; $\tau = R_{th}C$, \; $K = R_{th}$", "une enceinte"),
              (r"moteur ($L$ négligée) : \; tension $\to$ vitesse", "un moteur électrique")]
        for i, (s, fr) in enumerate(ex):
            m = pos(T(s, sc=0.68, color=ORANGE), -5.6, -1.5 - 0.62*i)
            self.ecr(self.a("b6", fr), m, rt=0.8)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"3.2 -- La réponse indicielle", "Premier ordre")
        e = pos(M(r"E(p) = \frac{E_0}{p}", sc=0.9), -6.3, 2.0)
        self.ecr(self.t("c1"), e, rt=0.6)
        s = pos(M(r"S(p) = \frac{K E_0}{p\,(1 + \tau p)} = K E_0\left(\frac{1}{p} - \frac{1}{p + 1/\tau}\right)", sc=0.9), -6.3, 0.8)
        self.ecr(self.t("c2"), s, rt=1.6)
        r = M(r"s(t) = K E_0\left(1 - e^{-t/\tau}\right)", sc=1.15, color=JAUNE).move_to([0, -0.6, 0])
        self.ecr(self.t("c3"), r, rt=1.1); self.play(Create(enc(r, col=JAUNE)), run_time=0.4)
        ax = axes(0, -2.5, 6.0, 1.6, [0, 5, 1], [0, 1.15, 1])
        cb = ax.plot(lambda t: 1 - np.exp(-t), x_range=[0, 4.9, 0.02], color=BLEU, stroke_width=5)
        fin = DashedLine(ax.c2p(0, 1), ax.c2p(5, 1), color=VERT, stroke_width=3); lf = M(r"KE_0", sc=0.6, color=VERT).next_to(ax.c2p(0, 1), LEFT, buff=0.1)
        self.at(self.t("c4"), Create(ax), Create(fin), FadeIn(lf), run_time=0.6); self.play(Create(cb), run_time=1.0)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"3.3 -- Les points remarquables", "Premier ordre")
        ax = axes(-1.6, -0.55, 8.0, 4.4, [0, 5.2, 1], [0, 1.15, 1])
        lt = M("t", sc=0.7).next_to(ax.x_axis.get_end(), DOWN, buff=0.12); ls = M("s(t)", sc=0.7).next_to(ax.y_axis.get_end(), LEFT, buff=0.12)
        cb = ax.plot(lambda t: 1 - np.exp(-t), x_range=[0, 5.1, 0.02], color=BLEU, stroke_width=5)
        fin = DashedLine(ax.c2p(0, 1), ax.c2p(5.2, 1), color=GRIS, stroke_width=3); lf = M(r"KE_0", sc=0.65, color=GRIS).next_to(ax.c2p(0, 1), LEFT, buff=0.1)
        self.at(self.t("d1"), Create(ax), FadeIn(lt), FadeIn(ls), Create(fin), FadeIn(lf), run_time=0.6); self.play(Create(cb), run_time=1.0)
        tg = Line(ax.c2p(0, 0), ax.c2p(1.08, 1.08), color=ORANGE, stroke_width=4)
        v1 = DashedLine(ax.c2p(1, 0), ax.c2p(1, 1), color=ORANGE, stroke_width=2)
        t1 = tick(ax, 1, r"\tau", col=ORANGE, sc=0.75)
        self.at(self.a("d2", "la tangente"), Create(tg), run_time=0.8)
        self.at(self.a("d2", "exactement"), Create(v1), FadeIn(t1), run_time=0.6)
        p63 = Dot(ax.c2p(1, 1 - np.exp(-1)), color=JAUNE, radius=0.09)
        l63 = T(r"63\,\%", sc=0.75, color=JAUNE).next_to(p63, RIGHT, buff=0.2)
        self.at(self.a("d3", "la sortie vaut"), FadeIn(p63, scale=2), FadeIn(l63), run_time=0.6)
        c63 = M(r"1 - e^{-1} \approx 0{,}63", sc=0.75, color=JAUNE).move_to(ax.c2p(2.6, 0.38))
        self.ecr(self.a("d3", "Car un moins"), c63, rt=0.9)
        p95 = Dot(ax.c2p(3, 1 - np.exp(-3)), color=VERT, radius=0.09); v3 = DashedLine(ax.c2p(3, 0), ax.c2p(3, 0.95), color=VERT, stroke_width=2)
        t3 = tick(ax, 3, r"3\tau", col=VERT, sc=0.75); l95 = T(r"95\,\%", sc=0.75, color=VERT).next_to(p95, DOWN, buff=0.3)
        self.at(self.a("d4", "à trois tau"), Create(v3), FadeIn(t3), FadeIn(p95, scale=2), FadeIn(l95), run_time=0.7)
        tr = M(r"t_{r5\%} = 3\tau", sc=1.0, color=VERT).move_to([4.9, 1.6, 0])
        self.ecr(self.a("d4", "Le temps de réponse"), tr, rt=0.8); self.play(Create(enc(tr, col=VERT)), run_time=0.4)
        nd = T(r"jamais de dépassement", sc=0.75, color=JAUNE).move_to([4.9, 0.5, 0])
        self.ecr(self.t("d5"), nd, rt=0.8)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"3.4 -- Le piège de la linéarité", "Premier ordre")
        q = T(r"$+10\,^\circ$C ou $+100\,^\circ$C : même durée ?", sc=0.85, color=ROUGE).move_to([0, 2.05, 0])
        self.ecr(self.t("e1"), q, rt=1.0)
        for k, (amp, col) in enumerate([(10, BLEU), (100, ORANGE)]):
            cx = -3.4 + 6.8*k
            ax = axes(cx, -0.25, 5.0, 2.8, [0, 5, 1], [0, 1.15, 1])
            cb = ax.plot(lambda t: 1 - np.exp(-t), x_range=[0, 4.9, 0.02], color=col, stroke_width=5)
            lf = M(r"%d\,^\circ\mathrm{C}" % amp, sc=0.65, color=col).next_to(ax.c2p(0, 1), LEFT, buff=0.1)
            fin = DashedLine(ax.c2p(0, 1), ax.c2p(5, 1), color=GRIS, stroke_width=2)
            v = DashedLine(ax.c2p(1, 0), ax.c2p(1, 1 - np.exp(-1)), color=JAUNE, stroke_width=2); tt = tick(ax, 1, r"\tau", col=JAUNE, sc=0.7)
            if k == 0: self.jusqua(self.a("e2", "Non"))
            self.play(Create(ax), Create(fin), FadeIn(lf), run_time=0.5)
            self.play(Create(cb), Create(v), FadeIn(tt), run_time=0.9)
        r = T(r"même $\tau$, même forme : c'est la \textbf{linéarité}", sc=0.78, color=JAUNE).move_to([0, -2.4, 0])
        self.ecr(self.a("e2", "Les deux courbes"), r, rt=1.0)
        sa = T(r"en pratique : la puissance \textbf{sature} pour les grands échelons", sc=0.72, color=ROUGE).move_to([0, -3.2, 0])
        self.ecr(self.a("e3", "En pratique"), sa, rt=1.1)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"3.5 -- La réponse à une rampe", "Premier ordre")
        e = pos(M(r"e(t) = a\,t", sc=0.9), -6.3, 2.05)
        self.ecr(self.t("f1"), e, rt=0.6)
        s = pos(M(r"s(t) = K a\left(t - \tau + \tau\, e^{-t/\tau}\right)", sc=0.9, color=JAUNE), -2.8, 2.05)
        self.ecr(self.t("f2"), s, rt=1.3)
        ax = axes(-1.2, -0.85, 8.6, 4.0, [0, 5.4, 1], [0, 5.4, 1])
        lt = M("t", sc=0.7).next_to(ax.x_axis.get_end(), DOWN, buff=0.12)
        ce = ax.plot(lambda t: t, x_range=[0, 5.2, 0.05], color=GRIS, stroke_width=3)
        cs = ax.plot(lambda t: t - 1 + np.exp(-t), x_range=[0, 5.3, 0.02], color=BLEU, stroke_width=5)
        le = M(r"e = at", sc=0.65, color=GRIS).move_to(ax.c2p(4.4, 5.2)); ls = M(r"s", sc=0.7, color=BLEU).move_to(ax.c2p(5.3, 3.9))
        self.at(self.a("f3", "Avec K égale un"), Create(ax), FadeIn(lt), Create(ce), FadeIn(le), run_time=0.6); self.play(Create(cs), FadeIn(ls), run_time=1.0)
        x = 4.2
        h = Line(ax.c2p(x - 1, x - 1), ax.c2p(x, x - 1), color=ORANGE, stroke_width=3)
        lh = M(r"\tau", sc=0.7, color=ORANGE).next_to(h, DOWN, buff=0.08)
        v = DoubleArrow(ax.c2p(x, x - 1), ax.c2p(x, x), color=ROUGE, buff=0, stroke_width=3, tip_length=0.14)
        lv = M(r"a\tau", sc=0.75, color=ROUGE).next_to(v, RIGHT, buff=0.12)
        self.at(self.a("f3", "avec un retard"), Create(h), FadeIn(lh), run_time=0.6)
        self.at(self.a("f3", "L'écart se stabilise"), GrowFromCenter(v), FadeIn(lv), run_time=0.6)
        tr = T(r"écart de traînage $a\tau$", sc=0.75, color=ROUGE).move_to([5.1, -1.2, 0])
        self.ecr(self.a("f3", "c'est l'écart de traînage"), tr, rt=0.8)
        k1 = T(r"$K \neq 1$ : l'écart diverge", sc=0.72, color=ORANGE).move_to([-3.3, 0.9, 0])
        self.ecr(self.t("f4"), k1, rt=0.8)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"3.6 -- La réponse fréquentielle", "Premier ordre")
        m = pos(M(r"|H(j\omega)| = \frac{K}{\sqrt{1 + \tau^2\omega^2}}, \qquad \varphi = -\arctan(\tau\omega)", sc=0.85, color=JAUNE), -6.3, 2.05)
        self.ecr(self.a("g2", "Son amplitude"), m, rt=1.5)
        ag, fg = cadre(-1.2, 0.0, 8.4, 2.0, -2, 2, -44, 8)
        ap, fp = cadre(-1.2, -2.3, 8.4, 1.5, -2, 2, -100, 10)
        lg = M(r"G\ (\mathrm{dB})", sc=0.6, color=GRIS).next_to(fg, LEFT, buff=0.15).align_to(fg, UP)
        lp = M(r"\varphi", sc=0.7, color=GRIS).next_to(fp, LEFT, buff=0.15).align_to(fp, UP)
        lw = VGroup(*[M(t, sc=0.55, color=GRIS).next_to(ap.c2p(k, -100), DOWN, buff=0.1) for k, t in [(-1, r"0{,}1/\tau"), (0, r"1/\tau"), (1, r"10/\tau")]])
        self.at(self.t("g3"), Create(fg), Create(fp), FadeIn(lg), FadeIn(lp), FadeIn(lw), run_time=0.7)
        G = lambda u: -10*np.log10(1 + 10**(2*u)); P = lambda u: -np.degrees(np.arctan(10**u))
        a1 = Line(ag.c2p(-2, 0), ag.c2p(0, 0), color=ORANGE, stroke_width=3); a2 = Line(ag.c2p(0, 0), ag.c2p(2, -40), color=ORANGE, stroke_width=3)
        l1 = M(r"20\log K", sc=0.6, color=ORANGE).next_to(ag.c2p(-1.4, 0), DOWN, buff=0.12)
        l2 = T(r"$-20$ dB/déc", sc=0.6, color=ORANGE).move_to(ag.c2p(1.35, -12))
        self.at(self.a("g4", "Aux basses pulsations"), Create(a1), FadeIn(l1), run_time=0.6)
        self.at(self.a("g4", "Aux hautes pulsations"), Create(a2), FadeIn(l2), run_time=0.6)
        cg = ag.plot(G, x_range=[-2, 2, 0.02], color=BLEU, stroke_width=5); cp = ap.plot(P, x_range=[-2, 2, 0.02], color=BLEU, stroke_width=5)
        vc = DashedLine(ag.c2p(0, 8), ap.c2p(0, -100), color=JAUNE, stroke_width=2)
        d3 = Dot(ag.c2p(0, -3), color=JAUNE, radius=0.08); l3 = T(r"$-3$ dB", sc=0.6, color=JAUNE).next_to(d3, DL, buff=0.1)
        d45 = Dot(ap.c2p(0, -45), color=JAUNE, radius=0.08); l45 = M(r"-45^\circ", sc=0.6, color=JAUNE).next_to(d45, RIGHT, buff=0.15)
        self.at(self.a("g5", "Les deux asymptotes"), Create(vc), Create(cg), run_time=1.0)
        self.at(self.a("g5", "la courbe réelle"), FadeIn(d3, scale=2), FadeIn(l3), Create(cp), run_time=0.9)
        self.at(self.a("g5", "la phase vaut"), FadeIn(d45, scale=2), FadeIn(l45), run_time=0.5)
        pb = M(r"t_{r5\%}\cdot\omega_c = 3", sc=0.85, color=VERT).move_to([5.2, -0.5, 0])
        self.ecr(self.a("g6", "temps de réponse fois"), pb, rt=0.8); self.play(Create(enc(pb, col=VERT, buff=0.15)), run_time=0.4)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"3.7 -- Identifier un premier ordre", "Premier ordre")
        ax = axes(2.8, -0.5, 6.4, 4.0, [0, 5, 1], [0, 1.2, 1])
        cb = ax.plot(lambda t: 0.2 + 0.8*(1 - np.exp(-(t - 0.5)/0.9)) if t > 0.5 else 0.2, x_range=[0, 4.9, 0.02], color=BLEU, stroke_width=5)
        h0 = DashedLine(ax.c2p(0, 0.2), ax.c2p(5, 0.2), color=GRIS, stroke_width=2); h1 = DashedLine(ax.c2p(0, 1.0), ax.c2p(5, 1.0), color=GRIS, stroke_width=2)
        self.at(self.t("h1"), Create(ax), Create(h0), Create(h1), run_time=0.6); self.play(Create(cb), run_time=0.9)
        ds = DoubleArrow(ax.c2p(4.4, 0.2), ax.c2p(4.4, 1.0), color=ORANGE, buff=0, stroke_width=3, tip_length=0.14)
        lds = M(r"\Delta s_\infty", sc=0.65, color=ORANGE).next_to(ds, RIGHT, buff=0.1)
        k = pos(M(r"K = \frac{\Delta s_\infty}{\Delta e}", sc=0.95, color=ORANGE), -6.3, 1.6)
        self.at(self.t("h2"), GrowFromCenter(ds), FadeIn(lds), run_time=0.6); self.ecr(self.a("h2", "divisée par"), k, rt=0.9)
        y63 = 0.2 + 0.8*0.632; x63 = 0.5 + 0.9
        p = Dot(ax.c2p(x63, y63), color=JAUNE, radius=0.09); v = DashedLine(ax.c2p(x63, 0), ax.c2p(x63, y63), color=JAUNE, stroke_width=2)
        lt = M(r"\tau", sc=0.7, color=JAUNE).next_to(ax.c2p(x63 - 0.45, 0), DOWN, buff=0.15)
        br = Line(ax.c2p(0.5, -0.05), ax.c2p(x63, -0.05), color=JAUNE, stroke_width=3)
        t = pos(T(r"$\tau$ : instant à $63\,\%$ de la variation", sc=0.72, color=JAUNE), -6.3, 0.35)
        self.at(self.t("h3"), FadeIn(p, scale=2), Create(v), Create(br), FadeIn(lt), run_time=0.7); self.ecr(self.a("h3", "l'instant"), t, rt=1.0)
        bo = pos(T(r"Bode : $K$ sur le plateau, \\ $\tau = 1/\omega_c$ à $-3$ dB", sc=0.72, color=BLEU), -6.3, -1.4)
        self.ecr(self.t("h4"), bo, rt=1.2)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"3.8 -- À vous : un four", "Exercice")
        d = pos(T(r"échelon de $2$ kW \;$\Rightarrow$\; $+80\,^\circ$C, \; $95\,\%$ atteints en $30$ min", sc=0.78), -6.3, 2.05)
        self.ecr(self.t("i1"), d, rt=1.4)
        q = pos(T(r"$K$ ? \quad $\tau$ ? \quad hausse au bout de $10$ min ?", sc=0.8, color=BLEU), -6.3, 1.2)
        self.ecr(self.t("i2"), q, rt=1.0)
        pa, arc = chrono(4.8, 1.2)
        self.at(self.a("i2", "Mettez sur pause"), FadeIn(pa), Create(arc), run_time=0.5)
        self.play(Uncreate(arc), run_time=2.6); self.play(FadeOut(pa), run_time=0.2)
        k = pos(M(r"K = \frac{80}{2000} = 0{,}04\ \mathrm{K/W}", sc=0.9), -6.3, -0.05)
        self.ecr(self.t("i3"), k, rt=1.0)
        t = pos(M(r"3\tau = 30\ \mathrm{min} \;\Rightarrow\; \tau = 10\ \mathrm{min}", sc=0.9), -6.3, -1.2)
        self.ecr(self.t("i4"), t, rt=1.1)
        r = pos(M(r"t = \tau \;\Rightarrow\; 0{,}63 \times 80 \approx 50\,^\circ\mathrm{C}", sc=0.9, color=JAUNE), -6.3, -2.4)
        self.ecr(self.t("i5"), r, rt=1.1); self.play(Create(enc(r, col=JAUNE)), run_time=0.4)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"3.9 -- Le premier ordre dans une boucle", "Premier ordre")
        y = 1.75
        s = som(-4.4, y); c = blk("K_c", -3.0, y, w=0.9); g = blk(r"\frac{K}{1 + \tau p}", -1.1, y, w=1.9, h=0.85)
        fs = [fl((-5.8, y), (-4.64, y)), fl((-4.16, y), (-3.45, y)), fl((-2.55, y), (-2.05, y)), fl((-0.15, y), (1.4, y))]
        r = fl((0.7, y), (0.7, y - 0.95), (-4.4, y - 0.95), (-4.4, y - 0.24), col=BLEU)
        self.at(self.t("j1"), *[Create(f) for f in fs], Create(s), Create(c[0]), FadeIn(c[1]), Create(g[0]), FadeIn(g[1]), Create(r), run_time=1.0)
        f1 = pos(M(r"\tau' = \frac{\tau}{1 + K_cK}, \qquad K' = \frac{K_cK}{1 + K_cK} < 1", sc=0.85, color=JAUNE), -6.3, 0.15)
        self.ecr(self.t("j2"), f1, rt=1.3)
        rp = pos(T(r"plus rapide, \\ mais un écart statique", sc=0.66, color=ORANGE), 2.6, 0.15)
        self.ecr(self.a("j2", "Mais il garde"), rp, rt=0.8)
        y = -1.45
        s2 = som(-4.4, y); i = blk(r"\frac{K}{p}", -2.8, y, w=1.1, h=0.85)
        fs2 = [fl((-5.8, y), (-4.64, y)), fl((-4.16, y), (-3.35, y)), fl((-2.25, y), (-0.9, y))]
        r2 = fl((-1.5, y), (-1.5, y - 0.9), (-4.4, y - 0.9), (-4.4, y - 0.24), col=BLEU)
        self.at(self.t("j3"), *[Create(f) for f in fs2], Create(s2), Create(i[0]), FadeIn(i[1]), Create(r2), run_time=0.9)
        f2 = pos(M(r"\frac{K/p}{1 + K/p} = \frac{1}{1 + p/K}", sc=0.9, color=JAUNE), 0.2, -1.45)
        self.ecr(self.a("j3", "On obtient"), f2, rt=1.0)
        g1 = pos(T(r"gain exactement $1$ : position finale $=$ consigne", sc=0.7, color=VERT), -6.3, -3.05)
        self.ecr(self.t("j4"), g1, rt=1.1)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"À retenir", "Bilan")
        pts = [("k1", r"$H(p) = \dfrac{K}{1 + \tau p}$ : un gain, une constante de temps", BLEU),
               ("k2", r"Échelon : $63\,\%$ à $\tau$, $95\,\%$ à $3\tau$, jamais de dépassement", VERT),
               ("k3", r"Rampe : retard $\tau$, écart de traînage $a\tau$ si $K = 1$", ORANGE),
               ("k4", r"Fréquence : passe-bas, cassure en $1/\tau$ : $-3$ dB et $-45^\circ$", JAUNE)]
        for k, (ph, txt, c) in enumerate(pts):
            y = 1.8 - 1.3*k
            ca = carte(k+1, c, -5.9, y); tx = pos(T(txt, sc=0.74), -5.35, y)
            self.at(self.t(ph), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice résolu -- l'énoncé", "Application")
        d1 = pos(T(r"échelon de $12$ V \;$\Rightarrow$\; $2\,400$ tr/min en régime permanent", sc=0.8), -6.3, 2.0)
        d2 = pos(T(r"au bout de $0{,}15$ s : $1\,512$ tr/min", sc=0.8), -6.3, 1.3)
        self.ecr(self.a("l1", "On applique"), d1, rt=1.3); self.ecr(self.t("l2"), d2, rt=1.0)
        qs = [r"le modèle, en unités SI ?", r"le temps de réponse à $5\,\%$ ?", r"la réponse à $u = \sin(20\,t)$ volts ?"]
        for k, (q, fr) in enumerate(zip(qs, ["son modèle", "Son temps de réponse", "Et sa réponse"])):
            m = pos(T(q, sc=0.75, color=ROUGE), -5.4, 0.25 - 0.62*k)
            self.at(self.a("l3", fr), Create(carte(k+1, ROUGE, -6.0, 0.25 - 0.62*k)), Ecrire(m, rt=0.8), run_time=0.8)
        rf = pos(T(r"Réfléchissons : montée douce, pas de dépassement $\Rightarrow$ premier ordre", sc=0.72, color=BLEU), -6.3, -2.2)
        rq = pos(M(r"\frac{1512}{2400} = \;?", sc=0.85, color=JAUNE), -6.3, -3.05)
        self.ecr(self.t("l4"), rf, rt=1.2); self.ecr(self.a("l4", "Et mille cinq cent douze"), rq, rt=0.8)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- la solution", "Application")
        def etape(k, c, y, m, ph, fr, rt=1.0):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(self.a(ph, fr), Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        etape(1, BLEU, 2.2, M(r"K = \frac{2400}{12} = 200\ \mathrm{tr\,min^{-1}\,V^{-1}}", sc=0.78), "m1", "Première étape", 1.2)
        si = pos(M(r"\times \frac{2\pi}{60} \;\Rightarrow\; K \approx 20{,}9\ \mathrm{rad\,s^{-1}\,V^{-1}}", sc=0.78, color=BLEU), -5.85, 1.35)
        self.ecr(self.t("m2"), si, rt=1.1)
        etape(2, VERT, 0.45, M(r"\frac{1512}{2400} = 0{,}63 \;\Rightarrow\; \tau = 0{,}15\ \mathrm{s}", sc=0.78), "m3", "Deuxième étape", 1.1)
        ax = axes(4.3, 0.9, 3.8, 2.6, [0, 1.0, 1], [0, 2800, 1000])
        cb = ax.plot(lambda t: 2400*(1 - np.exp(-t/0.15)), x_range=[0, 0.97, 0.005], color=BLEU, stroke_width=4)
        pm = Dot(ax.c2p(0.15, 1512), color=JAUNE, radius=0.08); lm = M(r"(0{,}15\,;\,1512)", sc=0.55, color=JAUNE).next_to(pm, RIGHT, buff=0.12)
        l2 = DashedLine(ax.c2p(0, 2400), ax.c2p(1.0, 2400), color=GRIS, stroke_width=2)
        self.at(self.a("m3", "Le repère"), Create(ax), Create(l2), Create(cb), FadeIn(pm, scale=2), FadeIn(lm), run_time=1.0)
        mo = pos(M(r"H(p) = \frac{20{,}9}{1 + 0{,}15\,p}, \qquad t_{r5\%} = 3\tau = 0{,}45\ \mathrm{s}", sc=0.78, color=JAUNE), -5.85, -0.45)
        self.ecr(self.t("m4"), mo, rt=1.3); self.play(Create(enc(mo, col=JAUNE, buff=0.12)), run_time=0.4)
        etape(3, ORANGE, -1.4, M(r"\tau\omega = 0{,}15 \times 20 = 3", sc=0.78), "m5", "Troisième étape")
        am = pos(M(r"\frac{20{,}9}{\sqrt{1 + 9}} \approx 6{,}6\ \mathrm{rad/s}", sc=0.78), -5.85, -2.3)
        ph = pos(M(r"\varphi = -\arctan 3 \approx -72^\circ", sc=0.78), -1.5, -2.3)
        self.ecr(self.a("m6", "Amplitude"), am, rt=1.0); self.ecr(self.t("m7"), ph, rt=0.9)
        ve = T(r"basse pulsation : $20{,}9$ \; ; \; ici : un tiers \;$\checkmark$", sc=0.64, color=VERT).move_to([3.0, -3.2, 0])
        self.ecr(self.t("m8"), ve, rt=1.1)
        nx = T(r"Prochain chapitre : le deuxième ordre", sc=0.62, color=GRIS).move_to([4.3, -1.15, 0])
        self.at(self.t("m9"), FadeIn(nx), run_time=0.6)
        self.fin()
