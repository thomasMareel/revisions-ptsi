# Physique-chimie de 1ʳᵉ année : corrections et encadrés « programme » (14/11/2026)

Source : `docs/audit-2026-11/physique-1a.md` (§3, §4), programme `pdf-pt/prog/ptsi.txt` (et `phys.txt`, `si.txt` pour
situer ce qui relève de la 2ᵉ année ou des SI). Chaque point a été revérifié (calcul ou ligne du programme) avant correction.
Aucune carte ajoutée, retirée ni déplacée ; une seule question retouchée (`ind` n° 18, `q_nouvelle`). Numéros de cartes
à partir de 0 (comme `cartes.py`).

Fichiers produits (tous dans `revue2/`) : 47 panneaux `*.src.html` et 22 fichiers `*-cartes-corr.json` (préfixes :
lor, thermo1, cst, mp, cc, mth, ind, opt, ond, sig, cin, cri, osc, od, fd, ce, emag, atm, mol, eq, th3, th2, cpt, mcin,
oxr, eph, acb).

## 1. Erreurs (audit §4)

| Point de l'audit | Vérification | Fait | Fichier(s) |
|---|---|---|---|
| 1. `lorentz` §2, déflexion | y(L) = qEL²/(2mv₀²), E = U/d : δ = qUL²/(2mdv₀²) = UL²/(4dU_acc). Audit juste | fait (facteur 2) ; carte n° 6 idem | lor-cours, lor-cartes |
| 2. `thermo1` §1, échelles | microscopique 0,1–1 nm ; 1 μm³ de gaz ≈ 2,4 × 10⁷ molécules, d'eau ≈ 3,3 × 10¹⁰. Audit juste | fait (plus de « ≈ 1 mole ») ; carte n° 4 | thermo1-cours, thermo1-cartes |
| 3. Vm « 22,4 L/mol à 1 bar » | RT/P = 22,71 L/mol à 273,15 K et 1 bar ; 22,41 à 1 atm ; 24,79 à 25 °C | fait : 22,7 L/mol (+ mention de 22,4 sous 1 atm) dans `thermo1` §5, `constantes` §2, cartes `thermo1` n° 29 et `cst` n° 15 | thermo1-cours, cst-cours, thermo1-cartes, cst-cartes |
| 4. `mecpt` §1, géocentrique | audit juste | fait : géocentrique ≪ 1 an, terrestre ≪ 1 jour ; carte `mp` n° 0 | mp-cours, mp-cartes |
| 5. `chcentral` §1, L = C | audit juste | fait : L = mr²θ̇ = mC, C constante des aires | cc-cours |
| 6. `machines`, signes | trois conventions confirmées | fait : convention unique « énergies reçues par le fluide » (W + Q_c + Q_f = 0, moteur W < 0, η = −W/Q_c, COP_PAC = −Q_c/W, W = −∮P dV < 0 en sens horaire), annoncée au §1 et appliquée au cours (§1, §3, §4, figure « aire = −W »), méthode 1 et pièges, exercices 1 à 6 et les deux « Concours PT », cartes n° 0, 2, 4, 11 | mth-cours, mth-meth, mth-exos, mth-cartes |
| 7. Carte `ind` n° 21 (RL) | audit juste (½LI² stockée, énergie fournie et dissipée non bornées) | fait | ind-cartes |
| 8. `optique` §2, microscope afocal | audit juste | fait : seule la lunette réglée à l'infini est afocale ; microscope : F′₁ et F₂ séparés par l'intervalle optique | opt-cours |
| 9. `ondes` §1, d'Alembert | audit juste | fait : « à une dimension, en milieu non dispersif (et sans absorption) » + signalé hors programme ; carte n° 1 idem | ond-cours, ond-cartes |
| 10. `oscill` §7, Tacoma | instabilité aéroélastique (flottement) | fait : exemple nuancé | osc-cours |
| 11. Carte `sig` THD | la formule est un rapport de valeurs efficaces | fait (carte n° 11) ; précisé aussi dans le cours | sig-cours, sig-cartes |
| 12. `cinetique` §2 « durée de vie » | | fait : « temps de demi-réaction » | cin-cours |
| 12. `cristallin` §1 « plus petit parallélépipède » | | fait : maille primitive / mailles conventionnelles cubiques (CFC non primitive) ; carte `cri` n° 0 idem | cri-cours, cri-cartes |
| 12. `induction` §5, orientation | avec Φ = +Blx, −dΦ/dt = −Blv : le signe dépendait d'une orientation non dite | fait : normale opposée à B (sens horaire sur la figure), Φ = −Blx, Ri = Blv ; force projetée sur l'axe des rails | ind-cours |
| 12. Carte `cc` « T = 24 h » | | fait (n° 23) : 1 jour sidéral ≈ 23 h 56 min | cc-cartes |

