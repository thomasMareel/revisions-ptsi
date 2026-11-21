# Revue du chapitre `det` (prefix `det`) « Déterminants » — 2026-11-21

Point 4 de l'audit, lot 5 (`docs/audit-2026-11/maths-1a.md` lignes 37, 61-64, 84, 87, 102, 114 ; `docs/audit-2026-11.md`
§5 point 6) : aligner sur la caractérisation du programme, opérations sur les colonnes, déterminant d'une famille et d'un
endomorphisme, lien avec le produit mixte ; comatrice et Cramer en hors-programme ; remplacer l'exercice « Concours PT »,
doublon de l'EXO 03.

## Fichiers produits (AN1/)
- `det-cours.src.html` (51 175 car. de HTML, ≈ 37 000 signes de texte contre 4 094 avant ; 9 sections § + bloc
  « AU PROGRAMME · PTSI » + « POUR ALLER PLUS LOIN » ; 12 exemples traités ; 9 démonstrations dépliables ; 2 figures
  calculées ; un bloc de code NumPy/SymPy). Gabarit `det-cours.tpl.html`, figures `det_figs.py` → `det_figs.json`
  (module `ev_svg.py`), assemblage `python3 det_construire.py det`.
- `det-meth.src.html` : 10 méthodes (avant : 3 + une liste de pièges), chacune avec exemple éclair chiffré ; 4 pièges.
- `det-exos.src.html` : 12 exercices (11 + « Concours PT » en 3 parties, 8 questions).
- `det-cartes-corr.json` (6 cartes) ; `det-cartes-ajout.js` (14 cartes, 25 → 39).
- Vérifications : `det_calculs.py` (37 contrôles sympy, cours), `det_calculs_meth.py` (16), `det_calculs_exos.py` (46),
  tous justes ; rendu des cartes par `ev_cartes_rendu.py` (0 erreur MathJax) ; figures `det_voir.py`, `ev_figsite.js`.
  Anciens panneaux : `det_orig_{cours,meth,exos}.html`.
