# `statique` (prefix `stat`) — chapitre complété (SI, 1ʳᵉ année), 2026-11-21

Demande : point 4 de l'audit du 2026-11-14 (`docs/audit-2026-11/si-1a.md` §2 point 3, §5 point 5) et alignement sur le
nouveau chapitre `liaisons` (liste « À aligner dans `cine` et `statique` » de `AN1/lia-revue.md`, traitée en entier).

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `stat-cours.src.html` | cours complété (≈ 104 000 signes) : bloc « AU PROGRAMME · PTSI », 12 sections §1 à §12, « POUR ALLER PLUS LOIN · HORS PROGRAMME », 17 exemples traités chiffrés, 10 figures calculées |
| `stat-meth.src.html` | 10 méthodes (étapes nommées, exemple éclair chiffré) + encadré « Pièges classiques » |
| `stat-exos.src.html` | 11 exercices (★ à ★★★) + 1 « Concours PT » en 5 parties (14 questions) ; 11 figures |
| `stat-cartes-corr.json` | 4 cartes corrigées (réponse seule) |
| `stat-cartes-ajout.js` | 15 cartes ajoutées, en fin de deck (30 → 45) |
| `stat-cours.tpl.html`, `stat-exos.tpl.html` | gabarits (`@@FIG:nom@@`) assemblés par `stat_construire.py` |
| `stat_svg.py`, `stat_figs.py`, `stat_figs_exos.py` → `stat_figs.json` | figures calculées (classes du site, aucune couleur en dur, vecteurs en gras, indices en `tspan` de 12 px) |
| `stat_calculs.py`, `stat_calculs_meth.py`, `stat_calculs_exos.py`, `stat_calculs_concours.py` | vérification sympy / numpy de tous les exemples, éclairs et corrigés |
| `stat_harness.py`, `stat_planche.py`, `stat_deborde.js`, `stat_cartes_test.py` | rendu des figures (clair / sombre, 358 et 540 px), planches, recherche de débordement, page d'essai des cartes |

Reconstruire : `python3 stat_figs.py && python3 stat_construire.py`.

## Erreurs trouvées et corrigées

1. **PFS énoncé en équivalence** (cours §2 « si et seulement si », carte 3) : la réciproque est fausse (arbre tournant à
   vitesse constante, mécanisme mobile). Énoncé corrigé (condition nécessaire, référentiel galiléen), carte 3 corrigée.
2. **Figures du cours** : vecteurs écrits avec la flèche combinante U+20D7 (« F⃗₁ », « R⃗ », affichée en carré), libellés à
   10 px dans la figure du cône. Toutes les figures sont refaites.
3. **Figures des exercices illisibles en sombre** : elles employaient les classes `.svg-label`, `.svg-label-vel`… définies
   seulement dans le `<style>` du panneau `cine-exos`, lui-même replié dans un `<template>` (inerte) : tant que le chapitre
   Cinématique n'avait pas été ouvert, les libellés étaient sans style (encre noire par défaut, invisible en sombre) ;
   libellés à 10-11 px. Les onze figures sont refaites aux classes `.schema` du site. (Le même défaut touche `sb-exos`,
   `s2-exos` et `bode-exos`, non traités ici : déplacer les règles `.svg-*` dans la région CONTENU du grand `<style>`.)
4. **EXO 02 (levier)** : G dessiné sur le pivot au lieu de 0,1 m du côté de B ; Q3 sans réponse (« on résout pour a ») :
   résolue, \(a = 0{,}5\,mg/(F_A + mg) \approx 0{,}198\) m ; phrase contradictoire sur la position de G retirée.
5. **EXO 03 (échelle)** : « < » brut dans une formule (`\(< 58{,}9\)`) → `\lt` ; ajout de Q4 (angle minimal 51,3°).
6. **Ancien « Concours PT »** (poutre sur deux appuis, deux questions triviales, ★★) : gardé comme EXO 07 (★), complété
   (poids propre, charge triangulaire, mobilité du modèle « deux appuis simples ») ; nouveau vrai sujet concours.
7. **EXO 05 (PTV, hors programme des deux années)** : réécrit au programme (bielle = deux glisseurs, isolements successifs,
   PFS) ; le PTV devient une dernière question signalée hors programme.
