# Revue : `va` « Variables aléatoires » (prefix `va`), 1ʳᵉ année — 2026-11-21

Restructuration (audit `docs/audit-2026-11/maths-1a.md` §2 point 8, §3, §5 point 5) : ce chapitre porte désormais les
**variables aléatoires sur un univers fini** : lois (certaine, uniforme, Bernoulli, binomiale), loi conditionnelle,
couples et n-uplets, indépendance et lemme des coalitions, somme de Bernoulli indépendantes, espérance, variance,
covariance, Markov et Bienaymé-Tchebychev appliqués à une moyenne. Notations **E(X), V(X)** partout.

## Fichiers produits
- `va-cours.src.html` (≈ 64 000 car., bloc « AU PROGRAMME · PTSI », 11 sections, 14 exemples, 4 figures calculées et un
  tableau de loi conjointe, « Pour aller plus loin »), `va-cours.tpl.html`, `va_figs.py` / `va_figs.json`, `va_construire.py`.
- `va-meth.src.html` (10 méthodes), `va-exos.src.html` (11 exercices + « Concours PT » en 4 parties).
- `va-cartes-corr.json` (5 cartes), `va-cartes-ajout.js` (15 cartes).
- `va_calculs.py` (99 vérifications, dont énumérations exhaustives : min/max de deux dés, permutations, marche aléatoire,
  tirages sans remise, quatre dés).
- Anciens panneaux : `va_old-{cours,meth,exos}.html`.

## Erreurs et défauts corrigés
- **Hors-programme présenté comme exigible** : variable « à image dénombrable » et fonction de répartition (ancien §1),
  lois de Poisson et géométrique (ancien §3, méthodes 1 et 3, EXO 03 et 04, « sommes de Poisson ») → « Pour aller plus
  loin » avec renvois à `vadisc1`, `vadisc2`, `espproba` ; les deux exercices sont retirés (ils existent en 2ᵉ année).
- **Manques comblés** : loi uniforme \(\mathcal U(E)\), variable certaine, indicatrice ; \(f(X)\) et \(X \sim Y\) ;
  **loi conditionnelle** ; couples et n-uplets (marginales ne déterminent pas la conjointe) ; indépendance de variables
  (définition du programme et caractérisation démontrée), \(f(X) \perp\!\!\!\perp g(Y)\), **lemme des coalitions** ;
  **\(X_1 + \dots + X_n \sim \mathcal B(n, p)\) démontré** ; \(E(X) = \sum_\omega X(\omega)P(\{\omega\})\), positivité,
  croissance, inégalité triangulaire, \(E(\mathbf 1_A) = P(A)\), transfert pour les couples, \(E(XY) = E(X)E(Y)\) démontré ;
  variable centrée réduite ; variances de Bernoulli, binomiale, uniforme démontrées ; décorrélation ; variance d'une
  somme de n variables ; preuves de Markov et Bienaymé-Tchebychev ; **application à une moyenne et interprétation
  fréquentiste** (absente avant).
- **Ancienne méthode 3** : l'erreur « Poisson plus précise que la binomiale » (audit §4) avait déjà été rectifiée ; la
  méthode entière (hors programme) disparaît.
- **EXO 06 ancien** : « \(\bar X_n \to p\) en probabilité » (notion de 2ᵉ année) → énoncé non asymptotique, la limite
  étant signalée comme vue en 2ᵉ année.
- **Ancien « Concours PT »** (binomiale + transformation affine, doublon des EXO 01-02) → sujet original en quatre parties
  (marche aléatoire : loi de \(S_n\), retours à l'origine par indicatrices, covariance \(\operatorname{Cov}(S_m, S_n)\) par les
  coalitions, Bienaymé-Tchebychev sur la vitesse moyenne).
