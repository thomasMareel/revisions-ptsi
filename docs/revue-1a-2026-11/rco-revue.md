# Revue du chapitre `regimecontinu` (prefix `rco`) — « Lois de l'électrocinétique — régime continu » — 2026-11-21

Objet (audit 2026-11-14, `docs/audit-2026-11/physique-1a.md` §2 point 7, §4, §5 point 6) : l'un des deux chapitres les plus
minces de la physique (3 322 signes de cours, 2 méthodes, 4 exercices, 14 cartes) alors qu'il ouvre l'électrocinétique.
Manquaient : condition de l'ARQS et ordres de grandeur, quantification de la charge, référence de potentiel, résistances
d'entrée et de sortie (seulement une méthode de `filtres`), bloc « Au programme ». Programme : PTSI 2021, partie 1.2
« Signaux électriques dans l'ARQS » (`pdf-pt/prog/ptsi.txt`, l. 664-700).

## Fichiers produits (dans `AN1/`)
- `rco-cours.src.html` (74 ko, 37 300 signes de texte hors figures) — assemblé par `rco_construire.py` depuis
  `rco-cours.tpl.html` et `rco_figs.json` ;
- `rco-meth.src.html` (10 méthodes), `rco-exos.src.html` (11 exercices + 1 « Concours PT », assemblé depuis `rco-exos.tpl.html`) ;
- `rco-cartes-corr.json` (2 réponses retouchées), `rco-cartes-ajout.js` (15 cartes) ;
- scripts : `rco_svg.py` (petite bibliothèque de schémas électriques aux classes du site, partagée avec `po`), `rco_figs.py`
  (11 figures), `rco_calculs.py` (exemples du cours), `rco_calculs_exos.py` (exercices anciens et nouveaux), `rco_voir.py`
  (aperçu clair/sombre des figures), `rco_cartes_rendu.py` (rendu MathJax des cartes), `rco_construire.py` ;
  copies des anciens panneaux : `rco_orig_{cours,meth,exos}.html`.

## Erreurs trouvées et corrigées
| Où | Problème | Correction |
|---|---|---|
| Cours §1 (ancien) | ARQS nommée sans sa condition ni ses conséquences | §3 complet : \(L/c \ll T \Leftrightarrow L \ll \lambda\), conséquences (même courant dans une branche, Kirchhoff instantané), figure calculée, 3 exemples |
| Cours §4 (ancien) | modèle de Norton et équivalence présentés comme exigibles (le programme 2021 ne cite que Thévenin) | Norton, Millman, superposition regroupés en « Pour aller plus loin · hors programme » |
| Cours §2 (ancien) | loi des nœuds non reliée à la conservation de la charge (capacité exigible) | démonstration dépliable au §5 |
| Cours (ancien) | aucune référence de potentiel, aucun ordre de grandeur (I, U, R) | §1, §2, §6 : trois tableaux d'ordres de grandeur |
| Ancien concours « échelle infinie », B2 | \(|R_4 - \varphi R|/\varphi R \approx 0{,}05\,\%\) | 0,06 % (34/21 = 1,61905 ; φ = 1,61803) |
| Ancien EXO 02, Q2 | Norton demandé sans signalement | question marquée « (Non exigible en PTSI.) », notation η du cours |
| Cartes 10 et 11 (Norton, équivalence) | hors programme non signalé | réponse préfixée « Hors programme en PTSI : » (questions inchangées) |

Aucune carte fausse sur le fond. Les deux anciens « Concours PT » (justes) deviennent EXO 10 et EXO 11 : un seul « Concours PT »
par chapitre.

