from manim import *
import json, numpy as np
config.background_color = "#1F2A24"
config.frame_rate = 30
tpl = TexTemplate()
tpl.add_to_preamble(r"\usepackage[T1]{fontenc}\usepackage[utf8]{inputenc}\usepackage{mathpazo}")
CRAIE, JAUNE, ROUGE, BLEU, VERT, ORANGE, GRIS = "#EDEBE4", "#F2D16B", "#F08A7E", "#8EC5F2", "#9BD49A", "#F2B36B", "#8FA097"
TLALL = json.load(open("timeline.json"))

def T(*s, sc=0.7, color=CRAIE, **k): return Tex(*s, tex_template=tpl, color=color, **k).scale(sc)
def M(*s, sc=0.85, color=CRAIE, **k): return MathTex(*s, tex_template=tpl, color=color, **k).scale(sc)
def ch(s): return r"\mathrm{" + s + "}"
def pos(m, x, y, bord=LEFT): m.move_to([x, y, 0], aligned_edge=bord); return m

def glyphes(mob):
    g = [m for m in mob.family_members_with_points() if len(m.submobjects) == 0]
    return sorted(g, key=lambda m: (round(m.get_left()[0], 1), -m.get_center()[1]))
class Ecrire(LaggedStart):
    def __init__(self, mob, rt=None, **kw):
        gs = glyphes(mob)
        if rt is None: rt = float(np.clip(len(gs) / 20, 0.5, 2.2))
        super().__init__(*[FadeIn(g, shift=0.04*UP) for g in gs], lag_ratio=0.35, run_time=rt, **kw)

class Cours(Scene):
    sid = None
    def setup(self):
        sc = TLALL["scenes"][self.sid]; self.duree = sc["duree"]; self.PH = {p["id"]: p for p in sc["phrases"]}
    def t(self, i): return self.PH[i]["debut"]
    def a(self, i, frag):
        p = self.PH[i]; txt = p["dit"]; k = txt.index(frag)
        return p["debut"] + k / len(txt) * (p["fin"] - p["debut"])
    def jusqua(self, t):
        dt = t - self.renderer.time
        if dt > 1/30: self.wait(dt)
        elif dt < -0.5: print(f"RETARD {self.sid} {dt:.2f}s à t={t:.1f}")
    def at(self, t, *anims, **kw):
        self.jusqua(t); self.play(*anims, **kw)
    def ecr(self, t, mob, **kw): self.at(t, Ecrire(mob, **kw))
    def entete(self, txt, tag=""):
        ti = T(r"\textbf{" + txt + "}", sc=0.85, color=JAUNE).to_corner(UL, buff=0.5)
        y = ti.get_bottom()[1] - 0.14
        tr = Line([ti.get_left()[0], y, 0], [6.6, y, 0], color=JAUNE, stroke_width=1.5, stroke_opacity=0.5)
        grp = [Ecrire(ti, rt=0.6), Create(tr)]
        if tag:
            tg = T(tag, sc=0.5, color=GRIS).to_corner(UR, buff=0.55); grp.append(FadeIn(tg))
        self.play(*grp, run_time=0.7)
    def fin(self):
        self.jusqua(self.duree - 0.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.35)
        r = self.duree - self.renderer.time
        if r > 0.4/30: self.wait(max(r, 1/30))
