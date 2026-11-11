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
DNU = r"\Delta\nu_{\text{gaz}}"
VH = r"\frac{" + D + r"\ln K^\circ}{" + D + r"T} = \frac{\Delta_r H^\circ}{RT^2}"

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"THERMOCHIMIE \;·\; PT*", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Chapitre 6}", sc=1.3, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Influence des paramètres et optimisation", sc=0.95).move_to([0, 1.75, 0])
        tr = Line([-4.4, 1.3, 0], [4.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=0.9), Create(tr), run_time=1.0)
        q = M(ch("N_2 + 3\\,H_2 = 2\\,NH_3"), r"\qquad K^\circ(450\,^\circ\mathrm{C}) = 1{,}9\times10^{-4}", sc=0.85).move_to([0, 0.75, 0]); q[1].set_color(ROUGE)
        self.at(self.a("a1", "L'ammoniac"), Ecrire(q[0], rt=0.9))
        self.at(self.a("a1", "sa constante d'équilibre"), Ecrire(q[1], rt=1.0))
        l1 = T(r"levier 1 : $K^\circ$ \;$\longleftarrow$\; $T$", sc=0.7, color=BLEU).move_to([-3.0, 0.05, 0])
        l2 = T(r"levier 2 : $Q_r$ \;$\longleftarrow$\; $P$, composition", sc=0.7, color=VERT).move_to([2.6, 0.05, 0])
        self.ecr(self.a("a3", "Soit on modifie K standard"), l1, rt=0.8); self.ecr(self.a("a3", "Soit on modifie Q r"), l2, rt=0.9)
        items = []
        for k, (txt, col) in enumerate([(r"Relation de Van 't Hoff", BLEU), ("Choix de la température", VERT), ("Pression et composition", ORANGE),
                                         ("Le procédé Haber--Bosch", ROUGE), (r"Exercice résolu : le dioxyde d'azote", JAUNE)]):
            y = -0.8 - 0.62*k
            items.append(VGroup(carte(k+1, col, -3.6, y), pos(T(txt, sc=0.78), -3.0, y)))
        for it, (sid, fr) in zip(items, [("a4", "la relation de Vant Off"), ("a4", "le choix de la température"), ("a4", "l'effet de la pression"),
                                         ("a4", "puis le procédé"), ("a5", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a5", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"6.1 -- Relation de Van 't Hoff", "1/4 · Température")
        q = pos(T(r"Comment $K^\circ$ dépend-il de $T$ ?", sc=0.8, color=BLEU), -6.3, 2.1)
        self.ecr(self.a("b1", "Comment K standard"), q, rt=0.9)
        nm = T(r"Relation de Van 't Hoff", sc=0.7, color=JAUNE).move_to([0, 1.62, 0])
        vh = M(r"\frac{" + D + r"\ln K^\circ}{" + D + r"T}", r"\;=\;", r"\frac{\Delta_r H^\circ}{RT^2}", sc=1.3).move_to([0, 0.12, 0])
        self.ecr(self.a("b2", "la relation de Vant Off"), nm, rt=0.6)
        self.at(self.a("b2", "La dérivée"), Ecrire(VGroup(vh[0], vh[1]), rt=1.0)); self.at(self.a("b2", "égale delta-r-H"), Ecrire(vh[2], rt=1.0))
        self.play(Create(enc(vh, col=JAUNE, buff=0.25)), run_time=0.4)
        self.at(self.a("b3", "c'est le signe"), Indicate(vh[2], color=JAUNE, scale_factor=1.2), run_time=0.8)
        R = [(r"\Delta_r H^\circ > 0", r"endothermique : $K^\circ$ \textbf{augmente} avec $T$", ROUGE, "b3", "Réaction endothermique", -1.25),
             (r"\Delta_r H^\circ < 0", r"exothermique : $K^\circ$ \textbf{diminue} quand $T$ augmente", BLEU, "b4", "Réaction exothermique", -2.1),
             (r"\Delta_r H^\circ \approx 0", r"athermique : $K^\circ$ quasi indépendante de $T$", VERT, "b5", "Et si la réaction", -2.95)]
        for fo, tx, col, sid, fr, y in R:
            a = pos(M(fo, sc=0.85, color=col), -5.6, y); b = pos(T(tx, sc=0.72, color=col), -2.4, y)
            self.at(self.a(sid, fr), Ecrire(a, rt=0.7)); self.play(Ecrire(b, rt=0.9))
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"6.1 -- Démonstration", "1/4 · Température")
        el = pos(T(r"Approximation d'Ellingham : $\Delta_r H^\circ$ et $\Delta_r S^\circ$ indépendantes de $T$", sc=0.68, color=GRIS), -6.3, 2.1)
        self.ecr(self.a("c1", "dans l'approximation"), el, rt=1.4)
        l1 = pos(M(r"\ln K^\circ", r"\;=\; -\frac{\Delta_r G^\circ}{RT}", r"\;=\; -\frac{\Delta_r H^\circ - T\,\Delta_r S^\circ}{RT}", sc=1.0), -6.3, 0.95)
        self.at(self.a("c2", "On part de"), Ecrire(VGroup(l1[0], l1[1]), rt=1.1)); self.at(self.a("c2", "Et on remplace"), Ecrire(l1[2], rt=1.3))
        l2 = pos(M(r"\ln K^\circ", r"\;=\;", r"-\frac{\Delta_r H^\circ}{RT}", r"\;+\;", r"\frac{\Delta_r S^\circ}{R}", sc=1.0), -6.3, -0.45)
        self.at(self.a("c3", "Il vient"), Ecrire(l2, rt=1.3))
        br = Brace(l2[4], DOWN, color=VERT); tb = T(r"constante", sc=0.6, color=VERT).next_to(br, DOWN, buff=0.08)
        self.at(self.a("c3", "Le second terme"), Create(br), FadeIn(tb), run_time=0.5)
        fi = M(VH, sc=1.1, color=JAUNE).move_to([2.6, -2.2, 0])
        ar = Arrow(l2.get_right() + RIGHT*0.15 + DOWN*0.2, fi.get_left() + LEFT*0.1 + UP*0.15, color=JAUNE, buff=0.05, stroke_width=3)
        self.at(self.a("c3", "on dérive le premier"), GrowArrow(ar), run_time=0.4); self.play(Ecrire(fi, rt=0.9))
        self.at(self.a("c3", "et voilà"), Create(enc(fi, col=JAUNE)), run_time=0.4)
        hp = pos(T(r"\textit{Hors programme} : vraie même si $\Delta_r H^\circ$ dépend de $T$ (Gibbs--Helmholtz)", sc=0.6, color=GRIS), -6.3, -3.4)
        self.ecr(self.a("c4", "Bonus"), hp, rt=1.3)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"6.1 -- Forme intégrée : la droite de Van 't Hoff", "1/4 · Température")
        fi = pos(M(r"\ln\frac{K^\circ(T_2)}{K^\circ(T_1)}", r"\;=\; -\frac{\Delta_r H^\circ}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right)", sc=0.85), -6.4, 1.95)
        hy = pos(T(r"($\Delta_r H^\circ$ constante)", sc=0.6, color=GRIS), 1.6, 1.95)
        self.at(self.a("d1", "avec delta-r-H"), FadeIn(hy), run_time=0.4)
        self.at(self.a("d2", "Le logarithme"), Ecrire(fi[0], rt=0.8)); self.at(self.a("d2", "égale moins"), Ecrire(fi[1], rt=1.4))
        self.play(Create(enc(fi, col=JAUNE)), run_time=0.4)
        af = pos(T(r"$\ln K^\circ$ : fonction \textbf{affine} de $1/T$", sc=0.72), -6.4, 0.65)
        self.ecr(self.a("d3", "Autrement dit"), af, rt=1.1)
        dat = np.loadtxt("../pdf/data/nh3_vh.dat", skiprows=1)
        ax = Axes(x_range=[1.0, 2.6, 0.5], y_range=[-12, 4.5, 4], x_length=5.8, y_length=4.0, axis_config={"stroke_opacity": 0}).move_to([3.3, -1.35, 0])
        o = ax.c2p(1.0, -12)
        axx = Arrow(o, ax.c2p(2.68, -12), color=CRAIE, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.04)
        axy = Arrow(o, ax.c2p(1.0, 4.9), color=CRAIE, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.05)
        lx = M(r"1000/T\ (\mathrm{K^{-1}})", sc=0.5).next_to(ax.c2p(2.68, -12), UP, buff=0.15).align_to(ax.c2p(2.68, -12), RIGHT)
        ly = M(r"\ln K^\circ", sc=0.6).next_to(ax.c2p(1.0, 4.9), RIGHT, buff=0.12)
        tx = VGroup(*[M(f"{v:.1f}".replace(".", "{,}"), sc=0.45, color=GRIS).next_to(ax.c2p(v, -12), DOWN, buff=0.1) for v in (1.0, 1.5, 2.0, 2.5)])
        ty = VGroup(*[M(s, sc=0.45, color=GRIS).next_to(ax.c2p(1.0, v), LEFT, buff=0.1) for s, v in (("0", 0), ("-10", -10))])
        z0 = DashedLine(ax.c2p(1.0, 0), ax.c2p(2.6, 0), color=GRIS, stroke_width=1.5, stroke_opacity=0.6)
        pts = VGroup(*[Dot(ax.c2p(x, y), radius=0.07, color=BLEU) for x, y in dat])
        dr = Line(ax.c2p(1.05, -12.0 + 0.0), ax.c2p(2.55, 4.5), color=BLEU, stroke_width=3)
        a_, b_ = np.polyfit(dat[:, 0], dat[:, 1], 1)
        dr = Line(ax.c2p(1.08, a_*1.08 + b_), ax.c2p(2.55, a_*2.55 + b_), color=BLEU, stroke_width=3)
        lg = VGroup(M(ch("N_2 + 3\\,H_2 = 2\\,NH_3"), sc=0.55, color=GRIS), T(r"de $400$ à $900$ K", sc=0.5, color=GRIS)).arrange(DOWN, aligned_edge=RIGHT, buff=0.08)
        lg.move_to(ax.c2p(2.6, -8.4), aligned_edge=RIGHT)
        self.at(self.a("d3", "Traçons-la"), Create(axx), Create(axy), FadeIn(lx), FadeIn(ly), FadeIn(tx), FadeIn(ty), FadeIn(z0), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(p, scale=1.8) for p in pts], lag_ratio=0.12), FadeIn(lg), run_time=1.0)
        self.at(self.a("d4", "Une belle droite"), Create(dr), run_time=0.7)
        p1, p2, p3 = ax.c2p(1.6, a_*1.6 + b_), ax.c2p(2.0, a_*1.6 + b_), ax.c2p(2.0, a_*2.0 + b_)
        tri = VMobject(color=ORANGE, stroke_width=3).set_points_as_corners([p1, p2, p3])
        pe = pos(M(r"\text{pente} = -\frac{\Delta_r H^\circ}{R} = +1{,}10\times10^{4}\ \mathrm{K}", sc=0.72, color=ORANGE), -6.4, -0.35)
        self.at(self.a("d4", "Sa pente"), Create(tri), run_time=0.5); self.play(Ecrire(pe, rt=1.3))
        lo = pos(M(r"T\nearrow \;\Rightarrow\; \tfrac{1}{T}\searrow \;\Rightarrow\; K^\circ\searrow", sc=0.8, color=BLEU), -6.4, -1.4)
        lo2 = pos(T(r"logique : synthèse exothermique", sc=0.6, color=GRIS), -6.4, -1.95)
        self.ecr(self.a("d5", "quand T augmente"), lo, rt=1.1); self.ecr(self.a("d5", "Logique"), lo2, rt=0.8)
        m1 = pos(T(r"\textbf{Mesure} : $K^\circ$ à plusieurs $T$, régression", sc=0.64, color=VERT), -6.4, -2.75)
        m2 = pos(T(r"pente $\Rightarrow \Delta_r H^\circ$, \;ordonnée $\Rightarrow \Delta_r S^\circ$", sc=0.64, color=VERT), -6.4, -3.3)
        self.ecr(self.a("d6", "on mesure K standard"), m1, rt=1.1); self.ecr(self.a("d6", "et la pente donne"), m2, rt=1.0)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"6.1 -- Calculer $K^\circ$ à une autre température", "1/4 · Température")
        v1 = pos(T(r"\textbf{Voie 1} : les tables", sc=0.75, color=BLEU), -6.3, 2.1)
        v1f = pos(M(r"\Delta_r G^\circ(T) = \Delta_r H^\circ - T\,\Delta_r S^\circ \;\Rightarrow\; K^\circ = \exp\!\left(-\frac{\Delta_r G^\circ}{RT}\right)", sc=0.75), -6.3, 1.4)
        self.ecr(self.a("e2", "Voie un"), v1, rt=0.7); self.ecr(self.a("e2", "On calcule"), v1f, rt=1.6)
        v2 = pos(T(r"\textbf{Voie 2} : une valeur connue + Van 't Hoff intégrée", sc=0.75, color=VERT), -6.3, 0.55)
        self.ecr(self.a("e3", "Voie deux"), v2, rt=1.2)
        ex = pos(T(r"Ammoniac à $450\,^\circ$C ($723$ K) :", sc=0.72, color=ORANGE), -6.3, -0.3)
        self.ecr(self.a("e4", "Testons"), ex, rt=0.9)
        l1 = pos(M(r"\text{voie 1 : }\; \Delta_r G^\circ(723) = -91{,}8 + 723\times0{,}1981 = +51{,}4\ \mathrm{kJ\cdot mol^{-1}}", r"\;\Rightarrow\; K^\circ = 1{,}9\times10^{-4}", sc=0.68), -6.3, -0.95)
        l1[1].set_color(JAUNE)
        self.at(self.a("e4", "Par les tables"), Ecrire(l1[0], rt=1.5)); self.at(self.a("e4", "donc K standard"), Ecrire(l1[1], rt=0.8))
        l2 = pos(M(r"\text{voie 2 : }\; K^\circ = 5{,}4\times10^{5}\times\exp\!\left[\frac{91{,}8\times10^3}{8{,}314}\left(\frac{1}{723}-\frac{1}{298}\right)\right]", r"= 1{,}9\times10^{-4}", sc=0.68), -6.3, -1.85)
        l2[1].set_color(JAUNE)
        ok = M(r"\checkmark", sc=0.9, color=VERT).next_to(l2, RIGHT, buff=0.25)
        self.at(self.a("e5", "Et par Vant Off"), Ecrire(l2[0], rt=1.6)); self.at(self.a("e5", "Exactement"), Ecrire(l2[1], rt=0.6), FadeIn(ok, scale=1.6))
        rt = T(r"$25\,^\circ$C $\to$ $450\,^\circ$C : \;$K^\circ$ divisée par $\approx 3\times10^{9}$ !", sc=0.82, color=ROUGE).move_to([0, -3.0, 0])
        self.ecr(self.a("e6", "Retenez"), rt, rt=1.3)
        self.at(self.a("e6", "Aïe"), Create(enc(rt)), run_time=0.4)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"6.2 -- Choix de la température", "2/4 · Choix de T")
        e1 = pos(T(r"Réaction \textbf{exothermique} : travailler à \textbf{basse} température", sc=0.75, color=BLEU), -6.3, 2.1)
        e2 = pos(T(r"Réaction \textbf{endothermique} : travailler à \textbf{haute} température", sc=0.75, color=ROUGE), -6.3, 1.45)
        self.ecr(self.a("f2", "Réaction exothermique"), e1, rt=1.2); self.ecr(self.a("f2", "Réaction endothermique"), e2, rt=1.2)
        ar = pos(M(r"\text{Mais : }\; k(T) = A\,e^{-E_a/RT}", sc=0.85, color=ORANGE), -6.3, 0.55)
        ar2 = pos(T(r"la vitesse augmente \textbf{toujours} avec $T$", sc=0.7, color=ORANGE), 0.4, 0.55)
        self.ecr(self.a("f3", "Mais attention"), ar, rt=1.0); self.ecr(self.a("f3", "La vitesse"), ar2, rt=1.0)
        L = Arrow([-5.6, -1.6, 0], [5.8, -1.6, 0], color=CRAIE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.03)
        lt = M("T", sc=0.8).next_to(L.get_end(), DOWN, buff=0.15)
        cz = Rectangle(width=2.6, height=0.5, fill_color=JAUNE, fill_opacity=0.3, stroke_width=0).move_to([0.6, -1.6, 0])
        tz = T(r"\textbf{compromis}", sc=0.65, color=JAUNE).next_to(cz, DOWN, buff=0.15)
        a1 = Arrow([-0.8, -0.85, 0], [-5.2, -0.85, 0], color=BLEU, buff=0, stroke_width=5)
        t1 = T(r"thermodynamique : rendement", sc=0.6, color=BLEU).next_to(a1, UP, buff=0.1)
        a2 = Arrow([2.0, -0.85, 0], [5.6, -0.85, 0], color=ORANGE, buff=0, stroke_width=5)
        t2 = T(r"cinétique : vitesse", sc=0.6, color=ORANGE).next_to(a2, UP, buff=0.1)
        ti = T(r"réaction exothermique :", sc=0.62, color=GRIS).move_to([-4.0, -2.3, 0])
        self.at(self.a("f4", "Pour une réaction exothermique"), Create(L), FadeIn(lt), FadeIn(ti), run_time=0.6)
        self.at(self.a("f4", "La thermodynamique réclame"), GrowArrow(a1), FadeIn(t1), run_time=0.6)
        self.at(self.a("f4", "la cinétique réclame"), GrowArrow(a2), FadeIn(t2), run_time=0.6)
        self.at(self.a("f4", "Il faut un compromis"), FadeIn(cz), FadeIn(tz), run_time=0.5)
        ca = pos(T(r"\textbf{Catalyseur} : accélère la réaction, \textbf{sans modifier} $K^\circ$", sc=0.75, color=VERT), -6.3, -3.25)
        self.ecr(self.a("f5", "on ajoute un catalyseur"), ca, rt=1.3)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"6.3 -- Modifier $Q_r$ : la méthode", "3/4 · Pression et composition")
        tf = pos(T(r"$T$ fixée \;$\Rightarrow$\; $K^\circ$ ne bouge pas", sc=0.75, color=GRIS), -6.3, 2.1)
        self.ecr(self.a("g1", "la température reste fixée"), tf, rt=1.0)
        L = NumberLine(x_range=[0, 10, 1], length=11, include_ticks=False, color=CRAIE, stroke_width=3).move_to([0, 0.3, 0])
        fl = Arrow(L.get_end() + LEFT*0.3, L.get_end() + RIGHT*0.2, color=CRAIE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.5)
        lq = M("Q_r", sc=0.8).next_to(L.get_end(), DOWN, buff=0.25)
        kk = Line(L.n2p(5) + UP*0.25, L.n2p(5) + DOWN*0.25, color=ROUGE, stroke_width=4); lk = M(r"K^\circ", sc=0.8, color=ROUGE).next_to(kk, DOWN, buff=0.15)
        q = Dot(L.n2p(5), radius=0.13, color=JAUNE)
        eq = T(r"équilibre : $Q_r = K^\circ$", sc=0.65, color=JAUNE).next_to(L.n2p(5), UP, buff=0.35)
        self.at(self.a("g2", "On part"), Create(L), FadeIn(fl), FadeIn(lq), Create(kk), FadeIn(lk), run_time=0.6)
        self.play(FadeIn(q, scale=2), FadeIn(eq), run_time=0.5)
        pe = T(r"perturbation \textbf{instantanée}", sc=0.65, color=ORANGE).next_to(L.n2p(5), UP, buff=0.35)
        self.at(self.a("g3", "On le perturbe"), FadeOut(eq), Wiggle(q, scale_value=1.6), FadeIn(pe), run_time=0.8)
        qq = M(r"Q_r \nearrow \text{ ou } \searrow \text{ ?}", sc=0.75, color=ORANGE).next_to(pe, UP, buff=0.15)
        self.at(self.a("g3", "Q r a-t-il"), FadeIn(qq), run_time=0.4)
        a1 = Arrow(L.n2p(1.8) + UP*0.55, L.n2p(4.6) + UP*0.55, color=VERT, stroke_width=5, buff=0)
        t1 = T(r"$Q_r < K^\circ$ : sens \textbf{direct}", sc=0.62, color=VERT).next_to(a1, UP, buff=0.12)
        self.at(self.a("g4", "Si Q r devient plus petit"), FadeOut(pe), FadeOut(qq), q.animate.move_to(L.n2p(1.5)), run_time=0.6)
        self.at(self.a("g4", "le système évolue"), GrowArrow(a1), FadeIn(t1), run_time=0.6)
        q2 = Dot(L.n2p(8.5), radius=0.13, color=JAUNE)
        a2 = Arrow(L.n2p(8.2) + UP*0.55, L.n2p(5.4) + UP*0.55, color=ORANGE, stroke_width=5, buff=0)
        t2 = T(r"$Q_r > K^\circ$ : sens \textbf{indirect}", sc=0.62, color=ORANGE).next_to(a2, UP, buff=0.12)
        self.at(self.a("g5", "S'il devient plus grand"), FadeIn(q2, scale=2), GrowArrow(a2), FadeIn(t2), run_time=0.6)
        st = [r"exprimer $Q_r$", r"$Q_r$ monte ou descend ?", r"comparer à $K^\circ$"]
        bx = [boite(T(s, sc=0.62), JAUNE, JAUNE, w=3.7, h=0.85).move_to([-4.4 + 4.4*k, -1.75, 0]) for k, s in enumerate(st)]
        ar = [Arrow(bx[k].get_right(), bx[k+1].get_left(), color=JAUNE, buff=0.08, stroke_width=3, max_tip_length_to_length_ratio=0.3) for k in range(2)]
        self.at(self.a("g5", "C'est toujours"), LaggedStart(FadeIn(bx[0]), GrowArrow(ar[0]), FadeIn(bx[1]), GrowArrow(ar[1]), FadeIn(bx[2]), lag_ratio=0.4), run_time=1.2)
        pi = T(r"Pas d'intuition : un \textbf{calcul} !", sc=0.8, color=ROUGE).move_to([0, -3.0, 0])
        self.ecr(self.a("g5", "Pas d'intuition"), pi, rt=0.9)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"6.3 -- Effet de la pression", "3/4 · Pression et composition")
        a = pos(M(r"a_i = \frac{P_i}{P^\circ}", r"\;=\; \frac{n_i}{n_{\text{tot}}}\,\frac{P}{P^\circ}", sc=0.9), -6.3, 2.0)
        ga = pos(T(r"gaz parfaits", sc=0.62, color=GRIS), -1.3, 2.0)
        self.at(self.a("h1", "Pour un mélange"), FadeIn(ga), run_time=0.4)
        self.at(self.a("h1", "l'activité de chaque gaz"), Ecrire(a[0], rt=0.8)); self.at(self.a("h1", "Soit"), Ecrire(a[1], rt=1.0))
        q = M(r"Q_r = \Big(\prod_{\text{gaz}} n_i^{\,\nu_i}\Big)", r"\left(\frac{P}{n_{\text{tot}}\,P^\circ}\right)^{\Delta\nu_{\text{gaz}}}", sc=1.0).move_to([-1.6, 0.55, 0])
        self.at(self.a("h2", "On regroupe tout"), Ecrire(q, rt=1.5)); self.play(Create(enc(q, col=JAUNE)), run_time=0.4)
        dn = pos(M(DNU + r" = \sum_{\text{gaz}} \nu_i", sc=0.8, color=ORANGE), 2.6, 0.55)
        self.at(self.a("h2", "c'est cet exposant"), Indicate(q[1], color=ORANGE, scale_factor=1.1), run_time=0.7); self.ecr(self.a("h2", "la variation"), dn, rt=0.9)
        p1 = pos(M(r"P \nearrow \;:\quad Q_r \propto P^{\Delta\nu_{\text{gaz}}}", sc=0.85), -6.3, -0.85)
        self.ecr(self.a("h3", "Augmentons"), p1, rt=1.2)
        p2 = pos(M(DNU + r" < 0", r"\;\Rightarrow\; Q_r \searrow \;\Rightarrow\;", r"\text{ sens direct}", sc=0.85, color=VERT), -6.3, -1.65)
        ex = pos(T(r"ex. : $\mathrm{NH_3}$, \;$" + DNU + r" = -2$", sc=0.62, color=GRIS), 1.6, -1.65)
        self.at(self.a("h4", "Si delta nu gaz"), Ecrire(VGroup(p2[0], p2[1]), rt=1.0), FadeIn(ex)); self.at(self.a("h4", "Sens direct"), Ecrire(p2[2], rt=0.6))
        rr = pos(T(r"$P\nearrow$ : favorise le sens qui \textbf{consomme du gaz}", sc=0.8, color=JAUNE), -6.3, -2.55)
        self.ecr(self.a("h5", "une hausse de pression"), rr, rt=1.3); self.play(Create(enc(rr, col=JAUNE, buff=0.15)), run_time=0.4)
        p3 = pos(M(DNU + r" = 0 \;\Rightarrow\; \text{aucun effet de } P", sc=0.8, color=GRIS), -6.3, -3.45)
        self.ecr(self.a("h6", "Et si delta nu gaz"), p3, rt=1.1)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"6.3 -- Composition : les pièges", "3/4 · Pression et composition")
        ti = pos(T(r"\textbf{Piège : l'ajout d'un gaz inerte}", sc=0.78, color=ROUGE), -6.4, 2.1)
        self.ecr(self.a("i1", "un piège classique"), ti, rt=1.0)
        sep = Line([0.75, 1.65, 0], [0.75, -1.0, 0], color=GRIS, stroke_width=1.5)
        lt = pos(T(r"\textbf{à $P$ fixée}", sc=0.72, color=BLEU), -6.4, 1.35)
        l1 = pos(M(r"n_{\text{tot}} \nearrow \;\Rightarrow\; Q_r \propto n_{\text{tot}}^{\,-\Delta\nu_{\text{gaz}}}", sc=0.78), -6.4, 0.6)
        l2 = pos(M(DNU + r" < 0 \Rightarrow Q_r \nearrow \Rightarrow \text{sens indirect}", sc=0.7, color=ORANGE), -6.4, -0.15)
        l3 = pos(T(r"même effet qu'une baisse de $P$", sc=0.6, color=GRIS), -6.4, -0.75)
        self.at(self.a("i2", "À pression fixée"), FadeIn(lt), Create(sep), run_time=0.4)
        self.ecr(self.a("i2", "le gaz inerte augmente"), l1, rt=1.3)
        self.ecr(self.a("i3", "Avec delta nu gaz"), l2, rt=1.3); self.ecr(self.a("i3", "Même effet"), l3, rt=0.8)
        rt = pos(T(r"\textbf{à $V$ fixé}", sc=0.72, color=VERT), 1.2, 1.35)
        r1 = pos(M(r"P_i = \frac{n_i\,RT}{V}\ \text{ inchangées}", sc=0.78), 1.2, 0.5)
        r2 = pos(T(r"\textbf{aucun effet} !", sc=0.78, color=VERT), 1.2, -0.4)
        self.at(self.a("i4", "Mais à volume fixé"), FadeIn(rt), run_time=0.4); self.ecr(self.a("i4", "Les pressions partielles"), r1, rt=1.1)
        self.ecr(self.a("i4", "Aucun effet"), r2, rt=0.6)
        self.at(self.a("i4", "Même gaz"), Indicate(lt, color=JAUNE), Indicate(rt, color=JAUNE), run_time=0.8)
        b1 = pos(T(r"Éliminer un produit, ajouter un réactif : $Q_r\searrow$ \;$\Rightarrow$\; sens direct", sc=0.68), -6.4, -1.75)
        b2 = pos(T(r"Ajouter un solide pur : activité $= 1$ \;$\Rightarrow$\; aucun effet", sc=0.68), -6.4, -2.45)
        b3 = pos(T(r"Catalyseur : ne déplace \textbf{jamais} l'équilibre", sc=0.68, color=ROUGE), -6.4, -3.15)
        self.ecr(self.a("i5", "On élimine"), b1, rt=1.4)
        self.ecr(self.a("i6", "On ajoute un solide"), b2, rt=1.2); self.ecr(self.a("i6", "Et un catalyseur"), b3, rt=1.0)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"6.3 -- À vous : un gaz inerte", "3/4 · Pression et composition")
        cad = RoundedRectangle(width=12.4, height=1.6, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, 1.7, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.72, color=JAUNE), -5.9, 1.7)
        e1 = pos(M(r"2\,\mathrm{SO_2(g)} + \mathrm{O_2(g)} = 2\,\mathrm{SO_3(g)}", sc=0.8), -4.0, 2.05)
        e2 = pos(T(r"à l'équilibre : on ajoute de l'\textbf{argon}, à $P$ fixée.", sc=0.7), -4.0, 1.4)
        e3 = T(r"Sens ?", sc=0.75, color=JAUNE).next_to(e2, RIGHT, buff=0.35)
        self.at(self.t("j1"), Create(cad), Ecrire(tq, rt=0.4), run_time=0.5)
        self.at(self.a("j1", "Le dioxyde de soufre"), Ecrire(e1, rt=1.2)); self.at(self.a("j1", "on ajoute de l'argon"), Ecrire(e2, rt=1.2))
        self.at(self.a("j1", "Dans quel sens"), Ecrire(e3, rt=0.4))
        pa, arc = chrono(5.7, 1.7)
        self.jusqua(self.PH["j1"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("j2") - self.renderer.time - 0.1), rate_func=linear)
        r1 = pos(M(DNU + r" = 2 - 3 = -1", sc=0.85), -6.0, 0.2)
        r2 = pos(M(r"n_{\text{tot}} \nearrow \;\Rightarrow\; Q_r \propto n_{\text{tot}}^{\,+1} \nearrow", sc=0.85), -6.0, -0.75)
        self.at(self.a("j2", "Réponse"), FadeOut(pa), FadeOut(arc), Ecrire(r1, rt=0.9)); self.at(self.a("j2", "Ajouter de l'argon"), Ecrire(r2, rt=1.2))
        r3 = pos(M(r"Q_r > K^\circ \;\Longrightarrow\;", r"\text{ sens indirect}", sc=0.9, color=VERT), -6.0, -1.85)
        r4 = pos(T(r"le $\mathrm{SO_3}$ se décompose un peu", sc=0.68, color=GRIS), -6.0, -2.7)
        self.at(self.a("j3", "Q r devient"), Ecrire(r3[0], rt=0.8)); self.at(self.a("j3", "sens indirect"), Ecrire(r3[1], rt=0.6))
        self.play(Create(enc(r3, col=VERT, buff=0.15)), run_time=0.3)
        self.ecr(self.a("j3", "Le trioxyde"), r4, rt=1.0)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"6.4 -- Le procédé Haber--Bosch", "4/4 · Haber--Bosch")
        eq = pos(M(ch("N_2(g) + 3\\,H_2(g) = 2\\,NH_3(g)"), sc=0.85), -6.4, 2.1)
        inf = pos(M(r"\Delta_r H^\circ = -91{,}8\ \mathrm{kJ\cdot mol^{-1}}, \quad " + DNU + r" = -2", sc=0.7, color=GRIS), 0.0, 2.1)
        self.at(self.a("k1", "Revenons"), Ecrire(eq, rt=1.0)); self.at(self.a("k1", "Réaction exothermique"), Ecrire(inf, rt=1.2))
        t1 = pos(T(r"\textbf{Température} : compromis $400$--$500\,^\circ$C, catalyseur au fer", sc=0.72, color=ROUGE), -6.4, 1.2)
        t2 = pos(T(r"\textbf{Pression} : $" + DNU + r" < 0$, on comprime : $150$ à $300$ bar", sc=0.72, color=BLEU), -6.4, 0.55)
        t3 = pos(T(r"\textbf{Composition} : $\mathrm{NH_3}$ liquéfié, $\mathrm{N_2}$ et $\mathrm{H_2}$ recyclés, argon purgé", sc=0.72, color=VERT), -6.4, -0.1)
        self.ecr(self.a("k2", "Température"), t1, rt=1.6); self.ecr(self.a("k3", "Pression"), t2, rt=1.4); self.ecr(self.a("k4", "Composition"), t3, rt=1.5)
        base = -3.35; X = [-1.6, 0.6, 2.8, 5.0]; V = [0.004, 0.16, 0.36, 0.43]; P = ["1", "50", "200", "300"]; Lb = [r"0{,}4\,\%", r"16\,\%", r"36\,\%", r"43\,\%"]
        sol = Line([-2.6, base, 0], [6.0, base, 0], color=CRAIE, stroke_width=2)
        tt = VGroup(T(r"$x_{\mathrm{NH_3}}$ à l'équilibre", sc=0.65, color=JAUNE), T(r"$450\,^\circ$C, mélange", sc=0.58, color=GRIS), T(r"stœchiométrique", sc=0.58, color=GRIS)).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        tt.move_to([-6.4, -1.9, 0], aligned_edge=LEFT)
        bars, labs, vals = [], [], []
        for x, v, p, lb in zip(X, V, P, Lb):
            h = max(v*5.0, 0.04)
            b = Rectangle(width=1.1, height=h, fill_color=JAUNE, fill_opacity=0.55, stroke_color=JAUNE, stroke_width=2).move_to([x, base + h/2, 0])
            bars.append(b); labs.append(T(p + " bar", sc=0.55, color=GRIS).move_to([x, base - 0.28, 0]))
            vals.append(M(lb, sc=0.6, color=JAUNE).next_to(b, UP, buff=0.1))
        self.at(self.a("k5", "Regardez"), FadeIn(tt), Create(sol), *[FadeIn(l) for l in labs], run_time=0.6)
        self.at(self.a("k5", "Sous un bar"), GrowFromEdge(bars[0], DOWN), FadeIn(vals[0]), run_time=0.5)
        self.at(self.a("k6", "Sous deux cents bars"), *[GrowFromEdge(bars[k], DOWN) for k in (1, 2, 3)], *[FadeIn(vals[k]) for k in (1, 2, 3)], run_time=0.9)
        self.at(self.a("k6", "Plus du tiers"), Indicate(bars[2], color=ROUGE, scale_factor=1.08), Indicate(vals[2], color=ROUGE), run_time=0.8)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, M(VH + r"\qquad \text{endo : } K^\circ \nearrow \text{ avec } T,\ \ \text{exo : } K^\circ \searrow", sc=0.78), "l2", 1.85),
                (VERT, T(r"$T$ fixée : perturber, voir si $Q_r$ monte ou descend, comparer à $K^\circ$", sc=0.72), "l3", 0.45),
                (ORANGE, VGroup(T(r"Gaz inerte : un effet à $P$ fixée, aucun à $V$ fixé.", sc=0.72), T(r"Catalyseur : ne déplace rien !", sc=0.72, color=ORANGE)).arrange(DOWN, aligned_edge=LEFT, buff=0.2), "l4", -1.0)]
        for k, (col, F, sid, y) in enumerate(data):
            c = carte(k+1, col, -5.9, y); pos(F, -5.3, y)
            self.at(self.t(sid), Create(c[0]), FadeIn(c[1]), run_time=0.4); self.play(Ecrire(F, rt=1.8))
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- La dissociation de $\mathrm{N_2O_4}$", "Exercice résolu")
        eq = M(ch("N_2O_4(g)"), r"\;=\;", r"2\," + ch("NO_2(g)"), sc=1.1).move_to([0, 2.05, 0])
        i1 = T(r"incolore", sc=0.6, color=GRIS).next_to(eq[0], DOWN, buff=0.15)
        i2 = T(r"brun", sc=0.6, color=ORANGE).next_to(eq[2], DOWN, buff=0.15)
        self.at(self.a("m1", "Le tétraoxyde"), Ecrire(eq, rt=1.2))
        self.at(self.a("m1", "incolore"), FadeIn(i1), run_time=0.4); self.at(self.a("m1", "un gaz brun"), FadeIn(i2), eq[2].animate.set_color(ORANGE), run_time=0.5)
        d = pos(M(r"K^\circ(298\ \mathrm{K}) = 0{,}14", r"\qquad \Delta_r H^\circ = +57{,}2\ \mathrm{kJ\cdot mol^{-1}}\ \ (\text{constante})", sc=0.8, color=BLEU), -6.4, 0.75)
        self.at(self.a("m2", "On donne"), Ecrire(d[0], rt=0.9)); self.at(self.a("m2", "et delta-r-H"), Ecrire(d[1], rt=1.3))
        q1 = pos(T(r"\textbf{1.} $K^\circ$ à $350$ K ?", sc=0.8, color=JAUNE), -6.4, -0.2)
        q2 = pos(T(r"\textbf{2.} $1$ mol de $\mathrm{N_2O_4}$ pur à $350$ K : $\xi_{\text{éq}}$ sous $1$ bar ?", sc=0.8, color=JAUNE), -6.4, -0.95)
        q3 = T(r"sous $10$ bar ?", sc=0.8, color=JAUNE).next_to(q2, RIGHT, buff=0.3)
        self.ecr(self.a("m3", "Première question"), q1, rt=0.9); self.ecr(self.a("m4", "Deuxième question"), q2, rt=1.6)
        self.ecr(self.a("m4", "Puis sous dix bars"), q3, rt=0.6)
        c = M(r"T \text{ change}", r"\;\Rightarrow\;", r"\text{Van 't Hoff}", r"\qquad", r"P \text{ change}", r"\;\Rightarrow\;", r"Q_r", sc=0.9, color=VERT).move_to([0, -2.4, 0])
        self.at(self.a("m5", "On change de température"), Ecrire(VGroup(c[0], c[1], c[2]), rt=0.9))
        self.at(self.a("m5", "Puis on change"), Ecrire(VGroup(c[4], c[5], c[6]), rt=0.8))
        self.at(self.a("m5", "Les deux leviers"), Create(enc(c, col=VERT)), run_time=0.4)
        self.fin()

