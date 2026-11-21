# Revue — `glou` (chapitre `pyglouton`, « Algorithmes gloutons », informatique, 1ʳᵉ année)

Nouveau chapitre. Fichiers : `glou-cours.src.html`, `glou-meth.src.html`, `glou-exos.src.html`, `glou-cartes.js` (22 cartes).

**Fabrication** : comme pour `dich`, les panneaux sont produits par `tests/dichglou/build.py html glou` à partir des
gabarits `tests/dichglou/glou-{cours,meth,exos}.tpl.html`, du code exécuté `tests/dichglou/glou_code.py` (33 valeurs
de démonstration vérifiées) et des figures calculées `tests/dichglou/glou_figs.py`. Chaque glouton est comparé à une
recherche exhaustive sur des milliers d'instances tirées au hasard (sélection d'activités, allocation et profondeur,
clé USB, points d'eau, relais, ordonnancement, sous-ensembles pondérés) ; le rendu de monnaie est comparé à la
programmation dynamique ; les contre-exemples cités sont tous vérifiés par programme. Ne pas retoucher les
`.src.html` à la main : éditer gabarit ou code, puis `python3 -I build.py html glou`.

## Couverture du programme (avant → après)
Avant : thème absent du site (audit 2026-11 §5 : « S1 : algorithmes gloutons ❌ »). Après :
- principe glouton, problème d'optimisation, solution réalisable / optimale, schéma « trier puis parcourir » (§1,
  exemple de la clé USB avec preuve) ;
- rendu de monnaie : glouton en liste et par division euclidienne, coût, démonstration pour le système (5, 2, 1),
  piège des flottants (0,03 − 0,02 < 0,01) (§2) ;
- systèmes non canoniques : (4, 3, 1), système britannique d'avant 1971 (48 pence), échec sans pièce de 1 (§3) ;
- sélection d'activités : critères faux (début au plus tôt, plus courte d'abord, moins de conflits) avec figure,
  fin au plus tôt, déroulé sur neuf demandes, coût (§4) ;
- preuves : « toujours en avance », argument d'échange, propriété du choix glouton, sous-structure optimale (§5) ;
- allocation de salles : glouton par début croissant, égalité avec la profondeur (démonstration), balayage des
  événements, contre-exemples d'ordre (non trié, trié par fin) (§6) ;
- limites et lien avec la programmation dynamique (S3) : sac à dos, tâches pondérées, récurrence du rendu optimal,
  `nb_min_pieces` de bas en haut, recherche automatique du plus petit contre-exemple (§7) ;
- « Pour aller plus loin » : borne de Kozen et Zaks, Dijkstra (renvoi au chapitre *Graphes*), Huffman, Kruskal,
  Prim, matroïdes, tas pour l'allocation.

## Méthodes (8)
Modéliser un problème d'optimisation ; écrire un glouton (trier puis parcourir) ; rendre la monnaie ; chercher un
contre-exemple ; prouver l'optimalité (en avance / échange) ; sélectionner des activités ; allouer des salles et
vérifier par la profondeur ; évaluer le coût.

## Exercices (10, dont 1 « Concours PT »)
01 ★ rendu en euros (billets compris), `nb_pieces`, coût selon la somme ; 02 ★ systèmes (7, 5, 1), (5, 3), (c, 1) et
puissances de 2 (preuves) ; 03 ★★ salle de réunion, contre-exemples, variante « début au plus tard » ;
04 ★★ allocation des colles, profondeur, ordre de traitement ; 05 ★★ minimiser la somme des instants de fin
(échange) ; 06 ★★ points d'eau sur un sentier (preuve « en avance ») ; 07 ★★ caisse à stock limité (échec du glouton,
recherche exhaustive à deux valeurs) ; 08 ★★★ relais radio dans un tunnel (échange) ; 09 ★★★ sac à dos entier et
fractionnaire ; **Concours PT** : imprimantes 3D d'un FabLab (validité d'un planning en O(n log n), sélection,
preuve guidée, nombre d'imprimantes = profondeur, demandes pondérées : contre-exemples et recherche récursive
exponentielle, ouverture vers la programmation dynamique).

## Choix
- `sorted` (hors annexe) est documenté au §1 du cours et dans l'énoncé du sujet concours ; l'ordre décroissant est
  obtenu en parcourant la liste triée depuis la fin (pas de `reverse=True` ni de `key=`) ; les activités sont triées
  par fin en triant les couples retournés `(f, d)`.
- Intervalles semi-ouverts [d, f[ partout (deux activités qui se suivent sont compatibles ; balayage : fins avant
  débuts à égalité).
- La programmation dynamique n'est montrée qu'en aperçu (récurrence et code de bas en haut du rendu de monnaie),
  signalée comme vue en 2ᵉ année ; mémoïsation et reconstruction renvoyées au chapitre *Dictionnaires et
  programmation dynamique*.

## Contrôles
- `verif_src.py` : aucune ERREUR ; une seule « attention » sur le cours (« pas de bloc AU PROGRAMME · PT »), artefact
  de l'outil qui cherche `AU PROGRAMME · PT` alors que les consignes demandent « AU PROGRAMME · INFORMATIQUE ».
- `apercu_src.py` à 390 et 1440 px pour les trois panneaux : `merr`, `brut`, `larges` vides, aucune erreur JS ; les
  trois figures (critères faux, neuf activités, planning des salles) vérifiées sur capture et tenant dans la colonne
  à 390 px.
- Cartes : `node -e … glouCards.length` → 22, questions distinctes, aucun HTML.

## Doutes
- « Le système de l'euro est canonique » est admis (vérifié par programme jusqu'à 10 €, ce qui suffit d'après la
  borne de Kozen et Zaks, citée hors programme ; la borne elle-même n'a été que testée sur 300 systèmes aléatoires).
- Le contre-exemple au critère « moins de conflits » (neuf activités) n'est que mentionné ; il est vérifié pour trois
  règles de départage des égalités. Instance : [1, 5[, [12, 16[, [3, 7[, [6, 9[, [11, 14[, [9, 12[, [4, 7[, [7, 10[,
  [11, 13[ (optimum 4, glouton 3).
- Le mot « sous-listes » pour les sous-ensembles suit le vocabulaire du programme (énumération des sous-listes).
