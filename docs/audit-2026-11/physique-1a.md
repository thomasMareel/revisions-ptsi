# Audit : physique-chimie de 1ʳᵉ année (PTSI)

Périmètre : les 37 chapitres `mat = physique`, `an = 1` de `mesures.json` (dont `constantes` et les aperçus `estat`, `emag`, `fluides`, `changement`). Référence : programme de physique-chimie de PTSI 2021 (`/home/user/pdf-pt/prog/ptsi.txt`). Méthode : les 37 cours lus en diagonale (extraction par panneau), méthodes et exercices survolés (titres, niveaux, corrigés), cartes relues sur 20 decks. Lecture seule, 2026-11-14.

## Synthèse

- La 1ʳᵉ année est **un niveau en dessous de la 2ᵉ** : 248 000 signes de cours en tout, médiane de 5 400 signes par chapitre (contre ≈ 30 900 en 2ᵉ année), 164 méthodes, 222 exercices (tous corrigés), 889 cartes, aucun encadré « Au programme » et aucun hors-programme regroupé en fin de chapitre.
- **Deux blocs transversaux manquent entièrement** : « Mesures et incertitudes » et les capacités numériques (aucune occurrence d'Euler ni de Python dans les 37 chapitres).
- **L'« introduction au monde quantique » n'est pas un manque** : elle n'est pas au programme de PTSI 2021 (elle l'est en PCSI et MPSI), ni à celui de PT. La seule trace quantique du site (nombres quantiques de `atome`) est hors programme.
- Le programme est surtout **couvert mais inégalement** : mécanique, oscillateurs, filtrage, thermodynamique (principes) et oxydoréduction sont solides. Induction, ondes, changements d'état, solutions aqueuses et cristallographie sont partiels ou minces.
- Des encadrés se trompent sur le programme. Young et les interférences sont déclarés « hors programme PTSI » alors qu'ils y sont (1.6). Les encadrés de `fluiddyn` et de `fluides` se contredisent. Une partie du programme de PTSI est renvoyée à la 2ᵉ année : `changement`, et `emag`, marqué « aperçu ».
- J'ai repéré une quinzaine d'erreurs ou d'incohérences, dont plusieurs recopiées dans les cartes (déflexion électrique, échelles de la thermodynamique, Vm = 22,4 L/mol à 1 bar, référentiel géocentrique, énergie du circuit RL).

## 1. Couverture du programme de PTSI

