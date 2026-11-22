# Revue du chapitre `chcentral` (prefix `cc`) — « Mouvement dans un champ central » — 2026-11-22

Objet (point 4 de l'audit, lot 6 ; `docs/audit-2026-11/physique-1a.md` l. 44, 70, 106, 121, 135, 147 ; `audit-2026-11.md` §5) :
doublon avec `mcinc` §3 (Kepler) ; confusion signalée entre \(L=mr^2\dot\theta\) et \(C=r^2\dot\theta\) ; capacité numérique
« trajectoires dans un champ de force centrale conservatif » absente ; deux « Concours PT » ; carte et cours divergents sur la
période géostationnaire. Programme : PTSI 2021, partie 2.6 (`pdf-pt/prog/ptsi.txt`, l. 1326-1380).

## Fichiers produits (dans `AN1/`)
- `cc-cours.src.html` (≈ 114 ko, `mcin_construire.py cc` depuis `cc-cours.tpl.html` et `cc_figs.json`) ;
- `cc-meth.src.html` (10 méthodes), `cc-exos.src.html` (11 exercices + 1 « Concours PT ») ;
- `cc-cartes-corr.json` (vide : aucune carte fausse), `cc-cartes-ajout.js` (14 cartes) ;
- scripts : `cc_figs.py` (6 figures), `cc_calculs.py`, `cc_calculs_exos.py`, `cc_code.py` et `cc_tester_code.py` (**tout le code
  affiché est exécuté**, cours et EXO 10), `cc_retouches*.py` ; copies des anciens panneaux `cc_orig_{cours,meth,exos}.html`.

## Erreurs et défauts corrigés
| Où | Problème | Correction |
|---|---|---|
| §1 (audit, erreur n° 5) | \(L\) et \(C\) confondus | déjà corrigé dans le dépôt (\(L=mC\)) ; repris : définition \(C=L_z/m\), notice « Erreur classique », carte |
| Concours 1 | géostationnaire calculé avec \(T=24\ \text{h}\) (86 400 s) | jour sidéral 86 164 s partout (EXO 07, §9, concours) |
| Deux « Concours PT » | format | un seul ; l'ancien « périgée/apogée » est repris par la méthode 7 et l'EXO 03 |
| Ancien EXO 02 (comète) | \(v_p=60\ \text{km/s}\) incompatible avec \(r_p\), \(r_a\) (l'énergie impose 58,1 km/s) ; excentricité demandée (hors programme) | données cohérentes (58,13 km/s), vérification \(E_m=-GMm/(2a)\) à la place de l'excentricité |
| Ancien EXO 03 (Lune) | « atomes d'H₂ » ; \(v_{\text{th}}\) d'un atome H comparée seule à \(v_{\text{lib}}\) | H₂ et N₂, critère \(v_{\text{lib}}\gt6v_{\text{th}}\), Lune et Terre |
| Ancien EXO 05 | \(C=5\times10^{10}\), \(GM=4\times10^{14}\) : orbite circulaire de 6 250 km, sous la surface | \(C=6\times10^{10}\) (9 000 km), bornes ajoutées |
| Ancien EXO 06 (Binet) | hors programme | retiré des exercices ; Binet et coniques en « Pour aller plus loin » |
| Ancienne figure \(E_{p,\text{eff}}\) | dessinée à la main, textes de 9-10 px | figure calculée (unités réduites), 12 px au moins |
| Ancienne figure des aires | aires « égales » dessinées à la main (triangles quelconques) | 12 secteurs de durées égales calculés par l'équation de Kepler |

## Couverture du programme (partie 2.6) : avant → après
| Capacité exigible | Avant | Après |
|---|---|---|
| Conservation de \(\vec L_O\) par le théorème ; mouvement plan ; loi des aires | définitions | §1-§2 (démonstrations, \(\vec L_O=\vec0\), Terre au périhélie et à l'aphélie, figure calculée), méthodes 1-2, EXO 03, cartes |
| Exprimer \(E_m\) à partir de l'équation du mouvement ; énergie potentielle effective | formule | §3-§4 (démonstration par \(\vec v\cdot\), tableau des \(E_p\), bornes calculées), méthode 3, EXO 05-06, cartes |
| Décrire qualitativement le mouvement radial ; lien entre borné et \(E_m\) | figure | §4-§5 (figure calculée, Coulomb répulsif et ressort, Rutherford), méthode 4, EXO 04-06, 09, cartes |
| Trajectoires par un langage de programmation | absent | §10 (`odeint`, validation par \(E_m\) et \(C\), dérive d'Euler, rosette d'une force en \(1/r^{2,3}\)), méthode 10, EXO 10, concours D, carte |
| Lois de Kepler, transposition aux satellites | liste | §6 (tableau des planètes, masse du Soleil), méthode 6, EXO 02 |
| Mouvement circulaire uniforme, période, troisième loi, énergie | formules | §7 (démonstrations, ISS, Lune, paradoxe du freinage), méthode 5, EXO 01, 07, cartes |
| Énergie du mouvement elliptique en fonction de \(a\) | « admis » | §8 (démonstration par les apsides, vis-viva, Halley, freinage de l'ISS), méthodes 7-8, EXO 03, 05, 08, concours, cartes |
| Orbites selon les missions ; géostationnaire, plan équatorial | encadré | §9 (justification, tableau des orbites, figure à l'échelle, libération, lancement vers l'est), méthode 9, EXO 07, 11, concours, cartes |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 10 sections + « Pour aller plus loin ») : §1 force centrale et conservation ; §2 loi des
aires ; §3 énergie ; §4 énergie potentielle effective ; §5 état lié, état de diffusion ; §6 lois de Kepler ; §7 mouvement
circulaire ; §8 mouvement elliptique ; §9 satellites ; §10 simulation ; hors programme : Binet, coniques, excentricité.
12 exemples traités chiffrés, 6 notices, 3 tableaux, 2 démonstrations dépliables, 2 programmes Python exécutés, 6 figures SVG
calculées (loi des aires sur une ellipse d'excentricité 0,6 ; \(E_{p,\text{eff}}\) newtonienne et trois niveaux ; Coulomb répulsif
et ressort ; orbites des satellites à l'échelle ; cinq trajectoires simulées selon la vitesse de lancement ; ellipse fermée et
rosette), vues en clair et en sombre. Le cours renvoie à l'onglet « Simulateur » existant.

**Méthodes** (10) : conservation et plan ; loi des aires ; énergie et \(E_{p,\text{eff}}\) ; nature du mouvement ; orbite
circulaire ; troisième loi ; orbite elliptique ; transfert de Hohmann ; orbite synchrone et choix d'orbite ; simuler et valider.

**Exercices** (12) : 01 orbite basse (ancien 01) ; 02 Kepler, masse de Mars ; 03 comète (ancien 02, **corrigé**) ; 04 libération et
atmosphères (ancien 03, **corrigé**) ; 05 lire une \(E_{p,\text{eff}}\) (ancien 05, **corrigé**) ; 06 palet et ressort (force centrale
non newtonienne, borne par dichotomie) ; 07 géostationnaire (ancien concours 1, jour sidéral, Paris) ; 08 Hohmann (ancien 04) ;
09 diffusion de Rutherford avec paramètre d'impact ; 10 simulation confrontée à la théorie (code) ; 11 GPS et Galileo ;
**Concours PT « De l'orbite d'attente à l'orbite géostationnaire »** (A orbite d'attente, gain du lancement vers l'est ;
B transfert ; C bilan d'énergie ; D simulation et seconde impulsion).

**Cartes** : 29 → 43 (14 ajoutées à la fin : \(L_z=mC\), vitesse aréolaire, \(\vec L_O=\vec0\), énergie depuis l'équation du
mouvement, \(v^2\) en polaires, critère d'état lié, ressort et Coulomb, démonstration de \(-GMm/(2a)\), vis-viva, cercle
uniforme, paradoxe du freinage, GPS et Galileo, simulation, Rutherford). Aucune carte fausse : `cc-cartes-corr.json` est vide.
Rendu MathJax : 0 erreur.

## Contrôles
`verif_src.py` sans erreur ni attention ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges` vides, aucune erreur JS,
pas de débordement (captures du cours à 390 px regardées : les deux figures larges défilent, libellés lisibles) ;
`corriger_cartes.py --essai` (0) et `ajouter_cartes.py --essai` (29 → 43) sans erreur ; tous les nombres recalculés
(`cc_calculs.py`, `cc_calculs_exos.py`, racines par `numpy.roots` et `brentq`, transfert simulé par `odeint`).

## Notations
\(\vec L_O\), \(L_z=mr^2\dot\theta=mC\), \(C=r^2\dot\theta\) (constante des aires), \(E_{p,\text{eff}}\), \(r_{\min}\), \(r_{\max}\),
\(a\), \(v_c\), \(v_{\text{lib}}\), \(G\) (comme `mecpt`), \(GM_T=3{,}986\times10^{14}\ \text{m}^3\text{·s}^{-2}\), jour sidéral 86 164 s.

## Doutes
- La carte 6 (« Type d'orbite selon E_m », parabole et hyperbole) porte `cat:'form'` alors qu'elle n'est pas une formule ;
  le champ `cat` ne se corrige pas par `corriger_cartes.py`.
- Le « théorème de Bertrand » est seulement cité (hors programme) pour expliquer la rosette du §10.
- `chcentral` garde le titre « Mouvement dans un champ central » ; le programme dit « champ de force centrale conservatif ».
