# Revue du chapitre `ev` (prefix `ev`) « Espaces vectoriels » — 2026-11-21

Point 4 de l'audit, lot 5 (`docs/audit-2026-11/maths-1a.md` ligne 34 et §3 « Doublons » ; `docs/audit-2026-11.md` §5) :
dimension finie complète (base extraite et base incomplète énoncées en une ligne ; manquaient le rang d'une famille,
K^Ω, les dimensions des espaces de solutions, la base adaptée), doublon des projecteurs avec `applin`, notations.

## Fichiers produits (AN1/)
- `ev-cours.src.html` (76 062 car. de HTML, ≈ 55 900 signes de texte contre 4 985 avant ; 10 sections § + bloc
  « AU PROGRAMME · PTSI » + « POUR ALLER PLUS LOIN » ; 16 exemples traités ; 20 démonstrations dépliables ; 4 figures
  calculées). Gabarit `ev-cours.tpl.html`, figures `ev_figs.py` → `ev_figs.json` (module `ev_svg.py`, copie de
  `lin_svg.py`), assemblage `python3 ev_construire.py ev`.
- `ev-meth.src.html` : 10 méthodes (avant : 4 + une liste de pièges), chacune avec exemple éclair chiffré ; 4 pièges.
- `ev-exos.src.html` : 12 exercices (11 + « Concours PT » en 5 parties).
- `ev-cartes-corr.json` (1 carte) ; `ev-cartes-ajout.js` (14 cartes, 25 → 39).
- Vérifications : `ev_calculs.py` (41 contrôles sympy, cours), `ev_calculs_meth.py` (15), `ev_calculs_exos.py` (51),
  tous justes ; rendu des cartes `ev_cartes_rendu.py` (0 erreur MathJax) ; figures `ev_voir.py` (clair/sombre),
  `ev_figsite.js` (figures dans la copie du site), diagnostics de débordement `ev_deborde*.js`.
  Anciens panneaux : `ev_orig_{cours,meth,exos}.html`.
- Contrôles : `verif_src.py` sans erreur ni « attention » sur les 3 fichiers ; `apercu_src.py` à 390 et 1440 :
  `merr`, `brut`, `larges` vides, aucune erreur JS, pas de débordement (scrollW = largeur) ; `corriger_cartes.py --essai`
  et `ajouter_cartes.py --essai` sans erreur.

## Erreurs et défauts de l'existant, et corrections
- Cours : pas d'erreur grossière, mais un résumé sans démonstration ; « toute famille libre peut être complétée en une
  base » sans hypothèse de dimension finie ; « toute base a le même cardinal » sans hypothèse ; projecteurs (§4) en
  doublon de `applin` §8 (retirés, renvoi à `applin` §8-§9 et à `projsym`).
- EXO 05 (Grassmann) : Q3 mal posée (« plus petite valeur possible de dim(F∩G) » pour deux sous-espaces **fixés**) et
  « théorème rang-nullité » (chapitre suivant). Réécrit : bases de F et G par résolution, minoration par Grassmann,
  calcul effectif de F ∩ G = Vect((−1, 3, −2, −1, 2)), F + G = ℝ⁵, somme non directe.
- EXO 03 Q2 : dimension justifiée par « forme linéaire non nulle, noyau de codimension 1 » (hyperplans : 2ᵉ année).
  Remplacé par une base explicite ((X − 1)X^k) ; ajout d'une Q4 (F_n ⊕ ℝ₀[X]).
