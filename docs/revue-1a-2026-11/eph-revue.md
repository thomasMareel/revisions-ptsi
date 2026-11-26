# Revue — « Diagrammes E-pH » (`eph`, prefix `eph`) — point 7, 2026-11-26

Le premier rédacteur n'avait rien produit pour ce chapitre (copies `eph_orig_*.html` seulement). Tout a été fait ici.

## Fichiers produits (dans `AN1/`)
- `eph-cours.src.html` (51 ko, assemblé par `construire_eph.py` depuis `eph-cours.tpl.html` et `eph_figs.json`) ;
- `eph-meth.src.html` ; `eph-exos.src.html` (assemblé depuis `eph_orig_exos.html` retouché et `eph-exos-nouveaux.tpl.html`) ;
- `eph-cartes-corr.json` (5 réponses corrigées) ; `eph-cartes-ajout.js` (8 cartes, à la fin) ;
- scripts : `eph_figs.py` (figures), `eph_exos_calculs.py` (vérifications), `couper_formules.py` (coupe des formules
  en ligne trop longues aux « = »).

Contrôles passés : `verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`,
`larges` vides (aussi en comptant les formules MathJax elles-mêmes), aucune erreur JS, scrollW = 390 ; captures
regardées ; figures vues en clair et en sombre ; `corriger_cartes.py --essai` (5) et `ajouter_cartes.py --essai`
(25 → 33) sans erreur.

## Figures (toutes calculées, `eph_figs.py`)
Moteur exact : pour chaque espèce d'un élément, une fonction linéaire de (pH, E) tirée des E°, pKs, pKa et des
conventions ; l'espèce stable minimise cette fonction ; chaque domaine est l'intersection exacte de demi-plans.
L'égalité de deux de ces fonctions est la formule de Nernst (ou la loi d'action des masses) avec les activités de
tracé : les frontières affichées coïncident avec les calculs à la main du cours (vérifié sommet par sommet).
1. eau (remplace l'ancien schéma, dont les deux « droites parallèles » ne l'étaient pas et dont les libellés
   faisaient 10 px) ; 2. fer (Fe, Fe²⁺, Fe³⁺, Fe(OH)₂, Fe(OH)₃, c_tr = 10⁻², pKs 38 et 15,1 comme `precipitation`) ;
3. chlore (Cl⁻, Cl₂, HClO, ClO⁻ ; c_tr = 0,10, Cl₂ sous 1 bar ; fin du domaine de Cl₂ à pH 2,5) ; 4. manganèse
simplifié + I₂/I⁻ + eau pour la méthode de Winkler ; 5. cuivre (énoncé du concours, 340 de large, domaines A-D).

## Erreurs trouvées et corrigées
**Cours**
- §3 : « Le potentiel d'équilibre dépend alors à la fois de E et du pH » (phrase vide de sens) ; pente « −0,06 h/n »
  sans le cas des H⁺ du côté du réducteur (pente positive, Cu²⁺/Cu₂O).
