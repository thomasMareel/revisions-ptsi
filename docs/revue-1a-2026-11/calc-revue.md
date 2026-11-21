# Nouveau chapitre `calculs` (prefix `calc`) — « Calculs algébriques et arithmétique » — compte rendu

Rédigé le 2026-11-21 (point 4 de l'audit, `docs/audit-2026-11/maths-1a.md` §2 points 7 et 9, §5 point 7). Chapitre
de 1ʳᵉ année placé juste après `logique` (groupe « Logique » des maths), déjà présent vide dans `AN1/site/index.html`.

## Fichiers
- `calc-cours.src.html` (≈ 90 000 car. dont ≈ 37 000 de figures) : construit par `calc_construire.py` à partir de
  `calc-cours.tpl.html` et `calc_figs.json` (`calc_figs.py`, outil `calc_svg.py`, copie de `cd_svg.py`).
- `calc-meth.src.html` (10 méthodes), `calc-exos.src.html` (11 exercices + 1 « Concours PT »), `calc-cartes.js` (30 cartes).
- Contrôles : `calc_calculs.py` (225 vérifications sympy / énumérations exhaustives, toutes justes), `calc_cartes_rendu.py`
  (114 formules des cartes rendues, 0 erreur MathJax), `calc_larges.js` (formules en ligne plus larges que leur bloc à
  390 px), `calc_deborde.js`, `calc_bisect.js` (recherche d'un débordement), `calc_voir.py` (captures des figures),
  `calc_enbloc.py` + `calc_longues.py` (passage en bloc des formules trop larges), `calc_retouches1.py`.

## Couverture du programme (avant → après)
| Capacité du programme de PTSI | Avant (site) | Après |
|---|---|---|
| Σ, Π, famille finie, ensemble d'indices vide | éparpillé (`suites` §4, `denombrmt`) | §1, méth. 1, EXO 01, cartes |
| Changements d'indice, regroupements, télescopage (sommes et produits) | absent | §2, méth. 2-3, EXO 02, cartes |
| Σk, Σk², Σxᵏ | `suites` §4 (Σk, géométrique) | §3 (démonstrations), EXO 01, EXO 03 (Σk³), cartes |
| Factorisation de aⁿ − bⁿ | absent | §3, EXO 09, cartes |
| Sommes doubles, produit de deux sommes, sommes triangulaires | absent | §4 + figure, méth. 4, EXO 04, cartes |
| Factorielle, coefficients binomiaux (convention), binôme dans ℝ | `denombrmt` (combinatoire) | §5 (preuves algébriques, renvoi à `denombrmt`), méth. 5, EXO 05 |
| Ordre sur ℝ, compatibilité, intervalles, majorer sommes / produits / quotients, inéquations (tableaux de signes) | absent | §6, méth. 6 et 8, EXO 06, EXO 11 |
| Majorant, minorant, maximum, minimum | `fonctions` §2 (fonctions seulement) | §6 (parties de ℝ ; borne sup. renvoyée à `suites`) |
| Valeur absolue, inégalité triangulaire, \|x − a\| ≤ b sur la droite | absent | §7 + figure, méth. 7, EXO 06, cartes |
| Partie entière ⌊x⌋ | absent | §7 + figure, méth. 10, EXO 07, cartes |
| Divisibilité, diviseurs, multiples, division euclidienne | absent | §8 (preuve), EXO 08, EXO 10 |
| PGCD (plus grand diviseur commun), PPCM, algorithme d'Euclide | absent (un `gcd` dans un corrigé) | §9 + figure, méth. 9, EXO 08, Concours |
| Nombres premiers, infinité, décomposition (preuve HP), application PGCD/PPCM | absent | §10 + crible, EXO 09-10, cartes |

Hors programme (« toute étude systématique de l'arithmétique ») regroupé en fin de cours : Bézout (avec Euclide remonté
sur l'exemple du §9), Gauss, congruences, division euclidienne dans ℤ (convention de Python). Une carte HP, préfixée
« Hors programme en PTSI : ». Le programme place l'arithmétique dans ℕ : le cours s'y tient (l'audit disait « dans ℤ »).

## Sections du cours
Bloc « AU PROGRAMME · PTSI » ; §1 Les symboles Σ et Π ; §2 Changement d'indice et télescopage ; §3 Sommes usuelles et
factorisation de aⁿ − bⁿ ; §4 Sommes doubles ; §5 Coefficients binomiaux et formule du binôme ; §6 Inégalités et
inéquations (majorants, maximum) ; §7 Valeur absolue et partie entière ; §8 Divisibilité et division euclidienne ;
§9 PGCD, PPCM et algorithme d'Euclide ; §10 Nombres premiers et décomposition ; Pour aller plus loin.
17 exemples traités chiffrés, 11 blocs dépliables (démonstrations, rapidité d'Euclide), une erreur classique par section.
Figures calculées (classes du site, vérifiées en clair et en sombre) : escaliers de Gauss (2Σk = n(n+1)), triangle des
couples (i, j), droite réelle pour |x − a| ≤ b et |x + 1| > 2, graphe de ⌊x⌋ entre y = x − 1 et y = x, pavage
d'Euclide d'un rectangle 84 × 30, crible d'Ératosthène jusqu'à 100.

## Méthodes (10)
Sommes usuelles ; changement d'indice ; télescopage ; somme double ; binôme ; inéquation ; valeur absolue ; majorer
somme / produit / quotient ; PGCD et PPCM ; partie entière. Chacune avec un exemple éclair chiffré, 4 pièges.

## Exercices (12)
01 sommes et produits directs ; 02 télescopages (Π(1 − 1/k²), Σ k·k!) ; 03 somme des cubes ; 04 sommes doubles
(min(i, j), triangle) ; 05 binôme (coefficient, 2 ≤ (1 + 1/n)ⁿ < 3) ; 06 inéquations et valeurs absolues (dont
√(x + 5) > x − 1) ; 07 partie entière (Hermite pour n = 2, comptage, nombre de chiffres) ; 08 division euclidienne,
PGCD, PPCM ; 09 divisibilités par aⁿ − bⁿ (2ⁿ − 1 premier ⇒ n premier, 6 | n³ − n) ; 10 nombres premiers (n! + k,
premiers modulo 6) ; 11 encadrer des sommes (Σ1/k² ≤ 2, divergence de la série harmonique) ; Concours PT « Algorithme
d'Euclide et nombres de Fibonacci » (sommes télescopiques, pgcd de termes consécutifs, nombre de divisions, pire cas
de Lamé avec φ, fonction Python).

## Notations
\(\binom nk\) (comme `denombrmt`, avec \(a^k b^{n-k}\)), \(\lfloor x\rfloor\), \(\operatorname{pgcd}(a, b)\) et
\(\operatorname{ppcm}(a, b)\) (variantes \(a \wedge b\), \(a \vee b\) citées), \(b \mid a\), \(\mathbb N^*\) ; code Python
comme `pyanalyse` (`a % b`, variant b).

## Renvois
`logique` (récurrence), `matrices` (pivot, binôme matriciel), `fonctions` (trigonométrie, log₁₀), `denombrmt`
(combinatoire), `suites` (borne supérieure), `complexes` (aⁿ − bⁿ dans ℂ), `pyanalyse` (terminaison d'Euclide),
`pyrec` (version récursive), `pyfonc` (test de primalité).

## Doutes
- La section « Sommes et produits » existe aussi en morceaux dans `suites` §4 et `denombrmt` §7 : pas de conflit de
  notation, mais une légère redondance (voulue : ce chapitre est la référence des calculs).
- Le binôme est démontré ici par récurrence et dans `denombrmt` par dénombrement : les deux preuves sont au programme.
- L'intitulé « matiereLabel : Calculs » vient de `chapitres.py` (intégrateur).
