# `bode` (prefix `bode`) — « Réponse fréquentielle et diagrammes de Bode », mise au format de la 2ᵉ année (point 7), 2026-11-22

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `bode-cours.src.html` | cours complété (≈ 92 000 car.) : bloc « AU PROGRAMME · PTSI », §1 à §9, « POUR ALLER PLUS LOIN · HORS PROGRAMME » ; 13 exemples traités, 6 figures (2 d'origine, 4 nouvelles calculées), un programme Python testé |
| `bode-meth.src.html` | 10 méthodes (étapes + exemple éclair chiffré) + « Pièges classiques » (5 méthodes sans exemple avant) |
| `bode-exos.src.html` | 10 exercices + « Concours PT » en 4 parties (A à D, 8 questions) |
| `bode-cartes-corr.json` | 1 carte corrigée (réponse seule) |
| `bode-cartes-ajout.js` | 14 cartes ajoutées en fin de deck (18 → 32) |
| `bode-cours.tpl.html`, `bode-exos.tpl.html` | gabarits (`@@FIG:nom@@`, `@@ORIG:bode:n@@` = exercice d'origine) assemblés par `bsp_construire.py` |
| `bode_figs.py` → `bode_figs.json`, `bsp_figs_orig.json`, `bsp_svgk.py` | figures calculées (classes du site, aucune couleur en dur) ; figures d'origine extraites telles quelles |
| `bode_calculs.py`, `bode_calculs_meth.py`, `bode_calculs_exos.py`, `bode_code.py` | vérification numpy / sympy / scipy de tous les exemples, éclairs et corrigés ; code Python du §4 exécuté |
| `bsp_voir.py`, `bsp_deborde.js`, `bsp_cartes_rendu.js`, `bsp_qcartes.js` | outils communs aux trois chapitres (rendu des figures clair / sombre, recherche de débordement, rendu des cartes par `flashPretty`, questions exactes d'un deck) |

Reconstruire : `python3 bode_figs.py && python3 bsp_construire.py bode`.

## Numérotation des §

**Inchangée** : §1 à §5 gardent leur titre et leur contenu (vidéo `video/slci/ch5`, renvois de `sys1`/`sys2`). Les sections nouvelles sont §6 à §9. Le texte du §5 sur Black et Nyquist a été déplacé dans la section finale « Pour aller plus loin ».

## Erreurs trouvées et corrigées

1. **Lieux de Black et de Nyquist** présentés au §5 comme d'autres représentations « le Bode restant la référence en PTSI » : ils sont **exclus des programmes des deux années** (commentaire de la partie C2). Déplacés en fin de cours, signalés hors programme.
2. **EXO 05** (ancien exercice au gabarit d'avant la refonte) : figure SVG codée à la main (libellés à 10 px, classes `svg-label`, couleurs `var(--…)` en attributs, asymptote fausse), texte « ω < 10 » avalé par un « < » brut, notation `ω_c` ; surtout, la conclusion **« Mφ ≈ 0,1° »** venait de la phase calculée à la coupure *asymptotique* (31,6 rad/s, où la phase vaut exactement −180°) : la vraie coupure est 30,1 rad/s et Mφ ≈ 1,6°, M_G ≈ 0,8 dB (gain limite 110). Exercice réécrit (Q2 montre pourquoi l'asymptote ne suffit pas, Q4 règle le gain pour Mφ = 45°), figure calculée dans la solution.
3. **Formules en ligne trop larges au téléphone** (débordement de la page à 390 px) dans les exercices d'origine 02, 03, 06 et le Concours : scindées.
4. Carte 14 (phase maximale du réseau à avance de phase) : correcteur de 2ᵉ année → réponse préfixée « Hors programme en PTSI (vu en 2ᵉ année, correcteur à avance de phase) : », question inchangée.
5. Notation du facteur de résonance alignée sur `sys2` (demande du coordinateur) : \(Q_r\) dans EXO 06 et au §6.

## Couverture du programme (S1-S2) : avant → après

| Capacité (programme SII 2021) | Avant | Après |
|---|---|---|
| Modéliser le signal d'entrée : signaux périodiques (B2, S1) | §1 (définition) | §1 + exemple chiffré, figure entrée/sortie calculée, décalage temporel Δt = −φ/ω |
| Réponse à une entrée sinusoïdale en régime permanent (C2, S1) | §1 | §1 (régime transitoire, erreurs classiques) |
| Allures des diagrammes réel et asymptotique de Bode (C2, S2) | §2-§4 (1er ordre, briques) | + exemples aux §2 et §4, tableau des écarts réel/asymptote, détermination de l'arctangente, §6 (2e ordre : ξ ≥ 1 en deux premiers ordres, correction −20 log 2ξ en ω₀, résonance qui coûte de la marge), §7 (retard pur) |
| Établir un modèle de comportement à partir d'une réponse fréquentielle : 1er, 2e ordre, dérivateur, intégrateur, gain, retard (B2, S2) | §5 (méthode générale) | §5 + identification d'un 2e ordre résonant chiffrée ; §7 identification d'un retard ; EXO 08 (vérin) |
| Rapidité : bande passante (C2, S2) | une phrase | §5 (1er ordre, t5·ω = 3), §8 (bande passante d'une boucle fermée lue sur la FTBO, figure FTBO/FTBF) ; EXO 09, Concours C |
| Choisir les entrées à imposer et les sorties pour identifier un modèle (D2, S2) ; vérifier la cohérence d'un modèle (B3, S2) | ❌ | §9 (protocole, mesure à l'oscilloscope, φ = −360° f Δt, confrontation modèle/mesure) ; EXO 08 |
| Lien informatique ⇆ I (déterminer la réponse fréquentielle) | ❌ | §4 : fonction `bode(H, w)` en numpy (`np.unwrap`), exécutée |
| Black-Nichols, Nyquist (hors programme) | présentés au §5 | section finale |

## Ajouts

- **Cours** : bloc programme ; §1 exemple et figure `sinus` (réponse transitoire puis permanente de 5/(1+0,2p) à 2 sin 10t) ; §2 exemple (intégrateur, dérivateur, retard) et renvoi à `sys1` §4 / `sys2` §3 ; §3 erreurs classiques ; §4 tableau des écarts, deux exemples, code Python ; §5 identification d'un 2e ordre, bande passante d'un 1er ordre ; **§6** deuxième ordre dans un tracé (figure `reso` : 2/(p(1+0,02p+0,0025p²)), M_G de 26 à 12 dB) ; **§7** retard pur (figure `retard` : four 2e^{−0,5p}/(1+5p)) ; **§8** boucle fermée (figure `boucle`) ; **§9** mesure ; section hors programme (Black, Nyquist, avance de phase → 2ᵉ année).
- **Méthodes** (5 → 10) : ajoutées 3 (forme canonique), 6 (courbe réelle), 7 (coupure à 0 dB exacte), 9 (relevé à l'oscilloscope), 10 (boucle fermée sur boucle ouverte) ; un exemple éclair chiffré par méthode.
- **Exercices** (7 + concours → 10 + concours) : EXO 05 réécrit ; nouveaux EXO 08 (identifier un vérin avec retard à partir de relevés), EXO 09 (bande passante d'un asservissement, deux réglages), EXO 10 (2e ordre très amorti) ; Concours complété : parties C (bande passante de l'axe asservi) et D (retard d'une commande numérique, retard maximal), B1 complétée (marge de phase), difficulté ★★★.
- **Cartes** (+14) : Δt = −φ/ω, dérivateur, gain en ω₀ d'un 2e ordre, 2e ordre très amorti, retard (repérage et valeur), FTBF aux basses / hautes pulsations, bande passante et ω_c0, décibels de 5 et 0,25, relevé à l'oscilloscope, amplitude d'essai, forme canonique de 1/(p+a), `np.unwrap`, phase à une octave.

## Notations

ω_c0 (coupure à 0 dB de la FTBO), M_φ, M_G, ω_π, ξ, ω₀, classe α, K ; H_BO, H_BF ; Q_r (facteur de résonance, comme `sys2`). Notations des vidéos (`video/slci/ch5`) respectées.

## Doutes / remarques

- §8 : « bande passante de la FTBF entre ω_c0 et 2 ω_c0 » est un repère (rapport 1,3 à 1,6 pour une FTBO K/(p(1+τp)) quand ξ va de 1 à 0,3), pas une loi.
- Les figures font 410 unités de large, comme celles d'origine ; la seule figure d'exercice (EXO 05) est dans la **solution**, et le contrôle à 390 px ne signale aucun débordement.
- Contrôles passés : `verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges` vides, aucune erreur JS (cours, méthodes, exercices) ; `corriger_cartes.py --essai` et `ajouter_cartes.py --essai` sans erreur ; rendu des cartes (`flashPretty` + MathJax) sans erreur, trois questions réécrites avec `\( \)` pour éviter « \(50 ms\) ».
