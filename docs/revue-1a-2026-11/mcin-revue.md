# Revue du chapitre `mcinc` (prefix `mcin`) — « Moment cinétique » — 2026-11-22

Objet (point 4 de l'audit, lot 6 ; `docs/audit-2026-11/physique-1a.md` l. 43, 86, 106, 134-138, 156 ; `audit-2026-11.md` §5) :
`mcinc` recouvrait `mvtsolide` (§2 : rotation, J, tableau de J) et `chcentral` (§3 : Kepler), avec des exercices en doublon
(pendule pesant, satellite) ; Huygens-Steiner présenté dans le cours (hors programme en physique) ; notations \(\vec M_O\) /
\(C\) (couple) divergentes ; aucune figure. Programme : PTSI 2021, partie 2.5 (`pdf-pt/prog/ptsi.txt`, l. 1306-1324).

## Fichiers produits (dans `AN1/`)
- `mcin-cours.src.html` (≈ 90 ko, assemblé par `mcin_construire.py mcin` depuis `mcin-cours.tpl.html` et `mcin_figs.json`) ;
- `mcin-meth.src.html` (9 méthodes), `mcin-exos.src.html` (10 exercices + 1 « Concours PT ») ;
- `mcin-cartes-corr.json` (6 réponses corrigées), `mcin-cartes-ajout.js` (15 cartes) ;
- scripts : `mcin_figs.py` (5 figures), `mcin_svg.py` (outils SVG, copie de `cpt_svg.py`, partagée avec msol et cc),
  `mcin_calculs.py`, `mcin_calculs_exos.py`, `mcin_construire.py` (commun aux trois chapitres), `mcin_voir.py` (aperçu des
  figures clair/sombre), `mcin_cartes_rendu.py` (rendu MathJax des cartes), `mcin_retouches*.py` ; copies des anciens panneaux
  `mcin_orig_{cours,meth,exos}.html`.

## Répartition entre les trois chapitres (doublons supprimés)
| Notion | Avant | Après |
|---|---|---|
| moment cinétique d'un point, axe orienté, système discret, moment d'une force, bras de levier, théorème, conservation | `mcinc` §1 (mince) | `mcinc` §1-§8 |
| solide en rotation, J, tableau de J, couple, pivot, pendule pesant, énergie | `mcinc` §2 **et** `mvtsolide` | `mvtsolide` seulement (un seul tableau de J) ; `mcinc` §3 introduit \(J=\sum m_ir_i^2\) et renvoie |
| force centrale, loi des aires, Kepler, satellites | `mcinc` §3 **et** `chcentral` | `chcentral` seulement ; `mcinc` §7 cite le cas et renvoie |
| Huygens-Steiner | `mcinc` §2 (hors programme dans le corps du cours) | « Pour aller plus loin » de `mvtsolide` |
| gyroscope | `mcinc` §4 | « Pour aller plus loin » de `mcinc` (notation \(\vec\Gamma\)) |

## Erreurs et défauts corrigés
| Où | Problème | Correction |
|---|---|---|
| Ancien EXO 06 (pendule conique) Q3 | énoncé « montrer que \(E_m=-\tfrac12mgl\cos\alpha\) » faux (le corrigé le reconnaissait et donnait \(mgl(1-3\cos^2\alpha)/(2\cos\alpha)\)) | exercice refait (EXO 06) : \(\vec L_O\) calculé, \(L_z\) conservé mais pas \(\vec L_O\), théorème vectoriel vérifié, direction de \(\vec L_O\) (\(L_z/\|\vec L_O\|=\sin\alpha\)) |
| Ancien EXO 03 | disque et Huygens-Steiner (solide, hors programme) | retiré ; repris dans `mvtsolide` EXO 07 avec \(J_A\) fourni |
| Ancien EXO 04 (patineur), EXO 05 (satellite) | doublons de `mvtsolide` et `chcentral` | remplacés (EXO 04 : deux patineurs et une perche, système discret ; le tabouret est dans `mvtsolide`) |
| Cartes 1, 9, 15, 16, 17, 22 | théorème « si O fixe ou O = G » (sans objet pour un point, hors programme) ; Huygens sans le préfixe « Hors programme en PTSI » ; « énergie de liaison » = \(E_m\) ; « force centripète » présentée comme une force à côté de la gravitation (cartes 16 et 22) ; gyroscope noté \(C\) (couple) et non signalé | réponses seules corrigées (`mcin-cartes-corr.json`) |
| Méthodes | « calculer \(J_\Delta\) (± Huygens) », pièges sur Huygens | méthodes réécrites sur le point matériel |
| Notations | \(\vec M_O\), couple \(C\) | \(\vec{\mathcal M}_O(\vec F)\), \(\mathcal M_\Delta\), \(\vec L_O\), \(L_\Delta\), \(L_z=mr^2\dot\theta\) ; couple \(\Gamma\) (comme `emag`, `induction`, `mvtsolide`) |

## Couverture du programme (partie 2.5) : avant → après
| Capacité exigible | Avant | Après |
|---|---|---|
| Relier direction et sens de \(\vec L_O\) au mouvement | définition seule | §1 (règle de la main droite, \(mvd\), figure 3D direct/indirect, balle, palet rectiligne), méthode 1, EXO 01, 06, 07, cartes |
| Moment cinétique par rapport à un axe orienté ; caractère algébrique | une ligne | §2 (indépendance du point, démonstration de \(L_z=mr^2\dot\theta\), signe, rond-point), méthode 2, EXO 02, cartes |
| Système discret de points | absent | §3 (somme algébrique, haltère, contrarotatifs, introduction de \(J\)), méthode 3, EXO 04, carte |
| Moment d'une force ; bras de levier | formule | §4-§5 (droite d'action, glissement, poids du pendule en composantes, \(\pm Fd\), figure de la porte, clé, couple et démonstration), méthodes 4-5, EXO 03, 3 cartes |
| Théorème du moment cinétique en un point fixe | énoncé | §6 (démonstration, vérification sur une chute libre, pendule simple, système : forces intérieures, démonstration), méthodes 6-7, EXO 05, 2 cartes |
| Identifier les cas de conservation | 2 lignes | §7 (quatre cas, palet et trou avec travail de l'opérateur et figure calculée, pendule conique, fil qui s'enroule avec figure), §8 (pulsar), méthodes 8-9, EXO 04, 06-10, concours, 4 cartes |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 8 sections + « Pour aller plus loin ») : §1 moment cinétique d'un point ; §2 axe
orienté ; §3 système discret ; §4 moment d'une force par rapport à un point ; §5 axe, bras de levier, couple ; §6 théorème du
moment cinétique (point, système) ; §7 conservation ; §8 analogies, choix de la méthode, ordres de grandeur ; hors programme :
gyroscope, point mobile, solide quelconque. 12 exemples traités chiffrés, 7 notices, 2 tableaux, 6 démonstrations dépliables,
5 figures SVG calculées (vecteur moment cinétique en 3D ; aires égales du mouvement rectiligne ; bras de levier d'une porte ;
spirale du palet tiré, intégrée par `odeint`, et \(v(r)\) ; fil qui s'enroule sur un poteau, développante), vues en clair et en sombre.

**Méthodes** (9) : moment cinétique d'un point ; scalaire avec signe ; système discret ; moment d'une force ; bras de levier ;
mettre en équation par le théorème ; choisir entre principe fondamental, moment cinétique et énergie ; identifier une
conservation ; exploiter une conservation entre deux états. 4 pièges.

**Exercices** (11) : 01 mouvement circulaire (ancien 01) ; 02 trois mobiles et un axe (signe) ; 03 clé, porte, produit vectoriel ;
04 deux patineurs et une perche (système discret, énergie des forces intérieures) ; 05 pendule simple par le théorème, tension par
le principe fondamental (ancien 02) ; 06 pendule conique (ancien 06, **corrigé**) ; 07 proton dans un champ magnétique (lien avec
`lorentz`) ; 08 lancer du marteau (moment non nul pendant l'accélération : bras de levier du câble) ; 09 fil qui s'enroule sur un
poteau (\(\ell(t)=\sqrt{\ell_0^2-2Rv_0t}\), vérifié par intégration numérique) ; 10 bille dans un bol (conservation de \(L_z\) et de
l'énergie, borne calculée par dichotomie) ; **Concours PT « Le palet, le trou et la masse suspendue »** (A conservation ; B travail
de l'opérateur ; C masse suspendue, énergie potentielle effective, orbite circulaire stable, petites oscillations radiales ;
D grandes oscillations, \(r_{\min}\) par dichotomie et par `odeint`, 0,2023 m).

**Cartes** : 25 → 40 (15 ajoutées à la fin : direction et sens, mouvement rectiligne, indépendance du point de l'axe, signe,
système discret, bras de levier ×2, couple, démonstration du théorème, forces intérieures, conservation de \(L_\Delta\) seul, palet
et trou, fil qui s'enroule, unités, ordres de grandeur) ; 6 réponses corrigées. Rendu MathJax : 0 erreur.

## Contrôles
`verif_src.py` sans erreur ni attention sur les trois panneaux ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges`
vides, aucune erreur JS, pas de débordement (trois formules en ligne coupées après un premier passage à 390 px) ;
`corriger_cartes.py --essai` (6 réponses) et `ajouter_cartes.py --essai` (25 → 40) sans erreur ; tous les nombres recalculés
(`mcin_calculs.py`, `mcin_calculs_exos.py` : sympy pour \(L_z\), l'indépendance du point et les moments ; `odeint` et `brentq`
pour les exercices 09, 10 et le concours).

## Doutes, remarques pour l'intégration
- Le deck garde ses anciennes cartes sur les moments d'inertie, le patineur et Kepler (cartes 4-8, 10-14, 18-19, 21, 23-24) : aucune
  n'est fausse, et les retirer ferait perdre la progression ; elles font doublon avec les decks `msol` et `cc`.
- Le titre « Moment cinétique » convient ; on pourrait préciser « Moment cinétique et moment d'une force ».
- Le théorème pour un système (forces intérieures sans moment) est démontré pour deux points : il sert au tabouret d'inertie
  (`mvtsolide` §10) ; le programme le suppose sans le citer explicitement.