- EXO 01 et EXO 04 : dimensions « 1 équation → 3 − 1 » sans base ; bases explicites données ; ajout de Q3 (EXO 01) et
  Q4 (EXO 04, décomposition d'un vecteur).
- Ancien « Concours PT » (3 questions, utilise det et produit vectoriel) : gardé comme EXO 07, prolongé (B2 :
  supplémentaire) ; remplacé par un vrai problème en 5 parties.
- Notations alignées sur `applin`, `matrices`, `ev2a` : vecteurs en lettres nues (plus de \vec), « sous-espace » au lieu
  de « SEV », \operatorname{rg}, \operatorname{Vect}, \(0_E\), ℝ_n[X] → \(\mathbb{K}_n[X]\).
- Carte 23 (dimension des solutions de u'' + ω²u = 0) : la base (cos ωt, sin ωt) n'en est une que pour ω ≠ 0, et une
  base s'écrit entre parenthèses → réponse corrigée (question inchangée). Les 24 autres cartes sont justes.

## Couverture du programme (PTSI, « Espaces vectoriels et applications linéaires », parties A et B)

| Capacité du programme | Avant | Après |
|---|---|---|
| Structure de K-ev ; Kⁿ, K[X], M_{n,p}(K) ; K^Ω, K^ℕ ; fonctions à valeurs dans un ev | §1 (axiomes, sans K^Ω) | §1 + règles de calcul démontrées, liste commentée |
| Combinaison linéaire d'une famille finie | §2 | §1, exemple traité (ℝ³, fonctions, suites) |
| Sous-espace : définition, caractérisation ; nul, droite, plan de ℝ³, K_n[X] | §1 | §2, exemple « 4 parties », figure réunion |
| Intersection d'une famille de sous-espaces (et réunion) | absent | §2 + démonstration |
| Vect, plus petit sous-espace contenant les xᵢ | §2 (sans « plus petit ») | §3 + démonstration, opérations qui conservent Vect |
| Paramétrage ↔ équations (objectif du programme) | une méthode, un sens | §3, deux exemples ; méthode 2 |
| Famille génératrice, libre, liée | §2 | §4 + propriétés démontrées, 4 exemples |
| Ajout d'un vecteur à une famille libre | absent | §4 + démonstration |
| Liberté d'une famille de polynômes à degrés distincts | absent | §4 + démonstration |
| Base, coordonnées ; bases canoniques | §2-§3 | §5 + démonstration, exemples |
| Bases de polynômes à degrés échelonnés | absent | §5 + démonstration, lien Taylor |
| Dimension finie ; existence de bases ; base extraite, base incomplète | une ligne | §6 : théorème du programme + démonstration, méthode, 2 exemples |
| n + 1 vecteurs d'un espace engendré par n sont liés ; dimension | énoncé | §7 : lemme démontré (récurrence), théorème |
| Dimensions de Kⁿ, K_n[X], M_{n,p}(K) | §3 | §7 (formulaire) |
| Dimension des solutions : EDL ordre 1, ordre 2 à coeff. constants, suites récurrentes d'ordre 2 | carte 23 seulement | §7 + exemple ; EXO 10 (preuve directe) |
| Bases = familles libres ou génératrices de n vecteurs | §2 | §7 + démonstration |
| Rang d'une famille, notation rg | absent | §8 : définition, propriétés, méthode du pivot, exemple à paramètre ; EXO 09 |
| Dimension d'un sous-espace, cas d'égalité | absent | §7 + démonstration, exemple F = G |
| Somme, somme directe, caractérisation par l'intersection | §3 (sans preuve) | §9 + démonstrations |
| Supplémentaires ; figures en dimension 2 et 3 | §4, sans figure | §9 : 2 figures, 3 exemples (dont dimension infinie) |
| Formule de Grassmann | énoncé | §10 + démonstration, 2 exemples, figure |
| Existence d'un supplémentaire ; caractérisation dimensionnelle | une phrase | §10 + démonstrations |
| Base adaptée à un sous-espace, à une somme directe | absent | §10 + exemple (aussi dans `applin` §5) |
| Projecteurs | §4 (doublon `applin`) | retirés ; renvoi `applin` §8-§9 |

Hors programme regroupé en fin de cours : sommes de plusieurs sous-espaces, produit, hyperplans (`ev2a`), supplémentaire
orthogonal, bases infinies.

## Sections du cours
§1 Espaces vectoriels · §2 Sous-espaces · §3 Sous-espace engendré, paramétrage et équations · §4 Familles libres,
génératrices · §5 Bases et coordonnées · §6 Dimension finie : existence de bases · §7 Dimension · §8 Rang d'une famille ·
§9 Somme, somme directe, supplémentaires · §10 Grassmann, supplémentaires, bases adaptées · Pour aller plus loin.

## Figures (calculées, classes du site, contrôlées en clair et en sombre et dans la copie du site à 390 px)
1. Réunion des droites y = x et y = −x : a + b hors de la réunion (§2). 2. Une droite F et deux supplémentaires G, G′ :
deux décompositions de x = (5, 4) (§9). 3. ℝ³ = plan z = 0 ⊕ Vect((1, 1, 2)), décomposition de (3, 1, 2), partie cachée
en pointillés (§9). 4. Deux plans P₁, P₂ et leur droite commune (Grassmann, §10).

## Méthodes (10)
Sous-espace ou non · équations ↔ paramétrage · liberté / relation de dépendance · base et coordonnées · base et dimension
d'un sous-espace défini par équations · rang et base extraite · compléter en une base · égalité de sous-espaces (inclusion +
dimension) · supplémentaires (dimension finie ; analyse-synthèse en dimension infinie) · Grassmann.

