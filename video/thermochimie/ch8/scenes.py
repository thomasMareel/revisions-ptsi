from base import *
D = r"\mathrm{d}"
WE = r"\delta W_{\text{élec}}"
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)
def chrono(x, y):
    pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([x, y, 0])
    arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
    return pa, arc

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"THERMOCHIMIE \;·\; PT*", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Chapitre 8}", sc=1.3, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Piles électrochimiques", sc=0.95).move_to([0, 1.75, 0])
        tr = Line([-4.4, 1.3, 0], [4.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=0.9), Create(tr), run_time=1.0)
        cv = M(r"\text{réaction rédox}", r"\;\longrightarrow\;", r"\text{énergie électrique}", sc=0.85, color=BLEU).move_to([0, 0.7, 0])
        self.at(self.a("a2", "Une pile convertit"), Ecrire(cv, rt=1.2))
        dg = T(r"tension et énergie maximale : fixées par $\Delta_r G$", sc=0.68, color=VERT).move_to([0, 0.1, 0])
        self.ecr(self.a("a2", "Et c'est l'enthalpie libre"), dg, rt=1.2)
        items = []
        for k, (txt, col) in enumerate([("Description d'une pile", BLEU), ("Bilan énergétique", VERT), (r"Tension à vide et $\Delta_r G$", ORANGE),
                                         ("Décharge et capacité", ROUGE), (r"Exercice résolu : bilan d'une pile zinc--argent", JAUNE)]):
            y = -0.75 - 0.6*k
            items.append(VGroup(carte(k+1, col, -3.6, y), pos(T(txt, sc=0.78), -3.0, y)))
        de = T(r"$\Delta_r G = -\gamma F\,\Delta E$ : enfin \textbf{démontrée} !", sc=0.65, color=ORANGE).next_to(items[2], RIGHT, buff=0.5)
        for k, (it, (sid, fr)) in enumerate(zip(items, [("a3", "la description"), ("a3", "son bilan"), ("a3", "la tension à vide"), ("a3", "puis la décharge"), ("a5", "un exercice résolu")])):
            if k == 4: self.at(self.a("a4", "On va enfin"), FadeIn(de, shift=LEFT*0.2), run_time=0.6)
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a5", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"8.1 -- La pile Daniell", "1/4 · Description")
        def becher(x):
            return VMobject(color=CRAIE, stroke_width=3).set_points_as_corners([[x-1.3, -0.6, 0], [x-1.3, -3.0, 0], [x+1.3, -3.0, 0], [x+1.3, -0.6, 0]])
        b1, b2 = becher(-3.3), becher(3.3)
        s1 = Rectangle(width=2.55, height=1.8, fill_color=BLEU, fill_opacity=0.12, stroke_width=0).move_to([-3.3, -2.08, 0])
        s2 = Rectangle(width=2.55, height=1.8, fill_color=BLEU, fill_opacity=0.32, stroke_width=0).move_to([3.3, -2.08, 0])
        zn = Rectangle(width=0.3, height=2.7, fill_color=GRIS, fill_opacity=0.9, stroke_width=0).move_to([-3.75, -1.15, 0])
        cu = Rectangle(width=0.3, height=2.7, fill_color=ORANGE, fill_opacity=0.85, stroke_width=0).move_to([3.75, -1.15, 0])
        lz = M(r"\mathrm{Zn}", sc=0.75).next_to(zn, LEFT, buff=0.15).shift(UP*0.9)
        lc = M(r"\mathrm{Cu}", sc=0.75).next_to(cu, RIGHT, buff=0.15).shift(UP*0.9)
        iz = M(r"\mathrm{Zn^{2+}},\ \mathrm{SO_4^{2-}}", sc=0.55).move_to([-2.85, -2.6, 0])
        ic = M(r"\mathrm{Cu^{2+}},\ \mathrm{SO_4^{2-}}", sc=0.55).move_to([2.85, -2.6, 0])
        self.at(self.a("b1", "Deux béchers"), Create(b1), Create(b2), run_time=0.6)
        self.at(self.a("b1", "À gauche"), FadeIn(s1), FadeIn(zn), FadeIn(lz), FadeIn(iz), run_time=0.6)
        self.at(self.a("b1", "À droite"), FadeIn(s2), FadeIn(cu), FadeIn(lc), FadeIn(ic), run_time=0.6)
        sep = T(r"réactifs \textbf{séparés}", sc=0.6, color=JAUNE).move_to([0, -2.6, 0])
        self.at(self.a("b2", "les réactifs ne se touchent"), FadeIn(sep, scale=1.2), run_time=0.5)
        fil = VMobject(color=CRAIE, stroke_width=3).set_points_as_corners([[-3.75, 0.2, 0], [-3.75, 1.6, 0], [-0.5, 1.6, 0]])
        fil2 = VMobject(color=CRAIE, stroke_width=3).set_points_as_corners([[0.5, 1.6, 0], [3.75, 1.6, 0], [3.75, 0.2, 0]])
        R = VGroup(Rectangle(width=1.0, height=0.42, color=CRAIE, stroke_width=3), M("R", sc=0.7))
        R.move_to([0, 1.6, 0])
        an = M(r"\text{anode : }\ \mathrm{Zn \to Zn^{2+} + 2\,e^-}", sc=0.6, color=BLEU).move_to([-3.3, -3.45, 0])
        ca = M(r"\text{cathode : }\ \mathrm{Cu^{2+} + 2\,e^- \to Cu}", sc=0.6, color=ROUGE).move_to([3.3, -3.45, 0])
        self.at(self.a("b3", "Le zinc s'oxyde"), FadeIn(an), run_time=0.5)
        ea = Arrow([-2.9, 1.95, 0], [-1.3, 1.95, 0], color=BLEU, buff=0, stroke_width=4); le = M(r"e^-", sc=0.7, color=BLEU).next_to(ea, UP, buff=0.08)
        self.at(self.a("b3", "qui partent"), Create(fil), Create(fil2), FadeIn(R), run_time=0.7); self.play(GrowArrow(ea), FadeIn(le), run_time=0.4)
        el = [Dot(radius=0.07, color=BLEU) for _ in range(3)]
        chemin = VMobject().set_points_as_corners([[-3.75, 0.2, 0], [-3.75, 1.6, 0], [3.75, 1.6, 0], [3.75, 0.2, 0]])
        self.play(LaggedStart(*[MoveAlongPath(d, chemin, rate_func=linear) for d in el], lag_ratio=0.3), run_time=1.6)
        self.remove(*el)
        pm = M(r"\ominus", sc=0.9).move_to([-4.5, 0.9, 0]); pp = M(r"\oplus", sc=0.9).move_to([4.5, 0.9, 0])
        self.at(self.a("b4", "Côté cuivre"), FadeIn(ca), FadeIn(pm), FadeIn(pp), run_time=0.6)
        ia = Arrow([2.9, 1.25, 0], [1.3, 1.25, 0], color=ROUGE, buff=0, stroke_width=4); li = M("i", sc=0.7, color=ROUGE).next_to(ia, DOWN, buff=0.08)
        self.play(GrowArrow(ia), FadeIn(li), run_time=0.4)
        pt = VMobject(color=GRIS, stroke_width=16, stroke_opacity=0.45).set_points_as_corners([[-2.3, -1.9, 0], [-2.3, -0.1, 0], [2.3, -0.1, 0], [2.3, -1.9, 0]])
        lp = T(r"pont salin ($\mathrm{K^+}$, $\mathrm{NO_3^-}$)", sc=0.55, color=GRIS).move_to([0, 0.25, 0])
        self.at(self.a("b5", "un pont salin"), FadeOut(sep), Create(pt), FadeIn(lp), run_time=0.7)
        k1 = Arrow([0.3, -0.45, 0], [1.6, -0.45, 0], color=ROUGE, buff=0, stroke_width=3); kk = M(r"\mathrm{K^+}", sc=0.5, color=ROUGE).next_to(k1, DOWN, buff=0.05)
        n1 = Arrow([-0.3, -0.45, 0], [-1.6, -0.45, 0], color=BLEU, buff=0, stroke_width=3); nn = M(r"\mathrm{NO_3^-}", sc=0.5, color=BLEU).next_to(n1, DOWN, buff=0.05)
        self.at(self.a("b5", "Ses ions migrent"), GrowArrow(k1), GrowArrow(n1), FadeIn(kk), FadeIn(nn), run_time=0.6)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"8.1 -- Vocabulaire", "1/4 · Description")
        a = pos(T(r"\textbf{Anode} : oxydation \qquad pôle $\ominus$", sc=0.85, color=BLEU), -6.3, 2.0)
        c = pos(T(r"\textbf{Cathode} : réduction \qquad pôle $\oplus$", sc=0.85, color=ROUGE), -6.3, 1.25)
        self.ecr(self.a("c2", "L'anode"), a, rt=1.1); self.ecr(self.a("c3", "La cathode"), c, rt=1.1)
        ast = pos(T(r"\textit{Astuce} : \textbf{A}node, \textbf{O}xydation : voyelles \quad \textbf{C}athode, \textbf{R}éduction : consonnes", sc=0.64, color=GRIS), -6.3, 0.55)
        self.ecr(self.a("c3", "Astuce"), ast, rt=1.5)
        e = pos(M(r"e = V_\oplus - V_\ominus\ \ (i = 0)", r"\;=\; E_\oplus - E_\ominus", r"\;>\; 0", sc=0.95), -6.3, -0.5)
        e[2].set_color(VERT)
        self.at(self.a("c4", "La tension à vide"), Ecrire(e[0], rt=1.1)); self.at(self.a("c4", "E plus moins E moins"), Ecrire(e[1], rt=0.8))
        self.at(self.a("c4", "Toujours positive"), Ecrire(e[2], rt=0.4))
        no = M(r"\ominus\ \ \mathrm{Zn(s)}\,|\,\mathrm{Zn^{2+}},\mathrm{SO_4^{2-}}\ \|\ \mathrm{Cu^{2+}},\mathrm{SO_4^{2-}}\,|\,\mathrm{Cu(s)}\ \ \oplus", sc=0.9, color=JAUNE).move_to([0, -1.8, 0])
        self.at(self.a("c5", "la notation"), Ecrire(no, rt=1.6))
        rx = M(r"\mathrm{Zn(s) + Cu^{2+} \longrightarrow Zn^{2+} + Cu(s)}", r"\qquad \gamma = 2", sc=0.8, color=GRIS).move_to([0, -2.85, 0])
        self.ecr(self.a("c5", "et la double barre"), rx, rt=1.2)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"8.2 -- Bilan énergétique", "2/4 · Bilan énergétique")
        w = pos(M(r"\text{travail reçu : }\ \delta W = -P\,\mathrm{d}V + " + WE, sc=0.85), -6.3, 2.05)
        self.ecr(self.a("d1", "Une pile reçoit"), w, rt=1.3)
        mm = pos(T(r"monotherme et monobare :", sc=0.68, color=GRIS), -6.3, 1.2)
        g = M(r"\Delta G \;\leq\; W_{\text{élec}}", sc=1.4, color=JAUNE).move_to([-0.6, 0.45, 0])
        rv = T(r"égalité si \textbf{réversible}", sc=0.62, color=GRIS).next_to(g, RIGHT, buff=0.7)
        self.at(self.a("d2", "à température et pression"), FadeIn(mm), run_time=0.4)
        self.at(self.a("d2", "delta G est inférieur"), Ecrire(g, rt=1.0)); self.play(Create(enc(g, col=JAUNE)), run_time=0.4)
        self.at(self.a("d2", "Avec égalité"), FadeIn(rv), run_time=0.4)
        p = pos(M(r"W_{\text{fournie}} = -W_{\text{élec}} \;\leq\; -\Delta G", r"\quad\Longrightarrow\quad W_{\max} = -\Delta G", sc=0.92), -6.3, -0.85)
        p[1].set_color(JAUNE)
        self.at(self.a("d3", "Pour une pile"), Ecrire(p[0], rt=1.2)); self.at(self.a("d3", "Et l'énergie fournie"), Ecrire(p[1], rt=0.9))
        li = pos(T(r"enthalpie \textbf{libre} : l'énergie \textit{libre} d'être convertie en travail", sc=0.75, color=VERT), -6.3, -1.95)
        self.ecr(self.a("d4", "L'enthalpie libre porte"), li, rt=1.4)
        re = pos(T(r"réel ($i \neq 0$) : effet Joule, irréversibilités $\Rightarrow$ on récupère moins que $-\Delta G$", sc=0.66, color=ORANGE), -6.3, -2.95)
        self.ecr(self.a("d5", "En fonctionnement réel"), re, rt=1.5)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"8.2 -- Démonstration", "2/4 · Bilan énergétique")
        l1 = pos(M(r"\text{1}^{\text{er}}\text{ principe } (P \text{ fixée}) :\quad " + D + r"H = " + WE + r" + \delta Q", sc=0.85), -6.3, 2.05)
        l2 = pos(M(r"\text{2}^{\text{e}}\text{ principe :}\quad " + D + r"S = \frac{\delta Q}{T} + \delta S_c", sc=0.85), -6.3, 1.1)
        self.ecr(self.t("e2") + 0.2, l1, rt=1.4); self.ecr(self.t("e3") + 0.2, l2, rt=1.3)
        l3 = pos(M(D + r"G = " + D + r"H - T\," + D + r"S", r"\;=\;", WE, r"\;+\;", r"\delta Q", r"\;-\;", r"\delta Q", r"\;-\;T\,\delta S_c", sc=0.95), -6.3, -0.15)
        self.at(self.a("e4", "On forme"), Ecrire(l3[0], rt=0.9)); self.play(Ecrire(VGroup(*l3[1:]), rt=1.3))
        x1 = Line(l3[4].get_corner(DL), l3[4].get_corner(UR), color=ROUGE, stroke_width=4); x2 = Line(l3[6].get_corner(DL), l3[6].get_corner(UR), color=ROUGE, stroke_width=4)
        self.at(self.a("e4", "se compensent"), Create(x1), Create(x2), run_time=0.5)
        r1 = pos(M(r"=\;" + WE + r" - T\,\delta S_c", sc=0.95, color=JAUNE), -3.95, -1.15)
        self.ecr(self.a("e4", "Il reste"), r1, rt=0.9)
        sc_ = pos(M(r"\delta S_c \geq 0", sc=0.85, color=VERT), 2.2, -1.15)
        self.ecr(self.a("e5", "L'entropie créée"), sc_, rt=0.6)
        fi = M(D + r"G \leq " + WE + r" \;\Longrightarrow\; \Delta G \leq W_{\text{élec}}", sc=1.15, color=JAUNE).move_to([0, -2.5, 0])
        self.ecr(self.a("e5", "dé G est donc"), fi, rt=1.1)
        self.at(self.a("e5", "Et voilà"), Create(enc(fi, col=JAUNE)), run_time=0.4)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"8.3 -- Tension à vide et enthalpie libre", "3/4 · Tension à vide")
        l1 = pos(M(D + r"\xi \;\Rightarrow\; \gamma\," + D + r"\xi \text{ moles d'électrons dans le circuit}", sc=0.85), -6.3, 2.05)
        self.ecr(self.a("f1", "Quand l'avancement"), l1, rt=1.4)
        q = pos(M(D + r"q = \gamma F\," + D + r"\xi", sc=0.9), -6.3, 1.2)
        w = pos(M(WE + r" = -e\,\gamma F\," + D + r"\xi", sc=0.9, color=ORANGE), -1.6, 1.2)
        self.ecr(self.a("f2", "La charge vaut"), q, rt=0.8); self.ecr(self.a("f2", "Et sous la tension e"), w, rt=1.1)
        r = pos(M(r"i \to 0\ (\text{réversible}) :\quad " + D + r"G = " + WE, sc=0.9), -6.3, 0.3)
        g = pos(M(D + r"G = \Delta_r G\," + D + r"\xi", sc=0.9, color=BLEU), 1.4, 0.3)
        self.ecr(self.a("f3", "À courant nul"), r, rt=1.2); self.ecr(self.a("f3", "Et dé G, c'est aussi"), g, rt=0.8)
        fi = M(r"e = -\frac{\Delta_r G}{\gamma F}", sc=1.4, color=JAUNE).move_to([0, -1.05, 0])
        self.at(self.a("f4", "On simplifie"), Indicate(VGroup(w, g), color=JAUNE, scale_factor=1.05), run_time=0.7)
        self.ecr(self.a("f4", "e égale moins"), fi, rt=0.9); self.play(Create(enc(fi, col=JAUNE)), run_time=0.4)
        de = pos(M(r"e = E_\oplus - E_\ominus \;\Longrightarrow\; \Delta_r G = -\gamma F\,(E_\oplus - E_\ominus)", sc=0.88), -6.3, -2.45)
        ok = pos(T(r"la relation du chapitre 7 est \textbf{démontrée} ! \;$\checkmark$", sc=0.7, color=VERT), -6.3, -3.25)
        self.ecr(self.a("f5", "Avec e égale"), de, rt=1.5); self.ecr(self.a("f5", "La relation du chapitre"), ok, rt=1.0)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"8.3 -- Loi de Nernst de la pile", "3/4 · Tension à vide")
        l1 = pos(M(r"e = e^\circ - \frac{RT}{\gamma F}\ln Q_r", r"\qquad e^\circ = -\frac{\Delta_r G^\circ}{\gamma F} = E^\circ_\oplus - E^\circ_\ominus", sc=0.88), -6.3, 2.0)
        l1[1].set_color(GRIS)
        self.at(self.a("g1", "On remplace"), Ecrire(l1[1], rt=1.3)); self.at(self.a("g1", "Et la tension à vide devient"), Ecrire(l1[0], rt=1.3))
        l2 = pos(M(r"e \underset{298\,\mathrm{K}}{=} e^\circ - \frac{0{,}06}{\gamma}\log Q_r", r"\;=\; \frac{0{,}06}{\gamma}\log\frac{K^\circ}{Q_r}", sc=1.0, color=JAUNE), -6.3, 0.55)
        self.at(self.a("g2", "À deux cent"), Ecrire(l2[0], rt=1.3)); self.at(self.a("g2", "Ou, plus compact"), Ecrire(l2[1], rt=1.1))
        self.play(Create(enc(l2, col=JAUNE)), run_time=0.4)
        dt = pos(T(r"\textbf{Pile Daniell} :", sc=0.75, color=ORANGE), -6.3, -0.85)
        d1 = pos(M(r"e^\circ = 0{,}34 - (-0{,}76) = 1{,}10\ \mathrm{V}", sc=0.88), -3.6, -0.85)
        self.at(self.a("g3", "Appliquons"), FadeIn(dt), run_time=0.4); self.ecr(self.a("g3", "Sa tension"), d1, rt=1.2)
        d2 = pos(M(r"\Delta_r G^\circ = -2\times 96\,485\times 1{,}10 = -212\ \mathrm{kJ\cdot mol^{-1}}", sc=0.85), -6.3, -1.8)
        d3 = pos(M(r"\log K^\circ = \frac{2\times1{,}10}{0{,}059} \approx 37", r"\;\Rightarrow\; K^\circ \approx 10^{37}", sc=0.85), -6.3, -2.85)
        d3[1].set_color(VERT)
        self.ecr(self.a("g4", "Donc delta-r-G standard"), d2, rt=1.4); self.at(self.a("g4", "et K standard vaut"), Ecrire(d3, rt=1.3))
        tt = T(r"réaction \textbf{totale}", sc=0.72, color=VERT).next_to(d3, RIGHT, buff=0.5)
        self.at(self.a("g4", "Une réaction totale"), FadeIn(tt), run_time=0.4)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"8.3 -- À vous : une tension à vide", "3/4 · Tension à vide")
        cad = RoundedRectangle(width=12.4, height=1.6, corner_radius=0.12, color=JAUNE, stroke_width=2.5).move_to([0, 1.7, 0])
        tq = pos(T(r"\textbf{À vous !}", sc=0.72, color=JAUNE), -5.9, 1.7)
        e1 = pos(M(r"\ominus\ \mathrm{Cu(s)}\,|\,\mathrm{Cu^{2+}}\ \|\ \mathrm{Ag^+}\,|\,\mathrm{Ag(s)}\ \oplus", sc=0.82), -4.0, 2.05)
        kq = M(r"e^\circ\ ?\qquad \gamma\ ?", sc=0.8, color=JAUNE).next_to(e1, RIGHT, buff=0.7)
        e2 = pos(M(r"E^\circ(\mathrm{Cu^{2+}/Cu}) = 0{,}34\ \mathrm{V} \qquad E^\circ(\mathrm{Ag^+/Ag}) = 0{,}80\ \mathrm{V}", sc=0.7, color=GRIS), -4.0, 1.4)
        self.at(self.t("h1"), Create(cad), Ecrire(tq, rt=0.4), run_time=0.5)
        self.at(self.a("h1", "Une pile cuivre-argent"), Ecrire(e1, rt=1.2), Ecrire(e2, rt=1.2))
        self.at(self.a("h1", "Que vaut sa tension"), Ecrire(kq, rt=0.6))
        pa, arc = chrono(5.7, 1.7)
        self.jusqua(self.PH["h1"]["fin"]); self.add(pa)
        self.play(Create(arc), run_time=max(0.5, self.t("h2") - self.renderer.time - 0.1), rate_func=linear)
        r1 = pos(M(r"e^\circ = E^\circ_\oplus - E^\circ_\ominus = 0{,}80 - 0{,}34", r"\;=\; 0{,}46\ \mathrm{V}", sc=0.9), -6.0, 0.15)
        r1[1].set_color(JAUNE)
        self.at(self.a("h2", "Réponse"), FadeOut(pa), FadeOut(arc), Ecrire(r1[0], rt=1.2)); self.at(self.a("h2", "Soit"), Ecrire(r1[1], rt=0.6))
        r2 = pos(M(r"\mathrm{Cu + 2\,Ag^+ \longrightarrow Cu^{2+} + 2\,Ag}", r"\qquad \gamma = 2", sc=0.9), -6.0, -1.05)
        r2[1].set_color(JAUNE)
        self.at(self.a("h3", "Et un atome"), Ecrire(r2[0], rt=1.2)); self.at(self.a("h3", "gamma égale deux"), Ecrire(r2[1], rt=0.5))
        self.play(Create(enc(r1[1], col=JAUNE, buff=0.12)), Create(enc(r2[1], col=JAUNE, buff=0.12)), run_time=0.4)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"8.4 -- La décharge", "4/4 · Décharge et capacité")
        q = pos(M(r"Q_r = \frac{[\mathrm{Zn^{2+}}]}{[\mathrm{Cu^{2+}}]}", r"\;\nearrow", sc=0.9), -6.4, 1.85)
        self.at(self.a("i1", "Pour la pile Daniell"), Ecrire(q[0], rt=1.0)); self.at(self.a("i1", "Il augmente"), Ecrire(q[1], rt=0.3))
        d = pos(T(r"donc $e$ diminue", sc=0.72), -6.4, 0.85)
        u = pos(T(r"pile \textbf{usée} :", sc=0.72, color=ROUGE), -6.4, 0.2)
        uf = pos(M(r"e = 0 \Leftrightarrow \Delta_r G = 0 \Leftrightarrow Q_r = K^\circ", sc=0.75, color=ROUGE), -6.4, -0.45)
        self.ecr(self.a("i2", "Donc la tension"), d, rt=0.7); self.at(self.a("i2", "Et la pile est usée"), FadeIn(u), run_time=0.4)
        self.ecr(self.a("i2", "e est nulle"), uf, rt=1.4)
        dat = np.loadtxt("../pdf/data/daniell.dat", skiprows=1)
        ax = Axes(x_range=[0, 1050, 500], y_range=[0.85, 1.15, 0.1], x_length=5.4, y_length=4.0, axis_config={"stroke_opacity": 0}).move_to([3.6, -0.55, 0])
        o = ax.c2p(0, 0.85)
        axx = Arrow(o, ax.c2p(1080, 0.85), color=CRAIE, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.04)
        axy = Arrow(o, ax.c2p(0, 1.17), color=CRAIE, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.05)
        lx = M(r"q\ (\mathrm{C})", sc=0.55).next_to(ax.c2p(1080, 0.85), UP, buff=0.12).align_to(ax.c2p(1080, 0.85), RIGHT)
        ly = M(r"e\ (\mathrm{V})", sc=0.6).next_to(ax.c2p(0, 1.17), RIGHT, buff=0.12)
        ty = VGroup(*[M(s, sc=0.45, color=GRIS).next_to(ax.c2p(0, v), LEFT, buff=0.1) for s, v in (("0{,}90", 0.9), ("1{,}00", 1.0), ("1{,}10", 1.1))])
        tx = VGroup(*[M(s, sc=0.45, color=GRIS).next_to(ax.c2p(v, 0.85), DOWN, buff=0.1) for s, v in (("0", 0), ("500", 500), ("1000", 1000))])
        pts = [ax.c2p(x, y) for x, y in dat[:, :2] if y >= 0.86] + [ax.c2p(dat[-1, 0], 0.85)]
        cb = VMobject(color=BLEU, stroke_width=4).set_points_as_corners(pts)
        self.at(self.a("i3", "Mais regardez"), Create(axx), Create(axy), FadeIn(lx), FadeIn(ly), FadeIn(ty), FadeIn(tx), run_time=0.5)
        self.play(Create(cb), run_time=1.2)
        pl = T(r"$\approx 1{,}10$ V : quasi constante", sc=0.55, color=BLEU).next_to(ax.c2p(450, 1.09), UP, buff=0.12)
        self.at(self.a("i3", "quasi constante"), FadeIn(pl), run_time=0.4)
        k = pos(M(r"K^\circ \approx 10^{37} \;\Rightarrow\; Q_r \ll K^\circ", sc=0.85, color=VERT), -6.4, -1.5)
        k2 = pos(T(r"pendant presque toute la décharge", sc=0.62, color=GRIS), -6.4, -2.1)
        self.ecr(self.a("i4", "Parce que K standard"), k, rt=1.1); self.ecr(self.a("i4", "Q r reste minuscule"), k2, rt=1.0)
        vl = DashedLine(ax.c2p(965, 0.85), ax.c2p(965, 1.15), color=ROUGE, stroke_width=2)
        lv = T(r"$\mathrm{Cu^{2+}}$ épuisé", sc=0.55, color=ROUGE).next_to(ax.c2p(965, 0.95), LEFT, buff=0.15)
        self.at(self.a("i5", "Elle ne chute"), Create(vl), FadeIn(lv), run_time=0.6)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"8.5 -- Capacité et énergie", "4/4 · Décharge et capacité")
        d = pos(T(r"\textbf{Capacité} : charge totale débitée jusqu'à épuisement du réactif limitant", sc=0.72, color=BLEU), -6.3, 2.05)
        self.ecr(self.a("j1", "la capacité"), d, rt=1.5)
        q = M(r"q_{\max} = \gamma F\,\xi_{\max}", sc=1.2, color=JAUNE).move_to([-2.4, 1.1, 0])
        ah = pos(M(r"1\ \mathrm{A\cdot h} = 3\,600\ \mathrm{C}", sc=0.8, color=GRIS), 1.4, 1.1)
        self.ecr(self.a("j2", "q max égale"), q, rt=0.9); self.play(Create(enc(q, col=JAUNE)), run_time=0.4)
        self.ecr(self.a("j2", "un ampère-heure"), ah, rt=0.8)
        w = pos(M(r"W_{\max} = -\Delta G = \gamma F\,\xi_{\max}\,e", r"\;=\; q_{\max}\,e", sc=0.92), -6.3, -0.05)
        w[1].set_color(JAUNE)
        self.at(self.a("j3", "Et comme la tension"), Ecrire(w[0], rt=1.2)); self.at(self.a("j3", "q max fois e"), Ecrire(w[1], rt=0.6))
        ex = pos(T(r"Exemple : $1$ g de zinc", sc=0.75, color=ORANGE), -6.3, -1.05)
        x = pos(M(r"\xi_{\max} = \frac{1}{65{,}4} = 15{,}3\ \mathrm{mmol}", sc=0.8), -2.6, -1.05)
        self.at(self.a("j4", "Exemple"), FadeIn(ex), run_time=0.4); self.ecr(self.a("j4", "Soit quinze"), x, rt=1.0)
        c = pos(M(r"q_{\max} = 2\times96\,485\times15{,}3\times10^{-3} = 2\,950\ \mathrm{C}", r"\;=\; 0{,}82\ \mathrm{A\cdot h}", sc=0.8), -6.3, -2.0)
        c[1].set_color(JAUNE)
        self.at(self.a("j4", "donc deux mille"), Ecrire(c[0], rt=1.2)); self.at(self.a("j4", "ou zéro virgule"), Ecrire(c[1], rt=0.6))
        t = pos(M(r"i = 10\ \mathrm{mA} :\quad \Delta t = \frac{q_{\max}}{i} \approx 82\ \mathrm{h}", sc=0.82), -6.3, -3.0)
        tj = T(r"plus de 3 jours !", sc=0.72, color=VERT).next_to(t, RIGHT, buff=0.5)
        self.ecr(self.a("j5", "Sous dix"), t, rt=1.2); self.at(self.a("j5", "Plus de trois jours"), FadeIn(tj, scale=1.3), run_time=0.4)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"8.5 -- Ordres de grandeur", "4/4 · Décharge et capacité")
        r1 = VGroup(pos(T(r"Pile alcaline AA", sc=0.75, color=BLEU), -6.3, 2.0), pos(M(r"1{,}5\ \mathrm{V},\quad \approx 2{,}5\ \mathrm{A\cdot h}\quad (\approx 3{,}5\ \mathrm{W\cdot h})", sc=0.8), -0.6, 2.0))
        r2 = VGroup(pos(T(r"Smartphone (lithium-ion)", sc=0.75, color=VERT), -6.3, 1.3), pos(M(r"3{,}7\ \mathrm{V},\quad \approx 4\ \mathrm{A\cdot h}\quad (\approx 15\ \mathrm{W\cdot h})", sc=0.8), -0.6, 1.3))
        s = 2.2; x0 = -3.4
        def barre(v, y, col, nom):
            b = Rectangle(width=v*s, height=0.42, fill_color=col, fill_opacity=0.5, stroke_color=col, stroke_width=2).move_to([x0 + v*s/2, y, 0])
            n = T(nom, sc=0.6, color=col).next_to([x0, y, 0], LEFT, buff=0.3)
            val = M(f"{v:.1f}".replace(".", "{,}") + r"\ \mathrm{V}", sc=0.6, color=col).next_to(b, RIGHT, buff=0.15)
            return b, n, val
        bA, nA, vA = barre(1.5, -1.45, BLEU, "AA alcaline"); bL, nL, vL = barre(3.7, -2.15, VERT, "lithium-ion"); bP, nP, vP = barre(2.1, -2.85, ORANGE, "plomb")
        self.ecr(self.a("k1", "Une pile alcaline"), r1, rt=1.4); self.at(self.a("k1", "un virgule cinq volt"), GrowFromEdge(bA, LEFT), FadeIn(nA), FadeIn(vA), run_time=0.6)
        self.ecr(self.a("k2", "Une batterie"), r2, rt=1.4); self.at(self.a("k2", "trois virgule sept"), GrowFromEdge(bL, LEFT), FadeIn(nL), FadeIn(vL), run_time=0.6)
        q = pos(T(r"Électrolyte aqueux : $e \lesssim 2$ V, au-delà l'eau se décompose", sc=0.7, color=ORANGE), -6.3, 0.3)
        q2 = pos(T(r"Lithium-ion : $> 3$ V grâce à un électrolyte \textbf{organique}", sc=0.7, color=VERT), -6.3, -0.35)
        lim = DashedLine([x0 + 2*s, -1.05, 0], [x0 + 2*s, -3.2, 0], color=ROUGE, stroke_width=2.5)
        ll = T(r"limite de l'eau", sc=0.55, color=ROUGE).next_to(lim, DOWN, buff=0.1)
        self.ecr(self.a("k3", "Pourquoi pas plus"), q, rt=1.3)
        self.at(self.a("k3", "c'est l'eau elle-même"), Create(lim), FadeIn(ll), GrowFromEdge(bP, LEFT), FadeIn(nP), FadeIn(vP), run_time=0.7)
        self.ecr(self.a("k3", "Le lithium dépasse"), q2, rt=1.2)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete("À retenir", "Bilan")
        data = [(BLEU, T(r"Anode : oxydation, pôle $\ominus$ \qquad Cathode : réduction, pôle $\oplus$", sc=0.75), "l2", 1.85),
                (VERT, M(r"e = -\frac{\Delta_r G}{\gamma F} \qquad W_{\max} = -\Delta G", sc=0.88), "l3", 0.45),
                (ORANGE, M(r"q_{\max} = \gamma F\,\xi_{\max} \qquad W \approx q_{\max}\,e", sc=0.88), "l4", -1.0)]
        for k, (col, F, sid, y) in enumerate(data):
            c = carte(k+1, col, -5.9, y); pos(F, -5.3, y)
            self.at(self.t(sid), Create(c[0]), FadeIn(c[1]), run_time=0.4); self.play(Ecrire(F, rt=1.8))
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- Bilan d'une pile zinc--argent", "Exercice résolu")
        no = M(r"\ominus\ \mathrm{Zn(s)}\,|\,\mathrm{Zn^{2+}}\ (0{,}10\ \mathrm{mol\cdot L^{-1}})", r"\ \|\ \mathrm{Ag^+}\ (0{,}10\ \mathrm{mol\cdot L^{-1}})\,|\,\mathrm{Ag(s)}\ \oplus", sc=0.82).move_to([0, 2.0, 0])
        self.at(self.a("m2", "Au pôle moins"), Ecrire(no[0], rt=1.4)); self.at(self.a("m2", "Au pôle plus"), Ecrire(no[1], rt=1.4))
        v = T(r"$V = 50$ mL par compartiment \quad ; \quad zinc en excès", sc=0.68, color=GRIS).move_to([0, 1.25, 0])
        self.at(self.a("m2", "aussi"), FadeIn(v), run_time=0.5)
        e = M(r"E^\circ(\mathrm{Zn^{2+}/Zn}) = -0{,}76\ \mathrm{V} \qquad E^\circ(\mathrm{Ag^+/Ag}) = 0{,}80\ \mathrm{V}", sc=0.75, color=GRIS).move_to([0, 0.6, 0])
        self.at(self.t("m3"), FadeIn(e), run_time=0.5)
        q1 = pos(T(r"\textbf{1.} Réaction de fonctionnement ? \qquad \textbf{2.} Tension à vide initiale ?", sc=0.78, color=JAUNE), -6.4, -0.35)
        q2 = pos(T(r"\textbf{3.} Capacité ? Durée de fonctionnement sous $i = 20$ mA ?", sc=0.78, color=JAUNE), -6.4, -1.05)
        self.ecr(self.a("m3", "Questions"), q1, rt=1.6); self.ecr(self.a("m3", "puis la capacité"), q2, rt=1.4)
        chn = M(r"\text{demi-équations}", r"\;\to\;", r"e\ (\text{Nernst})", r"\;\to\;", r"\text{réactif limitant}", r"\;\to\;", r"q_{\max}", sc=0.85, color=VERT).move_to([0, -2.4, 0])
        self.at(self.a("m4", "les demi-équations"), Ecrire(chn[0], rt=0.7))
        self.at(self.a("m4", "la tension par Nernst"), Ecrire(VGroup(chn[1], chn[2]), rt=0.7))
        self.at(self.a("m4", "puis le réactif limitant"), Ecrire(VGroup(*chn[3:]), rt=0.9)); self.play(Create(enc(chn, col=VERT)), run_time=0.4)
        self.fin()

