from base import *
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
def mat(rows, sc=0.8, col=CRAIE, h=0.9, v=0.65):
    m = Matrix([[str(x) for x in r] for r in rows], element_to_mobject=lambda s: MathTex(s, tex_template=tpl, color=col),
               left_bracket="(", right_bracket=")", h_buff=h, v_buff=v, bracket_h_buff=0.2)
    m.get_brackets().set_color(col); return m.scale(sc)
def pm(*rows): return r"\begin{pmatrix}" + r" \\ ".join(" & ".join(r) for r in rows) + r"\end{pmatrix}"

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"MATHÉMATIQUES \;·\; PTSI", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Matrices -- Chapitre 1}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Calcul matriciel : les méthodes", sc=0.95).move_to([0, 1.75, 0])
        tr = Line([-4.4, 1.3, 0], [4.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=0.9), Create(tr), run_time=1.0)
        de = mat([[2, 1, 0], [0, 2, 1], [0, 0, 2]], sc=0.55, col=BLEU).move_to([-2.6, 0.5, 0])
        dt = T(r"méthodes et exemples \textbf{en direct}", sc=0.72, color=JAUNE).next_to(de, RIGHT, buff=0.6)
        self.at(self.a("a1", "Les matrices"), FadeIn(de), run_time=0.6)
        self.ecr(self.a("a2", "les méthodes"), dt, rt=0.9)
        items = []
        for k, (txt, col) in enumerate([("Le produit matriciel", BLEU), ("Calculer une puissance", VERT), ("Le pivot de Gauss", ORANGE),
                                         ("Inverser une matrice", ROUGE), ("Exercice résolu", JAUNE)]):
            y = -0.75 - 0.6*k
            items.append(VGroup(carte(k+1, col, -3.6, y), pos(T(txt, sc=0.78), -3.0, y)))
        for it, (sid, fr) in zip(items, [("a3", "le produit"), ("a3", "le calcul d'une puissance"), ("a3", "le pivot de Gauss"),
                                         ("a3", "et le calcul d'un inverse"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"1 -- Le produit matriciel", "Produit")
        r = pos(T(r"coefficient $(i, j)$ de $AB$ : \textbf{ligne} $i$ de $A$ $\times$ \textbf{colonne} $j$ de $B$", sc=0.72, color=BLEU), -6.3, 2.15)
        self.ecr(self.a("b1", "On multiplie"), r, rt=1.4)
        tl = pos(M(r"(n \times ", r"p", r") \,\times\, (", r"p", r" \times q) \;\longrightarrow\; n \times q", sc=0.85), -6.3, 1.4)
        tl[1].set_color(ROUGE); tl[3].set_color(ROUGE)
        self.at(self.a("b2", "Attention aux tailles"), Ecrire(tl, rt=1.2))
        self.at(self.a("b2", "Le nombre de colonnes"), Indicate(tl[1], color=ROUGE, scale_factor=1.5), Indicate(tl[3], color=ROUGE, scale_factor=1.5), run_time=0.8)
        A = mat([[1, 2, 0], [-1, 3, 1]]).move_to([-4.2, -0.35, 0])
        B = mat([[2, 1], [0, -1], [4, 2]]).next_to(A, RIGHT, buff=0.35)
        eg = M("=").next_to(B, RIGHT, buff=0.35)
        C = mat([[2, -1], [2, -2]], col=JAUNE).next_to(eg, RIGHT, buff=0.35)
        la = T(r"$A$ : $2 \times 3$", sc=0.6, color=GRIS).next_to(A, DOWN, buff=0.25); lb = T(r"$B$ : $3 \times 2$", sc=0.6, color=GRIS).next_to(B, DOWN, buff=0.25)
        lc = T(r"$AB$ : $2 \times 2$", sc=0.6, color=JAUNE).next_to(C, DOWN, buff=0.25)
        self.at(self.a("b3", "Exemple"), Ecrire(A, rt=0.8), Ecrire(B, rt=0.8)); self.play(FadeIn(la), FadeIn(lb), run_time=0.4)
        self.at(self.a("b3", "le produit A B existe"), FadeIn(eg), FadeIn(C.get_brackets()), FadeIn(lc), run_time=0.6)
        e = C.get_entries()
        rl = SurroundingRectangle(A.get_rows()[0], color=BLEU, buff=0.1); rc = SurroundingRectangle(B.get_columns()[0], color=ROUGE, buff=0.1)
        calc = pos(M(r"1 \times 2 + 2 \times 0 + 0 \times 4 = 2", sc=0.8), -4.4, -2.45)
        self.at(self.a("b4", "Ligne un, colonne un"), Create(rl), Create(rc), run_time=0.5)
        self.at(self.a("b4", "un fois deux"), Ecrire(calc, rt=1.6))
        self.at(self.a("b4", "Ça fait deux"), FadeIn(e[0], scale=1.4), run_time=0.5)
        c2 = pos(M(r"1 - 2 + 0 = -1", sc=0.8), -4.4, -2.45)
        self.at(self.a("b5", "Ligne un, colonne deux"), Transform(rc, SurroundingRectangle(B.get_columns()[1], color=ROUGE, buff=0.1)), FadeOut(calc), run_time=0.5)
        self.play(Ecrire(c2, rt=0.8))
        self.at(self.a("b5", "Moins un"), FadeIn(e[1], scale=1.4), run_time=0.5)
        c3 = pos(M(r"-2 + 0 + 4 = 2", sc=0.8), -4.4, -2.45)
        self.at(self.a("b6", "Ligne deux, colonne un"), Transform(rl, SurroundingRectangle(A.get_rows()[1], color=BLEU, buff=0.1)),
                Transform(rc, SurroundingRectangle(B.get_columns()[0], color=ROUGE, buff=0.1)), FadeOut(c2), run_time=0.5)
        self.play(Ecrire(c3, rt=0.8))
        self.at(self.a("b6", "Deux. Et"), FadeIn(e[2], scale=1.4), run_time=0.4)
        c4 = pos(M(r"-1 - 3 + 2 = -2", sc=0.8), -4.4, -2.45)
        self.at(self.a("b6", "ligne deux, colonne deux"), Transform(rc, SurroundingRectangle(B.get_columns()[1], color=ROUGE, buff=0.1)), FadeOut(c3), run_time=0.4)
        self.play(Ecrire(c4, rt=0.8))
        self.at(self.a("b6", "Moins deux."), FadeIn(e[3], scale=1.4), run_time=0.4)
        ba = T(r"$BA$ existe aussi\dots\ mais il est de taille $3 \times 3$ !", sc=0.75, color=ROUGE).move_to([0, -3.3, 0])
        self.at(self.a("b7", "Et voilà"), FadeOut(rl), FadeOut(rc), Create(enc(C, col=JAUNE, buff=0.12)), run_time=0.5)
        self.ecr(self.a("b7", "B A existe aussi"), ba, rt=1.2)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"1 -- Trois pièges", "Produit")
        c1 = carte(1, BLEU, -6.1, 1.65); c2 = carte(2, VERT, -6.1, 0.0); c3 = carte(3, ORANGE, -6.1, -1.55)
        l1 = pos(M(r"A = " + pm(["1", "1"], ["0", "0"]) + r",\;\; B = " + pm(["1", "0"], ["1", "0"]), r"\qquad AB = " + pm(["2", "0"], ["0", "0"]) + r"\;\neq\; BA = " + pm(["1", "1"], ["1", "1"]), sc=0.75), -5.55, 1.65)
        l1[1].set_color(ROUGE)
        self.at(self.t("c2"), Create(c1[0]), FadeIn(c1[1]), run_time=0.4)
        self.at(self.a("c2", "Regardez ces deux matrices"), Ecrire(l1[0], rt=1.0)); self.at(self.a("c2", "les deux produits"), Ecrire(l1[1], rt=1.2))
        l2 = pos(M(r"N = " + pm(["0", "1"], ["0", "0"]) + r" \neq 0", r"\qquad\text{mais}\qquad N^2 = 0", sc=0.75), -5.55, 0.0)
        l2[1].set_color(ROUGE)
        self.at(self.t("c3"), Create(c2[0]), FadeIn(c2[1]), run_time=0.4)
        self.at(self.a("c3", "Cette matrice N"), Ecrire(l2[0], rt=0.9)); self.at(self.a("c3", "et pourtant"), Ecrire(l2[1], rt=0.8))
        l3 = pos(M(r"(A+B)^2 = A^2 + AB + BA + B^2", r"\;\neq\; A^2 + 2AB + B^2", sc=0.8), -5.55, -1.55)
        l3[1].set_color(ROUGE)
        n3 = pos(T(r"(égalité seulement si $AB = BA$)", sc=0.62, color=GRIS), -5.55, -2.3)
        self.at(self.t("c4"), Create(c3[0]), FadeIn(c3[1]), run_time=0.4); self.play(Ecrire(l3[0], rt=1.2))
        self.at(self.a("c4", "Pas de deux A B"), Ecrire(l3[1], rt=0.8)); self.ecr(self.a("c4", "sauf si"), n3, rt=0.8)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"2 -- Puissances : conjecturer, puis démontrer", "Puissances")
        m = pos(T(r"\textbf{Méthode 1} : calculer, conjecturer, démontrer par récurrence", sc=0.75, color=VERT), -6.3, 2.15)
        self.ecr(self.a("d1", "Première méthode"), m, rt=1.3)
        a = pos(M(r"A = " + pm(["1", "1"], ["0", "1"]), sc=0.9), -6.3, 0.95)
        a2 = pos(M(r"A^2 = " + pm(["1", "2"], ["0", "1"]), sc=0.9), -2.7, 0.95)
        a3 = pos(M(r"A^3 = " + pm(["1", "3"], ["0", "1"]), sc=0.9), 0.9, 0.95)
        self.ecr(self.a("d2", "Prenons cette matrice"), a, rt=0.7); self.ecr(self.a("d2", "A carré"), a2, rt=0.8); self.ecr(self.a("d2", "A cube"), a3, rt=0.8)
        cj = pos(M(r"A^n = " + pm(["1", "n"], ["0", "1"]), r"\;\; ?", sc=0.95, color=JAUNE), -6.3, -0.55)
        self.ecr(self.a("d3", "On devine"), cj, rt=1.0)
        rc = pos(M(r"A^{n+1} = A\,A^n = " + pm(["1", "1"], ["0", "1"]) + pm(["1", "n"], ["0", "1"]) + r" = " + pm(["1", "n+1"], ["0", "1"]), sc=0.85), -6.3, -1.95)
        ok = M(r"\checkmark", sc=1.0, color=VERT).next_to(rc, RIGHT, buff=0.4)
        self.ecr(self.a("d4", "Récurrence"), rc, rt=1.8); self.at(self.a("d4", "C'est héréditaire"), FadeIn(ok, scale=1.6), FadeOut(cj[1]), run_time=0.5)
        z = pos(T(r"$n = 0$ : on retrouve $I_2$ \;$\checkmark$", sc=0.7, color=GRIS), -6.3, -3.2)
        self.ecr(self.a("d5", "Toujours vérifier"), z, rt=1.0)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"2 -- Puissances : le binôme de Newton", "Puissances")
        bn = M(r"AB = BA", r"\;\Longrightarrow\; (A+B)^n = \sum_{k=0}^{n}\binom{n}{k}A^kB^{n-k}", sc=0.95).move_to([0, 1.75, 0])
        bn[0].set_color(ROUGE)
        self.at(self.a("e1", "le binôme de Newton"), Ecrire(bn[1], rt=1.4)); self.at(self.a("e1", "à une condition"), Ecrire(bn[0], rt=0.6))
        self.play(Create(enc(bn, col=JAUNE)), run_time=0.4)
        a = pos(M(r"A = " + pm(["2", "1"], ["0", "2"]), r"\;=\; 2I_2 + N,", r"\qquad N = " + pm(["0", "1"], ["0", "0"]), sc=0.88), -6.3, 0.15)
        self.at(self.a("e2", "L'astuce"), Ecrire(a[0], rt=0.7)); self.play(Ecrire(a[1], rt=0.6)); self.at(self.a("e2", "où N est"), Ecrire(a[2], rt=0.7))
        n2 = pos(M(r"N^2 = 0", r"\qquad 2I_2\text{ commute avec } N", sc=0.85, color=VERT), -6.3, -1.0)
        self.at(self.a("e3", "Ici"), Ecrire(n2[0], rt=0.5)); self.at(self.a("e3", "Et deux I commute"), Ecrire(n2[1], rt=0.9))
        r = pos(M(r"A^n = 2^n I_2 + n\,2^{n-1} N", sc=0.95, color=JAUNE), -6.3, -2.15)
        self.ecr(self.a("e4", "A puissance n"), r, rt=1.3)
        r2 = M(r"= " + pm([r"2^n", r"n\,2^{n-1}"], ["0", r"2^n"]), sc=0.95, color=JAUNE).next_to(r, RIGHT, buff=0.25)
        self.ecr(self.a("e5", "Soit la matrice"), r2, rt=1.1); self.play(Create(enc(VGroup(r, r2), col=JAUNE, buff=0.15)), run_time=0.4)
        v = pos(T(r"$n = 1$ : on retrouve $A$ \;$\checkmark$", sc=0.7, color=GRIS), -6.3, -3.3)
        self.ecr(self.a("e5", "Vérification"), v, rt=0.9)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"2 -- À vous : une puissance", "Puissances")
        cad = RoundedRectangle(width=12.4, height=1.6, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, 1.7, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.72, color=JAUNE), -5.9, 1.7)
        en = M(r"\text{Calculer } A^n \text{ pour } A = " + pm(["3", "1"], ["0", "3"]), sc=0.85).next_to(tq, RIGHT, buff=0.6)
        self.at(self.t("f1"), Create(cad), Ecrire(tq, rt=0.4), run_time=0.5)
        self.at(self.a("f1", "Calculez"), Ecrire(en, rt=1.3))
        pa, arc = chrono(5.7, 1.7)
        self.jusqua(self.PH["f1"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("f2") - self.renderer.time - 0.1), rate_func=linear)
        r1 = pos(M(r"A = 3I_2 + N, \qquad N = " + pm(["0", "1"], ["0", "0"]) + r",\quad N^2 = 0", sc=0.85), -6.0, -0.1)
        self.at(self.a("f2", "Réponse"), FadeOut(pa), FadeOut(arc), Ecrire(r1, rt=1.4))
        r2 = pos(M(r"A^n = 3^n I_2 + n\,3^{n-1}N", r"\;=\; " + pm([r"3^n", r"n\,3^{n-1}"], ["0", r"3^n"]), sc=0.95, color=JAUNE), -6.0, -1.75)
        self.at(self.a("f3", "Donc"), Ecrire(r2, rt=1.6)); self.play(Create(enc(r2, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"3 -- Résoudre un système : le pivot de Gauss", "Pivot de Gauss")
        op = pos(T(r"permis : \;$L_i \leftrightarrow L_j$ \qquad $L_i \leftarrow \lambda L_i\ (\lambda \neq 0)$ \qquad $L_i \leftarrow L_i + \lambda L_j$", sc=0.66, color=GRIS), -6.3, 2.15)
        self.ecr(self.a("g2", "Trois opérations"), op, rt=1.6)
        X = -5.6
        e1 = pos(M(r"x + y + z = 6", sc=0.9), X, 1.3); e2 = pos(M(r"2x + y - z = 1", sc=0.9), X, 0.65); e3 = pos(M(r"x - y + 2z = 5", sc=0.9), X, 0.0)
        ac = Brace(VGroup(e1, e2, e3), LEFT, color=CRAIE)
        self.at(self.a("g3", "Voici notre système"), FadeIn(ac), Ecrire(VGroup(e1, e2, e3), rt=1.2))
        o1 = pos(M(r"L_2 \leftarrow L_2 - 2L_1", sc=0.8, color=ORANGE), 0.3, 0.65); o2 = pos(M(r"L_3 \leftarrow L_3 - L_1", sc=0.8, color=ORANGE), 0.3, 0.0)
        e2b = pos(M(r"-y - 3z = -11", sc=0.9), X, 0.65); e3b = pos(M(r"-2y + z = -1", sc=0.9), X, 0.0)
        self.at(self.a("g3", "On fait L deux"), Ecrire(o1, rt=0.6)); self.play(ReplacementTransform(e2, e2b), run_time=0.7)
        self.at(self.a("g3", "et L trois"), Ecrire(o2, rt=0.6)); self.play(ReplacementTransform(e3, e3b), run_time=0.7)
        self.at(self.a("g4", "Les x ont disparu"), Indicate(VGroup(e2b, e3b), color=JAUNE, scale_factor=1.08), run_time=0.7)
        o3 = pos(M(r"L_3 \leftarrow L_3 - 2L_2", sc=0.8, color=ORANGE), 0.3, 0.0)
        e3c = pos(M(r"7z = 21", sc=0.9), X, 0.0)
        self.at(self.a("g4", "L trois reçoit L trois moins deux"), FadeOut(o1), FadeOut(o2), Ecrire(o3, rt=0.6)); self.play(ReplacementTransform(e3b, e3c), run_time=0.7)
        s1 = pos(M(r"z = 3", sc=0.9, color=JAUNE), X, -1.1)
        self.ecr(self.a("g5", "Donc z vaut"), s1, rt=0.5)
        s2 = pos(M(r"-y - 9 = -11 \;\Rightarrow\; y = 2", sc=0.9, color=JAUNE), X, -1.75)
        s3 = pos(M(r"x = 6 - 2 - 3 = 1", sc=0.9, color=JAUNE), X, -2.4)
        self.ecr(self.a("g6", "On remonte"), s2, rt=1.1); self.ecr(self.a("g6", "Et x égale"), s3, rt=1.0)
        so = M(r"(x, y, z) = (1, 2, 3)", sc=1.0, color=JAUNE).move_to([3.3, -1.75, 0])
        vk = T(r"vérifié dans les 3 équations \;$\checkmark$", sc=0.6, color=VERT).next_to(so, DOWN, buff=0.35)
        self.at(self.a("g7", "On vérifie"), FadeIn(vk), run_time=0.5)
        self.at(self.a("g7", "la solution unique"), Ecrire(so, rt=0.8)); self.play(Create(enc(so, col=JAUNE)), run_time=0.4)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"3 -- Combien de solutions ?", "Pivot de Gauss")
        R = [(r"une ligne $0 = c$ avec $c \neq 0$ : \textbf{aucune} solution", ROUGE, r"\left(\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & 5 \end{array}\right)", "h2", "Si une ligne", 1.4),
             (r"rang $r$ = nombre d'inconnues : solution \textbf{unique}", VERT, r"\left(\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 4 & 8 \end{array}\right)", "h3", "on compte les pivots", 0.0),
             (r"$r$ $<$ nombre $p$ d'inconnues : \textbf{infinité}, $p - r$ inconnues libres", ORANGE, r"\left(\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & 1 & 1 & 2 \end{array}\right)", "h4", "Et s'il y a moins", -1.4)]
        nb = T(r"rang = nombre de pivots", sc=0.75, color=JAUNE).move_to([0, -2.85, 0])
        for k, (tx, col, ex, sid, fr, y) in enumerate(R):
            t = pos(T(tx, sc=0.68, color=col), -6.3, y); e = M(ex, sc=0.8).move_to([4.6, y, 0])
            self.at(self.a(sid, fr), Ecrire(t, rt=1.3), FadeIn(e))
            if k == 1: self.at(self.a("h3", "Si r égale"), Ecrire(nb, rt=0.8))
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"4 -- Inverser une matrice de taille 2", "Inverse")
        d = pos(M(r"AB = BA = I_n \;\Longrightarrow\; A \text{ inversible},\ B = A^{-1}", sc=0.85), -6.3, 2.05)
        self.ecr(self.a("i1", "A est inversible"), d, rt=1.3)
        f = M(r"A = " + pm(["a", "b"], ["c", "d"]), r"\qquad A^{-1} = \frac{1}{ad - bc}" + pm(["d", "-b"], ["-c", "a"]), sc=1.0).move_to([0, 0.55, 0])
        self.at(self.a("i2", "il y a une formule"), Ecrire(f[0], rt=0.7)); self.at(self.a("i2", "on échange"), Ecrire(f[1], rt=1.6))
        self.play(Create(enc(f, col=JAUNE)), run_time=0.4)
        nz = pos(T(r"si $ad - bc = 0$ : \textbf{pas inversible}", sc=0.75, color=ROUGE), -6.3, -0.9)
        self.ecr(self.a("i3", "Et si"), nz, rt=1.0)
        ex = pos(M(pm(["2", "1"], ["5", "3"]), r"\;:\;\; ad - bc = 6 - 5 = 1", r"\;\;\Longrightarrow\;\; A^{-1} = " + pm(["3", "-1"], ["-5", "2"]), sc=0.88), -6.3, -2.35)
        ex[2].set_color(JAUNE)
        self.at(self.a("i4", "Exemple"), Ecrire(ex[0], rt=0.5)); self.at(self.a("i4", "Le déterminant"), Ecrire(ex[1], rt=0.9))
        self.at(self.a("i4", "L'inverse"), Ecrire(ex[2], rt=1.0))
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"4 -- Inverser : la méthode du système", "Inverse")
        m = pos(T(r"Résoudre $AX = Y$ en gardant $Y = (a, b, c)$ \textbf{en lettres}", sc=0.75, color=VERT), -6.3, 2.15)
        self.ecr(self.a("j1", "une méthode efficace"), m, rt=1.3)
        A = pos(M(r"A = " + pm(["1", "0", "1"], ["1", "1", "0"], ["0", "1", "1"]), sc=0.85), -6.3, 0.75)
        s = VGroup(M(r"x + z = a", sc=0.85), M(r"x + y = b", sc=0.85), M(r"y + z = c", sc=0.85)).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        pos(s, -1.6, 0.75); ac = Brace(s, LEFT, color=CRAIE)
        self.ecr(self.a("j2", "Prenons cette matrice"), A, rt=0.9)
        self.at(self.a("j2", "Le système s'écrit"), FadeIn(ac), Ecrire(s, rt=1.4))
        so = pos(M(r"2(x + y + z) = a + b + c", sc=0.88, color=ORANGE), 1.6, 0.75)
        self.ecr(self.a("j3", "on additionne tout"), so, rt=1.0)
        r = pos(M(r"x = \tfrac{a + b - c}{2}, \qquad y = \tfrac{-a + b + c}{2}, \qquad z = \tfrac{a - b + c}{2}", sc=0.88), -6.3, -0.75)
        self.ecr(self.a("j4", "Puis on retranche"), r, rt=1.6)
        iv = M(r"A^{-1} = \frac{1}{2}" + pm(["1", "1", "-1"], ["-1", "1", "1"], ["1", "-1", "1"]), sc=0.85, color=JAUNE).move_to([2.7, -2.45, 0])
        ui = pos(T(r"solution unique pour tout $Y$ : \textbf{inversible}", sc=0.65, color=VERT), -6.3, -1.6)
        self.at(self.a("j5", "la matrice est inversible"), FadeIn(ui), run_time=0.5)
        self.at(self.a("j5", "Et on lit"), Ecrire(iv, rt=1.3)); self.play(Create(enc(iv, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, T(r"\textbf{Produit} : ligne $\times$ colonne ; $AB \neq BA$ en général", sc=0.75), "k2", 1.9),
                (VERT, T(r"\textbf{Puissance} : conjecture + récurrence, ou binôme avec $A = \lambda I + N$", sc=0.75), "k3", 0.75),
                (ORANGE, T(r"\textbf{Système} : pivot de Gauss ; nombre de pivots = rang", sc=0.75), "k4", -0.4),
                (ROUGE, T(r"\textbf{Inverse} : formule en taille 2, ou résolution de $AX = Y$", sc=0.75), "k5", -1.55)]
        for k, (col, F, sid, y) in enumerate(data):
            c = carte(k+1, col, -5.9, y); pos(F, -5.3, y)
            self.at(self.t(sid), Create(c[0]), FadeIn(c[1]), run_time=0.4); self.play(Ecrire(F, rt=1.6))
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice résolu -- L'énoncé", "Exercice résolu")
        A = M(r"A = " + pm(["0", "1", "1"], ["1", "0", "1"], ["1", "1", "0"]), sc=1.0).move_to([0, 1.3, 0])
        self.at(self.a("l2", "Soit A"), Ecrire(A, rt=1.2))
        q1 = pos(T(r"\textbf{1.} Calculer $A^2$ et montrer que $A^2 = A + 2I_3$.", sc=0.82, color=JAUNE), -6.3, -0.35)
        q2 = pos(T(r"\textbf{2.} En déduire que $A$ est inversible et calculer $A^{-1}$.", sc=0.82, color=JAUNE), -6.3, -1.1)
        self.ecr(self.a("l3", "Première question"), q1, rt=1.4); self.ecr(self.a("l4", "Deuxième question"), q2, rt=1.4)
        ch = M(r"\textbf{1.}\ \text{ligne} \times \text{colonne}", r"\qquad\qquad", r"\textbf{2.}\ \text{faire apparaître } I_3", sc=0.85, color=VERT).move_to([0, -2.5, 0])
        self.at(self.a("l5", "Pour la première question"), Ecrire(ch[0], rt=0.9)); self.at(self.a("l5", "Et pour la seconde"), Ecrire(ch[2], rt=1.0))
        self.play(Create(enc(ch, col=VERT)), run_time=0.4)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- La solution, étape par étape", "Exercice résolu")
        c1 = carte(1, BLEU, -6.1, 2.15)
        s1 = pos(M(r"(A^2)_{11} = 0 + 1 + 1 = 2", r"\qquad (A^2)_{12} = 0 + 0 + 1 = 1", sc=0.78), -5.55, 2.15)
        self.at(self.t("m1"), Create(c1[0]), FadeIn(c1[1]), run_time=0.4); self.at(self.a("m1", "Ligne un fois colonne un"), Ecrire(s1[0], rt=1.0))
        self.at(self.a("m2", "Ligne un fois colonne deux"), Ecrire(s1[1], rt=1.0))
        c2 = carte(2, VERT, -6.1, 0.95)
        s2 = pos(M(r"A^2 = " + pm(["2", "1", "1"], ["1", "2", "1"], ["1", "1", "2"]), sc=0.75), -5.55, 0.95)
        s2b = M(r"= A + 2I_3 \;\;\checkmark", sc=0.85, color=VERT).next_to(s2, RIGHT, buff=0.3)
        self.at(self.a("m2", "Et par symétrie"), Ecrire(s2, rt=1.2))
        self.at(self.t("m3"), Create(c2[0]), FadeIn(c2[1]), run_time=0.4); self.at(self.a("m3", "C'est exactement"), Ecrire(s2b, rt=0.9))
        c3 = carte(3, ORANGE, -6.1, -0.4)
        s3 = pos(M(r"A^2 - A = 2I_3", r"\;\Longrightarrow\; A(A - I_3) = 2I_3", sc=0.85), -5.55, -0.4)
        self.at(self.t("m4"), Create(c3[0]), FadeIn(c3[1]), run_time=0.4); self.at(self.a("m4", "A carré moins A"), Ecrire(s3[0], rt=0.9))
        self.at(self.a("m4", "On factorise"), Ecrire(s3[1], rt=1.0))
        s4 = pos(M(r"A \times \tfrac{1}{2}(A - I_3) = I_3", r"\;\Longrightarrow\; A^{-1} = \tfrac{1}{2}(A - I_3)", sc=0.85), -5.55, -1.1)
        s4[1].set_color(JAUNE)
        self.at(self.a("m5", "On divise par deux"), Ecrire(s4[0], rt=1.0)); self.at(self.a("m5", "Donc A est inversible"), Ecrire(s4[1], rt=1.0))
        s5 = pos(M(r"A^{-1} = \frac{1}{2}" + pm(["-1", "1", "1"], ["1", "-1", "1"], ["1", "1", "-1"]), sc=0.75, color=JAUNE), -5.55, -2.4)
        self.ecr(self.a("m6", "Soit, explicitement"), s5, rt=1.2); self.play(Create(enc(s5, col=JAUNE, buff=0.12)), run_time=0.3)
        c4 = carte(4, ROUGE, 0.6, -2.4)
        s6 = pos(T(r"Vérifier : $0 + \tfrac{1}{2} + \tfrac{1}{2} = 1$ \;$\checkmark$", sc=0.72), 1.15, -2.4)
        self.at(self.t("m7"), Create(c4[0]), FadeIn(c4[1]), run_time=0.4); self.at(self.a("m7", "Ligne un de A"), Ecrire(s6, rt=1.4))
        self.jusqua(self.t("m8") - 0.2)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        f1 = T(r"relation polynomiale $\Longrightarrow$ inverse sans pivot", sc=0.85, color=VERT).move_to([0, 0.8, 0])
        f2 = T(r"Suite : les matrices en deuxième année", sc=0.85, color=JAUNE).move_to([0, -0.4, 0])
        self.ecr(self.a("m8", "Retenez l'idée"), f1, rt=1.3); self.ecr(self.a("m8", "On la retrouvera"), f2, rt=1.3)
        self.fin()
