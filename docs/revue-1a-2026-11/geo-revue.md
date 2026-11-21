# Revue : `geometrie` (prefix `geo`) → « Géométrie du plan » — 2026-11-21

Audit `docs/audit-2026-11/maths-1a.md` §2 point 5 et §5 point 4 : la géométrie du plan (partie A du programme
de PTSI, « Géométrie du plan et de l'espace ») était absente de tout le site. Le chapitre `geometrie`
(≈ 4 200 signes, titre « Géométrie de l'espace », plan et espace mélangés, rien sur le plan) est entièrement
réécrit en **« Géométrie du plan »** ; ce qu'il disait de l'espace est repris dans `geo3d` (voir `g3d-revue.md`).

## Fichiers produits

| Fichier | Contenu |
|---|---|
| `geo-cours.src.html` | cours complet (≈ 66 000 car. dont 9 figures) ; produit par `geo_construire.py geo` à partir de `geo-cours.tpl.html` et `geo_figs.json` |
| `geo-meth.src.html` | 10 méthodes |
| `geo-exos.src.html` | 11 exercices + 1 « Concours PT » |
| `geo-cartes-corr.json` | 3 cartes corrigées (réponse seule) |
| `geo-cartes-ajout.js` | 15 cartes ajoutées à la fin (25 → 40) |
| `geo_figs.py` → `geo_figs.json` | les 9 figures SVG calculées (classes du site, vecteurs en gras) |
| `geo_calculs.py`, `geo_calculs2.py` | vérification sympy de tous les exemples du cours, des méthodes et des corrigés |
| `geo_ancien_controle.py` | contrôle des exercices de l'ancien chapitre (erreurs ci-dessous) |
| `geo_voir.py`, `geo_cartes_tex.py`, `geo_cartes_rendu.py`, `geo_deborde.js`, `geo_mjlarge.js` | outils de contrôle (aperçu des figures clair/sombre, TeX et rendu MathJax des cartes, recherche d'un débordement) |

Intégration à faire par l'intégrateur (rien n'est touché dans le dépôt) : dans `CHAPTERS`, `name:'Géométrie du plan'`
(au lieu de « Géométrie de l'espace »), `mobLabel:'Géométrie du plan'` ; id `geometrie` et prefix `geo` inchangés
(progression des cartes conservée). Voir aussi `g3d-revue.md` (ordre dans `CHAP_GROUPS`, `__YEAR2A`).

## Erreurs trouvées dans l'ancien chapitre

1. **Formule de transport des moments fausse** (cours §4 et carte 14) : \(\vec M_{O'}=\vec M_O+\overrightarrow{OO'}\wedge\vec F\)
   au lieu de \(\overrightarrow{O'O}\wedge\vec F\) (sur l'exemple de l'ancien exercice 04 : 40 N·m au lieu de 20 N·m).
   Carte 14 corrigée (réponse) ; la formule juste est dans le cours de `geo3d` (§3, nouvelle application « moment d'une force »).
2. **Ancien exercice 03, Q3** : projeté de \(P(1,1,1)\) sur \(2x-3y+z=6\) donné égal à \(\big(\frac{13}7,-\frac27,\frac47\big)\),
   qui n'est pas sur le plan ; la bonne valeur est \(\big(\frac{13}7,-\frac27,\frac{10}7\big)\) (signe faux sur la 3ᵉ coordonnée).
   L'exercice disparaît avec la réécriture (l'espace est traité par `geo3d`, dont l'exercice 01 couvre ce calcul).
3. **Carte 0** imprécise : « u·v = u₁v₁ + u₂v₂ + u₃v₃ » sans « en base orthonormée » (faux sinon), et seulement en dimension 3.
   Réponse corrigée : base orthonormée, cas du plan et de l'espace.
4. **Carte 19** (double produit vectoriel) : hors programme de PTSI, présentée comme exigible. Réponse préfixée
   « Hors programme en PTSI : » (question inchangée).
5. Titre « Géométrie de l'espace » alors que le chapitre annonçait plan et espace ; méthodes réduites à des listes sans
   exemple ; pas de bloc « Au programme » ; inégalité de Cauchy-Schwarz « dans \(\mathbb R^n\) » (programme de PT).

Les autres exercices de l'ancien chapitre (01, 02, 05, 06, concours) étaient justes (recalculés).

## Couverture du programme (partie A) avant → après

| Capacité du programme de PTSI | Avant | Après |
|---|---|---|
| Coordonnées cartésiennes, coordonnées polaires | ❌ (cylindriques seulement) | §1 (+ base polaire, lien complexes), méthode 1, EXO 01, carte |
| Norme euclidienne, distance | 🔶 (dans \(\mathbb R^n\)) | §2 |
| Produit scalaire : définition géométrique, projection orthogonale | 🔶 | §2 (figure), méthode 2, EXO 02, carte |
| Bilinéarité, symétrie (démonstration non exigible) | 🔶 | §2 |
| Expression en base orthonormée ; identité \(\|\vec u+\vec v\|^2\) ; polarisation ; orthogonalité | 🔶 | §3 (+ Al-Kashi), méthode 2, EXO 02 Q4, EXO 11, cartes |
| Produit mixte dans le plan orienté : définition, aire orientée, bilinéarité, antisymétrie, base orthonormée directe, colinéarité | ❌ | §4 (figure, démonstration), méthode 3, EXO 03, cartes |
| Droites : paramétrage, équation cartésienne (point + directeur, deux points, point + normal), \(A+\operatorname{Vect}(\vec u)\) | ❌ (droites de l'espace) | §5 (figure, démonstration), méthodes 4-5, EXO 04, cartes |
| Lignes de niveau de \(M\mapsto\vec u\cdot\overrightarrow{AM}\) et \(M\mapsto[\vec u,\overrightarrow{AM}]\) ; régionnement | ❌ | §6 (2 figures), méthode 6, EXO 06, EXO 11, concours A, cartes |
| Projeté orthogonal sur une droite, distances | ❌ (espace seulement) | §7 (figure, 2 formules démontrées), méthode 7, EXO 05, cartes |
| Cercles : équation, paramétrage, cercle de diamètre \([AB]\) | ❌ | §8 (figure, démonstration), méthode 8, EXO 07, concours B, cartes |
| Problèmes d'intersection | ❌ | §9 (figure), méthode 9, EXO 07-09, cartes |
| Lien avec les complexes (alignement, orthogonalité) | ❌ | §10, méthode 10, EXO 10, carte |

## Cours (10 sections + bloc programme + « Pour aller plus loin »)

Bloc « AU PROGRAMME · PTSI » (partie A, capacités renvoyées aux §). §1 Repérage (cartésien, orientation admise,
polaires, base \((\vec e_r,\vec e_\theta)\) et ses dérivées) ; §2 Produit scalaire (norme, définition, projection,
propriétés) ; §3 En base orthonormée (démonstration, identités, polarisation, Al-Kashi, orthogonalité) ;
§4 Produit mixte (définition, aire orientée, propriétés, démonstration de l'expression \(xy'-yx'\) et du critère de
colinéarité) ; §5 Droites (paramétrage, théorème de l'équation cartésienne démontré, positions relatives) ;
§6 Lignes de niveau et régionnement (deux propriétés démontrées) ; §7 Projeté et distances (deux formules
démontrées, symétrique, droites parallèles) ; §8 Cercles (équation, paramétrage, cercle de diamètre \([AB]\)
démontré, tangente) ; §9 Intersections (droite-cercle démontré, deux cercles) ; §10 Complexes
(\(\overline z\,z'=\vec u\cdot\vec v+i[\vec u,\vec v]\), alignement, orthogonalité, rotation). « Pour aller plus loin » :
lignes de niveau de \(\overrightarrow{MA}\cdot\overrightarrow{MB}\), cercles d'Apollonius, passage à l'espace.
Chaque section : exemple traité chiffré (10 au total) et erreur classique. **9 figures calculées** (`geo_figs.py`) :
polaires, projection, parallélogramme orienté, droite (directeur, normal), lignes de niveau (deux familles),
régionnement d'un triangle, projeté et symétrique, cercle de diamètre \([AB]\) et tangente, deux cercles et leur
corde commune ; vérifiées en clair et en sombre (aplats `fl-accent-soft`, `fl-green-soft`).

## Méthodes (10)
1 polaires ; 2 produit scalaire et angle (choisir l'expression ; angle orienté par cos et sin) ; 3 produit mixte (aire,
alignement, orientation) ; 4 équation et paramétrage d'une droite ; 5 position de deux droites ; 6 régionnement et
lignes de niveau ; 7 projeté, distance, symétrique ; 8 cercle (reconnaître, paramétrer, tangente, diamètre) ;
9 intersections ; 10 complexes. Chacune avec un exemple éclair vérifié et, au besoin, un piège.

## Exercices (11 + concours, tous nouveaux, inventés, vérifiés par `geo_calculs2.py`)
01 polaires ★ ; 02 produit scalaire dans un triangle (Al-Kashi, projeté, polarisation) ★ ; 03 produit mixte (alignement
paramétré, aires, identité de Lagrange) ★ ; 04 hauteurs, médiatrices, droite d'Euler ★★ ; 05 distances, symétrique,
bissectrices, cercles tangents à deux droites ★★ ; 06 régionnement : production optimale d'un atelier (lignes de
niveau) ★★ ; 07 tangentes issues d'un point (deux méthodes) ★★ ; 08 cercle par trois points, intersections ★★ ;
09 point d'un cercle le plus proche d'une droite ★★ ; 10 complexes (triangle équilatéral, rotation, lieu) ★★ ;
11 lignes de niveau de \(MA^2\pm MB^2\) ★★★ ; **Concours PT** « Découper un disque dans une plaque triangulaire »
(4 parties : régionnement, cercle circonscrit par le diamètre, cercles inscrit et exinscrits par les distances,
relation d'Euler, distance d'un point mobile) ★★★.

## Cartes
- Corrigées (réponse seule, question inchangée) : 0 (base orthonormée), 14 (transport des moments), 19 (hors programme).
- Ajoutées (15, à la fin, formules en `\\( … \\)`, 9 en `cat:'form'`) : polaires, polarisation, projection, produit
  mixte, alignement, vecteurs normal/directeur, droite \((AB)\), distance point-droite (plan), projeté, lignes de
  niveau, côté d'une droite, cercle de diamètre \([AB]\), reconnaître un cercle, droite et cercle, \(\overline z\,z'\).
- Contrôles : `corriger_cartes.py geo … --essai` (3 réponses), `ajouter_cartes.py geo … --essai` (25 → 40), rendu MathJax
  des formules sans erreur (`geo_cartes_rendu.py`).

## Notations
Repère \((O;\vec\imath,\vec\jmath)\) orthonormé direct ; \(\vec e_r,\vec e_\theta\) (comme `geo3d` et la physique ; le
chapitre Courbes planes paramétrées écrit \(\vec u(\theta)\), \(\vec v(\theta)\), signalé dans le cours) ; produit mixte
\([\vec u,\vec v]\) (notation du programme), aussi \(\det(\vec u,\vec v)\) ; \(A+\operatorname{Vect}(\vec u)\) ;
\(\mathcal D\), \(\mathcal C\) ; \(d(M,\mathcal D)\). Dans les SVG, « D », « C » en italique (les lettres calligraphiques
Unicode n'ont pas de police sur le site) et vecteurs en gras.

## Doutes et points pour l'intégrateur
- **Deck `geo`** : 17 des 25 cartes existantes portent sur l'espace (produit vectoriel, plans, distances 3D, moment,
  cylindriques). La règle des cartes interdit de les retirer ou de les déplacer : elles restent dans le deck
  « Géométrie du plan », justes et utiles, mais hors sujet du titre. Si l'on accepte une remise à zéro de leur
  progression, on pourrait les déplacer vers `g3d` ; je ne l'ai pas fait.
- Le titre « Géométrie du plan » suppose que `geo3d` devienne un chapitre de 1ʳᵉ année (recommandé, voir `g3d-revue.md`) ;
  sinon, l'espace de PTSI ne serait plus qu'en 2ᵉ année.
- L'inégalité \(|\vec u\cdot\vec v|\leqslant\|\vec u\|\,\|\vec v\|\) est présentée comme conséquence de la définition
  géométrique (\(|\cos|\leqslant1\)) : l'inégalité de Cauchy-Schwarz générale est au programme de PT ; la carte 1
  (« Inégalité de Cauchy-Schwarz ») reste juste.
- Le §10 (complexes) reprend des capacités de la section « Nombres complexes » (partie h), déjà au chapitre `complexes` §5 ;
  il les relie aux deux produits sans les redévelopper.
- L'ancien exercice concours renvoyait aux « annales officielles de la Banque PT » (lien) : le nouvel exercice concours ne
  porte pas ce lien ; à rajouter si l'on tient à ce renvoi.
