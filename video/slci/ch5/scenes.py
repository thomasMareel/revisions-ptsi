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
def cadre(x, y, w, h, l0, l1, g0, g1):
    """Repère de Bode : abscisse = log10(omega) de l0 à l1, ordonnée de g0 à g1 ; cadre gris et décades."""
    ax = Axes(x_range=[l0, l1, 1], y_range=[g0, g1, 1], x_length=w, y_length=h, tips=False,
              axis_config={"stroke_opacity": 0, "include_ticks": False}).move_to([x, y, 0])
    fr = Rectangle(width=w, height=h, color=GRIS, stroke_width=2).move_to([x, y, 0])
    dec = VGroup(*[DashedLine(ax.c2p(k, g0), ax.c2p(k, g1), color=GRIS, stroke_width=1, dash_length=0.06) for k in range(int(np.ceil(l0)), int(np.floor(l1)) + 1)])
    return ax, VGroup(fr, dec)
def lig(ax, pts, col=ORANGE, sw=4):
    return VMobject(color=col, stroke_width=sw).set_points_as_corners([ax.c2p(a, b) for a, b in pts])
def crb(ax, f, l0, l1, col=BLEU, sw=5, gmin=None, gmax=None, n=200):
    u = np.linspace(l0, l1, n); v = np.array([f(10**x) for x in u])
    if gmin is not None: v = np.clip(v, gmin, gmax)
    return VMobject(color=col, stroke_width=sw).set_points_smoothly([ax.c2p(a, b) for a, b in zip(u, v)])
