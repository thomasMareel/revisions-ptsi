# Revue du chapitre `energie` (prefix `eme`) — « Énergie mécanique » — 2026-11-22

Objet (point 4 de l'audit, lot 6 ; `docs/audit-2026-11/physique-1a.md` l. 26, 41, 105, 132-133 ; `audit-2026-11.md` §5) :
chapitre mince (7 600 signes de cours, 5 méthodes, 4 exercices, 26 cartes), sans bloc « Au programme », sans capacité
numérique ; oscillateur amorti traité une troisième fois (§4), après `rlc` et `oscill`. Programme : PTSI 2021, partie 2.3
(`pdf-pt/prog/ptsi.txt`, l. 1019-1072), et 2.4 pour \(qV\), 1.4 pour « prévoir l'évolution par l'énergie ».

## Fichiers produits (dans `AN1/`)
- `eme-cours.src.html` (122 ko ; 45 800 signes de texte, contre 7 600) — assemblé par `eme_construire.py` depuis
  `eme-cours.tpl.html` et `eme_figs.json` ;
- `eme-meth.src.html` (10 méthodes), `eme-exos.src.html` (10 exercices + 1 « Concours PT ») ;
- `eme-cartes-corr.json` (3 réponses corrigées), `eme-cartes-ajout.js` (15 cartes) ;
- scripts : `eme_figs.py` (7 figures), `eme_calculs.py` (exemples du cours), `eme_calculs_meth.py`, `eme_calculs_exos.py`
  (dont les simulations des EXO 07 et du concours), `eme_code/pendule.py` (**code du §10, exécuté tel qu'affiché**),
  `eme_code/test_pendule.py` (contrôles : période exacte par l'intégrale elliptique, harmonique 3, dérive d'Euler,
  séparatrice), `eme_code/transverse.py` (code de la méthode 10), `eme_voir.py`, `eme_cartes_rendu.py` ; copies des anciens
  panneaux `eme_orig_{cours,meth,exos}.html`.

## Erreurs et incohérences trouvées
| Où | Problème | Correction |
|---|---|---|
| §4 et carte 25 (audit) | τ = m/α et enveloppe en e^(−t/2τ) | **déjà corrigé** dans le dépôt (τ = 2Q/ω₀ = 2m/α) ; l'oscillateur amorti n'est plus exposé ici : §11 en donne l'essentiel en un exemple et **renvoie** à `oscill` §5-§10 (exposé de référence, mêmes notations) |
| ξ (audit) | ξ pour l'amortissement | absent du nouveau chapitre (Q et τ seulement) |
| Carte 9 | « réaction normale d'un support sans frottement » ne travaille pas | précisé : support **fixe** ; un support mobile peut travailler (réponse seule) |
| Carte 19 | régime apériodique « retour monotone » (faux si la masse est lancée vers l'équilibre) | « retour sans oscillation » ; critique « sans dépassement » ; renvoi à `oscill` (réponse seule) |
| Carte 24 | « W = −ΔE_p est une différentielle exacte » (confusion entre W et δW ; « fonction d'état » emprunté à la thermodynamique) | δW = −dE_p différentielle exacte, W = −ΔE_p ; le travail n'est pas la variation d'une fonction de la position (réponse seule) |
| Ancien §2 | « Coulombienne / gravitationnelle » mêlées, sans démonstration ; aucune énergie électrique qV | §4 : tableau, démonstrations dépliables, qV et charges ponctuelles, lien mgz ↔ −GMm/r |
| Ancien §3 | aucun exemple chiffré, « états liés » sans figure, aucune capacité numérique | §6-§10 réécrits, 4 figures calculées, code testé |
| Ancien EXO 03 (oscillateur amorti) | doublon de `oscill` | déplacé dans `oscill` (EXO 06, notations τ et ω_p) |

## Couverture du programme : avant → après
| Capacité exigible (2.3, sauf mention) | Avant | Après |
|---|---|---|
| Puissance, travail ; caractère moteur ou résistant | définitions | §1 (deux calculs types, figure des deux chemins, cycliste, ordres de grandeur de puissance), méthode 1, EXO 01, 2 cartes |
| Théorèmes de l'énergie et de la puissance cinétiques ; choisir le théorème | énoncés | §2 (démonstration, tableau de choix, freinage, gouttière par la puissance cinétique), méthode 2, EXO 01, 04, carte |
| Énergie potentielle, gradient (fourni), force à partir de \(E_p\), lecture graphique | δW = −dE_p | §3 (F = −grad E_p, lecture du graphe, figure des forces, frottement non conservatif), méthode 5, EXO 05 |
| Établir et citer \(E_p\) de pesanteur, gravitation, élastique (+ \(qV\), partie 2.4) | formules | §4 (tableau, trois démonstrations, qV, mgz comme approximation, libération, Rutherford), EXO 02, 05, 09, 3 cartes |
| Énergie mécanique, théorème ; forces conservatives ou non ; cas de conservation ; conditions initiales | énoncés | §5 (démonstration, trois familles, luge, chariot, notice support mobile), méthodes 3, 4, EXO 08 |
| Mouvement conservatif 1D : barrière, puits, borné ou non, périodique, vitesse nulle | une liste | §6 (figure des trois niveaux, bosse, notice rail ≠ graphe), méthode 6, EXO 03, 2 cartes |
| Positions d'équilibre, stabilité | critère | §7 (justification, ressort transverse bistable avec figure, pendule), méthode 7, EXO 05 |
| Petits mouvements, puits harmonique, équation | k_eff | §8 (démonstration, angle, ressort transverse, molécule HCl, validité), méthode 8, EXO 03, 06, concours B |
| **Capacité numérique** : ED d'ordre 2 non linéaire, effet des termes non linéaires | absent | §9 (portrait de phase, figure calculée, séparatrice, pendule à fil ou à tige), §10 (odeint, code exécuté, figure θ(t), non-isochronisme, harmonique 3, contrôle de l'énergie, séparatrice numérique), méthodes 9, 10, EXO 07, concours C-D, 4 cartes |
| Prévoir l'évolution par l'énergie (1.4) ; bilans avec frottement | §4 (oscillateur amorti) | §11 (dE_m/dt = −αv², trajectoire de phase amortie dans le double puits, palet), concours D, carte ; renvoi à `oscill` |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 11 sections + « Pour aller plus loin ») : §1 Puissance et travail ; §2 Théorèmes
de la puissance et de l'énergie cinétiques ; §3 Forces conservatives et énergie potentielle ; §4 Énergies potentielles
usuelles ; §5 Énergie mécanique et conservation ; §6 Mouvement conservatif à une dimension ; §7 Équilibres et stabilité ;
§8 Petits mouvements ; §9 Portrait de phase ; §10 Résolution numérique (pendule aux grandes amplitudes) ; §11 Bilans avec
frottements ; hors programme : période par une intégrale (Borda), rotationnel, énergie potentielle effective (renvoi
`chcentral`), effet tunnel. 16 exemples traités chiffrés, 11 notices, 2 tableaux, 5 démonstrations ou justifications
dépliables, 1 programme Python testé, 7 figures SVG calculées (travail du poids sur deux chemins ; force lue sur le graphe
de \(E_p\) ; zones accessibles pour trois énergies ; ressort transverse, schéma et \(E_p\) ; portrait de phase du pendule ;
θ(t) exact et linéaire à 120° par odeint ; trajectoire de phase amortie dans le double puits), vérifiées en clair et en sombre.

**Méthodes** (10) : travail et puissance ; choisir le théorème ; vitesse par conservation ; conservation ou non ; énergie
potentielle ↔ force ; lire un graphe de \(E_p\) ; équilibres et stabilité ; petits mouvements ; portrait de phase ;
résolution numérique et contrôles (code testé). Les 5 anciennes méthodes et les pièges sont repris.

**Exercices** (11) : 01 téléski (nouveau) ; 02 saut à l'élastique (nouveau) ; 03 profil \(E_p\) (ancien 01, une question
ajoutée : points de rebroussement, asymétrie du puits) ; 04 plan incliné (ancien 02, titré « lois de Coulomb, vues en SI »,
centré sur le théorème de l'énergie cinétique) ; 05 charge entre deux charges (nouveau : \(E_p\) électrique, stabilité selon
la direction) ; 06 potentiel de Morse (nouveau : petits mouvements, anharmonicité) ; 07 ressort qui durcit (nouveau :
portrait de phase, simulation, période qui diminue) ; 08 looping (ancien concours, condition de contact justifiée par le
principe fondamental) ; 09 tir vertical, mgz contre gravitation (nouveau) ; 10 pendule lancé du bas : oscillations, tours,
fil qui se détend (nouveau) ; **Concours PT « Un récupérateur d'énergie bistable »** (A profil et équilibres ; B petits
mouvements et domaine harmonique ; C portrait de phase et séparatrice ; D simulation amortie, puits final, énergie
récupérée 9E_b, sensibilité du puits final).

