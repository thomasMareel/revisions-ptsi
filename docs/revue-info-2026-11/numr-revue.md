# `pynum` (prefix `numr`) — « Méthodes numériques » — compte rendu

Chapitre existant, 1ʳᵉ année. Rédaction entièrement originale : exemples, exercices et données inventés (l'équation
\(x^3 - 2x - 5 = 0\) et le cycle de Newton pour \(x^3 - 2x + 2\) sont des exemples mathématiques classiques, sans emprunt de
texte).

## Place dans les programmes (point central de la revue)
Le programme d'informatique commune 2021 **n'a pas de partie « méthodes numériques »** (elle existait dans le programme de
2013). Le chapitre a donc été recentré sur ce qui est exigible en informatique — dichotomie (S1), méthodes de programmation :
spécification, variant, invariant, complexité, tests (S2, 2.1), représentation des nombres et précision des flottants
(S2, 2.2, qui cite explicitement « l'utilisation d'algorithmes de calcul numérique ») — en signalant dans le bloc « Au
programme » et en tête des sections ce qui relève des autres disciplines :
- physique-chimie PTSI, annexe « outils numériques » : dichotomie avec précision donnée et `bisect`, rectangles, nombre
  dérivé approché, Euler explicite, système d'ordre 1 et `odeint`, `matplotlib` ; PT : différences finies → chapitre
  « Diffusion thermique » (non refait ici) ;
- mathématiques PTSI : TVI et dichotomie, sommes de Riemann, rectangles et trapèzes (→ « Intégration
  (approfondissements) », mêmes notations \(h\), \(x_k\), \(R_n\), \(T_n\), \(M_1\), \(M_2\)), Newton (→ « Suites numériques
  (approfondissements) »), Euler ;
- SI PT : → « Résolution numérique en sciences de l'ingénieur » (Newton §4, systèmes linéaires §5, validation §9), sans la
  refaire.
Newton est conservé (il était dans le chapitre et revient dans les sujets), présenté comme non exigible en informatique.