class S13(Cours):
    sid = "S13"
    def construct(self):
        self.entete(r"Exercice résolu -- La solution, étape par étape", "Exercice résolu")
        c1 = carte(1, BLEU, -6.1, 2.2)
        s1 = pos(M(r"\ominus :\ \mathrm{Zn \to Zn^{2+} + 2\,e^-}", r"\qquad \oplus :\ \mathrm{Ag^+ + e^- \to Ag}", sc=0.72), -5.55, 2.2)
        self.at(self.t("n1"), Create(c1[0]), FadeIn(c1[1]), run_time=0.4)
        self.at(self.a("n1", "À l'anode"), Ecrire(s1[0], rt=1.0)); self.at(self.a("n1", "À la cathode"), Ecrire(s1[1], rt=1.0))
        s1b = pos(M(r"\mathrm{Zn + 2\,Ag^+ \longrightarrow Zn^{2+} + 2\,Ag}", r"\qquad \gamma = 2", sc=0.75), -5.55, 1.55)
        s1b[1].set_color(JAUNE)
        self.at(self.a("n2", "on double"), Ecrire(s1b[0], rt=1.2)); self.at(self.a("n2", "Et gamma"), Ecrire(s1b[1], rt=0.4))
        c2 = carte(2, ORANGE, -6.1, 0.85)
        s2 = pos(M(r"e^\circ = 0{,}80 - (-0{,}76) = 1{,}56\ \mathrm{V}", sc=0.72), -5.55, 0.85)
        self.at(self.t("n3"), Create(c2[0]), FadeIn(c2[1]), run_time=0.4); self.ecr(self.a("n3", "La tension standard"), s2, rt=1.1)
        s2b = M(r"Q_r = \frac{0{,}10}{(0{,}10)^2} = 10 \;\Rightarrow\; e = 1{,}56 - \frac{0{,}06}{2}\log 10", r"\;=\; 1{,}53\ \mathrm{V}", sc=0.68); pos(s2b, -5.55, 0.1)
        s2b[1].set_color(JAUNE)
        self.at(self.a("n4", "Le quotient"), Ecrire(s2b[0], rt=1.4)); self.at(self.a("n4", "un virgule cinquante-trois"), Ecrire(s2b[1], rt=0.5))
        c3 = carte(3, VERT, -6.1, -0.75)
        s3 = pos(M(r"\text{limitant : }\ n(\mathrm{Ag^+}) = 0{,}10\times0{,}050 = 5{,}0\ \mathrm{mmol}", sc=0.72), -5.55, -0.75)
        self.at(self.t("n5"), Create(c3[0]), FadeIn(c3[1]), run_time=0.4); self.ecr(self.a("n5", "ce sont donc les ions"), s3, rt=1.3)
        s3b = M(r"\xi_{\max} = \frac{5{,}0}{2} = 2{,}5\ \mathrm{mmol}", sc=0.72, color=JAUNE).next_to(s3, RIGHT, buff=0.5)
        pg = pos(T(r"piège : \textbf{deux} $\mathrm{Ag^+}$ par avancement", sc=0.6, color=ROUGE), -5.55, -1.3)
        self.ecr(self.a("n6", "Attention au piège"), pg, rt=0.9); self.ecr(self.a("n6", "Ksi max vaut"), s3b, rt=0.9)
        c4 = carte(4, ROUGE, -6.1, -2.05)
        s4 = pos(M(r"q_{\max} = 2F\,\xi_{\max} = 482\ \mathrm{C}", sc=0.75, color=JAUNE), -5.55, -2.05)
        s4b = M(r"\Delta t = \frac{q_{\max}}{i} = \frac{482}{0{,}020} = 2{,}4\times10^{4}\ \mathrm{s} \approx 6\ \mathrm{h}\ 40", sc=0.7).next_to(s4, RIGHT, buff=0.5)
        self.at(self.t("n7"), Create(c4[0]), FadeIn(c4[1]), run_time=0.4); self.ecr(self.a("n7", "Elle vaut deux F"), s4, rt=1.0)
        self.ecr(self.a("n7", "Sous vingt"), s4b, rt=1.4)
        c5 = carte(5, JAUNE, -6.1, -2.95)
        s5 = pos(T(r"Vérifier : $K^\circ = 10^{52} \gg Q_r$ : $e$ quasi constante \;$\checkmark$", sc=0.7), -5.55, -2.95)
        s5b = pos(M(r"W \approx q_{\max}\,e = 482\times1{,}53 \approx 0{,}74\ \mathrm{kJ}", sc=0.72), -5.55, -3.55)
        self.at(self.t("n8"), Create(c5[0]), FadeIn(c5[1]), run_time=0.4); self.ecr(self.a("n8", "K standard vaut"), s5, rt=1.3)
        self.ecr(self.a("n8", "l'énergie vaut"), s5b, rt=1.1)
        self.at(self.a("n9", "C'est la fin"), *[FadeOut(m) for m in self.mobjects], run_time=0.4)
        f1 = T(r"\textbf{Fin du cours de thermochimie}", sc=1.0, color=JAUNE).move_to([0, 1.0, 0])
        f2 = T(r"Entraînez-vous : les exercices du chapitre", sc=0.8, color=CRAIE).move_to([0, 0.0, 0])
        f3 = T(r"Bon courage pour les concours !", sc=0.8, color=VERT).move_to([0, -0.9, 0])
        self.play(Ecrire(f1, rt=1.0))
        self.ecr(self.a("n9", "Pour vous entraîner"), f2, rt=1.2); self.ecr(self.a("n9", "Bon courage"), f3, rt=1.0)
        self.fin()
