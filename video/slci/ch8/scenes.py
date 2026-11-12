from base import *
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def enc(m, col=ROUGE, buff=0.22): return SurroundingRectangle(m, color=col, buff=buff, corner_radius=0.08)
def chrono(x, y):
    pa = VGroup(Rectangle(width=0.09, height=0.3), Rectangle(width=0.09, height=0.3)).arrange(RIGHT, buff=0.08).set_fill(JAUNE, 1).set_stroke(width=0).move_to([x, y, 0])
    arc = Circle(radius=0.3, color=JAUNE, stroke_width=4).move_to(pa).rotate(PI/2)
    return pa, arc
def cadre(x, y, w, h, l0, l1, g0, g1):
    ax = Axes(x_range=[l0, l1, 1], y_range=[g0, g1, 1], x_length=w, y_length=h, tips=False,
              axis_config={"stroke_opacity": 0, "include_ticks": False}).move_to([x, y, 0])
    fr = Rectangle(width=w, height=h, color=GRIS, stroke_width=2).move_to([x, y, 0])
    return ax, fr
def lig(ax, pts, col=ORANGE, sw=4):
    return VMobject(color=col, stroke_width=sw).set_points_as_corners([ax.c2p(a, b) for a, b in pts])
def crb(ax, f, l0, l1, col=BLEU, sw=5, n=200, lo=None, hi=None):
    u = np.linspace(l0, l1, n); v = np.array([f(10**x) for x in u])
    if lo is not None: v = np.clip(v, lo, hi)
    return VMobject(color=col, stroke_width=sw).set_points_smoothly([ax.c2p(a, b) for a, b in zip(u, v)])
def blk(lab, x, y, w=1.6, h=0.75, col=CRAIE, sc=0.7):
    r = Rectangle(width=w, height=h, color=col, stroke_width=3).move_to([x, y, 0])
    t = M(lab, sc=sc, color=col).move_to(r)
    if t.width > w - 0.15: t.scale_to_fit_width(w - 0.2)
    return VGroup(r, t)
def som(x, y, r=0.24, col=CRAIE):
    d = r*0.7
    return VGroup(Circle(radius=r, color=col, stroke_width=3).move_to([x, y, 0]), Line([x-d, y-d, 0], [x+d, y+d, 0], color=col, stroke_width=2), Line([x-d, y+d, 0], [x+d, y-d, 0], color=col, stroke_width=2))
def fl(*pts, col=CRAIE, sw=3):
    pts = [np.array([p[0], p[1], 0]) for p in pts]
    g = VGroup(*[Line(pts[i], pts[i+1], color=col, stroke_width=sw) for i in range(len(pts) - 2)])
    g.add(Arrow(pts[-2], pts[-1], buff=0, color=col, stroke_width=sw, max_tip_length_to_length_ratio=0.5, tip_length=0.18))
    return g
