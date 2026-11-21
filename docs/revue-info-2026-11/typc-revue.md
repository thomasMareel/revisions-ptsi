# `pytypes` (prefix `typc`) — « Types construits » — compte rendu (chapitre existant, 1ʳᵉ année)

Rédaction originale ; exemples et exercices inventés. Tout le code affiché est exactement le code testé.

## Fichiers produits (dans `INFO/`)
- `typc-cours.src.html` (≈ 68 000 car.) : bloc « AU PROGRAMME · INFORMATIQUE » + 8 sections + « POUR ALLER PLUS LOIN · HORS DE
  L'ANNEXE » ; 8 exemples traités, 4 figures SVG (indices et bornes d'une tranche, alias et copie, copie superficielle d'une liste
  de listes, piège `[[0] * 3] * 3`), 4 tableaux d'états calculés (miroir, affectation simultanée / successive, pile,
  regroupement par dictionnaire), 2 tableaux de synthèse (choix de la structure, coûts).
- `typc-meth.src.html` : 9 méthodes (choisir la structure, indices et tranches, construire une liste, parcourir, copier sans
  alias, tableau 2D, dictionnaire, nouvelle chaîne, coût des opérations) + 2 pièges.
- `typc-exos.src.html` : 10 exercices (3 ★, 5 ★★, 1 ★★★, 1 « Concours PT » en 4 parties, 13 questions).
- `typc-cartes-corr.json` (11 cartes retouchées), `typc-cartes-ajout.js` (12 cartes, 14 → 26).
- Sources et tests : `INFO/tests/typc/` — `code_typc.py` (58 blocs), `test_typc.py` (40 tests, plus les consoles vérifiées par
  doctest), `figs_typc.py`, gabarits, `build_typc.py`, `cartes_typc.py` (marquage par remplacements exacts dans le texte
  d'origine, contrôlé). Reconstruction : `python3 INFO/tests/typc/build_typc.py` puis `python3 INFO/tests/typc/cartes_typc.py`.

## Cours
§1 séquences (indices, tranches et leurs bornes + figure, `+`, `*`, indice positif valide, parcours par élément / par indice ;
la même fonction sur chaîne, tuple, liste) · §2 chaînes (immuables, construire une nouvelle chaîne : `miroir` déroulé,
`remplacer` avant `float`, ordre lexicographique, piège `"10" < "9"`, coût O(n²) des concaténations successives) · §3 tuples
(singleton `(7,)`, dépaquetage, affectation simultanée : Fibonacci contre version successive fausse, enregistrements, comparaison
de tuples) · §4 listes (trois modes de création, `append`, `pop`, pile déroulée, `append` contre `+` : O(n) contre O(n²),
erreurs `t[len(t)] = …` et `t = t.append(…)`) · §5 références, alias, copies (modifier / réaffecter, `copy`, `[:]`, copie
superficielle + figures, exemple de prédiction) · §6 tableaux 2D (compréhension, piège `[[0] * p] * n` + figure, position du
maximum, transposée) · §7 dictionnaires (syntaxe de l'annexe, `keys`, `items`, coût admis en boîte noire, masse molaire,
regroupement déroulé, inversion, clés immuables, `KeyError`, ajout pendant un parcours ; comptage renvoyé à `pydicho` §4,
hachage à `progdyn`) · §8 choisir sa structure (tableau des types, tableau des coûts renvoyant à `pyanalyse` §6, éléments
communs à deux listes : O(nm) contre O(n + m)) · hors annexe : indices négatifs, pas, `x in t`, méthodes de listes et de chaînes,
compréhension filtrée, `get`, `values`, `set`, `deepcopy`.

## Erreurs et écarts corrigés dans l'existant
- Cours : `t[-1]` présenté comme l'accès normal au dernier élément, alors que l'annexe ne retient que les indices positifs →
  `t[len(t) - 1]`, indices négatifs signalés hors annexe ; `pop`, `[e] * n`, copie superficielle, tuples à un élément,
  dépaquetage, `keys` / `items`, `copy` des dictionnaires : absents, ajoutés.
- Exercices : l'ancien « CONCOURS » (recherche dichotomique) relève du chapitre `pydicho` → gardé comme EXO 08 ordinaire, avec
  renvoi ; nouvel exercice « Concours PT » (vélos en libre-service : listes, tuples, dictionnaires, copie superficielle d'un
  dictionnaire de listes, coût). Anciens EXO 01 et 02 (somme, maximum) fusionnés en EXO 01 (cas de la liste vide, coût) ;
  ancien EXO 03 (occurrences) complété (lettre la plus fréquente).
- Cartes : aucune carte fausse. Une réponse alignée sur l'annexe (question inchangée) : n° 2 (dernier élément par
  `t[len(t) - 1]`, `t[-1]` signalé hors annexe). Les 10 autres : marquage seul. **Un seul côté retouché par carte** : question 3
  marquée (réponse inchangée) ; réponses 2, 4 à 12 (questions inchangées) ; cartes 0, 1 et 13 sans code, non touchées. Aucune
  carte retirée ni déplacée.

## Couverture du programme (annexe « Types structurés ») avant → après
| Notion | Avant | Après |
|---|---|---|
| Chaînes, tuples : `len`, indice positif, `+`, `*`, tranche | partiel (pas de `*`, `t[-1]`) | §1-§3, méthodes 2, 8, EXO 02, 06 |
| Dépaquetage de tuples | renvoi multiple seulement | §3, méthode 4, EXO 09, Concours |
| Listes : compréhension, `[e] * n`, `append` | compréhension, `append` | §4, méthode 3 |
| Listes : `pop` en dernière position | absent | §4 (pile), EXO 07 |
| Copie, caractère superficiel | `t[:]` seulement | §5, §6, méthode 5, EXO 04, Concours C2 |
| Tableaux à deux dimensions | absent | §6, méthode 6, EXO 05 |
| Dictionnaires : création, accès, insertion, `in`, `len`, `copy` | partiel | §7, méthode 7, EXO 03, 07, 09, Concours |
| Parcours `for` sur `keys` / `items` | `for cle in d` | §7 |
| Choix éclairé des collections, coûts | absent | §8, méthodes 1, 9, EXO 09, Concours D2 |

## Contrôles faits
- `python3 INFO/tests/typc/build_typc.py` : 58 blocs exécutés, tous les tests passent (dont tests aléatoires contre les fonctions
  de Python, valeurs citées dans les textes, tableaux d'états recalculés, rapport de durée `+` / `append`).
- `verif_src.py` : aucune erreur, aucune « attention » ; `apercu_src.py` à 390 et 1440 px, trois onglets : `merr`, `brut`,
  `larges` vides, aucune erreur JS ; figures capturées dans le site et regardées.
- `corriger_cartes.py typc … --essai` : 11 ; `ajouter_cartes.py typc … --essai` : 14 → 26.

## Doutes
- Hors annexe, utilisés et signalés : `type` (une console d'illustration, §3), `float` / `int` (conversions de `pybases`),
  `not in` (négation de `in`, comme dans `pydicho`), compréhensions imbriquées (forme de l'annexe appliquée deux fois).
- Le coût O(n²) des concaténations de chaînes est donné « dans le modèle de coût du programme » : l'interpréteur optimise
  parfois `r = r + c` ; la formulation reste prudente.
- Le piège `[[0] * p] * n` figure aussi dans `pyimages`, `graphes` et `progdyn` ; ici il a sa figure propre, comme référence
  des listes.
