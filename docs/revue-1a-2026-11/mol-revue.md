# Revue et réécriture : `molecules` (prefix `mol`), « Structure des molécules » — 2026-11-22

Point 4 de l'audit, lot 7 (`docs/audit-2026-11/physique-1a.md` l. 56-57, 80, 155 ; `docs/audit-2026-11.md` §3, §5).
Programme : PTSI 2021, parties 4.2.1 « Structure des entités chimiques » et 4.2.2 « Relations structure des entités - propriétés
physiques macroscopiques » (`pdf-pt/prog/ptsi.txt`, l. 1183-1258). Vérifié dans le programme de PT (`phys.txt`) : ni
VSEPR ni mésomérie. Rédaction originale, exemples et exercices inventés, valeurs tirées des tables usuelles et recalculées.

## Ce que le programme demande exactement (VSEPR, charges formelles, mésomérie)
- **Géométrie** : « Associer qualitativement la géométrie d'une entité à une minimisation de son énergie » et « Relier l'existence ou
  non d'un moment dipolaire permanent à la structure géométrique **donnée** d'une molécule ». La géométrie est donc fournie ; le
  principe qualitatif (répulsion des doublets, minimisation de l'énergie, doublets non liants qui referment les angles) est
  **au programme** ; la méthode VSEPR systématique (AXₙEₘ, figures de répulsion) est **hors programme** (fin de chapitre).
- **Charges formelles** : « Établir un schéma de Lewis **pertinent** pour une molécule ou un ion » : placer la charge d'un ion et
  choisir entre plusieurs schémas exige les charges formelles ; elles sont traitées comme au programme (§3). L'audit (l. 80) les
  rangeait avec la VSEPR parmi le hors-programme non signalé : c'est discutable, et le nouveau cours tranche ainsi.
- **Mésomérie** : absente des deux programmes ; hors programme (fin de chapitre, exercice 13 signalé).

## Fichiers (dans `AN1/`)
| Fichier | Contenu |
|---|---|
| `mol-cours.src.html` | construit par `mol_construire.py mol` depuis `mol-cours.tpl.html` + `mol_figs.json` |
| `mol-meth.src.html` | 10 méthodes au programme + méthode 11 (VSEPR) hors programme, 5 pièges |
| `mol-exos.src.html` | 12 exercices + « Concours PT » + 1 exercice hors programme en fin |
| `mol-cartes-corr.json`, `mol-cartes-ajout.js` | 7 réponses corrigées (questions inchangées), 15 cartes ajoutées en fin (22 → 37) ; corrections générées par `mol_cartes.py` |
| `mol_figs.py` → `mol_figs.json` | 8 figures calculées (dont un petit moteur de schémas de Lewis : liaisons, doublets, charges formelles, lacunes, électrons célibataires) |
| `mol_calculs.py`, `mol_calculs_exos.py` | vérification des nombres (électrons, charges formelles, ionicités, moments, énergie d'une paire d'ions, solubilité du diiode, extrapolation de \(T_{\text{éb}}\)) |
| `mol_voir.py`, `mol_deborde.js`, `mol_cartes_rendu.js` | aperçu des figures (clair et sombre, `mol_voir/`), recherche d'un débordement à 390 px, rendu MathJax des cartes |

## Erreurs et défauts trouvés (corrigés)
1. Hors-programme mal délimité (audit l. 80) : la VSEPR occupait tout le §2, deux exercices sur trois et le concours ; à l'inverse,
   le principe qualitatif de la géométrie (au programme) était marqué hors programme, comme les charges formelles dans la méthode.
2. Manques du programme (audit l. 56) : écarts à la règle de l'octet (absents), ordres de grandeur des liaisons (renvoyés à `atome`
   §7 avec un tableau et un exemple), direction et sens du vecteur moment dipolaire (absents), caractère ionique partiel,
   « associer une propriété d'un solvant à une grandeur », étapes de la mise en solution d'une espèce ionique, miscibilité partielle.
3. Ancienne méthode 1, étape 4 « envisager la mésomérie » : hors programme présenté comme une étape de la méthode ; retiré.
4. Anciens exercices : EXO 01 Q2, EXO 02 Q1, concours A2 demandaient le type VSEPR : adaptés (géométrie donnée, justification
   qualitative ; type VSEPR en mention « pour aller plus loin ») ; ancien concours « nitrate, mésomérie » gardé en EXO 13 signalé
   hors programme (partie A, charges formelles, au programme).
