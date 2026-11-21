# Revue du chapitre `machines` — « Machines thermiques » (1ʳᵉ année, prefix `mth`)

Revue du 2026-11-21 (lot 5 du point 4 de l'audit), d'après `CONSIGNES-1A.md` (et `em/CONSIGNES-EM.md`,
`em/CONSIGNES-EM-1A.md`, `revue/CONSIGNES-REVUE.md`, `maths/CONSIGNES.md`). Programme : PTSI 2021, partie 3.5
« Machines thermiques » (`pdf-pt/prog/ptsi.txt`, l. 1608-1624) et partie 3.2 (interprétation géométrique du
travail) ; 2ᵉ année : `phys.txt` parties 1.5-1.6 (l. 717-786 : écoulements, thermodynamique industrielle). Motifs :
audit `docs/audit-2026-11/physique-1a.md` (l. 52, 111, 122) et `docs/audit-2026-11.md` §5 point 3 (« conventions de
signe unifiées, cogénération, ordres de grandeur des rendements »). Rédaction originale ; toutes les valeurs recalculées.

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `mth-cours.src.html` | cours réécrit : bloc « AU PROGRAMME · PTSI », 11 sections §1-§11, une section « POUR ALLER PLUS LOIN · LES CYCLES INDUSTRIELS (2ᵉ ANNÉE) », 16 exemples traités chiffrés, 12 figures calculées, ≈ 101 ko |
| `mth-meth.src.html` | 10 méthodes (étapes, exemple éclair chiffré), 4 pièges |
| `mth-exos.src.html` | 12 exercices (11 + « Concours PT » en 4 parties), un seul `.exo-wrapper` |
| `mth-cartes-corr.json` | 12 corrections (11 réponses seules, 1 question seule) |
| `mth-cartes-ajout.js` | 13 cartes ajoutées en fin de deck (25 → 38) |
| `mth-cours.tpl.html` + `mth_construire.py` | gabarit du cours (`@@FIG:nom@@`) et assemblage |
| `mth_figs.py` → `mth_figs.json` | 12 figures : flux d'énergie des 3 machines, cycle rectangulaire en (P, V) et (T, S), diagramme de Raveau, Carnot en (P, V) et (T, S), Beau de Rochas et Diesel, Stirling, organes d'une centrale, organes d'une machine frigorifique, cycle de centrale dans le diagramme (P, v) de l'eau (CoolProp 8, IAPWS-95), cogénération, cycle de centrale en (T, s) et cycle frigorifique R134a en (log P, h) (CoolProp) |
| `mth_calculs.py`, `mth_calculs_exos.py` | vérification de tous les nombres du cours et des exercices (méthodes : vérifiées à la main et dans ces scripts) |
| `mth_cartes.py` | génère les deux fichiers de cartes |
| `mth_couper.py` | coupe aux « = » les formules en ligne trop longues pour le téléphone |
| `mth_voir.py`, `mth_cartes_rendu.js` | aperçu PNG des figures (clair et sombre) ; rendu MathJax des cartes corrigées et ajoutées |

Contrôles passés : `verif_src.py` sur les trois panneaux (aucune erreur ni « attention ») ; `apercu_src.py` à 390 et 1440 px
pour les trois panneaux : `merr`, `brut`, `larges` vides, `scrollW` = largeur, aucune erreur JS ; captures du cours (1440) et
des 12 figures (clair et sombre, `mth_voir.py`) regardées ; `corriger_cartes.py --essai` (12 corrigées) et
`ajouter_cartes.py --essai` (25 → 38) sans erreur ; rendu MathJax des 25 cartes touchées : aucune erreur.

## Erreurs trouvées dans l'existant (et corrigées)

1. **Conventions de signe** (point de l'audit) : le panneau du dépôt avait déjà été en partie repris (§1 et §4 en « énergie
   reçue »), mais il restait des mélanges : rendement écrit \(1 - |Q_f|/Q_c\) à côté de \(Q_f\) algébrique (§1, carte 0),
   entropie créée \(-Q_c/T_c + |Q_f|/T_f\) (carte 13), corrigé de l'ancien exo 01 Q3 « \(\Delta S_{univ} = -Q_c/T_c +
   (-Q_f)/T_f\) (attention aux signes…) ». **Une seule convention partout** : \(W\), \(Q_C\), \(Q_F\) reçus par le fluide,
   annoncée en tête du cours (§1) et rappelée dans les méthodes, les énoncés et les cartes ; \(S_{\text{créée}} =
   -(Q_C/T_C + Q_F/T_F)\).
