# Programme officiel de sciences industrielles PT (2021, semestres S3 et S4) ↔ chapitres du site

Inventaire établi le 2026-11-13, avant la réécriture des cours de SI de 2ᵉ année.

- **Programme** : annexe 3 de l'arrêté de 2021 (BO n° 31 du 26 août 2021), copie hébergée par l'UPSTI (`upsti.fr/static/public/espace-etudiants/programmes/2021/PT/PT_SciencesIndustrielles.pdf`), convertie en texte (`pdftotext -layout`). Les références « l. N » renvoient aux lignes de ce texte, « p. n »
  aux pages du PDF (n/27). Seules les lignes marquées **S3** ou **S4** sont inventoriées ; les notions
  S1/S2 ne sont citées que lorsqu'elles sont remobilisées ou manifestement absentes.
- **Site** : texte intégral des 11 cours de 2ᵉ année lu ; pour les
  26 chapitres de SI de 1ʳᵉ année et le chapitre d'informatique `pynum`, titres de sections (`sec-num`)
  puis recherches ciblées (`grep`) avant de déclarer une notion absente. « § » = section du panneau
  Cours actuel.
- **Manuel privé de PT** (dépôt privé `cours-pt-spe`, release v1, PDF de 789 pages scannées) : seuls les « résumés de cours » ont servi,
  pour vérifier la couverture et le niveau. Rien n'en est repris.
- Légende : ✅ couvert au niveau attendu · 🔶 couvert mais à approfondir · ❌ absent ·
  ⚠️ hors programme présenté comme exigible.

## Bilan (2026-11-13, après les compléments)

- **Trois chapitres de 2ᵉ année créés** pour les parties du programme qui n'avaient pas de cours :
  `energ2a` « Énergétique des systèmes de solides » (après `dyn2a`), `resnum` « Résolution numérique en
  sciences de l'ingénieur » (groupe Automatique, après `sysnum`), `chfonc` « Chaînes fonctionnelles :
  choisir et dimensionner les composants » (groupe Analyse système, après `multiphy`) ; chacun avec cours,
  méthodes, exercices et cartes.
- **Les 11 cours de 2ᵉ année complétés** : encadré « Au programme » en tête, manques comblés (voir les
  tableaux ci-dessous, colonne « ce qui manque »), hors-programme signalé et regroupé en fin de chapitre
  (« Pour aller plus loin »), sans rien retirer de juste.
- **Restent hors de ce chantier** (notions de 1ʳᵉ année remobilisées en S4, section 15) : systèmes
  séquentiels et diagrammes d'états, réseaux de communication ; compléments ponctuels de `transm`,
  `capteurs`, `usinage`, `trtherm`.
- Les tableaux qui suivent décrivent l'**état de départ** (avant compléments).

## Chapitres concernés

| Chapitre 2A (id, prefix) | Titre actuel | Cours (signes) | Chap. du manuel (p. imprimée) |
|---|---|---|---|
| `chaines` (chs) | Chaînes de solides — mobilité et hyperstatisme | 27 800 | 3 Étude des chaînes de solides (89) |
| `dyn2a` (dy2) | Cinétique et dynamique du solide (3D) | 32 500 | 4 Cinétique (131), 5 PFD (171) |
| — (aucun) | — | — | 6 Application du TEC (213) |
| `correcteurs` (corr) | Correction des SLCI — réglage des correcteurs | 23 500 | 9 Contrôle des SLCI (329) |
| `multiphy` (mph) | Modélisation multiphysique | 24 800 | 10 Modélisation multiphysique (367) |
| `sysnum` (snumx) | Systèmes numériques — acquisition, filtrage et commande | 24 300 | 11 Systèmes numériques (395) |
| — (aucun en SI ; `pynum` en info, 2 600 signes) | — | — | 12 Algorithmes de résolution numérique (427) |
| `ia` (ia) | Intelligence artificielle — apprentissage automatique | 36 300 | 13 Intelligence artificielle (465) |
| `rdm` (rdm) | Résistance des matériaux | 26 300 | 14 Résistance des matériaux (513) |
| `triphase` (tph) | Régimes alternatifs, redresseurs et onduleurs | 33 900 | 15 Régimes électriques et convertisseurs statiques (549) |
| `machalt` (mca) | Machines synchrone et asynchrone | 32 300 | 16 Machines électriques (595) |
| `conception` (cpl) | Conception des liaisons — assemblages et guidages | 34 200 | 17 Conception des liaisons mécaniques (643) |
| `ppm` (ppm) | Triptyque produit–procédé–matériau | 43 600 | 18 Produit-procédé-matériau (703) |

Chapitres de **1ʳᵉ année** qui portent des notions S3/S4 (vérifiés) : `dynsolide` (dyn, 7 400 signes) et
`energsi` (ensi, 5 400) pour la dynamique et l'énergétique (que le programme place en S3) ; `cine` (solide,
repère) ; `mcc` (modèle de la MCC, S4) ; `transm` (tr) ; `sys2` (s2, pôles dominants) ; `stabilite` (stab,
retard) ; `capteurs` (cap, 3 700) ; `usinage`, `moulage`, `deform`, `assemblage`, `addfab`, `trtherm`
(procédés S3, 3 000 à 6 400 signes chacun) ; `ingsys` (afs, SysML) ; `pynum` (info).

Constat général : les 11 cours de 2ᵉ année sont **déjà développés** (23 000 à 44 000 signes, démonstrations,
applications chiffrées, figures) et souvent au-dessus du niveau du manuel. Aucun n'a encore l'encadré
« Au programme » ni de section « Pour aller plus loin » regroupant le hors-programme. Les vrais trous
sont **hors de ces 11 chapitres** : énergétique (TEC, puissances, rendement), résolution numérique,
choix et dimensionnement des composants des chaînes fonctionnelles, et quelques blocs de fabrication.