## Fichiers produits (dans `INFO/`)
- `numr-cours.src.html` (≈ 104 000 car.) : bloc « AU PROGRAMME · INFORMATIQUE » + 8 sections + « Pour aller plus loin » ;
  8 exemples traités, 8 figures SVG calculées (tabulation et changement de signe ; intervalles successifs de la
  dichotomie ; tangentes de Newton ; rectangles et trapèzes ; erreur de la dérivée numérique en fonction du pas, échelles
  log ; polygone d'Euler contre \(\mathrm{e}^t\) ; pendule simulé avec deux pas ; erreur en fonction de \(n\), pentes −1 et
  −2), tableaux calculés (tabulation, trace de dichotomie, Newton, intégrales, Euler pas à pas et erreurs, périodes du
  pendule, rapports d'erreurs).
- `numr-meth.src.html` : 8 méthodes (étapes, exemple éclair) + pièges.
- `numr-exos.src.html` : 10 exercices (3 ★, 4 ★★, 2 ★★★, 1 « Concours PT » en 4 parties).
- `numr-cartes-corr.json` (8 réponses retouchées, **aucune question modifiée**), `numr-cartes-ajout.js` (12 cartes, 3 `cat:'form'`).
- Sources et tests : `INFO/tests/numr/` — `code_numr.py`, `code_numr_exos.py`, `test_numr.py` (56 blocs, 38 tests :
  dichotomie sur 200 cas aléatoires, ordre 1 d'Euler et ordres 1 et 2 des intégrales mesurés, périodes du pendule comparées
  à l'intégrale elliptique exacte de `scipy`, recherche dichotomique comparée à une recherche naïve, consoles par
  `doctest`), `figs_numr.py`, `tables_numr_exos.py`, gabarits, `build_numr.py`, `cartes_numr.py`.
  Reconstruction : `python3 INFO/tests/numr/build_numr.py`.

## Cours (avant : 4 sections, ≈ 3 700 car. de HTML)
1. Valeur approchée : fonctions passées en argument, `tableau_valeurs` (abscisses `a + k * h`), localisation d'une racine
   (`changements_de_signe`), `matplotlib` documenté, erreur de méthode / erreur d'arrondi, compromis.
2. Dichotomie : définition, `zero_dicho` (une évaluation par tour), parallèle avec `dicho` de `pydicho` (\([g, d]\) →
   \([a, b]\)), invariant, terminaison, \(N = \lceil \log_2((b-a)/\varepsilon) \rceil\), trace pour \(\sqrt 2\), version
   `zero_dicho_n` à nombre d'étapes fixé, **piège d'une précision plus fine que l'écart des flottants (boucle infinie)**,
   erreurs classiques, `bisect`.
3. Newton (signalé hors programme d'informatique) : formule, figure, `newton` borné, tableau de convergence quadratique,
   cycle, comparaison avec la dichotomie.
4. Rectangles et trapèzes : définitions, figure, code, coût \(O(n)\), tableau pour \(\int_0^1 \mathrm{e}^x\), majorations
   d'erreur (ordre 1, ordre 2), choix de \(n\) (476 trapèzes pour \(10^{-6}\)).
5. Mesures et dérivée : `trapezes_mesures` à pas variable, différences avant et centrée, `derivee_mesures`, **erreur de
   méthode contre erreur d'arrondi** (courbe en V, pas optimal \(\sqrt\epsilon\)).
6. Euler : définition, code (instants recalculés depuis `k`), exemple \(y' = y\), ordre 1 mesuré, instabilité pour
   \(h \gt 2\tau\).
7. Ordre 2 et systèmes : vecteur d'état, `euler_ordre2` (affectation multiple), pendule non linéaire (non-isochronisme),
   dérive d'énergie d'Euler, `odeint`.
8. Validation : cas exacts, mesure de l'ordre, coût d'une précision.
Hors programme : Simpson, Runge-Kutta, Euler implicite et symplectique, sécante, pivot de Gauss (renvois).

## Méthodes et exercices
- Méthodes : les 2 anciennes gardées et complétées (M2 « Appliquer la dichotomie », M3 « Choisir dichotomie ou Newton ») ;
  l'ancien encadré « Pièges classiques » est conservé à la fin, complété ; 6 nouvelles (localiser, intégrer, mesures,
  dérivée et pas, Euler, valider).
- Exercices gardés : anciens EXO 01, 02, 03 (énoncés et réponses conservés, questions ajoutées ; difficultés ramenées à ★,
  l'ancien EXO 03 était noté ★★★ pour deux multiplications).
- Nouveaux : dichotomie à précision donnée (\(\cos x = x\)), dichotomie qui ne termine pas, distance à partir de mesures,
  choix du pas d'une dérivée (tableau calculé), Newton/Héron, circuit RC en créneau (capacité de physique, calcul sur
  l'indice entier), « Concours PT » : chute d'un parachutiste (Euler, validation par l'ordre, trapèzes sur valeurs
  calculées, preuve de monotonie de la suite d'Euler, recherche dichotomique d'un premier indice avec invariant et
  variant, complexités).

## Cartes
- Corrigées (réponse seule, question identique) : 1, 3, 4, 5, 6, 7, 8, 9 — formules en `\( … \)`, notations alignées sur le
  cours (\(x_k\), \(t_k\), \(F\)), précisions (nombre exact d'étapes, ordre 1 / ordre 2, Newton signalé non exigible en
  informatique). Aucune carte n'était fausse ; la carte 7 (« ils suivent mieux la courbe ») était seulement vague.
  Cartes 0, 2, 10, 11 inchangées (ni code ni formule).
- Ajoutées (12) : invariant de la dichotomie, boucle infinie flottante, formule des trapèzes (form), cas exacts, dérivée
  approchée (form), pas trop petit, deux erreurs, Euler d'ordre 2, pas trop grand, coût (form), mesure de l'ordre,
  `bisect` et `odeint`.

## Contrôles
`verif_src` sans erreur ni « attention » ; `apercu_src` à 390 et 1440 px sur les trois onglets : `merr`, `brut`, `larges`
vides, aucune erreur JS, pas de débordement de page ; figures regardées en capture ; `corriger_cartes.py --essai` (8) et
`ajouter_cartes.py --essai` (12 → 24) sans erreur ; `verif_cartes.js` sans remarque.

## Doutes
- Faut-il garder Newton dans un chapitre d'informatique ? Gardé, signalé non exigible, car présent avant et fréquent dans
  les sujets ; à retirer facilement (§3 et EXO 08) si l'on veut s'en tenir au programme strict.
- Les valeurs du pendule « exactes » viennent de l'intégrale elliptique (calculée avec `scipy` dans les tests) : le cours
  dit seulement « une autre méthode (une intégrale, hors programme) ».
- Les renvois aux chapitres « Fonctions » (`tabuler`), « Spécification, correction et complexité » (§5, §8) et
  « Recherche séquentielle, dictionnaires et dichotomie » (§7) supposent l'intégration simultanée des nouveaux chapitres.
- Les consoles `scipy` (`bisect`, `odeint`) dépendent de la version installée pour les derniers chiffres (vérifiés avec
  scipy 1.18).