2. **Carte 10** « Loi de Gay-Lussac sur une adiabatique » : c'est la **loi de Laplace** (la question elle-même est fausse) →
   question corrigée, réponse inchangée (progression conservée par la réponse).
3. **Carte 20** : « l'aire sous la courbe [en (T, S)] représente la chaleur échangée \(Q = \int T\,\mathrm dS\) » sans
   l'hypothèse **réversible** → réponse corrigée.
4. **Carte 21** : « inégalité de Clausius pour un cycle réversible : = 0 » → égalité de Clausius, cas réversible de
   l'inégalité.
5. **Programme non couvert** : cogénération absente ; ordres de grandeur des rendements réels absents ; aucune justification
   du sens des échanges ni de l'impossibilité du moteur monotherme ; théorème de Carnot énoncé sans démonstration ;
   efficacités appelées « COP » sans le mot du programme ; pas de mise en œuvre expérimentale ; pas de machine à
   changement d'état (alors que le programme demande d'« analyser un dispositif concret »). Tout est traité (tableau
   ci-dessous).
6. **Ancien « Concours PT » n° 1** (Carnot 600/300 K, \(Q_c = 1\) kJ, puis COP de la pompe à chaleur) : doublon exact de
   l'exo 01 → fusionné dans l'exo 01 (Q5). Ancien « Concours PT » n° 2 (moteur réel, entropie créée) : gardé en exo 09,
   complété par la relation \(-W = \eta_C Q_C - T_F S_{\text{créée}}\). Nouveau sujet « Concours PT » en 4 parties.
7. Imprécisions de l'ancien cours supprimées : figure (T, S) dessinée à la main (remplacée par des figures calculées) ;
   « taux de détente isobare \(r_c\) » sans démonstration du rendement Diesel (démontré) ; formule de Beau de Rochas
   donnée sans démonstration (démontrée) ; « COP » sans borne de Carnot démontrée.

Les autres cartes ont été relues : justes.

## Couverture du programme, avant → après

| Capacité exigible (PTSI 3.5, et 3.2 pour le travail) | Avant | Après |
|---|---|---|
| Donner le sens des échanges pour un moteur ou un récepteur ditherme | énoncé sans justification | §4 (démonstration, diagramme de Raveau), §6 ; méthode 3 ; exos 01, 02 ; cartes |
| Analyser un dispositif concret et le modéliser par une machine ditherme | absent | §1, §10 (centrale, réfrigérateur, organes, figures) ; méthodes 1, 9 ; exos 03, 04, concours ; cartes |
| Définir rendement et efficacité, les relier aux énergies échangées | §1, §3 (formules) | §4, §6 ; méthode 4 ; tous les exercices |
| Justifier et utiliser le théorème de Carnot | énoncé | §2 (Clausius), §5 (démonstration, travail perdu), §6 (récepteurs), §7 ; méthode 5 ; exos 01, 02, 05, 09, 10, 11 |
| Citer des ordres de grandeur des rendements réels | 2 phrases | §4, §5, §6, §8, §9, §10, tableau du §11 ; carte ajoutée |
| Expliquer le principe de la cogénération | **absent** | §11 (définition, exemple chiffré, figure, coût en rendement de Carnot) ; méthode 4 ; concours C ; carte |
| Mettre en œuvre une machine cyclique ditherme | **absent** | §6 (pompe à chaleur pédagogique, efficacité mesurée), §9 (Stirling instrumenté) ; méthode 10 ; concours B |
| Travail sur un cycle, interprétation dans le diagramme de Clapeyron | §4 (une phrase) | §3 (figure calculée, (P, V) et (T, S)) ; méthode 7 |
| Cycles décrits par un énoncé (Carnot, Beau de Rochas, Diesel, Stirling) | Carnot, Otto, Diesel (formules) | §7, §8, §9 avec démonstrations ; méthodes 6, 8 ; exos 05-08 |
| Vu en 2ᵉ année : premier principe en écoulement, diagrammes (T, s) et (log P, h) des fluides réels | (T, S) cité sans statut | « Pour aller plus loin (2ᵉ année) » avec deux figures calculées et renvois à `thermoouv` et `thermodiff` |