def dB(z): return 20*np.log10(np.abs(z))
def ph(z): return np.degrees(np.angle(z))

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PT", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Automatique -- Chapitre 8}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Correction des SLCI : régler les correcteurs", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        ax, fr = cadre(3.8, -1.0, 4.2, 2.4, -1, 2, -10, 70)
        a = 4; T_ = 0.1
        c = crb(ax, lambda w: ph((1 + a*T_*1j*w)/(1 + T_*1j*w)), -1, 2, col=VERT)
        lb = T(r"avance de phase", sc=0.6, color=VERT).next_to(fr, DOWN, buff=0.15)
        self.at(self.a("a2", "avec des correcteurs"), Create(fr), Create(c), FadeIn(lb), run_time=1.2)
        items = []
        for k, (txt, col) in enumerate([("Le cahier des charges", BLEU), ("Les actions P, I et D", VERT), ("Le correcteur proportionnel", ORANGE),
                                         ("Le correcteur PI", ROUGE), ("L'avance de phase", BLEU), ("Exercice résolu", JAUNE)]):
            yy = 0.75 - 0.6*k
            items.append(VGroup(carte(k+1, col, -6.2, yy), pos(T(txt, sc=0.74), -5.65, yy)))
        for it, (sid, fr_) in zip(items, [("a3", "traduire le cahier"), ("a3", "les actions"), ("a3", "le correcteur proportionnel"),
                                          ("a3", "le P I"), ("a3", "l'avance de phase"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr_)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"8.1 -- Du cahier des charges à la FTBO", "Correction")
        t = pos(T(r"tout se règle sur le \textbf{Bode de la FTBO}", sc=0.78, color=JAUNE), -6.3, 2.05)
        self.ecr(self.t("b1"), t, rt=1.0)
        rows = [("b2", "Stabilité", r"marges à $\omega_{c0}$ et $\omega_\pi$", BLEU, "La stabilité"),
                ("b3", "Amortissement", r"$M_\varphi$ \; ; \; $\xi \approx M_\varphi/100$ \; ($60^\circ \to \approx 10\,\%$)", VERT, "L'amortissement"),
                ("b4", "Rapidité", r"$\omega_{c0}$ \; ; \; $t_{r5\%} \approx 3/\omega_{c0}$", ORANGE, "La rapidité"),
                ("b5", "Précision", r"basses pulsations : classe et gain", ROUGE, "Et la précision")]
        for k, (ph_, nom, txt, c, fr) in enumerate(rows):
            y = 0.95 - 0.95*k
            n = pos(T(r"\textbf{" + nom + "}", sc=0.76, color=c), -6.3, y)
            a = M(r"\longrightarrow", sc=0.8, color=GRIS).move_to([-2.5, y, 0])
            l = pos(T(txt, sc=0.74), -1.9, y)
            self.at(self.a(ph_, fr), Ecrire(n, rt=0.5), FadeIn(a), Ecrire(l, rt=1.0), run_time=1.0)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"8.2 -- Les actions P, I et D", "Correction")
        cel = [("P", r"K_p", lambda w: 12 + 0*w, r"\varphi = 0", "c1", "L'action proportionnelle", VERT),
               ("I", r"\frac{1}{T_i\,p}", lambda w: dB(1/(1j*w)), r"\varphi = -90^\circ", "c2", "L'action intégrale", ROUGE),
               ("D", r"T_d\,p", lambda w: dB(1j*w), r"\varphi = +90^\circ", "c3", "L'action dérivée", ORANGE)]
        EFF = [((r"règle rapidité", r"et précision"), "elle translate"), ((r"annule l'écart,", r"coûte de la phase"), "Elle annule"), ((r"remonte la phase,", r"amplifie le bruit"), "Elle remonte")]
        for k, (nom, ft, f, phs, ph_, fr, col) in enumerate(cel):
            cx = -4.3 + 4.3*k
            nm = T(r"\textbf{Action " + nom + "}", sc=0.72, color=col).move_to([cx - 0.6, 1.95, 0])
            fm = M(ft, sc=0.7, color=col).move_to([cx + 1.1, 1.95, 0])
            ax, fr_ = cadre(cx, 0.55, 3.4, 1.8, -1, 1, -25, 25)
            z0 = DashedLine(ax.c2p(-1, 0), ax.c2p(1, 0), color=GRIS, stroke_width=1.5)
            c = crb(ax, f, -1, 1, col=col, sw=4)
            pl = M(phs, sc=0.7, color=col).move_to([cx, -0.65, 0])
            self.at(self.a(ph_, fr), Ecrire(nm, rt=0.5), FadeIn(fm), Create(fr_), Create(z0), Create(c), FadeIn(pl), run_time=1.0)
            txt, fr2 = EFF[k]
            m = VGroup(*[T(x_, sc=0.6, color=col) for x_ in txt]).arrange(DOWN, buff=0.08).move_to([cx, -1.4, 0]); self.ecr(self.a(ph_, fr2), m, rt=0.8)
        idee = T(r"intégrale aux \textbf{basses} pulsations, dérivée autour de $\omega_{c0}$", sc=0.78, color=JAUNE).move_to([0, -2.6, 0])
        self.ecr(self.t("c4"), idee, rt=1.2); self.play(Create(enc(idee, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"8.3 -- Le correcteur proportionnel", "Correcteur P")
        t = pos(T(r"$K_p$ translate le gain : la \textbf{phase du processus} décide", sc=0.74, color=GRIS), -6.3, 2.1)
        self.ecr(self.t("d1"), t, rt=1.0)
        m1 = pos(M(r"\arg H(j\omega_\varphi) = -180^\circ + M_\varphi, \qquad K_p = \frac{1}{|H(j\omega_\varphi)|}", sc=0.85, color=JAUNE), -6.3, 1.15)
        self.ecr(self.t("d2"), m1, rt=1.5); self.play(Create(enc(m1, col=JAUNE, buff=0.15)), run_time=0.4)
        ex = pos(M(r"H(p) = \frac{1}{p\,(1 + 0{,}1p)}, \; M_\varphi = 45^\circ : \; 0{,}1\,\omega_\varphi = 1 \Rightarrow \omega_\varphi = 10", sc=0.78), -6.3, -0.1)
        self.ecr(self.t("d3"), ex, rt=1.6)
        k = pos(M(r"|H(j10)| = \frac{1}{10\sqrt{2}} \;\Rightarrow\; K_p = 10\sqrt{2} \approx 14", sc=0.85, color=VERT), -6.3, -1.25)
        self.ecr(self.t("d4"), k, rt=1.3)
        lim = pos(T(r"limite : \textbf{un seul réglage} pour précision, rapidité et marge", sc=0.72, color=ROUGE), -6.3, -2.5)
        self.ecr(self.t("d5"), lim, rt=1.1)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"8.4 -- Le correcteur PI", "Correcteur PI")
        f = pos(M(r"C(p) = K_p\,\frac{1 + T_i\,p}{T_i\,p}", sc=1.0, color=JAUNE), -6.3, 2.0)
        self.ecr(self.t("e1"), f, rt=1.0)
        ag, fg = cadre(3.6, 1.35, 5.4, 1.5, -1, 2, -5, 45); ap, fp = cadre(3.6, -0.35, 5.4, 1.2, -1, 2, -95, 5)
        g = lig(ag, [(-1, 40), (0, 20), (2, 20)]); p = crb(ap, lambda w: -np.degrees(np.arctan(1/w)), -1, 2, col=ORANGE, sw=4)
        lc = M(r"1/T_i", sc=0.6, color=GRIS).next_to(ap.c2p(0, -95), DOWN, buff=0.1)
        li = T("intégrateur", sc=0.55, color=ORANGE).move_to(ag.c2p(-0.45, 38)); lk = T(r"gain $K_p$", sc=0.55, color=ORANGE).move_to(ag.c2p(1.0, 27))
        self.at(self.a("e1", "Un intégrateur"), Create(fg), Create(fp), Create(g), Create(p), FadeIn(lc), FadeIn(li), FadeIn(lk), run_time=1.2)
        c1 = VGroup(T(r"classe $+1$ : écart statique nul,", sc=0.66, color=VERT), T(r"perturbations entrant après lui rejetées", sc=0.66, color=VERT)).arrange(DOWN, aligned_edge=LEFT, buff=0.1); pos(c1, -6.3, 0.75)
        self.ecr(self.t("e2"), c1, rt=1.1)
        r = pos(T(r"réglage : \textbf{$T_i$ d'abord}, $K_p$ ensuite", sc=0.74, color=BLEU), -6.3, -1.35)
        self.ecr(self.t("e3"), r, rt=0.9)
        s1 = pos(M(r"\text{1.}\;\; T_i \approx \frac{10}{\omega_{c0}} \;\; (\text{coût} \approx 6^\circ)", sc=0.8), -6.3, -2.25)
        s2 = pos(M(r"\text{2.}\;\; T_i = \tau_{\text{dominant}} \;\; (\text{compensation})", sc=0.8), -6.3, -3.1)
        self.ecr(self.t("e4"), s1, rt=1.1); self.ecr(self.t("e5"), s2, rt=1.1)
        self.fin()

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"8.5 -- Un PI par compensation", "Exemple en direct")
        h = pos(M(r"H(p) = \frac{2}{(1 + p)(1 + 0{,}1p)} \quad (\text{classe } 0), \qquad M_\varphi = 45^\circ", sc=0.85), -6.3, 2.0)
        self.ecr(self.t("f1"), h, rt=1.4)
        a = pos(M(r"T_i = 1\ \mathrm{s} \;\Rightarrow\; H_{BO} = K_p\,\frac{1 + p}{p}\cdot\frac{2}{(1 + p)(1 + 0{,}1p)} = \frac{2K_p}{p\,(1 + 0{,}1p)}", sc=0.8), -6.3, 0.7)
        self.ecr(self.t("f2"), a, rt=1.6)
        b = pos(M(r"\omega_{c0} = 10 : \; 2K_p = 10\sqrt{2} \;\Rightarrow\; K_p \approx 7{,}1", sc=0.88, color=JAUNE), -6.3, -0.6)
        self.ecr(self.t("f3"), b, rt=1.3); self.play(Create(enc(b, col=JAUNE, buff=0.15)), run_time=0.4)
        c = pos(T(r"classe $1$ : écart statique nul \;+\; $45^\circ$ de marge", sc=0.8, color=VERT), -6.3, -1.9)
        self.ecr(self.t("f4"), c, rt=1.1)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"8.6 -- Le correcteur à avance de phase", "Avance de phase")
        f = pos(M(r"C(p) = K_p\,\frac{1 + aTp}{1 + Tp}, \quad a > 1", sc=0.95, color=JAUNE), -6.3, 2.05)
        self.ecr(self.a("g2", "C de p égale"), f, rt=1.1)
        a = 5.0; Tt = 0.1
        C = lambda w: (1 + a*Tt*1j*w)/(1 + Tt*1j*w)
        ag, fg = cadre(3.4, 1.0, 6.0, 1.6, -1, 2.5, -2, 18); ap, fp = cadre(3.4, -0.85, 6.0, 1.6, -1, 2.5, -5, 50)
        cg = crb(ag, lambda w: dB(C(w)), -1, 2.5, col=VERT); cp = crb(ap, lambda w: ph(C(w)), -1, 2.5, col=VERT)
        self.at(self.a("g3", "Sa phase forme une bosse"), Create(fg), Create(fp), Create(cg), Create(cp), run_time=1.2)
        wm = 1/(Tt*np.sqrt(a)); pm = np.degrees(np.arcsin((a - 1)/(a + 1)))
        d = Dot(ap.c2p(np.log10(wm), pm), color=JAUNE, radius=0.09); ld = M(r"\varphi_m", sc=0.7, color=JAUNE).next_to(d, RIGHT, buff=0.15)
        v = DashedLine(ag.c2p(np.log10(wm), 18), ap.c2p(np.log10(wm), -5), color=JAUNE, stroke_width=2); lw = M(r"\omega_m", sc=0.65, color=JAUNE).next_to(ap.c2p(np.log10(wm), -5), DOWN, buff=0.1)
        s = pos(M(r"\sin\varphi_m = \frac{a - 1}{a + 1}", sc=0.9, color=VERT), -6.3, 0.75)
        self.at(self.a("g3", "Le maximum"), FadeIn(d, scale=2), FadeIn(ld), Ecrire(s, rt=1.0), run_time=1.0)
        w = pos(M(r"\omega_m = \frac{1}{T\sqrt{a}}, \quad |C(j\omega_m)| = K_p\sqrt{a}", sc=0.85, color=VERT), -6.3, -0.45)
        self.at(self.t("g4"), Create(v), FadeIn(lw), Ecrire(w, rt=1.2), run_time=1.2)
        dm = pos(T(r"démarche : $\varphi_m \to a$, \; $\omega_m = \omega_{c0}$ visée $\to T$, \; puis $K_p$", sc=0.74, color=JAUNE), -6.3, -2.4)
        self.ecr(self.t("g5"), dm, rt=1.4); self.play(Create(enc(dm, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"8.7 -- À vous : un réglage proportionnel", "Exercice")
        h = M(r"H(p) = \frac{1}{p\,(1 + 0{,}1p)} \qquad M_\varphi = 60^\circ \;?", sc=1.0, color=JAUNE).move_to([-1.0, 1.9, 0])
        self.ecr(self.a("h1", "H de p"), h, rt=1.1)
        pa, arc = chrono(4.6, 1.9)
        self.at(self.a("h1", "Mettez sur pause"), FadeIn(pa), Create(arc), run_time=0.5)
        self.play(Uncreate(arc), run_time=2.6); self.play(FadeOut(pa), run_time=0.2)
        a = pos(M(r"-90^\circ - \arctan(0{,}1\,\omega) = -120^\circ \;\Rightarrow\; \omega_\varphi \approx 5{,}8\ \mathrm{rad/s}", sc=0.88), -6.3, 0.3)
        self.ecr(self.t("h2"), a, rt=1.5)
        b = M(r"|H(j\omega_\varphi)| \approx 0{,}15 \;\Rightarrow\; K_p \approx 6{,}7", sc=1.0, color=JAUNE).move_to([-1.0, -1.15, 0])
        self.ecr(self.t("h3"), b, rt=1.2); self.play(Create(enc(b, col=JAUNE)), run_time=0.4)
        c = T(r"plus amorti, mais plus lent ($\omega_{c0} \approx 5{,}8$ au lieu de $10$)", sc=0.72, color=GRIS).move_to([-1.0, -2.4, 0])
        self.ecr(self.a("h3", "Plus amorti"), c, rt=1.0)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"8.8 -- Vérifier et choisir", "Correction")
        ck = [r"marges recalculées", r"dépassement et temps de réponse", r"écart statique"]
        for k, txt in enumerate(ck):
            m = pos(T(r"$\checkmark$ \; " + txt, sc=0.74, color=VERT), -6.3, 2.0 - 0.6*k)
            self.at(self.t("i1") + 0.9*k, Ecrire(m, rt=0.7), run_time=0.7)
        sat = pos(T(r"$\checkmark$ \; pic de commande sous la \textbf{saturation} (surtout avec l'avance de phase)", sc=0.72, color=ROUGE), -6.3, 0.2)
        self.ecr(self.t("i2"), sat, rt=1.3)
        ch = [(r"imprécis", r"PI", "imprécis"), (r"précis, mais peu amorti ou lent", r"avance de phase", "Précis mais"), (r"les deux défauts", r"PI + avance en série", "Les deux défauts")]
        for k, (de, co, fr) in enumerate(ch):
            y = -1.0 - 0.75*k
            a = pos(T(de, sc=0.72), -6.3, y); ar = M(r"\longrightarrow", sc=0.8, color=GRIS).move_to([-1.0, y, 0]); b = pos(T(r"\textbf{" + co + "}", sc=0.74, color=JAUNE), -0.3, y)
            self.at(self.a("i3", fr), Ecrire(a, rt=0.6), FadeIn(ar), Ecrire(b, rt=0.6), run_time=0.8)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"8.9 -- Stratégies avancées", "Correction")
        l1 = pos(T(r"\textbf{Boucles imbriquées} : courant $\subset$ vitesse $\subset$ position", sc=0.76, color=BLEU), -6.3, 2.05)
        self.ecr(self.t("j1"), l1, rt=1.1)
        rr = [Rectangle(width=w, height=h, color=c, stroke_width=3).move_to([3.6, 0.85, 0]) for w, h, c in [(5.6, 1.9, BLEU), (4.0, 1.3, VERT), (2.4, 0.7, ORANGE)]]
        lb = [T(t, sc=0.52, color=c).move_to([x_, y_, 0]) for t, c, x_, y_ in [("position", BLEU, 1.6, 1.65), ("vitesse", VERT, 2.35, 1.35), ("courant", ORANGE, 3.6, 0.85)]]
        self.at(self.a("j1", "courant, puis vitesse"), *[Create(r) for r in rr], *[FadeIn(l) for l in lb], run_time=1.0)
        l2 = pos(T(r"de l'intérieur vers l'extérieur, \\ chaque boucle $5$ à $10$ fois plus rapide", sc=0.68, color=GRIS), -6.3, 1.1)
        self.ecr(self.t("j2"), l2, rt=1.2)
        an = pos(T(r"\textbf{Anticipation} : terme $F(p)\,E(p)$ ajouté hors de la boucle", sc=0.74, color=VERT), -6.3, -0.55)
        self.ecr(self.t("j3"), an, rt=1.1)
        fe = pos(M(r"\varepsilon = \frac{1 - F\,G}{1 + C\,G}\,E \quad\Rightarrow\quad \text{stabilité inchangée}", sc=0.85, color=VERT), -6.3, -1.45)
        self.ecr(self.t("j4"), fe, rt=1.3)
        pid = pos(M(r"\text{PID réel} : \; K_p\,\frac{1 + T_ip}{T_ip}\cdot\frac{1 + aTp}{1 + Tp}", sc=0.85, color=JAUNE), -6.3, -2.7)
        self.ecr(self.t("j5"), pid, rt=1.3)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"À retenir", "Bilan")
        pts = [("k1", r"Sur la FTBO : $M_\varphi$ (amortissement), $\omega_{c0}$ (rapidité), classe (précision)", BLEU),
               ("k2", r"P : $\omega_\varphi$ où $\arg H = -180^\circ + M_\varphi$, puis $K_p = 1/|H(j\omega_\varphi)|$", VERT),
               ("k3", r"PI : $T_i$ d'abord ($10/\omega_{c0}$ ou compensation), $K_p$ ensuite", ORANGE),
               ("k4", r"Avance : $\varphi_m \to a$, \; $\omega_m \to T$, \; puis $K_p$", JAUNE)]
        for k, (ph_, txt, c) in enumerate(pts):
            yy = 1.8 - 1.3*k
            ca = carte(k+1, c, -5.9, yy); tx = pos(T(txt, sc=0.72), -5.35, yy)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        self.fin()

