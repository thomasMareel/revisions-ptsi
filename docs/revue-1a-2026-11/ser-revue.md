# `series` (prefix `ser`) — compte rendu, 2026-11-21

Point 2 de l'audit `docs/audit-2026-11/maths-1a.md` (§2) et recommandation 2 (§5). La correction du 2026-11-15 avait déjà
remplacé le bandeau faux et ajouté une comparaison série-intégrale ; ce travail réécrit le cours au format de la 1ʳᵉ année et
termine la remise au programme (d'Alembert, séries alternées et semi-convergence sortis du cours exigible).

## Fichiers produits

| Fichier | Contenu |
|---|---|
| `ser-cours.src.html` | cours complet (61 698 car. ; 10 sections + « Pour aller plus loin », 15 exemples, 4 figures) — construit par `ser_construire.py` depuis `ser-cours.tpl.html` et `ser_figs.json` |
| `ser-meth.src.html` | 10 méthodes + encadré « Pour aller plus loin (2ᵉ année) » + pièges |
| `ser-exos.src.html` | 11 exercices + 1 « Concours PT » — construit par `ser_exos_construire.py` (EXO 01, 02, 04 repris du site ; le reste dans `ser_exos_ajout.html`) |
| `ser-cartes-corr.json` | vide (`[]`) : aucune carte fausse |
| `ser-cartes-ajout.js` | 14 cartes nouvelles (25 → 39) |
| Scripts | `ser_calculs.py` (cours), `ser_calculs_meth.py`, `ser_calculs_exos.py`, `ser_figs.py` (utilise `int_svg.py`), `ser_construire.py`, `ser_exos_construire.py` ; copies d'origine `ser_orig_{cours,meth,exos}.html`, `ser_sr2_cours.txt` |

## Erreurs et défauts corrigés

1. **Hors-programme présenté comme du cours** : la règle de d'Alembert (§5), le critère spécial des séries alternées et la
   semi-convergence (§6) restaient des sous-sections du cours, simplement annotées ; l'algorithme du §7 et la reveal « Reconnaître
   ces séries » renvoyaient à d'Alembert. Tout est regroupé en fin de chapitre (« POUR ALLER PLUS LOIN · 2ᵉ ANNÉE ET HORS
   PROGRAMME »), avec renvoi à `series2a`. La semi-convergence est explicitement hors programme en PTSI.
2. **EXO 03 « Règle de d'Alembert (2ᵉ année) »** : entièrement fondé sur un outil non exigible. Réécrit avec les outils de PTSI
   (n!/nⁿ ≤ 2/n², série exponentielle, règle nᵅuₙ) ; d'Alembert reste en remarque. Mêmes séries, mêmes conclusions.
3. **EXO 05 et EXO 06** reposaient sur le CSSA : EXO 05 refait par les suites adjacentes (outil de 1ʳᵉ année, qui est la preuve
   du théorème de 2ᵉ année) ; EXO 06 traite en PTSI la convergence absolue et la divergence grossière, la question restante est
   marquée « Pour aller plus loin, 2ᵉ année ».
4. **Exercice « Concours PT »** : sa question B2 utilisait d'Alembert et l'ensemble (deux questions de cours) était trop mince.
   Remplacé par un problème en trois parties sur la méthode des rectangles (encadrement, reste de Σ1/kᵅ, accélération du
   calcul de π²/6, sommes partielles divergentes, premier n tel que Hₙ ≥ 10).
