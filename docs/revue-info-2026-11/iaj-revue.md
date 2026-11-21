# `iajeux` (prefix `iaj`) — Algorithmes pour l'IA et les jeux — compte rendu (2026-11-21)

Nouveau chapitre de 2ᵉ année, partie 3.3 du programme d'informatique commune (S3). Rédaction originale : jeux de données, arènes et exercices inventés.

## Fichiers produits (dans `INFO/`)
- `iaj-cours.src.html` (≈ 102 500 car.) : bloc « AU PROGRAMME · INFORMATIQUE » + 10 sections + « Pour aller plus loin ».
- `iaj-meth.src.html` : 9 méthodes (k-NN à la main, k-NN en Python et coût, matrice de confusion, k-moyennes et minimum local, modéliser un jeu, attracteur, prouver une stratégie gagnante, minimax à la main, concevoir une heuristique), 3 pièges.
- `iaj-exos.src.html` : 9 exercices + 1 « Concours PT » (le chat et la souris sur un plateau à trou : arène à 84 états construite avec un dictionnaire, attracteurs, tableau des issues, stratégie, heuristique par parcours en largeur, minimax, comparaison des coûts).
- `iaj-cartes.js` : 25 cartes (code entre accents graves, formules en `\\( … \\)`, 7 en `cat:'form'`).
- Sources et tests : `INFO/tests/iaj/` — `code_iaj.py` (38 blocs), `test_iaj.py` (38 tests : k-NN et Lloyd comparés à des références, attracteurs comparés à un point fixe et à une recherche exhaustive des victoires forcées — le rang est vérifié comme nombre minimal de coups —, minimax sur arbres aléatoires, morpion résolu), `figs_iaj.py` (8 figures), `build_iaj.py`. Relancer : `python3 build_iaj.py`.

## Contenu du cours
§1 supervisé / non supervisé, données en tuples, distance euclidienne ; §2 k plus proches voisins (sélection par tri par sélection sur les couples (distance, indice), vote par dictionnaire, règle d'égalité, exemple où k = 1 et k = 5 divergent à cause d'un point atypique, coût, choix de k) ; §3 matrice de confusion (même convention que le chapitre de SI `ia` : réel en ligne, prédit en colonne), exactitude, matrices pour k = 1 et k = 5, exactitude selon k (13 à 17 sur 18) ; §4 k-moyennes (inertie, algorithme, groupe vide, déroulé 1D) ; §5 minima locaux observés (1D : 71 contre 12,5 ; 2D : 1 138 départs sur 1 330 aboutissent au minimum global, figure des deux partitions), relances aléatoires, coude ; §6 arènes bipartites, trois types de finals, partie infinie = nul, allumettes avec dictionnaire à clés tuples ; §7 stratégie sans mémoire, stratégie et position gagnantes, preuve pour les allumettes ; §8 attracteurs (définition, rang, théorème démontré dans les deux sens, code, déroulé sur une arène à 14 états avec les trois issues, coût) ; §9 heuristique, minimax (code générique, arbre de profondeur 3, coût, effet d'horizon) ; §10 morpion (heuristique des lignes ouvertes, effet d'horizon montré à la profondeur 1, résolution exacte mémoïsée : 5 478 états contre 549 946 appels, valeur nulle). Alpha-bêta, preuve de convergence des k-moyennes, k-means++ : en fin de cours, hors programme.

## Cohérence avec le chapitre de SI `ia`
k-NN : mêmes définitions, même convention de matrice de confusion, même vocabulaire (exactitude ; précision et rappel renvoyés au §4 de `ia`), renvois à `ia` §3 (mise à l'échelle, validation) et §7 (k-NN avec bibliothèques). Ici, tout est programmé avec les seuls éléments de l'annexe (pas de numpy).

## Couverture du programme 3.3
Avant : seulement le k-NN du chapitre de SI. Après : toutes les notions (k-NN, matrice de confusion, lien supervisé / non supervisé, k-moyennes et minima locaux observés, jeux d'accessibilité sur graphe biparti, stratégies sans mémoire, positions gagnantes, attracteurs, construction de stratégies, heuristique, minimax ; alpha-bêta exclu).

## Contrôles
`verif_src.py` sans erreur ; aperçu 390 et 1440 px des trois panneaux : `merr`, `brut`, `larges` vides, aucune erreur JS ; figures capturées dans le site en clair et en sombre ; cartes : 25, formules rendues sans erreur MathJax.

## Choix et doutes
- Conventions fixées (à garder si un énoncé les rappelle) : égalité de vote → classe du plus proche voisin ; égalité de distance → plus petit indice ; groupe vide → centre inchangé ; états finals = états sans successeur ; partie infinie = match nul ; finals à ±100 dans minimax.
- Fonctions de modules documentées : `sqrt`, `random.sample` ; `tuple(L)` documenté.
- Le jeu « chat et souris avec un trou » est un classique (règles et plateau ici originaux).
- L'effet d'horizon du morpion repose sur l'ordre d'examen des coups (trois coups ex æquo pour l'heuristique, le centre examiné le premier) : c'est dit explicitement dans le cours et la légende.