## Couverture du programme (partie 1.2) : avant → après
| Capacité exigible | Avant | Après |
|---|---|---|
| Grandeurs continues compatibles avec la quantification de la charge | absent | §1 (argument chiffré), EXO 02, carte |
| Intensité = débit de charge | une formule | §1 (2 exemples : vitesse de dérive, mAh), EXO 02 |
| Ordres de grandeur des intensités et des tensions | absent | §1, §2 (tableaux), cartes `val` |
| Potentiel, référence, tension | une phrase | §2 (masse, additivité, exemple de changement de référence, piège des masses en TP) |
| Condition de l'ARQS (taille, fréquence) | nommée seulement | §3 (figure calculée log-log, 3 exemples), méthode 1, EXO 03, concours A1, 2 cartes |
| Loi des nœuds ↔ conservation de la charge ; loi des mailles | énoncés | §5 (démonstration, comptage des équations, exemple à deux mailles + bilan), méthodes 3-4, EXO 04 |
| Algébriser, conventions récepteur / générateur | une phrase | §4 (figure, justification de \(ui\), exemple batterie), méthode 2, carte |
| Relations i-u, ordres de grandeur de R, effet Joule | loi d'Ohm | §6 (caractéristiques calculées, tableau, exemple bouilloire et rallonge) |
| Énergie stockée (C, L), ordres de grandeur de L et C | absent | renvoyés au chapitre `premierordre` §1-2 (dit dans le bloc « Au programme ») |
| Représentation de Thévenin | présente | §7 (point de fonctionnement avec lampe non linéaire calculée, mesure de E et r, adaptation démontrée), méthodes 7-8, EXO 05, 09, 10 |
| Associations de deux résistances | formules | §8 (démonstration, réseau réduit pas à pas, figure), méthode 5, EXO 11 |
| Diviseurs de tension et de courant | formules | §9 (conditions, démonstrations, diviseur chargé, shunt), méthode 6, EXO 01, 06 |
| Résistances d'entrée et de sortie (notice, GBF, oscilloscope, multimètre) | absent du cours | §10 (définitions, figure calculée, tableau des appareils, tension moitié, voltmètre qui fausse la mesure), méthode 9, EXO 07, 08, concours C-D, 3 cartes |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 10 sections + « Pour aller plus loin ») : §1 Charge et courant ; §2 Potentiel et
tension ; §3 ARQS ; §4 Conventions et puissance ; §5 Lois de Kirchhoff ; §6 Résistances et sources idéales ; §7 Source
réelle : modèle de Thévenin ; §8 Associations de résistances ; §9 Diviseurs ; §10 Résistances d'entrée et de sortie ;
PAPL Norton, Millman, superposition (vérifiés sur l'exemple du §5). 14 exemples traités chiffrés, 9 notices « Erreur
classique », 8 figures SVG calculées (domaine de l'ARQS en log-log, conventions, circuit à deux mailles, caractéristiques,
Thévenin et point de fonctionnement avec lampe non linéaire, réseau à réduire, diviseurs, liaison sortie-entrée et courbe
\(R_e/(R_e+R_s)\)), vérifiées en clair et en sombre.

**Méthodes** (10) : vérifier l'ARQS ; orienter et choisir les conventions ; Kirchhoff ; loi des nœuds en potentiels ;
associations ; diviseurs ; modéliser une source par Thévenin ; Thévenin équivalent d'un réseau (variante Norton signalée
non exigible) ; effet d'une résistance d'entrée ou de sortie ; bilan de puissance. Les 2 anciennes méthodes sont reprises
(3 et 8).

**Exercices** (12) : EXO 01 pont diviseur (ancien) ; EXO 02 charge et vitesse des électrons ; EXO 03 ARQS dans quatre
situations ; EXO 04 deux sources (nœuds en potentiels, bilan) ; EXO 05 générateur réel (ancien) ; EXO 06 pont de Wheatstone
et jauge (figure) ; EXO 07 montages amont / aval (figure) ; EXO 08 GBF, oscilloscope, haut-parleur ; EXO 09 point de
fonctionnement d'une lampe ; EXO 10 Thévenin et transfert de puissance (ancien concours) ; EXO 11 échelle infinie (ancien
concours, corrigé) ; **Concours PT** « Chaîne de mesure d'une température par sonde Pt100 » (A câble et ARQS, B diviseur,
non-linéarité et auto-échauffement, C résistance d'entrée de la carte, D mesure en quatre fils, figure). Tous les résultats
recalculés (`rco_calculs_exos.py`).

**Cartes** : 14 → 29 (2 réponses préfixées « Hors programme en PTSI », 15 ajoutées à la fin : quantification, condition et
conséquences de l'ARQS, ordres de grandeur I/U/R, tension et flèche, convention générateur, loi des nœuds, résistances
d'entrée et de sortie, transmission d'une tension, tension moitié, diviseur de courant, puissance maximale, mesure de E et r).
Formules rendues par MathJax sans erreur (`rco_cartes_rendu.py`).

## Notations
\(i = \mathrm{d}q/\mathrm{d}t\), \(u_{AB} = V_A - V_B\) (flèche vers A), \(E\) f.é.m. et \(r\) résistance interne (convention
générateur : \(u = E - ri\)), \(\eta\) courant électromoteur (Norton, hors programme), \(R_{\text{éq}}\), \(G = 1/R\),
\(E_{\text{th}}, R_{\text{th}}\), \(R_s, R_e, E_s\), \(\lambda = c/f\). Cartes anciennes : \(e\) et \(i_0\) (non modifiées).

## Doutes, remarques pour l'intégration
- **Renommage possible** : le chapitre traite désormais l'ARQS et les signaux variables ; « Lois de l'électrocinétique (ARQS)
  » ou « Signaux électriques dans l'ARQS » décrirait mieux son contenu. Laissé tel quel.
- La formule \(R = \rho\ell/S\) et la vitesse de dérive \(I = neSv\) ne sont pas exigibles en PTSI : présentées comme ordres
  de grandeur ou exemples.
- **À alléger ailleurs (doublons du socle)** : `rlc` §1 « Les bases » (trois dipôles, continuités, énergies) refait
  `premierordre` §1-2 : le réduire à un rappel avec renvoi ; `rlc` §4 « Vision énergétique » (moitié dissipée) : renvoyer
  à `premierordre` §8 ; les impédances complexes sont exposées trois fois (`rlc` §5, `filtres` §1, `signaux` §4) : n'en garder
  qu'une (par exemple `rlc` §5) et renvoyer ; la méthode 6 de `filtres` (résistances d'entrée/sortie) peut renvoyer à
  `regimecontinu` §10 et méthode 9.
- Figures : viewBox de 300 à 540 unités ; libellés à 12-13 px. Pas de couleur en dur ; halo des libellés en
  `var(--paper)` (paint-order) sur la figure de l'ARQS.
