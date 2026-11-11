from base import *

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"THERMOCHIMIE \;·\; PT*", sc=0.55, color=GRIS).move_to([0, 2.9, 0])
        ti = T(r"\textbf{Chapitre 1}", sc=1.3, color=JAUNE).move_to([0, 2.1, 0])
        st = T(r"Rappels de première année", sc=1.0).move_to([0, 1.3, 0])
        tr = Line([-3.2, 0.8, 0], [3.2, 0.8, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), run_time=0.7)
        self.at(self.a("a1", "Bienvenue"), Ecrire(st, rt=0.9), Create(tr))
        items = []
        for k, (txt, col) in enumerate([(r"L'avancement $\xi$ d'une réaction", BLEU),
                                        (r"L'activité $a_i$ et le quotient de réaction $Q_r$", VERT),
                                        (r"L'oxydoréduction et la formule de Nernst", ORANGE)]):
            c = Circle(radius=0.27, color=col, stroke_width=3).move_to([-4.3, -0.2 - 1.0*k, 0])
            n = T(r"\textbf{%d}" % (k+1), sc=0.75, color=col).move_to(c)
            tx = pos(T(txt, sc=0.85), -3.7, -0.2 - 1.0*k)
            items.append(VGroup(c, n, tx))
        for it, fr in zip(items, ["Un :", "Deux :", "Trois :"]):
            self.jusqua(self.a("a3", fr))
            self.play(Create(it[0]), FadeIn(it[1]), run_time=0.35); self.play(Ecrire(it[2], rt=0.9))
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.25) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete("1.1 -- Système, constituant, phase", "1/3 · Avancement")
        l1 = pos(T(r"\textbf{Système physico-chimique} : des espèces réparties en une ou plusieurs phases"), -6.4, 2.3)
        self.ecr(self.a("b1", "un système"), l1, rt=2.0)
        l2 = pos(T(r"\textbf{Constituant}", r" = espèce chimique + état physique", color=BLEU), -6.4, 1.35)
        self.ecr(self.a("b2", "le constituant"), l2, rt=1.6)
        ex = pos(M(ch("H_2O(l)"), r"\;\neq\;", ch("H_2O(g)"), sc=0.9), -5.9, 0.55)
        note = T(r"deux constituants différents", sc=0.6, color=GRIS).next_to(ex, RIGHT, buff=0.5)
        self.at(self.a("b3", "l'eau liquide"), Ecrire(ex[0], rt=0.6))
        self.at(self.a("b3", "la vapeur"), Ecrire(ex[2], rt=0.6))
        self.at(self.a("b3", "deux constituants"), FadeIn(ex[1], scale=1.5), FadeIn(note), run_time=0.5)
        l3 = pos(T(r"\textbf{Phase}", r" : région où les grandeurs intensives varient continûment", color=VERT), -6.4, -0.45)
        self.ecr(self.a("b4", "la phase"), l3, rt=2.0)
        # dessins
        rng = np.random.default_rng(3)
        bg = RoundedRectangle(width=3.0, height=1.7, corner_radius=0.12, color=CRAIE, stroke_width=2).move_to([-3.6, -2.1, 0])
        pts = VGroup(*[Dot([-3.6 + rng.uniform(-1.3, 1.3), -2.1 + rng.uniform(-0.65, 0.65), 0], radius=0.055,
                           color=(BLEU if k % 2 else ORANGE)) for k in range(46)])
        lg = T(r"mélange de gaz : ", r"\textbf{1 phase}", sc=0.6).next_to(bg, DOWN, buff=0.2)
        s1 = Rectangle(width=1.35, height=1.2, color=BLEU, fill_color=BLEU, fill_opacity=0.35, stroke_width=2).move_to([2.6, -2.25, 0])
        s2 = Rectangle(width=1.35, height=1.2, color=ORANGE, fill_color=ORANGE, fill_opacity=0.35, stroke_width=2).move_to([4.1, -2.25, 0])
        ls = T(r"deux solides : ", r"\textbf{2 phases}", sc=0.6).next_to(VGroup(s1, s2), DOWN, buff=0.2).set_y(lg.get_y())
        self.at(self.a("b5", "Un mélange"), Create(bg), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in pts], lag_ratio=0.03, run_time=1.0)); self.play(Ecrire(lg, rt=0.7))
        self.at(self.a("b5", "En revanche"), FadeIn(s1, shift=RIGHT*0.2), FadeIn(s2, shift=LEFT*0.2), run_time=0.6)
        self.play(Ecrire(ls, rt=0.7))
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete("1.1 -- Équation de réaction", "1/3 · Avancement")
        eq = M(ch("N_2(g)"), "+", r"3\," + ch("H_2(g)"), "=", r"2\," + ch("NH_3(g)"), sc=1.15).move_to([0, 1.9, 0])
        self.ecr(self.a("c1", "la synthèse"), eq, rt=1.6)
        gen = M(r"0 \;=\; \sum_i \nu_i\,\mathrm{A}_i", sc=1.15).move_to([-3.0, -1.0, 0])
        self.ecr(self.a("c2", "zéro, égale"), gen, rt=1.6)
        leg = VGroup(M(r"\nu_i > 0", r"\;:\;\text{produit}", color=VERT), M(r"\nu_i < 0", r"\;:\;\text{réactif}", color=ORANGE)).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        pos(leg, 1.2, -1.0)
        self.at(self.a("c3", "positifs"), Ecrire(leg[0], rt=0.8))
        self.at(self.a("c3", "négatifs"), Ecrire(leg[1], rt=0.8))
        nus = [M(r"\nu = -1", color=ORANGE, sc=0.8).next_to(eq[0], DOWN, buff=0.45),
               M(r"\nu = -3", color=ORANGE, sc=0.8).next_to(eq[2], DOWN, buff=0.45),
               M(r"\nu = +2", color=VERT, sc=0.8).next_to(eq[4], DOWN, buff=0.45)]
        for n, fr, e in zip(nus, ["moins un", "moins trois", "plus deux"], [eq[0], eq[2], eq[4]]):
            self.at(self.a("c4", fr), Ecrire(n, rt=0.5), e.animate.set_color(n.get_color()), run_time=0.6)
        self.at(self.t("c5"), Create(SurroundingRectangle(gen, color=JAUNE, buff=0.25, corner_radius=0.08)), run_time=0.8)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"1.1 -- Avancement $\xi$", "1/3 · Avancement")
        l1 = pos(T(r"\textbf{Avancement} $\xi$ (en mol)", color=BLEU, sc=0.8), -6.4, 2.35)
        self.ecr(self.a("d1", "l'avancement"), l1, rt=1.0)
        f = M(r"n_i(\xi) \;=\; n_{i,0} \;+\; \nu_i\,\xi", sc=1.05).move_to([2.6, 2.3, 0])
        self.ecr(self.a("d2", "la quantité de chaque"), f, rt=2.2)
        self.play(Create(SurroundingRectangle(f, color=ROUGE, buff=0.2, corner_radius=0.08)), run_time=0.5)
        # tableau
        X = [-5.9, -1.7, 1.1, 3.9]; Y = [0.85, -0.05, -0.95]
        head = [M(ch("N_2(g)")), M(r"3\," + ch("H_2(g)")), M(r"2\," + ch("NH_3(g)"))]
        ops = [M("+").move_to([(X[1]+X[2])/2, Y[0], 0]), M("=").move_to([(X[2]+X[3])/2, Y[0], 0])]
        for m, x in zip(head, X[1:]): m.move_to([x, Y[0], 0])
        lab = [pos(T("état initial", sc=0.65, color=GRIS), X[0], Y[1]), pos(T(r"avancement $\xi$", sc=0.65, color=GRIS), X[0], Y[2])]
        r1 = [M(v).move_to([x, Y[1], 0]) for v, x in zip(["1", "3", "0"], X[1:])]
        r2 = [M(v).move_to([x, Y[2], 0]) for v, x in zip([r"1 - \xi", r"3 - 3\,\xi", r"2\,\xi"], X[1:])]
        hl = Line([X[0]-0.1, (Y[0]+Y[1])/2, 0], [5.2, (Y[0]+Y[1])/2, 0], color=CRAIE, stroke_width=1.5)
        vl = Line([-3.35, Y[0]+0.4, 0], [-3.35, Y[2]-0.4, 0], color=CRAIE, stroke_width=1.5)
        self.at(self.a("d3", "un tableau"), Ecrire(VGroup(*head, *ops), rt=1.0), Create(hl), Create(vl), run_time=1.1)
        self.at(self.a("d3", "On part"), FadeIn(lab[0]), run_time=0.3)
        self.at(self.a("d3", "une mole"), Ecrire(r1[0], rt=0.4))
        self.at(self.a("d3", "trois moles"), Ecrire(r1[1], rt=0.4), Ecrire(r1[2], rt=0.4))
        self.at(self.t("d4"), FadeIn(lab[1]), run_time=0.3)
        for m, fr in zip(r2, ["un moins ksi", "trois moins trois", "deux ksi"]):
            self.at(self.a("d4", fr), Ecrire(m, rt=0.6))
        self.at(self.a("d5", "On retrouve"), *[Indicate(m, color=JAUNE, scale_factor=1.25) for m in r2], run_time=1.2)
        l6 = pos(M(r"\xi_{\max}", r"\;=\; 1\ \mathrm{mol}", color=ROUGE, sc=0.9), -5.9, -2.2)
        n6 = pos(T("(épuisement du réactif limitant)", sc=0.55, color=GRIS), -5.9, -2.85)
        self.at(self.a("d6", "l'épuisement"), FadeIn(n6), run_time=0.4)
        self.ecr(self.a("d6", "ksi max"), l6, rt=0.8)
        l7 = VGroup(M(r"\xi > 0 \;:\; \text{sens direct}", color=VERT, sc=0.8), M(r"\xi < 0 \;:\; \text{sens indirect}", color=ORANGE, sc=0.8)).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        pos(l7, 1.0, -2.5)
        self.at(self.a("d7", "Positif"), Ecrire(l7[0], rt=0.8))
        self.at(self.a("d7", "négatif"), Ecrire(l7[1], rt=0.8))
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"1.2 -- Activité $a_i$", "2/3 · Activité et quotient")
        l1 = pos(T(r"\textbf{Activité} : nombre sans dimension, « poids » du constituant dans le mélange", color=BLEU), -6.4, 2.35)
        self.ecr(self.a("e1", "C'est un nombre"), l1, rt=2.0)
        rows = [("gaz parfait", r"a_i = \dfrac{P_i}{P^\circ}", r"P^\circ = 1\ \mathrm{bar}", "e3", "sa pression"),
                ("soluté dilué", r"a_i = \dfrac{c_i}{c^\circ}", r"c^\circ = 1\ \mathrm{mol\cdot L^{-1}}", "e4", "sa concentration"),
                ("solvant (eau)", r"a = 1", "", "e5", "l'activité"),
                ("solide ou liquide pur", r"a = 1", "", "e6", "l'activité")]
        Y = [1.25, 0.1, -0.95, -1.8]
        sep = Line([-1.6, 1.85, 0], [-1.6, -2.2, 0], color=CRAIE, stroke_width=1.5)
        self.at(self.t("e2"), Create(sep), run_time=0.6)
        for (lab, fo, std, sid, fr), y in zip(rows, Y):
            L = pos(T(lab, sc=0.8), -5.6, y); F = pos(M(fo, sc=0.95), -0.9, y)
            self.at(self.t(sid), Ecrire(L, rt=0.6))
            self.at(self.a(sid, fr), Ecrire(F, rt=0.7))
            if std:
                S = pos(M(std, sc=0.7, color=GRIS), 2.4, y)
                self.at(self.a(sid, "standard"), FadeIn(S, shift=LEFT*0.2), run_time=0.4)
        n = pos(T(r"$\Rightarrow$ les solides n'apparaissent jamais dans une constante d'équilibre", color=ROUGE, sc=0.75), -5.6, -3.0)
        self.ecr(self.a("e7", "les solides"), n, rt=1.6)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"1.2 -- Quotient de réaction $Q_r$", "2/3 · Activité et quotient")
        q = pos(M(r"Q_r \;=\; \prod_i a_i^{\,\nu_i}", sc=1.1), -5.6, 2.0)
        self.ecr(self.a("f2", "le produit"), q, rt=1.3)
        box = SurroundingRectangle(q, color=ROUGE, buff=0.2, corner_radius=0.08)
        self.play(Create(box), run_time=0.4)
        fr = M(r"=\;\dfrac{\text{activités des produits}}{\text{activités des réactifs}}", sc=0.85).next_to(box, RIGHT, buff=0.4)
        self.at(self.a("f3", "les produits au numérateur"), Ecrire(fr, rt=1.6))
        ex = pos(M(r"\mathrm{NH_3} :\quad Q_r = \dfrac{\left(P_{\mathrm{NH_3}}/P^\circ\right)^{2}}{\left(P_{\mathrm{N_2}}/P^\circ\right)\left(P_{\mathrm{H_2}}/P^\circ\right)^{3}}", sc=0.9), -5.6, 0.25)
        self.ecr(self.a("f4", "l'activité de l'ammoniac"), ex, rt=2.4)
        warn = T(r"ne pas oublier $P^\circ$ !", sc=0.65, color=ROUGE).next_to(ex, RIGHT, buff=0.6)
        self.at(self.a("f4", "Erreur classique"), FadeIn(warn, shift=LEFT*0.2), run_time=0.4)
        # quiz
        cad = RoundedRectangle(width=12.2, height=1.75, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, -1.75, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.75, color=JAUNE), -5.7, -1.3)
        eq = pos(M(ch("CaCO_3(s)"), "=", ch("CaO(s)"), "+", ch("CO_2(g)"), sc=0.9), -5.7, -2.05)
        qq = M(r"Q_r \;=\;", r"\;?", sc=1.0).move_to([2.9, -2.05, 0]); qq[1].set_color(JAUNE)
        self.at(self.t("f5"), Create(cad), Ecrire(tq, rt=0.5), run_time=0.6)
        self.at(self.a("f5", "le quotient"), Ecrire(eq, rt=1.2)); self.play(Ecrire(qq, rt=0.5))
        fin5 = self.PH["f5"]["fin"]; t6 = self.t("f6")
        pa = VGroup(Rectangle(width=0.1, height=0.34), Rectangle(width=0.1, height=0.34)).arrange(RIGHT, buff=0.09).set_fill(JAUNE, 1).set_stroke(width=0).move_to([5.2, -1.3, 0])
        arc = Circle(radius=0.34, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
        self.jusqua(fin5); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, t6 - self.renderer.time - 0.1), rate_func=linear)
        self.at(self.a("f6", "les deux solides"), eq[0].animate.set_opacity(0.35), eq[2].animate.set_opacity(0.35), FadeOut(pa), FadeOut(arc), run_time=0.6)
        rep = M(r"\dfrac{P_{\mathrm{CO_2}}}{P^\circ}", sc=1.0, color=VERT).next_to(qq[0], RIGHT, buff=0.2)
        self.at(self.a("f6", "Il ne reste"), FadeOut(qq[1]), eq[4].animate.set_color(VERT), run_time=0.4)
        self.play(Ecrire(rep, rt=0.8))
        n = pos(T(r"$Q_r$ dépend de l'état du système : il évolue pendant la transformation", sc=0.7, color=BLEU), -5.7, -3.3)
        self.ecr(self.a("f7", "dépend"), n, rt=1.6)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"1.2 -- Constante d'équilibre et critère d'évolution", "2/3 · Activité et quotient")
        l1 = pos(T(r"\textbf{Constante d'équilibre} $K^\circ(T)$ : ne dépend que de la température", color=BLEU), -6.4, 2.35)
        self.ecr(self.a("g1", "la constante"), l1, rt=1.8)
        lam = M(r"Q_{r,\text{éq}} \;=\; K^\circ(T)", sc=1.1).move_to([-2.6, 1.25, 0])
        nom = T("loi d'action des masses", sc=0.65, color=GRIS).next_to(lam, RIGHT, buff=0.9)
        self.ecr(self.t("g2") + 0.3, lam, rt=1.2)
        self.play(Create(SurroundingRectangle(lam, color=ROUGE, buff=0.2, corner_radius=0.08)), run_time=0.4)
        self.at(self.a("g2", "C'est la loi"), FadeIn(nom, shift=LEFT*0.2), run_time=0.4)
        y = -1.2
        ax = Arrow([-5.6, y, 0], [5.9, y, 0], color=CRAIE, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.02)
        lq = M("Q_r", sc=0.8).next_to(ax.get_end(), DOWN, buff=0.2)
        tick = Line([0, y-0.22, 0], [0, y+0.22, 0], color=ROUGE, stroke_width=5)
        lk = M(r"K^\circ", sc=0.9, color=ROUGE).next_to(tick, DOWN, buff=0.15)
        self.at(self.a("g3", "Plaçons"), GrowArrow(ax), FadeIn(lq), run_time=0.7); self.play(Create(tick), Ecrire(lk, rt=0.4), run_time=0.5)
        d1 = Dot([-3.9, y, 0], color=VERT, radius=0.11); t1 = M(r"Q_r < K^\circ", color=VERT, sc=0.85).move_to([-3.0, y+1.05, 0])
        s1 = T("sens direct", color=VERT, sc=0.7).next_to(t1, RIGHT, buff=0.25)
        self.at(self.t("g4"), FadeIn(d1, scale=2), Ecrire(t1, rt=0.6), run_time=0.7)
        self.at(self.a("g4", "le système"), FadeIn(s1), run_time=0.3)
        self.at(self.a("g4", "augmente"), d1.animate.move_to([-0.12, y, 0]), run_time=2.0, rate_func=smooth)
        d2 = Dot([3.9, y, 0], color=ORANGE, radius=0.11); t2 = M(r"Q_r > K^\circ", color=ORANGE, sc=0.85).move_to([2.2, y+1.05, 0])
        s2 = T("sens indirect", color=ORANGE, sc=0.7).next_to(t2, RIGHT, buff=0.25)
        self.at(self.t("g5"), FadeIn(d2, scale=2), Ecrire(t2, rt=0.6), run_time=0.7)
        self.at(self.a("g5", "le système"), FadeIn(s2), d2.animate.move_to([0.12, y, 0]), run_time=1.8, rate_func=smooth)
        n1 = pos(T(r"PTSI : critère \textit{admis}", sc=0.7, color=GRIS), -5.6, -3.0)
        n2 = T(r"$\longrightarrow$ \; PT : critère \textbf{démontré} (2\textsuperscript{e} principe), $K^\circ$ \textbf{calculée}", sc=0.7, color=JAUNE).next_to(n1, RIGHT, buff=0.35)
        self.ecr(self.t("g6"), n1, rt=0.8)
        self.ecr(self.a("g6", "Cette année"), n2, rt=1.6)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete("1.3 -- Oxydants et réducteurs", "3/3 · Oxydoréduction")
        o = pos(T(r"\textbf{Oxydant}", r" : capte des électrons", color=ORANGE, sc=0.85), -5.6, 2.1)
        r = pos(T(r"\textbf{Réducteur}", r" : cède des électrons", color=BLEU, sc=0.85), -5.6, 1.3)
        self.ecr(self.t("h2"), o, rt=1.0); self.ecr(self.a("h2", "Un réducteur"), r, rt=1.0)
        de = M(r"\alpha\,\mathrm{Ox}", r"\;+\;", r"\gamma", r"\,e^-", r"\;=\;", r"\beta\,\mathrm{Red}", sc=1.25).move_to([0, 0.0, 0])
        de[0].set_color(ORANGE); de[5].set_color(BLEU)
        self.ecr(self.a("h3", "une demi-équation"), de, rt=1.4)
        bx = SurroundingRectangle(de, color=ROUGE, buff=0.28, corner_radius=0.08); self.play(Create(bx), run_time=0.4)
        g = T(r"$\gamma$ : nombre d'électrons échangés", sc=0.7, color=JAUNE).next_to(bx, DOWN, buff=0.3)
        self.at(self.a("h3", "Le nombre"), de[2].animate.set_color(JAUNE), FadeIn(g, shift=DOWN*0.2), run_time=0.5)
        ex = M(ch("Cu^{2+}"), "+", r"2\,e^-", "=", ch("Cu(s)"), sc=1.0).move_to([-0.6, -2.6, 0])
        ex[0].set_color(ORANGE); ex[4].set_color(BLEU)
        eg = T(r"$\gamma = 2$", sc=0.75, color=JAUNE).next_to(ex, RIGHT, buff=0.8)
        self.at(self.a("h3b", "l'ion cuivre"), Ecrire(ex[0], rt=0.5))
        self.at(self.a("h3b", "capte deux"), Ecrire(VGroup(ex[1], ex[2]), rt=0.5), FadeIn(eg))
        self.at(self.a("h3b", "et donne"), Ecrire(VGroup(ex[3], ex[4]), rt=0.6))
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete("1.3 -- Nombre d'oxydation (n.o.)", "3/3 · Oxydoréduction")
        R = [(r"\textbf{1.}\; $\sum$ n.o. $=$ charge de l'édifice", "h5", 2.25),
             (r"\textbf{2.}\; O : $-\mathrm{II}$ en général \quad H : $+\mathrm{I}$", "h6", 1.55),
             (r"\textbf{3.}\; corps simple : n.o. $= 0$", "h7", 0.85)]
        for txt, sid, y in R:
            self.ecr(self.t(sid) + 0.5, pos(T(txt, sc=0.8), -5.9, y), rt=1.2)
        e1 = pos(M(ch("ClO_4^-"), r"\;:", sc=0.95, color=BLEU), -5.9, -0.45)
        self.ecr(self.a("h8a", "l'ion perchlorate"), e1, rt=0.6)
        c1 = M("x", r"\;+\;4\times(-2)", r"\;=\;-1", sc=0.95).next_to(e1, RIGHT, buff=0.5)
        c2 = M(r"\Longrightarrow\quad x = +\mathrm{VII}", sc=0.95, color=VERT).next_to(c1, RIGHT, buff=0.5)
        self.at(self.a("h8a", "Appelons"), Ecrire(c1[0], rt=0.3))
        self.at(self.a("h8b", "comptent"), Ecrire(c1[1], rt=0.8))
        self.at(self.a("h8b", "la charge"), Ecrire(c1[2], rt=0.6))
        self.at(self.a("h8b", "On trouve"), Ecrire(c2, rt=0.9))
        e2 = pos(M(ch("H_2O_2"), r"\;:", sc=0.95, color=BLEU), -5.9, -1.5)
        p2 = T(r"peroxyde $\Rightarrow$ O au n.o. $-\mathrm{I}$", sc=0.85, color=ROUGE).next_to(e2, RIGHT, buff=0.5)
        pg = T(r"(et non $-\mathrm{II}$ !)", sc=0.65, color=GRIS).next_to(p2, RIGHT, buff=0.4)
        self.ecr(self.a("h9", "l'eau oxygénée"), e2, rt=0.6)
        self.ecr(self.a("h9", "C'est un peroxyde"), p2, rt=1.2)
        self.at(self.a("h9", "et pas"), FadeIn(pg), run_time=0.3)
        o = pos(T(r"oxydation : n.o. $\nearrow$", sc=0.8, color=ORANGE), -5.9, -2.9)
        r = pos(T(r"réduction : n.o. $\searrow$", sc=0.8, color=BLEU), 0.2, -2.9)
        self.ecr(self.a("h10", "une oxydation"), o, rt=0.9); self.ecr(self.a("h10", "une réduction"), r, rt=0.9)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete("1.3 -- Formule de Nernst", "3/3 · Oxydoréduction")
        l1 = pos(T(r"Potentiel $E$ du couple, mesuré par rapport à l'\textbf{ESH} ($E = 0$ V par convention)", color=BLEU), -6.4, 2.35)
        self.ecr(self.a("i1", "un potentiel"), l1, rt=2.2)
        ne = M("E", r"\;=\;E^\circ", r"\;+\;\dfrac{RT}{\gamma F}", r"\,\ln", r"\dfrac{a_{\mathrm{Ox}}^{\,\alpha}}{a_{\mathrm{Red}}^{\,\beta}}", sc=1.05).move_to([-2.6, 1.1, 0])
        for part, fr in zip(ne, ["E égale", "E standard", "plus R T", "le logarithme", "du rapport"]):
            self.at(self.a("i3", fr), Ecrire(part, rt=0.6))
        bx = SurroundingRectangle(ne, color=ROUGE, buff=0.2, corner_radius=0.08); self.play(Create(bx), run_time=0.4)
        sens = VGroup(T("oxydant en haut", sc=0.6, color=ORANGE), T("réducteur en bas", sc=0.6, color=BLEU)).arrange(DOWN, aligned_edge=LEFT, buff=0.28).next_to(bx, RIGHT, buff=0.5)
        self.at(self.a("i3", "l'oxydant en haut"), FadeIn(sens[0], shift=LEFT*0.2), run_time=0.4)
        self.at(self.a("i3", "le réducteur"), FadeIn(sens[1], shift=LEFT*0.2), run_time=0.4)
        pr = pos(M(r"\text{à 25\,°C :}\quad E \;\approx\; E^\circ + ", r"\dfrac{0{,}06}{\gamma}", r"\,\log\dfrac{a_{\mathrm{Ox}}^{\,\alpha}}{a_{\mathrm{Red}}^{\,\beta}}", sc=0.95), -5.9, -0.95)
        self.ecr(self.a("i4", "la forme pratique"), pr, rt=2.0)
        why = M(r"\dfrac{RT\ln 10}{F} = 0{,}059\ \mathrm{V} \approx 0{,}06\ \mathrm{V}", sc=0.7, color=JAUNE).next_to(pr, RIGHT, buff=0.55)
        self.at(self.t("i5"), pr[1].animate.set_color(JAUNE), run_time=0.4)
        self.ecr(self.a("i5", "C'est simplement"), why, rt=1.8)
        ex = pos(M(ch("Cu^{2+}") + r" + 2\,e^- = " + ch("Cu(s)"), sc=0.9, color=BLEU), -5.9, -2.6)
        self.ecr(self.t("i6") + 0.2, ex, rt=1.0)
        res = M(r"E = 0{,}34 + 0{,}03\,\log\dfrac{[\mathrm{Cu^{2+}}]}{c^\circ}", sc=0.95, color=VERT).move_to([2.9, -2.6, 0])
        self.ecr(self.a("i7", "E égale"), res, rt=2.2)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"1.3 -- Règle du gamma et constante d'équilibre", "3/3 · Oxydoréduction")
        xa = -4.6
        ax = Arrow([xa, -3.2, 0], [xa, 2.5, 0], color=CRAIE, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.04)
        le = M(r"E^\circ", sc=0.75).next_to(ax.get_end(), LEFT, buff=0.15)
        yt, yb = 1.2, -1.5
        o1 = M(r"\mathrm{Ox_1}", sc=0.9).move_to([xa-0.85, yt, 0]); r1 = M(r"\mathrm{Red_1}", sc=0.9).move_to([xa+0.95, yt, 0])
        o2 = M(r"\mathrm{Ox_2}", sc=0.9).move_to([xa-0.85, yb, 0]); r2 = M(r"\mathrm{Red_2}", sc=0.9).move_to([xa+0.95, yb, 0])
        tk = VGroup(Line([xa-0.12, yt, 0], [xa+0.12, yt, 0], color=CRAIE), Line([xa-0.12, yb, 0], [xa+0.12, yb, 0], color=CRAIE))
        self.at(self.a("j1", "Classons"), GrowArrow(ax), FadeIn(le), run_time=0.7)
        self.play(Create(tk), Ecrire(VGroup(o1, r1), rt=0.6), Ecrire(VGroup(o2, r2), rt=0.6), run_time=0.8)
        self.at(self.t("j2"), o1.animate.set_color(ORANGE), Circumscribe(o1, color=ORANGE, run_time=1.0), run_time=1.0)
        self.at(self.a("j2", "Le réducteur"), r2.animate.set_color(BLEU), Circumscribe(r2, color=BLEU, run_time=1.0), run_time=1.0)
        g = VMobject(color=ROUGE, stroke_width=5)
        g.set_points_smoothly([[xa-0.8, yt-0.35, 0], [xa, -0.15, 0], [xa+0.85, yb+0.35, 0], [xa+1.75, yb-0.05, 0], [xa+1.0, yb-0.7, 0],
                               [xa, yb-0.85, 0], [xa-1.0, yb-0.7, 0], [xa-1.65, yb-0.05, 0], [xa-0.8, yb+0.35, 0], [xa, -0.15, 0], [xa+0.55, 0.5, 0]])
        tip = Arrow([xa+0.5, 0.44, 0], [xa+0.85, yt-0.32, 0], color=ROUGE, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.5)
        self.at(self.a("j3", "En reliant"), Create(g), run_time=2.0, rate_func=linear); self.play(GrowArrow(tip), run_time=0.3)
        X = -1.3
        rx = pos(M(r"\mathrm{Ox_1}", "+", r"\mathrm{Red_2}", r"\longrightarrow", r"\mathrm{Red_1} + \mathrm{Ox_2}", sc=0.9), X, 2.4)
        rx[0].set_color(ORANGE); rx[2].set_color(BLEU)
        self.ecr(self.a("j3", "c'est la règle"), rx, rt=1.2)
        eqm = pos(M(r"\text{à l'équilibre :}\quad E_1 = E_2", sc=0.85), X, 1.7)
        self.ecr(self.a("j4", "À l'équilibre"), eqm, rt=1.2)
        K = pos(M(r"\log K^\circ \;=\; \dfrac{\gamma\,(E_1^\circ - E_2^\circ)}{0{,}06}", sc=1.0), X + 0.2, 0.6)
        self.ecr(self.t("j5"), K, rt=2.6)
        bx = SurroundingRectangle(K, color=ROUGE, buff=0.2, corner_radius=0.08); self.play(Create(bx), run_time=0.4)
        nk = T("à 298 K", sc=0.6, color=GRIS).next_to(bx, RIGHT, buff=0.3)
        self.play(FadeIn(nk), run_time=0.3)
        d = pos(M(ch("Cu^{2+}"), "+", ch("Zn(s)"), r"\longrightarrow", ch("Cu(s)") + "+" + ch("Zn^{2+}"), sc=0.85, color=BLEU), X, -0.6)
        self.ecr(self.a("j6", "L'ion cuivre"), d, rt=1.4)
        pt = pos(M(r"E^\circ_{\mathrm{Cu^{2+}/Cu}} = 0{,}34\ \mathrm{V}", r"\qquad", r"E^\circ_{\mathrm{Zn^{2+}/Zn}} = -0{,}76\ \mathrm{V}", sc=0.72), X, -1.3)
        self.at(self.a("j6", "zéro virgule trente-quatre"), Ecrire(pt[0], rt=0.8))
        self.at(self.a("j6", "et moins"), Ecrire(pt[2], rt=0.8))
        cal = pos(M(r"\log K^\circ = \dfrac{2\times 1{,}10}{0{,}06}", r"\;\approx\; 37", sc=0.85), X, -2.15)
        self.at(self.a("j7", "logarithme"), Ecrire(cal[0], rt=1.6))
        self.at(self.a("j7", "Soit"), Ecrire(cal[1], rt=0.5))
        fin = pos(M(r"K^\circ \approx 10^{37}", r"\;:\;\text{réaction totale}", sc=0.9, color=ROUGE), X, -3.1)
        self.ecr(self.t("j8"), fin, rt=1.2)
        self.at(self.a("j8", "c'est gigantesque"), Indicate(fin[0], color=JAUNE, scale_factor=1.2), run_time=0.8)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, r"n_i = n_{i,0} + \nu_i\,\xi", "avancement et coefficients algébriques", "k2", 2.0),
                (VERT, r"Q_r = \prod_i a_i^{\,\nu_i} \qquad Q_r < K^\circ \Rightarrow \text{sens direct}", "quotient de réaction et critère d'évolution", "k3", 0.6),
                (ORANGE, r"E = E^\circ + \dfrac{0{,}06}{\gamma}\log\dfrac{a_{\mathrm{Ox}}^{\,\alpha}}{a_{\mathrm{Red}}^{\,\beta}} \qquad \log K^\circ = \dfrac{\gamma\,(E_1^\circ - E_2^\circ)}{0{,}06}", "Nernst et constante d'équilibre rédox", "k4", -1.25)]
        for k, (col, fo, lab, sid, y) in enumerate(data):
            c = Circle(radius=0.27, color=col, stroke_width=3).move_to([-5.9, y, 0]); n = T(r"\textbf{%d}" % (k+1), sc=0.75, color=col).move_to(c)
            L = pos(T(lab, sc=0.6, color=col), -5.3, y + (0.85 if k == 2 else 0.55)); F = pos(M(fo, sc=0.85), -5.3, y - 0.1)
            self.at(self.t(sid), Create(c), FadeIn(n), FadeIn(L), run_time=0.5)
            self.play(Ecrire(F, rt=1.8))
        nx = T(r"Chapitre 2 \;$\longrightarrow$\; enthalpie libre $G$ et potentiel chimique $\mu_i$", sc=0.8, color=JAUNE).move_to([0, -3.1, 0])
        self.ecr(self.a("k5", "l'enthalpie libre"), nx, rt=1.8)
        self.fin()