class S13(Cours):
    sid = "S13"
    def construct(self):
        self.entete(r"Exercice résolu -- La solution, étape par étape", "Exercice résolu")
        c1 = carte(1, BLEU, -6.1, 2.15)
        s1 = pos(M(r"\ln\frac{K^\circ_{350}}{K^\circ_{298}} = -\frac{57\,200}{8{,}314}\left(\frac{1}{350}-\frac{1}{298}\right) = +3{,}43", sc=0.7), -5.55, 2.15)
        self.at(self.t("n1"), Create(c1[0]), FadeIn(c1[1]), run_time=0.4); self.at(self.a("n1", "forme intégrée"), Ecrire(s1, rt=1.6))
        s1b = pos(M(r"K^\circ(350\ \mathrm{K}) = 0{,}14\times e^{3{,}43}", r"\;\approx\; 4{,}3", sc=0.72), -5.55, 1.3)
        s1b[1].set_color(JAUNE); x30 = T(r"$\times 30$ !", sc=0.65, color=ORANGE).next_to(s1b, RIGHT, buff=0.4)
        self.at(self.a("n2", "Donc K standard"), Ecrire(s1b[0], rt=1.1)); self.at(self.a("n2", "environ quatre"), Ecrire(s1b[1], rt=0.5))
        self.at(self.a("n2", "Trente fois"), FadeIn(x30, scale=1.4), run_time=0.4)
        c2 = carte(2, ORANGE, -6.1, 0.5)
        s2 = pos(M(r"\mathrm{N_2O_4} : 1-\xi \qquad \mathrm{NO_2} : 2\xi \qquad \text{gaz : } 1+\xi", sc=0.72), -5.55, 0.5)
        self.at(self.t("n3"), Create(c2[0]), FadeIn(c2[1]), run_time=0.4); self.at(self.a("n3", "Il reste"), Ecrire(s2, rt=1.6))
        c3 = carte(3, VERT, -6.1, -0.45)
        s3 = pos(M(r"Q_r = \frac{(2\xi)^2}{(1-\xi)(1+\xi)}\,\frac{P}{P^\circ} = \frac{4\xi^2}{1-\xi^2}\,\frac{P}{P^\circ}", sc=0.68), -5.55, -0.45)
        self.at(self.t("n4"), Create(c3[0]), FadeIn(c3[1]), run_time=0.4); self.at(self.a("n4", "Avec les pressions"), Ecrire(s3, rt=1.6))
        s3b = M(r"= K^\circ \;\Rightarrow\; \xi = \sqrt{\frac{K^\circ}{4P/P^\circ + K^\circ}}", sc=0.68, color=JAUNE).next_to(s3, RIGHT, buff=0.25)
        self.at(self.a("n5", "il égale K standard"), Ecrire(s3b[0][:3], rt=0.4)); self.at(self.a("n5", "ksi égale racine"), Ecrire(s3b[0][3:], rt=1.2))
        c4 = carte(4, ROUGE, -6.1, -1.5)
        s4 = pos(M(r"1\ \mathrm{bar} : \;\xi = 0{,}72\ \mathrm{mol}\ \ (72\,\%)", sc=0.75, color=JAUNE), -5.55, -1.5)
        s4b = pos(M(r"10\ \mathrm{bar} : \;\xi = 0{,}31\ \mathrm{mol}\ \ (31\,\%)", sc=0.75, color=ORANGE), 0.7, -1.5)
        self.at(self.t("n6"), Create(c4[0]), FadeIn(c4[1]), run_time=0.4); self.at(self.a("n6", "Sous un bar"), Ecrire(s4, rt=1.1))
        self.play(Create(enc(s4, col=JAUNE, buff=0.12)), run_time=0.3)
        self.at(self.a("n7", "Sous dix bars"), Ecrire(s4b, rt=1.1)); self.play(Create(enc(s4b, col=ORANGE, buff=0.12)), run_time=0.3)
        c5 = carte(5, JAUNE, -6.1, -2.45)
        s5 = pos(T(r"Vérifier : endothermique, $K^\circ \nearrow$ avec $T$ \;$\checkmark$", sc=0.7), -5.55, -2.45)
        s5b = pos(T(r"$" + DNU + r" = +1$ : comprimer favorise le sens indirect \;$\checkmark$", sc=0.7), -5.55, -3.05)
        self.at(self.t("n8"), Create(c5[0]), FadeIn(c5[1]), run_time=0.4); self.at(self.a("n8", "La réaction est endothermique"), Ecrire(s5, rt=1.3))
        self.at(self.a("n8", "Et delta nu gaz"), Ecrire(s5b, rt=1.5))
        br = pos(T(r"on chauffe : le gaz \textbf{brunit} !", sc=0.62, color=ORANGE), -5.55, -3.62)
        self.at(self.t("n9"), FadeIn(br), run_time=0.5)
        self.jusqua(self.t("n10") - 0.2)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        nx = T(r"Chapitre 7 \;$\longrightarrow$\; thermodynamique de l'oxydoréduction", sc=0.85, color=JAUNE).move_to([0, 0.3, 0])
        self.ecr(self.a("n10", "l'oxydoréduction"), nx, rt=1.8)
        self.fin()