## 2. Encadrés « programme »

| Chapitre | Fait | Fichier(s) |
|---|---|---|
| `optiqued` | encadré réécrit (« Programme PTSI : §1 et §2 seulement ») : au programme, superposition de deux ondes, chemin optique et déphasage, trous (fentes) d'Young, formule de Fresnel fournie ; 2ᵉ année : démonstration de Fresnel, cohérence temporelle, réseau ; hors programme des deux années : diffraction par une fente, Rayleigh, lames minces, anneaux de Newton. Notices en tête de §3 et §4, méthodes 2 à 4, exercices 3 à 6, partie B du 1ᵉʳ « Concours PT », 13 cartes | od-cours, od-meth, od-exos, od-cartes |
| `fluiddyn` | encadré réécrit : ni la dynamique ni la statique des fluides en PTSI (accord avec `fluides`) ; §1-§3 en 2ᵉ année (liens `ecoulement`, `ecoulreel`) ; tension superficielle (§4) hors des deux programmes | fd-cours |
| `changement` | encadré de tête réécrit : au programme de PTSI, diagramme (P, T), diagramme (P, v), titre et composition d'un mélange diphasé, enthalpies de changement d'état et bilans, Δh₁₂ = TΔs₁₂ (en signalant que (P, v) et cette relation ne sont pas encore développés dans le chapitre) ; 2ᵉ année : potentiel chimique, diagrammes (T, s), (h, s), (log P, h), tables ; hors programme : Clausius-Clapeyron | ce-cours |
| `emag` | encadré réécrit (« Programme PTSI : §1 et §3 ») : sources et cartes de champ, symétries, ordres de grandeur, champs fournis, moment magnétique, force de Laplace, couple m ∧ B ; 2ᵉ année : Ampère et conservation du flux (§2) ; hors des deux programmes : Biot et Savart, H et circuits magnétiques (§4). Notices sur place | emag-cours, emag-meth, emag-exos, emag-cartes |
| `optique`, « Programme PTSI : … grossissement » | réécrit : lunette et microscope seulement cités en exemples laissés au choix de l'enseignant, aucune formule de grossissement à connaître ; exigible : construire l'image par des lentilles minces | opt-cours |

## 3. Hors-programme signalé sur place (audit §3)

Tous vérifiés dans `ptsi.txt` (et `phys.txt` pour la mention « vu en 2ᵉ année »). Forme : notice `Hors programme en PTSI`
+ « (hors programme) » au titre ; méthodes, exercices, parties d'exercices et cartes marqués.

