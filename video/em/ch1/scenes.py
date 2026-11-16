from base import *
import os
# ---------- outils communs (repris des chapitres de RdM et de SLCI) ----------
def carte(k, col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0]); n = T(r"\textbf{%d}" % k, sc=0.75, color=col).move_to(c)
    return VGroup(c, n)
def coche(x, y, col=VERT, k=1.0):
    return VMobject(color=col, stroke_width=6).set_points_as_corners([P(x - 0.18*k, y), P(x - 0.05*k, y - 0.15*k), P(x + 0.2*k, y + 0.2*k)])
def carte_ok(col, x, y):
    c = Circle(radius=0.27, color=col, stroke_width=3).move_to([x, y, 0])
    return VGroup(c, coche(x + 0.01, y + 0.01, col=col, k=0.72).set_stroke(width=4))
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
def courbe(ax, xs, ys, col=ORANGE, sw=4):
    return VMobject(color=col, stroke_width=sw).set_points_as_corners([ax.c2p(a, b) for a, b in zip(xs, ys)])
def P(x, y): return np.array([x, y, 0.0])
def fleche(a, b, col=ROUGE, sw=4, tl=0.18):
    return Arrow(P(*a), P(*b), buff=0, color=col, stroke_width=sw, tip_length=tl, max_tip_length_to_length_ratio=0.6, max_stroke_width_to_length_ratio=20)
def cote_v(x, ya, yb, txt, col=GRIS, sc=0.55, cote_txt=RIGHT):
    l = DoubleArrow(P(x, ya), P(x, yb), buff=0, color=col, stroke_width=2, tip_length=0.12, max_tip_length_to_length_ratio=0.3)
    return VGroup(l, M(txt, sc=sc, color=col).next_to(l, cote_txt, buff=0.08))
def etape(sc, k, c, y, m, t, rt=1.0, x0=-6.35):
    ca = carte(k, c, x0, y); mm = pos(m, x0 + 0.5, y)
    sc.at(t, Create(ca[0]), FadeIn(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
    return mm
def verif(sc, c, y, m, t, rt=1.0, x0=-6.35):
    ca = carte_ok(c, x0, y); mm = pos(m, x0 + 0.5, y)
    sc.at(t, Create(ca[0]), Create(ca[1]), Ecrire(mm, rt=rt), run_time=max(0.6, rt))
    return mm
def rappel(sc, txt):
    r = pos(T(txt, sc=0.56, color=GRIS), 6.6, 2.72, bord=RIGHT); sc.play(FadeIn(r), run_time=0.4); return r
# ---------- dessins d'électrostatique ----------
def signe(x, y, s=1, a=0.1, col=CRAIE, sw=3):
    g = VGroup(Line(P(x - a, y), P(x + a, y), color=col, stroke_width=sw))
    if s > 0: g.add(Line(P(x, y - a), P(x, y + a), color=col, stroke_width=sw))
    return g
def charge(x, y, s=1, r=0.2):
    col = ROUGE if s > 0 else BLEU
    c = Circle(radius=r, color=col, stroke_width=3).set_fill(col, 0.35).move_to(P(x, y))
    return VGroup(c, signe(x, y, s, a=0.55*r))
def sortant(x, y, r=0.13, col=JAUNE):
    return VGroup(Circle(radius=r, color=col, stroke_width=3).move_to(P(x, y)), Dot(P(x, y), radius=0.04, color=col))
def pointe(p, d, col=CRAIE, L=0.13, op=1.0):
    d = np.array(d, dtype=float); d = d / (np.linalg.norm(d) + 1e-12); n = np.array([-d[1], d[0], 0.0])
    a = p + d*L*0.5; b = p - d*L*0.5 + n*L*0.42; c = p - d*L*0.5 - n*L*0.42
    return Polygon(a, b, c, stroke_width=0).set_fill(col, op)
def pointilles(mob, n=40, col=VERT, sw=3):
    return DashedVMobject(mob.set_stroke(col, sw), num_dashes=n, dashed_ratio=0.55)
# lignes de champ calculées (intégration RK4 du champ normalisé)
def champ(ch, x, y):
    ex = ey = 0.0
    for q, a, b in ch:
        dx, dy = x - a, y - b; r3 = (dx*dx + dy*dy)**1.5 + 1e-9; ex += q*dx/r3; ey += q*dy/r3
    return ex, ey
def ligne(ch, x0, y0, sens, bx, by, pas=0.012, nmax=1500, rstop=0.2):
    def f(x, y):
        ex, ey = champ(ch, x, y); n = np.hypot(ex, ey) + 1e-12; return sens*ex/n, sens*ey/n
    pts = [(x0, y0)]; x, y = x0, y0; dprec = None
    for _ in range(nmax):
        k1 = f(x, y); k2 = f(x + pas/2*k1[0], y + pas/2*k1[1]); k3 = f(x + pas/2*k2[0], y + pas/2*k2[1]); k4 = f(x + pas*k3[0], y + pas*k3[1])
        dx = pas/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]); dy = pas/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        if dprec is not None and dx*dprec[0] + dy*dprec[1] < 0: break       # point de champ nul
        x, y = x + dx, y + dy; dprec = (dx, dy)
        if abs(x) > bx or abs(y) > by:
            x, y = float(np.clip(x, -bx, bx)), float(np.clip(y, -by, by)); pts.append((x, y)); return pts, "bord"
        if any(np.hypot(x - a, y - b) < rstop for q, a, b in ch if q*sens < 0):
            pts.append((x, y)); return pts, "charge"
        pts.append((x, y))
    return pts, "fin"
def carte_champ(ch, cx, cy, k, bx, by, n=12, decal=0.5, col=CRAIE, op=0.6):
    """lignes issues des charges positives (et, pour compléter, remontées depuis les négatives) ;
    repère physique (x, y) -> tableau (cx + k x, cy + k y)"""
    g = VGroup(); tips = VGroup()
    def ajoute(pts, sens):
        if len(pts) < 6: return
        q = [P(cx + k*a, cy + k*b) for a, b in pts]
        g.add(VMobject(stroke_color=col, stroke_width=2, stroke_opacity=op).set_points_smoothly(q[::3] + [q[-1]]))
        L = np.cumsum([0] + [np.linalg.norm(q[i+1] - q[i]) for i in range(len(q) - 1)])
        cible = min(0.55, 0.5*L[-1]); i = int(np.searchsorted(L, cible)); i = min(max(i, 1), len(q) - 2)
        d = (q[i+1] - q[i-1]) * sens
        tips.add(pointe(q[i], d, col=col, op=min(1, op + 0.3)))
    for q0, a, b in ch:
        sens = 1 if q0 > 0 else -1
        for j in range(n):
            t = 2*PI*(j + decal)/n; x0, y0 = a + 0.21*np.cos(t), b + 0.21*np.sin(t)
            pts, fin = ligne(ch, x0, y0, sens, bx, by)
            if sens < 0 and fin == "charge": continue      # déjà tracée depuis la charge positive
            ajoute(pts, sens)
    return g, tips

class C(Cours):
    """Cours + aperçu rapide : APERCU=1 garde la dernière image pleine (contrôle de mise en page)"""
    def fin(self):
        if os.environ.get("APERCU"): self.wait(0.1); return
        super().fin()

# =====================================================================
class S0(C):
    sid = "S0"
    def construct(self):
        sur = T(r"PHYSIQUE \;·\; PT", sc=0.55, color=GRIS).move_to([0, 3.2, 0])
        ti = T(r"\textbf{Électromagnétisme -- Chapitre 1}", sc=1.1, color=JAUNE).move_to([0, 2.5, 0])
        st = T(r"Électrostatique : symétries et théorème de Gauss", sc=0.85).move_to([0, 1.75, 0])
        tr = Line([-5.4, 1.3, 0], [5.4, 1.3, 0], color=JAUNE, stroke_width=2)
        self.play(FadeIn(sur), Ecrire(ti, rt=0.6), Ecrire(st, rt=1.0), Create(tr), run_time=1.0)
        cx, cy = 4.35, -0.5
        bo = Circle(radius=0.6, color=ROUGE, stroke_width=3).set_fill(ROUGE, 0.25).move_to(P(cx, cy))
        pl = VGroup(*[signe(cx + dx, cy + dy, 1, a=0.08, sw=2.5) for dx, dy in [(0, 0), (-0.3, 0.2), (0.28, 0.22), (-0.22, -0.3), (0.25, -0.28), (0, 0.4), (0, -0.42)]])
        ga = pointilles(Circle(radius=1.05).move_to(P(cx, cy)), n=36)
        lS = M(r"\Sigma", sc=0.7, color=VERT).move_to(P(cx - 1.05, cy + 0.95))
        fl = VGroup(*[fleche((cx + 1.05*np.cos(t), cy + 1.05*np.sin(t)), (cx + 1.5*np.cos(t), cy + 1.5*np.sin(t)), col=JAUNE, sw=3, tl=0.13) for t in np.arange(8)*PI/4 + PI/8])
        q = M(r"\oint_{\Sigma}\vec E\cdot\vec n\,\mathrm{d}S = \frac{Q_{\text{int}}}{\varepsilon_0}", sc=0.72, color=JAUNE).move_to(P(cx, -2.75))
        self.at(self.a("a2", "Des charges immobiles"), Create(bo), FadeIn(pl), run_time=0.8)
        self.at(self.a("a2", "créent un champ"), *[GrowArrow(f) for f in fl], run_time=0.8)
        self.at(self.a("a2", "théorème de Gauss"), Create(ga), FadeIn(lS), Ecrire(q, rt=0.8), run_time=0.9)
        items = []
        for k, (txt, col) in enumerate([("Champ, symétries et théorème de Gauss", BLEU), ("Potentiel, énergie et condensateur plan", VERT),
                                         ("Exercice 1 : un tube chargé", ORANGE), ("Exercice 2 : une boule et sa coquille", ROUGE),
                                         ("Exercice 3 : un condensateur plan", JAUNE)]):
            yy = 0.65 - 0.68*k
            items.append(VGroup(carte(k+1, col, -6.2, yy), pos(T(txt, sc=0.72), -5.65, yy)))
        for it, (sid, fr_) in zip(items, [("a3", "un cours express"), ("a3", "puis le potentiel"), ("a4", "un tube chargé"),
                                          ("a4", "une boule entourée"), ("a4", "et un condensateur plan")]):
            self.jusqua(self.a(sid, fr_)); self.play(Create(it[0][0]), FadeIn(it[0][1]), Ecrire(it[1], rt=0.5), run_time=0.5)
        self.at(self.a("a4", "C'est parti"), *[Indicate(it[0], color=JAUNE, scale_factor=1.2) for it in items], run_time=0.8)
        self.fin()

