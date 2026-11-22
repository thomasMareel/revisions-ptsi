# `stabilite` (prefix `stab`) — « Stabilité des systèmes asservis », mise au format de la 2ᵉ année (point 7), 2026-11-22

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `stab-cours.src.html` | cours complété (≈ 84 000 car.) : bloc « AU PROGRAMME · PTSI », §1 à §8, « POUR ALLER PLUS LOIN · HORS PROGRAMME » ; 12 exemples traités, 5 figures (2 d'origine, 3 nouvelles calculées), 2 démonstrations dépliables |
| `stab-meth.src.html` | 9 méthodes (étapes + exemple éclair chiffré) + « Pièges classiques » (5 méthodes sans exemple avant) |
| `stab-exos.src.html` | 10 exercices + « Concours PT » en 4 parties (A à D, 9 questions) |
| `stab-cartes-corr.json` (écrit par `stab_cartes.py`) | 5 cartes corrigées (réponse seule) |
| `stab-cartes-ajout.js` | 11 cartes ajoutées en fin de deck (30 → 41) |
| `stab-cours.tpl.html`, `stab-exos.tpl.html` | gabarits assemblés par `bsp_construire.py` |
| `stab_figs.py` → `stab_figs.json` | figures calculées `revers`, `poles`, `axe` |
| `stab_calculs.py`, `stab_calculs_meth.py`, `stab_calculs_exos.py` | vérification numpy / sympy / scipy de tous les exemples, éclairs et corrigés |

Outils communs : voir `bode-revue.md`. Reconstruire : `python3 stab_figs.py && python3 bsp_construire.py stab`.

## Numérotation des §

**Inchangée** pour §1 à §5 (vidéo `video/slci/ch6`, renvois de `rsx`, `mph`, `snumx`, `slci`). Nouveaux : §6 à §8. Le bloc dépliable « Critère de Routh » du §2 et la phrase sur le lieu de Nyquist du §3 sont déplacés dans la section finale.

## Erreurs trouvées et corrigées

1. **Hors-programme présenté comme exigible** : le programme exclut les critères de **Routh** et de **Nyquist** (des deux années). La condition de degré 3 \(a_2a_1 \gt a_3a_0\) (cas particulier de Routh), donnée au §2 comme une propriété du cours, est maintenant signalée « Hors programme en PTSI, utilisable si l'énoncé la rappelle » ; la méthode au programme pour le gain limite (pôles imaginaires purs, \(p = j\omega\)) est enseignée à sa place (§2, méthode 2, EXO 04, Concours B1). Énoncé de Nyquist (§3) déplacé en fin de cours. EXO 04 (Routh) refait par les pôles imaginaires purs, Routh en dernière question signalée.
2. **EXO 07** : \(u = (-1 + \sqrt5)/0{,}5\) évalué à 1,236 au lieu de **2,472** : \(\omega_c\) valait 1,57 rad/s (et non 1,11) et la marge de phase **51,8°** (et non 60,9°) ; Q4 annonçait « marge voisine de 55° » avec un PI de \(\tau_i \approx 9\) s : refait (\(\tau_i \approx 6\) s, \(M_\varphi \approx 46°\)). Notations \(L(p)\), \(\Delta\phi\), \(\omega_c\) remplacées par \(H_{BO}\), \(M_\varphi\), \(\omega_{c0}\) ; Q3-Q4 signalées « vu en 2ᵉ année ».
3. **EXO 06** : « par essais, ω = 1,3 … ≈ 0 dB » puis \(M_\varphi \approx 30{,}2°\) : valeurs approchées fausses (\(\omega_{c0} \approx 1{,}24\), \(M_\varphi \approx 31{,}7°\)) ; l'énoncé disait les deux marges insuffisantes alors que \(M_G = 14{,}8\) dB convient ; Q3 laissait croire que l'avance de 55° suffit sans dire que le gain du correcteur (+10 dB) déplace \(\omega_{c0}\). Corrigé, Q2-Q3 signalées 2ᵉ année.
4. **EXO 01** : « Re < 0 » écrits avec des « < » bruts (avalés par l'extraction de texte) : réécrits en toutes lettres. Titre de l'EXO 02 faux (« système du 1er ordre en BO » pour un intégrateur suivi d'un premier ordre) : corrigé.
5. **Concours** trop mince (lecture de deux nombres) : gardé comme partie A, complété en vrai sujet en 4 parties.
6. **Cartes** : 4 (« un 1er ou 2e ordre en BO ne peut pas être instable en BF » : faux pour \(K/p^2\), conditions manquantes) ; 10 (condition nécessaire sur les coefficients marquée hors programme alors qu'elle découle de la position des pôles) ; 14 (« Hors programme… analyse de Nyquist complète » : faux, les pôles de la FTBF suffisent, exemple \(2/(p-1)\)) ; 20 (\(\omega_{c0}\) « c'est la bande passante » : imprécis) ; 23 (réponse confuse) — réponses corrigées, questions inchangées.

## Couverture du programme (S2) : avant → après

| Capacité (programme SII 2021) | Avant | Après |
|---|---|---|
| Stabilité : définition (C2) | §1 | §1 + exemples (pôles d'une FTBF, BO instable stabilisée), erreur classique |
| Position des pôles dans le plan complexe (C2) | §1 (condition) | §1, §2 (coefficients, démonstration, pôles imaginaires purs), **§6** (figure calculée plan complexe + réponses impulsionnelles, ω₀ = |p|, cos θ = ξ) |
| Amortissement (C2) ; dépassement relatif (C1) | règle ξ ≈ Mφ/100 | §4, **§6** (D₁ en fonction de ξ, tableau exact Mφ → ξ → D₁, exemple des pôles −2 ± 3j) |
| Marges de stabilité (C2) | §3, §4 | §3 (exemple et figure calculée du critère du revers, conditions d'emploi), §4 (calcul pas à pas, erreurs classiques), §5 (gain limite, retard) |
| Influence du gain, retard, constantes de temps négligées | §5 | §5 + **§7** (tableau des cas types, \(K_{lim} = 1/\tau_1 + 1/\tau_2\) démontré, double intégrateur stabilisé par un zéro) |
| Démarche d'évaluation des performances (C1) | ❌ | **§8** (axe asservi : \(K_{lim}\), M_G, Mφ, réglage, effet d'un retard de calculateur, figure calculée) |
| Routh, Nyquist, Black (hors programme des deux années) | §2 (degré 3 présenté comme exigible), §3 | signalés, regroupés en fin de cours |

## Ajouts

- **Cours** : bloc programme ; exemples aux §1, §2 (deux), §3, §4, §5 (deux) ; figures `revers` (Bode de \(K/(1+p)^3\) pour K = 2, 8, 10, cohérent avec la figure d'origine du §1), `poles`, `axe` ; §6, §7, §8 ; section hors programme (Routh, Nyquist, Black, lieu des racines).
- **Méthodes** (5 → 9) : ajoutées 2 (gain limite par \(p = j\omega\)), 3 (critère du revers), 8 (pôles, amortissement, dépassement), 9 (exigences de stabilité d'un cahier des charges).
- **Exercices** (7 + concours → 10 + concours) : EXO 04 refait, 06 et 07 corrigés ; nouveaux EXO 08 (pôles, amortissement, dépassement), EXO 09 (lévitation : boucle ouverte instable, gain minimal), EXO 10 (commande à distance : retard maximal, apparition d'un gain limite) ; Concours « antenne » : lecture d'un relevé, gain limite par \(p = j\omega\), réglage Mφ = 45°, retard d'une liaison radio et nouveau réglage.
- **Cartes** (+11) : gain limite par les pôles imaginaires purs, \(K_{lim} = 1/\tau_1 + 1/\tau_2\), pôles et réponse, dépassement, tableau Mφ/ξ/D, \(K/(p^2(1+\tau p))\), conditions du revers, effet d'un retard, marge exacte vs asymptotique, processus instable, définition par la réponse.

## Notations

\(H_{BO}\), \(H_{BF}\), \(\omega_{c0}\), \(\omega_\pi\), \(M_\varphi\), \(M_G\), \(K_{lim}\), \(T_{max}\), ξ, ω₀, \(D_1\) (comme `sys2` et `corr`), \(t_{r5\%}\). Notations des vidéos (`video/slci/ch6`) respectées (la vidéo énonce la condition de degré 3 ; le cours la garde, signalée hors programme).

## Doutes / remarques

- Cartes 4, 20, 23 (questions inchangées, en Unicode) : `flashPretty` mathématise des morceaux de leurs **questions** (« \(1er\) ou \(2e\) ordre », « \(0 dB ωc0\) », « \((p\) en BO) ») ; défaut d'affichage antérieur, non corrigé (la consigne interdit de retoucher question et réponse d'une même carte).
- Règle « ξ ≈ Mφ/100 » : exacte à 0,03 près pour la FTBO \(K/(p(1+\tau p))\) entre 45° et 70° ; repère seulement au-delà.
- Contrôles passés : `verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges` vides, aucune erreur JS (cours, méthodes, exercices ; captures du cours regardées) ; `corriger_cartes.py --essai`, `ajouter_cartes.py --essai` et rendu des cartes sans erreur.