## Exercices (12)
EXO 01-04, 06 gardés et complétés ; EXO 05 réécrit ; EXO 07 = ancien concours prolongé ; nouveaux : EXO 08 (familles de
fonctions, lemme fondamental), EXO 09 (rang selon un paramètre, base extraite, base complétée), EXO 10 (plan des suites
u_{n+2} = u_{n+1} + 6u_n, base prouvée sans le cours), EXO 11 (ℝ₃[X] = {P(1) = P(2) = 0} ⊕ ℝ₁[X], interpolation, base
adaptée) ; Concours PT « Carrés magiques d'ordre 3 » (sous-espace, Vect(J) ⊕ M₀, coefficient central σ/3, dimension 3,
base (J, U, V), intersections avec S₃ et A₃ et somme directe, carré de Lo Shu, carrés à coefficients 1…9).

## Cartes
Corrigée : n° 23 (réponse). Ajoutées (14) : opérations conservant Vect et rang ; ajout d'un vecteur ; polynômes à degrés
distincts ; base extraite / incomplète ; lemme n + 1 vecteurs ; K[X] non de dimension finie ; rang d'une famille ;
dimension d'un sous-espace ; caractérisation dimensionnelle des supplémentaires ; base adaptée ; existence et
non-unicité du supplémentaire ; dimension des suites récurrentes d'ordre 2 ; dimension des solutions de y' + a(t)y = 0 ;
dimension de ℂ sur ℝ et sur ℂ.

## Doutes et remarques pour l'intégration
- Ordre de la navigation : `CHAP_GROUPS` place `matrices`, `det`, `ev`, `applin` dans cet ordre ; le programme (et les
  renvois des cours) suit plutôt `ev` → `applin` → `matrices` (partie « Matrices et applications linéaires ») → `det`.
  Le cours `ev` ne dépend que du pivot de Gauss (premier semestre) et fonctionne dans les deux ordres ; à arbitrer.
- La carte 19 (projecteur associé à E = F ⊕ G) reste dans le deck `ev` (pas de retrait) ; elle est juste.
- EXO 07 utilise un déterminant (chapitre `det`) et un produit vectoriel (`geo3d`) ; une alternative par le pivot est
  donnée dans la correction.
- Le concours « carrés magiques » est un thème classique ; énoncé, découpage et rédaction sont originaux.
- Après application au dépôt : `python3 tools/replier_panneaux.py`, `validate.py`, `check_js.py`, bump de `CACHE_VERSION`.