| Programme (bloc) | Chapitre(s) et § | Statut | Remarque |
|---|---|---|---|
| Mesures et incertitudes (types A et B, composition, écart normalisé, régression, Monte-Carlo) | Aucun chapitre (seulement `sysnum`, SI de 2ᵉ année) | ❌ | Aucun cours, aucune méthode, aucune carte en physique-chimie |
| Capacités numériques (Euler au 1ᵉʳ ordre, ED non linéaire, trajectoires, état final chimique) | Aucun chapitre | ❌ | Aucun « Python » ni « Euler » dans les cours, méthodes ou exercices |
| 1.1 Sources, spectre, modèle de l'optique géométrique et ses limites | optgeo §1 | 🔶 | Pas de spectre de raies ni de spectre continu ; domaine visible donné de 400 à 800 nm |
| 1.1 Snell-Descartes, réflexion totale, miroir plan, Gauss, lentilles, formules de Descartes et de Newton, D ≥ 4f′ | optgeo §2-3, optique §1 | ✅ | |
| 1.1 Œil, appareil photo, fibre à saut d'indice | optique §2, optgeo §4 | 🔶 | Profondeur de champ définie mais pas construite ; rôle de la focale et du temps de pose absent ; fibre ✅ |
| 1.2 ARQS (condition taille/fréquence), charge quantifiée, ordres de grandeur | regimecontinu §1 | 🔶 | L'ARQS est nommée sans sa condition ; aucun ordre de grandeur (I, U, R, L, C) |
| 1.2 Dipôles, lois de Kirchhoff, diviseurs, Thévenin, résistances d'entrée et de sortie | regimecontinu §2-4, rlc §1, filtres méthode 6 | 🔶 | Résistances d'entrée et de sortie seulement en méthode, pas en cours |
| 1.3 Circuit du 1ᵉʳ ordre (ED, échelon, régime libre, deux mailles, bilan d'énergie) | premierordre §1-3 | 🔶 | 1 826 signes ; ni circuit à deux mailles ni régime libre RL ; Euler absent |
| 1.4 Oscillateurs libres, amortis et forcés, Q, résonance, impédances | rlc §2-7, oscill §2-7, energie §4 | ✅ | Traité trois fois (voir doublons) |
| 1.5 Signaux périodiques, valeur efficace, spectre, Parseval | signaux §1-3 | ✅ | S'y ajoutent du hors-programme : calcul des coefficients, THD, cos φ |
| 1.5 Fonction de transfert, Bode, filtres d'ordre 1 et 2, moyenneur, intégrateur, dérivateur | filtres §1-6 | ✅ | |
| 1.5 Filtrage mécanique (sismomètre…), non-linéarité, mise en cascade | filtres méthode 6 | 🔶 | Filtrage mécanique et repérage de la non-linéarité absents |
| 1.6 Onde progressive f(x − ct), f(t − x/c), retard, déphasage, double périodicité | ondes §1 | 🔶 | Forme f(t − x/c) absente ; d'Alembert (hors programme) en tête |
| 1.6 Milieux dispersifs (définition, exemples) | ondes (un « piège » de méthode) | ❌ | |
| 1.6 Interférences de deux ondes acoustiques ou mécaniques | ondes, exercices seulement | 🔶 | Aucun cours |
| 1.6 Interférences lumineuses, trous d'Young, chemin optique, formule de Fresnel | optiqued §1-2 | 🔶 | Contenu présent, mais sous un encadré « Hors programme PTSI » erroné |
| 1.7.1 Cartes de champ (aimant, spire, bobine), ordres de grandeur, symétries, moment magnétique | emag §1, §3 (chapitre « aperçu ») | 🔶 | Mêlé de hors-programme (Biot-Savart, Ampère, H, réluctance) ; ni carte d'aimant ni ordres de grandeur (IRM, champ terrestre) dans le cours |
| 1.7.2 Laplace sur une barre, couple m ∧ B, aimant et boussole, champ tournant | emag §3, induction §5 | 🔶 | Champ tournant absent ; boussole seulement en exercice |
| 1.7.3 Flux, loi de Faraday, loi de Lenz | induction §1-2 | ✅ | |
| 1.7.4 Auto-induction, inductance mutuelle de bobines coaxiales, circuits couplés en RSF, transformateur | induction §3-4 | 🔶 | M des bobines coaxiales et équations couplées absentes ; transformateur sans bilan de puissance |
| 1.7.5 Rails de Laplace, spire en rotation, courants de Foucault, moteur à courant continu à entrefer plan | induction §5 | 🔶 | Rails seulement ; alternateur en exercice ; Foucault et moteur à courant continu absents |
| 2.1 Cinématique (cartésiennes, cylindriques, sphériques, déplacement élémentaire, Frenet) | cinept §1-3 | 🔶 | Ni sphériques, ni déplacement élémentaire, ni degrés de liberté ; §4 (composition des vitesses) hors programme |
| 2.2 Lois de Newton, forces, pendule simple, chute avec frottement | mecpt §1-3, oscill §4 | 🔶 | Ni système de points, ni p = m v(G), ni conservation de la masse ; vitesse limite en exercice seulement ; pas d'équation adimensionnée |
| 2.3 Énergie, énergie potentielle et stabilité, petits mouvements | energie §1-3 | ✅ | |
| 2.4 Particule chargée dans E ou B uniforme | lorentz §1-4 | ✅ | Formule de déflexion fausse (voir §4, point 1) |
| 2.5 Moment cinétique, bras de levier, conservation | mcinc §1, mvtsolide §2 | ✅ | Le bras de levier n'apparaît que dans `mvtsolide` |
| 2.6 Force centrale, énergie potentielle effective, Kepler, satellites | chcentral §1-3 | ✅ | |
| 2.7 Solide : translation, rotation, TMC scalaire, pendule pesant, Ec, tabouret d'inertie | mvtsolide §1-4 | ✅ | Mince : 2 méthodes, 3 exercices |
| 3.1 Échelles, libre parcours, gaz parfait, u, Ec = 3/2 kT, phases condensées | thermo1 §1-6 | ✅ | Erreurs sur les échelles et sur Vm (voir §4, points 2 et 3) |
| 3.1 Gaz réel (isothermes de Clapeyron et d'Amagat), compressibilité liquide/gaz | thermo1 §5 (une phrase) | ❌ | |
| 3.1 Corps pur diphasé : (P, T), (P, v), titre, composition en un point de (P, v) | changement §1, §3 | 🔶 | Pas de diagramme (P, v) ni de règle des moments ; Clausius-Clapeyron (hors programme) à la place |
| 3.2-3.4 Transformations, travail, 1ᵉʳ principe, H, calorimétrie, 2ᵉ principe, Boltzmann, Laplace | thermo2 §1-6, thermo3 §1-3, §5 | ✅ | |
| 3.3 Enthalpies de changement d'état, bilans | changement §2, §4 | ✅ | Notées L (« chaleur latente ») et non Δh₁₂ |
| 3.4 Δh₁₂ = T Δs₁₂ | Aucun chapitre | ❌ | L'encadré de `changement` le renvoie à la 2ᵉ année |
| 3.5 Machines dithermes, Carnot, rendements réels, cogénération | machines §1-4 | 🔶 | Cogénération absente ; conventions de signe incohérentes |
| 4.1.1 Système physico-chimique (fraction molaire, pression partielle, grandeurs intensives et extensives) | Aucun chapitre | ❌ | P_i est employée dans les activités sans être définie |
| 4.1.1 Avancement, activité, Q_r, K°, critère d'évolution, état final | equilchim §1, §3 | ✅ | §2 hors programme (Le Chatelier, Van 't Hoff, K_p) |
| 4.1.2 Cinétique : ordres 0, 1, 2, méthodes, demi-vie, dégénérescence, Arrhenius | cinetique §1-3 | ✅ | |
| 4.2.1 Lewis, valence, écarts à l'octet, ordres de grandeur des liaisons, polarité | molecules §1, §3, atome §3 | 🔶 | Écarts à l'octet et ordres de grandeur (longueurs, énergies) absents |
| 4.2.2 Van der Waals, liaison H, solvants, miscibilité, solubilité | molecules §4-5 | ✅ | |
| 4.3 Cristal parfait, CFC, sites interstitiels, compacité, masse volumique, types de solides | cristallin §1-4 | 🔶 | Amorphe, allotropie, rayons (covalent, ionique, de van der Waals) et limites du modèle absents |
| 4.4.1 Acide-base : Ka, prédominance, distribution, acides usuels, combinaisons de K, état final | acidobase §1-2 | 🔶 | Combinaison linéaire des constantes absente ; §3 (calculs de pH) hors programme |
| 4.4.1 Précipitation : Ks, s, condition de précipitation, domaine d'existence, courbes s = f(variable) | precipitation §1-4 | 🔶 | Pas de courbe log s = f(pH) |
| 4.4.2 Nombre d'oxydation, pile, Nernst, K°, dismutation, diagrammes E-pH | oxred §1-5, eph §1-6 | ✅ | Électrodes de référence autres que l'ESH absentes ; thiosulfate et hypochlorite absents |

## 2. Manques importants, par fréquence aux concours PT

1. **Mesures et incertitudes** : questions présentes dans les écrits et omniprésentes à l'oral de TP ; le bloc est absent du site.
2. **Changements d'état** : le diagramme (P, v) avec le titre par la règle des moments et Δs = Δh/T sont exigibles en PTSI. Le site les renvoie en 2ᵉ année, alors que c'est la base de la thermodynamique industrielle de PT.
3. **Induction** : courants de Foucault, moteur à courant continu à entrefer plan, spire tournante (alternateur), champ tournant, inductance mutuelle de bobines coaxiales, circuits couplés. La conversion électromécanique est un sujet classique de PT. Le contenu 1.7.1 et 1.7.2 est dispersé dans un chapitre « aperçu ».
4. **Chimie des solutions et cristallographie**, très fréquentes en PT, sont minces : `acidobase` a 3 méthodes et 3 exercices, `precipitation` 2 méthodes, `cristallin` 2 méthodes et 3 exercices. Il manque la réaction prépondérante et l'état final, les combinaisons de K, les courbes de solubilité, les rayons et les limites du modèle.
5. **Interférences à deux ondes** (acoustiques et Young) : traitées sous un encadré qui les dit hors programme, et sans cours pour les ondes mécaniques.
6. **Capacités numériques** : méthode d'Euler, résolution d'ED non linéaires (pendule), trajectoires en champ central, état final d'une réaction.
7. **Électrocinétique de base** : condition de l'ARQS, ordres de grandeur, résistances d'entrée et de sortie, circuits à deux mailles du 1ᵉʳ ordre.
8. **Mécanique** : coordonnées sphériques et déplacement élémentaire, système de points (p = m v(G)), chute avec frottement en cours (vitesse limite, équation adimensionnée).
9. Points secondaires : gaz réels et isothermes d'Amagat, cogénération, milieux dispersifs, description d'un système chimique (fraction molaire, pression partielle), écarts à l'octet, ordres de grandeur des liaisons.

## 3. Hors-programme présenté comme exigible ; doublons

**Hors-programme sans signalement** (rien n'indique qu'il ne s'agit pas du programme) :

- `atome` §1-2 : les quatre nombres quantiques, Pauli, Klechkowski, Hund, et des « exceptions à connaître » (Cr, Cu). Le programme de PTSI ne demande que le nombre d'électrons de valence des blocs s et p d'après la position dans le tableau.
- `molecules` §2 : la méthode VSEPR (AXₙEₘ), la charge formelle, la mésomérie. Le programme fournit la géométrie.
- `equilchim` §2-3 : Le Chatelier, Van 't Hoff, ΔrG° = −RT ln K (2ᵉ année), K_p = K_c(RT)^Δn (notation abandonnée). Deux des quatre méthodes et la moitié des exercices portent sur ces notions.
- `thermo3` §4 : les identités thermodynamiques, présentées comme « à connaître par cœur ». C'est le 1.2 de PT ; en PTSI, l'expression de S est fournie. `changement` §2 : Clausius-Clapeyron.
- `ondes` : d'Alembert (le programme exclut toute équation d'onde), ondes stationnaires, modes propres, décibels, Doppler, cône de Mach. La moitié des méthodes y est consacrée.
- `signaux` : calcul des coefficients de Fourier (le programme dit « décomposition fournie »), THD, puissance active U·I·cos φ.
- `cinept` §4 (composition des vitesses) et `mecpt` §2 (lois de Coulomb du frottement solide) : relèvent du programme de SI.
- `mcinc` §2 : théorème de Huygens-Steiner (le moment d'inertie est fourni en physique).
- `oxred` §5 (électrolyse) et `eph` §6 (corrosion, passivation) : programme de 2ᵉ année.
- `thermo2` : méthode « Joule-Thomson » (2ᵉ année).
- `optique` §2 : « Programme PTSI : … calculer le grossissement pour une lunette ou un microscope ». Le programme ne cite ces instruments qu'en exemples laissés au choix de l'enseignant.
- `acidobase` §3 : le texte rappelle qu'aucune formule de pH n'est exigible, mais la méthode 1 (« Calculer le pH d'une solution »), l'exercice 1 et quatre cartes entraînent ces formules.

**Hors-programme correctement signalé** : `chcentral` §4 (Binet), `mcinc` §4 (gyroscope), `cinetique` §4 (mécanismes), `estat`, `fluides`, `fluiddyn`.

**Encadrés faux ou contradictoires** :

- `optiqued` : « L'optique ondulatoire (interférences, …) n'est pas au programme de PTSI ». C'est faux pour Young, le chemin optique et la formule de Fresnel (1.6). Le reste du chapitre (diffraction, réseau, lames minces, anneaux de Newton) est bien hors programme en PTSI.
- `fluiddyn` : « En 1ʳᵉ année, seule la statique des fluides […] est au programme ». Cela contredit `fluides` (« n'est pas au programme de PTSI »), qui a raison.
- `changement` et `emag` sont traités comme des aperçus alors qu'une grande partie de leur contenu est exigible en PTSI (3.1, 3.3, 3.4 ; 1.7.1, 1.7.2).

**Doublons** :

- **optgeo et optique** : complémentaires (bases, puis lentilles et instruments). Ce n'est pas un vrai doublon, seuls stigmatisme et conditions de Gauss sont présentés deux fois. On peut garder les deux chapitres.
- **regimecontinu, premierordre et rlc** : `rlc` §1 refait les dipôles, les continuités et les énergies ; « la moitié de l'énergie est dissipée » figure dans `premierordre` §3 et dans `rlc` §4 ; les impédances complexes sont exposées trois fois (`rlc` §5, `filtres` §1, `signaux` §4). `premierordre`, trop mince, gagnerait à absorber ce socle commun.
- **thermo1, thermo2, thermo3** : pas de doublon réel, ils suivent 3.1, puis 3.2-3.3, puis 3.4. Restent des chevauchements : les lois de Joule et C_V (`thermo1` §5 et `thermo2` §5), les causes d'irréversibilité et le thermostat (`thermo2` §1 et `thermo3`). `thermo3` §4 double aussi `thermodiff` (2ᵉ année).
- **Oscillateur amorti** : traité trois fois (`rlc` §3-6, `oscill` §6-7, `energie` §4), avec des τ différents (voir §4).
- **mcinc** : son §2 (rotation, J, tableau de J) double `mvtsolide` §1-2, et son §3 (Kepler) double `chcentral` §1-2. Ses exercices (pendule, satellite) aussi.
- **Divers** : la force de Lorentz est dans `mecpt` §2 et dans `lorentz` ; la statique des fluides est dans `fluides` et `fluidstat` (2ᵉ année), choix assumé.

## 4. Qualité

**Chapitres les plus minces** (signes de cours / méthodes / exercices) : `premierordre` 1 826 / 2 / 3 ; `precipitation` 2 954 / 2 / 4 ; `machines` 3 141 / 4 / 8 ; `regimecontinu` 3 317 / 2 / 4 ; `cinept` 3 632 / 4 / 7 ; `equilchim` 3 725 / 4 / 7 ; `changement` 3 762 / 4 / 7 ; `atome` 3 932 / 3 / 4 ; `acidobase` 3 945 / 3 / 3 ; `cristallin` 4 778 / 2 / 3 ; `mvtsolide` 4 792 / 2 / 3.

Huit cours n'ont aucune figure (dont `rlc`, `thermo1`, `thermo3`, `mcinc`, `equilchim`). Les exercices « Concours PT » de 1ʳᵉ année font souvent deux ou trois questions, loin du format réel.

**Erreurs et incohérences relevées** :

1. **`lorentz` §2** : « δ_y = qUL²/(4mdv₀²) = UL²/(4dU_acc) ». La première expression est fausse d'un facteur 2 : c'est qUL²/(2mdv₀²). Les deux membres sont donc incompatibles. Même erreur sur la carte `lor` n° 6.
2. **`thermo1` §1** : « échelle microscopique : 1 μm ou moins » et « mésoscopique : ≈ 1 mole, soit ≈ 1 cm³ pour un gaz ». C'est faux : l'échelle microscopique est de l'ordre de 0,1 à 1 nm ; un volume mésoscopique fait de l'ordre de 1 µm³ et contient de 10⁷ à 10⁹ molécules ; une mole de gaz occupe environ 24 L. Même erreur sur la carte `thermo1` n° 4.
3. **Vm ≈ 22,4 L/mol « à 0 °C et 1 bar »** (`thermo1` §5, `constantes` §2, cartes `thermo1` n° 29 et `cst` n° 15). 22,4 L/mol est la valeur à 1 atm ; à 1 bar, c'est 22,7 L/mol. La carte `cst` donne d'ailleurs 24,8 L/mol à 25 °C, valeur cohérente avec 22,7.
4. **`mecpt` §1** (et la carte correspondante) : « référentiel géocentrique : galiléen pour des durées ≪ 1 jour ». Il faut ≪ 1 an ; c'est le référentiel terrestre qui est limité à ≪ 1 jour.
5. **`chcentral` §1** : « L = mr²θ̇ = C = cste (moment cinétique par unité de masse) ». Confusion : L = mC.
6. **`machines`** : trois conventions de signe dans le même chapitre. Le §4 écrit « W = −∮P dV, positive si le cycle est parcouru dans le sens horaire (moteur) », alors qu'avec W reçu un moteur a W < 0 ; le §1 écrit W = Q_c + Q_f (travail fourni) ; le §3 écrit Q_c − Q_f (en valeurs absolues).
7. **Carte `ind` n° 21** : « RL en charge : moitié stockée dans L, moitié dissipée ». C'est le résultat du circuit RC. Dans un circuit RL en régime établi, l'énergie fournie et l'énergie dissipée croissent sans borne.
8. **`optique` §2** : la « configuration afocale » est présentée comme commune au microscope et à la lunette. Le microscope n'est pas afocal.
9. **`ondes` §1** : « Toute onde se propageant à la célérité c satisfait l'équation de d'Alembert ». Ce n'est vrai qu'en milieu non dispersif à une dimension.
10. **`oscill` §7** : le pont de Tacoma est présenté comme une résonance forcée. C'est contesté (instabilité aéroélastique) ; à nuancer.
11. **Carte `sig`** : le THD est présenté comme un « rapport de puissances », alors que la formule donnée est un rapport de valeurs efficaces.
12. **Imprécisions mineures** : `cinetique` §2, « Durée de vie : t₁/₂ » à l'ordre 0 (lire « temps de demi-réaction ») ; `cristallin` §1, la maille définie comme « le plus petit parallélépipède » (maille primitive, ce qui exclut la CFC conventionnelle) ; `induction` §5, « Ri = −dΦ/dt = Blv » sans convention d'orientation, que le programme exige ; carte `cc`, « T = 24 h » contre « jour sidéral » dans le cours.

**Notations incohérentes entre chapitres** :

- **τ d'amortissement** : τ = 2Q/ω₀ avec une enveloppe en e^(−t/τ) (`rlc`, `oscill`), mais τ = m/α avec une enveloppe en e^(−t/2τ) (`energie` §4, et sa carte n° 25).
- **ξ** désigne l'amortissement (`energie` §4, SI) et l'avancement (`equilchim`, `cinetique`).
- **L** désigne l'inductance, le moment cinétique (`mcinc`, `chcentral`) et la chaleur latente (`changement`). Le programme note l'enthalpie de changement d'état Δh₁₂.
- **C** désigne la capacité, la constante des aires (`chcentral`) et le couple (`mcinc` §4).
- **Entropie** : S_e et S_c en 1ʳᵉ année ; S_créée en 2ᵉ année ; S_éch et S_créé dans le programme.
- **Constantes d'équilibre** : K° sans dimension (`equilchim` §1, `oxred`) mais K_c et K_p dimensionnées (`equilchim`) ; Ka, Ks et Ke écrites sans c° (`acidobase`, `precipitation`). Le même deck `eq` donne K_c dimensionnée puis « K° sans unité ».
- **Moments** : \vec{M}_O dans `mcinc`, 𝓜_Δ dans `mvtsolide` ; les tableaux de moments d'inertie diffèrent entre ces deux chapitres.

**Méthodes, exercices, cartes** :

- Tous les exercices ont un corrigé (222 sur 222).
- `ondes` et `equilchim` consacrent l'essentiel de leurs méthodes à du hors-programme.
- `constantes` n'a ni méthode ni exercice, ce qui est normal pour une fiche.
- Je n'ai pas relevé de carte fausse en dehors de celles citées plus haut (`lor` n° 6, `thermo1` n° 4 et n° 29, `cst` n° 15, `mp` référentiel géocentrique, `ind` n° 21).

## 5. Recommandations, par priorité

1. **Corriger les erreurs factuelles et les encadrés faux.** Erreurs et cartes du §4 (points 1 à 9) ; encadré de `optiqued` (Young au programme) ; encadré de `fluiddyn` ; mention « Programme PTSI » de `optique`. Retoucher le texte d'une carte sans changer sa longueur ni sa place ne fait perdre aucune progression. **Petite.**
2. **Créer un chapitre « Mesures et incertitudes ».** Types A et B, composition, écart normalisé, régression, Monte-Carlo en Python. Ajouter les capacités numériques du programme dans les chapitres concernés (Euler dans `premierordre`, pendule non linéaire, champ central, état final chimique). **Moyenne à grande.**
3. **Compléter la thermodynamique de 1ʳᵉ année.** `changement` : diagramme (P, v) calculé, titre et règle des moments, Δs = Δh/T, notation Δh, sans renvoi en 2ᵉ année. `thermo1` : gaz réels et isothermes d'Amagat. `machines` : conventions de signe unifiées, cogénération, ordres de grandeur des rendements. **Moyenne.**
4. **Restructurer l'électromagnétisme de 1ʳᵉ année.** Rassembler le contenu PTSI de `emag` (cartes de champ, ordres de grandeur, symétries, moment magnétique, couple, boussole, champ tournant) dans `induction` ou dans un chapitre « Champ magnétique et actions de Laplace ». Y ajouter la spire tournante, les courants de Foucault, le moteur à courant continu à entrefer plan et l'inductance mutuelle de bobines coaxiales. `emag` resterait un pur aperçu d'Ampère. **Moyenne à grande.**
5. **Recentrer les ondes et les interférences sur le 1.6.** `ondes` : f(t − x/c), milieux dispersifs, interférences à deux ondes en cours ; d'Alembert, ondes stationnaires et Doppler en « pour aller plus loin ». `optiqued` : Young et Fresnel au programme, le reste en fin de chapitre. **Moyenne.**
6. **Étoffer les chapitres minces** (cible : environ 6 méthodes et 7 exercices). `premierordre` et `regimecontinu` : ARQS, ordres de grandeur, deux mailles, résistances d'entrée et de sortie. `acidobase` et `precipitation` : réaction prépondérante, combinaisons de K, courbes de solubilité. `cristallin` : amorphe, rayons, limites du modèle. Puis `mvtsolide`, `cinept` (sphériques) et `mecpt` (système de points, chute avec frottement). **Grande.**
7. **Appliquer le format de la 2ᵉ année** : encadré « Au programme · PTSI » en tête, hors-programme regroupé en fin de chapitre. Chapitres concernés : `atome` (nombres quantiques, Klechkowski), `molecules` (VSEPR), `equilchim` §2, `thermo3` §4, `signaux` (coefficients de Fourier, THD), `cinept` §4, `acidobase` §3, `oxred` §5, `eph` §6. **Moyenne.**
8. **Harmoniser les notations** (τ, ξ, S_éch et S_créé, Δh, K° avec c°, moments) **et alléger les doublons** : socle commun des dipôles et impédances ; oscillateur amorti exposé une fois avec renvois ; `mcinc` recentré sur le point matériel avec renvois vers `mvtsolide` et `chcentral`. **Petite à moyenne.**
