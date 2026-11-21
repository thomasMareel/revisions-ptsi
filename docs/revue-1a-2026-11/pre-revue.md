# Revue et réécriture : `precipitation` (prefix `pre`), « Réactions de dissolution et de précipitation » — 2026-11-21

Point 4 de l'audit (`docs/audit-2026-11/physique-1a.md` §2 point 4, §4 « chapitres minces », §5 points 6 et 7). Programme :
PTSI 2021, partie 4.4.1 (dissolution et précipitation), partie 4.1.1 (état final) et partie expérimentale 8 (titrages).

## Fichiers
- `pre-cours.src.html` (construit par `acb_construire.py` depuis `pre-cours.tpl.html` + `pre_figs.json`), `pre-meth.src.html`,
  `pre-exos.src.html` (depuis `pre-exos.tpl.html`), `pre-cartes-corr.json` (3 cartes), `pre-cartes-ajout.js` (15 cartes).
- Scripts : `pre_calculs.py` (cours), `pre_calculs_meth.py`, `pre_calculs_exos.py`, `pre_figs.py` (7 figures), `pre_code_cours.py`
  (code du §4, exécuté), `pre_scinder.py` (coupe les formules en ligne longues aux signes =) ; outils communs `acb_chimie.py`,
  `acb_tester_code.py`, `acb_cartes_rendu.js`, `acb_voir.py`.
- Copies des anciens panneaux : `pre_orig_{cours,meth,exos}.html`.

## Erreurs et défauts corrigés
1. Ancien §4 et carte 11 : « la frontière [d'un domaine d'existence] est une limite absolue, pas une convention ». Inexact : la
   frontière sépare bien présence et absence totale du solide, mais sa position dépend de la concentration de tracé, choisie par
   convention (cours §5, carte 11 corrigée par sa réponse).
2. Ancien §3 et carte 8 : « si l'anion du solide est une base faible (hydroxydes, carbonates, fluorures…) » — HO⁻ n'est pas une base
   faible ; réécrit (§7, carte 8).
3. Complexation présentée comme un facteur ordinaire : hors programme en PTSI, déplacée en « Pour aller plus loin » (avec un exemple
   chiffré, AgCl dans l'ammoniac) ; carte 13 préfixée « Hors programme en PTSI : ».
4. Deux exercices « Concours PT » dont l'un (A/B, effet d'ion commun en 3 questions) doublait l'EXO 01 : gardés comme EXO 03 et
   EXO 09 (justes, complétés), un vrai « Concours PT » en trois parties a été écrit.
5. Notations : \(K_s\) avec \(c^\circ\) partout, mol·L⁻¹, équations avec « = », divisions parenthésées.