5. Cartes (réponse seule corrigée) : n° 4 (principe de la VSEPR marqué entièrement hors programme alors que le principe qualitatif
   est au programme), n° 8 et 9 (justification qualitative d'une géométrie marquée hors programme), n° 7 (mélange géométries données
   / types VSEPR), n° 3, 5, 6 (préfixe harmonisé « Hors programme en PTSI (pour aller plus loin) : », comme `atome`). Les réponses
   corrigées sont écrites en `\( … \)` : `flashPretty` mathématisait les formules chimiques et les nombres de l'ancien texte.
   Aucune carte fausse des deux côtés ; les questions 5, 6, 7 et 9 (inchangées) restent mathématisées par `flashPretty` à l'affichage
   (« \(AX_nEₘ\) », « \(n+m = 2, 3, 4\) ») : à reformuler plus tard, seules, si on le souhaite.

## Couverture du programme (PTSI 4.2), avant → après
| Capacité | Avant | Après |
|---|---|---|
| Ordres de grandeur de longueurs et d'énergies de liaisons covalentes | ❌ | §1 (tableau, CO₂, C=C, N≡N ; renvoi `atome` §7), carte `atome` |
| Électrons de valence d'après la position (blocs s et p) | implicite | §1-§2 (renvoi `atome` §5), méthode 1, EXO 01 |
| Schéma de Lewis pertinent d'une molécule ou d'un ion | méthode en 4 lignes | §2 (méthode, CH₂O, HCN, figure de 8 molécules), §3 (charges formelles, schéma pertinent, N₂O, CO), méthodes 2-4, EXO 01, 03, 04 |
| Écarts à la règle de l'octet | ❌ | §4 (lacune, radicaux, hypervalence ; H₃N–BF₃, NO₂/N₂O₄, sulfate ; figure), méthode 5, EXO 05, 06, 07 |
| Géométrie et minimisation de l'énergie (géométrie donnée) | VSEPR hors programme | §5 (principe qualitatif, BF₃/NH₃, angle de l'eau, figure en représentation de Cram), méthode 6, EXO 02, 05, 07, concours A2 |
| Comparer des électronégativités ; polarisation d'une liaison | 1 phrase | §6 (renvoi `atome` §8, halogénures d'hydrogène), méthode 7 |
| Moment dipolaire : existence liée à la géométrie ; direction et sens du vecteur | somme vectorielle | §6 (convention − → +, debye, ionicité, figure), §7 (eau, symétries, CHCl₃, dichloroéthènes), méthode 8, EXO 07, 08, 09, concours B |
| Van der Waals, liaison hydrogène : ordres de grandeur ; températures de changement d'état | §4 | §8 (Keesom, Debye, London, dihalogènes, pentanes, propane/éthanal), §9 (éthanol/méthoxyméthane, enthalpies de vaporisation, HF/H₂O, nitrophénols, figures), méthode 9, EXO 10, 11, concours C |
| Solvants : moment dipolaire, permittivité, caractère protogène ; associer une propriété | liste | §10 (tableau de 9 solvants, énergie d'une paire d'ions dans trois solvants, HCl, acide éthanoïque, DMSO), méthode 10, EXO 12, concours D |
| Miscibilité de deux solvants ; solubilité d'une espèce moléculaire ou ionique | 2 phrases | §11 (miscibilité totale, partielle, nulle ; étapes de la dissolution ; extraction du diiode ; NaCl dans l'eau et l'éthanol ; figure de solvatation), méthode 10, EXO 12, concours D |
| Hors programme (VSEPR, mésomérie) | mêlé au cours | fin de chapitre (tableau AXₙEₘ, O₃, CO₃²⁻, benzène), méthode 11, EXO 13 |

