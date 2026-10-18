#!/usr/bin/env python3
"""Retire de TOLERES (tests/suites/visuel.js) les anomalies du contenu corrigées par la ligne B."""
P = '/home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-3/tests/suites/visuel.js'
s = open(P, encoding='utf-8').read()
lignes = [
  "  ['contraste', 'rlc-cours maxwell-cours', 'sombre', '*', { 'div.notice': 1.99, 'div.notice em': 1.99, 'div.notice mjx-container': 1.99 }],\n",
  "  ['contraste', 'rlc-simu', 'clair', '*', { 'span.lbl': 3.54 }],\n",
  "  ['taille', 'maxwell-cours', '*', 'tel', { 'text.lab-accent': 11.92, 'text.lab-accent2': 11.92, 'text.lab-it': 11.92, 'text.lab-muted': 10.54 }],\n",
  "  ['taille', 'rlc-cours maxwell-cours', '*', '*', { 'span.label': 11.2 }],\n",
  "  ['taille', 'rlc-cours maxwell-cours slci-cours', '*', '*', { 'div.def-box::before': 9.92, 'div.prop-box::before': 9.92 }],\n",
  "  ['taille', 'rlc-exos', '*', '*', { 'p.exo-part': 11.52, 'span.diff': 11.2 }],\n",
  "  ['taille', 'rlc-meth', '*', '*', { 'div.method-box::before': 9.92, 'span.step': 11.2 }],\n",
  "  ['taille', 'rlc-simu', '*', '*', { 'span.lbl': 11.2 }],\n",
  "  ['debordement', 'rlc-cours', '*', 'tel', { '#mob-header': 415, 'div.course-section li mjx-container': 414, 'page (scrollWidth)': 415 }],\n",
  "  ['cible44', 'rlc-exos', '*', 'tel', { 'button.toggle-sol': 34 }],\n",
  "  ['cible44', 'rlc-simu', '*', 'tel', { '#C': 16, '#L': 16, '#R': 16 }],\n",
]
for l in lignes:
    assert s.count(l) == 1, l
    s = s.replace(l, '')
# La ligne d'en-tête « — Débordement horizontal » n'a plus d'entrée : on la retire aussi
s = s.replace("  // — Débordement horizontal (bord droit, px) —\n  // — Cibles tactiles", "  // — Cibles tactiles")
open(P, 'w', encoding='utf-8').write(s)
print(len(lignes), 'entrées retirées')
