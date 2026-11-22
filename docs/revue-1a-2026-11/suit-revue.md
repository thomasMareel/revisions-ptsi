# Chapitre `suites` (prefix `suit`) — « Suites numériques » — compte rendu

Rédigé le 2026-11-22 (point 4 de l'audit, lot 8 ; `docs/audit-2026-11/maths-1a.md` lignes « Sommes et produits » et
« Réels et suites »). Le cours d'origine (≈ 15 100 car., 6 sections, sans encadré « Au programme », sommes éparpillées
au §4) est **réécrit en entier** au format de la 1ʳᵉ année ; méthodes refaites (10), exercices complétés (11 +
Concours) ; cartes relues, 1 complétée, 15 ajoutées. L'onglet Simulateur (`drawSuite`, toile d'araignée) n'est pas
touché ; le cours y renvoie (§10, EXO 04).

## Fichiers
- `suit-cours.src.html` (≈ 86 000 car. dont ≈ 33 000 de figures) : `suit_construire.py` assemble `suit-cours.tpl.html`
  et `suit_figs.json` (`suit_figs.py`, outil `cpx_svg.py`). Retouches : `suit_retouches1.py`, `suit_retouches2.py`.
  Code Python affiché (§11) : `suit_code.py`, exécuté tel quel.
- `suit-meth.src.html` (10 méthodes) ; `suit-exos.src.html` produit par `suit_finir_exos.py` (= `suit_assembler_exos.py` :
  EXO 01-06 d'origine corrigés, EXO 04 refait dans `suit_exo04.html`, nouveaux dans `suit_exos_nouveaux.html` ; puis
  `calc_enbloc.py` avec `suit_enbloc.txt`) ; code du Concours : `suit_code_exos.py`.
- `suit-cartes-corr.json` (1 carte), `suit-cartes-ajout.js` (15 cartes, 44 → 59).
- Contrôles : `suit_calculs.py` (46 vérifications du cours, sorties Python comprises), `suit_calculs_meth.py` (16),
  `suit_calculs_exos.py` (42, anciens exercices compris) : toutes justes. Cartes : `cpx_cartes_rendu.py` (0 erreur
  MathJax). `verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`,
  `larges` vides, aucune erreur JS, pas de débordement ; figures regardées en clair et en sombre (`suit_voir.py`).
  Copies d'origine : `suit_orig_cours.html`, `suit_orig_meth.html`, `suit_orig_exos.html`.

## Erreurs corrigées
- **EXO 01 Q4** (\(n!/n^n\)) : énoncé confus (« \(n! \le n \cdot n \cdots n/2\) ») et corrigé faux et circulaire
  (« \(x_n \le (1/n)^{n-1}\) » : faux dès \(n = 3\), \(x_3 = \frac{6}{27} \gt \frac19\)). Remplacé par l'encadrement
  \(0 \lt x_n \le \frac1n\) (produit de facteurs \(\frac kn \le 1\)).