def dB(z): return 20*np.log10(np.abs(z))
def ph(z): return np.degrees(np.angle(z))

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PTSI", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Automatique -- Chapitre 5}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Réponse fréquentielle et diagrammes de Bode", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        ax, fr = cadre(3.7, -1.0, 4.4, 2.6, -1, 2, -42, 24)
        a = lig(ax, [(-1, 20), (0, 20), (1, 0), (2, -40)]); c = crb(ax, lambda w: dB(10/((1 + 1j*w)*(1 + 0.1j*w))), -1, 2)
        self.at(self.a("a2", "le diagramme de Bode"), Create(fr), Create(a), run_time=0.8); self.play(Create(c), run_time=1.0)
        items = []
        for k, (txt, col) in enumerate([("La réponse harmonique", BLEU), ("Les décibels", VERT), ("Les briques élémentaires", ORANGE),
                                         ("Le tracé asymptotique", ROUGE), ("Lire un Bode", BLEU), ("Exercice résolu : identifier un axe", JAUNE)]):
            yy = 0.75 - 0.6*k
            items.append(VGroup(carte(k+1, col, -6.2, yy), pos(T(txt, sc=0.74), -5.65, yy)))
        for it, (sid, fr_) in zip(items, [("a3", "la réponse harmonique"), ("a3", "les décibels"), ("a3", "les briques"),
                                          ("a3", "le tracé asymptotique"), ("a3", "la lecture"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr_)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"5.1 -- La réponse harmonique", "Réponse fréquentielle")
        ax = axes(0, 0.75, 12.0, 3.0, [0, 12, 1], [-1.2, 1.2, 1], col=GRIS)
        lt = M("t", sc=0.7, color=GRIS).next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        e = ax.plot(lambda t: np.sin(1.6*t), x_range=[0, 11.8, 0.02], color=GRIS, stroke_width=4)
        s = ax.plot(lambda t: 0.55*np.sin(1.6*t - 1.0) if t > 0 else 0, x_range=[0, 11.8, 0.02], color=BLEU, stroke_width=5)
        le = M("e(t)", sc=0.7, color=GRIS).move_to(ax.c2p(0.5, 1.15)); ls = M("s(t)", sc=0.7, color=BLEU).move_to(ax.c2p(2.0, -0.85))
        self.at(self.t("b1"), Create(ax), FadeIn(lt), Create(e), FadeIn(le), run_time=1.2)
        self.at(self.a("b1", "la sortie est une sinusoïde"), Create(s), FadeIn(ls), run_time=1.4)
        t0 = (np.pi/2)/1.6 + 2*np.pi/1.6; t1 = t0 + 1.0/1.6
        am = DoubleArrow(ax.c2p(t0, 0), ax.c2p(t0, 1), color=GRIS, buff=0, stroke_width=3, tip_length=0.12); lam = M("E_m", sc=0.6, color=GRIS).next_to(am, LEFT, buff=0.08)
        sm = DoubleArrow(ax.c2p(t1, 0), ax.c2p(t1, 0.55), color=BLEU, buff=0, stroke_width=3, tip_length=0.12); lsm = M("S_m", sc=0.6, color=BLEU).next_to(sm, RIGHT, buff=0.08)
        dt = DoubleArrow(ax.c2p(t0, -1.05), ax.c2p(t1, -1.05), color=ORANGE, buff=0, stroke_width=3, tip_length=0.12); ldt = T("décalage", sc=0.55, color=ORANGE).next_to(dt, DOWN, buff=0.05)
        self.at(self.a("b2", "l'amplitude"), GrowFromCenter(am), FadeIn(lam), GrowFromCenter(sm), FadeIn(lsm), run_time=0.6)
        self.at(self.a("b2", "le décalage"), GrowFromCenter(dt), FadeIn(ldt), run_time=0.5)
        f = M(r"\frac{S_m}{E_m} = |H(j\omega)|, \qquad \varphi = \arg H(j\omega)", sc=1.0, color=JAUNE).move_to([0, -1.65, 0])
        self.ecr(self.t("b3"), f, rt=1.3); self.play(Create(enc(f, col=JAUNE)), run_time=0.4)
        pj = T(r"en pratique : \; $p \;\longrightarrow\; j\omega$ \; dans $H(p)$", sc=0.8, color=VERT).move_to([0, -2.95, 0])
        self.ecr(self.t("b4"), pj, rt=1.0)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"5.2 -- Décibels et échelle logarithmique", "Réponse fréquentielle")
        g = pos(M(r"G_{dB}(\omega) = 20\log|H(j\omega)|, \qquad \varphi(\omega) = \arg H(j\omega)", sc=0.9, color=JAUNE), -6.3, 2.05)
        self.ecr(self.t("c1"), g, rt=1.4)
        ln = NumberLine(x_range=[-1, 2, 1], length=6.0, color=GRIS, include_ticks=True, tick_size=0.1).move_to([-3.2, 1.0, 0])
        lb = VGroup(*[M(t, sc=0.6, color=GRIS).next_to(ln.n2p(k), DOWN, buff=0.15) for k, t in zip(range(-1, 3), ["0{,}1", "1", "10", "100"])])
        ld = T("une décade", sc=0.6, color=ORANGE).next_to(Line(ln.n2p(0), ln.n2p(1)), UP, buff=0.2)
        br = Line(ln.n2p(0) + 0.18*UP, ln.n2p(1) + 0.18*UP, color=ORANGE, stroke_width=4)
        self.at(self.t("c2"), Create(ln), FadeIn(lb), run_time=0.7)
        self.at(self.a("c2", "chaque décade"), Create(br), FadeIn(ld), run_time=0.5)
        so = pos(M(r"20\log|H_1H_2| = 20\log|H_1| + 20\log|H_2|", sc=0.85, color=BLEU), -6.3, -0.35)
        self.ecr(self.a("c3", "Parce qu'il change"), so, rt=1.3)
        sm = pos(T(r"Bode d'une chaîne $=$ \textbf{somme} des Bode", sc=0.75, color=BLEU), -6.3, -1.15)
        self.ecr(self.a("c3", "Le Bode d'une chaîne"), sm, rt=0.9)
        tb = VGroup(*[M(s, sc=0.82, color=VERT) for s in [r"\times 10 \;\to\; +20\ \mathrm{dB}", r"\times 2 \;\to\; +6\ \mathrm{dB}", r"\times\sqrt{2} \;\to\; +3\ \mathrm{dB}"]]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([3.7, 0.7, 0])
        for m, fr in zip(tb, ["un facteur dix", "Un facteur deux", "Et racine de deux"]):
            self.ecr(self.a("c4", fr), m, rt=0.6)
        ax, frm = cadre(-2.2, -2.75, 5.0, 1.15, -1, 2, -45, 5)
        pe = lig(ax, [(-1, 0), (0, 0), (2, -40)], col=ORANGE); lp = T(r"$-20$ dB/déc : $\div 10$ par décade", sc=0.66, color=ORANGE).move_to([3.3, -2.75, 0])
        self.at(self.t("c5"), Create(frm), Create(pe), run_time=0.8); self.ecr(self.a("c5", "L'amplitude est divisée"), lp, rt=1.0)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"5.3 -- Les briques élémentaires", "Réponse fréquentielle")
        cel = [("Gain pur", r"K", lambda w: 12 + 0*w, [(-1, 12), (2, 12)], r"\varphi = 0", "d1", "Le gain pur"),
               ("Intégrateur", r"\frac{K}{p}", lambda w: dB(3/(1j*w)), [(-1, 29.5), (2, -30.5)], r"\varphi = -90^\circ", "d2", "L'intégrateur"),
               ("Premier ordre", r"\frac{1}{1 + \tau p}", lambda w: dB(1/(1 + 1j*w)), [(-1, 0), (0, 0), (2, -40)], r"0 \to -90^\circ", "d3", "Le premier ordre"),
               ("Zéro", r"1 + \tau p", lambda w: dB(1 + 1j*w), [(-1, 0), (0, 0), (2, 40)], r"0 \to +90^\circ", "d3", "Un zéro"),
               ("2\\textsuperscript{e} ordre", r"\frac{1}{1 + \frac{2\xi}{\omega_0}p + \frac{p^2}{\omega_0^2}}", lambda w: dB(1/(1 - w*w/10 + 2j*0.15*w/np.sqrt(10))), [(-1, 0), (0.5, 0), (2, -60)], r"0 \to -180^\circ", "d4", "Le deuxième ordre"),
               ("Retard pur", r"e^{-Tp}", lambda w: 0*w, [(-1, 0), (2, 0)], r"\varphi = -\omega T", "d5", "Et le retard pur")]
        for k, (nom, ftx, f, asy, phs, ph_, fr) in enumerate(cel):
            cx = -4.4 + 4.4*(k % 3); cy = 1.25 if k < 3 else -1.9
            nm = T(r"\textbf{" + nom + "}", sc=0.66, color=JAUNE); nm.move_to([cx - 1.7 + nm.width/2, cy + 1.05, 0])
            fm = M(ftx, sc=0.6 if k != 4 else 0.52, color=BLEU); fm.move_to([cx + 1.7 - fm.width/2, cy + 1.05, 0])
            ax, frm = cadre(cx, cy - 0.15, 3.4, 1.45, -1, 2, -45, 45)
            zl = DashedLine(ax.c2p(-1, 0), ax.c2p(2, 0), color=GRIS, stroke_width=1.5)
            a = lig(ax, asy, col=ORANGE, sw=3); c = crb(ax, f, -1, 2, col=BLEU, sw=4, gmin=-45, gmax=45)
            pl = M(phs, sc=0.58, color=VERT).move_to([cx, cy - 1.15, 0])
            self.at(self.a(ph_, fr), Ecrire(nm, rt=0.5), FadeIn(fm), Create(frm), Create(zl), run_time=0.6)
            self.play(Create(a), Create(c), FadeIn(pl), run_time=0.8)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"5.4 -- La démarche du tracé asymptotique", "Tracer un Bode")
        pts = [("e1", r"Forme canonique ; cassures rangées par ordre croissant", BLEU),
               ("e2", r"Droite de départ : pente $-20\,\alpha$ dB/déc, passant par $20\log K$ en $\omega = 1$", VERT),
               ("e3", r"À chaque cassure : $-20$ (pôle), $+20$ (zéro), $-40$ (deuxième ordre)", ORANGE),
               ("e4", r"Phase : somme des arctangentes, aux pulsations utiles", ROUGE)]
        for k, (ph_, txt, c) in enumerate(pts):
            y = 1.8 - 1.3*k
            ca = carte(k+1, c, -5.9, y); tx = pos(T(txt, sc=0.74), -5.35, y)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.1), run_time=0.9)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"5.5 -- Exemple : deux premiers ordres", "Exemple en direct")
        h = pos(M(r"H(p) = \frac{10}{(1 + p)(1 + 0{,}1p)}", sc=0.9, color=JAUNE), -6.3, 2.0)
        self.ecr(self.t("f1"), h, rt=1.0)
        i = pos(T(r"$20\log 10 = 20$ dB \quad cassures : $1$ et $10$ rad/s", sc=0.7, color=BLEU), 0.4, 2.0)
        self.ecr(self.t("f2"), i, rt=1.1)
        ag, fg = cadre(0.2, 0.15, 10.4, 2.4, -1, 2, -44, 26)
        ap, fp = cadre(0.2, -2.45, 10.4, 1.7, -1, 2, -190, 10)
        lab = VGroup(*[M(t, sc=0.55, color=GRIS).next_to(ap.c2p(k, -190), DOWN, buff=0.1) for k, t in zip(range(-1, 3), ["0{,}1", "1", "10", "100"])])
        gl = VGroup(*[M(t, sc=0.55, color=GRIS).next_to(ag.c2p(-1, v), LEFT, buff=0.1) for v, t in [(20, "20"), (0, "0"), (-20, "-20"), (-40, "-40")]])
        pl = VGroup(*[M(t, sc=0.55, color=GRIS).next_to(ap.c2p(-1, v), LEFT, buff=0.1) for v, t in [(0, r"0^\circ"), (-90, r"-90^\circ"), (-180, r"-180^\circ")]])
        self.at(self.a("f2", "Deux cassures"), Create(fg), Create(fp), FadeIn(lab), FadeIn(gl), FadeIn(pl), run_time=0.8)
        s1 = lig(ag, [(-1, 20), (0, 20)]); s2 = lig(ag, [(0, 20), (1, 0)]); s3 = lig(ag, [(1, 0), (2, -40)])
        l2 = T(r"$-20$", sc=0.6, color=ORANGE).move_to(ag.c2p(0.62, 16)); l3 = T(r"$-40$", sc=0.6, color=ORANGE).move_to(ag.c2p(1.6, -12))
        self.at(self.a("f3", "un plateau"), Create(s1), run_time=0.6)
        self.at(self.a("f3", "De un à dix"), Create(s2), FadeIn(l2), run_time=0.8)
        self.at(self.t("f4"), Create(s3), FadeIn(l3), run_time=0.7)
        H = lambda w: 10/((1 + 1j*w)*(1 + 0.1j*w))
        cg = crb(ag, lambda w: dB(H(w)), -1, 2)
        self.at(self.a("f4", "Et voici la vraie courbe"), Create(cg), run_time=1.2)
        cp = crb(ap, lambda w: -np.degrees(np.arctan(w)) - np.degrees(np.arctan(0.1*w)), -1, 2)
        d = Dot(ap.c2p(0.5, -90), color=JAUNE, radius=0.09); ld = M(r"-90^\circ \text{ en } 3{,}16", sc=0.6, color=JAUNE).next_to(d, UR, buff=0.1)
        self.at(self.t("f5"), Create(cp), run_time=1.2)
        self.at(self.a("f5", "elle vaut exactement"), FadeIn(d, scale=2), FadeIn(ld), run_time=0.6)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"5.6 -- Exemple : un intégrateur et un zéro", "Exemple en direct")
        h = pos(M(r"H(p) = \frac{100\,(1 + 0{,}5p)}{p\,(1 + 5p)(1 + 0{,}02p)}", sc=0.9, color=JAUNE), -6.3, 2.0)
        self.ecr(self.t("g1"), h, rt=1.3)
        i = pos(T(r"classe $1$, $K = 100$ \; ; \; cassures $0{,}2$ (pôle), $2$ (zéro), $50$ (pôle)", sc=0.66, color=BLEU), -6.3, 1.1)
        self.ecr(self.t("g2"), i, rt=1.3)
        ag, fg = cadre(0.0, -0.8, 11.6, 3.3, np.log10(0.02), np.log10(500), -60, 80)
        lab = VGroup(*[M(t, sc=0.55, color=GRIS).next_to(ag.c2p(np.log10(v), -60), DOWN, buff=0.1) for v, t in [(0.2, "0{,}2"), (2, "2"), (10, "10"), (50, "50")]])
        gl = VGroup(*[M(t, sc=0.55, color=GRIS).next_to(ag.c2p(np.log10(0.02), v), LEFT, buff=0.1) for v, t in [(60, "60"), (40, "40"), (20, "20"), (0, "0"), (-20, "-20"), (-40, "-40")]])
        z0 = DashedLine(ag.c2p(np.log10(0.02), 0), ag.c2p(np.log10(500), 0), color=GRIS, stroke_width=2)
        self.at(self.a("g2", "Cassures"), Create(fg), FadeIn(lab), FadeIn(gl), Create(z0), run_time=0.8)
        L = np.log10
        p1 = (L(0.02), 74); p2 = (L(0.2), 54); p3 = (L(2), 14); p4 = (L(50), 14 - 20*L(25)); p5 = (L(500), 14 - 20*L(25) - 40)
        s1 = lig(ag, [p1, p2]); s2 = lig(ag, [p2, p3]); s3 = lig(ag, [p3, p4]); s4 = lig(ag, [p4, p5])
        v54 = M("54", sc=0.6, color=JAUNE).next_to(ag.c2p(*p2), UR, buff=0.08); v14 = M("14", sc=0.6, color=JAUNE).next_to(ag.c2p(*p3), UR, buff=0.08)
        v_14 = M("-14", sc=0.6, color=JAUNE).next_to(ag.c2p(*p4), UR, buff=0.08)
        self.at(self.a("g3", "Départ"), Create(s1), run_time=0.7); self.at(self.a("g3", "En zéro virgule deux"), FadeIn(v54), run_time=0.4)
        self.at(self.t("g4"), Create(s2), run_time=0.8); self.play(FadeIn(v14), run_time=0.3)
        self.at(self.a("g4", "Le zéro remonte"), Create(s3), run_time=0.8)
        H = lambda w: 100*(1 + 0.5j*w)/(1j*w*(1 + 5j*w)*(1 + 0.02j*w))
        cg = crb(ag, lambda w: dB(H(w)), L(0.02), L(500), gmin=-60, gmax=80)
        dc = Dot(ag.c2p(1, 0), color=VERT, radius=0.1); lc = T(r"$0$ dB vers $10$ rad/s", sc=0.62, color=VERT).next_to(dc, UR, buff=0.15)
        self.at(self.t("g5"), FadeIn(dc, scale=2), FadeIn(lc), run_time=0.6)
        self.at(self.a("g5", "Puis moins quarante"), Create(s4), FadeIn(v_14), run_time=0.7)
        self.play(Create(cg), run_time=1.0)
        pf = M(r"\varphi(10) = -90^\circ - \arctan 50 + \arctan 5 - \arctan 0{,}2 \approx -112^\circ", sc=0.75, color=ROUGE).move_to([0.6, -3.25, 0])
        self.ecr(self.t("g6"), pf, rt=1.6); self.play(Create(enc(pf, col=ROUGE, buff=0.12)), run_time=0.4)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"5.7 -- Les valeurs exactes", "Tracer un Bode")
        a = pos(T(r"asymptotes : l'\textbf{allure} \quad ; \quad calcul : les \textbf{valeurs}", sc=0.78, color=GRIS), -6.3, 2.0)
        self.ecr(self.t("h1"), a, rt=1.1)
        m = pos(M(r"|1 + j\tau\omega| = \sqrt{1 + \tau^2\omega^2}, \qquad |j\omega| = \omega", sc=0.95, color=BLEU), -6.3, 0.85)
        self.ecr(self.t("h2"), m, rt=1.3)
        p = pos(M(r"\arg(1 + j\tau\omega) = \arctan(\tau\omega), \qquad \arg\frac{1}{j\omega} = -90^\circ", sc=0.95, color=VERT), -6.3, -0.45)
        self.ecr(self.t("h3"), p, rt=1.4)
        ax, fr = cadre(-3.2, -2.45, 5.0, 1.4, -1, 1, -100, 10)
        a1 = lig(ax, [(-1, 0), (-1 + 0.0001, 0), (0 - 0.0001, 0), (0 + 0.0001, -90), (1, -90)], col=ORANGE, sw=3)
        a1 = lig(ax, [(-1, 0), (-0.001, 0), (0.001, -90), (1, -90)], col=ORANGE, sw=3)
        c = crb(ax, lambda w: -np.degrees(np.arctan(w)), -1, 1)
        e = DoubleArrow(ax.c2p(0, 0), ax.c2p(0, -45), color=ROUGE, buff=0, stroke_width=3, tip_length=0.12)
        le = M(r"45^\circ", sc=0.65, color=ROUGE).next_to(e, RIGHT, buff=0.1)
        at = T(r"marge de stabilité : \textbf{phase exacte} !", sc=0.75, color=ROUGE).move_to([3.6, -2.45, 0])
        self.at(self.t("h4"), Create(fr), Create(a1), Create(c), run_time=1.0)
        self.at(self.a("h4", "se trompe"), GrowFromCenter(e), FadeIn(le), run_time=0.5)
        self.ecr(self.a("h4", "Une marge"), at, rt=1.0)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"5.8 -- À vous : un tracé asymptotique", "Exercice")
        h = M(r"H(p) = \frac{20}{(1 + 0{,}5p)(1 + 0{,}05p)}", sc=1.0, color=JAUNE).move_to([-1.5, 2.0, 0])
        q = T(r"gain asymptotique ? \; coupure à $0$ dB ?", sc=0.72, color=BLEU).next_to(h, DOWN, buff=0.25)
        self.ecr(self.a("i1", "Tracez"), h, rt=1.1); self.ecr(self.a("i1", "Où coupe"), q, rt=0.8)
        pa, arc = chrono(4.3, 2.0)
        self.at(self.a("i1", "Mettez sur pause"), FadeIn(pa), Create(arc), run_time=0.5)
        self.play(Uncreate(arc), run_time=2.6); self.play(FadeOut(pa), run_time=0.2)
        ag, fg = cadre(0.0, -1.55, 11.0, 3.2, -1, 2, -30, 32)
        lab = VGroup(*[M(t, sc=0.55, color=GRIS).next_to(ag.c2p(np.log10(v), -30), DOWN, buff=0.1) for v, t in [(0.1, "0{,}1"), (2, "2"), (20, "20"), (100, "100")]])
        gl = VGroup(*[M(t, sc=0.55, color=GRIS).next_to(ag.c2p(-1, v), LEFT, buff=0.1) for v, t in [(26, "26"), (6, "6"), (0, "0")]])
        z0 = DashedLine(ag.c2p(-1, 0), ag.c2p(2, 0), color=GRIS, stroke_width=2)
        L = np.log10
        s1 = lig(ag, [(-1, 26), (L(2), 26)]); s2 = lig(ag, [(L(2), 26), (L(20), 6)]); s3 = lig(ag, [(L(20), 6), (2, 6 - 40*(2 - L(20)))])
        self.at(self.t("i2"), Create(fg), FadeIn(lab), FadeIn(gl), Create(z0), Create(s1), run_time=1.0)
        self.at(self.t("i3"), Create(s2), run_time=0.8)
        w0 = L(20) + 6/40
        d = Dot(ag.c2p(w0, 0), color=VERT, radius=0.09); ld = T(r"asymptote : $\approx 28$ rad/s", sc=0.62, color=VERT).next_to(d, UR, buff=0.12)
        self.at(self.t("i4"), Create(s3), run_time=0.8); self.at(self.a("i4", "L'asymptote coupe"), FadeIn(d, scale=2), FadeIn(ld), run_time=0.5)
        H = lambda w: 20/((1 + 0.5j*w)*(1 + 0.05j*w))
        cg = crb(ag, lambda w: dB(H(w)), -1, 2, gmin=-30, gmax=32)
        d2 = Dot(ag.c2p(L(24.9), 0), color=BLEU, radius=0.09); l2 = T(r"réel : $\approx 25$", sc=0.62, color=BLEU).next_to(d2, DL, buff=0.12)
        self.at(self.t("i5"), Create(cg), run_time=1.0); self.play(FadeIn(d2, scale=2), FadeIn(l2), run_time=0.4)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"5.9 -- Lire un diagramme de Bode", "Identifier")
        pts = [("j2", r"pente et phase de départ : classe ($-20$ dB/déc et $-90^\circ$ : classe $1$)", BLEU),
               ("j3", r"gain : plateau (classe $0$), ou coupure de la droite de départ (classe $1$)", VERT),
               ("j4", r"changement de pente : une cassure ; \; phase qui plonge : un \textbf{retard}", ORANGE)]
        t = pos(T(r"Du Bode mesuré à la fonction de transfert", sc=0.8, color=JAUNE), -6.3, 2.0)
        self.ecr(self.t("j1"), t, rt=1.0)
        for k, (ph_, txt, c) in enumerate(pts):
            y = 0.8 - 1.25*k
            ca = carte(k+1, c, -6.0, y); tx = pos(T(txt, sc=0.66), -5.45, y)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.2), run_time=1.0)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"À retenir", "Bilan")
        pts = [("k1", r"Sinusoïde $\to$ sinusoïde ; gain $|H(j\omega)|$, phase $\arg H(j\omega)$", BLEU),
               ("k2", r"En décibels, les Bode des blocs \textbf{s'additionnent}", VERT),
               ("k3", r"Départ $-20\,\alpha$ ; \; pôle $-20$, \; zéro $+20$, \; deuxième ordre $-40$", ORANGE),
               ("k4", r"Asymptotes pour l'allure, calcul exact pour les valeurs", JAUNE)]
        for k, (ph_, txt, c) in enumerate(pts):
            y = 1.8 - 1.3*k
            ca = carte(k+1, c, -5.9, y); tx = pos(T(txt, sc=0.74), -5.35, y)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        self.fin()

