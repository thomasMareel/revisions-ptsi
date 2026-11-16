from base import *
import os
APERCU = os.environ.get("APERCU")   # contrôle d'une scène en image fixe (pas d'effacement final)

# ---------- outils communs (repris des chapitres précédents)
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
def crb(ax, f, a, b, col=ORANGE, sw=4, n=160):
    u = np.linspace(a, b, n)
    return VMobject(color=col, stroke_width=sw).set_points_smoothly([ax.c2p(s, f(s)) for s in u])
def zero(ax, a, b): return DashedLine(ax.c2p(a, 0), ax.c2p(b, 0), color=GRIS, stroke_width=1.5, dash_length=0.08)
def P(x, y): return np.array([x, y, 0.0])
def fleche(a, b, col=ROUGE, sw=4, tl=0.18):
    return Arrow(P(*a), P(*b), buff=0, color=col, stroke_width=sw, tip_length=tl, max_tip_length_to_length_ratio=0.5, max_stroke_width_to_length_ratio=20)
def sep(y): return Line([-6.6, y, 0], [6.6, y, 0], color=GRIS, stroke_width=1.5, stroke_opacity=0.5)
def coche(x, y, col=VERT):
    return VMobject(color=col, stroke_width=6).set_points_as_corners([P(x - 0.16, y), P(x - 0.04, y - 0.13), P(x + 0.18, y + 0.18)])

# ---------- dessins d'électromagnétisme
def odot(x, y, col=BLEU, r=0.14):
    """vecteur sortant du tableau"""
    return VGroup(Circle(radius=r, color=col, stroke_width=3).move_to(P(x, y)), Dot(P(x, y), radius=0.045, color=col))
def otimes(x, y, col=BLEU, r=0.14):
    """vecteur entrant dans le tableau"""
    d = r*0.68
    return VGroup(Circle(radius=r, color=col, stroke_width=3).move_to(P(x, y)),
                  Line(P(x - d, y - d), P(x + d, y + d), color=col, stroke_width=3), Line(P(x - d, y + d), P(x + d, y - d), color=col, stroke_width=3))
def repere_cyl(x, y, l=0.55, col=GRIS):
    """e_z vers la droite, e_r vers le haut (point au-dessus de l'axe), e_theta sortant"""
    az = fleche((x, y), (x + l, y), col=col, sw=3, tl=0.12); ar = fleche((x, y), (x, y + l), col=col, sw=3, tl=0.12)
    lz = M(r"\vec e_z", sc=0.5, color=col).next_to(az.get_end(), RIGHT, buff=0.06)
    lr = M(r"\vec e_r", sc=0.5, color=col).next_to(ar.get_end(), UP, buff=0.05)
    th = odot(x, y, col=col, r=0.1); lt = M(r"\vec e_\theta", sc=0.5, color=col).next_to(th, DL, buff=0.03)
    return VGroup(az, ar, lz, lr, th, lt)
def condo(xg, xd, yc, h, col=CRAIE):
    """condensateur plan vu de côté : axe Oz horizontal, armatures verticales"""
    g = Line(P(xg, yc - h/2), P(xg, yc + h/2), color=col, stroke_width=8)
    d = Line(P(xd, yc - h/2), P(xd, yc + h/2), color=col, stroke_width=8)
    ax_ = DashedLine(P(xg - 0.55, yc), P(xd + 0.55, yc), color=GRIS, stroke_width=1.5, dash_length=0.08)
    return VGroup(g, d), ax_
def fil(x0, x1, y, h, col=CRAIE):
    """fil cylindrique vu de côté"""
    r = Rectangle(width=x1 - x0, height=h, color=col, stroke_width=3).set_fill(ORANGE, 0.12).move_to(P((x0 + x1)/2, y))
    e1 = Ellipse(width=0.22, height=h, color=col, stroke_width=2).move_to(P(x1, y))
    return VGroup(r, e1)

