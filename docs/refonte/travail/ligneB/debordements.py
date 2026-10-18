#!/usr/bin/env python3
"""Vide DEBORDEMENTS_CONNUS (tests/suites/mobile.js) : les 13 panneaux ne débordent plus."""
P = '/home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-3/tests/suites/mobile.js'
s = open(P, encoding='utf-8').read()
a = s.index('/* Panneaux qui débordent à 390 px au commit a04c445')
b = s.index('};', s.index('const DEBORDEMENTS_CONNUS = {')) + 2
nouveau = """/* Panneaux qui débordent à 390 px (mesurés avec cette suite, Chromium 141) : largeur de page
   mesurée (px) et formule en cause. Un panneau connu fait quand même échouer si sa largeur augmente
   de plus de MARGE px (nouvelle formule plus large). Quand un débordement est corrigé, la suite
   affiche un avertissement : retirer alors la ligne correspondante.
   Liste VIDE depuis la refonte du contenu (formules en bloc défilantes, formules en ligne trop
   larges en .mj-large, schémas élargis) : les 13 panneaux du commit a04c445 (rlc-cours 415 px,
   sig-meth, mp-exos, cpx-meth, pol-cours, suit-meth, cd-cours, dl-meth, asy-meth, prim-meth,
   va-cours, ensi-meth, repn-cours) ne débordent plus. Format d'une entrée :
   'rlc-cours': { largeur: 415, formule: '\\\\dot{u}_C(0) = 0 …' }, */
const DEBORDEMENTS_CONNUS = {};"""
s = s[:a] + nouveau + s[b:]
open(P, 'w', encoding='utf-8').write(s)
print('ok')
