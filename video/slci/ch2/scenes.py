from base import *
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)
def chrono(x, y):
    pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([x, y, 0])
    arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
    return pa, arc
def axes(x, y, w, h, xr, yr, col=CRAIE, sw=2):
    return Axes(x_range=xr, y_range=yr, x_length=w, y_length=h,
                axis_config={"color": col, "stroke_width": sw, "include_ticks": False, "tip_width": 0.14, "tip_height": 0.14}).move_to([x, y, 0])
# ---- schémas-blocs au tableau ----
def blk(lab, x, y, w=1.6, h=0.75, col=CRAIE, sc=0.7, tex=True):
    r = Rectangle(width=w, height=h, color=col, stroke_width=3).move_to([x, y, 0])
    t = (M(lab, sc=sc, color=col) if tex else T(lab, sc=sc, color=col)).move_to(r)
    if t.width > w - 0.15: t.scale_to_fit_width(w - 0.2)
    return VGroup(r, t)
def som(x, y, r=0.24, col=CRAIE):
    c = Circle(radius=r, color=col, stroke_width=3).move_to([x, y, 0])
    d = r*0.7
    return VGroup(c, Line([x-d, y-d, 0], [x+d, y+d, 0], color=col, stroke_width=2), Line([x-d, y+d, 0], [x+d, y-d, 0], color=col, stroke_width=2))
def fl(*pts, col=CRAIE, sw=3):
    """Flèche en ligne brisée : segments, puis une flèche sur le dernier."""
    pts = [np.array([p[0], p[1], 0]) for p in pts]
    g = VGroup(*[Line(pts[i], pts[i+1], color=col, stroke_width=sw) for i in range(len(pts) - 2)])
    g.add(Arrow(pts[-2], pts[-1], buff=0, color=col, stroke_width=sw, max_tip_length_to_length_ratio=0.5, tip_length=0.18))
    return g
