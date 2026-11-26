# `schblocs` (prefix `sb`) « Schéma-blocs et systèmes asservis » — mise au format de la 2ᵉ année (point 7), 2026-11-22 → 2026-11-26

Travail commencé le 2026-11-22 par un premier rédacteur (interrompu avant le compte rendu), repris, contrôlé et terminé le 2026-11-26 : tous les calculs refaits (`sb_calculs.py`, `sb_calculs_exos.py`), figures regardées en clair et en sombre, trois figures d'énoncé redessinées à 340 unités au plus, contrôles de `CONSIGNES-1A.md` relancés sur les fichiers finaux, état des cartes simulé avec le vrai `flashLoadState` du site.

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `sb-cours.src.html` | cours (≈ 74 000 signes dont ≈ 40 000 de figures SVG) : bloc « AU PROGRAMME · PTSI », §1 à §8 ; 10 exemples traités chiffrés ; 9 figures (2 d'origine gardées, 7 nouvelles calculées) |
| `sb-meth.src.html` | 10 méthodes (étapes + exemple éclair chiffré) + « Pièges classiques » |
| `sb-exos.src.html` | 11 exercices (★ à ★★★, 3 figures d'énoncé) + 1 « Concours PT » en 4 parties (A à D, 9 questions) |
| `sb-cartes-corr.json` | 17 cartes corrigées (voir plus bas) |
| `sb-cartes-ajout.js` | 12 cartes ajoutées en fin de deck (30 → 42) |
| `sb-cours-ajouts.tpl.html` + `sb_construire.py` | blocs ajoutés au panneau d'origine (`@@BLOC:…@@`) et figures (`@@FIG:…@@`) |
| `sb-exos.tpl.html` + `sb_construire_exos.py` | panneau Exercices complet, figures en `@@FIG:…@@` |
| `sb_figs.py` → `sb_figs.json` | 10 figures (7 du cours, 3 d'énoncé) ; classes du site, aucune couleur en dur ; outils communs `slsb_svgk.py`, `slsb_voir.py` (planches clair/sombre dans `sb_voir/`) |
| `sb_calculs.py`, `sb_calculs_exos.py` | vérification (sympy, numpy) de tous les exemples, éclairs et corrigés |
| `sb_cartes.py` | produit `sb-cartes-corr.json` à partir du deck actuel |
| `sb_orig_*.html` | panneaux d'origine (identiques au site `revisions-an1` du 2026-11-26) |

Reconstruire : `python3 sb_figs.py && python3 sb_construire.py && python3 sb_construire_exos.py`.

## Numérotation des §

**Aucune renumérotation** : §1 à §5 gardent leur numéro et leur titre (fiches « Voir dans le cours », vidéo `video/slci/ch2` de l'onglet Vidéos, renvoi du chapitre `afs` à `schblocs` §1). §6, §7 et §8 sont ajoutés à la suite. L'exemple des deux boucles imbriquées du §3 (\(4/p\), puis \(1/(1 + 0{,}5p)\)), repris par la vidéo, est gardé tel quel. Panneaux `-video`, `-simu`, `-flash` non touchés.

## Erreurs trouvées et corrigées

1. **Méthode 5** (retour unitaire) : « l'écart \(\varepsilon = E/(1 + H_{BO})\), exprimé dans l'unité de la consigne » confondait **écart** et **erreur** ; corrigé : l'erreur \(E - S = E/(1 + H_{BO})\) est dans l'unité de la consigne, l'écart en sortie du comparateur vaut \(K_a\) fois plus (exemple éclair chiffré).
2. **Ancien EXO 05** (« Chaîne fonctionnelle — robot ») incohérent : codeur donné « rad/s → pts/s » (un codeur mesure une position), consigne en degrés convertie par un « CAN 12 bits » sans lien avec le codeur, unités qui ne se raccordent pas au comparateur, « PID numérique » (hors programme). Remplacé par un exercice d'antenne de poursuite (schéma-blocs organique, unités, gain de l'adaptateur, résolution, FTBO, traînage).
3. **Ancien EXO 02, Q3** : appelait « erreur statique » l'écart \(E - B\,s_\infty\) d'un retour non unitaire, sans dire que la sortie ne rejoint pas la consigne ; corrigé (écart, erreur, rôle de l'adaptateur en Q4 nouvelle).
4. **Ancien EXO 04, Q3** : « classe du système global » ambigu (une FTBF stable est toujours de classe 0) → classe de la FTBO de la boucle externe.
5. **Cours** : vocabulaire du programme (« poursuite et régulation ») remplacé par « asservissement / régulation » ; chaîne directe et chaîne de retour non définies au §1 ; formule de Black (deux cas sur une ligne) et étape 3 de l'exemple des boucles imbriquées trop larges au téléphone → en bloc ; exemple de l'axe de robot purement littéral → chiffré. Aucune erreur de calcul dans le cours d'origine.
6. **Cartes 13 et 14 inversées** : « déplacer un point de prélèvement avant un bloc \(H\) : ajouter \(1/H\) » (c'est \(H\)) et « après : ajouter \(H\) » (c'est \(1/H\)), contraires au cours §3. **Carte 10** fausse des deux côtés (« les 4 fonctions » de la chaîne d'information : le programme en compte trois, acquérir, traiter, communiquer). **Carte 16** : numérateur « \(K_m\) » au lieu de \(K_i\). **Carte 22** (représentation d'état) : hors programme non signalé. **Cartes 7 et 8** affichées fausses par `flashPretty` (« \(F(p)/p\) » composé \(F\cdot\frac{p}{p}\) ; « \(S(p)/E(p)\) » composé \(S\cdot\frac{p}{E}(p)\)) ; 0 à 3, 11, 12, 20 : « HBF », « Hdirect », « H1 » composés en italique mathématique.
7. **Figures d'énoncé** (EXO 04, 06, 08) larges de 360 à 420 unités : redessinées en 316 à 336 unités (au téléphone, libellés ≥ 13 px sans défilement, contrôlé dans la page). Figure de l'axe (§5) : signe « − » du comparateur qui chevauchait l'unité « points », indice de \(\omega_m\) qui touchait la flèche → corrigés.
8. **Cours §6** : la puissance moyenne du thermostat (1 505 W) était dite « exactement » celle qui maintient 20 °C (1 500 W) → « pratiquement ».

## Couverture du programme (S1) : avant → après

| Capacité (programme SII 2021) | Avant | Après |
|---|---|---|
| Identifier la structure d'un système asservi : grandeurs d'entrée et de sortie, capteur, chaîne directe, chaîne de retour, commande, comparateur, consigne, correcteur, perturbation ; poursuite et régulation (A3, S1) | §1 (structure ; « asservissement » au lieu de « poursuite » ; chaînes directe et de retour non définies) | §1 complété + exemple du régulateur de vitesse (effet chiffré du bouclage) ; méthode 8 ; EXO 07 (régulation de niveau), concours A |
| Identifier et décrire les liens entre les chaînes fonctionnelles : systèmes asservis et séquentiels (A3, S1) | §5 (correspondance chaînes ↔ blocs, sans exemple) ; asservi / séquentiel ❌ | §5 (axe de robot chiffré, schéma-blocs organique avec unités) ; **§6** asservi ou séquentiel (thermostat chiffré, figure calculée) ; EXO 07 Q4, EXO 10 |
| Schéma-blocs organique d'un système (B2, S1) | §5 (littéral) | §5 (figure, unités à chaque flèche), §7 ; EXO 05, concours C1 |
| Élaboration de schéma-blocs (B2, S1) | §2 (moteur à courant continu) | §2 + moteur chiffré (pôles exacts, modèle simplifié justifié) ; **§7** schéma-blocs avec perturbation (pièce chauffée) ; **§8** blocs en série et effet de charge (cellules RC, figures, schéma-blocs à trois boucles) ; méthodes 1, 9 ; EXO 03, 09, 11 |
| Manipulation et réduction (B2, S1) | §3 (règles, boucles imbriquées) | §3 + boucles entrelacées (figure avant/après déplacement, exemple chiffré, contrôle par les équations) ; méthodes 2, 6, 7 ; EXO 01, 04, 08 |
| FT de chaîne directe et de retour, en boucle ouverte et fermée (B2, S1) | §4 | §4 + écart et adaptateur, boucle de vitesse à génératrice tachymétrique (saturation de la commande), effet statique d'une perturbation ; méthodes 3, 4, 5, 10 ; EXO 02, 06, concours B-C |
| Perturbation (A3, S1 ; écart statique dû à une perturbation : `precision`, S2) | §4 (superposition littérale) | §4, §7 (\(H_E\), \(H_D\) chiffrés, limites de la commande) ; méthodes 4, 10 ; EXO 06, 09, concours C2-C3 |
| Réglage des correcteurs (S4), multiphysique (S3), règle de Mason (hors programme) | — | signalés dans le bloc programme ; le PI n'apparaît que comme renvoi (« 2ᵉ année ») |

## Contenu ajouté

**Cours.** Bloc « AU PROGRAMME · PTSI » ; §1 poursuite/régulation, chaînes directe et de retour, exemple du régulateur de vitesse ; §2 moteur chiffré ; §3 boucles entrelacées ; §4 écart et adaptateur, boucle tachymétrique, effet d'une perturbation ; §5 axe de robot chiffré et schéma-blocs organique ; **§6** « Systèmes asservis et systèmes séquentiels » ; **§7** « Élaborer un schéma-blocs avec perturbation » ; **§8** « Blocs en série et effet de charge ». Figures nouvelles (calculées, `sb_figs.py`) : boucles entrelacées avant/après ; schéma-blocs organique de l'axe ; thermostat (température et chauffe, modèle du premier ordre) ; régulation de température ; deux cellules RC (circuit, schéma-blocs, réponses indicielles comparées).

**Méthodes (5 → 10).** Les 5 gardées (la 5 corrigée), chacune avec un exemple éclair chiffré ; nouvelles : 6 séparer deux boucles entrelacées, 7 réduire par les équations, 8 identifier la structure sur une description, 9 vérifier un schéma-blocs, 10 écart en présence d'une perturbation.

**Exercices (7 + 1 « concours » → 11 + 1 concours).** Gardés : EXO 01 à 04 et 06 (corrigés et rédigés plus complètement ; EXO 02 : Q4 sur l'adaptateur ; EXO 03 : Q4 modèle simplifié ; EXO 06 : comparaison sans bouclage). **Retirés** : l'ancien EXO 05 (incohérent, voir plus haut), l'ancien EXO 07 (FTBF d'un premier ordre, déjà fait par EXO 01 Q3, la méthode 3 et le §4) et l'ancien « Concours PT » (formule de Black et sensibilité en trois questions d'application directe, repris par EXO 02 et le §4) : le panneau reste ainsi à 12 exercices. Nouveaux : EXO 05 antenne de poursuite, EXO 07 régulation de niveau (structure, unités ; flotteurs → séquentiel), EXO 08 boucles entrelacées (équations, déplacement d'un sommateur, contrôle statique), EXO 09 réservoirs en cascade avec et sans interaction, EXO 10 four à thermostat, EXO 11 effet de charge d'une cellule RC ; **Concours PT** « treuil de levage » : structure, couple résistant ramené, modèle du moteur avec perturbation, schéma-blocs complet et adaptateur, FTBO, FTBF, rejet de la charge (÷ 19), saturation au démarrage (3 600 V demandés), adaptateur mal réglé.

**Cartes ajoutées (12).** Chaîne directe et chaîne de retour ; déplacer un sommateur ; boucles entrelacées ; retour ajouté (`form`) ; écart avec adaptateur (`form`) ; effet statique d'une perturbation (`form`) ; \(H_D\) (`form`) ; effet de charge (`form`) ; asservi ou séquentiel ; schéma-blocs organique ; saturation au démarrage ; vérifier un schéma-blocs.

## Cartes corrigées (17) et progression des élèves

| Index | Ce qui change | Pourquoi |
|---|---|---|
| 13, 14 | réponse | règles de déplacement d'un point de prélèvement inversées |
| 10 | **question et réponse** | « les 4 fonctions » de la chaîne d'information (il y en a trois) ; réponse : acquérir, traiter, communiquer, et lien avec la chaîne de puissance |
| 16 | **question et réponse** | numérateur faux (\(K_m\) au lieu de \(K_i\)) ; question « FT moteur DC (… boucle FEM) » mal rendue (« \(U,\) ») → « Fonction de transfert d'un moteur à courant continu… » |
| 22 | réponse | « Hors programme en PTSI comme en PT : » (représentation d'état) |
| 7, 8 | réponse | rendu faux (« \(F(p)/p\) » affiché \(F\,p/p\), « \(S(p)/E(p)\) » affiché \(S\,p/E(p)\)) ; 8 complétée (bloc, sommateur) |
| 0, 1, 2, 3, 11 | réponse | mêmes contenus en \( … \), notations du cours (\(A\), \(B\), \(H_{BO}\), \(H_{BF}\)) ; 2 : « si aucun bloc ne charge le précédent » ; 11 : écart statique |
| 12 | réponse | « signal d'erreur » : c'est l'**écart** \(\varepsilon = E - B\,S\) ; il ne mesure l'erreur \(E - S\) qu'avec un adaptateur de même gain que le capteur (notations de `precision`) |
| 20 | réponse | réponse tautologique (« l'ordre du dénominateur de HBF ») → ordre de la FTBO en général, avec la raison |
| 21, 23, 24 | question seule | « \(BF =\) », « \(FT = \frac1p\) » : sigles composés en italique mathématique → « fonction de transfert en boucle fermée », « bloc de fonction de transfert \(1/p\) » |

**Progression conservée** : aucune carte n'est ajoutée ni retirée entre les cartes retouchées (les 12 ajouts sont en fin de deck) ; les questions retouchées retrouvent leur état par leur réponse inchangée (21, 23, 24) ou par le rang (10, 16 : cas 3a de `flashLoadState`). **Vérifié** en simulant le vrai `flashLoadState` du site (copie `revisions-an1`) : 30/30 états retrouvés à leur place, aucune carte ajoutée ne reprend d'état (`python3 slsb_etat.py <prefix> <corr.json> <ajout.js>`). Seules 10 et 16 changent de question **et** de réponse (exception des consignes : carte fausse des deux côtés).

## Notations

\(E\), \(S\) (consigne, sortie), \(\varepsilon\) (écart en sortie du comparateur), erreur \(E - S\) ; \(A\) chaîne directe, \(B\) chaîne de retour ; \(H_{BO} = A\,B\) (FTBO), \(H_{BF}\) (FTBF), \(K_{BO} = H_{BO}(0)\) en classe 0 ; \(K_a\) adaptateur, \(K_{cap}\) capteur, \(K_c\) correcteur proportionnel ; \(D\) perturbation, \(H_E\), \(H_D\) ; moteur : \(R\), \(L\), \(k\) (\(K_e = K_i = k\)), \(J\), \(f\), \(\tau_m = RJ/k^2\), \(C_m\), \(C_r\) ; \(\omega_0\), \(\xi\) pour les boucles fermées du 2ᵉ ordre. Mêmes notations que `slci`, `sys1`, `sys2`, `stabilite`, `precision`, `correcteurs` ; la carte 3 du deck `slci` est alignée (\(A\), \(B\)).

## Vérifications (2026-11-26, fichiers finaux)

- `verif_src.py` sur les trois panneaux : aucune erreur ni « attention ».
- `apercu_src.py` (copie `revisions-an1`) à 390 et 1 440 px, cours, méthodes, exercices : `merr`, `brut`, `larges` vides, aucune erreur JS.
- Figures d'énoncé dans la page à 390 px : largeur affichée ≤ 339 px, sans défilement, plus petit libellé 13,1 px. Figures du cours : défilement horizontal au téléphone (comportement normal des schémas larges, libellés ≥ 12 px).
- Figures nouvelles ou modifiées regardées en clair et en sombre (`slsb_voir.py`).
- `corriger_cartes.py sb … --essai` (17 corrections) et `ajouter_cartes.py sb … --essai` (30 → 42) sans erreur ; cartes corrigées et ajoutées passées dans `flashPretty` puis MathJax (`slsb_cartes_rendu.js`) : aucune erreur.

## Doutes et points à valider

1. **Exercices retirés** (ancien EXO 07, ancien « Concours PT ») : justes mais redondants et très courts ; retirés pour rester à 12 exercices. À rétablir si l'on préfère ne rien retirer (ils n'ont ni état ni renvoi).
2. **§8 « effet de charge »** : le programme ne le cite pas en toutes lettres ; il est présenté comme une condition de validité de la mise en série (élaboration d'un schéma-blocs), avec un exemple électrique et un exemple hydraulique.
3. **Carte 20** : sa question garde un défaut de rendu mineur (« \(BF =\) ») ; non corrigée pour ne pas toucher question et réponse d'une carte juste. Même remarque générale que pour `slci` : les sigles (« HBF », « FT ») et « du 2e ordre » écrits sans \( … \) sont mathématisés par `flashPretty`.
4. Deck : de nombreuses retouches (17 cartes sur 30), presque toutes de rendu ; la progression est conservée (simulation ci-dessus).
