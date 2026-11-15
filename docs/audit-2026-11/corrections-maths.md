# Mathématiques de 1ʳᵉ année : corrections après l'audit du 14/11/2026

Source : `docs/audit-2026-11/maths-1a.md`, §3 et §4. Chaque point a été revérifié : le calcul a été refait avec sympy, ou la ligne a été relue dans `ptsi_maths.txt` (PTSI) et `maths.txt` (PT).
Tous les fichiers produits sont dans `REV2`. Le dépôt n'a pas été modifié : `corriger_cartes.py` a été lancé seulement avec `--essai`.
Les panneaux d'origine, qui servent de référence pour les `diff`, sont dans `REV2/_maths_orig/` (`_orig_<p>-<onglet>.html`).

## Fichiers produits

| Chapitre (prefix) | Panneaux | Cartes |
|---|---|---|
| series (`ser`) | `ser-cours`, `ser-meth`, `ser-exos` | `ser-cartes-corr.json` (8) |
| asympt (`asy`) | `asy-cours`, `asy-meth` | `asy-cartes-corr.json` (3) |
| dl (`dl`) | `dl-cours` | `dl-cartes-corr.json` (1) |
| contderiv (`cd`) | `cd-cours`, `cd-meth`, `cd-exos` | `cd-cartes-corr.json` (7) |
| fonctions (`fn`) | `fn-meth` | `fn-cartes-corr.json` (3) |
| complexes (`cpx`) | `cpx-cours`, `cpx-meth`, `cpx-exos` | `cpx-cartes-corr.json` (2) |
| det (`det`) | `det-cours`, `det-exos` | `det-cartes-corr.json` (3) |
| polynomes (`pol`) | `pol-cours`, `pol-meth`, `pol-exos` | `pol-cartes-corr.json` (3, dont 1 `q_nouvelle`) |
| logique (`log`) | `log-cours` | `log-cartes-corr.json` (1) |
| geometrie (`geo`) | — | `geo-cartes-corr.json` (1, `q_nouvelle`) |
| va (`va`) | `va-cours`, `va-meth`, `va-exos` | `va-cartes-corr.json` (6) |
| proba (`prb`) | `prb-cours`, `prb-meth`, `prb-exos` | `prb-cartes-corr.json` (5) |
| denombrmt (`denom`) | `denom-cours` | `denom-cartes-corr.json` (1) |

Les panneaux sont tous `REV2/<p>-<onglet>.src.html`. Aucune carte n'est ajoutée, retirée ni déplacée. Deux questions sont réécrites à rang inchangé (`pol` n° 22, `geo` n° 19) : la progression des élèves est donc conservée.

## Tableau des points de l'audit

### Erreurs (§4)

