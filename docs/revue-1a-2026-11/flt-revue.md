# Revue du chapitre `filtres` (prefix `flt`) — « Filtres du 1er et 2e ordre » — 2026-11-22

Objet (point 4 de l'audit, lot 7 ; `docs/audit-2026-11/physique-1a.md` l. 24-29, 103, 156 ; `audit-2026-11.md` §5) :
cours de 10 300 signes sans exemple traité ni notice, 6 méthodes, 7 exercices, 41 cartes ; filtrage mécanique,
cascade, gabarit et capacité numérique absents ou réduits à une méthode ; socle des impédances exposé trois fois
(`rlc` §5, `filtres` §1, `signaux` §4). Programme : PTSI 2021, partie 1.4 (impédances complexes, association de deux
impédances, représentation complexe du régime forcé : l. 785-791) et partie 1.5 « Filtrage linéaire » (l. 798-856).

## Décision sur les doublons : le socle vit dans `filtres`
**`filtres` §1 à §3 devient l'exposé de référence du site** sur la notation complexe, les impédances (établies), leurs
comportements limites, les associations de deux impédances, les lois des circuits et les diviseurs en complexes, et la
mesure d'une impédance. Raisons : le chapitre est dans ma mission et peut porter un exposé complet tout de suite ; c'est
ici que ces outils servent le plus (fonctions de transfert) ; `rlc` §5, très mince, n'établit pas les impédances, ne
traite ni les associations ni les diviseurs ; `signaux` §4 est supprimé (voir `sig-revue.md`).

**À faire dans les chapitres hors de ma mission** (renvois à poser lors de leur réécriture) :
- `rlc` §5 « Régime sinusoïdal forcé » : remplacer les blocs « Pourquoi les complexes ? » et « Impédances complexes »
  (notation complexe, dérivation \(\times j\omega\), trois impédances, lois en complexes) par un renvoi : « Notation
  complexe, impédances et associations : chapitre « Filtres du 1er et 2e ordre », §1 à §3 » ; garder seulement
  l'impédance du RLC série (module, argument) et son application. Aligner la notation \(\underline{X_m}\) sur
  \(\underline X_m\) (`osc`, `flt`).
- `rlc` §6 : « pour \(Q\) grand, \(U_C(\omega_0) \approx QE_m\) » est **exact pour tout \(Q\)** en \(\omega_0\) ; c'est le
  maximum qui vaut environ \(QE_m\) quand \(Q \gg 1\). La phrase « distinguer les cas \(Q\ \ 1/\sqrt2\) » a perdu son
  « < » (caractère brut lu comme une balise). Renvoyer au passe-bas d'ordre 2 de `filtres` §7 (même fonction de
  transfert) et à `osc` §10 pour \(\Delta\omega = \omega_0/Q\).
- `oscill`, bloc « Au programme » : « Les impédances complexes et la résonance du circuit RLC sont traitées dans
  « Circuit RLC série » » → « Les impédances complexes sont exposées dans « Filtres » (§1 à §3), la résonance du
  circuit RLC dans « Circuit RLC série » ».
- `premierordre`, bloc « Au programme » et §9 : renvoi déjà correct (« Circuit RLC série » et « Filtres ») ; on peut
  préciser « Filtres, §1 ».

## Fichiers produits (dans `AN1/`)
- `flt-cours.src.html` (114 ko ; 52 300 signes de texte contre 10 300) — assemblé par `flt_construire.py` depuis
  `flt-cours.tpl.html` et `flt_figs.json` ;
- `flt-meth.src.html` (10 méthodes), `flt-exos.src.html` (11 exercices + 1 « Concours PT », depuis `flt-exos.tpl.html`) ;
- `flt-cartes-corr.json` (5 réponses corrigées), `flt-cartes-ajout.js` (14 cartes) ;
- scripts : `flt_figs.py` (15 figures, dont 2 d'exercices), `flt_svg.py` (schémas électriques repris de `rco_svg.py`,
  grilles de Bode, quadripôles, simplification des tracés), `flt_calculs.py` (cours), `flt_calculs_exos.py`
  (méthodes, exercices ; hacheur vérifié par simulation), `flt_code_cours.py` (programme du §12, exécuté),
  `flt_code_extrait.py` (le même extrait du HTML : sortie identique), `flt_concours_e1.py` (partie E du concours),
  `flt_cartes.py`, `flt_cartes_rendu.js`, `flt_voir.py`, copies `flt_orig_{cours,meth,exos}.html`.