class S1(C):
    sid = "S1"
    def construct(self):
        self.entete(r"1.1 -- Charges, loi de Coulomb et champ", "Cours")
        l1 = pos(T(r"charge \textbf{algébrique}, \textbf{conservée}, \textbf{quantifiée} : $e = 1{,}6\times10^{-19}$ C", sc=0.62), -6.4, 2.3)
        self.ecr(self.t("b1"), l1, rt=1.2)
        # figure : deux charges q1, q2 > 0 en P1, P2 ; champ au point M
        p1, p2, m = np.array([2.9, -2.05]), np.array([5.9, -2.05]), np.array([4.4, -0.45])
        u1 = (m - p1)/np.linalg.norm(m - p1); u2 = (m - p2)/np.linalg.norm(m - p2); L = 1.0
        c1 = charge(*p1); c2 = charge(*p2)
        lp1 = M(r"q_1 \text{ en } P_1", sc=0.55).next_to(c1, DOWN, buff=0.12); lp2 = M(r"q_2 \text{ en } P_2", sc=0.55).next_to(c2, DOWN, buff=0.12)
        dm = Dot(P(*m), radius=0.06, color=CRAIE); lm = M(r"M", sc=0.6).next_to(dm, DOWN, buff=0.12)
        d1 = DashedLine(P(*p1), P(*m), color=GRIS, stroke_width=2); d2 = DashedLine(P(*p2), P(*m), color=GRIS, stroke_width=2)
        uu = fleche(tuple(p1 + 0.25*u1), tuple(p1 + 0.85*u1), col=GRIS, sw=3, tl=0.12)
        lu = M(r"\vec u_{P\to M}", sc=0.55, color=GRIS).next_to(uu.get_end(), LEFT, buff=0.12).shift(0.12*UP)
        fo = pos(M(r"\vec F_{P\to M} = \frac{q_1\,q}{4\pi\varepsilon_0}\,\frac{\overrightarrow{PM}}{PM^3}", sc=0.8), -6.4, 1.35)
        self.at(self.t("b2"), FadeIn(c1), FadeIn(lp1), FadeIn(dm), FadeIn(lm), Create(d1), run_time=0.7)
        self.at(self.a("b2", "une force en un sur r carré"), Ecrire(fo, rt=1.2), GrowArrow(uu), FadeIn(lu), run_time=1.2)
        l3 = pos(T(r"$1/(4\pi\varepsilon_0) \approx 9\times10^{9}$ SI \;;\; même signe : \textbf{répulsion}", sc=0.6, color=GRIS), -6.4, 0.55)
        self.ecr(self.t("b3"), l3, rt=1.0)
        f4 = pos(M(r"\vec F = q\,\vec E(M)", sc=0.85), -6.4, -0.25)
        t4 = pos(T(r"$\vec E$ en V/m, créé par les \textbf{sources}", sc=0.58, color=GRIS), -3.65, -0.25)
        e1 = fleche(tuple(m), tuple(m + L*u1), col=BLEU, sw=4, tl=0.15); le1 = M(r"\vec E_1", sc=0.6, color=BLEU).next_to(e1.get_end(), RIGHT, buff=0.08)
        self.at(self.t("b4"), Ecrire(f4, rt=0.7), GrowArrow(e1), FadeIn(le1), run_time=0.8)
        self.ecr(self.a("b4", "en volts par mètre"), t4, rt=0.8)
        su = pos(M(r"\vec E(M) = \frac{1}{4\pi\varepsilon_0}\sum_i q_i\,\frac{\overrightarrow{P_iM}}{P_iM^3}", sc=0.8, color=JAUNE), -6.4, -1.25)
        e2 = fleche(tuple(m), tuple(m + L*u2), col=BLEU, sw=4, tl=0.15); le2 = M(r"\vec E_2", sc=0.6, color=BLEU).next_to(e2.get_end(), LEFT, buff=0.08)
        es = m + L*(u1 + u2)
        et = fleche(tuple(m), tuple(es), col=JAUNE, sw=5, tl=0.18); let = M(r"\vec E", sc=0.65, color=JAUNE).next_to(et.get_end(), RIGHT, buff=0.1)
        pa = VGroup(DashedLine(P(*(m + L*u1)), P(*es), color=GRIS, stroke_width=1.5), DashedLine(P(*(m + L*u2)), P(*es), color=GRIS, stroke_width=1.5))
        self.at(self.t("b5"), FadeIn(c2), FadeIn(lp2), Create(d2), GrowArrow(e2), FadeIn(le2), run_time=0.8)
        self.at(self.a("b5", "on additionne"), Ecrire(su, rt=1.2), Create(pa), GrowArrow(et), FadeIn(let), run_time=1.2)
        self.play(Create(enc(su, col=JAUNE, buff=0.13)), run_time=0.4)
        pg = pos(T(r"on additionne des \textbf{vecteurs}, pas des normes !", sc=0.62, color=ROUGE), -6.4, -2.3)
        self.ecr(self.t("b6"), pg, rt=0.9)
        hx = L*u1[0]
        h1 = fleche(tuple(m), (m[0] + hx, m[1]), col=ORANGE, sw=3, tl=0.12); h2 = fleche(tuple(m), (m[0] - hx, m[1]), col=ORANGE, sw=3, tl=0.12)
        lh = T(r"les composantes en $x$ se compensent", sc=0.55, color=ORANGE).move_to(P(4.4, -2.95))
        self.at(self.a("b6", "les composantes horizontales"), GrowArrow(h1), GrowArrow(h2), FadeIn(lh), run_time=0.7)
        l7 = pos(T(r"distribution continue :", sc=0.62), -6.4, -3.25)
        f7 = M(r"\mathrm{d}q = \rho\,\mathrm{d}\tau,\quad \sigma\,\mathrm{d}S,\quad \lambda\,\mathrm{d}\ell", sc=0.75).next_to(l7, RIGHT, buff=0.25)
        self.ecr(self.t("b7"), l7, rt=0.6); self.ecr(self.a("b7", "dé q égale"), f7, rt=1.0)
        self.fin()

class S2(C):
    sid = "S2"
    def construct(self):
        self.entete(r"1.2 -- Symétries et invariances", "Cours")
        cu = pos(T(r"\textbf{Principe de Curie} : $\vec E$ a au moins les symétries des charges qui le créent", sc=0.64), -6.4, 2.35)
        self.ecr(self.a("c1", "Principe de Curie"), cu, rt=1.3)
        k, bx, by = 0.9, 2.0, 1.4
        def carte_(ch, cx, cy, plan_col, plan_lab, vec):
            g, tips = carte_champ(ch, cx, cy, k, bx, by, n=12)
            qs = VGroup(*[charge(cx + k*a, cy + k*b, q, r=0.17) for q, a, b in ch])
            fr = Rectangle(width=2*k*bx, height=2*k*by, color=GRIS, stroke_width=1.5, stroke_opacity=0.6).move_to(P(cx, cy))
            pl = DashedLine(P(cx, cy - k*by), P(cx, cy + k*by), color=plan_col, stroke_width=4, dash_length=0.12)
            lp = M(plan_lab, sc=0.65, color=plan_col).move_to(P(cx + 0.3, cy - k*by + 0.28))
            mm = np.array([cx, cy + k*0.55]); dm = Dot(P(*mm), radius=0.06, color=JAUNE)
            lm = M(r"M", sc=0.55, color=JAUNE).next_to(dm, LEFT if vec[0] == 0 else DOWN, buff=0.1).shift((0.05*DOWN if vec[0] == 0 else 0.2*LEFT))
            ev = fleche(tuple(mm), tuple(mm + np.array(vec)), col=JAUNE, sw=5, tl=0.16)
            le = M(r"\vec E", sc=0.6, color=JAUNE).next_to(ev.get_end(), RIGHT if vec[0] == 0 else UP, buff=0.08)
            return dict(g=g, tips=tips, qs=qs, fr=fr, pl=pl, lp=lp, dm=dm, lm=lm, ev=ev, le=le)
        A = carte_([(1, -0.8, 0), (1, 0.8, 0)], -4.4, 0.55, VERT, r"\Pi", (0, 0.62))
        B = carte_([(1, -0.8, 0), (-1, 0.8, 0)], 0.15, 0.55, ORANGE, r"\Pi^*", (0.62, 0))
        def montre(D, t):
            self.at(t, Create(D["fr"]), FadeIn(D["qs"]), Create(D["g"]), FadeIn(D["tips"]), run_time=1.0)
        montre(A, self.t("c2"))
        self.at(self.a("c2", "plan de symétrie"), Create(A["pl"]), FadeIn(A["lp"]), run_time=0.6)
        ca = T(r"$\Pi$ de symétrie : $\vec E(M)$ \textbf{dans} $\Pi$", sc=0.6, color=VERT).move_to(P(-4.4, -1.08))
        self.at(self.a("c2", "le champ est contenu"), FadeIn(A["dm"]), FadeIn(A["lm"]), GrowArrow(A["ev"]), FadeIn(A["le"]), Ecrire(ca, rt=0.8), run_time=0.8)
        montre(B, self.t("c3"))
        self.at(self.a("c3", "plan d'antisymétrie"), Create(B["pl"]), FadeIn(B["lp"]), run_time=0.6)
        cb = T(r"$\Pi^*$ d'antisymétrie : $\vec E(M) \perp \Pi^*$", sc=0.6, color=ORANGE).move_to(P(0.15, -1.08))
        self.at(self.a("c3", "orthogonal"), FadeIn(B["dm"]), FadeIn(B["lm"]), GrowArrow(B["ev"]), FadeIn(B["le"]), Ecrire(cb, rt=0.8), run_time=0.8)
        # deux plans de symétrie : leur intersection (perpendiculaire au tableau) porte E, sortant
        ix, iy = 4.9, 0.95
        p1 = DashedLine(P(ix - 1.05, iy - 0.75), P(ix + 1.05, iy + 0.75), color=VERT, stroke_width=3)
        p2 = DashedLine(P(ix - 1.05, iy + 0.75), P(ix + 1.05, iy - 0.75), color=VERT, stroke_width=3)
        so = sortant(ix, iy); lso = M(r"\vec E", sc=0.6, color=JAUNE).move_to(P(ix + 0.42, iy + 0.05))
        t4 = T(r"deux plans de symétrie :", sc=0.58).move_to(P(ix, iy - 1.2)); t4b = T(r"$\vec E$ sur leur \textbf{intersection}", sc=0.58).move_to(P(ix, iy - 1.62))
        self.at(self.t("c4"), Create(p1), Create(p2), run_time=0.7)
        self.at(self.a("c4", "porté par leur droite"), FadeIn(so), FadeIn(lso), Ecrire(t4, rt=0.6), Ecrire(t4b, rt=0.7), run_time=0.8)
        iv = pos(T(r"\textbf{invariances} $\to$ variables :", sc=0.62), -6.4, -1.85)
        iv2 = T(r"translation selon $Oz$ : pas de $z$ \;;\; rotation : pas d'angle", sc=0.62).next_to(iv, RIGHT, buff=0.25)
        self.ecr(self.t("c5"), iv, rt=0.7); self.ecr(self.a("c5", "Invariance par translation"), iv2, rt=1.1)
        X = [-6.4, -2.0, 2.4]
        tb = [pos(T(r"\textbf{sphère} : $\vec E = E_r(r)\,\vec e_r$", sc=0.64, color=BLEU), X[0], -2.7),
              pos(T(r"\textbf{cylindre} : $\vec E = E_r(r)\,\vec e_r$", sc=0.64, color=BLEU), X[1], -2.7),
              pos(T(r"\textbf{plan} : $\vec E = E_z(z)\,\vec e_z$", sc=0.64, color=BLEU), X[2], -2.7)]
        self.at(self.a("c6", "Au final"), *[Ecrire(t, rt=0.9) for t in tb], run_time=0.9)
        pg = T(r"piège : seuls comptent les plans qui \textbf{passent par $M$} !", sc=0.66, color=ROUGE).move_to(P(0, -3.5))
        self.ecr(self.t("c7"), pg, rt=0.9)
        self.fin()