class C(Cours):
    def etape(self, k, col, y, m, t, rt=1.0, x=-6.35):
        ca = carte(k, col, x, y); mm = pos(m, x + 0.5, y)
        self.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
        return mm
    def pause5(self, t, x, y):
        pa, arc = chrono(x, y)
        self.at(t, FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
    def rappel(self, txt):
        r = pos(T(txt, sc=0.54, color=GRIS), 6.6, 2.72, bord=RIGHT)
        self.play(FadeIn(r), run_time=0.4)
    def fin(self):
        if APERCU: self.wait(0.1); return
        super().fin()

# ---------------------------------------------------------------- S0
class S0(C):
    sid = "S0"
    def construct(self):
        sur = T(r"PHYSIQUE \;·\; PT", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Électromagnétisme -- Chapitre 3}", sc=1.1, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Équations de Maxwell, ARQS et énergie électromagnétique", sc=0.78).move_to([0, 1.75, 0])
        tr = Line([-5.4, 1.3, 0], [5.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        # un fil parcouru par un courant : l'énergie entre par le côté
        x0, x1, yf, h = 2.85, 6.3, -0.85, 0.5
        fl = fil(x0, x1, yf, h)
        fi = fleche((x0 + 0.25, yf), (x0 + 1.25, yf), col=ORANGE, sw=4, tl=0.15); lI = M(r"I", sc=0.6, color=ORANGE).move_to(P(x0 - 0.3, yf))
        pis = [fleche((x, yf + 1.05), (x, yf + 0.32), col=ROUGE, sw=4, tl=0.16) for x in (3.9, 4.75, 5.6)]
        pis += [fleche((x, yf - 1.05), (x, yf - 0.32), col=ROUGE, sw=4, tl=0.16) for x in (3.9, 4.75, 5.6)]
        lp = M(r"\vec\Pi", sc=0.65, color=ROUGE).move_to(P(3.45, yf + 0.75))
        bh, bb = odot(6.0, yf + 0.62), otimes(6.0, yf - 0.62)
        lb = M(r"\vec B", sc=0.6, color=BLEU).move_to(P(6.45, yf + 0.62))
        self.at(self.a("a1", "place aux équations"), Create(fl), GrowArrow(fi), FadeIn(lI), run_time=0.8)
        self.play(*[GrowArrow(p) for p in pis], FadeIn(lp), FadeIn(bh), FadeIn(bb), FadeIn(lb), run_time=0.9)
        items = []
        for k, (txt, col) in enumerate([("Les équations de Maxwell", BLEU), ("ARQS magnétique et loi d'Ohm locale", VERT),
                                         ("Énergie électromagnétique", ORANGE), ("Exercice 1 : une sphère qui se décharge", ROUGE),
                                         ("Exercice 2 : un condensateur en régime sinusoïdal", BLEU), ("Exercice 3 : un fil chauffant", JAUNE)]):
            yy = 0.75 - 0.6*k
            items.append(VGroup(carte(k+1, col, -6.2, yy), pos(T(txt, sc=0.68), -5.65, yy)))
        for it, (sid, fr_) in zip(items, [("a3", "les quatre équations"), ("a3", "l'A R Q S magnétique"), ("a3", "l'énergie électromagnétique"),
                                          ("a4", "une sphère"), ("a4", "un condensateur"), ("a4", "un fil chauffant")]):
            self.jusqua(self.a(sid, fr_)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

# ---------------------------------------------------------------- S1
class S1(C):
    sid = "S1"
    def construct(self):
        self.entete(r"3.1 -- Les quatre équations de Maxwell", "Cours")
        so = pos(T(r"sources : $\rho$ ($\mathrm{C\,m^{-3}}$) et $\vec j$ ($\mathrm{A\,m^{-2}}$) \; $\longrightarrow$ \; champs $\vec E(M,t)$ et $\vec B(M,t)$", sc=0.64, color=GRIS), -6.3, 2.3)
        self.ecr(self.t("b1"), so, rt=1.2)
        # grille 2 x 2 : (MG) (MΦ) en haut, (MF) (MA) en bas
        def cell(x0, y, tag, col, f, sens):
            tg = pos(T(r"\textbf{" + tag + "}", sc=0.64, color=col), x0, y)
            ff = pos(f, x0 + 1.15, y); ss = pos(T(sens, sc=0.6), x0 + 1.15, y - 0.78)
            return tg, ff, ss
        mg = cell(-6.3, 1.4, "(MG)", BLEU, M(r"\operatorname{div}\vec E=\frac{\rho}{\varepsilon_0}", sc=0.8), r"les charges sont les sources de $\vec E$")
        mf_ = cell(0.55, 1.4, r"(M$\Phi$)", VERT, M(r"\operatorname{div}\vec B=0", sc=0.8), r"pas de charge magnétique")
        mfa = cell(-6.3, -0.35, "(MF)", ORANGE, M(r"\overrightarrow{\operatorname{rot}}\,\vec E=-\frac{\partial\vec B}{\partial t}", sc=0.8), r"$\vec B$ variable crée $\vec E$ : l'\textbf{induction}")
        ma = cell(0.55, -0.35, "(MA)", ROUGE, M(r"\overrightarrow{\operatorname{rot}}\,\vec B=\mu_0\,\vec j+", r"\mu_0\varepsilon_0\,\frac{\partial\vec E}{\partial t}", sc=0.8),
                  r"courants \textbf{et} $\vec E$ variable créent $\vec B$")
        for (tg, ff, ss), ph_, f1, f2 in [(mg, "b2", "divergence de E", "Les charges sont"), (mf_, "b3", "divergence de B", "Pas de charge"),
                                          (mfa, "b4", "rotationnel de E", "Un champ B variable"), (ma, "b5", "rotationnel de B", "plus mu zéro epsilon")]:
            self.at(self.a(ph_, f1), FadeIn(tg), Ecrire(ff, rt=0.9), run_time=0.9)
            self.ecr(self.a(ph_, f2), ss, rt=0.8)
        vl = Line([0.25, 2.0, 0], [0.25, -1.4, 0], color=GRIS, stroke_width=1.5, stroke_opacity=0.4)
        hl = Line([-6.4, 0.3, 0], [6.6, 0.3, 0], color=GRIS, stroke_width=1.5, stroke_opacity=0.4)
        self.play(Create(vl), Create(hl), run_time=0.4)
        # courant de déplacement
        bx = enc(ma[1][1], col=ORANGE, buff=0.07)
        jd = pos(M(r"\vec j_D=\varepsilon_0\,\frac{\partial\vec E}{\partial t}", sc=0.8, color=ORANGE), -6.3, -1.98)
        self.at(self.t("b6"), Create(bx), run_time=0.5)
        self.ecr(self.a("b6", "est le courant de déplacement"), jd, rt=0.8)
        jt = pos(T(r"\textbf{courant de déplacement} ($\mathrm{A\,m^{-2}}$) : aucune charge ne bouge !", sc=0.62, color=ORANGE), -3.6, -1.98)
        self.ecr(self.a("b6", "Aucune charge"), jt, rt=1.0)
        cp = T(r"\textbf{couplage} : $\partial_t\vec B \to \vec E$ (MF) \quad et \quad $\partial_t\vec E \to \vec B$ (MA) \quad $\Rightarrow$ \quad ondes", sc=0.66, color=JAUNE).move_to([0, -2.72, 0])
        self.at(self.t("b7"), Indicate(mfa[1], color=JAUNE), run_time=0.7)
        self.at(self.a("b7", "E variable crée B"), Indicate(ma[1][1], color=JAUNE), run_time=0.7)
        self.ecr(self.a("b7", "l'origine des ondes") - 0.6, cp, rt=1.2)
        k1 = pos(M(r"\varepsilon_0\approx8{,}85\times10^{-12}\ \mathrm{F\,m^{-1}}", sc=0.66, color=GRIS), -6.3, -3.38)
        k2 = M(r"\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}", sc=0.66, color=GRIS).next_to(k1, RIGHT, buff=0.7)
        self.at(self.t("b8"), Ecrire(k1, rt=0.8), Ecrire(k2, rt=0.8), run_time=0.8)
        k3 = M(r"\mu_0\,\varepsilon_0\,c^2=1", sc=0.74, color=JAUNE).next_to(k2, RIGHT, buff=0.8)
        self.ecr(self.a("b8", "mu zéro epsilon"), k3, rt=0.7); self.play(Create(enc(k3, col=JAUNE, buff=0.1)), run_time=0.4)
        self.fin()

# ---------------------------------------------------------------- S2
class S2(C):
    sid = "S2"
    def construct(self):
        self.entete(r"3.2 -- Formes intégrales et conservation de la charge", "Cours")
        # surface fermée Σ et contour orienté Γ
        cx, cy, rs = -5.6, 1.45, 0.6
        sg = Circle(radius=rs, color=CRAIE, stroke_width=3).set_fill(GRIS, 0.18).move_to(P(cx, cy))
        lsg = M(r"\Sigma", sc=0.6).move_to(P(cx - 0.82, cy + 0.42)); lv = M(r"V", sc=0.55, color=GRIS).move_to(P(cx, cy))
        u = np.array([np.cos(0.75), np.sin(0.75)])
        ne = fleche(tuple(np.array([cx, cy]) + rs*u), tuple(np.array([cx, cy]) + (rs + 0.62)*u), col=VERT, sw=3, tl=0.14)
        lne = M(r"\vec n_{ext}", sc=0.55, color=VERT).next_to(ne.get_end(), UP, buff=0.04)
        gx, gy = -5.6, -0.4
        gam = Ellipse(width=1.7, height=0.62, color=CRAIE, stroke_width=3).set_fill(GRIS, 0.18).move_to(P(gx, gy))
        sens = fleche((gx - 0.12, gy - 0.31), (gx + 0.14, gy - 0.31), col=CRAIE, sw=3, tl=0.16)
        nn = fleche((gx, gy), (gx, gy + 0.85), col=VERT, sw=3, tl=0.14); lnn = M(r"\vec n", sc=0.55, color=VERT).next_to(nn.get_end(), RIGHT, buff=0.06)
        lga = M(r"\Gamma", sc=0.6).move_to(P(gx - 1.05, gy - 0.1)); ls = M(r"S", sc=0.5, color=GRIS).move_to(P(gx + 0.45, gy + 0.05))
        X0, XF = -3.75, -2.85
        def ligne(y, tag, col, f, nom):
            tg = pos(T(r"\textbf{" + tag + "}", sc=0.6, color=col), X0, y); ff = pos(f, XF, y)
            nm = T(nom, sc=0.58, color=GRIS).next_to(ff, RIGHT, buff=0.35)
            return tg, ff, nm
        g1 = ligne(2.05, "(MG)", BLEU, M(r"\iint_\Sigma\vec E\cdot\vec n_{ext}\,\mathrm dS=\frac{Q_{int}}{\varepsilon_0}", sc=0.74), "Gauss")
        g2 = ligne(1.1, r"(M$\Phi$)", VERT, M(r"\iint_\Sigma\vec B\cdot\vec n_{ext}\,\mathrm dS=0", sc=0.74), "flux conservatif")
        g3 = ligne(0.15, "(MF)", ORANGE, M(r"\oint_\Gamma\vec E\cdot\mathrm d\vec\ell=-\frac{\mathrm d\Phi_B}{\mathrm dt}", sc=0.74), "Faraday")
        g4 = ligne(-0.8, "(MA)", ROUGE, M(r"\oint_\Gamma\vec B\cdot\mathrm d\vec\ell=\mu_0\,I_{\text{enlacé}}+\mu_0\varepsilon_0\,\frac{\mathrm d\Phi_E}{\mathrm dt}", sc=0.74), "Ampère généralisé")
        self.at(self.t("c1"), Create(sg), FadeIn(lsg), FadeIn(lv), run_time=0.6)
        self.at(self.a("c1", "un rotationnel"), Create(gam), FadeIn(lga), FadeIn(ls), GrowArrow(sens), run_time=0.7)
        for (tg, ff, nm), ph_, fr_ in [(g1, "c2", "le flux sortant de E"), (g2, "c3", None), (g3, "c4", "la circulation de E"), (g4, "c5", "le théorème d'Ampère généralisé")]:
            t0 = self.a(ph_, fr_) if fr_ else self.t(ph_)
            self.at(t0, FadeIn(tg), Ecrire(ff, rt=1.0), run_time=1.0)
            self.play(FadeIn(nm), run_time=0.3)
        fb = pos(M(r"\Phi_B=\iint_S\vec B\cdot\vec n\,\mathrm dS", sc=0.56, color=GRIS), -6.45, -1.25)
        self.play(FadeIn(fb), run_time=0.4)
        self.at(self.a("c6", "normale sortante"), GrowArrow(ne), FadeIn(lne), run_time=0.6)
        mdr = T(r"main droite", sc=0.5, color=VERT).next_to(lnn, RIGHT, buff=0.12)
        self.at(self.a("c6", "main droite"), GrowArrow(nn), FadeIn(lnn), FadeIn(mdr), Indicate(sens, color=JAUNE, scale_factor=1.6), run_time=0.8)
        # conservation de la charge
        self.play(Create(sep(-1.6)), run_time=0.3)
        cc = pos(T(r"\textbf{Conservation de la charge} :", sc=0.7, color=VERT), -6.3, -2.15)
        fc = M(r"\frac{\partial\rho}{\partial t}+\operatorname{div}\vec j=0", sc=0.9, color=JAUNE).next_to(cc, RIGHT, buff=0.35)
        self.at(self.a("c7", "la conservation de la charge"), Ecrire(cc, rt=0.7), Ecrire(fc, rt=0.9), run_time=0.9)
        self.play(Create(enc(fc, col=JAUNE, buff=0.12)), run_time=0.4)
        vx, vy = 5.2, -2.6
        vol = Circle(radius=0.5, color=CRAIE, stroke_width=3).set_fill(GRIS, 0.18).move_to(P(vx, vy))
        lq = M(r"Q\searrow", sc=0.55).move_to(P(vx, vy))
        js = [fleche((vx + 0.5*np.cos(a), vy + 0.5*np.sin(a)), (vx + 1.05*np.cos(a), vy + 1.05*np.sin(a)), col=ORANGE, sw=3, tl=0.12) for a in (0.3, 1.9, 3.5, 5.1)]
        lj = M(r"\vec j", sc=0.55, color=ORANGE).move_to(P(vx + 1.25, vy + 0.62))
        self.play(Create(vol), FadeIn(lq), *[GrowArrow(j) for j in js], FadeIn(lj), run_time=0.9)
        dv = pos(T(r"divergence de (MA), puis (MG) :", sc=0.6, color=GRIS), -6.3, -3.0)
        dm = M(r"0=\operatorname{div}\big(\overrightarrow{\operatorname{rot}}\,\vec B\big)=\mu_0\Big(\operatorname{div}\vec j+\frac{\partial\rho}{\partial t}\Big)", sc=0.68).next_to(dv, RIGHT, buff=0.3)
        self.ecr(self.a("c9", "divergence de Maxwell-Ampère"), dv, rt=0.8)
        self.play(Ecrire(dm, rt=1.2))
        sj = pos(T(r"sans $\vec j_D$ : $\operatorname{div}\vec j=0$ toujours $\Rightarrow$ impossible de charger un condensateur !", sc=0.6, color=ROUGE), -6.3, -3.65)
        self.ecr(self.t("c10"), sj, rt=1.2)
        self.fin()

# ---------------------------------------------------------------- S3
class S3(C):
    sid = "S3"
    def construct(self):
        self.entete(r"3.3 -- ARQS magnétique et loi d'Ohm locale", "Cours")
        t1 = pos(T(r"approximation des régimes quasi stationnaires : \textbf{ARQS}", sc=0.66), -6.3, 2.25)
        self.ecr(self.a("d1", "l'approximation"), t1, rt=1.1)
        # longueur d'onde et petit dispositif
        xs0, lam, ys, am = 2.0, 4.2, 1.25, 0.38
        xx = np.linspace(xs0, xs0 + lam, 120)
        sn = VMobject(color=BLEU, stroke_width=3).set_points_smoothly([P(x, ys + am*np.sin(2*PI*(x - xs0)/lam)) for x in xx])
        cl = DoubleArrow(P(xs0, ys - 0.62), P(xs0 + lam, ys - 0.62), buff=0, color=GRIS, stroke_width=2, tip_length=0.12, max_tip_length_to_length_ratio=0.1)
        llam = M(r"\lambda", sc=0.6, color=GRIS).next_to(cl, DOWN, buff=0.06)
        dsp = Rectangle(width=0.3, height=0.3, color=JAUNE, stroke_width=3).move_to(P(xs0 + 0.55, ys + 0.75)); ldsp = M(r"L", sc=0.55, color=JAUNE).next_to(dsp, LEFT, buff=0.08)
        f2 = pos(M(r"L\ll\lambda=\frac{c}{f}", sc=0.95, color=JAUNE), -6.3, 1.25)
        self.at(self.t("d2"), Create(sn), GrowFromCenter(cl), FadeIn(llam), Create(dsp), FadeIn(ldsp), run_time=1.0)
        self.ecr(self.a("d2", "lambda égale"), f2, rt=0.8); self.play(Create(enc(f2, col=JAUNE, buff=0.12)), run_time=0.4)
        ex = pos(T(r"$50$ Hz : $\lambda = 6\,000$ km \; $\gg$ \; une maison", sc=0.62, color=GRIS), -3.65, 1.25)
        self.ecr(self.t("d3"), ex, rt=0.9)
        self.play(Create(sep(0.35)), run_time=0.3)
        a1 = pos(T(r"\textbf{ARQS magnétique} : $\vec j_D$ négligé devant $\vec j$ dans (MA)", sc=0.68, color=BLEU), -6.3, -0.15)
        self.ecr(self.t("d4"), a1, rt=1.0)
        a2 = pos(M(r"\overrightarrow{\operatorname{rot}}\,\vec B=\mu_0\,\vec j", sc=0.85), -6.3, -0.9)
        self.ecr(self.a("d4", "rotationnel de B"), a2, rt=0.7)
        a3 = M(r"\Rightarrow\quad\operatorname{div}\vec j=0", sc=0.85, color=VERT).next_to(a2, RIGHT, buff=0.45)
        self.ecr(self.t("d5"), a3, rt=0.7); self.play(Create(enc(a3, col=VERT, buff=0.1)), run_time=0.3)
        a4 = T(r"pas d'accumulation de charge : loi des nœuds", sc=0.6, color=GRIS).next_to(a3, RIGHT, buff=0.45)
        self.ecr(self.a("d5", "la loi des nœuds"), a4, rt=1.0)
        a5 = pos(T(r"piège : on \textbf{garde} $-\partial\vec B/\partial t$ dans (MF) : l'induction subsiste !", sc=0.64, color=ROUGE), -6.3, -1.65)
        self.ecr(self.t("d6"), a5, rt=1.1)
        self.play(Create(sep(-2.15)), run_time=0.3)
        o1 = pos(T(r"\textbf{Loi d'Ohm locale} :", sc=0.72, color=VERT), -6.3, -2.75)
        o2 = M(r"\vec j=\sigma\,\vec E", sc=1.0, color=JAUNE).next_to(o1, RIGHT, buff=0.4)
        self.at(self.a("d7", "j égale sigma E"), Ecrire(o1, rt=0.6), Ecrire(o2, rt=0.6), run_time=0.7)
        o3 = pos(T(r"$\sigma$ : conductivité ($\mathrm{S\,m^{-1}}$)", sc=0.62, color=GRIS), -6.3, -3.5)
        # conducteur : j et E parallèles
        bx0, bx1, by = 2.4, 6.2, -2.85
        bar = Rectangle(width=bx1 - bx0, height=0.8, color=CRAIE, stroke_width=3).set_fill(GRIS, 0.15).move_to(P((bx0 + bx1)/2, by))
        fe = fleche((bx0 + 0.5, by + 0.18), (bx0 + 2.0, by + 0.18), col=BLEU, sw=4, tl=0.15); le = M(r"\vec E", sc=0.6, color=BLEU).next_to(fe, RIGHT, buff=0.1)
        fj = fleche((bx0 + 0.5, by - 0.2), (bx0 + 2.3, by - 0.2), col=ORANGE, sw=4, tl=0.15); lj = M(r"\vec j", sc=0.6, color=ORANGE).next_to(fj, RIGHT, buff=0.1)
        self.at(self.a("d7", "où sigma est"), Create(enc(o2, col=JAUNE, buff=0.12)), Ecrire(o3, rt=0.6), Create(bar), GrowArrow(fe), FadeIn(le), GrowArrow(fj), FadeIn(lj), run_time=0.9)
        o4 = T(r"cuivre : $\sigma \approx 6\times10^{7}\ \mathrm{S\,m^{-1}}$", sc=0.62).next_to(o3, RIGHT, buff=0.6)
        self.ecr(self.t("d8"), o4, rt=0.8)
        self.fin()

# ---------------------------------------------------------------- S4
class S4(C):
    sid = "S4"
    def construct(self):
        self.entete(r"3.4 -- Énergie électromagnétique", "Cours")
        # volume V, frontière Σ, flux de Poynting sortant
        vx, vy, rv = 4.9, 0.95, 1.05
        vol = Circle(radius=rv, color=CRAIE, stroke_width=3).set_fill(GRIS, 0.15).move_to(P(vx, vy))
        lsg = M(r"\Sigma", sc=0.6).move_to(P(vx - 1.2, vy + 0.85)); lu = M(r"u_{em}", sc=0.6, color=BLEU).move_to(P(vx - 0.3, vy + 0.4))
        chs = VGroup(*[T(r"$+$", sc=0.6, color=ROUGE).move_to(P(vx + dx, vy + dy)) for dx, dy in ((0.15, -0.3), (0.5, -0.05), (-0.25, -0.5))])
        lje = M(r"\vec j\cdot\vec E", sc=0.55, color=ROUGE).move_to(P(vx + 0.1, vy - 0.8))
        pis = [fleche((vx + 0.75*rv*np.cos(a), vy + 0.75*rv*np.sin(a)), (vx + 1.55*rv*np.cos(a), vy + 1.55*rv*np.sin(a)), col=ORANGE, sw=4, tl=0.15) for a in (0.35, 1.25, -0.6)]
        lpi = M(r"\vec\Pi", sc=0.62, color=ORANGE).move_to(P(vx + 1.55, vy + 0.15))
        p1 = pos(T(r"puissance volumique cédée aux charges :", sc=0.66), -6.3, 2.25)
        p1m = M(r"p=\vec j\cdot\vec E", sc=0.8, color=ROUGE).next_to(p1, RIGHT, buff=0.3)
        self.at(self.t("e1"), Ecrire(p1, rt=0.9), Ecrire(p1m, rt=0.6), run_time=0.9)
        p1b = pos(T(r"($\mathrm{W\,m^{-3}}$) ; la force magnétique ne travaille pas", sc=0.6, color=GRIS), -6.3, 1.68)
        self.ecr(self.a("e1", "La force magnétique"), p1b, rt=0.9)
        p2 = pos(M(r"\text{ohmique : }\ \vec j\cdot\vec E=\frac{j^2}{\sigma}=\sigma E^2>0", sc=0.76), -6.3, 0.95)
        self.ecr(self.t("e2"), p2, rt=1.0)
        p2b = T(r"effet Joule", sc=0.62, color=ROUGE).next_to(p2, RIGHT, buff=0.3)
        self.ecr(self.a("e2", "c'est l'effet Joule"), p2b, rt=0.5)
        self.play(Create(vol), FadeIn(lsg), FadeIn(chs), FadeIn(lje), run_time=0.6)
        u1 = pos(M(r"u_{em}=\frac{\varepsilon_0E^2}{2}+\frac{B^2}{2\mu_0}", sc=0.82, color=BLEU), -6.3, 0.05)
        u1b = T(r"($\mathrm{J\,m^{-3}}$)", sc=0.6, color=GRIS).next_to(u1, RIGHT, buff=0.3)
        self.at(self.t("e3"), Ecrire(u1, rt=1.0), FadeIn(u1b), FadeIn(lu), run_time=1.0)
        q1 = pos(M(r"\vec\Pi=\frac{\vec E\wedge\vec B}{\mu_0}", sc=0.82, color=ORANGE), -6.3, -0.92)
        q1b = T(r"($\mathrm{W\,m^{-2}}$) \; : \; $\mathrm dP=\vec\Pi\cdot\vec n\,\mathrm dS$", sc=0.6, color=GRIS).next_to(q1, RIGHT, buff=0.3)
        self.at(self.t("e4"), Ecrire(q1, rt=0.9), *[GrowArrow(p) for p in pis], FadeIn(lpi), run_time=1.0)
        self.ecr(self.a("e4", "en watts par mètre carré"), q1b, rt=0.9)
        bl = pos(M(r"\frac{\partial u_{em}}{\partial t}+\operatorname{div}\vec\Pi=-\vec j\cdot\vec E", sc=0.95, color=JAUNE), -6.3, -2.14)
        bln = T(r"identité de Poynting", sc=0.6, color=GRIS).next_to(bl, RIGHT, buff=0.45)
        self.ecr(self.t("e5"), bl, rt=1.1); self.play(Create(enc(bl, col=JAUNE, buff=0.14)), FadeIn(bln), run_time=0.5)
        dm = pos(T(r"(MF) et (MA), avec", sc=0.6, color=GRIS), -6.3, -3.06)
        dm2 = M(r"\operatorname{div}(\vec E\wedge\vec B)=\vec B\cdot\overrightarrow{\operatorname{rot}}\,\vec E-\vec E\cdot\overrightarrow{\operatorname{rot}}\,\vec B", sc=0.66, color=GRIS).next_to(dm, RIGHT, buff=0.3)
        self.at(self.t("e6"), Ecrire(dm, rt=0.6), Ecrire(dm2, rt=1.1), run_time=1.1)
        lec = pos(T(r"énergie stockée $\searrow$ \; = \; sortie par $\Sigma$ \; + \; cédée aux charges", sc=0.6), -6.3, -3.68)
        self.at(self.t("e7"), Ecrire(lec, rt=1.0), run_time=1.0)
        self.at(self.a("e7", "si elle sort"), *[Indicate(p, color=JAUNE) for p in pis], run_time=0.6)
        self.at(self.a("e7", "cédée aux charges"), Indicate(lje, color=JAUNE), Indicate(chs, color=JAUNE), run_time=0.6)
        ex = T(r"\textbf{Place aux exercices !}", sc=0.8, color=JAUNE).move_to([4.75, -3.1, 0])
        self.ecr(self.a("e8", "Place aux exercices"), ex, rt=0.6)
        self.fin()

# ---------------------------------------------------------------- S5
def sphere(cx, cy, rs, n=8, r1=None, r2=None, col=BLEU):
    s = Circle(radius=rs, color=CRAIE, stroke_width=3).set_fill(GRIS, 0.3).move_to(P(cx, cy))
    r1 = r1 or rs + 0.1; r2 = r2 or rs + 0.75
    fs = VGroup(*[fleche((cx + r1*np.cos(a), cy + r1*np.sin(a)), (cx + r2*np.cos(a), cy + r2*np.sin(a)), col=col, sw=3, tl=0.13)
                  for a in np.linspace(0, 2*PI, n, endpoint=False) + PI/n])
    return s, fs

class S5(C):
    sid = "S5"
    def construct(self):
        self.entete(r"Exercice 1 -- une sphère qui se décharge", "Énoncé")
        cx, cy, rs = -4.9, 0.45, 0.72
        s, fs = sphere(cx, cy, rs, r2=rs + 0.8)
        lq = M(r"Q(t)", sc=0.6).move_to(P(cx, cy + 0.2)); o = Dot(P(cx, cy - 0.15), radius=0.05, color=CRAIE)
        ra = Line(P(cx, cy - 0.15), P(cx + rs*np.cos(-0.5), cy - 0.15 + rs*np.sin(-0.5)), color=JAUNE, stroke_width=2)
        lra = M(r"a", sc=0.55, color=JAUNE).move_to(P(cx + 0.32, cy - 0.5)); lo = M(r"O", sc=0.5).move_to(P(cx - 0.2, cy - 0.3))
        le = M(r"\vec E", sc=0.6, color=BLEU).move_to(P(cx + 1.45, cy + 0.95))
        air = T(r"air : $\sigma$, $\varepsilon_0$", sc=0.6, color=GRIS).move_to(P(cx, cy - 1.95))
        self.at(self.t("f1"), Create(s), FadeIn(lq), FadeIn(o), Create(ra), FadeIn(lra), FadeIn(lo), run_time=0.9)
        d1 = pos(T(r"sphère métallique : $a = 5{,}0$ cm, \; $Q(0) = Q_0 = 50$ nC", sc=0.68), -2.7, 2.25)
        self.ecr(self.a("f1", "porte la charge"), d1, rt=1.0)
        d2 = pos(T(r"air : $\sigma = 2{,}0\times10^{-14}\ \mathrm{S\,m^{-1}}$ \; (permittivité $\varepsilon_0$)", sc=0.68), -2.7, 1.6)
        self.at(self.t("f2"), Ecrire(d2, rt=1.1), FadeIn(air), run_time=1.1)
        q1 = pos(T(r"Q1. Champ $\vec E(M,t)$ et charge $Q(t)$ ? Durée de la décharge ?", sc=0.68), -2.7, 0.75)
        q2 = pos(T(r"Q2. Champ $\vec B$ ? Vérifier l'équation (MA).", sc=0.68), -2.7, 0.1)
        q3 = pos(T(r"Q3. Où passe l'énergie électrique ?", sc=0.68), -2.7, -0.55)
        self.at(self.t("f3"), Ecrire(q1, rt=1.0), *[GrowArrow(f) for f in fs], FadeIn(le), run_time=1.0)
        self.ecr(self.t("f4"), q2, rt=0.8); self.ecr(self.t("f5"), q3, rt=0.7)
        bx = SurroundingRectangle(VGroup(q1, q2, q3), color=ROUGE, buff=0.18, corner_radius=0.08)
        self.play(Create(bx), run_time=0.4)
        rf = pos(T(r"Réfléchissons : symétrie sphérique $\to$ Gauss ; bilan de charge + loi d'Ohm", sc=0.64, color=BLEU), -6.3, -2.25)
        self.ecr(self.t("f6"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-0.5, -3.2, 0])
        self.ecr(self.t("f7"), av, rt=0.7)
        self.pause5(self.PH["f7"]["fin"], 2.8, -3.2)
        self.fin()

# ---------------------------------------------------------------- S6
class S6(C):
    sid = "S6"
    def construct(self):
        self.entete(r"Exercice 1 -- la solution", "Solution")
        # petite figure : un plan (O, M) et les deux courants en M
        ox, oy, rs = 4.75, 0.85, 0.42
        s = Circle(radius=rs, color=CRAIE, stroke_width=3).set_fill(GRIS, 0.3).move_to(P(ox, oy)); o = Dot(P(ox, oy), radius=0.05)
        lo = M(r"O", sc=0.5).move_to(P(ox - 0.12, oy - 0.22))
        u = np.array([np.cos(0.35), np.sin(0.35)])
        pl = DashedLine(P(*(np.array([ox, oy]) - 1.3*u)), P(*(np.array([ox, oy]) + 1.95*u)), color=GRIS, stroke_width=2, dash_length=0.1)
        mm_ = np.array([ox, oy]) + 1.15*u; dm = Dot(P(*mm_), radius=0.05); lm = M(r"M", sc=0.5).move_to(P(mm_[0] - 0.05, mm_[1] + 0.27))
        fj = fleche(tuple(mm_), tuple(mm_ + 0.62*u), col=ORANGE, sw=4, tl=0.14); lj = M(r"\vec j", sc=0.55, color=ORANGE).move_to(P(*(mm_ + 0.5*u + np.array([0.05, -0.32]))))
        fd = fleche(tuple(mm_), tuple(mm_ - 0.55*u), col=BLEU, sw=4, tl=0.14); ld = M(r"\vec j_D", sc=0.55, color=BLEU).move_to(P(*(mm_ - 0.42*u + np.array([0.02, -0.36]))))
        lb0 = M(r"\vec B=\vec 0", sc=0.62, color=VERT).move_to(P(ox + 1.2, oy - 0.45))
        self.at(self.t("g1"), Create(s), FadeIn(o), FadeIn(lo), Create(pl), FadeIn(dm), FadeIn(lm), run_time=0.8)
        m1 = self.etape(1, BLEU, 2.2, T(r"plans $(O,M)$ de symétrie : $\vec E=E(r,t)\,\vec e_r$", sc=0.66), self.a("g1", "donc E est radial"), rt=1.0)
        m1b = M(r"\text{Gauss : }E=\frac{Q(t)}{4\pi\varepsilon_0r^2}", sc=0.72).next_to(m1, RIGHT, buff=0.45)
        self.ecr(self.t("g2"), m1b, rt=1.0)
        m2 = self.etape(2, VERT, 1.3, M(r"\frac{\mathrm dQ}{\mathrm dt}=-I", sc=0.72), self.a("g3", "le bilan de charge"), rt=0.7)
        m2b = M(r"I=\iint_\Sigma\vec j\cdot\vec n_{ext}\,\mathrm dS=\sigma E\,4\pi r^2=\frac{\sigma Q}{\varepsilon_0}", sc=0.72).next_to(m2, RIGHT, buff=0.45)
        self.ecr(self.a("g3", "le flux de j"), m2b, rt=1.2)
        m2c = pos(T(r"indépendant de $r$ : aucune accumulation de charge dans l'air", sc=0.6, color=GRIS), -5.85, 0.6)
        self.ecr(self.t("g4"), m2c, rt=1.0)
        m3 = pos(M(r"\frac{\mathrm dQ}{\mathrm dt}=-\frac{\sigma}{\varepsilon_0}\,Q\;\Rightarrow\;Q=Q_0\,e^{-t/\tau},\quad\tau=\frac{\varepsilon_0}{\sigma}", sc=0.72, color=VERT), -5.85, -0.15)
        self.ecr(self.t("g5"), m3, rt=1.3); self.play(Create(enc(m3, col=VERT, buff=0.1)), run_time=0.4)
        m3b = T(r"$\tau \approx 440$ s $\approx 7$ min", sc=0.66, color=JAUNE).next_to(m3, RIGHT, buff=0.45)
        self.ecr(self.t("g6"), m3b, rt=0.8)
        m4 = self.etape(3, ORANGE, -0.95, T(r"$\vec B$ pseudo-vecteur, $\perp$ à tous les plans $(O,M)$", sc=0.66), self.t("g7"), rt=1.0)
        m4b = M(r"\Rightarrow\;\vec B=\vec 0", sc=0.74, color=VERT).next_to(m4, RIGHT, buff=0.35)
        self.at(self.a("g8", "B est nul partout"), Ecrire(m4b, rt=0.5), FadeIn(lb0), run_time=0.6)
        m5 = pos(M(r"\text{(MA) : }\ \vec 0=\mu_0\Big(\vec j+\varepsilon_0\frac{\partial\vec E}{\partial t}\Big)", sc=0.7), -5.85, -1.7)
        self.ecr(self.t("g9"), m5, rt=1.0)
        m5b = M(r"\varepsilon_0\frac{\partial E}{\partial t}=\frac{1}{4\pi r^2}\frac{\mathrm dQ}{\mathrm dt}=-\sigma E", sc=0.7).next_to(m5, RIGHT, buff=0.45)
        self.at(self.t("g9b"), Ecrire(m5b, rt=1.1), GrowArrow(fj), FadeIn(lj), run_time=1.1)
        ok = coche(m5b.get_right()[0] + 0.35, -1.7)
        self.at(self.a("g9b", "Ça marche"), GrowArrow(fd), FadeIn(ld), Create(ok), run_time=0.7)
        m6 = pos(T(r"$\vec j_D=-\vec j$ : surtout \textbf{pas} d'ARQS magnétique ici !", sc=0.62, color=ROUGE), -5.85, -2.38)
        self.ecr(self.a("g10", "Piège"), m6, rt=0.9)
        m7 = self.etape(4, ROUGE, -3.05, M(r"\vec\Pi=\vec 0\;\Rightarrow\;\frac{\partial u_{em}}{\partial t}=-\vec j\cdot\vec E", sc=0.7), self.t("g11"), rt=1.0)
        m7b = T(r"énergie dissipée \textbf{sur place} (Joule dans l'air)", sc=0.6).next_to(m7, RIGHT, buff=0.45)
        self.ecr(self.t("g12"), m7b, rt=1.0)
        m8 = pos(T(r"vérification : $\varepsilon_0E\,\partial_tE=-\sigma E^2$ \; $\checkmark$ \qquad $[\varepsilon_0/\sigma]=\mathrm{F}\cdot\Omega=\mathrm{s}$", sc=0.6, color=VERT), -5.85, -3.68)
        self.ecr(self.t("g13"), m8, rt=1.1)
        self.fin()

# ---------------------------------------------------------------- S7
def schema_condo(xg, xd, yc, h, gen=True):
    """condensateur relié à son générateur (vue de côté)"""
    pl, ax_ = condo(xg, xd, yc, h)
    g = VGroup()
    if gen:
        yb = yc - h/2 - 0.75; xm = (xg + xd)/2
        g.add(Line(P(xg, yc), P(xg - 0.95, yc), color=CRAIE, stroke_width=3), Line(P(xg - 0.95, yc), P(xg - 0.95, yb), color=CRAIE, stroke_width=3),
              Line(P(xg - 0.95, yb), P(xm - 0.3, yb), color=CRAIE, stroke_width=3), Line(P(xm + 0.3, yb), P(xd + 0.95, yb), color=CRAIE, stroke_width=3),
              Line(P(xd + 0.95, yb), P(xd + 0.95, yc), color=CRAIE, stroke_width=3), Line(P(xd + 0.95, yc), P(xd, yc), color=CRAIE, stroke_width=3))
        ci = Circle(radius=0.3, color=CRAIE, stroke_width=3).move_to(P(xm, yb))
        sw = VMobject(color=CRAIE, stroke_width=3).set_points_smoothly([P(xm - 0.17 + 0.34*k/20, yb + 0.09*np.sin(2*PI*k/20)) for k in range(21)])
        g.add(ci, sw)
    return pl, ax_, g

class S7(C):
    sid = "S7"
    def construct(self):
        self.entete(r"Exercice 2 -- un condensateur en régime sinusoïdal", "Énoncé")
        xg, xd, yc, h = -5.25, -4.15, 0.75, 2.4
        pl, ax_, g = schema_condo(xg, xd, yc, h)
        lp = M(r"+q", sc=0.55).move_to(P(xg - 0.32, yc - h/2 + 0.2)); lm_ = M(r"-q", sc=0.55).move_to(P(xd + 0.35, yc - h/2 + 0.2))
        lu = M(r"u(t)", sc=0.6).move_to(P((xg + xd)/2, yc - h/2 - 1.3))
        ce = DoubleArrow(P(xg, yc + h/2 + 0.25), P(xd, yc + h/2 + 0.25), buff=0, color=GRIS, stroke_width=2, tip_length=0.12, max_tip_length_to_length_ratio=0.2)
        lce = M(r"e", sc=0.55, color=GRIS).next_to(ce, UP, buff=0.05)
        cr = DoubleArrow(P(xd + 0.5, yc), P(xd + 0.5, yc + h/2), buff=0, color=GRIS, stroke_width=2, tip_length=0.12, max_tip_length_to_length_ratio=0.2)
        lcr = M(r"R", sc=0.55, color=GRIS).next_to(cr, RIGHT, buff=0.06).shift(0.2*UP)
        nb = T(r"(échelle non respectée)", sc=0.48, color=GRIS).move_to(P((xg + xd)/2, yc - h/2 - 1.72))
        self.at(self.t("h1"), Create(pl), Create(g), FadeIn(lp), FadeIn(lm_), FadeIn(lu), run_time=1.0)
        d1 = pos(T(r"armatures circulaires : $R = 10$ cm, distance $e = 1{,}0$ mm", sc=0.64), -2.5, 2.25)
        self.at(self.t("h2"), Ecrire(d1, rt=1.0), GrowFromCenter(cr), FadeIn(lcr), run_time=1.0)
        self.at(self.a("h2", "distantes de"), GrowFromCenter(ce), FadeIn(lce), FadeIn(nb), run_time=0.6)
        d2 = pos(M(r"u(t)=U_0\cos\omega t,\quad U_0=200\ \mathrm V,\quad f=1{,}0\ \mathrm{MHz}", sc=0.72), -2.5, 1.55)
        self.ecr(self.t("h3"), d2, rt=1.1)
        d3 = pos(T(r"vide entre les armatures ; effets de bord négligés", sc=0.6, color=GRIS), -2.5, 0.95)
        self.ecr(self.a("h3", "Effets de bord"), d3, rt=0.8)
        q1 = pos(T(r"Q1. $\vec E$ et $\vec j_D$ entre les armatures ? ARQS justifiée ?", sc=0.68), -2.5, 0.15)
        q2 = pos(T(r"Q2. Champ $\vec B$ entre les armatures ?", sc=0.68), -2.5, -0.5)
        q3 = pos(T(r"Q3. Par où entre l'énergie ? Bilan avec $\vec\Pi$.", sc=0.68), -2.5, -1.15)
        self.ecr(self.t("h4"), q1, rt=1.0); self.ecr(self.t("h5"), q2, rt=0.8); self.ecr(self.t("h6"), q3, rt=0.9)
        bx = SurroundingRectangle(VGroup(q1, q2, q3), color=ROUGE, buff=0.18, corner_radius=0.08)
        self.play(Create(bx), run_time=0.4)
        rf = pos(T(r"Réfléchissons : aucun courant de conduction entre les armatures : qui crée $\vec B$ ?", sc=0.64, color=BLEU), -6.3, -2.62)
        self.ecr(self.t("h7"), rf, rt=1.2)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-0.5, -3.35, 0])
        self.ecr(self.t("h8"), av, rt=0.7)
        self.pause5(self.PH["h8"]["fin"], 2.8, -3.35)
        self.fin()

# ---------------------------------------------------------------- S8
class S8(C):
    sid = "S8"
    def construct(self):
        self.entete(r"Exercice 2 -- les champs", "Solution")
        self.rappel(r"$R = 10$ cm, \; $e = 1$ mm, \; $U_0 = 200$ V, \; $f = 1$ MHz")
        xg, xd, yc, h = 4.0, 5.2, 0.55, 2.4
        pl, ax_ = condo(xg, xd, yc, h)
        lp = M(r"+", sc=0.6).move_to(P(xg - 0.3, yc + h/2 - 0.1)); lm_ = M(r"-", sc=0.6).move_to(P(xd + 0.3, yc + h/2 - 0.1))
        rc = repere_cyl(5.95, -0.55)
        self.play(Create(pl), Create(ax_), FadeIn(lp), FadeIn(lm_), FadeIn(rc), run_time=0.7)
        fe = [fleche((xg + 0.08, y), (xd - 0.08, y), col=BLEU, sw=3, tl=0.13) for y in (yc + 0.95, yc, yc - 0.95)]
        le = M(r"\vec E", sc=0.6, color=BLEU).move_to(P((xg + xd)/2, yc + h/2 + 0.3))
        m1 = self.etape(1, BLEU, 2.25, M(r"\vec E=\frac{u}{e}\,\vec e_z=\frac{U_0}{e}\cos\omega t\;\vec e_z", sc=0.72), self.a("i1", "E égale u sur e"), rt=1.0)
        self.play(*[GrowArrow(f) for f in fe], FadeIn(le), run_time=0.6)
        m1b = T(r"$E_0 = 2{,}0\times10^{5}\ \mathrm{V\,m^{-1}}$", sc=0.62).next_to(m1, RIGHT, buff=0.4)
        self.ecr(self.a("i1", "deux fois dix"), m1b, rt=0.7)
        m2 = pos(M(r"\vec j_D=\varepsilon_0\frac{\partial\vec E}{\partial t},\quad j_{D,0}=\frac{\varepsilon_0\omega U_0}{e}\approx11\ \mathrm{A\,m^{-2}}", sc=0.72), -5.85, 1.4)
        self.ecr(self.t("i3"), m2, rt=1.3)
        m3 = pos(M(r"\pi R^2\,j_{D,0}\approx0{,}35\ \mathrm A=I_0\quad\text{(courant des fils)}", sc=0.7), -5.85, 0.65)
        self.ecr(self.t("i4"), m3, rt=1.1)
        m4 = pos(T(r"ARQS : $\lambda = c/f = 300$ m \; $\gg R$ \; (rapport $3\,000$)", sc=0.64, color=VERT), -5.85, 0.0)
        self.ecr(self.t("i5"), m4, rt=1.0); self.play(Create(coche(m4.get_right()[0] + 0.35, 0.0)), run_time=0.3)
        bs = [odot(4.6, yc + 0.48, col=VERT, r=0.12), otimes(4.6, yc - 0.48, col=VERT, r=0.12)]
        lbs = M(r"\vec B", sc=0.5, color=VERT).move_to(P(4.9, yc + 0.48))
        m5 = self.etape(2, VERT, -0.8, T(r"plans contenant l'axe : symétrie de $\vec j_D$ $\Rightarrow$ $\vec B=B(r,t)\,\vec e_\theta$", sc=0.64), self.t("i6"), rt=1.1)
        self.at(self.a("i6", "donc B est orthoradial"), *[FadeIn(b) for b in bs], run_time=0.5)
        m6 = self.etape(3, ORANGE, -1.55, T(r"Ampère généralisé : cercle de rayon $r$, orienté par $\vec e_\theta$ (normale $\vec e_z$)", sc=0.62), self.t("i7"), rt=1.1)
        # vue de face : lignes de B (cercles)
        fx, fy = 4.85, -2.45
        disq = Circle(radius=0.95, color=CRAIE, stroke_width=2).set_fill(GRIS, 0.12).move_to(P(fx, fy))
        lig = VGroup(*[Circle(radius=r, color=VERT, stroke_width=2.5).move_to(P(fx, fy)) for r in (0.3, 0.55, 0.8)])
        tips = VGroup(*[fleche((fx - 0.06, fy - r), (fx + 0.2, fy - r), col=VERT, sw=3, tl=0.15) for r in (0.3, 0.55, 0.8)])
        lvf = T(r"vue de face ($\vec e_z$ vers vous)", sc=0.48, color=GRIS).move_to(P(fx, fy - 1.2))
        self.at(self.a("i7", "orienté par e thêta"), Create(disq), Create(lig), FadeIn(tips), FadeIn(lvf), run_time=0.9)
        m7 = pos(M(r"2\pi r\,B=\mu_0\varepsilon_0\,\pi r^2\,\frac{\partial E}{\partial t}\qquad(I_{\text{enlacé}}=0)", sc=0.72), -5.85, -2.22)
        self.ecr(self.a("i8", "Seul compte"), m7, rt=1.2)
        m8 = pos(M(r"B=\frac{r}{2c^2}\frac{\partial E}{\partial t}=-\frac{r\,\omega U_0}{2c^2e}\sin\omega t", sc=0.72, color=VERT), -5.85, -3.22)
        self.ecr(self.t("i9"), m8, rt=1.1); self.play(Create(enc(m8, col=VERT, buff=0.1)), run_time=0.4)
        m9 = T(r"$B_{max}(R) \approx 0{,}70\ \mu$T", sc=0.64, color=JAUNE).next_to(m8, RIGHT, buff=0.5)
        self.at(self.t("i10"), Ecrire(m9, rt=0.8), FadeIn(lbs), run_time=0.8)
        self.fin()

# ---------------------------------------------------------------- S9
class S9(C):
    sid = "S9"
    def construct(self):
        self.entete(r"Exercice 2 -- le bilan d'énergie", "Solution")
        xg, xd, yc, h = 4.1, 5.1, 1.45, 1.5
        pl, ax_ = condo(xg, xd, yc, h)
        fe = fleche((xg + 0.08, yc + 0.4), (xd - 0.08, yc + 0.4), col=BLEU, sw=3, tl=0.12); le = M(r"\vec E", sc=0.55, color=BLEU).move_to(P(xg - 0.45, yc + 0.4))
        bh, bb = odot(4.6, yc + 0.62 - 0.02, col=VERT, r=0.1), otimes(4.6, yc - 0.6, col=VERT, r=0.1)
        lbh = M(r"\vec B", sc=0.5, color=VERT).move_to(P(xd + 0.35, yc - 0.6))
        pis = [fleche((4.6, yc + h/2 + 0.55), (4.6, yc + h/2 + 0.05), col=ORANGE, sw=4, tl=0.14), fleche((4.6, yc - h/2 - 0.55), (4.6, yc - h/2 - 0.05), col=ORANGE, sw=4, tl=0.14)]
        lpi = M(r"\vec\Pi", sc=0.58, color=ORANGE).move_to(P(5.0, yc + h/2 + 0.35))
        lch = T(r"(charge)", sc=0.5, color=ORANGE).move_to(P(5.65, yc + h/2 + 0.35))
        m1 = self.etape(4, BLEU, 2.25, M(r"\vec\Pi(R)=\frac{\vec E\wedge\vec B}{\mu_0},\qquad\vec e_z\wedge\vec e_\theta=-\vec e_r", sc=0.72), self.t("k1"), rt=1.1)
        self.play(Create(pl), Create(ax_), GrowArrow(fe), FadeIn(le), FadeIn(bh), FadeIn(bb), FadeIn(lbh), run_time=0.7)
        self.at(self.a("k1", "Attention"), Indicate(m1, color=JAUNE, scale_factor=1.05), run_time=0.6)
        m2 = pos(M(r"\Pi_r(R)=-\frac{E\,B(R)}{\mu_0}=-\frac{\varepsilon_0R}{4}\,\frac{\partial (E^2)}{\partial t}", sc=0.72), -5.85, 1.25)
        self.ecr(self.t("k2"), m2, rt=1.1)
        m2b = pos(T(r"charge ($E^2\nearrow$) : $\Pi_r<0$, vers l'axe", sc=0.62, color=ORANGE), -5.85, 0.55)
        self.at(self.a("k2", "l'énergie entre par le côté"), Ecrire(m2b, rt=0.8), *[GrowArrow(p) for p in pis], FadeIn(lpi), FadeIn(lch), run_time=0.9)
        m3 = pos(M(r"P_{entr}=-\Pi_r(R)\,2\pi Re=-\frac{C\omega U_0^2}{2}\,\sin2\omega t", sc=0.72), -5.85, -0.2)
        self.ecr(self.a("k3", "donne la puissance entrante"), m3, rt=1.1)
        m4 = self.etape(5, VERT, -1.2, M(r"P_{entr}=\frac{\mathrm d}{\mathrm dt}\Big(\frac12\,C\,u^2\Big)\;\;\checkmark", sc=0.72, color=VERT), self.t("k4"), rt=1.0)
        self.play(Create(enc(m4, col=VERT, buff=0.1)), run_time=0.4)
        # chronogramme : u(t) et puissance entrante sur une période
        ax, fr = cadre(4.4, -0.85, 4.2, 1.8, 0, 2*PI, -1.25, 1.25)
        cu = crb(ax, np.cos, 0, 2*PI, col=BLEU, sw=3); cp = crb(ax, lambda s: -np.sin(2*s), 0, 2*PI, col=ORANGE, sw=3)
        z = zero(ax, 0, 2*PI)
        lcu = VGroup(Line(P(2.6, -2.05), P(3.0, -2.05), color=BLEU, stroke_width=3), M(r"u(t)", sc=0.52, color=BLEU).move_to(P(3.42, -2.05)))
        lcp = VGroup(Line(P(4.2, -2.05), P(4.6, -2.05), color=ORANGE, stroke_width=3), M(r"P_{entr}(t)", sc=0.52, color=ORANGE).move_to(P(5.28, -2.05)))
        lt = M(r"t", sc=0.5, color=GRIS).next_to(fr, RIGHT, buff=0.08).shift(0.0*UP)
        m5 = pos(T(r"$C = 278$ pF : amplitude $35$ W, \textbf{moyenne nulle}", sc=0.62), -5.85, -1.97)
        self.at(self.t("k5"), Create(fr), Create(z), Create(cu), FadeIn(lcu), FadeIn(lt), Ecrire(m5, rt=1.0), run_time=1.0)
        self.at(self.a("k5", "Mais la moyenne est nulle"), Create(cp), FadeIn(lcp), run_time=0.9)
        zs = VGroup(*[Polygon(*([ax.c2p(a, 0)] + [ax.c2p(s, -np.sin(2*s)) for s in np.linspace(a, a + PI/2, 30)] + [ax.c2p(a + PI/2, 0)]), stroke_width=0).set_fill(ORANGE, 0.25)
                      for a in (PI/2, 3*PI/2)])
        m6 = pos(T(r"aller-retour : l'énergie entre si $|u|\nearrow$, ressort si $|u|\searrow$", sc=0.62), -5.85, -2.62)
        self.at(self.t("k6"), Ecrire(m6, rt=1.0), FadeIn(zs), run_time=1.0)
        m7 = self.etape(6, JAUNE, -3.32, M(r"\frac{U_m}{U_e}=\frac18\Big(\frac{\omega R}{c}\Big)^2\approx5\times10^{-7}", sc=0.72), self.t("k7"), rt=1.1)
        m8 = T(r"capacité pure ; c'est le critère ARQS : $R \ll c/\omega$", sc=0.62, color=VERT).next_to(m7, RIGHT, buff=0.5)
        self.ecr(self.a("k8", "c'est justement le critère"), m8, rt=1.0)
        self.fin()

# ---------------------------------------------------------------- S10
class S10(C):
    sid = "S10"
    def construct(self):
        self.entete(r"Exercice 3 -- un fil chauffant", "Énoncé")
        x0, x1, yf, h = 1.6, 6.0, 1.55, 0.6
        fl = fil(x0, x1, yf, h)
        ld = VGroup(Line(P(x0 - 0.9, yf), P(x0, yf), color=CRAIE, stroke_width=3))
        fi = fleche((x0 - 0.85, yf), (x0 - 0.2, yf), col=ORANGE, sw=4, tl=0.15); lI = M(r"I", sc=0.6, color=ORANGE).move_to(P(x0 - 0.55, yf + 0.3))
        cl = DoubleArrow(P(x0, yf - 0.62), P(x1, yf - 0.62), buff=0, color=GRIS, stroke_width=2, tip_length=0.12, max_tip_length_to_length_ratio=0.1)
        lcl = M(r"\ell", sc=0.6, color=GRIS).next_to(cl, DOWN, buff=0.05)
        ca = DoubleArrow(P(x1 + 0.45, yf - h/2), P(x1 + 0.45, yf + h/2), buff=0, color=GRIS, stroke_width=2, tip_length=0.1, max_tip_length_to_length_ratio=0.3)
        lca = M(r"2a", sc=0.55, color=GRIS).next_to(ca, RIGHT, buff=0.06)
        self.at(self.t("l1"), Create(fl), Create(ld), GrowArrow(fi), FadeIn(lI), run_time=1.0)
        d0 = pos(T(r"résistance chauffante : un fil de \textbf{nichrome}", sc=0.66), -6.3, 2.3)
        self.ecr(self.a("l1", "résistance chauffante"), d0, rt=0.9)
        d1 = pos(T(r"$a = 0{,}25$ mm, \; $\ell = 1{,}0$ m", sc=0.66), -6.3, 1.65)
        d2 = pos(T(r"$\sigma = 9{,}1\times10^{5}\ \mathrm{S\,m^{-1}}$", sc=0.66), -6.3, 1.05)
        self.at(self.t("l2"), Ecrire(d1, rt=0.8), GrowFromCenter(cl), FadeIn(lcl), GrowFromCenter(ca), FadeIn(lca), run_time=0.9)
        self.ecr(self.a("l2", "Sa conductivité"), d2, rt=0.8)
        d3 = pos(T(r"courant continu $I = 4{,}0$ A, uniforme dans la section", sc=0.66), -6.3, 0.4)
        self.ecr(self.t("l3"), d3, rt=1.0)
        q1 = pos(T(r"Q1. Champs $\vec E$ et $\vec B$ dans le fil ($r \le a$) ?", sc=0.68), -6.3, -0.45)
        q2 = pos(T(r"Q2. Vecteur de Poynting dans le fil ? Vérifier le bilan local.", sc=0.68), -6.3, -1.1)
        q3 = pos(T(r"Q3. Puissance entrant par la surface latérale ? Comparer à $RI^2$.", sc=0.68), -6.3, -1.75)
        self.ecr(self.t("l4"), q1, rt=0.9); self.ecr(self.t("l5"), q2, rt=1.0); self.ecr(self.t("l6"), q3, rt=1.0)
        bx = SurroundingRectangle(VGroup(q1, q2, q3), color=ROUGE, buff=0.18, corner_radius=0.08)
        self.play(Create(bx), run_time=0.4)
        rf = pos(T(r"Réfléchissons : Ohm $\to\vec E$, Ampère $\to\vec B$, puis $\vec E\wedge\vec B$", sc=0.62, color=BLEU), -6.3, -2.6)
        dn = pos(M(r"\text{donnée : }\operatorname{div}\big(A_r(r)\,\vec e_r\big)=\frac1r\,\frac{\mathrm d(rA_r)}{\mathrm dr}", sc=0.64, color=GRIS), 1.25, -2.6)
        self.ecr(self.t("l7"), rf, rt=1.1)
        self.ecr(self.a("l7", "La divergence en cylindriques"), dn, rt=1.0)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-1.0, -3.5, 0])
        self.ecr(self.t("l8"), av, rt=0.7)
        self.pause5(self.PH["l8"]["fin"], 2.3, -3.5)
        self.fin()

