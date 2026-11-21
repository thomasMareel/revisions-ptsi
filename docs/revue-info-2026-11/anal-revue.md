# `pyanalyse` (prefix `anal`) — « Spécification, correction et complexité » — compte rendu

Nouveau chapitre, 1ʳᵉ année, programme d'informatique commune 2021, partie 2.1 (2ᵉ semestre).
Rédaction entièrement originale : tous les exemples, exercices et données sont inventés.

## Fichiers produits (dans `INFO/`)
- `anal-cours.src.html` : bloc « AU PROGRAMME · INFORMATIQUE » + 9 sections + « Pour aller plus loin » ; 11 exemples traités
  (`method-box` « Exemple — … »), 5 figures SVG calculées, 4 tableaux d'états calculés par le code (≈ 81 000 caractères de
  HTML, dont ≈ 43 000 de texte ; le reste est le surlignage du code et les figures).
- `anal-meth.src.html` : 9 méthodes (étapes, exemple éclair) + 3 pièges.
- `anal-exos.src.html` : 10 exercices (2 ★, 5 ★★, 2 ★★★, 1 « Concours PT » en 4 parties), solutions complètes avec code,
  invariant, variant, complexité.
- `anal-cartes.js` : 25 cartes (`const analCards`), code entre accents graves, formules en `\\( … \\)`, 6 cartes `cat:'form'`.
- Sources et tests (dans `INFO/tests/anal/`) : `code_anal.py` (tous les blocs de code du chapitre), `test_anal.py` (un test
  par bloc, consoles vérifiées par `doctest`, vérifications des affirmations chiffrées des textes), `figs_anal.py`,
  gabarits `cours|meth|exos.tpl.html`, `build_anal.py` (lance les tests, puis assemble les panneaux : le code affiché est
  exactement le code testé), `outils.py` (commun avec `graphes`), `figs_capture.js` (captures des figures).
  Reconstruction : `python3 INFO/tests/anal/build_anal.py`.

## Contenu du cours
1. Instructions, expressions, effets de bord : affectation = instruction (conséquence : `if x = 3:` refusé, choix des
   concepteurs), effet de bord, partage des listes (appel par valeur d'une valeur partagée), copie superficielle ; figure
   « mémoire » ; exemple de prédiction d'affichage (`append` contre `t = t + [x]`).
2. Spécifier : signature (annotations documentées comme non vérifiées), préconditions, postcondition, effets de bord,
   `assert` sans message (levée = arrêt), commentaires utiles, choix des collections ; pièges `assert (x, "msg")` et
   assertion coûteuse.
3. Terminaison : variant (entier ≥ 0 strictement décroissant ⇒ au plus v₀ tours) ; Euclide (déroulé calculé), palindrome
   à deux indices, Syracuse (terminaison inconnue), fonctions récursives ; pièges : variant flottant, liste allongée pendant
   un `for`.
4. Correction : partielle / totale, invariant (figure des trois temps), division par soustractions (preuve complète +
   déroulé), boucle interrompue par `return`, correction d'une fonction récursive par récurrence (`binaire`).
5. Tests : jeu de tests en assertions, partition du domaine d'entrée, limites (figure calculée), exemple d'erreur trouvée
   seulement à la limite (`mention`), tests de flottants, piège de la sortie « attendue » calculée par le programme.
6. Complexité temporelle : taille, opérations élémentaires, pire cas, notation O, courbes de croissance (figure), tableau
   des temps à 10⁷ op/s (calculé), coût des opérations Python (`pop(0)`, `in`, tranches, `+`, dictionnaire), règles.
7. Calculs : boucles imbriquées dépendantes, boucle qui divise, coût caché + bon choix de collection (`sans_doublons` avec
   dictionnaire), relations de récurrence (démonstration dépliable), mesure expérimentale (`time.perf_counter`, rapport ×4).
8. Complexité en espace : en place contre copie, pile d'appels, coût caché des tranches (O(n²) en temps et en mémoire),
   sommes préfixes (mémoire contre temps).
9. Étude complète : séparer négatifs et positifs (spécification, invariant à trois zones avec figure, variant, déroulé,
   complexité, tests de propriété).

Exemples volontairement variés et sans tri (Euclide, palindrome, division, Horner, paysan russe, palier, médiane, montée
maximale…) ; les tris restent dans `pytri`, la dichotomie et l'exponentiation rapide dans `pydicho`.

## Couverture du programme 2.1 (avant → après)
| Notion | Avant (site) | Après |
|---|---|---|
| Instruction / expression, effet de bord | absent | §1, EXO 01 |
| Spécification, signature | 4 lignes dans `pyfonc` | §2, méthode 1, EXO 02, Concours A |
| Pré/postcondition, invariant en commentaire | `pyfonc` (bref) | §2, §4, tout le code |
| Assertion | `pyfonc` (bref) | §2 |
| Justification des choix (commentaires, collections) | absent | §2, §7, EXO 06 |
| Terminaison, variant | quelques lignes dans `pytri` | §3, méthode 2, EXO 03 |
| Correction partielle / totale, invariant | quelques lignes dans `pytri` | §4, méthodes 3-4, EXO 04, 05, 09, Concours C |
| Jeu de tests, partition, limites | absent | §5, méthode 5, EXO 02, 07, Concours A |
| Complexité temporelle pire cas | dispersée (tris) | §6, §7, méthodes 6-7, EXO 06 |
| Complexité en espace | absent | §8, méthode 8, EXO 08 |

## Contrôles faits
- Tous les blocs de code exécutés et testés (`python3 INFO/tests/anal/test_anal.py` : 54 blocs, 49 tests, consoles
  doctest, plus les vérifications des valeurs citées dans les textes : traces, nombres de tours, contre-exemples).
- `verif_src.py` : aucune erreur ; un seul avertissement (voir doutes).
- `apercu_src.py` à 390 et 1440 px pour les trois panneaux : `merr`, `brut`, `larges` vides, aucune erreur JS, pas de
  débordement. Figures capturées une à une (clair et sombre, 390 et 1440 px) et regardées.
- Cartes : `node -e …` → 25 ; questions uniques, pas de HTML, accents graves et délimiteurs appariés.

## Doutes et remarques pour l'intégration
- `verif_src.py` avertit « pas de bloc AU PROGRAMME · PT » : le surtitre est « AU PROGRAMME · INFORMATIQUE », comme le
  demandent les consignes d'informatique ; le contrôle (écrit pour les cours de 2ᵉ année) cherche la chaîne « PT ».
- Éléments hors annexe Python, tous documentés là où ils servent : annotations de type dans les signatures, `x in liste`
  (présenté avec son coût), `abs`, `str`, `time.perf_counter()`, `sorted` (seulement dans un test, signalé).
- Les durées (10⁷ opérations par seconde, mesures « environ × 4 ») sont des ordres de grandeur pour Python, annoncés
  comme tels.
- Les cartes contiennent des formules `\\( … \\)` et du code entre accents graves : elles supposent le rendu « texte tel
  quel » des decks d'informatique prévu par les consignes (aujourd'hui, les decks info passent par `flashPretty`).
- Le cours est long (9 sections) ; si l'on veut l'alléger, le §8 (espace) et l'exemple de mesure expérimentale du §7 se
  détachent facilement.