| Chapitre | Ce qui est signalé | Fichier(s) |
|---|---|---|
| `atome` | nombres quantiques, sous-couches (§1) ; configurations, Pauli, Klechkowski, Hund, exceptions (§2) ; méthodes 1-2, 3 exercices et une partie ; 7 cartes (pour aller plus loin : absent des deux programmes) | atm-* |
| `molecules` | mésomérie, VSEPR (§2), méthode 2, questions VSEPR de 3 exercices, exercice nitrate ; 7 cartes | mol-* |
| `equilchim` | K_c/K_p (pour aller plus loin), §2 Le Chatelier et Van 't Hoff, ΔrG° = −RT ln K (2ᵉ année) ; méthodes 2-3 ; 3 exercices et une partie ; 9 cartes (dont formule de pH n° 23) | eq-* |
| `thermo3` §4 | identités thermodynamiques (2ᵉ année ; en PTSI l'expression de S est fournie) ; cartes 10 à 13 | th3-cours, th3-cartes |
| `changement` | Clausius-Clapeyron (§2), méthode 3, exercices 2 (Clapeyron), 4 (règle des phases), 6 Q3 (enthalpie libre, 2ᵉ année) ; 7 cartes | ce-* |
| `ondes` | d'Alembert (2ᵉ année) ; intensité sonore et décibels, effet Doppler et Mach (pour aller plus loin) ; ondes stationnaires et modes propres (2ᵉ année, en électromagnétisme) ; méthodes 2-3 ; 5 exercices et 2 parties du sonar ; 15 cartes | ond-* |
| `signaux` | calcul des coefficients de Fourier et symétries, THD (pour aller plus loin) ; puissance active (hors physique-chimie, vue en SI) ; méthode 1 ; 4 exercices (dont Q3 de l'exo 5) ; cartes 5, 11, 15, 23 | sig-* |
| `cinept` §4 | composition des vitesses (hors physique-chimie, vue en SI de 1ʳᵉ année) ; carte 15 | cpt-cours, cpt-cartes |
| `mecpt` §2 | lois de Coulomb du frottement solide (SI, S2) ; carte 8 | mp-cours, mp-cartes |
| `mcinc` §2 | Huygens-Steiner (hors physique-chimie, vu en SI) ; exercice 3, carte 9 | mcin-* |
| `oxred` §5 | électrolyse (2ᵉ année) ; exercice 6 Q3 (protection contre la corrosion) | oxr-cours, oxr-exos |
| `eph` §6 | corrosion et passivation (2ᵉ année) ; carte 21 | eph-cours, eph-cartes |
| `thermo2` | détente de Joule-Thomson (cours §4 et méthode 5 ; 2ᵉ année, détendeur) ; carte 28 | th2-cours, th2-meth, th2-cartes |
| `acidobase` | formules de pH (titre du §3 « pH de solutions simples », méthode 1, exercice 1, cartes 7 à 9) : « aucune formule de calcul de pH n'est exigible » | acb-* |
| `chcentral` (en plus) | exercice 6 (Binet), méthode 3 (excentricité), cartes 7, 11, 24 (coniques) : hors programme, cohérent avec le §4 déjà signalé | cc-meth, cc-exos, cc-cartes |

## 4. Erreurs supplémentaires trouvées en relisant

- `chcentral`, carte n° 27 : « l'orbite doit contenir l'axe de rotation » (faux : le plan de l'orbite contient le centre de la
  Terre et le satellite décrit un parallèle ; seul l'équateur convient) → réécrite.
- `machines` : carte n° 15 « η ∝ r^(γ−1) » (faux : η = 1 − r^(1−γ)) ; carte n° 2 « travail = somme des chaleurs » (signe) ;
  exercice 4 Q2 (expression tronquée et incohérente) ; exercice 2 Q3 (arrondis : 27,2 kJ, −11,86 kJ, 56,5 %).
- `thermo1` §5 : volume massique de l'air 0,77 → 0,78 m³/kg (RT/(PM) = 0,783).
- `induction`, carte n° 18 : question contradictoire (« tige tombant verticalement sur rails horizontaux ») → question
  reformulée (rails verticaux, B horizontal), réponse inchangée : la carte garde sa progression (repli par rang).
- `changement` §1 : P_c de l'eau 218 bar → 221 bar (22,06 MPa ; 218 est la valeur en atm) ; §3 : l'eau bout à 100 °C sous
  1 atm (et non 1 bar).
- `emag`, méthode 2 : « la force s'oppose au déplacement (Lenz) » présenté comme général → limité au courant induit.
- `molecules`, exercice 2 : titre « Deux molécules linéaires » alors que SO₂ est coudée → « Deux molécules de formule AO₂ ».
- `oxred`, exercice 6 Q3 : la galvanisation donnée comme protection du zinc → retirée (elle protège l'acier par le zinc).
- `eph` §6 : « l'or ne s'oxyde pas malgré une thermodynamique défavorable » (contresens : c'est parce que) → corrigé.
- `cristallin` : `</p>` orphelin dans l'encadré « Multiplicité » → retiré (un avertissement `verif_src` en moins).

## 5. Noms de chapitres (proposition)

- `changement` « Changements d'état » → **« Corps pur diphasé et changements d'état »** (intitulé du programme 3.1).
- `emag` « Magnétostatique (aperçu) » → **« Champ magnétique et actions de Laplace »** : l'essentiel (§1, §3) est exigible
  en PTSI ; Ampère (§2, 2ᵉ année) et §4 (hors programme) sont signalés sur place.

## 6. Doutes, points laissés en l'état

- `thermo1`, cours §2 et carte n° 13 : libre parcours moyen d'un liquide « inférieur à 10⁻¹¹ m » ; on lit plutôt « de
  l'ordre de 10⁻¹⁰ m ». Non modifié (valeur mal définie dans un liquide).
- `thermo1` §4 : R = N_A k_B « justifié » par les expériences de Joule (justification approximative). Non modifié.
- `mecpt`, « Concours PT » du plan incliné : utilise les lois de Coulomb sans les rappeler. Non signalé.
- `induction` §5 « FEM de Lorentz » : le programme exclut l'étude du champ électromoteur, mais le passage n'est qu'une
  interprétation. Non signalé.
- `optique` : méthode et carte « G = f′₁/f′₂ » de la lunette, laissées (instruments au choix de l'enseignant, pas hors programme).
- `molecules` : charge formelle laissée (utile à un schéma de Lewis « pertinent » d'un ion ; l'audit la dit hors programme).
- `signaux` : symétries (méthode 2, cartes 6 à 8) laissées (outil d'analyse d'une décomposition fournie).
- `equilchim` exercices 4 (pH par tableau d'avancement : état final, au programme) et 6 (complexation) ; `acidobase`
  exercice 2 ; `oxred` carte 17 (pile / électrolyse) ; `thermo3` méthode 1 et carte 22 (« ΔS par l'identité ») ;
  `emag` carte 13 (lignes de champ fermées) : laissés.
- `oscill` : l'encadré « le calcul exact de ω_r n'est pas exigible » n'est pas écrit tel quel dans le programme. Non modifié.
- Pour les notions de SI, la mention est « hors programme de physique-chimie (vu en sciences industrielles) » ; Coulomb et
  composition des mouvements sont en S1-S2 (1ʳᵉ année), Huygens-Steiner (matrice d'inertie, S3) et puissance active sans
  semestre certain, d'où « vu en SI » sans année.
- Notations (L pour Δh₁₂, K_c, S_e/S_c…) non harmonisées : hors de ce lot.

## 7. Contrôles

- `verif_src.py` : aucune ERREUR sur les 47 panneaux ; les « attention » (formules en ligne longues, pas de bloc « AU
  PROGRAMME · PT », surtitre de `opt-cours`) existaient déjà, en même nombre (une de moins pour `cri-cours`).
- `corriger_cartes.py … --essai` : sans erreur pour les 22 fichiers de cartes.
- `diff` panneau d'origine / fichier : seules les modifications voulues (contrôlé fichier par fichier).
- `apercu_src.py` 390 et 1440 : propres (merr, brut, larges vides, 0 erreur JS) pour `lor-cours`, `thermo1-cours`,
  `cst-cours`, `mp-cours`. Les autres panneaux tournaient encore à la remise du compte rendu (journaux
  `/tmp/claude-0/-home-user/6f48d12f-3f0e-5709-96fa-34955b53c076/scratchpad/physcorr/v0.log` et `v1.log`) : à relire avant
  intégration. Un premier passage de `cc-exos` à 390 px signalait un débordement (formules en ligne longues des corrigés
  d'origine, la seule retouche du fichier étant un titre) : à comparer au panneau d'origine.
