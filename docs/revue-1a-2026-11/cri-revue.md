# Revue du chapitre `cristallin` — « Solides cristallins » (1ʳᵉ année, prefix `cri`)

Revue du 2026-11-21 (lot 5 du point 4 de l'audit), d'après `CONSIGNES-1A.md` (et `em/CONSIGNES-EM.md`,
`em/CONSIGNES-EM-1A.md`, `revue/CONSIGNES-REVUE.md`, `maths/CONSIGNES.md`). Programme : PTSI 2021, partie 4.3
« Structure et propriétés physiques des solides » (`pdf-pt/prog/ptsi.txt`, l. 1797-1866 ; « la maille CFC,
seule maille dont la connaissance est exigible »). Motifs : audit `docs/audit-2026-11/physique-1a.md` (l. 58, 68, 111, 128,
154) : chapitre mince (2 méthodes, 3 exercices), amorphe, allotropie, rayons et limites du modèle absents, maille définie
comme « le plus petit parallélépipède ». Rédaction originale ; toutes les valeurs recalculées (paramètres de maille des tables
usuelles, rayons ioniques de Shannon).

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `cri-cours.src.html` | cours réécrit : bloc « AU PROGRAMME · PTSI », 11 sections §1-§11, « POUR ALLER PLUS LOIN · HORS PROGRAMME », 14 exemples traités chiffrés, 7 figures calculées, un tableau (6 métaux CFC, ρ calculée et mesurée), ≈ 89 ko |
| `cri-meth.src.html` | 10 méthodes (étapes, exemple éclair chiffré), 3 pièges |
| `cri-exos.src.html` | 12 exercices (11 + « Concours PT » en 5 parties), un seul `.exo-wrapper` |
| `cri-cartes-corr.json` | liste vide : aucune carte fausse (contrôlé avec `corriger_cartes.py --essai`) |
| `cri-cartes-ajout.js` | 15 cartes ajoutées en fin de deck (21 → 36) |
| `cri-cours.tpl.html` + `cri_construire.py` | gabarit du cours (`@@FIG:nom@@`) et assemblage |
| `cri_figs.py` → `cri_figs.json` | 7 figures : réseau plan (motif, maille conventionnelle et primitive), maille CFC en perspective + face à l'échelle, plans compacts (couches A/B/C, sites O et T) + plan compact de la CFC, sites octaédriques et tétraédriques de la CFC, cubique centrée + coupe diagonale, diamant, NaCl et CsCl. Projection centrale calculée (azimut 35°, élévation 22°), tri en profondeur, arêtes cachées en tirets |
| `cri_calculs.py`, `cri_calculs_exos.py` | vérification de tous les nombres du cours, des méthodes et des exercices |
| `cri_cartes.py` | génère les deux fichiers de cartes |
| `cri_couper.py` | coupe aux « = » les formules en ligne trop longues pour le téléphone |
| `cri_voir.py`, `cri_cartes_rendu.js` | aperçu PNG des figures (clair et sombre) ; rendu MathJax des cartes ajoutées |

Contrôles passés : `verif_src.py` sur les trois panneaux (aucune erreur ni « attention ») ; `apercu_src.py` à 390 et 1440 px
pour les trois panneaux : `merr`, `brut`, `larges` vides, `scrollW` = largeur, aucune erreur JS ; captures du cours (1440) et
des 7 figures (clair et sombre) regardées ; `corriger_cartes.py --essai` (0) et `ajouter_cartes.py --essai` (21 → 36) sans
erreur ; rendu MathJax des 15 cartes ajoutées : aucune erreur.

## Erreurs trouvées dans l'existant (et corrigées)

1. **Définition de la maille** (point de l'audit) : le dépôt avait déjà nuancé la phrase (« la plus petite possible est dite
   primitive »), mais sans figure ni distinction claire entre maille primitive et conventionnelle. Le §2 définit réseau,
   nœud, motif, maille, maille primitive (un nœud) et maille conventionnelle (multiple, choisie pour la symétrie), avec une
   figure calculée et une notice « Erreur classique » qui cite la définition fausse.
2. **Couleurs codées en dur** dans l'ancienne figure NaCl / diamant (`fill:#fff` sur des libellés) et libellés de 7 à 9 px :
   interdits par les règles du site (contraste en sombre, police ≥ 12 px). Figure remplacée par des figures calculées aux
   classes du site.
3. **Figures CC et CFC dessinées à la main** (positions approximatives, pas de perspective) : remplacées par des projections
   calculées et des coupes à l'échelle (contact le long de la diagonale de face, de la grande diagonale).
4. **Ancien exo 02** (fer α / γ) : « le passage α → γ s'accompagne donc d'une contraction (à rayon atomique comparable) » :
   la prévision à rayon constant (8 %) est six fois plus grande que la contraction réelle (1 %) ; la question est complétée
   (Q3, données à 912 °C) et l'écart interprété (rayon métallique fonction de la coordinence), comme au §11.
5. **Habitabilité tétraédrique** « ≈ 0,22 R » : valeur exacte \((\sqrt{3/2} - 1)R = 0{,}225\,R\), démontrée.
6. **Ancien « Concours PT »** (cuivre CFC : Z, a, C, ρ) : doublon de l'exo 01 → fusionné dans l'exo 01 (Q2 démonstration de
   la compacité, Q4 calcul à partir du rayon). Nouveau sujet « Concours PT » en 5 parties.
7. **Programme non couvert** : amorphe / semi-cristallin, allotropie, influence des conditions de formation, rayons covalent,
   de van der Waals et ionique, empilements compacts et sites entre les plans, logiciel, métaux dans le tableau périodique,
   énergies de liaison, solubilisation, limites du modèle : tout est traité (tableau ci-dessous).

Les 21 cartes ont été relues : aucune n'est fausse (la carte 0 dit déjà que la maille CFC n'est pas primitive).