def sg(t, x, y, col=CRAIE): return M(t, sc=0.6, color=col).move_to([x, y, 0])
def pt(x, y, col=CRAIE): return Dot([x, y, 0], radius=0.06, color=col)

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PTSI", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Automatique -- Chapitre 2}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Schéma-blocs et systèmes asservis", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        y = 0.45
        s = som(-2.6, y); b = blk(r"H(p)", 0, y, w=1.7); ca = blk(r"\text{capteur}", 0, y - 0.95, w=1.7, h=0.6, sc=0.6, col=BLEU)
        f1 = fl((-4.3, y), (-2.84, y)); f2 = fl((-2.36, y), (-0.85, y)); f3 = fl((0.85, y), (3.2, y))
        r1 = fl((2.2, y), (2.2, y - 0.95), (0.85, y - 0.95), col=BLEU); r2 = fl((-0.85, y - 0.95), (-2.6, y - 0.95), (-2.6, y - 0.24), col=BLEU)
        self.at(self.a("a1", "assembler les blocs"), Create(b[0]), FadeIn(b[1]), Create(f2), Create(f3), run_time=0.7)
        self.at(self.a("a2", "mesurer la sortie"), Create(ca[0]), FadeIn(ca[1]), Create(r1), FadeIn(pt(2.2, y)), run_time=0.7)
        self.at(self.a("a2", "la comparer"), Create(s), Create(r2), Create(f1), run_time=0.7)
        self.at(self.a("a2", "et corriger"), Indicate(b, color=JAUNE, scale_factor=1.15), run_time=0.7)
        items = []
        for k, (txt, c) in enumerate([("Pourquoi boucler", BLEU), ("Le langage des schémas-blocs", VERT), ("Les règles de réduction", ORANGE),
                                       ("FTBO, FTBF et perturbations", ROUGE), ("Exercice résolu : asservissement de vitesse", JAUNE)]):
            yy = -1.05 - 0.55*k
            items.append(VGroup(carte(k+1, c, -3.4, yy), pos(T(txt, sc=0.76), -2.8, yy)))
        for it, (sid, fr) in zip(items, [("a3", "pourquoi boucler"), ("a3", "le langage"), ("a3", "les règles de réduction"),
                                         ("a3", "la boucle ouverte"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.6), run_time=0.6)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"2.1 -- Boucle ouverte ou boucle fermée", "Pourquoi boucler")
        tbo = pos(T(r"\textbf{Boucle ouverte}", sc=0.75, color=BLEU), -6.3, 2.1)
        self.ecr(self.t("b1"), tbo, rt=0.6)
        y = 1.1
        u = blk(r"\text{tension}", -3.3, y, w=1.9, sc=0.65, col=CRAIE); m = blk(r"\text{moteur + tapis}", 0.3, y, w=2.6, sc=0.65)
        g1 = fl((-5.5, y), (-4.25, y)); g2 = fl((-2.35, y), (-1.0, y)); g3 = fl((1.6, y), (3.4, y))
        lv = T("vitesse", sc=0.65).next_to(g3, RIGHT, buff=0.15); lc = T("consigne", sc=0.65).next_to(g1, LEFT, buff=0.15)
        self.at(self.a("b1", "on peut appliquer"), Create(u[0]), FadeIn(u[1]), Create(g1), FadeIn(lc), run_time=0.7)
        self.play(Create(g2), Create(m[0]), FadeIn(m[1]), Create(g3), FadeIn(lv), run_time=0.8)
        ch = blk(r"\text{charge}", 0.3, y + 1.0, w=1.5, h=0.55, sc=0.6, col=ROUGE)
        fc = fl((0.3, y + 0.72), (0.3, y + 0.38), col=ROUGE)
        av = pos(T(r"simple, mais \textbf{aveugle} : rien ne corrige la vitesse", sc=0.7, color=ROUGE), -6.3, 0.15)
        self.ecr(self.a("b2", "Simple, mais aveugle"), av, rt=1.0)
        self.at(self.a("b2", "si la charge augmente"), Create(ch[0]), FadeIn(ch[1]), Create(fc), run_time=0.6)
        tbf = pos(T(r"\textbf{Boucle fermée}", sc=0.75, color=VERT), -6.3, -0.75)
        self.ecr(self.t("b3"), tbf, rt=0.6)
        y = -1.9
        s = som(-3.6, y, col=VERT); c = blk(r"\text{correcteur}", -1.6, y, w=2.0, sc=0.62); m2 = blk(r"\text{moteur + tapis}", 1.6, y, w=2.4, sc=0.62)
        h1 = fl((-5.4, y), (-3.84, y)); h2 = fl((-3.36, y), (-2.6, y)); h3 = fl((-0.6, y), (0.4, y)); h4 = fl((2.8, y), (4.6, y))
        cap = blk(r"\text{capteur}", 1.6, y - 1.05, w=1.8, h=0.55, sc=0.6, col=VERT)
        r1 = fl((3.7, y), (3.7, y - 1.05), (2.5, y - 1.05), col=VERT); r2 = fl((0.7, y - 1.05), (-3.6, y - 1.05), (-3.6, y - 0.24), col=VERT)
        self.at(self.a("b3", "on mesure la vitesse"), Create(cap[0]), FadeIn(cap[1]), Create(h4), Create(m2[0]), FadeIn(m2[1]), Create(r1), FadeIn(pt(3.7, y)), run_time=0.8)
        self.at(self.a("b3", "on la compare"), Create(s), Create(h1), Create(r2), run_time=0.7)
        self.at(self.a("b3", "on corrige"), Create(h2), Create(c[0]), FadeIn(c[1]), Create(h3), run_time=0.7)
        mc = T(r"mesurer \;--\; comparer \;--\; corriger", sc=0.78, color=JAUNE).move_to([3.3, -0.75, 0])
        self.ecr(self.t("b4"), mc, rt=1.0); self.play(Create(enc(mc, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"2.2 -- La structure d'un système asservi", "Pourquoi boucler")
        y = 0.9
        e = M("e(t)", sc=0.72).move_to([-6.45, y + 0.35, 0])
        ad = blk(r"\text{Adaptateur}", -4.85, y, w=1.8, sc=0.58, col=BLEU)
        s = som(-3.25, y); c = blk(r"\text{Correcteur}", -1.75, y, w=1.75, sc=0.58, col=ORANGE)
        ac = blk(r"\text{Actionneur}", 0.45, y, w=1.75, sc=0.58); pr = blk(r"\text{Processus}", 2.65, y, w=1.75, sc=0.58)
        cp = blk(r"\text{Capteur}", 0.45, y - 1.45, w=1.75, sc=0.58, col=BLEU)
        f0 = fl((-6.75, y), (-5.75, y)); f1 = fl((-3.95, y), (-3.49, y)); f2 = fl((-3.01, y), (-2.63, y)); f3 = fl((-0.87, y), (-0.43, y))
        f4 = fl((1.33, y), (1.77, y)); f5 = fl((3.53, y), (5.0, y))
        ls = M("s(t)", sc=0.72, color=JAUNE).move_to([5.4, y, 0]); lep = M(r"\varepsilon", sc=0.65, color=ORANGE).move_to([-2.82, y + 0.32, 0])
        r1 = fl((4.25, y), (4.25, y - 1.45), (1.33, y - 1.45), col=BLEU); r2 = fl((-0.43, y - 1.45), (-3.25, y - 1.45), (-3.25, y - 0.24), col=BLEU)
        sp = sg("+", -3.6, y + 0.33); sm = sg("-", -3.5, y - 0.45)
        pe = T("perturbation", sc=0.55, color=ROUGE).move_to([2.65, y + 1.35, 0]); fp = fl((2.65, y + 1.12), (2.65, y + 0.4), col=ROUGE)
        self.at(self.t("c1"), FadeIn(e), Create(f0), Create(ad[0]), FadeIn(ad[1]), run_time=0.7)
        self.at(self.t("c2"), Create(f1), Create(s), FadeIn(sp), run_time=0.6)
        self.at(self.a("c2", "consigne adaptée"), Create(f2), FadeIn(lep), run_time=0.4)
        self.at(self.a("c3", "Le correcteur"), Create(c[0]), FadeIn(c[1]), Create(f3), run_time=0.6)
        self.at(self.a("c3", "Puis l'actionneur"), Create(ac[0]), FadeIn(ac[1]), Create(f4), Create(pr[0]), FadeIn(pr[1]), Create(f5), FadeIn(ls), run_time=0.9)
        self.at(self.a("c3", "soumise aux perturbations"), FadeIn(pe), Create(fp), run_time=0.5)
        self.at(self.t("c4"), Create(r1), FadeIn(pt(4.25, y)), Create(cp[0]), FadeIn(cp[1]), Create(r2), FadeIn(sm), run_time=1.0)
        at = pos(T(r"gain de l'adaptateur $=$ gain du capteur", sc=0.72, color=ROUGE), -6.3, -1.35)
        self.ecr(self.a("c5", "l'adaptateur doit avoir"), at, rt=1.0); self.play(Indicate(ad, color=ROUGE), Indicate(cp, color=ROUGE), run_time=0.8)
        a1 = pos(T(r"\textbf{Asservissement} : la consigne varie, la sortie la suit", sc=0.7, color=VERT), -6.3, -2.35)
        a2 = pos(T(r"\textbf{Régulation} : consigne fixe, rejet des perturbations", sc=0.7, color=VERT), -6.3, -3.0)
        self.ecr(self.t("c6"), a1, rt=1.0); self.ecr(self.a("c6", "Régulation"), a2, rt=1.0)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"2.3 -- Le langage des schémas-blocs", "Schémas-blocs")
        y = 1.6
        b = blk(r"H(p)", -4.3, y, w=1.6); f1 = fl((-6.2, y), (-5.1, y)); f2 = fl((-3.5, y), (-2.4, y))
        lx = M("X", sc=0.7).move_to([-5.7, y + 0.3, 0]); ly = M("Y", sc=0.7).move_to([-2.9, y + 0.3, 0])
        rel = M(r"Y = H(p)\,X", sc=0.85, color=JAUNE).move_to([-4.3, y - 0.85, 0])
        self.at(self.a("d1", "Un bloc"), Create(f1), Create(b[0]), FadeIn(b[1]), Create(f2), FadeIn(lx), FadeIn(ly), run_time=0.8)
        self.ecr(self.a("d1", "ce qui sort"), rel, rt=0.8)
        s = som(0.6, y); g1 = fl((-0.8, y), (0.36, y)); g2 = fl((0.84, y), (2.0, y)); g3 = fl((0.6, y - 1.0), (0.6, y - 0.24))
        l1 = M("X_1", sc=0.65).move_to([-0.5, y + 0.3, 0]); l2 = M("X_2", sc=0.65).move_to([0.95, y - 0.85, 0]); le = M(r"\varepsilon", sc=0.7).move_to([1.6, y + 0.3, 0])
        sp = sg("+", 0.2, y + 0.33); sm = sg("-", 0.3, y - 0.42)
        rs = M(r"\varepsilon = X_1 - X_2", sc=0.85, color=JAUNE).move_to([0.6, y - 1.55, 0])
        self.at(self.a("d2", "Un sommateur"), Create(g1), Create(s), Create(g2), Create(g3), FadeIn(l1), FadeIn(l2), FadeIn(le), FadeIn(sp), FadeIn(sm), run_time=0.9)
        self.ecr(self.a("d2", "Ici, epsilon"), rs, rt=0.8)
        p0 = pt(4.6, y); h1 = fl((3.4, y), (6.0, y)); h2 = fl((4.6, y), (4.6, y - 1.1))
        lp = T(r"le même signal", sc=0.6, color=GRIS).move_to([4.9, y - 1.45, 0])
        self.at(self.t("d3"), Create(h1), FadeIn(p0, scale=2), Create(h2), FadeIn(lp), run_time=0.8)
        rg = T(r"Règle d'or : signaux d'une \textbf{même unité} sur un sommateur", sc=0.78, color=ROUGE).move_to([0, -1.9, 0])
        self.ecr(self.t("d4"), rg, rt=1.2); self.play(Create(enc(rg)), run_time=0.4)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"2.4 -- Le moteur à courant continu", "Exemple en direct")
        eqs = [(r"U = RI + LpI + E \;\Rightarrow\; I = \frac{U - E}{R + Lp}", "e2", "Côté électrique"),
               (r"C_m = k\,I", "e3", "Le couple moteur"),
               (r"\Omega = \frac{C_m - C_r}{f + Jp}", "e4", "Côté mécanique"),
               (r"E = k\,\Omega", "e5", "Et la force")]
        for k, (s, ph, fr) in enumerate(eqs):
            m = pos(M(s, sc=0.75, color=BLEU), -6.4 + (0 if k in (0, 2) else 0), 2.05 - 0.78*k if k < 2 else 2.05 - 0.78*k)
            self.ecr(self.a(ph, fr), m, rt=1.0)
            if k == 0:
                y = -1.15
                s1 = som(-5.0, y); b1 = blk(r"\frac{1}{R + Lp}", -3.3, y, w=1.75, h=0.85); fu = fl((-6.6, y), (-5.24, y)); f1 = fl((-4.76, y), (-4.18, y))
                lu = M("U", sc=0.7).move_to([-6.3, y + 0.3, 0]); p1 = sg("+", -5.4, y + 0.33)
                self.play(Create(fu), FadeIn(lu), Create(s1), FadeIn(p1), Create(f1), Create(b1[0]), FadeIn(b1[1]), run_time=0.9)
            if k == 1:
                b2 = blk(r"k", -1.25, y, w=0.9); f2 = fl((-2.42, y), (-1.7, y)); li = M("I", sc=0.65).move_to([-2.06, y + 0.3, 0])
                self.play(Create(f2), FadeIn(li), Create(b2[0]), FadeIn(b2[1]), run_time=0.6)
            if k == 2:
                s2 = som(0.35, y); f3 = fl((-0.8, y), (0.11, y)); lc = M("C_m", sc=0.6).move_to([-0.42, y + 0.32, 0])
                cr = fl((0.35, y + 1.05), (0.35, y + 0.24), col=ROUGE); lcr = M("C_r", sc=0.65, color=ROUGE).move_to([0.75, y + 0.95, 0]); mr = sg("-", 0.62, y + 0.42, col=ROUGE)
                b3 = blk(r"\frac{1}{f + Jp}", 2.0, y, w=1.75, h=0.85); f4 = fl((0.59, y), (1.12, y)); f5 = fl((2.88, y), (4.6, y))
                lo = M(r"\Omega", sc=0.75, color=JAUNE).move_to([4.9, y, 0]); p2 = sg("+", -0.05, y - 0.4)
                self.play(Create(f3), FadeIn(lc), Create(s2), FadeIn(p2), Create(f4), Create(b3[0]), FadeIn(b3[1]), Create(f5), FadeIn(lo), run_time=1.0)
                self.at(self.a("e4", "Le couple résistant"), Create(cr), FadeIn(lcr), FadeIn(mr), run_time=0.6)
            if k == 3:
                b4 = blk(r"k", 0.35, y - 1.35, w=0.9, col=VERT)
                r1 = fl((3.8, y), (3.8, y - 1.35), (0.8, y - 1.35), col=VERT); r2 = fl((-0.1, y - 1.35), (-5.0, y - 1.35), (-5.0, y - 0.24), col=VERT)
                me = sg("-", -5.3, y - 0.45, col=VERT); le = M("E", sc=0.65, color=VERT).move_to([-2.5, y - 1.05, 0])
                self.play(Create(r1), FadeIn(pt(3.8, y, col=VERT)), Create(b4[0]), FadeIn(b4[1]), Create(r2), FadeIn(me), FadeIn(le), run_time=1.0)
        bo = T(r"une boucle interne, naturelle !", sc=0.7, color=VERT).move_to([0.35, -3.35, 0])
        self.ecr(self.a("e5", "Une boucle apparaît"), bo, rt=0.8)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"2.5 -- Réduire un schéma-blocs", "Schémas-blocs")
        se = pos(T(r"\textbf{Série} : \; $H = H_1 \, H_2$", sc=0.78, color=BLEU), -6.3, 2.1)
        pa = pos(T(r"\textbf{Parallèle} : \; $H = H_1 \pm H_2$", sc=0.78, color=BLEU), -6.3, 1.35)
        self.ecr(self.a("f1", "Des blocs en série"), se, rt=0.9); self.ecr(self.t("f2"), pa, rt=0.9)
        y = 0.05
        s = som(-4.6, y); a = blk("A", -2.9, y, w=1.1); b = blk("B", -2.9, y - 1.05, w=1.1, col=BLEU)
        f1 = fl((-6.2, y), (-4.84, y)); f2 = fl((-4.36, y), (-3.45, y)); f3 = fl((-2.35, y), (-0.6, y))
        r1 = fl((-1.25, y), (-1.25, y - 1.05), (-2.35, y - 1.05), col=BLEU); r2 = fl((-3.45, y - 1.05), (-4.6, y - 1.05), (-4.6, y - 0.24), col=BLEU)
        le = M("E", sc=0.7).move_to([-5.9, y + 0.3, 0]); ls = M("S", sc=0.7).move_to([-0.35, y, 0]); lep = M(r"\varepsilon", sc=0.65).move_to([-3.95, y + 0.3, 0])
        sp = sg("+", -5.0, y + 0.33); sm = sg("-", -4.9, y - 0.45)
        self.at(self.a("f3", "Et la boucle"), Create(f1), FadeIn(le), Create(s), FadeIn(sp), Create(f2), FadeIn(lep), Create(a[0]), FadeIn(a[1]), Create(f3), FadeIn(ls), run_time=1.0)
        self.play(Create(r1), FadeIn(pt(-1.25, y)), Create(b[0]), FadeIn(b[1]), Create(r2), FadeIn(sm), run_time=0.8)
        e1 = pos(M(r"S = A\,\varepsilon, \qquad \varepsilon = E - B\,S", sc=0.85), 0.6, 0.35)
        self.ecr(self.a("f3", "On a S égale"), e1, rt=1.1)
        e2 = pos(M(r"S\,(1 + AB) = A\,E", sc=0.85), 0.6, -0.55)
        self.ecr(self.t("f4"), e2, rt=1.0)
        fo = M(r"\frac{S}{E} = \frac{A}{1 + A\,B}", sc=1.15, color=JAUNE).move_to([-1.5, -2.35, 0])
        self.ecr(self.a("f5", "la formule de la boucle"), fo, rt=1.0); self.play(Create(enc(fo, col=JAUNE)), run_time=0.4)
        dp = VGroup(T(r"boucles emmêlées :", sc=0.64, color=GRIS), T(r"déplacer, en compensant par $H$ ou $1/H$", sc=0.64, color=GRIS)).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        pos(dp, 0.6, -1.95)
        self.ecr(self.t("f6"), dp, rt=1.2)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"2.6 -- La fonction de transfert du moteur", "Exemple en direct")
        a = pos(M(r"A = \frac{k}{(R + Lp)(f + Jp)}, \qquad B = k", sc=0.9), -6.3, 1.9)
        self.ecr(self.a("g1", "La chaîne directe"), a, rt=1.3)
        h = pos(M(r"\frac{\Omega}{U} = \frac{A}{1 + AB} = \frac{k}{(R + Lp)(f + Jp) + k^2}", sc=0.95, color=JAUNE), -6.3, 0.55)
        self.ecr(self.t("g2"), h, rt=1.4)
        d2 = T(r"$\Rightarrow$ un deuxième ordre", sc=0.72, color=VERT).next_to(h, DOWN, buff=0.25).align_to(h, LEFT)
        self.ecr(self.a("g2", "Un deuxième ordre"), d2, rt=0.7)
        ng = pos(T(r"$L \approx 0$, \; $f \approx 0$ :", sc=0.75, color=GRIS), -6.3, -1.25)
        s1 = pos(M(r"\frac{\Omega}{U} = \frac{k}{RJp + k^2}", sc=0.95), -3.5, -1.25)
        self.ecr(self.a("g3", "on néglige"), ng, rt=0.8); self.ecr(self.a("g3", "Il reste"), s1, rt=1.0)
        fc = M(r"\frac{\Omega}{U} = \frac{1/k}{1 + \tau_m\,p}, \qquad \tau_m = \frac{RJ}{k^2}", sc=1.0, color=JAUNE).move_to([0, -2.75, 0])
        self.ecr(self.t("g4"), fc, rt=1.3); self.play(Create(enc(fc, col=JAUNE)), run_time=0.4)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"2.7 -- Boucle ouverte et boucle fermée", "FTBO, FTBF")
        bo = pos(T(r"\textbf{FTBO} : produit de tous les blocs de la boucle", sc=0.75, color=BLEU), -6.3, 2.05)
        bom = pos(M(r"H_{BO}(p) = A(p)\,B(p)", sc=0.9, color=BLEU), -5.6, 1.35)
        self.ecr(self.a("h2", "La F T B O"), bo, rt=1.0); self.ecr(self.a("h2", "le produit"), bom, rt=0.8)
        bf = pos(T(r"\textbf{FTBF} : sortie sur consigne", sc=0.75, color=ORANGE), -6.3, 0.5)
        bfm = pos(M(r"H_{BF}(p) = \frac{S(p)}{E(p)}", sc=0.9, color=ORANGE), -5.6, -0.3)
        self.ecr(self.t("h3"), bf, rt=0.8); self.ecr(self.a("h3", "sortie sur consigne"), bfm, rt=0.8)
        y = 1.0
        s = som(2.2, y); c = blk(r"K_a\,C\,G", 3.9, y, w=1.6); f1 = fl((0.9, y), (1.96, y)); f2 = fl((2.44, y), (3.1, y)); f3 = fl((4.7, y), (6.3, y))
        r1 = fl((5.6, y), (5.6, y - 1.0), (2.2, y - 1.0), (2.2, y - 0.24), col=VERT)
        l1 = T(r"retour unitaire", sc=0.6, color=VERT).move_to([3.9, y - 1.3, 0]); sm = sg("-", 1.9, y - 0.45)
        self.at(self.a("h4", "on le fait passer"), Create(f1), Create(s), Create(f2), Create(c[0]), FadeIn(c[1]), Create(f3), run_time=0.8)
        self.at(self.a("h4", "Le retour devient unitaire"), Create(r1), FadeIn(pt(5.6, y)), FadeIn(l1), FadeIn(sm), run_time=0.8)
        fo = M(r"H_{BF}(p) = \frac{H_{BO}(p)}{1 + H_{BO}(p)}", sc=1.15, color=JAUNE).move_to([0, -2.1, 0])
        self.ecr(self.t("h5"), fo, rt=1.2); self.play(Create(enc(fo, col=JAUNE)), run_time=0.4)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"2.8 -- Les perturbations", "FTBO, FTBF")
        y = 1.3
        s = som(-4.4, y); c = blk("C", -3.0, y, w=0.9); g1 = blk("G_1", -1.4, y, w=0.9); s2 = som(0.1, y, col=ROUGE); g2 = blk("G_2", 1.6, y, w=0.9)
        fs = [fl((-6.0, y), (-4.64, y)), fl((-4.16, y), (-3.45, y)), fl((-2.55, y), (-1.85, y)), fl((-0.95, y), (-0.14, y)), fl((0.34, y), (1.15, y)), fl((2.05, y), (3.6, y))]
        d = fl((0.1, y + 1.0), (0.1, y + 0.24), col=ROUGE); ld = M("D", sc=0.7, color=ROUGE).move_to([0.45, y + 0.9, 0])
        r = fl((2.9, y), (2.9, y - 0.95), (-4.4, y - 0.95), (-4.4, y - 0.24), col=BLEU)
        le = M("E", sc=0.7).move_to([-5.7, y + 0.3, 0]); ls = M("S", sc=0.7, color=JAUNE).move_to([3.9, y, 0])
        self.at(self.t("i1"), *[Create(f) for f in fs], Create(s), Create(c[0]), FadeIn(c[1]), Create(g1[0]), FadeIn(g1[1]), Create(s2), Create(g2[0]), FadeIn(g2[1]),
                Create(r), FadeIn(pt(2.9, y)), FadeIn(le), FadeIn(ls), run_time=1.2)
        self.play(Create(d), FadeIn(ld), run_time=0.5)
        su = M(r"S = H_E\,E + H_D\,D", sc=1.0, color=JAUNE).move_to([0, -0.55, 0])
        self.ecr(self.t("i2"), su, rt=1.0)
        he = pos(M(r"H_E = \frac{C\,G_1G_2}{1 + C\,G_1G_2}", sc=0.85, color=BLEU), -6.3, -1.85)
        hd = pos(M(r"H_D = \frac{G_2}{1 + C\,G_1G_2}", sc=0.85, color=ROUGE), 0.6, -1.85)
        self.ecr(self.a("i2", "On calcule H E"), he, rt=1.0); self.ecr(self.t("i3"), hd, rt=1.0)
        md = T(r"même dénominateur $1 + H_{BO}$ : mêmes pôles !", sc=0.75, color=VERT).move_to([0, -3.15, 0])
        self.ecr(self.t("i4"), md, rt=1.0)
        self.play(Indicate(he[0][-9:], color=VERT), Indicate(hd[0][-9:], color=VERT), run_time=0.8)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"2.9 -- À vous de jouer", "Exercice")
        y = 1.65
        s1 = som(-5.0, y); s2 = som(-3.5, y); g1 = blk(r"\frac{4}{p}", -2.1, y, w=1.0, h=0.8); g2 = blk(r"\frac{1}{1 + 0{,}5p}", 0.4, y, w=1.9, h=0.8)
        fs = [fl((-6.4, y), (-5.24, y)), fl((-4.76, y), (-3.74, y)), fl((-3.26, y), (-2.6, y)), fl((-1.6, y), (-0.55, y)), fl((1.35, y), (3.0, y))]
        ri = fl((-1.05, y), (-1.05, y - 0.75), (-3.5, y - 0.75), (-3.5, y - 0.24), col=BLEU)
        re = fl((2.2, y), (2.2, y - 1.25), (-5.0, y - 1.25), (-5.0, y - 0.24), col=VERT)
        self.at(self.t("j1"), *[Create(f) for f in fs], Create(s1), Create(s2), Create(g1[0]), FadeIn(g1[1]), Create(g2[0]), FadeIn(g2[1]), run_time=1.0)
        self.at(self.a("j1", "retour unitaire"), Create(ri), FadeIn(pt(-1.05, y)), run_time=0.6)
        self.at(self.a("j1", "Le tout bouclé"), Create(re), FadeIn(pt(2.2, y)), run_time=0.6)
        pa, arc = chrono(4.6, y)
        self.at(self.a("j1", "Mettez sur pause"), FadeIn(pa), Create(arc), run_time=0.5)
        self.play(Uncreate(arc), run_time=2.6); self.play(FadeOut(pa), run_time=0.2)
        i = pos(M(r"\text{intérieur} : \frac{4/p}{1 + 4/p} = \frac{4}{p + 4} = \frac{1}{1 + 0{,}25p}", sc=0.8, color=BLEU), -6.3, -0.4)
        self.ecr(self.a("j2", "On commence par l'intérieur"), i, rt=1.4)
        a = pos(M(r"A = \frac{1}{(1 + 0{,}25p)(1 + 0{,}5p)}", sc=0.8), -6.3, -1.45)
        self.ecr(self.t("j3"), a, rt=1.1)
        b = pos(M(r"\frac{A}{1 + A} = \frac{1}{(1 + 0{,}25p)(1 + 0{,}5p) + 1}", sc=0.8), -0.4, -1.45)
        self.ecr(self.t("j4"), b, rt=1.2)
        r = M(r"H_{BF} = \frac{0{,}5}{1 + 0{,}375\,p + 0{,}0625\,p^2}", sc=0.95, color=JAUNE).move_to([0, -2.75, 0])
        self.ecr(self.t("j5"), r, rt=1.3); self.play(Create(enc(r, col=JAUNE)), run_time=0.4)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"2.10 -- Ce que le bouclage apporte", "FTBO, FTBF")
        h = pos(M(r"G(p) = \frac{K}{1 + \tau p}, \qquad C = K_c, \quad \text{retour unitaire}", sc=0.85), -6.3, 2.0)
        self.ecr(self.t("k1"), h, rt=1.2)
        bf = pos(M(r"H_{BF} = \frac{K'}{1 + \tau' p}, \qquad \tau' = \frac{\tau}{1 + K_cK}, \quad K' = \frac{K_cK}{1 + K_cK}", sc=0.85, color=JAUNE), -6.3, 0.85)
        self.ecr(self.a("k2", "La F T B F"), bf, rt=1.5)
        ax = axes(3.4, -1.4, 5.2, 2.9, [0, 5, 1], [0, 1.15, 1])
        lt = M("t", sc=0.65).next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        c0 = ax.plot(lambda t: 1 - np.exp(-t), x_range=[0, 4.9, 0.02], color=GRIS, stroke_width=4)
        c1 = ax.plot(lambda t: 0.9*(1 - np.exp(-10*t)), x_range=[0, 4.9, 0.01], color=VERT, stroke_width=4)
        l0 = T("sans boucle", sc=0.58, color=GRIS).move_to(ax.c2p(3.6, 0.72)); l1 = T("bouclé", sc=0.58, color=VERT).move_to(ax.c2p(1.0, 1.05))
        n1 = pos(T(r"$K_cK = 9$ : \; $\tau' = \tau/10$, \; $K' = 0{,}9$", sc=0.75, color=VERT), -6.3, -0.55)
        self.ecr(self.t("k3"), n1, rt=1.1)
        self.at(self.a("k3", "dix fois plus rapide"), Create(ax), FadeIn(lt), Create(c0), FadeIn(l0), run_time=0.8); self.play(Create(c1), FadeIn(l1), run_time=0.7)
        rb = pos(T(r"processus $\pm 20\,\%$ \;$\Rightarrow$\; sortie $\pm 2\,\%$", sc=0.75, color=JAUNE), -6.3, -1.75)
        rb2 = pos(T(r"le bouclage rend \textbf{robuste}", sc=0.75, color=JAUNE), -6.3, -2.5)
        self.ecr(self.t("k4"), rb, rt=1.1); self.ecr(self.a("k4", "Le bouclage rend"), rb2, rt=0.8)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"À retenir", "Bilan")
        pts = [("l1", r"Mesurer, comparer, corriger ; adaptateur $=$ gain du capteur", BLEU),
               ("l2", r"Série : $\times$ \quad Parallèle : $+$ \quad Boucle : $\dfrac{A}{1 + AB}$", VERT),
               ("l3", r"FTBO $=$ produit de la boucle ; \; $H_{BF} = \dfrac{H_{BO}}{1 + H_{BO}}$ à retour unitaire", ORANGE),
               ("l4", r"Consigne et perturbation : superposition, même dénominateur", JAUNE)]
        for k, (ph, txt, c) in enumerate(pts):
            y = 1.8 - 1.3*k
            ca = carte(k+1, c, -5.9, y); tx = pos(T(txt, sc=0.72), -5.35, y)
            self.at(self.t(ph), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- l'énoncé", "Application")
        y = 1.35
        ad = blk(r"0{,}1", -4.6, y, w=1.0, col=BLEU); s = som(-3.3, y); c = blk(r"K_c = 20", -1.7, y, w=1.6, col=ORANGE)
        m = blk(r"\frac{2}{1 + 0{,}5p}", 0.6, y, w=1.9, h=0.85); cp = blk(r"0{,}1", 0.6, y - 1.3, w=1.0, col=BLEU)
        fs = [fl((-6.5, y), (-5.1, y)), fl((-4.1, y), (-3.54, y)), fl((-3.06, y), (-2.5, y)), fl((-0.9, y), (-0.35, y)), fl((1.55, y), (3.6, y))]
        r = [fl((2.6, y), (2.6, y - 1.3), (1.1, y - 1.3), col=BLEU), fl((0.1, y - 1.3), (-3.3, y - 1.3), (-3.3, y - 0.24), col=BLEU)]
        lc = M(r"\Omega_c", sc=0.7).move_to([-6.2, y + 0.32, 0]); lo = M(r"\Omega", sc=0.75, color=JAUNE).move_to([3.9, y, 0])
        self.at(self.a("m1", "Un asservissement de vitesse"), *[Create(f) for f in fs], Create(m[0]), FadeIn(m[1]), FadeIn(lc), FadeIn(lo), run_time=1.0)
        self.at(self.a("m2", "Le capteur et l'adaptateur"), Create(ad[0]), FadeIn(ad[1]), Create(cp[0]), FadeIn(cp[1]), *[Create(x) for x in r], FadeIn(pt(2.6, y)), Create(s), run_time=1.0)
        self.at(self.a("m2", "Le correcteur"), Create(c[0]), FadeIn(c[1]), run_time=0.5)
        qs = [r"FTBF $\Omega/\Omega_c$ ?", r"vitesse finale pour $\Omega_c = 100$ rad/s ?", r"temps de réponse à 5\,\% ?"]
        for k, (q, fr) in enumerate(zip(qs, ["quelle F T B F", "Quelle vitesse finale", "quel temps de réponse"])):
            m_ = pos(T(q, sc=0.72, color=ROUGE), -5.4, -1.0 - 0.6*k)
            self.at(self.a("m3", fr), Create(carte(k+1, ROUGE, -6.0, -1.0 - 0.6*k)), Ecrire(m_, rt=0.8), run_time=0.8)
        rf = pos(T(r"Réfléchissons : adaptateur $=$ capteur $\Rightarrow$ retour unitaire", sc=0.7, color=BLEU), -6.3, -3.0)
        self.ecr(self.t("m4"), rf, rt=1.3)
        self.fin()

class S13(Cours):
    sid = "S13"
    def construct(self):
        self.entete(r"Exercice résolu -- la solution", "Application")
        def etape(k, c, y, m, ph, fr, rt=1.0):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(self.a(ph, fr), Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        etape(1, BLEU, 2.15, M(r"H_{BO} = 0{,}1 \times 20 \times \frac{2}{1 + 0{,}5p} = \frac{4}{1 + 0{,}5p}", sc=0.8), "n1", "Étape un", 1.3)
        etape(2, VERT, 0.95, M(r"H_{BF} = \frac{4}{1 + 0{,}5p + 4} = \frac{4}{5 + 0{,}5p}", sc=0.8), "n2", "Étape deux", 1.2)
        fc = pos(M(r"H_{BF} = \frac{0{,}8}{1 + 0{,}1\,p} \qquad K' = 0{,}8, \;\; \tau' = 0{,}1\ \mathrm{s}", sc=0.8, color=JAUNE), -5.85, -0.1)
        self.ecr(self.t("n3"), fc, rt=1.3); self.play(Create(enc(fc, col=JAUNE, buff=0.12)), run_time=0.4)
        etape(3, ORANGE, -1.25, M(r"\Omega_\infty = 0{,}8 \times 100 = 80\ \mathrm{rad/s}", sc=0.8), "n4", "Étape trois")
        ax = axes(4.1, 0.9, 4.0, 2.8, [0, 1.6, 1], [0, 110, 50])
        lt = M("t", sc=0.65).next_to(ax.x_axis.get_end(), DOWN, buff=0.1); lo = M(r"\Omega", sc=0.65).next_to(ax.y_axis.get_end(), LEFT, buff=0.1)
        cc = DashedLine(ax.c2p(0, 100), ax.c2p(1.6, 100), color=GRIS, stroke_width=3); l100 = M("100", sc=0.55, color=GRIS).next_to(ax.c2p(0, 100), LEFT, buff=0.1)
        cb = ax.plot(lambda t: 80*(1 - np.exp(-t/0.1)), x_range=[0, 1.55, 0.005], color=VERT, stroke_width=4)
        l80 = M("80", sc=0.55, color=VERT).next_to(ax.c2p(0, 80), LEFT, buff=0.1)
        self.at(self.a("n4", "Gain statique fois consigne"), Create(ax), FadeIn(lt), FadeIn(lo), Create(cc), FadeIn(l100), run_time=0.6)
        self.play(Create(cb), FadeIn(l80), run_time=0.8)
        ec = pos(T(r"écart de $20\,\%$ : pas précis !", sc=0.7, color=ROUGE), -5.85, -1.95)
        br = DoubleArrow(ax.c2p(1.35, 80), ax.c2p(1.35, 100), color=ROUGE, buff=0, stroke_width=3, tip_length=0.12)
        self.at(self.t("n5"), Ecrire(ec, rt=0.8), GrowFromCenter(br), run_time=0.8)
        etape(4, ROUGE, -2.75, M(r"t_{r5\%} = 3\tau' = 0{,}3\ \mathrm{s} \quad (1{,}5\ \mathrm{s}\ \text{sans boucle})", sc=0.8), "n6", "Étape quatre", 1.2)
        bi = VGroup(T(r"Bilan : $5$ fois plus rapide,", sc=0.66, color=VERT), T(r"mais il faudra un \textbf{intégrateur}", sc=0.66, color=VERT)).arrange(DOWN, buff=0.15).move_to([4.1, -1.2, 0])
        self.ecr(self.t("n7"), bi, rt=1.2)
        nx = T(r"Prochain chapitre : le premier ordre", sc=0.62, color=GRIS).move_to([4.1, -2.25, 0])
        self.at(self.t("n8"), FadeIn(nx), run_time=0.6)
        self.fin()
