# Revue `estat` (prefix `es`) — Électrostatique (aperçu de la 2ᵉ année)

Fichiers produits (dans `EM/`) : `es-cours.src.html`, `es-meth.src.html`, `es-exos.src.html`, `es-cartes-corr.json`,
`es-cartes-ajout.js`. Sources : `es-cours.tpl.html` et `es-exos.tpl.html` (gabarits, `@@FIG:nom@@`), assemblés par
`construire.py` avec `figs_es.json` ; figures calculées par `figs_es.py` ; vérifications numériques : `verif_es.py`.
Panneaux `es-simu` et `es-flash` non touchés.

Contrôles (lancés un par un) :
- `verif_src.py` sur les trois panneaux : aucune ERREUR ; une seule « attention » : « pas de bloc AU PROGRAMME · PT »
  sur le cours, **voulue** (consigne 1A : l'aperçu n'a pas de bloc « Au programme · PTSI » ; il s'ouvre par l'encadré
  `.hors-prog` « Aperçu de la 2ᵉ année · Non exigible en PTSI », comme `fluides`).
- `apercu_src.py` à 390 et 1440 px pour cours, méthodes, exercices : `merr`, `brut`, `larges` vides, aucune erreur JS,
  aucune ligne ATTENTION. Figures vérifiées en capture (390 et 1440 px) : à 390 px, la figure 1 passe en `.lisible`
  (364 px, libellés ≥ 12,1 px) sans défiler ; les autres tiennent dans la colonne.
- `corriger_cartes.py es … --essai` : 5 réponses corrigées ; `ajouter_cartes.py es … --essai` : 25 → 30 cartes.

## Erreurs et défauts trouvés dans l'existant (tous corrigés)
1. **Méthodes, ancienne méthode 1 et « Pièges »** : « Gauss ne s'applique que si E est uniforme sur la surface choisie —
   ne pas utiliser pour une distribution quelconque » : **faux**. Le théorème est toujours vrai ; il ne *donne le champ*
   que si les symétries rendent E constant sur la surface (étape « E·S_Gauss = Q_int/ε₀ » également abusive : les bases
   du cylindre ont un flux nul). Corrigé dans l'encadré du théorème (cours, dernière section).
2. **Cours, ancien §4** : un bloc « Champ magnétostatique — rappels » (fil infini par Ampère, solénoïde, force de Lorentz)
   égaré dans l'électrostatique, avec un résultat hors programme PTSI (Ampère) présenté sans réserve. Retiré ; la force
   de Lorentz complète est citée au §2 avec renvoi au chapitre `lorentz`.
3. **Notations divergentes avec `es2`** : \(\hat r\), \(\vec\nabla V\), \(\oiint\), énergie notée \(E\) (confondue avec le champ),
   unités F/m, V/m. Alignées sur `es2` : \(\vec u_{P\to M}\), \(\overrightarrow{\operatorname{grad}}\,V\), \(\oint_\Sigma\vec E\cdot\vec n\,\mathrm dS\),
   \(W_e\), \(w_e\), F·m⁻¹, V·m⁻¹, écartement \(e\) du condensateur (« noté \(d\) dans de nombreux énoncés »).
