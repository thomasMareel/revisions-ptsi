# Nouveau chapitre `incertitudes` (« Mesures et incertitudes », prefix `inc`) — 2026-11-21

Chapitre de physique-chimie de 1ʳᵉ année, partie « Référence ». Il comble le premier manque de l'audit
(`docs/audit-2026-11/physique-1a.md`, §2 point 1 et §5 point 2) : le bloc « Mesures et incertitudes » de la
formation expérimentale, présent dans les écrits et omniprésent à l'oral de TP, était absent du site.
Rédaction entièrement originale (aucun manuel ne couvre cette partie dans le dépôt privé ; aucune source copiée) ;
toutes les données numériques des exemples et exercices sont inventées ou simulées avec une graine fixe.

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu | Taille |
|---|---|---|
| `inc-cours.src.html` | cours : bloc « Au programme · PTSI », §1 à §11, « Pour aller plus loin » ; 9 figures, 4 programmes Python | 115 000 car. (dont ≈ 60 000 de SVG) |
| `inc-meth.src.html` | 10 méthodes, 5 pièges | 13 000 car. |
| `inc-exos.src.html` | 11 exercices + 1 « Concours PT » en 4 parties ; 2 figures, 3 programmes Python | 55 000 car. |
| `inc-cartes.js` | `const incCards = [ … ];`, 28 cartes (12 avec `cat`) | |
| `inc-cours.tpl.html`, `inc-meth.tpl.html`, `inc-exos.tpl.html` | gabarits (`@@FIG:nom@@`, `@@CODE:nom@@`) | |
| `inc_build.py` | assemble les gabarits : figures de `inc_figs.json`, code de `inc_code_*.py` coloré (`kw`, `cmt`, `str`) | |
| `inc_figs.py` → `inc_figs.json` | 11 figures calculées (graines fixes) | |
| `inc_code_*.py` (7) | **le code affiché, exactement** : `typeA`, `mc_focale`, `regression`, `mc_regression` (cours), `ex07`, `ex11`, `concours` (exercices) | |
| `inc_tests.py` + `inc_tests_suite.py` | exécutent les 7 programmes et vérifient 219 valeurs du cours, des méthodes et des exercices (sympy/numpy/scipy) | |
| `inc_cartes_verif.js` | contrôle du deck (nombre, doublons, champs sans `\(` qui seraient « mathématisés » par `flashPretty`) | |
| `inc_voir.py` → `inc_voir_captures/` | aperçu rapide des figures en clair et en sombre, à 540 et 360 px | |

Assemblage : `python3 inc_build.py` ; tests : `python3 inc_tests.py` (sortie « ÉCHECS : aucun — OK »).

## Contrôles effectués (un par un)

- `verif_src.py` sur les trois panneaux : aucune ERREUR, aucune « attention » (11 sections numérotées, 13 exemples, 9 figures dans le cours).
- `maths/apercu_src.py` (avec `P2A_INDEX=AN1/site/index.html`) à 390 et 1440 px pour cours, méthodes, exercices :
  `merr`, `brut`, `larges` vides, aucune erreur JS, `scrollW` égal à la largeur. Une première version des
  exercices débordait à 390 px (onze formules en ligne de 40 à 60 signes, enveloppées dans `.mj-colle` par la
  ponctuation qui les suit, que `verif_src.py` ne signalait pas) : passées en bloc ou raccourcies.
- Captures à 1440 px regardées pour chaque figure (cours et exercices), et toutes les figures en clair et en sombre
  avec `inc_voir.py` (libellés, recouvrements, axes coupés corrigés en route).
- Cartes : `node -e "eval(…'inc-cartes.js'…+';console.log(incCards.length)')"` → 28 ; `inc_cartes_verif.js` :
  0 doublon, 0 champ à risque ; le TeX des 56 champs a été rendu par MathJax dans la copie du site (0 `merr`).
- `inc_tests.py` : les 7 programmes s'exécutent (`MPLBACKEND=Agg`) et toutes les valeurs citées sont vérifiées.
  Les résultats des simulations de Monte-Carlo (sans graine dans le code affiché) ont été relancés plusieurs fois :
  les valeurs citées, arrondies, sont stables.

## Couverture du programme (PTSI, « 1. Mesures et incertitudes » ; identique mot pour mot en PT)