- **EXO 04** : avec \(u_0 = 2\), la suite était constante (corrigé qui s'en apercevait en cours de route). Refait :
  étude complète de \(u_{n+1} = \sqrt{u_n + 2}\) selon \(u_0\) (constante, croissante, décroissante), même titre.
- **EXO 06** (suites adjacentes vers \(e\)) : « hors PTSI ou en exercice » et « cette démonstration justifie aussi que
  \(e\) est irrationnel » (inexact : il faut un argument de plus) reformulés ; renvoi à la série exponentielle.
- **Concours d'origine** : même suite que l'EXO 04 (et que l'exemple du cours §10) avec 3 questions ; son contenu est
  repris par l'EXO 04, et un nouveau Concours le remplace (voir plus bas).
- Cours d'origine : sommes arithmétiques et géométriques détaillées (§4) et méthode 7 « sommes classiques » : renvoyées
  au chapitre `calculs` (§2, §3), où elles vivent désormais ; propriété de la borne supérieure, caractérisation des
  intervalles, approximations décimales, \(\ell \gt 0 \Rightarrow u_n \gt 0\), suites complexes géométriques et
  arithmético-géométriques à coefficients complexes, récurrences d'ordre 2 à coefficients complexes, vitesse de
  convergence : absents, ajoutés.
- **Carte 1** (modes de définition) : il manquait la définition implicite, citée par le programme — réponse complétée,
  question inchangée. Les autres cartes sont justes ; les cartes 41 à 43 (sommes) sont gardées (aucun retrait).

## Couverture du programme (avant → après)
| Capacité du programme de PTSI (« Nombres réels et suites numériques ») | Avant | Après |
|---|---|---|
| a) Borne supérieure, inférieure, propriété de la borne supérieure, sup X = +∞ ; caractérisation des intervalles | absent | §1 + figure, méth. 1, EXO 07, 3 cartes |
| b) Majorée, minorée, bornée (⟺ \|uₙ\| majorée), stationnaire, monotone ; explicite, implicite, récurrence | §1 (sans implicite) | §2, méth. 2, Concours A, carte 1 corrigée |
| c) Limite (inégalités larges), unicité, convergente ⇒ bornée, ℓ > 0 ⇒ uₙ > 0 APCR | §2 (sans démonstrations ni signe) | §3 + figure (bande ε, rang N), démonstrations, méth. 3, carte |
| c) Opérations, bornée × limite nulle, passage à la limite d'une inégalité large | §2 | §4 (démonstrations, \((1 + 1/n)^n \to e\)), méth. 4, EXO 01, cartes |
| c) Encadrement, \|uₙ − ℓ\| ≤ vₙ, minoration, majoration | §3 | §5, méth. 3, EXO 08 |
| d) Limite monotone, suites adjacentes ; approximations décimales, réels limites de rationnels | §3 (sans approximations) | §6 + figure, démonstrations, méth. 5, EXO 06, 11, Concours B, cartes |
| e) Suites extraites (divergence ; u₂ₙ et u₂ₙ₊₁ → ℓ ⇒ uₙ → ℓ) ; Bolzano-Weierstrass hors programme | §6 (sans la réciproque pair/impair) | §7 (démonstrations), méth. 6, EXO 09, carte ; BW en fin de cours |
| f) Suites complexes, caractérisation par Re et Im | §6 (une ligne) | §7, EXO 09 Q2-Q3, carte |
| g) Arithmétiques, géométriques (qⁿ, q complexe), arithmético-géométriques (a ∈ ℂ∖{1}, b ∈ ℂ) | §4 (réel seulement) | §8 (démonstration de qⁿ), méth. 7, EXO 02, 09, cartes |
| g) Récurrentes linéaires d'ordre 2 à coefficients constants | §4 (réel, sans démonstration) | §9 + figure, démonstration, méth. 8, EXO 03, 10, carte |
| g) uₙ₊₁ = f(uₙ) : intervalle stable, représentation, point fixe, monotonie (signe de f(x) − x, croissance de f) | §5 | §10 + 2 figures (escalier, escargot), méth. 9, EXO 04, 05, cartes |
| Vitesse de convergence (lente, géométrique, quadratique, nombre d'itérations) ; calcul de termes et seuil en Python | absent | §11 + figure (erreur en échelle log), code testé, méth. 10, EXO 11 Q4, Concours C-D, cartes |

## Cours (11 sections, 7 figures calculées)
Bloc « AU PROGRAMME · PTSI » ; §1 Borne supérieure et intervalles (figure : \(\{1 - 1/n\}\), majorants) ; §2 Généralités
(suite implicite \(x^n + x = 1\), monotonie de \(2^n/n!\)) ; §3 Limite (figure : bande \(\ell \pm \varepsilon\), rang \(N\) ;
unicité, bornée, signe démontrés) ; §4 Opérations et inégalités (quatre formes indéterminées, \((1 + 1/n)^n \to e\)) ;
§5 Encadrement (\(\sum n/(n^2 + k)\), \(\lfloor nx \rfloor/n\), \(\sum 1/\sqrt k\)) ; §6 Monotones et adjacentes (figure :
sommes alternées \(S_{2n}\), \(S_{2n+1}\) ; \(\sum 1/k^2 \lt 2\) ; approximations décimales) ; §7 Suites extraites et complexes ;
§8 Arithmétiques, géométriques, arithmético-géométriques (limite de \(q^n\) démontrée, dose de médicament → 500 mg en
13 prises, suite \(u_{n+1} = iu_n + 1\) de période 4) ; §9 Récurrences d'ordre 2 (figure : oscillation amortie ; trois cas,
Fibonacci, lien avec les équations différentielles) ; §10 \(u_{n+1} = f(u_n)\) (figures : escalier \(\sqrt{2 + x}\),
escargot \(1/(1 + x)\) ; plan d'étude ; majoration par l'IAF avec renvoi à `contderiv` §9) ; §11 Vitesse de convergence et
calcul numérique (figure : trois vitesses ; fonctions Python `termes` et `seuil`) ; Pour aller plus loin
(Bolzano-Weierstrass, Cesàro). Un exemple traité chiffré et une « Erreur classique » par section ; 10 démonstrations
dépliables.

