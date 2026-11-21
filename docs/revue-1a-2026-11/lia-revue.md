# Nouveau chapitre `liaisons` (prefix `lia`) — « Liaisons, graphe et schéma cinématique » (SI, 1ʳᵉ année)

Rédigé le 2026-11-21 (point 4 de l'audit du 2026-11-14 : `docs/audit-2026-11/si-1a.md` §2 point 1, §5 point 2).
Place : groupe Mécanique de SI, après `cine`, avant `statique` (déjà déclaré dans la copie `AN1/site/index.html`
par `chapitres.py` : onglets cours, méthodes, cartes, exercices ; pas de simulateur).

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `lia-cours.src.html` | cours complet (≈ 152 000 signes) : bloc « AU PROGRAMME · PTSI », 12 sections §1 à §12, « POUR ALLER PLUS LOIN · 2ᵉ ANNÉE », 21 exemples traités, 13 figures |
| `lia-meth.src.html` | 10 méthodes (étapes nommées, exemple éclair chiffré) + pièges classiques |
| `lia-exos.src.html` | 11 exercices (★ à ★★★) + 1 « Concours PT » en 5 parties (11 questions), 5 figures |
| `lia-cartes.js` | `const liaCards` : 30 cartes (14 `cat:'form'`, 2 `cat:'val'`) |
| `lia-cours.tpl1/2/3.html`, `lia-exos.tpl.html` | gabarits (`@@FIG:nom@@`), assemblés par `lia_construire.py` |
| `lia_geo.py`, `lia_figs_symboles.py`, `lia_figs_cours.py`, `lia_figs_exos.py` → `lia_figs.json` | figures calculées (vues planes + perspective orthogonale), classes du site, sans couleur en dur |
| `lia_calc.py` | outil sympy : torseurs des 11 liaisons, transport, fermetures (rang), liaisons en série / parallèle |
| `lia_verif_liaisons.py`, `lia_verif_pompe.py`, `lia_verif_exemples.py`, `lia_verif_exos.py`, `lia_verif_trappe.py` | vérification de tous les résultats (ddl, dualité, domaines de validité, rangs, m, h, valeurs numériques) |
| `lia_harness.py` | rendu rapide des figures (clair / sombre, 358 et 540 px) |

## Couverture du programme (S1, S2) : avant → après

| Capacité (programme 2021) | Avant (1ʳᵉ année) | Après (`liaisons`) |
|---|---|---|
| Liaisons parfaites, degrés de liberté (B2, S1) | cine §4 (définition « DDL ») | §1 (solide, 6 ddl, liaison, liaison parfaite, contact unilatéral) |
| Géométrie des contacts (B2, S1) | — | §2 (tableau plan / cylindre / sphère, centrage long ou court, \(\alpha \approx j/L\) démontré) |
| 11 liaisons normalisées, caractéristiques géométriques, symboles (B2, S1) | 7 liaisons, aucun symbole (cine §4) | §3 : tableau des 11 (anciens noms), 4 planches de symboles (plan + perspective), hélicoïdale |
| Repères d'expression privilégiés, torseur cinématique (B2, S1) | formes sans domaine de validité (cine §4) | §4 : forme locale, transport, domaine de validité démontré ; tableau §6 |
| Contact ponctuel : roulement, glissement (B2, S1) | RSG seulement (cine §6) | §5 : \(\vec V_g\), roulement et pivotement, exemple chiffré ; résistance au roulement et au pivotement (S2) |
| Torseur des actions transmissibles, glisseur et couple (B2, S2) | liaisons en 2D seulement (statique §3) | §6 : dualité \(n_s = 6 - n_c\), hélicoïdale \(L = -\frac{p_h}{2\pi}X\), glisseur / couple, tableau des 11 liaisons (torseurs cinématique et transmissible, validité) |
| Classes d'équivalence, graphe de liaisons (B2, S1) | une phrase (cine §6) | §7 : règles, exemple sur nomenclature (pompe à levier, coupe coloriée), graphe, \(\gamma\) démontré |
| Schéma cinématique, paramétrage, fermeture géométrique (B2 S1, C1 S1) | méthode en 4 lignes (cine §6) | §8 : méthode de tracé, schémas plan et perspective, figures de changement de base, loi entrée-sortie de la pompe chiffrée |
| Liaisons en série et en parallèle, liaisons équivalentes (B2, S2) | ❌ (seulement `chaines` §4, 2ᵉ année) | §9 : patin à rotule (série), porte sur deux gonds (parallèle, efforts calculés) |
| Mobilité, hyperstatisme (B2, S2) | une demi-page (statique §3, cine §6) | §10 : approches cinématique (rang de la fermeture) et statique, cohérence démontrée, \(m_u\), \(m_i\), exemples |
| Conditions géométriques, substitution, ajout de solide (B2, S2) | ❌ en 1ʳᵉ année | §11 : lecture des lignes « 0 = 0 », conséquences, ordres de grandeur, pompe rendue isostatique |
| Conditions et limites de la modélisation plane (B2, S2) | ❌ en 1ʳᵉ année | §12 : conditions, liaisons planes, \(h_{\text{plan}} \leq h\) |
| Graphe de structure, isolements (S3), petits déplacements (S3) | — | renvoi « Pour aller plus loin » vers `chaines` §3 (2ᵉ année) |

## Contenu

**Cours (12 sections).** §1 Modéliser un mécanisme ; §2 Géométrie des contacts ; §3 Les onze liaisons normalisées ;
§4 Torseur cinématique d'une liaison ; §5 Contact ponctuel : glissement, roulement, pivotement ; §6 Torseur des actions
transmissibles (tableau récapitulatif) ; §7 Classes d'équivalence et graphe ; §8 Schéma cinématique et paramétrage ;
§9 Liaisons équivalentes ; §10 Mobilité et hyperstatisme ; §11 Conditions géométriques et modèle isostatique ;
§12 Modélisation plane ; Pour aller plus loin · 2ᵉ année. Fil rouge inventé : une **pompe à levier** de puits
(\(a = 120\), \(\ell = 100\), \(c = 140\) mm) suivie de la nomenclature jusqu'au modèle isostatique : classes, graphe,
schémas plan et 3D, loi \(\lambda(\theta)\) (course 82,1 mm, 316 cm³ par coup), fermeture cinématique (\(r_c = 4\),
\(m = 1\), \(h = 2\), lignes \(R_x\) et \(T_z\)), sphérique en \(A\) → \(h = 0\), modèle plan \(h_{\text{plan}} = 0\).
Autres exemples chiffrés : portière, bague longue / courte, chaise de bureau, vis M10, vis à billes, pivot hors axe,
roue qui patine, chariot à roulettes, palpeur (glisseur), vis chargée, robot / pompe / trappe (\(\gamma\)),
patin à rotule, porte sur deux gonds (\(X_B \approx -73{,}6\) N), barrière à bielle à rotules, ordres de grandeur
(dilatation, désalignement admissible).

**Figures (cours) :** six ddl ; centrage long / court (angle calculé) ; 4 planches des 11 symboles (vue plane, vue de
bout quand elle distingue, perspective ; repère local) ; contact ponctuel (\(\vec V_g\), \(\vec\Omega_n\), \(\vec\Omega_t\)) ;
pompe en coupe coloriée par classes ; graphe ; schéma plan (θ = 15°, positions calculées) ; schéma en perspective ;
figures de changement de base ; série / parallèle.

**Méthodes (10).** Identifier une liaison ; torseur cinématique et validité ; torseur transmissible (dualité) ; classes et
graphe ; tracer et paramétrer un schéma ; fermeture géométrique ; contact ponctuel ; liaison équivalente ; mobilité et
hyperstatisme ; conditions géométriques et modèle isostatique ; pièges.

**Exercices (12).** 01 reconnaître 8 liaisons (★) ; 02 torseurs hors du point privilégié (★) ; 03 sauterelle de bridage :
classes, graphe, schéma (★, figures dans le corrigé) ; 04 presse d'établi à vis (★★) ; 05 variateur plateau-galet :
glissement, roulement, pivotement (★★, figure) ; 06 tourelle de caméra : pivots en série, axes concourants ou non (★★) ;
07 plateau de presse sur deux colonnes : parallèle, \(h\) = 3, 1, 0, efforts (★★) ; 08 trois mécanismes à compter (★★) ;
09 vérin électrique : fermeture cinématique 3D, conditions, Oldham (★★★) ; 10 arbre sur trois paliers (★★★) ;
11 robot SCARA, chaîne ouverte (★★, figure) ; **Concours PT** : ouvre-trappe de désenfumage à vérin électrique
(chaîne complexe \(\gamma = 2\), charnières équivalentes, anti-rotation, loi \(\lambda(\theta)\), course 304 mm,
\(h = 6 = 4 + 2\), modèle plan, rotule qui crée une mobilité parasite, montage final \(m = 2\), \(h = 4\) interne,
\(F \approx 530\) N, couple sur la vis 0,34 N·m / 0,96 N·m ; schéma fourni en SVG).

**Cartes (30).** Liaison parfaite ; pivot, glissière, hélicoïdale (2), pivot glissant, sphérique à doigt, appui plan,
sphérique, sphère-cylindre, cylindre-plan, sphère-plan ; dualité ; domaines de validité ; centrage long / court ; classe
d'équivalence ; graphe / schéma ; \(\gamma\) ; série ; parallèle ; sphérique + sphère-cylindre ; \(m\), \(h\) (deux
approches) ; \(m_u\), \(m_i\) ; lignes « 0 = 0 » ; rendre isostatique ; modèle plan ; \(\vec V_g\) ; roulement /
pivotement ; résistance au roulement. Formules en `\\( … \\)` (le champ entier est laissé à MathJax).

