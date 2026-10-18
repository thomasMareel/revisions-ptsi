#!/usr/bin/env python3
"""Remplace le contenu d'une région du grand <style> (entre l'en-tête de région
et sa balise de fin) par le contenu d'un fichier.
Usage : python3 remplacer_region.py index.html REGION fichier.css"""
import re, sys
chemin, region, fichier = sys.argv[1:4]
src = open(chemin, encoding='utf-8').read()
neuf = open(fichier, encoding='utf-8').read().strip('\n')
debut = '/* ===== RÉGION %s ===== */\n' % region
fin = '/* ===== FIN RÉGION %s ===== */' % region
i = src.index(debut)
# l'en-tête de région = la ligne de balise + le commentaire de description qui suit
j = src.index('*/', i + len(debut)) + 2
k = src.index(fin, j)
src = src[:j] + '\n\n' + neuf + '\n\n' + src[k:]
open(chemin, 'w', encoding='utf-8').write(src)
print('région', region, 'remplacée')
