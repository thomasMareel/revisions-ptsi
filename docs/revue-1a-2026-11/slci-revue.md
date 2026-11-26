# `slci` (prefix `slci`) « SLCI : modélisation et transformée de Laplace » — mise au format de la 2ᵉ année (point 7), 2026-11-22 → 2026-11-26

Travail commencé le 2026-11-22 par un premier rédacteur (interrompu avant le compte rendu), repris, contrôlé et terminé le 2026-11-26 : tous les calculs refaits (`slci_calculs.py`, `slci_calculs_exos.py`, `slci_code.py`), chaque figure regardée en clair et en sombre, contrôles de `CONSIGNES-1A.md` relancés sur les fichiers finaux, état des cartes simulé avec le vrai `flashLoadState` du site.

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `slci-cours.src.html` | cours (≈ 100 000 signes dont ≈ 42 000 de figures SVG) : bloc « AU PROGRAMME · PTSI », §1 à §8 ; 16 exemples traités chiffrés ; 6 figures (3 d'origine gardées, 3 nouvelles calculées) ; un programme Python exécuté |
| `slci-meth.src.html` | 10 méthodes (étapes + exemple éclair chiffré) + « Pièges classiques » |
| `slci-exos.src.html` | 11 exercices (★ à ★★★) + 1 « Concours PT » en 3 parties (A, B, C ; 7 questions) |
| `slci-cartes-corr.json` | 18 cartes corrigées (voir plus bas) |
| `slci-cartes-ajout.js` | 15 cartes ajoutées en fin de deck (37 → 52) |
| `slci-cours-ajouts.tpl.html` + `slci_construire.py` | blocs ajoutés au panneau d'origine (`@@BLOC:…@@`), figures `@@FIG:…@@`, sorties de programme `@@CODE:…@@` |
| `slci-exos-ajouts.tpl.html` + `slci_construire_exos.py` | exercices ajoutés au panneau d'origine |
| `slci_figs.py` → `slci_figs.json` | 3 figures nouvelles (classes du site, aucune couleur en dur), via `slsb_svgk.py` |
| `slci_code.py` → `slci_code.json` | exécute le code du §8 et la simulation de la suspension ; sorties recopiées telles quelles |
| `slci_calculs.py`, `slci_calculs_exos.py` | vérification (sympy, numpy) de tous les exemples, éclairs et corrigés |
| `slci_cartes.py` | produit `slci-cartes-corr.json` à partir du deck actuel |
| `slci_orig_*.html` | panneaux d'origine (identiques au site `revisions-an1` du 2026-11-26) |

Reconstruire : `python3 slci_figs.py && python3 slci_code.py && python3 slci_construire.py && python3 slci_construire_exos.py`.

## Numérotation des §

**Aucune renumérotation** : §1 à §5 gardent leur numéro et leur titre (fiches « Voir dans le cours », vidéo `video/slci/ch1` de l'onglet Vidéos, renvoi de `sys1` à `slci` §5). §6, §7 et §8 sont ajoutés à la suite. Les panneaux `-video`, `-simu` et `-flash` ne sont pas touchés.

## Erreurs trouvées et corrigées

Le cours d'origine (5 sections) ne contenait pas d'erreur de calcul ; ses défauts étaient de programme et de présentation :

1. **Hors-programme présenté comme exigible** : non-linéarités (limites de validité d'un modèle, S4) et linéarisation autour d'un point de fonctionnement (S3) au §1 ; décomposition en éléments simples et transformée inverse au §4 (le programme les exclut : « La résolution d'équations différentielles et les transformées inverses de Laplace ne sont pas au programme ») ; pôle dominant au §4 (S3). → encadrés « Hors programme en PTSI (vu en 2ᵉ année) » / « Hors programme (pour aller plus loin) » ; le §4 garde ses trois exemples (ils montrent d'où viennent les réponses-types) mais dit clairement ce qui est exigible (lien pôles ↔ allure).
2. **Démonstration du §2** : formule en ligne trop large pour un téléphone → passée en bloc. Même chose dans les corrigés des EXO 01 à 04.
3. **Méthodes 3 (décomposition) et 5 (linéarisation)** présentées comme des savoir-faire du chapitre → titre « (hors programme, pour aller plus loin) » / « (vu en 2ᵉ année) ».
4. **Exercices** : EXO 03 et 04 (décomposition) et EXO 06 (linéarisation) signalés hors programme dans leur titre. Le « Concours PT » n'avait que deux parties et 5 questions d'application → partie C ajoutée (puissance modulée, régime sinusoïdal, superposition, retard en fréquentiel), difficulté ★★★.
5. **Cartes** (18 corrections, détail plus bas) : 4 réponses fausses ou trompeuses (5 : « gain sans dimension » ; 7 : réponse incompréhensible ; 15 : énoncé du théorème de la valeur finale ; 22 : « toujours associer à un gain ou un PD ») ; 2 réponses imprécises (11 : « fréquence » pour une pulsation ; 3 : formules de boucle fermée embrouillées) ; 7 questions et 3 réponses **mal rendues** par `flashPretty` (« système \(du 2e\) ordre » composé en italique mathématique, « gain \(= −3 dB,\) », « \(−20log(2ξ) dB\) ») ; hors-programme non signalé (26, 27, 35 ; correcteur PI, 2ᵉ année : 23, 24).

## Couverture du programme (S1-S2) : avant → après

| Capacité (programme SII 2021) | Avant | Après |
|---|---|---|
| SLCI, causalité (B2, S1) | §1 : définition des SLCI ; causalité absente (seulement « fonction causale ») | §1 : causalité définie et justifiée (\(m \leq n\)), exemple « reconnaître un SLCI » (5 cas), EXO 07 |
| Modélisation par équations différentielles (B2, S1) | §3 (une équation donnée) | §6 « Établir un modèle de connaissance » : méthode, RLC, suspension, rotor (exemples chiffrés), erreurs classiques, ordres de grandeur ; EXO 08 (siège suspendu) ; concours A |
| Transformée de Laplace, propriétés, théorèmes (B2, S1) | §2 | §2 + unité de \(p\), exemple chiffré des théorèmes des valeurs initiale et finale, piège de la valeur finale |
| Fonction de transfert, forme canonique, gain, ordre, classe, pôles, zéros (B2, S1) | §3 | §3 + réponse impulsionnelle chiffrée ; méthodes 1, 2 |
| Signaux canoniques : impulsion, échelon, rampe, **signaux périodiques** (B2, S1) | §2 (sans les signaux périodiques) | §2 + signaux périodiques (Fourier → superposition), consigne composée (rampe saturée, théorème du retard) ; §7 régime sinusoïdal ; méthode 9 ; EXO 09 |
| Modèles de comportement : gain, intégrateur, dérivateur, 1er et 2e ordre, retard (B2, S2) | §5 (tableau) | §5 + figure calculée des six réponses indicielles, exemple « reconnaître les briques » ; méthode 6 ; identification renvoyée à `sys1` §5 et `sys2` §4 |
| Réponse temporelle : allures ; réponse sinusoïdale en régime permanent (C2, S1) | §4 (par décomposition, hors programme) | §7 « Exploiter une fonction de transfert sans revenir au temps » : stabilité, valeurs initiale et finale, pente à l'origine, régime sinusoïdal (figure calculée, exemples) ; méthodes 4, 8 ; EXO 05, 10 |
| Performances : théorème de la valeur finale, position des pôles (C2, S2) | §2, §4 | idem + exemple « prévoir l'allure par les seuls pôles » ; suite dans `stabilite`, `precision` |
| Grandeurs d'effort et de flux (D1, S2) | ❌ | §6 : tableau des analogies (électrique, translation, rotation, hydraulique, thermique) |
| Simulation numérique (C2 ⇆ informatique) | ❌ | §8 : méthode d'Euler (même fonction `euler` que `pynum` §6), choix du pas (figure calculée), suspension avec `euler_ordre2` ; renvoi à la validation (`sys1` §8, `sys2` §8) ; méthode 10 ; EXO 11 |
| Linéarisation (S3), non-linéarités (S4), pôles dominants (S3), transformée inverse (hors programme) | présentés comme exigibles | signalés sur place |

## Contenu ajouté

**Cours.** Bloc « AU PROGRAMME · PTSI » (capacités B2, C2, D1 avec renvois aux §, rappel de ce que le programme exclut) ; §1 causalité et exemple « reconnaître un SLCI », réservoir linéarisé chiffré (dans la partie signalée hors programme) ; §2 unité de \(p\), exemple des théorèmes, signaux périodiques, rampe saturée ; §3 réponse impulsionnelle chiffrée ; §4 exemple de lecture des pôles ; §5 figure des briques et exemple de décomposition en briques ; **§6** « Établir un modèle de connaissance » ; **§7** « Exploiter une fonction de transfert sans revenir au temps » ; **§8** « Simuler un SLCI en Python ». Figures nouvelles (calculées, `slci_figs.py`) : réponses indicielles des six briques ; réponse d'un système à zéro avec ses lectures directes (valeur initiale, pente, valeur finale, temps de réponse) ; Euler avec deux pas comparé à la solution exacte.

**Méthodes (6 → 10).** Les 6 méthodes gardées, chacune complétée d'un exemple éclair chiffré (3 et 5 signalées hors programme) ; nouvelles : 7 modèle de connaissance, 8 régime sinusoïdal permanent, 9 transformée d'une entrée composée, 10 simulation par Euler.

**Exercices (6 + 1 « concours » → 11 + 1 concours).** EXO 01 à 06 gardés (justes ; titres des 03, 04, 06 signalés hors programme ; formules longues en bloc) ; nouveaux : EXO 07 « SLCI ou pas ? » (linéarité, invariance, causalité, système affine), EXO 08 siège suspendu (modèle de connaissance avec zéro, valeurs initiale et finale, pente, régime sinusoïdal à \(\omega_0\), transmissibilité), EXO 09 consignes composées (créneau, rampe saturée, valeur finale, régime de poursuite), EXO 10 lecture d'une fonction de transfert à zéro (pente initiale multipliée par 4, régime sinusoïdal, temps de réponse), EXO 11 suspension simulée par Euler (pas, divergence au-delà de \(h = 0{,}08\) s par \(|1 + h\lambda|\)) ; Concours PT complété (partie C).

**Cartes ajoutées (15)**, toutes de modélisation et de Laplace (le deck est un deck de synthèse) : causalité ; continu et invariant ; dérivée hors conditions de Heaviside ; théorème de l'amortissement ; créneau ; rampe saturée ; unité de \(p\) ; pente à l'origine ; régime sinusoïdal permanent ; connaissance / comportement ; RLC série ; masse-ressort-amortisseur ; effort et flux ; transformée inverse non exigible ; Euler pour un premier ordre.

## Cartes corrigées (18) et progression des élèves

| Index | Ce qui change | Pourquoi |
|---|---|---|
| 3 | réponse | formules de boucle fermée embrouillées (« \(H_{BO}/(1+H_{BO})\) où \(H_{BO} = H_dH_r\) ») → retour unitaire, puis formule de Black avec \(A\), \(B\) comme `schblocs` |
| 5, 7, 11 | **question et réponse** | réponse fausse ou trompeuse (5 : \(K\) « sans dimension » ; 7 : texte incompréhensible ; 11 : « fréquence ») **et** question mal rendue (« \(du 1er\) ordre », « \(1er\) ordre », « \(2e\) ordre » en italique mathématique) |
| 6, 8, 9, 10 | question seule | « système \(du 2e\) ordre » mal rendu par `flashPretty` → « du premier/deuxième ordre », \(\tau\), \(\xi\), \(D_1\) en \( … \) |
| 15 | réponse | hypothèse du théorème de la valeur finale : limite finie de \(f\) (pôles de \(pF\)), pas « système stable » |
| 17 | réponse | \(\omega_{c0}\) (notation du site), « recommandée ≥ 45° » |
| 20, 21 | réponse | mêmes contenus, écrits en \( … \) (« −3 dB », « −20 log(2ξ) dB » étaient composés en italique mathématique) |
| 22 | réponse | « Toujours associer à un gain ou un PD » faux : c'est l'action proportionnelle (PI, 2ᵉ année) qui limite la perte de phase |
| 23, 24 | réponse | correcteur PI : « Hors programme en PTSI (vu en 2ᵉ année) : » comme dans le deck `prec` ; 24 : cassure \(1/T_i\) entre \(\omega_{c0}/10\) et \(\omega_{c0}/5\), perte de 6 à 11° |
| 26, 27, 35 | réponse | préfixe « Hors programme en PTSI (vu en 2ᵉ année) : » (non-linéarités, linéarisation, pôle dominant) ; 26 écrit « deuxième » (réponse sans formule : « 2ᵉ » serait mathématisé) |

**Progression conservée** : les questions retouchées n'ont pas de carte ajoutée ou retirée entre leurs voisines (les 15 ajouts sont en fin de deck) ; le cas 3a de `flashLoadState` (intervalle de même taille) leur rend l'état de même rang, et 6, 8, 9, 10 sont même reconnues par leur réponse inchangée. **Vérifié** en simulant le vrai `flashLoadState` du site (copie `revisions-an1`) sur l'ancien deck noté puis le nouveau : 37/37 états retrouvés à leur place, aucune carte ajoutée ne reprend d'état (`python3 slsb_etat.py <prefix> <corr.json> <ajout.js>`). Les cartes 5, 7 et 11 sont les seules dont la question **et** la réponse changent (exception prévue par les consignes : carte fausse des deux côtés).

## Notations

\(e(t)\), \(s(t)\), \(E(p)\), \(S(p)\), \(H(p)\) ; \(K\) gain, \(\alpha\) classe, \(n\) ordre ; \(\tau\), \(\omega_0\), \(\xi\) (et \(Q = 1/(2\xi)\) seulement pour faire le lien avec la physique) ; \(u(t)\) échelon unité, \(\delta(t)\) impulsion ; \(E_0\) amplitude d'un échelon, \(a\) pente d'une rampe, \(T\) retard ; \(H_{BO}\), \(H_{BF}\), \(\omega_{c0}\), \(M_\varphi\) dans les cartes de synthèse ; temps de réponse à 5 % (renvoi à \(t_{r5\%}\) de `sys1`). Mêmes notations que `sys1`, `sys2`, `bode`, `stabilite`, `precision`, `pynum`.

## Vérifications (2026-11-26, fichiers finaux)

- `verif_src.py` sur les trois panneaux : aucune erreur ni « attention ».
- `apercu_src.py` (copie `revisions-an1`) à 390 et 1 440 px, cours, méthodes, exercices : `merr`, `brut`, `larges` vides, aucune erreur JS.
- Figures nouvelles regardées en clair et en sombre (`slsb_voir.py`, `slci_voir/`).
- Programme du §8 exécuté (`slci_code.py`) : sortie identique à celle affichée.
- `corriger_cartes.py slci … --essai` (18 corrections) et `ajouter_cartes.py slci … --essai` (37 → 52) sans erreur ; cartes corrigées et ajoutées passées dans `flashPretty` puis MathJax (`slsb_cartes_rendu.js`) : aucune erreur.

## Doutes et points à valider

1. **§8 (simulation)** : en SII, la simulation numérique est au S4 et le schéma d'Euler au S3 ; la méthode d'Euler est en revanche au programme d'informatique de 1ʳᵉ année (`pynum` §6), et la capacité C2 « Déterminer la réponse temporelle » est marquée « ⇆ I ». Le §8 est donc présenté comme exigible, à titre de lien avec l'informatique, comme les §8 de `sys1` et `sys2`.
2. **§4 « Revenir au temps »** gardé à sa place (vidéo) alors que sa partie calculatoire est hors programme ; seul l'encadré « Les pôles décident de l'allure » est exigible.
3. **Deck de synthèse** : il garde des cartes de 2ᵉ année (correcteur PI) et de chapitres voisins (Bode, marges) ; elles sont signalées ou corrigées, pas retirées (règle des decks).
4. **Défaut de `flashPretty`** : « du 1er ordre », « du 2e ordre » sont mathématisés (« \(du 2e\) ») dans toute carte écrite sans \( … \). Corrigé ici dans les questions du deck `slci` ; d'autres decks peuvent avoir le même défaut (à traiter dans `flashPretty` plutôt que carte par carte).
5. Carte 9 : sa réponse garde un défaut de rendu mineur (« (2 pôles » partiellement mathématisé) ; non corrigée pour ne pas toucher question et réponse d'une carte juste.
