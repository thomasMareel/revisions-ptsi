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
        ti = T(r"\textbf{Matrices -- Chapitre 2}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Changement de base, rang et matrices équivalentes", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        de = M(r"A' = P^{-1}AP", sc=0.95, color=BLEU).move_to([-2.2, 0.5, 0])
        dt = T(r"même application, \textbf{autre base}", sc=0.72, color=JAUNE).next_to(de, RIGHT, buff=0.7)
        self.at(self.a("a2", "le portrait"), Ecrire(de, rt=0.8)); self.ecr(self.a("a2", "mais pas l'application"), dt, rt=0.9)
        items = []
        for k, (txt, c) in enumerate([("Matrice d'une application linéaire", BLEU), ("Matrice de passage, changement de base", VERT), ("Le rang", ORANGE),
                                       ("Matrices équivalentes", ROUGE), ("Exercice résolu : une projection", JAUNE)]):
            y = -0.75 - 0.6*k
            items.append(VGroup(carte(k+1, c, -3.6, y), pos(T(txt, sc=0.78), -3.0, y)))
        for it, (sid, fr) in zip(items, [("a3", "la matrice d'une application"), ("a3", "la matrice de passage"), ("a3", "le rang"),
                                         ("a3", "et les matrices équivalentes"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"2.1 -- Matrice d'une application linéaire", "Applications linéaires")
        r = pos(T(r"colonne $j$ = coordonnées de $f(e_j)$", sc=0.78, color=BLEU), -6.3, 2.15)
        y = pos(M(r"y = f(x) \iff Y = AX", sc=0.85, color=JAUNE), 1.4, 2.15)
        self.ecr(self.a("b1", "Le principe"), r, rt=1.0); self.ecr(self.a("b2", "Et alors"), y, rt=1.0)
        ex = pos(T(r"Exemple : $D$, la dérivation sur $\mathbb{R}_2[X]$, base $(1, X, X^2)$", sc=0.72, color=VERT), -6.3, 1.35)
        self.ecr(self.a("b3", "Exemple en direct"), ex, rt=1.3)
        im = [pos(M(s, sc=0.8), -6.3, yy) for s, yy in ((r"D(1) = 0", 0.45), (r"D(X) = 1", -0.2), (r"D(X^2) = 2X", -0.85))]
        A = mat([[0, 1, 0], [0, 0, 2], [0, 0, 0]], sc=0.85).move_to([-1.9, -0.2, 0])
        la = M(r"A =", sc=0.85).next_to(A, LEFT, buff=0.2)
        self.at(self.a("b4", "La dérivée de un"), Ecrire(im[0], rt=0.6), FadeIn(la), FadeIn(A.get_brackets())); self.play(FadeIn(A.get_columns()[0]), run_time=0.4)
        self.at(self.a("b4", "La dérivée de X, c'est un"), Ecrire(im[1], rt=0.6)); self.play(FadeIn(A.get_columns()[1]), run_time=0.4)
        self.at(self.a("b4", "La dérivée de X carré"), Ecrire(im[2], rt=0.6)); self.play(FadeIn(A.get_columns()[2]), run_time=0.4)
        t1 = pos(M(r"3 + 2X + 5X^2 \;\longleftrightarrow\; " + col(3, 2, 5), sc=0.75), 0.9, 0.55)
        self.ecr(self.a("b5", "Testons"), t1, rt=1.2)
        t2 = pos(M(r"A" + col(3, 2, 5) + r" = " + col(2, 10, 0), sc=0.75), 0.9, -1.15)
        t3 = pos(T(r"$2 + 10X$ : c'est bien la dérivée \;$\checkmark$", sc=0.7, color=VERT), 0.9, -2.45)
        self.ecr(self.a("b6", "On multiplie"), t2, rt=1.2); self.ecr(self.a("b6", "C'est-à-dire"), t3, rt=1.0)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"2.1 -- Composition et produit", "Applications linéaires")
        p = M(r"\operatorname{Mat}(g \circ f) = \operatorname{Mat}(g)\,\operatorname{Mat}(f)", sc=1.05, color=JAUNE).move_to([0, 1.9, 0])
        self.ecr(self.a("c1", "La propriété clé"), p, rt=1.2); self.play(Create(enc(p, col=JAUNE)), run_time=0.4)
        a2 = pos(M(r"A^2 = " + pm([0, 0, 2], [0, 0, 0], [0, 0, 0]), sc=0.85), -6.3, 0.3)
        d2 = pos(T(r"$D^2(X^2) = 2$ \;$\checkmark$", sc=0.7, color=VERT), -2.4, 0.3)
        self.ecr(self.a("c2", "Exemple"), a2, rt=1.0); self.ecr(self.a("c2", "La dérivée seconde"), d2, rt=0.8)
        a3 = pos(M(r"A^3 = 0", sc=0.95, color=ROUGE), 1.6, 0.3)
        self.ecr(self.a("c3", "Et A au cube"), a3, rt=0.6)
        b = pos(T(r"$f$ bijectif $\iff$ $\operatorname{Mat}(f)$ inversible", sc=0.78, color=BLEU), -6.3, -1.45)
        d = pos(T(r"$\dim \mathcal{L}(E, F) = np$", sc=0.78, color=BLEU), -6.3, -2.3)
        self.ecr(self.a("c4", "Un endomorphisme est bijectif"), b, rt=1.1); self.ecr(self.a("c4", "Et l'espace"), d, rt=0.8)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"2.2 -- La matrice de passage", "Changement de base")
        b = pos(M(r"\mathcal{B}\ (\text{ancienne}) \;\longrightarrow\; \mathcal{B}'\ (\text{nouvelle})", sc=0.85), -6.3, 2.1)
        self.ecr(self.a("d1", "Soit B"), b, rt=1.0)
        d = pos(T(r"$P$ : colonnes = \textbf{nouveaux} vecteurs écrits dans l'\textbf{ancienne} base", sc=0.76, color=JAUNE), -6.3, 1.3)
        self.ecr(self.a("d2", "La matrice de passage"), d, rt=1.5)
        self.at(self.a("d2", "nouveaux dans l'ancienne"), Indicate(d, color=JAUNE, scale_factor=1.05), run_time=0.7)
        x = pos(M(r"X = PX'", r"\qquad \text{(ancienne} = P \times \text{nouvelle)}", sc=0.95), -6.3, 0.35); x[1].set_color(GRIS)
        self.at(self.a("d3", "Et elle relie"), Ecrire(x[0], rt=0.6)); self.play(Ecrire(x[1], rt=0.9))
        e = pos(M(r"u_1 = (1, 1),\;\; u_2 = (1, -1)", r"\;\;\Longrightarrow\;\; P = " + pm([1, 1], [1, -1]), sc=0.85), -6.3, -0.95)
        self.at(self.a("d4", "Exemple"), Ecrire(e[0], rt=0.9)); self.at(self.a("d4", "P a pour colonnes"), Ecrire(e[1], rt=0.8))
        v = pos(M(r"X' = " + col(2, 1) + r" :\ 2u_1 + u_2", r"\qquad X = PX' = " + col(3, 1), sc=0.85), -6.3, -2.45); v[1].set_color(VERT)
        self.at(self.a("d5", "Un vecteur de nouvelles"), Ecrire(v[0], rt=1.0)); self.at(self.a("d5", "P fois deux"), Ecrire(v[1], rt=0.9))
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"2.2 -- La formule de changement de base", "Changement de base")
        f = M(r"A' = ", r"P^{-1}", r"A", r"P", sc=1.45, color=JAUNE).move_to([-2.4, 1.85, 0])
        self.at(self.a("e1", "sa matrice dans la nouvelle base"), Ecrire(f, rt=0.9)); self.play(Create(enc(f, col=JAUNE)), run_time=0.4)
        l = [pos(M(s, sc=0.88), x, 0.15) for s, x in ((r"Y = AX", -6.3), (r"X = PX'", -3.9), (r"Y = PY'", -1.5))]
        self.at(self.a("e2", "Y égale A X"), Ecrire(l[0], rt=0.5)); self.at(self.a("e2", "X égale P X prime"), Ecrire(l[1], rt=0.5))
        self.at(self.a("e2", "Et Y égale P Y prime"), Ecrire(l[2], rt=0.5))
        d = pos(M(r"PY' = APX'", r"\;\Longrightarrow\; Y' = P^{-1}AP\,X'", sc=0.88), -6.3, -0.75)
        self.at(self.a("e3", "Donc P Y prime"), Ecrire(d[0], rt=0.6)); self.at(self.a("e3", "On multiplie par P inverse"), Ecrire(d[1], rt=0.9))
        lab = [(3, r"$P$ : nouvelles coordonnées $\to$ anciennes", BLEU, "P passe", 2.3), (2, r"$A$ : applique $f$", VERT, "A applique f", 1.85),
               (1, r"$P^{-1}$ : retour dans la nouvelle base", ORANGE, "et P inverse revient", 1.4)]
        for i, tx, c, fr, yy in lab:
            t = pos(T(tx, sc=0.6, color=c), 0.6, yy)
            self.at(self.a("e4", fr), FadeIn(t, shift=LEFT*0.1), Indicate(f[i], color=c), run_time=0.6)
        er = pos(T(r"\textbf{Erreur classique} : $PAP^{-1}$ \;$\times$", sc=0.8, color=ROUGE), -6.3, -2.1)
        self.ecr(self.a("e5", "Attention"), er, rt=0.9)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"2.2 -- Exemple en direct : la bonne base", "Changement de base")
        a = pos(M(r"A = " + pm([3, 1], [1, 3]), sc=0.9), -6.3, 1.75)
        u = pos(T(r"$u_1 = (1, 1)$, \;$u_2 = (1, -1)$", sc=0.72, color=GRIS), -2.4, 1.75)
        self.at(self.a("f1", "Soit f de matrice"), Ecrire(a, rt=0.8), FadeIn(u))
        f1 = pos(M(r"Au_1 = " + col(4, 4), r" = 4u_1", sc=0.85), -6.3, 0.2); f1[1].set_color(VERT)
        f2 = pos(M(r"Au_2 = " + col(2, -2), r" = 2u_2", sc=0.85), -1.4, 0.2); f2[1].set_color(VERT)
        self.at(self.a("f2", "Calculons f de u un"), Ecrire(f1[0], rt=0.9)); self.at(self.a("f2", "C'est quatre fois"), Ecrire(f1[1], rt=0.5))
        self.at(self.a("f3", "Et f de u deux"), Ecrire(f2[0], rt=0.9)); self.at(self.a("f3", "C'est deux fois"), Ecrire(f2[1], rt=0.5))
        m = pos(M(r"\operatorname{Mat}_{(u_1, u_2)}(f) = " + pm([4, 0], [0, 2]), sc=0.9, color=JAUNE), -6.3, -1.3)
        mn = pos(T(r"lue sur les images, sans calculer $P^{-1}$", sc=0.65, color=GRIS), -1.0, -1.3)
        self.at(self.a("f4", "Donc dans la nouvelle base"), Ecrire(m, rt=1.0)); self.play(Create(enc(m, col=JAUNE, buff=0.12)), run_time=0.3)
        self.ecr(self.a("f4", "On la lit"), mn, rt=1.0)
        p = pos(M(r"A^n = P" + pm([r"4^n", 0], [0, r"2^n"]) + r"P^{-1}", sc=0.9, color=BLEU), -6.3, -2.85)
        self.ecr(self.a("f5", "Et le bénéfice"), p, rt=1.2)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"2.2 -- À vous : changer de base", "Changement de base")
        cad = RoundedRectangle(width=12.4, height=1.7, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, 1.65, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.72, color=JAUNE), -5.9, 1.65)
        en = pos(M(r"A = " + pm([5, -2], [4, -1]) + r",\;\; u_1 = (1, 2),\; u_2 = (1, 1)", r"\quad \operatorname{Mat}_{(u_1, u_2)}(f)\ ?", sc=0.78), -4.4, 1.65)
        en[1].set_color(JAUNE)
        self.at(self.t("g1"), Create(cad), Ecrire(tq, rt=0.4), run_time=0.5)
        self.at(self.a("g1", "Voici la matrice A"), Ecrire(en[0], rt=1.4)); self.at(self.a("g1", "Quelle est la matrice"), Ecrire(en[1], rt=0.7))
        pa, arc = chrono(5.85, 1.65)
        self.jusqua(self.PH["g1"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("g2") - self.renderer.time - 0.1), rate_func=linear)
        r1 = pos(M(r"Au_1 = " + col(1, 2) + r" = u_1", sc=0.85), -6.0, -0.15)
        self.at(self.a("g2", "Réponse"), FadeOut(pa), FadeOut(arc), Ecrire(r1, rt=0.9))
        r2 = pos(M(r"Au_2 = " + col(3, 3) + r" = 3u_2", sc=0.85), -1.4, -0.15)
        r3 = pos(M(r"\operatorname{Mat}_{(u_1, u_2)}(f) = " + pm([1, 0], [0, 3]), sc=0.9, color=JAUNE), -6.0, -1.65)
        self.ecr(self.a("g3", "Et A fois u deux"), r2, rt=0.9); self.ecr(self.a("g3", "La matrice est diagonale"), r3, rt=1.0)
        self.play(Create(enc(r3, col=JAUNE, buff=0.12)), run_time=0.3)
        v = pos(T(r"contrôle : trace $4 = 4$, \;déterminant $3 = 3$ \;$\checkmark$", sc=0.72, color=VERT), -6.0, -2.95)
        self.ecr(self.a("g4", "Vérification"), v, rt=1.2)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"2.3 -- Le rang", "Rang")
        d = pos(T(r"$\operatorname{rg} A$ = dimension de l'espace engendré par les \textbf{colonnes}", sc=0.78, color=BLEU), -6.3, 2.1)
        self.ecr(self.a("h1", "Le rang d'une matrice"), d, rt=1.4)
        p = pos(M(r"\operatorname{rg}(QAP) = \operatorname{rg}(A) \quad (P, Q \text{ inversibles})", sc=0.88, color=JAUNE), -6.3, 1.15)
        pv = pos(T(r"$\Rightarrow$ opérations sur lignes et colonnes : rang = \textbf{nombre de pivots}", sc=0.72), -6.3, 0.4)
        self.ecr(self.a("h2", "multiplier par une matrice inversible"), p, rt=1.3); self.ecr(self.a("h2", "Donc les opérations"), pv, rt=1.4)
        t = pos(M(r"\operatorname{rg}(A^\top) = \operatorname{rg}(A)", sc=0.95, color=VERT), -6.3, -0.75)
        tn = pos(T(r"lignes et colonnes : même dimension", sc=0.65, color=GRIS), -2.0, -0.75)
        self.ecr(self.a("h3", "le rang de la transposée"), t, rt=0.9); self.ecr(self.a("h3", "Les lignes et les colonnes"), tn, rt=1.0)
        r = pos(M(r"\operatorname{rg} A + \dim\ker A = p \qquad (p \text{ colonnes})", sc=0.95, color=ORANGE), -6.3, -2.05)
        self.ecr(self.a("h4", "Et le théorème du rang"), r, rt=1.2); self.play(Create(enc(r, col=ORANGE)), run_time=0.4)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"2.3 -- Rang et noyau en direct", "Rang")
        A = mat([[1, 2, 1, 0], [2, 4, 0, 2], [1, 2, -1, 2]], sc=0.75).move_to([-3.4, 1.0, 0])
        la = M(r"A =", sc=0.85).next_to(A, LEFT, buff=0.2)
        self.at(self.a("i1", "En direct"), FadeIn(la), Ecrire(A, rt=1.0))
        o1 = pos(M(r"L_2 \leftarrow L_2 - 2L_1,\;\; L_3 \leftarrow L_3 - L_1", sc=0.7, color=ORANGE), 0.3, 2.05)
        B = mat([[1, 2, 1, 0], [0, 0, -2, 2], [0, 0, -2, 2]], sc=0.75).move_to([3.4, 1.0, 0])
        sim = M(r"\sim", sc=1.0).move_to([0, 1.0, 0])
        self.at(self.a("i2", "L deux reçoit"), Ecrire(o1, rt=0.9)); self.play(FadeIn(sim), Ecrire(B, rt=1.0))
        self.at(self.a("i2", "Les deux lignes deviennent"), Indicate(VGroup(B.get_rows()[1], B.get_rows()[2]), color=JAUNE, scale_factor=1.1), run_time=0.7)
        o2 = pos(M(r"L_3 \leftarrow L_3 - L_2", sc=0.7, color=ORANGE), 0.3, 2.05)
        C = mat([[1, 2, 1, 0], [0, 0, -2, 2], [0, 0, 0, 0]], sc=0.75).move_to([3.4, 1.0, 0])
        self.at(self.a("i3", "L trois reçoit"), ReplacementTransform(o1, o2), ReplacementTransform(B, C), run_time=0.8)
        e = C.get_entries()
        p1 = Circle(radius=0.24, color=JAUNE, stroke_width=3).move_to(e[0]); p2 = Circle(radius=0.3, color=JAUNE, stroke_width=3).move_to(e[6])
        rg = pos(M(r"\operatorname{rg} A = 2", sc=1.0, color=JAUNE), -6.3, -0.75)
        self.at(self.a("i3", "Il reste deux pivots"), Create(p1), Create(p2), run_time=0.5); self.ecr(self.a("i3", "Le rang vaut"), rg, rt=0.5)
        k = pos(M(r"\dim\ker A = 4 - 2 = 2", sc=0.9, color=ORANGE), -2.9, -0.75)
        self.ecr(self.a("i4", "Théorème du rang"), k, rt=0.9)
        s = pos(M(r"x + 2y + z = 0,\;\; -2z + 2t = 0", r"\;\Longrightarrow\; z = t,\;\; x = -2y - t", sc=0.8), -6.3, -1.85)
        n = pos(M(r"\ker A = \operatorname{Vect}\big((-2, 1, 0, 0),\ (-1, 0, 1, 1)\big)", sc=0.85, color=JAUNE), -6.3, -2.85)
        self.at(self.a("i5", "On le décrit"), Ecrire(s[0], rt=0.8)); self.play(Ecrire(s[1], rt=0.9))
        self.ecr(self.a("i5", "Deux paramètres libres"), n, rt=1.3)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"2.4 -- Matrices équivalentes", "Matrices équivalentes")
        d = pos(M(r"B = QAP", r"\qquad P, Q \text{ inversibles}", sc=0.95), -6.3, 2.05); d[1].set_color(GRIS)
        self.ecr(self.a("j1", "Deux matrices de même taille"), d, rt=0.9)
        s = pos(T(r"même application linéaire, bases changées \textbf{au départ et à l'arrivée}", sc=0.7, color=GRIS), -6.3, 1.3)
        self.ecr(self.a("j2", "Autrement dit"), s, rt=1.3)
        t = M(r"\operatorname{rg} A = r \;\Longrightarrow\; A \text{ équivalente à } J_r = \begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}", sc=0.95, color=JAUNE).move_to([0, 0.1, 0])
        self.ecr(self.a("j3", "toute matrice de rang r"), t, rt=1.5); self.play(Create(enc(t, col=JAUNE)), run_time=0.4)
        p1 = pos(T(r"base d'un supplémentaire $S$ de $\ker f$, puis base de $\ker f$", sc=0.65), -6.3, -1.3)
        p2 = pos(T(r"$\to$ images : base de $\operatorname{Im} f$, complétée à l'arrivée $\;\to\;$ matrice $J_r$", sc=0.65), -6.3, -1.85)
        self.ecr(self.a("j4", "L'idée de la preuve"), p1, rt=1.4); self.ecr(self.a("j4", "Leurs images"), p2, rt=1.4)
        c = T(r"équivalentes $\iff$ \textbf{même rang}", sc=0.9, color=ORANGE).move_to([0, -2.95, 0])
        self.ecr(self.a("j5", "Conclusion"), c, rt=0.9); self.play(Create(enc(c, col=ORANGE, buff=0.15)), run_time=0.4)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"2.4 -- Les matrices de rang 1", "Matrices équivalentes")
        a = pos(M(r"A = X\,Y^\top", r"\qquad\text{(colonne} \times \text{ligne)}", sc=1.0, color=JAUNE), -6.3, 2.0); a[1].set_color(GRIS)
        self.ecr(self.a("k2", "Donc A s'écrit"), a, rt=1.0)
        e = pos(M(pm(1, 2, 3) if False else pm([1, 2, 3], [2, 4, 6], [-1, -2, -3]) + r" = " + col(1, 2, -1) + pm([1, 2, 3]), sc=0.82), -6.3, 0.55)
        self.ecr(self.a("k3", "Exemple"), e, rt=1.4)
        f = pos(M(r"A^2 = X\,", r"(Y^\top X)", r"\,Y^\top", r"\;=\; \operatorname{tr}(A)\,A", sc=0.95), -6.3, -0.95)
        f[3].set_color(JAUNE)
        br = Brace(f[1], DOWN, color=VERT); bt = T(r"un nombre : $\operatorname{tr} A$", sc=0.6, color=VERT).next_to(br, DOWN, buff=0.08)
        self.at(self.a("k4", "Et alors"), Ecrire(VGroup(f[0], f[1], f[2]), rt=1.0))
        self.at(self.a("k4", "Or Y transposée X"), Create(br), FadeIn(bt), run_time=0.6)
        self.at(self.a("k4", "Donc A au carré"), Ecrire(f[3], rt=0.7)); self.play(Create(enc(f[3], col=JAUNE, buff=0.12)), run_time=0.3)
        r = pos(M(r"\operatorname{tr} A = 1 + 4 - 3 = 2 \;\Longrightarrow\; A^2 = 2A", sc=0.9, color=VERT), -6.3, -2.85)
        self.ecr(self.a("k5", "Ici, la trace"), r, rt=1.2)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, T(r"Colonnes = images des vecteurs de base ; composée $\leftrightarrow$ produit", sc=0.75), "l2", 1.85),
                (VERT, T(r"$A' = P^{-1}AP$, \;$P$ = nouveaux vecteurs écrits dans l'ancienne base", sc=0.75), "l3", 0.55),
                (ORANGE, T(r"Rang = nombre de pivots ; \;équivalentes $\iff$ même rang", sc=0.75), "l4", -0.75)]
        for k, (c, F, sid, y) in enumerate(data):
            cc = carte(k+1, c, -5.9, y); pos(F, -5.3, y)
            self.at(self.t(sid), Create(cc[0]), FadeIn(cc[1]), run_time=0.4); self.play(Ecrire(F, rt=1.7))
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- La matrice d'une projection", "Exercice résolu")
        e = M(r"\mathcal{P} : x + y + z = 0", r"\qquad D = \operatorname{Vect}(1, 1, 1)", sc=1.0).move_to([0, 1.95, 0])
        self.at(self.a("m2", "on considère le plan"), Ecrire(e[0], rt=0.9))
        q = pos(T(r"$p$ : projection sur $\mathcal{P}$ parallèlement à $D$.", sc=0.75, color=JAUNE), -6.3, 1.1)
        q2 = pos(T(r"Matrice de $p$ dans la base \textbf{canonique} ?", sc=0.75, color=JAUNE), -6.3, 0.5)
        O = np.array([3.9, -2.4, 0])
        pl = Polygon(O + [-1.9, -0.55, 0], O + [1.6, -0.55, 0], O + [2.4, 0.75, 0], O + [-1.1, 0.75, 0], color=BLEU, stroke_width=2, fill_color=BLEU, fill_opacity=0.12)
        d = np.array([0.22, 1.25, 0])
        dl = Line(O - 0.35*d, O + 1.55*d, color=ORANGE, stroke_width=3)
        xt = O + np.array([1.35, 1.45, 0]); px = xt - 1.15*d
        vx = Arrow(O, xt, color=CRAIE, buff=0, stroke_width=3); vp = Arrow(O, px, color=JAUNE, buff=0, stroke_width=4)
        dd = DashedLine(xt, px, color=ORANGE, stroke_width=2)
        lp = M(r"\mathcal{P}", sc=0.6, color=BLEU).move_to(O + [-1.4, -0.3, 0]); ld = M("D", sc=0.6, color=ORANGE).next_to(O + 1.55*d, RIGHT, buff=0.1)
        lx = M("x", sc=0.6).next_to(xt, RIGHT, buff=0.1); lpx = M("p(x)", sc=0.55, color=JAUNE).next_to(px, RIGHT, buff=0.1)
        self.at(self.a("m2", "et la droite D"), Ecrire(e[1], rt=0.8), Create(pl), Create(dl), FadeIn(lp), FadeIn(ld), run_time=0.8)
        self.play(GrowArrow(vx), FadeIn(lx), run_time=0.5); self.play(Create(dd), GrowArrow(vp), FadeIn(lpx), run_time=0.8)
        self.ecr(self.a("m3", "Soit p"), q, rt=1.0); self.ecr(self.a("m3", "Question"), q2, rt=0.9)
        r1 = pos(T(r"base adaptée : matrice très simple\dots", sc=0.68, color=GRIS), -6.3, -0.45)
        r2 = pos(T(r"\dots\ mais on la veut dans la base \textbf{canonique}", sc=0.68, color=GRIS), -6.3, -1.0)
        self.ecr(self.a("m4", "Dans une base adaptée"), r1, rt=1.0); self.ecr(self.a("m4", "Mais on la veut"), r2, rt=1.0)
        s1 = pos(T(r"\textbf{1.} $P^{-1}AP$ : un inverse $3 \times 3$\dots", sc=0.68, color=GRIS), -6.3, -1.9)
        s2 = pos(T(r"\textbf{2.} une décomposition directe \;$\checkmark$", sc=0.68, color=VERT), -6.3, -2.5)
        self.ecr(self.a("m5", "Deux stratégies"), s1, rt=1.0); self.ecr(self.a("m5", "ou une décomposition directe"), s2, rt=1.0)
        self.fin()

