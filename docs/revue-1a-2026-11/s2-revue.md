# `sys2` (prefix `s2`) « Systèmes du 2e ordre » — mise au format de la 2ᵉ année (point 7), 2026-11-22

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `s2-cours.src.html` | cours (≈ 113 000 signes dont ≈ 77 000 de figures SVG) : bloc « AU PROGRAMME · PTSI », §1 à §8, « POUR ALLER PLUS LOIN · HORS PROGRAMME » ; 10 exemples traités chiffrés ; 8 figures (3 d'origine gardées, 5 nouvelles calculées) ; un programme Python exécuté |
| `s2-meth.src.html` | 10 méthodes (étapes, exemple éclair chiffré) + « Pièges classiques » |
| `s2-exos.src.html` | 11 exercices (★ à ★★★) + 1 « Concours PT » en 4 parties (10 questions) ; 2 figures calculées |
| `s2-cartes-corr.json` | 1 carte corrigée (réponse seule) |
| `s2-cartes-ajout.js` | 14 cartes ajoutées en fin de deck (30 → 44) |
| `s2-cours.tpl.html`, `s2-exos.tpl.html` + `s12_construire.py` | gabarits (`@@FIG:nom@@`, `@@ORIG:k@@`) |
| `s2_figs.py` → `s2_figs.json` | figures nouvelles (classes du site, aucune couleur en dur) |
| `s2_calculs.py`, `s2_calculs_meth.py`, `s2_calculs_exos.py` | vérification de tous les exemples, éclairs et corrigés (réponses exactes, abaque recalculé par recherche du dernier passage hors de la bande) |
| outils communs `s12_*` | voir `s1-revue.md` |

Reconstruire : `python3 s2_figs.py && python3 s12_construire.py`.

## Numérotation des §

Aucune renumérotation : §1 à §5 gardent leur numéro et leur titre (fiches, vidéo `video/slci/ch4`) ; §6 à §8 sont ajoutés à la suite. Le §3 (réponse fréquentielle) est gardé, avec renvoi à `bode` pour la méthode générale.

## Erreurs trouvées et corrigées

1. **Notation \(Q\) en double sens** : le cours (§3) et la méthode 4 appelaient \(Q\) le facteur de résonance \(\dfrac{1}{2\xi\sqrt{1 - \xi^2}}\), alors que la carte 21, l'EXO 06 et toute la physique du site (`oscill`, `rlc`, `filtres`) appellent \(Q = \dfrac{1}{2\xi}\) le facteur de qualité. Facteur de résonance renommé \(Q_r\) (cours, méthodes, exercices), encadré « Ne pas confondre » ajouté. **À aligner hors de ce lot** : `bode-exos` écrit encore \(Q\) pour le facteur de résonance (« \(Q = 2{,}55\) »).
2. **EXO 07** : figure dessinée à la main (courbe de Bézier qui n'est pas une réponse du 2ᵉ ordre, premier maximum placé à 0,71 s au lieu de 0,8 s, libellés de 10-11 px, classes `.svg-label` et couleurs `var(--accent)` en ligne) ; l'énoncé annonçait un « 2e passage par s(∞) à 1,6 s », alors que 1,6 s est l'instant du **premier minimum** (les passages par la valeur finale ont lieu à 0,49 s et 1,29 s). Figure recalculée, énoncé corrigé, Q4 de contrôle ajoutée ; dans le corrigé, \(2\xi\omega_0 = 3{,}01\) (et non 3,02) et numérateur 35,4 (et non 35,5).
3. **EXO 02** : \(\omega_0^2 = 283\) (et non 282).
4. **« < » brut dans des formules** (EXO 01 Q2, EXO 03 Q2, ancien concours A2 : « \(\xi = 0{,}3 < 1\) ») → `\lt`.
5. **Ancien « Concours PT »** : 3 questions d'application directe, notation \(\omega_n\) (le site écrit \(\omega_0\)) et « \(D\%\) » (le site écrit \(D_1\)). Gardé comme EXO 08 (★), notations alignées, questions ajoutées (premier maximum, temps de réponse, résonance) ; nouveau sujet concours.
6. **EXO 04, Q2** : « transition sous-amorti/critique optimale » ne justifiait rien ; explication réécrite (à \(\xi = 0{,}69\), le premier maximum dépasse de 5 % exactement : la sortie entre dans la bande à sa première montée et n'en sort plus).
7. **EXO 05** : « si la voiture passe sur un dos d'âne » n'est pas un échelon de l'entrée du modèle (force) → « on pose brusquement une charge sur la caisse » ; « un confort optimal vise \(\xi \approx 0{,}3\) » présenté comme un fait → reformulé (suspension plus souple) ; Q4 ajoutée (temps de réponse doublé).
8. **EXO 06, Q3** : « bande passante à −3 dB (\(\Delta\omega = \omega_0/Q\)) » confondait la largeur du pic de résonance (3 dB sous le maximum, \(\approx \omega_0/Q\)) et la bande passante du passe-bas (de 0 à \(1{,}55\,\omega_0\)) ; distinction faite, largeur vérifiée numériquement (\(1{,}003\times10^4\) rad/s).
9. **§5, pôle dominant** : présenté comme une notion de PTSI ; c'est une capacité de S3 (« Simplifier un modèle : pôles dominants et réduction de l'ordre ») → signalé « vu en 2ᵉ année », renvoi à `correcteurs` §1, complément en « Pour aller plus loin ».
10. **Carte 24** : « instabilité marginale » → « limite de stabilité, que l'on range avec les systèmes instables » (formulation du chapitre `stabilite`).
11. Manques par rapport au programme (voir le tableau) : allures des réponses impulsionnelle, à une rampe et à une sinusoïde (C2, S1), temps de montée et traduction d'un cahier des charges (C1, S2), validation d'un modèle (B3, S2).

## Couverture du programme (S1-S2) : avant → après

| Capacité (programme 2021) | Avant | Après |
|---|---|---|
| Modèle de connaissance, forme canonique, \(K\), \(\omega_0\), \(\xi\), pôles (B2, S1) | §1 (masse-ressort, RLC, pôles) | §1 + application numérique (quart de véhicule), exemple de lecture d'une fonction de transfert, figure des pôles dans le plan complexe, constantes de temps du cas apériodique, erreur classique |
| Expression de la réponse à un échelon (C2, S1) | §2 | §2 + démonstration des extremums et de \(D_1\), extremums successifs \(D_1^{\,k}\), exemple chiffré complet |
| Allures : impulsion, rampe, sinus en régime permanent (C2, S1) | ❌ (sinus seulement en Bode) | §6 : réponse impulsionnelle (formule, figure pour 5 valeurs de \(\xi\)), rampe (figure, écart de traînage \(2\xi a/\omega_0\), démonstration par la valeur finale), sinusoïde ; exemple d'un capteur |
| Réponse fréquentielle, Bode, résonance (C2, S2) | §3 | §3 gardé + exemple chiffré, bande passante à −3 dB (formule), \(Q_r\) / \(Q\), renvoi à `bode` |
| Modèle de comportement à partir d'une réponse (B2, S2) ; choix de l'essai (D2, S2) | §4 (méthode + suspension) | §4 + choix de l'essai, relevé calculé d'une nacelle de caméra (figure) identifié et contrôlé par le deuxième maximum, erreurs classiques |
| Critères : amortissement, dépassement relatif, temps de réponse, **temps de montée**, bande passante, erreur de traînage (C1, C2, S2) | \(D_1\), abaque | + table \(t_{r5\%}\,\omega_0\) et \(t_m\,\omega_0\) (§2), figure des grandeurs lues, bande passante (§3), traînage (§6), §7 « Traduire un cahier des charges » (tableau critère → contrainte, exemple complet jusqu'au réglage du gain) |
| Vérifier la cohérence du modèle (B3, S2) | ❌ | §8 : simulation par Euler (fonction `euler_ordre2` de `pynum`), effet du pas (Euler surestime le dépassement : 31,6° au lieu de 28,9° avec un pas de \(T_p/40\)) |
| Pôles dominants, réduction d'ordre (S3) | §5, comme exigible | §5 signalé « 2ᵉ année » ; justification en « Pour aller plus loin » |

## Contenu ajouté

**Cours.** Bloc « AU PROGRAMME · PTSI » ; §6 « Réponses à une impulsion, une rampe et une sinusoïde » ; §7 « Traduire un cahier des charges » ; §8 « Simuler et valider un modèle » ; « Pour aller plus loin » (effet d'un zéro : \(\dfrac{1 + 2p}{(1 + p)^2}\) dépasse de 13,5 % au régime critique ; réduction de l'ordre). Figures nouvelles : pôles dans le plan complexe ; grandeurs lues sur une réponse indicielle (\(D_1\), \(T_p\), \(t_m\), \(t_{r5\%}\)) ; relevé bruité d'une nacelle ; réponses impulsionnelles ; réponse à une rampe.

**Méthodes (5 → 10).** Gardées et complétées d'un exemple éclair : identifier \(K\), \(\omega_0\), \(\xi\) ; prévoir l'allure (+ valeurs remarquables) ; identifier sur un relevé (+ contrôle) ; Bode (\(Q_r\)) ; régler un gain. Nouvelles : lire l'abaque dans les deux sens ; traduire un cahier des charges ; rampe et impulsion ; passer de l'apériodique à deux premiers ordres et retour ; simuler par Euler.

**Exercices (7 + 1 « concours » → 11 + 1 concours).** EXO 01 à 07 corrigés (voir plus haut) ; EXO 08 : ancien concours ; nouveaux : EXO 09 capteur de déplacement (échelon, rampe, impulsion, sinusoïdes en \(\omega_0\) et \(3\omega_0\)), EXO 10 cahier des charges impossible à tenir avec un gain (dépassement ≤ 10 % ⇒ \(K \le 35{,}8\ \text{s}^{-1}\), traînage ⇒ \(K \geq 50\ \text{s}^{-1}\)), EXO 11 deuxième ordre apériodique (constante dominante, régime critique) ; **Concours PT** « antenne de suivi de satellites » : identification de la motorisation, réglage du gain (\(\xi = 0{,}69\)), saturation, confrontation à une réponse mesurée (figure calculée avec la constante électrique négligée par le modèle : \(\xi\) mesuré 0,60, temps de réponse 0,6 s au lieu de 0,32 s), erreur de traînage en poursuite et nécessité d'un correcteur PI.

**Cartes ajoutées (14).** Constantes de temps du cas apériodique ; extremums ; temps de montée (`val`) ; réponse impulsionnelle ; écart de traînage ; \(Q_r\) et \(Q\) ; \(\omega_r \lt \omega_p \lt \omega_0\) ; bande passante (`val`) ; \(\xi\) minimal pour 10 % et 5 % (`val`) ; valeurs de l'abaque (`val`) ; contrôle d'une identification ; Euler ; ordres de grandeur (`val`) ; effet d'un zéro (« Hors programme en PTSI : »).

## Notations

\(K\), \(\omega_0\), \(\xi\), \(\omega_p\), \(T_p\), \(t_1\), \(D_1\), \(D_k\), \(t_{r5\%}\), \(t_m\), \(\omega_r\), \(Q_r\) (facteur de résonance, nouveau nom), \(Q\) (facteur de qualité des physiciens), \(\omega_{BP}\), \(\varepsilon_v\) (écart de traînage, comme `precision`), \(\tau_1\), \(\tau_2\). Plus aucune trace de \(\omega_n\).

## Vérifications

- Tous les nombres recalculés (`s2_calculs*.py`), dont la table de l'abaque (\(t_{r5\%}\,\omega_0\)) et du temps de montée ; programme du §8 exécuté par `s12_tester_code.py`, sortie identique à celle affichée.
- `verif_src.py` : aucune erreur ni « attention » sur les trois panneaux.
- `apercu_src.py` (copie `revisions-an1`) à 390 et 1 440 px : `merr`, `brut`, `larges` vides, aucune erreur JS, pas de débordement de page ; plusieurs formules des corrigés passées en bloc ou raccourcies pour tenir à 390 px ; figures des exercices ramenées à 340 unités de large (comme `stat-exos`) : à 410, elles élargissaient la carte d'exercice au téléphone.
- Figures nouvelles regardées en clair et en sombre (planches `_tmp/pl_s2*.png`), cours regardé en situation à 1 440 px (captures).
- Cartes : `corriger_cartes.py s2 … --essai` (1 réponse) et `ajouter_cartes.py s2 … --essai` (30 → 44) sans erreur ; textes rendus sans erreur MathJax (`_tmp/s2-cartes-test.src.html`).

## Doutes et points à valider

1. **\(Q_r\)** : renommage choisi pour lever le double sens avec la physique ; `bode-exos` est à aligner (non modifié, hors de ce lot). La vidéo du chapitre ne nomme pas ce facteur.
2. **Notation \(t_{r5\%}\)** gardée (voir `s1-revue.md`, doute 1).
3. **Temps de montée** : définition 10 % → 90 % ; pour un système qui dépasse, certains sujets prennent le premier passage par la valeur finale (\((\pi - \arccos\xi)/\omega_p\)) : non introduit, pour garder une seule définition.
4. Le §5 (pôle dominant) est gardé à sa place (vidéo) mais signalé 2ᵉ année ; l'EXO 11 Q3 l'utilise en le signalant.
5. Cours long (≈ 113 000 signes, figures comprises).
