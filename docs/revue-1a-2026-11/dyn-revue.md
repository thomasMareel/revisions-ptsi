# `dynsolide` (prefix `dyn`) « Dynamique du solide » — chapitre réécrit (SI, 1ʳᵉ année, vu en avance), 2026-11-22

Demande : point 4 de l'audit du 2026-11-14, lot 8 (`docs/audit-2026-11/si-1a.md` : « Anticipations de S3/S4 placées en 1A »,
§3 « Doublons » dynsolide ↔ energsi, §4 « aucune figure », notations J/I, recommandation 8). Programme : `pdf-pt/prog/si.txt`,
B2 « caractéristiques d'un solide » (S3), C2 « actions mécaniques en dynamique, mouvement imposé » et « loi de mouvement »
(S3), C1 « choix des isolements, PFD ou TEC » (S3). Tout le chapitre est donc **vu en avance** (S3) : bloc « AU PROGRAMME ·
PTSI » + encadré « Vu en avance (2ᵉ année) », renvois à `dyn2a` (3D), `energsi` (volet énergétique), `mvtsolide` (physique).

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `dyn-cours.src.html` | cours réécrit (≈ 95 000 car. de HTML, ≈ 46 000 signes de texte ; ancien : 9 300) : bloc programme, 11 sections, « Pour aller plus loin · 2ᵉ année », 16 exemples traités chiffrés, 7 figures calculées |
| `dyn-meth.src.html` | 10 méthodes (étapes, exemple éclair chiffré) + pièges (ancien : 4 méthodes) |
| `dyn-exos.src.html` | 11 exercices + 1 « Concours PT » en 5 parties (9 questions), 1 figure (ancien : 6 + concours de 3 questions) |
| `dyn-cartes-corr.json` | 5 réponses corrigées (question inchangée) |
| `dyn-cartes-ajout.js` | 13 cartes ajoutées en fin de deck (28 → 41) |
| `dyn-cours.tpl.html`, `dyn-exos.tpl.html` + `dyn_figs.py` → `dyn_figs.json`, `dyn_construire.py` | gabarits `@@FIG:nom@@` et figures (classes du site, aucune couleur en dur, vecteurs en gras, dérivées dessinées en points séparés) |
| `dyn_svg.py`, `dyn_voir.py` | primitives SVG (copie de `stat_svg.py` + repères de courbes), aperçu clair/sombre des figures (`dyn_voir/`) |
| `dyn_calculs.py`, `dyn_calculs_meth.py`, `dyn_calculs_exos.py` | vérification (sympy, numpy) de tous les exemples, éclairs et corrigés |
| `dyn_cartes.py`, `dyn_cartes_actuelles.json`, `dyn_cartes_rendu.js` | écriture des corrections, cartes actuelles, rendu `flashPretty` + MathJax des cartes |
| `dyn_orig_{cours,meth,exos}.html` | copie des anciens panneaux |

Reconstruire : `python3 dyn_figs.py && python3 ensi_figs.py && python3 dyn_construire.py` (assemble aussi `ensi`).

## Erreurs et faiblesses corrigées

1. **Anticipation S3 non signalée** (audit §1) : bloc programme et encadré « Vu en avance (2ᵉ année) ».
2. **Doublon avec `energsi`** : l'ancien cours traitait énergie cinétique (§2), TEC, conservation de \(E_m\), puissance par
   dérivation (§4) et des « mouvements classiques » résolus par le TEC (§5). Répartition faite : ici masse, centre d'inertie,
   moments et matrice d'inertie, torseurs cinétique et dynamique, PFD, mouvement imposé, roulement par le PFD, choix des
   isolements ; l'énergétique est dans `energsi`, avec renvois croisés (§9 → energsi §9, §10 → energsi §10, §11 → energsi §5-§6).
3. **Moment d'une force** (ancien §3) : « \(M_\Delta = F_\perp\,d\), \(d\) bras de levier (distance du point d'application à
   l'axe) » mélangeait les deux définitions ; carte 23 du même type. Corrigé (bras de levier = distance de l'axe à la droite
   d'action ; \(M_\Delta = (\overrightarrow{OP}\wedge\vec F)\cdot\vec u\)).
