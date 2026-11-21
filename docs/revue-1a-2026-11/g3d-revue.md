# Revue : `geo3d` (prefix `g3d`) « Géométrie dans l'espace » — évaluation pour la 1ʳᵉ année — 2026-11-21

## Verdict : le chapitre couvre toute la partie B du programme de PTSI → le déplacer en 1ʳᵉ année

`geo3d` a été écrit en novembre 2026 comme « consolidation des acquis de PTSI » pour la 2ᵉ année. Confronté
ligne à ligne à la partie B « Géométrie de l'espace » du programme de PTSI (`ptsi_maths.txt`, l. 1177-1262), il en
couvre **toutes** les capacités, avec démonstrations, exemples vérifiés et figures. Le programme de PT n'a pas de section
de géométrie de l'espace : le chapitre est donc à sa place en 1ʳᵉ année, et reste visible en 2ᵉ année (la navigation
de 2ᵉ année montre les chapitres de 1ʳᵉ année, le quiz et le Bilan les incluent).

| Programme de PTSI, partie B | `geo3d` |
|---|---|
| a) Coordonnées cartésiennes, cylindriques | §1 ✅ |
| b) Norme dans \(\mathbb R^3\), produit scalaire (définition, bilinéarité, symétrie, base orthonormée) | §2 ✅ |
| c) Produit vectoriel (définition, orientation admise, propriétés, base orthonormée directe, aire, colinéarité) | §3 ✅ |
| d) Produit mixte (définition, trilinéarité, antisymétrie, base orthonormée directe, volume, coplanarité) | §4 ✅ |
| e) Plans (trois modes de définition, paramétrique, cartésienne, régionnement, intersections de plans) | §5 ✅ |
| e) Droites (trois modes de définition, paramétrage, système de deux équations, intersections) | §6 ✅ |
| e) Projeté orthogonal sur une droite ou un plan, distances | §7 ✅ (+ §8 distance de deux droites, application classique) |
| f) Sphères (équation, intersections) | §9 ✅ |

Hors programme de PTSI présent dans le chapitre (gardé, mais désormais signalé) : §10 cylindres et cônes de
révolution, matrices de rotation d'axe un axe du repère (programme de PT) ; double produit vectoriel (§3) ; plan tangent
par le gradient (§9, une phrase) ; méthode 10 ; exercice 07 ; ancien exercice concours (coniques) ; cartes 0, 1, 3, 4,
5, 21, 22, 23 (nappes, surfaces de révolution et réglées, quadriques, cylindres et cônes, rotations).

## Fichiers produits (copies retouchées des panneaux du dépôt ; originaux dans `g3d_{cours,meth,exos}_orig.html`)

| Fichier | Retouches |
|---|---|
| `g3d-cours.src.html` | bloc « AU PROGRAMME · PTSI » ; renvoi aux polaires du chapitre Géométrie du plan (§1) ; inégalité triangulaire (§2) ; **moment d'une force** et formule de transport juste (§3, repris de l'ancien `geometrie`, où elle était fausse) ; double produit « hors programme en PTSI » ; §8 présenté comme application ; « 2ᵉ année » pour le gradient (§9) ; encadré « Hors programme en PTSI (vu en 2ᵉ année) » en tête du §10 |
| `g3d-meth.src.html` | introduction ; méthode 3 : moment et transport ; méthode 9 : plan tangent à \(z=g(x,y)\) rattaché au programme de PTSI (fonctions de deux variables) ; méthode 10 titrée « hors programme en PTSI, vu en 2ᵉ année » |
| `g3d-exos.src.html` (via `g3d_retouches_exos.py` + `g3d_exos_ajout.html`) | EXO 03 : renvoi au programme de PTSI ; EXO 07 titré « hors programme en PTSI » ; **EXO 10 nouveau** (moment, transport ; repris et complété de l'ancien `geometrie`) ; **nouveau Concours PT de niveau PTSI** (pyramide : faces, régionnement, angle, volume par produits mixtes, sphères circonscrite et inscrite, section d'une sphère par une face) ; l'ancien concours (coniques) gardé, titré « (2ᵉ année) » |
| `g3d-cartes-corr.json` | 8 réponses préfixées « Hors programme en PTSI (vu en 2ᵉ année) : » (cartes 0, 1, 3, 4, 5, 21, 22, 23), questions inchangées |
| `g3d-cartes-ajout.js` | 5 cartes (24 → 29) : sphère de diamètre \([AB]\), côté d'un plan, projeté sur un plan, deux sphères, droite et plan |
| `g3d_calculs.py`, `g3d_controle_existant.py` | vérification sympy des ajouts et sondage des exercices existants (justes) |