## Notations (alignées sur `chaines` et `transm`)

\(n_c\) (ddl d'une liaison), \(n_s = 6 - n_c\), \(I_c = \sum n_c\), \(I_s = \sum n_s\), \(n\) (classes, bâti compris),
\(n_L\), \(\gamma = n_L - n + 1\), \(r_c\), \(r_s\), \(m = m_u + m_i\), \(h = m - I_c + 6\gamma = m + I_s - 6(n-1)\),
\(h_{\text{plan}} = m - I_c + 3\gamma\) ; \(\{\mathcal V(2/1)\} = \{\vec\Omega(2/1) \;;\; \vec V(P, 2/1)\}_P\), composantes
\(p, q, r, u, v, w\) ; \(\{\mathcal T(1\to2)\} = \{\vec R(1\to2) \;;\; \vec M(P, 1\to2)\}_P\), composantes \(X, Y, Z, L, M, N\) ;
pas de l'hélice \(p_h\) (comme `transm` ; `cine` écrit « p ») ; \(\vec V_g\), \(\delta\) (comme `energ2a`). Base locale :
\(\vec x\) axe / direction / ligne de contact, \(\vec z\) normale ; sphérique à doigt : rotation interdite autour de \(\vec z\).
Le lien avec la notation \(\vec v(P\in 2/1)\) de `cine` et \(\vec M_P\) de `statique` est dit dans le cours.

## Vérifications faites

- Tous les résultats recalculés en sympy / numpy (`lia_verif_*.py`) : ddl, dualité (comoment nul) et domaine de validité
  des 11 liaisons ; rangs, \(m\), \(h\) de tous les mécanismes (pompe et ses variantes, barrière, potence, presse,
  vérin électrique avec et sans Oldham, colonnes, arbre, trappe et ses 8 variantes) ; liaisons équivalentes (patin,
  porte, colonnes, tourelle, SCARA) ; toutes les valeurs numériques.
- `verif_src.py` : aucune ERREUR ni « attention » sur les trois panneaux.
- `apercu_src.py` (copie `AN1/site/index.html`) à 390 et 1 440 px : `merr`, `brut`, `larges` vides, aucune erreur JS,
  pour le cours, les méthodes et les exercices ; captures regardées (planches de symboles, tableau récapitulatif, graphe,
  exercice Concours). Figures nouvelles regardées en clair et en sombre (banc `lia_harness.py`).
- Cartes : `node … liaCards.length` → 30 ; questions toutes distinctes ; `\\(` / `\\)` équilibrés ; textes des cartes
  rendus sans erreur MathJax (page d'essai `_tmp/lia-cartes-test.src.html`).

## Erreurs relevées dans l'existant

Les erreurs de l'audit (§4 de `si-1a.md`) sur `cine` et `statique` sont **déjà corrigées** dans la version actuelle :
« glissière-rotule » remplacée par l'hélicoïdale, définition du schéma cinématique, formule \(m - h\), \(h \geq 0\),
appui plan à 2 inconnues en plan, appui ponctuel à 5 ddl, équilibre indifférent « sur l'axe », carte 23 de `stat`.
Restent des points d'alignement (section suivante), aucune erreur de fond.

## À aligner dans `cine` et `statique`

Rien n'a été modifié dans ces chapitres ; propositions précises pour l'intégrateur.

**`cine` (prefix `cine`)**
1. `cine-cours` §4 « LIAISONS MÉCANIQUES ET DEGRÉS DE LIBERTÉ » : 7 liaisons sur 11 (plus une ligne « Libre » qui n'est
   pas une liaison normalisée), aucun symbole, aucun domaine de validité (« Pivot d'axe Δ = (A, z) … \(\vec v(A) = \vec 0\) »
   sans « en tout point de l'axe »). Proposition : réduire §4 à un rappel (définition des ddl, trois formes de torseurs
   avec leur domaine de validité) et renvoyer à `#liaisons/cours` §3, §4 et §6 (tableau des 11 liaisons).
2. Même §4 : « DDL » (14 occurrences dans le cours, plus cartes 14 à 17) → \(n_c\) ou « degrés de liberté » ;
   « Pivot-glissant » (2 occurrences) → « pivot glissant » ; hélicoïdale \(\dot\lambda = \frac{p}{2\pi}\dot\theta\) →
   pas noté \(p_h\) (comme `transm` et `liaisons`, où \(p\) est la composante de rotation du torseur).
3. `cine-cours` §6 « Graphe des liaisons et schéma cinématique » et « Mobilité et hyperstatisme d'un mécanisme plan » :
   corrects mais en doublon de `liaisons` §7, §10, §12 ; garder une phrase et renvoyer. Écrire la formule plane
   \(m - h = 3(n-1) - I_s\) avec les notations \(I_s\), \(I_c\) de `liaisons` (aujourd'hui \(\sum(3 - n_{c,i})\)).
4. `cine-cours` §6 « Méthode vectorielle — fermeture de chaîne » (4 lignes, sans exemple) : renvoyer à `liaisons` §8
   (fermeture traitée sur la pompe) ; le paragraphe « Roulement sans glissement » : renvoyer à `liaisons` §5
   (vitesse de glissement, roulement, pivotement).
5. `cine-meth` méthode 4, étape 1 « Tracer le schéma cinématique » : renvoyer à la méthode 5 de `liaisons`.
6. Cartes 14 à 17 de `cine` : justes ; si l'on remplace « DDL » par « degrés de liberté », ne retoucher que la réponse
   (règle de `flashLoadState` : sans perte de progression).

**`statique` (prefix `stat`)**
1. `stat-cours` §3 « MODÉLISATION DES LIAISONS EN STATIQUE » : torseurs en 2D seulement, alors que le programme (S2)
   demande le torseur des actions transmissibles des liaisons normalisées ; ajouter une phrase et un lien vers
   `liaisons` §6 (dualité, tableau des 11 torseurs 3D) ; « Appui ponctuel » → « sphère-plan (ponctuelle) » ;
   préciser que le tableau 2D est la version plane des liaisons (renvoi à `liaisons` §12, tableau des liaisons planes).
2. `stat-cours` §3 (degré d'hyperstatisme, \(h = m + I_s - E_s\)) : juste ; renvoyer à `liaisons` §10 et §11 pour
   l'approche cinématique, les conditions géométriques et la façon de rendre un modèle isostatique.
3. `stat-cours` §1 « Torseur des actions de contact » : les torseurs **glisseur et couple** (S2) n'y sont pas nommés ;
   les définir ou renvoyer à `liaisons` §6.
4. `stat-cours` §4 « Frottement » : la résistance au roulement et au pivotement (S2) manque ; renvoyer à `liaisons` §5
   (présentation, ordres de grandeur) en attendant le complément prévu par l'audit (point 5 : modèle local, visqueux).
5. `stat-meth` méthode 3 : « h < 0 signale… » est écrit en clair dans le HTML (rendu correct aujourd'hui, mais fragile) :
   écrire \(h \lt 0\) ; renvoyer aux méthodes 9 et 10 de `liaisons`.
6. Cartes 7 à 10, 23, 24 de `stat` : justes et cohérentes avec `liaisons` (elles portent explicitement « en 2D »).

## Doutes et points à valider

1. **Formule demandée « h = m − 6γ + Nc »** : le signe est inversé ; avec \(N_c = I_c\) inconnues cinématiques, la bonne
   relation est \(h = m - I_c + 6\gamma\) (bielle-manivelle : \(1 - 4 + 6 = 3\), alors que \(1 - 6 + 4 = -1\)).
   Le cours emploie celle de `chaines`, avec \(I_c\), et signale la notation \(N_c\), \(N_s\).
2. **Symboles** : dessinés d'après la forme usuelle des cours de SI de la norme NF EN ISO 3952 ; les détails (vue de
   bout de la pivot, tracé du doigt de la sphérique à doigt, zigzag de l'hélicoïdale) varient selon les documents ;
   le cours le signale. À comparer au polycopié du cours.
3. **Sphérique à doigt** : orientée « rotation interdite autour de \(\vec z\) » (levier d'axe \(\vec z\)) ; certains
   tableaux interdisent la rotation autour d'un autre axe : c'est une convention, la forme se transpose.
4. **Résistance au pivotement** : notée \(\delta_p\) (aucune notation dans le site ni de consensus) ; présentée en
   quelques lignes, l'essentiel restant à `statique`.
5. Longueur du cours (≈ 152 000 signes) : au-dessus de la cible « maths » (25 000 à 45 000), comparable au cours
   `emag` de 1ʳᵉ année (≈ 127 000) ; les figures SVG en font environ 75 000.
6. Le chapitre `chaines` (2ᵉ année) reprend une partie de ce contenu (fermetures, liaisons équivalentes,
   hyperstatisme) : on pourrait y ajouter une phrase « rappels de 1ʳᵉ année : voir `liaisons` ». Les exemples des deux
   chapitres sont différents (pompe, porte, colonnes, trappe ici ; bielle-manivelle, benne, essuie-glace là-bas).
