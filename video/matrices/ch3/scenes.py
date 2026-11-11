from base import *
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)
def chrono(x, y):
    pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([x, y, 0])
    arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
    return pa, arc
def mat(rows, sc=0.8, col=CRAIE, h=0.9, v=0.65):
    m = Matrix([[str(x) for x in r] for r in rows], element_to_mobject=lambda s: MathTex(s, tex_template=tpl, color=col),
               left_bracket="(", right_bracket=")", h_buff=h, v_buff=v, bracket_h_buff=0.2)
    m.get_brackets().set_color(col); return m.scale(sc)
def pm(*rows): return r"\begin{pmatrix}" + r" \\ ".join(" & ".join(str(x) for x in r) for r in rows) + r"\end{pmatrix}"
def col(*xs): return pm(*[[x] for x in xs])

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"MATHÉMATIQUES \;·\; PT", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Matrices -- Chapitre 3}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Trace, matrices semblables et calcul par blocs", sc=0.88).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        de = M(r"B \overset{?}{=} P^{-1}AP", sc=0.95, color=BLEU).move_to([-2.3, 0.5, 0])
        dt = T(r"le \textbf{même} endomorphisme ?", sc=0.72, color=JAUNE).next_to(de, RIGHT, buff=0.7)
        self.at(self.a("a2", "comment savoir"), Ecrire(de, rt=0.8)); self.play(Ecrire(dt, rt=0.8))
        items = []
        for k, (txt, c) in enumerate([("La trace", BLEU), ("Matrices semblables", VERT), ("Prouver ou réfuter une similitude", ORANGE),
                                       ("Calcul par blocs, sous-espaces stables", ROUGE), ("Exercice résolu : une rotation cachée", JAUNE)]):
            y = -0.75 - 0.6*k
            items.append(VGroup(carte(k+1, c, -3.6, y), pos(T(txt, sc=0.78), -3.0, y)))
        for it, (sid, fr) in zip(items, [("a3", "la trace"), ("a3", "les matrices semblables"), ("a3", "comment prouver"),
                                         ("a3", "puis le calcul par blocs"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"3.1 -- La trace", "Trace")
        d = pos(M(r"\operatorname{tr} A = \sum_{i} a_{ii}", sc=0.9, color=BLEU), -6.3, 2.15)
        dl = pos(T(r"linéaire, \;$\operatorname{tr}(A^\top) = \operatorname{tr} A$", sc=0.68, color=GRIS), -2.4, 2.15)
        self.ecr(self.a("b1", "La trace d'une matrice"), d, rt=0.8); self.ecr(self.a("b1", "Elle est linéaire"), dl, rt=0.9)
        f = M(r"\operatorname{tr}(AB) = \operatorname{tr}(BA)", sc=1.3, color=JAUNE).move_to([0, 1.05, 0])
        self.ecr(self.a("b2", "propriété magique"), f, rt=0.9); self.play(Create(enc(f, col=JAUNE)), run_time=0.4)
        p1 = pos(M(r"\operatorname{tr}(AB) = \sum_i (AB)_{ii} = \sum_i \sum_k a_{ik}\,b_{ki}", sc=0.85), -6.3, -0.2)
        p2 = pos(M(r"= \sum_k \sum_i b_{ki}\,a_{ik} = \sum_k (BA)_{kk} = \operatorname{tr}(BA)", sc=0.85), -4.75, -1.25)
        self.ecr(self.a("b3", "La preuve en direct"), p1, rt=1.6); self.ecr(self.a("b4", "On échange"), p2, rt=1.6)
        ex = pos(M(r"A = " + pm([1, 2], [3, 4]) + r",\ B = " + pm([0, 1], [1, 0]) + r" :\ AB = " + pm([2, 1], [4, 3]) + r" \neq BA = " + pm([3, 4], [1, 2]), r"\;\;\operatorname{tr} = 5", sc=0.7), -6.3, -2.45)
        ex[1].set_color(VERT)
        self.at(self.a("b5", "Exemple"), Ecrire(ex[0], rt=1.6)); self.at(self.a("b5", "mais elles ont la même trace"), Ecrire(ex[1], rt=0.5))
        w = pos(T(r"circulaire seulement : $\operatorname{tr}(ABC) = \operatorname{tr}(BCA)$, mais en général $\neq \operatorname{tr}(BAC)$", sc=0.64, color=ROUGE), -6.3, -3.45)
        self.ecr(self.a("b6", "Attention"), w, rt=1.5)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"3.1 -- Deux résultats grâce à la trace", "Trace")
        q = pos(M(r"AB - BA = I_n \ \ ?", sc=1.05), -6.3, 1.85)
        self.ecr(self.a("c2", "Premier résultat"), q, rt=0.8)
        r = pos(M(r"\operatorname{tr}(AB) - \operatorname{tr}(BA) = 0", r"\;\neq\; \operatorname{tr}(I_n) = n", sc=0.9), -6.3, 0.85)
        im = T(r"\textbf{impossible} !", sc=0.8, color=ROUGE).next_to(r, RIGHT, buff=0.5)
        self.at(self.a("c3", "À gauche"), Ecrire(r[0], rt=1.0)); self.at(self.a("c3", "À droite"), Ecrire(r[1], rt=0.8))
        self.at(self.a("c3", "Impossible"), FadeIn(im, scale=1.3), run_time=0.4)
        p = pos(T(r"\textbf{Trace d'un projecteur} = rang", sc=0.85, color=VERT), -6.3, -0.55)
        self.ecr(self.a("c4", "Deuxième résultat"), p, rt=0.9)
        m = pos(M(r"\operatorname{Mat}(p) = \operatorname{diag}(\underbrace{1, \ldots, 1}_{\dim \operatorname{Im} p}, 0, \ldots, 0)", sc=0.85), -6.3, -1.75)
        t = pos(T(r"trace = nombre de 1 = $\dim \operatorname{Im} p$ = rang", sc=0.75, color=JAUNE), -6.3, -3.0)
        self.ecr(self.a("c5", "Dans une base adaptée"), m, rt=1.4); self.ecr(self.a("c5", "La trace compte"), t, rt=1.1)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"3.2 -- Matrices semblables", "Semblables")
        d = M(r"B = P^{-1}AP", r"\qquad P \text{ inversible}", sc=1.15, color=JAUNE).move_to([0, 1.95, 0]); d[1].set_color(GRIS)
        self.ecr(self.a("d1", "Deux matrices carrées"), d, rt=1.0); self.play(Create(enc(d[0], col=JAUNE)), run_time=0.4)
        s = T(r"le \textbf{même endomorphisme} dans deux bases", sc=0.75, color=BLEU).move_to([0, 1.05, 0])
        self.ecr(self.a("d2", "Traduction"), s, rt=1.0)
        inv = ["rang", "trace", "déterminant", "polynôme caractéristique", "valeurs propres"]
        ch = VGroup(*[T(x, sc=0.66, color=VERT) for x in inv]).arrange(RIGHT, buff=0.45).move_to([0, 0.05, 0])
        sep = VGroup(*[T(r"·", sc=0.66, color=GRIS).move_to((ch[i].get_right() + ch[i+1].get_left())/2) for i in range(len(inv) - 1)])
        self.at(self.a("d3", "Le rang"), LaggedStart(*[FadeIn(x, shift=UP*0.1) for x in ch], lag_ratio=0.35), FadeIn(sep), run_time=1.6)
        p = pos(M(r"B^2 = P^{-1}A", r"P\,P^{-1}", r"AP", r"\;=\; P^{-1}A^2P", sc=0.95), -6.3, -1.25)
        x1 = Line(p[1].get_corner(DL), p[1].get_corner(UR), color=ROUGE, stroke_width=4)
        self.at(self.a("d4", "Et les puissances suivent"), Ecrire(VGroup(p[0], p[1], p[2]), rt=1.1))
        self.at(self.a("d4", "s'annulent"), Create(x1), run_time=0.4); self.play(Ecrire(p[3], rt=0.7))
        k = pos(M(r"B^k = P^{-1}A^kP", sc=1.0, color=JAUNE), -6.3, -2.55)
        self.ecr(self.a("d4", "Et de même"), k, rt=0.8)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"3.3 -- Prouver qu'elles ne sont pas semblables", "Semblables")
        m = pos(T(r"Méthode : un \textbf{invariant} qui diffère", sc=0.8, color=ORANGE), -6.3, 2.1)
        self.ecr(self.a("e1", "On cherche un invariant"), m, rt=0.9)
        e = pos(M(r"\operatorname{diag}(1, 2)\ \text{et}\ \operatorname{diag}(1, 3) :\ \operatorname{tr} = 3 \neq 4", sc=0.85), -6.3, 1.35)
        ex = T(r"pas semblables", sc=0.7, color=ROUGE).next_to(e, RIGHT, buff=0.5)
        self.ecr(self.a("e2", "Facile ici"), e, rt=1.2); self.at(self.a("e2", "Pas semblables"), FadeIn(ex), run_time=0.4)
        mt = pos(M(r"I_2 = " + pm([1, 0], [0, 1]) + r"\qquad T = " + pm([1, 1], [0, 1]), sc=0.88), -6.3, 0.15)
        iv = pos(T(r"trace $2 = 2$, \;déterminant $1 = 1$, \;rang $2 = 2$, \;$\chi = (X - 1)^2$", sc=0.68, color=VERT), -6.3, -0.8)
        self.at(self.a("e3", "Mais voici un piège"), Ecrire(mt, rt=1.0)); self.ecr(self.a("e3", "Même trace"), iv, rt=2.2)
        r = pos(M(r"P^{-1} I_2 P = I_2 \neq T", sc=0.95, color=ROUGE), -6.3, -1.8)
        rt = T(r"\textbf{pas semblables} !", sc=0.75, color=ROUGE).next_to(r, RIGHT, buff=0.5)
        self.at(self.a("e4", "Et pourtant"), FadeIn(rt), run_time=0.4); self.ecr(self.a("e4", "Car pour toute"), r, rt=1.0)
        s = pos(M(r"\operatorname{rg}(I_2 - I_2) = 0 \;\neq\; \operatorname{rg}(T - I_2) = 1", sc=0.9, color=JAUNE), -6.3, -2.95)
        self.ecr(self.a("e5", "L'invariant qui les sépare"), s, rt=1.3)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"3.3 -- Prouver qu'elles sont semblables", "Semblables")
        m = pos(T(r"Méthode : trouver une \textbf{base} où la matrice est la bonne", sc=0.8, color=VERT), -6.3, 2.1)
        self.ecr(self.a("f1", "On cherche une base"), m, rt=1.2)
        b = pos(M(r"B = " + pm([2, 5], [0, 1]), sc=0.95), -6.3, 1.0)
        self.ecr(self.a("f2", "Exemple en direct"), b, rt=0.8)
        v1 = pos(M(r"B" + col(1, 0) + r" = " + col(2, 0) + r" = 2" + col(1, 0), sc=0.85), -6.3, -0.4)
        v2 = pos(M(r"B" + col(5, -1) + r" = " + col(5, -1), sc=0.85), -0.3, -0.4)
        self.ecr(self.a("f3", "B fois un, zéro"), v1, rt=1.1); self.ecr(self.a("f3", "Et B fois cinq"), v2, rt=1.1)
        n = pos(M(r"\text{base } \big((5, -1),\ (1, 0)\big) :\quad \operatorname{Mat} = " + pm([1, 0], [0, 2]), sc=0.88, color=JAUNE), -6.3, -1.75)
        self.ecr(self.a("f4", "Dans la base"), n, rt=1.4); self.play(Create(enc(n, col=JAUNE, buff=0.12)), run_time=0.3)
        c = pos(M(pm([1, 0], [0, 2]) + r"\ \text{ et }\ " + pm([2, 5], [0, 1]) + r"\ \text{ semblables}", sc=0.85, color=VERT), -6.3, -3.0)
        self.ecr(self.a("f5", "Conclusion"), c, rt=1.3)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"3.3 -- À vous : semblables ou pas ?", "Semblables")
        cad = RoundedRectangle(width=12.4, height=1.6, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, 1.7, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.72, color=JAUNE), -5.9, 1.7)
        en = M(pm([2, 1], [0, 2]) + r"\ \text{ et }\ 2I_2 \;:\;", r"\text{ semblables ?}", sc=0.85).next_to(tq, RIGHT, buff=0.6); en[1].set_color(JAUNE)
        self.at(self.t("g1"), Create(cad), Ecrire(tq, rt=0.4), run_time=0.5)
        self.at(self.a("g1", "La matrice deux, un"), Ecrire(en, rt=1.3))
        pa, arc = chrono(5.7, 1.7)
        self.jusqua(self.PH["g1"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("g2") - self.renderer.time - 0.1), rate_func=linear)
        r1 = pos(M(r"P^{-1}(2I_2)P = 2I_2 \quad\text{pour toute } P", sc=0.9, color=JAUNE), -6.0, 0.0)
        self.at(self.a("g2", "Réponse"), FadeOut(pa), FadeOut(arc), Ecrire(r1, rt=1.1))
        r2 = pos(M(pm([2, 1], [0, 2]) + r" \neq 2I_2 \;\Longrightarrow\; \text{pas semblables}", sc=0.9, color=ROUGE), -6.0, -1.35)
        r3 = pos(T(r"(même trace 4, même déterminant 4 : les invariants ne suffisent pas)", sc=0.62, color=GRIS), -6.0, -2.35)
        self.ecr(self.a("g3", "Or la matrice"), r2, rt=1.2); self.ecr(self.a("g3", "même si trace"), r3, rt=1.1)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"3.4 -- Le calcul par blocs", "Blocs")
        f = M(r"\begin{pmatrix} A & B \\ C & D \end{pmatrix}\begin{pmatrix} A' & B' \\ C' & D' \end{pmatrix} = \begin{pmatrix} AA' + BC' & AB' + BD' \\ CA' + DC' & CB' + DD' \end{pmatrix}", sc=0.78).move_to([-0.6, 1.75, 0])
        o = T(r"l'ordre compte !", sc=0.65, color=ROUGE).next_to(f, RIGHT, buff=0.3)
        self.at(self.a("h1", "On découpe"), Ecrire(f, rt=1.6)); self.at(self.a("h2", "en respectant l'ordre"), FadeIn(o), run_time=0.4)
        d = pos(M(r"M = \begin{pmatrix} A & I_2 \\ 0 & 2I_2 \end{pmatrix}, \qquad A = " + pm([1, 1], [0, 1]), sc=0.85), -6.3, 0.2)
        self.ecr(self.a("h3", "Exemple en direct"), d, rt=1.3)
        Mm = mat([["A^2", "A + 2I_2"], ["0", "4I_2"]], sc=0.8, h=2.6).move_to([-3.2, -1.55, 0])
        lm = M(r"M^2 =", sc=0.85).next_to(Mm, LEFT, buff=0.2)
        e = Mm.get_entries()
        self.at(self.a("h4", "Bloc en haut à gauche"), FadeIn(lm), FadeIn(Mm.get_brackets()), FadeIn(e[0]), run_time=0.5)
        self.at(self.a("h4", "Bloc en bas à droite"), FadeIn(e[3]), run_time=0.4)
        self.at(self.a("h4", "Bloc en bas à gauche"), FadeIn(e[2]), run_time=0.4)
        ca = pos(M(r"A \times I_2 + I_2 \times 2I_2 = A + 2I_2", sc=0.75, color=ORANGE), -6.3, -2.85)
        self.at(self.a("h5", "Et en haut à droite"), Ecrire(ca, rt=1.2)); self.play(FadeIn(e[1]), run_time=0.4)
        nm = M(r"= " + pm([1, 2, 3, 1], [0, 1, 0, 3], [0, 0, 4, 0], [0, 0, 0, 4]), sc=0.75, color=JAUNE).next_to(Mm, RIGHT, buff=0.3)
        self.ecr(self.a("h5", "Une matrice quatre"), nm, rt=1.2)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"3.4 -- Déterminant par blocs", "Blocs")
        f = M(r"\det\begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \det(A)\,\det(D)", sc=1.05, color=JAUNE).move_to([0, 1.9, 0])
        self.ecr(self.a("i1", "Pour une matrice triangulaire par blocs"), f, rt=1.3); self.play(Create(enc(f, col=JAUNE)), run_time=0.4)
        Mm = mat([[1, 2, 5, 7], [3, 4, 6, 8], [0, 0, 2, 1], [0, 0, 1, 1]], sc=0.78).move_to([-3.3, -0.35, 0])
        lm = M(r"M =", sc=0.85).next_to(Mm, LEFT, buff=0.2)
        e = Mm.get_entries()
        ra = SurroundingRectangle(VGroup(e[0], e[1], e[4], e[5]), color=BLEU, buff=0.1)
        rd = SurroundingRectangle(VGroup(e[10], e[11], e[14], e[15]), color=VERT, buff=0.1)
        rb = SurroundingRectangle(VGroup(e[2], e[3], e[6], e[7]), color=GRIS, buff=0.1)
        lb = T(r"n'importe quoi", sc=0.6, color=GRIS).next_to(Mm, RIGHT, buff=0.35).align_to(rb, UP)
        self.at(self.a("i2", "Exemple"), FadeIn(lm), Ecrire(Mm, rt=1.2)); self.play(Create(ra), Create(rd), run_time=0.5)
        self.at(self.a("i2", "Le bloc en haut à droite"), Create(rb), FadeIn(lb), run_time=0.5)
        c = pos(M(r"\det M = \det" + pm([1, 2], [3, 4]) + r"\times\det" + pm([2, 1], [1, 1]) + r" = (-2) \times 1 = -2", sc=0.82, color=JAUNE), -6.3, -2.35)
        self.ecr(self.a("i3", "Le déterminant de un"), c, rt=1.8)
        d = pos(T(r"diagonale par blocs : puissances, inverse, polynômes \textbf{bloc par bloc}", sc=0.7, color=VERT), -6.3, -3.4)
        self.ecr(self.a("i4", "Et pour une matrice diagonale"), d, rt=1.3)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"3.5 -- Sous-espaces stables", "Blocs")
        d = pos(M(r"F \text{ stable par } u \iff u(F) \subset F", sc=0.9), -6.3, 2.05)
        self.ecr(self.a("j1", "Un sous-espace F"), d, rt=1.0)
        t = pos(M(r"\operatorname{Mat}_{\mathcal{B}}(u) = \begin{pmatrix} A & B \\ 0 & D \end{pmatrix}", r"\quad\text{(}\mathcal{B}\text{ commence par une base de } F\text{)}", sc=0.82), -6.3, 0.95)
        t[1].set_color(GRIS)
        self.at(self.a("j2", "Prenons une base"), Ecrire(t[1], rt=1.1)); self.at(self.a("j2", "Alors F est stable"), Ecrire(t[0], rt=1.0))
        g = pos(M(r"E = F \oplus G,\ F \text{ et } G \text{ stables} \;\Longrightarrow\; \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix}", sc=0.82), -6.3, -0.35)
        self.ecr(self.a("j3", "Et si E"), g, rt=1.3)
        r = pos(M(r"\begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}", sc=0.8), -6.3, -2.0)
        lp = T(r"plan $\perp$ axe", sc=0.58, color=BLEU).next_to(r, RIGHT, buff=0.25).shift(UP*0.35)
        la = T(r"axe", sc=0.58, color=VERT).next_to(r, RIGHT, buff=0.25).shift(DOWN*0.45)
        self.at(self.a("j4", "une rotation de l'espace"), Ecrire(r, rt=1.4)); self.at(self.a("j4", "Dans une base adaptée"), FadeIn(lp), FadeIn(la), run_time=0.5)
        tr = pos(M(r"\operatorname{tr} = 1 + 2\cos\theta", sc=0.95, color=JAUNE), 0.9, -1.75)
        tb = pos(T(r"lisible sur \textbf{n'importe quelle} matrice", sc=0.62, color=GRIS), 0.9, -2.5)
        self.ecr(self.a("j5", "Sa trace vaut"), tr, rt=1.0); self.ecr(self.a("j5", "Et comme la trace"), tb, rt=1.0)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, T(r"$\operatorname{tr}(AB) = \operatorname{tr}(BA)$ ; semblables : même trace, rang, déterminant", sc=0.75), "k2", 1.85),
                (VERT, T(r"Réfuter : un invariant qui diffère ; prouver : une base bien choisie", sc=0.75), "k3", 0.55),
                (ORANGE, T(r"Blocs : calcul dans l'ordre ; bloc nul sous la diagonale = sous-espace stable", sc=0.75), "k4", -0.75)]
        for k, (c, F, sid, y) in enumerate(data):
            cc = carte(k+1, c, -5.9, y); pos(F, -5.3, y)
            self.at(self.t(sid), Create(cc[0]), FadeIn(cc[1]), run_time=0.4); self.play(Ecrire(F, rt=1.7))
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice résolu -- Une rotation cachée", "Exercice résolu")
        A = M(r"A = " + pm([0, 0, 1], [1, 0, 0], [0, 1, 0]), sc=0.95).move_to([0, 1.75, 0])
        self.at(self.a("l2", "Soit A"), Ecrire(A, rt=1.2))
        q1 = pos(T(r"\textbf{1.} Calculer $A^3$.", sc=0.75, color=JAUNE), -6.3, 0.35)
        q2 = pos(T(r"\textbf{2.} Montrer que $D = \operatorname{Vect}(1, 1, 1)$ et $\mathcal{P} : x + y + z = 0$ sont stables par $f$.", sc=0.75, color=JAUNE), -6.3, -0.3)
        q3 = pos(T(r"\textbf{3.} Matrice de $f$ dans $(u_1, u_2, u_3)$ ; reconnaître $f$.", sc=0.75, color=JAUNE), -6.3, -0.95)
        bs = pos(M(r"u_1 = (1, -1, 0),\;\; u_2 = (0, 1, -1),\;\; u_3 = (1, 1, 1)", sc=0.75, color=GRIS), -5.8, -1.55)
        self.ecr(self.a("l3", "Première question"), q1, rt=0.7); self.ecr(self.a("l4", "Deuxième question"), q2, rt=1.6)
        self.ecr(self.a("l5", "Troisième question"), q3, rt=1.2); self.play(Ecrire(bs, rt=1.0))
        ch = M(r"\text{stables} \;\Rightarrow\; \text{diagonale par blocs}", r"\qquad\text{contrôle : la trace}", sc=0.82, color=VERT).move_to([0, -2.75, 0])
        self.at(self.a("l6", "Deux sous-espaces stables"), Ecrire(ch[0], rt=1.0)); self.at(self.a("l6", "Et la trace"), Ecrire(ch[1], rt=0.8))
        self.play(Create(enc(ch, col=VERT)), run_time=0.4)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- La solution, étape par étape", "Exercice résolu")
        c1 = carte(1, BLEU, -6.1, 2.2)
        s1 = pos(M(r"Ae_1 = e_2,\;\ Ae_2 = e_3,\;\ Ae_3 = e_1", r"\qquad A(x, y, z) = (z, x, y)", sc=0.75), -5.55, 2.2)
        self.at(self.t("m1"), Create(c1[0]), FadeIn(c1[1]), run_time=0.4)
        self.at(self.a("m1", "Ses colonnes"), Ecrire(s1[0], rt=1.2)); self.at(self.a("m1", "Autrement dit"), Ecrire(s1[1], rt=0.9))
        s1b = pos(M(r"A^3 = I_3", sc=0.85, color=JAUNE), -5.55, 1.55)
        self.ecr(self.a("m2", "A cube égale"), s1b, rt=0.6)
        c2 = carte(2, VERT, -6.1, 0.75)
        s2 = pos(M(r"f(1, 1, 1) = (1, 1, 1)", r"\;\Rightarrow\; D \text{ stable}", sc=0.75), -5.55, 0.75)
        self.at(self.t("m3"), Create(c2[0]), FadeIn(c2[1]), run_time=0.4)
        self.at(self.a("m3", "f de un, un, un"), Ecrire(s2[0], rt=0.9)); self.at(self.a("m3", "la droite D est stable"), Ecrire(s2[1], rt=0.6))
        s2b = pos(M(r"x + y + z = 0 \;\Rightarrow\; z + x + y = 0", r"\;\Rightarrow\; \mathcal{P} \text{ stable}", sc=0.75), -5.55, 0.1)
        self.at(self.a("m4", "Et si x plus y"), Ecrire(s2b[0], rt=1.0)); self.at(self.a("m4", "le plan P est stable"), Ecrire(s2b[1], rt=0.6))
        c3 = carte(3, ORANGE, -6.1, -0.75)
        s3 = [pos(M(s, sc=0.75), x, -0.75) for s, x in ((r"f(u_1) = u_2,", -5.55), (r"f(u_2) = -u_1 - u_2,", -3.15), (r"f(u_3) = u_3", 0.7))]
        self.at(self.t("m5"), Create(c3[0]), FadeIn(c3[1]), run_time=0.4)
        self.at(self.a("m5", "f de u un"), Ecrire(s3[0], rt=0.7)); self.at(self.a("m5", "Et f de u deux"), Ecrire(s3[1], rt=0.9))
        self.at(self.a("m5", "Et f de u trois"), Ecrire(s3[2], rt=0.6))
        s3b = pos(M(r"\operatorname{Mat}_{(u_1, u_2, u_3)}(f) = " + pm([0, -1, 0], [1, -1, 0], [0, 0, 1]), sc=0.75, color=JAUNE), -5.55, -2.05)
        self.ecr(self.a("m6", "La matrice est diagonale"), s3b, rt=1.3); self.play(Create(enc(s3b, col=JAUNE, buff=0.12)), run_time=0.3)
        c4 = carte(4, ROUGE, 1.0, -1.65)
        v1 = pos(M(r"\operatorname{tr} = -1 + 1 = 0 = \operatorname{tr} A \;\checkmark", sc=0.75), 1.55, -1.65)
        v2 = pos(M(r"1 + 2\cos\theta = 0 \;\Rightarrow\; \theta = \tfrac{2\pi}{3}", sc=0.75, color=JAUNE), 1.55, -2.4)
        self.at(self.t("m7"), Create(c4[0]), FadeIn(c4[1]), run_time=0.4)
        self.at(self.a("m7", "La trace vaut"), Ecrire(v1, rt=1.0)); self.at(self.a("m7", "Et un plus deux cosinus"), Ecrire(v2, rt=1.1))
        cc = pos(T(r"$f$ : rotation d'angle $\frac{2\pi}{3}$ autour de $(1, 1, 1)$ \;$\Rightarrow\;$ $A^3 = I_3$", sc=0.72, color=VERT), -5.55, -3.4)
        self.ecr(self.a("m8", "Conclusion"), cc, rt=1.4)
        self.jusqua(self.t("m9") - 0.2)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        nx = T(r"Chapitre 4 \;$\longrightarrow$\; polynômes de matrices, nilpotentes, puissances", sc=0.8, color=JAUNE).move_to([0, 0.3, 0])
        self.ecr(self.a("m9", "les polynômes de matrices"), nx, rt=1.6)
        self.fin()
