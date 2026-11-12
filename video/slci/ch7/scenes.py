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
def courbe(ax, t, y, col, sw=4):
    return VMobject(color=col, stroke_width=sw).set_points_smoothly([ax.c2p(a, b) for a, b in zip(t, y)])

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PTSI", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Automatique -- Chapitre 7}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Performances : précision et rapidité", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        ax = axes(3.7, -1.0, 4.4, 2.6, [0, 12, 2], [0, 1.25, 1])
        t = np.linspace(0, 11.9, 200); _, y = signal.step(signal.lti([0.9], [1, 0.8, 1]), T=t)
        cs = DashedLine(ax.c2p(0, 1), ax.c2p(12, 1), color=GRIS, stroke_width=3)
        self.at(self.a("a1", "atteint-il vraiment"), Create(ax), Create(cs), Create(courbe(ax, t, y, BLEU, 5)), run_time=1.5)
        items = []
        for k, (txt, c) in enumerate([("Les critères", BLEU), ("L'écart en régime permanent", VERT), ("La classe", ORANGE),
                                       ("Les perturbations", ROUGE), ("La rapidité, les correcteurs", BLEU), ("Exercice résolu : une enceinte", JAUNE)]):
            yy = 0.75 - 0.6*k
            items.append(VGroup(carte(k+1, c, -6.2, yy), pos(T(txt, sc=0.74), -5.65, yy)))
        for it, (sid, fr) in zip(items, [("a3", "les critères"), ("a3", "l'écart en régime"), ("a3", "la classe"),
                                         ("a3", "les perturbations"), ("a3", "la rapidité"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"7.1 -- Les critères du cahier des charges", "Performances")
        ax = axes(-1.8, -0.5, 8.0, 4.6, [0, 14, 2], [0, 1.35, 1])
        lt = M("t", sc=0.7).next_to(ax.x_axis.get_end(), DOWN, buff=0.12)
        t = np.linspace(0, 13.9, 260); _, y = signal.step(signal.lti([0.9], [1, 0.8, 1]), T=t)
        cs = DashedLine(ax.c2p(0, 1), ax.c2p(14, 1), color=GRIS, stroke_width=3); lc = T("consigne", sc=0.62, color=GRIS).next_to(ax.c2p(7, 1), UP, buff=0.08)
        b1 = DashedLine(ax.c2p(0, 0.945), ax.c2p(14, 0.945), color=GRIS, stroke_width=1.5); b2 = DashedLine(ax.c2p(0, 0.855), ax.c2p(14, 0.855), color=GRIS, stroke_width=1.5)
        self.at(self.t("b1"), Create(ax), FadeIn(lt), Create(cs), FadeIn(lc), run_time=0.6); self.play(Create(courbe(ax, t, y, BLEU, 5)), run_time=1.2)
        i = y.argmax(); tm, ym = t[i], y[i]
        d = Line(ax.c2p(tm, 0.9), ax.c2p(tm, ym), color=VERT, stroke_width=5); ld = M("D_1", sc=0.75, color=VERT).next_to(d, RIGHT, buff=0.1)
        td = pos(T(r"$D_1$ : \textbf{amortissement}", sc=0.72, color=VERT), 2.9, 1.9)
        self.at(self.t("b2"), Create(d), FadeIn(ld), Ecrire(td, rt=0.8), run_time=0.8)
        out = np.where(np.abs(y - 0.9) > 0.045)[0]; tr = t[out[-1] + 1]
        v = DashedLine(ax.c2p(tr, 0), ax.c2p(tr, y[out[-1] + 1]), color=ORANGE, stroke_width=3); lv = M(r"t_{r5\%}", sc=0.65, color=ORANGE).next_to(ax.c2p(tr, 0), DOWN, buff=0.12)
        tt = pos(T(r"$t_{r5\%}$ : \textbf{rapidité}", sc=0.72, color=ORANGE), 2.9, 1.25)
        self.at(self.t("b3"), Create(b1), Create(b2), Create(v), FadeIn(lv), Ecrire(tt, rt=0.8), run_time=1.0)
        e = DoubleArrow(ax.c2p(12.6, 0.9), ax.c2p(12.6, 1.0), color=ROUGE, buff=0, stroke_width=3, tip_length=0.1); le = M(r"\varepsilon_s", sc=0.7, color=ROUGE).next_to(e, LEFT, buff=0.1)
        te = pos(T(r"$\varepsilon_s$ : \textbf{précision}", sc=0.72, color=ROUGE), 2.9, 0.6)
        self.at(self.t("b4"), GrowFromCenter(e), FadeIn(le), Ecrire(te, rt=0.8), run_time=0.8)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"7.2 -- L'écart en régime permanent", "Précision")
        a = pos(M(r"\varepsilon = E - S", sc=0.95), -6.3, 1.9)
        self.ecr(self.t("c1"), a, rt=0.7)
        b = M(r"\varepsilon(p) = \frac{E(p)}{1 + H_{BO}(p)}", sc=1.15, color=JAUNE).move_to([0, 0.6, 0])
        self.ecr(self.a("c2", "on trouve"), b, rt=1.1); self.play(Create(enc(b, col=JAUNE)), run_time=0.4)
        c = M(r"\varepsilon_\infty = \lim_{p \to 0} \; p\,\frac{E(p)}{1 + H_{BO}(p)}", sc=1.0, color=BLEU).move_to([0, -1.2, 0])
        self.ecr(self.t("c3"), c, rt=1.2)
        st = T(r"\textbf{si la boucle est stable !}", sc=0.78, color=ROUGE).move_to([0, -2.55, 0])
        self.ecr(self.a("c3", "Si la boucle est stable"), st, rt=0.7)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"7.3 -- La classe décide de tout", "Précision")
        f = pos(M(r"H_{BO}(p) = \frac{K}{p^\alpha} \cdot \frac{1 + \cdots}{1 + \cdots}", sc=0.95, color=JAUNE), -6.3, 2.0)
        self.ecr(self.t("d1"), f, rt=1.1)
        cols = [-3.4, -0.6, 1.9, 4.4]; ys = [0.7, -0.35, -1.4]
        hd = [T(r"\textbf{consigne}", sc=0.7, color=GRIS), T(r"\textbf{classe 0}", sc=0.7, color=GRIS), T(r"\textbf{classe 1}", sc=0.7, color=GRIS), T(r"\textbf{classe 2}", sc=0.7, color=GRIS)]
        for m, x in zip(hd, cols): m.move_to([x, ys[0], 0])
        r1 = [T(r"échelon $E_0$", sc=0.72), M(r"\frac{E_0}{1 + K}", sc=0.85, color=ORANGE), M("0", sc=0.85, color=VERT), M("0", sc=0.85, color=VERT)]
        r2 = [T(r"rampe $a\,t$", sc=0.72), M(r"\infty", sc=0.85, color=ROUGE), M(r"\frac{a}{K}", sc=0.85, color=ORANGE), M("0", sc=0.85, color=VERT)]
        for m, x in zip(r1, cols): m.move_to([x, ys[1], 0])
        for m, x in zip(r2, cols): m.move_to([x, ys[2], 0])
        lg = VGroup(Line([-4.8, 0.3, 0], [5.4, 0.3, 0], color=GRIS, stroke_width=2), Line([-2.0, 1.0, 0], [-2.0, -1.95, 0], color=GRIS, stroke_width=2))
        self.at(self.a("d2", "Pour un échelon"), *[FadeIn(m) for m in hd], Create(lg), FadeIn(r1[0]), run_time=0.7)
        self.at(self.a("d2", "en classe zéro"), FadeIn(r1[1]), run_time=0.5)
        self.at(self.a("d2", "Dès la classe un"), FadeIn(r1[2]), FadeIn(r1[3]), run_time=0.5)
        self.at(self.t("d3"), FadeIn(r2[0]), run_time=0.4)
        self.at(self.a("d3", "infini en classe"), FadeIn(r2[1]), run_time=0.4)
        self.at(self.a("d3", "a sur K"), FadeIn(r2[2]), run_time=0.4)
        self.at(self.a("d3", "et nul en classe deux"), FadeIn(r2[3]), run_time=0.4)
        p = T(r"chaque \textbf{intégrateur} de la FTBO annule un type d'écart", sc=0.78, color=JAUNE).move_to([0, -2.85, 0])
        self.ecr(self.t("d4"), p, rt=1.1); self.play(Create(enc(p, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"7.4 -- Deux exemples en direct", "Précision")
        a = pos(M(r"H_{BO} = \frac{9}{(1 + 2p)(1 + 0{,}1p)} : \;\text{classe } 0, \; K = 9", sc=0.85), -6.3, 1.9)
        self.ecr(self.t("e1"), a, rt=1.2)
        b = pos(M(r"\varepsilon_s = \frac{1}{1 + 9} = 0{,}1 \;\;\Rightarrow\;\; 90\,\%\ \text{de la consigne}", sc=0.85, color=ORANGE), -6.3, 0.75)
        self.ecr(self.t("e2"), b, rt=1.2)
        c = pos(M(r"H_{BO} = \frac{20}{p\,(1 + 0{,}1p)} : \;\text{classe } 1 \;\Rightarrow\; \varepsilon_s = 0", sc=0.85), -6.3, -0.6)
        self.ecr(self.t("e3"), c, rt=1.2)
        d = pos(M(r"\text{rampe } 0{,}5\ \mathrm{m/s} : \;\; \varepsilon_v = \frac{0{,}5}{20} = 2{,}5\ \mathrm{cm}", sc=0.85, color=ROUGE), -6.3, -1.85)
        self.ecr(self.t("e4"), d, rt=1.2); self.play(Create(enc(d, col=ROUGE, buff=0.15)), run_time=0.4)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"7.5 -- Rejeter une perturbation", "Perturbations")
        ex = pos(T(r"couple résistant, porte qui s'ouvre, rafale de vent", sc=0.72, color=GRIS), -6.3, 2.1)
        self.ecr(self.t("f1"), ex, rt=1.0)
        y = 0.75
        s = som(-5.0, y); c = blk("C", -3.7, y, w=0.9); g1 = blk("G_1", -2.2, y, w=0.9); s2 = som(-0.8, y, col=ROUGE); g2 = blk("G_2", 0.6, y, w=0.9)
        fs = [fl((-6.5, y), (-5.24, y)), fl((-4.76, y), (-4.15, y)), fl((-3.25, y), (-2.65, y)), fl((-1.75, y), (-1.04, y)), fl((-0.56, y), (0.15, y)), fl((1.05, y), (2.4, y))]
        d = fl((-0.8, y + 0.95), (-0.8, y + 0.24), col=ROUGE); ld = M("D", sc=0.7, color=ROUGE).move_to([-0.45, y + 0.85, 0])
        r = fl((1.8, y), (1.8, y - 0.9), (-5.0, y - 0.9), (-5.0, y - 0.24), col=BLEU)
        self.at(self.a("f1", "un couple résistant"), *[Create(f) for f in fs], Create(s), Create(c[0]), FadeIn(c[1]), Create(g1[0]), FadeIn(g1[1]), Create(s2), Create(g2[0]), FadeIn(g2[1]), Create(r), Create(d), FadeIn(ld), run_time=1.2)
        su = pos(M(r"S = H_E\,E + H_D\,D, \qquad \text{effet permanent} : H_D(0)\,D_0", sc=0.8), -6.3, -0.75)
        self.ecr(self.t("f2"), su, rt=1.3)
        hd = pos(M(r"H_D = \frac{-\,G_2}{1 + C\,G_1G_2}", sc=0.9, color=ROUGE), -6.3, -1.85)
        self.ecr(self.t("f3"), hd, rt=1.0)
        k = T(r"rejet total $\iff$ un intégrateur \textbf{en amont} de $D$", sc=0.78, color=JAUNE).move_to([1.8, -1.85, 0])
        self.ecr(self.t("f4"), k, rt=1.1); self.play(Create(enc(k, col=JAUNE, buff=0.15)), run_time=0.4)
        am = Brace(VGroup(c, g1), UP, color=VERT); lam = T("en amont", sc=0.6, color=VERT).next_to(am, UP, buff=0.05)
        self.at(self.t("f5"), GrowFromCenter(am), FadeIn(lam), run_time=0.6)
        av = T(r"un intégrateur en aval ne suffit pas", sc=0.7, color=ROUGE).move_to([1.8, -2.95, 0])
        self.ecr(self.a("f5", "Un intégrateur placé après"), av, rt=1.0)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"7.6 -- Deux intégrateurs qui ne se valent pas", "Perturbations")
        a = pos(M(r"C = 4, \qquad G_1 = \frac{2}{1 + 0{,}5p}", sc=0.9), -6.3, 1.9)
        self.ecr(self.t("g1"), a, rt=1.1)
        b = pos(M(r"G_2 = \frac{5}{1 + 2p} : \;\; H_D(0) = -\frac{5}{1 + 4\times2\times5} = -\frac{5}{41}", sc=0.85), -6.3, 0.6)
        self.ecr(self.t("g2"), b, rt=1.3)
        b2 = pos(T(r"$\approx -12\,\%$ de la perturbation, en permanence", sc=0.68, color=ORANGE), -5.6, -0.25)
        self.ecr(self.a("g2", "La sortie baisse"), b2, rt=0.9)
        c = pos(M(r"G_2 = \frac{5}{p} : \;\; H_D(0) = -\frac{1}{8} \;\;\text{(intégrateur en aval)}", sc=0.85, color=ROUGE), -6.3, -1.2)
        self.ecr(self.t("g3"), c, rt=1.3)
        d = pos(M(r"C = K_c\,\frac{1 + T_ip}{T_ip} \;\;\text{(en amont)} : \;\; H_D(0) = 0", sc=0.85, color=VERT), -6.3, -2.45)
        self.ecr(self.t("g4"), d, rt=1.3); self.play(Create(enc(d, col=VERT, buff=0.15)), run_time=0.4)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"7.7 -- La rapidité", "Rapidité")
        a = pos(T(r"boucle fermée du 1\textsuperscript{er} ordre : $t_{r5\%} = 3\tau'$ \quad ; \quad du 2\textsuperscript{e} ordre : abaque", sc=0.75), -6.3, 1.9)
        self.ecr(self.t("h1"), a, rt=1.3)
        b = M(r"t_{r5\%} \approx \frac{3}{\omega_{c0}}", sc=1.3, color=JAUNE).move_to([0, 0.45, 0])
        self.ecr(self.t("h2"), b, rt=1.0); self.play(Create(enc(b, col=JAUNE)), run_time=0.4)
        bb = T(r"boucle bien amortie ; $\omega_{c0}$ : coupure à $0$ dB de la FTBO", sc=0.68, color=GRIS).move_to([0, -0.85, 0])
        self.ecr(self.a("h2", "La pulsation de coupure"), bb, rt=1.0)
        c = T(r"aller vite $=$ commander fort : la \textbf{saturation} de l'actionneur limite", sc=0.75, color=ROUGE).move_to([0, -2.2, 0])
        self.ecr(self.t("h3"), c, rt=1.2)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"7.8 -- À vous : un écart statique", "Exercice")
        h = M(r"H_{BO} = \frac{5}{(1 + p)(1 + 0{,}2p)}", sc=1.0, color=JAUNE).move_to([-1.2, 1.9, 0])
        q = T(r"écart pour un échelon de $2$ ? \; pour une rampe ?", sc=0.72, color=BLEU).next_to(h, DOWN, buff=0.3)
        self.ecr(self.a("i1", "F T B O"), h, rt=1.1); self.ecr(self.a("i1", "Quel écart"), q, rt=0.9)
        pa, arc = chrono(4.3, 1.9)
        self.at(self.a("i1", "Mettez sur pause"), FadeIn(pa), Create(arc), run_time=0.5)
        self.play(Uncreate(arc), run_time=2.6); self.play(FadeOut(pa), run_time=0.2)
        a = pos(M(r"\text{classe } 0, \; K = 5 : \;\; \varepsilon_s = \frac{2}{1 + 5} \approx 0{,}33", sc=0.92), -6.3, -0.3)
        self.ecr(self.t("i2"), a, rt=1.3)
        b = pos(T(r"rampe : l'écart \textbf{diverge} (classe $0$)", sc=0.8, color=ROUGE), -6.3, -1.6)
        self.ecr(self.t("i3"), b, rt=1.0); self.play(Create(enc(b)), run_time=0.4)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"7.9 -- Le dilemme et les correcteurs", "Correction")
        a = pos(T(r"gain $\nearrow$ : écart $\searrow$, plus rapide \ldots{} mais marges $\searrow$", sc=0.75, color=ORANGE), -6.3, 2.0)
        b = pos(T(r"intégrateur : écart annulé \ldots{} mais $-90^\circ$ partout", sc=0.75, color=ORANGE), -6.3, 1.3)
        self.ecr(self.t("j1"), a, rt=1.2); self.ecr(self.t("j2"), b, rt=1.1)
        c = pos(T(r"\textbf{correcteur} : agir différemment selon les pulsations \;$\Rightarrow$\; le \textbf{PI}", sc=0.75, color=VERT), -6.3, 0.45)
        self.ecr(self.t("j3"), c, rt=1.2)
        f = pos(M(r"C(p) = K_p\,\frac{1 + T_i\,p}{T_i\,p}", sc=1.0, color=JAUNE), -6.3, -0.75)
        self.ecr(self.t("j4"), f, rt=1.0); self.play(Create(enc(f, col=JAUNE, buff=0.15)), run_time=0.4)
        ax = Axes(x_range=[-2, 1, 1], y_range=[-5, 40, 10], x_length=5.0, y_length=2.0, tips=False, axis_config={"stroke_opacity": 0}).move_to([3.2, -0.9, 0])
        fr = Rectangle(width=5.0, height=2.0, color=GRIS, stroke_width=2).move_to([3.2, -0.9, 0])
        asy = VMobject(color=ORANGE, stroke_width=4).set_points_as_corners([ax.c2p(-2, 40), ax.c2p(-1, 20), ax.c2p(1, 20)])
        li = T(r"intégrateur", sc=0.55, color=ORANGE).move_to(ax.c2p(-1.5, 22)); lg = T(r"gain $K_p$", sc=0.55, color=ORANGE).move_to(ax.c2p(0.2, 13))
        lc = M(r"1/T_i", sc=0.6, color=GRIS).next_to(ax.c2p(-1, -5), DOWN, buff=0.1)
        self.at(self.a("j4", "Un intégrateur en basses"), Create(fr), Create(asy), FadeIn(li), FadeIn(lg), FadeIn(lc), run_time=1.0)
        r = T(r"cassure une décade sous $\omega_{c0}$ : $-6^\circ$ de marge seulement, écart statique nul", sc=0.72, color=VERT).move_to([0, -2.8, 0])
        self.ecr(self.t("j5"), r, rt=1.3)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"À retenir", "Bilan")
        pts = [("k1", r"$\varepsilon = \dfrac{E}{1 + H_{BO}}$, valeur finale si la boucle est stable", BLEU),
               ("k2", r"Classe $0$ : $\dfrac{E_0}{1 + K}$ \; ; \; classe $1$ : $0$ à l'échelon, $\dfrac{a}{K}$ à la rampe", VERT),
               ("k3", r"Perturbation rejetée : un intégrateur \textbf{en amont}", ORANGE),
               ("k4", r"$t_{r5\%} \approx 3/\omega_{c0}$ ; \; le PI pour la précision", JAUNE)]
        for k, (ph, txt, c) in enumerate(pts):
            yy = 1.8 - 1.3*k
            ca = carte(k+1, c, -5.9, yy); tx = pos(T(txt, sc=0.74), -5.35, yy)
            self.at(self.t(ph), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice résolu -- l'énoncé", "Application")
        y = 1.2
        s = som(-5.0, y); c = blk(r"K_c = 20", -3.4, y, w=1.6, col=ORANGE); s2 = som(-1.6, y, col=ROUGE); g = blk(r"\frac{0{,}5}{1 + 100p}", 0.4, y, w=2.1, h=0.9)
        fs = [fl((-6.5, y), (-5.24, y)), fl((-4.76, y), (-4.2, y)), fl((-2.6, y), (-1.84, y)), fl((-1.36, y), (-0.65, y)), fl((1.45, y), (3.0, y))]
        d = fl((-1.6, y + 0.95), (-1.6, y + 0.24), col=ROUGE); ld = T(r"pertes $100$ W", sc=0.6, color=ROUGE).move_to([-1.6, y + 1.2, 0])
        r = fl((2.3, y), (2.3, y - 1.0), (-5.0, y - 1.0), (-5.0, y - 0.24), col=BLEU)
        lc = M(r"40\ \mathrm{K}", sc=0.65).move_to([-6.1, y + 0.32, 0]); lt = M(r"\theta", sc=0.75, color=JAUNE).move_to([3.3, y, 0])
        self.at(self.a("l1", "Une enceinte chauffée"), Create(g[0]), FadeIn(g[1]), Create(fs[3]), Create(fs[4]), FadeIn(lt), run_time=0.8)
        self.at(self.a("l2", "Un correcteur"), Create(fs[0]), Create(s), Create(fs[1]), Create(c[0]), FadeIn(c[1]), Create(fs[2]), Create(s2), Create(r), run_time=1.0)
        self.at(self.a("l2", "Consigne"), FadeIn(lc), run_time=0.4)
        self.at(self.t("l3"), Create(d), FadeIn(ld), run_time=0.6)
        qs = [(r"écart dû à la consigne ?", "l'écart dû"), (r"effet de la perturbation ?", "L'effet"), (r"comment tout annuler ?", "Et comment")]
        for i, (q, fr) in enumerate(qs):
            m = pos(T(q, sc=0.78, color=ROUGE), -5.4, -0.8 - 0.65*i)
            self.at(self.a("l4", fr), Create(carte(i+1, ROUGE, -6.0, -0.8 - 0.65*i)), Ecrire(m, rt=0.7), run_time=0.7)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- la solution", "Application")
        def etape(k, c, y, m, ph, fr, rt=1.0):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(self.a(ph, fr), Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        etape(1, BLEU, 2.15, M(r"K_c\,G = \frac{10}{1 + 100p} : \;\text{classe } 0, \; K = 10", sc=0.78), "m1", "Première étape", 1.2)
        a = pos(M(r"\varepsilon_s = \frac{40}{1 + 10} \approx 3{,}6\ \mathrm{K} \;\Rightarrow\; \theta = 36{,}4\ \mathrm{K}", sc=0.78, color=ORANGE), -5.85, 1.1)
        self.ecr(self.t("m2"), a, rt=1.2)
        etape(2, VERT, 0.0, M(r"H_D(0) = \frac{-0{,}5}{1 + 10} \;\Rightarrow\; -4{,}5\ \mathrm{K} \text{ pour } 100\ \mathrm{W}", sc=0.78), "m3", "Deuxième étape", 1.2)
        b = pos(T(r"$\theta \approx 31{,}8$ K : écart de plus de $8$ K !", sc=0.72, color=ROUGE), -5.85, -0.85)
        self.ecr(self.t("m4"), b, rt=1.0)
        ax = axes(4.3, 0.6, 4.4, 3.0, [0, 600, 100], [0, 45, 10])
        lt = M("t", sc=0.6).next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        cs = DashedLine(ax.c2p(0, 40), ax.c2p(600, 40), color=GRIS, stroke_width=2); l40 = M("40", sc=0.55, color=GRIS).next_to(ax.c2p(0, 40), LEFT, buff=0.1)
        t = np.linspace(0, 590, 300)
        # P seul : consigne à t = 0, pertes à t = 300 s
        def pseul(tt):
            y = 36.36*(1 - np.exp(-tt*11/100))
            return np.where(tt > 300, y - 4.545*(1 - np.exp(-(tt - 300)*11/100)), y)
        cp = VMobject(color=ORANGE, stroke_width=4).set_points_smoothly([ax.c2p(a_, b_) for a_, b_ in zip(t, pseul(t))])
        lp = T("P", sc=0.6, color=ORANGE).move_to(ax.c2p(560, 28))
        self.at(self.a("m4", "Au total"), Create(ax), FadeIn(lt), Create(cs), FadeIn(l40), Create(cp), FadeIn(lp), run_time=1.2)
        etape(3, ORANGE, -1.75, M(r"C = 20\,\frac{1 + T_ip}{T_ip} \;\Rightarrow\; \text{classe } 1", sc=0.78), "m5", "Troisième étape", 1.2)
        c = pos(T(r"écart et effet des pertes : \textbf{nuls}", sc=0.72, color=VERT), -5.85, -2.55)
        self.ecr(self.t("m6"), c, rt=0.9)
        # PI : simulation numérique simple
        Ti = 100.0; Kc = 20.0; dt = 0.5; th = 0.0; integ = 0.0; tt_, yy_ = [], []
        for k in range(int(590/dt)):
            tk = k*dt; e = 40 - th; integ += e*dt
            u = Kc*(e + integ/Ti) - (100 if tk > 300 else 0)
            th += dt*(0.5*u - th)/100; tt_.append(tk); yy_.append(th)
        cpi = VMobject(color=VERT, stroke_width=4).set_points_smoothly([ax.c2p(a_, b_) for a_, b_ in zip(tt_[::4], yy_[::4])])
        lpi = T("PI", sc=0.6, color=VERT).move_to(ax.c2p(560, 43.5))
        self.at(self.a("m6", "s'annulent"), Create(cpi), FadeIn(lpi), run_time=1.2)
        ti = T(r"$T_i \approx 100$ s : une décade sous $\omega_{c0} \approx 0{,}1$ rad/s", sc=0.62, color=BLEU).move_to([4.0, -1.55, 0])
        self.ecr(self.t("m7"), ti, rt=1.1)
        nx = T(r"Prochain chapitre (2\textsuperscript{e} année) : réglage des correcteurs", sc=0.58, color=GRIS).move_to([3.6, -3.15, 0])
        self.at(self.t("m8"), FadeIn(nx), run_time=0.6)
        self.fin()
