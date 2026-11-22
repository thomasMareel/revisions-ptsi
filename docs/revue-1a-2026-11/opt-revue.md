# Revue du chapitre `optique` (prefix `opt`) — « Optique géométrique — Lentilles & instruments » — 2026-11-22

Objet (lot 8 du point 4 de l'audit, `docs/audit-2026-11/physique-1a.md` §1 lignes « 1.1 », §3 « Hors-programme
présenté comme exigible », §4 point 8 ; `docs/audit-2026-11.md` §5) : remettre au niveau des chapitres réécrits la
seconde moitié de la partie 1.1 « Formation des images » (lentilles minces, œil, appareil photographique), corriger
l'encadré « Programme PTSI » (lunette et microscope ne sont que des exemples au choix de l'enseignant) et l'erreur
« configuration afocale commune au microscope et à la lunette ». Avant : 2 sections (≈ 18 ko, figures dessinées à la
main), 3 méthodes, 6 exercices, 19 cartes ; onglet Simulateur (`drawOpt`) non modifié, cité dans le cours.

## Fichiers produits (dans `AN1/`)
- `opt-cours.src.html` (105 ko, dont ≈ 62 ko de figures), assemblé par `opt_construire.py` depuis `opt-cours.tpl.html`
  et `opt_figs.json` ; `opt-meth.src.html` (10 méthodes) ; `opt-exos.src.html` (12 exercices dont 1 « Concours PT »,
  assemblé depuis `opt-exos.tpl.html`) ;
- `opt-cartes-corr.json` (2 réponses corrigées), `opt-cartes-ajout.js` (14 cartes) ;
- scripts : `opt_figs.py` (13 figures, avec `og_optique.py`), `opt_calculs.py`, `opt_calculs_meth.py`,
  `opt_calculs_exos.py` ; copies des anciens panneaux `opt_orig_*.html`.

## Contrôles
`verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges` vides, aucune
erreur JS, aucun débordement (huit formules en ligne trop larges au téléphone coupées ou passées en bloc) ; captures à
390 px regardées (figures défilantes comme prévu) ; figures vues une à une en clair et en sombre ;
`corriger_cartes.py --essai` (2) et `ajouter_cartes.py --essai` (19 → 33) sans erreur ; rendu des cartes : 0 erreur MathJax.