| Capacité exigible | Avant | Après (cours / méthode / exercice / carte) |
|---|---|---|
| Identifier les incertitudes liées à l'opérateur, l'environnement, les instruments, la méthode | ❌ | §1 / M1 / EXO 02, 04 Q4, 09, concours A3 / cartes 2, 3 |
| Incertitude-type, erreur aléatoire et systématique, mesurande | ❌ | §1 / M1 / EXO 05 Q4, concours A3 / cartes 1, 3, 4 |
| Évaluation de type A | ❌ | §2 (+ code) / M2 / EXO 01, 05 Q4, 09, concours A1 / cartes 5, 6 |
| Évaluation de type B | ❌ | §3 / M3 / EXO 02, 04, 05 / cartes 7, 8, 9, 27 |
| Intervalle de confiance, loi normale | ❌ | §4 / M4 / EXO 01 Q3 / carte 10 |
| Incertitudes composées (somme, différence, produit, quotient), comparer les contributions | ❌ | §5 / M5 / EXO 01, 04, 05, 06 / cartes 11, 12, 14 (puissance : carte 13) |
| Capacité numérique : simuler la variabilité d'une grandeur composée | ❌ | §6 (+ code) / M6 / EXO 07 (code) / cartes 15, 16 |
| Écrire un résultat (chiffres significatifs) | ❌ | §7 / M7 / EXO 03 / carte 17 |
| Écart normalisé ; analyser une incompatibilité | ❌ | §8 / M8 / EXO 04, 05, 06, 07, 08, 11, concours C3, D2 / cartes 18, 19 |
| Régression linéaire : logiciel, validation par barres ou écarts normalisés (pas R²) | ❌ | §9 (+ code) / M9 / EXO 10, 11, concours B / cartes 20 à 23 |
| Capacité numérique : Monte-Carlo sur les paramètres d'un modèle | ❌ | §10 (+ code) / M10 / EXO 10, 11 (code), concours C, D (code) / carte 24 |
| Annexe 3 (outils numériques) : `random.normal`, tirages, `hist`, moyenne et écart-type, `polyfit` | ❌ | §2, §6, §9, §10 / M2, M6, M9, M10 / EXO 07, 11, concours / cartes 5, 16, 20 |
| Ordres de grandeur, bonnes pratiques de TP (formation expérimentale) | ❌ | §11 / M1 / EXO 02, 09 / cartes 25, 26, 27 |

Hors programme, regroupé en fin de cours (« Pour aller plus loin ») : formule générale de propagation par les
dérivées partielles et corrélations (recoupée avec la simulation du §6), facteur de Student, formules des moindres
carrés, régression pondérée et χ². Une carte (n° 28) le signale par « Hors programme en PTSI : ».

## Contenu