## Couverture du programme, avant → après
| Capacité (PTSI 2021) | Avant | Après |
|---|---|---|
| Constante de dissolution, \(K_s\) | §1 | §1 (tableau de pK<sub>s</sub>, \(K_s\) déduit d'une solubilité) |
| Solubilité, lien avec \(K_s\), comparaisons | §1 (AX, AX₂) | §2 (formule générale, piège Ag₂CrO₄/AgCl, hydroxydes très peu solubles), méthode 1, EXO 01, 04 |
| Condition de précipitation, saturation | §2 | §3 (figure Q/K<sub>s</sub> calculée, mélange chiffré), méthode 2, EXO 02 |
| État final : équilibre ou transformation totale (rupture) | ❌ | §4 (méthode, exemples), méthode 3, EXO 05 |
| Combinaison linéaire des constantes | ❌ | §4 (conversion, dissolution par un acide, calcaire), méthode 4, EXO 06, concours A4 et B1 |
| Capacité numérique état final | ❌ | §4 (programme testé, avec test de rupture), EXO 05 Q3, EXO 06 Q2 |
| Domaine d'existence, espèces incompatibles | §4 (schéma) | §5 (figure calculée de 5 hydroxydes, concentration de tracé), méthode 5, EXO 07 |
| Facteurs : ion commun | 1 phrase | §6 (figure log s = f(log c) calculée, trinôme), méthode 6, EXO 03 |
| Facteurs : pH, courbes de solubilité | 1 phrase | §7 (figure pS = f(pH) : Cu(OH)₂, Al(OH)₃ amphotère, CaF₂), méthodes 7 et 10, EXO 08 |
| Facteurs : température, solvant | ❌ | §10 (tartre, données de la littérature) |
| Précipitations compétitives, séparation | exercice seul | §8 (figure pAg, Cl⁻/I⁻, Fe³⁺/Cu²⁺), méthode 8, EXO 07, 09, concours A3, C2 |
| Titrages par précipitation (Mohr, conductimétrie, indirect) | ❌ | §9 (2 figures simulées), méthode 9, EXO 10, 11, concours C |
| Procédés de retraitement, recyclage, séparation | ❌ | §8, §10 (5 procédés), concours (magnésium de l'eau de mer) |

## Contenu
- **Cours** : bloc « AU PROGRAMME · PTSI » + 10 sections (§1 produit de solubilité ; §2 solubilité ; §3 condition de précipitation ;
  §4 état final et combinaisons, avec programme Python ; §5 domaine d'existence ; §6 ion commun ; §7 influence du pH ;
  §8 précipitations compétitives ; §9 titrages par précipitation ; §10 température, solvant, procédés) + « Pour aller plus loin »
  (complexation, activités). 12 exemples traités chiffrés, 7 figures calculées. ≈ 60 000 car.
- **Méthodes** : 10 (les 2 anciennes reprises), chacune avec exemple éclair vérifié, 3 pièges.
- **Exercices** : 12 (les 4 anciens repris et complétés) : 01 solubilité de AgCl ; 02 précipitation après mélange ; 03 ion commun
  (avec le cas où l'approximation échoue) ; 04 comparer des solubilités (BaSO₄ en radiologie) ; 05 chlorure de plomb, équilibre ou
  dissolution totale, résolution numérique ; 06 conversions et dissolutions par combinaison (Mg(OH)₂ dans NH₄Cl, calcaire et vinaigre) ;
  07 séparation de Fe³⁺, Cu²⁺, Zn²⁺ par le pH ; 08 courbe de solubilité de Al(OH)₃ ; 09 séparation Cl⁻/I⁻ ; 10 méthode de Mohr
  (saumure) et conductimétrie ; 11 titrage indirect de Charpentier-Volhard ; **Concours PT** « Le magnésium de l'eau de mer »
  (précipitation par la chaux, combinaison de constantes, lavage, Mohr, titrage simultané Cl⁻ + Br⁻).
- **Cartes** : 3 réponses corrigées (8, 11, 13), questions inchangées ; 15 ajoutées (formule générale de \(s\), comparaison des
  solubilités, rupture d'équilibre, conversion, dissolution d'un hydroxyde par un acide, pH d'apparition, courbe pS(pH), amphotère,
  précipitations compétitives, Mohr, conductimétrie, pK<sub>s</sub> usuels, ion commun, tartre, procédés).
  `corriger_cartes.py … --essai` : 3 corrigées ; `ajouter_cartes.py … --essai` : 15 → 30. Rendu par `flashPretty` + MathJax contrôlé
  (`acb_cartes_rendu.js pre`) : aucune erreur.

## Vérifications
- Tous les nombres recalculés : `pre_calculs.py`, `pre_calculs_meth.py`, `pre_calculs_exos.py` ; code du §4 exécuté
  (`acb_tester_code.py pre-cours.tpl.html`, sorties conformes aux commentaires).
- `verif_src.py` : aucune erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges` vides, aucune erreur JS
  (formules en ligne longues coupées aux signes = par `pre_scinder.py`) ; figures regardées en clair et en sombre.

## Notations
\(K_s\), \(\text{p}K_s\), \(s\) (mol·L⁻¹), pS = −log(s/c°), pAg = −log([Ag⁺]/c°), \(Q\) (quotient de la dissolution), ξ ; mêmes
pK<sub>a</sub> que le chapitre acide-base. pK<sub>s</sub> : AgCl 9,75 ; AgBr 12,3 ; AgI 16,1 ; Ag₂CrO₄ 11,95 ; CaCO₃ 8,5 ; CaF₂ 10,4 ;
BaSO₄ 10,0 ; PbI₂ 8,0 ; PbCl₂ 4,8 ; AgSCN 12,0 ; Mg(OH)₂ 11,2 ; Ca(OH)₂ 5,3 ; Fe(OH)₂ 15,1 ; Fe(OH)₃ 38 ; Cu(OH)₂ 19,7 ;
Zn(OH)₂ 16,4 ; Ni(OH)₂ 15,2 ; Al(OH)₃ 32 (avec \(K = 10\) pour l'aluminate).

## Doutes
- Les pK<sub>s</sub> des hydroxydes (Fe(OH)₃, Al(OH)₃, Zn(OH)₂) et la constante de l'aluminate varient beaucoup selon les tables ; les
  valeurs choisies sont des valeurs d'école cohérentes entre elles. Le chapitre « Diagrammes E-pH » (`eph`) cite une frontière
  Fe³⁺/Fe(OH)₃ « à pH ≈ 3 » (autre concentration de tracé) : pas de contradiction, mais à harmoniser si ce chapitre est repris.
- L'EXO 09 (ancien) garde \(K_s(\mathrm{AgI}) = 8{,}5\times10^{-17}\) (pK<sub>s</sub> 16,07) au lieu de 16,1 : données de
  l'énoncé, résultats justes.
- Les données de pK<sub>s</sub> de CaCO₃ selon la température (§10) viennent de la loi de Plummer et Busenberg (1982), citée comme
  « données de la littérature ».
- Le titrage simultané Cl⁻ + Br⁻ du concours (C2) suppose les activités égales aux concentrations dans l'eau de mer diluée 20 fois
  (force ionique ≈ 0,035 mol·L⁻¹) : ordre de grandeur correct.
