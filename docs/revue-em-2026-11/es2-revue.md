# Revue `estat2a` (prefix `es2`) — Électrostatique : champ, potentiel, théorème de Gauss

Fichiers produits (dans `EM/`) : `es2-cours.src.html`, `es2-meth.src.html`, `es2-exos.src.html`,
`es2-cartes-corr.json`, `es2-cartes-ajout.js` ; vérifications numériques : `verif_es2.py` ;
scripts d'assemblage : `_edit_es2_cours.py`, `_longues.py`, `_assemble_es2_exos.py`, `_longues2.py`.
Contrôles : `verif_src.py` sans erreur ni « attention » sur les trois panneaux ; `apercu_src.py` à 390 et 1440 px :
`merr`, `brut`, `larges` vides, aucune erreur JS, pas de débordement ; `corriger_cartes.py --essai` (6 réponses)
et `ajouter_cartes.py --essai` (40 → 50 cartes) sans erreur.

## Cours (relecture complète, calculs refaits)
Tous les calculs et exemples ont été refaits (sympy / numpy) : champ sur la médiatrice (maximum en a/√2), boule
ρ₀(1 − r/R) (Q = πρ₀R³/3), disque (limites, écart 10 % à z = R/10), plan (flux des bases), récapitulatif (sphère
chargée en surface, couche), boule ρ₀r/R, potentiels (boule : V(0) = 1,5 V(R) ; fil ; plan), V = V₀(x² − y²)/a²,
condensateur (89 pF, 89 nC, 8,9 µC·m⁻², 44 µJ), électron sous 2 kV (2,7·10⁷ m·s⁻¹), couche par Poisson, g₀/2
(altitude 0,41 R ≈ 2 600 km), ordres de grandeur (5·10¹¹ V·m⁻¹ pour l'hydrogène, rapport 10³⁶), effet de pointe,
capacité de la Terre (0,7 mF), dipôle, script Python (ordre des sorties de `np.gradient`). **Aucune erreur de
physique ni de calcul.** Renvois § vérifiés ; programme 4.1 (et Poisson/Laplace de 4.3) entièrement couvert.

Corrections et compléments ciblés :
- **Notation** : le potentiel gravitationnel était noté Φ (§11), lettre qui désigne le flux au §5 → \(V_g\).
- **§4** (aucun exemple traité) : « Exemple — écartement des lignes et intensité du champ d'un fil » (conservation
  du flux dans un tube, E ∝ 1/r retrouvé, 9,0·10⁴ puis 3,0·10⁴ V·m⁻¹), avec la limite de la lecture quantitative
  (carte méridienne d'une distribution de révolution : classement seulement qualitatif).
- **§5** (aucun exemple traité) : « Exemple — charge de la Terre déduite du champ de beau temps » (Gauss, Q ≈ −4,6·10⁵ C,
  σ ≈ −0,9 nC·m⁻², un électron pour 180 µm²).
- 5 formules en ligne trop longues pour le téléphone passées en bloc (§7 circulation, §9 vitesse, §10 divergence et
  laplacien, exemple du §5).

## Méthodes (`es2-meth.src.html`) — 8 → 10 méthodes, chacune avec étapes, exemple éclair chiffré et piège
1 direction et variables (exemple : deux charges, 6,4·10² V·m⁻¹) · **2 superposition (nouvelle : anneau)** ·
3 Gauss, **variante gravitationnelle** (coquille, g lunaire 1,6 m·s⁻²) · 4 Maxwell-Gauss (problème inverse) ·
5 champ ↔ potentiel (boule : 1,9·10² V) · 6 Poisson/Laplace (charge d'espace entre deux plans : 1,4 V) ·
7 **capacité du condensateur plan** (recentrée sur le programme) · **8 énergie potentielle qV (nouvelle : proton
sous 10 kV)** · 9 lire une carte · 10 Python.
Corrigé au passage : l'ancienne méthode 5 tirait les charges des armatures de « σ = ε₀Eₙ côté isolant » et l'ancienne
méthode 6 raisonnait sur l'armature intérieure de condensateurs cylindrique/sphérique (conducteurs à l'équilibre,
hors programme) : ces condensateurs sont désormais signalés hors programme dans un piège.

## Exercices (`es2-exos.src.html`) — 7 → 11 (10 numérotés + Concours PT)
(Le panneau comptait 7 exercices, pas 13.) Tous les corrigés existants ont été recalculés : justes.
| n° | Titre | Niveau | Origine |
|---|---|---|---|
| 01 | Symétries, invariances et charge totale | ★☆☆ | ancien 01 |
| 02 | **Quatre charges aux sommets d'un carré** (superposition discrète, V nul sur un plan d'antisymétrie, travail qV) | ★☆☆ | nouveau |
| 03 | Cylindre infini à densité croissante | ★★☆ | ancien 02 |
| 04 | Couche plane à profil sinusoïdal | ★★☆ | ancien 03 |
| 05 | **Modèle de Thomson de l'atome d'hydrogène** (Gauss, oscillateur, 120 nm, Earnshaw et Poisson, 22 eV) | ★★☆ | nouveau |
| 06 | **Condensateur plan et déviation d'un faisceau d'électrons** (capacité par superposition, qV, Uₘₐₓ ≈ 31 V) | ★★☆ | nouveau |
| 07 | Condensateur sphérique | ★★☆ | ancien 04, **adapté** |
| 08 | **Champ uniforme dans une cavité cylindrique** (superposition + Gauss, électron : 10 ns) | ★★☆ | nouveau |
| 09 | Planète à noyau dense | ★★☆ | ancien 05 |
| 10 | Carte de champ de deux charges inégales en Python | ★★★ | ancien 06 |
| CPT | Zone de charge d'espace d'une jonction PN | ★★★ | inchangé |

