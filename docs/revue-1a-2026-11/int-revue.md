# `integrales` (prefix `int`) — compte rendu, 2026-11-21

Point 3 de l'audit `docs/audit-2026-11/maths-1a.md` (§2) et recommandation 3 (§5). Cours réécrit en entier au format de la
1ʳᵉ année (bloc « AU PROGRAMME · PTSI », sections §n, exemples traités chiffrés, démonstrations en `.reveal`, figures
calculées), méthodes et exercices complétés, cartes relues et complétées.

## Fichiers produits

| Fichier | Contenu |
|---|---|
| `int-cours.src.html` | cours complet (98 111 car., dont ≈ 42 000 de SVG ; 11 sections, 17 exemples, 5 figures) — construit par `int_construire.py` depuis `int-cours.tpl.html` et `int_figs.json` |
| `int-meth.src.html` | 10 méthodes + encadré des pièges |
| `int-exos.src.html` | 11 exercices + 1 « Concours PT » — construit par `int_exos_existants.py` (EXO 01-06 conservés) puis `int_exos_construire.py` (+ `int_exos_ajout.html`) |
| `int-cartes-corr.json` | 1 carte corrigée (réponse seule) |
| `int-cartes-ajout.js` | 14 cartes nouvelles (25 → 39) |
| Scripts | `int_calculs.py` (exemples du cours), `int_calculs_exos.py` (méthodes, exercices), `int_figs.py` + `int_svg.py` (figures, outil commun avec `ser`), `int_voir.py` (captures des figures), `int_cartes_rendu.py` (rendu MathJax des cartes) ; copies des panneaux d'origine `int_orig_{cours,meth,exos}.html` |

## Erreurs et défauts corrigés

1. **Définition contraire au programme** : l'intégrale était *définie* par une primitive (« ∫ = F(b) − F(a) »), alors que le
   programme de PTSI la construit à partir des fonctions en escalier et démontre ensuite le lien avec les primitives. Le cours
   suit maintenant l'ordre du programme (§1 escalier, §2 encadrement, §7 théorème fondamental). La **carte 0** disait la même
   chose : réponse corrigée (question inchangée).
2. **Manques signalés par l'audit**, tous comblés : subdivision, pas et fonctions en escalier (§1) ; théorème d'approximation et
   définition (§2) ; inégalité de Taylor-Lagrange avec démonstration, différence Taylor-Young / Taylor-Lagrange, formule avec
   reste intégral signalée non exigible (§10) ; méthodes des rectangles et des trapèzes avec majorations d'erreur (§6) ;
   intégrale d'une fonction à valeurs complexes, majoration du module, Taylor-Lagrange complexe (§11).
3. **Exercice « Concours PT » sans substance** : ses deux questions reprenaient l'EXO 02 Q1 et l'exemple du cours (somme de
   Riemann de 1/(n+k)). Remplacé par un vrai problème en quatre parties (quatre façons d'approcher ln 2).
4. **Méthode 3** proposait `x = a sh u` (« hors programme strict mais utile ») : les fonctions hyperboliques réciproques sont
   hors programme ; retiré.
5. **Débordements au téléphone** : six formules en ligne des solutions conservées (EXO 02, 03, 05) dépassaient 390 px ; passées
   en bloc (`.formula`). Différentielles harmonisées (`\mathrm{d}x` au lieu de `dx`, comme `integ2a`).

Les exercices EXO 01 à 06 d'origine sont justes (recalculés en sympy) et conservés.

## Couverture du programme (section « Intégration » de PTSI) avant → après

| Capacité | Avant | Après |
|---|---|---|
| Subdivision, pas, fonction en escalier | ❌ | ✅ §1 (cours, carte, EXO 07) |
| Intégrale d'une fonction continue, interprétation géométrique, notations, b ≤ a | 🔶 (par les primitives) | ✅ §2 (figure aire algébrique, figure escaliers, EXO 07) |
| Linéarité, positivité, croissance, inégalité triangulaire, Chasles | ✅ | ✅ §3 (démonstrations, encadrement de ∫e^{−t²}) |
| Continue positive d'intégrale nulle | 🔶 (énoncé seul) | ✅ §3 (démonstration, EXO 08) |
| Parité, périodicité, valeur moyenne | 🔶 | ✅ §4 (démonstrations, valeur efficace, figure) |
| Sommes de Riemann, démonstration C¹ | 🔶 (sans démonstration) | ✅ §5 |
| Rectangles et trapèzes, comparaison | ❌ | ✅ §6 (figure, tableau, majorations, méthode 8, EXO 10, concours) |
| Dérivation de x ↦ ∫ₐˣ f, existence de primitives | ✅ | ✅ §7 (démonstration, bornes variables, méthode 9) |
| Intégration par parties, changement de variable | ✅ | ✅ §8, §9 (récurrences, piège numérique) |
| Inégalité de Taylor-Lagrange ; Young local / Lagrange global | ❌ | ✅ §10 (démonstration par récurrence, figure, méthode 10, EXO 11) |
| Fonctions à valeurs complexes (définition, module, Taylor-Lagrange) | ❌ | ✅ §11 (démonstration de \|∫f\| ≤ ∫\|f\|, EXO 05, 11) |

## Cours

§1 Subdivisions et fonctions en escalier · §2 Intégrale d'une fonction continue (théorème d'approximation admis, preuve dans
le cas C¹ ; aire entre deux courbes) · §3 Propriétés · §4 Symétries et valeur moyenne · §5 Sommes de Riemann · §6 Méthodes des
rectangles et des trapèzes · §7 Intégrale et primitives · §8 Intégration par parties · §9 Changement de variable · §10 Inégalité
de Taylor-Lagrange · §11 Fonctions à valeurs complexes · Pour aller plus loin (continues par morceaux, égalité de
Taylor-Lagrange, Simpson, Heine). Figures calculées : escaliers encadrant t², aire algébrique de sin, valeur moyenne de sin,
rectangles et trapèzes pour 4/(1+t²), polynômes de Taylor de ln(1+x) ; vérifiées en clair et en sombre.

