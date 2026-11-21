# `pybases` (prefix `pyb`) — « Bases de Python » — compte rendu

Chapitre existant, 1ʳᵉ année, annexe « Langage Python » du programme d'informatique commune 2021 (mise en place au
1ᵉʳ semestre). Rédaction entièrement originale : exemples, exercices et données inventés.

## Fichiers produits (dans `INFO/`)
- `pyb-cours.src.html` (≈ 58 600 car.) : bloc « AU PROGRAMME · INFORMATIQUE » + 8 sections + « Pour aller plus loin » ;
  8 exemples traités, 3 figures SVG (état de la mémoire, arbre d'une expression, évaluation paresseuse), 4 tableaux calculés
  (trace d'un échange, types et valeurs, table de vérité, années bissextiles).
- `pyb-meth.src.html` : 9 méthodes (étapes, exemple éclair) + pièges.
- `pyb-exos.src.html` : 10 exercices (2 ★, 6 ★★, 1 ★★★, 1 « Concours PT » en 3 parties).
- `pyb-cartes-corr.json` (16 réponses retouchées, **aucune question modifiée**), `pyb-cartes-ajout.js` (12 cartes, 2 `cat:'form'`).
- Sources et tests : `INFO/tests/pyb/` — `code_pyb*.py` (tous les blocs de code), `test_pyb.py` (un test par bloc, consoles
  vérifiées par `doctest`, affirmations chiffrées des textes), `figs_pyb.py`, `tables_pyb_exos.py`, gabarits `*.tpl.html`
  (code en ligne écrit entre accents graves), `build_pyb.py` (tests puis assemblage : le code affiché est exactement le code
  testé), `cartes_pyb.py`. Outils communs avec `pyc` : `outils.py` (copie adaptée de `tests/anal/outils.py` : sorties et erreurs
  attendues capturées, accents graves → code en ligne), `figs.py`. Reconstruction : `python3 INFO/tests/pyb/build_pyb.py`.

## Cours (avant : 4 sections, ≈ 6 000 car. de HTML)
1. Écrire et exécuter : console / script, commentaires, expression / instruction (renvoi à `pyanalyse` §1), lire un message
   d'erreur (exemple : script interrompu à la ligne 3).
2. Variables et affectation : évaluation du membre de droite puis liaison, figure « état mémoire », règles de nommage, trace
   de l'échange par sommes, échange faux / juste, dépaquetage, `+=` (signalé hors annexe).
3. Types de base, typage dynamique (exigible, absent avant), entiers exacts / flottants approchés, tableau « type et valeur ».
4. Opérations : division euclidienne `a = bq + r` (formule nommée), priorités (figure arbre), durées, chiffres d'un entier,
   piège `^`.
5. Comparaisons : ordre lexicographique des chaînes (majuscules avant minuscules, `"10" < "9"`), flottants et tolérance.
6. Booléens : table de vérité, priorités, De Morgan, année bissextile, piège `x == 1 or 2`.
7. Évaluation paresseuse (exigible, absente avant) : figure, démonstration par une fonction témoin, gardes `d != 0 and …`,
   `i < len(mot) and mot[i] …`.
8. `print` simple, afficher ≠ renvoyer (`None`), chaînes `+ * len`, conversions `int/float/str` (signalées hors annexe,
   indispensables pour les fichiers).
Hors programme regroupé en fin : `input`, f-strings, `sep`/`end`, `//` et `%` avec opérandes négatifs (l'ancien cours
présentait `input` et les f-strings comme du cours).

## Couverture de l'annexe (avant → après)
| Élément | Avant | Après |
|---|---|---|
| Typage dynamique | absent | §3 |
| `int` : `+ - * // ** %` (opérandes positifs) | bref | §4, M2-M3, EXO 01-05, 08 |
| `float` : `+ - * / **` | bref | §3-§4, §5 (tolérance), M7 |
| `not`, `and`, `or` et caractère paresseux | opérateurs cités, paresse absente | §6-§7, M5-M6, EXO 06-07, Concours B |
| Comparaisons | citées | §5 |
| Affectation, dépaquetage | bref | §2, M1, EXO 04 |
| Commentaire `#`, `print` simple | bref | §1, §8, Concours C |

## Méthodes et exercices
- Méthodes : les 2 anciennes gardées (« lire au clavier » est fondue dans M8 avec `input` signalé hors programme ; « choisir
  `/`, `//`, `%` » = M2), 7 nouvelles.
- Exercices gardés : anciens EXO 01 (+ Q2 sur les types), 02 (adapté : la donnée est une ligne lue dans un fichier au lieu de
  `input`, + Q3), 03 (+ permutation circulaire) ; l'ancien « CONCOURS » devient EXO 09 (★★★, ses questions A2, A3 gardées, A1
  sur les opérandes négatifs signalé « hors programme », + `^`), sa partie B (somme des chiffres) passe dans EXO 05.
- Nouveaux : types d'expressions, chiffres, De Morgan, paresse (tableau calculé), calendrier et horloge (dates vérifiées avec
  `datetime`), Concours PT « Horodatage d'une station météo » (conversions, `meme_heure` sans `if`, `valide` / `suspecte` par De
  Morgan, `proche` protégé par l'évaluation paresseuse, `afficher` et `None`, limite d'un compteur 32 bits).

## Cartes
- Corrigées (réponse seule, question identique : progression conservée) : marquage du code de toutes les cartes ; les
  formulations « un seul symbole / symbole doublé / deux astérisques », écrites pour éviter l'ancienne mathématisation, sont
  remplacées par `/`, `//`, `**` ; cartes 9 (`input`) et 10 (f-string) préfixées « Hors programme (non exigible aux
  concours) » ; carte 2 : `type` signalé hors annexe ; petites précisions (carte 0 : membre de droite calculé d'abord ; carte 5 :
  `^`). Aucune carte n'était fausse.
- Ajoutées (12) : division euclidienne (form), chiffres, priorités de `**`, lecture de `not a or b and c`, typage dynamique,
  paresse, garde `d != 0 and …`, flottants, De Morgan (form), `"3" * 4`, `int(3.9)`, `2 ^ 3`.

## Contrôles
`verif_src` sans erreur ; `apercu_src` à 390 et 1440 px sur les trois onglets : `merr`, `brut`, `larges` vides, aucune erreur
JS ; figures regardées en capture (390 px) ; `corriger_cartes.py --essai` (16) et `ajouter_cartes.py --essai` (16 → 28) sans
erreur. 69 blocs de code testés.

## Doutes
- Conversions `int/float/str`, `type`, `abs`, `+=` ne sont pas dans l'annexe : présentés comme « d'usage courant, rappelés par
  les énoncés ». À trancher si l'on veut être plus strict.
- Les consoles d'erreur reproduisent les messages de Python 3.13 ; d'anciennes versions formulent parfois différemment.
- Le concours utilise `def`/`return` et des annotations de type avant le chapitre « Fonctions » (rappelés dans l'énoncé).