class S3(C):
    sid = "S3"
    def construct(self):
        self.entete(r"1.3 -- Flux et théorème de Gauss", "Cours")
        # surface fermée quelconque
        cx, cy = -4.85, 1.2
        th = np.linspace(0, 2*PI, 200)
        rr = 1.0 + 0.16*np.cos(2*th) + 0.09*np.sin(3*th)
        pts = [P(cx + 1.2*r*np.cos(t), cy + 1.02*r*np.sin(t)) for r, t in zip(rr, th)]
        su = VMobject(color=VERT, stroke_width=3).set_points_smoothly(pts).set_fill(VERT, 0.06)
        ls = M(r"\Sigma", sc=0.7, color=VERT).move_to(P(cx - 1.45, cy + 1.0))
        qi = VGroup(charge(cx - 0.5, cy + 0.25, 1, r=0.16), charge(cx + 0.35, cy - 0.3, 1, r=0.16))
        qe = charge(-2.9, 0.62, 1, r=0.16); lqe = T(r"extérieure", sc=0.5, color=GRIS).next_to(qe, DOWN, buff=0.08)
        k0 = 40; p0 = pts[k0]; tg = pts[k0 + 1] - pts[k0 - 1]; nn = np.array([tg[1], -tg[0], 0]); nn /= np.linalg.norm(nn)
        ds = Line(p0 - 0.18*tg/np.linalg.norm(tg), p0 + 0.18*tg/np.linalg.norm(tg), color=CRAIE, stroke_width=7)
        vn = Arrow(p0, p0 + 0.7*nn, buff=0, color=VERT, stroke_width=4, tip_length=0.14); lvn = M(r"\vec n", sc=0.6, color=VERT).next_to(vn.get_end(), UP, buff=0.05)
        ve = Arrow(p0, p0 + 0.75*np.array([np.cos(0.25), np.sin(0.25), 0]), buff=0, color=JAUNE, stroke_width=4, tip_length=0.14)
        lve = M(r"\vec E", sc=0.6, color=JAUNE).next_to(ve.get_end(), RIGHT, buff=0.06)
        lds = M(r"\mathrm{d}S", sc=0.5).next_to(ds, LEFT, buff=0.05).shift(0.12*DOWN)
        self.at(self.t("d1"), Create(su), FadeIn(ls), FadeIn(ds), FadeIn(lds), run_time=0.9)
        f1 = pos(M(r"\Phi = \iint_S \vec E\cdot\vec n\,\mathrm{d}S", sc=0.8), -2.1, 2.25)
        self.at(self.a("d1", "la somme des"), Ecrire(f1, rt=0.9), GrowArrow(ve), FadeIn(lve), run_time=0.9)
        t1 = pos(T(r"surface fermée : $\vec n$ \textbf{sortant}", sc=0.6, color=VERT), 1.9, 2.25)
        self.at(self.a("d1", "Pour une surface fermée"), GrowArrow(vn), FadeIn(lvn), Ecrire(t1, rt=0.7), run_time=0.7)
        ga = pos(M(r"\oint_{\Sigma}\vec E\cdot\vec n\,\mathrm{d}S = \frac{Q_{\text{int}}}{\varepsilon_0}", sc=1.0, color=JAUNE), -2.1, 1.15)
        self.at(self.t("d2"), FadeIn(qi), Ecrire(ga, rt=1.2), run_time=1.2)
        self.play(Create(enc(ga, col=JAUNE, buff=0.15)), run_time=0.4)
        tf = pos(T(r"quelle que soit la forme de $\Sigma$", sc=0.58, color=GRIS), 2.4, 1.15)
        self.ecr(self.a("d2", "quelle que soit"), tf, rt=0.7)
        t3 = pos(T(r"charges extérieures : flux nul, mais \textbf{du champ} sur $\Sigma$ !", sc=0.6, color=GRIS), -2.1, 0.15)
        self.at(self.t("d3"), FadeIn(qe), FadeIn(lqe), Ecrire(t3, rt=1.0), run_time=1.0)
        sep = Line(P(-6.6, -0.38), P(6.6, -0.38), color=GRIS, stroke_width=1.5, stroke_opacity=0.5)
        self.play(Create(sep), run_time=0.3)
        ys = [-0.9, -1.55, -2.2, -2.85, -3.5]
        st = [(1, BLEU, r"symétries : direction et variable de $\vec E$", self.a("d4", "Premièrement")),
              (2, VERT, r"$\Sigma$ fermée par $M$ : $\vec E$ normal et constant, ou tangent", self.t("d5")),
              (3, ORANGE, r"flux sortant à travers $\Sigma$", self.t("d6")),
              (4, ROUGE, r"$Q_{\text{int}}$ : $M$ dans la distribution, ou dehors", self.a("d6", "Quatrièmement")),
              (5, JAUNE, r"égaler, puis \textbf{vérifier} : continuité, limite", self.t("d7"))]
        for (kk, c, txt, t), y in zip(st, ys):
            etape(self, kk, c, y, T(txt, sc=0.6), t, rt=0.8)
        # plan infini : cylindre à cheval
        yp = -1.85
        pl = Line(P(2.5, yp), P(6.4, yp), color=ROUGE, stroke_width=6); lpl = M(r"\sigma", sc=0.7, color=ROUGE).move_to(P(2.35, yp + 0.3))
        cyl = pointilles(Rectangle(width=1.2, height=1.2).move_to(P(4.1, yp)), n=24)
        n1 = fleche((4.1, yp + 0.6), (4.1, yp + 1.05), col=VERT, sw=3, tl=0.12); n2 = fleche((4.1, yp - 0.6), (4.1, yp - 1.05), col=VERT, sw=3, tl=0.12)
        ln = M(r"\vec n", sc=0.55, color=VERT).next_to(n1.get_end(), LEFT, buff=0.08)
        E1 = fleche((5.5, yp + 0.25), (5.5, yp + 0.95), col=JAUNE, sw=4, tl=0.14); E2 = fleche((5.5, yp - 0.25), (5.5, yp - 0.95), col=JAUNE, sw=4, tl=0.14)
        lE = M(r"\vec E", sc=0.6, color=JAUNE).next_to(E1, RIGHT, buff=0.1)
        fp = M(r"E = \sigma/(2\varepsilon_0)", sc=0.72, color=JAUNE).move_to(P(4.45, -3.45))
        self.at(self.t("d8"), Create(pl), FadeIn(lpl), run_time=0.6)
        self.at(self.a("d8", "Un cylindre à cheval"), Create(cyl), GrowArrow(n1), GrowArrow(n2), FadeIn(ln), run_time=0.8)
        self.at(self.a("d8", "sigma sur deux"), GrowArrow(E1), GrowArrow(E2), FadeIn(lE), Ecrire(fp, rt=0.8), run_time=0.8)
        self.at(self.a("d8", "de chaque côté"), Indicate(E1, color=JAUNE), Indicate(E2, color=JAUNE), run_time=0.6)
        self.fin()