## Méthodes (10)
Borne supérieure ; sens de variation ; majorer \(|u_n - \ell|\) (rang \(N\)) ; lever une indétermination ; convergence
sans la limite (monotone, adjacentes) ; divergence par suites extraites ; arithmético-géométrique ; ordre 2 ; plan
d'étude de \(u_{n+1} = f(u_n)\) ; nombre d'itérations et seuil en Python. Les méthodes d'origine sont reprises
(reformulées) ; « sommes classiques » renvoyée à `calculs` ; trois encadrés « Piège ».

## Exercices (12)
EXO 01-03, 05-06 d'origine gardés (01 Q4 et 06 corrigés, formules trop larges passées en bloc) ; EXO 04 refait.
Nouveaux : 07 bornes supérieures et approximations décimales ; 08 trois encadrements (\(\frac{1}{n^2}\sum\lfloor kx \rfloor\),
\(\sum 1/\sqrt{n^2 + k}\), \((2^n + 3^n)^{1/n}\)) ; 09 suites extraites et complexes (arithmético-géométrique de raison \(\frac i2\)) ;
10 ordre 2 (période 6, racine double, instabilité numérique d'une récurrence exacte, constatée en Python) ; 11 constante
d'Euler par suites adjacentes, \(H_n \gt 10\) pour \(n = 12\,367\). Concours PT nouveau, en 4 parties : suite définie
implicitement par \(x_n^n + x_n = 1\) (existence, croissance, limite 1 par l'absurde, dichotomie en Python, convergence
lente : \(n(1 - x_n)\) non majorée).

## Cartes
Correction (réponse seule) : carte 1. Ajouts (15, à la fin, formules en `\\( … \\)`) : borne supérieure, caractérisation
par \(\varepsilon\), intervalles, signe d'une suite de limite \(\ell \gt 0\), bornée × limite nulle, passage à la limite d'une
inégalité stricte, approximations décimales, \(u_{2n}\) et \(u_{2n+1}\), \(q^n\) complexe, ordre 2 complexe, intervalle stable,
signe de \(f(x) - x\), majoration par l'IAF, vitesses géométrique et quadratique, seuil en Python.
`corriger_cartes.py --essai` : 1 réponse corrigée ; `ajouter_cartes.py --essai` : 44 → 59.

## Notations
\(\sup\), \(\inf\), \(u_n \to \ell\), \(\lim u_n\), constantes \(\lambda\), \(\mu\) des récurrences d'ordre 2 et équation
caractéristique \(r^2 = ar + b\) (comme `suites2a` §7 et `edo`), point fixe \(\ell\), intervalle stable \(J\), erreur
\(e_n = |u_n - \ell|\), \(\lfloor x \rfloor\) (comme `calculs`), \(\operatorname{Re}\), \(\operatorname{Im}\).

## Renvois
Aucun renvoi numéroté vers ce chapitre dans le site (les renvois de `calculs`, `contderiv`, `suites2a` ne citent pas de §).
Le cours renvoie à `calculs` §2, §3, §6, `fonctions` §7, `contderiv` §4 et §9, `asympt` §8, `edo` §6-7, `pynum` §3,
`suites2a` §6.

## Doutes
- La vitesse de convergence est citée dans le bandeau de la section « Limites, continuité, dérivabilité » du programme
  de PTSI (« occasion d'introduire ») et non comme capacité détaillée : traitée au §11 sur des exemples, l'étude générale
  (Newton, ordre) restant dans `suites2a` §6 et `pynum` §3.
- `suites2a` (2ᵉ année) reprend une partie de ce chapitre (adjacentes vers \(e\), récurrences) : les exemples du cours de
  1ʳᵉ année ont été choisis différents pour éviter les doublons ; l'EXO 06 d'origine (vers \(e\)) recoupe l'exemple du §1 de
  `suites2a`, gardé parce qu'il est juste.
- Les limites \(\frac{\pi^2}{6}\) et \(\ln 2\) des exemples du §6 sont données comme résultats admis.
