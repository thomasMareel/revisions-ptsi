# `sys1` (prefix `s1`) « Systèmes du 1er ordre » — mise au format de la 2ᵉ année (point 7), 2026-11-22

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `s1-cours.src.html` | cours (≈ 94 000 signes dont ≈ 55 000 de figures SVG) : bloc « AU PROGRAMME · PTSI », §1 à §8, « POUR ALLER PLUS LOIN · HORS PROGRAMME » ; 13 exemples traités chiffrés ; 9 figures (3 d'origine gardées, 6 nouvelles calculées) ; un programme Python exécuté |
| `s1-meth.src.html` | 10 méthodes (étapes, exemple éclair chiffré) + « Pièges classiques » |
| `s1-exos.src.html` | 11 exercices (★ à ★★★) + 1 « Concours PT » en 4 parties (12 questions, programme Python exécuté) |
| `s1-cartes-corr.json` | 4 cartes corrigées (réponse seule) |
| `s1-cartes-ajout.js` | 15 cartes ajoutées en fin de deck (29 → 44) |
| `s1-cours.tpl.html` + `s12_construire.py` | gabarit (`@@FIG:nom@@` : figure nouvelle, `@@ORIG:k@@` : k-ième figure du panneau d'origine) |
| `s1_figs.py` → `s1_figs.json` | figures nouvelles (classes du site, aucune couleur en dur), données de mesure simulées avec graine fixe |
| `s1_calculs.py`, `s1_calculs_meth.py`, `s1_calculs_concours.py` | vérification numérique de tous les exemples, éclairs et corrigés |
| `s12_base.py`, `s12_svgk.py`, `s12_harness.py`, `s12_planche.py`, `s12_tester_code.py`, `s12_cartes_test.py`, `s12_deborde.js` | outils communs aux deux chapitres (réponses du 2ᵉ ordre, rendu des figures en clair et sombre, exécution des programmes du panneau et comparaison à la sortie affichée, page d'essai des cartes, recherche de débordement) |
| `s1_orig_*.html` | copies des panneaux d'origine |

Reconstruire : `python3 s1_figs.py && python3 s12_construire.py`.

## Numérotation des §

Aucune renumérotation : §1 à §6 gardent leur numéro et leur titre (fiches « Voir dans le cours », vidéo `video/slci/ch3`) ; §7 et §8 sont ajoutés à la suite. Le §4 (réponse fréquentielle), que suit la vidéo, est gardé tel quel et renvoie au chapitre `bode` pour la méthode générale.

## Erreurs trouvées et corrigées

1. **Cours, tableau du §1** : le « réservoir linéarisé » était présenté comme un premier ordre ordinaire ; la linéarisation autour d'un point de fonctionnement est au programme de S3. Ligne marquée « (2ᵉ année) », démarche détaillée en « Pour aller plus loin ».
2. **EXO 03, Q2** : « \(\omega < 100\) » écrit avec un « < » brut dans la formule → `\lt`.
3. **EXO 04** : l'énoncé prenait pour sortie « la température en °C » alors que \(K = 1/(hS)\) relie la puissance à l'**écart** de température ; le corrigé donnait \(\tau\) et \(K\) sans le bilan. Énoncé corrigé (sortie \(T - T_0\)), bilan d'énergie écrit, température à \(t = \tau\) ajoutée (avec le piège des 63 %).
4. **Deux exercices « Concours PT »** de 2 et 3 questions (application directe), sans parties véritables : gardés comme EXO 07 (★) et EXO 08 (★★, complété : comparaison des temps de réponse, gain pour 2 % d'écart, limites) ; nouveau sujet concours.
5. **Carte 3** (« 99 % … t ≈ 5τ ») : \(\tau\ln 100 = 4{,}6\,\tau\) ; réponse précisée (99,3 % à \(5\tau\)).
6. **Carte 12** : deux premiers ordres en série ne donnent « pas nécessairement un 2e ordre canonique » — faux : c'est toujours un deuxième ordre canonique de \(\xi \geq 1\) (apériodique). Réponse corrigée.
7. **Carte 13** : « moteur DC à basse vitesse (avec frottement dominant) » — la condition est que l'inductance soit négligeable, pas la vitesse. Réponse corrigée.
8. **Carte 17** : « Pas d'erreur statique en BO : la sortie atteint exactement KE » — trompeur (la sortie n'égale l'entrée que si \(K = 1\)) ; réponse réécrite (l'écart concerne un système asservi ; écart \(1/(1 + K_cK)\) une fois bouclé).
9. Manques par rapport au programme (voir le tableau) : temps de montée (critère S2 absent de tout le site), choix de l'essai (D2), validation d'un modèle (B3), modèles de comportement « retard » et « intégrateur » (B2, S2), allure de la réponse à une sinusoïde dans le temps (C2, S1).

## Couverture du programme (S1-S2) : avant → après

| Capacité (programme 2021) | Avant | Après |
|---|---|---|
| Modèle de connaissance, forme canonique, gain, constante de temps, pôle (B2, S1) | §1 (tableau, sans exemple) | §1 + exemple de mise sous forme canonique, exemple chiffré du moteur à courant continu, démonstration, erreur classique |
| Signaux canoniques : échelon, rampe, impulsion, sinusoïde (B2, S1) | §2, §3, §4 | idem, chacun avec un exemple chiffré |
| Expression de la réponse à un échelon (C2, S1) | §2 | §2 + instants \(t_x\), table, exemple d'un four partant de 20 °C, erreur classique (63 % de la variation) |
| Allures : impulsion, rampe, sinus en régime permanent (C2, S1) | §3 (impulsion en une phrase), sinus seulement en Bode | §3 (figure de la réponse impulsionnelle, impulsion réelle d'aire \(A\), exemple de la sonde en retard) ; §4 (figure temporelle de la réponse à une sinusoïde, exemple chiffré : amplitude × 0,77, retard 6,7 s) |
| Réponse fréquentielle, Bode réel et asymptotique (C2, S2) | §4 | §4 gardé, renvoi au chapitre `bode` (§2, §3) |
| Modèle de comportement à partir d'une réponse temporelle ou fréquentielle (B2, S2) | §5 (méthodes + moteur) | §5 + relevé calculé d'une étuve (figure) identifié pas à pas ; §7 : tableau des allures (gain, intégrateur, 1er ordre, 1er ordre retardé, intégrateur + 1er ordre, 2e ordre), premier ordre retardé (figure, exemple), intégrateur + premier ordre (figure, exemple) |
| Choisir les entrées à imposer pour identifier (D2, S2) | ❌ | §5 « Choisir l'essai » ; concours B1 |
| Vérifier la cohérence du modèle par confrontation (B3, S2) | ❌ | §8 : simulation par Euler (même fonction `euler` que `pynum` et `premierordre`), essai de validation différent (figure), écart chiffré, erreur de méthode |
| Critères : temps de réponse, temps de montée, bande passante (C1/C2, S2) | \(t_{r5\%}\), bande passante | + temps de montée \(t_m = \tau\ln 9\) (§2) |
| Écart statique / de traînage d'un premier ordre bouclé (C2, S2) | §6 (formules) | §6 + exemples chiffrés (boucle de vitesse du moteur avec saturation de la commande, axe positionné et écart de traînage) |
| Linéarisation (S3), régression (traitement de données) | dans le tableau, sans mention | « Pour aller plus loin » |

## Contenu ajouté

**Cours.** Bloc « AU PROGRAMME · PTSI » ; §7 « Reconnaître un modèle de comportement » ; §8 « Valider un modèle » ; « Pour aller plus loin » (linéariser un réservoir, régression). Figures nouvelles : réponse impulsionnelle ; réponse temporelle d'un capteur à une sinusoïde ; relevé bruité d'une étuve avec la lecture à 63 % ; premier ordre retardé ; intégrateur et premier ordre (asymptote) ; validation chauffe puis refroidissement (mesures et modèle simulé par Euler). Les données « mesurées » sont simulées : vrai système à deux constantes de temps (144 s et 6 s pour la sonde) plus un bruit de 0,15 K, d'où un départ arrondi et des écarts systématiques que le cours exploite.

**Méthodes (5 → 10).** Gardées et complétées d'un exemple éclair : forme canonique, réponse indicielle, identification, Bode, rampe (+ impulsion). Nouvelles : raisonner en variations autour d'un équilibre ; réponse à une sinusoïde ; identifier un premier ordre retardé ou un intégrateur + premier ordre ; boucler un premier ordre (avec vérification de la commande initiale) ; simuler et valider un modèle.

**Exercices (6 + 2 « concours » → 11 + 1 concours).** EXO 01 à 06 gardés (relus, rédaction des corrigés étoffée ; EXO 05 : Q4 sur la forme canonique du 2ᵉ ordre, \(\xi = 1{,}34\)) ; EXO 07, 08 : anciens « concours » ; nouveaux : EXO 09 convoyeur partant d'un équilibre non nul (tableau de mesures, erreur classique chiffrée), EXO 10 échangeur avec retard de transport (comparaison avec un modèle sans retard, phase en régime sinusoïdal), EXO 11 axe de positionnement (intégrateur + premier ordre, puis boucle de position du 2ᵉ ordre, \(\xi = 1\)) ; **Concours PT** « couveuse néonatale » : modèle de connaissance (\(C\), \(G\)), identification et validation sur un relevé, sonde de température (écart de traînage, simplification), régulation proportionnelle (écart statique, saturation à 200 W : 343 s au lieu des 57 s du modèle linéaire), programme Python avec saturation (sortie vérifiée).

**Cartes ajoutées (15).** Temps de montée ; instant d'une fraction de la variation ; 63 % de la variation ; réponse impulsionnelle ; lien impulsion / échelon / rampe ; retard en régime sinusoïdal ; premier ordre retardé ; intégrateur + premier ordre ; premier ordre ou deuxième ordre apériodique ; choix de l'essai ; Euler ; validation sur un autre essai ; ordres de grandeur de \(\tau\) (`val`) ; limite d'un grand gain (saturation) ; linéarisation (« Hors programme en PTSI (vu en 2ᵉ année) : »).

## Notations

\(K\), \(\tau\), \(E_0\), \(t_{r5\%}\) (dite aussi \(t_{5\%}\), comme dans la vidéo), \(t_m\) (temps de montée 10 % → 90 %), \(\omega_c = 1/\tau\), \(K_c\), \(\tau'\), \(T\) (retard pur), \(\xi\), \(\omega_0\) (renvois au 2ᵉ ordre). Mêmes notations que `slci`, `bode`, `precision`, `correcteurs`.

## Vérifications

- Tous les nombres recalculés (`s1_calculs*.py`) ; les programmes Python du cours (§8) et du concours (D4) exécutés par `s12_tester_code.py`, sortie identique à celle affichée.
- `verif_src.py` : aucune erreur ni « attention » sur les trois panneaux.
- `apercu_src.py` (copie `revisions-an1`) à 390 et 1 440 px : `merr`, `brut`, `larges` vides, aucune erreur JS, pas de débordement de page (cours, méthodes, exercices).
- Figures nouvelles regardées en clair et en sombre (`s12_harness.py`, planches `_tmp/pl_s1*.png`).
- Cartes : `corriger_cartes.py s1 … --essai` (4 réponses) et `ajouter_cartes.py s1 … --essai` (29 → 44) sans erreur ; textes rendus sans erreur MathJax (`_tmp/s1-cartes-test.src.html`).

## Doutes et points à valider

1. **Notation du temps de réponse** : la consigne cite \(t_{5\%}\) ; tout le site (`s1`, `s2`, `precision`, `correcteurs`, `mph`, cartes : ≈ 60 occurrences) écrit \(t_{r5\%}\), la vidéo « t₅% ». J'ai gardé \(t_{r5\%}\) et ajouté « noté aussi \(t_{5\%}\) » dans la définition (§2) ; un changement global serait à faire partout à la fois.
2. **Temps de montée** : le programme ne le définit pas ; j'ai pris la définition usuelle 10 % → 90 %. Il n'était traité nulle part sur le site.
3. Le §4 (Bode du premier ordre) est gardé en entier parce que la vidéo du chapitre le suit ; il recoupe en partie `bode` §2.
4. Programme : « les transformées inverses de Laplace ne sont pas au programme » ; les calculs par éléments simples du §2-§3 sont gardés (ils étaient dans le cours et la vidéo), présentés comme justifications.
5. Cours long (≈ 94 000 signes avec figures), dans la fourchette des chapitres récents (`stat`, `liaisons`).