H = lambda w: 5/(1j*w*(1 + 0.2j*w))
class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice résolu -- l'énoncé", "Application")
        y = 1.55
        s = som(-4.6, y); c = blk(r"C(p)", -3.0, y, w=1.3, col=ORANGE); g = blk(r"\frac{5}{p\,(1 + 0{,}2p)}", -0.8, y, w=2.3, h=0.9)
        fs = [fl((-6.2, y), (-4.84, y)), fl((-4.36, y), (-3.65, y)), fl((-2.35, y), (-1.95, y)), fl((0.35, y), (2.0, y))]
        r = fl((1.3, y), (1.3, y - 1.0), (-4.6, y - 1.0), (-4.6, y - 0.24), col=BLEU)
        self.at(self.t("l1"), *[Create(f) for f in fs], Create(s), Create(c[0]), FadeIn(c[1]), Create(g[0]), FadeIn(g[1]), Create(r), run_time=1.0)
        c1 = pos(T(r"$M_\varphi \geq 45^\circ$", sc=0.8, color=BLEU), -6.3, -0.15)
        c2 = pos(T(r"écart de traînage $\leq 5\,\%$ pour une rampe de pente $1$", sc=0.8, color=BLEU), -6.3, -0.85)
        self.ecr(self.a("l2", "une marge de phase"), c1, rt=0.7); self.ecr(self.a("l2", "et un écart de traînage"), c2, rt=1.2)
        q = T(r"Un correcteur P suffit-il ? Sinon : avance de phase", sc=0.8, color=ROUGE).move_to([0, -1.95, 0])
        self.ecr(self.t("l3"), q, rt=1.1); self.play(Create(enc(q)), run_time=0.4)
        rf = T(r"Réfléchissons : la précision fixe le gain, puis on lit la marge", sc=0.72, color=BLEU).move_to([0, -3.0, 0])
        self.ecr(self.t("l4"), rf, rt=1.0)
        self.fin()