---------------------------------------------------------------------------------------------------

## 1. Mécanique : solide, cinétique, dynamique

| Point du programme (compétence · connaissances · en clair) | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **B2 Déterminer les caractéristiques d'un solide ou d'un ensemble de solides indéformables** · solide indéformable (définition, repère, équivalence solide/repère), volume et masse, centre d'inertie, matrice d'inertie · *savoir où est la matière et l'écrire dans une matrice 3×3* | l. 570–581, p. 11, S3 | `dyn2a` §1 (masse, G), §2 (opérateur, matrice), §3 (symétries), §4 (Huygens, solides usuels) ; `cine` §1, §3 (définition, repère, 1ʳᵉ année) ; `dynsolide` §1 (J, 1ʳᵉ année) | ✅ | Rappel d'une phrase en tête de `dyn2a` : définition du solide indéformable et équivalence solide/repère (aujourd'hui seulement dans `cine`). Commentaire l. 580–581 : « les calculs intégraux des éléments d'inertie ne donnent pas lieu à évaluation » → le dire dans `dyn2a` (démonstrations du §2, exercice 02 « plaque triangulaire »). |
| **C2 Déterminer les actions mécaniques en dynamique (mouvement imposé) / la loi de mouvement (efforts connus)** · 1ʳᵉ partie : torseurs cinétique et dynamique d'un solide ou d'un ensemble, PFD en référentiel galiléen, énergie cinétique, inertie et masse équivalentes | l. 936–958, p. 17, S3 | `dyn2a` §5 (torseur cinétique), §6 (dynamique, dérivation en base mobile), §7 (Ec par comoment, Jéq, Méq), §8 (galiléen, TRD/TMD, actions réciproques), §9 (rotor, paliers, équilibrage) | ✅ | — (niveau supérieur au résumé du manuel, chap. 4–5). |
| **C1 Proposer une démarche permettant la détermination d'une action mécanique inconnue ou d'une loi de mouvement** · graphe de structure, choix des isolements, choix des équations du PFS ou du PFD, TEC | l. 819–829, p. 15, S3 | `chaines` §1 (graphe), §3 (cadre de l'étude, isolements, décompte E/I) ; `dyn2a` §8 (tableau « je cherche / j'isole / j'écris ») ; TEC : `energsi` §3 (1ʳᵉ année) | 🔶 | Le tableau de stratégie de `dyn2a` §8 ignore le **TEC** (quand le préférer au PFD : système à un paramètre, inter-efforts inutiles ; une seule équation scalaire, non indépendante du PFD). Pas de méthode pour une chaîne fermée ou complexe en dynamique (ordre des isolements guidé par le graphe). |
| **B2 Simplifier un modèle** · linéarisation autour d'un point de fonctionnement (volet mécanique) | l. 544–547, p. 11, S3 | `dyn2a` §8 (position d'équilibre, linéarisation, fonction de transfert) ; `multiphy` §3 | ✅ | — |

## 2. Puissance, énergie, rendement

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **C2 (suite)** · puissance d'une action mécanique extérieure à un solide ou à un ensemble de solides dans son mouvement par rapport au repère galiléen | l. 949–954, p. 17, S3 | `energsi` §1 (P = F·v, P = C·ω, 1ʳᵉ année) ; `multiphy` §5 (effort × flux) | 🔶 | Puissance comme **comoment** du torseur des actions et du torseur cinématique, calcul en un point quelconque (R·V(A) + M(A)·Ω) ; puissance d'un actionneur linéaire / rotatif ; travail entre deux instants. Rien en 2ᵉ année. |
| · puissance intérieure à un ensemble de solides | l. 955–956, S3 | `energsi` §1 (une phrase) ; `chaines` §3 (liaison parfaite : puissance nulle) | ❌ | Puissance des **inter-efforts** entre deux solides = comoment avec le **mouvement relatif** (indépendante du référentiel) ; nulle pour une liaison parfaite ; calcul avec frottement de Coulomb (glissement), frottement visqueux, résistance au roulement. |
| · théorème de l'énergie cinétique | l. 957, S3 | `energsi` §3, `dynsolide` §4 (1ʳᵉ année, forme scalaire plane) ; `multiphy` §6 (exemple convoyeur) | 🔶 | Énoncé pour un solide puis pour un **ensemble de solides** (dEc/dt = P_ext + P_int), forme intégrée ; lien avec le PFD (une équation, pas d'information nouvelle) ; méthode « équation de mouvement par le TEC » sur un mécanisme à plusieurs solides (bielle-manivelle, réducteur + charge). |
| · inertie et masse équivalentes (et effort / couple résistant équivalent) | l. 948, S3 | `dyn2a` §7 (Jéq), `multiphy` §6 (Cr,éq par la puissance), `machalt` §9 | ✅ / 🔶 | Le « modèle équivalent ramené sur l'actionneur » (Méq ou Jéq **et** Fr,éq ou Cr,éq, par égalité des énergies et des puissances) n'est pas présenté comme méthode générale. |
| · rendement en régime permanent | l. 958, S3 | `energsi` §4 (η = Pu/Pf, produit des rendements) ; `transm` §1 ; `machalt` §3 | 🔶 | Bilan de puissances (absorbée, utile, dissipée), rendement sur un cycle ; **rendement dans le TEC selon le sens de transfert de la puissance** (marche motrice / charge entraînante : pertes égales à (1 − η) fois la valeur absolue de la puissance transmise) ; irréversibilité (roue et vis sans fin, vis-écrou). |