## Méthodes (10)

Choisir la technique ; choisir u′ et v ; enchaîner les IPP ou passer en complexes ; changement de variable ; parité,
périodicité, symétrie ; encadrer une intégrale ou une suite d'intégrales ; reconnaître une somme de Riemann ; approcher une
intégrale avec une précision garantie ; étudier une fonction définie par une intégrale ; majorer une erreur par
Taylor-Lagrange. Les six méthodes d'origine sont reprises (fractions rationnelles intégrées à la méthode 1).

## Exercices (12)

EXO 01-06 conservés ; nouveaux : 07 escaliers et définition (∫eᵗ sans primitive), 08 propriétés (intégrale nulle,
x − x²/2 ≤ ln(1+x) ≤ x), 09 suite ∫(1−t²)ⁿ (récurrence, formule close, limite via la majoration de Φ du cours), 10 rectangles
ou trapèzes pour ∫e^{−t²}, 11 Taylor-Lagrange et inégalités intégrées (dont \|e^{iθ} − 1\| ≤ \|θ\|) ; Concours PT « Quatre
façons d'approcher ln 2 » (Riemann, trapèzes, série géométrique intégrée, Taylor-Lagrange, bilan).

## Cartes

Corrigée : carte 0 (définition de l'intégrale). Ajoutées (14) : subdivision, fonction en escalier, théorème d'approximation,
rectangles, trapèzes, comparaison des deux, inégalité de Taylor-Lagrange, Young / Lagrange, intégrale complexe,
∫₀^{2π} e^{ipt}, primitive de e^{λt}, périodicité, valeur efficace (`cat:'val'`), reste intégral (« Non exigible en PTSI »).
Les 24 autres cartes sont justes et inchangées.

## Notations

Celles d'`integ2a` et de `pynum` : pas h = (b − a)/n, xₖ = a + kh, Rₙ (rectangles à gauche), Tₙ (trapèzes), M₁ = max\|f′\|,
M₂ = max\|f″\| ; Tₙ(x) pour le polynôme de Taylor au §10 seulement (comme dans `integ2a`, où la même lettre sert aux deux) ;
u′ primitivée et v dérivée dans l'IPP ; `\mathrm{d}t`.

## Doutes

- La majoration de l'erreur des trapèzes n'est pas exigée par le programme (le bandeau demande seulement de comparer les
  performances) : elle est donnée avec une démonstration marquée « non exigible » (deux IPP). `integ2a` la dit « admise » :
  cohérent, mais on pourrait y renvoyer à cette preuve.
- Les fonctions continues par morceaux ne figurent dans aucun des deux programmes : placées en « Pour aller plus loin », comme
  demandé par la consigne (« et continues par morceaux »).
- Le théorème d'approximation par des escaliers est admis (la preuve générale demande la continuité uniforme, hors
  programme) ; prouvé seulement pour f de classe C¹.
- Doublon partiel assumé avec `integ2a` (rappels de 2ᵉ année) ; exemples et figures choisis différents (4/(1+t²), ln(1+x),
  e^{−t²}…) pour ne pas répéter ceux de 2ᵉ année.
- La carte 9 (théorème de la moyenne, « c ∈ [a, b] ») est juste ; le programme ne nomme que la valeur moyenne, le cours en
  donne l'égalité comme conséquence du théorème des valeurs intermédiaires.
