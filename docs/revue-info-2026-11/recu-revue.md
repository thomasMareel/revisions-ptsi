# Revue du chapitre `pyrec` (prefix `recu`) — « Récursivité »

Chapitre existant (≈ 3 300 car. de cours, 3 méthodes, 3 exercices), réécrit entièrement ; cartes marquées et complétées.

## Fichiers produits (dans `INFO/`)
- `recu-cours.src.html` (≈ 69 000 car. : bloc « AU PROGRAMME · INFORMATIQUE », 9 sections §1–§9, « POUR ALLER PLUS LOIN », 8 exemples traités, 6 figures SVG calculées, 1 tableau d'appels calculé).
- `recu-meth.src.html` (8 méthodes, 3 pièges), `recu-exos.src.html` (9 exercices ★ à ★★★ + 1 « Concours PT » en 3 parties, 8 questions).
- `recu-cartes-corr.json` (4 marquages), `recu-cartes-ajout.js` (12 cartes nouvelles).
- Sources et tests : `INFO/tests/recu/` — `recu_code.py` (code + démonstrations vérifiées + tests), `recu_figs.py` (figures tracées avec les points et segments renvoyés par les fonctions du chapitre), gabarits `recu-{cours,meth,exos}.tpl.html`. Construction : `cd INFO/tests/tri && MPLBACKEND=Agg python3 -I build.py html recu` (même outil que le chapitre `tri`).

## Couverture du programme (avant → après)
| Notion (programme 2021, S1 « Fonctions récursives ») | Avant | Après |
|---|---|---|
| Cas de base, appel récursif | factorielle, somme | §1 : factorielle, palindrome sur une chaîne (indices), fonction d'appel |
| Dépassement de la taille de la pile | une phrase | §2 : cadres, pile, figure des 8 états de `factorielle(3)`, `RecursionError` mesurée (900 : correct ; 1000 et 2000 : erreur), cas de base jamais atteint, espace \(O(p)\) |
| Terminaison, correction, coût (S2) | variant cité | §3 : variant, récurrence forte, relation de coût ; Fibonacci : \(2F_{n+1} - 1\) appels, arbre de `fib(5)`, version itérative |
| Version récursive des algorithmes dichotomiques | absent | §4 : `dicho_rec(x, t, g, d)` (notations du chapitre `pydicho`), tableau des appels, coût \(O(\log n)\), piège des tranches ; exponentiation rapide récursive, piège du double appel (2047 appels au lieu de 11 pour n = 1000) |
| Figures alphanumériques par `print` | absent | §5 : triangles (print avant/après l'appel), règle graduée (\(2^n - 1\) lignes), triangle de Sierpiński en caractères |
| Dessins de fractales | absent | §6 : courbe de von Koch (points, \(4^n\) segments, longueur \((4/3)^n\), tracé `matplotlib` documenté), arbre fractal (\(2^n - 1\) segments) |
| Énumération des sous-listes | absent | §7 : schéma « avec / sans », arbre de décision, \(2^n\) résultats, coût \(O(n\,2^n)\), somme atteinte par exploration |
| Énumération des permutations | absent | §8 : schéma « choisir le premier », arbre des choix, \(n!\) résultats, anagrammes |
| Récursif ou itératif | une phrase | §9 : récursion terminale → boucle (`dicho_iter`), tableau de choix |

## Erreurs ou faiblesses corrigées
- Aucune carte fausse. L'ancien cours se cantonnait aux fonctions mathématiques (factorielle, somme, puissance, Fibonacci), ce que le programme demande précisément d'éviter ; aucune des activités citées par le programme (dichotomie récursive, figures, fractales, sous-listes, permutations, pile) n'y figurait.
- Ancienne carte 7 (« récursivité et itération sont équivalentes ») : juste, précisée dans le cours (pile gérée à la main si besoin).

## Choix
- Exemples hors mathématiques en priorité (chaînes, figures, fractales, énumérations, tournée de drone) ; factorielle et Fibonacci gardés car les cartes existantes s'y réfèrent et parce que Fibonacci illustre le coût exponentiel.
- Renvois sans redite : variant, invariant, relations de coût et espace des appels récursifs → *Spécification, correction et complexité* (même liste de relations \(C(n)\)) ; dichotomie et exponentiation itératives → *Recherche séquentielle, dictionnaires et dichotomie* ; tris récursifs → *Algorithmes de tri* ; mémoïsation → 2ᵉ année.
- `print` utilisé sans paramètre facultatif (lignes construites par `"*" * n` et concaténation) ; seuls les éléments de l'annexe dans le code (compréhensions simples, tranches, `append`) ; `math.sqrt`, `math.cos`, `math.sin`, `math.pi` et `matplotlib.pyplot` (`plot`, `axis`, `show`) documentés là où ils servent.
- Tests : dichotomie et première occurrence comparées à une recherche séquentielle (≈ 500 listes), sous-listes / parties à k éléments / permutations comparées à `itertools`, Hanoï simulé (aucun disque posé sur un plus petit), affichages comparés caractère par caractère, nombres d'appels vérifiés contre les formules, tournée optimale comparée à l'énumération brute (60 cas aléatoires) ; le tracé `matplotlib` est exécuté (backend sans fenêtre).

## Cartes
- Corrections (`recu-cartes-corr.json`) : **réponses seules**, marquage du code (cartes 3, 6, 10, 11) ; questions intactes. Les 8 autres cartes ne contiennent pas de code : inchangées.
- Ajouts (12, à la fin) : `RecursionError`, mémoire de la pile, dichotomie récursive (paramètres, coût, piège des tranches), exponentiation rapide, coût de Fibonacci naïf, place du `print`, sous-listes, permutations, courbe de von Koch, récursion terminale, Hanoï.
- Contrôles : `corriger_cartes.py recu … --essai` → 4 réponses ; `ajouter_cartes.py recu … --essai` → 12 → 24 cartes.

## Contrôles passés
- `verif_src.py` sur les trois fichiers : aucune erreur (seul « pas de bloc AU PROGRAMME · PT », faux positif connu).
- `apercu_src.py` à 390 et 1440 px (cours, méthodes, exercices) : `merr`, `brut`, `larges` vides, aucune erreur JS ; figures regardées en capture.

## Doutes
- Le programme parle d'« énumération des sous-listes » sans définir le terme ; le cours l'entend au sens de sous-suites (éléments non forcément voisins, \(2^n\) résultats) et le précise, les tranches étant un cas particulier.
- Les seuils de `RecursionError` cités (factorielle(900) passe, factorielle(1000) échoue) sont ceux de la limite par défaut de Python 3.13 ; le cours dit « environ mille ».
- Le nombre d'appels de l'exemple « 10 lieux au hasard » du concours (116 843 contre 986 410) dépend du tirage ; il est donné comme une mesure.