**Bilan** : l'énergétique, placée en S3 par le programme, n'existe qu'au niveau d'une introduction de
1ʳᵉ année (`energsi`, 5 400 signes). `dyn2a` §7 renvoie à un « chapitre Énergétique » de 2ᵉ année qui
n'existe pas. Le manuel y consacre un chapitre entier (chap. 6). **Manque le plus important de la
mécanique.**

## 3. Liaisons, chaînes de solides, petits déplacements

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **B2 Modéliser les petits déplacements** · torseur des petits déplacements | l. 631, p. 12, S3 | `rdm` §2 (torseur des petits déplacements et des petites déformations) | ✅ | (Le manuel ne l'emploie aussi qu'en RdM.) |
| Rappels S1/S2 remobilisés : liaisons, fermetures géométrique et cinématique, liaisons équivalentes (série, parallèle), mobilité, hyperstatisme, modélisation plane, rendre isostatique | l. 600–660, S1–S2 | `chaines` §1–§7 | ✅ | — (même périmètre que le chap. 3 du manuel, traité plus en profondeur). |

## 4. Résistance des matériaux

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **B2 Associer un modèle poutre à un solide** · hypothèses de géométrie, fibre neutre, section droite, continuité, élasticité, homogénéité, isotropie, Navier-Bernoulli, Barré de Saint-Venant, HPP | l. 663–676, p. 13, S3 | `rdm` §1 | ✅ | — |
| **C1 Démarche pour les contraintes et déplacements le long d'une poutre** · tronçons, méthode des coupures, théorème de superposition | l. 843–853, p. 16, S3 | `rdm` §3 (coupure, tronçons), §4 (diagrammes), §8 (superposition des flèches) ; `rdm` méthodes | ✅ | Commentaire « méthodes hyperstatiques HP » respecté (aucune). |
| **C2 Déterminer les grandeurs relatives au comportement d'une poutre** · torseur de cohésion, sollicitations (traction, torsion, flexion, cisaillement), contraintes dans une section droite, déplacements de la ligne moyenne, déformations, conditions aux limites | l. 961–969, p. 17, S3 | `rdm` §2–§9 ; cisaillement : `rdm` §3 (tableau), §8 (τ moyen, Jourawski), dimensionnement goupille/clavette dans `conception` §4 | ✅ | Le **cisaillement pur** n'a pas de paragraphe propre dans `rdm` (seulement une ligne de tableau) : ajouter un court paragraphe ou un renvoi explicite à `conception` §4. |
| **B2 Choisir un modèle adapté** · solides indéformable et déformable | l. 472–476, p. 10, S4 | `rdm` §1 (domaine du modèle poutre) ; `chaines` §6 (l'hyperstatisme exige un modèle déformable) ; `multiphy` §7 | 🔶 | Aucun passage ne dit **quand** remplacer un solide indéformable par un modèle déformable dans un mécanisme ou un modèle multiphysique (raideur de torsion d'un arbre long, élasticité d'une courroie ; fréquence propre comparée à la bande passante). |

## 5. Automatique

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **B2 Simplifier un modèle** · pôles dominants et réduction de l'ordre : principe, justification, limites | l. 548–553, p. 11, S3 | `sys2` §5 (1ʳᵉ année, règle τ₁ ≥ 5–10 τ₂), `slci` §4 (pôle le plus proche de l'axe), `correcteurs` §4 (b) (compensation) | 🔶 | Principe seulement, en 1ʳᵉ année. Manquent la **justification** (poids des modes rapides dans la réponse indicielle, rapport des parties réelles, conservation du gain statique) et les **limites** (zéro proche d'un pôle, paire complexe peu amortie, début de la réponse faux, compensation non robuste). |
| **B2 Modéliser un correcteur numérique** · signaux à temps discret (échantillonnage, quantification) ; équations de récurrence d'un correcteur P, PI et à avance de phase | l. 554–567, p. 11, S4 | `sysnum` §1–§4 (signaux, Shannon, quantification, bloqueur), §8 (P, PI forme position et incrémentale, influence de Te) | 🔶 | **Correcteur à avance de phase numérique absent** (aucune récurrence). Commentaire « augmenter Te montre les limites du modèle continu » ✅ (§8) ; « transformée en z HP » respecté ✅. |
| **C1 Proposer une démarche de réglage d'un correcteur** · compensation de pôles, réglage de marges, amortissement, rapidité, bande passante ; P, PI, avance de phase | l. 797–805, p. 15, S3 | `correcteurs` §1–§6, §9 | ✅ | — |
| **C2 Mettre en œuvre une démarche de réglage d'un correcteur** · P, PI, avance de phase | l. 913–917, p. 17, S4 | `correcteurs` §3–§6 + méthodes + 7 exercices | ✅ | — |
| **F2 Modifier la commande** · choix et paramètres d'un correcteur | l. 1311–1316, p. 24, S4 | `correcteurs` §6 (tableau défaut → correcteur), §9 | ✅ | (volet « programme séquentiel » : voir §10). |
| **B3 Préciser les limites de validité d'un modèle** · point de fonctionnement, non-linéarités (courbure, hystérésis, saturation, seuil), retard pur | l. 766–771, p. 14, S4 | `multiphy` §3 (linéarisation, gain dépendant du point), §7 (saturation, frottement sec, jeu, hystérésis, quantification) ; retard : `stabilite` §5 (1ʳᵉ année), `sysnum` §4 | ✅ | Le retard pur pourrait être cité dans la liste du §7 de `multiphy`. |
| **B3 Modifier les paramètres et enrichir le modèle** pour réduire l'écart simulation/mesure | l. 773–777, p. 14, S4 | `multiphy` §7 (« Valider un modèle », recalage, validation sur un autre essai) | ✅ | — |
| Commentaire S2 : Routh, Nyquist, Black-Nichols hors programme | l. 910–911, p. 17 | `stabilite` §2 (Routh en « Pour aller plus loin » : bien signalé) ; **exercice 04 de `stabilite` « Critère de Routh »** posé comme exercice ordinaire ; `bode` §5 et `stabilite` §3 citent Black et Nyquist | ⚠️ (1ʳᵉ année) | Signaler l'exercice 04 comme hors programme ; laisser Black/Nyquist en simple culture. |
| `correcteurs` §8 : anticipation, PID, réglage de Ziegler-Nichols | — | `correcteurs` §8 | ⚠️ | Le programme ne retient que P, PI et avance de phase (l. 801–804, 913–917) : ranger §8 en « Pour aller plus loin » (le PID série = PI + avance de phase peut rester comme association). |

## 6. Systèmes numériques, ingénierie numérique, traitement de données

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **D3 Effectuer des traitements à partir de données** ⇆ I · traitement de fichiers de données, moyenne et écart type, moyenne glissante, filtres numériques passe-bas du 1ᵉʳ et du 2ᵉ ordre | l. 1117–1122, p. 20, S3 | `sysnum` §5 (récurrences, moyenne glissante), §6 (passe-bas du 1ᵉʳ ordre, schémas avant/arrière) ; `ia` §3 (moyenne, écart type pour la standardisation) | 🔶 | **Passe-bas numérique du 2ᵉ ordre** absent ; **lecture et traitement d'un fichier de mesures** (csv, numpy) absent ; moyenne et écart type d'une série de mesures seulement évoqués. |
| **C3 Résoudre numériquement une équation ou un système d'équations** ⇆ I · réécriture des équations (forme exploitable par une bibliothèque, forme matricielle : problème de Cauchy, système linéaire), dichotomie et Newton, A·X = B (bibliothèque), Euler explicite, intégration et dérivation numériques (schémas avant et arrière) | l. 1006–1031, p. 18, S3 | `sysnum` §6–§7 (différences avant/arrière, rectangles, trapèzes, en temps réel) ; `multiphy` §3 (Euler explicite, pas du solveur) ; `ia` §5 (`np.linalg.solve`) ; info `pynum` §1–§4 (dichotomie, Newton, intégration, Euler scalaire ; 2 600 signes) | 🔶 / ❌ | **Pas de chapitre de SI** (le manuel en a un, chap. 12). Manquent : mise sous **forme de Cauchy** (vecteur d'état) d'une équation du mouvement du 2ᵉ ordre et son intégration par Euler explicite ; résolution d'une **loi entrée-sortie géométrique** par Newton ou dichotomie (critère d'arrêt) ; mise sous forme **A·X = B** d'un problème de statique ou de dynamique et résolution par bibliothèque ; aspects théoriques non exigibles (commentaires l. 1020–1027). |
| **C3 Mener une simulation numérique** ⇆ I · choix des grandeurs physiques, du solveur et de ses paramètres (pas, durée), des paramètres de classification ; influence des paramètres du modèle sur les performances | l. 995–1004, p. 18, S4 | `multiphy` §3 (solveur, pas, système raide, boucle algébrique), §7 ; `ia` §3–§4, §7 (choix de k, seuil) | 🔶 | Durée de simulation (quelques temps de réponse), choix des grandeurs observées, **étude d'influence d'un paramètre** (balayage) : non traités explicitement. |
| **C1 Choisir une démarche de résolution d'un problème d'ingénierie numérique ou d'IA** · décomposition d'un problème complexe en sous-problèmes simples ; choix des algorithmes (réseaux de neurones, kNN, régression linéaire multiple) | l. 806–813, p. 15, S3 | `ia` §2 (tableau des familles), §5, §7, §8 ; méthode 1 de `ia` (méthodes) | ✅ (IA) / 🔶 (ingénierie numérique) | La décomposition d'un problème d'ingénierie numérique dépend du chapitre de résolution numérique manquant. |
| (B2 correcteur numérique : voir §5) | | | | |

## 7. Électrotechnique et conversion d'énergie

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **C2 Déterminer les signaux électriques dans les circuits** · régime sinusoïdal, Fresnel, puissance active (continu, monophasé, triphasé), puissances apparente et réactive (mono, tri), ondulation en régime permanent dans les convertisseurs, composants de filtrage | l. 976–991, p. 18, S3 | `triphase` §2 (moyen, efficace, complexe, Fresnel), §3 (P, Q, S, Boucherot, cos φ), §4–§6 (triphasé, couplages, puissances), §7 (PD2, PD3, ondulation, filtrage L, C, LC), §8–§9 (onduleurs, MLI) ; ondulation de courant d'un hacheur : rappel en `triphase` §8, calcul dans les exercices de `hacheurs` | ✅ | Ondulation de **tension** en sortie d'un hacheur filtré par condensateur non traitée ; puissance en continu seulement implicite. |
| **B2 Modéliser un convertisseur électromécanique** · MCC ; MS (f.é.m., réactance synchrone, résistance) ; MAS (inductance magnétisante en parallèle avec la résistance et l'inductance de fuite du rotor) ; bilan des puissances en régime permanent · *commentaires : physique des machines HP, modèles fournis, fréquence fixe ou lentement variable, seule la commande scalaire U/f, fonctionnement qualifié dans les quatre quadrants* | l. 717–741, p. 14, S4 | MCC : `mcc` §3–§5 (1ʳᵉ année, quatre quadrants) ; MAS : `machalt` §2–§5 ; MS : `machalt` §6–§7 ; bilans : `machalt` §3, §7 | ✅ / 🔶 | **Quatre quadrants des machines alternatives** : pas de synthèse dans le plan (C, Ω) (génératrice MAS en §4, MS en §7, freinage en `triphase` §9, mais pas de vue d'ensemble « moteur / frein dans les deux sens, inversion de séquence »). |
| ⚠️ dans le même chapitre | l. 734–741, 756 | `machalt` §1 (théorème de Ferraris démontré, champ tournant), §8 (démonstrations de Clarke, Concordia, Park ; commande vectorielle de la MAS, défluxage) | ⚠️ | Physique des machines hors programme ; modèle (d, q) **fourni** ; pour les machines alternatives, seule la commande scalaire est au programme. |
| **B2 Modéliser la commande d'un ensemble asservi** (modulateur + machine + charge) · commande en couple, en vitesse ; modèle dynamique (d, q) des machines synchrones et asynchrones (fourni) | l. 744–756, p. 14, S4 | `machalt` §8 (modèle (d, q) de la MSAP, boucles de courant et de vitesse) ; `correcteurs` §7 (boucles imbriquées courant / vitesse / position) | ✅ | — |
| Rappel S2 : modéliser les convertisseurs statiques (interrupteurs, cellules, réversibilité, synthèse hacheur / onduleur / redresseur) | l. 692–714 | `cvs`, `hacheurs` (1ʳᵉ année), `triphase` §1, §7–§9 | ✅ | — |

## 8. Modélisation multiphysique, validation, écarts

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **B1 Identifier performances, grandeurs d'entrée et de sortie, paramètres, hypothèses** · grandeurs flux, grandeurs effort | l. 444–462, p. 9, S4 | `multiphy` §2 (paramètres), §5 (couples effort/flux, analogies) | ✅ | — |
| **B2 Compléter un modèle multiphysique ; associer un modèle aux composants des chaînes** · paramètres, grandeurs flux et effort, sources parfaites · *domaines électrique, mécanique, thermique, hydraulique et pneumatique* | l. 480–491, p. 10, S3 | `multiphy` §2–§6 (causal, acausal, ports, sources d'effort / de flux, convertisseurs idéaux, exemple du convoyeur) | ✅ | Domaine **pneumatique** absent (seul l'hydraulique figure dans le tableau des analogies). |
| **B2 Choisir un modèle adapté aux performances** · phénomènes physiques, domaine de validité, solides indéformable et déformable | l. 472–476, p. 10, S4 | `multiphy` §2 (parcimonie), §7 (tableau objectif → modèle) | 🔶 | Volet « solide déformable » (voir §4). |
| **A4 Analyser les performances et les écarts** · ordre de grandeur, homogénéité, matrice de confusion, sensibilité et spécificité d'un test | l. 375–394, p. 8, S4 | `multiphy` §1 (trois écarts), §7 (écart relatif, causes) ; `ia` §4 (matrice de confusion, sensibilité, spécificité) | ✅ | — |

## 9. Intelligence artificielle

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **A3 Analyser les principes d'IA** ⇆ I · régression et classification, apprentissages supervisé et non supervisé, phases d'apprentissage et d'inférence, modèle linéaire mono ou multivariable, réseaux de neurones (couches, neurones, biais, poids, activation) | l. 312–325, p. 7, S3 | `ia` §1, §2, §5, §8 | ✅ | — |
| **A4** matrice de confusion, sensibilité, spécificité | l. 385–388, p. 8, S4 | `ia` §4 | ✅ | — |
| **C1** choix des algorithmes (RN, kNN, RLM) | l. 806–813, p. 15, S3 | `ia` §2, §5, §7, §8 ; méthodes | ✅ | — |
| **C3 Résoudre un problème avec une solution d'IA** ⇆ I · apprentissage supervisé, choix des données d'apprentissage, mise en œuvre (RN, kNN, RLM), apprentissage et inférence · *bibliothèques préimplémentées* | l. 1036–1048, p. 19, S3 | `ia` §3 (prétraitement, séparation, sur-apprentissage), §5, §7, §8–§9 ; méthodes (scikit-learn) | ✅ | — |
| **C3** (S4) choix des paramètres de classification | l. 1001–1002, p. 18, S4 | `ia` §3, §4 (seuil), §7 (k) | ✅ | — |
| ⚠️ dans le même chapitre | l. 1048 | `ia` §6 (descente stochastique, mini-lots, Ridge, LASSO détaillés), §9 (rétropropagation sous forme matricielle), §2 (renforcement, ACP), §8 (théorème d'approximation universelle) | ⚠️ | Au-delà du libellé (le manuel présente Ridge, LASSO, entropie croisée et descente de gradient, mais précise que la rétropropagation « n'est pas explicitement au programme »). Le k-moyennes, lui, est au programme d'informatique commune (S3). À regrouper en « Pour aller plus loin ». |

## 10. Chaînes fonctionnelles : caractériser, choisir, dimensionner des composants

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **A3 Justifier le choix des constituants dédiés aux fonctions** · diagramme de définition de blocs, de blocs internes, chaînes fonctionnelles | l. 255–266, p. 6, S4 | `ingsys` §2–§3 (1ʳᵉ année, 4 400 signes), `multiphy` §1 | ✅ (lecture) | — |
| **A3 Caractériser un constituant de la chaîne de puissance** · alimentation d'énergie ; association préactionneurs-actionneurs (caractéristiques, réversibilité, domaines) ; transmetteurs (caractéristiques, réversibilité, domaines) | l. 275–293, p. 6, S3 | électrique : `triphase` §1, §9, `machalt` §9, `mcc` ; transmetteurs : `transm` (1ʳᵉ année : engrenages, trains, courroies, rendement ; vis sans fin « irréversible » en une ligne) ; vérin : `multiphy` §5 (F = pS, Q = Sv) | 🔶 | **Alimentation** (réseau, batteries : tension, capacité, énergie massique) ❌ ; **préactionneurs et actionneurs pneumatiques / hydrauliques** (distributeurs, vérins simple / double effet, pompes, moteurs hydrauliques) ❌ ; **réversibilité des transmetteurs** (condition d'irréversibilité d'une vis-écrou ou d'une roue et vis sans fin) ❌. |
| **F1 Proposer une architecture fonctionnelle et organique** | l. 1246–1257, p. 23, S4 | `ingsys`, `multiphy` §1 | 🔶 | Activité de projet ; une méthode « allouer des composants aux exigences » (association de blocs, interfaces) manque. |
| **F2 Proposer et hiérarchiser des critères de choix** · autonomie énergétique, coût, durée de vie, encombrement, impact environnemental, précision et rapidité, rendement, réversibilité, résistance et déplacement | l. 1279–1292, p. 23, S4 | tableaux épars : `machalt` §9 (motorisations), `conception` §5 (guidages), `ppm` §6 (procédés) | 🔶 | Pas de démarche générale (critères, niveaux, pondération, matrice de décision). |
| **F2 Choisir les composants de la chaîne d'information** · technologie de capteur, carte de commande | l. 1302–1304, p. 24, S4 | `capteurs` (1ʳᵉ année, 3 700 signes, catalogue), `sysnum` §1, §3 | 🔶 | Critères de choix d'une technologie de capteur (mesurande, étendue, résolution, bande passante, sortie TOR / analogique / numérique, contact, environnement) et d'une carte de commande (entrées-sorties, CAN, cadence, mémoire, communication). |
| **F2 Choisir les composants de la chaîne de puissance** · dispositifs de stockage d'énergie, modulateur, convertisseur, transmetteur | l. 1305–1309, p. 24, S4 | modulateur / convertisseur : `triphase` §9 ; actionneur : `machalt` §9 ; transmetteur : `transm` | 🔶 / ❌ | **Stockage d'énergie** (batterie, supercondensateur, volant d'inertie, accumulateur hydraulique, réservoir d'air) ❌. |
| **F2 Modifier la commande** · modification d'un programme : système séquentiel, structures algorithmiques | l. 1311–1316, p. 24, S4 | — (structures algorithmiques : chapitres d'info) | ❌ | Aucun chapitre sur les **systèmes séquentiels** (diagrammes d'états, S2 l. 345–358 et 682–688 : `ingsys` §2 en cinq lignes). |
| **F3 Dimensionner un composant à partir d'une documentation technique** · *information* : capteurs (étendue de mesure, précision, justesse, fidélité, sensibilité), carte de commande (résolution, mémoire), débit de communication · *puissance* : durée de vie, capacité et consommation électrique, couple thermique équivalent, puissance, rapport de transmission | l. 1320–1342, p. 24, S4 | capteurs : `capteurs` §1 ; résolution : `sysnum` §3 ; durée de vie : `conception` §8 (L10) ; couple thermique : `machalt` §9 (C_eff) ; puissance : `machalt` §9, `ppm` §8 ; rapport : `dyn2a` §7 (inertie ramenée) | 🔶 | Capteurs : **justesse**, linéarité absentes, aucun exemple de dimensionnement ; **mémoire** de la carte ❌ ; **débit de communication** ❌ (pas de chapitre « réseaux », S2 l. 326–344) ; **capacité et consommation électrique** (autonomie d'une batterie) ❌ ; couple thermique équivalent : une formule sans exemple ; **choix du rapport de transmission** (compromis vitesse / couple, adaptation d'inertie) ❌. |

## 11. Conception mécanique

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **F3 Concevoir et dimensionner une liaison mécanique** · assemblage, guidage en rotation, guidage en translation ; puissance, vitesse, effort ; durée de vie ; encombrement | l. 1342–1350, p. 24, S4 | `conception` §1–§9 | ✅ | — (au moins le niveau du chap. 17 du manuel). Ajustements chiffrés (H7/g6, k5…) donnés en exemples : non exigibles (commentaire S2 l. 441–442, seule la nature de l'ajustement). |

## 12. Matériaux, procédés, contrôle, écoconception

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **A5 Analyser un compromis produit-procédés-matériaux** · propriétés physiques (acoustique, électrique, magnétique, mécanique, thermique), classes de matériaux, domaines d'application, diagrammes d'Ashby, impact environnemental · *essais de traction, dureté, résilience, fatigue ; désignations normalisées HP* | l. 397–415, p. 8, S3 | `ppm` §2 (familles, propriétés, ordres de grandeur, ACV en un paragraphe), §3 (Ashby), §4 (indices) ; traction : `rdm` §6 | 🔶 | Essais : **dureté** (échelles seulement nommées), **résilience** ❌, **fatigue** ❌ (seulement celle des roulements) ; propriétés **acoustiques** ❌, électriques et magnétiques à peine. ⚠️ `ppm` §2 donne un tableau « désignation normalisée des alliages usuels » (HP explicite, l. 413) et la ténacité K_Ic avec sa formule. |
| **F3 Concevoir une pièce en optimisant le triptyque produit-procédés-matériaux** · familles et propriétés, méthode de choix (fonction, objectif, contraintes), indicateur de performances, résistance et déplacement, influence du procédé sur la géométrie | l. 1351–1373, p. 24, S4 | `ppm` §1, §3–§6 | ✅ | — |
| **F1 Intégrer les contraintes d'écoconception** · cycle de vie ; nouveau concept, matériaux à moindre impact, réduction de matière, techniques de production, logistique, durée de vie, fin de vie (recyclabilité, valorisation) | l. 1259–1276, p. 23, S4 | `ppm` §2 (énergie grise, CO₂, ACV : un paragraphe), §3 (Ashby module – énergie grise) | 🔶 | Les sept leviers du commentaire ne sont pas traités ; pas d'exemple d'arbitrage d'écoconception. |
| **G2 Choisir et ordonnancer des procédés** · forme, matériau, coûts, taille de série, impact environnemental | l. 1405–1416, p. 25, S3 | `ppm` §6 (critères, compatibilités, IT et Ra, coût et série), §7 (gamme) | ✅ / 🔶 | Impact environnemental des procédés non traité. |
| **G2 Évaluer la capacité d'un procédé à réaliser une pièce métallique** · déformation plastique, moulage, découpage ; procédés additifs ; soudage ; traitements thermiques des aciers volumiques (trempe, revenu, recuit) et surfaciques (trempe, cémentation, nitruration) ; domaines ; règles de conception · *approche qualitative ; métallurgie exclue* | l. 1432–1462, p. 26, S3 | `deform`, `moulage`, `addfab`, `assemblage`, `trtherm`, `trsurf` (1ʳᵉ année, 2 700 à 6 400 signes) ; découpage : `ppm` §6 | 🔶 | Règles de conception présentes pour le moulage (`moulage` §4) et l'injection (`ppm` §5) seulement : absentes pour forgeage / estampage, emboutissage / pliage, soudage, fabrication additive métallique. **Trempe superficielle** absente de `trtherm` (citée dans la gamme de `ppm` §7). ⚠️ `trtherm` §1 et §4 (austénite, martensite, trempabilité) relèvent de la métallurgie exclue (l. 1460–1461). |
| **G2 Évaluer la capacité d'un procédé à réaliser des opérations de finition** · enlèvement de matière (principe de génération et cinématique), choix de cinématique de machine, choix des phases, choix d'une mise en position · *tours 2–3 axes, centres 3–5 axes ; phases détaillées HP ; seul le symbole d'élimination d'un ddl en translation* | l. 1464–1481, p. 26, S3 | `usinage` (1ʳᵉ année) ; `ppm` §7 (gamme, mise en position 3-2-1, axes des MOCN), §8 (puissance de coupe, IT, Ra, capabilité) | 🔶 | **Principe de génération des surfaces** (génératrice / directrice, travail de forme / d'enveloppe, mouvements de coupe et d'avance par procédé) seulement esquissé (`usinage` §1). ⚠️ `ppm` §7 donne une gamme détaillée phase par phase (« la définition détaillée des phases n'est pas au programme », l. 1476) : la présenter comme illustration ; capabilité Cp/Cpk déjà marquée « complément ». |
| **G2 Contrôler la conformité géométrique et dimensionnelle** · dispositifs de contrôle, nuages de points, méthodes d'association · *pas de gamme de mesure ; plan, cercle, droite, cylindre seulement* | l. 1485–1497, p. 27, S3 | `ppm` §9 (moyens, incertitude, calibres, MMT, critères d'association) | ✅ | Préciser les quatre géométries associables et traiter un petit nuage de points (cercle ou plan par moindres carrés). |
| Rappel S2 : pièces plastiques et composites (injection, composites, additifs, règles de conception) | l. 1421–1431 | `ppm` §5, `addfab` | ✅ | — |

## 13. Communication et documents techniques

| Point du programme | Réf. | Chapitre(s) du site | État | Ce qui manque précisément |
|---|---|---|---|---|
| **E1 Lire et décoder un document technique** · SysML ; schémas cinématique, électrique, hydraulique et pneumatique ; représentation 2D normalisée (dessin de définition, plan d'ensemble), 3D · *normes fournies* | l. 1160–1174, p. 21, S4 | SysML : `ingsys` §2 ; cinématique : `cine`, `chaines` ; électrique : `triphase`, `hacheurs` ; cotation : `cotation` | 🔶 | **Schémas hydrauliques et pneumatiques** ❌ (aucun symbole de distributeur, vérin, pompe, limiteur) ; lecture d'un plan d'ensemble : rien (pratique plus que cours). |
| **E2 Produire des documents techniques** (SysML, chaîne fonctionnelle, schéma-blocs, schémas, graphe de structure, croquis, spécifications d'algorithmes) | l. 1205–1226, p. 22, S4 | diffus (chaque chapitre produit ses schémas) | — | Compétence de pratique, pas de cours. |
| **E2 Utiliser un vocabulaire, des symboles et des unités adéquats** · SI, homogénéité | l. 1229–1234, p. 22, S4 | diffus (rubriques « Unités », ordres de grandeur) | ✅ | — |

## 14. Notions S3/S4 qui ne relèvent pas d'un cours (une ligne chacune)

- **D2 Choisir le protocole en fonction de l'objectif visé** (l. 1075–1076, S4) : TP ; au plus une méthode « concevoir un essai d'identification » dans les méthodes de `multiphy`.
- **D2 Justifier le choix d'un capteur ou d'un appareil de mesure** (l. 1100–1102, S3) : en partie cours, rattaché aux manques de `capteurs` (voir §10).
- **D3 Mettre en œuvre un appareil de mesure adapté** (l. 1112–1114, S3) : TP.
- **E2 Produire des documents techniques** (l. 1205–1226, S4) : pratique, évaluée dans les épreuves.
- **F1 Proposer une architecture fonctionnelle et organique** (l. 1246–1257, S4) : « l'activité de projet est une modalité pédagogique à privilégier ».
- **G1 Réaliser tout ou partie d'un prototype, intégrer, implémenter un programme sur une cible, valider** (l. 1378–1399, S4) : projet / TP ; « l'acquisition de savoir-faire professionnels est exclue ».

## 15. Notions S1/S2 absentes repérées au passage (remobilisées en S3/S4)

- **Systèmes séquentiels** : diagramme d'états, état, transition, événement, condition de garde, activité,
  action, chronogrammes (l. 345–358, 682–688, S2) — ❌ (`ingsys` §2 en cinq lignes). Remobilisé par F2 S4.
- **Réseaux de communication** : architecture, débit, support, canal, multiplexage, protocole, trame,
  adressage (l. 326–344, S2) — ❌. Remobilisé par F3 S4 (débit).
- **Transmetteurs vis-écrou et pignon-crémaillère** (l. 924–933, S2) — absents de `transm` (liaison
  hélicoïdale en `cine` §4, pignon-crémaillère seulement dans `multiphy` §5).
- **Capteurs** (l. 285–299, S2) : `capteurs` est court (3 700 signes), sans justesse ni linéarité.
- **Schémas hydrauliques et pneumatiques** (E1, voir §13).

## 16. Hors programme présenté comme exigible (⚠️) — récapitulatif

| Chapitre | Contenu | Ligne du programme |
|---|---|---|
| `machalt` §1 | Champ tournant, théorème de Ferraris démontré | l. 734–735 (physique des machines HP) |
| `machalt` §8 | Démonstrations de Clarke / Concordia / Park ; commande vectorielle de la MAS, défluxage | l. 738–739 (seule la commande scalaire), l. 756 (modèle (d, q) fourni) |
| `correcteurs` §8 | Anticipation, PID, Ziegler-Nichols | l. 801–804, 913–917 (P, PI, avance de phase) |
| `ia` §2, §6, §8, §9 | Renforcement, ACP ; SGD, Ridge, LASSO détaillés ; approximation universelle ; rétropropagation matricielle | l. 1048 (bibliothèques préimplémentées) |
| `ppm` §2 | Désignations normalisées des alliages ; ténacité K_Ic | l. 413 ; l. 410–412 (essais au programme) |
| `ppm` §7 | Gamme détaillée phase par phase (à garder comme illustration) | l. 1476 |
| `ppm` §8 | Capabilité Cp, Cpk (déjà « complément ») | — |
| `conception` §1, §5, §6 | Ajustements normalisés chiffrés (H7/g6, k5, N7…) en exemples | l. 441–442 |
| `dyn2a` §2, exercice 02 | Calculs intégraux d'éléments d'inertie | l. 580–581 (non évalués) |
| `triphase` §1, §7, §6 | Gradateur, redresseurs commandés (déjà « hors du cadre »), méthode des deux wattmètres | l. 706–709 (synthèse limitée à hacheur, onduleur, redresseur) |
| `trtherm` §1, §4 (1ʳᵉ année) | Austénite, martensite, ferrite-perlite, trempabilité | l. 1460–1461 |
| `stabilite` exercice 04 (1ʳᵉ année) | « Critère de Routh » posé comme exercice ordinaire | l. 910–911 |

## 17. Synthèse

**Couvert au niveau attendu** : cinétique et PFD 3D (`dyn2a`), chaînes de solides (`chaines`), RdM
(`rdm`), réglage des correcteurs (`correcteurs`), multiphysique (`multiphy`), IA (`ia`), régimes
alternatifs et convertisseurs (`triphase`), machines alternatives (`machalt`), conception des liaisons
(`conception`), choix matériau-procédé et contrôle (`ppm`, sauf les points listés).

**Manques importants (par ordre de priorité)** :

1. **Énergétique de 2ᵉ année** (C2 S3) : puissance d'une action extérieure (comoment), puissance des
   inter-efforts, TEC pour un ensemble de solides, modèle équivalent, rendement selon le sens de transfert.
   Aucun chapitre de 2ᵉ année. → chapitre nouveau (ou trois sections ajoutées à `dyn2a`).
2. **Résolution numérique en SI** (C3 S3, C1 S3, C3 S4) : Cauchy + Euler, Newton / dichotomie sur une loi
   entrée-sortie, A·X = B, intégration et dérivation de mesures. → chapitre nouveau (chap. 12 du manuel).
3. **Choix et dimensionnement des composants des chaînes fonctionnelles** (A3 S3, F2 S4, F3 S4) :
   alimentation et stockage d'énergie, autonomie, pneumatique / hydraulique, réversibilité des
   transmetteurs, rapport de transmission, capteurs (justesse, linéarité), carte de commande (mémoire),
   débit, critères de choix hiérarchisés. → chapitre nouveau de 2ᵉ année.
4. **`sysnum`** : correcteur à avance de phase numérique, passe-bas du 2ᵉ ordre, traitement d'un fichier
   de mesures (moyenne, écart type).
5. **`ppm`** : essais (dureté, résilience, fatigue), écoconception, génération des surfaces, règles de
   conception des procédés métalliques, trempe superficielle.
6. **Systèmes séquentiels et réseaux** (S2, remobilisés en S4) : deux chapitres de 1ʳᵉ année à créer.
7. Compléments courts : pôles dominants (justification, limites), quatre quadrants des machines
   alternatives, solide déformable / indéformable, cisaillement pur, pneumatique en multiphysique,
   durée de simulation ; encadrés « Au programme » et sections « Pour aller plus loin » partout.