- Contrôles : `verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 : `merr`, `brut`, `larges`
  vides, aucune erreur JS, pas de débordement ; `corriger_cartes.py --essai` et `ajouter_cartes.py --essai` sans erreur.

## État de départ, erreurs et corrections
- Le panneau du dépôt avait déjà reçu des retouches (lot 1) : définition par la caractérisation (admise), comatrice et
  Cramer signalés « hors programme », correction de l'EXO 03 Q3 (L₃ = 3L₂ − 2L₁) et carte 23 réécrite. Restaient :
  calcul présenté surtout par les lignes alors que le programme demande les colonnes ; aucune démonstration ; ni
  déterminant d'une famille dans une base, ni déterminant d'un endomorphisme, ni lien avec le produit mixte ;
  comatrice et Cramer encore en sous-section du §4 ; transposée « A^T » ; 3 méthodes sans exemple.
- Exercice « Concours PT » : même matrice (1, 1, 1 / 1, 2, m / 1, 4, m²) et mêmes questions que l'EXO 03 → remplacé par
  un problème original (matrices circulantes). L'EXO 03 (devenu EXO 04) est gardé.
- EXO 04 et EXO 05 (comatrice, Cramer, hors programme) : fusionnés en un seul EXO 11 « pour aller plus loin », dont
  l'énoncé rappelle les formules ; les cofacteurs y sont notés c_{ij} (C_j désigne désormais les colonnes).
- Cartes corrigées (réponse seule, sauf n° 20) :
  - n° 10 (cofacteur) : mineur noté Δ_{ij} comme dans le cours et `det2a`, comatrice signalée hors programme ;
  - n° 11, 12 (comatrice, Cramer) : préfixe normalisé « Hors programme en PTSI (et en PT) : » et méthode du programme ;
  - n° 13 : « libre ⟺ det ≠ 0 » n'a de sens que pour **n** vecteurs de Kⁿ (sinon, un rang) ;
  - n° 20 : question « Sign de … » → « Signe de … » (`q_nouvelle`, réponse inchangée ; malgré les ajouts en fin de deck,
    la progression est conservée : question reformulée, réponse inchangée, voisines reconnues) ;
  - n° 24 (produit mixte) : préciser « dans une base orthonormée directe » (faux dans une base quelconque).

## Couverture du programme (PTSI, « Matrices et déterminants », partie B ; repris à l'identique en PT)

| Capacité du programme | Avant | Après |
|---|---|---|
| Lien avec le produit mixte (n = 2, 3), aire et volume orientés | absent (une phrase) | §1 : trois propriétés lues sur la figure, exemple aire + volume |
| Théorème-définition (linéarité par colonne, antisymétrie, det Iₙ = 1), admis pour n ≥ 4 | §1, sans preuve | §2 : preuve pour n = 2, idée pour n = 3 (Sarrus), exemple sur la linéarité |
| Deux colonnes égales ⟹ det nul ; det(λA) | §2 (lignes) | §3 + démonstrations, exemple |
| Effet des opérations élémentaires **sur les colonnes** ; calcul par ces opérations | §2-§3 (lignes) | §4 + démonstrations, méthode, 2 exemples ; méthodes 2-3 ; EXO 02 |
| Déterminant d'une matrice triangulaire | énoncé | §4 + démonstration |
| A inversible ⟺ det A ≠ 0 ; det(AB) (admis), det(A⁻¹) | énoncés | §5 + démonstration, exemple à paramètre, raisonnements sans calcul ; EXO 06 |
| det(Aᵀ) = det A (admis) ; mêmes propriétés pour les lignes | énoncé | §6 + exemple 4 × 4 par les lignes ; EXO 03 |
| Développement suivant une ligne ou une colonne (non exigible) | §1 | §7 : formules, damier, idée de preuve, exemple 4 × 4, stratégie ; EXO 05 |
| Outil informatique pour les calculs lourds | absent | §7 : NumPy / SymPy |
| Déterminant d'une famille dans une base, caractérisation des bases | une ligne (§4) | §8 + démonstration, 3 exemples, orientation ; méthode 7, EXO 07 |
| Déterminant d'un endomorphisme, automorphismes, traduction des propriétés | absent | §9 + démonstrations, figure, 4 exemples ; méthode 8, EXO 10 |
| Hors programme : comatrice, Cramer, formes multilinéaires alternées, groupe symétrique, changement de base | comatrice et Cramer dans le §4 | regroupés en fin de cours ; EXO 11 « pour aller plus loin » |

## Sections du cours
§1 Aire et volume orientés · §2 Définition du déterminant · §3 Premières conséquences · §4 Opérations élémentaires sur les
colonnes · §5 Inversibilité, produit, inverse · §6 Transposée et opérations sur les lignes · §7 Développement suivant une
ligne ou une colonne · §8 Déterminant d'une famille de vecteurs · §9 Déterminant d'un endomorphisme · Pour aller plus loin.

## Figures (calculées, contrôlées en clair et en sombre et dans la copie du site à 390 px)
1. Linéarité par rapport au second vecteur : parallélogrammes (u, v) et (u, w) empilés, d'aires 6 et 4, et (u, v + w),
d'aire 10 (§1). 2. Triangle ABC et son image par f(x, y) = (x + 2y, 2x + y), de déterminant −3 : aire triplée, sens de
parcours inversé (§9). (Les figures de `det2a` — cisaillement, carré unité — n'ont pas été reprises.)

## Méthodes (10)
Petit déterminant direct · triangulation par les colonnes · factorisation à paramètre · développement creux · pivot sur les
lignes · inversibilité selon un paramètre (et système) · base par le déterminant · déterminant d'un endomorphisme ·
raisonnements sans calcul · aires, volumes, alignement, coplanarité.

## Exercices (12)
Gardés : EXO 01 (+ Sarrus), EXO 03 (ancien 02, 4 × 4), EXO 04 (ancien 03), EXO 09 (ancien 06, Vandermonde 3 × 3),
EXO 11 (anciens 04 + 05, hors programme). Nouveaux : EXO 02 (opérations sur les colonnes, dont 3a + 1), EXO 05
(développements, tridiagonal Dₙ = n + 1 conjecturé), EXO 06 (raisonner sans calculer : det(3A), A² = A, A³ = −A en taille
impaire, matrices non semblables), EXO 07 (base selon un paramètre dans ℝ³ et ℝ₂[X], orientation), EXO 08 (aire,
coplanarité, volume, aire d'une image), EXO 10 (endomorphismes : (X + 1)P′ − 2P de noyau Vect((X + 1)²), P(2X) de
déterminant 2^{n(n+1)/2}, M + Mᵀ, symétrie oblique) ; Concours PT « Matrices circulantes d'ordre 3 » (det =
(a + b + c)(a² + b² + c² − ab − bc − ca) = a³ + b³ + c³ − 3abc, structure aI + bJ + cJ², stabilité par produit,
endomorphisme M ↦ AM de matrice Aᵀ, inverse circulant).

## Cartes ajoutées (14)
Les trois propriétés ; opérations sur les colonnes ; deux colonnes égales ; Sarrus (taille 3 seulement) ; développement
suivant une colonne ; déterminant d'une famille ; caractérisation des bases ; déterminant d'un endomorphisme ; ce que dit
det f ; aire d'un triangle et volume d'un tétraèdre ; matrices semblables ; det(−A) ; symétrie, projecteur, rotation ;
ce que le programme exclut.

## Notations
Celles de `det2a` et `matrices` : colonnes C_j, lignes L_i, mineurs Δ_{ij}, \det\nolimits_{\mathcal B}, \operatorname{Mat}_{\mathcal B}(f),
P_{\mathcal B\to\mathcal B'}, Aᵀ (A^\top), barres verticales (vmatrix) ; vecteurs fléchés seulement dans le cadre
géométrique du §1 (comme `geometrie`, `geo3d`).

## Doutes et remarques pour l'intégration
- La consigne citait « forme n-linéaire alternée » ; le programme déclare **hors programme** le vocabulaire des formes
  multilinéaires alternées. Le cours énonce la caractérisation (linéarité par colonne, antisymétrie, det Iₙ = 1) sans ce
  vocabulaire, qui n'apparaît qu'en fin de chapitre.
- Ordre de la navigation : `det` est placé avant `ev` et `applin` dans `CHAP_GROUPS`, alors que ses §8-§9 utilisent bases,
  coordonnées et endomorphismes (renvois explicites). Le programme les traite dans l'ordre inverse ; je suggère de
  déplacer `det` après `applin` (et `matrices` aussi, qui s'appuie sur `applin`), à arbitrer.
- Le programme de PT reprend mot pour mot la partie « Déterminants » : `det` (1ʳᵉ année) est désormais complet, `det2a`
  reste la révision de 2ᵉ année (exemples tous différents ; blocs, tridiagonaux par récurrence, Vandermonde en taille n
  y restent, avec renvoi).
- Après application au dépôt : `python3 tools/replier_panneaux.py`, `validate.py`, `check_js.py`, bump de `CACHE_VERSION`.
