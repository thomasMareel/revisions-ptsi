# Revue `magnetostat` (prefix `mgs`) — Magnétostatique : théorème d'Ampère

Fichiers produits (dans `EM/`) : `mgs-cours.src.html`, `mgs-meth.src.html`, `mgs-exos.src.html`,
`mgs-cartes-ajout.js` (pas de `mgs-cartes-corr.json` : aucune carte fausse) ; figure recalculée : `figs_mgs_em.py`
(→ `figs_mgs_em.json`) ; vérifications : `verif_mgs.py` ; scripts : `_edit_mgs_cours.py`, `_longues.py`,
`_assemble_mgs_exos.py`, `_longues3.py`.
Contrôles : `verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges`
vides, aucune erreur JS, pas de débordement ; nouvelle figure regardée en capture (1440 px) ; `ajouter_cartes.py
--essai` : 19 → 33 cartes.

## Cours (relecture complète)
Calculs refaits : vitesse de dérive (0,8 mm·s⁻¹), fil épais, B à 1 cm de 1 A (20 µT), câble coaxial, solénoïde de TP
(2,5 mT ; 80 A pour 1 T), tore, cavité (μ₀/2 j⃗ ∧ OO′⃗), orientation du contour ABCD (normale +e⃗_z, nℓI compté
positivement), sens des flèches des figures (● en haut ⇒ B⃗ vers la droite), ordres de grandeur du tableau.

Erreurs corrigées :
1. **§2, spire seule** : « seul un point de l'axe a un champ forcément axial » est faux — le plan de la spire est plan
   de symétrie des courants, donc \(\vec B\) y est aussi axial. Corrigé, avec la forme générale
   \(\vec B=B_r(r,z)\,\vec e_r+B_z(r,z)\,\vec e_z\) (pas de composante orthoradiale).
2. **Figure du §3 (carte spire / solénoïde)** : cadrage faux — panneaux décentrés, échelles différentes sur les deux
   axes (75 px/unité en horizontal, 57,5 en vertical : lignes déformées), solénoïde coupé à droite (dernière spire
   hors du cadre et en partie hors de la figure). Recalculée (champ exact d'une spire par intégrales elliptiques,
   Runge-Kutta, échelle isotrope, lignes fermées tracées une fois) : 16 Ko au lieu de 35 Ko ; légende précisée.
3. **§5, câble coaxial** : « ne rayonne pas de champ magnétique » (impropre en statique) → « ne crée aucun champ » ;
   champ dans l'âme et dans la gaine \(B_\theta=\frac{\mu_0I}{2\pi r}\frac{c^2-r^2}{c^2-b^2}\) écrits explicitement.
4. **Hors programme** : moment magnétique \(\vec m\) → \(\vec{\mathcal M}\), couple \(\vec\Gamma=\vec{\mathcal M}\wedge\vec B\)
   (notations du groupe).
5. 4 formules en ligne trop longues passées en bloc (vitesse de dérive, cavité, Stokes) ou raccourcies.

Compléments (sections sans exemple traité, capacités peu illustrées) :
- §3 « Exemple — vérifier et exploiter la carte du solénoïde » (plans de symétrie / d'antisymétrie sur la figure,
  sens par la main droite, tube de champ : 2,5 mT → 125 µT quand la section passe de 1 à 20 cm²).