class S13(Cours):
    sid = "S13"
    def construct(self):
        self.entete(r"Exercice résolu -- La solution, étape par étape", "Exercice résolu")
        c1 = carte(1, BLEU, -6.1, 2.2)
        s1 = pos(M(r"u_1 = (1, -1, 0),\;\; u_2 = (0, 1, -1) \in \mathcal{P}, \qquad u_3 = (1, 1, 1) \in D", sc=0.72), -5.55, 2.2)
        self.at(self.t("n1"), Create(c1[0]), FadeIn(c1[1]), run_time=0.4); self.at(self.a("n1", "u un égale"), Ecrire(s1, rt=1.8))
        s1b = pos(M(r"\operatorname{Mat}_{(u_1, u_2, u_3)}(p) = \operatorname{diag}(1, 1, 0)", r"\;\Longrightarrow\; \operatorname{rg} p = \operatorname{tr} p = 2", sc=0.72), -5.55, 1.55)
        s1b[1].set_color(VERT)
        self.at(self.a("n2", "Dans cette base"), Ecrire(s1b[0], rt=1.1)); self.at(self.a("n2", "On sait déjà"), Ecrire(s1b[1], rt=0.9))
        c2 = carte(2, VERT, -6.1, 0.75)
        s2 = pos(M(r"x = p(x) + \lambda(1, 1, 1), \qquad p(x) \in \mathcal{P}", sc=0.75), -5.55, 0.75)
        self.at(self.t("n3"), Create(c2[0]), FadeIn(c2[1]), run_time=0.4); self.at(self.a("n3", "Tout vecteur x"), Ecrire(s2, rt=1.3))
        s2b = pos(M(r"(x + y + z) - 3\lambda = 0", r"\;\Longrightarrow\; \lambda = \frac{x + y + z}{3}", sc=0.75), -5.55, 0.0)
        s2b[1].set_color(JAUNE)
        self.at(self.a("n4", "La somme des coordonnées"), Ecrire(s2b[0], rt=1.0)); self.at(self.a("n4", "lambda égale x plus y"), Ecrire(s2b[1], rt=0.8))
        c3 = carte(3, ORANGE, -6.1, -0.85)
        s3 = pos(M(r"e_1 :\ \lambda = \tfrac{1}{3}, \quad p(e_1) = \left(\tfrac{2}{3}, -\tfrac{1}{3}, -\tfrac{1}{3}\right)", sc=0.75), -5.55, -0.85)
        self.at(self.t("n5"), Create(c3[0]), FadeIn(c3[1]), run_time=0.4); self.at(self.a("n5", "Pour e un"), Ecrire(s3, rt=1.4))
        s3b = pos(M(r"A = \frac{1}{3}" + pm([2, -1, -1], [-1, 2, -1], [-1, -1, 2]), sc=0.75, color=JAUNE), -5.55, -2.3)
        self.ecr(self.a("n6", "La matrice"), s3b, rt=1.4); self.play(Create(enc(s3b, col=JAUNE, buff=0.12)), run_time=0.3)
        c4 = carte(4, ROUGE, 0.85, -1.75)
        v = [pos(M(s, sc=0.75), 1.4, y) for s, y in ((r"\operatorname{tr} A = 2 = \operatorname{rg} p \;\checkmark", -1.75),
                                                       (r"A\,(1, 1, 1)^\top = 0 \;\checkmark", -2.55), (r"Au_1 = u_1 \;\checkmark", -3.35))]
        self.at(self.t("n7"), Create(c4[0]), FadeIn(c4[1]), run_time=0.4)
        self.at(self.a("n7", "La trace vaut"), Ecrire(v[0], rt=0.9)); self.at(self.a("n7", "A fois un, un, un"), Ecrire(v[1], rt=0.9))
        self.at(self.a("n7", "Et A fois u un"), Ecrire(v[2], rt=0.6))
        self.jusqua(self.t("n8") - 0.2)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        nx = T(r"Chapitre 3 \;$\longrightarrow$\; trace, matrices semblables, calcul par blocs", sc=0.8, color=JAUNE).move_to([0, 0.3, 0])
        self.ecr(self.a("n8", "la trace"), nx, rt=1.6)
        self.fin()
