from base import *
from scipy import signal
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
    ax = Axes(x_range=[l0, l1, 1], y_range=[g0, g1, 1], x_length=w, y_length=h, tips=False,
              axis_config={"stroke_opacity": 0, "include_ticks": False}).move_to([x, y, 0])
    fr = Rectangle(width=w, height=h, color=GRIS, stroke_width=2).move_to([x, y, 0])
    return ax, fr
def crb(ax, f, l0, l1, col=BLEU, sw=5, n=200):
    u = np.linspace(l0, l1, n); v = np.array([f(10**x) for x in u])
    return VMobject(color=col, stroke_width=sw).set_points_smoothly([ax.c2p(a, b) for a, b in zip(u, v)])
def croix(p, col=ROUGE, r=0.12):
    return VGroup(Line(p + np.array([-r, -r, 0]), p + np.array([r, r, 0]), color=col, stroke_width=5),
                  Line(p + np.array([-r, r, 0]), p + np.array([r, -r, 0]), color=col, stroke_width=5))
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
def bf3(K, t):
    den = np.polyadd(np.polymul(np.polymul([1, 1], [1, 1]), [1, 1]), [K])
    _, y = signal.step(signal.lti([K], den), T=t); return y
def coupe(ax, t, y, col, ymin, ymax, sw=4):
    pts, seg = [], []
    for a, b in zip(t, y):
        if ymin <= b <= ymax: seg.append(ax.c2p(a, b))
        else:
            if len(seg) > 1: pts.append(seg)
            seg = []
    if len(seg) > 1: pts.append(seg)
    return VGroup(*[VMobject(color=col, stroke_width=sw).set_points_smoothly(s) for s in pts])
def dB(z): return 20*np.log10(np.abs(z))
def phd(z): return np.degrees(np.unwrap(np.angle(z)))

