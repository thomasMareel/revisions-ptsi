# Revue du chapitre `pytri` (prefix `tri`) — « Algorithmes de tri »

Chapitre existant, réécrit entièrement (cours, méthodes, exercices) ; cartes corrigées et complétées.

## Fichiers produits (dans `INFO/`)
- `tri-cours.src.html` (≈ 83 000 car. : bloc « AU PROGRAMME · INFORMATIQUE », 8 sections §1–§8, « POUR ALLER PLUS LOIN », 9 exemples traités, 7 figures SVG calculées, 7 tableaux d'états calculés).
- `tri-meth.src.html` (8 méthodes, 4 pièges), `tri-exos.src.html` (8 exercices ★ à ★★★ + 1 « Concours PT » en 3 parties, 9 questions).
- `tri-cartes-corr.json` (12 réponses : 1 carte fausse corrigée + 11 marquages), `tri-cartes-ajout.js` (12 cartes nouvelles).
- Sources et tests : `INFO/tests/tri/` — `tri_code.py` (tout le code du chapitre, blocs `# >>> nom`, démonstrations `expr  # valeur` vérifiées, tests), `tri_figs.py` (figures et tableaux produits en exécutant les algorithmes), gabarits `tri-{cours,meth,exos}.tpl.html`, `build.py` (`python3 -I build.py html tri` : teste puis écrit les trois `.src.html` ; échoue si un test échoue), `longueurs.py` (lignes de code ≤ 58 signes).

## Couverture du programme (avant → après)
| Notion (programme 2021) | Avant | Après |
|---|---|---|
| Tri par sélection, par insertion | code, invariant, coût | + déroulés calculés, preuves complètes, nombre exact de comparaisons, décalages = inversions, stabilité démontrée sur un exemple |
| Tri à bulles (S1, boucles imbriquées) | « complément », « pas au cœur du programme » | §2 complet : invariant, coût meilleur/pire, échanges = inversions |
| Tri par partition-fusion | une phrase, renvoyé au chapitre Récursivité (qui ne le traitait pas) | §5 : fusion (invariant, variant, coût), tri récursif, arbre des appels, récurrence \(C(n) = 2C(n/2) + cn\) démontrée, espace, stabilité |
| Tri rapide | absent | §6 : version listes, partition en place (invariant, figure, déroulé), pire cas \(n(n-1)/2\) et `RecursionError` sur liste triée (vérifié : 1000 valeurs), meilleur cas, non-stabilité, pivot aléatoire |
| Tri par comptage | absent | §7 : code, coût \(O(n+m)\), limites, version stable à clés (concours) |
| Stable / en place / comparatif | stable, en place | §1 définitions + bilan §8 (tableau des 6 tris, courbes et mesures de comparaisons) |
| Tests, spécification, complexité en espace | — | §1 (postcondition double), §8 (jeu de tests + comparaison à `sorted`), espace de chaque tri |

## Erreurs ou faiblesses corrigées dans l'ancien contenu
- Carte 15 (fausse) : « le tri fusion … Il est vu avec la récursivité » — aucun chapitre ne le traitait ; il est maintenant dans ce chapitre. Réponse corrigée (question inchangée).
- Ancien cours : « Les algorithmes au programme procèdent par comparaisons et échanges » (faux pour le tri par comptage) ; tri à bulles présenté comme hors du cœur du programme alors qu'il est cité au S1 ; libellés de figure à 9 px (< 12 px).
- Anciennes fonctions en place qui faisaient aussi `return t` : désormais un tri en place ne renvoie rien (et l'erreur `t = tri_insertion(t)` est expliquée), un tri qui renvoie une nouvelle liste ne modifie pas son entrée.

## Choix
- Notation \(t[a..b]\) (indices inclus, comme \(t[g..d]\) du chapitre `pydicho`) définie au §1 et reliée aux tranches Python ; renvois aux chapitres *Spécification, correction et complexité* (preuves, relations de coût) et *Recherche séquentielle, dictionnaires et dichotomie*, sans les refaire.
- Tri rapide : pivot = premier élément, partition « à un indice » (k, j) ; la partition en trois zones est l'exercice 8 (drapeau). Le coût moyen (≈ 1,39 n log₂ n) est signalé hors programme ; le cours cite seulement les mesures (≈ 11 000 comparaisons contre 8 700 pour la fusion, n = 1000).
- Seuls les éléments de l'annexe sont utilisés dans le code présenté (pas de compréhension filtrée, pas de `pop(0)`, pas d'indice négatif) ; `sorted`, `sort`, `random.randint` sont documentés et réservés aux tests.
- Erreurs classiques toutes vérifiées par exécution : `j >= 0` oublié ([2, 1, 1, 3] → [1, 1, 3, 2] sans message), `range(n - k)` (IndexError), `imin = 0`, cas de base n = 0 seul dans le tri fusion (RecursionError), pivot gardé dans l'appel de droite (RecursionError).
- Tests : chaque tri comparé à `sorted` sur ≈ 400 listes aléatoires + cas limites (vide, une valeur, toutes égales, triée, à l'envers, doublons, négatifs) ; stabilité testée sur des couples ; décomptes (comparaisons, échanges, décalages, profondeur) vérifiés contre les formules.

## Cartes
- Corrections (`tri-cartes-corr.json`) : **seules les réponses** sont modifiées (questions intactes, progression conservée). Carte 15 : contenu corrigé. Cartes 0, 2, 4–10, 12, 16 : marquage seul (code en accents graves, formules en `\( … \)`), même texte.
- Non modifiées (pas de code) : 1, 3, 11, 13, 14. Les questions des cartes 10 (« x = t[i] ») et 12 (« echange ») contiennent un bout de code non marqué : laissées telles quelles pour ne toucher qu'un côté de chaque carte.
- Ajouts (12, à la fin) : partition-fusion (principe, coût de la fusion, récurrence, en place/stable), tri rapide (principe, pire cas, meilleur cas, en place/stable), comptage, tri comparatif, inversions, classement sur deux critères.
- Contrôles : `corriger_cartes.py tri … --essai` → 12 réponses ; `ajouter_cartes.py tri … --essai` → 17 → 29 cartes.

## Contrôles passés
- `verif_src.py` sur les trois fichiers : aucune erreur (seul « pas de bloc AU PROGRAMME · PT », faux positif connu).
- `apercu_src.py` à 390 et 1440 px (cours, méthodes, exercices) : `merr`, `brut`, `larges` vides, aucune erreur JS ; figures regardées en capture.

## Doutes
- Les cartes existantes parlent de « tableau » ; le nouveau cours dit « liste » (vocabulaire de l'annexe) en signalant l'équivalence : laissé tel quel pour ne pas toucher aux questions.
- La limite de récursion (≈ 1000) dépend de l'installation de Python ; les valeurs citées (liste triée de 1000 valeurs → `RecursionError`, 900 → correct) sont celles de Python 3.13 par défaut.