## Couverture du programme, avant → après

| Capacité exigible (PTSI 4.3) | Avant | Après |
|---|---|---|
| Solide amorphe, cristallin, semi-cristallin ; allotropie ; influence des conditions de formation | **absent** | §1 (définitions, trempe, exemples chiffrés : quartz / verre, étain) ; exo 03 ; cartes |
| Décrire un cristal parfait comme assemblage de mailles parallélépipédiques | 1 paragraphe | §2 (réseau, motif, maille primitive et conventionnelle, figure) ; méthode 1 ; cartes |
| Population, coordinence, compacité pour une structure fournie | CS, CC, CFC | §3, §4, §5 (hc), §7 (CC), §8 (diamant), §10 (NaCl, CsCl) ; méthodes 2, 4, 5 ; exos 01, 02, 04, 05, 07, 10 |
| Masse volumique | formule | §3, §4 (tableau calcul / mesure), §5, §7-§10 ; méthode 6 ; exos 01, 02, 05, 07-10, concours |
| Rayons métallique, covalent, de van der Waals, ionique reliés à la maille | rayon « R » seulement | §7, §8, §9, §10 (définitions, exemples chiffrés) ; méthode 3 ; exos 07, 08, 11 ; cartes |
| Empilements compacts : interstices T et O entre les plans | 1 phrase (reveal) | §5 (couches A/B/C, ABAB et ABCABC, sites entre plans, figure) ; exo 10 ; carte |
| Maille CFC : localiser, dénombrer les sites, habitabilité | valeurs sans démonstration | §6 (figure, démonstrations, acier, palladium) ; méthode 7 ; exo 06, concours B |
| Utiliser un logiciel ou des modèles cristallins | **absent** | §6 (paragraphe « Utiliser un logiciel ») |
| Limites du modèle du cristal parfait | **absent** | §11 (défauts, vibrations, fer à 912 °C, Fe₁₋ₓO, porosité, c/a du zinc, blende) ; méthode 10 ; exos 04, 10, 11, concours D |
| Métaux : position dans le tableau, liaison métallique et propriétés | 1 ligne | §7 ; méthode 9 ; exo 03, concours A3, E1 |
| Solides covalents et moléculaires : liaisons, énergies, directionnalité, propriétés | 2 lignes | §8, §9 (graphite, argon, glace, solubilité) ; exos 03, 07, 09 ; cartes |
| Solides ioniques : énergie, non-directionnalité, charges localisées, propriétés | 1 ligne + 6/6 | §10 (modèle, NaCl, CsCl, condition de stabilité, énergie, dissolution) ; méthode 8 ; exos 02, 08, 11, concours C, E |

## Sections du cours

§1 Amorphe, cristallin, semi-cristallin (allotropie) · §2 Modèle du cristal parfait (réseau, motif, maille ; figure) · §3
Population, coordinence, compacité, masse volumique (polonium) · §4 Maille CFC (figure, démonstrations, cuivre, tableau) ·
§5 Empilements compacts (couches, hc fournie, magnésium et zinc ; figure) · §6 Sites de la CFC (figure, habitabilité démontrée,
acier, palladium, alliages, logiciel) · §7 Cristaux métalliques (tableau périodique, liaison, propriétés, CC fournie : fer α,
sodium) · §8 Cristaux covalents (diamant, silicium, graphite) · §9 Cristaux moléculaires (argon, glace, solubilité) · §10
Cristaux ioniques (NaCl, CsCl, condition de stabilité, énergie, propriétés) · §11 Limites du modèle (fer à 912 °C, Fe₁₋ₓO,
autres écarts) · Pour aller plus loin (diffraction X et loi de Bragg, réseaux de Bravais, maille primitive de la CFC).

