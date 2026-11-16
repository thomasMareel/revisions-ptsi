# Revue — `oemvide` (prefix `oev`), « Ondes électromagnétiques dans le vide » (2ᵉ année, programme PT 4.5)

Fichiers produits (dans `EM/`) : `oev-cours.src.html`, `oev-meth.src.html`, `oev-exos.src.html`,
`oev-cartes-corr.json` (1 correction), `oev-cartes-ajout.js` (9 cartes). Travail : `oev-exos-nouveaux.html`,
`orig/` (panneaux et cartes d'origine), scripts communs `oem3_*.py`.

Contrôles : `verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`,
`larges` vides, aucune erreur JS ; `corriger_cartes.py --essai` (1 réponse) et `ajouter_cartes.py --essai`
(40 → 49) sans erreur.

## 1. Relecture du cours : ce qui a été corrigé

Démonstrations (d'Alembert, solution générale 1 D, relation de structure, notation complexe), sens de
rotation des polarisations, valeurs du spectre, éclairements (Soleil, téléphone, Wi-Fi, laser), critère
d'onde plane locale (a²/8r) : **refaits, justes**. Corrections :

| Où | Problème | Correction |
|---|---|---|
| §3 | Capacité « décrire la structure d'une **onde plane** » (pas seulement progressive) non traitée. | Sous-section « Structure d'une onde plane quelconque » : transversalité démontrée par (MG) et la composante longitudinale de (MA) ; relation de structure valable seulement pour chaque composante progressive. |
| §6 | Polarisations circulaire et elliptique titrées « (complément) ». | « (hors programme, pour aller plus loin) ». |
| §6 | Capacité « mettre en évidence une polarisation rectiligne » sans expérience ; rien sur les ondes centimétriques. | Exemple chiffré : émetteur à cornet 10 GHz, grille de fils (axe de transmission **perpendiculaire** aux fils), extinction et loi de Malus. Bloc « Au programme » mis à jour. |
| §7 | Bilan local d'énergie de l'OPP non vérifié (capacité « étude énergétique »). | Bloc dépliable : vérification de ∂u/∂t + div Π = 0 pour une OPP quelconque. |
| §3 / §7 | Incohérence : B₀ ≈ 3 µT « quinze fois » moins que le champ terrestre au §3, « dix fois » au §7. | « une quinzaine de fois » partout (5·10⁻⁵ / 3·10⁻⁶ ≈ 15). |
| §4 | Nombre d'onde noté σ, comme la conductivité du chapitre suivant. | Mention « notation de l'optique, à ne pas confondre avec la conductivité σ ». |
| §2 | Renvoi « exercice 7 » (renumérotation). | « exercice 11 » (deux renvois). |
| §3, §4 | Trois formules en ligne trop longues. | Passées en bloc ou reformulées. |

## 2. Couverture du programme (4.5, vide) avant → après

| Capacité exigible | Avant | Après |
|---|---|---|
| Solutions de d'Alembert à 1 D | cours §2, méthode 2, exercice | inchangé + carte |
| Structure d'une onde plane et d'une OPP | OPP seulement | + onde plane quelconque (§3), méthode 5, exercice 4, carte |
| Caractère idéal de l'OPPM | cours §8, cartes | + méthode 10, carte |
| Domaines du spectre et applications | cours §5, 2 cartes | + exercice 2, méthode 10, 2 cartes |
| Poynting et énergie volumique d'une OPPM | cours §7, méthodes, exercices | inchangé |
| Étude énergétique d'une OPP | cours §7, exercices 1, 3 | + bilan local (§7), exercice 9, carte |
| Reconnaître une polarisation rectiligne ; polariseurs | cours §6, exercices | + méthodes 6-7 |
| Mettre en évidence une polarisation rectiligne | application qualitative | + exemple ondes centimétriques (§6), exercice 7 (TP), 2 cartes |

## 3. Méthodes (7 → 10, toutes avec exemple éclair chiffré)

1 équation de propagation · 2 reconnaître une OPP · 3 B à partir de E · 4 notation complexe ·
5 vérifier qu'un champ est électromagnétique (**nouvelle**) · 6 état de polarisation (circulaire signalée
hors programme) · 7 polariseur, Malus et mise en évidence (grille) · 8 grandeurs énergétiques moyennes ·
9 de la puissance de la source au champ · 10 spectre et validité du modèle de l'OPPM (**nouvelle**).

## 4. Exercices (8 → 12, dont le Concours PT)

Tous les anciens corrigés recalculés : **justes**. Nouveaux corrigés vérifiés (sympy et Python).

| N° | Titre | Statut |
|---|---|---|
| 01 ★ | Lire une onde plane progressive monochromatique | ancien 01 |
| 02 ★ | Le spectre électromagnétique au quotidien | **nouveau** |
| 03 ★ | Une impulsion régressive | ancien 02 |
| 04 ★★ | Ces champs sont-ils des ondes électromagnétiques ? | **nouveau** (champ longitudinal, mauvaise dispersion, onde plane stationnaire, impulsion à 45°) |
| 05 ★★ | Onde oblique et notation complexe | ancien 03 |
| 06 ★★ | Faire passer la lumière entre deux polariseurs croisés | ancien 05 |
| 07 ★★ | TP : mettre en évidence la polarisation d'une onde centimétrique | **nouveau** |
| 08 ★★ | Émetteur radio : onde sphérique et onde plane locale | ancien 06 |
| 09 ★★ | Bilan d'énergie local et faisceau laser de découpe | **nouveau** |
| 10 ★★ | Une onde polarisée circulairement (**hors programme**) | ancien 04, titre signalé |
| 11 ★★★ | Deux ondes contra-propagatives | ancien 07 |
| Concours | Réception d'une chaîne de télévision par satellite | question C3 signalée « hors programme : polarisation circulaire » |

## 5. Cartes

- Corrigée : **24** (polarisation circulaire) : préfixe « Hors programme en PT (pour aller plus loin) : ».
- Ajoutées (9) : structure d'une onde plane non progressive, d'Alembert ne suffit pas, mise en évidence d'une
  polarisation rectiligne, grille de fils, éclairement et impédance du vide (form), bilan local dans le vide
  (form), domaines du spectre (val), repères ν ↔ λ (val), validité du modèle de l'OPPM.

## 6. Notations

Convention `e^{i(ωt − k·r)}` (∂/∂t → iω, ∇ → −ik), identique à `mxw` et `oec` ; `Π`, `u_em`, `I` pour
l'éclairement ; (MG), (MΦ), (MF), (MA) comme dans `mxw`. Le nombre d'onde `σ = 1/λ` est conservé (usage de
l'optique), avec mise en garde.

## 7. Doutes

- Le programme ne cite que la polarisation rectiligne : circulaire et elliptique, l'exercice 10 et la
  question C3 du concours sont gardés mais signalés hors programme.
- L'exercice 7 (TP) suppose un récepteur sensible à la seule composante parallèle à son axe : c'est le cas
  des cornets usuels, à préciser oralement si le matériel du lycée diffère.