- Le panneau `flt-simu` (simulateur de Bode à 5 modes) n'est pas modifié ; le cours le cite (§6).

## Erreurs et défauts trouvés
| Où | Problème | Correction |
|---|---|---|
| Cours (ancien) | aucun exemple chiffré, aucune notice, une seule figure ; filtrage mécanique, gabarit, effet de charge, capacité numérique absents | 12 sections, 15 exemples, 13 notices, 13 figures calculées |
| Cours §5 (ancien) | pulsation de résonance du passe-bas d'ordre 2 et passe-haut d'ordre 2 présentés comme exigibles | \(G(\omega_0) = QH_0\), condition \(Q \gt 1/\sqrt2\) au §7 ; calcul de \(\omega_r\), passe-haut et coupe-bande d'ordre 2 en « Pour aller plus loin » (cohérent avec `osc` §10, « non exigible ») |
| Cours §6 (ancien) | intégrateur « \(s_s \propto \int s_e\,\mathrm{d}t\) … en transformée inverse » : la composante continue n'est pas intégrée, et la condition porte sur toutes les composantes | énoncé corrigé (partie variable, toutes les raies au-delà de \(f_c\)), même chose pour le dérivateur |
| Ancien EXO 03 | « pour le circuit ci-dessous » sans figure ; en HF « tout le courant passe par L » alors que la bobine est un interrupteur ouvert | figure ajoutée ; raisonnement corrigé (aucun courant, \(u_s = u_e\)) ; question sur la bobine réelle |
| Ancienne méthode 4 | équation des pulsations de coupure écrite de façon confuse | méthode réécrite ; démonstration de \(\Delta\omega = \omega_0/Q\) en deux lignes (cours §7) |
| Ancien « Concours PT » | trois parties d'une question chacune, sans spectre | remplacé par un concours en 5 parties (spectre, passe-bas, passe-bande, charge, Python) ; son contenu est dans EXO 02 et le cours |
| Carte 27 | « R = 0 à BF → tout sur C » : explication fausse | en BF le condensateur est ouvert, \(i = 0\), \(u_s = u_e\) ; en HF il est un fil ; \(\omega_0\), \(Q\), résonance si \(Q \gt 1/\sqrt2\) |
| Carte 36 | « \(Q\) est aussi appelé acuité de résonance » | \(Q\) mesure l'acuité de la résonance |
| Carte 38 | « intersection des asymptotes » donnée comme pulsation de coupure sans condition | vrai pour un premier ordre seulement ; pour un ordre 2, l'intersection donne \(\omega_0\) |
| Carte 30 | intégrateur imprécis (composante continue, condition) | précisé |
| Carte 21 | \(\omega_r\) sans condition d'existence ni mention « non exigible » | complété ; à retenir : \(G(\omega_0) = QH_0\), \(\varphi = -\pi/2\) |