## Erreurs trouvées et corrigées
| Où | Erreur | Correction |
|---|---|---|
| Cours §1 (relations de Newton) et carte 15 | grandissement \(\gamma = -\overline{F'A'}/f' = -f'/\overline{FA}\) : la seconde expression a le mauvais signe (f′ = 10 cm, OA = −30 cm donne +0,5 au lieu de −0,5) | \(\gamma = f'/\overline{FA}\) (démonstration par triangles semblables au §4) ; carte 15 corrigée (réponse) |
| Cours §2, méthode 3 (audit, point 8) | « configuration afocale » présentée comme commune à la lunette et au microscope | §6 (définition d'un système afocal), §10 : le microscope n'est pas afocal (intervalle optique Δ), notice dédiée ; figure exacte du microscope ; nouvelle carte « Le microscope est-il afocal ? » ; EXO 11 Q3 |
| Encadré « Programme PTSI » (audit) | « calculer le grossissement pour une lunette ou un microscope » présenté comme exigible | bloc « AU PROGRAMME · PTSI » : exemples laissés au choix de l'enseignant, aucune formule de grossissement exigible ; §10 « des exemples à analyser » ; carte 13 préfixée « Exemple d'application, non exigible en PTSI » et précisée (\(|G| = f'_1/f'_2\), \(G = -f'_1/f'_2\)) |
| Ancien EXO 03, Q1 | calcul intermédiaire faux : \(1/(-8) - 1/(-12) = -1/24\) puis \(\overline{OA'} = -24/5\) (incohérent) | \(1/\overline{OA'} = 1/f' + 1/\overline{OA} = -5/24\) ; Q3 avec une figure calculée à l'échelle |
| Ancien EXO 05 (microscope) | titre « Microscopique — … profondeur de champ » (aucune question sur la profondeur de champ) ; « objet placé juste après \(F_1\) » (entre \(F_1\) et l'objectif, l'image serait virtuelle) ; grandissement et grossissement confondus (« grandissement commercial », \(G = G_1\times G_2 = -400\)) ; « distance optique » ; formule de résolution \(\lambda/(2NA)\) hors programme, en anglais | réécrit en EXO 11 « Microscope : un instrument non afocal » : objet 0,1 mm avant \(F_1\) (Newton), \(\gamma_1 = -40\), \(|G| = 400\) calculé par les angles, comparaison avec la lunette, limite par la diffraction en ordre de grandeur |
| Ancien EXO 02 (loupe), Q3 | « cohérent avec le grandissement obtenu (avec œil au foyer) » : confusion grandissement / grossissement | EXO 09 : calcul de \(\alpha'\) et \(\alpha\), \(G = 5 = G_c\) expliqué (œil en \(F'\)) |
| Ancien « Concours PT » | deux questions d'application directe, loin du format | devenu EXO 05 ; nouveau « Concours PT » en 4 parties (appareil photographique d'un téléphone) |
| Audit (couverture) | profondeur de champ définie mais pas construite ; rôle de la focale et du temps de pose absent | §8 complet (tirage, champ, \(N\), \(t/N^2\), construction de la profondeur de champ avec figure exacte), méthode 8, concours |

## Couverture du programme (1.1, seconde moitié) : avant → après
| Capacité exigible | Avant | Après |
|---|---|---|
| Lentilles minces : centre optique, foyers principaux et secondaires, distance focale, vergence | foyers principaux ; foyers secondaires absents | §1-§2 (formes calculées, centre optique justifié, foyers secondaires, table de vergences, image du Soleil), méthodes 1-2, EXO 02, cartes |
| Construire l'image d'un objet à distance finie ou infinie ; nature réelle ou virtuelle | une figure à la main | §3 (4 figures exactes : image réelle, loupe, divergente, rayon quelconque ; objet à l'infini ; récapitulatif), méthodes 1-2, EXO 03 (figure), cartes |
| Formules de conjugaison et de grandissement de Descartes et de Newton | formules (Newton faux) | §4 (démonstration, courbe de conjugaison, objet virtuel), méthodes 3-4, EXO 01, 05, carte corrigée |
| Établir et utiliser D ≥ 4f′ | énoncé | §5 (démonstration, Bessel, figure D(p)), méthode 5, EXO 04, 07, cartes |
| (Association de lentilles, utile aux instruments) | méthode seulement | §6 (image intermédiaire, objet virtuel, lentilles accolées démontrées, système afocal), méthode 6, EXO 06 (téléobjectif) |
| Œil : modèle, PP, PR, ordres de grandeur de la résolution et de la plage d'accommodation | qualitatif | §7 (modèle, accommodation chiffrée, ΔV ≈ 4 δ, 3×10⁻⁴ rad justifié, défauts et corrections calculées, figure exacte), méthode 7, EXO 08, cartes |
| Appareil photographique : modèle, profondeur de champ construite, influence de la focale, du temps de pose, du diaphragme | modèle et PdC qualitative | §8 (tirage, champ, nombre d'ouverture, exposition, construction de la PdC, exemple calculé N = 2,8 / 11), méthode 8, concours, cartes |
| Expérimental : former une image, choisir les lentilles, estimer une focale, collimateur et lunette autocollimatrice, viseur | absent | §9 (gestes, autocollimation avec figure, Bessel, Silbermann, régression, divergente, viseur à frontale fixe, renvoi à « Mesures et incertitudes »), méthode 9, EXO 07 |
| Lunette, microscope, loupe (exemples au choix) | présentés comme exigibles, microscope dit afocal | §10 (signalés non exigibles, figures exactes de la lunette afocale et du microscope non afocal), méthode 10, EXO 09-11 |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 10 sections + « Pour aller plus loin ») : §1 Lentilles minces ; §2 Foyers,
distance focale, vergence ; §3 Construire l'image ; §4 Relations de conjugaison ; §5 Image réelle d'un objet réel ;
§6 Associer deux lentilles ; §7 L'œil ; §8 L'appareil photographique ; §9 En TP : former une image, mesurer une focale ;
§10 Instruments (exemples) ; PAPL : formule des opticiens, aberrations chromatiques et doublet, ce qu'apporte la 2ᵉ année.
10 exemples traités chiffrés, 10 notices, 12 figures SVG calculées (tracés exacts dans les conditions de Gauss).

**Méthodes** (10) : construire une image ; rayon quelconque ; Descartes ; Newton ; choisir et placer une lentille pour
projeter ; deux lentilles ; œil et corrections ; réglages d'un appareil photographique ; mesurer une focale ; analyser un
instrument (application, non exigible).

**Exercices** (12) : EXO 01 (ancien 1 + vérification par Newton), 02 vergence, foyers secondaires, image de la Lune,
03 (ancien 3, corrigé, figure), 04 projeter une image (D ≥ 4f′), 05 (ancien concours), 06 téléobjectif à deux
lentilles (objet virtuel, focale équivalente 36 cm dans 20 cm), 07 focométrie (autocollimation, Bessel, divergente
accolée), 08 œil (accommodation, myopie, nouveau PP, résolution), 09 loupe (ancien 2, corrigé), 10 lunette (ancien 4,
signe de G), 11 microscope (ancien 5, réécrit) ; « Concours PT » : appareil photographique d'un téléphone (A mise au
point par Newton, B champ, pixels et diffraction, C exposition et flou de bougé, D profondeur de champ et distance
hyperfocale établie, comparaison avec un reflex).

**Cartes** : 19 → 33 (2 réponses corrigées, 14 ajoutées à la fin : foyer secondaire, image d'un objet à l'infini,
rayon quelconque, établir D ≥ 4f′, Bessel, lentilles accolées, microscope non afocal, modèle de l'œil, plage
d'accommodation, correction de la myopie, nombre d'ouverture et exposition, mise au point, profondeur de champ,
influence de la focale).

## Notations
\(O\), \(F\), \(F'\), \(f' = \overline{OF'}\), \(f = \overline{OF} = -f'\), \(V = 1/f'\) (δ), \(\gamma\) (grandissement),
\(G\) (grossissement), \(\varphi'\) (foyer secondaire), \(p\), \(p'\) distances positives pour la projection, \(\Delta\)
intervalle optique, \(N = f'/D\), \(\varepsilon\) tache tolérée, PP / PR, \(d_m = 25\ \text{cm}\). Mêmes conventions que
`optgeo` (axe orienté dans le sens de la lumière, angles à partir de la normale).

## Doutes et remarques pour l'intégration
- L'erreur « microscope afocal » et l'encadré « Programme PTSI » avaient déjà été en partie corrigés dans le dépôt
  (2026-11-15) ; il restait la méthode 3, la carte 13 et l'ancien EXO 05. La carte 12 (définition d'un système afocal)
  est juste et n'a pas été touchée.
- La carte 13 n'était pas fausse en valeur absolue ; elle est retouchée pour dire qu'elle n'est pas exigible et donner le signe.
- Figure de l'œil : myopie forte (PR à 10 cm) pour que la correction soit visible ; dit dans la légende. Figure de la
  profondeur de champ : échelle verticale dilatée (tracé affine, intersections exactes).
- Concours B1 : focale « équivalente 24 × 36 » calculée par le rapport des largeurs (27 mm), pas des diagonales (26 mm).
- Exemple de profondeur de champ (§8) : limites calculées exactement par la tache sur le capteur (2,73–3,33 m à N = 2,8 ;
  2,16–4,91 m à N = 11), sans formule approchée.
- Nom du chapitre : on pourrait le renommer « Lentilles minces, œil et appareil photographique » pour refléter le
  programme (les instruments n'y sont que des exemples) ; non fait, à décider à l'intégration.