- §4 « Exemple — compter les courants enlacés » (3 − 5 + 20 × 0,20 = 2 A ; fil extérieur : circulation nulle).
- §6 encadré « Validité du modèle infini » (résultat fourni de Biot et Savart : 2 % d'écart au centre pour L = 10R).
- §7 « Exemple — champ à l'extrémité d'un long solénoïde » : B_z = μ₀nI/2 sur toute la face de sortie, établi sans
  Biot et Savart (superposition des deux moitiés + symétrie par rapport au plan de coupe), lien avec le flux (§3).

## Méthodes (`mgs-meth.src.html`) — 5 → 10, chacune avec étapes, exemple éclair chiffré et piège
1 intensité à partir de j⃗ (9,4 A) · 2 direction et variables de B⃗ (spire) · **3 reconnaître les cas où Ampère donne
le champ** (tube creux) · **4 choisir et orienter le contour, courant enlacé algébrique** · **5 fil épais / câble**
(2,0 mT ; 1,0 mT) · **6 solénoïde et bobine torique** (1,3 mT ; 2,0 mT) · 7 superposition (deux fils, 40 µT) ·
**8 conservation du flux** (tube : 5 → 1 mT) · 9 lire et vérifier une carte (écartement ∝ r autour d'un fil) ·
**10 ordre de grandeur** (Œrsted : 5 A à 5 cm). Les 5 méthodes d'origine sont reprises (reformulées).

## Exercices (`mgs-exos.src.html`) — 5 → 11 (10 numérotés + Concours PT)
| n° | Titre | Niveau | Origine |
|---|---|---|---|
| 01 | **Symétries, courants enlacés et carte de champ de deux fils** | ★☆☆ | nouveau |
| 02 | Densité de courant non uniforme | ★☆☆ | ancien 01 (notation I_enlacé) |
| 03 | Bobine torique à section rectangulaire (L ≈ 0,41 mH) | ★☆☆ | ancien 02 |
| 04 | **Câble coaxial en courant continu : champ dans les quatre zones** (flux, 0,28 µH·m⁻¹) | ★★☆ | nouveau |
| 05 | **Plaque épaisse parcourue par un courant** (barre omnibus, 6,3 mT ; deux plaques ↔ condensateur plan) | ★★☆ | nouveau |
| 06 | **Concevoir un solénoïde** (4 couches, j ≈ 3,2 A·mm⁻², validité du modèle, sens, champ terrestre) | ★★☆ | nouveau |
| 07 | Cavité dans un conducteur : un champ uniforme | ★★☆ | ancien 03 |
| 08 | Deux solénoïdes coaxiaux en sens contraires : flux de retour et blindage actif | ★★☆ | ancien 04, **refait (Q2, Q3)** |
| 09 | Ligne bifilaire à courant continu : champ sous la ligne | ★★☆ | ancien 05 (« concours ») |
| 10 | **Faisceau de protons : répulsion électrique et pincement magnétique** (rapport v²/c²) | ★★★ | nouveau |
| CPT | **Les champs magnétiques d'un tokamak** (4 parties : tore, fil épais, lignes hélicoïdales et facteur q, énergie) | ★★★ | nouveau |

- **Ancien 04** : Q2 concluait que n₁ = n₂ donnait « une région protégée du champ de la bobine (enceinte blindée) »,
  interprétation sans objet (sans bobine, pas de champ à protéger). Remplacé par le calcul des flux Φ₁, Φ₂, la
  condition n₁R₁² = n₂R₂² (flux de retour dans la couronne) et le blindage actif des IRM ; Q3 (n₁ = 2n₂, R₂ = √2 R₁)
  rattachée à cette condition.
- **Ancien 05** : présenté comme « Concours PT » (classe concours mais numéro « EXO 05 », 3 questions, pas d'encadré
  source) → exercice ordinaire ★★☆ renommé ; calculs vérifiés (20 mT, 1,6 mT, 1 µT).
- Nappes de courant (courants surfaciques) volontairement absentes : non introduites par le programme en
  magnétostatique ; la « plaque épaisse » (courant volumique) en tient lieu.
- Concours : valeurs d'ordre de grandeur publiques d'ITER (R₀ = 6,2 m, a = 2,0 m, 18 × 134 spires × 68 kA → 5,3 T ;
  15 MA → B_P(a) = 1,5 T ; q ≈ 1,1 dans le modèle du cylindre uniforme, comparé au q ≈ 3 réel dans la correction).

## Cartes
- Les 19 cartes sont justes : aucune correction.
- **Ajouts** (`mgs-cartes-ajout.js`, 14 cartes) : surface d'Ampère indifférente, bobine de N spires enlacée, sens du
  champ d'un solénoïde, resserrement des lignes, lignes et plans de symétrie, champ dans le plan d'une spire,
  cylindre plein (forme vectorielle, form), champ dans un coaxial (form), extrémité d'un solénoïde semi-infini,
  validité du modèle infini, deux fils opposés en 1/r², solénoïde de TP (val), LHC et record (val), Gauss ↔ Ampère.

## Couverture du programme (4.2) : avant → après
| Capacité | Cours | Méthode | Exercice | Carte |
|---|---|---|---|---|
| j⃗, intensité = flux de j⃗, distributions volumique et linéique | §1 | M5 → M1 | 01 → 02, 04, 10, CPT | 0-2 |
| Symétries et invariances des courants | §2 | M1 → M2 | — → 01, 05, CPT | 3-5 → + spire, lignes |
| Identifier les situations où Ampère donne B | §4 | (M2) → M3 | — → 01 | 18 → + Gauss/Ampère |
| Choisir, orienter contour et surface | §4 | M2 → M4 | 01-05 → + 01, 04, 05 | 7 → + surface, bobine |
| Superposition | §7 | M3 → M7 | 03, 04, 05 → 01, 07, 08, 09 | 14 → + 1/r², extrémité |
| Ordres de grandeur de B | §8 | — → M10 | 05 → 04, 05, 06, 09, CPT | 15, 16 → + TP, LHC |
| Fil épais (établir) | §5 | M2 → M5 | 01, 05 → 02, 04, 09, 10, CPT | 9, 10 → + vectoriel, coaxial |
| Solénoïde infini (établir, extérieur nul admis) | §6 | — → M6 | 04 → 06, 08 (tore : 03, CPT) | 11, 12 → + sens, validité |
| Lignes et tubes de champ : orienter, intensité, compatibilité | §3 | M4 → M8, M9 | 04 (Q3) → 01, 08, CPT | 6 → + resserrement |

## Notations, divergences entre chapitres, doutes
- Notations : \(\vec B\), \(\mu_0\), \(\vec j\), \(I\), \(I_{\text{enlacé}}\), \(\Phi\) (flux), \(\vec{\mathcal M}\), \(\vec\Gamma\),
  main droite pour orienter contours et normales.
- **Divergence** : `maxwell` écrit \(I_{enl}\) (sans `\text`) ; `mgs` écrit \(I_{\text{enlacé}}\), comme `emag`
  (« I_{enlacé} ») : à harmoniser dans `mxw`.
- **Divergence** : `emag` (1ʳᵉ année, version actuelle du site) note le moment magnétique \(\vec m\) ; `mgs` passe à
  \(\vec{\mathcal M}\), conformément aux consignes du groupe.
- La figure du §6 (contour ABCD) et celle du §5 (fil épais) sont justes et gardées.
- Pas de renommage du chapitre.
