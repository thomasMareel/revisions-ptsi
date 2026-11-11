from base import *
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)
def chrono(x, y):
    pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([x, y, 0])
    arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
    return pa, arc
def pm(*rows): return r"\begin{pmatrix}" + r" \\ ".join(" & ".join(str(x) for x in r) for r in rows) + r"\end{pmatrix}"
def col(*xs): return pm(*[[x] for x in xs])
N3 = pm([0, 1, 1], [0, 0, 1], [0, 0, 0])

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"MATHÉMATIQUES \;·\; PT", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Matrices -- Chapitre 4}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Polynômes de matrices, nilpotentes et puissances", sc=0.88).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        de = M(r"A^2 = A + 2I", sc=0.95, color=BLEU).move_to([-2.3, 0.5, 0])
        dt = T(r"toute l'information !", sc=0.72, color=JAUNE).next_to(de, RIGHT, buff=0.7)
        self.at(self.a("a2", "Une simple relation"), Ecrire(de, rt=0.8)); self.ecr(self.a("a2", "contient toute"), dt, rt=0.8)
        items = []
        for k, (txt, c) in enumerate([("Polynômes de matrices", BLEU), ("Polynôme annulateur et inverse", VERT), (r"$A^n$ par division euclidienne", ORANGE),
                                       ("Matrices nilpotentes", ROUGE), ("Exercice résolu : une machine en panne", JAUNE)]):
            y = -0.75 - 0.6*k
            items.append(VGroup(carte(k+1, c, -3.6, y), pos(T(txt, sc=0.78), -3.0, y)))
        for it, (sid, fr) in zip(items, [("a3", "les polynômes de matrices"), ("a3", "le polynôme annulateur"), ("a3", "le calcul de A puissance n"),
                                         ("a3", "et les matrices nilpotentes"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"4.1 -- Polynômes de matrices", "Polynômes de matrices")
        d = pos(M(r"Q = \sum c_k X^k \;\longmapsto\; Q(A) = \sum c_k A^k", r"\qquad (A^0 = I_n)", sc=0.9, color=BLEU), -6.3, 2.05); d[1].set_color(GRIS)
        self.ecr(self.a("b1", "On va l'évaluer"), d, rt=1.3)
        e = pos(M(r"Q = X^2 - 3X + 2", r"\;\longmapsto\; Q(A) = A^2 - 3A + ", r"2I", sc=0.95), -6.3, 0.9)
        self.at(self.a("b2", "Exemple"), Ecrire(e, rt=1.3)); self.at(self.a("b2", "Attention au piège"), Indicate(e[2], color=ROUGE, scale_factor=1.6), e[2].animate.set_color(ROUGE), run_time=0.8)
        p = pos(M(r"(QR)(A) = Q(A)\,R(A)", sc=1.05, color=JAUNE), -6.3, -0.4)
        self.ecr(self.a("b3", "Propriété clé"), p, rt=0.9); self.play(Create(enc(p, col=JAUNE)), run_time=0.4)
        c1 = pos(T(r"$\Rightarrow$ deux polynômes en $A$ \textbf{commutent}", sc=0.78, color=VERT), -6.3, -1.45)
        c2 = pos(M(r"Q\big(\operatorname{diag}(\lambda_1, \ldots, \lambda_n)\big) = \operatorname{diag}\big(Q(\lambda_1), \ldots, Q(\lambda_n)\big)", sc=0.8), -6.3, -2.45)
        self.ecr(self.a("b4", "deux polynômes en A commutent"), c1, rt=1.0); self.ecr(self.a("b4", "Et pour une matrice diagonale"), c2, rt=1.4)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"4.1 -- Polynôme annulateur", "Polynômes de matrices")
        d = pos(M(r"Q(A) = 0", r"\quad\Longleftrightarrow\quad Q \text{ annulateur de } A", sc=0.95), -6.3, 2.1)
        self.ecr(self.a("c1", "Un polynôme Q est annulateur"), d, rt=1.1)
        x = pos(M(r"I_n, A, A^2, \ldots, A^{n^2} :\ n^2 + 1 \text{ matrices, dimension } n^2", sc=0.82), -6.3, 1.3)
        li = T(r"liées !", sc=0.72, color=ROUGE).next_to(x, RIGHT, buff=0.4)
        self.ecr(self.a("c2", "Pourquoi"), x, rt=1.4); self.at(self.a("c2", "Elles sont forcément liées"), FadeIn(li, scale=1.3), run_time=0.4)
        f = M(r"A^2 - \operatorname{tr}(A)\,A + \det(A)\,I_2 = 0", sc=1.05, color=JAUNE).move_to([-0.4, 0.3, 0])
        t2 = T(r"(taille 2)", sc=0.62, color=GRIS).next_to(f, RIGHT, buff=0.5)
        self.ecr(self.a("c3", "En taille deux"), f, rt=1.3); self.play(Create(enc(f, col=JAUNE)), FadeIn(t2), run_time=0.4)
        v = pos(M(r"A = " + pm([1, 2], [3, 4]) + r" :\ \operatorname{tr} A = 5,\ \det A = -2,", r"\quad A^2 = " + pm([7, 10], [15, 22]), sc=0.8), -6.3, -1.15)
        self.at(self.a("c4", "Vérifions en direct"), Ecrire(v[0], rt=1.4)); self.at(self.a("c4", "Et A carré égale"), Ecrire(v[1], rt=0.9))
        r = pos(M(r"A^2 - 5A - 2I_2 = " + pm(["7 - 5 - 2", "10 - 10"], ["15 - 15", "22 - 20 - 2"]) + r" = 0 \;\checkmark", sc=0.8, color=VERT), -6.3, -2.65)
        self.ecr(self.a("c5", "A carré, moins cinq A"), r, rt=2.0)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"4.2 -- Inverser grâce à un polynôme annulateur", "Inverse")
        a = pos(M(r"A = " + pm([1, 2], [2, 1]), r" :\quad A^2 - 2A - 3I_2 = 0", sc=0.9), -6.3, 1.95)
        self.at(self.a("d1", "Prenons A"), Ecrire(a[0], rt=0.7)); self.at(self.a("d1", "donc A carré"), Ecrire(a[1], rt=1.0))
        b = pos(M(r"A^2 - 2A = 3I_2", sc=0.95), -6.3, 0.8)
        self.ecr(self.a("d2", "On isole"), b, rt=0.8)
        c = pos(M(r"A(A - 2I_2) = 3I_2", r"\;\Longrightarrow\; A \times \tfrac{1}{3}(A - 2I_2) = I_2", sc=0.95), -6.3, -0.2)
        self.at(self.a("d3", "On factorise"), Ecrire(c[0], rt=0.8)); self.at(self.a("d3", "Et on divise"), Ecrire(c[1], rt=1.0))
        d = pos(M(r"A^{-1} = \tfrac{1}{3}(A - 2I_2) = \tfrac{1}{3}" + pm([-1, 2], [2, -1]), sc=0.95, color=JAUNE), -6.3, -1.45)
        self.ecr(self.a("d4", "Conclusion"), d, rt=1.3); self.play(Create(enc(d, col=JAUNE, buff=0.15)), run_time=0.4)
        e = pos(T(r"condition : le terme constant de l'annulateur est \textbf{non nul}", sc=0.75, color=ORANGE), -6.3, -2.85)
        self.ecr(self.a("d5", "La condition"), e, rt=1.2)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"4.2 -- À vous : un inverse", "Inverse")
        cad = RoundedRectangle(width=12.4, height=1.6, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, 1.7, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.72, color=JAUNE), -5.9, 1.7)
        en = M(r"\text{Inverser } A = " + pm([2, 1], [1, 2]) + r"\text{ grâce à un polynôme annulateur}", sc=0.8).next_to(tq, RIGHT, buff=0.5)
        self.at(self.t("e1"), Create(cad), Ecrire(tq, rt=0.4), run_time=0.5)
        self.at(self.a("e1", "Inversez"), Ecrire(en, rt=1.4))
        pa, arc = chrono(5.7, 1.7)
        self.jusqua(self.PH["e1"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("e2") - self.renderer.time - 0.1), rate_func=linear)
        r1 = pos(M(r"\operatorname{tr} A = 4,\ \det A = 3 \;\Longrightarrow\; A^2 - 4A + 3I_2 = 0", sc=0.88), -6.0, 0.0)
        self.at(self.a("e2", "Réponse"), FadeOut(pa), FadeOut(arc), Ecrire(r1, rt=1.4))
        r2 = pos(M(r"A(4I_2 - A) = 3I_2 \;\Longrightarrow\; A^{-1} = \tfrac{1}{3}(4I_2 - A) = \tfrac{1}{3}" + pm([2, -1], [-1, 2]), sc=0.88, color=JAUNE), -6.0, -1.45)
        self.ecr(self.a("e3", "Donc A fois"), r2, rt=1.8); self.play(Create(enc(r2, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"4.3 -- $A^n$ par division euclidienne", "Puissances")
        t = pos(T(r"Calculer $A^n$ \textbf{sans diagonaliser}", sc=0.8, color=BLEU), -6.3, 2.15)
        self.ecr(self.a("f1", "Deuxième application"), t, rt=0.9)
        d = pos(M(r"X^n = Q\,S + R, \qquad \deg R < \deg Q", sc=0.9), -6.3, 1.4)
        self.ecr(self.a("f2", "On divise X puissance n"), d, rt=1.2)
        r = pos(M(r"Q(A) = 0 \;\Longrightarrow\; A^n = R(A)", sc=1.0, color=JAUNE), -6.3, 0.5)
        self.ecr(self.a("f3", "On remplace X par A"), r, rt=1.0); self.play(Create(enc(r, col=JAUNE, buff=0.15)), run_time=0.4)
        q = pos(M(r"Q = X^2 - 2X - 3 = (X - 3)(X + 1),", r"\qquad R = aX + b", sc=0.85), -6.3, -0.5)
        self.at(self.a("f4", "Pour A égale"), Ecrire(q[0], rt=1.3)); self.at(self.a("f4", "Le reste est de degré un"), Ecrire(q[1], rt=0.7))
        e1 = pos(M(r"X = 3 :\quad 3^n = 3a + b", sc=0.85, color=VERT), -6.3, -1.45)
        e2 = pos(M(r"X = -1 :\quad (-1)^n = -a + b", sc=0.85, color=VERT), -0.6, -1.45)
        self.at(self.a("f5", "L'astuce"), Indicate(q[0], color=VERT, scale_factor=1.05), run_time=0.6)
        self.ecr(self.a("f5", "En trois"), e1, rt=0.9); self.ecr(self.a("f5", "En moins un"), e2, rt=0.9)
        s = pos(M(r"a = \frac{3^n - (-1)^n}{4}, \qquad b = \frac{3^n + 3(-1)^n}{4}", sc=0.9, color=JAUNE), -6.3, -2.75)
        self.ecr(self.a("f6", "On soustrait"), s, rt=1.6)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"4.3 -- Le résultat, et la vérification", "Puissances")
        a = pos(M(r"A^n = aA + bI_2", sc=1.0), -6.3, 2.05)
        self.ecr(self.a("g1", "Il ne reste qu'à assembler"), a, rt=0.8)
        r = pos(M(r"A^n = \frac{1}{2}" + pm([r"3^n + (-1)^n", r"3^n - (-1)^n"], [r"3^n - (-1)^n", r"3^n + (-1)^n"]), sc=0.95, color=JAUNE), -6.3, 0.6)
        self.ecr(self.a("g2", "Sur la diagonale"), r, rt=2.0); self.play(Create(enc(r, col=JAUNE, buff=0.15)), run_time=0.4)
        v = pos(M(r"n = 2 :\quad \tfrac{9 + 1}{2} = 5,\ \ \tfrac{9 - 1}{2} = 4 \;\Longrightarrow\; " + pm([5, 4], [4, 5]), sc=0.85), -6.3, -1.2)
        self.ecr(self.a("g3", "Vérifions pour n"), v, rt=1.5)
        w = pos(M(r"A^2 = " + pm([1, 2], [2, 1]) + pm([1, 2], [2, 1]) + r" = " + pm(["1 + 4", "2 + 2"], ["2 + 2", "4 + 1"]) + r" = " + pm([5, 4], [4, 5]) + r"\;\checkmark", sc=0.78, color=VERT), -6.3, -2.6)
        self.ecr(self.a("g4", "Et le calcul direct"), w, rt=1.8)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"4.4 -- Matrices nilpotentes", "Nilpotentes")
        d = pos(M(r"N^p = 0", r"\qquad \text{indice } \leq n", sc=1.0), -6.3, 2.05); d[1].set_color(GRIS)
        self.at(self.a("h1", "N est nilpotente"), Ecrire(d[0], rt=0.6)); self.at(self.a("h1", "Le plus petit exposant"), Ecrire(d[1], rt=0.7))
        n = pos(M(r"N = " + N3, sc=0.85), -6.3, 0.55)
        self.ecr(self.a("h2", "Exemple en direct"), n, rt=1.0)
        n2 = pos(M(r"N^2 = " + pm([0, 0, 1], [0, 0, 0], [0, 0, 0]), sc=0.85), -2.45, 0.55)
        n3 = pos(M(r"N^3 = 0", sc=1.0, color=ROUGE), 1.6, 0.55)
        self.ecr(self.a("h3", "N carré"), n2, rt=1.0); self.ecr(self.a("h3", "Et N cube"), n3, rt=0.5)
        dg = pos(T(r"à chaque puissance, la diagonale non nulle recule d'un cran", sc=0.66, color=GRIS), -6.3, -0.75)
        self.ecr(self.a("h3", "À chaque puissance"), dg, rt=1.2)
        r1 = pos(T(r"strictement triangulaire $\Rightarrow$ \textbf{nilpotente}", sc=0.78, color=VERT), -6.3, -1.75)
        r2 = pos(T(r"nilpotente : \textbf{jamais inversible}, trace nulle", sc=0.78, color=ORANGE), -6.3, -2.6)
        self.ecr(self.a("h4", "Retenez"), r1, rt=1.0); self.ecr(self.a("h4", "Et une nilpotente"), r2, rt=1.0)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"4.4 -- Le binôme avec une nilpotente", "Nilpotentes")
        a = pos(M(r"A = I_3 + N = " + pm([1, 1, 1], [0, 1, 1], [0, 0, 1]), sc=0.88), -6.3, 1.8)
        self.ecr(self.a("i1", "Prenons A"), a, rt=1.1)
        b = pos(M(r"A^n = I_3 + nN + \frac{n(n-1)}{2}N^2", sc=0.95, color=JAUNE), -6.3, 0.35)
        bn = T(r"(car $N^3 = 0$)", sc=0.65, color=GRIS).next_to(b, RIGHT, buff=0.4)
        self.ecr(self.a("i2", "I et N commutent"), b, rt=1.4); self.at(self.a("i2", "Et c'est tout"), FadeIn(bn), run_time=0.4)
        c = pos(M(r"(A^n)_{13} = n + \frac{n(n-1)}{2} = \frac{n(n+1)}{2}", sc=0.88), -6.3, -1.15)
        full = pos(M(r"A^n = " + pm([1, "n", r"\frac{n(n+1)}{2}"], [0, 1, "n"], [0, 0, 1]), sc=0.82, color=JAUNE), 1.5, -1.15)
        self.ecr(self.a("i3", "Le coefficient en haut à droite"), c, rt=1.5); self.ecr(self.a("i3", "Total"), full, rt=1.0)
        v = pos(M(r"n = 5 :\ \ \tfrac{5 \times 6}{2} = 15 \;\checkmark", sc=0.88, color=VERT), -6.3, -2.75)
        self.ecr(self.a("i4", "Pour n égale cinq"), v, rt=1.0)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"4.4 -- Inverse de $I - N$", "Nilpotentes")
        a = pos(M(r"N^p = 0 \;\Longrightarrow\; I - N \text{ inversible}", sc=0.95), -6.3, 2.05)
        self.ecr(self.a("j1", "Encore plus fort"), a, rt=1.0)
        f = M(r"(I - N)^{-1} = I + N + N^2 + \cdots + N^{p-1}", sc=1.05, color=JAUNE).move_to([0, 1.0, 0])
        g = T(r"comme $\dfrac{1}{1 - x} = 1 + x + x^2 + \cdots$", sc=0.68, color=GRIS).move_to([0, 0.1, 0])
        self.ecr(self.a("j2", "Son inverse"), f, rt=1.3); self.play(Create(enc(f, col=JAUNE)), run_time=0.4)
        self.ecr(self.a("j2", "Comme la série géométrique"), g, rt=1.0)
        p = pos(M(r"(I - N)(I + N + N^2) = I + N + N^2 - N - N^2 - N^3 = I - N^3 = I", sc=0.82), -6.3, -0.95)
        self.ecr(self.a("j3", "La preuve"), p, rt=1.8)
        r = pos(M(r"(I_3 - N)^{-1} = I_3 + N + N^2 = " + pm([1, 1, 2], [0, 1, 1], [0, 0, 1]), sc=0.9, color=JAUNE), -6.3, -2.4)
        self.ecr(self.a("j4", "Avec notre N"), r, rt=1.5); self.play(Create(enc(r, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, T(r"Annulateur à terme constant non nul $\Rightarrow$ inverse, en isolant $I$", sc=0.75), "k2", 1.85),
                (VERT, T(r"$A^n = R(A)$, reste de $X^n$ par l'annulateur, trouvé aux racines", sc=0.75), "k3", 0.55),
                (ORANGE, T(r"$A = \lambda I + N$, $N$ nilpotente : le binôme s'arrête tout seul", sc=0.75), "k4", -0.75)]
        for k, (c, F, sid, y) in enumerate(data):
            cc = carte(k+1, c, -5.9, y); pos(F, -5.3, y)
            self.at(self.t(sid), Create(cc[0]), FadeIn(cc[1]), run_time=0.4); self.play(Ecrire(F, rt=1.7))
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice résolu -- Une machine en panne", "Exercice résolu")
        l1 = pos(T(r"Chaque jour : en \textbf{marche} (M) ou en \textbf{panne} (P)", sc=0.75, color=BLEU), -6.3, 2.1)
        self.ecr(self.a("l1", "Une machine"), l1, rt=1.1)
        cm = Circle(radius=0.4, color=VERT, stroke_width=3).move_to([2.4, 0.85, 0]); cp = Circle(radius=0.4, color=ROUGE, stroke_width=3).move_to([5.6, 0.85, 0])
        tm = M("M", sc=0.8, color=VERT).move_to(cm); tp = M("P", sc=0.8, color=ROUGE).move_to(cp)
        a1 = CurvedArrow(cm.get_top() + RIGHT*0.2, cp.get_top() + LEFT*0.2, angle=-PI/3, color=CRAIE, stroke_width=3)
        a2 = CurvedArrow(cp.get_bottom() + LEFT*0.2, cm.get_bottom() + RIGHT*0.2, angle=-PI/3, color=CRAIE, stroke_width=3)
        l12 = M(r"0{,}2", sc=0.6).next_to(a1, UP, buff=0.05); l21 = M(r"0{,}3", sc=0.6, color=JAUNE).next_to(a2, DOWN, buff=0.05)
        rm = M(r"\circlearrowleft\ 0{,}8", sc=0.6, color=VERT).next_to(cm, LEFT, buff=0.15); rp = M(r"0{,}7\ \circlearrowright", sc=0.6, color=ROUGE).next_to(cp, RIGHT, buff=0.15)
        self.at(self.a("l2", "En marche"), Create(cm), FadeIn(tm), Create(cp), FadeIn(tp), FadeIn(rm), Create(a1), FadeIn(l12), run_time=0.9)
        self.at(self.a("l2", "En panne"), FadeIn(rp), Create(a2), FadeIn(l21), run_time=0.8)
        x = pos(M(r"X_{k+1} = AX_k, \qquad X_k = " + col("m_k", "p_k"), r", \qquad A = " + pm(["0{,}8", "0{,}3"], ["0{,}2", "0{,}7"]), sc=0.82), -6.3, -0.55)
        self.at(self.a("l3", "On note m k"), Ecrire(x[0], rt=1.2)); self.at(self.a("l3", "avec cette matrice A"), Ecrire(x[1], rt=1.0))
        q = pos(T(r"\textbf{1.} un polynôme annulateur \quad \textbf{2.} $A^k$ \quad \textbf{3.} limite quand $k \to +\infty$", sc=0.75, color=JAUNE), -6.3, -1.75)
        self.ecr(self.a("l4", "Questions"), q, rt=1.6)
        c = M(r"\text{taille 2} \to \text{annulateur} \to \text{division euclidienne} \to \text{limite}", sc=0.8, color=VERT).move_to([0, -2.85, 0])
        self.ecr(self.a("l5", "Réfléchissons"), c, rt=2.0)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- La solution, étape par étape", "Exercice résolu")
        c1 = carte(1, BLEU, -6.1, 2.2)
        s1 = pos(M(r"\operatorname{tr} A = 1{,}5,", r"\quad \det A = 0{,}56 - 0{,}06 = 0{,}5", sc=0.75), -5.55, 2.2)
        self.at(self.t("m1"), Create(c1[0]), FadeIn(c1[1]), run_time=0.4)
        self.at(self.a("m1", "Trace"), Ecrire(s1[0], rt=0.7)); self.at(self.a("m1", "Déterminant"), Ecrire(s1[1], rt=1.1))
        s1b = pos(M(r"A^2 - 1{,}5A + 0{,}5I_2 = 0", r"\qquad \text{racines } 1 \text{ et } \tfrac{1}{2}", sc=0.75), -5.55, 1.55)
        s1b[1].set_color(VERT)
        self.at(self.a("m2", "Donc A carré"), Ecrire(s1b[0], rt=1.0)); self.at(self.a("m2", "Et ce polynôme"), Ecrire(s1b[1], rt=0.7))
        c2 = carte(2, VERT, -6.1, 0.75)
        s2 = pos(M(r"A^k = a_kA + b_kI_2 :", r"\quad 1 = a_k + b_k,", r"\quad (\tfrac{1}{2})^k = \tfrac{1}{2}a_k + b_k", sc=0.75), -5.55, 0.75)
        self.at(self.t("m3"), Create(c2[0]), FadeIn(c2[1]), run_time=0.4); self.at(self.a("m3", "Deuxième étape"), Ecrire(s2[0], rt=0.8))
        self.at(self.a("m3", "En un :"), Ecrire(s2[1], rt=0.6)); self.at(self.a("m3", "En un demi"), Ecrire(s2[2], rt=0.8))
        s2b = pos(M(r"a_k = 2\big(1 - (\tfrac{1}{2})^k\big), \qquad b_k = 1 - a_k", sc=0.78, color=JAUNE), -5.55, 0.0)
        self.ecr(self.a("m4", "On soustrait"), s2b, rt=1.2)
        c3 = carte(3, ORANGE, -6.1, -0.85)
        s3 = pos(M(r"(\tfrac{1}{2})^k \to 0 :\quad a_k \to 2,\ b_k \to -1,", r"\quad A^k \to 2A - I_2", sc=0.75), -5.55, -0.85)
        self.at(self.t("m5"), Create(c3[0]), FadeIn(c3[1]), run_time=0.4); self.at(self.a("m5", "Un demi puissance k"), Ecrire(s3[0], rt=1.2))
        self.at(self.a("m5", "A puissance k tend vers"), Ecrire(s3[1], rt=0.7))
        s3b = pos(M(r"2A - I_2 = " + pm(["0{,}6", "0{,}6"], ["0{,}4", "0{,}4"]), sc=0.8, color=JAUNE), -5.55, -2.0)
        self.ecr(self.a("m6", "Et deux A moins I"), s3b, rt=1.0); self.play(Create(enc(s3b, col=JAUNE, buff=0.12)), run_time=0.3)
        it = pos(T(r"à long terme : \textbf{marche} 60 \%, \;\textbf{panne} 40 \%", sc=0.75, color=VERT), 0.2, -2.0)
        self.ecr(self.a("m7", "Interprétation"), it, rt=1.2)
        c4 = carte(4, ROUGE, -6.1, -3.25)
        s4 = pos(M(r"0{,}6 \times 0{,}2 = 0{,}12 = 0{,}4 \times 0{,}3 \;\checkmark", sc=0.75), -5.55, -3.25)
        s4b = pos(T(r"autant de pannes que de réparations", sc=0.62, color=GRIS), 0.6, -3.25)
        self.at(self.t("m8"), Create(c4[0]), FadeIn(c4[1]), run_time=0.4); self.at(self.a("m8", "Vérification"), Ecrire(s4, rt=1.4))
        self.ecr(self.a("m8", "Autant de pannes"), s4b, rt=0.9)
        self.jusqua(self.t("m9") - 0.2)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        f1 = T(r"\textbf{Fin de la série « Matrices »}", sc=0.95, color=JAUNE).move_to([0, 0.8, 0])
        f2 = T(r"Prochaine étape : la réduction des endomorphismes", sc=0.8, color=VERT).move_to([0, -0.3, 0])
        self.ecr(self.a("m9", "C'est la fin"), f1, rt=1.0); self.ecr(self.a("m9", "Prochaine étape"), f2, rt=1.3)
        self.fin()
