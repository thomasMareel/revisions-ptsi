# Revue du chapitre `signaux` (prefix `sig`) — « Signaux périodiques et Fourier » — 2026-11-22

Objet (point 4 de l'audit, lot 7 ; `docs/audit-2026-11/physique-1a.md` l. 27, 84, 103, 155 ; `audit-2026-11.md` §3 n° 10
et §5) : cours de 6 100 signes, 5 méthodes (dont 2 hors programme), 7 exercices (dont 2 entièrement hors programme),
25 cartes ; calcul des coefficients de Fourier et THD au premier plan alors que le programme dit « décomposition
fournie » ; socle des impédances exposé une troisième fois (§4). Programme : PTSI 2021, partie 1.5 (l. 803-813,
« Signaux périodiques ») et capacités expérimentales (l. 323-336 : fréquences, analyse spectrale, déphasage ;
l. 346-359 : nature d'une mesure), plus « détecter le caractère non linéaire » (1.5, l. 848).

## Décision sur les doublons (socle des dipôles et impédances)
Le socle « notation complexe, impédances, associations, diviseurs » vit désormais **dans `filtres` §1 à §3** (exposé de
référence du site, voir `flt-revue.md`). L'ancien §4 « Signaux en régime sinusoïdal forcé » de `signaux` est
**supprimé** ; le cours y renvoie (bloc « Au programme », §1, §2). Les cartes d'impédance de `sig` (n° 12, 13, 14) sont
justes et restent (aucun retrait de carte) ; la n° 24 est réécrite en notation du site (\(\underline S_m\)).

## Fichiers produits (dans `AN1/`)
- `sig-cours.src.html` (77 ko ; 37 400 signes de texte contre 6 100) — assemblé par `sig_construire.py` depuis
  `sig-cours.tpl.html` et `sig_figs.json` ;
- `sig-meth.src.html` (10 méthodes), `sig-exos.src.html` (11 exercices + 1 « Concours PT », assemblé depuis
  `sig-exos.tpl.html`) ;
- `sig-cartes-corr.json` (10 réponses corrigées), `sig-cartes-ajout.js` (15 cartes) ;
- scripts : `sig_figs.py` (11 figures, dont 2 d'exercices ; spectres par `numpy.fft`), `sig_calculs.py` (cours),
  `sig_calculs_exos.py` (méthodes, exercices, concours ; sympy pour les intégrales), `sig_code_cours.py` (programme du
  §9 extrait du HTML et exécuté), `sig_cartes.py` (génère les deux fichiers de cartes), `sig_cartes_rendu.js` (rendu
  des cartes par `flashPretty` + MathJax), `sig_voir.py` (aperçu des figures en clair et en sombre), copies des anciens
  panneaux `sig_orig_{cours,meth,exos}.html`. Outils communs : `flt_svg.py` (schémas, Bode, simplification des tracés).
- Le chapitre n'a pas d'onglet Simulateur.

## Erreurs et défauts trouvés
| Où | Problème | Correction |
|---|---|---|
| Cours §2-3 (ancien) | calcul des coefficients, symétries, forme complexe \(c_n\), THD au cœur du cours ; le programme dit « décomposition fournie » | regroupés en « Pour aller plus loin · hors programme » ; le cours travaille sur \(S_0\), \(S_n\), \(\varphi_n\) fournis |
| Cours §3 (ancien) | « Un amplificateur … a un THD < 1% » : le « < » brut était lu comme une balise, la fin de phrase disparaissait | phrase réécrite (THD < 0,1 % pour un bon amplificateur audio ; 48 % pour un carré, calculé) |
| Cours §3 (ancien) | spectre « \(\lvert c_n\rvert\) ou \(\sqrt{a_n^2+b_n^2}/2\) » : demi-amplitude bilatérale, alors que la figure montrait des amplitudes | spectre en amplitude \(S_n\) (amplitude de l'harmonique) partout |
| Cours §4 (ancien) | troisième exposé des impédances, puissance active \(UI\cos\varphi\) (hors programme de physique) | supprimé ; renvoi à `filtres` §1-3 ; \(P = UI\cos\varphi\) en fin de chapitre, renvoyé à la SI (`triphase`) |
| Exercices 02, 03 (anciens) | solutions bâclées (« \((1-\cos n\pi)\times2/2\ldots\) », intégration par parties non menée) | fusionnés en EXO 11 (hors programme), calculs complets vérifiés avec sympy |
| Exercice 05 (ancien) | puissances active et réactive (hors programme) dans un exercice de RSF | exercice déplacé, sans les puissances, en `flt` EXO 01 |
| Exercice 06 (ancien) | THD (hors programme) | THD retiré ; question sur l'erreur « on ajoute les valeurs efficaces » (61 % d'erreur sur la puissance) |
| Méthodes 1-2 (anciennes) | consacrées au calcul des coefficients (hors programme) ; pièges sur la convergence de Fourier | remplacées par les savoir-faire exigibles (10 méthodes) |
| Carte 3 | « carré d'amplitude A : S_eff = A » sans préciser symétrique (un créneau 0/A a \(A/\sqrt2\)) | réponse précisée |
| Cartes 6, 7, 8 | symétries de Fourier sans mention hors programme | réponses préfixées « Hors programme en PTSI : » |
| Cartes 5, 11 | préfixe « Hors programme (pour aller plus loin) » | harmonisé : « Hors programme en PTSI : » ; THD réécrit avec \(S_n\) |
| Carte 10 | Parseval en \(a_n\), \(b_n\), \(c_n\) (notations hors programme) | énoncé du programme : somme des carrés des valeurs efficaces |
| Carte 20 | « le signal se lisse vers une sinusoïde » (faux si \(f_c \ll f\) : triangle) | trois cas selon la coupure |
| Carte 22 | Gibbs « environ 9 % » sans dire de quoi (c'est 9 % du saut, 18 % de \(E\) pour un carré \(\pm E\)) ; hors programme non signalé | précisé et préfixé |
| Carte 24 | « phaseur \(\tilde S\) » : notation absente du site | amplitude complexe \(\underline S_m\), comme `flt` et `osc` |
| Ancien « Concours PT » | deux parties de deux ou trois questions | gardé (juste) comme EXO 07, complété (part de la puissance, composante continue) ; nouveau concours en 4 parties |

## Couverture du programme : avant → après
| Capacité (PTSI) | Avant | Après |
|---|---|---|
| Caractériser un signal sinusoïdal (amplitude, phase, période, fréquence, pulsation) ; mesurer une période | définitions | §1 (définitions, ordres de grandeur, oscillogramme chiffré), méthode 1, EXO 01, carte |
| Avance/retard de phase ; décalage temporel ↔ déphasage ; déphasage nul en mode XY | absent | §2 (définition, \(\varphi = 2\pi\Delta t/T\), figure, mode XY et \(\lvert\sin\varphi\rvert = y_0/Y\), 5 ellipses calculées), méthodes 2-3, EXO 01, 06, 2 cartes |
| Définir valeur moyenne et valeur efficace | formules | §3, §4 (sens physique, tableau des signaux usuels, figure calculée, composante continue \(S_{\text{eff}}^2 = \langle s\rangle^2 + S_{\sim\text{eff}}^2\), \(\langle\mathrm{d}s/\mathrm{d}t\rangle = 0\)), méthodes 4-5, EXO 02-04, 3 cartes |
| Établir la valeur efficace d'un signal sinusoïdal | résultat seul | §4 (démonstration, figure \(s\) et \(s^2\)), EXO 03 |
| Nature d'une mesure (moyenne, efficace, amplitude, crête à crête), limites des appareils | absent | §5 (oscilloscope DC/AC, multimètre DC/AC/AC+DC, TRMS ou non, bande passante, résistance d'entrée), méthode 8, EXO 05, 2 cartes |
| Analyser une décomposition fournie | partiel (calculée) | §6 (énoncé admis, rangs, trois décompositions à lire, synthèse et spectres calculés, timbre, fondamental absent), méthode 6, EXO 07, concours A, 3 cartes |
| \(S_{\text{eff}}^2\) = somme des carrés des valeurs efficaces des harmoniques | Parseval en \(a_n, b_n, c_n\) | §7 (énoncé du programme, justification des termes croisés, 81 % / 98,6 %), méthode 7, EXO 07, 08, concours B, 2 cartes |
| Détecter une non-linéarité par l'apparition de fréquences nouvelles | mention (THD) | §8 (linéarité, superposition, quadratique, écrêtage calculé par FFT, redressement, pendule), méthode 9, EXO 09, concours C, 2 cartes |
| Choisir \(f_e\) et la durée d'acquisition ; analyse spectrale d'un signal périodique | absent | §9 (règles, \(\Delta f = 1/T_a\), exemple, programme Python exécuté, figure de fuite spectrale), méthode 10, EXO 10, concours D, 2 cartes |

## Contenu
**Cours** (« AU PROGRAMME · PTSI » + 9 sections + « Pour aller plus loin ») : §1 Signaux périodiques et sinusoïdaux ;
§2 Déphasage et décalage temporel ; §3 Valeur moyenne ; §4 Valeur efficace ; §5 Mesurer : ce qu'affiche un appareil ;
§6 Décomposition spectrale ; §7 Valeur efficace et spectre ; §8 Systèmes linéaires et non linéaires ; §9 Analyse
spectrale en pratique et en Python ; hors programme : coefficients de Fourier et symétries, Gibbs, THD, puissance active.
11 exemples traités chiffrés, 10 notices, 2 tableaux, 3 blocs dépliables, 9 figures calculées (signal périodique annoté ;
deux sinusoïdes décalées ; cinq ellipses XY ; quatre signaux usuels avec moyenne et efficace ; \(s\) et \(s^2\) ;
synthèse du carré par 1, 3 et 15 harmoniques ; spectres du carré et du triangle ; écrêtage et son spectre par FFT ;
spectres calculés par `rfft` pour deux durées d'acquisition), vérifiées en clair et en sombre.

**Code Python (§9)** : synthèse d'un signal à partir de son spectre fourni, contrôle de \(S_{\text{eff}}\) par la forme et par
le spectre (4,9746 V les deux), spectre recalculé par `np.fft.rfft` sur une acquisition simulée (6,366 V et 2,122 V
retrouvés) ; même style que `pynum` et la fonction `euler` de `premierordre` (fonctions commentées, résultats en
commentaire) ; la fonction `synthese` est reprise telle quelle dans `filtres` §12.

**Méthodes** (10) : lire un oscillogramme ; décalage → déphasage ; déphasage nul en XY ; valeur moyenne ; valeur
efficace par la forme ; exploiter un spectre fourni ; valeur efficace par le spectre ; choisir une mesure ; détecter une
non-linéarité ; régler une acquisition. 4 pièges.

**Exercices** (11 + concours) : 01 oscillogramme à deux voies (figure calculée) ; 02 créneau (ancien 01, + mesure AC) ;
03 secteur et radiateur (démonstration de \(S_m/\sqrt2\), puissance instantanée) ; 04 tensions redressées ; 05 ce
qu'affiche un multimètre (TRMS ou non) ; 06 déphasage et mode XY ; 07 spectre du créneau (ancien concours, complété) ;
08 puissance d'une tension déformée (ancien 06 sans THD) ; 09 non-linéarité cubique ; 10 régler une acquisition ;
11 coefficients de Fourier (hors programme, anciens 02 et 03) ; **Concours PT** « Le son d'une guitare électrique »
(A spectre, B valeur efficace et préamplificateur, C pédale de distorsion : écrêtage, valeur efficace par les raies et
par la forme, intermodulation ; D acquisition). L'ancien EXO 04 (carré dans un RC) est repris dans `flt` EXO 08.

**Cartes** : 10 réponses corrigées (questions inchangées : progression conservée) ; 15 ajoutées (déphasage, mode XY,
efficace avec composante continue, créneau de rapport cyclique α, sinus redressé, multimètre DC/AC/AC+DC, bobine en
régime périodique, part du fondamental d'un carré, détecter une non-linéarité, fréquences créées par \(x^2\), résolution
\(1/T_a\), choix de \(f_e\), secteur 325 V, fondamental absent, hauteur et timbre). Deck : 25 → 40 cartes. Rendu contrôlé
(`sig_cartes_rendu.js` : aucune erreur MathJax ; les réponses délicates sont écrites en \(\ldots\) pour éviter les
découpages de `flashPretty`).

## Notations
\(T\), \(f\), \(\omega\) (pulsation du signal, et du fondamental), \(S_m\), \(\varphi\), \(\langle s\rangle\), \(S_{\text{eff}}\),
\(S_{\sim\text{eff}}\), \(S_0\), \(S_n\), \(\varphi_n\), \(f_e\), \(T_a\), \(\Delta f\) ; amplitude complexe \(\underline S_m\) (comme `osc` et `flt`).
Le fondamental n'est plus noté \(\omega_0\) (réservé à la pulsation propre des filtres et oscillateurs).

## Contrôles
`verif_src.py` (3 fichiers) : aucune erreur ni « attention ». `apercu_src.py` à 390 et 1440 px pour les trois onglets :
`merr`, `brut`, `larges` vides, aucune erreur JS. Cartes : `corriger_cartes.py sig … --essai` (10 réponses) et
`ajouter_cartes.py sig … --essai` (25 → 40) sans erreur. Calculs : `sig_calculs.py`, `sig_calculs_exos.py`,
`sig_code_cours.py`.

## Doutes et suggestions
- Renommer le chapitre « Signaux périodiques et spectres » (le calcul des coefficients de Fourier n'est plus le sujet).
- Le §9 recoupe un peu `signum` §7 (2ᵉ année) : on s'y limite aux règles pratiques et on y renvoie pour la TFD et
  Nyquist-Shannon.
- Les figures de 540-560 px de large défilent horizontalement au téléphone (mécanisme `.lisible`/`.defile` du site).
