# Revue du chapitre `oscill` (prefix `osc`) — « Oscillateurs harmoniques » — 2026-11-22

Objet (point 4 de l'audit, lot 6 ; `docs/audit-2026-11/physique-1a.md` l. 26, 105, 126, 132-133 ; `audit-2026-11.md` §5) :
chapitre de 10 500 signes, 5 méthodes, 7 exercices, 25 cartes ; oscillateur amorti exposé trois fois (`rlc`, `oscill`,
`energie`) avec des τ différents. Décision : **`oscill` devient l'exposé de référence** de l'oscillateur amorti (Q, ω₀,
τ = 2Q/ω₀), `energie` y renvoie. Programme : PTSI 2021, partie 1.4 (l. 744-795), côté mécanique, avec 2.2 (pendule simple,
analogie) et 2.3 (petits mouvements).

## Fichiers produits (dans `AN1/`)
- `osc-cours.src.html` (131 ko ; 37 400 signes de texte, contre 10 500) — assemblé par `osc_construire.py` depuis
  `osc-cours.tpl.html` et `osc_figs.json` ;
- `osc-meth.src.html` (10 méthodes), `osc-exos.src.html` (11 exercices + 1 « Concours PT ») ;
- `osc-cartes-corr.json` (3 réponses corrigées), `osc-cartes-ajout.js` (14 cartes) ;
- scripts : `osc_figs.py` (9 figures ; temps de réponse à 5 % et périodes du pendule calculés avec odeint),
  `osc_calculs.py` (exemples du cours), `osc_calculs_meth.py`, `osc_calculs_exos.py` ; copies des anciens panneaux
  `osc_orig_{cours,meth,exos}.html`. Le panneau `osc-simu` n'est pas modifié (le cours cite ses réglages par défaut).

## Erreurs et incohérences trouvées
| Où | Problème | Correction |
|---|---|---|
| τ (audit) | trois conventions sur le site | ici τ = 2Q/ω₀ = 2m/α, enveloppe en e^(−t/τ), énergie en e^(−2t/τ) ; notice dédiée ; `energie` y renvoie |
| ξ (audit) | ξ pour l'amortissement | absent ; une seule mention en passerelle : « en SI, coefficient d'amortissement ξ = 1/(2Q) » (§5) |
| §7 (audit) | pont de Tacoma | **déjà nuancé** dans le dépôt ; repris au §10 (instabilité aéroélastique, pas résonance forcée) |
| Ancien §6, carte 17 | régime apériodique « retour monotone » | faux si la masse est lancée vers l'équilibre : « sans oscillation, au plus un passage par l'équilibre » (notice ; carte : réponse seule) |
| Carte 4 | isochronisme « vrai uniquement pour les oscillateurs harmoniques » (affirmation trop forte) | propriété de l'équation linéaire, perdue en général par un oscillateur non linéaire (réponse seule) |
| Carte 10 | \(E_p=\tfrac12kx^2\) « où x est l'écart à l'équilibre » (faux pour le ressort vertical) | \(\tfrac12k(\ell-\ell_0)^2\), allongement ; cas horizontal et vertical distingués (réponse seule) |
| Ancien EXO 06 (couplés) | « transfert complet » à 2π/Δω (126 s) ; hors programme non signalé | premier transfert complet à π/Δω ≈ 63 s, retour à 126 s ; titre « hors programme, pour aller plus loin » |
| Ancien concours | coefficient noté h, deux questions par partie | noté α ; devenu EXO 07 (question sur l'amplitude après une pseudo-période ajoutée) |
| Notation | pseudo-pulsation notée ω dans `rlc`, comme la pulsation d'excitation | notée ω_p ici (dit dans le cours, §6) |

## Couverture du programme : avant → après
| Capacité exigible (1.4, sauf mention) | Avant | Après |
|---|---|---|
| Établir, reconnaître, résoudre l'équation de l'oscillateur harmonique (CI) | masse-ressort | §1 (reconnaître ẍ + a x = b, contre-exemple a < 0, LC), §2 (CI, amplitude et phase), méthodes 1, 2, EXO 01, 2 cartes |
| Amplitude, phase, période, fréquence, pulsation | partiel | §2 (figure annotée calculée, quadrature de la vitesse), carte |
| Pendule simple : analogie dans l'approximation linéaire (2.2) ; ressort vertical | §3, §4 | §3 (renvoi `mecpt` §11 pour l'équation, suspension, Foucault, Δℓ), §11, EXO 02, 03, carte |
| Bilan énergétique, stockage et dissipation | §5 | §4 (E_c, E_p à 2ω₀, équation par l'énergie, portrait de phase), §5 (dE_m/dt, Q ≈ 2πE/ΔE démontré), méthode 3, EXO 04, 06, 2 cartes |
| Forme canonique, ω₀ et Q ; prévoir l'évolution par l'énergie | §6 | §5 (identification, ordres de grandeur de Q, analogue RLC), méthode 4, EXO 05, 07, 2 cartes |
| Nature de la réponse selon Q ; réponse détaillée (racines du polynôme) en régime libre ou échelon | régimes cités, sans solution | §6 (polynôme, trois solutions, lâcher sans vitesse, figure calculée), §7 (échelon, ressort vertical), méthodes 5, 6, EXO 09, 2 cartes |
| Durée du transitoire selon Q | absent | §7 (3τ, 3/(Qω₀), minimum vers Q ≈ 0,7 ; figure calculée t₅% ω₀ en fonction de Q), EXO 09, carte |
| Relevés expérimentaux du transitoire | absent | §6 (décrément logarithmique, exemple), méthode 7, EXO 08, concours B, carte |
| Similitude mécanique / électrique | table | §8 (tableau complet avec énergies, puissances, τ ; circuit jumeau), méthode 8, EXO 05 |
| Régime forcé en complexes | équation complexe | §9 (amplitude complexe réduite, trois limites, exemple), méthode 9, carte |
| Acuité de la résonance et Q ; ω₀ et Q sur des graphes d'amplitude et de phase | énoncés | §10 (résonance en vitesse, Δω = ω₀/Q démontré, résonance en élongation, figures amplitude-phase et vitesse calculées, méthodes de mesure), méthode 10, EXO 10, concours C, 2 cartes |
| Effet des termes non linéaires (2.3, capacité numérique, avec `energie` §10) | absent | §11 (non-isochronisme, figure T/T₀ par odeint et valeur exacte, harmonique 3, horloge), EXO 03 Q4 |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 11 sections + « Pour aller plus loin ») : §1 Modèle et équation ; §2 Solution et
grandeurs caractéristiques ; §3 Ressort vertical et pendule simple ; §4 Énergie et portrait de phase ; §5 Forme canonique
et facteur de qualité ; §6 Régime libre : trois régimes ; §7 Durée du transitoire, réponse à un échelon ; §8 Analogie
électromécanique ; §9 Régime sinusoïdal forcé ; §10 Résonances en vitesse et en élongation ; §11 Limites du modèle
linéaire ; hors programme : période exacte et Borda, frottement solide, oscillateurs couplés. 12 exemples traités chiffrés,
11 notices, 1 tableau, 4 démonstrations ou calculs dépliables, 9 figures SVG calculées (masse-ressort ; x(t) annoté ;
ressort vertical ; énergies et portrait de phase ; trois régimes ; durée du transitoire en fonction de Q ; amplitude et
phase de l'élongation ; vitesse et bande passante ; période du pendule selon l'amplitude), vérifiées en clair et en sombre.

**Méthodes** (10) : reconnaître l'oscillateur et ω₀ ; x(t) par les CI ; équation par l'énergie (tube en U) ; forme
canonique ; régime libre détaillé ; échelon ; relevé expérimental ; analogie ; régime forcé en complexes ; courbe de
résonance. Les 5 anciennes méthodes et les pièges sont repris.

**Exercices** (12) : 01 à 05 anciens (01-04 complétés d'une question ; 05 avec τ) ; 06 décroissance de l'énergie (ancien
EXO 03 d'`energie`, notations τ et ω_p, question ajoutée sur Q ≈ 2πE/ΔE) ; 07 libre puis amorti (ancien concours) ;
08 exploiter un enregistrement (nouveau) ; 09 régler l'amortissement d'une balance (nouveau, temps de réponse) ; 10 lire une
courbe de résonance mesurée (nouveau, tableau calculé pour Q = 8) ; 11 oscillateurs couplés (ancien 06, corrigé, hors
programme) ; **Concours PT « La suspension d'une machine à laver »** (A équilibre, ω₀ ; B Q par le décrément, α ;
C balourd en m_b e ω², amplitude, maximum au-dessus de ω₀, force transmise au sol amplifiée à 240 tr/min et réduite à 9 %
à 1 200 tr/min ; D puissance dissipée 33 W, traversée de la résonance).

**Cartes** : 25 → 39 (14 ajoutées à la fin, formules en `\\( … \\)` : grandeurs de la sinusoïde, amplitude et phase par les
CI, énergies à 2ω₀, portrait de phase, ressort vertical et Δℓ, régime pseudo-périodique avec τ et ω_p, polynôme
caractéristique, décrément, durée du transitoire, interprétation énergétique de Q, ordres de grandeur de Q, amplitude
complexe, bande passante, mesure de ω₀ et Q) ; 3 réponses corrigées (questions inchangées).

## Contrôles
`verif_src.py` sans erreur ni attention sur les trois panneaux ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`,
`larges` vides, aucune erreur JS ; captures relues (figures en clair et en sombre) ; `corriger_cartes.py --essai`
(3 réponses) et `ajouter_cartes.py --essai` (25 → 39) sans erreur ; rendu MathJax des cartes ajoutées : 0 erreur ; tous les
nombres recalculés (`osc_calculs*.py`, sympy pour les solutions exactes, odeint pour les temps de réponse et les périodes).

## Notations
\(\omega_0\), \(f_0\), \(T_0\), \(X_m\), \(\varphi\) ; \(-\alpha\vec v\) ; \(Q=m\omega_0/\alpha\), \(\tau=2Q/\omega_0=2m/\alpha\) ;
pseudo-pulsation \(\omega_p\), pseudo-période \(T_p\) ; décrément \(\delta\) ; \(u=\omega/\omega_0\), \(\underline X_m\),
\(\underline V_m\), \(\Delta\omega=\omega_0/Q\) ; analogie \(m\leftrightarrow L\), \(\alpha\leftrightarrow R\), \(k\leftrightarrow1/C\).

## Doutes, remarques pour l'intégration
- **ξ** : la seule occurrence est la passerelle vers la SI (§5) ; à retirer si l'on veut zéro ξ en physique.
- **ω_p** : `rlc` note la pseudo-pulsation ω ; à aligner lors de la révision de `rlc` (dont les §3-6 pourraient renvoyer ici).
- **Titre** : « Oscillateurs harmoniques » couvre mal l'amorti et le forcé ; proposition : « Oscillateurs mécaniques : libres,
  amortis, forcés » (mobLabel inchangé).
- Les exercices 01 à 04 restent faciles et proches : gardés (règle « garder les exercices justes »).
- L'EXO 10 donne des mesures « exactes » (calculées pour Q = 8) : on pourrait les bruiter pour un TP plus réaliste.
