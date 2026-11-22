# Chapitre `polynomes` (prefix `pol`) — « Polynômes » — compte rendu

Rédigé le 2026-11-22 (point 4 de l'audit, lot 6 ; `docs/audit-2026-11/maths-1a.md` lignes 33, 65, 109-111 ; §5 de
`docs/audit-2026-11.md`). Chapitre existant de 1ʳᵉ année (second semestre, partie « Polynômes » du programme).

## Fichiers
- `pol-cours.src.html` (≈ 78 000 car., dont ≈ 27 000 de figures) : `pol_construire.py` assemble `pol-cours.tpl.html`
  et `pol_figs.json` (`pol_figs.py`, outil `pol_svg.py` = copie de `calc_svg.py`, retouches `pol_retouches_figs.py`).
- `pol-meth.src.html` (10 méthodes) ; `pol-exos.src.html` (11 exercices + « Concours PT », construit depuis
  `pol-exos.tpl.html` pour la figure de Tchebychev ; retouches `pol_retouches1.py`, `pol_retouches2.py`).
- `pol-cartes-corr.json` (5 cartes, réponse seule), `pol-cartes-ajout.js` (15 cartes : 25 → 40).
- Contrôles : `pol_calculs.py` (497 vérifications sympy : divisions, restes de \(X^n\) pour n ≤ 14, Leibniz et Taylor
  sur plusieurs polynômes, racines de l'unité n ≤ 11, intégrales, sommes jusqu'à n = 29, Tchebychev jusqu'à \(T_{31}\),
  fonctions Python des corrigés ; toutes justes) ; `log_cartes_rendu.py` (84 formules des cartes, 0 erreur MathJax) ;
  `log_voir.py` (figures en clair et en sombre) ; `log_deborde5.js` (débordements à 390 px).
