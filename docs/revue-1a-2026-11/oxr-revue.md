# Revue — « Oxydoréduction » (`oxred`, prefix `oxr`) — point 7, 2026-11-26

Reprise du travail d'un premier rédacteur interrompu : il n'avait produit que des scripts (données `oxr_chimie.py`,
outils SVG `oxr_svg.py`, calculs `oxr_calculs.py`) et six figures (`oxr_figs.py` → `oxr_figs.json`), sans aucun
panneau. Figures contrôlées et gardées, deux défauts corrigés (« ESH (référence absolue) » → « 0 V par convention » ;
libellés « x = 0,080 » et « x (mol·L⁻¹) » superposés sous l'axe de la figure d'équilibre). Tous ses calculs ont été
refaits (`oxr_calculs.py`, `oxr_calculs2.py`, `oxr_exos_calculs.py`).

## Fichiers produits (dans `AN1/`)
- `oxr-cours.src.html` (82 ko, assemblé par `construire_oxr.py` à partir de `oxr-cours.tpl.html` et `oxr_figs.json`) ;
- `oxr-meth.src.html` ; `oxr-exos.src.html` ;
- `oxr-cartes-corr.json` (7 réponses corrigées) ; `oxr-cartes-ajout.js` (8 cartes, à la fin) ;
- scripts : `oxr_figs.py` (figures), `oxr_calculs.py`, `oxr_calculs2.py`, `oxr_exos_calculs.py` (vérifications).

Contrôles passés : `verif_src.py` sans erreur ni « attention » sur les trois panneaux ; `apercu_src.py` à 390 et
1440 px : `merr`, `brut`, `larges` vides, aucune erreur JS, pas de débordement (scrollW = 390) ; captures du cours
regardées ; figures à aplats vues en clair et en sombre ; `corriger_cartes.py --essai` (7 corrigées) et
`ajouter_cartes.py --essai` (25 → 33) sans erreur.

## Erreurs trouvées et corrigées
**Cours**
- « Conditions standard : activités = 1, pression 1 bar, température = 298 K » : faux, l'état standard ne fixe pas
  la température (E° dépend de T, les tables le donnent à 298 K).
- Formule de Nernst « générale » sans les coefficients stœchiométriques (Cr₂O₇²⁻/2 Cr³⁺ demande [Cr³⁺]²).
- Critère « ΔE° entre 0 et 0,3 V : équilibre, ni totale ni négligeable » : imprécis ; remplacé par un tableau
  ΔE° → K° pour n = 1 et 2 et par la règle « comparer les E et non les E° quand ΔE° est petit ».
- L'électrolyse (hors programme PTSI) occupait la fin du §5 : déplacée dans « Pour aller plus loin ».
- Formules en `$$` sans `.formula`, F₂ composé en italique, terme « FEM » au lieu de « tension à vide » (programme).

**Méthodes** : panneau intitulé « OXYDORÉDUCTION & E-pH » (les diagrammes E-pH ont leur chapitre) ; méthode de
Nernst sans coefficients ; seulement 5 méthodes.

**Exercices**
- EXO 04 : Q1 demandait un schéma absent du corrigé (ajouté : notation conventionnelle et renvoi à la figure du §5) ;
  « f.é.m. peu changée par rapport à la valeur standard » → exactement la valeur standard (concentrations égales) ;
  formule en ligne qui débordait à 390 px (défaut préexistant, scrollW 446) coupée ; difficulté ★★★ → ★★☆.
