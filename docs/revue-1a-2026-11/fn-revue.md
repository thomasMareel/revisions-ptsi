# Chapitre `fonctions` (prefix `fn`) — « Fonctions réelles — généralités » — compte rendu

Rédigé le 2026-11-21 (point 4 de l'audit, `docs/audit-2026-11/maths-1a.md` §2 point 7, §3, §5 points 7 et 8).
Le cours d'origine (3 274 signes, 4 sections, aucun encadré « Au programme ») est **réécrit en entier** au format de la
1ʳᵉ année ; méthodes et exercices complétés ; cartes relues, une corrigée, 15 ajoutées.

## Fichiers
- `fn-cours.src.html` (≈ 102 000 car. dont ≈ 50 000 de figures) : `fn_construire.py` assemble `fn-cours.tpl.html` et
  `fn_figs.json` (`fn_figs.py`, outil commun `calc_svg.py`). Retouches scriptées : `fn_retouches1.py`, `fn_retouches2.py`,
  `fn_retouches_figs.py` ; formules passées en bloc par `calc_enbloc.py`.
- `fn-meth.src.html` (10 méthodes), `fn-exos.src.html` (11 exercices + « Concours PT »), `fn-cartes-corr.json` (1 carte),
  `fn-cartes-ajout.js` (15 cartes, 25 → 40).
- Contrôles : `fn_calculs.py` (152 vérifications sympy / numériques, toutes justes, y compris les anciens exercices),
  `calc_cartes_rendu.py` (formules des cartes : 0 erreur MathJax), `calc_larges.js`, `fn_voir.py` (figures en clair et
  en sombre). Copies des panneaux d'origine : `fn_orig_cours.html`, `fn_orig_meth.html`, `fn_orig_exos.html`,
  `fn_cartes_orig.txt`.

## Erreurs et hors-programme corrigés
- **th, Argsh, Argch présentés comme méthode** (méthode 4 d'origine) : la méthode « fonctions hyperboliques » ne garde
  que ch, sh, leurs dérivées et ch² − sh² = 1 (seule formule exigible d'après le programme) ; th, Argsh, Argch passent en
  « Pour aller plus loin · hors programme » en fin de cours, avec un piège qui le rappelle.
- **EXO 05 Q3** demandait la formule de la réciproque de sh (Argsh, hors programme) : remplacée par la résolution de
  sh x = 2 (u = eˣ), la formule d'Argsh n'étant plus qu'une remarque « pour aller plus loin ».
- **EXO 06 Q2-Q3** : le maximum de a cos x + b sin x était cherché en x₀ = arctan(b/a) « si a > 0 », puis φ = arctan(b/a)
  donné en général (faux si a < 0). Questions réordonnées : écriture R cos(x − φ) avec cos φ = a/R, sin φ = b/R, puis
  maximum √(a² + b²) atteint en φ ; application à 3 cos x − 4 sin x.
- **EXO 03 Q2** : « f est constante sur ℝ⁺ » → sur l'intervalle ]0, +∞[ (1/x n'est pas défini en 0), avec la remarque que
  la constante vaut −π/2 pour x < 0.
- **Carte 19** (Argsh) : réponse préfixée « Hors programme en PTSI : » (convention des chapitres de 1ʳᵉ année) — seule
  la réponse change. Les autres cartes sont justes (la mnémonique du sinus et la carte 23 avaient déjà été corrigées) ;
  aucune carte fausse des deux côtés.
- Coquille « tangeante » de l'audit : absente de la version actuelle.

## Couverture du programme (avant → après)
| Capacité du programme de PTSI | Avant | Après |
|---|---|---|
| Ensemble de définition, graphe, transformations f(x + a), f(ax), λf + b | absent | §1 + figure, méth. 7, EXO 01 Q4, carte |
| Parité, périodicité, réduction du domaine | §1 (définitions) | §2 (interprétation, réduction, exemple), EXO 01 |
| Monotonie, composée, bornée ⟺ \|f\| majorée | §2 (partiel) | §3, carte |
| Dérivation : rappels, tableau de variations, inégalités, C¹, dérivées successives | absent | §4 (tableau des dérivées usuelles), méth. 1 et 6 |
| Exemples simples de dérivées partielles | absent | §4, EXO 11 Q1-Q2 |
| Réciproque : graphe, dérivée, interprétation | absent | §5 + figure, méth. 5, EXO 10, Concours A3, carte |
| exp, ln, puissances (définies sur ]0, +∞[, prolongement), log₁₀, log₂, règles | §3 (bref, sans log₁₀ ni log₂) | §6 + figure, EXO 07, cartes |
| Croissances comparées ; eˣ ≥ 1 + x, ln(1 + x) ≤ x | croissances seules | §7 + figure (démonstrations), méth. 6, EXO 09, Concours C, cartes |
| Cercle, congruence mod 2π, π ± x, π/2 ± x, formules (justification géométrique), \|sin x\| ≤ \|x\|, équations | §3 (formules) | §8 + figure, méth. 2-3, EXO 02, EXO 09 Q4, cartes |
| Fonction tangente, tan(π ± x), angles usuels, tan(a ± b) | absent | §9 + figure, méth. 8, EXO 08, cartes |
| Arcsin, Arccos, Arctan : dérivées, variations, graphes | §4 (sans dérivées) | §10 + figure, méth. 8, EXO 03, EXO 10, cartes |
| ch, sh (seule formule ch² − sh² = 1) ; th et réciproques hors programme | méthode avec th, Argsh, Argch | §11 + figure, méth. 9, EXO 05, Concours B3 ; HP en fin |
| Fonctions à valeurs complexes, dérivée de exp(φ) | absent | §12, méth. 10, EXO 11 Q3-Q4, carte |

## Cours (12 sections, 8 figures calculées)
Bloc « AU PROGRAMME · PTSI » ; §1 Définition, graphe et transformations (figure : sin(x + π/2), sin 2x) ; §2 Parité,
périodicité, domaine d'étude ; §3 Monotonie et fonctions bornées ; §4 Dérivation : rappels et étude pratique (dérivées
partielles) ; §5 Fonction réciproque (figure : x² et √ avec tangentes de pentes 3 et 1/3) ; §6 Exponentielle,
logarithmes, puissances (figure : x^α) ; §7 Croissances comparées et inégalités usuelles (figure : exp, ln et leurs
tangentes) ; §8 Trigonométrie (figure : cercle avec cos, sin, tan et l'arc) ; §9 Tangente (figure) ; §10 Fonctions
circulaires réciproques (figure : trois graphes) ; §11 ch et sh (figure) ; §12 Fonctions à valeurs complexes ;
Pour aller plus loin (th, Argsh, Argch). 13 exemples traités chiffrés, une erreur classique par section, démonstrations
dépliables (transformations, composée, inégalités usuelles, croissances comparées, cos(a − b) par le produit scalaire,
|sin x| ≤ |x|, tan(a + b), dérivées des réciproques, ch² − sh² = 1). Les théorèmes de dérivation restent admis et
renvoient à « Continuité et dérivabilité » (§5, §7, §9, §12), comme le veut le programme.

## Méthodes (10)
Étudier une fonction (avec les croissances comparées) ; valeurs exactes ; équations et inéquations trigonométriques ;
a cos x + b sin x = R cos(x − φ) ; bijection et réciproque ; inégalité par étude de fonction ; graphe transformé ;
tangente et arctangentes ; ch et sh ; dérivation par l'exponentielle complexe. Les 5 méthodes d'origine sont gardées
(reformulées) ; l'ancienne liste « Pièges classiques » devient un encadré.

## Exercices (12)
EXO 01 à 06 d'origine gardés et corrigés (voir plus haut ; EXO 01 complété d'une question sur les graphes transformés,
quelques justifications ajoutées). Nouveaux : 07 logarithmes, puissances, croissances comparées (nombre de bits) ;
08 tangente (tan π/8, tan 2x = √3, tan x ≥ x, formule de Machin) ; 09 inégalités usuelles (encadrement de la somme des
inverses par ln, de e, cos x ≥ 1 − x²/2) ; 10 réciproques et dérivées (arctan((1 + x)/(1 − x)) − arctan x constante par
intervalle) ; 11 dérivées partielles et fonctions à valeurs complexes. Concours PT étoffé : parties A (A3 : dérivée de la
réciproque de deux façons), B (inéquation exponentielle, ch x = 5/4), C nouvelle (encadrement par eˣ ≥ 1 + x).

## Cartes
Correction : carte 19 (réponse). Ajouts (15, à la fin) : transformations du graphe, bornée ⟺ |f| majorée, dérivée d'une
réciproque, x^α, log₁₀ et log₂, croissances comparées, inégalités exp / ln, |sin x| ≤ |x|, cos et sin de π − x et
π/2 − x, dérivée de tan, tan(a ± b), tan des angles usuels, dérivées de arcsin / arccos / arctan, ch et sh (dérivées,
variations), dérivée de e^φ. `corriger_cartes.py --essai` : 1 réponse corrigée ; `ajouter_cartes.py --essai` : 25 → 40.

## Notations
\(\arcsin\), \(\arccos\), \(\arctan\) en minuscules (comme `cd`, `dl`, `asy` ; « notées aussi Arcsin… » dans le cours),
\(\operatorname{ch}\), \(\operatorname{sh}\), \(\log_{10}\), \(\log_2\), \(a \equiv b\ [2\pi]\), \(\mathcal C^1\),
\(\frac{\partial f}{\partial x}\).

## Doutes
- Le nom du chapitre « Fonctions réelles — généralités » ne dit plus tout (trigonométrie, fonctions usuelles, valeurs
  complexes) ; « Fonctions usuelles et trigonométrie » serait plus juste, mais d'autres cours y renvoient par ce nom :
  laissé à l'intégrateur.
- `cd` §12 traite aussi les fonctions à valeurs complexes (limites, IAF) : le §12 d'ici ne garde que le calcul
  pratique et y renvoie (pas de contradiction).
- Le renvoi « (§9, chapitre « Fonctions réelles — généralités ») » de `cd-cours` pour eˣ ≥ 1 + x désigne en fait le §9 de
  `cd` (monotonie) ; les inégalités sont ici au §7 : à vérifier par l'intégrateur.
