# `precision` (prefix `prec`) — « Performances : précision et rapidité », mise au format de la 2ᵉ année (point 7), 2026-11-22

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `prec-cours.src.html` | cours complété (≈ 57 000 car.) : bloc « AU PROGRAMME · PTSI », §1 à §8, « POUR ALLER PLUS LOIN · 2ᵉ ANNÉE ET HORS PROGRAMME » ; 11 exemples traités, 5 figures (1 d'origine, 4 nouvelles calculées) |
| `prec-meth.src.html` | 9 méthodes (étapes + exemple éclair chiffré) + « Pièges classiques » (5 méthodes sans exemple avant) |
| `prec-exos.src.html` | 11 exercices + « Concours PT » en 5 parties (A à E, 7 questions) |
| `prec-cartes-corr.json` (écrit par `prec_cartes.py`) | 5 cartes corrigées (réponse seule) |
| `prec-cartes-ajout.js` | 10 cartes ajoutées en fin de deck (30 → 40) |
| `prec-cours.tpl.html`, `prec-exos.tpl.html` | gabarits assemblés par `bsp_construire.py` |
| `prec_figs.py` → `prec_figs.json` | figures calculées `pert`, `capteur` (schémas-blocs), `rampe`, `cdc` |
| `prec_calculs.py`, `prec_calculs_meth.py`, `prec_calculs_exos.py` | vérification numpy / sympy / scipy (réponses simulées : dépassement, \(t_{r5\%}\), \(t_m\)) |

Outils communs : voir `bode-revue.md`. Reconstruire : `python3 prec_figs.py && python3 bsp_construire.py prec`.

## Numérotation des §

**Inchangée** pour §1 à §5 (vidéo `video/slci/ch7` ; `corr-cours` renvoie au §5 pour les structures P, PI, PID). Nouveaux : §6 à §8. Les compléments du §4 (temps de montée, bande passante, exemples) sont insérés dans la section.

## Erreurs trouvées et corrigées

1. **EXO 07** : avec \(H'_{BO} = \dfrac{10}{p^2(1+0{,}5p)}\), le corrigé concluait « classe 2 → écart de traînage nul ». Or l'équation caractéristique \(0{,}5p^3 + p^2 + 10 = 0\) n'a pas de terme en \(p\) : **la boucle est instable** et le théorème de la valeur finale ne s'applique pas. Corrigé (Q2 devient le piège), et cette erreur classique est ajoutée au cours (§2), aux méthodes et aux cartes (carte 18 corrigée, une carte ajoutée).
2. **EXO 08** : \(\omega_c\) estimé à 4 rad/s sur l'asymptote (avec une phrase fausse « pour ω_c ≤ 1 ») et \(M_\varphi = 65{,}3°\) ; valeurs exactes \(\omega_{c0} \approx 3{,}2\ \text{rad/s}\), \(M_\varphi \approx 75°\), donc \(T_i \approx 3\) s au lieu de 2,5 s. Corrigé.
3. **EXO 03** : supposait \(\omega_{c0} \approx 2\) rad/s pour le même processus que l'exemple du cours, qui trouve 1,6 rad/s (valeur exacte 1,62) : \(T_i\) passe de 5 s à 6 s, comme au §5.
4. **EXO 04** : stabilité du PI affirmée « si \(T_i \gt 1\) s » par la condition de degré 3 (cas de Routh, hors programme) : justifiée maintenant par les pôles imaginaires purs (au programme).
5. **Correcteurs présentés sans statut** : le programme place le réglage des correcteurs P, PI, avance de phase en S3-S4 (2ᵉ année) et exclut PD, PID, Ziegler-Nichols. Encadré « Vu en 2ᵉ année » au §5, mentions dans le tableau et l'exemple du PI, titres des EXO 03, 05, 08 signalés ; cartes 11 et 29 (réglage du PI) préfixées « Hors programme en PTSI (vu en 2ᵉ année) : » ; carte 14 (« compenser avec D ») et carte 24 (conseillait un correcteur « double intégrateur », qui déstabilise la boucle) corrigées.
6. **Ancien Concours** mince (deux questions et une question PID hors programme) : remplacé par un sujet en 5 parties qui reprend sa partie A.
7. Formules en ligne trop larges au téléphone (démonstration du §2, EXO 03, 04, 06) : scindées ou passées en bloc.

## Couverture du programme (S1-S2) : avant → après

| Capacité (programme SII 2021) | Avant | Après |
|---|---|---|
| Critères du cahier des charges : dépassement relatif, temps de réponse, **temps de montée**, bande passante, **retard de traînage** (C1) | §1 (D₁, t_r5%) | §1 (t_m défini, D₁ rapporté à la valeur finale, exemple chiffré sur la figure), §4, §7 |
| Théorème de la valeur finale (C2) | utilisé sans énoncé | §2 (énoncé, conditions, erreur classique sur une boucle instable) |
| Écart statique, lien classe / écart (C2) | §2 | §2 (inchangé, + erreurs classiques) |
| Écart / erreur vis-à-vis d'une **perturbation** (C2) ; poursuite et régulation (B2, S1) | §3 | §3 (définitions poursuite/régulation, schéma-blocs calculé, exemple de superposition consigne + perturbation) |
| **Écart et erreur** distingués (C2) | une phrase | **§6** (retour non unitaire, schéma-blocs, régulation d'un four, adaptateur mal étalonné) ; méthode 3 ; EXO 09 |
| **Erreur de traînage** vis-à-vis de la consigne (C2) | tableau du §2 | **§7** (\(\varepsilon_v = a/K\), \(t_v = 1/K\), figure calculée de la poursuite d'une rampe) ; EXO 11 |
| Rapidité : temps de réponse à 5 %, **temps de montée**, **bande passante** (C2) | §4 (repères) | §4 (formules du 1er ordre, exemples 1er et 2e ordre chiffrés) ; EXO 10 |
| Démarche d'évaluation (C1) ; confronter modèle et mesures (B3) | méthode 5 | **§8** (convoyeur : précision contre amortissement, figure calculée, confrontation à un essai) ; Concours |
| Réglage des correcteurs (2ᵉ année) ; PD, PID, Ziegler-Nichols (hors programme) | non signalés (sauf PD, PID) | signalés ; section finale |

## Ajouts

- **Cours** : bloc programme ; §1 (temps de montée, exemple, erreur classique) ; §2 (théorème de la valeur finale, piège) ; §3 (poursuite/régulation, figure `pert`, superposition) ; §4 (exemples 1er et 2e ordre) ; §5 (encadré 2ᵉ année) ; **§6** écart et erreur (figure `capteur`) ; **§7** rampe (figure `rampe`) ; **§8** cahier des charges (figure `cdc`) ; section finale.
- **Méthodes** (5 → 9) : ajoutées 2 (théorème de la valeur finale), 3 (écart → erreur, retour non unitaire), 5 (erreur et retard de traînage), 7 (lire une réponse indicielle).
- **Exercices** (8 + concours → 11 + concours) : 03, 04, 07, 08 corrigés ; nouveaux EXO 09 (régulation de vitesse : écart, erreur, saturation, adaptateur), EXO 10 (deux réglages : t_r5 %, t_m, bande passante, traînage), EXO 11 (imprimante 3D : erreur et retard de traînage contre dépassement) ; Concours « convoyeur à bande » : précision, stabilité, réglage, rejet d'une charge, conclusion (PI de 2ᵉ année).
- **Cartes** (+10) : temps de montée, écart / erreur, retard de traînage, poursuite / régulation, superposition, dépassement rapporté à la valeur finale, rapidité d'un 1er ordre bouclé, effet du bouclage, limites du gain, piège de la valeur finale.

## Notations

\(\varepsilon\) (écart), \(\varepsilon_s\), \(\varepsilon_v\), \(t_v\), \(t_{r5\%}\), \(t_m\), \(D_1\), \(H_E\), \(H_D\), \(K_a\), \(K_c\), classe α, \(K\) (gain de la FTBO, noté \(K_{BO}\) dans `corr`), \(\omega_{c0}\), \(M_\varphi\). Convention de signe de la perturbation : soustraite (comme l'ancien cours et la vidéo `ch7` ; `sb` §4 l'ajoute, le signe est explicité dans chaque énoncé).

## Doutes / remarques

- Temps de montée : convention 10 %-90 % retenue (la plus courante), l'autre (premier passage à la valeur finale) est signalée.
- Cartes 11, 14, 18 (questions inchangées, en Unicode) : `flashPretty` mathématise des morceaux des **questions** (« \(\dfrac{1}{Ti} du\) correcteur », « correcteur \(I\) ») ; défaut d'affichage antérieur, non corrigé ici (une seule des deux faces modifiable).
- Le §5 garde le PI chiffré (« aperçu de 2ᵉ année ») parce que `corr-cours` §2 renvoie à ce chapitre pour les structures des correcteurs.
- Contrôles passés : `verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges` vides, aucune erreur JS (cours, méthodes, exercices ; captures du cours regardées) ; `corriger_cartes.py --essai`, `ajouter_cartes.py --essai` et rendu des cartes sans erreur.