class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- la solution", "Application")
        def etape(k, c, y, m, ph_, fr, rt=1.0):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(self.a(ph_, fr), Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        etape(1, BLEU, 2.2, M(r"\varepsilon_v = \frac{1}{K_{BO}} \leq 0{,}05 \;\Rightarrow\; K_{BO} \geq 20, \; K_p \geq 4", sc=0.72), "m1", "Première étape", 1.2)
        etape(2, VERT, 1.25, M(r"K_p = 4 : \; \omega_{c0} \approx 9{,}4, \;\; \varphi \approx -152^\circ", sc=0.72), "m2", "Deuxième étape", 1.2)
        # Bode : FTBO avec P seul et avec l'avance
        a = 3; Tt = 1/(12.69*np.sqrt(3)); C = lambda w: 4*(1 + a*Tt*1j*w)/(1 + Tt*1j*w)
        ag, fg = cadre(4.4, 1.05, 4.6, 1.9, -0.5, 2.3, -40, 50); ap, fp = cadre(4.4, -1.1, 4.6, 1.6, -0.5, 2.3, -190, -80)
        z0 = DashedLine(ag.c2p(-0.5, 0), ag.c2p(2.3, 0), color=GRIS, stroke_width=1.5); m180 = DashedLine(ap.c2p(-0.5, -180), ap.c2p(2.3, -180), color=GRIS, stroke_width=1.5)
        gP = crb(ag, lambda w: dB(4*H(w)), -0.5, 2.3, col=ORANGE, sw=4, lo=-40, hi=50); pP = crb(ap, lambda w: ph(H(w)), -0.5, 2.3, col=ORANGE, sw=4)
        gA = crb(ag, lambda w: dB(C(w)*H(w)), -0.5, 2.3, col=VERT, sw=4, lo=-40, hi=50); pA = crb(ap, lambda w: ph(C(w)*H(w)), -0.5, 2.3, col=VERT, sw=4)
        lp = T("P seul", sc=0.55, color=ORANGE).next_to(fg, UP, buff=0.08).align_to(fg, LEFT); la = T("avec avance", sc=0.55, color=VERT).next_to(fg, UP, buff=0.08).align_to(fg, RIGHT)
        self.at(self.a("m2", "coupe vers"), Create(fg), Create(fp), Create(z0), Create(m180), Create(gP), Create(pP), FadeIn(lp), run_time=1.2)
        n = pos(T(r"$M_\varphi \approx 28^\circ$ : le P ne suffit pas !", sc=0.66, color=ROUGE), -5.85, 0.6)
        self.ecr(self.t("m3"), n, rt=0.9)
        etape(3, ORANGE, -0.15, M(r"a = 3 : \; \varphi_m = 30^\circ, \;\; |C(j\omega_m)| = 4\sqrt{3}", sc=0.72), "m4", "Troisième étape", 1.2)
        wm = pos(M(r"\omega_m \approx 12{,}7\ \mathrm{rad/s}", sc=0.74, color=ORANGE), -5.85, -0.9)
        self.ecr(self.a("m5", "On résout"), wm, rt=0.8)
        r = pos(M(r"-158{,}5^\circ + 30^\circ = -128{,}5^\circ \Rightarrow M_\varphi \approx 51{,}5^\circ", sc=0.72, color=VERT), -5.85, -1.65)
        self.ecr(self.t("m6"), r, rt=1.3)
        self.at(self.a("m6", "Avec les trente degrés"), Create(gA), Create(pA), FadeIn(la), run_time=1.2)
        cf = pos(M(r"C(p) = 4\,\frac{1 + 0{,}136\,p}{1 + 0{,}045\,p}", sc=0.85, color=JAUNE), -5.85, -2.6)
        self.ecr(self.t("m7"), cf, rt=1.2); self.play(Create(enc(cf, col=JAUNE, buff=0.12)), run_time=0.4)
        bi = T(r"précis, amorti, et plus rapide", sc=0.64, color=VERT).move_to([4.4, -2.45, 0])
        self.ecr(self.t("m8"), bi, rt=0.9)
        fin = T(r"Fin du cours d'automatique : bonnes révisions !", sc=0.52, color=GRIS).move_to([4.3, -3.1, 0])
        self.at(self.t("m9"), FadeIn(fin), run_time=0.6)
        self.fin()