4. Ancien §3 : « \(J_G\,\dot\omega = \sum \overrightarrow{GP_i}\wedge\vec F_i\cdot\vec u_\Delta\) » sans hypothèse (vrai en
   projection, pour \(\vec u_\Delta\) fixe en direction) ; « tensions dans les liaisons » parmi les forces qui ne travaillent
   pas. Remplacés par les énoncés précis des §5 à §8 (\(\vec\delta = \mathrm d\vec\sigma/\mathrm dt\) en \(G\) ou en un point fixe).
5. **Exercices** : EXO 05 (yo-yo) : « \(a_G = g/3 < g\) » avec « < » brut dans la formule, `<ul>` dans un `<p>`, masse de
   l'axe non précisée ; EXO 03 et 06 résolus par le TEC et redondants (deux fois le même plan incliné) : 03 refait par le PFD
   (+ condition d'adhérence), 06 transformé en « rouler ou glisser ? » (glissement effectif à 40°) ; EXO 01 Q3 et EXO 07
   (ancien concours) demandaient une énergie cinétique : remplacées par des questions de couple (Huygens, freinage), l'énergie
   restant citée en renvoi ; EXO 02 : intégrale première tirée du PFD et action du pivot ajoutée. L'ancien « Concours PT »
   (2 questions, ★★) devient EXO 07 ; nouveau sujet concours.
6. **Notations** alignées sur `statique`, `cine`, `dyn2a` : \(\vec V(A, S/\mathcal R)\), \(\vec\Gamma\), \(\{\mathcal C\}\),
   \(\{\mathcal D\}\), \(\vec\sigma\), \(\vec\delta\), \(\vec M(A, 1\to2)\), \(\overline{\overline{I}}(O,S)\) ; \(J_\Delta\) gardé
   (signalé « noté \(I_\Delta\) en 2ᵉ année ») ; \(\mathcal M_\Delta\) de la physique cité au §8 ; \(f_v\) pour le visqueux.

## Couverture du programme (S3) : avant → après

| Capacité | Avant | Après |
|---|---|---|
| Solide indéformable, repère lié, masse, centre d'inertie (B2) | ❌ | §1 (définitions, symétrie, associativité, évidement, 2 exemples, figure du bras) |
| Moment d'inertie, Huygens, solides composés (B2) | §1 (tableau, Huygens) | §2, §3 (tableau étendu, rayon de giration, démonstrations, bras, poulie évidée, 2 figures) |
| Matrice d'inertie (B2) | ❌ | §4 aperçu (opérateur, A…F, \(J_\Delta = u^T[I]u\), symétries, panneau autour de sa diagonale) |
| Torseurs cinétique et dynamique (C2) | ❌ | §5, §6 (cas plans, accélération en rotation, roue de vélo, bras ; figure) |
| PFD en référentiel galiléen, actions réciproques (C2) | §3 (moment en G seulement) | §7 (énoncé torseur, TRD/TMD, démarche, report de charge d'un chariot) |
| Mouvement imposé → actions (C2) | ❌ | §8 (actions dans le pivot), §9 (loi en trapèze, couple par phase, profil en trois tiers ; figure calculée), §10 (adhérence d'un robot) |
| Efforts connus → loi de mouvement (C2) | §5 (pendule, plan incliné par le TEC) | §8 (tambour freiné : sec + visqueux), §10 (rouler ou glisser ; figure) ; pendule renvoyé à `mvtsolide` et au simulateur |
| Choix des isolements, PFD ou TEC (C1) | ❌ | §11 (tableau, chariot tiré par un treuil ; figure), renvoi à `energsi` §10 |
| 3D, équilibrage | ❌ | « Pour aller plus loin » (renvoi `dyn2a` ; balourd du volant percé du §1) |

## Contenu

**Cours.** §1 Masse et centre d'inertie ; §2 Moment d'inertie ; §3 Huygens et solides composés ; §4 Matrice d'inertie
(aperçu) ; §5 Torseur cinétique ; §6 Torseur dynamique ; §7 PFD ; §8 Rotation autour d'un axe fixe ; §9 Loi en trapèze et
couple moteur ; §10 Rouler ou glisser ; §11 Stratégie d'isolement ; Pour aller plus loin. Figures : bras de robot composé,
rayon de giration (disque, jante), Huygens, solide en rotation (accélérations tangentielle et normale), loi en trapèze
(θ, ω, C calculés), cylindre sur plan incliné, chariot tiré par un treuil ; exercice : barrière levante.

**Méthodes (10).** Centre d'inertie composé ; Huygens ; lire une matrice ; torseurs dans un cas plan ; PFD ; couple pour un
mouvement imposé ; actions dans un pivot ; loi de mouvement ; rouler ou glisser ; choisir ses isolements ; pièges.

**Exercices (12).** 01 Huygens et matrice du disque (★) ; 02 pendule pesant, intégrale première, action du pivot (★★) ;
03 disque roulant par le PFD (★★) ; 04 roue freinée (★★) ; 05 yo-yo (★★★) ; 06 rouler ou glisser (★★★) ; 07 volant (★) ;
**nouveaux** : 08 bras SCARA (★★) ; 09 plateau en trapèze, comparaison au profil en trois tiers (★★) ; 10 centrifugeuse
mal chargée (★★) ; 11 chariot sur rampe, deux isolements puis TEC (★★★) ; Concours PT « Barrière levante de péage »
(inertie composée, contrepoids, trapèze, actions du pivot, frein d'urgence).

## Cartes (28 → 41)

Corrigées (réponse seule) : 11 (relation de roulement : norme, signe par \(\vec V(I) = \vec 0\)) ; 13 (TEC d'un solide :
forme dérivée, lien au PFD, renvoi à `energsi`) ; 23 (moment par rapport à un axe, bras de levier exact) ; 26 (\(P = C\omega\)
relié à \(J\dot\omega = C\)) ; 27 (conservation de \(E_m\) : « ni moteur » manquait ; exemple du pendule). Les doublons avec
`energsi` (13, 14, 26, 27) ne peuvent pas être retirés (règle de progression) : leurs réponses sont recentrées sur le lien
avec le PFD et renvoient à `energsi`. Carte 18 (\(\sqrt{3g/2L}\)) vérifiée par `flashPretty` : rendue \(\sqrt{\frac{3g}{2L}}\),
juste, non modifiée. Ajoutées (13) : centre d'inertie, rayon de giration, ordres de grandeur d'inertie, termes de la matrice,
symétries, \(J = u^T[I]u\), torseur cinétique plan, \(\vec\delta = \mathrm d\vec\sigma/\mathrm dt\), accélération en
rotation, PFD, loi en trapèze, balourd, rouler ou glisser. Rendu vérifié (`dyn_cartes_rendu.js`) : aucune erreur MathJax ;
questions nouvelles écrites en `\\( … \\)` pour éviter la ponctuation avalée par `flashPretty`.

## Contrôles

`verif_src.py` sans erreur ni « attention » sur les trois panneaux ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`,
`larges` vides, aucune erreur JS (cours, méthodes, exercices) ; figures regardées en clair et en sombre (`dyn_voir/`) ;
`corriger_cartes.py --essai` (5 corrigées) et `ajouter_cartes.py --essai` (28 → 41) sans erreur.

## Doutes, à décider à l'intégration

- **Ordre du groupe Mécanique** (`CHAP_GROUPS`) : `… dynsolide, dyn2a, energ2a, energsi, rdm` ; en 1ʳᵉ année les chapitres
  2A sont masqués, mais en 2ᵉ année `energsi` apparaît après `energ2a`. Proposer `dynsolide, energsi, dyn2a, energ2a`.
- **Tags** `matiereLabel` : « Mécanique des solides » (dyn) et « Énergétique » (ensi) : inchangés.
- Le **simulateur** (pendule pesant, `drawPend`) reste : le cours y renvoie au §8 ; le pendule est traité en physique.
- J\_Δ (1A, SI) et I\_Δ (dyn2a) : gardé \(J_\Delta\), comme `mvtsolide` et `energ2a` ; signalé dans l'encadré des notations.