- §5 : « En dessous de la droite H⁺/H₂, le proton H⁺ est suffisamment oxydant pour transformer toute espèce
  réductrice en H₂ » : raisonnement inversé (au-dessous, c'est H₂ qui est stable ; c'est l'espèce dont le domaine est
  là qui réduit l'eau). « Toute chimie aqueuse se passe à l'intérieur de cette bande » : faux (espèces métastables :
  permanganate, eau de Javel).
- §1 et méthodes : « Le programme demande de savoir lire et utiliser un diagramme (pas de le construire) » / « le
  tracé est surtout approfondi en 2ᵉ année » : le programme de PTSI demande le « principe de construction » (§7 ajouté).
- §3 : « Fe³⁺ ↔ Fe(OH)₃ à pH ≈ 3 » sans convention (pH 2,0 pour c_tr = 10⁻², 3,3 pour 10⁻⁶ : §4).
- Notation OH⁻ → HO⁻ (notation du site) ; corrosion et passivation (2ᵉ année) déplacées en fin de chapitre.

**Exercices**
- EXO 03 Q3 concluait « le fer reste relativement stable dans l'eau neutre désaérée », en contradiction avec l'EXO 06
  (corrosion favorisée) : réécrite (favorisée mais très lente : écart cinétique).
- EXO 05 : « en milieu basique (pH > 7 environ), le domaine de Cl₂ disparaît » : faux ; seuil calculé (pH 0,5 pour
  c_tr = 10⁻², 2,5 pour 0,10), données ajoutées à l'énoncé ; OH⁻ → HO⁻ ; difficulté ★★★ → ★★☆.
- EXO 06 : « la présence d'oxygène accélère fortement la corrosion » déduit d'un écart de potentiel (la thermodynamique
  ne dit rien des vitesses) : corrigé ; « < » brut dans une formule → `\lt` ; Fe₂O₃ → Fe(OH)₃ (cohérence avec le
  cours) ; « f.e.m. » remplacé par « écart de potentiel ».
- Ancien « Concours PT » (trois questions sur le seul diagramme de l'eau, doublon du §5) **remplacé**.

**Cartes** (réponses seules) : n° 7 (pente sans le cas positif), 13 (« toute chimie aqueuse se déroule dans cette
bande »), 14 (« ne peut pas exister durablement » : les espèces métastables existent), 15 (« on observe un dégagement
gazeux » : pas toujours, cinétique), 23 (« les frontières verticales acide-base se déplacent avec c_tr » : faux pour
deux espèces dissoutes ; ce sont les frontières avec un solide qui bougent).

## Couverture du programme (PTSI, « Diagrammes potentiel-pH »)
| Capacité exigible | Avant | Après |
|---|---|---|
| Identifier les domaines d'un diagramme fourni | §2 (qualitatif) | §1 (lecture chiffrée), §2 (méthode + exemple), méthode 1, EXO 01, concours A |
| Déterminer la pente d'une frontière | §3 (formule) | §3 (exemples, pente positive), §7, méthode 2, EXO 02, 08, concours B3, carte |
| Justifier la position d'une frontière verticale | absent (une valeur sans calcul) | §4 (calcul, influence de c_tr), méthode 3, EXO 06, 07, concours B1, carte |
| Principe de construction | déclaré hors exigence | §7 (fer, pas à pas, vérification dépliable), méthode 4, EXO 07, concours B, carte |
| Diagramme de l'eau ; stabilité des espèces dans l'eau | §5 | §5 (figure calculée, trois exemples), méthode 6, EXO 03, 07 |
| Superposition de diagrammes, caractère favorisé | §6 (qualitatif) | §6 (exemples chiffrés), méthode 7, EXO 04, 09, concours D |
| Dismutation / médiamutation en fonction du pH | « domaine vide » seulement | §6, §8 (chlore, seuil calculé), méthode 8, EXO 05, 08, concours C, cartes |
| Confronter prévisions et expérience, écarts cinétiques | une remarque | §9 (quatre observations), méthode 9, EXO 03, 06, 07 |
| Mettre en œuvre des réactions s'appuyant sur les diagrammes | absent | §10 (méthode de Winkler, figure), méthode 9, EXO 08 Q4, 09, carte |

## Sections (numérotation §1 à §6 gardée)
| Ancien § | Nouveau § |
|---|---|
| §1 · POURQUOI CE CHAPITRE ? | §1 (même titre ; figure du fer, exemple de lecture) |
| §2 · ORIENTATION DU DIAGRAMME | §2 (même titre ; méthode d'attribution, exemple du chlore) |
| §3 · LES TROIS TYPES DE FRONTIÈRES | §3 (même titre ; pentes du fer, pente positive) |
| §4 · PRÉDOMINANCE & EXISTENCE | §4 · PRÉDOMINANCE, EXISTENCE ET CONVENTIONS DE TRACÉ |
| §5 · DIAGRAMME E-pH DE L'EAU | §5 (même titre) |
| §6 · UTILISATIONS | §6 · UTILISATIONS : SUPERPOSER DES DIAGRAMMES (corrosion → fin) |
| — | §7 Construire un diagramme : le fer ; §8 Dismutation et médiamutation selon le pH : le chlore ; §9 Thermodynamique et cinétique ; §10 Mise en œuvre : doser le dioxygène dissous ; Pour aller plus loin (corrosion, immunité, passivation) |

Bloc « AU PROGRAMME · PTSI » ajouté. Dix exemples traités chiffrés, une notice « Erreur classique » par section.

## Méthodes (6 → 9)
Attribuer les domaines ; pente ; frontière verticale ; équation d'une frontière d'oxydoréduction ; lire l'espèce d'un
milieu ; stabilité dans l'eau ; superposition ; dismutation selon le pH ; confronter à l'expérience et choisir le pH
d'un protocole. Chacune avec un exemple éclair chiffré.

## Exercices (7 → 10)
Gardés et corrigés : EXO 01 à 06. Nouveaux : EXO 07 construire le diagramme du zinc (★★), EXO 08 iode : pentes,
dismutation de I₂ au-delà de pH 8, médiamutation iodate-iodure (★★★), EXO 09 déferriser une eau souterraine (★★).
**Concours PT** « Le diagramme potentiel-pH du cuivre » (A lecture des domaines A-D et des droites de l'eau ;
B frontières, point triple (3,3 ; 0,28 V), pentes +0,06 et −0,06 ; C cuivre(I) : dismutation de Cu⁺, Cu₂O au-delà
de pH 3,3, médiamutation à pH 4 ; D attaque par l'acide et par l'air, cémentation par le fer : 2,8 kg de fer et
3,2 kg de cuivre par m³).

## Cartes
Deck de **25 cartes** (et non 78) : 5 corrigées, 8 ajoutées à la fin (pente Fe(OH)₃/Fe²⁺, frontière verticale
`form`, conventions, principe de construction, stabilité du dichlore, iodométrie et pH, Winkler `form`, cuivre et
acide).

## Notations
Celles d'« Oxydoréduction » : demi-équation α Ox + p H⁺ + n e⁻ = β Red + q H₂O, pente −0,06 p/n, c_tr, gaz sous
1 bar, HO⁻. Convention des figures : chaque espèce dissoute à c_tr sur une frontière (et non « égalité de la
concentration en atomes », qui ne change que les frontières de Cl₂ ou I₂ de quelques centièmes de volt) ; énoncée à
chaque figure.

## Doutes
- Diagramme du manganèse volontairement simplifié (n.o. +II et +III, sans MnO₂ ni MnO₄⁻) comme dans les présentations
  usuelles de la méthode de Winkler ; en réalité Mn³⁺ libre se dismute en MnO₂ et Mn²⁺. Le texte le dit (« diagramme
  simplifié »).
- E°(IO₃⁻/I₂) = 1,19 V ; E°(HClO/Cl₂) = 1,63 V ; pKs(Cu₂O, ½ Cu₂O + ½ H₂O = Cu⁺ + HO⁻) = 14,7 : valeurs usuelles des
  tables, cohérentes avec la frontière Cu₂O/Cu donnée dans l'énoncé du concours (E = 0,48 − 0,06 pH).
- Carte n° 1 (« Marcel Pourbaix (1938) ») laissée telle quelle : la date varie selon les sources (premiers travaux
  vers 1938, thèse en 1945).