| Point de l'audit | Fait ? | Fichier |
|---|---|---|
| `asympt` méthode 2 : e^{sin x} | Fait. Le DL est refait (sympy : 1 + x + x²/2 + o(x³), terme en x³ nul). Il manquait u³/6, et le « + x³/2 » est supprimé. Le développement final est mis en bloc. | `asy-meth` |
| `asympt` carte n° 20 (même DL) | Fait. Réponse réécrite en `\( \)`. | `asy-cartes-corr.json` |
| `fonctions` méthode 2 : mnémonique du sinus | Fait. « sin(πk/6) = √k/2 » est faux. La règle porte sur les angles 0, π/6, π/4, π/3, π/2 : sin = √k/2 pour k = 0…4, et le cosinus dans l'ordre inverse. | `fn-meth` |
| `det` EXO 03 Q3 : corrigé inachevé | Fait. Réécrit : C₂ = C₃, puis α + β = 1 et α + 2β = 4, d'où L₃ = 3L₂ − 2L₁ (vérifié). Conclusion sur l'inversibilité et le système. | `det-exos` |
| `asympt` §2 : « coefficients a_k = f^(k)(a)/k! » | Fait. Les coefficients sont uniques s'ils existent. La formule n'est valable que si f est Cⁿ (Taylor-Young). Contre-exemple : x³ sin(1/x), cohérent avec `dl` §4. | `asy-cours` |
| `asympt` §2 : « dériver terme à terme » | Fait. Primitivation énoncée correctement (terme constant F(a)). Pour la dérivation : on ne dérive pas sans hypothèse, ce qui est cohérent avec `dl` §6. | `asy-cours` |
| `asympt` §4 : branche parabolique inventée | Fait. Les directions (Ox), (Oy) et y = ax sont données avec un exemple chacune. | `asy-cours` |
| `asympt`, pièges : x + x² ≁ 2x | Fait. Remplacé par un vrai contre-exemple de somme d'équivalents : en +∞, x + 1 ∼ x et −x ∼ −x, mais la somme vaut 1 et n'est pas équivalente à 0. | `asy-meth` |
| `contderiv` §1 : « limite ssi ℓ⁻ = ℓ⁺ » | Fait. Si f n'est pas définie en a : ℓ⁻ = ℓ⁺. Si f est définie en a : il faut de plus que la valeur commune soit f(a) (convention du programme). Exemple : f = 0 sur ℝ* et f(0) = 1. | `cd-cours` |
| `va` méthode 3 : Poisson « plus précise » | Fait. La binomiale est la loi exacte et Poisson n'en est qu'une approximation, plus simple à calculer. | `va-meth` |
| `polynomes` méthode 4 : forme de la DES | Fait. Pour des pôles simples, la forme est F = E + Σ λᵢ/(X − zᵢ). Pour un pôle multiple ou un facteur de degré 2, la forme est donnée par l'énoncé (programme). | `pol-meth` |
| `polynomes` §4 : X et x mélangés | Fait. La DES est écrite en X et la primitive en x, sur un intervalle ne contenant ni 1 ni −1. | `pol-cours` |
| Carte `logique` n° 14 (De Morgan) | Fait. Réponse propre en `\( \)`. | `log-cartes-corr.json` |
| Carte `det` n° 23 | Fait. Formule complète en a_{ij}, vérifiée avec sympy. | `det-cartes-corr.json` |
| Carte `geometrie` n° 19 (« identité de Jacobi ») | Fait. La question devient « Formule du double produit vectoriel » (`q_nouvelle`). La réponse, vérifiée avec sympy, cite la vraie identité de Jacobi. | `geo-cartes-corr.json` |
| Carte `fonctions` n° 23 (φ = arctan(b/a)) | Fait. φ est défini par cos φ = a/R et sin φ = b/R. arctan(b/a) ne convient que si a > 0. | `fn-cartes-corr.json` |
| Carte `fonctions` n° 24 (k en double) | Fait. L'entier devient n, avec la condition \|k\| ≤ 1. La question est inchangée. | `fn-cartes-corr.json` |
| Coquille « La tangeante » | Fait. | `fn-meth` |
| Coquille « l'algèbrement clos » | Fait. La phrase dit maintenant que ℂ est algébriquement clos (d'Alembert-Gauss), avec l'énoncé correct. | `cpx-cours` |

### Encadré faux et comparaison série-intégrale

