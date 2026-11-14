# Audit : mathématiques de 1ʳᵉ année (PTSI)

Audit en lecture seule, fait le 2026-11-14. Périmètre : les 20 chapitres `mat == "maths"`, `an == 1` de `mesures.json`. Référence : programme de mathématiques de PTSI 2021 (`ptsi_maths.txt`).
Méthode : j'ai lu en entier les 20 cours, les méthodes et les cartes des chapitres minces, et les exercices en diagonale. Les DL douteux ont été vérifiés par calcul formel (sympy).
J'ai consulté les chapitres de 2ᵉ année (`docs/programme-pt/mathematiques.md` et les encadrés « Au programme ») seulement pour savoir où une notion de 1ʳᵉ année est reprise.
À savoir : le programme de PTSI marque de « ★ » trois blocs que le programme de PT reprend en entier : les déterminants, la convergence absolue et les suites sommables, les fonctions de deux variables. Leurs manques en 1ʳᵉ année pèsent donc moins.

## 1. Couverture du programme de PTSI

| Bloc du programme | Notions / capacités exigibles | Chapitre(s) et § du site | Statut | Remarque |
|---|---|---|---|---|
| Raisonnement | quantificateurs, implication, négation, contraposée, absurde, disjonction, récurrences | `logique` §1, §4 | ✅ | Le raisonnement par analyse-synthèse (et le couple CN / CS) n'est jamais nommé. |
| Ensembles | opérations, produit cartésien, 𝒫(E), recouvrement disjoint, partition | `logique` §2 | 🔶 | 𝒫(E) et la partition sont absents. Les relations d'équivalence et d'ordre, absentes du programme, sont exposées. |
| Nombres usuels : arithmétique | division euclidienne dans ℕ, PGCD, PPCM, algorithme d'Euclide, nombres premiers (infinité, décomposition) | aucun | ❌ | Absent de tout le site, 2ᵉ année comprise : seul un `gcd` apparaît dans un corrigé de `logique`. |
| Applications | graphe, famille, indicatrice 1_A, restriction, image directe et réciproque, injections, bijections | `logique` §3 | 🔶 | L'indicatrice, la restriction, le prolongement et les familles sont absents. |
| Sommes et produits | Σ, Π, télescopage, Σk, Σk², Σxᵏ, aⁿ−bⁿ, sommes doubles, binôme | éparpillé : `denombrmt` §3, `suites` §4, `series` §4, cartes 41-43 de `suites` | 🔶 | Aucun cours sur ce bloc. aⁿ−bⁿ, les sommes doubles et les produits Π manquent. |
| Petits systèmes linéaires | pivot de Gauss, opérations Lᵢ ← … | `matrices` §3 | ✅ | Exemple 3 × 3 traité, discussion selon un paramètre. |
| Inégalités | ordre, valeur absolue, inégalité triangulaire réelle, majorants, partie entière ⌊x⌋, inéquations | `fonctions` §2 (bornes seulement) | ❌ | La valeur absolue, la partie entière et la résolution d'inéquations ne sont traitées nulle part. |
| Trigonométrie | cercle, congruence modulo 2π, formules, tangente, tan(a±b), \|sin x\| ≤ \|x\|, équations | `fonctions` §3 et méth. 2-3, `complexes` §4 | 🔶 | La fonction tangente, tan(a±b) et \|sin x\| ≤ \|x\| manquent. La mnémonique est fausse (voir §4). |
| Nombres complexes (a à h) | formes, module, 𝕌, Euler, angle moitié, Moivre, racines carrées et n-ièmes, eᶻ, géométrie | `complexes` §1–§5 | ✅ | C'est le chapitre le plus complet. La méthode 7 parle de « similitude », hors programme. |
| Fonctions : généralités, dérivation | transformations du graphe f(x+a), f(ax), parité, monotonie, dérivée de la réciproque | `fonctions` §1-2, `dl` §1-2 | 🔶 | Les transformations du graphe et les dérivées partielles simples manquent. |
| Fonctions usuelles | exp, ln, puissances, log₁₀, croissances comparées, eˣ ≥ 1+x, ln(1+x) ≤ x, Arcsin/Arccos/Arctan, ch, sh | `fonctions` §3-4 et méth. 4, `dl` §2 | 🔶 | Les deux inégalités usuelles et le log décimal manquent. th, Argsh et Argch (hors programme) sont donnés en méthode. |
| Fonctions complexes d'une variable réelle | dérivée, dérivée de exp(φ), primitives et intégrales à valeurs complexes | aucun | ❌ | Seule l'astuce de complexification apparaît (`primitives` méth. 5, `edo` §4). |
| Primitives | primitives usuelles, 1/(ax²+bx+c), e^{λx} avec λ ∈ ℂ, IPP, changement de variable | `primitives` §1-4 et méth. 3, 5, `integrales` §3-4 | ✅ | Bon chapitre, mais limité aux fonctions à valeurs réelles. |
| Équations différentielles linéaires | ordre 1 (variation de la constante, problème de Cauchy), ordre 2 à coefficients constants, seconds membres | `edo` §1-5 | ✅ | Cadre réel seulement (K ∈ ℝ), alors que le programme prend a, b, f complexes. |
| Réels et suites | borne supérieure, limites, encadrement, limite monotone, suites adjacentes, extraites, complexes, uₙ₊₁ = f(uₙ) | `suites` §1-6 | ✅ | La propriété de la borne supérieure de ℝ et les approximations décimales manquent. La vitesse de convergence est vue en 2ᵉ année (`suites2a` §6). |
| Limites et continuité | limite, opérations, TVI, bornes atteintes, bijection continue | `contderiv` §1-2 | 🔶 | La limite monotone d'une fonction et l'image d'une suite manquent. Continuité uniforme et Heine : hors programme. |
| Dérivabilité | Rolle, TAF, IAF, limite de la dérivée, classe Cᵏ, Leibniz, cas complexe | `contderiv` §3, `dl` §1-3 | 🔶 | La limite de la dérivée, la classe Cᵏ et Leibniz manquent. Rolle et TAF sont traités deux fois. |
| Calcul matriciel (S1) | opérations, transposée, binôme, inverses, Mₙ(K), GLₙ | `matrices` §1-4 | ✅ | Réécrit, exemples entièrement calculés. Matrices et opérations élémentaires vues comme produits : très bref. |
| Analyse asymptotique | o, O, ∼, DL, Taylor-Young, DL usuels, applications, extremum à l'ordre 2, cas des suites | `dl` §4-7, `asympt` §1-4 | ✅ ⚠️ | Contenu présent mais en double, avec des erreurs (voir §4). |
| **Géométrie du plan** | coordonnées polaires, produit scalaire, produit mixte dans le plan, droites, projeté, lignes de niveau, cercles | aucun | ❌ | Absente de tout le site : seuls quelques exercices de 2ᵉ année s'en servent. |
| Géométrie de l'espace | coordonnées cylindriques, produits scalaire, vectoriel et mixte, plans, droites, projetés, sphères | `geometrie` §1-3 | 🔶 | Les sphères, les projetés et le régionnement manquent. Tout est couvert en 2ᵉ année par `geo3d` (36 907 signes). |
| Polynômes | K[X], division, racines, multiplicité, Taylor, Leibniz, irréductibles, Xⁿ−1, décomposition en éléments simples (DES) | `polynomes` §1-4 | 🔶 | La formule de Taylor polynomiale, Leibniz et Xⁿ−1 manquent. PGCD, Bézout, Gauss et fonctions symétriques : hors programme. |
| Espaces vectoriels | sous-espaces, Vect, familles, bases, dimension, rang d'une famille, Grassmann, supplémentaires, base adaptée | `ev` §1-4 | 🔶 | Base extraite ou incomplète : énoncées en une ligne. Manquent le rang d'une famille, K^Ω, la dimension des solutions d'EDL et de suites, la base adaptée. |
| Applications linéaires | Ker, Im, rang, rg(v∘u), projecteurs, **symétries**, détermination par une base, forme géométrique du rang, équations u(x) = a | `applin` §1-6 | 🔶 | Les symétries (s² = id), la forme géométrique du rang et les équations linéaires manquent. |
| Matrices et applications linéaires | matrice d'une application linéaire, rang, **changement de base**, matrices semblables, systèmes | `matrices` §5 | 🔶 | Matrice de passage et matrices semblables absentes en 1ʳᵉ année. Elles sont traitées en 2ᵉ année (`matrices2a` §1, §4). |
| ★ Déterminants | caractérisation, opérations sur les colonnes, famille de vecteurs, endomorphisme, lien avec le produit mixte | `det` §1-4 | 🔶 ⚠️ | Définition par récurrence (cofacteurs). Comatrice et Cramer sont présentés comme exigibles. Le déterminant d'une famille et d'un endomorphisme manque. |
| Intégration | fonctions en escalier, propriétés, sommes de Riemann, lien avec la primitive, **Taylor-Lagrange**, cas complexe | `integrales` §1-6 | 🔶 | L'intégrale est définie par une primitive. Taylor-Lagrange, rectangles et trapèzes et le cas complexe manquent. Ils sont en 2ᵉ année (`integ2a`). |
| Dénombrement | cardinaux, applications, p-listes, combinaisons, Pascal | `denombrmt` §1-3, `proba` §1 | ✅ | Traité deux fois. |
| Probabilités finies | univers fini, conditionnement, Bayes, lois U(E), B(p), B(n,p), loi conditionnelle, couples, indépendance mutuelle, coalitions | `proba` §2-4, `va` §1, §3-4 | 🔶 | U(E), la loi conditionnelle, les n-uplets, l'indépendance mutuelle et les coalitions manquent. Le cadre dénombrable (σ-additivité, Poisson, géométrique) est présenté comme exigible. |
| Espérance et variance | transfert, linéarité, covariance, variance d'une somme, Markov, Bienaymé-Tchebychev | `va` §2, §4, `proba` §3 | ✅ | L'application à une moyenne de variables (interprétation fréquentiste) manque. |
| Séries numériques | convergence, séries géométriques, eᶻ, termes positifs, Riemann, **méthode des rectangles**, ★ convergence absolue | `series` §1-6 | 🔶 ⚠️ | Un bandeau faux dit les séries hors programme. La comparaison série-intégrale manque. CSSA, d'Alembert et semi-convergence relèvent de la PT. |
| ★ Fonctions de deux variables | ouverts, dérivées partielles, gradient, règle de la chaîne, points critiques | aucun en 1ʳᵉ année | ❌ | Traité en 2ᵉ année (`fpv`). |

