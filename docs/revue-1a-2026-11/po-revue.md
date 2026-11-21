# Revue du chapitre `premierordre` (prefix `po`) — « Circuit linéaire du premier ordre » — 2026-11-21

Objet (audit 2026-11-14, `docs/audit-2026-11/physique-1a.md` §1, §2 points 6 et 7, §4, §5 points 2 et 6) : le chapitre le
plus mince de la physique (1 826 signes de cours, 2 méthodes, 3 exercices, 11 cartes). Manquaient : condensateur et bobine
comme dipôles (ordres de grandeur, énergies, démonstration des continuités), régime libre RL, circuits à deux mailles,
bilan énergétique au-delà du seul RC, lecture d'un relevé, et la capacité numérique « méthode d'Euler ». Programme : PTSI
2021, partie 1.3 et fin de 1.2 (`pdf-pt/prog/ptsi.txt`, l. 676-737).

## Fichiers produits (dans `AN1/`)
- `po-cours.src.html` (94 ko, 29 500 signes de texte hors figures) — assemblé par `po_construire.py` depuis
  `po-cours.tpl.html` et `po_figs.json` ;
- `po-meth.src.html` (10 méthodes), `po-exos.src.html` (11 exercices + 1 « Concours PT », assemblé depuis `po-exos.tpl.html`) ;
- `po-cartes-corr.json` (vide : aucune carte fausse), `po-cartes-ajout.js` (14 cartes) ;
- scripts : `po_figs.py` (12 figures, utilise `rco_svg.py`), `po_euler.py` (**tout le code Python du chapitre, exécuté et
  testé** : cours §9, EXO 10, concours D, figure de la sinusoïde), `po_calculs.py` (exemples du cours, vérifications sympy :
  `dsolve`, bilan RL symbolique), `po_calculs_exos.py` (exercices), `po_construire.py` ; aperçu des figures et rendu des cartes
  par `rco_voir.py` et `rco_cartes_rendu.py` ; copies des anciens panneaux : `po_orig_{cours,meth,exos}.html`.

