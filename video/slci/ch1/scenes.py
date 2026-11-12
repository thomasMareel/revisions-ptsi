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
def croix(p, col=ROUGE, r=0.13):
    return VGroup(Line(p + np.array([-r, -r, 0]), p + np.array([r, r, 0]), color=col, stroke_width=5),
                  Line(p + np.array([-r, r, 0]), p + np.array([r, -r, 0]), color=col, stroke_width=5))
def boite(txt, x, y, w=2.4, h=0.9, col=CRAIE, sc=0.7):
    r = Rectangle(width=w, height=h, color=col, stroke_width=3).move_to([x, y, 0])
    return VGroup(r, T(txt, sc=sc, color=col).move_to(r))

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PTSI", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Automatique -- Chapitre 1}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Modélisation et transformée de Laplace", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        sy = boite("Système", 0, 0.45, w=2.2, h=0.8, col=BLEU)
        fe = Arrow([-3.3, 0.45, 0], [-1.15, 0.45, 0], color=CRAIE, buff=0, stroke_width=4)
        fs = Arrow([1.15, 0.45, 0], [3.3, 0.45, 0], color=CRAIE, buff=0, stroke_width=4)
        le = M(r"e(t)", sc=0.8).next_to(fe, UP, buff=0.1); ls = M(r"s(t)", sc=0.8, color=JAUNE).next_to(fs, UP, buff=0.1)
        self.at(self.a("a2", "Un moteur"), Create(sy[0]), FadeIn(sy[1]), run_time=0.6)
        self.at(self.a("a2", "reçoivent une entrée"), GrowArrow(fe), FadeIn(le), run_time=0.5)
        self.at(self.a("a2", "produisent une sortie"), GrowArrow(fs), FadeIn(ls), run_time=0.5)
        self.at(self.a("a2", "prévoir cette sortie"), Indicate(ls, color=JAUNE, scale_factor=1.3), run_time=0.8)
        items = []
        for k, (txt, c) in enumerate([("Les SLCI et la linéarité", BLEU), ("La transformée de Laplace", VERT), ("La fonction de transfert", ORANGE),
                                       ("Revenir au temps : les pôles", ROUGE), ("Exercice résolu", JAUNE)]):
            yy = -0.65 - 0.58*k
            items.append(VGroup(carte(k+1, c, -3.4, yy), pos(T(txt, sc=0.78), -2.8, yy)))
        for it, (sid, fr) in zip(items, [("a3", "les S L C I"), ("a3", "la transformée de Laplace"), ("a3", "la fonction de transfert"),
                                         ("a3", "le retour au temps"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"1.1 -- Les systèmes linéaires continus et invariants", "Modélisation")
        sy = boite("Système", 0, 1.95, w=2.2, h=0.75, col=BLEU)
        fe = Arrow([-3.0, 1.95, 0], [-1.1, 1.95, 0], color=CRAIE, buff=0, stroke_width=4); fs = Arrow([1.1, 1.95, 0], [3.0, 1.95, 0], color=CRAIE, buff=0, stroke_width=4)
        le = M(r"e(t)", sc=0.8).next_to(fe, LEFT, buff=0.15); ls = M(r"s(t)", sc=0.8, color=JAUNE).next_to(fs, RIGHT, buff=0.15)
        self.at(self.t("b1"), Create(sy[0]), FadeIn(sy[1]), GrowArrow(fe), FadeIn(le), run_time=0.7); self.play(GrowArrow(fs), FadeIn(ls), run_time=0.5)
        c1 = pos(T(r"\textbf{Continu} : grandeurs définies à chaque instant", sc=0.72), -6.3, 0.95)
        c2 = pos(T(r"\textbf{Invariant} : même comportement à tout instant", sc=0.72), -6.3, 0.4)
        self.ecr(self.a("b2", "Continu"), c1, rt=1.0); self.ecr(self.a("b2", "Invariant"), c2, rt=1.0)
        c3 = pos(T(r"\textbf{Linéaire} : principe de superposition", sc=0.72, color=BLEU), -6.3, -0.2)
        sp = pos(M(r"e_1 \mapsto s_1,\; e_2 \mapsto s_2 \;\Longrightarrow\; \lambda e_1 + \mu e_2 \mapsto \lambda s_1 + \mu s_2", sc=0.78, color=BLEU), -5.8, -0.85)
        self.ecr(self.a("b3", "Et linéaire"), c3, rt=0.9); self.ecr(self.a("b3", "Si e un donne"), sp, rt=1.6)
        db = pos(T(r"entrée $\times 2$ \;$\Rightarrow$\; sortie $\times 2$ : même forme de réponse", sc=0.7, color=VERT), -5.8, -1.5)
        self.ecr(self.a("b4", "doubler l'entrée"), db, rt=1.2)
        eq = M(r"a_n\, s^{(n)} + \cdots + a_1\, s' + a_0\, s = b_m\, e^{(m)} + \cdots + b_0\, e", sc=0.85, color=JAUNE).move_to([0, -2.45, 0])
        self.ecr(self.a("b5", "est régi par"), eq, rt=1.4); self.play(Create(enc(eq, col=JAUNE)), run_time=0.4)
        od = T(r"ordre $= n$", sc=0.72, color=ORANGE).next_to(eq, DOWN, buff=0.45).align_to(eq, LEFT)
        self.at(self.a("b6", "La plus haute dérivée"), Indicate(eq[0][0:6], color=ORANGE, scale_factor=1.2), run_time=0.7); self.ecr(self.a("b6", "donne l'ordre"), od, rt=0.6)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"1.2 -- Non-linéarités et linéarisation", "Modélisation")
        att = pos(T(r"Aucun système réel n'est parfaitement linéaire", sc=0.72, color=ROUGE), -6.3, 2.25)
        self.ecr(self.t("c1"), att, rt=1.0)
        noms = [("Saturation", "c2"), ("Seuil", "c3"), ("Hystérésis", "c4")]
        for k, (nom, ph) in enumerate(noms):
            cx = -4.3 + 4.3*k
            ax = axes(cx, 0.75, 2.6, 2.0, [-1.2, 1.2, 1], [-1.1, 1.1, 1])
            if k == 0:
                cb = VMobject(color=BLEU, stroke_width=5).set_points_as_corners([ax.c2p(-1.15, -0.6), ax.c2p(-0.5, -0.6), ax.c2p(0.5, 0.6), ax.c2p(1.15, 0.6)])
                extra = []
            elif k == 1:
                cb = VMobject(color=BLEU, stroke_width=5).set_points_as_corners([ax.c2p(-1.15, -0.7), ax.c2p(-0.35, 0), ax.c2p(0.35, 0), ax.c2p(1.15, 0.7)])
                extra = []
            else:
                cb = VMobject(color=BLEU, stroke_width=5).set_points_as_corners([ax.c2p(-1.15, -0.55), ax.c2p(0.3, -0.55), ax.c2p(0.3, 0.55), ax.c2p(1.15, 0.55)])
                extra = [VMobject(color=ORANGE, stroke_width=5).set_points_as_corners([ax.c2p(1.15, 0.55), ax.c2p(-0.3, 0.55), ax.c2p(-0.3, -0.55), ax.c2p(-1.15, -0.55)])]
            lb = T(r"\textbf{" + nom + "}", sc=0.72, color=JAUNE).move_to([cx, -0.55, 0])
            le = M("e", sc=0.6, color=GRIS).next_to(ax.x_axis.get_end(), DOWN, buff=0.08); ls = M("s", sc=0.6, color=GRIS).next_to(ax.y_axis.get_end(), LEFT, buff=0.08)
            self.at(self.t(ph), Create(ax), FadeIn(le), FadeIn(ls), Ecrire(lb, rt=0.5), run_time=0.6)
            self.play(Create(cb), run_time=0.8)
            if extra: self.play(Create(extra[0]), run_time=0.8)
        ax = axes(-4.3, -2.35, 2.8, 1.75, [0, 3, 1], [0, 2, 1])
        f = lambda x: 0.25 + 0.95*np.sqrt(x); x0 = 1.3; fp = 0.95/(2*np.sqrt(x0))
        cb = ax.plot(f, x_range=[0.01, 2.8, 0.02], color=BLEU, stroke_width=4)
        tg = ax.plot(lambda x: f(x0) + fp*(x - x0), x_range=[0.2, 2.6, 0.05], color=ORANGE, stroke_width=4)
        pt = Dot(ax.c2p(x0, f(x0)), color=JAUNE, radius=0.08)
        self.at(self.t("c5"), Create(ax), Create(cb), run_time=0.8)
        self.at(self.a("c5", "autour d'un point"), FadeIn(pt, scale=2), run_time=0.4)
        self.at(self.a("c5", "on remplace"), Create(tg), run_time=0.7)
        lin = pos(M(r"g(x) \approx g(x_0) + g'(x_0)\,\Delta x", sc=0.85, color=ORANGE), -1.9, -1.85)
        self.ecr(self.a("c5", "par sa tangente"), lin, rt=1.0)
        ok = pos(T(r"$\Rightarrow$ un SLCI, valable pour de \textbf{petites variations}", sc=0.72, color=VERT), -1.9, -2.75)
        self.ecr(self.t("c6"), ok, rt=1.2)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"1.3 -- La transformée de Laplace", "Outil de calcul")
        F = M(r"F(p) = \mathcal{L}\big[f(t)\big] = \int_0^{+\infty} f(t)\, e^{-pt}\, dt", sc=1.0, color=JAUNE).move_to([0, 1.65, 0])
        ca = T(r"$f$ causale : $f(t) = 0$ pour $t < 0$ \quad ; \quad $p$ : variable complexe", sc=0.66, color=GRIS).move_to([0, 0.42, 0])
        self.at(self.a("d2", "nulle avant zéro"), FadeIn(ca), run_time=0.6)
        self.ecr(self.a("d2", "on associe"), F, rt=1.5); self.play(Create(enc(F, col=JAUNE)), run_time=0.4)
        de = pos(M(r"\mathcal{L}\big[f'\big] = p\,F(p)", sc=0.95, color=BLEU), -6.0, -0.35)
        rp = pos(T(r"système au repos (conditions de Heaviside)", sc=0.6, color=GRIS), -6.0, -1.05)
        self.at(self.a("d3", "part du repos"), FadeIn(rp), run_time=0.5); self.ecr(self.a("d3", "dériver revient"), de, rt=1.0)
        it = pos(M(r"\mathcal{L}\Big[\int_0^t f(u)\,du\Big] = \frac{F(p)}{p}", sc=0.95, color=BLEU), 0.9, -0.35)
        self.ecr(self.t("d4"), it, rt=1.1)
        ar = pos(T(r"équation différentielle \;$\longrightarrow$\; équation \textbf{algébrique}", sc=0.75, color=VERT), -4.8, -2.05)
        self.ecr(self.a("d4", "Les équations différentielles"), ar, rt=1.2)
        cv = M(r"f(t) \;\longleftrightarrow\; F(p)", sc=0.95).move_to([0, -3.05, 0])
        self.ecr(self.t("d5"), cv, rt=0.8)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"1.4 -- La table et les théorèmes", "Outil de calcul")
        lignes = [(r"\delta(t) \;\longmapsto\; 1", "e1", "L'impulsion"), (r"u(t) \;\longmapsto\; \frac{1}{p}", "e1", "L'échelon"),
                  (r"t \;\longmapsto\; \frac{1}{p^2}", "e1", "La rampe"), (r"e^{-at} \;\longmapsto\; \frac{1}{p + a}", "e2", "L'exponentielle"),
                  (r"\sin(\omega t) \;\longmapsto\; \frac{\omega}{p^2 + \omega^2}", "e2", "Et sinus"), (r"f(t - T) \;\longmapsto\; e^{-Tp}\,F(p)", "e3", "Un retard")]
        ys = [2.05, 1.35, 0.55, -0.3, -1.2, -2.15]
        for (s, ph, fr), y in zip(lignes, ys):
            m = pos(M(s, sc=0.85, color=ORANGE if ph == "e3" else CRAIE), -6.3, y)
            self.ecr(self.a(ph, fr), m, rt=0.7)
        vi = pos(T(r"\textbf{Valeur initiale}", sc=0.72, color=BLEU), 0.6, 1.9)
        vim = pos(M(r"\lim_{t \to 0^+} f(t) = \lim_{p \to +\infty} p\,F(p)", sc=0.85), 0.6, 1.15)
        self.ecr(self.a("e4", "La valeur initiale"), vi, rt=0.5); self.ecr(self.a("e4", "c'est la limite"), vim, rt=1.1)
        vf = pos(T(r"\textbf{Valeur finale}", sc=0.72, color=BLEU), 0.6, 0.15)
        vfm = pos(M(r"\lim_{t \to +\infty} f(t) = \lim_{p \to 0} p\,F(p)", sc=0.85), 0.6, -0.6)
        self.ecr(self.t("e5"), vf, rt=0.5); self.ecr(self.a("e5", "c'est la limite"), vfm, rt=1.1)
        av = pos(T(r"seulement si le système est \textbf{stable} !", sc=0.75, color=ROUGE), 0.9, -1.75)
        self.ecr(self.a("e6", "n'a de sens"), av, rt=0.9); self.play(Create(enc(av)), run_time=0.4)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"1.5 -- La fonction de transfert", "Exemple en direct")
        e1 = pos(M(r"2s'' + 3s' + s = 4e", sc=0.9), -6.3, 2.05)
        self.ecr(self.a("f1", "Un système vérifie"), e1, rt=1.0)
        e2 = pos(M(r"(2p^2 + 3p + 1)\,S(p) = 4\,E(p)", sc=0.9), -6.3, 1.2)
        self.ecr(self.a("f2", "On passe en Laplace"), e2, rt=1.2)
        h = pos(M(r"H(p) = \frac{S(p)}{E(p)} = \frac{4}{1 + 3p + 2p^2}", sc=0.95, color=JAUNE), -6.3, 0.0)
        self.ecr(self.a("f3", "c'est le rapport"), h, rt=1.3); self.play(Create(enc(h, col=JAUNE)), run_time=0.4)
        sh = pos(T(r"pour toute entrée : $S = H \times E$", sc=0.72, color=BLEU), -6.3, -1.1)
        self.ecr(self.a("f4", "Pour toute entrée"), sh, rt=0.9)
        g = pos(T(r"gain statique : $4$ \qquad ordre : $2$", sc=0.72), -6.3, -1.85)
        self.ecr(self.a("f5", "Gain statique"), g, rt=1.0)
        fa = pos(M(r"1 + 3p + 2p^2 = (1 + p)(1 + 2p)", sc=0.85), -6.3, -2.6)
        self.ecr(self.a("f5", "le dénominateur se factorise"), fa, rt=1.1)
        ax = axes(3.6, -1.6, 4.4, 2.6, [-1.6, 0.6, 1], [-1, 1, 1], col=GRIS)
        lr = M(r"\mathrm{Re}", sc=0.55, color=GRIS).next_to(ax.x_axis.get_end(), DOWN, buff=0.1); li = M(r"\mathrm{Im}", sc=0.55, color=GRIS).next_to(ax.y_axis.get_end(), LEFT, buff=0.1)
        p1 = croix(ax.c2p(-1, 0)); p2 = croix(ax.c2p(-0.5, 0))
        l1 = M("-1", sc=0.6, color=ROUGE).next_to(p1, DOWN, buff=0.15); l2 = M(r"-\tfrac12", sc=0.6, color=ROUGE).next_to(p2, UP, buff=0.15)
        pl = T(r"pôles", sc=0.7, color=ROUGE).move_to([3.6, -0.05, 0])
        self.at(self.t("f6"), Create(ax), FadeIn(lr), FadeIn(li), FadeIn(pl), run_time=0.6)
        self.at(self.a("f6", "valent donc"), FadeIn(p1, scale=2), FadeIn(l1), run_time=0.5)
        self.at(self.a("f6", "moins un demi"), FadeIn(p2, scale=2), FadeIn(l2), run_time=0.5)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"1.6 -- Forme canonique : le piège du gain", "Fonction de transfert")
        fc = M(r"H(p) = \frac{K}{p^{\alpha}} \cdot \frac{1 + b_1 p + \cdots}{1 + a_1 p + \cdots}", sc=1.0, color=JAUNE).move_to([0, 1.85, 0])
        self.ecr(self.a("g1", "La forme canonique"), fc, rt=1.3); self.play(Create(enc(fc, col=JAUNE)), run_time=0.4)
        lbs = [(r"$K$ : gain", -4.8, "le gain K"), (r"$\alpha$ : classe (intégrateurs)", -0.7, "la classe alpha"), (r"ordre : degré du dénominateur", 3.9, "et l'ordre")]
        for txt, x, fr in lbs:
            m = T(txt, sc=0.68, color=BLEU).move_to([x, 0.75, 0]); self.ecr(self.a("g2", fr), m, rt=0.7)
        pg = pos(M(r"\frac{10}{p + 5}", sc=1.0), -6.2, -0.55)
        nn = pos(T(r"gain $\neq 10$ !", sc=0.75, color=ROUGE), -4.6, -0.55)
        self.ecr(self.a("g3", "dans dix sur p plus cinq"), pg, rt=0.6); self.ecr(self.a("g3", "le gain n'est pas"), nn, rt=0.6)
        ok = pos(M(r"= \frac{2}{1 + 0{,}2p} \quad\Rightarrow\quad K = 2", sc=1.0, color=VERT), -1.4, -0.55)
        self.ecr(self.a("g4", "On divise"), ok, rt=1.1)
        ex = pos(M(r"\frac{6p + 12}{p^3 + 4p^2} = \frac{3}{p^2} \cdot \frac{1 + 0{,}5p}{1 + 0{,}25p}", sc=0.95), -6.2, -2.0)
        self.ecr(self.a("g5", "Autre exemple"), ex, rt=1.5)
        rs = pos(T(r"$K = 3$, \; classe $2$, \; ordre $3$", sc=0.78, color=VERT), 1.6, -2.0)
        self.ecr(self.t("g6"), rs, rt=0.9); self.play(Create(enc(rs, col=VERT)), run_time=0.4)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"1.7 -- Revenir au temps", "Réponse temporelle")
        h = pos(M(r"H(p) = \frac{2}{1 + 0{,}5p}, \qquad E(p) = \frac{1}{p}", sc=0.85), -6.4, 2.1)
        self.ecr(self.a("h1", "Prenons H de p"), h, rt=1.2)
        s = pos(M(r"S(p) = \frac{4}{p\,(p + 2)} = \frac{A}{p} + \frac{B}{p + 2}", sc=0.85), -6.4, 1.0)
        self.ecr(self.t("h2"), s, rt=1.3)
        a = pos(M(r"A = \Big[\frac{4}{p + 2}\Big]_{p = 0} = 2", sc=0.85, color=BLEU), -6.4, -0.2)
        self.ecr(self.a("h3", "pour A"), a, rt=1.1)
        b = pos(M(r"B = \Big[\frac{4}{p}\Big]_{p = -2} = -2", sc=0.85, color=BLEU), -6.4, -1.35)
        self.ecr(self.t("h4"), b, rt=1.1)
        r = pos(M(r"s(t) = 2\,\big(1 - e^{-2t}\big)", sc=0.95, color=JAUNE), -6.4, -2.6)
        self.ecr(self.a("h5", "La table donne"), r, rt=1.0); self.play(Create(enc(r, col=JAUNE)), run_time=0.4)
        ax = axes(3.7, -0.5, 5.0, 3.4, [0, 3.2, 1], [0, 2.5, 1])
        lt = M("t", sc=0.7).next_to(ax.x_axis.get_end(), DOWN, buff=0.12); ls = M("s(t)", sc=0.7).next_to(ax.y_axis.get_end(), LEFT, buff=0.12)
        cb = ax.plot(lambda t: 2*(1 - np.exp(-2*t)), x_range=[0, 3.1, 0.02], color=BLEU, stroke_width=5)
        self.at(self.a("h5", "Une belle exponentielle"), Create(ax), FadeIn(lt), FadeIn(ls), run_time=0.5); self.play(Create(cb), run_time=1.0)
        asy = DashedLine(ax.c2p(0, 2), ax.c2p(3.2, 2), color=VERT, stroke_width=3)
        l2 = M("2", sc=0.75, color=VERT).next_to(ax.c2p(0, 2), LEFT, buff=0.12)
        d0 = Dot(ax.c2p(0, 0), color=VERT, radius=0.09)
        v0 = T(r"$s(0) = 0$", sc=0.62, color=VERT).next_to(ax.c2p(0, 0), UR, buff=0.15)
        vf = T(r"$s(\infty) = 2$", sc=0.62, color=VERT).next_to(ax.c2p(2.4, 2), DOWN, buff=0.18)
        self.at(self.a("h6", "départ à zéro"), FadeIn(d0, scale=2), FadeIn(v0), run_time=0.5)
        self.at(self.a("h6", "arrivée à deux"), Create(asy), FadeIn(l2), FadeIn(vf), run_time=0.6)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"1.8 -- Les pôles décident de tout", "Réponse temporelle")
        ex = M(r"\text{pôle } p_i \;\longrightarrow\; \text{terme } e^{p_i t}", sc=0.95, color=JAUNE).move_to([0, 2.15, 0])
        self.ecr(self.a("i1", "chaque pôle"), ex, rt=1.1)
        ax = axes(-3.7, -0.75, 4.6, 4.4, [-2.8, 1.5, 1], [-2.6, 2.6, 1], col=GRIS)
        lr = M(r"\mathrm{Re}", sc=0.55, color=GRIS).next_to(ax.x_axis.get_end(), DOWN, buff=0.1); li = M(r"\mathrm{Im}", sc=0.55, color=GRIS).next_to(ax.y_axis.get_end(), LEFT, buff=0.1)
        self.at(self.a("i1", "fait apparaître"), Create(ax), FadeIn(lr), FadeIn(li), run_time=0.6)
        zone = Polygon(ax.c2p(-2.8, -2.6), ax.c2p(0, -2.6), ax.c2p(0, 2.6), ax.c2p(-2.8, 2.6), stroke_width=0, fill_color=VERT, fill_opacity=0.13)
        t = np.linspace(0, 6, 160)
        cas = [("i2", "A", [(-1.8, 0)], np.exp(-1.1*t), "Un pôle réel"),
               ("i3", "B", [(-0.7, 1.6), (-0.7, -1.6)], np.exp(-0.45*t)*np.cos(3*t), "Deux pôles complexes"),
               ("i4", "C", [(0.9, 0)], np.exp(0.5*t)/np.exp(3.0), "Un pôle à droite"),
               ("i5", "D", [(0, 2.2), (0, -2.2)], np.cos(3*t), "Et sur l'axe")]
        marques = {}
        for k, (ph, nom, pts, y, fr) in enumerate(cas):
            cr = VGroup(*[croix(ax.c2p(a, b), col=ORANGE if nom == "B" else ROUGE) for a, b in pts])
            ln = T(r"\textbf{" + nom + "}", sc=0.62, color=JAUNE).next_to(cr[0], UR, buff=0.05)
            marques[nom] = cr
            yy = 1.0 - 1.2*k
            q = axes(3.6, yy, 4.6, 0.9, [0, 6, 1], [-1.05, 1.05, 1], col=GRIS, sw=1.5)
            cb = q.plot_line_graph(t, np.clip(y, -1.05, 1.05), add_vertex_dots=False, line_color=BLEU, stroke_width=4)
            nq = T(r"\textbf{" + nom + "}", sc=0.62, color=JAUNE).next_to(q, LEFT, buff=0.15)
            self.at(self.a(ph, fr), FadeIn(cr, scale=2), FadeIn(ln), Create(q), FadeIn(nq), run_time=0.6)
            self.play(Create(cb), run_time=0.9)
            if ph == "i4":
                st = T("stable", sc=0.6, color=VERT).move_to(ax.c2p(-1.7, -2.15))
                self.play(FadeIn(zone), FadeIn(st), run_time=0.5)
        dom = pos(T(r"pôle dominant : le plus proche de l'axe", sc=0.68, color=ORANGE), -6.3, -3.35)
        self.at(self.a("i6", "c'est le pôle dominant"), Ecrire(dom, rt=0.9), Indicate(marques["B"], color=ORANGE, scale_factor=1.4), run_time=0.9)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"1.9 -- À vous de jouer", "Exercice")
        S = M(r"S(p) = \frac{6}{p\,(p + 1)(p + 3)}", sc=1.05, color=JAUNE).move_to([-0.6, 1.95, 0])
        q = T(r"Retrouvez $s(t)$.", sc=0.75, color=BLEU).next_to(S, DOWN, buff=0.35)
        self.ecr(self.a("j1", "Retrouvez"), S, rt=1.2); self.ecr(self.a("j1", "pour S de p"), q, rt=0.6)
        pa, arc = chrono(4.3, 1.95)
        self.at(self.a("j1", "Mettez sur pause"), FadeIn(pa), Create(arc), run_time=0.5)
        self.play(Uncreate(arc), run_time=2.6)
        self.play(FadeOut(pa), run_time=0.2)
        a = pos(M(r"A = \frac{6}{1 \times 3} = 2", sc=0.85), -6.3, -0.25)
        self.ecr(self.a("j2", "A égale"), a, rt=0.9)
        b = pos(M(r"B = \frac{6}{(-1) \times 2} = -3", sc=0.85), -2.3, -0.25)
        c = pos(M(r"C = \frac{6}{(-3) \times (-2)} = 1", sc=0.85), 2.1, -0.25)
        self.ecr(self.a("j3", "B, en p"), b, rt=1.0); self.ecr(self.a("j3", "Et C"), c, rt=1.0)
        r = M(r"s(t) = 2 - 3\,e^{-t} + e^{-3t}", sc=1.0, color=JAUNE).move_to([-0.6, -1.55, 0])
        self.ecr(self.a("j4", "Donc s de t"), r, rt=1.1); self.play(Create(enc(r, col=JAUNE)), run_time=0.4)
        v = T(r"$s(0) = 2 - 3 + 1 = 0$ \;$\checkmark$", sc=0.72, color=VERT).move_to([-0.6, -2.45, 0])
        self.ecr(self.a("j4", "Et s de zéro"), v, rt=0.9)
        d = T(r"pôle dominant : $-1$ \; ($e^{-3t}$ s'éteint trois fois plus vite)", sc=0.7, color=ORANGE).move_to([-0.6, -3.25, 0])
        self.ecr(self.t("j5"), d, rt=1.3)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"1.10 -- Six modèles de référence", "Réponse à un échelon")
        t = np.linspace(0, 4, 120)
        modeles = [("Gain pur", r"K", lambda: np.where(t > 0.4, 0.8, 0), "k2", "Le gain pur"),
                   ("Intégrateur", r"\frac{K}{p}", lambda: np.clip(0.3*(t - 0.4), 0, None), "k2", "L'intégrateur"),
                   ("Dérivateur", r"K\,p", None, "k3", "Le dérivateur"),
                   ("Premier ordre", r"\frac{K}{1 + \tau p}", lambda: np.where(t > 0.4, 0.8*(1 - np.exp(-(t - 0.4)/0.6)), 0), "k3", "Le premier ordre"),
                   ("Deuxième ordre", r"\frac{K}{1 + \frac{2\xi}{\omega_0}p + \frac{p^2}{\omega_0^2}}", lambda: np.where(t > 0.4, 0.8*(1 - np.exp(-1.2*(t - 0.4))*(np.cos(4*(t - 0.4)) + 0.3*np.sin(4*(t - 0.4)))), 0), "k4", "Le deuxième ordre"),
                   ("Retard pur", r"e^{-Tp}", lambda: np.where(t > 1.6, 0.8, 0), "k4", "Et le retard pur")]
        cellules = []
        for k, (nom, ft, fn, ph, fr) in enumerate(modeles):
            cx = -4.4 + 4.4*(k % 3); cy = 1.15 if k < 3 else -1.95
            nm = T(r"\textbf{" + nom + "}", sc=0.7, color=JAUNE).move_to([cx, cy + 1.05, 0])
            fm = M(ft, sc=0.72 if k != 4 else 0.52, color=BLEU).move_to([cx, cy + 0.42, 0])
            q = axes(cx, cy - 0.75, 3.0, 1.25, [0, 4, 1], [0, 1.0, 1], col=GRIS, sw=1.5)
            if fn is None:
                cb = Arrow(q.c2p(0.4, 0), q.c2p(0.4, 1.0), color=BLEU, buff=0, stroke_width=5, max_tip_length_to_length_ratio=0.25)
            else:
                cb = q.plot_line_graph(t, fn(), add_vertex_dots=False, line_color=BLEU, stroke_width=4)
            self.at(self.a(ph, fr), Ecrire(nm, rt=0.5), FadeIn(fm), Create(q), run_time=0.6)
            self.play(Create(cb), run_time=0.6)
            cellules.append(VGroup(nm, fm, q, cb))
        self.at(self.a("k5", "se décompose"), *[Indicate(c[0], color=VERT, scale_factor=1.1) for c in cellules], run_time=1.0)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"À retenir", "Bilan")
        pts = [("l1", r"SLCI : superposition, équation différentielle à coefficients constants", BLEU),
               ("l2", r"Système au repos : dériver $\longleftrightarrow$ multiplier par $p$", VERT),
               ("l3", r"$H(p) = S(p)/E(p)$ sous forme canonique : gain, classe, ordre", ORANGE),
               ("l4", r"Retour au temps : éléments simples, puis valeurs initiale et finale", ROUGE),
               ("l5", r"Les pôles décident de l'allure de la réponse et de la stabilité", JAUNE)]
        for k, (ph, txt, c) in enumerate(pts):
            y = 1.9 - 1.05*k
            ca = carte(k+1, c, -5.9, y); tx = pos(T(txt, sc=0.72), -5.35, y)
            self.at(self.t(ph), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- l'énoncé", "Application")
        eq = M(r"s'' + 2s' + 5s = 5e", sc=1.15, color=JAUNE).move_to([0, 1.7, 0])
        self.ecr(self.a("m1", "Un système obéit"), eq, rt=1.0)
        do = T(r"entrée : échelon unité \quad ; \quad système au repos", sc=0.75).move_to([0, 0.75, 0])
        self.ecr(self.t("m2"), do, rt=1.0)
        q = T(r"Que vaut $s(t)$ ? Quelle allure a la réponse ?", sc=0.8, color=ROUGE).move_to([0, -0.3, 0])
        self.ecr(self.a("m2", "Question"), q, rt=1.0); self.play(Create(enc(q)), run_time=0.4)
        rf = T(r"Réfléchissons : équation différentielle + échelon $\Longrightarrow$ \textbf{Laplace}", sc=0.75, color=BLEU).move_to([0, -1.5, 0])
        self.ecr(self.t("m3"), rf, rt=1.2)
        etapes = ["FT", "pôles", "éléments simples", "table", "vérifications"]
        grp = VGroup(*[T(e, sc=0.7, color=GRIS) for e in etapes]).arrange(RIGHT, buff=0.85).move_to([0, -2.55, 0])
        fl = VGroup(*[MathTex(r"\to", color=GRIS).scale(0.8).move_to((grp[i].get_right() + grp[i+1].get_left())/2) for i in range(4)])
        self.at(self.t("m4"), LaggedStart(*[FadeIn(g) for g in grp], lag_ratio=0.4), FadeIn(fl), run_time=1.8)
        self.fin()

class S13(Cours):
    sid = "S13"
    def construct(self):
        self.entete(r"Exercice résolu -- la solution", "Application")
        def etape(k, c, y, m, ph, fr, rt=1.0):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(self.a(ph, fr), Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        etape(1, BLEU, 2.2, M(r"H(p) = \frac{5}{p^2 + 2p + 5}", sc=0.82), "n1", "Première étape")
        etape(2, VERT, 1.2, M(r"\Delta = 4 - 20 = -16 \;\Rightarrow\; p = -1 \pm 2j", sc=0.82), "n2", "Étape deux", 1.2)
        ex = pos(T(r"complexes, $\mathrm{Re} < 0$ : oscillation amortie", sc=0.66, color=BLEU), -5.85, 0.5)
        self.ecr(self.a("n3", "Des pôles complexes"), ex, rt=0.9)
        etape(3, ORANGE, -0.35, M(r"S(p) = \frac{A}{p} + \frac{Bp + C}{p^2 + 2p + 5}", sc=0.82), "n4", "Étape trois", 1.2)
        v = pos(M(r"A = 1, \quad B = -1, \quad C = -2", sc=0.8, color=BLEU), -5.85, -1.25)
        self.ecr(self.t("n5"), v, rt=1.0)
        etape(4, ROUGE, -2.0, M(r"p^2 + 2p + 5 = (p + 1)^2 + 4", sc=0.82), "n6", "Étape quatre")
        r = pos(M(r"s(t) = 1 - e^{-t}\big(\cos 2t + \tfrac12 \sin 2t\big)", sc=0.85, color=JAUNE), -6.4, -3.05)
        self.ecr(self.t("n7"), r, rt=1.3); self.play(Create(enc(r, col=JAUNE, buff=0.15)), run_time=0.4)
        ax = axes(3.9, 0.55, 4.6, 3.1, [0, 6.2, 1], [0, 1.45, 1])
        lt = M("t", sc=0.7).next_to(ax.x_axis.get_end(), DOWN, buff=0.12); ls = M("s(t)", sc=0.7).next_to(ax.y_axis.get_end(), LEFT, buff=0.12)
        f = lambda t: 1 - np.exp(-t)*(np.cos(2*t) + 0.5*np.sin(2*t))
        cb = ax.plot(f, x_range=[0, 6.1, 0.02], color=BLEU, stroke_width=5)
        self.at(self.t("n8"), Create(ax), FadeIn(lt), FadeIn(ls), run_time=0.5); self.play(Create(cb), run_time=1.2)
        un = DashedLine(ax.c2p(0, 1), ax.c2p(6.2, 1), color=VERT, stroke_width=3); l1 = M("1", sc=0.7, color=VERT).next_to(ax.c2p(0, 1), LEFT, buff=0.12)
        ck = T(r"$s(0) = 0$, \; $s(\infty) = 1$ \;$\checkmark$", sc=0.66, color=VERT).move_to([3.9, -1.35, 0])
        self.at(self.a("n8", "Et s tend vers un"), Create(un), FadeIn(l1), Ecrire(ck, rt=0.8), run_time=0.8)
        a, b = np.pi/2, 3*np.pi/2
        fl = DoubleArrow(ax.c2p(a, 1.33), ax.c2p(b, 1.33), color=ORANGE, buff=0, stroke_width=3, tip_length=0.15)
        lp = M(r"T = \pi", sc=0.7, color=ORANGE).next_to(fl, UP, buff=0.06)
        self.at(self.a("n9", "pseudo-période"), GrowFromCenter(fl), FadeIn(lp), run_time=0.6)
        env = ax.plot(lambda t: 1 + np.exp(-t), x_range=[0.9, 6.1, 0.05], color=GRIS, stroke_width=2)
        self.at(self.a("n9", "s'amortit"), Create(env), run_time=0.8)
        nx = T(r"Prochain chapitre : les schémas-blocs", sc=0.66, color=GRIS).move_to([3.9, -2.3, 0])
        self.at(self.t("n10"), FadeIn(nx), run_time=0.6)
        self.fin()