## 2. Manques importants, classés selon leur poids aux concours PT

1. **Changement de base, matrices semblables, symétries.** C'est la base de la réduction, sujet n° 1 des écrits PT. Ces notions sont absentes de `applin`, `matrices` et `ev` ; seuls `matrices2a` et `projsym` (2ᵉ année) les traitent.
2. **Comparaison série-intégrale (méthode des rectangles).** Elle est exigible en PTSI. Le site l'omet et la dit même « hors programme strict » (`series` EXO 03 Q4, méthodes « Réflexe 5 »).
3. **Intégration sur un segment.** Manquent la définition par les fonctions en escalier, l'inégalité de Taylor-Lagrange, les méthodes des rectangles et des trapèzes, et l'intégrale à valeurs complexes. Seul `integ2a` (2ᵉ année) les donne : un élève de 1ʳᵉ année ne les voit pas.
4. **Dimension finie et applications linéaires.** Manquent le rang d'une famille, la base adaptée, la forme géométrique du théorème du rang, rg(v∘u) ≤ min, les équations linéaires u(x) = a et la dimension des espaces de solutions.
5. **Géométrie du plan.** Droites (paramétrage, équation, vecteur normal), cercles, produit mixte dans le plan, coordonnées polaires, distance à une droite. C'est le seul bloc du programme absent du site entier. Il est indispensable pour `courbes`, `coniques` et `geoplane`.
6. **Dérivabilité.** Théorème de la limite de la dérivée, classe Cᵏ, formule de Leibniz (absente de toute la 1ʳᵉ année), formule de Taylor polynomiale.
7. **Outils de calcul du 1ᵉʳ semestre.** Inégalités et inéquations, valeur absolue, partie entière, sommes doubles, aⁿ−bⁿ, fonction tangente et tan(a±b), eˣ ≥ 1+x, ln(1+x) ≤ x, fonctions à valeurs complexes.
8. **Probabilités.** Loi uniforme, loi conditionnelle, indépendance mutuelle (« deux à deux » ne suffit pas), lemme des coalitions, somme de Bernoulli indépendantes de loi B(n, p) démontrée.
9. **Arithmétique des entiers.** Division euclidienne, PGCD, PPCM, Euclide, nombres premiers. Peu présente aux écrits PT, mais au programme et utile en informatique.

