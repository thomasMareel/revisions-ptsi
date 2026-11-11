from base import *
D = r"\mathrm{d}"
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def boite(txt, col, fond, w=3.5, h=1.0):
    r = RoundedRectangle(width=w, height=h, corner_radius=0.1, color=col, stroke_width=2.5, fill_color=fond, fill_opacity=0.25)
    return VGroup(r, txt.move_to(r))
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)
def chrono(x, y):
    pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([x, y, 0])
    arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
    return pa, arc

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"THERMOCHIMIE \;·\; PT*", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Chapitre 4}", sc=1.3, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Premier principe : effets thermiques des réactions", sc=0.95).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=0.9), Create(tr), run_time=1.0)
        q1 = M(r"1\ \mathrm{m^3}\ \text{de gaz}", r"\;\longrightarrow\;", r"?\ \mathrm{kWh}", sc=0.85, color=BLEU).move_to([-2.9, 0.55, 0]); q1[2].set_color(JAUNE)
        q2 = M(r"T_{\text{flamme}}", r"\;=\;", r"?\ \mathrm{K}", sc=0.85, color=ORANGE).move_to([3.1, 0.55, 0]); q2[2].set_color(JAUNE)
        self.at(self.a("a1", "Un mètre cube"), Ecrire(VGroup(q1[0], q1[1]), rt=1.0))
        self.at(self.a("a1", "Mais combien"), Ecrire(q1[2], rt=0.5))
        self.at(self.a("a2", "à quelle température"), Ecrire(q2, rt=1.0))
        items = []
        for k, (txt, col) in enumerate([(r"Réacteur isotherme : transfert thermique $Q$", BLEU), (r"Réacteur adiabatique : température finale", VERT),
                                         (r"Température de flamme", ORANGE), (r"Simulation : l'emballement thermique", ROUGE),
                                         (r"Exercice résolu : la calorimétrie", JAUNE)]):
            y = -0.5 - 0.68*k
            items.append(VGroup(carte(k+1, col, -3.6, y), pos(T(txt, sc=0.8), -3.0, y)))
        for it, (sid, fr) in zip(items, [("a4", "la chaleur échangée"), ("a4", "la température atteinte"), ("a4", "et la température de flamme"), ("a5", "une simulation"), ("a5", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a5", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"Rappel -- Coefficients stœchiométriques algébriques", "Rappel")
        fo = M(r"0", r"\;=\;", r"\sum_i \nu_i\,\mathrm{A}_i", sc=1.2).move_to([-3.2, 1.75, 0])
        self.at(self.a("b2", "zéro égale"), Ecrire(fo, rt=1.0)); self.play(Create(enc(fo, col=JAUNE)), run_time=0.4)
        p = pos(M(r"\text{produit : } \nu_i > 0", sc=0.85, color=VERT), 0.6, 2.15)
        r = pos(M(r"\text{réactif : } \nu_i < 0", sc=0.85, color=ROUGE), 0.6, 1.35)
        self.at(self.a("b2", "Les produits"), Ecrire(p, rt=0.8)); self.at(self.a("b2", "les réactifs"), Ecrire(r, rt=0.8))
        eq = M(ch("CH_4"), "+", r"2\," + ch("O_2"), r"\longrightarrow", ch("CO_2"), "+", r"2\," + ch("H_2O"), sc=1.15).move_to([0, -0.15, 0])
        self.at(self.t("b3"), Ecrire(eq, rt=1.2))
        nus = [(eq[0], r"-1", ROUGE, "moins un"), (eq[2], r"-2", ROUGE, "moins deux"), (eq[4], r"+1", VERT, "plus un"), (eq[6], r"+2", VERT, "plus deux")]
        for part, v, col, fr in nus:
            m = M(r"\nu = " + v, sc=0.75, color=col).next_to(part, DOWN, buff=0.3)
            self.at(self.a("b3", fr), FadeIn(m, shift=UP*0.15), Indicate(part, color=col, scale_factor=1.1), run_time=0.5)
        n = M(r"n_i", r"\;=\;", r"n_{i,0}", r"\;+\;", r"\nu_i\,\xi", sc=1.15).move_to([-2.0, -2.5, 0]); n[4].set_color(JAUNE)
        self.at(self.a("b4", "n i égale"), Ecrire(n, rt=1.2)); self.play(Create(enc(n, col=JAUNE)), run_time=0.4)
        d1 = pos(T(r"réactifs : $n_i$ diminue", sc=0.65, color=ROUGE), 1.9, -2.2); d2 = pos(T(r"produits : $n_i$ augmente", sc=0.65, color=VERT), 1.9, -2.8)
        self.at(self.a("b4", "Les réactifs disparaissent"), FadeIn(d1, shift=LEFT*0.2), run_time=0.4)
        self.at(self.a("b4", "les produits apparaissent"), FadeIn(d2, shift=LEFT*0.2), run_time=0.4)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"4.1 -- Vocabulaire des transformations", "1/4 · Réacteur isotherme")
        L = [("monobare", BLEU, r"$P_{\text{ext}}$ constante, et $P_I = P_F = P_{\text{ext}}$", 2.15),
             ("isotherme", ORANGE, r"$T$ constante", 0.95),
             ("adiabatique", VERT, r"aucun transfert thermique : $Q = 0$", -0.05)]
        rows = []
        for mot, col, txt, y in L:
            a = pos(T(r"\textbf{" + mot + "}", sc=0.85, color=col), -6.3, y); b = pos(T(txt, sc=0.75), -3.5, y)
            rows.append((a, b))
        self.at(self.a("c2", "monobare"), Ecrire(rows[0][0], rt=0.5)); self.at(self.a("c2", "si la pression"), Ecrire(rows[0][1], rt=1.6))
        n1 = pos(T(r"réacteur ouvert sur l'atmosphère", sc=0.6, color=GRIS), -3.5, 1.6); self.at(self.t("c3"), FadeIn(n1), run_time=0.4)
        self.at(self.a("c4", "isotherme"), Ecrire(rows[1][0], rt=0.5)); self.at(self.a("c4", "si la température"), Ecrire(rows[1][1], rt=0.6))
        n2 = pos(T(r"réacteur dans un bain thermostaté", sc=0.6, color=GRIS), -3.5, 0.4); self.at(self.a("c4", "par exemple"), FadeIn(n2), run_time=0.4)
        self.at(self.a("c5", "adiabatique"), Ecrire(rows[2][0], rt=0.5)); self.at(self.a("c5", "s'il n'y a"), Ecrire(rows[2][1], rt=1.0))
        n3 = pos(T(r"calorimètre, réaction très rapide", sc=0.6, color=GRIS), -3.5, -0.6); self.at(self.a("c5", "un calorimètre"), FadeIn(n3), run_time=0.4)
        pp = M(r"\Delta H", r"\;=\;", r"Q", sc=1.4).move_to([-2.4, -2.25, 0])
        self.at(self.a("c6", "delta H égale"), Ecrire(pp, rt=0.8)); bx = enc(pp, buff=0.25); self.play(Create(bx), run_time=0.4)
        npp = VGroup(T(r"transformation \textbf{monobare}", sc=0.65, color=JAUNE), T(r"$Q$ : transfert thermique \textbf{reçu}", sc=0.65, color=JAUNE)).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(bx, RIGHT, buff=0.6)
        self.at(self.a("c6", "le transfert"), FadeIn(npp, shift=LEFT*0.2), run_time=0.5)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"4.2 -- Variation d'enthalpie due à la réaction", "1/4 · Réacteur isotherme")
        l1 = pos(M(D + r"H", r"\;=\;", r"\Delta_r H\;" + D + r"\xi", sc=1.1), -6.0, 2.1)
        n1 = T(r"(à $T$ et $P$ fixées)", sc=0.6, color=GRIS).next_to(l1, RIGHT, buff=0.5)
        self.at(self.a("d1", "À température"), FadeIn(n1), run_time=0.4); self.at(self.a("d1", "dé H égale"), Ecrire(l1, rt=1.2))
        ap = pos(M(r"\Delta_r H", r"\;\simeq\;", r"\Delta_r H^\circ", sc=1.1, color=JAUNE), -6.0, 0.95)
        na = T(r"approximation admise au programme", sc=0.6, color=GRIS).next_to(ap, RIGHT, buff=0.5)
        self.at(self.a("d2", "une approximation"), FadeIn(na), run_time=0.4); self.at(self.a("d2", "delta-r-H est égale"), Ecrire(ap, rt=1.2))
        j1 = pos(T(r"gaz parfait : $H$ ne dépend que de $T$ (pas de $P_i$)", sc=0.7, color=BLEU), -5.6, -0.15)
        j2 = pos(T(r"liquide, solide : $H$ dépend très peu de $P$", sc=0.7, color=BLEU), -5.6, -0.8)
        self.at(self.a("d3", "l'enthalpie d'un gaz"), Ecrire(j1, rt=1.6)); self.at(self.t("d4") + 0.2, Ecrire(j2, rt=1.4))
        fi = M(r"\Delta H", r"\;=\;", r"\xi_F\,\Delta_r H^\circ(T)", sc=1.35).move_to([-1.0, -2.45, 0]); fi[2].set_color(VERT)
        self.at(self.a("d5", "delta H égale"), Ecrire(fi, rt=1.3)); self.play(Create(enc(fi, buff=0.25)), run_time=0.4)
        nf = T(r"$\xi_F$ : avancement final", sc=0.6, color=GRIS).next_to(fi, RIGHT, buff=0.7)
        self.play(FadeIn(nf), run_time=0.3)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"4.3 -- Réacteur monobare et isotherme", "1/4 · Réacteur isotherme")
        bain = Rectangle(width=4.2, height=3.6, color=BLEU, stroke_width=2.5, fill_color=BLEU, fill_opacity=0.12).move_to([3.7, 0.0, 0])
        rea = RoundedRectangle(width=1.8, height=2.0, corner_radius=0.15, color=CRAIE, stroke_width=3, fill_color=GRIS, fill_opacity=0.25).move_to([3.7, -0.1, 0])
        tb = T(r"thermostat à $T$", sc=0.55, color=BLEU).next_to(bain, UP, buff=0.12); tr = T(r"réacteur", sc=0.55).move_to(rea)
        self.at(self.t("e1") + 0.2, Create(bain), FadeIn(tb), run_time=0.6); self.play(Create(rea), FadeIn(tr), run_time=0.6)
        fo = M(r"Q", r"\;=\;", r"\Delta H", r"\;=\;", r"\xi_F\,\Delta_r H^\circ", sc=1.25).move_to([-3.3, 1.5, 0])
        self.at(self.a("e2", "Q égale"), Ecrire(VGroup(fo[0], fo[1], fo[2]), rt=0.7)); self.at(self.a("e2", "égale ksi"), Ecrire(VGroup(fo[3], fo[4]), rt=0.8))
        self.play(Create(enc(fo, buff=0.25)), run_time=0.4)
        ex = pos(T(r"exothermique : $\Delta_r H^\circ < 0 \Rightarrow Q < 0$", sc=0.72, color=ROUGE), -6.4, 0.05)
        exn = pos(T(r"le système \textbf{cède} de la chaleur", sc=0.65, color=ROUGE), -6.0, -0.5)
        out = VGroup(*[Arrow(rea.get_center() + d*1.0, rea.get_center() + d*1.6, color=ROUGE, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.35) for d in [LEFT, RIGHT, DOWN]])
        self.at(self.a("e3", "Réaction exothermique"), Ecrire(ex, rt=1.4))
        self.at(self.a("e3", "Le système cède"), FadeIn(exn), *[GrowArrow(a) for a in out], run_time=0.7)
        en = pos(T(r"endothermique : $\Delta_r H^\circ > 0 \Rightarrow Q > 0$", sc=0.72, color=BLEU), -6.4, -1.35)
        enn = pos(T(r"le système \textbf{reçoit} de la chaleur", sc=0.65, color=BLEU), -6.0, -1.9)
        inn = VGroup(*[Arrow(rea.get_center() + d*1.6, rea.get_center() + d*1.0, color=BLEU, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.35) for d in [LEFT, RIGHT, DOWN]])
        self.at(self.t("e4"), Ecrire(en, rt=1.4))
        self.at(self.a("e4", "le système reçoit"), FadeIn(enn), ReplacementTransform(out, inn), run_time=0.7)
        cs = pos(T(r"$Q$ : toujours compté du point de vue du \textbf{système}", sc=0.72, color=JAUNE), -6.4, -2.95)
        self.ecr(self.t("e5") + 0.2, cs, rt=1.5)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"4.3 -- Exemple : le chauffage au gaz", "1/4 · Réacteur isotherme")
        l1 = pos(T(r"$1\ \mathrm{m^3}$ de méthane, à $1$ bar et $298$ K", sc=0.8, color=BLEU), -6.3, 2.15)
        self.ecr(self.a("f1", "On brûle"), l1, rt=1.3)
        l2 = pos(M(r"n = \frac{PV}{RT} = \frac{10^5 \times 1}{8{,}314 \times 298}", r"\;=\; 40{,}3\ \mathrm{mol}", sc=0.8), -6.3, 1.2)
        self.at(self.a("f2", "Avec la loi"), Ecrire(l2[0], rt=1.4)); self.at(self.a("f2", "cela fait"), Ecrire(l2[1], rt=0.7))
        eq = pos(M(ch("CH_4(g)") + r" + 2\," + ch("O_2(g)") + r"\longrightarrow " + ch("CO_2(g)") + r" + 2\," + ch("H_2O(l)"), sc=0.8), -6.3, 0.15)
        hs = pos(M(r"\Delta_r H^\circ = -393{,}5 + 2(-285{,}8) + 74{,}6", r"\;=\;-890{,}5\ \mathrm{kJ\cdot mol^{-1}}", sc=0.8), -6.3, -0.65); hs[1].set_color(ROUGE)
        self.at(self.a("f3", "La loi de Hess"), Ecrire(eq, rt=1.3)); self.at(self.a("f3", "avec de l'eau"), Ecrire(hs[0], rt=1.4))
        self.at(self.a("f3", "moins huit cent"), Ecrire(hs[1], rt=0.8))
        xf = pos(M(r"\text{combustion totale : } \xi_F = 40{,}3\ \mathrm{mol}", sc=0.8), -6.3, -1.5)
        self.ecr(self.t("f4") + 0.1, xf, rt=1.2)
        q = M(r"Q = \xi_F\,\Delta_r H^\circ", r"\;=\; -35{,}9\ \mathrm{MJ}", r"\;\approx\; -10\ \mathrm{kWh}", sc=1.0).move_to([-1.3, -2.5, 0]); q[1].set_color(ROUGE); q[2].set_color(ROUGE)
        self.at(self.a("f5", "Q égale"), Ecrire(VGroup(q[0], q[1]), rt=1.2)); self.at(self.a("f5", "environ dix"), Ecrire(q[2], rt=0.6))
        self.play(Create(enc(q, buff=0.2)), run_time=0.4)
        fac = T(r"facture de gaz : $\approx 10$ kWh par m$^3$", sc=0.65, color=VERT).move_to([0, -3.4, 0])
        self.ecr(self.a("f6", "ce que facturent"), fac, rt=1.3)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"4.4 -- Réacteur adiabatique : chemin fictif", "2/4 · Réacteur adiabatique")
        l1 = pos(M(r"Q = 0", r"\;\Longrightarrow\;", r"\Delta H = 0", sc=1.0), -6.3, 2.15)
        self.at(self.a("g1", "Aucun échange"), Ecrire(l1[0], rt=0.5)); self.at(self.a("g1", "donc delta H"), Ecrire(VGroup(l1[1], l1[2]), rt=0.7))
        l2 = pos(T(r"l'énergie libérée \textbf{chauffe} le contenu", sc=0.65, color=ORANGE), -6.3, 1.5)
        self.ecr(self.a("g2", "elle chauffe"), l2, rt=1.0)
        I = boite(T(r"\textbf{état initial}\\réactifs, $T_I$", sc=0.6), BLEU, BLEU, w=3.0, h=1.05).move_to([-4.6, -1.0, 0])
        A = boite(T(r"\textbf{intermédiaire}\\système final, $T_I$", sc=0.6), BLEU, BLEU, w=3.0, h=1.05).move_to([1.4, -1.0, 0])
        F = boite(T(r"\textbf{état final}\\système final, $T_F$", sc=0.6), ROUGE, ROUGE, w=3.0, h=1.05).move_to([1.4, 1.75, 0])
        reel = DashedLine(I.get_top() + UP*0.08, F.get_left() + LEFT*0.08, color=GRIS, stroke_width=3).add_tip(tip_length=0.2)
        tre = T(r"réel : $\Delta H = 0$", sc=0.55, color=GRIS).move_to([-3.4, 0.75, 0])
        self.at(self.a("g3", "on imagine un chemin"), FadeIn(I), FadeIn(F), run_time=0.6); self.play(Create(reel), FadeIn(tre), run_time=0.7)
        fl1 = Arrow(I.get_right(), A.get_left(), color=CRAIE, stroke_width=4, buff=0.1, max_tip_length_to_length_ratio=0.08)
        e1 = T(r"(1) réaction à $T_I$", sc=0.55).next_to(fl1, UP, buff=0.1)
        h1 = M(r"\Delta H_1 = \xi_F\,\Delta_r H^\circ(T_I)", sc=0.62, color=VERT).move_to([-1.6, -1.9, 0])
        self.at(self.t("g4"), GrowArrow(fl1), FadeIn(e1), run_time=0.6); self.play(FadeIn(A), run_time=0.4)
        self.at(self.a("g4", "Sa variation"), Ecrire(h1, rt=1.2))
        fl2 = Arrow(A.get_top(), F.get_bottom(), color=CRAIE, stroke_width=4, buff=0.1, max_tip_length_to_length_ratio=0.12)
        e2 = pos(T(r"(2) échauffement", sc=0.55), 3.15, 0.55)
        h2 = pos(M(r"\Delta H_2 = \Big(\sum_j n_j\,C^\circ_{p,j}\Big)(T_F - T_I)", sc=0.6, color=VERT), 3.15, 0.05)
        self.at(self.a("g5", "on chauffe"), GrowArrow(fl2), FadeIn(e2), run_time=0.6)
        self.at(self.a("g6", "la somme"), Ecrire(h2, rt=1.5))
        bil = M(r"\Delta H_1 + \Delta H_2 = 0", r"\;\Longrightarrow\;", r"T_F = T_I - \frac{\xi_F\,\Delta_r H^\circ(T_I)}{\sum_j n_j\,C^\circ_{p,j}}", sc=0.85).move_to([0, -2.95, 0])
        self.at(self.t("g7"), Ecrire(bil[0], rt=0.8)); self.at(self.a("g7", "on en tire"), Ecrire(VGroup(bil[1], bil[2]), rt=1.3))
        self.play(Create(enc(bil[2], buff=0.15)), run_time=0.4)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"4.4 -- La méthode", "2/4 · Réacteur adiabatique")
        data = [(BLEU, r"Tableau d'avancement : $\xi_F$", "h2", "le tableau", 1.95),
                (ROUGE, r"Inventaire \textbf{complet} de l'état final : produits, réactifs en excès, \textbf{spectateurs}", "h3", "l'inventaire", 0.85),
                (VERT, r"$\Delta H_1 + \Delta H_2 = 0$ le long du chemin fictif", "h4", "la variation", -0.25),
                (ORANGE, r"Vérifier : $T_F > T_I$ pour une réaction exothermique", "h5", "Pour une réaction", -1.35)]
        for k, (col, txt, sid, fr, y) in enumerate(data):
            c = carte(k+1, col, -5.9, y); L = pos(T(txt, sc=0.72), -5.35, y)
            self.at(self.t(sid), Create(c[0]), FadeIn(c[1]), run_time=0.4); self.at(self.a(sid, fr), Ecrire(L, rt=1.4))
        ce = pos(T(r"Changement d'état pendant l'échauffement : on ajoute $n\,\Delta_{\text{vap}}H^\circ$ (ou $\Delta_{\text{fus}}H^\circ$)", sc=0.68, color=JAUNE), -6.3, -2.65)
        self.ecr(self.a("h6", "si un constituant"), ce, rt=1.8)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"4.4 -- Température de flamme", "3/4 · Température de flamme")
        df = pos(T(r"\textbf{Température de flamme} : combustion totale, adiabatique et monobare", sc=0.72, color=BLEU), -6.4, 2.2)
        self.ecr(self.a("i1", "C'est la température"), df, rt=1.8)
        air = pos(T(r"air : $\approx 4\ \mathrm{N_2}$ pour $1\ \mathrm{O_2}$", sc=0.6, color=GRIS), 1.6, 0.85)
        self.at(self.a("i2", "L'air apporte"), FadeIn(air), run_time=0.4)
        eq = pos(M(ch("CH_4") + r" + 2\," + ch("O_2"), r" + 8\," + ch("N_2"), r"\;\longrightarrow\;", ch("CO_2") + r" + 2\," + ch("H_2O(g)"), r" + 8\," + ch("N_2"), sc=0.85), -6.3, 1.5)
        eq[1].set_color(GRIS); eq[4].set_color(GRIS)
        self.at(self.a("i3", "On part donc"), Ecrire(VGroup(eq[0], eq[1]), rt=1.2))
        self.at(self.a("i4", "on forme directement"), Ecrire(VGroup(eq[2], eq[3], eq[4]), rt=1.2))
        h = pos(M(r"\Delta_r H^\circ = -802{,}5\ \mathrm{kJ\cdot mol^{-1}}", sc=0.78, color=ROUGE), -6.3, 0.65)
        self.ecr(self.a("i4", "L'enthalpie standard"), h, rt=1.0)
        c = pos(M(r"\sum_j n_j C^\circ_{p,j} = 37{,}1 + 2 \times 33{,}6", r"\;+\; 8 \times 29{,}1", r"\;=\; 337\ \mathrm{J\cdot K^{-1}}", sc=0.78), -6.3, -0.2)
        c[1].set_color(GRIS)
        self.at(self.a("i5", "La capacité"), Ecrire(VGroup(c[0], c[2]), rt=1.6))
        nn = T(r"diazote : $233$", sc=0.55, color=GRIS).next_to(c[1], DOWN, buff=0.12)
        self.at(self.a("i5", "dont deux cent"), Ecrire(c[1], rt=0.6), FadeIn(nn))
        tf = M(r"T_F = 298 + \frac{802{,}5 \times 10^3}{337}", r"\;\approx\; 2\,700\ \mathrm{K}", sc=0.9).move_to([-2.6, -1.55, 0]); tf[1].set_color(JAUNE)
        self.at(self.t("i6"), Ecrire(tf[0], rt=1.0)); self.at(self.a("i6", "environ"), Ecrire(tf[1], rt=0.6))
        self.play(Create(enc(tf, buff=0.18)), run_time=0.4)
        me = pos(T(r"mesurée : $\approx 2\,200$ K \;($C_p$ croissants, dissociation)", sc=0.65, color=ORANGE), -6.3, -2.6)
        self.ecr(self.a("i7", "on mesure plutôt"), me, rt=1.6)
        x0, w = -4.0, 8.0
        b1 = Rectangle(width=w*0.69, height=0.4, color=GRIS, fill_color=GRIS, fill_opacity=0.7, stroke_width=1.5).move_to([x0 + w*0.69/2, -3.4, 0])
        b2 = Rectangle(width=w*0.31, height=0.4, color=ROUGE, fill_color=ROUGE, fill_opacity=0.6, stroke_width=1.5).move_to([x0 + w*0.69 + w*0.31/2, -3.4, 0])
        t1 = T(r"$\mathrm{N_2}$ : $\approx 70\,\%$ de l'énergie", sc=0.55).move_to(b1); t2 = T(r"$\mathrm{CO_2}$, $\mathrm{H_2O}$", sc=0.5).move_to(b2)
        self.at(self.a("i8", "il absorbe"), GrowFromEdge(b1, LEFT), FadeIn(t1), run_time=0.7); self.play(GrowFromEdge(b2, LEFT), FadeIn(t2), run_time=0.4)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"4.4 -- À vous : flamme dans le dioxygène pur", "3/4 · Température de flamme")
        cad = RoundedRectangle(width=12.4, height=1.4, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, 1.6, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.72, color=JAUNE), -5.9, 1.6)
        eq = M(ch("CH_4") + r" + 2\," + ch("O_2") + r"\ (\text{pur})", r"\;\longrightarrow\;", ch("CO_2") + r" + 2\," + ch("H_2O(g)"), sc=0.85).next_to(tq, RIGHT, buff=0.4)
        qq = M(r"T_F", r"\;?", sc=0.9).next_to(eq, RIGHT, buff=0.5); qq[1].set_color(JAUNE)
        self.at(self.t("j1"), Create(cad), Ecrire(tq, rt=0.4), run_time=0.5)
        self.at(self.a("j1", "Même combustion"), Ecrire(eq, rt=1.4)); self.at(self.a("j1", "Estimez"), Ecrire(qq, rt=0.5))
        pa, arc = chrono(5.7, 1.6)
        self.jusqua(self.PH["j1"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("j2") - self.renderer.time - 0.1), rate_func=linear)
        c = pos(M(r"\sum_j n_j C^\circ_{p,j} = 37{,}1 + 2 \times 33{,}6 = 104\ \mathrm{J\cdot K^{-1}}", sc=0.8), -6.0, 0.15)
        self.at(self.a("j2", "sans le diazote"), FadeOut(pa), FadeOut(arc), Ecrire(c, rt=1.5))
        tf = pos(M(r"T_F = 298 + \frac{802{,}5 \times 10^3}{104}", r"\;\approx\; 8\,000\ \mathrm{K}", sc=0.9), -6.0, -1.0); tf[1].set_color(JAUNE)
        self.at(self.a("j2", "Le calcul"), Ecrire(tf[0], rt=0.9), Ecrire(tf[1], rt=0.9))
        i1 = pos(T(r"irréaliste : les produits se \textbf{dissocient}", sc=0.72, color=ORANGE), -6.0, -2.2)
        i2 = pos(T(r"mais flamme bien plus chaude : le \textbf{chalumeau}", sc=0.72, color=VERT), -6.0, -2.95)
        self.ecr(self.a("j3", "c'est irréaliste"), i1, rt=1.3); self.ecr(self.a("j3", "Mais la flamme"), i2, rt=1.3)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"4.5 -- Simulation : l'emballement thermique", "4/4 · Emballement thermique")
        ar = pos(M(r"\text{Arrhenius : } k(T) = A\,e^{-E_a/RT}", sc=0.8, color=BLEU), -6.4, 2.1)
        self.ecr(self.a("k2", "La vitesse"), ar, rt=1.3)
        bou = pos(T(r"réaction $\to$ $T$ monte $\to$ $k$ monte $\to$ plus rapide", sc=0.62, color=ORANGE), -6.4, 1.3)
        self.ecr(self.a("k3", "une réaction exothermique"), bou, rt=1.8)
        e1 = pos(M(r"\frac{" + D + r"\xi}{" + D + r"t} = k(T)\,(n_0 - \xi)", sc=0.72), -6.4, 0.3)
        e2 = pos(M(r"C\,\frac{" + D + r"T}{" + D + r"t} = -\Delta_r H^\circ\,\frac{" + D + r"\xi}{" + D + r"t}", sc=0.72), -6.4, -0.65)
        ne = pos(T(r"méthode d'Euler", sc=0.55, color=GRIS), -6.4, -1.35)
        self.at(self.a("k4", "la méthode"), Ecrire(e1, rt=1.1), FadeIn(ne)); self.at(self.a("k4", "on fait le bilan"), Ecrire(e2, rt=1.3))
        dat = np.loadtxt("../pdf/data/adiab.dat", skiprows=1)
        ax = Axes(x_range=[0, 62, 10], y_range=[20, 72, 10], x_length=5.6, y_length=3.9,
                  axis_config={"color": CRAIE, "stroke_width": 2, "include_ticks": False, "tip_width": 0.18, "tip_height": 0.18}).move_to([3.55, -0.35, 0])
        lx = M(r"t\ (\mathrm{min})", sc=0.55).next_to(ax.x_axis.get_end(), DOWN, buff=0.12)
        ly = M(r"T\ (^\circ\mathrm{C})", sc=0.55).next_to(ax.y_axis.get_end(), RIGHT, buff=0.12)
        pts = [ax.c2p(t, T) for t, T in dat[::3, :2] if t <= 60]
        cb = VMobject(color=ROUGE, stroke_width=4).set_points_smoothly(pts)
        self.at(self.t("k5"), Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.5)
        self.at(self.a("k5", "une courbe en S"), Create(cb), run_time=0.9)
        hl = DashedLine(ax.c2p(0, 65), ax.c2p(60, 65), color=JAUNE, stroke_width=2.5)
        th = M(r"T_I + 40\ \mathrm{K}", sc=0.55, color=JAUNE).move_to(ax.c2p(48, 65)).shift(UP*0.25)
        b0 = M(r"25\,^\circ\mathrm{C}", sc=0.5, color=GRIS).next_to(ax.c2p(0, 25), LEFT, buff=0.1)
        self.at(self.a("k5", "et monte"), Create(hl), FadeIn(th), FadeIn(b0), run_time=0.6)
        v = pos(T(r"vitesse $\times 45$ : fin $\approx 3$ fois plus tôt", sc=0.65, color=VERT), -6.4, -2.2)
        self.ecr(self.a("k6", "la vitesse"), v, rt=1.4)
        em = T(r"\textbf{emballement thermique}", sc=0.85, color=ROUGE).move_to([0, -3.2, 0])
        self.ecr(self.a("k7", "l'emballement"), em, rt=1.0); self.play(Create(enc(em, buff=0.15)), run_time=0.4)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, M(r"\text{Isotherme : } Q = \Delta H = \xi_F\,\Delta_r H^\circ \qquad (Q < 0 \text{ si exothermique})", sc=0.8), "l2", 1.9),
                (VERT, M(r"\text{Adiabatique : } \xi_F\,\Delta_r H^\circ(T_I) + \Big(\sum_j n_j\,C^\circ_{p,j}\Big)(T_F - T_I) = 0", sc=0.8), "l3", 0.55),
                (ORANGE, T(r"Inventaire de l'état final : \textbf{toutes} les espèces, spectateurs compris", sc=0.75), "l4", -0.8)]
        for k, (col, F, sid, y) in enumerate(data):
            c = carte(k+1, col, -5.9, y); pos(F, -5.3, y)
            self.at(self.t(sid), Create(c[0]), FadeIn(c[1]), run_time=0.4); self.play(Ecrire(F, rt=1.8))
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- Mesure d'une enthalpie de réaction", "Exercice résolu")
        cal = VGroup(Rectangle(width=2.5, height=2.9, color=CRAIE, stroke_width=3), Rectangle(width=2.1, height=2.5, color=GRIS, stroke_width=2))
        liq = Rectangle(width=2.1, height=1.5, stroke_width=0, fill_color=BLEU, fill_opacity=0.3)
        cal.move_to([4.3, 0.2, 0]); liq.align_to(cal[1], DOWN).align_to(cal[1], LEFT)
        th = Line([4.75, 2.0, 0], [4.75, -0.6, 0], color=ROUGE, stroke_width=5)
        tc = T(r"calorimètre", sc=0.55, color=GRIS).next_to(cal, DOWN, buff=0.15)
        self.at(self.a("m2", "Dans un calorimètre"), Create(cal), run_time=0.6); self.play(FadeIn(liq), Create(th), FadeIn(tc), run_time=0.5)
        e1 = pos(T(r"$100$ mL d'acide chlorhydrique à $1{,}00$ mol$\cdot$L$^{-1}$", sc=0.72), -6.4, 2.1)
        e2 = pos(T(r"$+\ 100$ mL de soude à $1{,}00$ mol$\cdot$L$^{-1}$", sc=0.72), -6.4, 1.5)
        self.at(self.a("m2", "on mélange"), Ecrire(e1, rt=1.2)); self.at(self.a("m2", "cent millilitres de soude"), Ecrire(e2, rt=1.1))
        e3 = pos(M(r"T_I = 20{,}0\ ^\circ\mathrm{C}", r"\;\longrightarrow\;", r"T_F = 25{,}8\ ^\circ\mathrm{C}", sc=0.85), -6.4, 0.7); e3[2].set_color(ROUGE)
        self.at(self.a("m3", "Les deux solutions"), Ecrire(e3[0], rt=0.7)); self.at(self.a("m3", "le thermomètre"), Ecrire(VGroup(e3[1], e3[2]), rt=0.8))
        e4 = pos(M(r"C_{\text{cal}} = 120\ \mathrm{J\cdot K^{-1}}", sc=0.85), -6.4, -0.1)
        self.ecr(self.a("m4", "La capacité"), e4, rt=0.9)
        q = M(r"\Delta_r H^\circ", r"\;=\;", r"?", sc=1.3).move_to([-3.5, -1.3, 0]); q[2].set_color(JAUNE)
        self.at(self.a("m4", "Question"), Ecrire(q, rt=0.8)); self.play(Create(enc(q, col=JAUNE)), run_time=0.4)
        r1 = pos(T(r"calorimètre isolé \;$\Rightarrow$\; réacteur \textbf{adiabatique}", sc=0.72, color=VERT), -6.4, -2.55)
        r2 = pos(T(r"$\Rightarrow$ la méthode du \textbf{chemin fictif}", sc=0.72, color=VERT), -6.4, -3.2)
        self.ecr(self.a("m5", "Un calorimètre"), r1, rt=1.4); self.ecr(self.a("m5", "vous savez faire"), r2, rt=1.0)
        self.fin()