## Sections du cours

§1 Machines thermiques et sources (définitions, convention unique, figure des flux) · §2 Bilans sur un cycle (premier principe,
inégalité de Clausius, pas de moteur monotherme, test d'une machine) · §3 Le cycle dans les diagrammes (\(W = -\oint P\,\mathrm dV\),
aire en (T, S), cycle rectangulaire calculé) · §4 Moteur ditherme et rendement (sens des échanges démontré, Raveau, voiture) ·
§5 Théorème de Carnot (démonstration, \(-W = \eta_C Q_C - T_F S_{\text{créée}}\), centrale au charbon) · §6 Réfrigérateur,
climatiseur, pompe à chaleur (efficacités, bornes démontrées, maison, congélateur, mesure en TP) · §7 Cycle de Carnot d'un
gaz parfait (calcul complet, figure) · §8 Moteurs à combustion interne (Beau de Rochas et Diesel démontrés, cylindre de
500 cm³) · §9 Moteur de Stirling (régénérateur, TP) · §10 Machines à changement d'état (organes, cycle de centrale dans le
diagramme (P, v) de l'eau, refroidissement d'une centrale nucléaire, efficacité d'un réfrigérateur au R134a) · §11 Rendements
réels et cogénération (tableau, exemple, figure) · Pour aller plus loin (2ᵉ année).

## Méthodes (10)

1 Modéliser un dispositif · 2 Écrire les deux bilans sur un cycle · 3 Trouver le sens des échanges · 4 Définir et calculer un
rendement ou une efficacité (et une cogénération) · 5 Utiliser le théorème de Carnot · 6 Calculer W et Q transformation par
transformation · 7 Lire un cycle dans un diagramme · 8 Établir le rendement d'un cycle à deux adiabatiques · 9 Analyser une
machine à changement d'état · 10 Exploiter des mesures sur une machine réelle.

## Exercices (12)

| N° | Titre | Origine |
|---|---|---|
| 01 ★ | Rendement de Carnot, moteur réel et machine inversée | ancien exo 01 + ancien « Concours PT » n° 1 (doublon), réécrit en convention unique, Q4 ajoutée |
| 02 ★ | Machines possibles ou impossibles (Raveau) | nouveau |
| 03 ★★ | Réfrigérateur : efficacité et irréversibilité | ancien exo 03, notations |
| 04 ★★ | Pompe à chaleur ou chauffage électrique | ancien exo 05, Q2 complétée (puissance prise dehors) |
| 05 ★★ | Cycle de Carnot d'un gaz monoatomique | ancien exo 04, Q4 ajoutée (travaux des adiabatiques) |
| 06 ★★ | Cycle de Beau de Rochas | ancien exo 02 (« r » → « a », redondance du corrigé retirée), Q4 ajoutée |
| 07 ★★ | Cycle Diesel | nouveau |
| 08 ★★ | Moteur de Stirling et régénérateur | nouveau |
| 09 ★★★ | Moteur ditherme réel : entropie créée et travail perdu | ancien « Concours PT » n° 2, Q4 complétée |
| 10 ★★★ | Cycle combiné d'une centrale électrique | ancien exo 06, Q4 ajoutée (valeurs réelles) |
| 11 ★★★ | Moteur entre deux réservoirs de capacité finie | nouveau |
| Concours PT | Chauffer un bâtiment : pompe à chaleur ou cogénération ? (A pompe à chaleur, B essai sur banc, C cogénération, D bilan) | nouveau |