- **Cartes fausses ou imprécises** : 13 (« \(V(\sum \lambda_iX_i) = \sum \lambda_i^2V(X_i)\) » sans hypothèse) ; 16
  (\(\varepsilon \gt 0\) manquant) ; 17 (loi des grands nombres sans hypothèse, en convergence en probabilité, notion de
  2ᵉ année) ; 24 (« au plus 25 % des valeurs » : c'est une probabilité ; \(\mu\) non défini) ; 6 (C(n,k) → \(\binom nk\)).

## Couverture du programme (avant → après)
| Capacité (programme PTSI, Probabilités A d, f ; B a, b, c) | Avant | Après |
|---|---|---|
| Loi \(P_X\), distribution, \(X \sim Y\), \(f(X)\) | partiel, cadre dénombrable | §1 (deux exemples), méth. 1, cartes |
| Lois certaine, \(\mathcal U(E)\), \(\mathcal B(p)\), \(\mathcal B(n, p)\) | B(p), B(n,p) seules | §2, figure, méth. 2, cartes |
| Loi conditionnelle sachant un événement | absent | §3 (deux exemples), méth. 3, EXO 05, carte |
| Couples, loi conjointe, marginales, n-uplets | oui (bref) | §4, tableau min/max, méth. 4, EXO 06, carte |
| Variables indépendantes, caractérisation, n-uplets, \(f(X) \perp\!\!\!\perp g(Y)\), coalitions | définition seule | §5 (démos), méth. 7-8, EXO 07, 11, Concours C, cartes |
| Somme de Bernoulli indépendantes de loi \(\mathcal B(n, p)\) | énoncée en carte | §6 (démo), EXO 03-04, carte |
| Espérance, propriétés, transfert (couples), \(E(\mathbf 1_A)\), \(E(XY)\) indépendantes | partiel | §7 (démos), méth. 5, EXO 02, 09, cartes |
| Variance, écart type, \(V(aX+b)\), König-Huygens, centrée réduite, variances usuelles | partiel | §8 (démos), méth. 6, EXO 01, carte |
| Covariance, décorrélation, variance d'une somme | oui (bref) | §9 (min/max, contre-exemple), EXO 06-08, cartes |
| Markov, Bienaymé-Tchebychev, concentration | énoncés seuls | §10 (démos), figure, méth. 9, EXO 04, 09 |
| Application à une moyenne, interprétation fréquentiste | absent | §11, figure, méth. 10, EXO 10, Concours D, cartes |
| Hors programme : dénombrable, géométrique, Poisson, répartition, loi faible (limite) | présentés comme cours | « Pour aller plus loin » |

## Contenu
- **Sections** : §1 variable et loi (somme de deux dés, bâtons ; \(|S - 7|\)) ; §2 lois usuelles (bâtons de deux
  binomiales) ; §3 loi conditionnelle (pièce choisie au hasard : mélange non binomial) ; §4 couples (tableau min/max) ;
  §5 indépendance, coalitions ; §6 somme de Bernoulli (QCM) ; §7 espérance (points fixes par indicatrices) ; §8 variance ;
  §9 covariance (min/max, \(\operatorname{Cov} = 1\,225/1\,296\)) ; §10 Markov, Bienaymé-Tchebychev (figure \(\mathcal B(100, \frac12)\),
  0,057 contre 0,25) ; §11 moyenne et fréquence (figure probabilité exacte contre borne 25/n, taille d'un sondage).
- **Méthodes** : loi ; loi usuelle ; loi par cas ; loi conjointe ; espérance (indicatrices) ; variance ; indépendance ;
  coalitions ; Markov / Bienaymé-Tchebychev ; dimensionner un échantillon.
- **Exercices** : 01 dé (gardé) ; 02 maximum de deux dés ; 03 tirs (gardé) ; 04 QCM ; 05 dé puis pièces ; 06 loi
  conjointe (gardé + Q4) ; 07 décorrélation ; 08 sans remise (covariance négative) ; 09 points fixes (\(E = V = 1\)) ;
  10 Bienaymé-Tchebychev et fréquence (gardé, corrigé) ; 11 coalitions avec quatre dés ; Concours : marche aléatoire.
- **Cartes** : 25 → 40. Ajouts : \(\mathcal U(E)\), loi et \(X \sim Y\), loi conditionnelle, marginales, somme de Bernoulli,
  coalitions, indicatrice, \(E = np\) par linéarité, centrée réduite, variance d'une somme, Markov, moyenne, fréquence,
  Bernoulli décorrélées, tirages sans remise. Les cartes Poisson / géométrique (8-11, 19) restent, déjà préfixées
  « Hors programme ».

## Notations
\(E(X)\), \(V(X)\), \(\sigma(X)\), \(\operatorname{Cov}(X, Y)\), \(X \perp\!\!\!\perp Y\), \(\mathcal U(E)\), \(\mathcal B(p)\),
\(\mathcal B(n, p)\), \(\mathbf 1_A\), \(\overline X_n\), \(F_n\) : identiques à `vadisc1` et `vadisc2`.

## Doutes
- Le chapitre pourrait être renommé « Variables aléatoires sur un univers fini » (non fait : le nom est dans `CHAPTERS`).
- Quelques formules en bloc défilent au téléphone dans les encadrés étroits (prévu par le site), notamment les marginales et
  la variance d'une somme ; le tableau min/max (8 colonnes) défile aussi.
- La valeur « environ 1 100 personnes » du sondage (approximation normale) est citée comme hors programme.