## Contenu
- **Cours** : « AU PROGRAMME · PTSI » + 11 sections + « Pour aller plus loin » ; 22 exemples traités, 8 figures calculées (schémas
  de Lewis de 8 molécules, ions et charges formelles, écarts à l'octet, géométries usuelles en Cram, moments dipolaires de HCl,
  H₂O, CO₂, températures d'ébullition des hydrures des colonnes 14 à 17 avec l'extrapolation pour l'eau, liaison hydrogène entre deux
  molécules d'eau, solvatation de Na⁺ et Cl⁻). ≈ 107 000 caractères (dont ≈ 62 000 de figures).
- **Méthodes** : 10 au programme + 1 hors programme, avec exemples éclairs vérifiés ; 5 pièges.
- **Exercices** : 01 schémas de Lewis (H₂S, PCl₃, C₂H₂, HOCl) ; 02 ammoniac (ancien 01 adapté) ; 03 ions et charges formelles
  (H₃O⁺, NH₂⁻, ClO⁻, NO₂⁻) ; 04 schéma pertinent de l'ion cyanate ; 05 BF₃ et NH₃, adduit (ancien concours 1 adapté) ;
  06 radicaux et hypervalence (NO, ClO₂, NO₂, PCl₃/PCl₅, NCl₅) ; 07 CO₂ et SO₂ (ancien 02 adapté, moment S=O) ; 08 moments de
  liaison de H₂O et H₂S, ionicité ; 09 chlorométhanes, modèle additif des moments et ses limites, dichloroéthènes ;
  10 températures d'ébullition (gaz nobles, hydrures à 10 électrons, quatre composés de masse 44-46) ; 11 nitrophénols ;
  12 choisir un solvant (dissolution, miscibilité, extraction) ; **Concours PT** « L'eau, une molécule singulière » (4 parties :
  structure, polarité, liaison hydrogène et ébullition avec régression, l'eau solvant) ; puis 13 ion nitrate (hors programme).
- **Cartes** : 15 ajoutées (électrons d'un ion, somme des charges formelles, schéma pertinent, trois écarts à l'octet,
  hypervalence, sens et unité du moment dipolaire, ionicité, moment d'une molécule coudée, London, éthanol/méthoxyméthane,
  liaison hydrogène intramoléculaire, solvant ionisant/dissociant, étapes de la dissolution, eau/cyclohexane, solvant
  d'extraction). Rendu MathJax vérifié : aucune erreur, aucune réponse nouvelle mathématisée à tort.

## Contrôles
`verif_src.py` (3 panneaux) : aucune erreur ni « attention » ; `apercu_src.py` à 390 et 1 440 px (un par un) : `merr`, `brut`, `larges`
vides, aucune erreur JS, `scrollW` = largeur ; figures regardées en clair et en sombre (`mol_voir/`) et dans la page (captures à 390
et 1 440 px) ; `corriger_cartes.py --essai` (7) et `ajouter_cartes.py --essai` (22 → 37) sans erreur.

## Notations
\(C_F = N_v - N_{nl} - N_l/2\) (comme l'ancien cours et la carte 2) ; \(\chi\) (Pauling, comme `atome`) ; charges partielles \(\pm\delta\)
en coulombs (\(0 \lt \delta \lt e\), comme `atome` §8) ; moment dipolaire \(\vec\mu = \delta\,\overrightarrow{\mathrm{BA}}\), dirigé de − vers +,
identique au \(\vec p = q\,\overrightarrow{NP}\) de `estat2a` ; debye \(1\ \text{D} = 3{,}336\times10^{-30}\ \text{C·m}\) ; pourcentage d'ionicité \(\delta/e\) ;
\(\varepsilon_r\) ; charges formelles entourées (⊕, ⊖) ; lacune notée par un rectangle.

## Doutes
- Valeurs de tables arrondies (moments dipolaires, températures de changement d'état, permittivités) : écarts de quelques % selon
  les sources. Solubilité du diiode dans le cyclohexane estimée à ≈ 22 g·L⁻¹ d'après une fraction molaire de 0,0092 à 25 °C
  (Hildebrand) : écrite « de l'ordre de 20 g·L⁻¹ », rapport « soixante fois » à l'eau. Nitrophénols : 4-nitrophénol bouillant
  « vers 280 °C » (il se décompose).
- Ion sulfate : les deux écritures (octet avec charges formelles, ou soufre hypervalent) sont présentées ; les professeurs ne sont pas
  tous d'accord ; l'exercice 07 (SO₂) demande les deux.
- Le vocabulaire « ionisant / dissociant » (associé à \(\mu\) et à \(\varepsilon_r\)) est l'usage des classes préparatoires, pas un mot du programme.
- Au téléphone, les figures à trois colonnes (géométries, Lewis, octet) prennent leur largeur minimale lisible et défilent, comme
  les autres figures larges du site.