- Ancien EXO 06 « Corrosion électrochimique » **remplacé** : le modèle (Cu²⁺ réduit sur un câble zinc-cuivre « dans
  une solution saline ») est physiquement trompeur (dans une corrosion galvanique, c'est O₂ ou H⁺ qui est réduit), et
  sa Q3 (protection contre la corrosion) relève de la 2ᵉ année (`electrochimie`).
- Ancien « Concours PT » (pile Daniell, une seule question B1) : doublon de l'EXO 04, **remplacé** par un vrai
  problème en quatre parties.
- Retouches : demi-équations écrites avec « = » et contrôlées par les n.o. (EXO 01), « Explique » → « Expliquer ».

**Cartes** (réponses seules, questions inchangées) : n° 6 (E° « à T = 298 K »), 7 (Nernst sans coefficients),
9 (« seules les espèces dissoutes » ont une activité : les gaz aussi), 17 (électrolyse : préfixe « Hors programme
en PTSI »), 18 (« état standard d'oxydoréduction … T = 25 °C » : faux), 19 (Nernst avec [Ox]/[Red] non divisés par
c°, sans préciser solides et solvant), 21 (frontière verticale : aussi la précipitation, formulation « rupture de H⁺ »).

## Couverture du programme (PTSI, partie 4.4.2 et titrages)
| Capacité exigible | Avant | Après |
|---|---|---|
| Identifier oxydant et réducteur d'un couple, demi-équations | §1 | §1 (+ milieu basique, exemple chiffré), méthodes 1-3, EXO 01, 06 |
| Nombre d'oxydation | §2 | §2 |
| Position dans le tableau ↔ caractère oxydant/réducteur du corps simple | absent | §2, EXO 06, carte |
| N.o. extrêmes d'après le tableau périodique | absent | §2 (tableau), méthode 1, EXO 06, carte |
| Oxydants et réducteurs usuels (thiosulfate, permanganate, hypochlorite, H₂O₂) | permanganate seul | §2 (tableau), EXO 06, 10, concours, carte |
| Potentiel d'électrode, formule de Nernst | §3 (coefficients manquants) | §3, méthode 4, EXO 03 |
| Pile, tension à vide, fonctionnement à partir d'une mesure ou des potentiels | §5 (sans mesure) | §5, méthode 6, EXO 04, 08, carte |
| Électrodes de référence | absent (une ligne sur l'ESH) | §6 (ECS, Ag/AgCl, types d'électrodes, E = U + E_réf), carte |
| Diagrammes de prédominance ou d'existence, espèces incompatibles | absent | §7, méthode 8, EXO 07 |
| Caractère favorisé (qualitatif et quantitatif), K° | §4 | §4 (justification dépliable), §8 (état final), méthodes 5 et 9, EXO 02, 08, 09 |
| Dismutation et médiamutation | EXO 05 seulement | §9, méthode 7, EXO 05, 07, 11, concours D, carte |
| Analyse quantitative (titrages directs, indirects, suivi potentiométrique) | absent | §10, méthode 10, EXO 10, concours C, carte |
| Influence du milieu (pH, précipitation) | une remarque | §11 |
| Blocages cinétiques | une phrase | §4, §9 (H₂O₂), EXO 11 |

Hors programme regroupé en fin de cours : ΔrG° = −nFΔE°, combinaison des potentiels par les enthalpies libres,
capacité d'une pile, électrolyse, corrosion (renvois à `thermochimie` §9-§10 et `electrochimie`).

## Sections (numérotation gardée pour §1 à §5)
| Ancien § | Nouveau § |
|---|---|
| §1 · DÉFINITIONS | §1 · OXYDANTS, RÉDUCTEURS ET DEMI-ÉQUATIONS (même sujet) |
| §2 · NOMBRE D'OXYDATION | §2 · NOMBRE D'OXYDATION (+ n.o. extrêmes, espèces usuelles) |
| §3 · POTENTIEL & FORMULE DE NERNST | §3 · POTENTIEL D'ÉLECTRODE ET FORMULE DE NERNST |
| §4 · PRÉVISION DES RÉACTIONS | §4 · PRÉVOIR UNE RÉACTION : RÈGLE DU γ ET CONSTANTE D'ÉQUILIBRE |
| §5 · PILES ET ÉLECTROLYSE | §5 · PILES ET TENSION À VIDE (électrolyse → fin du chapitre) |
| — | §6 Électrodes de référence ; §7 Diagrammes de prédominance et d'existence ; §8 État final ; §9 Dismutation et médiamutation ; §10 Titrages ; §11 Influence du milieu ; Pour aller plus loin |

Bloc « AU PROGRAMME · PTSI » ajouté en tête. Chaque section a au moins un exemple chiffré (16 au total) et une
notice « Erreur classique ». Six figures calculées : échelle des E°, pile Daniell, diagrammes de prédominance
(Fe, Cu, Sn), croisement des potentiels à l'équilibre (Ag + Fe³⁺), électrodes de référence, titrage
potentiométrique Fe²⁺/MnO₄⁻ (simulé : E(V_E/2) = 0,77 V, E_éq = 1,39 V, saut 0,89 → 1,49 V entre 19,8 et 20,2 mL).

## Méthodes (5 → 10)
n.o. et oxydant d'un couple ; équilibrer une demi-équation (acide, basique) ; écrire une réaction ; Nernst ; sens et
K° ; décrire une pile (potentiels ou mesure, électrode de référence) ; dismutation/médiamutation ; diagramme de
prédominance ; état final ; exploiter un titrage. Chaque méthode a un exemple éclair chiffré et vérifié.

## Exercices (7 → 12)
Gardés : EXO 01 à 05 (retouchés). Nouveaux : EXO 06 n.o. et tableau périodique (★), EXO 07 diagrammes fer/étain
(★★), EXO 08 pile dont la polarité contredit les E° (Ag⁺ 0,010 / Fe³⁺ = Fe²⁺, état final de la pile usée : Q_r = K°)
(★★), EXO 09 gravure des circuits imprimés au chlorure de fer(III) (★★), EXO 10 titre d'une eau oxygénée « 10
volumes » au permanganate (★★), EXO 11 conserver une solution de fer(II) : oxydation lente par l'air, médiamutation
avec un clou (★★★). **Concours PT** « Eau de Javel : dangers, dosage et conservation » (A espèces du chlore,
B médiamutation HClO + Cl⁻ en milieu acide, C dosage iodométrique, D seuil de dismutation de Cl₂ à pH 4,5).

## Cartes
Le deck `oxr` compte **25 cartes** (et non 103 comme l'indiquait la consigne ; `eph` en compte 25, non 78 : vérifié
dans la copie de travail et dans le dépôt). 7 corrigées, 8 ajoutées à la fin : espèces usuelles,
n.o. extrêmes, caractère du corps simple, mesure avec une électrode de référence (`val`), pôles d'une pile d'après une
mesure, potentiel unique à l'équilibre, critère de dismutation, iodométrie (`form`).

## Notations
E°, E, K°, Q_r, c° = 1 mol·L⁻¹, P° = 1 bar, (RT/F) ln 10 ≈ 0,06 V ; **n** pour le nombre d'électrons (comme
`electrochimie` ; `thermochimie` §9 emploie γ, et parle aussi de « règle du gamma » : divergence signalée, non
corrigée ici) ; demi-équation α Ox + p H⁺ + n e⁻ = β Red + q H₂O ; tension à vide e = E₊ − E₋ ; E = U + E_réf ;
concentration de tracé c_tr ; potentiel standard apparent E°_app(pH).

## Doutes
- E(ECS) = 0,244 V à 25 °C (valeur des tables françaises ; certaines sources donnent 0,241 V).
- E°(HClO/Cl₂) = 1,63 V et E°(HClO/Cl⁻) = 1,49 V : valeurs usuelles des tables, cohérentes entre elles
  ((1,63 + 1,36)/2 = 1,495 V).
- Le concours a plusieurs `.statement` (déjà le cas de 14 exercices concours du site).
