from base import *
D = r"\mathrm{d}"
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def boite(txt, col, fond, w=3.5, h=1.0, sc=0.65):
    r = RoundedRectangle(width=w, height=h, corner_radius=0.1, color=col, stroke_width=2.5, fill_color=fond, fill_opacity=0.25)
    return VGroup(r, txt.move_to(r))
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"THERMOCHIMIE \;·\; PT*", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Chapitre 3}", sc=1.3, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Grandeurs de réaction et grandeurs standard", sc=0.95).move_to([0, 1.75, 0])
        tr = Line([-4.4, 1.3, 0], [4.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=0.9), Create(tr), run_time=1.0)
        q = M(ch("CH_4") + r" + 2\," + ch("O_2") + r"\longrightarrow " + ch("CO_2") + r" + 2\," + ch("H_2O"), r"\qquad 890\ \mathrm{kJ}", r"\;\;?", sc=0.9, color=BLEU).move_to([0, 0.55, 0]); q[2].set_color(JAUNE)
        self.at(self.a("a1", "Brûler"), Ecrire(q[0], rt=1.2))
        self.at(self.a("a1", "huit cent"), Ecrire(q[1], rt=0.6)); self.at(self.a("a1", "Comment"), FadeIn(q[2], scale=1.6), run_time=0.3)
        items = []
        for k, (txt, col) in enumerate([("Grandeurs de réaction", BLEU), ("Grandeurs standard", VERT), ("Loi de Hess", ORANGE), ("Influence de la température", ROUGE)]):
            y = -0.6 - 0.75*k
            items.append(VGroup(carte(k+1, col, -3.2, y), pos(T(txt, sc=0.82), -2.6, y)))
        for it, fr in zip(items, ["les grandeurs de réaction", "les grandeurs standard", "la loi de Hess", "et l'influence"]):
            self.jusqua(self.a("a3", fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a4", "dériver"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.9)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete("3.1 -- Grandeur de réaction : définition", "1/4 · Grandeurs de réaction")
        l1 = pos(T(r"Réaction d'avancement $\xi$, à $T$ et $P$ fixées", color=BLEU), -6.4, 2.35)
        self.ecr(self.t("b1") + 0.2, l1, rt=1.4)
        l2 = pos(M(r"X = X(T,\,P,\,\xi)", r"\qquad X = H,\ S,\ G\,\dots", sc=0.85), -5.9, 1.65)
        self.at(self.a("b2", "l'enthalpie"), Ecrire(l2[1], rt=0.9)); self.at(self.a("b2", "dépendent"), Ecrire(l2[0], rt=0.9))
        df = pos(M(r"\Delta_r X", r"\;=\;", r"\left(\dfrac{\partial X}{\partial \xi}\right)_{T,\,P}", sc=1.1), -5.7, -0.35)
        self.at(self.a("b4", "notée"), Ecrire(df[0], rt=0.5))
        self.at(self.a("b4", "la dérivée partielle"), Ecrire(VGroup(df[1], df[2]), rt=1.5))
        bx = enc(df); self.play(Create(bx), run_time=0.4)
        nom = T("grandeur de réaction", sc=0.6, color=GRIS).next_to(bx, UP, buff=0.15).align_to(bx, LEFT); self.play(FadeIn(nom), run_time=0.3)
        ax = Axes(x_range=[0, 1.05, 1], y_range=[0, 4.0, 1], x_length=4.6, y_length=3.6,
                  axis_config={"color": CRAIE, "stroke_width": 2, "include_ticks": False, "tip_width": 0.18, "tip_height": 0.18}).move_to([3.7, -0.7, 0])
        f = lambda x: 3.4 - 4.2*x + 3.2*x*x; fp = lambda x: -4.2 + 6.4*x
        cb = ax.plot(f, x_range=[0.02, 0.98, 0.01], color=BLEU, stroke_width=4)
        lx = M(r"\xi", sc=0.8).next_to(ax.x_axis.get_end(), DOWN, buff=0.15); ly = M("X", sc=0.8).next_to(ax.y_axis.get_end(), LEFT, buff=0.15)
        self.at(self.t("b5"), Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.5); self.play(Create(cb), run_time=0.8)
        x0 = 0.3; pt = Dot(ax.c2p(x0, f(x0)), color=JAUNE, radius=0.08)
        tg = Line(ax.c2p(x0-0.2, f(x0)-0.2*fp(x0)), ax.c2p(x0+0.25, f(x0)+0.25*fp(x0)), color=ROUGE, stroke_width=4)
        lt = M(r"\text{pente} = \Delta_r X", sc=0.72, color=ROUGE).move_to(ax.c2p(0.66, 3.3))
        self.at(self.a("b5", "la pente"), FadeIn(pt, scale=2), Create(tg), run_time=0.7); self.play(Ecrire(lt, rt=0.7))
        w = pos(T(r"$\Delta_r$ : pas une différence, une \textbf{dérivée}", sc=0.75, color=ROUGE), -5.9, -2.05)
        self.ecr(self.a("b6", "ce n'est pas"), w, rt=1.3)
        u = pos(T(r"en J$\cdot$mol$^{-1}$ (par mole d'avancement)", sc=0.75, color=VERT), -5.9, -2.9)
        self.ecr(self.a("b7", "en joules"), u, rt=1.2)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"3.1 -- Enthalpie libre de réaction", "1/4 · Grandeurs de réaction")
        l1 = pos(M(D+r"n_i = \nu_i\,"+D+r"\xi", sc=0.95, color=BLEU), -5.9, 2.25)
        self.ecr(self.a("c1", "la quantité"), l1, rt=1.0)
        l2 = pos(M(D+r"G \;=\; \sum_i \mu_i\,"+D+"n_i", r"\;=\;\Big(\sum_i \nu_i\,\mu_i\Big)\,"+D+r"\xi", sc=0.95), -5.9, 1.15)
        n2 = T(r"(à $T$, $P$ fixées)", sc=0.55, color=GRIS).next_to(l2, RIGHT, buff=0.5)
        self.at(self.a("c2", "dé G est"), Ecrire(l2[0], rt=1.3), FadeIn(n2))
        self.at(self.a("c2", "C'est-à-dire"), Ecrire(l2[1], rt=1.5))
        rg = pos(M(r"\Delta_r G", r"\;=\;", r"\sum_i \nu_i\,\mu_i", sc=1.25), -5.7, -0.35)
        self.ecr(self.a("c3", "delta-r-G"), rg, rt=1.3)
        bx = enc(rg, buff=0.25); self.play(Create(bx), run_time=0.4)
        gen = M(r"\Delta_r X \;=\; \sum_i \nu_i\,X_{m,i}", sc=0.95).move_to([3.2, -0.2, 0])
        ng = T("grandeurs molaires partielles", sc=0.55, color=GRIS).next_to(gen, DOWN, buff=0.2)
        self.at(self.a("c4", "elle se généralise"), Ecrire(gen, rt=1.5)); self.at(self.a("c4", "les grandeurs molaires"), FadeIn(ng), run_time=0.4)
        ex = pos(M(r"\mathrm{NH_3} :\quad \Delta_r G =", r"2\,\mu_{\mathrm{NH_3}}", r"-\,\mu_{\mathrm{N_2}}", r"-\,3\,\mu_{\mathrm{H_2}}", sc=0.9, color=VERT), -5.9, -1.75)
        self.at(self.t("c5"), Ecrire(ex[0], rt=0.8))
        for part, fr in zip(ex[1:], ["deux fois mu", "moins mu du diazote", "moins trois fois"]):
            self.at(self.a("c5", fr), Ecrire(part, rt=0.5))
        r1 = pos(T(r"attachée à l'équation écrite : coefficients $\times 2 \Rightarrow \Delta_r X \times 2$", sc=0.7, color=ORANGE), -5.9, -2.7)
        r2 = pos(T(r"dépend de $T$, de $P$ et de la \textbf{composition}", sc=0.7, color=ORANGE), -5.9, -3.3)
        self.ecr(self.a("c6", "Une grandeur"), r1, rt=1.6); self.ecr(self.t("c7") + 0.2, r2, rt=1.3)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete("3.2 -- Grandeurs standard de réaction", "2/4 · Grandeurs standard")
        df = M(r"\Delta_r X^\circ(T)", r"\;=\;", r"\sum_i \nu_i\,X^\circ_{m,i}(T)", sc=1.1).move_to([0, 2.0, 0])
        self.ecr(self.a("d2", "on fait le même calcul"), df, rt=1.8)
        bx = enc(df); self.play(Create(bx), run_time=0.4)
        nd = T("chaque constituant dans son état standard", sc=0.6, color=GRIS).next_to(bx, RIGHT, buff=0.35)
        nd = T("constituants dans leur état standard", sc=0.55, color=GRIS).next_to(bx, DOWN, buff=0.15)
        self.at(self.a("d2", "chaque constituant"), FadeIn(nd), run_time=0.4)
        R = boite(T(r"Réactifs purs\\dans leur état standard", sc=0.6), BLEU, BLEU).move_to([-4.0, 0.05, 0])
        P = boite(T(r"Produits purs\\dans leur état standard", sc=0.6), VERT, VERT).move_to([4.0, 0.05, 0])
        fl = Arrow(R.get_right(), P.get_left(), color=ROUGE, stroke_width=4, buff=0.15, max_tip_length_to_length_ratio=0.06)
        t1 = T(r"réaction fictive, à $T$ fixée, $P = P^\circ$", sc=0.55).next_to(fl, UP, buff=0.1)
        self.at(self.a("d3", "des réactifs"), FadeIn(R, shift=RIGHT*0.2), run_time=0.6)
        self.at(self.a("d3", "transformés"), GrowArrow(fl), run_time=0.6); self.play(FadeIn(P, shift=LEFT*0.2), run_time=0.5)
        self.at(self.t("d4"), FadeIn(t1), run_time=0.4)
        av = T(r"ne dépend que de $T$ \;$\Rightarrow$\; tabulable", sc=0.75, color=JAUNE).move_to([0, -0.95, 0])
        self.ecr(self.a("d4", "une grandeur standard"), av, rt=1.4)
        tr = VGroup(*[VGroup(M(s, sc=0.9, color=c), T(n, sc=0.5, color=GRIS)).arrange(DOWN, buff=0.12) for s, n, c in
                      [(r"\Delta_r H^\circ", "enthalpie standard de réaction", ORANGE), (r"\Delta_r S^\circ", "entropie standard de réaction", BLEU), (r"\Delta_r G^\circ", "enthalpie libre standard de réaction", VERT)]])
        tr.arrange(RIGHT, buff=0.9).move_to([0, -1.85, 0])
        for g, fr in zip(tr, ["l'enthalpie standard", "l'entropie standard", "et l'enthalpie libre"]):
            self.at(self.a("d5", fr), FadeIn(g, shift=UP*0.15), run_time=0.5)
        rel = M(r"\Delta_r G^\circ", r"\;=\;", r"\Delta_r H^\circ", r"\;-\;T\,", r"\Delta_r S^\circ", sc=1.1).move_to([0, -3.05, 0])
        rel[0].set_color(VERT); rel[2].set_color(ORANGE); rel[4].set_color(BLEU)
        for part, fr in zip([VGroup(rel[0], rel[1]), rel[2], VGroup(rel[3], rel[4])], ["delta-r-G standard", "delta-r-H standard", "moins T"]):
            self.at(self.a("d6", fr), Ecrire(part, rt=0.6))
        self.play(Create(enc(rel, buff=0.18)), run_time=0.4)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete("3.2 -- Signe des grandeurs standard", "2/4 · Grandeurs standard")
        h1 = pos(M(r"\Delta_r H^\circ < 0 \;:\; \text{exothermique}", sc=0.85, color=ROUGE), -5.9, 2.3)
        h2 = pos(M(r"\Delta_r H^\circ > 0 \;:\; \text{endothermique}", sc=0.85, color=BLEU), -5.9, 1.65)
        self.ecr(self.t("e2") + 0.2, h1, rt=1.2); self.ecr(self.a("e2", "Si elle est positive"), h2, rt=1.2)
        # barres d'entropie
        x0, y0 = 3.3, 0.85
        b1 = Rectangle(width=0.8, height=1.2, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, stroke_width=2).move_to([x0, y0+0.6, 0])
        b2 = Rectangle(width=0.8, height=0.35, color=GRIS, fill_color=GRIS, fill_opacity=0.5, stroke_width=2).move_to([x0+1.7, y0+0.175, 0])
        base = Line([x0-0.8, y0, 0], [x0+2.5, y0, 0], color=CRAIE, stroke_width=2)
        tb1 = T("gaz", sc=0.55).next_to(b1, DOWN, buff=0.12); tb2 = T("solide, liquide", sc=0.55).next_to(b2, DOWN, buff=0.12)
        vb1 = M(r"\approx 200", sc=0.55, color=ORANGE).next_to(b1, UP, buff=0.08); vb2 = M(r"\approx 50", sc=0.55, color=GRIS).next_to(b2, UP, buff=0.08)
        tu = M(r"S^\circ_m\ (\mathrm{J\cdot K^{-1}\cdot mol^{-1}})", sc=0.5, color=GRIS).move_to([x0+2.0, y0+1.45, 0])
        self.at(self.t("e4"), Create(base), GrowFromEdge(b1, DOWN), FadeIn(tb1), FadeIn(vb1), FadeIn(tu), run_time=0.8)
        self.at(self.a("e4", "que celle"), GrowFromEdge(b2, DOWN), FadeIn(tb2), FadeIn(vb2), run_time=0.6)
        rg = pos(M(r"\Delta_r S^\circ \text{ a le signe de }", r"\Delta\nu_{\text{gaz}} = \sum_{\text{gaz}} \nu_i", sc=0.85, color=JAUNE), -5.9, 0.45)
        self.at(self.a("e4", "Si la réaction crée"), Ecrire(rg, rt=1.8))
        ex = pos(M(ch("N_2(g)") + r" + 3\," + ch("H_2(g)") + " = 2\," + ch("NH_3(g)"), r"\qquad \Delta\nu_{\text{gaz}} = 2 - 4 = -2", r"\;\Rightarrow\; \Delta_r S^\circ < 0", sc=0.75), -5.9, -0.55)
        self.at(self.t("e5") + 0.3, Ecrire(ex[0], rt=1.0))
        self.at(self.a("e5", "On passe"), Ecrire(ex[1], rt=1.0)); self.at(self.a("e5", "On prévoit"), Ecrire(ex[2], rt=0.8))
        cal = pos(M(r"\Delta_r S^\circ = 2(192{,}8) - 191{,}6 - 3(130{,}7) =", r"-198{,}1\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}", sc=0.72), -5.9, -1.25); cal[1].set_color(VERT)
        self.at(self.a("e6", "avec les entropies"), Ecrire(cal[0], rt=1.5)); self.at(self.a("e6", "on trouve"), Ecrire(cal[1], rt=1.0))
        cad = RoundedRectangle(width=12.2, height=1.3, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, -2.7, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.72, color=JAUNE), -5.8, -2.7)
        eq = M(ch("CaCO_3(s)") + " = " + ch("CaO(s)") + " + " + ch("CO_2(g)"), sc=0.8).next_to(tq, RIGHT, buff=0.4)
        qq = M(r"\Delta_r S^\circ", r"\;?", sc=0.85).next_to(eq, RIGHT, buff=0.6); qq[1].set_color(JAUNE)
        self.at(self.t("e7"), Create(cad), Ecrire(tq, rt=0.4), run_time=0.5)
        self.at(self.a("e7", "Quel est"), Ecrire(eq, rt=1.0), Ecrire(qq, rt=0.6))
        pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([5.5, -2.7, 0])
        arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
        self.jusqua(self.PH["e7"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("e8") - self.renderer.time - 0.1), rate_func=linear)
        rep = M(r">0", r"\quad(+160)", sc=0.85, color=VERT).next_to(qq[0], RIGHT, buff=0.2)
        self.at(self.a("e8", "positif"), FadeOut(pa), FadeOut(arc), FadeOut(qq[1]), Ecrire(rep[0], rt=0.4))
        self.at(self.a("e8", "On trouve"), Ecrire(rep[1], rt=0.6))
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete("3.3 -- Grandeurs standard de formation", "3/4 · Loi de Hess")
        l1 = pos(T(r"\textbf{Réaction de formation} : forme ", r"\textbf{1 mol}", r" de l'espèce", color=BLEU), -6.4, 2.35)
        l2 = pos(T(r"à partir de ses éléments, pris dans leur \textbf{état standard de référence}", color=BLEU), -6.4, 1.8)
        self.ecr(self.a("f3", "la réaction qui forme"), l1, rt=1.3); self.ecr(self.a("f3", "à partir"), l2, rt=1.8)
        eq = M(r"\tfrac{1}{2}\," + ch("N_2(g)"), "+", r"\tfrac{3}{2}\," + ch("H_2(g)"), r"\longrightarrow", ch("NH_3(g)"), sc=1.1).move_to([0, 0.6, 0])
        for part, fr in zip([eq[0], VGroup(eq[1], eq[2]), VGroup(eq[3], eq[4])], ["un demi", "plus trois demis", "donnent"]):
            self.at(self.a("f4", fr), Ecrire(part, rt=0.6))
        df = M(r"\Delta_f H^\circ(\mathrm{NH_3(g)})", r"\;=\; -45{,}9\ \mathrm{kJ\cdot mol^{-1}}", sc=0.9, color=VERT).move_to([0, -0.35, 0])
        nf = T("enthalpie standard de formation", sc=0.55, color=GRIS).next_to(df, DOWN, buff=0.15)
        self.at(self.a("f5", "l'enthalpie standard de formation"), Ecrire(df[0], rt=0.9), FadeIn(nf))
        self.at(self.a("f5", "moins quarante"), Ecrire(df[1], rt=0.9))
        z = M(r"\Delta_f H^\circ\big(\text{corps simple dans son ESR}\big) \;=\; 0", sc=0.9).move_to([-2.2, -1.95, 0])
        self.ecr(self.a("f6", "pour un corps simple"), z, rt=1.8)
        bx = enc(z); self.play(Create(bx), run_time=0.4)
        exs = M(ch("O_2(g)") + r",\ " + ch("H_2(g)") + r",\ \mathrm{C(graphite)}\dots", sc=0.6, color=GRIS).next_to(bx, RIGHT, buff=0.35)
        self.play(FadeIn(exs), run_time=0.4)
        w = pos(M(r"\text{mais}\quad \Delta_f H^\circ(\mathrm{O_3}) \neq 0 \qquad \Delta_f H^\circ(\text{diamant}) \neq 0", sc=0.8, color=ROUGE), -5.9, -3.1)
        self.ecr(self.a("f7", "c'est faux"), w, rt=1.6)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete("3.3 -- Loi de Hess", "3/4 · Loi de Hess")
        hs = pos(M(r"\Delta_r H^\circ", r"\;=\;", r"\sum_i \nu_i\,\Delta_f H^\circ_i", sc=1.1), -5.7, 2.05)
        self.ecr(self.t("g2") + 0.2, hs, rt=2.0)
        bx = enc(hs); self.play(Create(bx), run_time=0.4)
        fe = VGroup(T(r"$H$ est une fonction d'état :", sc=0.65, color=JAUNE), T("le chemin est libre", sc=0.65, color=JAUNE)).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(bx, RIGHT, buff=0.6)
        self.at(self.a("g3", "Parce que"), Ecrire(fe[0], rt=0.9)); self.at(self.a("g3", "On peut choisir"), Ecrire(fe[1], rt=0.7))
        R = boite(M(ch("CH_4(g)") + " + " + ch("Cl_2(g)"), sc=0.75), BLEU, BLEU, w=3.6, h=0.8).move_to([-3.9, 0.35, 0])
        P = boite(M(ch("CH_3Cl(g)") + " + " + ch("HCl(g)"), sc=0.75), VERT, VERT, w=3.9, h=0.8).move_to([3.9, 0.35, 0])
        E = boite(VGroup(M(r"\mathrm{C(gr)} + 2\," + ch("H_2(g)") + " + " + ch("Cl_2(g)"), sc=0.7), T("éléments dans leur ESR", sc=0.45, color=GRIS)).arrange(DOWN, buff=0.1), GRIS, GRIS, w=4.6, h=1.05).move_to([0, -1.7, 0])
        top = Arrow(R.get_right(), P.get_left(), color=ROUGE, stroke_width=5, buff=0.12, max_tip_length_to_length_ratio=0.07)
        tt = M(r"\Delta_r H^\circ = \;?", sc=0.75, color=ROUGE).next_to(top, UP, buff=0.1)
        self.at(self.t("g4"), FadeIn(R), run_time=0.4); self.play(GrowArrow(top), FadeIn(P), FadeIn(tt), run_time=0.7)
        a1 = Arrow(R.get_bottom(), E.get_corner(UL) + RIGHT*0.6, color=CRAIE, stroke_width=3.5, buff=0.1, max_tip_length_to_length_ratio=0.1)
        a2 = Arrow(E.get_corner(UR) + LEFT*0.6, P.get_bottom(), color=CRAIE, stroke_width=3.5, buff=0.1, max_tip_length_to_length_ratio=0.1)
        self.at(self.a("g5", "on décompose"), GrowArrow(a1), run_time=0.6); self.play(FadeIn(E), run_time=0.4)
        self.at(self.a("g5", "puis on reforme"), GrowArrow(a2), run_time=0.6)
        t1 = M(r"-\Delta_f H^\circ(\mathrm{CH_4})", sc=0.62, color=BLEU).move_to([-5.0, -1.05, 0])
        t2 = VGroup(M(r"+\Delta_f H^\circ(\mathrm{CH_3Cl})", sc=0.62, color=VERT), M(r"+\Delta_f H^\circ(\mathrm{HCl})", sc=0.62, color=VERT)).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to([5.0, -1.2, 0])
        self.at(self.t("g6"), Ecrire(t1, rt=0.8)); self.at(self.a("g6", "Former"), Ecrire(t2, rt=1.2))
        cal = pos(M(r"\Delta_r H^\circ =", r"-81{,}9", r"-\,92{,}3", r"+\,74{,}6", r"\;=\; -99{,}6\ \mathrm{kJ\cdot mol^{-1}}", sc=0.85), -6.0, -3.0)
        cal[4].set_color(ROUGE)
        self.at(self.t("g7"), Ecrire(cal[0], rt=0.5))
        for part, fr in zip(cal[1:], ["moins quatre-vingt-un", "moins quatre-vingt-douze", "plus soixante-quatorze", "On obtient"]):
            self.at(self.a("g7", fr), Ecrire(part, rt=0.6))
        exo = T(r"exothermique", sc=0.7, color=ROUGE).next_to(cal, RIGHT, buff=0.4)
        self.at(self.a("g8", "Et la réaction"), FadeIn(exo, shift=LEFT*0.2), run_time=0.4)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete("3.3 -- Entropie standard et pièges classiques", "3/4 · Loi de Hess")
        l1 = pos(T(r"Tables : entropies molaires standard $S^\circ_m$ (valeurs \textbf{absolues})", color=BLEU), -6.4, 2.35)
        self.ecr(self.a("h1", "Les tables"), l1, rt=1.8)
        fs = pos(M(r"\Delta_r S^\circ", r"\;=\;", r"\sum_i \nu_i\,S^\circ_{m,i}", sc=1.1), -5.7, 1.2)
        self.ecr(self.t("h2") + 0.3, fs, rt=1.8); self.play(Create(enc(fs)), run_time=0.4)
        P = [(r"\textbf{Piège 1}", r"S^\circ_m(\mathrm{O_2}) = 205\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}} \neq 0", r"\text{mais } \Delta_f H^\circ(\mathrm{O_2}) = 0", "h4", "Pour le dioxygène", "Seule", -0.35),
             (r"\textbf{Piège 2}", r"\Delta_r H^\circ \text{ en } \mathrm{kJ\cdot mol^{-1}}", r"\Delta_r S^\circ \text{ en } \mathrm{J\cdot K^{-1}\cdot mol^{-1}}", "h5", "Les enthalpies", "les entropies", -1.5),
             (r"\textbf{Piège 3}", r"\Delta_f H^\circ(\mathrm{H_2O(l)}) = -285{,}8", r"\Delta_f H^\circ(\mathrm{H_2O(g)}) = -241{,}8\ \mathrm{kJ\cdot mol^{-1}}", "h6", "L'eau liquide", "l'eau vapeur", -2.65)]
        for lab, a, b, sid, fa, fb, y in P:
            L = pos(T(lab, sc=0.75, color=ROUGE), -5.9, y); A = pos(M(a, sc=0.7), -4.3, y); B = M(b, sc=0.7, color=ORANGE).next_to(A, RIGHT, buff=0.5)
            self.at(self.t(sid), Ecrire(L, rt=0.4)); self.at(self.a(sid, fa), Ecrire(A, rt=1.0)); self.at(self.a(sid, fb), Ecrire(B, rt=1.0))
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete("3.3 -- Combinaisons linéaires de réactions", "3/4 · Loi de Hess")
        rg = M(r"(3) = a\,(1) + b\,(2)", r"\quad\Longrightarrow\quad", r"\Delta_r X^\circ_3 = a\,\Delta_r X^\circ_1 + b\,\Delta_r X^\circ_2", sc=0.95).move_to([0, 2.05, 0])
        self.at(self.t("i2") + 0.2, Ecrire(rg[0], rt=0.9)); self.at(self.a("i2", "ses grandeurs"), Ecrire(VGroup(rg[1], rg[2]), rt=1.6))
        self.play(Create(enc(rg)), run_time=0.4)
        but = pos(M(r"\text{But : } \Delta_f H^\circ(\mathrm{CO}) \;?", sc=0.8, color=JAUNE), -5.9, 0.85)
        self.ecr(self.a("i3", "l'enthalpie de formation"), but, rt=1.0)
        e1 = pos(M(r"(1)\quad \mathrm{C(gr)} + " + ch("O_2") + r" \longrightarrow " + ch("CO_2"), sc=0.85), -5.9, 0.0)
        v1 = pos(M(r"\Delta_r H^\circ_1 = -393{,}5\ \mathrm{kJ\cdot mol^{-1}}", sc=0.8, color=BLEU), 1.2, 0.0)
        e2 = pos(M(r"(2)\quad " + ch("CO") + r" + \tfrac{1}{2}\," + ch("O_2") + r" \longrightarrow " + ch("CO_2"), sc=0.85), -5.9, -0.75)
        v2 = pos(M(r"\Delta_r H^\circ_2 = -283{,}0\ \mathrm{kJ\cdot mol^{-1}}", sc=0.8, color=BLEU), 1.2, -0.75)
        self.at(self.a("i4", "la combustion du carbone"), Ecrire(e1, rt=1.0), Ecrire(v1, rt=1.0))
        self.at(self.a("i4", "et celle"), Ecrire(e2, rt=1.0), Ecrire(v2, rt=1.0))
        tr = Line([-5.9, -1.25, 0], [5.6, -1.25, 0], color=CRAIE, stroke_width=1.5)
        e3 = pos(M(r"(1) - (2)\quad \mathrm{C(gr)} + \tfrac{1}{2}\," + ch("O_2") + r" \longrightarrow " + ch("CO"), sc=0.85, color=JAUNE), -5.9, -1.8)
        self.at(self.t("i5"), Create(tr), run_time=0.4); self.play(Ecrire(e3, rt=1.6))
        cal = pos(M(r"\Delta_f H^\circ(\mathrm{CO}) =", r"-393{,}5", r"+\,283{,}0", r"\;=\; -110{,}5\ \mathrm{kJ\cdot mol^{-1}}", sc=0.9), -5.9, -2.9); cal[3].set_color(VERT)
        self.at(self.t("i6"), Ecrire(cal[0], rt=0.5))
        for part, fr in zip(cal[1:], ["moins trois cent", "plus deux cent", "Soit"]):
            self.at(self.a("i6", fr), Ecrire(part, rt=0.6))
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete("3.4 -- Approximation d'Ellingham", "4/4 · Influence de la température")
        l1 = pos(T(r"\textbf{Ellingham} : $\Delta_r H^\circ$ et $\Delta_r S^\circ$ indépendantes de $T$ (hors changement d'état)", color=BLEU), -6.4, 2.35)
        self.ecr(self.a("j3", "l'enthalpie"), l1, rt=2.2)
        af = pos(M(r"\Delta_r G^\circ(T) = \Delta_r H^\circ - T\,\Delta_r S^\circ", sc=0.9), -6.0, 1.25)
        self.ecr(self.t("j4") + 0.2, af, rt=1.6); bx = enc(af, buff=0.18); self.play(Create(bx), run_time=0.4)
        na = T(r"fonction \textbf{affine} de $T$", sc=0.6, color=JAUNE).next_to(bx, DOWN, buff=0.15).align_to(bx, LEFT); self.play(FadeIn(na), run_time=0.3)
        H, S = -91.8, -0.1981
        ax = Axes(x_range=[0, 950, 100], y_range=[-110, 105, 50], x_length=4.9, y_length=4.4,
                  axis_config={"color": CRAIE, "stroke_width": 2, "include_ticks": False, "tip_width": 0.18, "tip_height": 0.18}).move_to([3.6, -1.0, 0])
        lx = M(r"T\ (\mathrm{K})", sc=0.6).next_to(ax.x_axis.get_end(), DOWN, buff=0.12); ly = M(r"\Delta_r G^\circ", sc=0.65).next_to(ax.y_axis.get_end(), RIGHT, buff=0.12)
        dr = Line(ax.c2p(0, H), ax.c2p(900, H - 900*S), color=BLEU, stroke_width=4)
        self.at(self.t("j5"), Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.6); self.play(Create(dr), run_time=1.0)
        p0 = Dot(ax.c2p(0, H), color=ORANGE, radius=0.08); t0 = M(r"\Delta_r H^\circ", sc=0.6, color=ORANGE).next_to(p0, LEFT, buff=0.12)
        self.at(self.a("j5", "L'ordonnée"), FadeIn(p0, scale=2), FadeIn(t0), run_time=0.4)
        tp = M(r"\text{pente} = -\Delta_r S^\circ > 0", sc=0.55, color=BLEU).move_to(ax.c2p(380, 78))
        self.at(self.a("j5", "La pente"), FadeIn(tp), run_time=0.4)
        o1 = pos(M(r"\Delta_r H^\circ = -91{,}8\ \mathrm{kJ\cdot mol^{-1}}", sc=0.7, color=ORANGE), -6.0, -0.35)
        o2 = pos(M(r"\Delta_r S^\circ = -198\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}", sc=0.7, color=BLEU), -6.0, -0.95)
        self.play(FadeIn(o1), FadeIn(o2), run_time=0.5)
        p1 = Dot(ax.c2p(298, H - 298*S), color=VERT, radius=0.08)
        g1 = pos(M(r"\Delta_r G^\circ(298\ \mathrm{K}) = -32{,}7\ \mathrm{kJ\cdot mol^{-1}}", sc=0.7, color=VERT), -6.0, -1.7)
        self.at(self.t("j6"), FadeIn(p1, scale=2), Ecrire(g1, rt=1.2))
        Ti = H/S; p2 = Dot(ax.c2p(Ti, 0), color=ROUGE, radius=0.09); t2 = M("T_i", sc=0.65, color=ROUGE).next_to(p2, DOWN, buff=0.15).shift(RIGHT*0.15)
        g2 = pos(M(r"T_i = \dfrac{\Delta_r H^\circ}{\Delta_r S^\circ} = 463\ \mathrm{K}", sc=0.75, color=ROUGE), -6.0, -2.55)
        self.at(self.a("j7", "à la température"), FadeIn(p2, scale=2), FadeIn(t2), run_time=0.4)
        self.at(self.a("j7", "le rapport"), Ecrire(g2, rt=1.4))
        z1 = T(r"$\Delta_r G^\circ < 0$", sc=0.55, color=VERT).move_to(ax.c2p(125, -16)); z2 = T(r"$\Delta_r G^\circ > 0$", sc=0.55, color=ORANGE).move_to(ax.c2p(760, 22))
        self.at(self.t("j8"), FadeIn(z1), run_time=0.4); self.at(self.a("j8", "Au-dessus"), FadeIn(z2), run_time=0.4)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, r"\Delta_r X = \left(\dfrac{\partial X}{\partial \xi}\right)_{T,P} \qquad \Delta_r G = \sum_i \nu_i\,\mu_i", "k2", 2.05),
                (VERT, r"\Delta_r G^\circ(T) = \Delta_r H^\circ - T\,\Delta_r S^\circ", "k3", 0.7),
                (ORANGE, r"\Delta_r H^\circ = \sum_i \nu_i\,\Delta_f H^\circ_i \qquad \Delta_f H^\circ(\text{corps simple, ESR}) = 0", "k4", -0.5),
                (ROUGE, r"\text{Ellingham : } \Delta_r H^\circ,\ \Delta_r S^\circ \text{ constantes} \;\Rightarrow\; \Delta_r G^\circ \text{ affine en } T", "k5", -1.7)]
        for k, (col, fo, sid, y) in enumerate(data):
            c = carte(k+1, col, -5.9, y); F = pos(M(fo, sc=0.82), -5.3, y)
            self.at(self.t(sid), Create(c[0]), FadeIn(c[1]), run_time=0.4); self.play(Ecrire(F, rt=1.8))
        nx = T(r"Chapitre 4 \;$\longrightarrow$\; effets thermiques et température de flamme", sc=0.8, color=JAUNE).move_to([0, -3.0, 0])
        self.ecr(self.a("k6", "la chaleur"), nx, rt=1.8)
        self.fin()