**Cartes** : 26 → 41 (15 ajoutées à la fin, formules en `\\( … \\)` : puissance motrice ou résistante, travail d'un
frottement, choix du théorème, \(qV\), mgz et gravitation, vitesse de libération, puits et barrière, mouvement périodique,
petits mouvements avec un angle, portrait de phase, séparatrice du pendule, système d'ordre 1 et odeint, effets non
linéaires, contrôle d'une simulation, état final avec frottement) ; 3 réponses corrigées (questions inchangées).

## Contrôles
`verif_src.py` sans erreur ni attention sur les trois panneaux ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`,
`larges` vides, aucune erreur JS (cours, méthodes, exercices) ; captures des figures relues ; `corriger_cartes.py --essai`
(3 réponses) et `ajouter_cartes.py --essai` (26 → 41) sans erreur ; rendu MathJax des cartes ajoutées : 0 erreur ;
code du §10 et de la méthode 10 exécutés ; tous les nombres recalculés (`eme_calculs*.py`).

## Notations
\(\mathcal P\), \(\delta W\), \(W_{A\to B}\), \(E_c\), \(E_p\), \(E_m\), \(\vec F_{\text{nc}}\) ;
\(\vec F=-\overrightarrow{\operatorname{grad}}\,E_p\) (comme `lorentz`) ; \(\mathcal GM_T\), \(g_0\) (comme `mecpt`) ;
\(x_e\), \(E_p''(x_e)\), \(\omega_0\) ; \(-\alpha\vec v\) (frottement fluide, comme `mecpt` et `oscill`) ; Q, τ = 2Q/ω₀
(jamais ξ) ; vecteur d'état \(Y=(\theta,\omega)\), `odeint(F, Y0, t)` avec `F(Y, t)` comme `pynum` §7.

## Doutes, remarques pour l'intégration
- **Titre** : « Énergie mécanique » convient ; « Approche énergétique du mouvement d'un point » suivrait le programme.
- Le **portrait de phase** n'est pas cité par le programme de PTSI : présenté comme outil (dit dans le bloc « Au programme »).
- Le §10 reprend l'exemple du pendule de `pynum` §7 sous l'angle physique (odeint, portrait, harmoniques) sans refaire la
  table des périodes ; le pendule pesant reste à `mvtsolide` (renvoi).
- L'EXO 04 (Coulomb) existe aussi, sous forme proche, dans `mecpt` (EXO 05) : gardé ici pour le bilan énergétique.
- `rlc` §3-6 garde son propre exposé électrique des régimes (non modifié ici) ; il pourrait renvoyer à `oscill` §6-§7.
