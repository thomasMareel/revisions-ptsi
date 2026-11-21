# Revue du chapitre `optiqued` (prefix `od`) — « Optique ondulatoire » — 2026-11-21

Objet (audit 2026-11-14, `docs/audit-2026-11/physique-1a.md` §2 point 5, §3 (`optiqued`), §5 points 1 et 5) : les
interférences lumineuses à deux ondes, les trous d'Young, la différence de chemin optique et la formule de Fresnel sont au
programme de PTSI (partie 1.6), alors que le chapitre les traitait en deux sections minces sous un encadré `.hors-prog`
(déjà partiellement corrigé : « Programme PTSI : §1 et §2 seulement »), le reste du chapitre (diffraction, Rayleigh, réseau,
lames minces, anneaux de Newton) étant hors programme. Avant : 4 sections (≈ 9,5 ko), 4 méthodes (3 hors programme),
8 exercices (4 hors programme, 2 « Concours PT » dont un doublon de l'exercice 2).

## Fichiers produits (dans `AN1/`)
- `od-cours.src.html` (98 ko, dont ≈ 63 ko de figures) — assemblé par `od_construire.py` à partir de `od-cours.tpl.html`
  et `od_figs.json` ;
- `od-meth.src.html` (10 méthodes), `od-exos.src.html` (12 exercices dont 1 « Concours PT ») ;
- `od-cartes-corr.json` (4 corrections de réponse), `od-cartes-ajout.js` (12 cartes) ;
- scripts : `od_figs.py` (figures), `od_calculs.py` (cours et exercices), `od_calculs_meth.py` (méthodes), `od_cartes.py`,
  `od_construire.py`, `od_couper.py` (coupure des formules en ligne trop larges au téléphone) ; aperçu des figures par
  `ond_voir.py od_figs.json …`.

## Erreurs trouvées et corrigées
| Où | Erreur | Correction |
|---|---|---|
| Cours (encadré `.hors-prog` d'origine, puis §1-§2) | Young, chemin optique et Fresnel au programme mais sous un encadré de hors-programme ; aucune démonstration de δ (capacité « établir l'expression littérale ») | encadré remplacé par le bloc « AU PROGRAMME · PTSI » ; 8 sections au programme, δ établi pas à pas (§5) ; hors-programme regroupé en 2 sections finales |
| Cours §1 (ancien) | superposition écrite avec « E₀ cos » et « I » sans définir l'intensité ni ce que mesure un détecteur | §1 (vibration scalaire, détecteur, intensité ℰ ∝ ⟨s²⟩), §3 (Fresnel, conditions) |
| Exercice 3 (devenu EXO 08) | Q2 « ouvertures petites devant Lλ/a » (critère maladroit) ; Q3 redonnait la valeur de Q1 (1 cm = 10 mm) | critère b² ≲ λL ; Q3 portée à 2 cm (b = 0,1 mm) |
| Exercice 5 (devenu EXO 10, Newton) | liquide d'indice 1,5 entre deux verres d'indice ≈ 1,5 : les réflexions disparaîtraient (adaptation d'indice), donc plus d'anneaux | eau (n = 1,33) : r′₁₀ = 2,60 mm ; remarque sur l'adaptation d'indice ; formule r_k = √(kλR/n) fournie |
| Exercice 6 (devenu EXO 11) | titre « … et cohérence » sans rapport ; « LRO … bien équipée d'optiques spécialisées » (c'est sa distance de 50 km qui compte) | titre « Limite de résolution d'un télescope » ; explication par la distance, diamètre nécessaire depuis la Terre ≈ 64 m |
| Concours (parties diffraction) | « 10 franges dans la tache centrale » : il y a 10 interfranges mais 9 franges brillantes (ordres ±5 sur les zéros de diffraction) | corrigé (et figure calculée de l'enveloppe en PAPL) |
| Concours 2 (lame mince) | doublon de l'exercice 2, présenté comme second « Concours PT » | devenu EXO 06 (repère et signe de δ précisés) ; un seul « Concours PT » |
| Carte 3 (Fresnel) | « Max = 4I₀ » avec I₀ non défini | « pour I₁ = I₂ = I₀ : max 4I₀, min 0 » |
| Carte 17 (phénomène de Gibbs) | carte de signaux égarée dans ce deck, sans mention de hors-programme (non retirable) | réponse préfixée « Hors programme en PTSI (signaux, pour aller plus loin) : » et précisée (9 % du saut, ne diminue pas) |
| Carte 18 | la même lettre a désigne l'écart des fentes et la largeur d'une fente | b pour la largeur ; 2a/b interfranges dans la tache |
| Carte 23 | « division d'amplitude (miroirs, …) » : les miroirs de Fresnel divisent le front d'onde ; Young ne fait pas de division d'amplitude | réponse reformulée (Young = division du front d'onde ; Michelson, lames minces = division d'amplitude) |

## Couverture du programme (partie 1.6, interférences lumineuses) : avant → après
| Capacité exigible | Avant | Après |
|---|---|---|
| Signal lumineux, λ₀, couleur, indice ; intensité (1.1 et 1.6) | λ_n = λ/n, plage visible | §1 (détecteurs, tableau de sources, exemple), méthode 1, EXO 02, cartes |
| Relier le déphasage à la différence de chemin optique | formule seule, chemin optique non défini | §2 (chemin optique, ordre p, exemple), méthodes 1-2, EXO 02, cartes |
| Interférences de deux ondes de même fréquence : conditions constructives / destructives | formules | §3 (conditions, cohérence qualitative), méthodes 2 et 7, EXO 03, cartes |
| Exploiter la formule de Fresnel fournie | formule seule | §3 (figure calculée, 2 exemples), §6, méthode 3, EXO 03, cartes |
| Trous d'Young : dispositif | schéma dessiné à la main | §4 (figure calculée : cônes de diffraction, H, θ ; rôle de la diffraction, bifente) |
| Établir l'expression littérale de la différence de chemin optique | résultat admis | §5 (démonstration en 3 étapes, lecture géométrique, validité chiffrée), méthode 4, EXO 04, concours A1, carte |
| Répartition d'intensité, franges, interfrange | formules | §6 (figure calculée écran + profil, 2 exemples dont mesure de λ₀), méthode 5, EXO 01, cartes |
| Lame sur un trajet, changement de milieu | une ligne | §7 (figure calculée, 2 exemples), méthode 6, EXO 05-06, concours B (indice de l'air), carte |
| Mettre en œuvre un dispositif d'interférences | absent | §8 (montage, ordres de grandeur, mesures, lumière blanche avec figure calculée, analogie ultrasonore), méthodes 5 et 8, EXO 07, cartes |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 8 sections + 2 « Pour aller plus loin ») : §1 La lumière, une onde ; §2 Chemin
optique et déphasage ; §3 Superposition de deux ondes lumineuses (Fresnel fournie, lien avec l'amplitude en bloc
dépliable, conditions) ; §4 Dispositif des trous d'Young ; §5 Différence de chemin optique (δ ≈ nax/D établi) ; §6 Franges
et interfrange ; §7 Modifier la différence de marche ; §8 Les interférences en pratique (lumière blanche) ; PAPL « Ce que
l'on verra en 2ᵉ année » (démonstration de Fresnel, cohérences, contraste, réseau, Michelson) ; PAPL « Diffraction et lames
minces » (fente, Rayleigh, lames minces, anneaux de Newton : contenu des anciens §3-§4, condensé). 11 exemples traités
chiffrés, 8 notices, 6 figures SVG calculées (Fresnel pour deux rapports d'intensités, montage d'Young, franges et profil,
décalage par une lame, trois couleurs en lumière blanche, enveloppe de diffraction).

**Méthodes** (10) : chemin optique et déphasage ; nature des interférences ; formule de Fresnel ; établir δ des trous
d'Young ; franges et mesure de λ₀ ; lame ou changement de milieu ; vérifier qu'il peut y avoir interférences ; lumière
blanche ; diffraction et réseau (hors programme, ancien 3 et 4 fusionnés) ; lames minces (hors programme, ancienne 2) ;
pièges d'origine conservés en notice finale.

**Exercices** (12) : au programme d'abord (EXO 01 ancien, EXO 02 chemin optique, EXO 03 Fresnel à faisceaux inégaux,
EXO 04 δ exact / approché, avec erreur comparée à λ₀, EXO 05 et 06 anciens (lame), EXO 07 lumière blanche et spectre
cannelé) ; puis anciens hors programme corrigés et signalés (EXO 08 diffraction, 09 réseau (2ᵉ année), 10 Newton, 11
Rayleigh) ; « Concours PT » : A interférences (δ à établir), **B nouvelle partie au programme** (mesure de l'indice de l'air
par défilement de 23 franges, incertitude 1,2 × 10⁻⁶, rôle du second tube), C diffraction (hors programme, corrigée).

**Cartes** : 25 → 37 (4 réponses corrigées, 12 ajoutées à la fin : chemin optique, Δφ = 2πδ/λ₀, ordre p, ℰ_max et ℰ_min,
établir δ, interfrange en milieu d'indice n, forme des franges, rôle des petits trous, ordres de grandeur, sources
incohérentes, ce que mesure un détecteur, mesure de λ₀).

## Notations
Celles des chapitres de 2ᵉ année `interf` et `dispinterf`, pour les préparer mot pour mot : λ₀ (vide), n, (AB) chemin
optique, δ = (S₂M) − (S₁M), Δφ = φ₂ − φ₁ = 2πδ/λ₀ (retard de phase φ, s = a cos(ωt − φ)), ordre p = δ/λ₀, intensité ℰ
(« intensité lumineuse, ou éclairement »), S₁ en x = +a/2 et S₂ en x = −a/2, i = λ₀D/(na). La lame sur un trajet est notée
n_ℓ, e comme en 2ᵉ année. Les mêmes conventions (retard de phase, δ = S₂M − S₁M) sont employées dans `ondes` pour les ondes
mécaniques.

## Doutes et remarques pour l'intégration
- Notation divergente laissée en place : la question de la carte 1 parle de « hauteur y » et les cartes d'origine emploient
  I (et non ℰ) ; le simulateur (non modifié) affiche I(x) = 2I₀[…] et λ. Le cours signale que ℰ est « notée parfois I ».
- Le site a désormais un chapitre « Ondes mécaniques » qui contient l'amplitude de la somme de deux sinusoïdes : `od` y
  renvoie (§3) au lieu de la refaire. Si `ondes` est renommé (suggestion : « Propagation d'un signal et interférences »),
  mettre à jour les 4 renvois de `od-cours`.
- Renommage possible : « Optique ondulatoire : interférences et trous d'Young » décrirait mieux le chapitre ; non indispensable.
- La diffraction n'est pas citée par la partie 1.6 ; elle intervient au §4 seulement en ordre de grandeur (λ/b), comme
  limite de l'optique géométrique (partie 1.1) et condition des interférences d'Young ; la formule des minima d'une fente et
  le critère de Rayleigh restent en « Pour aller plus loin ».
- L'EXO 07 (spectre cannelé) touche à la variation de l'ordre avec la longueur d'onde (capacité de PT 3.3) ; il n'exige
  que les conditions d'interférences constructives / destructives du programme de PTSI.
