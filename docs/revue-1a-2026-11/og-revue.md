# Revue du chapitre `optgeo` (prefix `og`) — « Optique géométrique — Les bases » — 2026-11-22

Objet (lot 8 du point 4 de l'audit, `docs/audit-2026-11/physique-1a.md` §1 lignes « 1.1 », §3 « Doublons ») : remettre
au niveau des chapitres réécrits la première moitié de la partie 1.1 « Formation des images » du programme de PTSI,
sans recouvrement avec `optique` (lentilles et instruments). Avant : 4 sections (≈ 13 ko, dont 2 figures dessinées à la
main), 2 méthodes, 5 exercices (dont 2 « Concours PT », l'un sur le prisme, hors programme), 13 cartes.

## Fichiers produits (dans `AN1/`)
- `og-cours.src.html` (88 ko, dont ≈ 52 ko de figures), assemblé par `og_construire.py` depuis `og-cours.tpl.html` et
  `og_figs.json` ; `og-meth.src.html` (10 méthodes) ; `og-exos.src.html` (12 exercices dont 1 « Concours PT », assemblé
  depuis `og-exos.tpl.html`) ;
- `og-cartes-corr.json` (3 réponses corrigées), `og-cartes-ajout.js` (13 cartes) ;
- scripts : `og_optique.py` (outils de tracé communs à `og` et `opt` : repère, rayons fléchés, lentilles minces,
  Snell-Descartes vectoriel), `og_figs.py` (9 figures), `og_aberration.py` (tracé exact d'une lentille plan-convexe),
  `og_calculs.py`, `og_calculs_meth.py`, `og_calculs_exos.py` (toutes les valeurs du cours, des méthodes et des
  exercices), `og_voir.py` (aperçu des figures en clair et en sombre), `og_cartes_rendu.js` (cartes passées dans
  `flashPretty` et MathJax) ; copies des anciens panneaux `og_orig_*.html`.

## Contrôles
`verif_src.py` sans erreur ni « attention » sur les trois panneaux ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`,
`larges` vides, aucune erreur JS, aucun débordement (deux formules en ligne trop larges au téléphone passées en bloc) ;
figures regardées une à une en clair et en sombre ; `corriger_cartes.py --essai` (3 corrections) et
`ajouter_cartes.py --essai` (13 → 26 cartes) sans erreur ; rendu des cartes nouvelles ou corrigées : 0 erreur MathJax.

## Erreurs trouvées et corrigées
| Où | Erreur | Correction |
|---|---|---|
| Cours §1, carte 1 | domaine visible « de 400 à 800 nm » (audit) | 400 à 750 nm environ, comme `optiqued` ; carte 1 corrigée (réponse) |
| Carte 6 | réflexion totale « d'un milieu plus dense à un moins dense » : c'est l'indice qui compte, pas la densité | « vers un milieu moins réfringent » (réponse) ; notice dans le cours §4 |
| Carte 10 | angle de réfraction limite noté \(i_\lambda\) (λ est la longueur d'onde) | \(i_\ell\), le même angle que celui de la réflexion totale par retour inverse (réponse) |
| Exercices | deux « Concours PT », dont un sur le prisme, hors programme de PTSI | un seul « Concours PT » (fibre, étendu à 4 parties) ; le prisme devient l'EXO 11, signalé « hors programme, pour aller plus loin » |
| Ancien concours prisme, A2 | argument de retour inverse présenté comme une preuve du minimum | « en admettant que ce minimum est unique » |
| Ancien concours fibre | figure dessinée à la main, angles non respectés | remplacée par une figure calculée (injection par une lentille, partie D nouvelle) ; la figure calculée de la fibre est dans le cours |
| Cours (ancien §2-§4) | cône d'acceptance et dispersion intermodale donnés sans démonstration, alors que le programme demande de les établir | démonstrations pas à pas au §8 (cours), méthodes 9-10, concours B et C |
| Doublon avec `optique` (audit) | stigmatisme et conditions de Gauss exposés dans les deux chapitres | ici seulement (§5, §7) ; `optique` §1 y renvoie |

## Couverture du programme (1.1, première moitié) : avant → après
| Capacité exigible | Avant | Après |
|---|---|---|
| Caractériser une source par son spectre ; longueur d'onde dans le vide et couleur ; source ponctuelle monochromatique | λ et « monochromatique » en une ligne, aucun spectre | §1 (spectres continus, de raies, laser, LED ; figure calculée ; couleurs ; spectromètre à fibre ; sécurité laser), méthode 1, EXO 02, cartes |
| Définir le modèle de l'optique géométrique ; indice | principes cités | §2 (milieu THI, indice et table, quatre principes, dispersion chiffrée), cartes |
| Indiquer les limites du modèle | une phrase | §2 (diffraction θ ≈ λ₀/a, trois cas chiffrés, pupille), méthode 2, EXO 10, carte |
| Lois de Snell-Descartes | énoncé + figure à la main | §3 (figure exacte, courbe i₂(i₁), vitre et décalage latéral), méthodes 3 et 5, EXO 01, 05 |
| Établir la condition de réflexion totale | formule seule | §4 (démonstration, table d'angles limites, piscine, prisme à réflexion totale), méthode 4, EXO 03, 06, 08, cartes |
| Stigmatisme | définition | §5 (objet/image réels ou virtuels, stigmatisme rigoureux ou approché, aplanétisme, dioptre plan non stigmatique : figure exacte, profondeur apparente démontrée), méthode 7, EXO 07, cartes |
| Construire l'image par un miroir plan | règle + figure à la main | §6 (démonstration, construction pour l'œil, champ, rotation 2α), méthode 6, EXO 04, 09, carte |
| Conditions de Gauss et conséquences ; stigmatisme approché et détecteur | absents (dans `optique` seulement) | §7 (définition, conséquences, table sin θ ≈ θ, aberration sphérique tracée exactement, tache comparée au pixel, limite par la diffraction), méthode 8, EXO 10, cartes |
| Fibre à saut d'indice : cône d'acceptance et dispersion intermodale (établir) | résultats admis | §8 (deux démonstrations, ordres de grandeur, débit, monomode), méthodes 9-10, EXO 03, concours, cartes |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 8 sections + « Pour aller plus loin ») : §1 Sources lumineuses et spectres ;
§2 Le modèle de l'optique géométrique ; §3 Lois de Snell-Descartes ; §4 Réflexion totale ; §5 Objets, images et
stigmatisme ; §6 Miroir plan ; §7 Conditions de l'approximation de Gauss ; §8 Fibre optique à saut d'indice ;
PAPL : prisme (déviation minimale), milieux d'indice variable (mirage, fibre à gradient), principe de Fermat.
8 exemples traités chiffrés (un par section), 9 notices (erreurs classiques, sécurité laser), 8 figures SVG calculées :
spectres (lois de Planck normées, raies Hg, Na, H, laser), réflexion-réfraction à l'échelle, i₂(i₁) dans les deux sens,
source au fond d'un bassin (disque de sortie), non-stigmatisme du dioptre plan, miroir plan, aberration sphérique d'une
lentille plan-convexe (tracé exact), fibre (rayon guidé et rayon perdu).

**Méthodes** (10) : λ₀, fréquence, couleur, indice ; validité de l'optique géométrique ; angle de réfraction ; réflexion
totale ; dioptres plans successifs (invariant n sin i) ; image par un miroir plan ; profondeur apparente ; netteté
(Gauss et détecteur) ; cône d'acceptance ; dispersion intermodale et débit. Exemples éclair chiffrés et vérifiés.

**Exercices** (12) : EXO 01 (ancien 1), 02 deux couleurs dans un verre (nouveau), 03 (ancien 2, complété), 04 (ancien 3,
Q3 ajoutée : bords du miroir à 0,80 m et 1,65 m), 05 lame à faces parallèles (exact et Gauss), 06 rendre une lampe
invisible, 07 pêche au harpon et stigmatisme, 08 prisme à réflexion totale (dans l'air et dans l'eau), 09 rotation d'un
miroir et dièdre droit, 10 diffraction et pixels (téléphone limité par la diffraction), 11 prisme (ancien concours,
hors programme) ; « Concours PT » fibre : A réflexion totale, B cône d'acceptance (anciens), C dispersion intermodale et
débit, D injection par une lentille (focale minimale 4,0 mm ; 57 % de la puissance guidée avec 3 mm).

**Cartes** : 13 → 26 (3 réponses corrigées, 13 ajoutées à la fin : spectres, fréquence et longueur d'onde dans un
milieu, principes du modèle, limites (diffraction), établir la réflexion totale, angles limites usuels, stigmatisme,
aplanétisme, profondeur apparente, conséquences des conditions de Gauss, stigmatisme et détecteur, rotation d'un
miroir, débit d'une fibre). Les cartes nouvelles et corrigées sont écrites en `\( … \)`.

## Notations
\(\lambda_0\) (longueur d'onde dans le vide, comme `optiqued` et la 2ᵉ année), \(n\), \(i_1, i_1', i_2\) (angles à partir
de la normale), \(i_\ell\) angle limite (un seul nom pour la réflexion totale et la réfraction limite), \(\theta_a\) et
ON pour la fibre, \(\delta t\) dispersion intermodale (comme la carte d'origine), \(\overline{HA'}\) pour le dioptre plan.

## Doutes et remarques pour l'intégration
- La carte 6 n'était pas fausse au sens strict (« dense » pour « réfringent » est un abus répandu) : corrigée par cohérence avec la notice du §4.
- Les cartes d'origine restent en Unicode (rendu par `flashPretty`) ; les cartes nouvelles ou corrigées sont en `\( … \)` pour un rendu propre.
- Figure de la fibre : indices exagérés (1,50 / 1,40) pour que les angles soient visibles ; c'est dit dans la légende.
- §7 : la tache de diffraction est donnée en ordre de grandeur (\(2\lambda_0 f'/D\), sans le facteur 1,22 d'Airy, hors programme).
- Le prisme n'est pas au programme de PTSI ; on le garde en fin de cours et en exercice signalé, car il sert en TP (goniomètre).
- Les outils de tracé `og_optique.py` servent aussi aux figures de `opt` (préfixe `og_` gardé).
