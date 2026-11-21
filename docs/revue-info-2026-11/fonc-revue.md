# `pyfonc` (prefix `fonc`) — « Fonctions » — compte rendu (chapitre existant, 1ʳᵉ année)

Rédaction originale ; exemples et exercices inventés. Tout le code affiché est exactement le code testé.

## Fichiers produits (dans `INFO/`)
- `fonc-cours.src.html` (≈ 63 000 car.) : bloc « AU PROGRAMME · INFORMATIQUE » + 8 sections + « POUR ALLER PLUS LOIN · HORS DE
  L'ANNEXE » ; 9 exemples traités (`method-box` « Exemple — … »), 4 figures SVG (arbre d'évaluation d'un appel, espaces de noms
  local / global, pile d'appels, partage d'une liste passée en argument), 1 tableau d'états calculé, 1 trace d'erreur réelle.
- `fonc-meth.src.html` : 9 méthodes (écrire une fonction, afficher ou renvoyer, sortir d'une boucle par `return`, prédire un appel,
  local ou global, pile d'appels et trace d'erreur, modifier en place ou renvoyer, fonction en argument, coût d'appels imbriqués)
  + 2 pièges.
- `fonc-exos.src.html` : 10 exercices (3 ★, 5 ★★, 1 ★★★, 1 « Concours PT » en 4 parties, 13 questions).
- `fonc-cartes-corr.json` (10 cartes retouchées), `fonc-cartes-ajout.js` (12 cartes, 13 → 25).
- Sources et tests : `INFO/tests/fonc/` — `code_fonc.py` (67 blocs), `test_fonc.py` (58 tests, plus les consoles vérifiées par doctest),
  `figs_fonc.py`, gabarits `cours|meth|exos.tpl.html`, `build_fonc.py` (lance les tests, calcule tableaux et trace, assemble),
  `cartes_fonc.py` (produit le JSON en contrôlant le marquage), `outils.py` (copie de celui de `anal`).
  Reconstruction : `python3 INFO/tests/fonc/build_fonc.py` puis `python3 INFO/tests/fonc/cartes_fonc.py`.

## Cours
§1 définir et appeler (en-tête, corps, appel = expression, trace d'un programme ; oubli des parenthèses, appel avant la définition) ·
§2 `return` (sortie anticipée : `est_premier`, tableau des tours, coût O(√n) justifié ; `return` dans un `else` de boucle ;
afficher ≠ renvoyer, `None` ; plusieurs valeurs, dépaquetage) · §3 appel par valeur (règle en 4 temps, `incremente`, ordre
d'évaluation des arguments + figure, typage dynamique, signature annotée) · §4 portée lexicale (recherche locale puis globale,
globale lue au moment de l'appel, masquage, `UnboundLocalError`, exemple de prédiction + figure) · §5 pile d'appels (cadres,
empiler/dépiler, figure, lien avec la récursivité, lecture d'une trace d'erreur réelle) · §6 listes en argument et effets de bord
(modifier l'objet / réaffecter le nom, figure, deux contrats ; renvoi à `pyanalyse` §1-§2 pour le détail) · §7 fonctions en
argument (`tabuler`, `compter_si`, coût n·c ; passer `f(4)` au lieu de `f`) · §8 concevoir (dates : décomposition + jeu de tests ;
coût d'un appel, `nb_premiers` en O(N√N)) · hors annexe : valeurs par défaut (piège de la liste par défaut), arguments nommés,
`global`, `lambda`, exceptions.

## Erreurs et écarts corrigés dans l'existant
- Cours : valeurs par défaut (`def puissance(x, n=2)`) présentées comme exigibles → déplacées en « hors de l'annexe » avec le piège
  de la liste par défaut ; « on évite de lire des globales » nuancé (la portée lexicale permet de lire une constante globale) ;
  la spécification (docstring, `assert`) renvoie désormais à `pyanalyse` §2 au lieu d'être refaite.
- Exercices : l'ancien EXO 03 (`min_max`) utilisait `min` et `max`, hors annexe, alors que l'EXO 01 les interdisait → réécrit en
  réutilisant `maxi` / `mini` (fusionné avec l'EXO 01). L'ancien « CONCOURS » (PGCD) devient l'EXO 08 ordinaire (précondition
  `p >= 0` au lieu d'un `abs`, variant cité) ; nouvel exercice « Concours PT » (horaires d'une ligne de car). EXO 02 complété
  (réciproque, test de flottants à tolérance).
- Cartes : aucune carte fausse. Deux réponses précisées (question inchangée) : n° 6 (valeur par défaut : signalée hors annexe,
  liste par défaut à proscrire), n° 9 (communication avec l'extérieur : nuance sur les globales). Les 8 autres : marquage seul.
  **Un seul côté retouché par carte** : questions 2 et 11 marquées (réponses inchangées) ; réponses 1, 3, 4, 6, 7, 9, 10, 12
  (questions inchangées). Aucune carte retirée ni déplacée.

## Couverture du programme (avant → après)
| Notion (annexe Python, partie 2.1) | Avant | Après |
|---|---|---|
| `def`, `return`, appel | §1-§2 (brefs) | §1, §2, méthodes 1-3, EXO 01-03 |
| `return` dans une boucle | absent | §2, méthode 3, EXO 03 |
| Dépaquetage, plusieurs résultats | bref | §2, EXO 01, Concours |
| Appel par valeur | absent | §3 + figure, méthode 4, EXO 04-05 |
| Typage dynamique, signature | absent | §3 |
| Portée lexicale | « locale / globale » (bref) | §4 + figure, méthode 5, EXO 04 |
| Pile d'appels, trace d'erreur | absent | §5 + figure, méthode 6, EXO 06 |
| Effet de bord (listes) | absent | §6 + figure, méthode 7, EXO 05, Concours D2 (renvoi `pyanalyse`) |
| Fonctions en argument | absent | §7, méthode 8, EXO 07, Concours D1 |
| Décomposition, tests, coût d'un appel | absent | §8, méthode 9, EXO 06, 09, Concours |

## Doutes
- Hors annexe utilisés et documentés là où ils servent : annotations de type dans les signatures (comme les sujets), `sqrt` du
  module `math` (§5), `abs` (test de flottants, EXO 02), `type` n'est pas utilisé ici ; `lambda`, `global`, valeurs par défaut
  seulement dans la dernière section.
- La trace d'erreur du §5 est la sortie réelle de Python 3.13, sans les lignes de repères `^^^`/`~~~` (signalé dans le texte).
- Le message d'`UnboundLocalError` affiché est celui des versions récentes ; le texte précise qu'il varie selon la version.
- Le cours est long (8 sections) : §7 (fonctions en argument) et l'exemple « dates » du §8 se détachent facilement si besoin.

## Contrôles faits
- `python3 INFO/tests/fonc/build_fonc.py` : 67 blocs exécutés, tous les tests passent (sorties affichées, traces, valeurs citées
  dans le texte : nombres de tours, durées, résultats des exemples).
- `verif_src.py` sur les trois panneaux : aucune erreur, aucune « attention ».
- `apercu_src.py` à 390 et 1440 px, trois onglets : `merr`, `brut`, `larges` vides, aucune erreur JS ; figures capturées dans le
  site (clair et sombre, 390 px) et regardées.
- `corriger_cartes.py fonc … --essai` : 10 réponses (dont 2 questions marquées) ; `ajouter_cartes.py fonc … --essai` : 13 → 25.

