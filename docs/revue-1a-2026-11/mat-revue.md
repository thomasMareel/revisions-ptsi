# Revue du chapitre `matrices` (prefix `mat`) « Calcul matriciel » — 2026-11-21

Point 4 de l'audit (`docs/audit-2026-11/maths-1a.md` §2 point 1, §5 point 3) : matrice de passage, changement de base,
matrices semblables, rang d'une matrice et lien avec les systèmes, absents en 1ʳᵉ année (seul `matrices2a` les traitait).
Le chapitre avait déjà été réécrit une fois (§1 à §4, exemples calculés) : ces quatre sections sont gardées, complétées
et renumérotées ; le reste est nouveau. Le panneau `mat-video` n'est pas touché.

## Fichiers produits (AN1/)
- `mat-cours.src.html` (65 789 car., 11 sections §, 17 exemples traités, 4 figures) ; gabarit `mat-cours.tpl.html`
  (+ `mat_retouches_cours.py`), figures `mat_figs.py` → `mat_figs.json`, assemblage `lin_construire.py mat`.
- `mat-meth.src.html` : 10 méthodes (avant : 8 + pièges).
- `mat-exos.src.html` : 12 exercices (11 + Concours PT), construit par `mat_exos_construire.py` (+ `mat_retouches_exos.py`)
  à partir des exercices actuels et de `mat-exos-ajout.tpl.html`.
- `mat-cartes-corr.json` : 2 réponses corrigées ; `mat-cartes-ajout.js` : 15 cartes (30 → 45).
- Vérifications : `mat_calculs.py` (122 contrôles sympy, tous justes) ; rendu des cartes `lin_cartes_rendu.py`.