## Erreurs trouvées et corrigées
| Où | Problème | Correction |
|---|---|---|
| Cours (ancien) | continuités affirmées sans justification ; « régime permanent à 5τ » seul repère | démonstrations énergétiques (§1, §2) ; temps de réponse à 5 % \(t_{5\%} = \tau\ln 20 \approx 3\tau\) (§6) |
| Cours §3 (ancien) | « la moitié de l'énergie dissipée » sans dire que c'est propre au RC (l'audit relève la carte `ind` n° 21 qui le transpose au RL) | §8 : bilan RC et bilan RL séparés, notice « Erreur classique », EXO 09 qui réfute l'affirmation |
| Ancien concours RL, A2 | « la bobine se comporte en coupe-circuit » | « se comporte un instant comme un interrupteur ouvert » |
| Ancien concours cycle, B1 | origine des temps et orientation de \(i\) implicites à la décharge | précisées ; charge « terminée » : 3τ à 5 %, 5τ à 1 % |

Les deux anciens « Concours PT » (justes) deviennent EXO 05 et EXO 11 ; un seul « Concours PT » par chapitre. Les 11 cartes
sont justes : aucune correction (fichier de corrections vide).

## Couverture du programme : avant → après
| Capacité exigible | Avant | Après |
|---|---|---|
| Relations i-u du condensateur et de la bobine (1.2) | formules au §3 | §1, §2 (figure des trois dipôles, bobine réelle), méthode 1, EXO 02, 2 cartes |
| Ordres de grandeur de L et C (1.2) | absent | §1, §2 (tableau, exemples, supercondensateur), 2 cartes `val` |
| Énergie stockée (1.2) | formules | §1, §2 (démonstrations), EXO 02-03, carte |
| Continuité de \(u_C\) et de \(i_L\) | une phrase | §1, §2 (démonstrations, étincelle de rupture), méthode 2, EXO 03, 06, 08, carte |
| ED d'un circuit à une ou **deux mailles** | une maille, forme canonique | §3, §4, §5 ; **§7 deux mailles** (loi des nœuds, raccourci de Thévenin, figure calculée), méthodes 4 et 6, EXO 07, 08, concours A, 2 cartes |
| Réponse en régime libre ou à un échelon | charge RC, établissement RL | §3 (charge), §4 (décharge, demi-vie, échelle log), §5 (RL : échelon **et régime libre**, protection d'un relais), §6 (solution générale), méthode 5, EXO 01, 04-08 |
| Durée du régime transitoire ; transitoire / permanent sur un relevé ; acquisition | « 5τ, 1 % » | §6 (t à 5 %, 63 %, tangente, régression en log, protocole en créneaux, rôle des 50 Ω du GBF et de l'oscilloscope), méthode 7, EXO 04, 3 cartes |
| Bilan énergétique | phrase sur RC | §8 (bilan de puissance RC et RL, figure calculée des énergies, deux exemples), méthode 8, EXO 09, 11, concours B-C, carte |
| **Méthode d'Euler** pour une excitation quelconque (capacité numérique) | absent | §9 (schéma, programme Python testé, validation sur l'échelon, stabilité, réponse à une sinusoïde calculée, deux figures), méthodes 9-10, EXO 10 (rampe), concours D (charge progressive), 2 cartes ; renvoi au chapitre d'informatique `pynum` « Méthodes numériques » (§6, exercice 09), qui renvoie déjà à ce chapitre ; même fonction `euler(F, t0, y0, h, n)` |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 9 sections) : §1 Le condensateur ; §2 La bobine ; §3 Circuit RC soumis à un
échelon ; §4 Régime libre du circuit RC ; §5 Circuit RL : établissement et rupture ; §6 Méthode générale et durée du
régime transitoire ; §7 Circuits à deux mailles ; §8 Bilans d'énergie ; §9 Simulation numérique : méthode d'Euler. Pas de
« Pour aller plus loin » : tout est au programme. 11 exemples traités chiffrés (au moins un par section), 8 notices
« Erreur classique », 8 figures SVG calculées (dipôles ; charge RC avec 63 %, 95 % et zone permanente ; décharge et droite
en log ; RL établissement puis extinction dans une résistance de protection ; deux mailles comparées au RC simple ; énergies
de la charge ; Euler pour deux pas ; réponse à une sinusoïde calculée par le programme du cours), vérifiées en clair et en
sombre.

**Méthodes** (10) : lois des dipôles et convention ; valeurs à \(0^+\) ; régime permanent ; ED et forme canonique ;
solution sans résoudre ; deux mailles (nœuds ou Thévenin) ; lire τ sur un relevé ; bilan énergétique ; simuler par Euler ;
choisir le pas et valider. Les 2 anciennes méthodes sont reprises (5 et 7).

**Exercices** (12) : EXO 01 charge (ancien) ; EXO 02 courant, tension, énergie ; EXO 03 valeurs initiales et finales
(figure) ; EXO 04 mesure de C par la décharge (régression, résistance d'entrée de la carte) ; EXO 05 RL (ancien concours) ;
EXO 06 contacteur et résistance de protection ; EXO 07 RC à deux mailles (figure) ; EXO 08 RL à deux mailles (figure) ;
EXO 09 bilan d'énergie du RL ; EXO 10 rampe par la méthode d'Euler (code) ; EXO 11 cycle charge-décharge (ancien concours) ;
**Concours PT** « Le condensateur d'un défibrillateur » (A charge à deux mailles, B résistance de sécurité, C choc tronqué,
D simulation d'une charge progressive par Euler, résultat 5,56 s vérifié par le calcul exact ; figure).

**Cartes** : 11 → 25 (14 ajoutées à la fin : relations de C et L, ordres de grandeur de C et L, continuité, \(t_{5\%}\),
régime libre RL, τ par la résistance vue, \(x(0^+)\) et \(x_\infty\), bilan RL, récurrence d'Euler, choix du pas, mesure de τ
en log, rôle des 50 Ω du GBF). Formules rendues sans erreur.

## Notations
\(u_C\), \(i_L\), \(u_L\), τ (constante de temps), \(\tau = RC\), \(\tau = L/R\), \(\tau = R_{\text{th}}C\), \(x(0^+)\),
\(x_\infty\), \(t_{5\%}\), \(\mathcal E_C = \tfrac12 Cu_C^2\), \(\mathcal E_L = \tfrac12 Li_L^2\) (comme `rlc`), \(W_E\),
\(W_J\), \(h\) (pas), \(t_k = kh\). Même signature Python que `pynum`.

## Doutes, remarques pour l'intégration
- **À alléger ailleurs** : `rlc` §1 « Les bases » refait §1-2 de ce chapitre (dipôles, continuités, énergies, mémo) : le
  réduire à un rappel renvoyant à « Circuit linéaire du premier ordre » ; `rlc` §4 « Vision énergétique » peut renvoyer au
  §8 ; `induction` §4 garde sa figure RL (point de vue de l'auto-induction) mais peut renvoyer au §5 pour la résolution ;
  la carte `ind` n° 21 (RL : « moitié stockée »), signalée fausse par l'audit, avait déjà été corrigée lors de la revue de
  l'électromagnétisme de 1ʳᵉ année (vérifié à l'intégration) ; l'EXO 09 et la carte « Bilan d'énergie d'un circuit RL » vont
  dans le même sens.
- La figure du §9 et l'exemple « réponse à une sinusoïde » anticipent le régime sinusoïdal forcé (amplitude \(E/\sqrt2\),
  retard \(\pi/4\)) : présentés comme un aperçu avec renvoi à « Filtres ».
- EXO 03 porte sur un circuit à deux éléments réactifs (second ordre) : seules les valeurs initiales et finales sont
  demandées, ce que l'énoncé dit.
- La carte ancienne n° 6 (« environ 5τ, écart inférieur à 1 % ») est juste ; le cours retient en plus \(3\tau\) à 5 %.
