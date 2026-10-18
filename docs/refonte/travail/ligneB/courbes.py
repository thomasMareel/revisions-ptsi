#!/usr/bin/env python3
"""Courbe principale des simulateurs en --chap-vif (SPEC §3.7, §7.14) : remplacements ligne
par ligne, chacun vérifié (le texte attendu doit être sur la ligne), puis ajout de __CVchap."""
P = '/home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-3/index.html'
L = open(P, encoding='utf-8').read().split('\n')
CH = '__CVchap(ctx.canvas)'
E = [
  # RLC (drawSim) : régime libre, échelon, forcé ; enveloppe en gris
  (62916, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";   // courbe principale : encre du chapitre"),
  (62930, "__CVA('accent2',0.4)", "__hexAlpha(getCanvasColors().muted, 0.75)"),
  (63018, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  (63054, "ctx.strokeStyle = __CV().accent2;", "ctx.strokeStyle = " + CH + ";"),
  # Optique : la lentille
  (63167, "octx.strokeStyle = __CV().accent2;", "octx.strokeStyle = __CVchap(octx.canvas);"),
  # Oscillateur
  (64060, "oscCtx.strokeStyle = __CV().accent;", "oscCtx.strokeStyle = __CVchap(oscCtx.canvas);"),
  (64075, "__CVA('accent2',0.4)", "__hexAlpha(getCanvasColors().muted, 0.75)"),
  (64131, "oscCtx.strokeStyle = __CV().accent2;", "oscCtx.strokeStyle = __CVchap(oscCtx.canvas);"),
  # Séries : sommes partielles
  (64442, "c.strokeStyle = __CV().accent;", "c.strokeStyle = __CVchap(c.canvas);"),
  (64452, "c.fillStyle = __CV().accent;", "c.fillStyle = __CVchap(c.canvas);"),
  # Coniques, courbes paramétrées
  (64518, "ctx.strokeStyle = col.accent;", "ctx.strokeStyle = " + CH + ";"),
  (64576, "ctx.strokeStyle=col.accent;", "ctx.strokeStyle=" + CH + ";"),
  (64581, "ctx.fillStyle=col.accent;", "ctx.fillStyle=" + CH + ";"),
  # Applications linéaires : image du carré unité
  (66536, "c.fillStyle = __CVA('accent',0.15);", "c.fillStyle = __hexAlpha(__CVchap(c.canvas), 0.15);"),
  (66546, "c.strokeStyle = __CV().accent;", "c.strokeStyle = __CVchap(c.canvas);"),
  (66633, "→ image (rouge)", "→ image (trait plein)"),
  # SLCI : réponses temporelles et gains
  (69500, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  (69634, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  (69713, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  (69801, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  # Filtres (physique) : gain à l'encre du chapitre, phase en rouge (sinon deux bleus)
  (70064, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  (70074, "ctx.strokeStyle = __CV().accent2;", "ctx.strokeStyle = __CV().accent;"),
  # Hacheurs : u(t) et sa moyenne
  (70283, "ctx.strokeStyle = __CV().accent2;", "ctx.strokeStyle = " + CH + ";"),
  (70330, "__CVA('accent2',0.5)", "__hexAlpha(" + CH + ", 0.5)"),
  (70337, "ctx.fillStyle = __CV().accent2;", "ctx.fillStyle = " + CH + ";"),
  (70395, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  # MCC
  (70547, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  (70653, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  # Thermo (transformations)
  (70860, "__CVA('accent',0.13)", "__hexAlpha(" + CH + ", 0.13)"),
  (70870, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  # Cinématique : trajectoire
  (71239, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
  # Statique : l'échelle
  (71755, "ctx.strokeStyle=C.accent2;", "ctx.strokeStyle=" + CH + ";"),
  # 2e ordre : réponse selon le régime (mêmes couleurs que le badge : matière / ambre / neutre)
  (71905, "d.regime==='pseudo'?C.accent : (d.regime==='critique'?C.amber:C.accent2)", "d.regime==='pseudo'?" + CH + " : (d.regime==='critique'?C.amber:C.ink)"),
  # Pendule : tige à l'encre, balourd et portrait de phase à l'encre du chapitre
  (72032, "ctx.strokeStyle=C.accent2;", "ctx.strokeStyle=C.ink;"),
  (72034, "ctx.fillStyle=C.accent;", "ctx.fillStyle=" + CH + ";"),
  (72037, "withA(C.accent,0.6)", "withA(" + CH + ",0.6)"),
  (72069, "ctx.strokeStyle=C.accent;", "ctx.strokeStyle=" + CH + ";"),
  (72073, "ctx.fillStyle=C.accent;", "ctx.fillStyle=" + CH + ";"),
  # 1er ordre
  (72197, "ctx.strokeStyle=C.accent;", "ctx.strokeStyle=" + CH + ";"),
  (72205, "ctx.fillStyle=C.accent;", "ctx.fillStyle=" + CH + ";"),
  # Ondes : la corde à l'encre du chapitre, repère λ en rouge, enveloppe en gris
  (72272, "ctx.strokeStyle=C.accent;", "ctx.strokeStyle=" + CH + ";"),
  (72277, "withA(C.accent2,0.9)", "withA(C.accent,0.9)"),
  (72282, "ctx.fillStyle=C.accent2;", "ctx.fillStyle=C.accent;"),
  (72292, "withA(C.accent2,0.45)", "withA(C.muted,0.8)"),
  (72297, "ctx.strokeStyle=C.accent;", "ctx.strokeStyle=" + CH + ";"),
  # Kepler : trace et corps à l'encre du chapitre, rayon focal en gris
  (72413, "withA(C.accent,0.55)", "withA(" + CH + ",0.55)"),
  (72420, "withA(C.accent2,0.7)", "withA(C.muted,0.9)"),
  (72430, "ctx.fillStyle=C.accent;", "ctx.fillStyle=" + CH + ";"),
  # Électrostatique : lignes de champ (le test sur l'ancienne encre sombre ne marchait plus)
  (72624, "ctx.strokeStyle=`rgba(${C.ink===('#e6e3d8')?'210,210,200':'70,80,95'},0.8)`;", "ctx.strokeStyle=__hexAlpha(C.muted, 0.85);"),
  # Suites : la fonction f
  (73028, "ctx.strokeStyle=C.accent2;", "ctx.strokeStyle=" + CH + ";"),
  (73030, "ctx.fillStyle=C.accent2;", "ctx.fillStyle=" + CH + ";"),
  # Intégrales : la fonction
  (73293, "ctx.strokeStyle = __CV().accent;", "ctx.strokeStyle = " + CH + ";"),
]
for n, old, new in E:
    l = L[n - 1]
    assert l.count(old) == 1, (n, old, l)
    L[n - 1] = l.replace(old, new)
s = '\n'.join(L)
old = """/* Invalidation du cache au changement de thème (attribut data-theme sur <html>) */
new MutationObserver(() => { __CVcache = null; })"""
new = """/* Encre vive du chapitre d'une toile (--chap-vif, posée par data-mat sur .chapter) : couleur de
   la courbe principale des simulateurs (SPEC §3.7). Lue par getComputedStyle(canvas), mise en
   cache par toile (cache vidé au changement de thème) ; repli : accent. */
let __CVchapCache = new WeakMap();
function __CVchap(cv){
  if(!cv) return __CV().accent;
  let c = __CVchapCache.get(cv);
  if(!c){
    c = String(getComputedStyle(cv).getPropertyValue('--chap-vif') || '').trim();
    if(!/^#[0-9a-f]{3,8}$/i.test(c) || !cv.closest('[data-mat]')) return __CV().accent;   // pas encore de matière : pas de cache
    __CVchapCache.set(cv, c);
  }
  return c;
}
/* Invalidation du cache au changement de thème (attribut data-theme sur <html>) */
new MutationObserver(() => { __CVcache = null; __CVchapCache = new WeakMap(); })"""
assert s.count(old) == 1
s = s.replace(old, new)
open(P, 'w', encoding='utf-8').write(s)
print(len(E), 'remplacements')