class S0(Cours):
    sid = "S0"
    def construct(self):
        sur = T(r"SCIENCES INDUSTRIELLES \;·\; PTSI", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Automatique -- Chapitre 6}", sc=1.2, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Stabilité des systèmes asservis", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-4.6, 1.3, 0], [4.6, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        ax = axes(3.7, -1.0, 4.4, 2.6, [0, 20, 5], [-0.6, 2.4, 1])
        t = np.linspace(0, 19.5, 300)
        cb = coupe(ax, t, bf3(10, t), ROUGE, -0.6, 2.4)
        self.at(self.a("a1", "Un drone"), Create(ax), run_time=0.5); self.play(Create(cb), run_time=2.0)
        items = []
        for k, (txt, c) in enumerate([("Définition et pôles", BLEU), ("Critères algébriques", VERT), ("Le critère du revers", ORANGE),
                                       ("Les marges de stabilité", ROUGE), ("Le gain et le retard", BLEU), ("Exercice résolu : les marges", JAUNE)]):
            yy = 0.75 - 0.6*k
            items.append(VGroup(carte(k+1, c, -6.2, yy), pos(T(txt, sc=0.74), -5.65, yy)))
        for it, (sid, fr) in zip(items, [("a3", "la définition"), ("a3", "les critères algébriques"), ("a3", "le critère du revers"),
                                         ("a3", "les marges"), ("a3", "et l'effet du gain"), ("a4", "un exercice résolu")]):
            self.jusqua(self.a(sid, fr)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(Cours):
    sid = "S1"
    def construct(self):
        self.entete(r"6.1 -- La notion de stabilité", "Stabilité")
        d = pos(T(r"\textbf{Stable} : entrée bornée $\Rightarrow$ sortie bornée", sc=0.8, color=JAUNE), -6.3, 2.05)
        self.ecr(self.t("b1"), d, rt=1.1)
        d2 = pos(T(r"écarté de l'équilibre, il y revient", sc=0.72, color=GRIS), -6.3, 1.35)
        self.ecr(self.t("b2"), d2, rt=0.9)
        ax = axes(-3.0, -1.05, 6.0, 3.8, [-3, 1.5, 1], [-2, 2, 1], col=GRIS)
        lr = M(r"\mathrm{Re}", sc=0.55, color=GRIS).next_to(ax.x_axis.get_end(), DOWN, buff=0.1); li = M(r"\mathrm{Im}", sc=0.55, color=GRIS).next_to(ax.y_axis.get_end(), LEFT, buff=0.1)
        zone = Polygon(ax.c2p(-3, -2), ax.c2p(0, -2), ax.c2p(0, 2), ax.c2p(-3, 2), stroke_width=0, fill_color=VERT, fill_opacity=0.15)
        ls = T("stable", sc=0.65, color=VERT).move_to(ax.c2p(-2.2, 1.6))
        cr = pos(T(r"tous les pôles : $\mathrm{Re}(p_i) < 0$", sc=0.72, color=VERT), 0.8, 0.3)
        self.at(self.t("b3"), Create(ax), FadeIn(lr), FadeIn(li), FadeIn(zone), FadeIn(ls), run_time=0.8)
        st = VGroup(croix(ax.c2p(-1.5, 0), col=VERT), croix(ax.c2p(-0.6, 1.2), col=VERT), croix(ax.c2p(-0.6, -1.2), col=VERT))
        self.at(self.a("b3", "tous les pôles"), FadeIn(st, scale=2), Ecrire(cr, rt=1.0), run_time=1.0)
        ins = croix(ax.c2p(0.8, 0.0), col=ROUGE); lin = pos(T(r"un seul pôle à droite : \textbf{instable}", sc=0.66, color=ROUGE), 0.8, -0.6)
        self.at(self.t("b4"), FadeIn(ins, scale=2), Ecrire(lin, rt=0.9), run_time=0.9)
        lim = VGroup(croix(ax.c2p(0, 1.6), col=ORANGE), croix(ax.c2p(0, -1.6), col=ORANGE))
        llm = pos(T(r"sur l'axe : oscillation entretenue", sc=0.66, color=ORANGE), 0.8, -1.5)
        self.at(self.a("b4", "Des pôles sur l'axe"), FadeIn(lim, scale=2), Ecrire(llm, rt=1.0), run_time=1.0)
        self.fin()

class S2(Cours):
    sid = "S2"
    def construct(self):
        self.entete(r"6.2 -- Boucler peut déstabiliser", "Stabilité")
        eq = pos(M(r"\text{pôles de la FTBF} : \; 1 + H_{BO}(p) = 0", sc=0.9, color=JAUNE), -6.3, 2.05)
        self.ecr(self.a("c1", "ce sont les pôles"), eq, rt=1.2)
        y = 0.95
        s = som(-5.0, y); g = blk(r"\frac{K}{(1 + p)^3}", -3.2, y, w=2.0, h=0.9)
        fs = [fl((-6.5, y), (-5.24, y)), fl((-4.76, y), (-4.2, y)), fl((-2.2, y), (-0.8, y))]
        r = fl((-1.5, y), (-1.5, y - 0.9), (-5.0, y - 0.9), (-5.0, y - 0.24), col=BLEU)
        self.at(self.t("c2"), *[Create(f) for f in fs], Create(s), Create(g[0]), FadeIn(g[1]), Create(r), run_time=1.0)
        ax = axes(2.7, -1.2, 7.6, 3.4, [0, 18, 2], [-0.4, 2.2, 1])
        lt = M("t", sc=0.65).next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        t = np.linspace(0, 17.8, 260)
        self.at(self.a("c2", "Bouclons-la"), Create(ax), FadeIn(lt), run_time=0.6)
        for K, col, ph, fr, lab, pp in [(2, VERT, "c3", "Avec K", r"K = 2", (15, 0.85)), (8, ORANGE, "c4", "Avec K", r"K = 8", (15.6, 2.0)), (10, ROUGE, "c5", "Et avec K", r"K = 10", (9.8, 2.05))]:
            cb = coupe(ax, t, bf3(K, t), col, -0.4, 2.2)
            l = M(lab, sc=0.65, color=col).move_to(ax.c2p(*pp))
            self.at(self.a(ph, fr), Create(cb), FadeIn(l), run_time=1.5)
        mm = VGroup(T(r"même système,", sc=0.68, color=ROUGE), T(r"juste plus de gain !", sc=0.68, color=ROUGE)).arrange(DOWN, aligned_edge=LEFT, buff=0.12); pos(mm, -6.3, -1.4)
        self.ecr(self.a("c5", "Le même système"), mm, rt=0.9)
        self.fin()

class S3(Cours):
    sid = "S3"
    def construct(self):
        self.entete(r"6.3 -- Les critères algébriques", "Stabilité")
        p = pos(M(r"a_n p^n + \cdots + a_1 p + a_0", sc=0.95, color=JAUNE), -6.3, 2.05)
        self.ecr(self.t("d1"), p, rt=0.9)
        c1 = pos(T(r"\textbf{nécessaire} : tous les $a_i > 0$ (un manquant ou négatif : instable)", sc=0.72, color=BLEU), -6.3, 1.15)
        self.ecr(self.t("d2"), c1, rt=1.2)
        c2 = pos(T(r"ordres $1$ et $2$ : c'est aussi \textbf{suffisant}", sc=0.72, color=VERT), -6.3, 0.45)
        c3 = pos(M(r"\text{ordre } 3 : \; a_i > 0 \;\text{ et }\; a_2\,a_1 > a_3\,a_0", sc=0.9, color=VERT), -6.3, -0.3)
        self.ecr(self.t("d3"), c2, rt=0.9); self.ecr(self.a("d3", "Pour l'ordre trois"), c3, rt=1.1); self.play(Create(enc(c3, col=VERT, buff=0.15)), run_time=0.4)
        ex = pos(M(r"(1 + p)^3 + K = p^3 + 3p^2 + 3p + 1 + K", sc=0.85), -6.3, -1.45)
        self.ecr(self.t("d4"), ex, rt=1.3)
        r = pos(M(r"3 \times 3 > 1 + K \;\Longrightarrow\; K < 8", sc=0.95, color=JAUNE), -6.3, -2.4)
        self.ecr(self.a("d4", "Il faut trois fois trois"), r, rt=1.0); self.play(Create(enc(r, col=JAUNE, buff=0.15)), run_time=0.4)
        w = pos(M(r"K = 8 : \; \omega = \sqrt{3}", sc=0.85, color=ORANGE), 2.0, -2.4)
        self.ecr(self.a("d5", "Et à K égale huit"), w, rt=0.8)
        self.fin()

class S4(Cours):
    sid = "S4"
    def construct(self):
        self.entete(r"6.4 -- Le point critique", "Critère du revers")
        t = pos(T(r"une méthode qui se lit sur la \textbf{boucle ouverte}, même mesurée", sc=0.75, color=GRIS), -6.3, 2.05)
        self.ecr(self.t("e1"), t, rt=1.1)
        pc = M(r"H_{BO}(j\omega) = -1 \;\iff\; 0\ \mathrm{dB} \;\text{ et }\; -180^\circ", sc=1.0, color=JAUNE).move_to([0, 1.0, 0])
        self.ecr(self.t("e2"), pc, rt=1.4); self.play(Create(enc(pc, col=JAUNE)), run_time=0.4)
        y = -0.85
        s = som(-5.0, y); g = blk(r"H_{BO}", -2.8, y, w=1.6)
        fs = [fl((-5.0 + 0.24, y), (-3.6, y)), fl((-2.0, y), (0.4, y))]
        r = fl((-0.6, y), (-0.6, y - 1.1), (-5.0, y - 1.1), (-5.0, y - 0.24), col=BLEU)
        m = M("-", sc=0.8).move_to([-5.35, y - 0.45, 0])
        self.at(self.t("e3"), Create(s), Create(g[0]), FadeIn(g[1]), *[Create(f) for f in fs], Create(r), FadeIn(m), run_time=1.0)
        ph = VGroup(T(r"$-180^\circ$ + signe $-$ :", sc=0.68, color=ORANGE), T(r"le signal revient \textbf{dans le même sens}", sc=0.68, color=ORANGE)).arrange(DOWN, buff=0.15).move_to([3.7, -0.85, 0])
        self.ecr(self.a("e3", "un signal fait le tour"), ph, rt=1.2)
        a1 = pos(T(r"revient \textbf{amplifié} : l'oscillation croît", sc=0.72, color=ROUGE), -6.3, -2.85)
        a2 = pos(T(r"revient \textbf{atténué} : elle s'éteint", sc=0.72, color=VERT), 1.2, -2.85)
        self.ecr(self.t("e4"), a1, rt=1.0); self.ecr(self.a("e4", "S'il revient atténué"), a2, rt=0.9)
        self.fin()

# FTBO d'illustration (différente de l'exercice) : 2 / (p (1 + p)(1 + 0,1 p))
Hi = lambda w: 2/(1j*w*(1 + 1j*w)*(1 + 0.1j*w))
def bode_illu(self, x, y, w=8.6, hg=2.3, hp=1.8):
    ag, fg = cadre(x, y + 1.25, w, hg, -1, 2, -60, 30)
    ap, fp = cadre(x, y - 1.05, w, hp, -1, 2, -270, -90)
    z0 = DashedLine(ag.c2p(-1, 0), ag.c2p(2, 0), color=GRIS, stroke_width=2); m180 = DashedLine(ap.c2p(-1, -180), ap.c2p(2, -180), color=GRIS, stroke_width=2)
    l0 = M(r"0\ \mathrm{dB}", sc=0.55, color=GRIS).next_to(ag.c2p(-1, 0), LEFT, buff=0.1); l180 = M(r"-180^\circ", sc=0.55, color=GRIS).next_to(ap.c2p(-1, -180), LEFT, buff=0.1)
    cg = crb(ag, lambda w: dB(Hi(w)), -1, 2); cp = crb(ap, lambda w: -90 - np.degrees(np.arctan(w)) - np.degrees(np.arctan(0.1*w)), -1, 2)
    return ag, ap, VGroup(fg, fp, z0, m180, l0, l180), cg, cp

class S5(Cours):
    sid = "S5"
    def construct(self):
        self.entete(r"6.5 -- Le critère du revers", "Critère du revers")
        t = pos(T(r"boucle ouverte stable, Bode de la FTBO", sc=0.72, color=GRIS), -6.3, 2.1)
        ag, ap, dec, cg, cp = bode_illu(self, -2.1, -0.6, w=7.4)
        self.at(self.t("f1"), Ecrire(t, rt=0.9), FadeIn(dec), Create(cg), Create(cp), run_time=1.2)
        from scipy.optimize import brentq
        wc = brentq(lambda w: abs(Hi(w)) - 1, 0.3, 10); phc = -90 - np.degrees(np.arctan(wc)) - np.degrees(np.arctan(0.1*wc))
        v = DashedLine(ag.c2p(np.log10(wc), 0), ap.c2p(np.log10(wc), phc), color=JAUNE, stroke_width=3)
        d1 = Dot(ag.c2p(np.log10(wc), 0), color=JAUNE, radius=0.09); lw = M(r"\omega_{c0}", sc=0.65, color=JAUNE).next_to(d1, DL, buff=0.08)
        self.at(self.t("f2"), FadeIn(d1, scale=2), FadeIn(lw), Create(v), run_time=0.8)
        d2 = Dot(ap.c2p(np.log10(wc), phc), color=VERT, radius=0.09)
        ok = VGroup(T(r"phase au-dessus de $-180^\circ$ :", sc=0.64, color=VERT), T(r"\textbf{stable}", sc=0.64, color=VERT)).arrange(DOWN, buff=0.1).move_to([4.6, 0.2, 0])
        ko = T(r"en dessous : \textbf{instable}", sc=0.64, color=ROUGE).move_to([4.6, -0.75, 0])
        self.at(self.a("f3", "Si, à cette pulsation"), FadeIn(d2, scale=2), Ecrire(ok, rt=1.0), run_time=1.0)
        self.ecr(self.a("f3", "En dessous"), ko, rt=0.7)
        wpi = 1/np.sqrt(0.1)
        d3 = Dot(ap.c2p(np.log10(wpi), -180), color=ORANGE, radius=0.09); d4 = Dot(ag.c2p(np.log10(wpi), dB(Hi(wpi))), color=ORANGE, radius=0.09)
        v2 = DashedLine(ap.c2p(np.log10(wpi), -180), ag.c2p(np.log10(wpi), dB(Hi(wpi))), color=ORANGE, stroke_width=3)
        eq = VGroup(T(r"ou : gain $< 0$ dB", sc=0.64, color=ORANGE), T(r"là où $\varphi = -180^\circ$", sc=0.64, color=ORANGE)).arrange(DOWN, buff=0.1).move_to([4.6, -1.9, 0])
        self.at(self.t("f4"), FadeIn(d3, scale=2), Create(v2), FadeIn(d4, scale=2), Ecrire(eq, rt=1.0), run_time=1.0)
        self.fin()

class S6(Cours):
    sid = "S6"
    def construct(self):
        self.entete(r"6.6 -- Les marges de stabilité", "Marges")
        t = pos(T(r"stable \ldots{} avec de la \textbf{marge}", sc=0.75, color=GRIS), -6.3, 2.1)
        self.ecr(self.t("g1"), t, rt=0.8)
        ag, ap, dec, cg, cp = bode_illu(self, -1.6, -0.6, w=7.6)
        self.play(FadeIn(dec), Create(cg), Create(cp), run_time=1.0)
        from scipy.optimize import brentq
        wc = brentq(lambda w: abs(Hi(w)) - 1, 0.3, 10); phc = -90 - np.degrees(np.arctan(wc)) - np.degrees(np.arctan(0.1*wc))
        mp = Arrow(ap.c2p(np.log10(wc), -180), ap.c2p(np.log10(wc), phc), color=VERT, buff=0, stroke_width=5, max_tip_length_to_length_ratio=0.3)
        lmp = M(r"M_\varphi", sc=0.7, color=VERT).next_to(mp, LEFT, buff=0.1)
        fmp = pos(M(r"M_\varphi = 180^\circ + \arg H_{BO}(j\omega_{c0})", sc=0.72, color=VERT), 2.6, 1.0)
        self.at(self.a("g2", "La marge de phase"), GrowArrow(mp), FadeIn(lmp), run_time=0.7); self.ecr(self.a("g2", "M phi égale"), fmp, rt=1.2)
        wpi = 1/np.sqrt(0.1); gpi = dB(Hi(wpi))
        mg = Arrow(ag.c2p(np.log10(wpi), gpi), ag.c2p(np.log10(wpi), 0), color=ORANGE, buff=0, stroke_width=5, max_tip_length_to_length_ratio=0.3)
        lmg = M(r"M_G", sc=0.7, color=ORANGE).next_to(mg, RIGHT, buff=0.1)
        fmg = pos(M(r"M_G = -20\log|H_{BO}(j\omega_\pi)|", sc=0.72, color=ORANGE), 2.6, 0.2)
        self.at(self.t("g3"), GrowArrow(mg), FadeIn(lmg), run_time=0.7); self.ecr(self.a("g3", "l'écart du gain"), fmg, rt=1.1)
        vu = VGroup(T(r"usuel : $M_\varphi \geq 45^\circ$,", sc=0.66, color=JAUNE), T(r"$M_G$ de $6$ à $10$ dB", sc=0.66, color=JAUNE)).arrange(DOWN, aligned_edge=LEFT, buff=0.12); pos(vu, 2.6, -0.95)
        self.ecr(self.t("g4"), vu, rt=1.1); self.play(Create(enc(vu, col=JAUNE, buff=0.12)), run_time=0.4)
        asu = VGroup(T(r"assurances contre :", sc=0.62, color=GRIS), T(r"gain qui dérive, retard,", sc=0.62, color=GRIS), T(r"constante oubliée", sc=0.62, color=GRIS)).arrange(DOWN, aligned_edge=LEFT, buff=0.1); pos(asu, 2.6, -2.45)
        self.ecr(self.t("g5"), asu, rt=1.1)
        self.fin()

class S7(Cours):
    sid = "S7"
    def construct(self):
        self.entete(r"6.7 -- Marge de phase et amortissement", "Marges")
        r = M(r"\xi \approx \frac{M_\varphi\,(^\circ)}{100}", sc=1.2, color=JAUNE).move_to([0, 1.65, 0])
        self.ecr(self.a("h1", "ksi vaut environ"), r, rt=1.0); self.play(Create(enc(r, col=JAUNE)), run_time=0.4)
        t = np.linspace(0, 12, 200)
        for k, (mp, z, txt, col, fr) in enumerate([(45, 0.42, r"45^\circ : \approx 20\,\%", ROUGE, "Quarante-cinq"), (60, 0.61, r"60^\circ : \approx 10\,\%", ORANGE, "Soixante degrés"), (70, 0.8, r"70^\circ : \approx 0", VERT, "Soixante-dix")]):
            cx = -4.3 + 4.3*k
            ax = axes(cx, -1.0, 3.6, 2.2, [0, 12, 3], [0, 1.4, 1])
            _, y = signal.step(signal.lti([1], [1, 2*z, 1]), T=t)
            cb = VMobject(color=col, stroke_width=4).set_points_smoothly([ax.c2p(a, b) for a, b in zip(t, y)])
            fin = DashedLine(ax.c2p(0, 1), ax.c2p(12, 1), color=GRIS, stroke_width=2)
            lb = M(txt, sc=0.72, color=col).move_to([cx, -2.5, 0])
            self.at(self.a("h2", fr), Create(ax), Create(fin), Create(cb), FadeIn(lb), run_time=1.0)
        at = T(r"marge faible, même positive : réponse très oscillante !", sc=0.72, color=ROUGE).move_to([0, -3.25, 0])
        self.ecr(self.t("h3"), at, rt=1.1)
        self.fin()

class S8(Cours):
    sid = "S8"
    def construct(self):
        self.entete(r"6.8 -- À vous : régler un gain", "Exercice")
        h = M(r"H_{BO}(p) = \frac{K}{p\,(1 + 0{,}5p)} \qquad M_\varphi = 45^\circ \;?", sc=1.0, color=JAUNE).move_to([-0.8, 1.9, 0])
        self.ecr(self.a("i1", "F T B O"), h, rt=1.2)
        pa, arc = chrono(5.0, 1.9)
        self.at(self.a("i1", "Mettez sur pause"), FadeIn(pa), Create(arc), run_time=0.5)
        self.play(Uncreate(arc), run_time=2.6); self.play(FadeOut(pa), run_time=0.2)
        a = pos(M(r"\varphi = -90^\circ - \arctan(0{,}5\,\omega) = -135^\circ", sc=0.88), -6.3, 0.5)
        self.ecr(self.t("i2"), a, rt=1.3)
        b = pos(M(r"\arctan(0{,}5\,\omega) = 45^\circ \;\Rightarrow\; \omega_{c0} = 2\ \mathrm{rad/s}", sc=0.88), -6.3, -0.6)
        self.ecr(self.t("i3"), b, rt=1.2)
        c = M(r"\frac{K}{2\sqrt{2}} = 1 \;\Rightarrow\; K = 2\sqrt{2} \approx 2{,}8", sc=1.0, color=JAUNE).move_to([-0.8, -2.1, 0])
        self.ecr(self.t("i4"), c, rt=1.2); self.play(Create(enc(c, col=JAUNE)), run_time=0.4)
        self.fin()

class S9(Cours):
    sid = "S9"
    def construct(self):
        self.entete(r"6.9 -- L'effet du gain", "Gain et retard")
        ag, ap, dec, cg, cp = bode_illu(self, -1.6, -0.6, w=7.6)
        self.at(self.t("j1"), FadeIn(dec), Create(cg), Create(cp), run_time=1.0)
        cg2 = crb(ag, lambda w: dB(3*Hi(w)), -1, 2, col=ROUGE)
        fl_ = Arrow(ag.c2p(-0.5, dB(Hi(10**-0.5))), ag.c2p(-0.5, dB(3*Hi(10**-0.5))), color=ROUGE, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.35)
        tk = VGroup(T(r"$K \times 3$ : courbe de gain", sc=0.62, color=ROUGE), T(r"translatée vers le haut", sc=0.62, color=ROUGE)).arrange(DOWN, buff=0.08).move_to([4.6, 1.65, 0])
        self.at(self.a("j1", "translate la courbe"), Create(cg2), GrowArrow(fl_), Ecrire(tk, rt=0.9), run_time=1.0)
        ph = T(r"la phase ne bouge pas", sc=0.64, color=BLEU).move_to([4.6, 0.85, 0])
        self.ecr(self.a("j1", "La phase"), ph, rt=0.7)
        o1 = T(r"$\omega_{c0} \nearrow$ : plus rapide", sc=0.66, color=VERT).move_to([4.6, 0.0, 0])
        o2 = T(r"$M_\varphi \searrow$ : moins amorti", sc=0.66, color=ROUGE).move_to([4.6, -0.6, 0])
        self.ecr(self.t("j2"), o1, rt=0.8); self.ecr(self.a("j2", "la marge de phase fond"), o2, rt=0.8)
        kl = M(r"K_{lim} = K \cdot 10^{M_G/20}", sc=0.85, color=JAUNE).move_to([4.6, -1.8, 0])
        self.ecr(self.a("j3", "Le gain limite"), kl, rt=1.0); self.play(Create(enc(kl, col=JAUNE, buff=0.15)), run_time=0.4)
        self.fin()

class S10(Cours):
    sid = "S10"
    def construct(self):
        self.entete(r"6.10 -- Le danger du retard", "Gain et retard")
        r = pos(M(r"e^{-Tp} : \; |\cdot| = 1, \qquad \varphi = -\omega T\ (\mathrm{rad})", sc=0.95, color=BLEU), -6.3, 2.0)
        self.ecr(self.t("k1"), r, rt=1.2)
        m = pos(M(r"M_\varphi \;\longrightarrow\; M_\varphi - \omega_{c0}\,T", sc=0.95), -6.3, 0.85)
        self.ecr(self.t("k2"), m, rt=1.0)
        tm = M(r"T_{max} = \frac{M_\varphi\ (\mathrm{rad})}{\omega_{c0}}", sc=1.15, color=JAUNE).move_to([3.0, 0.85, 0])
        self.ecr(self.a("k2", "Le retard maximal"), tm, rt=1.1); self.play(Create(enc(tm, col=JAUNE)), run_time=0.4)
        ex = pos(M(r"45^\circ = 0{,}785\ \mathrm{rad}, \;\; \omega_{c0} = 10\ \mathrm{rad/s} \;\Rightarrow\; T_{max} \approx 79\ \mathrm{ms}", sc=0.88, color=ORANGE), -6.3, -0.75)
        self.ecr(self.t("k3"), ex, rt=1.5)
        c = T(r"boucle rapide $\Rightarrow$ retard toléré \textbf{petit}", sc=0.8, color=ROUGE).move_to([0, -2.2, 0])
        self.ecr(self.t("k4"), c, rt=1.0); self.play(Create(enc(c)), run_time=0.4)
        self.fin()

class S11(Cours):
    sid = "S11"
    def construct(self):
        self.entete(r"À retenir", "Bilan")
        pts = [("l1", r"Stable $\iff$ tous les pôles de la FTBF à partie réelle $< 0$", BLEU),
               ("l2", r"Ordre $3$ : coefficients $> 0$ et $a_2a_1 > a_3a_0$", VERT),
               ("l3", r"Critère du revers : phase $> -180^\circ$ là où le gain vaut $0$ dB", ORANGE),
               ("l4", r"Marges : $45^\circ$ et $6$ à $10$ dB ; gain et retard les rongent", JAUNE)]
        for k, (ph, txt, c) in enumerate(pts):
            yy = 1.8 - 1.3*k
            ca = carte(k+1, c, -5.9, yy); tx = pos(T(txt, sc=0.74), -5.35, yy)
            self.at(self.t(ph), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        self.fin()

He = lambda w, K=4: K/(1j*w*(1 + 0.5j*w)*(1 + 0.05j*w))
class S12(Cours):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice résolu -- l'énoncé", "Application")
        y = 1.6
        s = som(-4.6, y); g = blk(r"\frac{K}{p\,(1 + 0{,}5p)(1 + 0{,}05p)}", -1.9, y, w=3.8, h=0.95)
        fs = [fl((-6.2, y), (-4.84, y)), fl((-4.36, y), (-3.8, y)), fl((0.0, y), (1.8, y))]
        r = fl((1.1, y), (1.1, y - 1.1), (-4.6, y - 1.1), (-4.6, y - 0.24), col=BLEU)
        k = M(r"K = 4", sc=0.85, color=JAUNE).move_to([3.4, y, 0])
        self.at(self.a("m1", "Une F T B O"), *[Create(f) for f in fs], Create(s), Create(g[0]), FadeIn(g[1]), Create(r), run_time=1.0)
        self.at(self.a("m1", "Avec K égale quatre"), FadeIn(k), run_time=0.4)
        qs = [(r"marges de phase et de gain ?", "les marges"), (r"gain limite de stabilité ?", "Le gain limite"), (r"quel $K$ pour $M_\varphi = 45^\circ$ ?", "Et quel K")]
        for i, (q, fr) in enumerate(qs):
            m = pos(T(q, sc=0.78, color=ROUGE), -5.4, -0.55 - 0.65*i)
            self.at(self.a("m2", fr), Create(carte(i+1, ROUGE, -6.0, -0.55 - 0.65*i)), Ecrire(m, rt=0.8), run_time=0.8)
        rf = pos(T(r"Réfléchissons : marges sur la boucle ouverte ; $\omega_{c0}$, puis $\omega_\pi$", sc=0.72, color=BLEU), -6.3, -2.85)
        self.ecr(self.t("m3"), rf, rt=1.2)
        self.fin()

class S13(Cours):
    sid = "S13"
    def construct(self):
        self.entete(r"Exercice résolu -- la solution", "Application")
        def etape(k, c, y, m, ph, fr, rt=1.0):
            ca = carte(k, c, -6.35, y); mm = pos(m, -5.85, y)
            self.at(self.a(ph, fr), Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
            return mm
        ag, fg = cadre(4.4, 1.0, 4.6, 1.9, -1, 2, -60, 40)
        ap, fp = cadre(4.4, -1.2, 4.6, 1.6, -1, 2, -270, -90)
        z0 = DashedLine(ag.c2p(-1, 0), ag.c2p(2, 0), color=GRIS, stroke_width=2); m180 = DashedLine(ap.c2p(-1, -180), ap.c2p(2, -180), color=GRIS, stroke_width=2)
        cg = crb(ag, lambda w: dB(He(w)), -1, 2); cp = crb(ap, lambda w: -90 - np.degrees(np.arctan(0.5*w)) - np.degrees(np.arctan(0.05*w)), -1, 2)
        etape(1, BLEU, 2.15, M(r"|H_{BO}(j\omega_{c0})| = 1 \;\Rightarrow\; \omega_{c0} \approx 2{,}5\ \mathrm{rad/s}", sc=0.72), "n1", "Première étape", 1.2)
        self.play(Create(fg), Create(fp), Create(z0), Create(m180), Create(cg), Create(cp), run_time=1.0)
        wc = 2.487; phc = -148.3
        mp = Arrow(ap.c2p(np.log10(wc), -180), ap.c2p(np.log10(wc), phc), color=VERT, buff=0, stroke_width=5, max_tip_length_to_length_ratio=0.3)
        r1 = pos(M(r"\varphi \approx -148^\circ \;\Rightarrow\; M_\varphi \approx 32^\circ", sc=0.75, color=ORANGE), -5.85, 1.35)
        self.at(self.t("n2"), Ecrire(r1, rt=1.1), GrowArrow(mp), run_time=1.1)
        pm = pos(T(r"stable, mais trop peu amorti", sc=0.62, color=ORANGE), -5.85, 0.8)
        self.ecr(self.a("n2", "Stable, mais"), pm, rt=0.7)
        etape(2, VERT, 0.05, M(r"0{,}5\,\omega \cdot 0{,}05\,\omega = 1 \;\Rightarrow\; \omega_\pi = \sqrt{40} \approx 6{,}3", sc=0.72), "n3", "Deuxième étape", 1.3)
        wpi = np.sqrt(40); gpi = dB(He(wpi))
        mg = Arrow(ag.c2p(np.log10(wpi), gpi), ag.c2p(np.log10(wpi), 0), color=ORANGE, buff=0, stroke_width=5, max_tip_length_to_length_ratio=0.3)
        r2 = pos(M(r"G(\omega_\pi) = -14{,}8\ \mathrm{dB} \;\Rightarrow\; M_G \approx 15\ \mathrm{dB}", sc=0.75, color=VERT), -5.85, -0.7)
        self.at(self.t("n4"), Ecrire(r2, rt=1.1), GrowArrow(mg), run_time=1.1)
        etape(3, ORANGE, -1.5, M(r"K_{lim} = 4 \times 10^{14{,}8/20} = 22", sc=0.75), "n5", "Troisième étape", 1.0)
        etape(4, ROUGE, -2.35, M(r"\varphi = -135^\circ \text{ en } \omega \approx 1{,}69 \;\Rightarrow\; K \approx 2{,}2", sc=0.72), "n6", "Quatrième étape", 1.3)
        dv = T(r"il faut presque diviser le gain par deux !", sc=0.66, color=ROUGE).move_to([-2.3, -3.05, 0])
        self.ecr(self.a("n7", "Il faut presque"), dv, rt=0.9)
        bi = T(r"Bilan : il faudra un \textbf{correcteur}", sc=0.66, color=VERT).move_to([4.4, -2.55, 0])
        self.ecr(self.t("n8"), bi, rt=0.9)
        nx = T(r"Prochain chapitre : précision et rapidité", sc=0.6, color=GRIS).move_to([4.4, -3.15, 0])
        self.at(self.t("n9"), FadeIn(nx), run_time=0.6)
        self.fin()
