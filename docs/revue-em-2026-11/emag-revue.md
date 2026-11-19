# Revue du chapitre `emag` — « Champ magnétique et actions de Laplace » (1ʳᵉ année, prefix `emag`)

Revue du 2026-11-19, d'après `CONSIGNES-EM.md` et `CONSIGNES-EM-1A.md`. Programme : PTSI 2021, parties 1.7.1 et 1.7.2
(`/home/user/pdf-pt/prog/ptsi.txt`, l. 1650-1720). Rédaction originale ; toutes les valeurs numériques recalculées
(`emag_calculs.py` pour le cours et les méthodes, `emag_calculs_exos.py` pour les exercices, sympy pour les dérivées).

## Fichiers produits (dans `EM/`)

| Fichier | Contenu |
|---|---|
| `emag-cours.src.html` | cours réécrit en entier : bloc « AU PROGRAMME · PTSI », 12 sections §1-§12, « POUR ALLER PLUS LOIN », 15 exemples traités chiffrés, 11 figures calculées (127 ko, dont ≈ 80 ko de SVG) |
| `emag-meth.src.html` | 10 méthodes (étapes, exemple éclair chiffré, pièges) |
| `emag-exos.src.html` | 12 exercices (11 + « Concours PT »), dans un seul `.exo-wrapper`, 2 figures |
| `emag-cartes-corr.json` | 6 réponses corrigées (questions inchangées) |
| `emag-cartes-ajout.js` | 15 cartes ajoutées en fin de deck (25 → 40) |
| `figs_emag.py` / `figs_emag.json` | figures (brouillon repris et largement corrigé, 4 figures nouvelles) |
| `emag-cours.tpl.html`, `emag-exos.tpl.html` | gabarits (`@@FIG:nom@@`), assemblés par `construire.py` |
| `emag_tmp/` | outils de travail : aperçu des figures, détecteur de formules défilantes, générateur des cartes |

Contrôles passés : `verif_src.py` (aucune erreur ni « attention ») ; `apercu_src.py` à 390 et 1440 px pour les trois
panneaux : `merr`, `brut`, `larges` vides, aucune erreur JS ; captures du cours et des exercices regardées ;
`corriger_cartes.py --essai` (6 corrigées) et `ajouter_cartes.py --essai` (25 → 40) sans erreur.

## Erreurs trouvées dans l'existant (et corrigées)

1. **Exo 01 Q3** : en un point à l'est d'un câble vertical à courant montant, le champ pointe vers le **nord**
   (\(\vec e_z\wedge\vec e_x = \vec e_y\)), pas vers le sud.
2. **Exo 04 Q3** (fils parallèles) : « 25 N par cm » → \(25\ \text{N·m}^{-1}\), soit 0,25 N par cm ; le « principe du
   déclencheur magnétique » par répulsion était inexact (le déclencheur usuel est un électroaimant) : nuancé (« certains
   disjoncteurs limiteurs exploitent cette répulsion »).
3. **Exo 06** (circuit magnétique avec entrefer, hors des deux programmes) : \(\mu_0S = 1{,}26\times10^{-10}\) et non
   \(10^{-11}\) ; d'où \(\mathcal R_{air} = 8{,}0\times10^{6}\) (et non \(8\times10^{7}\)), \(B \approx 96\ \text{mT}\) (et non 12 mT),
   \(L \approx 3{,}8\ \text{mH}\) (et non 0,5 mH). Exercice **retiré** (faux, et hors programme de physique des deux années) ;
   les notions restent résumées dans « Pour aller plus loin » pour les cartes 14 à 17 et 19.
4. **Exo 03** (rails) : bilan « \(P_{elec} = EI = P_{mec}\) » sans convention de signe ; refait (exo 09) avec
   \(e = -B\ell v\) en convention générateur et \(\mathcal P_{\text{Laplace}} + eI = 0\), cohérent avec le chapitre Induction.
5. **Ancien « Concours PT »** : partie A fondée sur le théorème d'Ampère (hors programme PTSI) ; repris en exo 05 avec
   les symétries et le champ admis ; nouveau sujet « Concours PT ».
6. **Cours** : la loi de Biot et Savart était posée en encadré « Définition » du champ (hors programme des deux années) ;
   le théorème d'Ampère et la conservation du flux occupaient une section ; \(\vec H\) et la réluctance une autre : tout
   cela est passé en « Pour aller plus loin ». Notations \(\vec m\), \(\vec C\) remplacées par \(\vec{\mathcal M}\), \(\vec\Gamma\).
7. **Méthodes** : 3 des 5 méthodes portaient sur du hors-programme (Ampère, circuits magnétiques, \(\vec B\)/\(\vec H\)) ;
   remplacées.
