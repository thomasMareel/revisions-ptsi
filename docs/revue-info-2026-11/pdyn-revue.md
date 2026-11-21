# `progdyn` (prefix `pdyn`) — Dictionnaires et programmation dynamique — compte rendu (2026-11-21)

Nouveau chapitre de 2ᵉ année, partie 3.2 du programme d'informatique commune (S3). Rédaction originale : exemples, données et exercices inventés.

## Fichiers produits (dans `INFO/`)
- `pdyn-cours.src.html` (≈ 140 000 car., dont ≈ 30 000 de code surligné et ≈ 51 000 de SVG) : bloc « AU PROGRAMME · INFORMATIQUE » + 10 sections + « Pour aller plus loin ».
- `pdyn-meth.src.html` : 9 méthodes (dictionnaire, table de hachage à la main, reconnaître un problème de PD, récurrence, mémoïsation, bas en haut, reconstruction, coûts temps/mémoire, déroulés PLSC/Levenshtein/Floyd), 4 pièges.
- `pdyn-exos.src.html` : 9 exercices + 1 « Concours PT » (correcteur orthographique : lexique en dictionnaire, distance récursive, mémoïsation, deux lignes, suggestion avec filtrage par longueur, ordres de grandeur).
- `pdyn-cartes.js` : 25 cartes (code entre accents graves, formules en `\\( … \\)`, 7 en `cat:'form'`).
- Sources et tests : `INFO/tests/pdyn/` — `code_pdyn.py` (49 blocs, tout le code affiché), `test_pdyn.py` (44 tests : références par force brute, Dijkstra, tirages aléatoires ; consoles vérifiées par doctest), `figs_pdyn.py` (9 figures calculées), `build_pdyn.py` (tests → figures → tableaux calculés → gabarits `*.tpl.html`). Relancer : `python3 build_pdyn.py`.

## Contenu du cours
§1 dictionnaires (syntaxe, parcours, regroupement, copie superficielle et alias, erreur de modification pendant le parcours, liste ou dictionnaire) ; §2 hachage (table à alvéoles et chaînage, programmée et déroulée sur 6 clés, collisions, facteur de charge, agrandissement, pire cas, bonne fonction de hachage, clés hachables et pourquoi une clé mutable serait perdue — démontré avec la table jouet —, 1 == 1.0, flottants) ; §3 chevauchement (chemins dans une grille, arbre des appels, tableau des appels naïfs/mémoïsés, mémoïsation par dictionnaire à clés tuples, bas en haut) ; §4 sous-structure optimale (récolte maximale dans une grille, preuve, reconstruction, échec du glouton, tableau glouton / PD, contre-exemple du plus long chemin élémentaire) ; §5 mémoïsation ou bas en haut, profondeur de récursion (RecursionError), enjeux de mémoire, réduction à une ligne, méthode en 5 étapes ; §6 partition équilibrée (sommes atteignables, `and` paresseux, reconstruction, échec du glouton, pseudo-polynomial) ; §7 tâches pondérées (preuve de la récurrence, déroulé, reconstruction, deux gloutons en échec, O(n²) puis O(n log n)) ; §8 PLSC ; §9 Levenshtein (table, opérations, mémoïsation, deux lignes, lien avec la PLSC) ; §10 Floyd-Warshall (mise à jour sur place justifiée, déroulé par k, matrice des successeurs, chemins). Lien avec les gloutons de 1ʳᵉ année : renvoi au chapitre `pyglouton` sans le refaire (le rendu de monnaie avec reconstruction est l'exercice 4).

## Couverture du programme 3.2
Avant : rien sur le site (dictionnaires seulement en boîte noire en 1ʳᵉ année). Après : toutes les notions (dictionnaires, hachage et limites des clés, syntaxe et parcours, sous-structure optimale, chevauchement, bas en haut / mémoïsation, mémoire, reconstruction, les cinq exemples cités, rapport avec les gloutons).

## Contrôles
`verif_src.py` sans erreur sur les trois panneaux ; aperçu 390 et 1440 px : `merr`, `brut`, `larges` vides, aucune erreur JS (une formule en ligne trop large de l'exercice 7 passée en bloc) ; figures capturées dans le site en clair et en sombre ; cartes : `node -e …` → 25, formules des cartes rendues sans erreur MathJax.

## Choix et doutes
- Fonctions hors annexe documentées sur place : `ord`, `max`, `min`, `tuple` ; `None` renvoyé par `chercher` (« rien »).
- Ordres de grandeur mesurés sur la machine : Levenshtein ≈ 5,7 × 10⁶ cases/s, Floyd-Warshall ≈ 3 × 10⁷ tours/s (d'où « de l'ordre d'une heure » pour 10¹⁰ cases, « de l'ordre de la minute » pour n = 1 000).
- Le fonctionnement réel des `dict` de Python (adressage ouvert, agrandissement) n'est que mentionné, en hors-programme.
- Taille du panneau Cours (140 Ko) supérieure aux autres chapitres d'informatique (code et 9 figures) ; à alléger si l'intégration le demande.