def condensateur(x0, x1, yh, yb, lab=True, sc=0.6):
    ph = Line(P(x0, yh), P(x1, yh), color=ROUGE, stroke_width=7); pb = Line(P(x0, yb), P(x1, yb), color=BLEU, stroke_width=7)
    g = VGroup(ph, pb)
    if lab:
        g.add(M(r"+\sigma", sc=sc, color=ROUGE).next_to(ph, LEFT, buff=0.15), M(r"-\sigma", sc=sc, color=BLEU).next_to(pb, LEFT, buff=0.15))
    return g
def superpo(x, yh, yb, h=0.42, dx=0.36):
    """petites flèches : champ du plan + (rouge) et du plan - (bleu), dans les trois régions"""
    g = VGroup(); ym = (yh + yb)/2
    for yc, sh, sb in [(yh + 0.36, +1, -1), (ym, -1, -1), (yb - 0.36, -1, +1)]:
        g.add(fleche((x, yc - sh*h/2), (x, yc + sh*h/2), col=ROUGE, sw=3, tl=0.11),
              fleche((x + dx, yc - sb*h/2), (x + dx, yc + sb*h/2), col=BLEU, sw=3, tl=0.11))
    return g

class S4(C):
    sid = "S4"
    def construct(self):
        self.entete(r"1.4 -- Potentiel, énergie et condensateur plan", "Cours")
        f1 = pos(M(r"\vec E = -\overrightarrow{\operatorname{grad}}\,V", sc=0.85, color=JAUNE), -6.4, 2.25)
        f1b = pos(M(r"\mathrm{d}V = -\vec E\cdot\mathrm{d}\vec\ell", sc=0.8), -2.6, 2.25)
        self.ecr(self.a("e1", "dérive d'un potentiel"), f1, rt=0.8); self.play(Create(enc(f1, col=JAUNE, buff=0.12)), run_time=0.3)
        self.ecr(self.a("e1", "et dé V"), f1b, rt=0.8)
        # charge ponctuelle : lignes de champ radiales et équipotentielles
        qx, qy = 4.6, 1.45
        q0 = charge(qx, qy, 1, r=0.18)
        eq = VGroup(*[DashedVMobject(Circle(radius=r, color=VERT, stroke_width=2.5).move_to(P(qx, qy)), num_dashes=int(26*r) + 10) for r in (0.5, 0.8, 1.1)])
        lv = VGroup(*[ln for ln in [Line(P(qx + 0.24*np.cos(t), qy + 0.24*np.sin(t)), P(qx + 1.2*np.cos(t), qy + 1.2*np.sin(t)), color=CRAIE, stroke_width=2, stroke_opacity=0.7) for t in np.arange(8)*PI/4]])
        tps = VGroup(*[pointe(P(qx + 0.66*np.cos(t), qy + 0.66*np.sin(t)), (np.cos(t), np.sin(t), 0)) for t in np.arange(8)*PI/4])
        lV = T(r"$V$ décroît", sc=0.5, color=VERT).move_to(P(qx + 1.55, qy - 0.95))
        t2 = pos(T(r"$\vec E$ \textbf{descend} les potentiels, $\perp$ aux équipotentielles", sc=0.58, color=GRIS), -6.4, 1.55)
        self.at(self.t("e2"), FadeIn(q0), Create(lv), FadeIn(tps), Ecrire(t2, rt=1.0), run_time=1.0)
        self.at(self.a("e2", "coupe les équipotentielles"), Create(eq), FadeIn(lV), run_time=0.8)
        f3 = pos(M(r"V = \frac{q}{4\pi\varepsilon_0\,r}", sc=0.8), -6.4, 0.75)
        t3 = pos(T(r"($V(\infty) = 0$) \;;\; $V$ toujours \textbf{continu}", sc=0.58, color=GRIS), -4.0, 0.75)
        self.ecr(self.a("e3", "V égale q sur"), f3, rt=0.8); self.ecr(self.a("e3", "toujours continu"), t3, rt=0.8)
        f4 = pos(M(r"E_p(M) = q\,V(M)", sc=0.85, color=VERT), -6.4, -0.15)
        t4 = pos(T(r"électron ($q < 0$) : \textbf{remonte} les potentiels", sc=0.58, color=GRIS), -3.4, -0.15)
        self.ecr(self.a("e4", "l'énergie potentielle"), f4, rt=0.8); self.play(Create(enc(f4, col=VERT, buff=0.12)), run_time=0.3)
        self.ecr(self.a("e4", "Un électron"), t4, rt=0.9)
        # condensateur plan
        x0, x1, yh, yb = 2.85, 5.95, -0.85, -2.2
        cp = condensateur(x0, x1, yh, yb)
        sp = superpo(3.05, yh, yb)
        self.at(self.t("e5"), Create(cp), run_time=0.8)
        self.at(self.a("e5", "Leurs champs"), FadeIn(sp), run_time=0.7)
        ym = (yh + yb)/2
        bg = VGroup(*[fleche((x, yh - 0.12), (x, yb + 0.12), col=JAUNE, sw=4, tl=0.15) for x in (5.0, 5.65)])
        lb = M(r"E = \frac{\sigma}{\varepsilon_0}", sc=0.6, color=JAUNE).next_to(bg, LEFT, buff=0.15)
        z1 = M(r"\vec E = \vec 0", sc=0.55, color=GRIS).move_to(P(5.3, yh + 0.38)); z2 = M(r"\vec E = \vec 0", sc=0.55, color=GRIS).move_to(P(5.3, yb - 0.38))
        self.at(self.a("e5", "s'ajoutent"), *[GrowArrow(b) for b in bg], FadeIn(lb), run_time=0.7)
        self.at(self.a("e5", "se compensent"), FadeIn(z1), FadeIn(z2), run_time=0.5)
        ce = cote_v(6.3, yh, yb, r"e")
        f6 = pos(M(r"E = \frac{\sigma}{\varepsilon_0} \qquad C = \frac{\varepsilon_0 S}{e} \qquad W_e = \frac{CU^2}{2}", sc=0.8, color=JAUNE), -6.4, -1.15)
        self.at(self.t("e6"), FadeIn(ce), Ecrire(f6, rt=1.5), run_time=1.5); self.play(Create(enc(f6, col=JAUNE, buff=0.13)), run_time=0.3)
        f7 = pos(M(r"\operatorname{div}\vec E = \frac{\rho}{\varepsilon_0}", sc=0.8), -6.4, -2.35)
        f7b = pos(M(r"\oint\vec{\mathcal G}\cdot\vec n\,\mathrm{d}S = -4\pi G\,M_{\text{int}}", sc=0.75), -3.75, -2.35)
        self.ecr(self.a("e7", "Maxwell-Gauss"), f7, rt=0.9)
        self.ecr(self.a("e7b", "la gravitation"), f7b, rt=1.1)
        ex = T(r"\textbf{Place aux exercices !}", sc=0.85, color=JAUNE).move_to([-1.6, -3.45, 0])
        self.ecr(self.a("e8", "place aux exercices"), ex, rt=0.6)
        self.fin()

# ---------- exercice 1 : tube chargé ----------
def coupe_tube(cx, cy, r1, r2, avec_cotes=True):
    an = Annulus(inner_radius=r1, outer_radius=r2, color=ROUGE, fill_opacity=0.28, stroke_width=0).move_to(P(cx, cy))
    bords = VGroup(Circle(radius=r1, color=ROUGE, stroke_width=3).move_to(P(cx, cy)), Circle(radius=r2, color=ROUGE, stroke_width=3).move_to(P(cx, cy)))
    pl = VGroup(*[signe(cx + (r1 + r2)/2*np.cos(t), cy + (r1 + r2)/2*np.sin(t), 1, a=0.07, sw=2.5) for t in np.arange(8)*PI/4 + PI/8])
    ax = sortant(cx, cy, r=0.11, col=GRIS); lz = M(r"Oz", sc=0.5, color=GRIS).move_to(P(cx + 0.28, cy - 0.22))
    g = dict(an=an, bords=bords, pl=pl, ax=ax, lz=lz)
    if avec_cotes:
        a1, a2 = 3.6, -0.5
        g["c1"] = VGroup(Line(P(cx, cy), P(cx + r1*np.cos(a1), cy + r1*np.sin(a1)), color=CRAIE, stroke_width=2.5),
                         M(r"R_1", sc=0.55).move_to(P(cx + 0.55*r1*np.cos(a1), cy + 0.55*r1*np.sin(a1)) + 0.2*UP))
        g["c2"] = VGroup(Line(P(cx, cy), P(cx + r2*np.cos(a2), cy + r2*np.sin(a2)), color=CRAIE, stroke_width=2.5),
                         M(r"R_2", sc=0.55).move_to(P(cx + 0.62*r2*np.cos(a2), cy + 0.62*r2*np.sin(a2)) + 0.22*DOWN))
    return g