8. **Cartes** (`emag-cartes-corr.json`) :
   - n° 9 : la force de Lorentz « courbe la trajectoire sans modifier la vitesse » → sans modifier la **norme** de la vitesse ;
   - n° 13 : « lignes toujours fermées (∇·B = 0) » → elles ne partent d'aucun point, se referment ou vont à l'infini ;
     \(\operatorname{div}\vec B = 0\) signalé comme vu en 2ᵉ année ;
   - n° 7 : « I∧B donne F » (imprécis, et la seconde phrase n'était pas une règle) → produit \(I\,\mathrm d\vec\ell\wedge\vec B\),
     règle des trois doigts ;
   - n° 10, 11, 12 : notations \(m\), \(\vec C\) → \(\vec{\mathcal M}\), \(\vec\Gamma\) (questions inchangées).
9. **Brouillon de figures** (`figs_emag.py` de la session précédente) : légende fausse (« flux égal entre deux lignes
   voisines » pour la spire, la bobine et l'aimant, dont les lignes partent de points choisis) ; pointes de flèche trop
   grosses (épaisseur de trait de la classe) ; remplissages `*-soft` qui rendaient presque invisibles les contours du même
   élément (opacité) ; flèches empilées près des fils de la spire ; libellés superposés (Helmholtz, cadre) ; sens « I »
   mal placé. Tout corrigé ; marques des spires compactées (bobine : 16 → 12 ko).

## Couverture du programme PTSI (1.7.1 et 1.7.2)

| Capacité exigible | Avant | Après (cours · méthode · exercice · carte) |
|---|---|---|
| Exploiter une carte de champ (uniforme, faible, sources) | ❌ | §2 + figure calculée · M1 · exo 02 · carte « espacement » |
| Tracer les cartes : aimant droit, spire, bobine longue | 🔶 (dessin du solénoïde seul) | §4, §5 + 2 figures calculées · M2 · exo 02 · carte « aimant droit » |
| Dispositif de champ quasi uniforme | ❌ | §6 (bobine, Helmholtz, entrefer) + figure · exo 06, concours · carte |
| Ordres de grandeur (aimants, IRM, Terre) | ❌ (cours) | §1 (tableau), §5 (Terre, figure) · M4 · exos 01, 07 · carte `val` |
| Symétries et invariances | ❌ | §3 + figure · M3 · exos 02, 05 · carte |
| Évaluer un champ à partir d'expressions fournies | 🔶 | §4, §5 · M4 · exos 01, 06, 07 |
| Moment magnétique (boucle, aimant, ordre de grandeur) | 🔶 | §7 + figure + tableau · M5 · exos 03, 07 · cartes 10 + ajout `val` |
| Force de Laplace, champ extérieur / champ propre | 🔶 (sans le champ propre) | §8 · M6 · exos 04, 05, 08 · cartes |
| Résultante sur une barre (établir) | 🔶 | §8 (démonstration) · M6 · exos 04, 09 · carte |
| Puissance des forces de Laplace | ❌ | §9 · M7 · exos 09, 10 · carte |
| Couple sur une spire rectangulaire, \(\vec{\mathcal M}\wedge\vec B\), puissance | 🔶 (formule seule) | §10 (démonstration + figure) · M8 · exos 11, 03 · cartes |
| Aimant dans un champ uniforme, équilibre, stabilité, boussole | 🔶 (exercice seul) | §11 + figure · M9 · exos 03, 11, concours · cartes |
| Champ tournant (deux ou trois bobines), aiguille entraînée | ❌ | §12 + figure (démonstration triphasée) · M10 · concours · cartes |

## Cours : plan

AU PROGRAMME · PTSI ; §1 Le champ magnétique et ses sources (ordres de grandeur) ; §2 Lignes et cartes de champ ;
§3 Symétries et invariances ; §4 Fil, spire, bobine plate (expressions fournies) ; §5 Bobine longue, aimant droit,
champ terrestre ; §6 Champ quasi uniforme (Helmholtz : démonstration de \(d = R\)) ; §7 Moment magnétique ; §8 Force de
Laplace (origine microscopique dépliable, champ propre, résultante, fils parallèles) ; §9 Puissance, rails alimentés,
haut-parleur ; §10 Couple sur un cadre (démonstration vectorielle) ; §11 Équilibre, stabilité, \(E_p\), oscillations
d'une boussole ; §12 Champ tournant, triphasé, moteur synchrone ; POUR ALLER PLUS LOIN (Biot et Savart, Ampère et flux
→ `magnetostat`, milieux ferromagnétiques et circuits magnétiques, renvoi de l'inductance au chapitre Induction).

Figures (calculées) : `lecture` (fil dans un champ uniforme, nouvelle), `deuxfils`, `cartes1` (fil, spire),
`cartes2` (bobine, aimant), `terre` (modèle dipolaire, inclinaison 64° en France, nouvelle), `helmholtz`, `moment`,
`rails`, `cadre`, `energie`, `tournant` ; exercices : `ex_deuxfils` (deux fils, courants 1 : 3, nouvelle), `cc_boussole`.

## Méthodes (10)

1 Lire une carte · 2 Tracer l'allure d'une carte · 3 Symétries et invariances · 4 Évaluer un champ avec une expression
fournie · 5 Orienter un circuit, sa normale, son moment · 6 Force de Laplace sur une barre ou un circuit · 7 Puissance des
actions de Laplace · 8 Couple sur une spire ou un aimant · 9 Équilibre, stabilité, oscillations · 10 Champ tournant.

## Exercices (12)

| N° | Titre | Origine |
|---|---|---|
| 01 ★ | Champ d'un câble et boussole déviée | ancien 01, corrigé (sens du champ) et complété (boussole à l'est / au sud) |
| 02 ★ | Lire une carte : deux fils parallèles | nouveau (figure calculée, courants 1 : 3) |
| 03 ★ | Moment magnétique et couple sur une spire carrée | ancien 05, notations et travail de retournement |
| 04 ★ | La balançoire de Laplace | nouveau |
| 05 ★★ | Bobine longue : champ, fil et petite spire | ancien « Concours », sans Ampère (symétries + champ admis) |
| 06 ★★ | Bobines de Helmholtz, compensation du champ terrestre | nouveau |
| 07 ★★ | Aimants : moment magnétique et ordres de grandeur (Terre) | nouveau |
| 08 ★★ | Force entre deux fils parallèles | ancien 04, corrigé + actions réciproques |
| 09 ★★ | Rails de Laplace alimentés : effet moteur | ancien 03, refait (convention générateur) |
| 10 ★★ | Haut-parleur électrodynamique | nouveau |
| 11 ★★★ | Cadre rectangulaire : couple, oscillations, principe du moteur | nouveau |
| Concours PT ★★★ | Boussole, bobines de Helmholtz et champ tournant (3 parties, 11 questions) | nouveau |

Retirés : ancien 02 (inductance d'un solénoïde par Ampère : hors programme et relevant du chapitre Induction) et ancien
06 (circuit magnétique, faux et hors programme des deux années).

## Cartes

Corrigées : n° 7, 9, 10, 11, 12, 13 (voir plus haut). Ajoutées (15) : ordres de grandeur (`val`), lecture d'une carte,
carte d'un aimant droit, règles de symétrie, face nord, pôle magnétique proche du nord géographique, dispositifs de champ
uniforme, moment d'un aimant usuel (`val`), résultante sur une barre (`form`), champ extérieur / champ propre, puissance
des actions de Laplace (`form`), couple sur un cadre (`form`), période d'une boussole (`form`), champ tournant (`form`),
moteur synchrone. Les cartes hors programme existantes (3, 4, 14-17, 19, 22, 23) gardent leur préfixe.

## Notations retenues (alignées sur `mgs` et le brouillon d'`induction`)

\(\vec B\), \(\mu_0 = 4\pi\times10^{-7}\ \text{H·m}^{-1}\), \(\vec{\mathcal M} = IS\,\vec n\) (normale par la main droite),
\(\vec\Gamma = \vec{\mathcal M}\wedge\vec B\), \(\theta = (\vec B, \vec n)\) orienté par \(\vec e_\Delta\), \(\Gamma_\Delta = -\mathcal MB\sin\theta\),
\(E_p = -\vec{\mathcal M}\cdot\vec B\), \(\mathrm d\vec F = I\,\mathrm d\vec\ell\wedge\vec B\), \(\vec F = I\,\overrightarrow{AB}\wedge\vec B\),
\(\mathcal P = \vec F\cdot\vec v\) et \(\Gamma_\Delta\,\omega\), bobine longue \(B = \mu_0 nI\), \(n = N/L\) ; plans \(\Pi\) / \(\Pi^*\) ;
⊙ / ⊗ pour les courants sortant / entrant ; \(e = -B\ell v\) en convention générateur (exo 09, comme `induction`).

## Doutes et points à signaler

- **Divergence de notation** : le rayon d'une spire est \(R\) ici (usage de PTSI), \(a\) dans la section hors programme de
  `mgs` (où \(a\) est aussi le rayon du fil épais). À harmoniser éventuellement dans `mgs`.
- \(E_p = -\vec{\mathcal M}\cdot\vec B\) n'est pas cité par le programme : présenté comme conséquence du couple (stabilité).
  La force sur un aimant en champ non uniforme n'est mentionnée que qualitativement.
- Ordres de grandeur estimés : aiguille de boussole \(\sim10^{-2}\ \text{A·m}^2\) (aiguille d'acier de ≈ 0,5 g) ; record
  de champ permanent ≈ 45 T ; « aimant usuel ≈ 1 A·m² » (via \(\mathcal M \approx B_rV/\mu_0\), donné dans l'exo 07).
- La carte n° 20 (inductance d'un solénoïde) relève du chapitre Induction ; gardée (pas de retrait).
- Taille du panneau Cours : 127 ko (11 figures). Quelques formules en bloc de démonstrations ou de solutions défilent
  encore légèrement au téléphone (≤ 20 % de dépassement, défilement prévu par le site) ; aucune ne déborde de la page.
- Titre du chapitre inchangé (« Champ magnétique et actions de Laplace »), il correspond au contenu.
- Le rédacteur du chapitre Induction doit garder les renvois : rails couplés (§8 de son brouillon), moteur à courant
  continu, inductance ; le cours `emag` y renvoie par `#induction/cours`.