- `verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px pour les trois panneaux : `merr`,
  `brut`, `larges` vides, aucune erreur JS, page de 390 px au téléphone ; `corriger_cartes.py --essai`,
  `ajouter_cartes.py --essai` sans erreur.

## Erreurs trouvées et corrigées
- Cours : « deg(P ∘ Q) = deg P · deg Q » sans l'hypothèse « Q non constant » ; « λ = lim_{X→z_i}(X − z_i)F(X) »
  (limite prise sur l'indéterminée) → \(\lambda_k = P(a_k)/Q'(a_k)\) ou valeur en \(a_k\) de \((X - a_k)F\) simplifiée.
- Hors programme présenté dans le corps du cours (§2 PGCD, Bézout, Gauss ; §3 fonctions symétriques \(s_2, \ldots\)) →
  regroupé en fin de chapitre ; la somme et le produit des racines, seuls au programme, restent au §6.
- Méthode 4 d'origine : forme de la DES mal décrite (déjà en partie reprise) → méthode 10 réécrite ; méthode 5 (relations
  coefficients-racines, HP) supprimée, remplacée par une méthode « somme et produit des racines » au programme.
- EXO 01 Q2 : la somme des produits deux à deux (11) donnée comme formule de Viète exigible → signalée hors programme.
- EXO 03 et 05 : coefficients obtenus par « lim_{X→1} » → méthode du cache rédigée correctement. EXO 05 : la forme
  d'une décomposition avec pôle double n'était pas fournie (le programme l'exige) → forme donnée dans l'énoncé ;
  l'intégrale \(\int_2^{+\infty}\) (2ᵉ année) remplacée par \(I(T)\) et sa limite (outils de 1ʳᵉ année), même résultat
  \(\frac32 - \frac{\ln 3}{4}\).
- Cartes : 20 (« Σ(−1)ᵏC(n,k) = 0 » faux pour n = 0), 17 (limite sur l'indéterminée), 11 (degré 1 réduit à « X − a »),
  18 et 21 (notation C(n,k) → \(\binom nk\), comme le reste du site). Réponses seules modifiées.

## Couverture du programme (avant → après)
| Capacité du programme de PTSI | Avant | Après |
|---|---|---|
| 𝕂[X], combinaison linéaire, produit, binôme, composition | §1 (sans binôme ni exemple) | §1 (coefficients d'un produit, identification), méth. 1 |
| Degré, coefficient dominant, unitaire, 𝕂ₙ[X], degré somme/produit, intégrité | §1 | §2 (démonstration, arguments de degré), méth. 2, EXO 06 |
| Divisibilité, division euclidienne, algorithme | §2 | §3 (démonstration, potence, reste de Xⁿ), méth. 3-4, EXO 07 |
| Fonction polynomiale, racine ⟺ divisibilité, Horner | §3 (sans Horner) | §4 (démonstration, tableau, Python), méth. 5, EXO 08 |
| Nombre de racines ≤ degré, polynôme déterminé par sa fonction | 1 ligne | §5 (démonstration, P(x + 1) = P(x), unicité d'interpolation), méth. 7 |
| Multiplicité, scindé, somme et produit des racines | §3 (Viète général, HP) | §6 + figure, méth. 9, EXO 01 |
| Dérivée formelle, opérations, Leibniz | absent | §7 (démonstration, exemple), carte |
| Formule de Taylor polynomiale ; multiplicité par les dérivées | caractérisation seule | §8 (deux démonstrations, racine triple), méth. 6, EXO 02 |
| D'Alembert-Gauss, irréductibles et décomposition dans ℂ[X], Xⁿ − 1 | §3 (sans Xⁿ − 1) | §9 + figure des racines de l'unité, EXO 09 |
| Irréductibles de ℝ[X], racines conjuguées de même multiplicité | §3 (sans preuve) | §10 (démonstration, X⁶ − 1, X⁴ + 1), méth. 8, EXO 04 |
| DES à pôles simples sur ℂ et ℝ, forme fournie sinon ; primitives, dérivées k-ièmes | §4 | §11 + figure (asymptote), méth. 10, EXO 03, 05, 10 |

Hors programme regroupé en fin de cours : fonctions symétriques élémentaires, PGCD/Bézout/Gauss dans 𝕂[X],
interpolation de Lagrange (non citée par le programme de PTSI), décomposition générale, polynômes d'endomorphisme
(hors programme aussi en PT ; renvoi au polynôme caractéristique de `reduction`). Une carte HP (Lagrange).

## Sections du cours
Bloc « AU PROGRAMME · PTSI » ; §1 L'ensemble 𝕂[X] ; §2 Degré ; §3 Divisibilité et division euclidienne ; §4 Fonction
polynomiale, racines, Horner ; §5 Nombre de racines ; §6 Multiplicité, scindés, somme et produit des racines ;
§7 Dérivation et Leibniz ; §8 Taylor et multiplicité ; §9 Factorisation dans ℂ[X] ; §10 Factorisation dans ℝ[X] ;
§11 Décomposition en éléments simples ; Pour aller plus loin. 14 exemples traités, 10 blocs dépliables, une « erreur
classique » par section. Figures calculées : allure en une racine simple, double, triple ; racines 5ᵉ et 6ᵉ de
l'unité et paires conjuguées ; courbe de (x³ + 1)/((x − 1)(x − 2)) avec ses trois asymptotes ; (exercices) courbes
de Tchebychev T₂ à T₅.

## Méthodes (10, contre 5)
Coefficients et identification ; degré ; division ; reste sans division ; Horner ; multiplicité ; polynôme nul ou
déterminé ; factorisation ℂ puis ℝ ; somme et produit des racines ; DES et applications.

## Exercices (12)
01-05 d'origine corrigés (01 complété : somme et produit, paramètre) ; 06 arguments de degré (P(X²) = (X² + 1)P,
(P')² = 4P, P ∘ P = X² + 1) ; 07 restes (Xⁿ + X + 1 mod X² − 1, (X − 1)² | nXⁿ⁺¹ − (n + 1)Xⁿ + 1,
X² + X + 1 | X⁴ + aX² + 1, (X + 1)ⁿ mod X² + 1) ; 08 Horner et Python ; 09 racines de l'unité
(∏ sin(kπ/n) = n/2ⁿ⁻¹, cos(2π/5)) ; 10 DES (télescopage, dérivées n-ièmes, intégrales, dont une avec arctan et forme
fournie) ; 11 = ancien EXO 06 (fonctions symétriques, hors programme, déplacé à la fin) ; Concours PT « Polynômes de
Tchebychev » (degré et coefficient dominant, parité, T_n(cos θ) = cos nθ, unicité, Tₙ ∘ Tₘ = Tₙₘ, racines et
factorisation, somme et produit des racines, T_n'(1) = n², fonction Python).

## Notations
𝕂[X], 𝕂ₙ[X], deg 0 = −∞, \(\widetilde P\) puis \(P(x)\), \(P^{(k)}\), \(\binom nk\), ω = e^{2iπ/n} et 𝕌ₙ comme
`complexes`, j = e^{2iπ/3}, λ_k = P(a_k)/Q'(a_k).

## Renvois
`calculs` (binôme, aⁿ − bⁿ, télescopage), `complexes` (racines n-ièmes), `ev` (base (X − a)ᵏ), `dl` (Taylor des
fonctions), `contderiv` (Leibniz des fonctions), `applin` (exemples), `reduction` (polynôme caractéristique, 2ᵉ année).

## Doutes
- Le programme dit « fonctions rationnelles » : j'emploie « fraction rationnelle » (écrite en X) pour la décomposition
  et la fonction associée pour primitives et dérivées, comme le faisait déjà le chapitre.
- L'interpolation de Lagrange n'apparaît pas dans le programme de PTSI : présentée en « Pour aller plus loin » ; le cas
  particulier du §5 (unicité par le nombre de racines) reste au programme.
- Titre « Polynômes » gardé.