## Erreurs et défauts trouvés dans l'existant, et corrections
- Cours §4 : « pour une matrice carrée, AB = I suffit » affirmé sans justification → démontré au §8 (inversible d'un seul côté).
- Méthodes : la méthode « déterminant 3 × 3 par cofacteurs » relève du chapitre Déterminants → retirée ; le piège « la règle
  de Cramer ne s'applique qu'aux systèmes carrés… » présentait les formules de Cramer, **hors programme** (PTSI et PT) →
  remplacé par « système de Cramer » (vocabulaire du programme) et résolution par le pivot.
- EXO 03 : résolu par les **formules de Cramer** (hors programme) → réécrit par le pivot (L₁ ↔ L₂ car m peut être nul).
- EXO 05 : corrigé inachevé (« L₃ ← L₃ + L₂/3, etc. Après calcul complet ») → Gauss-Jordan détaillé jusqu'au bout.
- EXO 06 : « théorème rang-nullité », `\text{Im}`, `\text{Vect}` → « théorème du rang », `\operatorname{Im}`, `\operatorname{Vect}`.
- EXO 04 : juste ; une question ajoutée (inverse à coefficients entiers par résolution de AX = Y, et AX = (1, 1, 1)).
- Ancien « Concours PT » (3 questions, juste) gardé en EXO 07 ; `^{\mathsf T}` → `^\top`.
- Formules en ligne trop longues des exercices gardés passées en bloc (débordaient au téléphone).
- Carte 18 (« Formule de Cramer… ») : réponse préfixée « Hors programme en PTSI (et en PT) : », avec la méthode exigible.
- Carte 25 (« Que signifie AB = 0 pour A, B ≠ 0 ? ») : « A ou B est un diviseur de zéro… det(A) = 0 ou det(B) = 0 »
  était trompeur → les deux sont diviseurs de zéro et aucun n'est inversible (det A = det B = 0).
  Les deux corrections ne touchent que la réponse.

## Couverture du programme (PTSI : « Calcul matriciel et systèmes linéaires » S1 ; « Matrices et applications linéaires » S2)

| Capacité du programme | Avant | Après |
|---|---|---|
| Opérations, produit, transposée | §1 | §1 (gardé) |
| Matrices élémentaires, E_ij E_kl = δ_jk E_il, AX combinaison des colonnes | absent | §1 |
| I_n, scalaires, diagonales, triangulaires, S_n, A_n, nilpotentes, diviseurs de zéro | §1 (partiel) | §2, exemples |
| Binôme, puissances | §2 | §3 (gardé) + démonstration |
| Opérations élémentaires vues comme produits matriciels | absent (l'audit : « très bref ») | §4, exemple |
| Système AX = B, homogène associé, compatibilité, solutions X₀ + Y, pivot | §3 (sans structure ni compatibilité) | §5, figure, 2 exemples |
| Inversibles, GL_n, inverse d'un produit/transposée, calcul de l'inverse | §4 | §6 (gardé) |
| Triangulaires inversibles, inverse triangulaire | absent | §6, exemple |
| Matrice d'un vecteur, d'une famille, d'une AL ; rotation, homothétie | §5 (bref) | §7, figure, 3 exemples |
| Isomorphisme L(E,F) ≅ M_{n,p}, dimension ; composée, réciproque | une phrase | §7 + démonstration |
| Application canoniquement associée ; noyau, image, rang d'une matrice | une phrase | §8, 2 exemples |
| Inversibilité ⟺ Ker = {0} ⟺ colonnes génératrices ⟺ rang n ; inversible d'un seul côté | partiel, sans preuve | §8 + démonstration |
| Opérations élémentaires et image/noyau/rang ; rg(Aᵀ) = rg A (admis) | absent | §8 |
| Matrice de passage, inverse, X = PX' | absent | §9 + démonstration, figure |
| Changement de couple de bases A' = Q⁻¹AP, endomorphisme A' = P⁻¹AP | absent | §9 + démonstration, 2 exemples |
| Matrices semblables, recherche d'une matrice simple semblable | absent | §10, figure, 3 exemples |
| Systèmes et rang : noyau, dim = p − r, compatible ⟺ B ∈ Im A, système de Cramer | absent | §11, discussion complète |

Méthodes : produit, puissances, pivot, inverse, matrice d'une application, rang/noyau/image, changement de base, matrice
simple semblable, semblables ou non, discussion d'un système par le rang. Exercices nouveaux : EXO 08 (u(P) = (X+1)P' :
matrice, base (1, X+1, (X+1)²) où elle est diagonale, puissances, équation), EXO 09 (rang et système à deux paramètres,
noyau et équation de l'image), EXO 10 (changement de base dans ℝ³, matrice diagonale semblable, Aⁿ), EXO 11 (semblables
ou non : E₁₂ et E₂₁, matrice de carré nul de rang 1, invariants), Concours PT (noyaux de A − I, A − 2I, base où la
matrice est triangulaire T = D + N, Tⁿ, Aⁿ, trois suites couplées, inverse et formule pour n = −1).

## Figures (calculées, contrôlées en clair et en sombre)
1. Lecture d'un système par les colonnes (cas inversible / colonnes colinéaires) (§5). 2. Rotation : images de e₁, e₂ (§7).
3. Un même vecteur dans deux bases, quadrillages canonique et oblique, X = (3, 5), X' = (2, 1) (§9). 4. Action de
A = [[0, 1], [−2, 3]] sur la maille (u₁, u₂) : étirement 2 le long de u₁ (§10).

## Notations
Exactement celles de `matrices2a` : `\operatorname{Mat}_{\mathcal{B},\mathcal{C}}(u)`, `\operatorname{Mat}_{\mathcal{B}}(u)`,
`P_{\mathcal{B}\to\mathcal{B}'}`, `A' = Q^{-1}AP`, `A' = P^{-1}AP`, `\operatorname{rg}`, `A^\top`, `\mathrm{GL}_n(\mathbb{K})`,
`E_{ij}`, `\delta_{jk}` ; u, v pour les applications (comme le programme et `al2`). Exemples tous différents de ceux de
`matrices2a` (qui reste le chapitre de 2ᵉ année).

## Doutes
- La consigne citait la notation \(P_{\mathcal B}^{\mathcal B'}\) ; le site (`matrices2a` §1) emploie
  \(P_{\mathcal{B}\to\mathcal{B}'}\) : j'ai gardé celle du site et cité l'autre entre parenthèses dans la définition (§9).
- Carte 3 (« Rouché-Fontené ») : énoncé juste, nom hors programme ; carte 22 (« théorème rang-nullité ») : réponse juste,
  nom non officiel. Non modifiées (questions justes ; les changer n'apporterait rien et toucherait la progression).
- Les déterminants restent au chapitre Déterminants ; le cours y renvoie (critère det ≠ 0, invariance par similitude).
- Après application des panneaux au dépôt : `python3 tools/replier_panneaux.py`, puis `validate.py`, `check_js.py`.
