# Revue du chapitre `rlc` (prefix `rlc`) — « Circuit RLC série » — 2026-11-22

Objet (point 4 de l'audit, lot 8 ; `docs/audit-2026-11/physique-1a.md` l. 26, 103, 105, 113, 132 ; `flt-revue.md`,
« À faire dans les chapitres hors de ma mission » ; `osc-revue.md`, « ω_p ») : cours de 16 300 signes sans figure, 5 méthodes,
7 exercices + 1 « Concours PT » de 5 questions, 26 cartes ; socle des dipôles et des impédances refait (`premierordre`,
`filtres`), oscillateur amorti exposé deux fois (`oscill`). Programme : PTSI 2021, partie 1.4 « Oscillateurs libres et
forcés » (l. 744-795), côté électrique, et annexe « outils numériques » (odeint).

## Décisions
- **Socle commun renvoyé** : dipôles, continuités, énergies → `premierordre` §1-§2 (rappel d'une formule) ; notation
  complexe, impédances, associations, diviseurs, Fresnel → `filtres` §1-§3 ; le §5 ne garde que l'**impédance du RLC
  série** (forme réduite \(R[1+jQ(x-1/x)]\), module, argument, comportements, figure calculée) et son application.
- **Oscillateur amorti** : notations de `oscill` (\(\omega_0\), \(Q\), \(\tau=2Q/\omega_0=2L/R\), pseudo-pulsation
  \(\omega_p\), \(T_p\), décrément \(\delta\)) ; polynôme et durée du transitoire renvoyés à `oscill` §6-§7 ; le RLC garde
  ce qui lui est propre : conditions initiales par les continuités, résistance critique, courant, premier dépassement exact,
  impédance, surtension, bilan de puissance, mesures en TP (GBF, masses, résistances parasites), simulation.
- **Numérotation** conservée pour les renvois existants : `oscill` §5 → §2, `oscill` §7 → §4, `filtres` §7 → §6
  (résonance en intensité et surtension). Le panneau `rlc-simu` n'est pas modifié ; ses réglages par défaut (20 Ω, 50 mH,
  10 µF) servent d'exemple fil rouge (Q = 3,54, ω_p = 1 400 rad/s, √(4Q²−1) = 7 exactement).
- `rlc` est le seul chapitre non replié dans le site : les `.src.html` sont des panneaux ordinaires (1ʳᵉ ligne identique),
  à intégrer sans repli (`replier_panneaux.py` laisse `chap-rlc` de côté).