Le cours et les autres exercices existants ont été relus : aucune erreur trouvée (le script d'origine
`maths/geo2/calc_g3d.py` et mon sondage redonnent tous les résultats).

## Contenu de l'espace de l'ancien `geometrie` : où il se trouve désormais

| Ancien `geometrie` | Dans `geo3d` |
|---|---|
| Produit scalaire dans \(\mathbb R^n\), Cauchy-Schwarz, inégalité triangulaire | §2 (inégalité triangulaire ajoutée) |
| Produit vectoriel, déterminant symbolique, propriétés, figure | §3 |
| Produit mixte, volume | §4 |
| Plans, droites, distances point-plan, point-droite, droites gauches | §5 à §8 |
| Moment d'une force, formule de transport (fausse) | §3 « Application : moment d'une force » (juste), méthode 3, EXO 10 |
| Coordonnées cylindriques, dérivées de \(\vec e_r\), \(\vec e_\theta\) | §1 (cylindriques) ; les dérivées de la base polaire sont dans « Géométrie du plan » §1 |
| Exercices 01, 02, 03, 05, 06, concours | couverts par les exercices 01, 02, 04, 05, 08 et les méthodes 2 à 8 de `geo3d` |
| Exercice 04 (moment) | EXO 10 |
| Cartes sur l'espace (17) | restent dans le deck `geo` (règle des cartes) |

## Intégration (à faire par l'intégrateur)
1. Retirer `'geo3d'` de `window.__YEAR2A` (60 → 59 ids : maths 28 → 27).
2. `CHAP_GROUPS`, groupe Géométrie : `['geometrie','geo3d','coniques','conred','courbes','geoplane','surfaces']`
   (plan puis espace en 1ʳᵉ année, avant les chapitres de 2ᵉ année).
3. `CHAPTERS` : `geometrie` renommé « Géométrie du plan » ; `geo3d` garde son nom « Géométrie dans l'espace »
   (`mobLabel` « Géométrie 3D »). Le bloc de 2ᵉ année « POUR ALLER PLUS LOIN » et les « Ressources vidéo » sont inchangés.
4. Mettre à jour `docs/programme-pt/mathematiques.md` (geo3d n'est plus un chapitre de 2ᵉ année) et l'audit (point 4).
5. Les autres chapitres qui disent « acquis de PTSI (Géométrie dans l'espace) » restent justes.

## Doutes
- Deux exercices « Concours PT » dans le même onglet (le nouveau, de niveau PTSI, puis l'ancien, titré « 2ᵉ année ») :
  la puce du filtre affichera « Concours PT · 2 ». On peut aussi déplacer l'ancien vers `surfaces` ou `coniques` (2ᵉ année).
- §10 (cylindres, cônes, rotations) laissé en place avec un encadré « hors programme en PTSI » plutôt que déplacé en fin
  de chapitre, pour ne pas renuméroter les § cités par les méthodes, les exercices et les cartes.
- La distance de deux droites et la perpendiculaire commune (§8, méthode 8, EXO 08, cartes 18-19) ne sont pas citées
  nommément par le programme ; je les ai gardées comme application des distances (classique aux concours), sans les
  marquer hors programme.
- À 390 px, 9 formules en ligne d'origine (cours : 6, méthodes : 3) défilent dans leur ligne (`.mj-large`) : ce n'est pas
  une erreur (contrôles `merr`, `brut`, `larges` vides), mais on pourrait les scinder ; celles que j'ai ajoutées tiennent.
- Exercices 03 et 08 (Q4) utilisent les dérivées partielles : au programme de PTSI (fonctions de deux variables, fin
  d'année), donc à faire après ce chapitre.
