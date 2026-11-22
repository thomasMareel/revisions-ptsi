# Revue et réécriture : `atome` (prefix `atm`), « Architecture de la matière » — 2026-11-22

Point 4 de l'audit, lot 6 (`docs/audit-2026-11/physique-1a.md` l. 9, 56, 79, 111, 155 ; `docs/audit-2026-11.md` §5).
Programme : PTSI 2021 (`pdf-pt/prog/ptsi.txt`). Le programme n'a pas de partie « atome » : il fait du tableau
périodique l'outil du chimiste et en tire des capacités dispersées dans 4.2.1 (électrons de valence des blocs s et p d'après la
position, Lewis, écarts à l'octet, ordres de grandeur des liaisons covalentes, électronégativité, polarisation), 4.3 (positionner
et reconnaître métaux et non-métaux) et 4.4.2 (caractère oxydant ou réducteur des corps simples, nombres d'oxydation extrêmes
d'après la position). Acquis du lycée réinvestis : noyau, isotopes, configuration électronique jusqu'à \(Z = 18\) (seconde).
L'introduction au monde quantique n'est au programme ni de PTSI ni de PT.

## Fichiers (dans `AN1/`)
| Fichier | Contenu |
|---|---|
| `atm-cours.src.html` | construit par `eq_construire.py atm` depuis `atm-cours.tpl.html` + `atm_figs.json` |
| `atm-meth.src.html` | 10 méthodes, 2 pièges |
| `atm-exos.src.html` | 11 exercices + « Concours PT » + 2 exercices hors programme en fin |
| `atm-cartes-corr.json`, `atm-cartes-ajout.js` | 10 réponses corrigées (questions inchangées), 15 cartes ajoutées en fin (15 → 30) ; générés par `atm_cartes.py` |
| `atm_donnees.py` | symboles, positions (période, colonne, bloc), électrons de valence, électronégativités de Pauling, énergies d'ionisation (NIST), énergies et longueurs de liaison |
| `atm_figs.py` → `atm_figs.json` | 7 figures calculées à partir de `atm_donnees.py` |
| `atm_calculs.py`, `atm_calculs_exos.py` | vérification des nombres du cours, des méthodes et des exercices |
| `atm_voir.py`, `atm_orig_{cours,meth,exos}.html` | aperçu des figures ; copies des anciens panneaux |

## Erreurs et défauts trouvés (corrigés)
1. **Cours centré sur le hors-programme** (audit) : §1-§2 consacrés aux quatre nombres quantiques, Pauli, Klechkowski, Hund et aux
   « exceptions à connaître » (Cr, Cu), alors que rien de cela n'est exigible. Tout est regroupé en « POUR ALLER PLUS LOIN · STRUCTURE
   ÉLECTRONIQUE DES ATOMES » ; le cours est recentré sur la lecture du tableau.
2. « Électrons de valence : électrons de la couche de plus grand n, plus ceux de la sous-couche d en cours de remplissage » : définition
   du bloc d (hors programme) ; remplacée par la règle exigible (blocs s et p, d'après la colonne), carte n° 8 corrigée de même.
3. Capacités exigibles absentes : nombres d'oxydation extrêmes d'après la position, caractère oxydant/réducteur des corps simples,
   métaux/non-métaux, ordres de grandeur des longueurs et énergies des liaisons covalentes (signalé absent du site par l'audit), nombre de
   liaisons d'un atome, ions usuels et formules des composés ioniques, comparaison des électronégativités et polarisation.
4. Méthodes 1 et 2 et trois exercices sur quatre hors programme ; ancien « Concours PT » (Na, Cl) en deux questions, marqué hors programme
   alors que les configurations de Na et Cl (\(Z \le 18\)) sont un acquis du lycée : repris en EXO 05, sans cette mention, et complété.
5. Ancienne figure : tableau schématique sans éléments. Remplacée par 7 figures calculées.
6. Le cours affirmait que l'électronégativité augmente « de bas en haut » sans réserve : la figure et une notice montrent les irrégularités
   (\(\chi_{\mathrm{Ga}} \gt \chi_{\mathrm{Al}}\)) et la règle sûre (même ligne ou même colonne seulement).
7. Cartes (réponse seule) : n° 8 (bloc d) et n° 14 (énergie d'ionisation, hors programme, mêlée à l'électronégativité) réécrites ;
   n° 2 à 7, 9 et 13 : préfixe harmonisé « Hors programme en PTSI (pour aller plus loin) : » (n° 13, rayon atomique, ne l'avait pas).
   Aucune carte n'est fausse des deux côtés.

## Couverture du programme, avant → après
| Capacité (PTSI) | Avant | Après |
|---|---|---|
| Acquis : Z, A, isotopes, masse molaire, entités et espèces | §1 (court) | §1 (ordres de grandeur, Fe 56), §2 (Cl, Cu), §3 (ions polyatomiques), méthodes 1-2, EXO 01-02 |
| Tableau périodique : périodes, colonnes, blocs, familles | §3 (texte) | §4 (tableau complet calculé, situer un élément d'après Z), méthode 3, EXO 03 |
| Électrons de valence des blocs s et p d'après la position (4.2.1) | définition bloc d | §5 (règle, rappel Z ≤ 18, figure de Lewis des atomes), méthode 4, EXO 03-05 |
| Octet, ions usuels, composés ioniques | méthode 3 | §6 (tableau des ions, isoélectroniques, formules), méthode 5, EXO 05-06 |
| Nombre de liaisons ; écarts à l'octet (renvoi à `molecules`) | ❌ | §7, méthode 6, EXO 07 |
| Ordres de grandeur des longueurs et énergies de liaison covalente (4.2.1) | ❌ | §7 (tableau, figure log, photon qui casse une liaison), méthode 10, EXO 11, concours B |
| Comparer des électronégativités d'après la position ; polarisation (4.2.1) | 1 ligne | §8 (figure calculée, règle et limites, Δχ), méthode 7, EXO 08, concours B1 |
| Positionner et reconnaître métaux et non-métaux (4.3) | ❌ | §9 (figure), méthode 8, EXO 09 |
| Caractère oxydant ou réducteur du corps simple d'après la position (4.4.2) | ❌ | §9 (Na + eau, halogènes), méthode 8, EXO 09, concours C |
| Nombres d'oxydation extrêmes d'après la position (4.4.2) | ❌ | §10 (figure période 3, N, S, Cl, oxydants usuels du programme), méthode 9, EXO 10, concours D |

## Contenu
- **Cours** : « AU PROGRAMME · PTSI » + 10 sections (§1 atome ; §2 isotopes et masse molaire ; §3 entités et espèces ; §4 tableau ;
  §5 électrons de valence ; §6 octet et ions ; §7 valence et liaison covalente ; §8 électronégativité ; §9 métaux, oxydants, réducteurs ;
  §10 n.o. extrêmes) + « Pour aller plus loin » (quantification, nombres quantiques, Pauli, Klechkowski, Hund, Fe, Cr, Cu, énergie
  d'ionisation, rayon). 12 exemples traités chiffrés, 7 figures calculées (tableau périodique complet par blocs ; Lewis des atomes
  H à Ar ; électronégativité par période ; métaux, semi-métaux, oxydants et réducteurs ; n.o. extrêmes de la période 3 ; énergies des
  liaisons et interactions en échelle log ; énergie de 1ʳᵉ ionisation de Z = 1 à 38). ≈ 86 000 car.
- **Méthodes** : 10 (composition, isotopes, situer, valence, ions, liaisons, électronégativité, corps simples, n.o. extrêmes, ordres de grandeur).
- **Exercices** : 01 composition ; 02 isotopes (Li, Cu) ; 03 se repérer ; 04 soufre (ancien EXO 01, complété) ; 05 sodium et chlore (ancien
  concours, complété) ; 06 ions isoélectroniques ; 07 liaisons et formules (BF₃) ; 08 électronégativité, série H–X ; 09 métaux, oxydants,
  réducteurs ; 10 n.o. ; 11 ordres de grandeur (atome/noyau, photons) ; **Concours PT** « Les halogènes » (4 parties : position, isotopes et
  spectre de masse de Cl₂ ; liaisons H–X ; pouvoir oxydant et états physiques ; n.o. et eau de Javel) ; puis hors programme : 12 cuivre
  (ancien 02), 13 nombres quantiques et énergies d'ionisation (ancien second concours).
- **Cartes** : 15 ajoutées (valence d'après la colonne, octet, ions usuels, formule d'un composé ionique, nombre de liaisons, ordres de
  grandeur des liaisons et des tailles, électronégativité, comparaison, polarisation, métaux, oxydants/réducteurs, dihalogènes, n.o.
  extrêmes, masse molaire isotopique). Chaque champ mêlant texte et symboles contient une formule `\\( … \\)` pour que `flashPretty` ne
  mette pas « s », « p », « H, C, N » ni les nombres en italique mathématique (rendu MathJax vérifié, aucune erreur).

## Contrôles
`verif_src.py` (3 panneaux) : aucune erreur ni « attention » ; `apercu_src.py` à 390 et 1 440 px (un par un) : `merr`, `brut`, `larges`
vides, aucune erreur JS (trois formules d'exercices et une étiquette de figure corrigées au passage) ; figures regardées en clair et en
sombre (`atm_voir/`), toutes à 12 px au moins ; `corriger_cartes.py --essai` (10) et `ajouter_cartes.py --essai` (15 → 30) sans erreur.

## Notations
\(Z\), \(A\), \(N\), \(^A_Z\mathrm X\), \(N_A\), \(v\) (nombre d'électrons de valence), \(\chi\) (électronégativité de Pauling), \(\Delta\chi\),
\(\delta+\)/\(\delta-\), n.o. en chiffres romains (comme `oxred`), doublets en traits et électrons célibataires en points (Lewis).

## Doutes
- Le titre « Architecture de la matière » est gardé (il est cité par `cristallin`) ; « Atomes et tableau périodique » décrirait mieux le
  chapitre recentré.
- La place du lanthane : la figure met les 15 lanthanides (La-Lu) et actinides (Ac-Lr) en rangées séparées, avec un renvoi en colonne 3
  (présentation la plus courante ; l'UICPA discute de Lu/Lr en colonne 3).
- Seuils de polarité (\(\Delta\chi\) ≈ 2 pour « ionique ») et valeurs moyennes d'énergies de liaison : repères des tables usuelles, présentés
  comme tels. Les énergies de liaison du §7 (C=O 745, F–F 159…) varient de quelques % selon les sources.
- `molecules` reste mince (Lewis, écarts à l'octet, VSEPR hors programme) : ce chapitre y renvoie sans le refaire ; les ordres de grandeur
  des liaisons y sont maintenant traités (§7), à reprendre tels quels si `molecules` est réécrit.