## Fichiers produits (dans `AN1/`)
- `rlc-cours.src.html` (87 ko ; 39 600 signes de texte contre 16 300) — assemblé par `rlc_construire.py` depuis
  `rlc-cours.tpl.html`, `rlc_figs.json` et `rlc_code_cours.py` (code coloré et sa sortie réelle, exécutée à l'assemblage) ;
- `rlc-meth.src.html` (10 méthodes, 3 pièges) ; `rlc-exos.src.html` (11 exercices + « Concours PT », depuis `rlc-exos.tpl.html`) ;
- `rlc-cartes-corr.json` (4 réponses corrigées) ; `rlc-cartes-ajout.js` (15 cartes) ;
- scripts : `rlc_figs.py` (10 figures, dont 1 d'exercice), `rlc_calculs.py` (cours, sympy + odeint), `rlc_calculs_meth.py`,
  `rlc_calculs_exos.py`, `rlc_code_cours.py`, `rlc_construire.py`, `rlc_voir.py`, `rlc_cartes_rendu.js` ; copies
  `rlc_orig_{cours,meth,exos}.html`.

## Erreurs trouvées et corrigées
| Où | Problème | Correction |
|---|---|---|
| Ancien EXO 02 | \(\omega_p\approx3\,081\) rad/s, \(B\approx3{,}25\) V, \(T\approx2{,}04\) ms : faux (\(Q^2=2{,}5\), donc \(\omega_p=\omega_0\sqrt{0{,}9}=3\,000\) rad/s) | \(\omega_p=3\,000\) rad/s, \(B=10/3\) V, \(T_p=2{,}09\) ms ; solution vérifiée par odeint (écart 2·10⁻¹⁰) |
| Ancien EXO 03 | \(\omega_0=10^4\) rad/s avec \(L=20\) mH, \(C=50\) nF (en fait \(LC=10^{-9}\), \(\omega_0=3{,}16\times10^4\)) ; donc \(Q=4\) faux (12,6) ; \(\Delta\omega=2\,500\) juste par hasard | corrigé ; question « montrer \(\Delta\omega=R/L\) » et surtension (63 V) ajoutées |
| Ancien cours §4 | premier dépassement \(\approx e^{-\pi/(2Q)}\) « au voisinage de \(T_0/2\) » ; durée « 5τ à 1 % » seule | valeur exacte \(D=e^{-\pi/\sqrt{4Q^2-1}}\) atteinte exactement en \(T_p/2\) (démontrée) ; durée alignée sur `oscill` §7 (≈ 3τ à 5 %) |
| Ancien cours §3, carte 6 | apériodique « retour monotone » | « au plus un passage par la valeur finale » (comme `oscill`) |
| Cours §3-§4, cartes | pseudo-pulsation notée \(\omega\), comme la pulsation du générateur | \(\omega_p\), \(T_p\) (carte 7 : réponse seule) |
| Ancien cours §5, carte 19 | \(Q=2\pi\,\mathcal E/\Delta\mathcal E\) sans condition | exact en régime forcé à \(\omega_0\) (démontré), approché en régime libre si \(Q\gg1\) |
| Ancien EXO 05, carte 18 | « \(U_{C,\max}=100\) V » confondu avec \(U_C(\omega_0)\) ; « \(U_C(\omega_0)\approx QE_m\) pour Q grand » | \(U_C(\omega_0)=QE_m\) exactement pour tout Q ; le maximum en diffère de 10⁻⁵ ici |
| Ancien cours | §1 refait dipôles et continuités ; §5 refait notation complexe et impédances | renvois à `premierordre` et `filtres` |

## Couverture du programme : avant → après
| Capacité (PTSI 1.4, côté électrique) | Avant | Après |
|---|---|---|
| Circuit LC : équation, solution par les CI, grandeurs | absent | §1 (équation, solution, énergie, exemple chiffré), carte |
| Forme canonique, \(\omega_0\), \(Q\) | §2 | §2 (figure du circuit orienté, équation en \(u_C\), \(q\), \(i\), ordres de grandeur, piège \(Q\) à l'envers), méthode 1, EXO 01 |
| Nature de la réponse selon Q ; réponse détaillée (racines) en régime libre ou pour un échelon | §3-§4 | §3 (résistance critique, CI à \(0^+\), \(i(t)\), figure des trois régimes calculée), §4 (trois régimes, \(i(t)\), dépassement exact, figure tension et courant), méthodes 2-4, EXO 01, 02, 06, 08, cartes |
| Durée du transitoire selon Q | « 5τ » | §4 (3τ, \(3/(Q\omega_0)\), \(4{,}7/\omega_0\) ; renvoi `oscill` §7), méthode 2 |
| Stockage et dissipation ; prévoir par l'énergie | §7 (bilan esquissé) | §4 (bilan de la charge), §7 (bilan de puissance, régime libre, régime forcé, \(Q\) énergétique exact à \(\omega_0\), figure des énergies calculée), méthode 5, EXO 07, concours C, 2 cartes |
| Impédances ; représentation complexe du régime forcé | §5 (triple emploi) | §5 (impédance du RLC seule, figure module-argument), renvoi `filtres` §1-§3, méthode 6, carte |
| Acuité de la résonance et Q ; ω₀ et Q sur graphes d'amplitude et de phase | §6 | §6 (intensité et tension, phase ±45°, \(f_1f_2=f_0^2\), deux figures calculées), §9, méthodes 7-8, EXO 03, 05, 08, 10, cartes |
| Similitude des oscillateurs | absent | §8 (tableau, jumeaux numériques), carte |
| Relevés expérimentaux ; acquisition d'un transitoire ; caractériser une résonance | méthode 5 | §9 (montage, masses, créneau, GBF 50 Ω et bobine, figure calculée, décrément, Lissajous, deux exemples), méthodes 8-9, EXO 09, 10, cartes |
| Capacité numérique (odeint, Euler, ordre 2) | absent | §10 (programme exécuté : établissement du régime forcé, Euler d'ordre 1 comparé), méthode 10, EXO 11, concours D, carte |

## Contenu
**Cours** (« AU PROGRAMME · PTSI » + 10 sections + « Pour aller plus loin ») : §1 Dipôles et oscillateur LC ; §2 Mise en
équation ; §3 Régime libre ; §4 Réponse à un échelon ; §5 Régime sinusoïdal forcé (impédance du RLC) ; §6 Résonances ;
§7 Aspects énergétiques ; §8 Analogie électromécanique ; §9 Exploiter des relevés expérimentaux ; §10 Simulation numérique ;
hors programme : \(\omega_r\) et \(U_{C,\max}\) exacts, circuit bouchon, puissance moyenne et facteur de puissance.
10 exemples traités chiffrés, 10 notices, 1 tableau, 9 figures calculées : circuit orienté ; trois régimes libres
(20, 141, 400 Ω) ; échelon (\(u_C\) et \(i\), dépassement, bande ±5 %) ; \(|\underline Z|\) et \(\arg\underline Z\) ;
résonance en intensité (amplitude, phase, bande passante) ; \(U_C/E_m\) pour 4 valeurs de Q ; énergies en régime libre ;
créneau de GBF avec et sans résistances parasites ; sortie du programme Python. Vérifiées en clair et en sombre.

**Méthodes** (10) : équation et identification ; régime et résistance critique ; conditions initiales ; régime libre ou
échelon ; bilan d'énergie ; impédance et courant ; résonance ; mesures ; dimensionner avec les résistances parasites ;
simuler. Les 5 anciennes méthodes et leurs pièges sont repris.

**Exercices** (11 + concours) : 01-07 anciens, corrigés et complétés d'une question chacun ; 08 ancien « Concours PT »
(question sur le dépassement et la puissance ajoutée) ; 09 exploiter un enregistrement de TP (décrément, \(L\), \(r\) de la
bobine, GBF) ; 10 lire une courbe de résonance mesurée (phase, bande passante, \(r\), \(L\), \(C\)) ; 11 simuler la réponse
indicielle avec odeint (programme exécuté : `0.998 3.468`) ; **Concours PT « Le circuit de décharge d'un défibrillateur »**
(A énergie et charge ; B décharge, résistance critique, \(i_{\max}=U_0\sqrt{C/L}/e\approx47\) A ; C énergie reçue par le
patient \(R/(R+r)\), rôle de la bobine ; D simulation, tableau calculé pour 25 à 150 Ω, impulsion biphasique).

**Cartes** : 4 réponses corrigées (questions inchangées : 6, 7, 18, 19) ; 15 ajoutées à la fin (résistance critique, CI,
courant de l'échelon, dépassement, impédance réduite, phase en bande passante, pourquoi deux résonances, bilan de puissance,
énergies, résistances parasites, décrément, Lissajous, système pour odeint, analogie, ordres de grandeur). Deck : 26 → 41.
Rendu MathJax contrôlé (`rlc_cartes_rendu.js`, aucune erreur ; une question reformulée pour éviter « ordre \(1\) »).

## Contrôles
`verif_src.py` (3 fichiers) : aucune erreur ni « attention ». `apercu_src.py` à 390 et 1440 px pour les trois panneaux :
`merr`, `brut`, `larges` vides, `scrollW` égal à la largeur, aucune erreur JS ; captures du cours relues. Cartes :
`corriger_cartes.py rlc … --essai` (4) et `ajouter_cartes.py rlc … --essai` (26 → 41) sans erreur. Tous les nombres
recalculés (sympy pour les solutions exactes, odeint pour les durées, maximums et le tableau du défibrillateur).

## Notations
\(\omega_0=1/\sqrt{LC}\), \(Q=\tfrac1R\sqrt{L/C}\), \(\tau=2Q/\omega_0=2L/R\), \(\omega_p\), \(T_p\), \(D\) (premier
dépassement), \(\delta\), \(R_c=2\sqrt{L/C}\), \(x=\omega/\omega_0\), \(\underline Z\), \(\underline I_m\), \(\underline U_{Cm}\),
\(\underline E_m\) (comme `osc`, `flt`), \(\mathcal E\) énergie stockée, \(\langle\mathcal P_J\rangle\).

## Doutes et points pour l'intégration
- `oscill` §6 écrit encore « Le chapitre « Circuit RLC série » note la pseudo-pulsation \(\omega\) » : à remplacer
  (le RLC note désormais \(\omega_p\)). `oscill`, bloc « Au programme » : « Les impédances complexes et la résonance du
  circuit RLC sont traitées dans « Circuit RLC série » » → « impédances : « Régime sinusoïdal forcé et filtrage linéaire »,
  §1-§3 ; résonance du RLC : « Circuit RLC série », §6 » (déjà signalé par `flt-revue.md`).
- Questions des cartes 7 et 18 inchangées (« pseudo-pulsation ω », « pour un Q élevé ») : réponses corrigées seulement.
- La carte 24 (« environ 5τ, 1 % ») est juste pour le pseudo-périodique ; laissée telle quelle.
- L'exemple Lissajous et les valeurs « typiques » (GBF 50 Ω, bobine 10-20 Ω) sont des ordres de grandeur de TP.
- Le défibrillateur est un modèle pédagogique (onde de Lown) ; les appareils actuels sont biphasiques et pilotés.