# ---------------------------------------------------------------- S11
class S11(C):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice 3 -- les champs et le vecteur de Poynting", "Solution")
        self.rappel(r"$a = 0{,}25$ mm, \; $\ell = 1$ m, \; $\sigma = 9{,}1\cdot10^{5}\ \mathrm{S\,m^{-1}}$, \; $I = 4$ A")
        x0, x1, yf, R_ = 3.3, 6.3, 1.2, 0.6
        fl = fil(x0, x1, yf, 2*R_)
        ax_ = DashedLine(P(x0 - 0.2, yf), P(x1 + 0.2, yf), color=GRIS, stroke_width=1.5, dash_length=0.08)
        rc = repere_cyl(5.7, -0.95)
        self.play(Create(fl), Create(ax_), FadeIn(rc), run_time=0.7)
        fe = fleche((x0 + 0.3, yf), (x0 + 1.3, yf), col=BLEU, sw=4, tl=0.15); le = M(r"\vec E", sc=0.58, color=BLEU).move_to(P(x0 + 1.0, yf - 0.25))
        m1 = self.etape(1, BLEU, 2.25, M(r"j=\frac{I}{\pi a^2}\approx2{,}0\times10^{7}\ \mathrm{A\,m^{-2}}\quad(20\ \mathrm{A/mm^2})", sc=0.7), self.a("m1", "la densité de courant"), rt=1.1)
        m1b = pos(M(r"\vec E=\frac{\vec j}{\sigma}\approx22\ \mathrm{V\,m^{-1}}\;\vec e_z\quad\text{(uniforme)}", sc=0.7), -5.85, 1.4)
        self.at(self.t("m1b"), Ecrire(m1b, rt=1.0), GrowArrow(fe), FadeIn(le), run_time=1.0)
        bs = [odot(x0 + 0.55, yf + 0.38, col=VERT, r=0.11), otimes(x0 + 0.55, yf - 0.38, col=VERT, r=0.11)]
        lbs = M(r"\vec B", sc=0.52, color=VERT).move_to(P(x0 + 0.95, yf + 0.38))
        m2 = self.etape(2, VERT, 0.6, T(r"plan $(M, Oz)$ de symétrie $\Rightarrow$ $\vec B=B(r)\,\vec e_\theta$", sc=0.64), self.t("m2"), rt=1.0)
        self.at(self.a("m2", "B est orthoradial"), *[FadeIn(b) for b in bs], FadeIn(lbs), run_time=0.5)
        m3 = pos(M(r"2\pi r\,B=\mu_0\,I\,\frac{r^2}{a^2}", sc=0.68), -5.85, -0.08)
        self.ecr(self.t("m3"), m3, rt=0.9)
        m3b = M(r"\Rightarrow\;B=\frac{\mu_0Ir}{2\pi a^2},\quad B(a)=3{,}2\ \mathrm{mT}", sc=0.68, color=VERT).next_to(m3, RIGHT, buff=0.4)
        self.ecr(self.t("m3b"), m3b, rt=1.0)
        m4 = self.etape(3, ORANGE, -1.02, M(r"\vec\Pi=\frac{\vec E\wedge\vec B}{\mu_0}=\frac{EB}{\mu_0}\,(\vec e_z\wedge\vec e_\theta)=-\frac{I^2\,r}{2\sigma\pi^2a^4}\,\vec e_r", sc=0.68), self.t("m4"), rt=1.3)
        self.play(Create(enc(m4, col=ORANGE, buff=0.08)), run_time=0.4)
        # Π vers l'axe, proportionnel à r (calculé), et entrée par la surface latérale
        pin = VGroup(*[fleche((xs, yf + s*r), (xs, yf + s*0.25*r), col=ORANGE, sw=3, tl=0.1) for xs, r in ((x0 + 1.7, 0.25), (x0 + 2.15, 0.42), (x0 + 2.6, 0.58)) for s in (1, -1)])
        pout = VGroup(*[fleche((x, yf + s*(R_ + 0.5)), (x, yf + s*(R_ + 0.04)), col=ORANGE, sw=4, tl=0.13) for x in (x0 + 0.6, x0 + 1.6) for s in (1, -1)])
        lpi = M(r"\vec\Pi", sc=0.58, color=ORANGE).move_to(P(x0 + 1.1, yf + R_ + 0.4))
        m5 = pos(T(r"vers l'axe, $\propto r$ : l'énergie entre \textbf{par le côté}", sc=0.64, color=ORANGE), -5.85, -1.85)
        self.at(self.t("m5"), Ecrire(m5, rt=0.9), FadeIn(pin), run_time=0.9)
        self.at(self.a("m5", "L'énergie entre dans le fil"), *[GrowArrow(p) for p in pout], FadeIn(lpi), run_time=0.7)
        m6 = self.etape(4, ROUGE, -2.55, T(r"régime permanent : $\partial u_{em}/\partial t=0$", sc=0.64), self.t("m6"), rt=0.9)
        m7 = M(r"\operatorname{div}\vec\Pi=\frac1r\frac{\mathrm d(r\Pi_r)}{\mathrm dr}", sc=0.7).next_to(m6, RIGHT, buff=0.5)
        self.ecr(self.a("m6", "il reste à vérifier"), m7, rt=0.9)
        m8 = pos(M(r"\operatorname{div}\vec\Pi=-\frac{I^2}{\sigma\pi^2a^4}=-\frac{j^2}{\sigma}=-\vec j\cdot\vec E\quad\checkmark", sc=0.7, color=VERT), -5.85, -3.42)
        self.ecr(self.t("m8"), m8, rt=1.1)
        self.fin()

