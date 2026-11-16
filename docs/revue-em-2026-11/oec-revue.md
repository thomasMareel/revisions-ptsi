# Revue — `oemcond` (prefix `oec`), « Ondes électromagnétiques et conducteurs » (2ᵉ année, programme PT 4.5)

Fichiers produits (dans `EM/`) : `oec-cours.src.html`, `oec-meth.src.html`, `oec-exos.src.html`,
`oec-cartes-corr.json` (23 corrections), `oec-cartes-ajout.js` (8 cartes). Travail : `oec-exos-nouveaux.html`,
`orig/` (panneaux et cartes d'origine), scripts communs `oem3_*.py`.

Contrôles : `verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`,
`larges` vides, aucune erreur JS (un débordement à 390 px apparu après une retouche a été corrigé) ;
`corriger_cartes.py --essai` (23 réponses) et `ajouter_cartes.py --essai` (40 → 48) sans erreur.

## 1. Relecture du cours : ce qui a été corrigé

Calculs refaits (Python) : épaisseurs de peau (table du cuivre, aluminium), rapport j_D/j, phase de B
(retard π/4), v_φ, réflexion (r = −1, champs totaux réels, j_s, nœuds), énergie de l'onde stationnaire,
modes de cavité, pression de radiation, plasma (f_p ≈ 9√n) : **justes**. Les problèmes sont de structure et
de programme :

| Où | Problème | Correction |
|---|---|---|
| §1 | **Contradiction** : le bloc « Au programme » annonçait le modèle de Drude « regroupé en fin de chapitre », mais le §1 était le modèle de Drude (hors programme) ; la loi d'Ohm exigible n'en était qu'une conséquence. | Nouveau §1 « Le conducteur ohmique » : loi d'Ohm locale admise (`σ` réelle), domaine de validité, ordres de grandeur, effet Joule, application chiffrée. Le modèle de Drude (avec la conductivité complexe) devient la section « Pour aller plus loin · Modèle de Drude (hors programme) », avant le plasma. |
| §7 | Guide d'onde entre deux plans présenté comme exigible (bloc « Au programme » et §7) alors qu'il n'est pas au programme PT 4.5. | Déplacé dans « Pour aller plus loin · Dispersion… » comme exemple de milieu dispersif. |
| §7 | Capacité expérimentale « mettre en œuvre un dispositif d'étude des ondes centimétriques » absente. | Sous-section « Étudier une onde centimétrique en TP » (émetteur Gunn, détection quadratique, plaques, grille) + exemple chiffré de mesure de λ par les nœuds. |
| §4 | Aspects énergétiques de l'effet de peau seulement en exercice. | Encadré « Bilan d'énergie » : P_S = σE_s²δ/4 = flux moyen de Poynting entrant. |
| §2-§7 | Notation `σ₀` (conductivité statique de Drude) utilisée dans toute la partie exigible. | `σ` (20 remplacements), comme dans `mxw` et le programme ; `σ₀` réservée au modèle de Drude. §2 renommé « Neutralité et ARQS magnétique » (l'effet Joule passe au §1). |
| §7 | Pression de radiation « (complément) ». | « (complément hors programme) ». |
| §6 | Pas d'application chiffrée. | Application : j_s ≈ 0,53 A·m⁻¹, B double sur la plaque, nœuds tous les 1,5 cm à 10 GHz. |
| Bloc « Au programme » | Liste à reprendre. | Réécrit (loi d'Ohm, ARQS, atténuation, métal parfait, réflexion, onde stationnaire, cavité, ondes centimétriques, hors-programme nommé, intensité à travers un segment hors programme). |
| §3, §4, §7 | Trois formules en ligne trop longues. | Passées en bloc. |

## 2. Couverture du programme (4.5, conducteurs) avant → après

| Capacité exigible | Avant | Après |
|---|---|---|
| Loi d'Ohm locale (sans modèle), effet Joule | via Drude (§1-§2) | §1 exigible, méthode 1, carte |
| Grandeur caractéristique d'atténuation (épaisseur de peau) : établir, interpréter | §3-§4, méthodes, exercices | + méthodes 2-4, exercice 1 |
| Aspects énergétiques dans un milieu ohmique | exercice 3 | + encadré §4, méthode 5, exercice 5, carte |
| Nullité des champs dans un métal parfait | §5, méthode 5 | + méthode 6, exercice 2 (onde rasante) |
| Établir l'onde réfléchie (relations de passage fournies) | §6, exercices | + méthode 7 |
| Interpréter qualitativement les courants localisés en surface | §5-§6 | + exercice 2, carte |
| Caractériser une onde stationnaire | §6-§7, exercices | + méthode 8, carte |
| Cavités à une dimension : quantification des modes | §7, exercice 7 (ancien) | + méthode 9, exercice 7 (nouveau) |
| Ondes centimétriques : dispositif d'étude | exercice 5 (ancien) seul | + §7, méthode 10, exercice 7, carte |

## 3. Méthodes (7 → 10, toutes avec exemple éclair chiffré)

1 justifier les simplifications dans un conducteur · 2 équation de diffusion · 3 relation de dispersion et δ ·
4 champs réels et interprétation · 5 bilan d'énergie (R_s) · 6 métal parfait et relations de passage ·
7 onde réfléchie · 8 onde stationnaire · 9 modes d'une cavité · 10 mesure de λ en ondes centimétriques.
Les anciennes méthodes « conductivité complexe » et « plasma » deviennent une notice « Hors programme,
souvent guidé » ; le guide d'onde n'a plus de méthode.

## 4. Exercices (8 → 12, dont le Concours PT)

Anciens corrigés recalculés : **justes**. Nouveaux corrigés vérifiés (sympy et Python).

| N° | Titre | Statut |
|---|---|---|
| 01 ★ | Épaisseur de peau : du sous-marin à la plaque à induction | **nouveau** |
| 02 ★ | Onde rasante le long d'un plan métallique | **nouveau** (σ_s, j_s, conservation de la charge en surface) |
| 03 ★★ | Blindage d'un boîtier électronique | ancien 02 (σ₀ → σ) |
| 04 ★★ | Pertes par effet Joule et résistance de surface | ancien 03 (σ₀ → σ) |
| 05 ★★ | Bilan d'énergie local dans un conducteur : Poynting et effet Joule | **nouveau** |
| 06 ★★ | Mesure de longueur d'onde sur un banc micro-ondes | ancien 05 |
| 07 ★★ | TP : résonances d'une cavité à miroir mobile | **nouveau** |
| 08 ★★★ | Modes propres d'une cavité plane | ancien 07 (Q6 pression signalée hors programme) |
| 09 ★ | Modèle de Drude appliqué à l'aluminium (**hors programme**) | ancien 01 |
| 10 ★★ | Black-out radio d'une capsule (plasma : **hors programme**) | ancien 04 |
| 11 ★★ | Voile solaire et pression de radiation (**complément hors programme**) | ancien 06 |
| Concours | Du miroir métallique réel à la cavité résonante | partie A signalée « modèle de Drude : hors programme, guidé » ; σ à partir de A2 |

Les exercices hors programme sont regroupés en fin de liste (avant le concours), d'où la reprise à ★ pour
l'exercice 9. Renvois vérifiés : cours §4 → « exercices 4 et 5 » ; §5 → « question C4 » ; exercice 1 → « exercice 4 ».

## 5. Cartes

- Corrigées (questions inchangées), 23 :
  - préfixe « Hors programme en PT (pour aller plus loin) : » : 0, 1, 2, 3, 4 (Drude), 19 à 26 (plasma),
    38 (pression de radiation), 39 (guide d'onde) ; les réponses en Unicode (2, 19, 21-24, 38) sont
    réécrites en `\( … \)` pour que le préfixe ne soit pas mathématisé ;
  - notation σ₀ → σ dans 8 cartes **justes** de la partie exigible (5, 6, 7, 8, 9, 10, 12, 15), pour la
    cohérence avec le cours (demande explicite de notations homogènes). **À arbitrer** : ces 8-là peuvent être
    retirées du lot si l'on préfère ne toucher aucune carte juste.
- Ajoutées (8) : loi d'Ohm et validité (form), bilan d'énergie de l'effet de peau (form), résistance de
  surface et fil en HF (form), nœuds et ventres devant un miroir, mesure de λ en ondes centimétriques, j_s
  comme limite du courant volumique, épaisseur de peau de l'eau de mer (val), cuivre conducteur parfait à 10 GHz.

## 6. Notations

`σ` conductivité, `σ₀` conductivité statique de Drude, `σ_s` charge surfacique, `j⃗_s` courant surfacique,
`n⃗` normale **sortante** du métal ; convention `e^{i(ωt − k̲z)}`, `k̲ = k′ − ik″` (identique à `oev`, `mxw`).
Divergence signalée : la charge surfacique est `σ` dans `estat2a` et au §5 de `mxw`.

## 7. Doutes

- 23 cartes corrigées dans un même lot que 8 ajouts : d'après la règle de `flashLoadState`, une carte dont
  seule la réponse change garde son état si sa question est reconnue ; prévenir l'utilisateur qu'au pire ces
  cartes repartent de zéro.
- Guide d'onde et plasma classés hors programme d'après le texte 4.5 (seules les cavités à une dimension et
  les ondes centimétriques y figurent) ; à confirmer si un professeur les traite.
- Chapitre non renommé.
