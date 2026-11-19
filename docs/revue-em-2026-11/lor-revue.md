# Revue du chapitre `lorentz` (« Particules chargées — Lorentz », prefix `lor`) — 2026-11-19

Chapitre de physique de 1ʳᵉ année, partie 2.4 du programme de PTSI (« Mouvement de particules chargées dans
des champs électrique et magnétostatique, uniformes et stationnaires »). Le cours a été réécrit en entier
(à partir du brouillon de la session précédente, relu d'un œil critique, corrigé et complété), les méthodes
et les exercices réécrits, les cartes relues et complétées. Panneaux `lor-simu` (simulateur SVG) et
`lor-flash` non touchés.

## Fichiers produits (dans `EM/`)

| Fichier | Contenu | Taille |
|---|---|---|
| `lor-cours.src.html` | cours complet (bloc « Au programme · PTSI », §1 à §8, « Pour aller plus loin ») | 66 000 car. (ancien : 10 400) |
| `lor-meth.src.html` | 10 méthodes, 6 pièges | 15 500 car. (ancien : 4 350) |
| `lor-exos.src.html` | 11 exercices + 1 exercice « Concours PT » en 4 parties | 55 700 car. (ancien : 13 800) |
| `lor-cartes-corr.json` | 6 réponses corrigées (index 4, 15, 16, 17, 19, 21) | |
| `lor-cartes-ajout.js` | 14 cartes ajoutées en fin de deck (25 → 39) | |
| `lor-cours.tpl.html`, `lor-exos.tpl.html` | gabarits (`@@FIG:nom@@`), assemblés par `construire.py` avec `figs_lor.json` | |
| `figs_lor.py` → `figs_lor.json` | 8 figures calculées (7 dans le cours, 1 dans l'exercice concours) | |
| `lor_verif.py` | vérification numérique (et sympy) de toutes les valeurs du cours, des méthodes, des exercices | |

Copies des brouillons d'origine : `lor-cours.brouillon.tpl.html`, `lor-cours.brouillon.src.html`,
`figs_lor.brouillon.py`, `figs_lor.brouillon.json`. Scripts d'édition : `_edit_lor_cours.py`,
`_edit_lor_exos.py`, `_edit_lor_exos2.py`, `_cartes_lor.py`.

Assemblage : `python3 construire.py lor-cours.tpl.html figs_lor.json lor-cours.src.html` (idem `lor-exos`).

## Contrôles effectués (un par un)

- `verif_src.py` sur les trois panneaux : aucune erreur, aucune « attention » (sept formules en ligne trop
  longues passées en bloc ou raccourcies).
- `maths/apercu_src.py` à 390 et 1440 px pour cours, méthodes, exercices : `merr`, `brut`, `larges` vides,
  aucune erreur JS, `scrollW` égal à la largeur (deux débordements corrigés en route : figure « isochrone »
  de 1 px à 390 px, élargie puis réduite à 360 de large ; une formule en ligne de l'exercice 8 qui n'était
  pas signalée par `larges` parce qu'elle est elle-même un `mjx-container`).
- Captures à 1440 px regardées pour chaque figure nouvelle ou modifiée.
- Cartes : `corriger_cartes.py lor … --essai` (6 réponses corrigées) et `ajouter_cartes.py lor … --essai`
  (25 → 39) sans erreur ; le TeX des 20 textes de cartes a été rendu par MathJax dans une copie du site
  (aucune erreur).
- Toutes les valeurs numériques recalculées dans `lor_verif.py` (constantes CODATA arrondies ; relativité
  vérifiée pour les cas limites).

## Erreurs trouvées et corrigées

### Dans le site actuel
1. **Exercice 4 « Spectrométrie de masse »** (faux) : avec \(U=5\) kV et \(B=0{,}2\) T, \(m/q=r^2B^2/(2U)\)
   vaut \(1{,}88\times10^{-7}\) kg/C pour \(r=21{,}7\) cm, et non \(1{,}98\times10^{-28}\) ; les rayons
   donnés correspondent à 18 u et 19,5 u, pas au carbone ; la conclusion « 11,5 u et 11,8 u, probablement
   ¹²C et ¹³C » est fausse. Exercice refait (EXO 07) : impacts à 35,3 et 36,7 cm, qui donnent bien 12,0 u et
   13,0 u, plus le sens, les ions doublement chargés et la résolution.
2. **Exercice concours** : la figure montrait un proton dans un champ sortant, au point le plus à droite
   du cercle, vitesse vers le haut et force vers le centre ; or \(\vec v\wedge\vec B\) y pointe vers
   l'extérieur (un proton tourne dans le sens horaire quand \(\vec B\) pointe vers le lecteur). Exercice
   remplacé par un vrai problème en quatre parties (implanteur ionique).
3. **Exercice 5** : la question sur l'hélice (vitesse non orthogonale à \(\vec B\)), hors programme en
   PTSI, était présentée comme exigible. Remplacé par un exercice au programme (EXO 09 : filtre de Wien puis
   tri des isotopes du lithium, comparaison avec un spectromètre sans filtre).
4. **Cartes** :
   - n° 4 « trajectoire dans un champ électrique uniforme » : « parabolique » seulement ; c'est une droite
     si \(\vec v_0\) est nulle ou parallèle à \(\vec E\) → réponse complétée (mouvement à vecteur
     accélération constant).
   - n° 15, 16, 17 (hélice) : hors programme en PTSI non signalé → réponses préfixées « Hors programme en
     PTSI : ».
   - n° 19 « Pourquoi peut-on **toujours** négliger le poids » : faux pour un objet chargé macroscopique
     (gouttelette de Millikan) → réponse nuancée (question inchangée).
   - n° 21 « Sens de rotation pour q > 0, B = B u_z (entrant) » : « entrant » contredit la réponse (« horaire
     vue de l'axe +z », où \(\vec B\) pointe vers l'observateur) → réponse qui lève l'ambiguïté (les deux
     points de vue, vecteur rotation \(-q\vec B/m\)).
   - La carte n° 6 (déviation, signalée fausse par l'audit du 14/11) et le §2 du cours étaient déjà
     corrigés sur le site (facteur 2) : vérifié.

### Dans le brouillon de la session précédente
5. **Figures presque invisibles** : plaques, canon, source et électrodes en D tracés avec
   `class="sk-ink fl-soft"` ; la classe `fl-soft` met l'opacité de **tout** l'élément à 0,06, contour
   compris. Remplissage et contour séparés en deux éléments.
6. **Vecteurs des figures** écrits avec la flèche combinante U+20D7, absente des polices du site
   (rendue par un carré dans l'environnement de test) : remplacés par des lettres en gras, comme dans les
   figures de 2ᵉ année (`mgs`, `es2`) ; légendes sans flèche combinante.
7. **Figure de la déviation** : l'angle α chevauchait le libellé δ ; le libellé U était dans la boîte du
   canon. Déplacés.
8. **§2** : « le rapport dépasse 10¹⁰ » contredit par le proton du vent solaire dans le champ terrestre
   (2 × 10⁸) → « couramment 10¹⁰, au moins 10⁸ ».
9. **Aurores polaires** : nuancé (particules piégées par le champ terrestre, guidage par mouvement en
   hélice renvoyé à la fin de chapitre).
10. Toutes les autres valeurs du brouillon ont été recalculées et sont justes (forces, rapports
    Coulomb/gravitation, Millikan, tube cathodique, champ retardateur, rayons et fréquences cyclotron,
    région limitée, isotopes du chlore, cyclotron médical, aurores).

## Couverture du programme (PTSI, partie 2.4)

| Capacité exigible | Avant | Après |
|---|---|---|
| Force de Lorentz ; champs \(\vec E\) et \(\vec B\) | cours §1 (sans exemple) | §1 (produit vectoriel en composantes, exemple, erreur classique) ; méthode 2 ; exos 3, 9 ; cartes |
| Ordres de grandeur des forces électrique ou magnétique, comparaison aux forces gravitationnelles | une phrase | §2 (tableaux de charges, masses, champs ; exemple ; contre-exemple de Millikan) ; méthode 1 ; exo 2, concours A1 ; carte 19 corrigée |
| Puissance : \(\vec E\) modifie \(E_c\), \(\vec B\) courbe sans fournir d'énergie | §1 | §3 (+ énergie potentielle \(qV\), conservation de \(E_m\), exemple) ; méthode 3 ; exos 3, concours D3 ; cartes |
| Champ \(\vec E\) uniforme : mise en équation, mouvement à vecteur accélération constant | §2 (cas orthogonal seulement) | §4 : cas général, cas orthogonal, déviation entre plaques et sur écran, **lancement oblique (miroir électrostatique)** ; méthodes 4, 5 ; exos 4, 5, 11, concours C |
| Bilan énergétique : vitesse acquise sous une différence de potentiel | §1 (une formule) | §5 (théorème de l'énergie cinétique, électronvolt, validité classique, champ retardateur) ; méthode 6 ; exos 1, 2, concours A |
| Champ \(\vec B\) uniforme, \(\vec v_0\perp\vec B\) : rayon et sens de parcours | §3 | §6 (deux démonstrations, isochronisme), §7 (vecteur rotation, centre, sens, région limitée) ; méthodes 7, 8, 9 ; exos 3, 6, 8, 10 ; cartes |
| « Situations physiques variées » (texte du programme) | spectromètre, Wien, cyclotron (cours) | tube cathodique, miroir électrostatique, déviation magnétique, spectromètre, cyclotron, filtre de Wien, aurores, détecteurs (§4, §5, §7, §8) ; implanteur ionique, mesure de e/m (exercices) |
| Hors programme (hélice, champs croisés, relativité, lien Lorentz/Laplace) | mêlé au cours | « Pour aller plus loin · hors programme » en fin de cours ; cartes 15-17 préfixées ; exo 10 Q5 signalée « formule fournie, hors programme » |

## Cours : sections et figures

Bloc « AU PROGRAMME · PTSI » (capacités renvoyant aux §), puis : §1 La force de Lorentz · §2 Ordres de
grandeur · §3 Puissance de la force de Lorentz (énergie potentielle \(qV\)) · §4 Mouvement dans un champ
électrique uniforme (dont le miroir électrostatique, ajouté) · §5 Bilan énergétique · §6 Mouvement dans un
champ magnétique uniforme (démonstrations dépliables ; isochronisme, ajouté) · §7 Sens de parcours, région
de champ limitée · §8 Applications (spectromètre, cyclotron, filtre de Wien, aurores et détecteurs) ·
Pour aller plus loin · hors programme. 11 exemples traités chiffrés, 8 erreurs classiques (deux ajoutées :
§2 et §8).

Figures calculées (7) : déviation entre plaques et écran ; **miroir électrostatique à l'échelle de
l'exemple** (nouvelle) ; **isochronisme : trois vitesses, positions aux mêmes instants alignées avec M₀**
(nouvelle) ; sens de rotation selon le signe de q ; région de champ limitée (déviation / demi-tour) ;
spectromètre ; cyclotron. Dans les exercices : **tri magnétique de l'implanteur, à l'échelle** (nouvelle).

## Méthodes (10, contre 4 + un algorithme + une liste de pièges)

1 Faire le bilan des forces et comparer leurs ordres de grandeur · 2 Calculer une force de Lorentz en
composantes · 3 Savoir quel champ modifie la vitesse (puissance) · 4 Mettre en équation un mouvement dans
un champ électrique uniforme · 5 Calculer une déviation électrique, des plaques à l'écran · 6 Déterminer
une vitesse par un bilan énergétique · 7 Établir le mouvement circulaire dans un champ magnétique uniforme ·
8 Trouver le centre et le sens de parcours · 9 Traiter une région de champ limitée · 10 Étudier un
dispositif à plusieurs étages. Chaque méthode : étapes, exemple éclair chiffré original ; 6 pièges.

## Exercices (12, contre 7)

| N° | Titre | Diff. | Origine |
|---|---|---|---|
| 01 | Accélération d'un proton, puis d'un électron | ★ | ancien 01, complété (eV, \(mc^2\), électron à 0,2 c) |
| 02 | Faut-il tenir compte du poids ? | ★ | nouveau |
| 03 | Mouvement circulaire d'un proton | ★ | ancien 03, complété (mouvement plan, centre, sens, électron) |
| 04 | Déflexion électrique dans un oscilloscope | ★★ | ancien 02, complété (droite de sortie, écran, sensibilité, protons) |
| 05 | Analyseur à miroir électrostatique | ★★ | nouveau (tir oblique, condition énergétique, focalisation à 45°) |
| 06 | Trois particules de même énergie dans un champ magnétique | ★★ | nouveau (sens, \(R\propto\sqrt{m}\), périodes, zone limitée) |
| 07 | Spectrométrie de masse : isotopes du carbone | ★★ | ancien 04, refait (valeurs fausses) |
| 08 | Déviation magnétique d'un faisceau d'électrons | ★★ | nouveau |
| 09 | Filtre de Wien, puis tri des isotopes du lithium | ★★★ | ancien 05, refait sans l'hélice |
| 10 | Cyclotron : énergie, nombre de tours, rayons successifs | ★★★ | ancien 06, complété (durée, \(R_n=R_1\sqrt n\), désaccord relativiste avec formule fournie) |
| 11 | Mesure du rapport e/m de l'électron par des champs croisés | ★★★ | nouveau |
| Concours PT | Un implanteur ionique pour la microélectronique (A accélération, B tri magnétique, C balayage électrostatique, D dose et échauffement) | ★★★ | nouveau (remplace l'ancien, faible et à figure fausse) |

## Cartes

Corrigées (réponse seulement, questions inchangées) : n° 4, 15, 16, 17, 19, 21 (voir plus haut).
Ajoutées (14, formules en `\\( … \\)`, `cat` quand pertinent) : électronvolt (val) ; champ entre deux
plaques \(U/d\) (form) ; \(E_p=qV\) et conservation de \(E_m\) (form) ; composante de la vitesse
conservée dans \(\vec E\) ; angle de sortie et écran (form) ; vecteur rotation \(-q\vec B/m\) (form) ;
centre de la trajectoire ; zone de champ limitée (demi-tour, \(2R\), \(T/2\)) ; fréquences cyclotron
28 GHz/T et 15 MHz/T (val) ; énergie maximale d'un cyclotron (form) ; \(mv=|q|BR\) dans un détecteur ;
validité de la mécanique classique (val) ; vitesse d'un électron sous 1 kV (val) ; un spectromètre
mesure \(m/q\). La carte n° 24 doublonne la n° 0 (même contenu) : laissée, aucune carte n'étant retirée.

## Notations retenues

\(\vec F=q(\vec E+\vec v\wedge\vec B)\) (mot pour mot comme `mxw`) ; base \((\vec e_x,\vec e_y,\vec e_z)\)
comme `mgs` ; \(\mathcal P\) pour la puissance ; \(E_c\), \(E_p=qV\), \(E_m\) ; rayon \(R=mv/(|q|B)\) ;
\(\omega_c=|q|B/m\), \(T\), \(f_c\) ; vecteur rotation \(\vec\omega=-q\vec B/m\) ; \(U_a\) tension
d'accélération, \(\delta\) déviation à la sortie des plaques, \(\alpha\) angle de sortie, \(Y\) déviation
sur l'écran à la distance \(D\) du milieu des plaques ; \(\theta\) déviation magnétique, \(\ell\) largeur de
zone ; \(\mathcal P_{\text{Laplace}}+e\,i=0\) en fin de chapitre, cohérent avec la convention générateur
du chapitre « Induction ». Divergence restante (non corrigée, cartes justes) : les anciennes cartes notent
\(\vec u_z\) et \(r\) pour le rayon.

## Doutes et propositions

- **Titre** : le programme parle de « mouvement de particules chargées dans des champs électrique et
  magnétostatique uniformes et stationnaires ». Proposition, si Thomas le souhaite : « Particules chargées
  dans des champs uniformes : force de Lorentz » (le titre actuel convient aussi). Le tag
  `matiereLabel` « Mécanique » est cohérent avec le programme, qui range la partie 2.4 dans « Mouvements
  et interactions », bien que le chapitre soit dans le groupe Électromagnétisme.
- **Flèche combinante U+20D7** : encore ≈ 140 occurrences ailleurs dans le site (figures et textes
  d'autres chapitres) ; son rendu dépend des polices du système (carré dans le conteneur de test). Point
  à vérifier sur téléphone, hors du périmètre de cette revue.
- La démonstration « par la courbure » du §6 utilise l'accélération normale \(v^2/\rho\) (base de Frenet,
  au programme de cinématique de PTSI) ; une seconde démonstration par les composantes est fournie.
- Exercice 10, Q5 : utilise une formule relativiste **fournie** et signalée hors programme ; à retirer si
  l'on préfère un chapitre strictement limité au programme.
- Le simulateur (onglet `lor-simu`) n'est pas modifié ; le cours renvoie à ses modes « Champ B seul »,
  « Champ E seul », « Champs croisés », « Hélicoïdal » (noms vérifiés).