## Cartes

- **Corrigées** (`mth-cartes-corr.json`, 12) : 0, 13 (convention mêlée à \(|Q_f|\)), 10 (question : Gay-Lussac → Laplace),
  20 (hypothèse réversible), 21 (égalité de Clausius), et, **réponses seules** pour harmoniser les notations avec le cours et
  la 2ᵉ année : 1, 2, 3, 4, 16, 22, 24 (\(T_c\), \(T_f\), \(Q_c\), \(Q_f\), « COP » → \(T_C\), \(T_F\), \(Q_C\), \(Q_F\),
  \(e_F\), \(e_{PAC}\)). Toutes ne touchent qu'un côté de la carte : progression conservée. Si l'on préfère ne corriger que
  les cartes fausses, retirer 1, 2, 3, 4, 16, 22 et 24 du fichier.
- **Ajoutées** (`mth-cartes-ajout.js`, 13) : inégalité de Clausius ; moteur monotherme ; sens des échanges ; travail perdu ;
  ordres de grandeur (val) ; cogénération ; Diesel / Beau de Rochas ; régénérateur ; pourquoi un changement d'état ; organes
  d'une machine frigorifique ; écarts de température dans les échangeurs ; efficacité mesurée en TP (form) ; climatiseur
  (val).

## Notations

Celles de la 2ᵉ année (`thermoouv`) : \(T_C\), \(T_F\) (températures des sources), \(Q_C\), \(Q_F\), \(W\) reçus par le fluide,
\(\eta = -W/Q_C\), \(\eta_C\), \(e_F\), \(e_{PAC}\), \(e_{F,C}\), \(e_{PAC,C}\) ; \(S_{\text{éch}}\), \(S_{\text{créée}}\) comme
`thermo3` ; énergies massiques \(q_C\), \(q_F\), \(w\) au §10. Majuscules choisies aussi pour éviter la collision avec
\(T_f\) (température finale, `thermo2`/`thermo3`) et \(T_c\) (température critique, `changement`). Rapport volumétrique \(a\),
rapport de détente préalable \(b\).

## Doutes et points à signaler

- **Questions des cartes 21, 22, 23** : elles gardent « Q_c », « T_c », « T_f » (minuscules) ; on ne pouvait pas toucher à la
  fois la question et la réponse des cartes 21 et 22. Sans conséquence pour la compréhension.
- **Machines à changement d'état en PTSI** : le §10 raisonne sur un kilogramme de fluide qui décrit un cycle et donne les
  énergies massiques \(q_C\), \(q_F\), \(w\) comme données (« les tables donnent… ») ; le premier principe en écoulement
  (\(\Delta h = w_i + q\)) et la lecture des diagrammes (T, s), (log P, h) sont signalés « 2ᵉ année » et regroupés en fin de
  chapitre, conformément au programme de PT (partie 1.6).
- **Simulateur** (`mth-simu`, non modifié) : son texte écrit encore « Q_chaud / Q_froid » et « η = |W|/Q_chaud » ; juste,
  mais à harmoniser un jour avec \(Q_C\), \(Q_F\).
- **`thermo2`, exercice « Cycle de Carnot — rendement et travail »** : notation \(Q_h\), \(T_h\) (encore une autre), hors du
  périmètre de ce lot ; à harmoniser.
- Figures larges (600 à 640 px de viewBox pour les figures doubles) : sur téléphone, le mécanisme `.lisible` du site les
  élargit puis les fait défiler ; contrôles à 390 px sans débordement de page.
- Valeurs « réelles » du tableau du §11 et des exemples : ordres de grandeur usuels (fourchettes), non tirés d'une source
  unique.
