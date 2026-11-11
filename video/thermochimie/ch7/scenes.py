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
def fleche(a, b, col=BLEU): return Arrow(a.get_right(), b.get_left(), color=col, buff=0.15, stroke_width=3, max_tip_length_to_length_ratio=0.08)
LOGK = r"\log K^\circ \underset{298\,\mathrm{K}}{=} \frac{\gamma\,\Delta E^\circ}{0{,}06}"

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"THERMOCHIMIE \;·\; PT*", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Chapitre 7}", sc=1.3, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Thermodynamique de l'oxydoréduction", sc=0.95).move_to([0, 1.75, 0])
        tr = Line([-4.4, 1.3, 0], [4.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=0.9), Create(tr), run_time=1.0)
        g = VGroup(T(r"PTSI : potentiels", sc=0.7, color=BLEU), M(r"E,\ \text{Nernst},\ \text{règle du }\gamma", sc=0.7, color=BLEU)).arrange(DOWN, buff=0.12).move_to([-3.6, 0.55, 0])
        d = VGroup(T(r"PT : enthalpie libre", sc=0.7, color=VERT), M(r"\Delta_r G,\ \ K^\circ", sc=0.7, color=VERT)).arrange(DOWN, buff=0.12).move_to([3.6, 0.55, 0])
        pt = DoubleArrow([-1.4, 0.55, 0], [1.4, 0.55, 0], color=JAUNE, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.12)
        self.at(self.a("a1", "c'étaient des potentiels"), Ecrire(g, rt=1.0))
        self.at(self.a("a2", "on parle d'enthalpie libre"), Ecrire(d, rt=1.0))
        self.at(self.a("a3", "on fait le pont"), GrowFromCenter(pt), run_time=0.6)
        items = []
        for k, (txt, col) in enumerate([(r"$\Delta_r G$ et potentiels", BLEU), ("Constante d'équilibre", VERT), ("Enthalpie libre d'une demi-équation", ORANGE),
                                         ("Calcul d'un potentiel standard inconnu", ROUGE), (r"Exercice résolu : la dismutation du cuivre(I)", JAUNE)]):
            y = -0.7 - 0.62*k
            items.append(VGroup(carte(k+1, col, -3.6, y), pos(T(txt, sc=0.78), -3.0, y)))
        for it, (sid, fr) in zip(items, [("a4", "delta-r-G et les potentiels"), ("a4", "la constante d'équilibre"), ("a4", "l'enthalpie libre d'une"),
                                         ("a4", "et le calcul"), ("a5", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a5", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"7.1 -- Enthalpie libre et potentiels", r"1/4 · $\Delta_r G$ et potentiels")
        c1 = pos(M(r"\text{couple 1 : }\ \mathrm{Ox_1/Red_1}", sc=0.8, color=BLEU), -6.3, 2.1)
        c2 = pos(M(r"\text{couple 2 : }\ \mathrm{Ox_2/Red_2}", sc=0.8, color=VERT), 0.6, 2.1)
        self.at(self.a("b1", "Prenons deux couples"), Ecrire(c1, rt=0.8), Ecrire(c2, rt=0.8))
        rx = M(r"a_1\,\mathrm{Ox_1} + b_2\,\mathrm{Red_2} \;=\; b_1\,\mathrm{Red_1} + a_2\,\mathrm{Ox_2}", sc=0.85).move_to([-0.9, 1.3, 0])
        ge = M(r"(\gamma\ e^-)", sc=0.75, color=GRIS).next_to(rx, RIGHT, buff=0.4)
        self.at(self.a("b1", "L'oxydant du couple un"), Ecrire(rx, rt=1.3)); self.at(self.a("b1", "en échangeant"), FadeIn(ge), run_time=0.4)
        f = M(r"\Delta_r G", r"\;=\;", r"-\gamma F\,(E_1 - E_2)", sc=1.3, color=JAUNE).move_to([0, 0.1, 0])
        self.at(self.a("b2", "delta-r-G égale"), Ecrire(f, rt=1.2)); self.play(Create(enc(f, col=JAUNE)), run_time=0.4)
        e = pos(T(r"$E_1$, $E_2$ : potentiels de Nernst, composition \textbf{actuelle}", sc=0.7), -6.3, -1.1)
        fa = pos(M(r"F \approx 96\,500\ \mathrm{C\cdot mol^{-1}}\ \ (\text{Faraday})", sc=0.75, color=GRIS), -6.3, -1.7)
        self.ecr(self.a("b3", "E un et E deux"), e, rt=1.4); self.ecr(self.a("b3", "Et F, c'est"), fa, rt=1.1)
        fs = pos(M(r"\Delta_r G^\circ = -\gamma F\,(E_1^\circ - E_2^\circ)", sc=0.95, color=VERT), -6.3, -2.6)
        self.ecr(self.a("b4", "delta-r-G standard égale"), fs, rt=1.3)
        no = pos(T(r"origine : travail électrique dans une pile (chapitre 8)", sc=0.6, color=GRIS), -6.3, -3.35)
        self.ecr(self.a("b5", "Du travail électrique"), no, rt=1.0)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"7.1 -- Cohérence avec la loi de Nernst", r"1/4 · $\Delta_r G$ et potentiels")
        n = pos(M(r"E_1 = E_1^\circ + \frac{RT}{\gamma F}\ln\frac{a_{\mathrm{Ox_1}}^{a_1}}{a_{\mathrm{Red_1}}^{b_1}}", r"\qquad E_2 = E_2^\circ + \frac{RT}{\gamma F}\ln\frac{a_{\mathrm{Ox_2}}^{a_2}}{a_{\mathrm{Red_2}}^{b_2}}", sc=0.75, color=GRIS), -6.3, 1.95)
        self.at(self.a("c2", "On écrit Nernst"), Ecrire(n, rt=1.6))
        l2 = pos(M(r"E_1 - E_2 = (E_1^\circ - E_2^\circ) - \frac{RT}{\gamma F}\ln Q_r", sc=0.95), -6.3, 0.6)
        self.at(self.a("c2", "Il vient"), Ecrire(l2, rt=1.5))
        l3 = M(r"-\gamma F(E_1 - E_2)", r"\;=\;", r"-\gamma F(E_1^\circ - E_2^\circ)", r"\;+\;", r"RT\ln Q_r", sc=1.0).move_to([0, -0.75, 0])
        mu = pos(T(r"$\times\,(-\gamma F)$", sc=0.7, color=ORANGE), 3.4, 0.6)
        self.at(self.a("c3", "Multiplions"), FadeIn(mu), run_time=0.4); self.play(Ecrire(l3, rt=1.5))
        b = [(0, r"\Delta_r G", BLEU, "À gauche"), (2, r"\Delta_r G^\circ", VERT, "Puis delta-r-G standard")]
        for i, tx, col, fr in b:
            br = Brace(l3[i], DOWN, color=col); lb = M(tx, sc=0.8, color=col).next_to(br, DOWN, buff=0.1)
            self.at(self.a("c4", fr), Create(br), FadeIn(lb), run_time=0.5)
        self.at(self.a("c4", "Et le terme"), Indicate(l3[4], color=ORANGE), run_time=0.7)
        fi = M(r"\Delta_r G = \Delta_r G^\circ + RT\ln Q_r", sc=1.1, color=JAUNE).move_to([-0.8, -2.9, 0])
        ch5 = T(r"(chapitre 5) \;$\checkmark$", sc=0.65, color=VERT).next_to(fi, RIGHT, buff=0.5)
        self.at(self.a("c4", "C'est exactement"), Ecrire(fi, rt=1.0)); self.play(Create(enc(fi, col=JAUNE)), FadeIn(ch5), run_time=0.5)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"7.1 -- Sens d'évolution et équilibre", r"1/4 · $\Delta_r G$ et potentiels")
        s = pos(M(r"\Delta_r G < 0 \;\Longleftrightarrow\; E_1 > E_2", sc=1.0), -6.3, 1.9)
        s2 = pos(T(r"l'oxydant du couple de plus \textbf{haut} potentiel est réduit", sc=0.66, color=BLEU), -6.3, 1.15)
        self.ecr(self.a("d2", "Delta-r-G négatif"), s, rt=1.0); self.ecr(self.a("d2", "L'oxydant du couple"), s2, rt=1.4)
        ax = Arrow([4.3, -2.3, 0], [4.3, 1.0, 0], color=CRAIE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.06)
        le = M("E", sc=0.8).next_to(ax.get_end(), RIGHT, buff=0.15)
        o1 = M(r"\mathrm{Ox_1}", sc=0.8, color=BLEU).move_to([3.3, 0.2, 0]); r1 = M(r"\mathrm{Red_1}", sc=0.8, color=BLEU).move_to([5.4, 0.2, 0])
        o2 = M(r"\mathrm{Ox_2}", sc=0.8, color=VERT).move_to([3.3, -1.6, 0]); r2 = M(r"\mathrm{Red_2}", sc=0.8, color=VERT).move_to([5.4, -1.6, 0])
        t1 = Line([4.1, 0.2, 0], [4.5, 0.2, 0], color=BLEU, stroke_width=4); t2 = Line([4.1, -1.6, 0], [4.5, -1.6, 0], color=VERT, stroke_width=4)
        self.at(self.a("d3", "Sur une échelle"), Create(ax), FadeIn(le), *[FadeIn(m) for m in (o1, r1, o2, r2, t1, t2)], run_time=0.7)
        gm = VMobject(color=JAUNE, stroke_width=5).set_points_as_corners([o1.get_bottom() + DOWN*0.1, r2.get_top() + UP*0.1])
        tip = Arrow(o1.get_bottom() + DOWN*0.1, r2.get_top() + UP*0.1, color=JAUNE, buff=0, stroke_width=5)
        self.at(self.a("d3", "l'oxydant du haut"), GrowArrow(tip), run_time=0.7)
        ju = T(r"règle du $\gamma$ \textbf{justifiée} !", sc=0.72, color=JAUNE).move_to([4.3, -2.8, 0])
        self.ecr(self.a("d3", "La règle du gamma"), ju, rt=0.9)
        e = pos(M(r"\text{équilibre : }\ \Delta_r G = 0 \;\Longleftrightarrow\; E_1 = E_2", sc=0.9, color=VERT), -6.3, -0.9)
        e2 = pos(T(r"la solution n'a plus qu'\textbf{un seul} potentiel", sc=0.66, color=GRIS), -6.3, -1.6)
        self.ecr(self.a("d4", "à l'équilibre"), e, rt=1.3); self.ecr(self.a("d4", "La solution"), e2, rt=1.1)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"7.2 -- Constante d'équilibre", "2/4 · Constante d'équilibre")
        l1 = pos(M(r"\Delta_r G^\circ = -RT\ln K^\circ", r"\;=\; -\gamma F\,(E_1^\circ - E_2^\circ)", sc=0.95), -6.3, 2.0)
        self.at(self.a("e1", "On égale moins"), Ecrire(l1[0], rt=0.9)); self.at(self.a("e1", "et moins gamma F"), Ecrire(l1[1], rt=1.0))
        l2 = pos(M(r"\ln K^\circ = \frac{\gamma F}{RT}\,(E_1^\circ - E_2^\circ)", sc=0.95), -6.3, 0.75)
        self.ecr(self.a("e2", "Résultat"), l2, rt=1.3)
        lk = pos(M(LOGK, sc=1.15, color=JAUNE), 0.6, 0.75)
        self.ecr(self.a("e3", "log K standard égale"), lk, rt=1.2)
        self.at(self.a("e3", "La formule à connaître"), Create(enc(lk, col=JAUNE)), run_time=0.4)
        og = pos(T(r"\textbf{Ordres de grandeur}", sc=0.72, color=ORANGE), -6.3, -0.7)
        o1 = pos(M(r"\Delta E^\circ = 0{,}1\ \mathrm{V},\ \gamma = 1 \;\Rightarrow\; K^\circ \approx 10^{1{,}7} \approx 50", sc=0.82), -6.3, -1.45)
        o2 = pos(M(r"\text{pile Daniell : }\ \Delta E^\circ = 1{,}10\ \mathrm{V},\ \gamma = 2 \;\Rightarrow\; K^\circ \approx 10^{37}", sc=0.82), -6.3, -2.3)
        to = pos(T(r"réaction \textbf{totale}", sc=0.72, color=VERT), -6.3, -3.1)
        self.at(self.a("e4", "Ordres de grandeur"), FadeIn(og), run_time=0.4); self.ecr(self.a("e4", "Un écart"), o1, rt=1.4)
        self.ecr(self.a("e5", "Et pour la pile Daniell"), o2, rt=1.5); self.ecr(self.a("e5", "Une réaction totale"), to, rt=0.6)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"7.2 -- À vous : une constante d'équilibre", "2/4 · Constante d'équilibre")
        cad = RoundedRectangle(width=12.4, height=1.6, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, 1.7, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.72, color=JAUNE), -5.9, 1.7)
        e1 = pos(M(r"\mathrm{Ce^{4+} + Fe^{2+} = Ce^{3+} + Fe^{3+}}", sc=0.8), -4.0, 2.05)
        kq = M(r"K^\circ\ ?", sc=0.85, color=JAUNE).next_to(e1, RIGHT, buff=0.6)
        e2 = pos(M(r"E^\circ(\mathrm{Ce^{4+}/Ce^{3+}}) = 1{,}74\ \mathrm{V} \qquad E^\circ(\mathrm{Fe^{3+}/Fe^{2+}}) = 0{,}77\ \mathrm{V}", sc=0.7, color=GRIS), -4.0, 1.4)
        self.at(self.t("f1"), Create(cad), Ecrire(tq, rt=0.4), run_time=0.5)
        self.at(self.a("f1", "Les ions cérium"), Ecrire(e1, rt=1.1)); self.at(self.a("f1", "Avec les potentiels"), Ecrire(e2, rt=1.3))
        self.at(self.a("f1", "calculez K standard"), Ecrire(kq, rt=0.4))
        pa, arc = chrono(5.7, 1.7)
        self.jusqua(self.PH["f1"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("f2") - self.renderer.time - 0.1), rate_func=linear)
        r1 = pos(M(r"\gamma = 1, \qquad \Delta E^\circ = 1{,}74 - 0{,}77 = 0{,}97\ \mathrm{V}", sc=0.85), -6.0, 0.2)
        self.at(self.a("f2", "Réponse"), FadeOut(pa), FadeOut(arc), Ecrire(r1, rt=1.3))
        r2 = pos(M(r"\log K^\circ = \frac{0{,}97}{0{,}06} \approx 16", r"\;\Rightarrow\; K^\circ \approx 10^{16}", sc=0.9), -6.0, -1.0)
        r2[1].set_color(JAUNE)
        self.at(self.a("f3", "Donc log K standard"), Ecrire(r2[0], rt=1.2)); self.at(self.a("f3", "K standard vaut dix"), Ecrire(r2[1], rt=0.7))
        r3 = pos(T(r"réaction totale : idéale pour un \textbf{titrage}", sc=0.75, color=VERT), -6.0, -2.2)
        self.ecr(self.a("f3", "la réaction est totale"), r3, rt=1.2)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"7.3 -- Enthalpie libre d'une demi-équation", "3/4 · Demi-équations")
        de = pos(M(r"\alpha\,\mathrm{Ox} + \gamma\,e^- + \dots \;=\; \beta\,\mathrm{Red} + \dots", sc=0.9), -6.3, 2.05)
        self.ecr(self.a("g1", "À chaque demi-équation"), de, rt=1.1)
        cv = M(r"\Delta_{1/2}G^\circ = -\gamma F\,E^\circ(\mathrm{Ox/Red})", sc=1.2, color=JAUNE).move_to([0, 0.85, 0])
        tc = T(r"(convention)", sc=0.6, color=GRIS).next_to(cv, RIGHT, buff=0.5)
        self.at(self.a("g2", "Par convention"), FadeIn(tc), Ecrire(cv, rt=1.2)); self.play(Create(enc(cv, col=JAUNE)), run_time=0.4)
        es = pos(T(r"référence : l'électrode standard à hydrogène, \;$E^\circ(\mathrm{H^+/H_2}) = 0$", sc=0.68, color=GRIS), -6.3, -0.35)
        self.ecr(self.a("g3", "par rapport à"), es, rt=1.4)
        ad = pos(M(r"\Delta_r G^\circ = \Delta_{1/2}G_1^\circ - \Delta_{1/2}G_2^\circ", sc=0.9, color=VERT), -6.3, -1.3)
        el = pos(T(r"elles s'additionnent ; les électrons s'éliminent", sc=0.64, color=VERT), 0.3, -1.3)
        self.ecr(self.a("g4", "Ces grandeurs"), ad, rt=1.2); self.ecr(self.a("g4", "Les électrons"), el, rt=1.0)
        ro = T(r"\textbf{Règle d'or} : on n'additionne \textbf{jamais} les potentiels !", sc=0.85, color=ROUGE).move_to([0, -2.65, 0])
        self.ecr(self.a("g5", "la règle d'or"), ro, rt=1.3); self.play(Create(enc(ro)), run_time=0.4)
        self.at(self.a("g5", "Ce sont les enthalpies"), Indicate(ad, color=JAUNE, scale_factor=1.08), run_time=0.8)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"7.4 -- Calculer un potentiel standard : la méthode", "4/4 · Potentiel inconnu")
        st = [(BLEU, T(r"Écrire la demi-équation cherchée, avec ses $\gamma$ électrons", sc=0.7), "h2", 1.8),
              (VERT, T(r"\textbf{Combiner} des demi-équations et des réactions connues ($K_s$, $K_a$, $\Delta_f G^\circ$)", sc=0.66), "h3", 0.75),
              (ORANGE, T(r"Additionner les \textbf{enthalpies libres} : \;$\Delta_{1/2}G^\circ = -\gamma F E^\circ$, \;$\Delta_r G^\circ = -RT\ln K^\circ$", sc=0.66), "h4", -0.3),
              (ROUGE, T(r"Diviser par $-\gamma F$", sc=0.7), "h5", -1.35)]
        for k, (col, F, sid, y) in enumerate(st):
            c = carte(k+1, col, -6.0, y); pos(F, -5.4, y)
            self.at(self.t(sid), Create(c[0]), FadeIn(c[1]), run_time=0.4); self.play(Ecrire(F, rt=1.4))
        fi = T(r"\textit{Et c'est fini !}", sc=0.75, color=JAUNE).move_to([0, -2.6, 0])
        self.ecr(self.a("h5", "Et c'est fini"), fi, rt=0.6)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"7.4 -- Exemple : le fer", "4/4 · Potentiel inconnu")
        A = M(r"\mathrm{Fe^{3+}}", sc=1.0).move_to([-4.5, 0.9, 0]); B = M(r"\mathrm{Fe^{2+}}", sc=1.0).move_to([0, 0.9, 0]); C = M(r"\mathrm{Fe(s)}", sc=1.0).move_to([4.5, 0.9, 0])
        f1, f2 = fleche(A, B), fleche(B, C)
        l1 = M(r"0{,}77\ \mathrm{V}", sc=0.65, color=BLEU).next_to(f1, UP, buff=0.1); g1 = M(r"\gamma = 1", sc=0.6, color=GRIS).next_to(f1, DOWN, buff=0.1)
        l2 = M(r"-0{,}44\ \mathrm{V}", sc=0.65, color=BLEU).next_to(f2, UP, buff=0.1); g2 = M(r"\gamma = 2", sc=0.6, color=GRIS).next_to(f2, DOWN, buff=0.1)
        self.at(self.a("i1", "On connaît fer trois"), FadeIn(A), FadeIn(B), GrowArrow(f1), FadeIn(l1), FadeIn(g1), run_time=0.7)
        self.at(self.a("i1", "et fer deux sur fer"), FadeIn(C), GrowArrow(f2), FadeIn(l2), FadeIn(g2), run_time=0.7)
        arc = CurvedArrow(A.get_top() + UP*0.1, C.get_top() + UP*0.1, angle=-PI/4, color=ORANGE, stroke_width=3)
        la = M(r"\gamma = 3 : \; E_3^\circ\ ?", sc=0.7, color=ORANGE).move_to([0, 2.55, 0])
        self.at(self.a("i2", "On cherche"), Create(arc), FadeIn(la), run_time=0.8)
        s = pos(M(r"-3F\,E_3^\circ = -1\cdot F\,E_1^\circ - 2F\,E_2^\circ", sc=0.95), -6.3, -0.45)
        self.ecr(self.a("i3", "On additionne"), s, rt=1.5)
        r = pos(M(r"E_3^\circ = \frac{E_1^\circ + 2E_2^\circ}{3} = \frac{0{,}77 - 0{,}88}{3}", r"\;=\; -0{,}04\ \mathrm{V}", sc=0.95), -6.3, -1.6)
        r[1].set_color(JAUNE)
        self.at(self.a("i4", "On divise"), Ecrire(r[0], rt=1.3)); self.at(self.a("i4", "E trois standard vaut"), Ecrire(r[1], rt=0.6))
        self.play(Create(enc(r[1], col=JAUNE, buff=0.12)), run_time=0.3)
        p = pos(T(r"\textbf{Piège} : pas la moyenne simple ($0{,}17$ V) ! Moyenne \textbf{pondérée par $\gamma$}", sc=0.72, color=ROUGE), -6.3, -2.95)
        self.ecr(self.a("i5", "Attention au piège"), p, rt=1.6)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"7.4 -- Exemple : l'électrode au calomel", "4/4 · Potentiel inconnu")
        t = pos(T(r"Calomel $\mathrm{Hg_2Cl_2(s)}$ : électrode de référence", sc=0.75, color=BLEU), -6.3, 2.1)
        self.ecr(self.a("j1", "l'électrode au calomel"), t, rt=1.1)
        d1 = pos(M(r"E_1^\circ(\mathrm{Hg_2^{2+}/Hg}) = 0{,}797\ \mathrm{V}", sc=0.75, color=GRIS), -6.3, 1.4)
        d2 = pos(M(r"\mathrm{p}K_s(\mathrm{Hg_2Cl_2}) = 17{,}9", sc=0.75, color=GRIS), 0.6, 1.4)
        self.ecr(self.a("j2", "On connaît le couple"), d1, rt=1.0); self.ecr(self.a("j2", "Et le produit"), d2, rt=0.8)
        X, Y = -5.9, 1.0
        r1 = pos(M(r"\mathrm{Hg_2Cl_2(s) = Hg_2^{2+} + 2\,Cl^-}", sc=0.78), X, 0.45); g1 = pos(M(r"\Delta_r G^\circ = -RT\ln K_s", sc=0.72, color=ORANGE), Y, 0.45)
        s2 = pos(M(r"+", sc=0.8), -6.45, -0.3)
        r2 = pos(M(r"\mathrm{Hg_2^{2+} + 2\,e^- = 2\,Hg(l)}", sc=0.78), X, -0.3); g2 = pos(M(r"\Delta_{1/2}G^\circ = -2F\,E_1^\circ", sc=0.72, color=ORANGE), Y, -0.3)
        hl = Line([-6.5, -0.72, 0], [6.6, -0.72, 0], color=GRIS, stroke_width=1.5)
        s3 = pos(M(r"=", sc=0.8), -6.45, -1.15)
        r3 = pos(M(r"\mathrm{Hg_2Cl_2(s) + 2\,e^- = 2\,Hg(l) + 2\,Cl^-}", sc=0.78, color=JAUNE), X, -1.15)
        g3 = pos(M(r"-2F\,E^\circ = -RT\ln K_s - 2F\,E_1^\circ", sc=0.72, color=JAUNE), Y, -1.15)
        self.ecr(self.a("j3", "la dissolution"), r1, rt=1.0); self.at(self.a("j3", "plus la réduction"), FadeIn(s2), Ecrire(r2, rt=1.0))
        self.at(self.a("j3", "On obtient"), Create(hl), FadeIn(s3), Ecrire(r3, rt=1.2))
        self.at(self.a("j4", "Les enthalpies libres"), Ecrire(g1, rt=0.6), Ecrire(g2, rt=0.6)); self.play(Ecrire(g3, rt=0.9))
        res = pos(M(r"E^\circ = E_1^\circ + \frac{RT}{2F}\ln K_s = 0{,}797 - 0{,}0296\times 17{,}9", r"\;=\; 0{,}27\ \mathrm{V}", sc=0.85), -6.3, -2.2)
        res[1].set_color(JAUNE)
        self.at(self.a("j4", "On divise"), Ecrire(res[0], rt=1.4)); self.at(self.a("j4", "et E standard vaut"), Ecrire(res[1], rt=0.6))
        self.play(Create(enc(res[1], col=JAUNE, buff=0.12)), run_time=0.3)
        pg = pos(T(r"Gardez $0{,}059$ : face à un grand p$K_s$, l'arrondi à $0{,}06$ coûte $0{,}01$ V", sc=0.68, color=ORANGE), -6.3, -3.3)
        self.ecr(self.a("j5", "Un détail"), pg, rt=1.5)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"7.4 -- À partir des enthalpies libres de formation", "4/4 · Potentiel inconnu")
        de = pos(M(r"\mathrm{O_2(g) + 4\,H^+ + 4\,e^- = 2\,H_2O(l)}", sc=0.95), -6.3, 2.0)
        self.ecr(self.a("k1", "Dernier exemple"), de, rt=1.1)
        es = pos(M(r"\xrightarrow{\ \text{avec l'ESH}\ }\quad \mathrm{O_2(g) + 2\,H_2(g) \longrightarrow 2\,H_2O(l)}", r"\qquad \gamma = 4", sc=0.85), -6.3, 1.1)
        es[1].set_color(ORANGE)
        self.at(self.a("k2", "Associée"), Ecrire(es[0], rt=1.4)); self.at(self.a("k2", "avec quatre électrons"), Ecrire(es[1], rt=0.5))
        g = pos(M(r"\Delta_r G^\circ = 2\,\Delta_f G^\circ(\mathrm{H_2O,\ell}) = 2\times(-237{,}1)", r"\;=\; -474{,}2\ \mathrm{kJ\cdot mol^{-1}}", sc=0.85), -6.3, 0.05)
        self.at(self.a("k3", "Son enthalpie libre"), Ecrire(g[0], rt=1.4)); self.at(self.a("k3", "Soit moins"), Ecrire(g[1], rt=0.9))
        e4 = pos(M(r"\;=\; -4F\,(E^\circ - 0)", sc=0.85, color=BLEU), -2.0, -0.85)
        self.ecr(self.a("k4", "Elle égale"), e4, rt=0.8)
        r = M(r"E^\circ(\mathrm{O_2/H_2O}) = \frac{474{,}2\times10^3}{4\times 96\,485}", r"\;=\; 1{,}23\ \mathrm{V}", sc=1.0).move_to([0, -2.3, 0])
        r[1].set_color(JAUNE)
        self.at(self.a("k4", "On divise"), Ecrire(r[0], rt=1.2)); self.at(self.a("k4", "et E standard vaut"), Ecrire(r[1], rt=0.6))
        self.at(self.a("k4", "La valeur bien connue"), Create(enc(r[1], col=JAUNE, buff=0.12)), run_time=0.4)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, M(r"\Delta_r G = -\gamma F\,\Delta E \qquad \text{sens d'évolution : règle du }\gamma", sc=0.8), "l2", 1.85),
                (VERT, M(LOGK, sc=0.85), "l3", 0.45),
                (ORANGE, T(r"Potentiel inconnu : additionner les \textbf{enthalpies libres}, jamais les potentiels !", sc=0.72), "l4", -1.0)]
        for k, (col, F, sid, y) in enumerate(data):
            c = carte(k+1, col, -5.9, y); pos(F, -5.3, y)
            self.at(self.t(sid), Create(c[0]), FadeIn(c[1]), run_time=0.4); self.play(Ecrire(F, rt=1.8))
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- Le cuivre au degré +I", "Exercice résolu")
        A = M(r"\mathrm{Cu^{2+}}", sc=1.1).move_to([-4.0, 1.7, 0]); B = M(r"\mathrm{Cu^{+}}", sc=1.1).move_to([0, 1.7, 0]); C = M(r"\mathrm{Cu(s)}", sc=1.1).move_to([4.0, 1.7, 0])
        self.at(self.a("m1", "au degré deux"), FadeIn(A), run_time=0.4); self.at(self.a("m1", "au degré un"), FadeIn(B), run_time=0.4)
        self.at(self.a("m1", "et à l'état de métal"), FadeIn(C), run_time=0.4)
        f1, f2 = fleche(A, B), fleche(B, C)
        l1 = M(r"0{,}16\ \mathrm{V}", sc=0.7, color=BLEU).next_to(f1, UP, buff=0.1); l2 = M(r"0{,}52\ \mathrm{V}", sc=0.7, color=BLEU).next_to(f2, UP, buff=0.1)
        self.at(self.a("m2", "zéro virgule seize"), GrowArrow(f1), FadeIn(l1), run_time=0.6)
        self.at(self.a("m2", "et zéro virgule cinquante-deux"), GrowArrow(f2), FadeIn(l2), run_time=0.6)
        q1 = pos(T(r"\textbf{1.} $E^\circ(\mathrm{Cu^{2+}/Cu})$ ?", sc=0.8, color=JAUNE), -6.4, 0.4)
        q2 = pos(T(r"\textbf{2.} Solution de $\mathrm{Cu^+}$ à $0{,}10\ \mathrm{mol\cdot L^{-1}}$ : stable ? Composition à l'équilibre ?", sc=0.78, color=JAUNE), -6.4, -0.4)
        self.ecr(self.a("m3", "Première question"), q1, rt=0.9); self.ecr(self.a("m4", "Deuxième question"), q2, rt=2.0)
        r1 = pos(M(r"E^\circ \;\Longleftarrow\; \text{combiner, additionner les } \Delta_{1/2}G^\circ", sc=0.85, color=VERT), -6.4, -1.6)
        r2 = pos(M(r"\text{stabilité} \;\Longleftarrow\; K^\circ", sc=0.85, color=VERT), -6.4, -2.45)
        self.ecr(self.a("m5", "Pour le potentiel"), r1, rt=1.3); self.ecr(self.a("m5", "Pour la stabilité"), r2, rt=0.9)
        self.fin()