# ---------------------------------------------------------------- S12
class S12(C):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice 3 -- la puissance entrante", "Solution")
        self.rappel(r"$E \approx 22\ \mathrm{V\,m^{-1}}$, \; $B(a) = 3{,}2$ mT, \; $\vec\Pi$ vers l'axe")
        m1 = self.etape(5, BLEU, 2.2, M(r"\Pi(a)=\frac{E\,B(a)}{\mu_0}\approx5{,}7\times10^{4}\ \mathrm{W\,m^{-2}}", sc=0.72), self.a("n1", "au bord"), rt=1.1)
        m2 = pos(T(r"bases : $\vec\Pi$ tangent, flux nul \; ; \; aire latérale $2\pi a\ell$", sc=0.64), -5.85, 1.4)
        self.ecr(self.t("n2"), m2, rt=1.1)
        m3 = pos(M(r"P=\Pi(a)\,2\pi a\ell=\frac{I^2\,\ell}{\sigma\pi a^2}=R\,I^2", sc=0.76, color=JAUNE), -5.85, 0.6)
        self.ecr(self.t("n3"), m3, rt=1.0)
        self.at(self.a("n3", "c'est la résistance"), Create(enc(m3, col=JAUNE, buff=0.1)), run_time=0.4)
        m4 = pos(M(r"R=\frac{\ell}{\sigma\pi a^2}\approx5{,}6\ \Omega,\qquad P\approx90\ \mathrm W", sc=0.72, color=VERT), -5.85, -0.42)
        self.ecr(self.t("n4"), m4, rt=1.0)
        m5 = self.etape(6, JAUNE, -1.22, T(r"$57\ \mathrm{kW\,m^{-2}}$ $\approx 50 \times$ l'éclairement solaire : le fil rougit", sc=0.64), self.t("n5"), rt=1.1)
        # profils dans le fil (calculés) : Π(r) linéaire, P(r) en r²
        ax, fr = cadre(4.55, 0.95, 3.6, 2.3, 0, 1, 0, 1.15)
        cpi = crb(ax, lambda s: s, 0, 1, col=ORANGE, sw=4); cpr = crb(ax, lambda s: s**2, 0, 1, col=BLEU, sw=4)
        l0 = M(r"0", sc=0.5, color=GRIS).next_to(ax.c2p(0, 0), DOWN, buff=0.1); la = M(r"a", sc=0.55, color=GRIS).next_to(ax.c2p(1, 0), DOWN, buff=0.1)
        lr = M(r"r", sc=0.55, color=GRIS).next_to(ax.c2p(0.5, 0), DOWN, buff=0.1)
        lpi = M(r"\Pi(r)/\Pi(a)", sc=0.5, color=ORANGE).move_to(ax.c2p(0.3, 0.85)); lpr = M(r"P(r)/RI^2", sc=0.5, color=BLEU).move_to(ax.c2p(0.78, 0.25))
        m6 = pos(T(r"cylindre de rayon $r<a$ : $P(r)=RI^2\,r^2/a^2$ = effet Joule de ce cylindre", sc=0.62), -5.85, -1.92)
        self.at(self.t("n6"), Create(fr), FadeIn(l0), FadeIn(la), FadeIn(lr), Create(cpi), FadeIn(lpi), Ecrire(m6, rt=1.1), run_time=1.1)
        self.play(Create(cpr), FadeIn(lpr), run_time=0.7)
        dz = Dot(ax.c2p(0, 0), radius=0.08, color=JAUNE)
        m7 = pos(T(r"sur l'axe : $\vec\Pi=\vec 0$, toute l'énergie a été absorbée en chemin", sc=0.62), -5.85, -2.6)
        self.at(self.a("n6", "Et rien n'arrive"), Ecrire(m7, rt=1.0), FadeIn(dz), Flash(dz, color=JAUNE), run_time=1.0)
        m8 = pos(T(r"$50$ Hz : $\lambda = 6\,000$ km $\gg \ell$ : ARQS, mêmes résultats en valeur efficace", sc=0.62, color=VERT), -5.85, -3.28)
        self.ecr(self.t("n8"), m8, rt=1.2)
        self.fin()

