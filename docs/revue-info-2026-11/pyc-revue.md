# `pyctrl` (prefix `pyc`) — « Conditions & boucles » — compte rendu

Chapitre existant, 1ʳᵉ année, annexe « Langage Python », rubrique « Structures de contrôle » (1ᵉʳ semestre). Rédaction
entièrement originale : exemples, exercices et données inventés. Invariants, variants et complexité sont seulement
mentionnés, avec renvoi à `pyanalyse` (« Spécification, correction et complexité ») ; listes et dictionnaires renvoient à
`pytypes` ; la recherche séquentielle et les algorithmes à boucles imbriquées du programme (facteur, deux plus proches) restent
dans `pydicho`.

## Fichiers produits (dans `INFO/`)
- `pyc-cours.src.html` (≈ 59 600 car.) : « AU PROGRAMME · INFORMATIQUE » + 8 sections + « Pour aller plus loin » ;
  10 exemples traités, 4 figures SVG (blocs et indentation, organigrammes `if/elif/else` et `while`, grille des couples
  `i < j`), 6 tableaux calculés (tarifs, traces de `n!`, `nb_doublets`, `nb_chiffres`, `est_premier(91)`, `indice_max`) et le
  tableau des accumulateurs.
- `pyc-meth.src.html` : 9 méthodes + pièges.
- `pyc-exos.src.html` : 10 exercices (3 ★, 5 ★★, 1 ★★★, 1 « Concours PT » en 3 parties).
- `pyc-cartes-corr.json` (15 réponses retouchées, **aucune question modifiée**), `pyc-cartes-ajout.js` (12 cartes, 2 `cat:'form'`).
- Sources et tests : `INFO/tests/pyc/` — `code_pyc*.py`, `test_pyc.py` + `test_pyc_suite.py` (85 blocs, 68 tests, consoles par
  `doctest`, comparaisons à des implémentations de référence sur des listes aléatoires), `figs_pyc.py`, `tables_pyc_exos.py`,
  gabarits, `build_pyc.py`, `cartes_pyc.py` (outils communs dans `tests/pyb/`). Reconstruction :
  `python3 INFO/tests/pyc/build_pyc.py`.

## Cours (avant : 4 sections, ≈ 4 600 car.)
1. Blocs et indentation (figure), quelles lignes s'exécutent, `IndentationError`.
2. `if / elif / else` : organigramme, ordre des tests (tarifs, branche inaccessible), deux `if` contre `elif`, nombre de racines
   d'un trinôme, renvoyer un booléen, pièges (`x == 1 or 2`, `if trouve == True`).
3. `for` sur `range` : nombre de tours \(b - a\) (formule nommée), trace de \(n!\), `print` dedans / après la boucle, `range`
   n'accepte que des entiers (grille `x = a + k * h`), variable de boucle, pas (signalé hors annexe).
4. Parcours de chaînes, listes, tuples, dictionnaires (`keys`, `items`) ; par élément ou par indice, trace de `nb_doublets`.
5. `while` : organigramme, `nb_chiffres` (trace, variant mentionné), seuil (capital), `for` → `while`, boucle de recherche à
   condition double et évaluation paresseuse, boucle infinie, compteur flottant (11 tours au lieu de 10).
6. `break` et `return` dans une boucle (exigibles, absents avant) : schéma de recherche et ses deux `return`, erreur du `else:
   return False` (liste vide → `None`), `est_premier` (trace de 91), `break` et sa version `while`.
7. Accumulateurs : tableau des schémas, maximum (piège de l'initialisation à 0), indice du maximum (`>` ou `>=`), chaîne
   renversée, plusieurs accumulateurs (`stats`).
8. Boucles imbriquées : étoiles, couples `i < j` et \(n(n-1)/2\) (figure, formule nommée), triplets pythagoriciens, coût.
Hors programme regroupé en fin : `continue`, `for/while … else`, expression conditionnelle, `enumerate`, `zip` (l'ancien
cours présentait `continue` comme du cours).

## Couverture de l'annexe (avant → après)
| Élément | Avant | Après |
|---|---|---|
| Principe d'indentation | 1 encadré | §1 |
| `if`, `elif`, `else` | 1 exemple | §2, M4, EXO 04 |
| `for` sur `range(a, b)` | bref | §3, M3, EXO 01-02 |
| `for` sur chaîne, tuple, liste, dictionnaire (`keys`, `items`) | chaîne seulement | §4, EXO 05, 07 |
| `while` (sans `else`) | bref | §5, M8, EXO 03, 09, Concours A |
| `break`, `return` dans un corps de boucle | `break` cité | §6, M5, EXO 05-06, Concours A-B |
| Accumulateurs, boucles imbriquées | bref | §7-§8, M2, M6, M9, EXO 07-08, Concours C |

## Méthodes et exercices
- Méthodes : les 2 anciennes (choisir `for`/`while`, accumuler) gardées et complétées, 7 nouvelles ; pièges anciens gardés.
- Exercices gardés : anciens EXO 01-03 (chacun + une question : somme des carrés, `n // 2`, exposant) ; l'ancien
  « CONCOURS » Syracuse devient EXO 09 (★★★, code et texte gardés, + une phrase sur la terminaison inconnue et le résultat
  pour \(N = 30\) : 27, 111 étapes).
- Nouveaux : frais de port (ordre des tests), parcours de chaîne, diviseurs et premiers (avec la fonction fautive à
  `else: return True`), maximum et écarts, boucles imbriquées accélérées (\(\sqrt N\) tours), Concours PT « Surveillance d'une
  crue » (recherche avec `return`, `while` à garde, comptage d'épisodes avec garde `i == 0 or …`, plus long épisode, moyennes
  glissantes naïves puis linéaires, comptes d'opérations, comparaison de flottants).

## Cartes
- Corrigées (réponse seule, question identique : progression conservée) : marquage du code ; **carte 10** (`break` /
  `continue`) : `continue` signalé hors programme ; **carte 15** (maximum) : l'ancienne réponse autorisait « une valeur très
  petite » comme initialisation, piège classique → initialisation par le premier élément, avec la raison ; précisions mineures
  (cartes 3 : pas hors annexe ; 5 : aucun tour possible ; 6 : égalité jamais atteinte ; 7 : initialisation du maximum ; 14 :
  `note >= 10`). Carte 8 inchangée (pas de code).
- Ajoutées (12) : nombre de tours d'un `range` (form), `return` dans une boucle, place du `return False`, `if`/`if` contre
  `if`/`elif`, `x == 1 or 2`, parcours d'un dictionnaire, couples `i < j` (form, formule en `\\( … \\)`), `break` imbriqué,
  variable de boucle, ordre de la condition double, variant, `range` et flottants.

## Contrôles
`verif_src` sans erreur ; `apercu_src` à 390 et 1440 px sur les trois onglets : `merr`, `brut`, `larges` vides, aucune erreur
JS ; figures regardées en capture (390 px, ligatures du code coupées dans les SVG) ; `corriger_cartes.py --essai` (15) et
`ajouter_cartes.py --essai` (16 → 28) sans erreur.

## Doutes
- `range(n)` et `range(a, b, p)` : l'annexe ne cite que `range(a, b)` ; `range(n)` est présenté comme son abréviation, le pas
  comme hors annexe.
- Les exemples utilisent `def` / `return` avant le chapitre « Fonctions » (indispensable pour `return` dans une boucle) ; un
  encadré le signale.
- L'exercice Syracuse (EXO 09) recoupe l'exemple de terminaison de `pyanalyse` §3 ; il y renvoie.
