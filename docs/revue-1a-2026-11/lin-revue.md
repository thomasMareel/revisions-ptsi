# Revue du chapitre `applin` (prefix `lin`) « Applications linéaires » — 2026-11-21

Point 4 de l'audit (`docs/audit-2026-11/maths-1a.md` §2 points 1 et 4, §5 point 3) : symétries, rang d'une famille et d'une
application, base adaptée, forme géométrique du théorème du rang, rg(v∘u) ≤ min, équations linéaires u(x) = a.

## Fichiers produits (AN1/)
- `lin-cours.src.html` (61 890 car., 9 sections §, 13 exemples traités, 5 figures calculées) ; gabarit `lin-cours.tpl.html`
  + figures `lin_figs.py` → `lin_figs.json`, assemblage `lin_construire.py lin` (module de tracé `lin_svg.py`).
- `lin-meth.src.html` : 10 méthodes (avant : 6 + une liste de pièges).
- `lin-exos.src.html` : 12 exercices (11 + Concours PT) ; EXO 01-06 gardés (`lin_exos_garde.html`), EXO 07-11 et
  Concours dans `lin-exos-ajout.tpl.html`, assemblage `lin_retouche_exos.py`.
- `lin-cartes-corr.json` : `[]` (aucune carte fausse) ; `lin-cartes-ajout.js` : 14 cartes (27 → 41).
- Vérifications : `lin_calculs.py` (97 contrôles sympy, tous justes : cours, méthodes, exercices) ; rendu des cartes
  `lin_cartes_rendu.py` ; aperçu des figures `lin_apercu.py` (clair/sombre). Anciens panneaux : `lin_mat_orig/`.

## Erreurs et défauts trouvés dans l'existant, et corrections
- Cours : pas d'erreur mathématique, mais couverture incomplète (voir tableau) ; démonstrations en `<h4>` hors bloc
  dépliable ; un §7 « Méthodologie » qui doublait l'onglet Méthodes (retiré, contenu repris dans les méthodes).
- EXO 06 : « endomorphisme nilpotent d'indice 2 » imprécis (f = 0 vérifie f² = 0 et est d'indice 1) → « de carré nul »,
  avec un exemple où Im N = Ker N.
- EXO 05 : ajout d'une remarque (la direction est ici perpendiculaire au plan : projection orthogonale, 2ᵉ année).
- Ancien « Concours PT » trop court (3 questions) : gardé tel quel en parties A-B et prolongé (parties C à E).
- Notations harmonisées : `\mathrm{im}\,f`, `\mathrm{rg}\,f` → `\operatorname{Im} f`, `\operatorname{rg} f` ; formules en
  ligne trop longues des exercices gardés passées en bloc ou coupées (débordement au téléphone).
- Cartes : les 27 relues, toutes justes.

## Couverture du programme (PTSI, « Espaces vectoriels et applications linéaires », C, + B c)

| Capacité du programme | Avant | Après |
|---|---|---|
| Application linéaire, L(E,F), endo/iso/automorphisme, exemples (Kⁿ, K[X], fonctions, K^ℕ) | §1 (sans suites) | §1, exemple traité |
| Combinaison linéaire, composition, bilinéarité, réciproque | §2 | §2 + démonstration |
| Identité, homothéties, uᵏ ; GL(E), uᵏ pour k ∈ ℤ | absent (GL, k ∈ ℤ) | §2, exemple w^k, k ∈ ℤ |
| Image directe et réciproque d'un sous-espace | absent | §3, exemple traité |
| Noyau, image, injectivité, Im u = Vect(u(xᵢ)) | §3 | §3 + démonstrations, exemple (Ker ⊂ Im) |
| Rang d'une famille finie | absent | §4 |
| rg(v∘u) ≤ min(rg u, rg v), invariance par isomorphisme | absent | §4 + démonstration, exemples |
| Détermination par l'image d'une base ; injectivité/surjectivité/bijectivité lues sur cette image | §5 (sans preuve) | §5 + démonstration, figure |
| Espaces isomorphes ⟺ même dimension ; dim L(E,F) | absent | §5 |
| Application définie par ses restrictions à E₁ ⊕ E₂ | absent | §5 (recollement) |
| Base adaptée à un sous-espace, à une somme directe | absent | §5, utilisée §8-§9 |
| Forme géométrique du théorème du rang | absent | §6 + démonstration, figure calculée |
| Théorème du rang, inj ⟺ surj ⟺ bij, inversible d'un seul côté | §4 (sans le dernier point) | §6 + démonstrations, 2 exemples |
| Équations linéaires u(x) = a, x₀ + Ker u ; systèmes, EDL, suites a-g | absent | §7, 4 exemples (dont Σk²) |
| Dimension des solutions d'EDL homogènes et de récurrences d'ordre 2 | absent | §7 (via isomorphismes) |
| Projecteurs : définition géométrique, p² = p | §6 (par p² = p seulement) | §8 : définition géométrique, théorème, 2 figures (plan, espace) |
| Symétries : définition géométrique, s² = id | absent | §9 : définition, théorème, 2 figures |

Méthodes : 10 (linéarité, noyau, image, rang, injectivité/bijectivité, image d'une base, équation linéaire, projecteur,
symétrie, matrice d'une projection/symétrie donnée géométriquement). Exercices nouveaux : EXO 07 (rang d'une famille selon
un paramètre, rang de v∘u et u∘v), EXO 08 (interpolation par le théorème du rang), EXO 09 (trois équations linéaires),
EXO 10 (symétrie de ℝ³ donnée par sa matrice), EXO 11 (Ker u ⊕ Im u ⟺ rg u² = rg u, cas u³ = u), Concours PT prolongé
(rang 1, A² = 8A, projecteur f/8, symétrie, équation f(x) = a, fᵏ, inverse de f + id).

## Figures (calculées, classes du site, contrôlées en clair et en sombre)
1. Image d'un quadrillage et d'une lettre F par u(x, y) = (2x + y, y) (§5). 2. Fibres et forme géométrique du théorème
du rang pour u(x, y) = (x − y, y − x), deux panneaux (§6, reprise au §7). 3. Projection sur F = Vect((2, 1)) parallèlement à
G = Vect((−1, 1)) (§8). 4. Symétrie oblique sur un vecteur et un drapeau (§9). 5. Projection et symétrie de ℝ³ par rapport
au plan x + 2y − z = 0 parallèlement à Vect((1, 1, 1)), parties cachées en pointillés (§8-§9).

## Notations
Celles du programme et de la 2ᵉ année (`al2`, `psy`, `mx2`) : u, v pour les applications, `\ker u`, `\operatorname{Im} u`,
`\operatorname{rg} u`, `\mathcal{L}(E,F)`, `\mathrm{GL}(E)`, `\mathrm{id}`, `\operatorname{Mat}_{\mathcal{B}}(p)`,
`\operatorname{diag}`, vecteurs en lettres nues ; vecteurs en gras dans les SVG. Les exercices gardés conservent leurs noms
(f, φ, p).

## Doutes et remarques pour l'intégration
- Le rang d'une famille et la base adaptée relèvent de la partie B (chapitre `ev`), qui ne les traite pas encore : ils sont
  posés ici (§4, §5) ; le futur `ev` réécrit pourra y renvoyer ou les reprendre.
- Projecteurs : `ev` §4 en parle aussi (doublon signalé par l'audit) ; c'est `applin` qui porte désormais la version complète.
- Le simulateur (`lin-simu`) n'est pas touché ; le cours y renvoie (§9).
- Après application des panneaux au dépôt : `python3 tools/replier_panneaux.py`, puis `validate.py`, `check_js.py`.