4. **Ancien exo 05** (solénoïde + électron) : électromagnétisme hors sujet, et « Équilibre : evB = mv²/r » est une
   formulation fausse (il n'y a pas d'équilibre : c'est le PFD du mouvement circulaire). Exercice retiré (voir doutes).
5. **Ancien exo 04** (boule chargée, Q = 1 µC, R = 5 cm) : E(R) = 3,6 MV·m⁻¹ dépasse le champ de claquage de l'air, sans
   commentaire. Gardé (exo 07) avec une question qui l'exploite (charge maximale ≈ 0,8 µC).
6. **Ancien concours 2** (« deux charges ») : la racine parasite x = 2d/3 de l'équation élevée au carré n'était pas
   discutée, ni l'absence de zéro pour x < 0. Ajouté (exo 03).
7. **Cartes** : 20 « r = mv/(|q|B) (balance force centripète et Lorentz) » : condition \(\vec v_0\perp\vec B\) absente et idée
   d'équilibre erronée ; 14 « E = CV²/2 » : notations contraires au cours (E = champ, V = potentiel) ; 21, 22 (dipôle) et
   24 (conducteur en équilibre) : hors programme des deux années, non signalé.
8. Un « CONCOURS PT » pour un chapitre non exigible en PTSI, et deux parties en double (condensateur de l'exo 03 et du
   concours 1, sphère de l'exo 04 et du concours 1) : fusionnés.

Tous les calculs des anciens corrigés gardés ont été refaits (`verif_es.py`) : justes.

## Cours (`es-cours.src.html`, 4,6 k → 59,5 k caractères dont ≈ 34 k de figures)
Encadré d'ouverture `.hors-prog` « Aperçu de la 2ᵉ année · Non exigible en PTSI », renvoi à `#estat2a/cours`, et liste des
points **déjà exigibles en PTSI** (renvois `#lorentz/cours`, `#premierordre/cours`), signalés sur place par des notices
« Exigible dès la PTSI ».

| Section | Contenu | Exemple traité (vérifié) |
|---|---|---|
| §1 Charge et loi de Coulomb | charge (quantifiée, conservée), Coulomb vectoriel, \(k\), rapport électrique/gravitation \(2\times10^{39}\) | deux billes électrisées : 4,0 mN contre 2,0 mN de poids, 3·10⁻¹⁵ N de gravitation, 1 électron sur 500 milliards |
| §2 Champ électrostatique | définition, charge ponctuelle, superposition, tableau d'ordres de grandeur, \(\vec a = q\vec E/m\) (PTSI), Lorentz complète | +q/−q sur la médiatrice (3-4-5) : 8,6·10³ V·m⁻¹ ; **figure 1** (construction à l'échelle) |
| §3 Potentiel et énergie potentielle | dV = −E·dℓ, gradient, potentiel d'une charge et superposition, champ uniforme U = Eℓ, \(E_p = qV\), travail, eV | V = 0 mais E ≠ 0 ; particule α sous 3,0 kV : 6,0 keV, 5,4·10⁵ m·s⁻¹ |
| §4 Lignes et équipotentielles | définitions, cinq propriétés, \(E\approx\Delta V/\Delta n\), renvoi au Simulateur | **figure 2** : carte calculée +4q/−q (lignes à flux égal, 4 sur 16 aboutissent sur −q, point nul à 2a au-delà de −q) ; estimation 4,0·10³ V·m⁻¹ |
| §5 Condensateur plan | modèle, E = σ/ε₀ = U/e, C = ε₀S/e, \(W_e\), \(w_e\), lien \(\mathcal E_C = \tfrac12Cu_C^2\) (PTSI) | 0,71 nF, 2,0 MV·m⁻¹, 0,71 µC, 0,35 mJ ; 56 m² pour 1 µF dans l'air, 0,17 m² avec un film de 5 µm ; **figure 3** : effets de bord (Laplace résolu numériquement) |
| Pour aller plus loin · ce que la 2ᵉ année ajoute | symétries, théorème de Gauss, tableau boule/sphère/fil/plan ; dipôle et conducteurs signalés hors programme des deux années | retrouver E = σ/ε₀ du condensateur par superposition de deux plans (1,0 + 1,0 MV·m⁻¹) |

## Méthodes (`es-meth.src.html`) : 5 + « pièges » → 6 méthodes (étapes, exemple éclair chiffré, piège)
1 superposition (q₁ = +2 nC, q₂ = −1 nC : 1,8·10⁴ V·m⁻¹, incliné de 9°) · **2 comparer force électrique et poids (nouvelle,
PTSI)** · 3 potentiel, tension, travail (420 V ; 4,2·10⁻⁷ J) · 4 bilan d'énergie d'une particule accélérée (électron
sous 150 V : 7,3·10⁶ m·s⁻¹ ; PTSI) · **5 lire une carte (nouvelle)** · 6 condensateur plan (0,22 nF ; Q ou U constant).
Note finale : Gauss et symétries → méthodes 1 et 3 de `es2`. L'ancienne méthode « Appliquer le théorème de Gauss »
(fautive, point 1) est remplacée par l'encadré du cours et ce renvoi.

## Exercices (`es-exos.src.html`) : 8 → 8 (aucun « Concours PT », conformément au complément 1A)
| n° | Titre | Niveau | Origine |
|---|---|---|---|
| 01 | Champ et potentiel d'une charge ponctuelle | ★☆☆ | ancien 01, + comparaison au claquage et distance où E = 100 V·m⁻¹ (13 m) |
| 02 | **Une gouttelette d'huile en lévitation** (poids/force électrique, sens du champ, Millikan) | ★☆☆ | nouveau, PTSI |
| 03 | Deux charges : champ nul et potentiel nul | ★★☆ | ancien concours 2, raisonnement complété |
| 04 | **Spectromètre à temps de vol : isotopes du lithium** (eU, vitesse, t ∝ √(m/q), phase d'accélération) | ★★☆ | nouveau, PTSI |
| 05 | **Lire une carte de champ : deux charges inconnues** (figure calculée cotée en kV ; signes, rapport 4, q = 1 et 4 nC, ΔV/Δn, travail, col instable) | ★★☆ | nouveau |
| 06 | Condensateur plan : capacité, énergie, claquage (+ condensateur isolé dont on double l'écartement) | ★★☆ | anciens 03 et concours 1-B fusionnés |
| 07 | Sphère chargée en volume ou en surface (Gauss, saut σ/ε₀, claquage) | ★★☆ | anciens 04 et concours 1-A fusionnés |
| 08 | **Compteur Geiger : le champ intense d'un fil fin** (Gauss pour le fil, U = λ/(2πε₀) ln(b/a), 6,0 MV·m⁻¹ au fil, gaine d'avalanche ≈ 38 µm) | ★★★ | ancien 02 étendu |

Retirés : ancien 05 (solénoïde et cyclotron, magnétisme : relève de `lorentz`) et ancien 06 (dipôle, hors programme en
PTSI comme en PT ; le résultat reste dans les cartes 21-22, désormais signalées).

## Cartes
- **Corrections** (`es-cartes-corr.json`, questions inchangées) : 14 (énergie du condensateur en \(W_e\), lien \(\mathcal E_C\)),
  20 (cercle si \(\vec v_0\perp\vec B\), force magnétique centripète), 21 et 22 (préfixe « Hors programme en PTSI (pour aller
  plus loin) : »), 24 (justification par dV = −E·dℓ ; conducteur en équilibre signalé hors programme).
- **Ajouts** (`es-cartes-ajout.js`, 5 cartes, toutes sur des savoir-faire exigibles en PTSI, donc sans préfixe) :
  rapport électrique/gravitation (val), accélération dans un champ uniforme (form), vitesse sous une tension U (form),
  électron-volt (val), champ entre deux plaques et claquage (form).

## Couverture (avant → après)
| Capacité | Cours | Méthode | Exercice | Carte |
|---|---|---|---|---|
| PTSI 2.4 : comparer force électrique et gravitation/poids | — → §1 | — → M2 | — → 02 | — → + rapport |
| PTSI 2.4 : mouvement dans E uniforme (a constant) | — → §2 | M4 (3 lignes) → M4 | — → 02, 04 | — → + accélération |
| PTSI 2.4 : vitesse d'une particule accélérée (bilan) | — → §3 | M4 → M4 | — → 04 | 23 → + vitesse, eV |
| PTSI électrocinétique : énergie du condensateur | §4 → §5 | M3 → M6 | 03, CPT1 → 06 | 14 (corrigée) |
| PT : Coulomb, champ, superposition, ordres de grandeur | §1 → §1, §2 | M2 → M1 | 01, CPT2 → 01, 03 | 0-3 |
| PT : potentiel, d.d.p. comme circulation | §2 → §3 | M2 → M3 | 01, CPT2 → 01, 03, 05, 08 | 4-6, 23 |
| PT : lignes, équipotentielles, lecture de carte | 2 lignes → §4 + figure | — → M5 | — → 05 | 7, 24 |
| PT : condensateur plan | 1 ligne → §5 + figure | M3 → M6 | 03 → 06 | 13 → + plaques |
| PT : symétries, Gauss, sphère/fil/plan | §3 → pour aller plus loin | M1 (faux) → renvoi `es2` | 02, 04, CPT1 → 07, 08 | 8-12 |
| Hors programme (dipôle, conducteurs) | non signalé → signalé | — | 06 → retiré | 21, 22, 24 → préfixées |

## Notations (identiques à `es2`)
\(\vec F_{P\to M}\), \(\vec u_{P\to M}\), \(\varepsilon_0 = 8{,}854\times10^{-12}\ \text{F·m}^{-1}\), \(\vec E\), \(V\), \(U_{AB} = V(A)-V(B)\),
\(\overrightarrow{\operatorname{grad}}\,V\), \(E_p = qV\), \(W_{A\to B}\), \(\Phi\), \(\oint_\Sigma\vec E\cdot\vec n\,\mathrm dS = Q_{\text{int}}/\varepsilon_0\), \(\sigma\), \(\lambda\),
\(C = \varepsilon_0S/e\), \(W_e\), \(w_e = \varepsilon_0E^2/2\). Lien avec la PTSI : \(\mathcal E_C = \tfrac12Cu_C^2\) (électrocinétique). Exercices :
écartement \(d\) quand une charge \(e\) intervient (comme l'exo 06 de `es2`).

## Doutes
- L'unique « attention » de `verif_src.py` (pas de bloc AU PROGRAMME) est voulue ; le contournement (écrire la chaîne en
  capitales dans l'encadré) a été jugé artificiel.
- Les cartes 15-17 et 19-20 (solénoïde, fil infini, force magnétique, μ₀, rayon) sont du magnétisme dans un deck
  d'électrostatique ; on ne peut pas les retirer. La 16 (B = μ₀I/(2πr)) n'est pas exigible en PTSI (« expressions
  fournies ») : à préfixer si le rédacteur d'`emag` adopte cette règle pour le même résultat.
- Ancien exo 05 retiré : vérifier que `lorentz` garde un exercice « rayon et période dans un champ uniforme ».
- Les cartes existantes d'électrostatique ne sont pas préfixées « Hors programme en PTSI (vu en 2ᵉ année) » (deck
  d'aperçu entier, comme `flu`) ; seules les notions hors programme des deux années le sont.
