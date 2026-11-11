from base import *
D = r"\mathrm{d}"
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"THERMOCHIMIE \;·\; PT*", sc=0.55, color=GRIS).move_to([0, 3.1, 0])
        ti = T(r"\textbf{Chapitre 2}", sc=1.3, color=JAUNE).move_to([0, 2.4, 0])
        st = T(r"Enthalpie libre et potentiel chimique", sc=1.0).move_to([0, 1.6, 0])
        tr = Line([-3.9, 1.15, 0], [3.9, 1.15, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=0.9), Create(tr), run_time=1.0)
        q = M(r"\text{diamant}", r"\;\;\longrightarrow\;\;", r"\text{graphite}", r"\;\;?", sc=1.0, color=BLEU).move_to([0, 0.3, 0]); q[3].set_color(JAUNE)
        self.at(self.a("a1", "pourquoi un diamant"), Ecrire(q[0], rt=0.5))
        self.at(self.a("a1", "en graphite"), Ecrire(VGroup(q[1], q[2]), rt=0.6)); self.play(FadeIn(q[3], scale=1.6), run_time=0.3)
        items = []
        for k, (txt, col) in enumerate([(r"L'enthalpie libre $G$", BLEU), (r"Le potentiel chimique $\mu_i$", VERT), (r"Les états standard", ORANGE)]):
            y = -1.0 - 0.85*k
            items.append(VGroup(carte(k+1, col, -3.0, y), pos(T(txt, sc=0.85), -2.4, y)))
        for it, fr in zip(items, ["Un :", "Deux :", "Trois :"]):
            self.jusqua(self.a("a3", fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), run_time=0.3); self.play(Ecrire(it[1], rt=0.8))
        self.at(self.a("a4", "notre diamant"), Indicate(q, color=JAUNE, scale_factor=1.12), run_time=0.9)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete("2.1 -- La fonction enthalpie libre", "1/3 · Enthalpie libre")
        l1 = pos(T(r"En chimie : transformations à ", r"\textbf{température et pression fixées}"), -6.4, 2.35); l1[1].set_color(BLEU)
        self.ecr(self.a("b1", "la plupart"), l1, rt=1.8)
        rap = VGroup(M(r"U", r"\;:\;\text{énergie interne}", sc=0.8), M(r"H = U + PV", r"\;:\;\text{enthalpie}", sc=0.8), M(r"S", r"\;:\;\text{entropie}", sc=0.8)).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        pos(rap, -5.9, 0.75).set_color(GRIS)
        for r, fr in zip(rap, ["L'énergie interne", "L'enthalpie", "Et l'entropie"]):
            self.at(self.a("b3", fr), Ecrire(r, rt=0.8))
        g = M("G", r"\;=\;", r"H - TS", sc=1.3).move_to([2.6, 0.75, 0])
        self.ecr(self.a("b4", "G égale"), g, rt=1.2)
        bx = SurroundingRectangle(g, color=ROUGE, buff=0.25, corner_radius=0.08); self.play(Create(bx), run_time=0.4)
        nom = T("enthalpie libre (énergie de Gibbs)", sc=0.6, color=GRIS).next_to(bx, UP, buff=0.2)
        self.play(FadeIn(nom), run_time=0.3)
        g2 = M("G", r"\;=\;", "U", r"\;+\;PV", r"\;-\;TS", sc=1.2).move_to([2.6, -1.15, 0])
        self.ecr(self.a("b5", "G égale"), g2, rt=1.4)
        w = T(r"c'est bien $+\,PV$ \, (car $H = U + PV$)", sc=0.65, color=ROUGE).next_to(g2, DOWN, buff=0.45)
        self.at(self.a("b6", "c'est un plus"), g2[3].animate.set_color(ROUGE), Circumscribe(g2[3], color=ROUGE, run_time=1.0), FadeIn(w), run_time=1.0)
        e = pos(T(r"$G$ : grandeur \textbf{extensive}, en joules", sc=0.8, color=VERT), -5.9, -2.9)
        self.ecr(self.t("b7") + 0.2, e, rt=1.2)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete("2.1 -- Identité thermodynamique", "1/3 · Enthalpie libre")
        hyp = pos(T("système fermé, composition fixée", sc=0.6, color=GRIS), -6.4, 2.45)
        self.at(self.a("c1", "Prenons"), FadeIn(hyp), run_time=0.4)
        X = -5.2
        L1 = pos(M(D+"G =", D+"U", r"+\,P\,"+D+"V", r"+\,V\,"+D+"P", r"-\,T\,"+D+"S", r"-\,S\,"+D+"T", sc=0.95), X, 1.75)
        for part, fr in zip(L1, ["dé G égale", "dé U, plus", "plus P dé V", "plus V dé P", "moins T dé S", "moins S dé T"]):
            self.at(self.a("c2", fr), Ecrire(part, rt=0.45))
        L2 = pos(M(D+"U =", r"-\,P\,"+D+"V", r"+\,T\,"+D+"S", sc=0.95, color=BLEU), X, 0.85)
        n2 = T("(transformation réversible)", sc=0.55, color=GRIS).next_to(L2, RIGHT, buff=0.5)
        self.at(self.a("c3", "dé U égale"), Ecrire(L2, rt=1.6), FadeIn(n2))
        L3 = pos(M(D+"G =", r"-\,P\,"+D+"V", r"+\,T\,"+D+"S", r"+\,P\,"+D+"V", r"+\,V\,"+D+"P", r"-\,T\,"+D+"S", r"-\,S\,"+D+"T", sc=0.95), X, -0.15)
        L3[1].set_color(BLEU); L3[2].set_color(BLEU)
        self.at(self.t("c4"), L1[1].animate.set_color(BLEU), Ecrire(L3, rt=1.0), run_time=1.0)
        barre = lambda m, c: Line(m.get_corner(DL) + LEFT*0.02, m.get_corner(UR) + RIGHT*0.02, color=c, stroke_width=4)
        self.at(self.a("c4", "Les termes en P"), Create(barre(L3[1], ORANGE)), Create(barre(L3[3], ORANGE)), run_time=0.6)
        self.at(self.a("c4", "Les termes en T"), Create(barre(L3[2], VERT)), Create(barre(L3[5], VERT)), run_time=0.6)
        R = pos(M(D+"G", r"\;=\;", r"V\,"+D+"P", r"\;-\;S\,"+D+"T", sc=1.25), X, -1.45)
        self.ecr(self.a("c5", "dé G égale"), R, rt=1.3)
        bx = SurroundingRectangle(R, color=ROUGE, buff=0.25, corner_radius=0.08); self.play(Create(bx), run_time=0.4)
        fe = VGroup(T(r"$G$ est une fonction d'état :", sc=0.62, color=GRIS), T(r"vrai pour toute transformation", sc=0.62, color=GRIS)).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(bx, RIGHT, buff=0.5)
        self.at(self.a("c6", "ce résultat"), FadeIn(fe, shift=LEFT*0.2), run_time=0.5)
        v = pos(T(r"Variables naturelles de $G$ : ", r"$P$ et $T$", sc=0.8, color=VERT), X, -2.65)
        self.ecr(self.a("c7", "les variables"), v, rt=1.2)
        z = T(r"à $T$, $P$ fixées et composition fixée : $\mathrm{d}G = 0$", sc=0.7, color=JAUNE).next_to(v, DOWN, buff=0.3).align_to(v, LEFT)
        self.ecr(self.a("c7", "À température"), z, rt=1.4)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete("2.2 -- Potentiel chimique : définition", "2/3 · Potentiel chimique")
        l1 = pos(T(r"Réaction chimique $\Rightarrow$ les quantités de matière $n_i$ varient", color=BLEU), -6.4, 2.35)
        self.ecr(self.a("d1", "la composition"), l1, rt=1.6)
        gf = pos(M(r"G = G(T,\,P,\,n_1,\,n_2,\,\dots)", sc=0.95), -5.9, 1.55)
        self.ecr(self.t("d2") + 0.2, gf, rt=1.4)
        df = pos(M(r"\mu_i", r"\;=\;", r"\left(\dfrac{\partial G}{\partial n_i}\right)_{T,\,P,\,n_{j\neq i}}", sc=1.05), -5.7, -0.35)
        self.at(self.a("d3", "noté mu i"), Ecrire(df[0], rt=0.4))
        self.at(self.a("d3", "la dérivée partielle"), Ecrire(VGroup(df[1], df[2]), rt=1.8))
        bx = SurroundingRectangle(df, color=ROUGE, buff=0.22, corner_radius=0.08); self.play(Create(bx), run_time=0.4)
        nom = T("potentiel chimique", sc=0.6, color=GRIS).next_to(bx, UP, buff=0.15).align_to(bx, LEFT)
        self.play(FadeIn(nom), run_time=0.3)
        # graphe G(n_i)
        ax = Axes(x_range=[0, 4.2, 1], y_range=[0, 4.2, 1], x_length=4.6, y_length=3.7,
                  axis_config={"color": CRAIE, "stroke_width": 2, "include_ticks": False, "tip_width": 0.18, "tip_height": 0.18}).move_to([3.8, -0.9, 0])
        f = lambda x: 0.5 + 1.75*np.sqrt(x + 0.15); fp = lambda x: 1.75/(2*np.sqrt(x + 0.15))
        cb = ax.plot(f, x_range=[0, 3.9, 0.02], color=BLEU, stroke_width=4)
        lx = M("n_i", sc=0.8).next_to(ax.x_axis.get_end(), DOWN, buff=0.15); ly = M("G", sc=0.8).next_to(ax.y_axis.get_end(), LEFT, buff=0.15)
        self.at(self.t("d4"), Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.5); self.play(Create(cb), run_time=0.7)
        x0 = 1.6; pt = Dot(ax.c2p(x0, f(x0)), color=JAUNE, radius=0.08)
        self.at(self.a("d4", "on ajoute"), FadeIn(pt, scale=2), run_time=0.4)
        dx = 0.9
        h = Line(ax.c2p(x0, f(x0)), ax.c2p(x0+dx, f(x0)), color=ORANGE, stroke_width=3); vv = Line(ax.c2p(x0+dx, f(x0)), ax.c2p(x0+dx, f(x0)+fp(x0)*dx), color=VERT, stroke_width=3)
        lh = M(D+"n_i", sc=0.6, color=ORANGE).next_to(h, DOWN, buff=0.1); lv = M(D+"G", sc=0.6, color=VERT).next_to(vv, RIGHT, buff=0.1)
        self.play(Create(h), FadeIn(lh), run_time=0.6)
        self.at(self.a("d4", "de combien"), Create(vv), FadeIn(lv), run_time=0.6)
        tg = Line(ax.c2p(x0-1.0, f(x0)-fp(x0)*1.0), ax.c2p(x0+1.6, f(x0)+fp(x0)*1.6), color=ROUGE, stroke_width=4)
        lt = M(r"\text{pente} = \mu_i", sc=0.75, color=ROUGE).move_to(ax.c2p(1.25, 3.75))
        self.at(self.a("d5", "la pente"), Create(tg), run_time=0.8); self.play(Ecrire(lt, rt=0.7))
        add = pos(M(r"\text{ajout de }\mathrm{d}n_i \;\Rightarrow\; \mathrm{d}G = \mu_i\,\mathrm{d}n_i", sc=0.8, color=JAUNE), -5.9, -2.0)
        self.play(Ecrire(add, rt=1.0))
        it = pos(T(r"grandeur \textbf{intensive}, en J$\cdot$mol$^{-1}$", sc=0.8, color=VERT), -5.9, -2.95)
        self.ecr(self.t("d6") + 0.1, it, rt=1.2)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete("2.2 -- Enthalpie libre d'un mélange", "2/3 · Potentiel chimique")
        dg = M(D+"G", r"\;=\;", r"V\,"+D+"P", r"\;-\;S\,"+D+"T", r"\;+\;\sum_i \mu_i\,"+D+"n_i", sc=1.15).move_to([-0.6, 1.75, 0])
        for part, fr in zip([VGroup(dg[0], dg[1]), dg[2], dg[3], dg[4]], ["dé G égale", "V dé P", "moins S dé T", "plus la somme"]):
            self.at(self.a("e2", fr), Ecrire(part, rt=0.6))
        bx = SurroundingRectangle(dg, color=ROUGE, buff=0.22, corner_radius=0.08); self.play(Create(bx), run_time=0.4)
        br = Brace(dg[4], DOWN, color=JAUNE, buff=0.12); bt = T("terme chimique", sc=0.6, color=JAUNE).next_to(br, DOWN, buff=0.1)
        self.at(self.t("e3"), dg[4].animate.set_color(JAUNE), GrowFromCenter(br), FadeIn(bt), run_time=0.7)
        eu = pos(M("G", r"\;=\;", r"\sum_i n_i\,\mu_i", sc=1.15), -5.6, -0.85)
        self.ecr(self.a("e4", "G est simplement"), eu, rt=1.3)
        bx2 = SurroundingRectangle(eu, color=ROUGE, buff=0.22, corner_radius=0.08); self.play(Create(bx2), run_time=0.4)
        ne = T("identité d'Euler (admise)", sc=0.6, color=GRIS).next_to(bx2, UP, buff=0.15).align_to(bx2, LEFT)
        dv = M(r"=\; n_1\,\mu_1 + n_2\,\mu_2 + \dots", sc=0.95).next_to(bx2, RIGHT, buff=0.4)
        self.play(FadeIn(ne), run_time=0.3)
        self.at(self.a("e5", "chaque constituant"), Ecrire(dv, rt=1.6))
        cp = pos(M(r"\text{corps pur :}\quad G = n\,\mu", r"\quad\Longrightarrow\quad", r"\mu = \dfrac{G}{n} = G_m", sc=0.95, color=VERT), -5.6, -2.55)
        self.at(self.a("e6", "pour un corps pur"), Ecrire(cp[0], rt=1.0))
        self.at(self.a("e6", "Le potentiel chimique"), Ecrire(VGroup(cp[1], cp[2]), rt=1.2))
        nm = T("enthalpie libre molaire", sc=0.6, color=GRIS).next_to(cp[2], DOWN, buff=0.2)
        self.at(self.a("e6", "son enthalpie"), FadeIn(nm, shift=LEFT*0.2), run_time=0.4)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete("2.2 -- Expression du potentiel chimique", "2/3 · Potentiel chimique")
        mu = pos(M(r"\mu_i", r"\;=\;", r"\mu_i^\circ(T)", r"\;+\;RT", r"\,\ln a_i", sc=1.15), -5.9, 2.0)
        for part, fr in zip([VGroup(mu[0], mu[1]), mu[2], mu[3], mu[4]], ["Mu i égale", "mu i standard", "plus R T", "logarithme"]):
            self.at(self.a("f2", fr), Ecrire(part, rt=0.6))
        bx = SurroundingRectangle(mu, color=ROUGE, buff=0.22, corner_radius=0.08); self.play(Create(bx), run_time=0.4)
        ns = VGroup(T(r"$\mu_i^\circ$ : potentiel chimique standard", sc=0.65, color=JAUNE), T(r"valeur pour $a_i = 1$ ; ne dépend que de $T$", sc=0.6, color=GRIS)).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(bx, RIGHT, buff=0.5)
        self.at(self.t("f3"), mu[2].animate.set_color(JAUNE), Ecrire(ns[0], rt=0.9), run_time=0.9)
        self.at(self.a("f3", "la valeur"), FadeIn(ns[1]), run_time=0.4)
        rows = [(r"\text{gaz :}\quad \mu_i = \mu_i^\circ + RT\ln\dfrac{P_i}{P^\circ}", "Pour un gaz", 0.55),
                (r"\text{soluté :}\quad \mu_i = \mu_i^\circ + RT\ln\dfrac{c_i}{c^\circ}", "Pour un soluté", -0.55),
                (r"\text{solide, liquide pur :}\quad \mu = \mu^\circ", "Et pour un solide", -1.5)]
        for fo, fr, y in rows:
            self.ecr(self.a("f4", fr), pos(M(fo, sc=0.8), -5.9, y), rt=1.3)
        ax = Axes(x_range=[0, 3.3, 1], y_range=[-2.6, 1.6, 1], x_length=4.4, y_length=3.3,
                  axis_config={"color": CRAIE, "stroke_width": 2, "include_ticks": False, "tip_width": 0.18, "tip_height": 0.18}).move_to([4.1, -1.2, 0])
        cb = ax.plot(lambda a: np.log(a), x_range=[0.075, 3.1, 0.01], color=BLEU, stroke_width=4)
        lx = M("a_i", sc=0.8).next_to(ax.x_axis.get_end(), DOWN, buff=0.15); ly = M(r"\mu_i", sc=0.8).next_to(ax.y_axis.get_end(), LEFT, buff=0.15)
        self.at(self.t("f5"), Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.7)
        self.at(self.a("f5", "C'est une courbe"), Create(cb), run_time=1.3)
        p1 = Dot(ax.c2p(1, 0), color=JAUNE, radius=0.09); l1 = M("1", sc=0.7, color=JAUNE).next_to(ax.c2p(1, 0), DOWN, buff=0.15)
        l0 = M(r"\mu_i^\circ", sc=0.75, color=JAUNE).next_to(ax.c2p(0, 0), LEFT, buff=0.15)
        self.at(self.a("f5", "qui passe"), FadeIn(p1, scale=2), FadeIn(l1), FadeIn(l0), run_time=0.5)
        fl = Arrow(ax.c2p(1.5, 0.75), ax.c2p(2.7, 1.35), color=ORANGE, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.2)
        self.at(self.t("f6"), GrowArrow(fl), run_time=0.8)
        o1 = pos(M(r"RT \approx 2{,}5\ \mathrm{kJ\cdot mol^{-1}}\ \text{à 298 K}", sc=0.7, color=VERT), -5.9, -2.5)
        o2 = pos(M(r"P_i \times 2 \;\Rightarrow\; \mu_i + RT\ln 2 \approx \mu_i + 1{,}7\ \mathrm{kJ\cdot mol^{-1}}", sc=0.7, color=VERT), -5.9, -3.15)
        self.ecr(self.a("f7", "R T vaut"), o1, rt=1.2)
        self.ecr(self.a("f7", "Doubler"), o2, rt=1.8)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete("2.3 -- États standard", "3/3 · États standard")
        l1 = pos(T(r"\textbf{État standard} : état de référence, choisi par convention", color=BLEU), -6.4, 2.35)
        self.ecr(self.a("g1", "C'est un état"), l1, rt=1.6)
        c1 = T(r"même température $T$ que le système", sc=0.75, color=JAUNE); c2 = T(r"pression $P^\circ = 1$ bar", sc=0.75, color=JAUNE)
        ch_ = VGroup(c1, c2).arrange(RIGHT, buff=1.2).move_to([0, 1.45, 0])
        b1 = SurroundingRectangle(c1, color=JAUNE, buff=0.18, corner_radius=0.1, stroke_width=2); b2 = SurroundingRectangle(c2, color=JAUNE, buff=0.18, corner_radius=0.1, stroke_width=2)
        self.at(self.a("g2", "la même"), Ecrire(c1, rt=0.9), Create(b1), run_time=0.9)
        self.at(self.a("g2", "et la pression"), Ecrire(c2, rt=0.8), Create(b2), run_time=0.8)
        rows = [("gaz", r"gaz parfait pur, sous $P^\circ$", "g3", 0.4), ("solide ou liquide", r"corps pur, sous $P^\circ$", "g4", -0.3),
                ("soluté", r"$c^\circ = 1$ mol$\cdot$L$^{-1}$, comportement infiniment dilué", "g5", -1.0)]
        for lab, de, sid, y in rows:
            self.at(self.t(sid), Ecrire(pos(T(r"\textbf{" + lab + "}", sc=0.75), -5.6, y), rt=0.4))
            self.play(Ecrire(pos(T(de, sc=0.75), -2.3, y), rt=1.0))
        p1 = pos(T(r"\textbf{Piège 1} : pas de « température standard » — un état standard \textit{à chaque} $T$", sc=0.7, color=ROUGE), -5.6, -2.2)
        p2 = pos(T(r"\textbf{Piège 2} : l'état standard peut être fictif (référence de calcul)", sc=0.7, color=ORANGE), -5.6, -3.0)
        self.ecr(self.t("g6") + 0.2, p1, rt=2.2)
        self.ecr(self.t("g7") + 0.2, p2, rt=1.8)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete("2.3 -- État standard de référence (ESR)", "3/3 · États standard")
        l1 = pos(T(r"\textbf{ESR d'un élément} : état standard du corps simple \textbf{le plus stable} à $T$", color=BLEU), -6.4, 2.35)
        self.ecr(self.a("h2", "l'état standard"), l1, rt=2.0)
        rows = [("O", ch("O_2(g)"), r"et non $\mathrm{O_3(g)}$", "h3", 1.4), ("C", r"\text{graphite}", "et non le diamant", "h4", 0.7),
                ("Fe", ch("Fe(s)") + r"\text{ jusqu'à 1811 K}", r"puis $\mathrm{Fe(l)}$", "h5", 0.0)]
        for el, es, no, sid, y in rows:
            a = pos(M(r"\mathrm{" + el + r"}\;:", sc=0.85, color=JAUNE), -5.6, y); b = pos(M(es, sc=0.85, color=VERT), -4.3, y)
            c = T(no, sc=0.65, color=GRIS).next_to(b, RIGHT, buff=0.5)
            self.at(self.t(sid), Ecrire(a, rt=0.3)); self.play(Ecrire(b, rt=0.7)); self.play(FadeIn(c), run_time=0.3)
        cad = RoundedRectangle(width=12.2, height=1.75, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, -1.55, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.75, color=JAUNE), -5.7, -1.1)
        en = T(r"$\mathrm{Br_2}$ : $T_{\text{éb}} = 332$ K", sc=0.7).next_to(tq, RIGHT, buff=0.6)
        q1 = pos(M(r"\text{ESR à 298 K :}", sc=0.8), -5.7, -1.9); q2 = pos(M(r"\text{ESR à 400 K :}", sc=0.8), 0.6, -1.9)
        self.at(self.t("h6"), Create(cad), Ecrire(tq, rt=0.5), run_time=0.6)
        self.at(self.a("h6", "Le dibrome"), Ecrire(en, rt=0.8))
        self.at(self.a("h6", "Quel est"), Ecrire(q1, rt=0.8)); self.at(self.a("h6", "Et à quatre"), Ecrire(q2, rt=0.8))
        pa = VGroup(Rectangle(width=0.1, height=0.34), Rectangle(width=0.1, height=0.34)).arrange(RIGHT, buff=0.09).set_fill(JAUNE, 1).set_stroke(width=0).move_to([5.3, -1.1, 0])
        arc = Circle(radius=0.34, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
        self.jusqua(self.PH["h6"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("h7") - self.renderer.time - 0.1), rate_func=linear)
        r1 = M(ch("Br_2(l)"), sc=0.9, color=VERT).next_to(q1, RIGHT, buff=0.3); r2 = M(ch("Br_2(g)"), sc=0.9, color=VERT).next_to(q2, RIGHT, buff=0.3)
        self.at(self.a("h7", "le dibrome liquide"), FadeOut(pa), FadeOut(arc), Ecrire(r1, rt=0.6))
        self.at(self.a("h7", "et le dibrome gazeux"), Ecrire(r2, rt=0.6))
        ex = pos(T(r"\textbf{Exception} : H, N, O, F, Cl $\rightarrow$ gaz diatomique à toute température", sc=0.72, color=ORANGE), -5.7, -3.15)
        self.ecr(self.t("h8") + 0.3, ex, rt=2.4)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete("Retour à la question : diamant ou graphite ?", "Application")
        l1 = pos(M(r"\text{solides purs :}\quad a = 1 \;\Rightarrow\; \mu = \mu^\circ", sc=0.85, color=BLEU), -6.2, 2.2)
        self.ecr(self.a("i1", "deux solides purs"), l1, rt=1.6)
        l2 = VGroup(pos(M(r"\mu^\circ(\text{diamant}) - \mu^\circ(\text{graphite})", sc=0.8), -6.2, 1.3), pos(M(r"=\; +2{,}9\ \mathrm{kJ\cdot mol^{-1}}\quad\text{(à 298 K)}", sc=0.8), -5.6, 0.65))
        self.at(self.a("i2", "mu standard du diamant"), Ecrire(l2[0], rt=1.4))
        self.at(self.a("i2", "égale plus"), Ecrire(l2[1], rt=1.0))
        # niveaux
        xa = 3.4
        ax = Arrow([xa, -2.6, 0], [xa, 1.6, 0], color=CRAIE, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.05)
        la = M(r"\mu^\circ", sc=0.8).next_to(ax.get_end(), LEFT, buff=0.15)
        nd = Line([xa+0.5, 0.6, 0], [xa+2.3, 0.6, 0], color=BLEU, stroke_width=6); ng = Line([xa+0.5, -1.6, 0], [xa+2.3, -1.6, 0], color=VERT, stroke_width=6)
        td = T("diamant", sc=0.75, color=BLEU).next_to(nd, UP, buff=0.12); tg = T("graphite", sc=0.75, color=VERT).next_to(ng, DOWN, buff=0.12)
        self.at(self.t("i3"), GrowArrow(ax), FadeIn(la), run_time=0.5)
        self.play(Create(ng), FadeIn(tg), Create(nd), FadeIn(td), run_time=0.8)
        ec = DoubleArrow([xa+2.7, -1.6, 0], [xa+2.7, 0.6, 0], color=GRIS, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.1)
        te = M(r"2{,}9", sc=0.65, color=GRIS).next_to(ec, RIGHT, buff=0.1)
        self.play(GrowFromCenter(ec), FadeIn(te), run_time=0.5)
        fl = Arrow([xa+1.4, 0.45, 0], [xa+1.4, -1.45, 0], color=ROUGE, stroke_width=6, buff=0, max_tip_length_to_length_ratio=0.15)
        l4 = pos(T(r"évolution spontanée vers les $\mu$ les plus bas", sc=0.75, color=ROUGE), -6.2, -0.35)
        self.at(self.t("i4"), GrowArrow(fl), run_time=0.9); self.play(Ecrire(l4, rt=1.2))
        l5 = pos(T(r"diamant $\rightarrow$ graphite : ", r"possible", r", mais infiniment lent", sc=0.75), -6.2, -1.25); l5[1].set_color(VERT)
        self.at(self.a("i5", "est donc possible"), Ecrire(VGroup(l5[0], l5[1]), rt=1.0))
        self.at(self.a("i5", "Mais elle"), Ecrire(l5[2], rt=0.9))
        ms = T(r"le diamant est \textbf{métastable}", sc=0.75, color=JAUNE).next_to(l5, DOWN, buff=0.3).align_to(l5, LEFT)
        self.at(self.a("i5", "on dit"), Ecrire(ms, rt=0.9))
        f1 = pos(T(r"\textbf{Thermodynamique} : ce qui \textit{peut} se produire", sc=0.75, color=VERT), -6.2, -2.85)
        f2 = pos(T(r"\textbf{Cinétique} : à quelle vitesse", sc=0.75, color=ORANGE), -6.2, -3.4)
        self.ecr(self.a("i6", "la thermodynamique"), f1, rt=1.3)
        self.ecr(self.a("i6", "La cinétique"), f2, rt=1.0)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, r"G = H - TS \qquad \mathrm{d}G = V\,\mathrm{d}P - S\,\mathrm{d}T", "enthalpie libre et identité thermodynamique", "k2", 2.0, 0.55),
                (VERT, r"\mu_i = \left(\dfrac{\partial G}{\partial n_i}\right)_{T,P,n_{j\neq i}} \qquad G = \sum_i n_i\,\mu_i", "potentiel chimique", "k3", 0.35, 0.8),
                (ORANGE, r"\mu_i = \mu_i^\circ(T) + RT\ln a_i", "expression du potentiel chimique", "k4", -1.45, 0.55)]
        for k, (col, fo, lab, sid, y, dy) in enumerate(data):
            c = carte(k+1, col, -5.9, y)
            L = pos(T(lab, sc=0.6, color=col), -5.3, y + dy); F = pos(M(fo, sc=0.85), -5.3, y - 0.1)
            self.at(self.t(sid), Create(c[0]), FadeIn(c[1]), FadeIn(L), run_time=0.5); self.play(Ecrire(F, rt=1.8))
        nx = T(r"Chapitre 3 \;$\longrightarrow$\; grandeurs de réaction : $\Delta_r G = \sum_i \nu_i\,\mu_i$", sc=0.8, color=JAUNE).move_to([0, -3.0, 0])
        self.ecr(self.a("k5", "on applique"), nx, rt=1.8)
        self.fin()
