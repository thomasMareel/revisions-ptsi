# Revue du chapitre `thermo1` — « Introduction thermodynamique » (1ʳᵉ année, prefix `thermo1`)

Revue du 2026-11-21, d'après `CONSIGNES-1A.md`. Programme : PTSI 2021, partie 3.1 (le programme officiel de PTSI,
l. 1460-1505). Motif : audit `docs/audit-2026-11/physique-1a.md` (§1 « Gaz réel … ❌ », §2 point 9, §4 point 2) : gaz réels
et isothermes d'Amagat absents. Consigne : **compléter** (sections ajoutées en fin de cours, reste inchangé sauf erreur).

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `thermo1-cours.src.html` | cours actuel + bloc « AU PROGRAMME · PTSI » en tête + §7, §8, §9 + « Pour aller plus loin · Van der Waals » ; 6 corrections ciblées ; 3 figures calculées |
| `thermo1-meth.src.html` | 6 méthodes actuelles + méthodes 7 et 8 + un piège (avant l'encadré « Pièges classiques », gardé en dernier) |
| `thermo1-exos.src.html` | exercices actuels corrigés + exos 07, 08, 09 (avant le « Concours PT ») + partie C ajoutée au Concours |
| `thermo1-cartes-corr.json` | 1 réponse corrigée |
| `thermo1-cartes-ajout.js` | 8 cartes ajoutées en fin de deck (45 → 53) |
| `ce_thermo1.py` (+ `thermo1-ajout.tpl.html`, `thermo1-cours.tpl.html`, `ce_construire.py`) | construction du cours à partir du panneau actuel |
| `ce_thermo1_mx.py` | construction des méthodes et des exercices à partir des panneaux actuels |
| `ce_calculs_thermo1.py` | vérification des nombres (CoolProp, numpy) ; figures dans `ce_figs.py` (`t1_*`) |

Contrôles passés : `verif_src.py` sans erreur ni « attention » (les 13 formules en ligne trop longues des exercices
existants ont été coupées) ; `apercu_src.py` à 390 et 1440 px pour les trois panneaux : `merr`, `brut`, `larges` vides,
pas de débordement, aucune erreur JS (l'ancien panneau Exercices débordait à 390 px : exos 03, 04, 06) ; figures
regardées en clair et en sombre ; `corriger_cartes.py --essai` et `ajouter_cartes.py --essai` (45 → 53) sans erreur.

## Erreurs trouvées (et corrigées)

1. **§2, libre parcours moyen dans un liquide** : « \(\ell \lt 10^{-11}\) m », plus petit qu'un atome → de l'ordre de la
   taille d'une molécule, quelques \(10^{-10}\) m ; **carte n° 13** identique, corrigée (réponse seule).
2. **§4, « Pourquoi R = N_A·k_B ? »** : « les expériences de Joule donnent \(E_c^{\text{tot}} = \frac32 nRT\) » (faux :
   la détente de Joule montre \(U = U(T)\)) → comparaison de \(PV = \frac23E_c^{\text{tot}} = Nk_BT\) (pression
   cinétique, admise) et de l'équation expérimentale \(PV = nRT\).
3. **§5, vibrations des diatomiques** « vers 6 000 K » → progressivement au-delà de 1 000 K environ pour N₂ et O₂ ;
   précision : \(U\) d'un diatomique est en général fourni.
4. **§6, « Diagramme isotherme P-V »** : axes mélangés (« V en fonction de P », liquide « quasiment horizontal », mais
   « palier à pression constante ») → isotherme dans le diagramme de Clapeyron (P en fonction de V) : branche liquide
   presque verticale, palier horizontal, branche gaz hyperbolique ; renvois au §9 et au chapitre `changement`.
5. **§5, encadré « En pratique »** : « Pour la PTSI, on reste dans le cadre du gaz parfait » — contraire au programme,
   qui demande de comparer gaz réel et gaz parfait → renvoi au §8, Van der Waals signalé hors programme.
6. **§3** : « Les interactions n'ont lieu uniquement pendant les chocs » (grammaire).
7. **Exo 02 Q3** : « 1 934 m/s, très proche de la vitesse de libération (11,2 km/s) divisée par quelques unités » →
   six fois moins, mais queue de distribution et haute atmosphère chaude : échappement lent de H₂.
8. **Exo 06 (Van der Waals)** : 24,94/1,957 = 12,74 (et non 12,72), d'où 11,83 bar (et non 11,81) ; valeur mesurée
   (11,7 bar) ajoutée ; titre « (hors programme, pour aller plus loin) ».
9. **Exo 05 Q1** : « Sous quelle forme s'exprime-t-elle, en eV ? » reformulée. **Concours** : notations \(p\), \(u^*\) →
   \(P\), \(u\) (celles du cours).

## Couverture du programme (partie 3.1), avant → après

| Capacité | Avant | Après |
|---|---|---|
| Échelles, libre parcours moyen | §1, §2 (ℓ liquide faux) | idem, corrigé |
| Paramètres d'un état microscopique et d'un état macroscopique | implicite | §7 (définitions, exemple chiffré : 1 L d'argon) |
| Pression par équilibre mécanique, température par équilibre thermique | méthodes 4-5, exos 03-04 | §7 (encadré + 2 exemples : piston diathermane, thermomètre à gaz) |
| Ordres de grandeur de volumes molaires ou massiques | \(V_m\) gaz, air | §9 (tableau eau, glace, fer, mercure, air, vapeur) ; cartes |
| Différence de compressibilité liquide / gaz sur des isothermes | une liste (axes faux) | §6 corrigé, §9 (figure calculée, exemple chiffré, dilatation) ; méthode 8 ; exo 09 ; cartes |
| Comparer gaz réel et gaz parfait (Clapeyron, Amagat) | une phrase | §8 (isothermes de CO₂ façon Andrews, isothermes d'Amagat de N₂, tableau des écarts, 3 exemples, ordres de grandeur) ; méthode 7 ; exos 07, 08, Concours C ; cartes |
| Hors programme | Van der Waals en exercice non signalé | « Pour aller plus loin · Van der Waals » (a, b depuis le point critique, exemple) ; exo 06 signalé |

## Contenu ajouté

- **Bloc « AU PROGRAMME · PTSI »** (en tête, sans §, numérotation inchangée), capacités renvoyant aux §.
- **§7** État microscopique, état macroscopique, équilibre ; **§8** Du gaz réel au gaz parfait ; **§9** Liquide et gaz :
  compressibilité, volumes usuels ; **Pour aller plus loin** : Van der Waals (la constante \(a\) déduite du point critique
  de CO₂, 3,66 L²·bar·mol⁻², recoupe la donnée de l'exo 06). Ces sections sont en fin de cours, comme demandé : le §7
  aurait sa place logique après le §2 si l'on réordonne un jour le chapitre.
- **Figures** (dans `ce_figs.py`) : isothermes de CO₂ en coordonnées de Clapeyron avec l'hyperbole du gaz parfait à
  50 °C ; isothermes d'Amagat de N₂ à 200, 300 et 500 K ; volume relatif de l'air et de l'eau comprimés à 20 °C.
- **Méthodes** : 7 « Comparer un gaz réel au modèle du gaz parfait » ; 8 « Choisir le modèle d'une phase et évaluer sa
  compressibilité ».
- **Exercices** : 07 mesurer \(R\) par extrapolation d'Amagat (CO₂ à 400 K, \(R\) retrouvé à 0,01 %) ; 08 bouteille de
  plongée (masse, autonomie, gaz réel contre gaz parfait) ; 09 compressibilité de l'eau des océans (≈ 35 m de niveau) ;
  Concours : partie C (écart au gaz parfait de l'air sous 200 bar).
- **Cartes** (+8) : coordonnées d'Amagat ; limite des basses pressions ; ordres de grandeur de l'écart ; forme des
  isothermes d'Amagat ; isothermes de Clapeyron d'un gaz réel ; compression de l'air et de l'eau ; volumes molaires
  usuels ; Van der Waals (préfixée « Hors programme en PTSI : »).

## Doutes

- Les 6 sections d'origine n'ont pas été réécrites (consigne) : elles restent sans exemple encadré ni figure, et le
  « Concours PT » existant reste court (une partie C ajoutée seulement).
- Le facteur \(PV_m/(RT)\) (facteur de compressibilité) et \(\chi_T\) ne sont pas nommés par le programme : le premier est
  introduit comme simple outil de comparaison, le second en « pour aller plus loin ».
- Les tables des écarts au gaz parfait et les données des exercices 07-08 sont calculées avec CoolProp (équations de
  référence) ; les valeurs de l'exo 09 (0,50 % pour 100 bar, 4,7 % à 1 100 bar à 2 °C) aussi.