- **07 adapté** : l'énoncé reposait sur des « sphères conductrices » et la correction sur « l'intérieur du conducteur »
  (conducteurs en équilibre : hors programme) → armatures modélisées par deux sphères chargées en surface ; résultats
  identiques ; mention « effet de pointe » remplacée.
- Concours : une formule en ligne débordait à 390 px (ε = 11,7 × 8,85·10⁻¹² …) → raccourcie.
- 3 anciennes formules en ligne longues passées en bloc.

## Cartes
- **Corrections** (`es2-cartes-corr.json`, questions inchangées) : hors programme signalé en tête de réponse
  (« Hors programme en PT (pour aller plus loin) : ») pour 28 effet de pointe, 30 condensateur cylindrique,
  31 condensateur sphérique, 38 et 39 dipôle ; 14 relation de passage : « Non exigible en PT (relation fournie par
  les énoncés) : ». Les réponses 28 et 31, en Unicode, sont réécrites en \( … \) (phrase + formule).
- **Ajouts** (`es2-cartes-ajout.js`, 10 cartes) : champ extérieur d'une distribution sphérique, cylindre chargé en
  volume, condensateur plan (champ), disque sur l'axe, validité d'un modèle infini, champ atmosphérique (val),
  électronvolt (val), potentiel au centre d'une boule, Earnshaw, vitesse sous une tension U.

## Couverture du programme (4.1, et Poisson/Laplace de 4.3) : avant → après
| Capacité | Cours | Méthode | Exercice | Carte |
|---|---|---|---|---|
| Champ d'une distribution discrète, ordres de grandeur | §1 | — → M1, M2 | (10) → 02, 10 | 34, 35 → + champ atmosphérique |
| Distributions continues, décomposition, modèle infini, charge totale | §2 | M2 (charge) → M2, M3 | 01, 03 → + 08 | — → disque, modèle infini |
| Symétries et invariances | §3 | M1 | 01 → + 02, 08 | 0-3 |
| Potentiel (lien, charges ponctuelles, gradient, d.d.p.) | §7 | M4 → M5 | 03, 04 → + 02, 05 | 15-21 → + boule |
| Gauss : sphère, cylindre, plan ; extérieur d'une distribution sphérique | §5, §6 | M2 → M3 | 03, 07, 09 → + 05, 08 | 6-10 → + sphérique, cylindre |
| Capacité du condensateur plan | §8 | M6 (général) → M7 (plan) | **aucun** → 06 | 29, 32, 33 → + champ |
| Lignes, tubes, équipotentielles, compatibilité d'une carte | §4, §7 | M7 → M9 | 10 | 4, 5, 26, 27 |
| Capacité numérique (Python) | §12 | M8 → M10 | 10 | — |
| Énergie potentielle d'une charge (qV) | §9 | **aucune** → M8 | **aucun** → 02, 05, 06 | 22, 23 → + eV, vitesse |
| Gauss pour la gravitation | §11 | — → M3 | 09 | 36, 37 |
| Poisson et Laplace (4.3) | §10 | M3, M5 → M4, M6 | 04, CPT → + 05 | 11-13, 24, 25 → + Earnshaw |

## Notations, doutes
- Notations conformes au groupe : \(\vec E\), \(V\), \(\rho\), \(\sigma\), \(\lambda\), \(\varepsilon_0\), \(\Phi\) (flux),
  \(Q_{\text{int}}\), \(\vec{\mathcal G}\) et \(V_g\) (gravitation), \(\vec p\) (dipôle, hors programme).
- Les cartes 30, 31, 38, 39 gardent `cat:'form'` (l'outil ne modifie que q et a) : elles restent dans le filtre
  « Formules » du quiz alors qu'elles sont hors programme.
- Pas de renommage du chapitre.
