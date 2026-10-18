#!/usr/bin/env python3
"""Ligne A, coquille : remplace le HTML de l'en-tête, de la barre téléphone, du menu ⋯
et du tiroir ; pose class="desk" sur <body> ; enveloppe la colonne de lecture
(sommaire de matière + <main> ×2 + pager + pied) dans <div id="app-main">.
Usage : python3 etape_html.py index.html coquille.html"""
import sys
chemin, frag = sys.argv[1:3]
src = open(chemin, encoding='utf-8').read()
neuf = open(frag, encoding='utf-8').read().strip('\n')

def unique(s, motif):
    n = s.count(motif)
    assert n == 1, (motif[:60], n)
    return s.index(motif)

# 1) bloc skip-link … fin du tiroir
i = unique(src, '<a href="#" class="skip-link" id="skip-link">Aller au contenu</a>')
fin_tiroir = '  <!-- Liste des chapitres (remplie dynamiquement) -->\n  <div id="mob-chap-list"></div>\n</div>'
j = unique(src, fin_tiroir) + len(fin_tiroir)
src = src[:i] + neuf + src[j:]

# 2) <body> → <body class="desk">
k = src.index('</head>\n<body>\n')   # le 1er = la page (le 2e est dans le gabarit d'impression)
assert k < src.index('<header'), 'mauvais <body>'
src = src[:k] + '</head>\n<body class="desk">\n' + src[k + len('</head>\n<body>\n'):]

# 3) colonne de lecture : <div id="app-main"> avant le 1er <main>, fermée après </footer>
m = unique(src, '\n<main>\n')
src = src[:m] + ('\n<!-- Colonne de lecture (décalée par la barre latérale à partir de 1200 px) -->\n'
                 '<div id="app-main">\n'
                 '<!-- Sommaire de la matière (#sommaire/<matière>) : rempli à l\'ouverture -->\n'
                 '<section id="sommaire-matiere" class="sommaire" aria-label="Sommaire de la matière" hidden></section>\n'
                 '<main>\n') + src[m + len('\n<main>\n'):]
f_old = '<footer>\n  PTSI · Mes cours de physique · Programme officiel\n</footer>\n'
f = unique(src, f_old)
src = src[:f] + ('<footer class="pied">\n  <span class="brand-mark" aria-hidden="true"></span>'
                 '<span>Mes cours de <em>prépa</em> · PTSI → PT · programme officiel · fonctionne hors ligne</span>\n'
                 '</footer>\n</div><!-- fin #app-main -->\n') + src[f + len(f_old):]

# 4) retour en haut : icône du jeu maison
b_old = '<button id="back-to-top" title="Retour en haut" aria-label="Retour en haut">↑</button>'
unique(src, b_old)
src = src.replace(b_old, '<button id="back-to-top" class="btn btn-icon" type="button" title="Retour en haut" aria-label="Retour en haut">'
                  '<svg class="ic" aria-hidden="true"><use href="#i-chev-right"></use></svg></button>')
open(chemin, 'w', encoding='utf-8').write(src)
print('HTML de la coquille remplacé')