class S13(Cours):
    sid = "S13"
    def construct(self):
        self.entete(r"Exercice résolu -- La solution, étape par étape", "Exercice résolu")
        c1 = carte(1, BLEU, -6.1, 2.15)
        s1 = pos(M(r"\mathrm{Cu^{2+} + 2\,e^- = Cu}", r"\;=\; (\mathrm{Cu^{2+} + e^- = Cu^+}) + (\mathrm{Cu^+ + e^- = Cu})", sc=0.7), -5.55, 2.15)
        self.at(self.t("n1"), Create(c1[0]), FadeIn(c1[1]), run_time=0.4)
        self.at(self.a("n1", "La demi-équation"), Ecrire(s1[0], rt=0.8)); self.at(self.a("n1", "la somme des deux"), Ecrire(s1[1], rt=1.3))
        s2 = pos(M(r"-2F\,E^\circ = -F\times0{,}16 - F\times0{,}52", r"\;\Rightarrow\; E^\circ = 0{,}34\ \mathrm{V}", sc=0.72), -5.55, 1.45)
        s2[1].set_color(JAUNE)
        self.at(self.a("n2", "Moins deux F"), Ecrire(s2[0], rt=1.3)); self.at(self.a("n2", "Donc E standard"), Ecrire(s2[1], rt=0.6))
        mo = T(r"poids égaux : la moyenne", sc=0.58, color=GRIS).next_to(s2, RIGHT, buff=0.35)
        self.at(self.a("n3", "Ici, c'est bien"), FadeIn(mo), run_time=0.5)
        c2 = carte(2, ORANGE, -6.1, 0.55)
        ax = Arrow([4.6, -1.15, 0], [4.6, 1.0, 0], color=CRAIE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.07)
        le = M(r"E^\circ", sc=0.6).next_to(ax.get_end(), LEFT, buff=0.15)
        ha = VGroup(M(r"\mathrm{Cu^+}", sc=0.7, color=BLEU).move_to([3.85, 0.5, 0]), Line([4.4, 0.5, 0], [4.8, 0.5, 0], color=BLEU, stroke_width=4), M(r"\mathrm{Cu}", sc=0.7, color=BLEU).move_to([5.45, 0.5, 0]), M(r"0{,}52", sc=0.5, color=GRIS).move_to([6.35, 0.5, 0]))
        ba = VGroup(M(r"\mathrm{Cu^{2+}}", sc=0.7, color=VERT).move_to([3.85, -0.75, 0]), Line([4.4, -0.75, 0], [4.8, -0.75, 0], color=VERT, stroke_width=4), M(r"\mathrm{Cu^+}", sc=0.7, color=VERT).move_to([5.45, -0.75, 0]), M(r"0{,}16", sc=0.5, color=GRIS).move_to([6.35, -0.75, 0]))
        s4 = pos(T(r"$\mathrm{Cu^+}$ : oxydant en haut, réducteur en bas", sc=0.68), -5.55, 0.55)
        self.at(self.t("n4"), Create(c2[0]), FadeIn(c2[1]), run_time=0.4)
        self.at(self.a("n4", "Placez les couples"), Create(ax), FadeIn(le), FadeIn(ha), FadeIn(ba), run_time=0.7)
        self.at(self.a("n4", "L'ion cuivre un est"), Ecrire(s4, rt=1.1), Indicate(ha[0], color=JAUNE), Indicate(ba[2], color=JAUNE))
        gm = Arrow(ha[0].get_bottom() + DOWN*0.05, ba[2].get_top() + UP*0.05, color=JAUNE, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.15)
        self.at(self.a("n5", "il réagit"), GrowArrow(gm), run_time=0.6)
        s5 = pos(M(r"2\,\mathrm{Cu^+} = \mathrm{Cu^{2+}} + \mathrm{Cu(s)}", r"\quad\text{(dismutation)}", sc=0.72), -5.55, -0.1)
        s5[1].set_color(ORANGE)
        self.ecr(self.a("n5", "C'est une dismutation"), s5, rt=1.3)
        s6 = pos(M(r"\Delta E^\circ = 0{,}36\ \mathrm{V} \Rightarrow \log K^\circ = \frac{0{,}36}{0{,}06} = 6", r"\;\Rightarrow\; K^\circ = 10^6", sc=0.68), -5.55, -0.85)
        s6[1].set_color(JAUNE)
        self.at(self.a("n6", "Un électron échangé"), Ecrire(s6[0], rt=1.4)); self.at(self.a("n6", "K standard égale"), Ecrire(s6[1], rt=0.5))
        c3 = carte(3, VERT, -6.1, -1.85)
        s7 = pos(M(r"\text{quasi totale : }\ [\mathrm{Cu^{2+}}] = 0{,}050", sc=0.7), -5.55, -1.85)
        self.at(self.t("n7"), Create(c3[0]), FadeIn(c3[1]), run_time=0.4); self.ecr(self.a("n7", "Réaction quasi totale"), s7, rt=1.3)
        s8 = pos(M(r"[\mathrm{Cu^+}] = \sqrt{\frac{0{,}050}{10^6}}", r"\;=\; 2{,}2\times10^{-4}\ \mathrm{mol\cdot L^{-1}}", sc=0.7), -0.5, -1.85)
        s8[1].set_color(JAUNE)
        self.at(self.a("n8", "Et l'ion cuivre un restant"), Ecrire(s8[0], rt=0.9)); self.at(self.a("n8", "deux virgule deux"), Ecrire(s8[1], rt=0.8))
        c4 = carte(4, ROUGE, -6.1, -2.8)
        s9 = pos(T(r"Vérifier : $2{,}2\times10^{-4} \ll 0{,}10$ \;$\checkmark$ \quad hypothèse validée", sc=0.7), -5.55, -2.8)
        s9b = pos(T(r"$\mathrm{Cu^+}$ se \textbf{dismute} dans l'eau !", sc=0.72, color=JAUNE), -5.55, -3.45)
        self.at(self.t("n9"), Create(c4[0]), FadeIn(c4[1]), run_time=0.4); self.ecr(self.a("n9", "C'est bien négligeable"), s9, rt=1.4)
        self.ecr(self.a("n9", "Conclusion"), s9b, rt=1.0)
        self.jusqua(self.t("n10") - 0.2)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        nx = T(r"Chapitre 8 \;$\longrightarrow$\; les piles électrochimiques", sc=0.85, color=JAUNE).move_to([0, 0.3, 0])
        self.ecr(self.a("n10", "les piles électrochimiques"), nx, rt=1.6)
        self.fin()