## Méthodes (10)

1 Décrire un cristal (réseau, motif, maille) · 2 Calculer la population · 3 Trouver la direction de contact et relier
paramètre et rayons · 4 Déterminer une coordinence · 5 Calculer une compacité · 6 Calculer une masse volumique (ou remonter
au paramètre) · 7 Localiser, dénombrer et évaluer les sites de la CFC · 8 Analyser une structure ionique fournie · 9 Relier
la nature des liaisons aux propriétés · 10 Confronter le modèle aux mesures.

## Exercices (12)

| N° | Titre | Origine |
|---|---|---|
| 01 ★ | Le cuivre (CFC) | ancien exo 01 + ancien « Concours PT » (doublon) : démonstration de la compacité, Q4 à partir du rayon |
| 02 ★ | Lire une structure fournie : populations et formules (cuprite, fluorine, ReO₃) | nouveau |
| 03 ★ | Reconnaître le type d'un solide | nouveau |
| 04 ★★ | Comparaison CC / CFC : le fer | ancien exo 02, Q3 ajoutée (912 °C, limite du modèle) |
| 05 ★★ | Identifier une structure par la masse volumique : le niobium | nouveau |
| 06 ★★ | Sites de la CFC : le carbone dans l'austénite | nouveau |
| 07 ★★ | Un solide covalent : le carbure de silicium | nouveau |
| 08 ★★ | Structures ioniques : la règle des rapports de rayons (KCl, CsCl) | nouveau |
| 09 ★★ | Carboglace et quartz : deux dioxydes, deux types de solides | nouveau |
| 10 ★★★ | Hexagonal compact : le titane (contact entre couches quand \(c/a \lt 1{,}633\)) | nouveau |
| 11 ★★★ | Mesurer des rayons ioniques (additivité, méthode de Landé) | nouveau |
| Concours PT | Le nickel et son oxyde (A métal CFC, B insertion, C NiO, D non-stœchiométrie, E propriétés) | nouveau |

## Cartes

- **Corrigées** : aucune (`cri-cartes-corr.json` = `[]`).
- **Ajoutées** (`cri-cartes-ajout.js`, 15) : cristallin / amorphe / semi-cristallin ; vitesse de refroidissement ; allotropie ;
  maille primitive et conventionnelle ; empilements ABAB et ABCABC ; position des sites tétraédriques ; habitabilité (form) ;
  rayons métallique, covalent, de van der Waals ; rayon ionique ; NaCl (form) ; CsCl (form) ; diamant (form) ; énergies de
  cohésion (val) ; ionique cassant / métal ductile ; limites du modèle.

## Notations

\(a\) paramètre de maille, \(Z\) population, \(R\) rayon (métallique), \(r_+\), \(r_-\) rayons ioniques, \(r_O\), \(r_T\)
habitabilités, \(r_{\text{cov}}\), \(r_{\text{vdW}}\), \(C\) compacité, \(\rho\), \(M\), \(N_A\) (écriture majoritaire du site :
l'ancien cours écrivait \(\mathcal N_A\)). Structures fournies explicitement signalées « (fournie) ».

## Doutes et points à signaler

- **Valeurs expérimentales** : paramètres de maille des tables usuelles (température ambiante, sauf fer à 912 °C et argon
  près de 0 K) ; distance Ar–Ar 376 pm (valeur classique des tables des cristaux de gaz nobles) ; maille de la glace
  \(a = 452{,}3\), \(c = 736{,}7\) pm et de CO₂ solide \(a = 562{,}4\) pm à 150 K : valeurs de la littérature citées de mémoire,
  cohérentes avec les masses volumiques connues (0,917 et 1,64 g·cm⁻³). Wüstite et NiO non stœchiométriques : données
  choisies plausibles (\(x\) de quelques pour cent).
- La carte 10 (« r_T ≈ 0,22 R ») reste juste à l'arrondi près ; la carte d'habitabilité ajoutée donne 0,225.
- Le §5 présente l'hexagonal compact comme structure **fournie** (le programme n'exige que la CFC) ; l'exo 10 donne la
  distance entre couches \(\sqrt{a^2/3 + c^2/4}\) comme admise.
- Les figures 3D sont en perspective centrale réelle (les arêtes verticales convergent légèrement) ; les sphères sont
  réduites pour laisser voir la structure, ce que disent les légendes.
