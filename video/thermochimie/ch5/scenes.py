from base import *
D = r"\mathrm{d}"
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def boite(txt, col, fond, w=3.5, h=1.0):
    r = RoundedRectangle(width=w, height=h, corner_radius=0.1, color=col, stroke_width=2.5, fill_color=fond, fill_opacity=0.2)
    return VGroup(r, txt.move_to(r))
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)
def chrono(x, y):
    pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([x, y, 0])
    arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
    return pa, arc
AX = {"color": CRAIE, "stroke_width": 2, "include_ticks": False, "tip_width": 0.18, "tip_height": 0.18}

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"THERMOCHIMIE \;·\; PT*", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Chapitre 5}", sc=1.3, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Deuxième principe : évolution et équilibre", sc=0.95).move_to([0, 1.75, 0])
        tr = Line([-4.4, 1.3, 0], [4.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=0.9), Create(tr), run_time=1.0)
        q = M(r"Q_r", r"\;\longrightarrow\;", r"K^\circ", r"\quad ?", sc=1.0, color=BLEU).move_to([-2.6, 0.55, 0]); q[3].set_color(JAUNE)
        self.at(self.a("a1", "Pourquoi une réaction"), Ecrire(VGroup(q[0], q[1], q[2]), rt=0.9))
        self.at(self.a("a1", "à un équilibre précis"), FadeIn(q[3], scale=1.6), run_time=0.4)
        ad = T(r"PTSI : \textit{admis}", sc=0.7, color=GRIS).move_to([2.0, 0.75, 0])
        de = T(r"PT : \textbf{démontré}", sc=0.7, color=VERT).move_to([2.0, 0.3, 0])
        self.at(self.a("a2", "c'était admis"), FadeIn(ad), run_time=0.4); self.at(self.a("a3", "on le démontre"), Ecrire(de, rt=0.6))
        items = []
        for k, (txt, col) in enumerate([("Critère d'évolution", BLEU), ("Constante d'équilibre", VERT), (r"Courbe $G(\xi)$", ORANGE),
                                         ("État final : équilibre ou transformation totale", ROUGE), ("Exercice résolu : le haut fourneau", JAUNE)]):
            y = -0.5 - 0.68*k
            items.append(VGroup(carte(k+1, col, -3.6, y), pos(T(txt, sc=0.8), -3.0, y)))
        for it, (sid, fr) in zip(items, [("a4", "le critère"), ("a4", "la constante"), ("a4", "la courbe"), ("a4", "et l'état final"), ("a5", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a5", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"5.1 -- Création d'entropie", "1/4 · Critère d'évolution")
        ca = pos(T(r"Système fermé, une réaction, $T$ et $P$ fixées", sc=0.75, color=BLEU), -6.4, 2.2)
        self.ecr(self.a("b1", "un système fermé"), ca, rt=1.3)
        f1 = pos(M(r"T\,\delta S_c", r"\;=\;", r"-\Delta_r G\;" + D + r"\xi", r"\;\geq\; 0", sc=1.05), -6.0, 1.05); f1[3].set_color(VERT)
        self.at(self.a("b2", "T fois l'entropie"), Ecrire(VGroup(f1[0], f1[1], f1[2]), rt=1.2))
        self.at(self.a("b2", "toujours positive"), Ecrire(f1[3], rt=0.5)); self.play(Create(enc(f1)), run_time=0.4)
        f2 = pos(M(D + r"G", r"\;=\;", r"-T\,\delta S_c", r"\;\leq\; 0", sc=1.05), -6.0, -0.35); f2[3].set_color(JAUNE)
        self.at(self.a("b3", "dé G égale"), Ecrire(VGroup(f2[0], f2[1], f2[2]), rt=1.0)); self.at(self.a("b3", "Donc dé G"), Ecrire(f2[3], rt=0.5))
        po = pos(T(r"$G$ \textbf{diminue} : potentiel thermodynamique", sc=0.72, color=JAUNE), -6.0, -1.5)
        self.ecr(self.a("b4", "l'enthalpie libre ne peut"), po, rt=1.3)
        ax = Axes(x_range=[-1.2, 1.2, 1], y_range=[0, 1.6, 1], x_length=4.6, y_length=3.0, axis_config={"stroke_opacity": 0}).move_to([3.7, -1.0, 0])
        va = ax.plot(lambda x: x*x, x_range=[-1.15, 1.15, 0.01], color=BLEU, stroke_width=4)
        bi = Dot(ax.c2p(-1.0, 1.0), radius=0.14, color=ORANGE).shift(UP*0.14)
        lg = M("G", sc=0.8, color=BLEU).next_to(ax.c2p(-1.15, 1.32), UP, buff=0.05)
        eq = T(r"équilibre", sc=0.6, color=VERT).next_to(ax.c2p(0, 0), DOWN, buff=0.2)
        self.at(self.a("b5", "Comme une bille"), Create(va), FadeIn(lg), FadeIn(bi), run_time=0.8)
        self.at(self.a("b5", "le système descend"), MoveAlongPath(bi, ax.plot(lambda x: x*x + 0.08, x_range=[-1.0, 0.0, 0.01])), run_time=1.4, rate_func=smooth)
        self.at(self.a("b5", "c'est l'équilibre"), FadeIn(eq), Flash(bi, color=VERT), run_time=0.6)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"5.1 -- Démonstration", "1/4 · Critère d'évolution")
        l1 = pos(M(r"\text{1}^{\text{er}}\text{ principe (monobare) :}\quad " + D + r"H = \delta Q", sc=0.85), -6.3, 2.1)
        l2 = pos(M(r"\text{2}^{\text{e}}\text{ principe :}\quad " + D + r"S = \frac{\delta Q}{T} + \delta S_c", sc=0.85), -6.3, 1.2)
        self.ecr(self.t("c2") + 0.2, l1, rt=1.3); self.ecr(self.t("c3") + 0.2, l2, rt=1.4)
        l3 = pos(M(D + r"G = " + D + r"H - T\," + D + r"S", r"\;=\;", r"\delta Q", r"\;-\;", r"\delta Q", r"\;-\;T\,\delta S_c", sc=0.95), -6.3, 0.05)
        self.at(self.a("c4", "dé G égale"), Ecrire(l3[0], rt=1.0)); self.play(Ecrire(VGroup(*l3[1:]), rt=1.2))
        b1 = Line(l3[2].get_corner(DL), l3[2].get_corner(UR), color=ROUGE, stroke_width=4); b2 = Line(l3[4].get_corner(DL), l3[4].get_corner(UR), color=ROUGE, stroke_width=4)
        self.at(self.a("c4", "se compensent"), Create(b1), Create(b2), run_time=0.5)
        r1 = M(r"=\;-T\,\delta S_c", sc=0.95, color=JAUNE).next_to(l3, RIGHT, buff=0.3)
        self.at(self.a("c4", "Il reste"), Ecrire(r1, rt=0.7))
        l4 = pos(M(r"\text{Or : }\; " + D + r"G = \sum_i \mu_i\," + D + r"n_i", r"\;=\;\Delta_r G\;" + D + r"\xi", sc=0.95), -6.3, -1.2)
        self.at(self.a("c5", "Par ailleurs"), Ecrire(l4[0], rt=1.1)); self.at(self.a("c5", "c'est-à-dire"), Ecrire(l4[1], rt=0.8))
        fi = M(r"T\,\delta S_c = -\Delta_r G\;" + D + r"\xi", sc=1.15).move_to([0, -2.6, 0])
        self.at(self.a("c5", "On égale"), Ecrire(fi, rt=1.0)); self.play(Create(enc(fi)), run_time=0.4)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"5.2 -- Critère d'évolution spontanée", "1/4 · Critère d'évolution")
        cr = M(r"\Delta_r G\;" + D + r"\xi \;\leq\; 0", sc=1.15).move_to([0, 2.05, 0])
        self.at(self.a("d1", "le produit"), Ecrire(cr, rt=1.0)); self.play(Create(enc(cr, col=JAUNE)), run_time=0.4)
        R = [(r"\Delta_r G < 0 \;\Rightarrow\; " + D + r"\xi > 0", r"sens \textbf{direct} $\longrightarrow$", VERT, "d2", "Si delta-r-G est négatif", 0.85),
             (r"\Delta_r G > 0 \;\Rightarrow\; " + D + r"\xi < 0", r"sens \textbf{indirect} $\longleftarrow$", ORANGE, "d3", "Si delta-r-G est positif", 0.05),
             (r"\Delta_r G = 0", r"\textbf{équilibre} chimique", BLEU, "d4", "Et si delta-r-G est nul", -0.75)]
        for fo, tx, col, sid, fr, y in R:
            a = pos(M(fo, sc=0.9, color=col), -5.6, y); b = pos(T(tx, sc=0.75, color=col), 0.6, y)
            self.at(self.a(sid, fr), Ecrire(a, rt=0.9)); self.play(Ecrire(b, rt=0.6))
        p1 = pos(T(r"\textbf{Piège 1} : c'est le signe de $\Delta_r G$, pas celui de $\Delta_r G^\circ$ !", sc=0.72, color=ROUGE), -6.0, -2.0)
        p2 = pos(T(r"\textbf{Piège 2} : possible ne veut pas dire rapide (le diamant !)", sc=0.72, color=ROUGE), -6.0, -2.8)
        self.ecr(self.a("d5", "Attention"), p1, rt=1.5); self.ecr(self.a("d6", "Et piège"), p2, rt=1.5)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"5.3 -- Enthalpie libre de réaction et quotient", "1/4 · Critère d'évolution")
        l1 = pos(M(r"\Delta_r G = \sum_i \nu_i\,\mu_i", sc=0.95), -6.3, 2.15)
        l2 = pos(M(r"\mu_i = \mu_i^\circ + RT\ln a_i", sc=0.95, color=BLEU), 0.8, 2.15)
        self.ecr(self.a("e1", "On part"), l1, rt=1.0); self.ecr(self.a("e2", "On remplace"), l2, rt=1.1)
        l3 = M(r"\Delta_r G \;=\;", r"\sum_i \nu_i\,\mu_i^\circ", r"\;+\;", r"RT\sum_i \nu_i \ln a_i", sc=1.0).move_to([0, 0.75, 0])
        self.at(self.a("e2", "mu i standard"), Ecrire(l3, rt=1.6))
        br1 = Brace(l3[1], DOWN, color=VERT); t1 = M(r"\Delta_r G^\circ", sc=0.8, color=VERT).next_to(br1, DOWN, buff=0.1)
        self.at(self.a("e3", "Le premier morceau"), Create(br1), Ecrire(t1, rt=0.5), run_time=0.6)
        br2 = Brace(l3[3], DOWN, color=ORANGE); t2 = M(r"RT \ln \prod_i a_i^{\,\nu_i} \;=\; RT\ln Q_r", sc=0.8, color=ORANGE).next_to(br2, DOWN, buff=0.1)
        self.at(self.a("e4", "les nu i passent"), Create(br2), Ecrire(t2, rt=1.2), run_time=0.8)
        fi = M(r"\Delta_r G", r"\;=\;", r"\Delta_r G^\circ", r"\;+\;", r"RT\ln Q_r", sc=1.3).move_to([0, -2.4, 0]); fi[2].set_color(VERT); fi[4].set_color(ORANGE)
        self.at(self.a("e5", "delta-r-G égale"), Ecrire(fi, rt=1.3)); self.play(Create(enc(fi, col=JAUNE, buff=0.25)), run_time=0.4)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"5.4 -- Constante d'équilibre", "2/4 · Constante d'équilibre")
        k = pos(M(r"K^\circ(T) = \exp\!\left(-\frac{\Delta_r G^\circ}{RT}\right)", sc=0.95), -6.3, 2.1)
        self.ecr(self.a("f1", "K standard égale"), k, rt=1.4); self.play(Create(enc(k)), run_time=0.4)
        nk = T(r"sans dimension, ne dépend que de $T$", sc=0.6, color=GRIS).next_to(k, RIGHT, buff=0.6)
        self.at(self.t("f2"), FadeIn(nk), run_time=0.4)
        g = pos(M(r"\Delta_r G", r"\;=\;", r"RT\ln\frac{Q_r}{K^\circ}", sc=1.1, color=JAUNE), -6.3, 0.3)
        self.at(self.a("f3", "delta-r-G s'écrit"), Ecrire(g, rt=1.2)); self.play(Create(enc(g, col=JAUNE)), run_time=0.4)
        la = VGroup(pos(T(r"équilibre : $Q_r = K^\circ$", sc=0.75, color=BLEU), 0.6, 0.55), pos(T(r"loi d'action des masses", sc=0.62, color=GRIS), 0.6, 0.0))
        self.ecr(self.a("f4", "À l'équilibre"), la, rt=1.4)
        L = NumberLine(x_range=[0, 10, 1], length=11, include_ticks=False, color=CRAIE, stroke_width=3).move_to([0, -1.9, 0])
        fl = Arrow(L.get_end() + LEFT*0.3, L.get_end() + RIGHT*0.2, color=CRAIE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.5)
        lq = M("Q_r", sc=0.8).next_to(L.get_end(), DOWN, buff=0.25)
        kk = Line(L.n2p(5) + UP*0.25, L.n2p(5) + DOWN*0.25, color=ROUGE, stroke_width=4); lk = M(r"K^\circ", sc=0.8, color=ROUGE).next_to(kk, DOWN, buff=0.15)
        self.at(self.a("f5", "Et hors équilibre"), Create(L), FadeIn(fl), FadeIn(lq), Create(kk), FadeIn(lk), run_time=0.7)
        a1 = Arrow(L.n2p(1.5) + UP*0.5, L.n2p(4.4) + UP*0.5, color=VERT, stroke_width=5, buff=0)
        t1 = T(r"$Q_r < K^\circ$ : sens direct", sc=0.6, color=VERT).next_to(a1, UP, buff=0.12)
        a2 = Arrow(L.n2p(8.5) + UP*0.5, L.n2p(5.6) + UP*0.5, color=ORANGE, stroke_width=5, buff=0)
        t2 = T(r"$Q_r > K^\circ$ : sens indirect", sc=0.6, color=ORANGE).next_to(a2, UP, buff=0.12)
        self.at(self.a("f5", "Si Q r est plus petit"), GrowArrow(a1), FadeIn(t1), run_time=0.6)
        self.at(self.a("f6", "Si Q r est plus grand"), GrowArrow(a2), FadeIn(t2), run_time=0.6)
        self.at(self.a("f6", "Le quotient évolue"), Indicate(kk, color=JAUNE, scale_factor=1.6), run_time=0.7)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"5.4 -- Ce que dit $\Delta_r G^\circ$", "2/4 · Constante d'équilibre")
        s = pos(M(r"\Delta_r G^\circ < 0 \;\Longleftrightarrow\; K^\circ > 1", r"\quad\text{: thermodynamiquement favorisée}", sc=0.85), -6.3, 2.1); s[1].set_color(VERT)
        self.at(self.a("g2", "Si delta-r-G standard"), Ecrire(s[0], rt=1.2)); self.at(self.a("g2", "la réaction est dite"), Ecrire(s[1], rt=1.0))
        L = NumberLine(x_range=[-8, 8, 2], length=11, color=CRAIE, stroke_width=3, include_numbers=False, tick_size=0.06).move_to([0, 0.2, 0])
        lab = M(r"\log K^\circ", sc=0.7).next_to(L.get_end(), RIGHT, buff=0.15)
        z1 = Rectangle(width=L.n2p(-4)[0] - L.n2p(-8)[0], height=0.4, fill_color=ROUGE, fill_opacity=0.35, stroke_width=0).move_to((L.n2p(-8) + L.n2p(-4))/2)
        z3 = Rectangle(width=L.n2p(8)[0] - L.n2p(4)[0], height=0.4, fill_color=VERT, fill_opacity=0.35, stroke_width=0).move_to((L.n2p(4) + L.n2p(8))/2)
        t1 = T(r"quasi nulle", sc=0.6, color=ROUGE).next_to(z1, UP, buff=0.12); t3 = T(r"quasi totale", sc=0.6, color=VERT).next_to(z3, UP, buff=0.12)
        n1 = M(r"-4", sc=0.55, color=GRIS).next_to(L.n2p(-4), DOWN, buff=0.15); n2 = M(r"+4", sc=0.55, color=GRIS).next_to(L.n2p(4), DOWN, buff=0.15)
        n0 = M(r"0", sc=0.55, color=GRIS).next_to(L.n2p(0), DOWN, buff=0.15)
        self.at(self.a("g3", "Quelques repères"), Create(L), FadeIn(lab), FadeIn(n0), run_time=0.6)
        self.at(self.a("g3", "quasi totale"), FadeIn(z3), FadeIn(t3), FadeIn(n2), run_time=0.5)
        self.at(self.a("g3", "En dessous"), FadeIn(z1), FadeIn(t1), FadeIn(n1), run_time=0.5)
        ex = pos(M(r"\mathrm{NH_3},\ 298\ \mathrm{K} :\;\; \Delta_r G^\circ = -32{,}7\ \mathrm{kJ\cdot mol^{-1}}", r"\;\Rightarrow\; K^\circ = 5{,}4\times 10^{5}", sc=0.85), -6.3, -1.45)
        ex[1].set_color(JAUNE)
        pt = Dot(L.n2p(5.73), radius=0.1, color=JAUNE)
        self.at(self.a("g4", "la synthèse"), Ecrire(ex[0], rt=1.4)); self.at(self.a("g4", "donc K standard"), Ecrire(ex[1], rt=0.9), FadeIn(pt, scale=2))
        le = pos(T(r"très favorisée\dots\ mais infiniment lente sans catalyseur", sc=0.72, color=ORANGE), -6.3, -2.5)
        self.ecr(self.t("g5") + 0.1, le, rt=1.5)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"5.4 -- À vous : sens d'évolution", "2/4 · Constante d'équilibre")
        cad = RoundedRectangle(width=12.4, height=1.4, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, 1.7, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.72, color=JAUNE), -5.9, 1.7)
        en = M(r"\mathrm{NH_3},\ 298\ \mathrm{K} :\;\; K^\circ = 5{,}4\times10^5,\quad Q_r = 10^3", r"\qquad\text{sens ?}", sc=0.8).next_to(tq, RIGHT, buff=0.4); en[1].set_color(JAUNE)
        self.at(self.t("h1"), Create(cad), Ecrire(tq, rt=0.4), run_time=0.5)
        self.at(self.a("h1", "a un quotient"), Ecrire(en[0], rt=1.4)); self.at(self.a("h1", "Dans quel sens"), Ecrire(en[1], rt=0.5))
        pa, arc = chrono(5.7, 1.7)
        self.jusqua(self.PH["h1"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("h2") - self.renderer.time - 0.1), rate_func=linear)
        r1 = pos(M(r"Q_r = 10^3 \;<\; K^\circ", r"\;\Longrightarrow\;\text{sens direct : formation de } \mathrm{NH_3}", sc=0.85, color=VERT), -6.0, 0.15)
        self.at(self.a("h2", "Réponse"), FadeOut(pa), FadeOut(arc), Ecrire(r1[0], rt=0.8)); self.at(self.a("h2", "Donc sens direct"), Ecrire(r1[1], rt=1.1))
        r2 = pos(M(r"\Delta_r G = RT\ln\frac{Q_r}{K^\circ} = 2{,}48\times\ln\!\left(\frac{10^3}{5{,}4\times10^5}\right)", r"\;\approx\; -15{,}6\ \mathrm{kJ\cdot mol^{-1}}", sc=0.85), -6.0, -1.3)
        r2[1].set_color(JAUNE)
        self.at(self.a("h3", "on peut même chiffrer"), Ecrire(r2[0], rt=1.6)); self.at(self.a("h3", "soit environ"), Ecrire(r2[1], rt=0.8))
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"5.5 -- La courbe $G(\xi)$", r"3/4 · Courbe $G(\xi)$")
        dat = np.loadtxt("../pdf/data/gxi.dat", skiprows=1)
        ax = Axes(x_range=[0, 1.05, 0.5], y_range=[-3.3, 0.4, 1], x_length=6.0, y_length=4.6, axis_config=AX).move_to([3.3, -0.55, 0])
        lx = M(r"\xi\ (\mathrm{mol})", sc=0.6).next_to(ax.x_axis.get_end(), DOWN, buff=0.12)
        ly = M(r"G - G(0)\ (\mathrm{kJ})", sc=0.6).next_to(ax.y_axis.get_end(), RIGHT, buff=0.12)
        self.at(self.a("i1", "Traçons"), Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.6)
        ex = pos(M(r"\mathrm{A(g)} = \mathrm{B(g)}", sc=0.85), -6.4, 2.1)
        ex2 = pos(M(r"\Delta_r G^\circ = -2\ \mathrm{kJ\cdot mol^{-1}}", sc=0.8), -6.4, 1.45)
        self.at(self.a("i2", "une isomérisation"), Ecrire(ex, rt=0.7)); self.at(self.a("i2", "avec delta-r-G"), Ecrire(ex2, rt=0.9))
        lin = DashedLine(ax.c2p(0, 0), ax.c2p(1, -2), color=GRIS, stroke_width=2.5)
        tl = T(r"sans mélange", sc=0.55, color=GRIS).move_to(ax.c2p(0.62, -0.75))
        pts = [ax.c2p(x, g) for x, g in dat[::4, :2]] + [ax.c2p(dat[-1, 0], dat[-1, 1])]
        cb = VMobject(color=BLEU, stroke_width=4).set_points_smoothly(pts)
        self.at(self.a("i3", "Sans mélange"), Create(lin), FadeIn(tl), run_time=0.6)
        self.at(self.a("i3", "la courbe se creuse"), Create(cb), run_time=1.0)
        G = lambda x: x*-2 + 2.4776*((1-x)*np.log(1-x) + x*np.log(x))
        dG = lambda x: -2 + 2.4776*np.log(x/(1-x))
        def tang(x0, w, col): return Line(ax.c2p(x0-w, G(x0)-w*dG(x0)), ax.c2p(x0+w, G(x0)+w*dG(x0)), color=col, stroke_width=5)
        t1, t2 = tang(0.3, 0.13, VERT), tang(0.9, 0.08, ORANGE)
        p = pos(T(r"pente $= \Delta_r G$", sc=0.72, color=JAUNE), -6.4, 0.5)
        self.at(self.a("i4", "Sa pente"), Ecrire(p, rt=0.6))
        self.at(self.a("i4", "À gauche"), Create(t1), run_time=0.5); self.at(self.a("i4", "À droite"), Create(t2), run_time=0.5)
        pe = Dot(ax.c2p(0.691, G(0.691)), radius=0.1, color=ROUGE); vl = DashedLine(ax.c2p(0.691, -3.3), ax.c2p(0.691, G(0.691)), color=ROUGE, stroke_width=2)
        te = pos(M(r"\xi_{\text{éq}} = 0{,}69\ \mathrm{mol}", sc=0.8, color=ROUGE), -6.4, -0.4)
        self.at(self.a("i5", "le minimum"), FadeIn(pe, scale=2), Create(vl), run_time=0.5); self.play(Ecrire(te, rt=0.7))
        mi = pos(T(r"minimum \textbf{à l'intérieur} :", sc=0.68, color=ORANGE), -6.4, -1.5)
        mi2 = pos(T(r"jamais rigoureusement total", sc=0.68, color=ORANGE), -6.4, -2.05)
        self.at(self.a("i6", "le minimum est à l'intérieur"), Ecrire(mi, rt=0.8)); self.at(self.a("i6", "un équilibre"), Ecrire(mi2, rt=0.8))
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"5.6 -- Équilibre ou transformation totale ?", "4/4 · État final")
        E = boite(VGroup(T(r"\textbf{Équilibre}", sc=0.75, color=VERT), T(r"tous les constituants présents", sc=0.6), M(r"Q_r = K^\circ,\quad \Delta_r G = 0", sc=0.75)).arrange(DOWN, buff=0.15), VERT, VERT, w=5.6, h=2.0).move_to([-3.2, 1.25, 0])
        F = boite(VGroup(T(r"\textbf{Transformation totale}", sc=0.75, color=ORANGE), T(r"un réactif épuisé : $\xi = \xi_{\max}$", sc=0.6), M(r"\Delta_r G < 0 \text{ : arrêt hors équilibre}", sc=0.7)).arrange(DOWN, buff=0.15), ORANGE, ORANGE, w=5.6, h=2.0).move_to([3.2, 1.25, 0])
        self.at(self.a("j2", "Soit l'équilibre"), FadeIn(E, shift=UP*0.2), run_time=0.7)
        self.at(self.a("j3", "Soit un réactif"), FadeIn(F, shift=UP*0.2), run_time=0.7)
        ru = T(r"solide pur épuisé : \textbf{rupture d'équilibre}", sc=0.65, color=ROUGE).next_to(F, DOWN, buff=0.2)
        self.ecr(self.a("j4", "si le réactif épuisé"), ru, rt=1.2)
        st = [r"supposer l'équilibre : $\xi_{\text{éq}}$", r"vérifier : $\xi_{\text{éq}} \leq \xi_{\max}$ ?", r"sinon : transformation totale"]
        bx = [boite(T(s, sc=0.55), JAUNE, JAUNE, w=3.85, h=0.85).move_to([-4.45 + 4.45*k, -2.3, 0]) for k, s in enumerate(st)]
        ar = [Arrow(bx[k].get_right(), bx[k+1].get_left(), color=JAUNE, buff=0.08, stroke_width=3, max_tip_length_to_length_ratio=0.3) for k in range(2)]
        tm = T(r"\textbf{La méthode}", sc=0.65, color=JAUNE).move_to([-4.45, -1.5, 0])
        self.at(self.a("j5", "La méthode"), FadeIn(tm), FadeIn(bx[0]), run_time=0.5)
        self.at(self.a("j5", "puis on vérifie"), GrowArrow(ar[0]), FadeIn(bx[1]), run_time=0.5)
        self.at(self.a("j5", "Sinon"), GrowArrow(ar[1]), FadeIn(bx[2]), run_time=0.5)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"5.6 -- Exemple : le calcaire en enceinte fermée", "4/4 · État final")
        eq = pos(M(ch("CaCO_3(s)") + " = " + ch("CaO(s)") + " + " + ch("CO_2(g)"), r"\qquad T = 1100\ \mathrm{K},\ V = 10\ \mathrm{L}", sc=0.8), -6.4, 2.15); eq[1].set_color(GRIS)
        self.at(self.a("k1", "on chauffe"), Ecrire(eq[1], rt=0.8)); self.at(self.a("k1", "Il se décompose"), Ecrire(eq[0], rt=1.2))
        k = pos(M(r"K^\circ = \frac{P_{\mathrm{CO_2}}}{P^\circ} = 0{,}722", sc=0.8), -6.4, 1.15)
        self.ecr(self.a("k2", "K standard vaut"), k, rt=1.1)
        pk = pos(M(r"\Rightarrow\; P_{\text{éq}} = 0{,}722\ \mathrm{bar}", sc=0.75, color=BLEU), -6.4, 0.45)
        self.ecr(self.a("k2", "à l'équilibre"), pk, rt=0.9)
        xe = pos(M(r"\xi_{\text{éq}} = \frac{P_{\text{éq}}V}{RT} = 78{,}9\ \mathrm{mmol}", sc=0.8, color=JAUNE), -6.4, -0.45)
        dat = np.loadtxt("../pdf/data/caco3.dat", skiprows=1)
        ax = Axes(x_range=[0, 155, 50], y_range=[0, 0.92, 0.5], x_length=5.0, y_length=3.6, axis_config=AX).move_to([3.9, -0.45, 0])
        lx = M(r"n_0\ (\mathrm{mmol})", sc=0.55).next_to(ax.x_axis.get_end(), DOWN, buff=0.12)
        ly = M(r"P_{\mathrm{CO_2}}\ (\mathrm{bar})", sc=0.55).next_to(ax.y_axis.get_end(), RIGHT, buff=0.12)
        cb = VMobject(color=BLEU, stroke_width=4).set_points_as_corners([ax.c2p(n, p) for n, p in dat if n <= 150])
        self.at(self.a("k3", "Pour atteindre"), Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.5); self.play(Create(cb), run_time=0.8)
        self.ecr(self.a("k3", "il faut former"), xe, rt=1.2)
        v1 = Dot(ax.c2p(100, 0.722), radius=0.09, color=VERT)
        a1 = pos(T(r"$n_0 = 100$ mmol : \textbf{équilibre}, il reste du calcaire", sc=0.65, color=VERT), -6.4, -1.6)
        self.at(self.a("k4", "Avec cent"), FadeIn(v1, scale=2), Ecrire(a1, rt=1.3))
        v2 = Dot(ax.c2p(50, 0.457), radius=0.09, color=ORANGE)
        a2 = pos(T(r"$n_0 = 50$ mmol : tout disparaît, \textbf{rupture d'équilibre}", sc=0.65, color=ORANGE), -6.4, -2.4)
        self.at(self.a("k5", "Mais avec cinquante"), FadeIn(v2, scale=2), run_time=0.4); self.at(self.a("k5", "Tout le calcaire"), Ecrire(a2, rt=1.3))
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, M(r"T,\,P \text{ fixées : } " + D + r"G \leq 0 \qquad \text{sens d'évolution} = \text{signe de } \Delta_r G", sc=0.8), "l2", 1.9),
                (VERT, M(r"\Delta_r G = RT\ln\frac{Q_r}{K^\circ} \qquad K^\circ = \exp\!\left(-\frac{\Delta_r G^\circ}{RT}\right)", sc=0.8), "l3", 0.5),
                (ORANGE, VGroup(T(r"État final : équilibre ($Q_r = K^\circ$) ou transformation totale.", sc=0.72), T(r"On suppose, puis on vérifie !", sc=0.72, color=ORANGE)).arrange(DOWN, aligned_edge=LEFT, buff=0.2), "l4", -1.1)]
        for k, (col, F, sid, y) in enumerate(data):
            c = carte(k+1, col, -5.9, y); pos(F, -5.3, y)
            self.at(self.t(sid), Create(c[0]), FadeIn(c[1]), run_time=0.4); self.play(Ecrire(F, rt=1.8))
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- L'équilibre de Boudouard", "Exercice résolu")
        eq = M(r"\mathrm{C(graphite)}", r" + ", ch("CO_2(g)"), r" = ", r"2\," + ch("CO(g)"), sc=1.05).move_to([0, 2.05, 0])
        self.at(self.a("m2", "Le carbone"), Ecrire(eq, rt=1.4))
        co = pos(T(r"$1$ mol de $\mathrm{CO_2}$ + graphite en excès, \quad $T = 1\,000$ K, \quad $P = 1$ bar", sc=0.75, color=BLEU), -6.4, 1.15)
        self.ecr(self.a("m3", "On place"), co, rt=1.6)
        d1 = pos(M(r"\Delta_f H^\circ\ (\mathrm{kJ\cdot mol^{-1}}) :\quad \mathrm{CO}\ -110{,}5 \qquad \mathrm{CO_2}\ -393{,}5", sc=0.75, color=GRIS), -6.4, 0.3)
        d2 = pos(M(r"S^\circ_m\ (\mathrm{J\cdot K^{-1}\cdot mol^{-1}}) :\quad \mathrm{C}\ 5{,}7 \qquad \mathrm{CO}\ 197{,}7 \qquad \mathrm{CO_2}\ 213{,}8", sc=0.75, color=GRIS), -6.4, -0.35)
        q = M(r"\text{Composition à l'équilibre ?}", sc=1.0, color=JAUNE).move_to([0, -1.35, 0])
        self.at(self.a("m4", "Question"), Ecrire(q, rt=1.0)); self.play(Create(enc(q, col=JAUNE)), run_time=0.4)
        self.at(self.a("m4", "On dispose"), FadeIn(d1), FadeIn(d2), run_time=0.6)
        ch_ = M(r"\text{composition}", r"\;\Longleftarrow\;", r"K^\circ", r"\;\Longleftarrow\;", r"\Delta_r G^\circ", r"\;\Longleftarrow\;", r"\text{tables}", sc=0.9, color=VERT).move_to([0, -2.75, 0])
        self.at(self.a("m5", "Pour une composition"), Ecrire(VGroup(ch_[0], ch_[1], ch_[2]), rt=0.9))
        self.at(self.a("m5", "Et pour K standard"), Ecrire(VGroup(ch_[3], ch_[4]), rt=0.7))
        self.at(self.a("m5", "On commence donc"), Ecrire(VGroup(ch_[5], ch_[6]), rt=0.7))
        self.fin()

