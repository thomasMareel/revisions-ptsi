# `graphes` (prefix `gra`) — « Graphes : parcours et plus courts chemins » — compte rendu

Nouveau chapitre, 1ʳᵉ année, programme d'informatique commune 2021, partie 2.3 (2ᵉ semestre).
Rédaction entièrement originale : graphes, poids, grilles, réseau du sujet concours et liste de mots inventés.

## Fichiers produits (dans `INFO/`)
- `gra-cours.src.html` : bloc « AU PROGRAMME · INFORMATIQUE » + 10 sections + « Pour aller plus loin » ; 11 exemples
  traités, 8 figures SVG calculées, 3 déroulés pas à pas (tableaux d'états produits par le code lui-même) ; ≈ 94 000
  caractères de HTML, dont ≈ 41 000 de texte (la figure A* sur grille pèse 18 Ko).
- `gra-meth.src.html` : 9 méthodes (étapes, exemple éclair) + 2 pièges.
- `gra-exos.src.html` : 10 exercices (3 ★, 5 ★★, 1 ★★★, 1 « Concours PT » en 4 parties : réseau de vélos, parcours en
  largeur, Dijkstra, A* avec heuristique admissible justifiée).
- `gra-cartes.js` : 25 cartes (`const graCards`), 5 `cat:'form'`.
- Sources et tests (dans `INFO/tests/gra/`) : `code_gra.py` (29 blocs), `test_gra.py` (tests contre des implémentations de
  référence indépendantes — tas de `heapq`, comptage d'arêtes pour les cycles — sur des centaines de graphes aléatoires,
  orientés ou non, pondérés ou non), `figs_gra.py`, gabarits, `build_gra.py` (tests, puis déroulés et panneaux).
  Reconstruction : `python3 INFO/tests/gra/build_gra.py`.

## Contenu du cours
1. Modéliser : \(G = (S, A)\), orienté / non orienté, sommet, arc, arête, boucle, pas de multi-arcs ; figures de \(G_1\)
   (non orienté, degrés) et \(D\) (orienté, boucle, arcs opposés) ; tableau des tailles typiques (métro, routes, web,
   réseau social, protéines) ; nombre maximal de liens.
2. Vocabulaire : \(d(s)\), \(d^+(s)\), \(d^-(s)\), somme des degrés (démonstration), chemin et longueur, cycle,
   connexité, composantes.
3. Représentations : matrice d'adjacence (matrice de \(D\)), degrés par lignes / colonnes, listes d'adjacence (liste et
   dictionnaire), conversions, tableau comparatif des coûts, exemple chiffré du réseau routier.
4. Graphes pondérés : poids, étiquettes, couples (voisin, poids), `float('inf')` documenté, poids d'un chemin, figure de
   \(P\) ; piège du 0 dans une matrice pondérée.
5. Piles et files : LIFO / FIFO (figure), pile = liste, inefficacité de `pop(0)` (mesurée : quadratique), `collections.deque`
   documenté (`append`, `popleft`, `len`).
6. Parcours en largeur avec `deque` : figure des couches et de l'arbre, déroulé complet, propriété des distances (idée de
   preuve), parents et reconstruction d'un chemin, complexité \(O(n + m)\).
7. Parcours en profondeur : version avec pile (déroulé, copies ignorées), version récursive (ordre différent expliqué),
   complexité, limite de récursion.
8. Connexité et cycles : composantes (figure de \(G_3\)), cycle par l'exception du parent (déroulé), au moins \(n - 1\)
   arêtes pour un graphe connexe (démonstration dépliable).
9. Dijkstra : principe, file de priorité naïve, code, déroulé complet (mises à jour à chaque étape), figure avec distances et
   arbre des plus courts chemins, idée de preuve (invariant, rôle des poids positifs), complexité \(O(n^2)\),
   contre-exemple à poids négatif exécuté.
10. A* : heuristique, admissibilité, A* = Dijkstra qui minimise `d[v] + h[v]` et s'arrête à la cible ; figure calculée sur
    une grille (Dijkstra 100 cases fixées, A* 57, même chemin de 16 pas) ; résultat admis sur l'heuristique cohérente.

## Couverture du programme 2.3 (avant → après)
Avant : rien sur le site (❌ dans l'audit du 2026-11-14). Après : toutes les notions et commentaires de la partie 2.3 —
vocabulaire et notations (§1-2), listes / dictionnaire / matrice (§3), pondération (§4), piles, files et `deque` (§5),
parcours (§6-7), cycles et connexité en non orienté (§8), Dijkstra avec file naïve (§9), A* en sensibilisation (§10) —,
chacune reprise par au moins une méthode et un exercice.

## Contrôles faits
- `python3 INFO/tests/gra/test_gra.py` : 29 blocs, 25 tests + vérification des valeurs citées dans les textes
  (déroulés, ordre de visite, distances, échelle de mots, chemin unique du labyrinthe, contre-exemples).
- `verif_src.py` : aucune erreur ; un avertissement (voir doutes).
- `apercu_src.py` à 390 et 1440 px pour les trois panneaux : `merr`, `brut`, `larges` vides, aucune erreur JS. Figures
  capturées une à une (clair / sombre, 390 / 1440 px) et regardées ; flèches = marqueurs `sk-arrow-*`, classes du site.
- Cartes : 25, questions uniques, pas de HTML.

## Doutes et remarques pour l'intégration
- Même avertissement de `verif_src.py` que pour `pyanalyse` (surtitre « AU PROGRAMME · INFORMATIQUE » imposé par les
  consignes).
- Les tailles de graphes réels sont des ordres de grandeur volontairement arrondis (« quelques centaines », « plusieurs
  millions », « des dizaines de milliards ») : à garder ainsi, les chiffres précis varient selon les sources et les années.
- Hors annexe, documentés sur place : `deque`, `float('inf')`, `sqrt` (sujet concours), annotations de type, `while True`
  dans A* (sortie par `return`).
- Le nombre de cases fixées par A* sur la grille dépend du départage des égalités (ici, le premier sommet minimal dans
  l'ordre des numéros, comme dans le code affiché) ; la figure est calculée avec exactement cet algorithme.
- « Un graphe connexe a au moins \(n - 1\) arêtes » (§8) n'est pas cité par le programme : présenté comme outil de
  contrôle, avec démonstration dépliable.
- Les cartes supposent, comme pour `pyanalyse`, le rendu « texte tel quel » des decks d'informatique.