MES = [(1, 12.0, -92.9), (2, 6.0, -95.7), (20, -17.0, -135.0), (200, -54.0, -174.3)]
class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice résolu -- l'énoncé", "Application")
        t = pos(T(r"Axe motorisé : tension $\to$ position. Mesures :", sc=0.78), -6.3, 2.0)
        self.ecr(self.t("l1"), t, rt=1.0)
        hd = VGroup(*[T(s, sc=0.7, color=GRIS) for s in [r"$\omega$ (rad/s)", "gain (dB)", "phase"]])
        rows = [[M(str(w), sc=0.75), M(str(g).replace(".", "{,}").replace("-", "-"), sc=0.75), M((str(p).replace(".", "{,}")) + r"^\circ", sc=0.75)] for w, g, p in MES]
        tab = VGroup(*[VGroup(*c) for c in zip(hd, *rows)])
        for k, col in enumerate(tab):
            for j, m in enumerate(col):
                m.move_to([-5.4 + 2.0*k, 1.15 - 0.55*j, 0])
        ag, fg = cadre(3.6, 0.2, 5.4, 3.0, -0.3, 2.5, -62, 20)
        lab = VGroup(*[M(t_, sc=0.55, color=GRIS).next_to(ag.c2p(np.log10(v), -62), DOWN, buff=0.1) for v, t_ in [(1, "1"), (10, "10"), (100, "100")]])
        dots = VGroup(*[Dot(ag.c2p(np.log10(w), g), color=JAUNE, radius=0.08) for w, g, _ in MES])
        self.at(self.t("l1") + 1.6, FadeIn(VGroup(*hd)), Create(fg), FadeIn(lab), run_time=0.6)
        for j, fr in [(0, "À un radian"), (1, "À deux"), (2, "À vingt"), (3, "Et à deux cents")]:
            ph_ = "l2" if j < 2 else "l3"
            self.at(self.a(ph_, fr), *[FadeIn(tab[k][j + 1]) for k in range(3)], FadeIn(dots[j], scale=2), run_time=0.5)
        q = T(r"Quelle fonction de transfert ?", sc=0.8, color=ROUGE).move_to([-1.5, -1.95, 0])
        self.ecr(self.t("l4"), q, rt=0.8); self.play(Create(enc(q)), run_time=0.4)
        rf = T(r"Réfléchissons : la classe, le gain, puis les cassures", sc=0.72, color=BLEU).move_to([-1.5, -3.0, 0])
        self.ecr(self.a("l4", "Réfléchissons"), rf, rt=1.0)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- la solution", "Application")
        def etape(k, c, y, m, ph_, fr, rt=1.0):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(self.a(ph_, fr), Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        ag, fg = cadre(4.6, 0.55, 4.4, 3.0, -0.3, 2.5, -62, 20)
        lab = VGroup(*[M(t_, sc=0.55, color=GRIS).next_to(ag.c2p(np.log10(v), -62), DOWN, buff=0.1) for v, t_ in [(1, "1"), (10, "10"), (100, "100")]])
        dots = VGroup(*[Dot(ag.c2p(np.log10(w), g), color=JAUNE, radius=0.08) for w, g, _ in MES])
        etape(1, BLEU, 2.15, T(r"$-20$ dB/déc et phase $\approx -90^\circ$", sc=0.68), "m1", "Première étape", 1.2)
        self.play(Create(fg), FadeIn(lab), FadeIn(dots), run_time=0.6)
        c1 = pos(T(r"$\Rightarrow$ un intégrateur : classe $1$", sc=0.7, color=BLEU), -5.85, 1.45)
        self.ecr(self.t("m2"), c1, rt=0.8)
        etape(2, VERT, 0.6, M(r"20\log K = 12 \;\Rightarrow\; K = 10^{12/20} \approx 4", sc=0.8), "m3", "Deuxième étape", 1.2)
        etape(3, ORANGE, -0.6, T(r"$\varphi(20) = -135^\circ$ : cassure en $20$ rad/s", sc=0.68), "m4", "Troisième étape", 1.2)
        tc = pos(M(r"\tau = \frac{1}{20} = 0{,}05\ \mathrm{s}", sc=0.8, color=ORANGE), -5.85, -1.35)
        self.ecr(self.t("m5"), tc, rt=0.8)
        mo = pos(M(r"H(p) = \frac{4}{p\,(1 + 0{,}05\,p)}", sc=0.95, color=JAUNE), -5.85, -2.6)
        H = lambda w: 4/(1j*w*(1 + 0.05j*w))
        cg = crb(ag, lambda w: dB(H(w)), -0.3, 2.5, gmin=-62, gmax=20)
        self.at(self.t("m6"), Ecrire(mo, rt=1.0), Create(cg), run_time=1.0); self.play(Create(enc(mo, col=JAUNE, buff=0.15)), run_time=0.4)
        v = T(r"$200$ rad/s : $-54$ dB, \; $-174^\circ$ \;$\checkmark$", sc=0.7, color=VERT).move_to([4.6, -1.55, 0])
        self.ecr(self.a("m7", "Vérifions"), v, rt=1.0); self.play(Indicate(dots[3], color=VERT, scale_factor=2), run_time=0.6)
        nx = T(r"Prochain chapitre : la stabilité", sc=0.62, color=GRIS).move_to([4.6, -2.5, 0])
        self.at(self.t("m8"), FadeIn(nx), run_time=0.6)
        self.fin()