## 3. Hors-programme présenté comme exigible, et doublons

### Hors-programme présenté comme exigible
- **`contderiv`** : §4 « Fonctions convexes, inégalité de Jensen » (au programme ni de PTSI ni de PT), continuité uniforme et théorème de Heine (§1), cartes 13-19, et l'exercice « Concours PT » « TVI et inégalité de convexité ». `dl` §3 et sa carte 16 parlent aussi de convexité.
- **`det`** :
  - le §1 définit le déterminant par récurrence (mineurs et cofacteurs) et le présente comme « multilinéaire alternée » ;
  - le §4 donne la comatrice et la règle de Cramer, ainsi que les cartes 10-12 et les EXO 04-05.
  - Le programme les déclare explicitement hors programme, et `det2a` les range justement en « Pour aller plus loin » : les deux années se contredisent.
- **`polynomes`** : §2 PGCD, Bézout et lemme de Gauss dans K[X] ; §3 et méthode 5 : fonctions symétriques s₁, s₂, s₃ (« hors programme » d'après le texte officiel).
- **`fonctions`** : méthode 4 avec th, Argsh, Argch, et la carte 19 « arcsinh ». Le programme ne retient que ch, sh et ch² − sh² = 1.
- **`proba` et `va`** :
  - `proba` §2 : espace (Ω, 𝒜, P) σ-additif ; `va` §1 : variable « à image dénombrable » et fonction de répartition ;
  - lois géométrique et de Poisson avec l'approximation binomiale (`proba` §4, `va` §3, méthodes) ;
  - loi hypergéométrique (`denombrmt` §4) ; formule du crible à 3 ensembles (carte 20 de `denombrmt`). Tout cela relève de la 2ᵉ année ou en sort.
- **`series`** : la règle de d'Alembert (§5), le critère spécial des séries alternées (CSSA) et la semi-convergence (§6) sont exposés comme du cours. La semi-convergence est explicitement hors programme en PTSI ; ces trois points sont au programme de PT (`series2a`).
- **Plus bref** : relations d'équivalence et d'ordre (`logique` §2), Stirling « hors programme mais à connaître » (`asympt` §3), similitudes (`complexes`, méthode 7), « identité de Jacobi » (`geometrie`, carte 19).
- **Cas inverse** : du programme est présenté comme hors programme. C'est le bandeau des séries et la comparaison série-intégrale (voir §2).

### Doublons
- **`proba`, `denombrmt` et `va` se recouvrent en triple.**
  - Le dénombrement est traité deux fois (`proba` §1 et `denombrmt` §1-3), ainsi que les lois usuelles (`proba` §4 et `va` §3) et l'espérance et la variance (`proba` §3 et `va` §2).
  - Markov et Bienaymé-Tchebychev apparaissent dans les deux chapitres de probabilités.
  - Les notations diffèrent : 𝔼[X], Var et C_n^p dans `proba`, E(X) et V(X) dans `va` ; binôme écrit aᵏbⁿ⁻ᵏ dans l'un, aⁿ⁻ᵏbᵏ dans l'autre.
  - `proba` s'intitule « Probabilités & dénombrement » alors que `denombrmt` existe.
- **`contderiv` §3 et `dl` §1-3** répètent la dérivée, les règles de calcul, Rolle, le TAF, l'IAF et la convexité. **`dl` §4-6 et `asympt` §2** répètent la définition des DL, les DL usuels et les opérations, en se contredisant (voir §4).
- **Projecteurs** : `ev` §4, `applin` §6 et `projsym` (2ᵉ année).
- **Une 1ʳᵉ année mince doublée par une 2ᵉ année qui la contient.**
  - `det` (3 552 signes) face à `det2a` (38 866) ; `geometrie` (4 214) face à `geo3d` (36 907), dont l'encadré dit « tout est acquis en PTSI ».
  - Il en va de même pour `integrales` face à `integ2a`, et `suites` face à `suites2a`.
  - La version complète du contenu de 1ʳᵉ année n'est visible qu'en 2ᵉ année : en 1ʳᵉ année, la navigation ne montre que les fiches courtes.
- **`det`** : l'EXO 03 et l'exercice « Concours PT » portent sur la même matrice (1,1,1 / 1,2,m / 1,4,m²) avec les mêmes questions.

## 4. Qualité

### Chapitres minces
- Cours de 1ʳᵉ année : de 3 274 à 16 070 signes (médiane ≈ 5 600). Cours de 2ᵉ année : de 18 764 à 50 798.
- Aucun encadré « Au programme · PTSI », 0 à 2 figures par chapitre, presque aucun exemple traité hors `matrices`, `applin`, `primitives` et `integrales`.
- Les plus minces : `fonctions` 3 274, `logique` 3 418, `det` 3 552, `denombrmt` 3 673, `va` 3 919, `geometrie` 4 214, puis `proba` 5 349 et `ev` 5 371.
- Méthodes réduites à des listes sans exemple : `logique` (3), `denombrmt`, `va`, `det` et `geometrie` (4 chacun).
- Chaque chapitre a 7 exercices, tous corrigés, dont un « Concours PT ». Ces derniers sont courts (2 à 4 questions) : à étoffer.

### Erreurs repérées en passant
- **`asympt` méthode 2 et carte 20** : « e^{sin x} = 1 + x + x²/2 + x³/3 + o(x³) » est faux, le coefficient de x³ est nul. Le DL de e^u est tronqué sans u³/6, et un terme « + x³/2 » sort de nulle part.
- **`fonctions` méthode 2** : « sin(πk/6) = √k/2 pour k = 0…4 » est faux (pour k = 2, sin(π/3) = √3/2). La mnémonique porte sur les angles 0, π/6, π/4, π/3, π/2.
- **Bandeau de `series`** : « Les séries numériques ne sont pas au programme de PTSI 1ʳᵉ année » est faux. Elles occupent une section du 2ᵉ semestre (convergence, termes positifs, Riemann, rectangles, convergence absolue).
- **`det` EXO 03 Q3** : correction bâclée (« L₃ = 2L₂ − L₁ (vérification … ≠ …). Recalculons … En fait … ») qui ne conclut pas. La relation est L₃ = 3L₂ − 2L₁ (les colonnes 2 et 3 sont égales).
- **`asympt` §2** : « Les coefficients sont uniques : a_k = f^(k)(a)/k! » est faux sans hypothèse Cᵏ et contredit `dl` §4. La phrase « Dérivation : dériver terme à terme (perd un ordre) », donnée sans réserve, contredit `dl` §6.
- **`asympt`, pièges** :
  - « x ∼ x et x² ∼ x² mais x + x² ≁ 2x (le terme dominant est x²) » n'illustre rien, et c'est faux en 0, où x + x² ∼ x.
  - §4 « Branche parabolique : si a = 0 mais f(x)/√x → ℓ » est un critère inventé.
- **`contderiv` §1** : « Une limite en a existe ssi ℓ⁻ = ℓ⁺ » est faux si a ∈ I : il faut aussi f(a), selon la convention du programme.
- **`va` méthode 3** : l'approximation de Poisson serait « plus précise que la binomiale ». C'est absurde : la binomiale est la loi exacte.
- **`polynomes`** :
  - La méthode 4 décrit mal la forme de la DES : « un terme par facteur, numérateur de degré ≤ multiplicité − 1 ».
  - L'exemple du §4 mélange l'indéterminée et la variable d'intégration : « ∫ 1/(X²−1) dx = ½ ln|X−1| … ».
- **Cartes fautives** :
  - `logique` 14 : De Morgan, réponse brouillon « → non : … Correct : » ;
  - `det` 23 : « a₁₁(e₂₂e₃₃ − e₂₃e₃₂) − a₁₂(…) », lettres mélangées et « (…) » en guise de termes ;
  - `geometrie` 19 : le double produit vectoriel est appelé « identité de Jacobi » ;
  - `fonctions` 23 : φ = arctan(b/a), faux si a < 0 ;
  - `fonctions` 24 : la lettre k désigne à la fois la valeur et l'entier.
- **Coquilles** : « La tangeante » (`fonctions`), « C'est l'algèbrement clos » (`complexes`).

### Notations incohérentes, entre chapitres de 1ʳᵉ année et avec la 2ᵉ année
| Notion | Une forme… | …l'autre forme |
|---|---|---|
| Espérance, variance | 𝔼[X], Var(X) (`proba`) | E(X), V(X) (`va`, `vadisc1-2`) |
| Coefficient binomial | C_n^p (`proba`) | \(\binom{n}{p}\) |
| Fonctions hyperboliques | cosh, sinh (`dl`, cartes `fonctions`) | ch, sh (`fonctions` méth., `primitives`, 2ᵉ année) |
| Transposée | A^T (`det`) | A^⊤ (`matrices`, 2ᵉ année) |
| Rang | rang(A) (`det`, `ev`) | rg (`applin`, 2ᵉ année) |
| Vecteurs d'un espace vectoriel abstrait | fléchés \vec{u} (`ev`) | lettres nues (`applin`, `ev2a`) |
| Bornes atteintes | « théorème de Weierstrass / des valeurs extrêmes » (`contderiv`, `fonctions`) | « bornes atteintes » (programme, `fpv`) |
| Intervalle ouvert | (−π/2, π/2) pour Arctan | ]−π/2, π/2[ |
| Amortissement | ζ (`edo` §3) | ξ (sciences de l'ingénieur du site) |
| Définition des limites | inégalités strictes (`contderiv`) | inégalités larges (programme, `suites`) |

## 5. Recommandations, par priorité

1. **Corriger les erreurs du §4** : e^{sin x} dans la méthode et dans la carte, mnémonique du sinus, bandeau des séries, `det` EXO 03, `asympt` §2, §4 et pièges, `contderiv` §1, Poisson, DES, cartes fautives, coquilles. *Ampleur : petite.* Les retouches de texte d'une carte à rang inchangé ne font pas perdre la progression.
2. **Séries** : retirer le bandeau, ajouter la comparaison série-intégrale par la méthode des rectangles (cours, méthode, exercice). Passer d'Alembert, le CSSA et la semi-convergence en « Pour aller plus loin », avec renvoi à `series2a`. *Ampleur : petite à moyenne.*
3. **Réécrire les cours de 1ʳᵉ année au format de la 2ᵉ année** : encadré « AU PROGRAMME · PTSI », démonstrations, exemples traités, hors-programme en fin de chapitre. Ordre conseillé :
   - `applin` et `matrices` : symétries, changement de base, matrices semblables, équations linéaires ;
   - `integrales` : fonctions en escalier, Taylor-Lagrange, rectangles et trapèzes, cas complexe ;
   - `ev` : dimension finie complète ;
   - `contderiv`, `dl` et `asympt` : supprimer les doublons, ajouter limite de la dérivée, Cᵏ et Leibniz ;
   - `polynomes` et `fonctions`.

   *Ampleur : grande.*
4. **Géométrie** : créer la géométrie du plan, absente du site (repérage et polaires, produits scalaire et mixte, droites, projeté, cercles). Pour le doublon `geometrie` / `geo3d`, deux options :
   - soit passer `geo3d` en 1ʳᵉ année (le retirer de `__YEAR2A`, puisqu'il se dit « acquis de PTSI ») et réduire `geometrie` au plan ;
   - soit réécrire `geometrie` en « plan + espace ».

   *Ampleur : moyenne.*
5. **Restructurer les probabilités** en trois chapitres sans recouvrement :
   - `denombrmt` : le dénombrement seul ;
   - `proba` : univers fini, conditionnement, indépendance mutuelle, coalitions ;
   - `va` : lois U, B, binomiale et conditionnelles, couples, espérance et variance, Bienaymé-Tchebychev appliqué à une moyenne.

   Renvoyer σ-additivité, Poisson et géométrique en « Pour aller plus loin » (avec lien vers `espproba` et `vadisc1`) et adopter une seule notation, E(X) et V(X). *Ampleur : moyenne.* Retoucher les cartes sur place plutôt que de les déplacer d'un deck à l'autre, pour garder la progression.
6. **`det`** : aligner sur `det2a` (caractérisation, opérations sur les colonnes, déterminant d'une famille et d'un endomorphisme, lien avec le produit mixte). Passer la comatrice et Cramer en hors-programme et remplacer l'exercice « Concours PT », doublon de l'EXO 03. *Ampleur : petite à moyenne.*
7. **Combler les outils du 1ᵉʳ semestre** :
   - un chapitre « Calculs algébriques et arithmétique » : sommes et produits, sommes doubles, inégalités, valeur absolue, partie entière, division euclidienne, PGCD et PPCM, Euclide, nombres premiers. Ajouter un chapitre touche les 5 endroits listés dans `CLAUDE.md` ;
   - compléter `fonctions` : tangente, inégalités usuelles, transformations du graphe, fonctions à valeurs complexes.

   *Ampleur : moyenne.*
8. **Harmoniser les notations** selon le tableau du §4, sur celles de la 2ᵉ année et du programme. Retirer ou renvoyer en fin de chapitre le hors-programme de `contderiv` (convexité, Heine), `polynomes` (PGCD, Bézout, fonctions symétriques) et `fonctions` (th, Argsh). *Ampleur : petite.*
