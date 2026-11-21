# Revue du chapitre `cinept` (prefix `cpt`) — « Cinématique du point » — 2026-11-21

Objet (point 4 de l'audit, lot 5 ; `docs/audit-2026-11/physique-1a.md` l. 39, 85, 111, 154-155) : chapitre mince
(3 600 signes de cours, 4 méthodes, 7 exercices, 25 cartes) ; ni coordonnées sphériques, ni déplacement élémentaire, ni
degrés de liberté ; §4 (composition des vitesses) relevant du programme de SI. Programme : PTSI 2021, partie 2.1
(`pdf-pt/prog/ptsi.txt`, l. 916-966) et annexe 3 (dérivée numérique).

## Fichiers produits (dans `AN1/`)
- `cpt-cours.src.html` (92 ko ; 41 800 signes de texte avec les légendes, contre 3 900) — assemblé par `cpt_construire.py`
  depuis `cpt-cours.tpl.html` et `cpt_figs.json` ;
- `cpt-meth.src.html` (9 méthodes), `cpt-exos.src.html` (11 exercices + 1 « Concours PT ») ;
- `cpt-cartes-corr.json` (6 réponses retouchées), `cpt-cartes-ajout.js` (14 cartes) ;
- scripts : `cpt_svg.py` (outils SVG communs avec `mp`, projection 3D orthographique `Vue3D`), `cpt_figs.py` (7 figures),
  `cpt_calculs.py` (exemples du cours), `cpt_calculs_meth.py`, `cpt_calculs_exos.py` (sympy pour la cycloïde et la
  parabole), `cpt_concours.py` (concours, code de la partie D exécuté), `cpt_video.py` (code du §9 exécuté),
  `mp_tester_code.py` (extrait et exécute **tout** le code affiché dans les panneaux cpt et mp), `cpt_voir.py` (aperçu des
  figures en clair et en sombre), `cpt_cartes_rendu.py` (rendu MathJax des cartes), `cpt_secs.py` ; copies des anciens
  panneaux `cpt_orig_{cours,meth,exos}.html`.

## Erreurs trouvées et corrigées
| Où | Problème | Correction |
|---|---|---|
| Ancien EXO 06 (bille quittant un plan), Q3 | racine du trinôme prise avec le mauvais signe : \(t=(3{,}13+10{,}39)/9{,}81\approx1{,}38\) s et portée 7,48 m | \(t=(-3{,}13+\sqrt{107{,}9})/9{,}81\approx0{,}740\) s, distance 4,0 m (EXO 05, avec une note sur l'erreur de signe) ; la vitesse au bord est obtenue cinématiquement (accélération \(g\sin\alpha\) admise) et non plus par l'énergie |
| Ancien EXO 05 (parabole) | \(R_0\) absent de l'énoncé, fixé seulement dans la correction (« si \(R_0=3\) m ») | \(R_0=3{,}0\) m dans l'énoncé (EXO 10), question ajoutée sur le rayon de courbure au sommet d'un tir |
| Ancien §4 | composition des vitesses présentée en section numérotée | déplacée en « Pour aller plus loin », signalée « vue en SI », renvoi à `cine` §5 et à `mecpt` §2 (mouvement relatif de deux référentiels galiléens) |
| Cartes 6, 13, 19 | portée, angles complémentaires, chute libre : hypothèses manquantes (arrivée à l'altitude du départ, sans frottement, sans vitesse initiale) ; carte 6 notait \(R\) la portée | réponses complétées ; portée notée \(D\) comme dans le cours |
| Cartes 3, 8, 14 | Frenet noté \((\vec t,\vec n)\) et rayon de courbure \(R\), alors que le cours, `mecpt` et SI `cine` écrivent \((\vec T,\vec N)\) et que le cours note \(\rho\) | réponses harmonisées (questions inchangées : progression conservée) |

Aucune autre carte fausse. La carte 11 (« terme de Coriolis » pour \(2\dot r\dot\theta\)) est gardée : l'appellation est
usuelle (c'est l'accélération de Coriolis du repère tournant avec \(\vec e_r\)).

## Couverture du programme : avant → après
| Capacité exigible (2.1) | Avant | Après |
|---|---|---|
| Référentiel, relativité du mouvement, distances et durées absolues ; situation où la description classique est en défaut | absent | §1 (définition, TGV, muons cosmiques chiffrés, GPS), méthode 1, cartes |
| Déplacement élémentaire à partir d'un schéma, trièdre local, vitesse déduite géométriquement (cartésiennes, cylindriques) | absent | §2, §3 (figures cylindrique et polaire avec élément \(\mathrm{d}r\), \(r\,\mathrm{d}\theta\)), méthode 2, cartes |
| Composantes de position, déplacement, vitesse, accélération en cartésiennes et cylindriques | polaires seulement, sans \(z\), sans démonstration | §2, §3 (dérivée de la base démontrée, rampe hélicoïdale), méthode 3, EXO 06, 07 |
| Coordonnées sphériques (déplacement élémentaire, trièdre) | absent | §4 (figure, Terre : parallèle et méridien, vitesse de Paris), EXO 08, 2 cartes |
| Degrés de liberté ; choix des coordonnées | absent | §5 (tableau, perle sur cerceau tournant), méthode 1, EXO 07, 11, concours A1, carte |
| Mouvement à accélération constante, trajectoire cartésienne | formules | §6 (intégration vectorielle, relation sans le temps, freinage, lancer de poids avec hauteur, figure des 5 angles), méthodes 4-5, EXO 01, 02, 04, 05, concours B |
| Mouvement circulaire uniforme et non uniforme en polaires | formules | §7 (ordres de grandeur, centrifugeuse, figure), méthode 6, EXO 03, 09, concours A |
| Direction qualitative de \(\vec v\), \(\vec a\) ; Frenet : courbure, norme et variation de la vitesse | formule de Frenet | §8 (justification de \(v^2/\rho\), règle de la concavité, \(\rho=v^3/\|\vec v\wedge\vec a\|\), figure), méthodes 7-8, EXO 10, 11, concours C |
| Enregistrement vidéo ; dérivée numérique (annexe 3) | absent | §9 (différences centrées, code numpy testé, bruit de pointage, régression `polyfit`, chronophotographie calculée), méthode 9, concours D (code), carte |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 9 sections + « Pour aller plus loin ») : §1 Espace, temps et référentiel ;
§2 Vecteurs position, vitesse, accélération (cartésiennes) ; §3 Cylindriques et polaires ; §4 Sphériques ; §5 Degrés de
liberté et choix des coordonnées ; §6 Accélération constante ; §7 Mouvement circulaire ; §8 Repère de Frenet ; §9 Mesurer
vitesse et accélération (vidéo, dérivation numérique) ; hors programme : composition des vitesses (SI), accélération en
sphériques. 11 exemples traités chiffrés (au moins un par section), 9 notices « Erreur classique », 3 tableaux d'ordres de
grandeur, 2 démonstrations dépliables, 7 figures SVG calculées (base polaire et élément de déplacement ; cylindriques et
sphériques en perspective calculée ; cinq paraboles ; circulaire accéléré ; Frenet avec cercle osculateur ; chronophotographie
avec vitesses et accélérations estimées par le programme du cours), vérifiées en clair et en sombre.

**Méthodes** (9) : poser le cadre ; déplacement élémentaire ; cylindriques ; accélération constante ; tir ; circulaire ;
Frenet ; lecture qualitative ; vidéo. Les 3 anciennes méthodes et les pièges sont repris (3, 5, 7 et notices).

**Exercices** (12) : 01 chute libre et lancer horizontal (ancien 01) ; 02 distance d'arrêt (nouveau) ; 03 virage (ancien 02) ;
04 portée et angle (ancien 04, Q4 ajoutée) ; 05 bille quittant un plan (ancien 06, **corrigé**) ; 06 spirale (ancien 03,
Q3 spirale d'Archimède) ; 07 grue à tour en cylindriques (nouveau) ; 08 sphériques sur la Terre (nouveau) ; 09 rotation
uniformément accélérée (ancien « Concours », trop court pour en rester un) ; 10 rayon de courbure (ancien 05, complété) ;
11 valve de vélo : cercle et cycloïde, \(\rho=4R\) au sommet (nouveau) ; **Concours PT « Le lancer du marteau »** (A dernier
tour circulaire accéléré, B vol parabolique avec hauteur de lâcher, C courbure, D vidéo à 100 images/s : différence seconde
inexploitable, ajustement `polyfit` ; tous les nombres et le code vérifiés dans `cpt_concours.py`).

**Cartes** : 25 → 39 (14 ajoutées à la fin : référentiel et repère, limite classique, position et déplacement en
cylindriques, sphériques, déplacement en sphériques, degrés de liberté, accélération constante, trajectoire du projectile,
côté de l'accélération, rayon de courbure, différences centrées, ordres de grandeur, tr/min → rad/s). Rendu MathJax : 0 erreur.

## Contrôles
`verif_src.py` sans erreur ni attention sur les trois panneaux ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`,
`larges` vides, aucune erreur JS ; `corriger_cartes.py --essai` (6 réponses) et `ajouter_cartes.py --essai` (25 → 39) sans
erreur ; code Python des panneaux exécuté par `mp_tester_code.py`.

## Notations
Bases \((\vec e_x,\vec e_y,\vec e_z)\), \((\vec e_r,\vec e_\theta,\vec e_z)\), \((\vec e_r,\vec e_\theta,\vec e_\varphi)\) comme
`es2`, `mgs` ; \(\theta\) colatitude, \(\varphi\) azimut ; Frenet \((\vec T,\vec N)\), rayon de courbure \(\rho\) (comme SI
`cine` pour \(\vec T,\vec N\)) ; portée \(D\), flèche \(H\) ; \(\omega=\dot\theta\) ; \(\Delta t\) pas d'échantillonnage.

## Doutes, remarques pour l'intégration
- Les noms de formules longs (`data-nom` « Déplacement élémentaire en cylindriques ») se coupent en milieu de mot dans la
  marge à 1 440 px (comme d'autres chapitres) ; sans conséquence sur le Formulaire.
- SI `cine` §2 refait position, vitesse, accélération, Frenet et MRUA : il pourrait renvoyer à ce chapitre (et noter
  \(\rho\) le rayon de courbure).
- La figure sphérique montre \(\vec e_\varphi\) un peu raccourci par la perspective (choix de vue fait par calcul pour
  séparer les trois vecteurs).