5. **Méthodes 1, 3 et 4** (d'Alembert, CSSA) : condensées dans un encadré « Pour aller plus loin (2ᵉ année) » en fin d'onglet.
6. **Comparaison série-intégrale** : présente depuis le 15/11 mais noyée dans le §5 ; elle a maintenant sa section (§7), le cas
   des fonctions croissantes, deux figures calculées, une méthode, trois exercices (02 Q4, 08, 09) et le concours.
7. Formules en ligne trop larges à 390 px dans les solutions conservées : passées en bloc.

Les EXO 01, 02 et 04 d'origine sont justes (recalculés) et repris tels quels. Le bandeau `.hors-prog` du haut du cours est
remplacé par le bloc « AU PROGRAMME · PTSI ».

## Couverture du programme (section « Séries numériques » de PTSI) avant → après

| Capacité | Avant | Après |
|---|---|---|
| Sommes partielles, convergence, somme, linéarité | ✅ | ✅ §1 (figure des sommes partielles) |
| Divergence grossière, reste | ✅ | ✅ §2 (exemples (1+1/n)ⁿ, cos n) |
| Lien suite-série, télescopage | ✅ | ✅ §3 |
| Séries géométriques (raison complexe) | 🔶 (somme seule) | ✅ §4 (démonstration, reste exact, figure, balle qui rebondit, raison complexe) |
| eᶻ = Σ zⁿ/n! pour z ∈ ℂ | 🔶 (énoncé seul) | ✅ §5 (démonstration par Taylor-Lagrange complexe, calcul de cos 1) |
| Termes positifs : majoration, comparaison, équivalents | ✅ | ✅ §6 (démonstrations) |
| Méthode des rectangles, étude de sommes partielles | 🔶 (ajout du 15/11) | ✅ §7 (décroissante et croissante, Hₙ, Σ√k, reste de Σ1/k²) |
| Séries de Riemann | ✅ | ✅ §8 (démonstration par §7, règle nᵅuₙ) |
| ★ Convergence absolue, sommabilité, uₙ = O(vₙ) | 🔶 | ✅ §9 (démonstration, cas complexe, notation Σ\|uₙ\| < +∞) |
| D'Alembert, séries alternées, semi-convergence (PT) | présentés comme du cours | regroupés en fin de chapitre, renvoi `series2a` |

## Méthodes (10)

Commencer par le terme général ; séries géométriques et exponentielles ; télescopage ; comparer (termes positifs) ;
équivalent du terme général ; règle nᵅuₙ ; méthode des rectangles ; majorer un reste ; signe variable ou complexe
(convergence absolue) ; discuter selon un paramètre (Σ nᵃqⁿ). Puis « Pour aller plus loin » (d'Alembert, séries alternées) et
les pièges.

## Exercices (12)

01, 02, 04 conservés ; 03, 05, 06 adaptés (voir plus haut) ; nouveaux : 07 sommes géométriques et exponentielles (dont un
décimal périodique et une raison complexe), 08 ln(n!) ~ n ln n par une fonction croissante, 09 constante d'Euler (suites
adjacentes), 10 développements limités du terme général, 11 convergence absolue et séries complexes ; Concours PT « Sommes
partielles et restes par la méthode des rectangles ».

## Cartes

Aucune carte fausse : les 7 cartes sur d'Alembert, le CSSA et la semi-convergence portent déjà le préfixe « Hors programme
en PTSI (vu en 2ᵉ année) : » (correction du 15/11). Ajoutées (14) : reste, série géométrique décalée et son reste,
démonstration de eᶻ, encadrement des rectangles (décroissante), cas croissant, encadrement de Hₙ et γ, équivalent de
Σ1/kᵅ (α < 1), reste de Σ1/k², rôle de la monotonie, règle nᵅuₙ, domination complexe, suite sommable, critère des termes
positifs, Σ n!/nⁿ sans d'Alembert. Questions contenant une formule écrites en `\\( … \\)`.

## Notations

Celles de `series2a` : Sₙ, Rₙ, Hₙ, γ ; « nature », « divergence grossière », « absolument convergente », « sommable » ;
séries notées Σ uₙ, somme Σ_{n=n₀}^{+∞} uₙ.

## Doutes

- L'estimation du **reste** d'une série convergente par la méthode des rectangles (§7, méthode 8, concours) n'utilise que des
  intégrales sur des segments puis un passage à la limite ; le programme de PTSI parle des sommes partielles, celui de PT
  l'étend : présentée comme une application, sans intégrale généralisée.
- La convergence de Σ(−1)ᵏ⁻¹/k vers ln 2 est démontrée en PTSI par Taylor-Lagrange (chapitre `integrales` §10) et par les
  suites adjacentes (EXO 05) ; seul le mot « semi-convergente » est signalé de 2ᵉ année.
- Le contre-exemple du critère des équivalents en signe variable (§6) s'appuie sur la convergence de Σ(−1)ⁿ/√n, établie à
  l'EXO 05 Q3 par les suites adjacentes.
- `ser-cartes-corr.json` est une liste vide (rien à corriger) ; `corriger_cartes.py ser … --essai` l'accepte.