class S13(Cours):
    sid = "S13"
    def construct(self):
        self.entete(r"Exercice résolu -- La solution, étape par étape", "Exercice résolu")
        c1 = carte(1, BLEU, -6.1, 2.15)
        s1 = pos(M(ch("H^+") + " + " + ch("HO^-") + r"\longrightarrow " + ch("H_2O"), r"\qquad K^\circ = 10^{14}", sc=0.78), -5.55, 2.15)
        s1b = pos(M(r"\text{totale :}\quad \xi_F = 0{,}100\ \mathrm{mol}", sc=0.78, color=BLEU), 1.4, 2.15)
        self.at(self.t("n1"), Create(c1[0]), FadeIn(c1[1]), run_time=0.4); self.at(self.a("n1", "Les ions"), Ecrire(s1[0], rt=1.0))
        self.at(self.a("n1", "avec une constante"), Ecrire(s1[1], rt=0.7)); self.at(self.a("n2", "Elle est donc totale"), Ecrire(s1b, rt=1.2))
        c2 = carte(2, ORANGE, -6.1, 1.15)
        s2 = pos(M(r"\underbrace{200 \times 4{,}18}_{\text{solution}} = 836", r"\;+\; \underbrace{120}_{\text{calorimètre}}", r"\;=\; 956\ \mathrm{J\cdot K^{-1}}", sc=0.72), -5.55, 0.95)
        s2b = pos(M(r"\Delta T = 5{,}8\ \mathrm{K}", sc=0.78, color=ORANGE), 2.6, 1.15)
        self.at(self.t("n3"), Create(c2[0]), FadeIn(c2[1]), run_time=0.4)
        self.at(self.a("n4", "deux cents grammes"), Ecrire(s2[0], rt=1.4)); self.at(self.a("n4", "n'oubliez pas"), Ecrire(s2[1], rt=0.9), Indicate(c2, color=ROUGE))
        self.at(self.a("n5", "Au total"), Ecrire(s2[2], rt=0.8)); self.at(self.a("n5", "à chauffer"), Ecrire(s2b, rt=0.7))
        c3 = carte(3, VERT, -6.1, -0.35)
        s3 = pos(M(r"\xi_F\,\Delta_r H^\circ", r"\;+\; 956 \times 5{,}8", r"\;=\; 0", sc=0.85), -5.55, -0.35)
        self.at(self.t("n6"), Create(c3[0]), FadeIn(c3[1]), run_time=0.4)
        self.at(self.a("n6", "Ksi final"), Ecrire(s3[0], rt=0.7)); self.at(self.a("n6", "plus neuf cent"), Ecrire(s3[1], rt=0.8)); self.at(self.a("n6", "égale zéro"), Ecrire(s3[2], rt=0.4))
        res = M(r"\Delta_r H^\circ = -\frac{956 \times 5{,}8}{0{,}100}", r"\;=\; -55{,}4\ \mathrm{kJ\cdot mol^{-1}}", sc=0.8); pos(res, -5.4, -1.25); res[1].set_color(JAUNE)
        self.at(self.a("n7", "On isole"), Ecrire(res[0], rt=0.9)); self.at(self.a("n7", "on trouve"), Ecrire(res[1], rt=0.8))
        self.play(Create(enc(res, col=JAUNE, buff=0.15)), run_time=0.4)
        c4 = carte(4, ROUGE, -6.1, -2.45)
        s4 = pos(T(r"Vérifier : $\Delta_r H^\circ < 0$, exothermique, et $T$ monte \;\checkmark", sc=0.72), -5.55, -2.45)
        self.at(self.t("n8"), Create(c4[0]), FadeIn(c4[1]), run_time=0.4); self.at(self.a("n8", "Le signe"), Ecrire(s4, rt=1.6))
        tb = pos(M(r"\text{tables : } -55{,}8\ \mathrm{kJ\cdot mol^{-1}}", r"\quad(\text{écart} < 1\,\%)", sc=0.75, color=VERT), -5.55, -3.1)
        self.at(self.a("n9", "Et les tables"), Ecrire(tb[0], rt=1.0)); self.at(self.a("n9", "Moins d'un pour cent"), Ecrire(tb[1], rt=0.7))
        ec = pos(T(r"pertes thermiques ; solution $\neq$ eau pure", sc=0.6, color=GRIS), -5.55, -3.62)
        self.at(self.a("n10", "des pertes"), FadeIn(ec), run_time=0.5)
        self.jusqua(self.t("n11") - 0.2)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        nx = T(r"Chapitre 5 \;$\longrightarrow$\; deuxième principe : évolution et équilibre", sc=0.85, color=JAUNE).move_to([0, 0.3, 0])
        self.ecr(self.a("n11", "le deuxième principe"), nx, rt=1.8)
        self.fin()
