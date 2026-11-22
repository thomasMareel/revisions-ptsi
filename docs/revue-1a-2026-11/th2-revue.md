# Revue du chapitre `thermo2` (prefix `th2`) — « 1er principe thermo » — 2026-11-22

Objet (point 7 de l'audit : mettre la 1ʳᵉ année au format de la 2ᵉ) : cours de 15 500 signes en 6 sections, une figure
dessinée à main levée, pas de bloc « Au programme », pas d'exemple traité ; 6 méthodes ; 7 exercices dont un « Concours PT »
de deux questions ; 32 cartes. Programme : PTSI 2021, parties 3.2 « Énergie échangée par un système au cours d'une
transformation » et 3.3 « Premier principe. Bilans d'énergie » (`ptsi.txt` l. 1524-1582), plus la capacité expérimentale
« Mettre en œuvre une technique de calorimétrie » (l. 421). Vérifié : le premier principe pour un fluide en écoulement
(détendeur, Joule-Thomson) est au programme de PT (`phys.txt` l. 682-754), pas de PTSI ; la loi de Laplace est en 3.4.

## Décisions
- **Numérotation conservée** : §1 à §6 gardent leur numéro et leur sujet (`thermo3` renvoie à §1 pour les définitions, le
  thermostat et les causes d'irréversibilité, à §5 pour la démonstration de Laplace par le premier principe, à §6 pour
  Joule-Gay-Lussac). Nouvelles sections **après** : §7 Bilans sur un chemin donné, §8 Calorimétrie, §9 Premier principe en
  puissance, puis « Pour aller plus loin ».
- **Table ancien § → nouveau §** : §1-§5 inchangés ; §6 garde Joule-Gay-Lussac (titre de section « Détente de
  Joule-Gay-Lussac et transformations brutales ») ; l'ancienne partie « Calorimétrie » du §6 passe au §8 (développée) ;
  l'ancienne partie « Joule-Thomson » (signalée hors programme au milieu du §6) passe en fin de chapitre. Aucun autre
  chapitre ne renvoyait à la calorimétrie du §6 ; les liens « Voir dans le cours » des cartes sont calculés à l'affichage
  (`flashCible`) et suivent le contenu.
- **Changements d'état** (3.3) : traités dans `changement` §7-§8 ; ici, bloc programme et §8 y renvoient.
- **Loi de Laplace** (3.4) : énoncé, conditions et démonstration par le premier principe entre deux états voisins gardés au
  §5 (démonstration en bloc dépliable), renvoi à `thermo3` §8.
- **Notations** alignées sur `thermo1`, `thermo3`, `machines` : \(P\), \(P_{\text{ext}}\), \(W\) et \(Q\) reçus, \(C_V\),
  \(C_P\), \(C_{V,m}\), \(c\), \(\gamma\), \(T_0\) thermostat, \(\mu\) valeur en eau, \(W_e\) travail électrique,
  \(\mathcal P\) puissance (pour ne pas la confondre avec la pression), « quasi statique » sans trait d'union comme `thermo3`.

## Fichiers produits (dans `AN1/`)
- `th2-cours.src.html` (82 ko, 48 700 signes de texte contre 15 500) — assemblé par `th2_construire.py` depuis
  `th2-cours.tpl.html` et `th2_figs.json` ; `th2-meth.src.html` (10 méthodes, 4 encadrés de pièges) ;
  `th2-exos.src.html` (11 exercices + « Concours PT », assemblé depuis `th2-exos.tpl.html`) ;
- `th2-cartes-corr.json` (3 réponses corrigées) ; `th2-cartes-ajout.js` (14 cartes) ;
- scripts : `th2_figs.py` (8 figures), `th2_calculs.py` (cours, avec CoolProp), `th2_calculs_exos.py` (méthodes,
  exercices, concours ; sympy), `th2_construire.py`, `th2_voir.py`, `th2_deborde.js`, `th2_elements.js`,
  `th2_cartes_rendu.js` ; copies `th2_orig_{cours,meth,exos}.html`.

## Erreurs trouvées et corrigées
| Où | Problème | Correction |
|---|---|---|
| Cours §6 (calorimétrie) | \(C_{\text{métal}} = \dfrac{(m_0c_{\text{eau}} + C_{\text{calo}})(T_f - T_0)}{m(T_f - T_1)}\) : signe faux (résultat négatif), et « \(m\,C_{\text{métal}}\) » mêle capacité et capacité massique | §8 : \(c = \dfrac{(m_0 + \mu)c_{\text{eau}}(T_f - T_0)}{m(T_1 - T_f)}\), notice sur le signe |
| Ancien EXO 04 | données incohérentes : avec \(T_f = 30{,}4\) °C, \(c_{\text{Al}} = 10\,433/10\,440 = 0{,}999\), et non 0,899 annoncé | \(T_f = 29{,}5\) °C, \(c_{\text{Al}} = 0{,}901\) J·K⁻¹·g⁻¹ (tabulé 0,897) ; Q4 sur la sensibilité (1,2 % pour 0,1 °C) |
| Ancien EXO 02 | cycle non fermé (C → A « isobare à \(P_2\) de \(V_2\) à \(V_1\) » arrive en (\(V_1\), \(P_2\)), pas en A) ; corrigé laissé en brouillon (« C(V₁+,P₂)... Attendons ») | cycle rectangulaire ABCDA (4 étapes), \(Q\) par étape vérifié, rendement 0,15 |
| Ancien EXO 01 | \(\Delta U \approx 499\) J et \(W \approx -138\) J (arrondis intermédiaires) | \(nRT_0 = P_0V_0 = 200\) J exactement : \(\Delta U = 500\) J, \(W = -139\) J ; \(Q\) ajouté |
| Ancien EXO 03, Q3 | « 182 °C dans une pompe à vélo, bien observable, très raisonnable » : faux | commentaire nuancé (échanges avec le corps de pompe, valve) ; Q3 ajoutée (isotherme : 55 J contre 69 J) |
| Ancien EXO 06 (Carnot) | exercice de deuxième principe et de machines (entropie créée), hors du chapitre | retiré (couvert par `machines` §5 et `thermo3` §11, EXO 06) ; remplacé par des exercices de premier principe |
| Ancien « Concours PT » | deux questions d'application directe | nouveau problème en 4 parties (voir plus bas) ; l'ancien contenu est couvert par l'EXO 01 et le §7 |
| Cours §3 | « transformation quasi statique isobare ou monobare » : la formule \(W = -P_{\text{ext}}\Delta V\) vaut pour toute monobare, même brutale | distinction monobare (même brutale) / isobare quasi statique ; \(P_{\text{ext}}\) toujours |
| Cours §2 | « Q = 0 … paroi parfaitement diathermane avec le milieu extérieur à même température » : confus | supprimé ; définitions de \(W\) et \(Q\) réécrites |
| Cours §1 | « monobare : la pression interne peut ne pas être uniforme » imprécis ; « adiabatique : transformation très rapide » sans échelle ; « polytropique » parmi les transformations de base (hors programme) | monobare avec équilibre mécanique au début et à la fin ; « rapide devant la durée des transferts thermiques » ; polytropique en fin de chapitre |
| Cours §5 | conditions de Laplace incomplètes (ni « gaz parfait » ni « γ constant » dans l'encadré) | quatre conditions, renvoi `thermo3` §8 |
| Carte 17 | \(\Delta H = Q\) sans la condition d'équilibre mécanique initial et final | réponse corrigée (question inchangée) |
| Carte 26 | conditions de Laplace sans « gaz parfait, γ constant » | réponse corrigée |
| Carte 27 | « gaz réel : ΔT < 0 » présenté comme général | « varie un peu, en général léger refroidissement » |

Remarque : les phrases qui paraissent tronquées dans l'extraction texte de l'ancien cours (« dV  0 », « V₁ moteur ») ne
l'étaient pas sur le site (« < » suivi d'une espace est du texte en HTML). Le nouveau texte écrit \(\lt\) dans les formules.

## Couverture du programme : avant → après
| Capacité (3.2, 3.3) | Avant | Après |
|---|---|---|
| Définir un système adapté ; évolutions isochore, isotherme, isobare, monobare, monotherme | §1 (liste) | §1 (liste précisée, choix du système), §2 (système {voiture}), §6 (système {gaz, piston, masse}), méthode 1, EXO 01, 06, 07 |
| Exploiter les conditions imposées par le milieu extérieur pour l'état final | absent | §1 (piston lesté dans un bain, figure à l'échelle), §6 (masse posée d'un coup ou grain par grain ; compression adiabatique brutale), méthode 4, EXO 11, concours A, cartes |
| Identifier les systèmes modélisables par un thermostat | définition | §1 (exemples, tasse de thé dans une pièce chiffrée), carte existante |
| Distinguer conduction, convection, rayonnement | liste | §2 (exemples, ordre de grandeur solaire, bouteille isotherme) |
| Bilan énergétique d'un système fermé (W, Q) ; extensivité de U | énoncé | §2 (énoncé avec \(\Delta E_c\), figure système-frontière, freinage d'une voiture chiffré, extensivité), EXO 06 (grenaille de plomb), concours C2 |
| Premier principe entre deux états voisins | formule | §2, §5 (Laplace), §9 (bilans en puissance), méthode 10, EXO 10 |
| Statut de \(\Delta U\) / termes d'échange ; Q sur un chemin donné | une phrase | §2, §7 (méthode, tableau des transformations du gaz parfait, deux chemins chiffrés et figure calculée), méthode 5, EXO 01, 02, 08, cartes |
| Travail par découpage et sommation (une variable) ; lecture dans le diagramme de Clapeyron | §3 | §3 (gaz poussant un ressort, 1 bar·L = 100 J, figure calculée isotherme / détente brutale), §7, méthodes 2-3, EXO 02, 08 |
| Bilan d'enthalpie en monobare avec équilibre mécanique initial et final | §4 | §4 (conditions explicites, exemple chiffré), méthode 6, EXO 07, 11 Q5 |
| \(H_m(T)\) du gaz parfait à partir de \(U_m\) | GPM/GPD | §4 (\(H_m = U_m + RT\)), carte |
| \(H_m\) d'une phase condensée fonction de \(T\) seule | une ligne | §4 (chiffré avec les tables de l'eau, CoolProp), carte |
| Capacité thermique à pression constante ; ordre de grandeur de \(c_{\text{eau}}\) | §5 sans ordre de grandeur | §5 (Mayer, γ, encadré \(c_{\text{eau}} \approx 4{,}18\) kJ·K⁻¹·kg⁻¹, tableau de valeurs, air par Mayer vs mesure, bain chiffré), méthode 7, cartes |
| Technique de calorimétrie ; protocole de mesure | un paragraphe (formule fausse) | §8 (calorimètre en figure, valeur en eau et sa mesure, mélanges avec sensibilité, méthode électrique, précautions), méthode 9, EXO 04, 09, cartes |
| Transitions de phase (3.3) | absent | renvoi `changement` §7-§8 (bloc programme, §8, méthode 9) |
| Loi de Laplace (3.4) | §5 | §5 (démonstration par le premier principe, détente de l'air chiffrée), méthode 8, EXO 03, concours B ; énoncé et conditions : `thermo3` §8 |

## Contenu
**Cours** (« AU PROGRAMME · PTSI » + 9 sections + « Pour aller plus loin ») : §1 Transformations (vocabulaire, quasi statique,
réversible, thermostat, état final imposé) ; §2 Premier principe (W, Q, trois modes de transfert, énoncé avec \(\Delta E_c\),
statuts, extensivité) ; §3 Travail des forces de pression ; §4 Enthalpie ; §5 Capacités thermiques, Mayer, γ, Laplace ;
§6 Joule-Gay-Lussac et transformations brutales ; §7 Bilans sur un chemin donné ; §8 Calorimétrie ; §9 Premier principe en
puissance ; hors programme : Joule-Thomson et premier principe industriel (2ᵉ année), polytropiques. 17 exemples traités
chiffrés, 9 notices « Erreur classique », 1 démonstration dépliable, 2 tableaux, 7 figures calculées (transformations au
départ d'un même état, piston lesté à l'échelle, système et frontière, travail = aire, deux chemins, calorimètre,
chauffage avec pertes), vérifiées en clair et en sombre.

**Méthodes** (10) : système et transformation ; travail sur un chemin ; lecture dans Clapeyron ; état final d'une
transformation brutale ; Q sur un chemin ; bilan d'enthalpie ; capacités du gaz parfait ; Laplace ; bilan calorimétrique ;
bilan en puissance ; 4 encadrés de pièges (dont les anciens pièges, corrigés). Les anciennes méthodes 1-4 sont reprises ;
l'ancienne méthode 5 (Joule-Gay-Lussac / Joule-Thomson) est fondue dans la méthode 4 et les pièges.

**Exercices** (11 + concours) : 01 vocabulaire (corrigé) ; 02 cycle rectangulaire (refait) ; 03 pompe à vélo (Q3-Q4
corrigées) ; 04 calorimétrie de l'aluminium (données corrigées) ; 05 Joule-Gay-Lussac, gaz parfait et gaz réel (ancien,
juste) ; 06 grenaille de plomb et chute d'eau ; 07 gaz chauffé sous un piston lesté ; 08 trois chemins entre deux états ;
09 méthode électrique (μ, capacité de l'éthanol, effet des pertes) ; 10 ballon d'eau chaude (bilan en puissance, nuit sans
chauffage) ; 11 compression brutale calorifugée (\(T_f = T_i[1 + (\gamma-1)P_e/P_i]/\gamma\), limite \(\gamma/(\gamma-1)\)) ;
**Concours PT « Deux compartiments, un piston et une résistance »** (A conditions imposées ; B état final par Laplace,
1,52 L, 366 K, 3,48 L, 834 K ; C travaux et \(W_e = 2V_0(P_f - P_0)/(\gamma - 1) = 1\,250\) J par deux bilans ; D piston
rendu diathermane : 600 K et 2,00 bar, variante hélium 750 J), avec une figure.

**Cartes** : 3 réponses corrigées (17, 26, 27 ; questions inchangées, réponses écrites en `\( … \)` pour éviter un découpage
fautif par `flashPretty`) ; 14 ajoutées à la fin (\(c_{\text{eau}}\), travail monobare, \(\Delta U + \Delta E_c\), statuts,
Q sur un chemin, \(H_m(T)\), phase condensée, monotherme ≠ isotherme, état final brutal, valeur en eau, méthode électrique,
bilan en puissance, énergie d'un bain, \(c_V\) et \(c_P\) de l'air). Deck : 32 → 46. Rendu contrôlé par
`th2_cartes_rendu.js` : aucune erreur MathJax.

## Contrôles
`verif_src.py` (3 fichiers) : aucune erreur ni « attention ». `apercu_src.py` à 390 et 1440 px pour les trois panneaux :
`merr`, `brut`, `larges` vides, `scrollW` égal à la largeur, aucune erreur JS (une quinzaine de formules en ligne trop larges au téléphone,
repérées par l'aperçu et `th2_deborde.js`, ont été raccourcies ou passées en bloc). Cartes : `corriger_cartes.py th2 …
--essai` (3) et `ajouter_cartes.py th2 … --essai` (32 → 46) sans erreur. Tous les nombres recalculés (`th2_calculs.py`,
`th2_calculs_exos.py`).

## Doutes et points pour l'intégration
- **Titre** : « 1er principe thermo » est un libellé court ; proposition « Premier principe : bilans d'énergie »
  (mobLabel « 1er principe » inchangé), pendant de « Deuxième principe : bilans d'entropie ». Les liens textuels de
  `thermo3` (« 1er principe thermo »), `changement` et `machines` (« 1er principe ») seraient alors à harmoniser.
- Les cartes d'origine emploient « GPM / GPD » et des formules Unicode ; laissées telles quelles (justes).
- Le simulateur (`drawTh2`, non modifié) propose encore un mode « Cycle de Carnot » : sans objet ici, mais pas faux.
- Valeurs tabulées choisies à la main (capacités des solides, huile ≈ 1,7 à 2, éthanol 2,44, ordre de grandeur solaire
  1 kW·m⁻²) ; eau, air, CO₂ calculés avec CoolProp. La détente de Joule-Gay-Lussac du CO₂ donne −6,3 K avec l'énergie
  interne de Van der Waals fournie, −11 K avec les équations de référence : le cours le dit.
- §9 utilise une loi de pertes \(G(T - T_a)\) **fournie par l'énoncé** (la conduction est au programme de PT) ; résolution
  d'une équation du premier ordre, connue de l'électrocinétique.