## Couverture du programme : avant → après
| Capacité (PTSI) | Avant | Après |
|---|---|---|
| Représentation complexe du régime forcé (1.4) | rappel | §1 (régime forcé, amplitude complexe, \(\times j\omega\), retour au réel, exemple RC chiffré), méthode 1, carte |
| Établir et citer les impédances de R, L, C (1.4) | citées | §2 (démonstration, comportements limites, ordres de grandeur, figure \(\lvert Z\rvert(f)\), bobine réelle), méthode 2, EXO 01, cartes |
| Association série ou parallèle de deux impédances (1.4) ; diviseurs ; mesure d'une impédance | formules | §3 (associations, diviseurs de tension et de courant, Fresnel calculé, RLC et bouchon, exemple R∥C, mesure à l'oscilloscope), méthode 2, EXO 01, 2 cartes |
| Fonction de transfert, gain, gain en dB, phase ; réponse à une excitation sinusoïdale | définitions | §4 (définition en sortie ouverte, réponse sinusoïdale, tableau des dB, lien avec l'équation différentielle, mesure à l'oscilloscope), méthode 4, cartes |
| Échelles logarithmiques, zones rectilignes | partiel | §5 (asymptote \(K(j\omega)^n\) : \(20n\ \text{dB}\)/déc et \(n\pi/2\), produit, bande passante, exemple de lecture), méthode 6, carte |
| Tracer le Bode d'un ordre 1 | asymptotes | §6 (méthode complète, valeurs à 0,1/1/10, RC et RL, passe-haut, exemple \(H_0 \neq 1\) avec \(\omega_c = 1/((R_1\parallel R_2)C)\), 2 figures calculées), méthode 5, EXO 02-04 |
| Utiliser une fonction de transfert donnée d'ordre 2 ; passe-bas et passe-bande | formes canoniques | §7 (passe-bas RLC sur C, \(G(\omega_0) = QH_0\), résonance si \(Q \gt 1/\sqrt2\) ; passe-bande sur R, \(\Delta\omega = \omega_0/Q\) démontrée ; 2 figures calculées à plusieurs \(Q\)), EXO 05-07, cartes |
| Action sur une somme de sinusoïdes, sur un signal périodique ; filtrage d'un signal non sinusoïdal à partir d'une analyse spectrale | formule | §8 (principe, méthode, carré dans un passe-bas pour 3 coupures, spectres d'entrée et de sortie d'un passe-bande, extraction d'un harmonique), méthode 7, EXO 08, concours B-C, cartes |
| Moyenneur, intégrateur, dérivateur : conditions | 3 lignes | §9 (conditions sur toutes les raies, exemples secteur redressé, carré → triangle, triangle → carré, figure calculée), méthode 8, EXO 09, carte |
| Cahier des charges ; faible impédance de sortie, forte impédance d'entrée ; dispositif à plusieurs étages | méthode 6 | §10 (gabarit calculé, ordre nécessaire, modèle de Thévenin, formule de cascade, deux cellules RC, appareils de mesure), méthodes 9-10, EXO 10, concours D, 3 cartes |
| Filtrage par un dispositif mécanique (sismomètre, amortisseur, accéléromètre) | absent | §11 (équation du capteur inertiel, passe-haut d'ordre 2, sismomètre / accéléromètre, suspension, figure calculée, exemples chiffrés), EXO 11, 2 cartes |
| Capacité numérique : simuler l'action d'un filtre sur un signal de spectre fourni ; influence des caractéristiques | absent | §12 (programme exécuté : `synthese`, `passe_bas_1`, `passe_bande`, `filtrer` ; influence de \(f_c\) et de \(Q\) ; figure produite par le même calcul), concours E, carte |
| Non-linéarité (nouvelles fréquences) | absent | renvoi à `signaux` §8 (bloc « Au programme ») |

## Contenu
**Cours** (« AU PROGRAMME · PTSI » + 12 sections + « Pour aller plus loin ») : §1 Régime sinusoïdal forcé et notation
complexe ; §2 Impédances complexes ; §3 Associations, lois des circuits et diviseurs ; §4 Fonction de transfert, gain
et phase ; §5 Diagramme de Bode et échelles logarithmiques ; §6 Filtres du premier ordre ; §7 Filtres du deuxième
ordre ; §8 Action d'un filtre sur un signal périodique ; §9 Moyenneur, intégrateur, dérivateur ; §10 Choisir et
associer des filtres ; §11 Filtrage mécanique ; §12 Simulation numérique ; hors programme : passe-haut et coupe-bande
d'ordre 2, \(\omega_r\) exacte, ordres supérieurs, filtres actifs, notation de Laplace de la SI.
13 figures calculées : modules des impédances (log-log) ; Fresnel du RLC ; Bode RC passe-bas et CR passe-haut avec
schémas ; passe-bas RLC pour \(Q\) = 0,5 ; 0,71 ; 2 ; 5 ; passe-bande RLC pour \(Q\) = 1 et 5 avec \(\Delta\omega\) ; carré
dans un passe-bas pour 3 coupures ; spectres d'entrée et de sortie d'un passe-bande ; intégrateur et dérivateur ;
gabarit avec filtres d'ordre 1 et 2 ; cascade (modèle de Thévenin) ; capteur inertiel et son gain ; sortie du programme
Python. Vérifiées en clair et en sombre.

**Méthodes** (10) : notation complexe ; impédance équivalente ; nature d'un filtre sans calcul ; établir \(\underline H\) et
l'identifier ; tracer un Bode d'ordre 1 ; lire un Bode ; sortie pour un signal périodique (et en Python) ; moyenneur,
intégrateur, dérivateur ; choisir un filtre ; cascade. 5 pièges.

**Exercices** (11 + concours) : 01 impédances du RLC (ancien `sig` EXO 05 sans les puissances) ; 02 cellule RC
(ancien 01) ; 03 cellule RL et bobine réelle (ancien 03, figure ajoutée) ; 04 établir et tracer un passe-haut de
gain 0,8 ; 05 passe-bande RLC (ancien 02) ; 06 dimensionner un passe-bande, effet de \(r\) (ancien 06) ; 07 résonance du
passe-bas d'ordre 2 (ancien 04, « calcul non exigible ») ; 08 carré dans un passe-bas (ancien 05 et ancien `sig` 04) ;
09 lisser la sortie d'un hacheur (moyenneur, intégrateur, ondulation vérifiée par simulation : 0,181 V) ; 10 gabarit et
cascade (suiveur, effet de charge, cellule ×10) ; 11 accéléromètre ; **Concours PT** « Fabriquer une sinusoïde à partir
d'un créneau » (A spectre et valeur efficace ; B passe-bas RC insuffisant ; C passe-bande RLC, \(Q \geq 12{,}5\), bobine
réelle ; D charge de 8 Ω et suiveur ; E boucle Python, résultat 12,5 vérifié).

**Cartes** : 5 réponses corrigées (questions inchangées) ; 14 ajoutées (amplitude complexe, parallèle, diviseur et sa
condition, mesure d'une impédance, zones rectilignes, \(G(\omega_0) = QH_0\), composante continue \(H(0)\), équation
différentielle ↔ \(\underline H\), cascade avec impédances, gabarit, ordre nécessaire, sismomètre/accéléromètre,
accéléromètre 10 nm, simulation Python). Deck : 41 → 55 cartes. Rendu contrôlé (`flt_cartes_rendu.js`, aucune erreur).

## Notations
\(\underline X_m = X_me^{j\varphi}\) (comme `osc`), \(j\), \(\underline Z\), \(\underline Y\), \(\underline H(j\omega) = \underline U_{sm}/\underline U_{em}\),
\(G\), \(G_{\text{dB}} = 20\log G\), \(\varphi\), \(H_0\), \(\omega_c\), \(f_c\), \(\omega_0\), \(Q\), \(x = \omega/\omega_c\) ou \(\omega/\omega_0\)
(`osc` emploie \(u\) pour la pulsation réduite ; ici \(u\) désigne des tensions) ; \(u_e\), \(u_s\) ; impédances
d'entrée et de sortie \(\underline Z_e\), \(\underline Z_s\) comme `ali` (2ᵉ année). Vecteurs de Fresnel en gras dans la figure.

## Contrôles
`verif_src.py` (3 fichiers) : aucune erreur ni « attention ». `apercu_src.py` à 390 et 1440 px pour les trois onglets :
`merr`, `brut`, `larges` vides, aucune erreur JS. Cartes : `corriger_cartes.py flt … --essai` (5 réponses) et
`ajouter_cartes.py flt … --essai` (41 → 55) sans erreur. Code du §12 extrait du HTML et exécuté : sortie identique.

## Doutes et suggestions
- Renommer le chapitre « Régime sinusoïdal forcé et filtrage linéaire » (il porte désormais le socle des impédances).
- Ordre du groupe « Ondes & signaux » : `rlc` précède `signaux` et `filtres` mais utilise les impédances ; le renvoi
  vers l'avant est assumé (le site se lit dans le désordre). Autre option, si l'on réécrit `rlc` : y placer le socle
  et faire renvoyer `filtres` — je ne l'ai pas fait, `rlc` étant hors de ma mission et trop mince aujourd'hui.
- Les questions des cartes n° 19 à 24 contiennent « 2nd », que `flashPretty` met en formule (« \(du\ 2nd\) ») : défaut
  d'affichage préexistant, non corrigé (la réponse de la carte 21 étant corrigée, on ne pouvait pas aussi changer sa
  question).
- Les figures de 560 px défilent horizontalement au téléphone (mécanisme du site) ; les diagrammes de Bode restent
  lisibles à l'ordinateur.
