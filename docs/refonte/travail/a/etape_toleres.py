#!/usr/bin/env python3
"""Suite visuel : retire de TOLERES les constats de la coquille qui ont disparu (en-tête,
navigation, barre du téléphone, menu Plus) ; les sélecteurs d'autres régions restent.
Usage : python3 etape_toleres.py tests/suites/visuel.js"""
import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

rep("  ['contraste', 'chapitres', 'sombre', 'ordi', { '#rev-badge': 2.99 }],\n", "")
rep("  ['contraste', 'chapitres', 'sombre', 'tel', { '#rev-badge-mob': 2.99 }],\n", "")
rep("  ['contraste', 'tiroir', '*', '*', { 'button.mob-mat-btn': 3.18 }],\n", "")
rep("  ['contraste', 'tiroir', 'clair', '*', { '#mob-drawer-close': 4.09 }],\n", "")
rep("  ['taille', 'chapitres', '*', 'ordi', { '#rev-badge': 9.92, '#search-btn kbd': 9.6, '#theme-label': 11.2, 'div.eyebrow': 11.2, 'span.ctb-sub': 10.88, 'span.hdr-btn-label': 11.2 }],\n",
    "  ['taille', 'chapitres', '*', 'ordi', { 'span.ctb-sub': 10.88 }],\n")
rep("  ['taille', 'chapitres', '*', 'tel', { '#rev-badge-mob': 9.92, 'button.tab': 11.52 }],\n",
    "  ['taille', 'chapitres', '*', 'tel', { 'button.tab': 11.52 }],\n")
rep("  ['taille', 'menu-plus', '*', 'ordi', { '#backup-btn': 11.52, '#flag-btn': 11.52, '#formula-btn': 11.52, '#print-btn': 11.52, '#today-btn': 11.52, 'button.hdr-more-item': 11.52, 'span.read-size-val': 11.2 }],\n", "")
rep("  ['taille', 'tiroir', '*', '*', { 'button.mob-mat-btn': 10.88, 'button.mob-subdomain-label.mob-sub-toggle': 10.24, 'span.mob-filter-tag.mt-anglais': 10.24, 'span.mob-filter-tag.mt-si': 10.24, 'span.mob-subdomain-label.mob-drawer-section': 10.24, 'span.sub-chev': 9.6, 'span.sub-count': 10.56 }],\n", "")
rep("{ '#mob-header': 415, 'div.course-section li mjx-container': 414, 'page (scrollWidth)': 415 }",
    "{ 'div.course-section li mjx-container': 414, 'page (scrollWidth)': 415 }")
rep("  ['cible44', 'tiroir', '*', 'tel', { '#mob-drawer-close': 27.4, '#mob-filter': 40, 'button.mob-subdomain-label.mob-sub-toggle': 40 }],\n", "")
open(p, 'w', encoding='utf-8').write(s)
print('TOLERES : constats de la coquille retirés')