8. **EXO 06** : sens du couple non précisé (le corrigé supposait le sens trigonométrique) → précisé.
9. Cartes 11 (« opposées en direction » → sens opposés) et 15 (« cône d'angle φ » → demi-angle ; « si la réaction sort du
   cône → glissement » reformulé : la réaction ne sort jamais du cône) corrigées ; carte 21 : « 1 DDL » → mobilité 1.
10. Notation « DDL » du tableau du §3 remplacée par \(n_c\) ; « h < 0 » écrit en clair dans la méthode 3 → `\lt`.

## Couverture du programme (S2) : avant → après

| Capacité (programme 2021) | Avant | Après |
|---|---|---|
| Actions à distance et de contact ; modèle local (densités linéique, surfacique, volumique) | ❌ | §1 (définitions, pression de contact, ordres de grandeur, exemple) |
| Modèle global ; torseur d'une action mécanique extérieure | §1 (torseur, transport) | §2 (notations de `liaisons`, moment par rapport à un axe, démonstration du transport, exemple 3D de la clé) |
| Torseurs glisseur et couple | ❌ | §3 (définitions, automoment, décomposition, démonstration, axe d'un glisseur plan, figure) |
| Passage du modèle local au modèle global | une phrase | §4 (poids et G, charges linéiques uniforme / triangulaire, pression uniforme plane et demi-cylindre \(pDL\), pression hydrostatique) ; §5 (pression linéaire sous un appui plan, tiers central, contact partiel) ; frein à disque (§10) |
| Torseur des actions transmissibles | liaisons en 2D seulement | §6 (dualité, tableau 3D de 8 liaisons, renvoi au tableau des 11 de `liaisons` §6, contact unilatéral) ; dénombrement \(h\) avec renvoi à `liaisons` §10-§11 |
| Référentiel galiléen, PFS, actions réciproques | §2 (PFS en équivalence) | §7 (énoncé exact, réciproque fausse, démarche, exemple 3D d'arbre en porte-à-faux) |
| Conditions et limites de la modélisation plane | ❌ | §8 (conditions, PFS plan, formes planes, \(h_{\text{plan}} \leq h\), liaisons symétriques ; exemple de la potence) |
| Statique graphique (deux et trois glisseurs) | §4 (sans exemple) | §9 (démonstration, figure calculée concourance + triangle des forces) |
| Frottement sec, lois de Coulomb | §3, §4 | §10 (lois avec \(\vec V_g\), cône, tableau de coefficients, démarche hypothèse / vérification / seuil, plan incliné, frottement réparti d'un frein à disque) ; §11 arc-boutement (coulisseau, condition \(L \le 2fd\), figure des cônes) |
| Frottement visqueux | ❌ | §12 (\(c\), \(f_v\) comme `energ2a`, exemples) |
| Résistance au roulement et au pivotement | ❌ (seulement `energ2a`, 2ᵉ année) | §12 (\(\delta\), \(\delta_p\) comme `liaisons`, figure calculée, exemple du vélo) |
| Principe des travaux virtuels | présenté au §4 (signalé HP) | déplacé en « Pour aller plus loin » |

## Contenu

**Cours.** §1 Modèle local ; §2 Torseur d'une action ; §3 Glisseur et couple ; §4 Du local au global ; §5 Pression sous un
appui plan ; §6 Actions transmissibles par les liaisons ; §7 PFS ; §8 Problème plan ; §9 Deux ou trois glisseurs ;
§10 Coulomb ; §11 Arc-boutement ; §12 Visqueux, roulement, pivotement ; Pour aller plus loin (PTV, graphe de structure,
inertie, Hertz, inconnues hyperstatiques). Le contenu juste de l'ancien cours est conservé (BABAR, isolement, choix du
point, deux / trois forces, cône, arc-boutement, centre de gravité, stabilité). Figures : glisseur et couple ; charges
réparties ; palier (pression sur un demi-cylindre) ; vanne (pression hydrostatique) ; semelle (trois répartitions) ;
potence ; résolution graphique (concourance + triangle des forces à l'échelle) ; cône de frottement et plan incliné ;
coulisseau arc-bouté (cônes, point K à \(L/2f\)) ; résistance au roulement (réaction décalée de δ passant par le centre).

**Méthodes (10).** Isoler et faire le BAME ; écrire / transporter un torseur, glisseur ou couple ; passer du local au
global ; inconnues d'une liaison ; dénombrer et vérifier l'isostatisme ; appliquer le PFS (modèle, point, projections) ;
deux ou trois glisseurs ; Coulomb ; arc-boutement ; visqueux et roulement ; pièges.

**Exercices (12).** 01 poutre encastrée (★) ; 02 levier (★★) ; 03 échelle (★★, + angle minimal) ; 04 treillis (★★★) ;
05 bielle-manivelle par le PFS, PTV en question hors programme (★★★) ; 06 poutre encastrée, charge et couple (★★★, Q3 2ᵉ
année signalée) ; 07 poutre sur deux appuis, charges ponctuelle puis réparties (★) ; **nouveaux** : 08 panneau sur massif,
tiers central (★★) ; 09 arbre sur deux paliers, PFS 3D avec pignon et poulie (★★) ; 10 wagonnet sur rail incliné :
résistance au roulement, visqueux des paliers, freinage par adhérence (★★) ; 11 bras coulissant sur colonne,
arc-boutement et serre-joint (★★★) ; **Concours PT** : frein à sabot d'un treuil (modélisation et \(h\), équilibre du
levier dans les deux sens, auto-serrage et arc-boutement \(e \geq a/f\), maintien de la charge, modèle local de la
garniture \(2pbR\sin\beta\) et couple \(fNR\,\beta/\sin\beta\), efforts sur l'arbre et intérêt du double sabot).

**Cartes ajoutées (15).** Densités d'effort ; passage local → global ; charges réparties ; pression uniforme plane et
demi-cylindre ; glisseur ; couple ; tiers central ; frottement visqueux ; résistance au roulement ; résistance au
pivotement ; ordres de grandeur de \(f\) (`val`) ; angle limite sur plan incliné ; couple d'une garniture annulaire ;
modèle plan et liaisons symétriques ; condition d'arc-boutement d'un coulisseau. Formules en `\\( … \\)`.

## Notations (alignées sur `liaisons`, `chaines`, `energ2a`)

\(\{\mathcal T(1\to2)\} = \{\vec R(1\to2) \;;\; \vec M(P, 1\to2)\}_P\) (noté aussi \(\vec M_P\)), composantes \(X, Y, Z, L, M, N\) ;
en problème plan \(X, Y, M_z\) (la composante \(N\) de `liaisons`, renommée pour ne pas la confondre avec l'effort normal) ;
\(n_c\), \(n_s = 6 - n_c\), \(I_s\), \(E_s = 6(n-1)\), \(m\), \(h = m + I_s - 6(n-1)\) ; Coulomb \(N, T, f, f_0\) (noté aussi
\(f_s\) dans les anciennes cartes), \(\varphi\), \(\vec V_g\) ; visqueux \(c\), \(f_v\) ; roulement \(\delta\), pivotement \(\delta_p\).

## Vérifications

- Tous les nombres recalculés (`stat_calculs*.py`, sympy et numpy) : exemples du cours, éclairs des méthodes, corrigés
  (anciens et nouveaux), concours.
- `verif_src.py` : aucune erreur ni « attention » sur les trois panneaux.
- `apercu_src.py` (copie `AN1/site/index.html`) à 390 et 1 440 px : `merr`, `brut`, `larges` vides, aucune erreur JS,
  pas de débordement de page (cours, méthodes, exercices) ; captures regardées ; figures regardées en clair et en sombre
  (`stat_harness.py`).
- Cartes : `corriger_cartes.py stat … --essai` (4 réponses) et `ajouter_cartes.py stat … --essai` (30 → 45) sans erreur ;
  textes rendus sans erreur MathJax (`_tmp/stat-cartes-test.src.html`).

## Doutes et points à valider

1. Le cours dépasse la cible « maths » (≈ 104 000 signes, dont ≈ 45 000 de figures SVG) ; comparable à `liaisons`.
2. Coefficients de frottement, δ et pressions admissibles : ordres de grandeur usuels des cours de SI (variables selon les
   sources), donnés comme tels.
3. Carte 3 corrigée par sa réponse seule (question inchangée, progression conservée) ; les cartes 14 et 25 gardent \(f_s\),
   le cours dit « \(f_0\) (noté aussi \(f_s\)) ».
4. L'EXO 06 Q3 (torseur de cohésion) reste signalé « 2ᵉ année », comme avant.
5. Le titre du chapitre (« Statique ») pourrait devenir « Actions mécaniques et statique » pour refléter le contenu
   (modèle local, frottements) ; non modifié.