**Cours** : §1 Variabilité de la mesure (mesurande, quatre familles de sources, erreur aléatoire et systématique,
incertitude-type ; exemple : chute chronométrée à la main) · §2 Type A (moyenne, écart-type expérimental,
\(s/\sqrt N\), justification par la variance d'une somme ; exemple : 8 chronométrages de 10T, code numpy) · §3 Type B
(loi uniforme, \(a/\sqrt3\) démontré ; graduation, affichage, notice « ±(p % + n digits) », verrerie, latitude de
mise au point ; exemple : voltmètre et image nette) · §4 Loi normale et intervalles 68/95/99,7 %, incertitude élargie
(et ce qui change pour une loi uniforme) · §5 Composition (somme/différence, produit/quotient, justification ; bilan
d'incertitude ; exemples : R = U/I, distance par différence, g du pendule ; puissance en complément) · §6 Monte-Carlo
(méthode, fonctions numpy, focométrie par la relation de conjugaison avec x_O commun aux deux distances, code,
contributions source par source) · §7 Écriture du résultat · §8 Écart normalisé, seuil 2, analyse d'une
incompatibilité en cinq causes (exemple : célérité du son à la bonne température) · §9 Régression linéaire
(linéarisation, `polyfit`, résidus et écarts normalisés, barres ±2u, piège du R² : T(L) donne R² = 0,991 avec une
arche de −8,8 à +6,3) · §10 Monte-Carlo sur les paramètres (code ; g = 9,81 m·s⁻², u = 0,06 ; b compatible avec 0)
· §11 Ordres de grandeur (tableau) et bonnes pratiques (combien de périodes chronométrer) · Pour aller plus loin.

**Figures** (calculées) : dispersion et décalage (4 séries) ; histogramme de 40 chronométrages avec loi normale ;
loi uniforme et loi normale de même écart-type ; loi normale et intervalles ; histogramme Monte-Carlo de f' ;
écarts normalisés de quatre binômes (célérité du son, deux références) ; T² = f(L) et résidus avec barres ±2u ;
T = f(L) avec R² = 0,991 et écarts normalisés structurés ; histogramme Monte-Carlo de g ; (exercices) écarts
normalisés de Beer-Lambert sur 8 et 5 points ; écarts normalisés de la sonde Pt100 pour deux précisions.

**Méthodes** (10) : identifier les sources ; type A ; type B ; intervalle de confiance ; composer et comparer les
contributions ; Monte-Carlo d'une grandeur composée ; écrire un résultat ; écart normalisé et analyse d'une
incompatibilité ; valider une régression ; Monte-Carlo sur les paramètres. Chacune avec étapes, exemple éclair chiffré
(nouvelles données, vérifiées) et, pour cinq d'entre elles, un piège.

**Exercices** (★ à ★★★) : 01 période d'un oscillateur (type A, intervalle, k, nombre de périodes) · 02 type B en
salle de TP · 03 écrire un résultat · 04 résistance par la loi d'Ohm (bilan, ohmmètre, tolérance, choix du montage :
erreur de méthode) · 05 titrage (bilan, type A contre type B, tolérance systématique) · 06 célérité des ultrasons
(référence à la bonne température) · 07 méthode de Bessel par Monte-Carlo (programme) · 08 un g trop faible
(trois causes chiffrées : amplitude, longueur, pendule pesant) · 09 choisir son protocole (rame de papier, périodes)
· 10 Beer-Lambert (R² = 0,9996 mais modèle rejeté ; domaine restreint ; ε et une concentration inconnue) · 11 pile
(régression avec incertitudes sur x et y, Monte-Carlo sur les deux grandeurs, E comparée à la tension à vide) ·
**Concours PT** « Étalonner une sonde de platine » : A mesure à quatre fils (type A, erreur systématique des fils) ;
B modèle affine sur 0-100 °C rejeté à 0,020 Ω mais accepté à 0,15 Ω ; C étalonnage 0-50 °C, programme de
Monte-Carlo, α comparé à l'α « nominal » (incompatibilité due à la définition du mesurande) ; D mesure d'une
température, incertitude incluant l'étalonnage, comparaison à un thermomètre médical, biais d'un modèle rejeté.

**Cartes** (28) : définitions, formules (`cat:'form'`), ordres de grandeur (`cat:'val'`), pièges (R², puissance,
chronométrage), fonctions numpy. Toutes les formules en `\\( … \\)` ; aucun champ sans `\(` ne contient de jeton que
`flashPretty` mettrait en formule (les noms de fonctions numpy restent en texte).

## Notations

\(x\) valeur mesurée, \(u(x)\) incertitude-type, \(u(x)/|x|\) incertitude relative ; \(\bar x\), \(s_x\) (écart-type
expérimental, diviseur \(N-1\)), \(u(\bar x)=s_x/\sqrt N\) ; demi-largeur \(a\) (type B), pas de graduation \(\Delta\) ;
incertitude élargie \(k\,u\) (sans symbole propre, pour éviter la confusion avec la tension \(U\)) ; \(E_N\) écart
normalisé (« z-score » cité) ; régression \(y=ax+b\), résidus \(y_i-(ax_i+b)\), écarts normalisés \(z_i\). Notations
de physique alignées sur le site : \(\overline{OA}\), \(f'\), \(T=2\pi\sqrt{L/g}\), \(c(\theta)\) ; « type A / type B »
comme le programme. Valeurs numériques à la française (virgule, `{,}` dans le TeX).

## Capacités numériques du programme de PTSI et chapitre qui devrait les porter

Relevé dans le programme officiel de PTSI (lignes indiquées). Aucune n'était traitée en physique-chimie
(l'audit ne trouve ni « Python » ni « Euler » dans les 37 chapitres de 1ʳᵉ année ; contrôlé de nouveau sur les
panneaux cours, méthodes et exercices de `po`, `osc`, `eme`, `cc`, `msol`, `eq`, `flt`, `cin`, `sig` : 0 occurrence).
Je ne les ai pas écrites (hors de ma mission), sauf les deux du bloc incertitudes.

| Partie du programme | Capacité numérique (résumé) | Chapitre du site qui devrait la porter |
|---|---|---|
| Mesures et incertitudes (l. 261) | simuler un processus aléatoire caractérisant la variabilité d'une grandeur composée | **`incertitudes` §6 (fait)** |
| Mesures et incertitudes (l. 280) | Monte-Carlo pour l'incertitude sur les paramètres d'un modèle (régression) | **`incertitudes` §10 (fait)** |
| 1.3 Circuit linéaire du 1ᵉʳ ordre (l. 735) | méthode d'Euler pour simuler la réponse d'un système du 1ᵉʳ ordre à une excitation de forme quelconque | `premierordre` (prefix `po`) ; renvoyer à `pynum` §6, qui traite déjà Euler côté informatique |
| 1.5 Filtrage linéaire (l. 850) | simuler l'action d'un filtre sur un signal périodique de spectre fourni, influence des caractéristiques du filtre | `filtres` (`flt`), en s'appuyant sur `signaux` (`sig`) pour le spectre |
| 2.3 Approche énergétique, mouvement conservatif 1D (l. 1069) | résoudre numériquement une équation différentielle du 2ᵉ ordre non linéaire, faire apparaître l'effet des termes non linéaires | `energie` (`eme`, §3 « Mouvement conservatif à 1D ») ; l'exemple du pendule simple peut vivre dans `oscill` (`osc` §4) ; outils : `pynum` §7 (système d'ordre 1, `odeint`) |
| 4.1 Transformations de la matière (l. 1130) | déterminer l'état final d'un système siège d'une réaction unique à partir des conditions initiales et de K | `equilchim` (`eq`) ; outil : dichotomie / `bisect` de `pynum` §2 |
| 2.6 Champ de force centrale conservatif (l. 1351) | obtenir des trajectoires d'un point matériel soumis à une force centrale conservative | `chcentral` (`cc`) ; outil : `pynum` §7 |
| 2.7 Mouvement d'un solide, pendule pesant (l. 1430) | mettre en évidence le non-isochronisme des oscillations | `mvtsolide` (`msol`) ; l'exercice 08 d'`incertitudes` utilise déjà la formule de Borda (admise) |
| 4.1.2 Cinétique chimique (l. 1140-1162, sans l'étiquette « capacité numérique ») | vitesse de réaction par méthode numérique ou graphique ; exploitation de mesures par programme (méthodes différentielle et intégrale) | `cinetique` (`cin`) ; la validation d'une loi intégrée par régression renvoie à `incertitudes` §9-10 |
| Annexe 3, outils numériques (l. 2212-2290) | matplotlib (nuage de points, courbe, courbe paramétrée) ; dichotomie et `bisect` ; rectangles ; dérivée approchée ; Euler explicite ; ordre n → système, `odeint` | `pynum` §1, §2, §4, §5, §6, §7 (déjà traités côté informatique) |
| Annexe 3, probabilités-statistiques | tirages `random` / `numpy`, `hist`, moyenne et écart-type ; `polyfit` ; `random.normal` | **`incertitudes` §2, §6, §9, §10 (fait)** |

## Doutes et points à trancher à l'intégration

1. **Place dans la partie « Référence »** : la demande dit « avant `constantes` », mais la copie du site
   (`AN1/site/index.html`, `CHAP_GROUPS`) range le groupe `['ref', 'Référence', ['constantes','incertitudes']]`,
   donc après. À ajuster par l'intégrateur (je n'ai pas touché à la copie, partagée).
2. **Puissance** : le programme ne cite que somme, différence, produit, quotient. La règle de la puissance est
   donnée dans le cours comme complément « fourni par l'énoncé ou par simulation » (avec sa justification au
   premier ordre), et utilisée dans des exercices où l'énoncé la rappelle. La formule générale par dérivées
   partielles est en « Pour aller plus loin ».
3. **Seuil de l'écart normalisé** : 2, présenté comme une convention (le programme n'en fixe pas).
4. **API numpy** : le code utilise `np.random.normal` / `np.random.uniform` (API historique, citée par le
   programme : « fonction random.normal de numpy ») plutôt que `np.random.default_rng()`. Les sorties varient d'une
   exécution à l'autre ; les valeurs citées sont arrondies et vérifiées sur plusieurs exécutions.
5. **Évaluation de la tolérance de la burette** (EXO 05 Q4) traitée comme systématique (même burette pour les trois
   titrages), donc ajoutée au type A de la moyenne : choix courant mais discutable selon les enseignants.
6. **Taille** : 115 000 caractères pour le cours, dont ≈ 60 000 de SVG (9 figures, chacune < 12 Ko) ; panneau
   replié au chargement comme les autres, donc sans effet sur le démarrage.
7. **Blocs de code** : lignes de 62 caractères au plus ; ils défilent au téléphone (comportement normal de
   `.codeblock`). Les commentaires du code sont en français ; les nombres dans le code restent au format Python.
8. **Valeurs de la Pt100** du concours : données simulées à partir du modèle normalisé
   \(R_0(1+A\theta+B\theta^2)\), \(A=3{,}9083\times10^{-3}\), \(B=-5{,}775\times10^{-7}\) (valeurs publiques de la
   norme CEI 60751), avec un bruit de 0,020 Ω ; l'α « nominal » 3,851×10⁻³ °C⁻¹ en découle.