class S5(C):
    sid = "S5"
    def construct(self):
        self.entete(r"Exercice 1 -- un tube chargé", "Énoncé")
        cx, cy, r1, r2 = -4.75, 0.75, 0.6, 1.2
        g = coupe_tube(cx, cy, r1, r2)
        lc = T(r"vue en coupe", sc=0.5, color=GRIS).move_to(P(cx, cy - r2 - 0.3))
        lr = M(r"\rho", sc=0.65, color=ROUGE).move_to(P(cx + 0.65, cy + 1.25))
        self.at(self.t("f1"), FadeIn(g["an"]), Create(g["bords"]), FadeIn(g["ax"]), FadeIn(g["lz"]), FadeIn(lc), run_time=1.0)
        d1 = pos(T(r"long tube isolant, chargé \textbf{uniformément} dans son épaisseur", sc=0.66), -2.6, 2.25)
        self.at(self.a("f1", "un long tube"), FadeIn(g["pl"]), FadeIn(lr), Ecrire(d1, rt=1.1), run_time=1.1)
        d2 = pos(T(r"$R_1 = 1{,}0$ cm, \; $R_2 = 2{,}0$ cm, \; $\rho = 10\ \mu$C$\cdot$m$^{-3}$", sc=0.66), -2.6, 1.6)
        self.at(self.t("f2"), FadeIn(g["c1"]), run_time=0.5)
        self.at(self.a("f2", "Rayon extérieur"), FadeIn(g["c2"]), run_time=0.5)
        self.ecr(self.a("f2", "densité volumique"), d2, rt=1.1)
        d3 = pos(T(r"tube supposé \textbf{infini} \; ; \; $\varepsilon_0 = 8{,}85\times10^{-12}$ F$\cdot$m$^{-1}$", sc=0.66), -2.6, 0.95)
        self.ecr(self.a("f3", "On le suppose infini"), d3, rt=1.0)
        q = T(r"Champ $\vec E$ en tout point ? \quad Où est-il maximal ?", sc=0.78, color=ROUGE).move_to([1.55, -0.3, 0])
        self.ecr(self.a("f3", "Question"), q, rt=1.0); self.play(Create(enc(q)), run_time=0.4)
        rf = pos(T(r"Réfléchissons : très symétrique $\Rightarrow$ \textbf{Gauss}. Quelle surface ? Combien de zones ?", sc=0.64, color=BLEU), -2.6, -1.6)
        self.ecr(self.t("f4"), rf, rt=1.3)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([0.6, -2.95, 0])
        self.ecr(self.t("f5"), av, rt=0.7)
        pa, arc = chrono(3.9, -2.95)
        self.at(self.PH["f5"]["fin"], FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
        self.fin()

class S6(C):
    sid = "S6"
    def construct(self):
        self.entete(r"Exercice 1 -- la solution", "Solution")
        rappel(self, r"$R_1 = 1$ cm, \; $R_2 = 2$ cm, \; $\rho = 10\ \mu$C$\cdot$m$^{-3}$")
        sc = 0.64
        etape(self, 1, BLEU, 2.2, T(r"deux plans de symétrie par $M$ $\Rightarrow$ $\vec E$ \textbf{radial}", sc=sc), self.t("g1"), rt=1.0)
        m1b = pos(M(r"\text{invariances : } \vec E = E_r(r)\,\vec e_r", sc=0.7), -5.85, 1.6)
        # vue de côté : tube, surface de Gauss
        ya, a1, a2, xg0, xg1, rg = 1.05, 0.42, 0.85, 3.55, 5.25, 0.64
        mu = VGroup(*[Rectangle(width=4.1, height=a2 - a1, stroke_width=0).set_fill(ROUGE, 0.28).move_to(P(4.45, ya + s*(a1 + a2)/2)) for s in (1, -1)])
        bo = VGroup(*[Line(P(2.4, ya + s*a), P(6.5, ya + s*a), color=ROUGE, stroke_width=2.5) for s in (1, -1) for a in (a1, a2)])
        axe = DashedLine(P(2.3, ya), P(6.6, ya), color=GRIS, stroke_width=2); lz = M(r"z", sc=0.5, color=GRIS).move_to(P(6.45, ya - 0.2))
        mm = P(4.4, ya + rg); dmm = Dot(mm, radius=0.055, color=JAUNE); lmm = M(r"M", sc=0.5, color=JAUNE).move_to(mm + np.array([-0.22, 0.18, 0]))
        er = fleche((4.4, ya + rg), (4.4, ya + rg + 0.55), col=JAUNE, sw=4, tl=0.13)
        self.at(self.a("g1", "Deux plans de symétrie"), FadeIn(mu), Create(bo), Create(axe), FadeIn(lz), FadeIn(dmm), FadeIn(lmm), run_time=0.9)
        self.at(self.t("g2"), GrowArrow(er), run_time=0.5)
        self.ecr(self.a("g3", "E égale E r de r"), m1b, rt=0.9)
        sg = pointilles(Rectangle(width=xg1 - xg0, height=2*rg).move_to(P((xg0 + xg1)/2, ya)), n=34)
        lsg = M(r"\Sigma", sc=0.6, color=VERT).move_to(P(xg0 + 0.22, ya + rg - 0.24))
        crr = cote_v(xg0 + 0.42, ya, ya + rg, r"r"); chh = VGroup(DoubleArrow(P(xg0, ya - a2 - 0.22), P(xg1, ya - a2 - 0.22), buff=0, color=GRIS, stroke_width=2, tip_length=0.12),
                                                               M(r"h", sc=0.55, color=GRIS).move_to(P((xg0 + xg1)/2 + 0.25, ya - a2 - 0.42)))
        etape(self, 2, VERT, 0.95, T(r"$\Sigma$ : cylindre \textbf{fermé}, coaxial, rayon $r$, hauteur $h$", sc=sc), self.t("g4"), rt=1.0)
        self.at(self.a("g4", "un cylindre fermé"), Create(sg), FadeIn(lsg), FadeIn(crr), FadeIn(chh), run_time=0.9)
        nb = [fleche((xg0, ya - 0.3), (xg0 - 0.48, ya - 0.3), col=VERT, sw=3, tl=0.12), fleche((xg1, ya - 0.3), (xg1 + 0.48, ya - 0.3), col=VERT, sw=3, tl=0.12)]
        eb = [fleche((xg1, ya + 0.53), (xg1, ya + 0.93), col=JAUNE, sw=3, tl=0.11)]
        lnb = M(r"\vec n", sc=0.5, color=VERT).next_to(nb[1].get_end(), UP, buff=0.06)
        m2 = pos(T(r"bases : $\vec E \perp \vec n$, flux nul \;;\; $\Phi = 2\pi r h\,E_r(r)$", sc=sc), -5.85, 0.38)
        self.at(self.a("g5", "les deux bases"), *[Indicate(sg, color=VERT, scale_factor=1.03)], *[GrowArrow(n) for n in nb], FadeIn(lnb), run_time=0.8)
        self.at(self.a("g5", "le champ y est tangent"), *[GrowArrow(e) for e in eb], run_time=0.5)
        self.ecr(self.t("g6"), m2, rt=1.1)
        m3 = etape(self, 3, ORANGE, -0.35, M(r"r < R_1 :\ Q_{\text{int}} = 0 \;\Rightarrow\; E_r = 0", sc=0.68), self.a("g7", "Dans le creux"), rt=0.9)
        m4 = pos(M(r"R_1 \le r \le R_2 :\ Q_{\text{int}} = \rho\pi h\,(r^2 - R_1^2)", sc=0.68), -5.85, -1.02)
        self.ecr(self.t("g8"), m4, rt=1.0)
        m5 = pos(M(r"E_r = \frac{\rho\,(r^2 - R_1^2)}{2\varepsilon_0\,r}", sc=0.7, color=VERT), -4.6, -1.78)
        self.ecr(self.a("g8b", "E r égale"), m5, rt=1.0); self.play(Create(enc(m5, col=VERT, buff=0.1)), run_time=0.3)
        m6 = pos(M(r"r \ge R_2 :\ E_r = \frac{\rho\,(R_2^2 - R_1^2)}{2\varepsilon_0\,r}", sc=0.7, color=VERT), -5.85, -2.65)
        self.ecr(self.t("g9"), m6, rt=1.1); self.play(Create(enc(m6, col=VERT, buff=0.1)), run_time=0.3)
        verif(self, JAUNE, -3.5, T(r"continu en $R_1$ et $R_2$ \;;\; loin : $\lambda/(2\pi\varepsilon_0 r)$, un \textbf{fil}", sc=0.6), self.t("g10"), rt=1.0)
        # graphe E_r(r)
        ax, fr = cadre(4.4, -1.6, 4.2, 1.9, 0, 6, 0, 10.5)
        k = 10e-6/(2*8.85e-12)/1000      # rho/(2 eps0) en kV/m par m
        rs = np.linspace(0, 6, 241); Es = np.where(rs < 1, 0, np.where(rs < 2, k*((rs/100)**2 - 1e-4)/(rs/100), k*3e-4/(rs/100)))
        cb = courbe(ax, rs, Es, col=ORANGE)
        lE = M(r"E_r\ (\mathrm{kV/m})", sc=0.5, color=ORANGE).move_to(ax.c2p(1.25, 9.2)); lr = M(r"r\ (\mathrm{cm})", sc=0.5, color=GRIS).move_to(ax.c2p(5.35, 1.0))
        tk = VGroup(*[M(t, sc=0.5, color=GRIS).move_to(ax.c2p(v, 0) + 0.25*DOWN) for t, v in ((r"R_1", 1), (r"R_2", 2))])
        gu = VGroup(*[DashedLine(ax.c2p(v, 0), ax.c2p(v, 10.5), color=GRIS, stroke_width=1.2, stroke_opacity=0.5) for v in (1, 2)])
        self.at(self.a("g12", "Le champ croît"), Create(fr), FadeIn(gu), FadeIn(tk), FadeIn(lE), FadeIn(lr), Create(cb), run_time=1.2)
        ca4 = carte(4, JAUNE, 2.55, -3.3)
        m7 = pos(M(r"E_{max} = E(R_2) \approx 8{,}5\ \mathrm{kV\cdot m^{-1}}", sc=0.66, color=JAUNE), 3.0, -3.3)
        pk = Dot(ax.c2p(2, k*3e-4/0.02), radius=0.07, color=JAUNE)
        self.at(self.a("g12", "il est maximal"), Create(ca4[0]), FadeIn(ca4[1]), FadeIn(pk), Ecrire(m7, rt=0.9), run_time=0.9)
        self.play(Create(enc(m7, col=JAUNE, buff=0.1)), run_time=0.3)
        self.at(self.a("g13", "nuage d'orage"), Indicate(m7, color=JAUNE, scale_factor=1.08), run_time=0.7)
        self.fin()

# ---------- exercice 2 : boule et coquille ----------
def boule_coquille(cx, cy, R, signes=True):
    bo = Circle(radius=R, color=ROUGE, stroke_width=3).set_fill(ROUGE, 0.28).move_to(P(cx, cy))
    co = Circle(radius=2*R, color=BLEU, stroke_width=4).move_to(P(cx, cy))
    o = Dot(P(cx, cy), radius=0.05, color=CRAIE); lo = M(r"O", sc=0.5).move_to(P(cx - 0.18, cy - 0.2))
    pl = VGroup(*[signe(cx + dx, cy + dy, 1, a=0.07, sw=2.5) for dx, dy in [(0.3*R, 0.45*R), (-0.45*R, 0.25*R), (0.45*R, -0.3*R), (-0.15*R, -0.55*R)]])
    mo = VGroup(*[signe(cx + 2*R*np.cos(t), cy + 2*R*np.sin(t), -1, a=0.07, sw=2.5).shift(0.17*np.array([np.cos(t), np.sin(t), 0])) for t in np.arange(10)*PI/5 + 0.3])
    return dict(bo=bo, co=co, o=o, lo=lo, pl=pl if signes else VGroup(), mo=mo if signes else VGroup())

class S7(C):
    sid = "S7"
    def construct(self):
        self.entete(r"Exercice 2 -- une boule et sa coquille", "Énoncé")
        cx, cy, R = -4.75, 0.45, 0.68
        g = boule_coquille(cx, cy, R)
        lQ = M(r"+Q", sc=0.55, color=ROUGE).move_to(P(cx + 0.25, cy + R + 0.22))
        lmQ = M(r"-Q", sc=0.6, color=BLEU).move_to(P(cx + 1.6, cy + 1.28))
        cR = VGroup(Line(P(cx, cy), P(cx - R, cy), color=CRAIE, stroke_width=2.5), M(r"R", sc=0.5).move_to(P(cx - R/2, cy + 0.17)))
        c2R = VGroup(Line(P(cx, cy), P(cx + 2*R*np.cos(-0.6), cy + 2*R*np.sin(-0.6)), color=CRAIE, stroke_width=2.5),
                     M(r"2R", sc=0.5).move_to(P(cx + 1.25*R*np.cos(-0.6), cy + 1.25*R*np.sin(-0.6)) + 0.2*DOWN + 0.1*LEFT))
        self.at(self.a("h1", "Une boule"), Create(g["bo"]), FadeIn(g["o"]), FadeIn(g["lo"]), FadeIn(cR), run_time=0.8)
        d1 = pos(T(r"boule de rayon $R = 5{,}0$ cm, charge $Q = 10$ nC \textbf{uniforme} en volume", sc=0.64), -2.5, 2.25)
        self.at(self.a("h1", "porte la charge"), FadeIn(g["pl"]), FadeIn(lQ), Ecrire(d1, rt=1.2), run_time=1.2)
        d2 = pos(T(r"coquille sphérique mince, de rayon $2R$ : charge $-Q$ en surface", sc=0.64), -2.5, 1.6)
        self.at(self.t("h2"), Create(g["co"]), FadeIn(c2R), run_time=0.8)
        self.at(self.a("h2", "la charge opposée"), FadeIn(g["mo"]), FadeIn(lmQ), Ecrire(d2, rt=1.1), run_time=1.1)
        d3 = pos(T(r"$1/(4\pi\varepsilon_0) = 9{,}0\times10^{9}$ SI, \quad $V(\infty) = 0$", sc=0.64), -2.5, 0.95)
        self.ecr(self.t("h3"), d3, rt=1.0)
        q = VGroup(T(r"$\vec E$ et $V$ en tout point ? \quad $V(O)$ ?", sc=0.76, color=ROUGE), T(r"Tracer $E_r(r)$ et $V(r)$", sc=0.76, color=ROUGE)).arrange(DOWN, buff=0.15).move_to([1.6, -0.45, 0])
        self.ecr(self.t("h4"), q, rt=1.2); self.play(Create(enc(q)), run_time=0.4)
        rf = pos(T(r"Réfléchissons : symétrie \textbf{sphérique} $\Rightarrow$ sphère de Gauss ; puis $V$ depuis l'infini", sc=0.64, color=BLEU), -2.5, -1.75)
        self.ecr(self.t("h5"), rf, rt=1.3)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([0.6, -2.95, 0])
        self.ecr(self.t("h6"), av, rt=0.7)
        pa, arc = chrono(3.9, -2.95)
        self.at(self.PH["h6"]["fin"], FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
        self.fin()

class S8(C):
    sid = "S8"
    def construct(self):
        self.entete(r"Exercice 2 -- le champ", "Solution")
        rappel(self, r"$Q = 10$ nC, \; $R = 5$ cm, \; coquille $-Q$ en $2R$")
        cx, cy, R = 4.6, 0.75, 0.55
        g = boule_coquille(cx, cy, R)
        self.play(Create(g["bo"]), Create(g["co"]), FadeIn(g["o"]), FadeIn(g["lo"]), FadeIn(g["pl"]), FadeIn(g["mo"]), run_time=0.8)
        etape(self, 1, BLEU, 2.2, M(r"\text{symétrie sphérique : } \vec E = E_r(r)\,\vec e_r", sc=0.7), self.t("i1"), rt=1.0)
        rg = 0.82; tM = 0.7
        sg = pointilles(Circle(radius=rg).move_to(P(cx, cy)), n=30)
        mm = P(cx + rg*np.cos(tM), cy + rg*np.sin(tM)); dm = Dot(mm, radius=0.05, color=JAUNE)
        lm = M(r"M", sc=0.5, color=JAUNE).move_to(mm + np.array([-0.05, 0.25, 0]))
        er = Arrow(mm, mm + 0.55*np.array([np.cos(tM), np.sin(tM), 0]), buff=0, color=JAUNE, stroke_width=4, tip_length=0.13)
        ler = M(r"\vec E", sc=0.55, color=JAUNE).next_to(er.get_end(), RIGHT, buff=0.05)
        self.at(self.a("i1", "plan de symétrie"), FadeIn(dm), FadeIn(lm), GrowArrow(er), FadeIn(ler), run_time=0.7)
        etape(self, 2, VERT, 1.45, M(r"\text{sphère de rayon } r :\ \ \Phi = 4\pi r^2\,E_r(r)", sc=0.7), self.t("i2"), rt=1.0)
        lsg = M(r"\Sigma", sc=0.55, color=VERT).move_to(P(cx - rg - 0.05, cy - rg + 0.05))
        self.at(self.a("i2", "la sphère de Gauss"), Create(sg), FadeIn(lsg), run_time=0.8)
        m3 = etape(self, 3, ORANGE, 0.6, M(r"r \le R :\ Q_{\text{int}} = Q\,\frac{r^3}{R^3}", sc=0.68), self.a("i3", "Dans la boule"), rt=0.9)
        m3b = M(r"\Rightarrow\; E_r = \frac{Q\,r}{4\pi\varepsilon_0 R^3}", sc=0.68, color=VERT).next_to(m3, RIGHT, buff=0.25)
        self.ecr(self.t("i4"), m3b, rt=0.9)
        m4 = pos(M(r"R \le r < 2R :\ Q_{\text{int}} = Q \;\Rightarrow\; E_r = \frac{Q}{4\pi\varepsilon_0 r^2}", sc=0.68, color=VERT), -5.85, -0.3)
        self.ecr(self.t("i5"), m4, rt=1.1)
        m5 = pos(M(r"r > 2R :\ Q_{\text{int}} = Q - Q = 0 \;\Rightarrow\; \vec E = \vec 0", sc=0.68, color=VERT), -5.85, -1.1)
        ext = pointilles(Circle(radius=2*R + 0.32).move_to(P(cx, cy)), n=40, col=GRIS, sw=2)
        ecr_ = T(r"la coquille fait \textbf{écran}", sc=0.58, color=BLEU).move_to(P(cx, cy - 2*R - 0.75))
        self.at(self.t("i6"), Create(ext), Ecrire(m5, rt=1.1), run_time=1.1)
        self.ecr(self.a("i6", "la coquille fait écran"), ecr_, rt=0.7)
        m6 = pos(M(r"E(R) = \frac{9\times10^{9} \times 10^{-8}}{0{,}05^2} = 36\ \mathrm{kV\cdot m^{-1}}", sc=0.68, color=JAUNE), -5.85, -1.95)
        self.ecr(self.t("i7"), m6, rt=1.1); self.play(Create(enc(m6, col=JAUNE, buff=0.1)), run_time=0.3)
        verif(self, JAUNE, -2.85, T(r"continu en $R$ : pas de charge surfacique sur la boule", sc=0.62), self.t("i8"), rt=1.0)
        m8 = pos(T(r"en $2R$ : saut de $9$ kV$\cdot$m$^{-1}$ à $0$, \; c'est $|\sigma|/\varepsilon_0$", sc=0.62, color=ROUGE), -5.85, -3.5)
        self.ecr(self.t("i9"), m8, rt=1.0)
        self.at(self.a("i9", "la signature"), Indicate(g["co"], color=ROUGE, scale_factor=1.06), run_time=0.7)
        self.fin()

class S9(C):
    sid = "S9"
    def construct(self):
        self.entete(r"Exercice 2 -- le potentiel", "Solution")
        rappel(self, r"$Q = 10$ nC, \; $R = 5$ cm, \; $V(\infty) = 0$")
        sc = 0.68
        etape(self, 4, BLEU, 2.2, M(r"\mathrm{d}V = -E_r\,\mathrm{d}r, \quad \text{depuis } V(\infty) = 0", sc=sc), self.a("j1", "On part de l'infini"), rt=1.0)
        a2 = pos(M(r"r \ge 2R :\ V = 0", sc=sc), -5.85, 1.5)
        self.ecr(self.t("j2"), a2, rt=0.7)
        a3 = pos(M(r"R \le r \le 2R :\ V = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{r} - \frac{1}{2R}\right)", sc=sc), -5.85, 0.72)
        self.ecr(self.t("j3"), a3, rt=1.2)
        a4 = pos(M(r"V(R) = 9\times10^{9}\times10^{-8}\times(20 - 10) = 900\ \mathrm{V}", sc=0.62, color=GRIS), -5.85, -0.02)
        self.ecr(self.t("j4"), a4, rt=0.9)
        a5 = pos(M(r"r \le R :\ V = V(R) + \frac{Q\,(R^2 - r^2)}{8\pi\varepsilon_0 R^3}", sc=sc), -5.85, -0.78)
        self.ecr(self.t("j5"), a5, rt=1.1)
        a6 = pos(M(r"V(0) = \frac{Q}{4\pi\varepsilon_0 R} = 1\,800\ \mathrm{V}", sc=0.72, color=VERT), -5.85, -1.62)
        self.ecr(self.t("j6"), a6, rt=1.0); self.play(Create(enc(a6, col=VERT, buff=0.1)), run_time=0.3)
        # graphes E_r(r) et V(r), même échelle en r
        rr = np.linspace(0, 3, 301)
        Er = np.where(rr < 1, 36*rr, np.where(rr < 2, 36/np.maximum(rr, 1e-9)**2, 0))
        Vr = np.where(rr < 1, 1800 - 900*rr**2, np.where(rr < 2, 1800/np.maximum(rr, 1e-9) - 900, 0))
        aE, fE = cadre(4.55, 1.3, 4.0, 1.55, 0, 3, -4, 42); aV, fV = cadre(4.55, -0.72, 4.0, 1.55, 0, 3, -200, 2100)
        cE1 = courbe(aE, rr[rr < 2], Er[rr < 2], col=ORANGE); cE2 = courbe(aE, [2, 3], [0, 0], col=ORANGE)
        saut = DashedLine(aE.c2p(2, 9), aE.c2p(2, 0), color=ROUGE, stroke_width=3)
        cV = courbe(aV, rr, Vr, col=BLEU)
        gu = VGroup(*[DashedLine(aE.c2p(v, -4), aE.c2p(v, 42), color=GRIS, stroke_width=1.2, stroke_opacity=0.5) for v in (1, 2)],
                    *[DashedLine(aV.c2p(v, -200), aV.c2p(v, 2100), color=GRIS, stroke_width=1.2, stroke_opacity=0.5) for v in (1, 2)])
        tk = VGroup(*[M(t, sc=0.5, color=GRIS).move_to(aV.c2p(v, -200) + 0.22*DOWN) for t, v in ((r"R", 1), (r"2R", 2))])
        lE = M(r"E_r\ (\mathrm{kV/m})", sc=0.48, color=ORANGE).move_to(aE.c2p(2.45, 34)); lV = M(r"V\ (\mathrm{V})", sc=0.48, color=BLEU).move_to(aV.c2p(2.55, 1700))
        v36 = M(r"36", sc=0.45, color=ORANGE).move_to(aE.c2p(1.0, 36) + 0.2*LEFT + 0.05*DOWN); v9 = M(r"9", sc=0.45, color=ROUGE).move_to(aE.c2p(2.0, 9) + 0.2*RIGHT + 0.12*UP)
        v18 = M(r"1\,800", sc=0.45, color=BLEU).move_to(aV.c2p(0.0, 1800) + 0.45*RIGHT + 0.2*DOWN); v9b = M(r"900", sc=0.45, color=BLEU).move_to(aV.c2p(1.0, 900) + 0.35*RIGHT + 0.12*UP)
        c5 = carte(5, ORANGE, 2.1, 1.3)
        self.at(self.t("j7"), Create(c5[0]), FadeIn(c5[1]), Create(fE), Create(fV), FadeIn(gu), FadeIn(tk), FadeIn(lE), FadeIn(lV), run_time=0.9)
        self.at(self.a("j7", "une droite"), Create(cE1), FadeIn(v36), run_time=1.4)
        self.at(self.a("j7", "puis un saut"), Create(saut), Create(cE2), FadeIn(v9), run_time=0.6)
        self.at(self.a("j8", "ne saute jamais"), Create(cV), FadeIn(v18), FadeIn(v9b), run_time=1.6)
        verif(self, JAUNE, -2.65, T(r"sans coquille : $V(0) = 2\,700$ V \;;\; la coquille ajoute $-900$ V, uniformes à l'intérieur", sc=0.62), self.t("j9"), rt=1.3)
        j10 = pos(T(r"superposition : dans une coquille chargée, $\vec E = \vec 0$ et $V$ uniforme", sc=0.62, color=GRIS), -5.85, -3.35)
        self.ecr(self.t("j10"), j10, rt=1.0)
        self.fin()

# ---------- exercice 3 : condensateur plan ----------
def electron(x, y, r=0.13):
    return VGroup(Circle(radius=r, color=BLEU, stroke_width=3).set_fill(BLEU, 0.6).move_to(P(x, y)), signe(x, y, -1, a=0.06, sw=2.5))

class S10(C):
    sid = "S10"
    def construct(self):
        self.entete(r"Exercice 3 -- un condensateur plan", "Énoncé")
        x0, x1, yh, yb = -6.0, -3.2, 1.75, 0.35
        ph = Line(P(x0, yh), P(x1, yh), color=ROUGE, stroke_width=7); pb = Line(P(x0, yb), P(x1, yb), color=BLEU, stroke_width=7)
        lh = M(r"+Q,\ V = U", sc=0.52, color=ROUGE).next_to(ph, UP, buff=0.12); lb = M(r"-Q,\ V = 0", sc=0.52, color=BLEU).next_to(pb, DOWN, buff=0.12)
        cd = cote_v(x1 + 0.3, yb, yh, r"d")
        lS = M(r"S", sc=0.55).move_to(P(x0 + 0.35, yh + 0.32))
        self.at(self.t("k1"), Create(ph), Create(pb), run_time=0.8)
        d1 = pos(T(r"condensateur plan \textbf{à air} : $S = 0{,}10$ m$^2$, \; $d = 1{,}0$ mm, \; $U = 500$ V", sc=0.62), -2.4, 2.25)
        self.at(self.t("k2"), FadeIn(lh), FadeIn(lb), FadeIn(cd), FadeIn(lS), Ecrire(d1, rt=1.3), run_time=1.3)
        d2 = pos(T(r"$\varepsilon_0 = 8{,}85\times10^{-12}$ F$\cdot$m$^{-1}$ ; électron : $-e$, $e = 1{,}6\times10^{-19}$ C, $m = 9{,}1\times10^{-31}$ kg", sc=0.58), -2.4, 1.65)
        d3 = pos(T(r"$d$ : écartement (et $e$ : charge élémentaire) \; ; \; effets de bord négligés", sc=0.58, color=GRIS), -2.4, 1.1)
        self.ecr(self.t("k3"), d2, rt=1.2); self.ecr(self.a("k3", "Et on néglige"), d3, rt=1.0)
        q1 = pos(T(r"Q1. $\vec E$, $C$, $Q$ et l'énergie $W_e$ ?", sc=0.66, color=ROUGE), -2.4, 0.3)
        q2 = pos(T(r"Q2. électron lâché sans vitesse sur l'armature $-$ : vitesse à l'arrivée ?", sc=0.66, color=ROUGE), -2.4, -0.3)
        q3 = pos(T(r"Q3. force d'attraction entre les armatures ?", sc=0.66, color=ROUGE), -2.4, -0.9)
        el = electron(-4.6, yb + 0.2); tr = DashedLine(P(-4.6, yb + 0.38), P(-4.6, yh - 0.15), color=BLEU, stroke_width=2.5)
        tip = pointe(P(-4.6, (yb + yh)/2 + 0.1), (0, 1, 0), col=BLEU, L=0.16)
        self.ecr(self.t("k4"), q1, rt=0.9)
        self.at(self.t("k5"), FadeIn(el), Ecrire(q2, rt=1.3), run_time=1.3)
        self.at(self.a("k5", "À quelle vitesse"), Create(tr), FadeIn(tip), run_time=0.6)
        self.ecr(self.t("k6"), q3, rt=0.9); self.play(Create(enc(VGroup(q1, q2, q3), buff=0.18)), run_time=0.4)
        rf = pos(T(r"Réfléchissons : deux plans infinis $\Rightarrow$ \textbf{superposition} ; électron : énergie $qV$", sc=0.64, color=BLEU), -5.9, -1.95)
        self.ecr(self.t("k7"), rf, rt=1.3)
        av = T(r"\textbf{À vous !} \; Pause, et essayez", sc=0.8, color=JAUNE).move_to([-1.0, -3.0, 0])
        self.ecr(self.t("k8"), av, rt=0.7)
        pa, arc = chrono(2.3, -3.0)
        self.at(self.PH["k8"]["fin"], FadeIn(pa), Create(arc), run_time=0.3)
        self.play(Uncreate(arc), run_time=4.5); self.play(FadeOut(pa), run_time=0.2)
        self.fin()

class S11(C):
    sid = "S11"
    def construct(self):
        self.entete(r"Exercice 3 -- champ, capacité et énergie", "Solution")
        rappel(self, r"$S = 0{,}10$ m$^2$, \; $d = 1{,}0$ mm, \; $U = 500$ V")
        x0, x1, yh, yb = 3.0, 6.1, 1.25, -0.45
        cp = condensateur(x0, x1, yh, yb)
        etape(self, 1, BLEU, 2.2, T(r"$d \ll \sqrt{S} \approx 30$ cm : deux \textbf{plans infinis} $\pm\sigma$", sc=0.64), self.t("l1"), rt=1.0)
        self.at(self.a("l1", "deux plans infinis"), Create(cp), run_time=0.8)
        sp = superpo(3.4, yh, yb, h=0.46, dx=0.4)
        l2 = pos(T(r"chaque plan : $\sigma/(2\varepsilon_0)$, de part et d'autre", sc=0.64), -5.85, 1.55)
        self.at(self.t("l2"), FadeIn(sp), Ecrire(l2, rt=1.0), run_time=1.0)
        ym = (yh + yb)/2
        bg = VGroup(*[fleche((x, yh - 0.14), (x, yb + 0.14), col=JAUNE, sw=4, tl=0.16) for x in (5.0, 5.75)])
        lb = M(r"\frac{\sigma}{\varepsilon_0}", sc=0.62, color=JAUNE).next_to(bg, LEFT, buff=0.12)
        z1 = M(r"\vec 0", sc=0.6, color=GRIS).move_to(P(5.37, yh + 0.38)); z2 = M(r"\vec 0", sc=0.6, color=GRIS).move_to(P(5.37, yb - 0.38))
        l3 = pos(M(r"\text{entre : } E = \frac{\sigma}{\varepsilon_0}\qquad \text{dehors : } \vec E = \vec 0", sc=0.7), -5.85, 0.8)
        self.at(self.t("l3"), *[GrowArrow(b) for b in bg], FadeIn(lb), Ecrire(l3, rt=1.2), run_time=1.2)
        self.at(self.a("l3", "Dehors"), FadeIn(z1), FadeIn(z2), run_time=0.5)
        cdd = cote_v(6.4, yb, yh, r"d")
        l4 = etape(self, 2, VERT, -0.05, M(r"U = \int_+^- \vec E\cdot\mathrm{d}\vec\ell = E\,d \;\Rightarrow\; E = \frac{U}{d} = 5{,}0\times10^{5}\ \mathrm{V\cdot m^{-1}}", sc=0.66), self.t("l4"), rt=1.4)
        self.play(FadeIn(cdd), run_time=0.3)
        l5 = pos(T(r"six fois moins que le claquage de l'air ($3$ MV$\cdot$m$^{-1}$) : pas d'étincelle", sc=0.58, color=GRIS), -5.85, -0.82)
        self.ecr(self.t("l5"), l5, rt=1.0)
        l6 = pos(M(r"C = \frac{Q}{U} = \frac{\varepsilon_0 S}{d} \approx 0{,}89\ \mathrm{nF} \qquad Q = CU \approx 0{,}44\ \mu\mathrm{C}", sc=0.68, color=VERT), -5.85, -1.6)
        self.ecr(self.t("l6"), l6, rt=1.4); self.play(Create(enc(l6, col=VERT, buff=0.1)), run_time=0.3)
        l7 = etape(self, 3, ORANGE, -2.55, M(r"W_e = \frac{CU^2}{2} \approx 0{,}11\ \mathrm{mJ}", sc=0.72, color=JAUNE), self.t("l7"), rt=0.9)
        self.play(Create(enc(l7, col=JAUNE, buff=0.1)), run_time=0.3)
        verif(self, JAUNE, -3.42, M(r"\frac{\varepsilon_0 E^2}{2}\times S\,d = \frac{8{,}85\times10^{-12}\times(5\times10^5)^2}{2}\times10^{-4} \approx 0{,}11\ \mathrm{mJ}", sc=0.6), self.t("l8"), rt=1.3)
        self.fin()

class S12(C):
    sid = "S12"
    def construct(self):
        self.entete(r"Exercice 3 -- l'électron et la force", "Solution")
        rappel(self, r"$U = 500$ V, \; $Q \approx 0{,}44\ \mu$C, \; $W_e \approx 0{,}11$ mJ")
        x0, x1, yh, yb = 2.6, 5.0, 1.3, -0.6
        ph = Line(P(x0, yh), P(x1, yh), color=ROUGE, stroke_width=7); pb = Line(P(x0, yb), P(x1, yb), color=BLEU, stroke_width=7)
        lh = M(r"+Q,\ V = U", sc=0.52, color=ROUGE).next_to(ph, RIGHT, buff=0.12); lb = M(r"-Q,\ V = 0", sc=0.52, color=BLEU).next_to(pb, RIGHT, buff=0.12)
        Ev = VGroup(*[fleche((x, yh - 0.15), (x, yb + 0.15), col=JAUNE, sw=3, tl=0.13) for x in (4.45, 4.85)])
        lE = M(r"\vec E", sc=0.55, color=JAUNE).next_to(Ev, LEFT, buff=0.08)
        self.play(Create(ph), Create(pb), FadeIn(lh), FadeIn(lb), *[GrowArrow(e) for e in Ev], FadeIn(lE), run_time=0.8)
        etape(self, 4, BLEU, 2.2, T(r"électron : $E_p = -e\,V$, énergie mécanique \textbf{conservée}", sc=0.64), self.t("m1"), rt=1.0)
        el = electron(2.95, yb + 0.22)
        tr = DashedLine(P(2.95, yb + 0.4), P(2.95, yh - 0.16), color=BLEU, stroke_width=2.5); tip = pointe(P(2.95, (yh + yb)/2 + 0.2), (0, 1, 0), col=BLEU, L=0.16)
        fe = fleche((2.95, yb + 0.22), (2.95, yb + 0.9), col=VERT, sw=4, tl=0.13); lfe = M(r"-e\vec E", sc=0.5, color=VERT).next_to(fe, RIGHT, buff=0.06)
        m2 = pos(T(r"armature $-$ ($V = 0$) $\to$ armature $+$ ($V = U$) : il \textbf{remonte} les potentiels", sc=0.62), -5.85, 1.55)
        self.at(self.t("m2"), FadeIn(el), GrowArrow(fe), FadeIn(lfe), Ecrire(m2, rt=1.3), run_time=1.3)
        self.at(self.a("m2", "et arrive au potentiel"), Create(tr), FadeIn(tip), run_time=0.7)
        m3 = pos(M(r"0 + (-e)\times 0 = \tfrac12 m v^2 + (-e)\,U \;\Rightarrow\; \tfrac12 m v^2 = eU = 500\ \mathrm{eV}", sc=0.66), -5.85, 0.82)
        self.ecr(self.t("m3"), m3, rt=1.3)
        m4 = pos(M(r"v = \sqrt{\frac{2eU}{m}} \approx 1{,}3\times10^{7}\ \mathrm{m\cdot s^{-1}} \approx 4\,\%\ \text{de } c", sc=0.68, color=VERT), -5.85, -0.02)
        self.ecr(self.t("m4"), m4, rt=1.2); self.play(Create(enc(m4, col=VERT, buff=0.1)), run_time=0.3)
        m5 = etape(self, 5, ROUGE, -0.95, T(r"piège : une armature ne subit \textbf{pas} son propre champ", sc=0.64, color=ROUGE), self.a("m5", "Le piège"), rt=1.0)
        self.play(FadeOut(el), FadeOut(tr), FadeOut(tip), FadeOut(fe), FadeOut(lfe), run_time=0.4)
        fh = fleche((3.7, yh + 0.75), (3.7, yh + 0.1), col=ROUGE, sw=5, tl=0.15); fb = fleche((3.7, yb - 0.75), (3.7, yb - 0.1), col=ROUGE, sw=5, tl=0.15)
        lfh = M(r"\vec F", sc=0.55, color=ROUGE).next_to(fh, LEFT, buff=0.08); lfb = M(r"-\vec F", sc=0.55, color=ROUGE).next_to(fb, LEFT, buff=0.08)
        m6 = pos(T(r"armature $-$ : champ de l'armature $+$ \textbf{seule}, $\sigma/(2\varepsilon_0)$", sc=0.62), -5.85, -1.65)
        self.at(self.t("m6"), GrowArrow(fb), FadeIn(lfb), Ecrire(m6, rt=1.1), run_time=1.1)
        m7 = pos(M(r"F = Q\,\frac{\sigma}{2\varepsilon_0} = \frac{Q^2}{2\varepsilon_0 S} \approx 0{,}11\ \mathrm{N}", sc=0.7, color=JAUNE), -5.85, -2.5)
        self.at(self.t("m7"), GrowArrow(fh), FadeIn(lfh), Ecrire(m7, rt=1.1), run_time=1.1); self.play(Create(enc(m7, col=JAUNE, buff=0.1)), run_time=0.3)
        lat = T(r"attraction", sc=0.55, color=ROUGE).move_to(P(3.95, yb - 1.05))
        self.at(self.a("m7", "Une force attractive"), FadeIn(lat), run_time=0.4)
        verif(self, JAUNE, -3.4, M(r"F\,d \approx 0{,}11\ \mathrm{N} \times 10^{-3}\ \mathrm{m} = 0{,}11\ \mathrm{mJ} = W_e", sc=0.66), self.t("m8"), rt=1.2)
        self.fin()

class S13(C):
    sid = "S13"
    def construct(self):
        self.entete(r"Ce qu'il faut retenir", "Méthode")
        t0 = pos(T(r"la méthode pour \textbf{calculer un champ électrostatique}", sc=0.74, color=GRIS), -6.3, 2.2)
        self.ecr(self.t("n1"), t0, rt=0.9)
        pts = [("n2", 1, r"\textbf{symétries} $\to$ direction de $\vec E$ \;;\; \textbf{invariances} $\to$ variables", BLEU, 1.4),
               ("n3", 2, r"surface de Gauss \textbf{fermée}, passant par $M$ (bases du cylindre !)", VERT, 0.62),
               ("n4", 3, r"$Q_{\text{int}}$ zone par zone, puis $\Phi = Q_{\text{int}}/\varepsilon_0$", ORANGE, -0.16),
               ("n5", 4, r"potentiel : $\mathrm{d}V = -E_r\,\mathrm{d}r$, une constante par zone, $V$ \textbf{continu}", ROUGE, -0.94),
               ("n7", 5, r"\textbf{vérifier} : continuité, limite à grande distance, ordre de grandeur", JAUNE, -2.42)]
        for ph_, k, txt, c, yy in pts:
            ca = carte(k, c, -5.9, yy); tx = pos(T(txt, sc=0.7), -5.35, yy)
            self.at(self.t(ph_), Create(ca[0]), FadeIn(ca[1]), Ecrire(tx, rt=1.0), run_time=0.8)
            if ph_ == "n5":
                n6 = pos(T(r"sinon : \textbf{superposition} \;;\; charge en mouvement : $E_p = qV$", sc=0.64, color=GRIS), -5.35, -1.68)
                self.ecr(self.t("n6"), n6, rt=1.0)
        nx = T(r"Prochaine vidéo : magnétostatique et théorème d'Ampère", sc=0.66, color=GRIS).move_to([0, -3.4, 0])
        self.ecr(self.t("n8"), nx, rt=1.2)
        self.fin()