class S13(Cours):
    sid = "S13"
    def construct(self):
        self.entete(r"Exercice résolu -- La solution, étape par étape", "Exercice résolu")
        c1 = carte(1, BLEU, -6.1, 2.2)
        s1 = pos(M(r"\Delta_r H^\circ = 2(-110{,}5) + 393{,}5 = +172{,}5\ \mathrm{kJ\cdot mol^{-1}}", sc=0.72), -5.55, 2.2)
        s1b = pos(M(r"\Delta_r S^\circ = 2(197{,}7) - 213{,}8 - 5{,}7 = +175{,}9\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}", sc=0.72), -5.55, 1.6)
        self.at(self.t("n1"), Create(c1[0]), FadeIn(c1[1]), run_time=0.4); self.at(self.a("n1", "la loi de Hess"), Ecrire(s1, rt=1.4))
        self.at(self.a("n2", "Et delta-r-S"), Ecrire(s1b, rt=1.4))
        c2 = carte(2, VERT, -6.1, 0.85)
        s2 = pos(M(r"\Delta_r G^\circ(1000) = -3{,}4\ \mathrm{kJ\cdot mol^{-1}}", r"\;\Rightarrow\; K^\circ = e^{3400/(8{,}314\times 1000)} = 1{,}50", sc=0.72), -5.55, 0.85)
        s2[1].set_color(VERT)
        self.at(self.t("n3"), Create(c2[0]), FadeIn(c2[1]), run_time=0.4); self.at(self.a("n3", "À mille kelvins"), Ecrire(s2[0], rt=1.1))
        self.at(self.a("n3", "donc K standard"), Ecrire(s2[1], rt=1.1))
        c3 = carte(3, ORANGE, -6.1, 0.05)
        s3 = pos(M(r"\mathrm{CO_2} : 1-\xi \qquad \mathrm{CO} : 2\xi \qquad \text{gaz : } 1+\xi", sc=0.72), -5.55, 0.05)
        s3b = pos(M(r"a(\mathrm{C}) = 1", sc=0.72, color=ORANGE), 2.2, 0.05)
        self.at(self.t("n4"), Create(c3[0]), FadeIn(c3[1]), run_time=0.4); self.at(self.a("n4", "Il reste"), Ecrire(s3, rt=1.6))
        self.at(self.a("n5", "Le graphite"), Ecrire(s3b, rt=0.6))
        c4 = carte(4, ROUGE, -6.1, -0.85)
        s4 = pos(M(r"Q_r = \frac{(2\xi)^2}{(1-\xi)(1+\xi)}\,\frac{P}{P^\circ} = \frac{4\xi^2}{1-\xi^2}", r"\;=\; 1{,}50", sc=0.72), -5.55, -0.85)
        self.at(self.t("n6"), Create(c4[0]), FadeIn(c4[1]), run_time=0.4); self.at(self.a("n6", "Le quotient vaut"), Ecrire(s4[0], rt=1.4))
        self.at(self.a("n6", "il doit égaler"), Ecrire(s4[1], rt=0.5))
        r = M(r"\xi = 0{,}52\ \mathrm{mol}", sc=0.9, color=JAUNE).move_to([3.8, -0.85, 0])
        self.at(self.a("n7", "On résout"), Ecrire(r, rt=0.7)); self.play(Create(enc(r, col=JAUNE, buff=0.15)), run_time=0.3)
        co = pos(M(r"\mathrm{CO_2} : 0{,}48\ \mathrm{mol} \qquad \mathrm{CO} : 1{,}05\ \mathrm{mol}", sc=0.78, color=JAUNE), -5.55, -1.7)
        self.at(self.a("n7", "Il reste"), Ecrire(co, rt=1.2))
        c5 = carte(5, VERT, -6.1, -2.55)
        s5 = pos(T(r"Vérifier : $\xi < \xi_{\max} = 1$ \;$\checkmark$ \quad le gaz contient $69\,\%$ de $\mathrm{CO}$", sc=0.7), -5.55, -2.55)
        self.at(self.t("n8"), Create(c5[0]), FadeIn(c5[1]), run_time=0.4); self.at(self.a("n8", "Ksi est bien"), Ecrire(s5, rt=1.8))
        hf = pos(T(r"$\mathrm{CO}$ : le réducteur du minerai de fer", sc=0.6, color=GRIS), -5.55, -3.3)
        self.at(self.t("n9"), FadeIn(hf), run_time=0.5)
        self.jusqua(self.t("n10") - 0.2)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        nx = T(r"Chapitre 6 \;$\longrightarrow$\; déplacer un équilibre : $T$, $P$, composition", sc=0.85, color=JAUNE).move_to([0, 0.3, 0])
        self.ecr(self.a("n10", "déplacer un équilibre"), nx, rt=1.8)
        self.fin()