| Point | Fait ? | Fichier |
|---|---|---|
| Bandeau de `series` (« hors programme PTSI ») | Fait. Le bandeau est réécrit avec l'étiquette « Au programme · PTSI (2ᵉ semestre) ». Il cite ce qui est au programme d'après la section « Séries numériques » de `ptsi_maths.txt` : convergence, séries géométriques, termes positifs, méthode des rectangles, Riemann, convergence absolue. Il signale que d'Alembert, le CSSA et la semi-convergence relèvent de la 2ᵉ année, avec un lien vers `#series2a/cours`. | `ser-cours` |
| Série-intégrale dite hors programme : « EXO 03 Q4 » | Fait, mais c'est l'**EXO 02 Q4** (l'EXO 03 n'a pas de Q4 : l'audit se trompe de numéro). La mention « hors programme strict » est retirée. La correction est refaite par la méthode des rectangles : Σ 1/(k ln k) ≥ ln ln(N+1) − ln ln 2 → +∞. L'indice trompeur de l'énoncé (« comparer à 1/n ») est remplacé. | `ser-exos` |
| Série-intégrale : méthodes, « Réflexe 5 » | Fait. Le réflexe 5 renvoie à la nouvelle méthode 6. | `ser-meth` |
| Ajout au cours (exception autorisée) | Fait. Dans §5, un h3 « Comparaison série-intégrale (méthode des rectangles) » donne l'encadrement par rectangles, l'encadrement des sommes partielles et une conséquence (prop-box). Un exemple traité couvre la série harmonique (ln(N+1) ≤ H_N ≤ 1 + ln N, d'où H_N ∼ ln N) et les séries de Riemann (α > 1 : S_N ≤ α/(α−1) ; 0 < α < 1 : divergence). Les bornes ont été vérifiées numériquement (Σ 1/n² ≈ 1,645 ≤ 2). Le §3 renvoie à ce paragraphe pour H_n ∼ ln n. | `ser-cours` |
| Ajout aux méthodes | Fait. Une « Méthode 6 — Comparer une série à une intégrale » en 4 étapes. Exemple original : S_N = Σ 1/√k, encadré par 2√(N+1) − 2 ≤ S_N ≤ 2√N − 1, d'où S_N ∼ 2√N. Contrôle numérique pour N = 100 : 18,10 ≤ 18,59 ≤ 19. | `ser-meth` |

### Hors-programme signalé sur place (§3)

Chaque cas a été vérifié dans le texte officiel. Ce qui est encore au programme de PT est marqué « vu en 2ᵉ année ». Ce qui n'est au programme d'aucune des deux années est marqué « pour aller plus loin ».

| Chapitre | Signalé | Vérification dans le programme |
|---|---|---|
| `series` | §5 d'Alembert : notice et « (hors programme) » au h3. §6 : notice avant la semi-convergence, h3 du CSSA. §7 et §3 : mentions « (2ᵉ année) ». Méthodes 1, 3 et 4 et réflexe 3. EXO 03, 05 et 06 « (2ᵉ année) ». Concours B2 : « d'Alembert, vu en 2ᵉ année, ou série exponentielle ». Cartes 11, 12, 15, 16, 17, 18 et 24 préfixées, 21 retouchée. | PTSI : la semi-convergence est explicitement hors programme, et ni d'Alembert ni le CSSA ne figurent au programme. Les trois sont au programme de PT (`maths.txt`, Séries numériques). |
| `contderiv` | §1 continuité uniforme et Heine : notice et h3. §4 convexité et Jensen : h2 et notice, qui rappelle que e^x ≥ 1 + x et ln(1+x) ≤ x sont au programme. Méthode 5, EXO 05, cartes 13 à 17 et 19 préfixées. Carte 18 réécrite : bornes atteintes, puis Heine signalé. | « convexe », « uniforme » et « Heine » n'apparaissent ni dans `ptsi_maths.txt` ni dans `maths.txt`. |
| `dl` | §3 « Dérivée seconde et convexité » : notice et h3. Carte 16 préfixée. | Idem. |
| `det` | §1 restructuré. La définition suit le programme : unique application linéaire par rapport à chaque colonne, antisymétrique, valant 1 en I_n (théorème admis). Le développement par rapport à une ligne devient une propriété (prop-box, démonstration non exigible). L'intro et le §2 n'emploient plus « multilinéaire alternée ». §4 : notice, comatrice et Cramer « (hors programme) ». EXO 04 et 05, cartes 11 et 12. | « Le vocabulaire des formes multilinéaires alternées […] et les formules de Cramer sont hors programme » ; « La notion de comatrice est hors programme » (PTSI et PT). |
| `polynomes` | §2 PGCD, Bézout et Gauss : notice et h3. §3 Viète : notice (s₂…s_{n−1} hors programme, somme et produit au programme). §4 : notice « pôles simples seulement ». Méthode 5, EXO 06 (s₂ demandé), cartes 4 et 5. EXO 05 « (2ᵉ année) », pour son intégrale sur [2, +∞[. | Le PGCD de polynômes est absent des deux programmes. « Les fonctions symétriques élémentaires sont hors programme. » DES : « la forme cherchée doit être fournie ». Intégrale généralisée : PT. |
| `fonctions` | Méthode 4 : th, (th)′ et Argsh/Argch marqués en ligne, « seule formule exigible » sur ch² − sh² = 1. Carte 19 (arcsinh) préfixée. | « La fonction tangente hyperbolique et les fonctions hyperboliques réciproques sont hors programme. La seule formule exigible est ch² − sh² = 1. » |
| `proba` | §2 : notice sur la tribu et la σ-additivité, avec le cadre fini (Ω, P) de PTSI ; h3 retouché. §3 : « E fini (le cas dénombrable relève de la 2ᵉ année) ». §4 : notice et h3 pour les lois géométrique et de Poisson. Méthode 3 marquée en ligne. EXO 04 et 05. Cartes 19, 20, 21 et 23 « vu en 2ᵉ année », carte 22 (approximation) « pour aller plus loin ». | PTSI : « On se limite au cas d'un univers fini ». σ-additivité, G(p) et P(λ) : PT. |
| `va` | §1 : notice sur le cadre dénombrable (PT) et la fonction de répartition (au programme d'aucune année). §3 : notice et h3 pour Poisson et la loi géométrique. Méthode 1 marquée en ligne, méthode 3 (approximation) « pour aller plus loin », piège Poisson « (2ᵉ année) ». EXO 03 et 04. Cartes 8, 10, 11 et 19 « vu en 2ᵉ année », carte 9 « pour aller plus loin », carte 0 réécrite pour le cadre fini. | Idem. « répartition » est absent des deux programmes, et l'approximation B(n, p) ≈ P(np) aussi (PT : seulement l'« interprétation […] comme loi des événements rares »). |
| `denombrmt` | §4 loi hypergéométrique : notice et h3. Carte 20 (crible à 3 ensembles) préfixée. | « La formule du crible est hors programme » ; « hypergéométrique » est absent des deux programmes. |
| `logique` | §2 relations : notice et h3 « (relations : hors programme) ». | « Le programme se limite strictement aux notions de base » ; seuls l'ordre de ℝ et la congruence modulo 2π y figurent. |
| `asympt` | §3 Stirling : notice, et suppression de « mais à connaître ». Carte 18 préfixée. | « Stirling » est absent des deux programmes. |
| `complexes` | Méthode 7 : z ↦ z + b et z ↦ az (rotation et homothétie de centre O) restent au programme ; l'étude générale de z ↦ az + b (similitude) est marquée hors programme. EXO 06. Carte 41 préfixée, carte 39 reformulée sans le mot « similitude » (contenu au programme). | « L'étude générale des similitudes est hors programme. » |

## Erreurs supplémentaires trouvées en relisant (corrigées)

- **`contderiv` EXO 06 Q3**. L'énoncé demandait de montrer u_n ∈ [1/2, 1], ce qui est faux (u₁ = e⁻¹ ≈ 0,368). La correction le remarquait en cours de route (« Non, 0,37 < 0,5… ») puis concluait de façon brouillonne. L'énoncé et le corrigé sont réécrits : I = [e⁻¹, 1] est stable, puis l'inégalité des accroissements finis donne \|u_n − α\| ≤ kⁿ\|u₀ − α\| avec k = e^{−1/e} ≈ 0,692.
- **`series` §5**, application de d'Alembert à e^x. Le texte disait « u_n = xⁿ/n! est de signe constant », ce qui est faux si x < 0. Le raisonnement porte désormais sur \|u_n\|.
- **`series` EXO 02 Q4** : l'indice trompeur de l'énoncé est corrigé (voir plus haut).
- **`polynomes` EXO 03 Q3 et EXO 05**. On y trouvait le même mélange de X et de x dans les intégrales et les primitives. L'écriture est corrigée en x. La valeur de l'EXO 03 a été vérifiée avec sympy : (2 ln 5 − 3 ln 2)/3.
- **Carte `polynomes` n° 22** : même mélange X/x dans la question et la réponse (`q_nouvelle`).
- **Carte `asympt` n° 21**. La réponse disait « ln f ∼ ln g *seulement si* … », ce qui est faux (cela marche aussi si g → 0). La condition est rendue juste (g → +∞ ou g → 0) et un contre-exemple est donné.

## Noms de chapitres à changer (proposition)

- `proba`, « Probabilités & dénombrement » → « Probabilités sur un univers fini ». Le chapitre `denombrmt` existe déjà, et le cadre de PTSI est fini.
- `contderiv` : l'exercice « Concours PT » s'intitule « TVI et inégalité de convexité » alors que sa partie B se résout par une étude de fonction (au programme). Son titre pourrait devenir « TVI et inégalité eˣ ≥ 1 + x ». Je ne l'ai pas modifié, car rien n'y est hors programme.

## Doutes et points laissés en l'état

- **Libellé des méthodes**. Pour une méthode qui relève de la 2ᵉ année (d'Alembert, CSSA), j'ai écrit « (hors programme en PTSI, vu en 2ᵉ année) » au lieu de « (hors programme, pour aller plus loin) ». Ce dernier libellé aurait été inexact, puisque ces notions sont au programme de PT. Il reste employé pour ce qui n'est au programme d'aucune des deux années.
- **Méthodes mixtes**. Quand une méthode mêle du programme et du hors-programme (`fn` méthode 4, `cpx` méthode 7, méthodes de `series`, `va` et `prb`), le marquage est fait en ligne sur l'élément concerné, pas sur le titre entier.
- **`det` carte 10** (cofacteur) : non signalée. Le développement par rapport à une ligne, avec le signe (−1)^{i+j}, est au programme ; seule la comatrice est exclue. L'EXO « Concours PT » de `det` reste un doublon de l'EXO 03 : le remplacer serait une réécriture.
- **`denombrmt` EXO 05** (« Loi hypergéométrique — contrôle qualité ») : non signalé. Les questions se traitent par dénombrement, mais Q3 compare à nK/N, formule hors programme. À trancher.
- **`fonctions` EXO 05 Q3**. On y calcule la réciproque de sh : c'est un exercice de bijection faisable en PTSI, même si Argsh est hors programme. Non signalé.
- **`geometrie` carte 19**. La formule du double produit vectoriel n'est pas citée par le programme, mais elle se vérifie en coordonnées. Non signalée, seul le nom a été corrigé.
- **`va` carte 17** (« converge en probabilité ») : ce vocabulaire est hors programme en PT. Non retouchée, faute d'être dans l'audit ; à revoir avec la réécriture.
- **Cartes en Unicode préfixées « Hors programme en PTSI (vu en 2ᵉ année) : »**. `flashPretty` met « 2ᵉ » en formule. Une capture du rendu MathJax montre un résultat quasi identique au texte : ce n'est pas gênant.

## Contrôles

- `verif_src.py` sur les 26 panneaux : aucune ERREUR. Les « attention » (formules en ligne longues, pas de bloc « AU PROGRAMME ») existaient toutes dans les panneaux d'origine : la comparaison avant/après ne donne aucun avertissement nouveau.
- `apercu_src.py`, lancé sur les 26 panneaux à 390 et 1440 px :
  - `merr` et `brut` sont vides partout, et il n'y a aucune erreur JS.
  - À 1440 px, `larges` est vide partout.
  - À 390 px, `larges` est vide pour tous les cours et toutes les méthodes. Sept onglets Exercices affichent l'« ATTENTION débordement » : `ser`, `cd`, `cpx`, `det`, `pol`, `va` et `prb`. Ces débordements **existaient déjà** : j'ai passé les panneaux d'origine (`REV2/_maths_orig/`) au même outil, et les listes sont identiques pour `ser`, `cpx`, `det`, `va` et `prb`.
  - Pour `cd` et `pol`, les listes sont plus courtes qu'à l'origine : la Q3 refaite de `cd` EXO 06 et la primitive de `pol` EXO 05 n'y figurent plus.
  - Ces débordements viennent de formules en ligne anciennes dans les solutions. L'outil affiche les solutions en forçant leur style, sans passer par `toggleSol` ni par le module CONTENU, qui pose `.mj-large`.
  - La longue formule de `pol` EXO 03 Q3, ligne que j'avais retouchée, a été passée en `$$` (deux blocs fusionnés). Elle débordait même à 1440 px.
- `corriger_cartes.py … --essai` : les 13 fichiers passent sans erreur.
- `diff` panneau actuel ↔ `REV2/<p>-<onglet>.src.html` : seules les modifications voulues apparaissent (en plus de l'absence de saut de ligne final).