# ---------------------------------------------------------------- S13
class S13(C):
    sid = "S13"
    def construct(self):
        self.entete(r"Ce qu'il faut retenir", "Méthode")
        t0 = pos(T(r"la méthode pour un exercice de \textbf{Maxwell et d'énergie}", sc=0.74, color=GRIS), -6.3, 2.2)
        self.ecr(self.t("o1"), t0, rt=0.9)
        pts = [("o2", r"\textbf{symétries} des sources : $\vec E$ dans les plans de symétrie, $\vec B$ perpendiculaire", BLEU),
               ("o3", r"\textbf{forme intégrale} : Gauss ($\vec E$), Ampère généralisé ($\vec B$), Faraday ($\vec E$ induit)", VERT),
               ("o4", r"\textbf{orientations} : $\vec n_{ext}$ sortante, main droite, sans oublier $\vec j_D$", ORANGE),
               ("o5", r"\textbf{ARQS} justifiée ($L \ll \lambda$) ; conservation de la charge vérifiée", ROUGE),
               ("o6", r"\textbf{bilan d'énergie} : $\vec\Pi$, surface orientée, comparer à $RI^2$ ou $Cu^2/2$", JAUNE)]
        for k, (ph_, txt, c) in enumerate(pts):
            yy = [1.35, 0.45, -0.45, -1.35, -2.25][k]
            ca = carte(k+1, c, -5.9, yy); tx = pos(T(txt, sc=0.62), -5.35, yy)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
        nx = T(r"Prochaine vidéo : ondes électromagnétiques dans le vide", sc=0.66, color=GRIS).move_to([0, -3.4, 0])
        self.ecr(self.t("o7"), nx, rt=1.2)
        self.fin()
