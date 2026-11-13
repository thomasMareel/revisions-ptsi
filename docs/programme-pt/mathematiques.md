# Programme officiel de mathématiques PT (2021) ↔ chapitres du site

Inventaire tenu pendant la réécriture des cours de 2ᵉ année (demande de l'utilisateur du 2026-11-13 :
« retravaille la partie cours de tous les chapitres de deuxième année […] assure-toi que tout le
programme est bien retranscrit »).

- **Source du programme** : programme de mathématiques de la classe de PT, annexe de l'arrêté du
  13 juillet 2021 (BO n° 31 du 26 août 2021), copie hébergée par l'UPSTI
  (`upsti.fr/static/public/espace-etudiants/programmes/2021/PT/PT_Mathematiques.pdf`).
  Le programme de PTSI (même arrêté) sert à délimiter ce qui est acquis en 1ʳᵉ année.
- **Manuel de référence** (dépôt privé `cours-pt-spe`, release v1, PDF de 733 pages scannées, 17 chapitres) :
  utilisé seulement pour vérifier la couverture et les notations. Rédaction du site **originale**.
- Légende des états : ✅ couvert au niveau attendu · 🔶 couvert mais à approfondir · ❌ absent ·
  ⚠️ contient du hors-programme présenté comme exigible.

## Constat de départ (2026-11-13)

- 28 chapitres de maths de 2ᵉ année. Trois ont déjà un cours développé : `matrices2a` (réécrit le
  2026-11-11), `conred` et `surfaces` (plus de 30 000 signes). Les **25 autres** ont un cours de 1 500
  à 3 000 signes de texte : définitions et énoncés justes, mais presque aucune démonstration, aucun
  exemple traité, peu de figures.
- Le découpage du site suit à peu près celui du programme, avec trois chapitres « d'approfondissement »
  de notions de 1ʳᵉ année (`suites2a`, `integ2a`, `geo3d`) qui n'ont pas de section propre dans le
  programme de PT : ils sont gardés et recentrés sur les outils de 1ʳᵉ année que la 2ᵉ année réinvestit.
- Notions **absentes** : produit d'espaces vectoriels ; intégration terme à terme ; enveloppe d'une famille
  de droites et développée ; courbes du plan définies par une équation cartésienne (lignes de niveau,
  gradient normal) ; théorème de Cauchy linéaire énoncé pour une équation d'ordre 2 à coefficients
  variables avec la méthode « solution de l'homogène connue ne s'annulant pas » (seulement esquissée) ;
  continuité croissante/décroissante, système quasi-complet, lemme des coalitions, fonctions génératrices
  (esquissées) ; théorème des bornes atteintes, fonctions de ℝᵖ dans ℝⁿ.
- Notions **hors programme 2021** présentées comme exigibles : dual et polynômes d'endomorphisme
  (`applin2a`), comatrice, formules de Cramer et formes multilinéaires alternées (`det2a`), familles
  sommables (`series2a`), théorème de Cesàro (`suites2a`), courbes en polaires et équation polaire des
  coniques (`courbes`, `coniques`), formule de la courbure par le déterminant (`geoplane`), systèmes
  différentiels linéaires (`edo2a`). Elles passent en fin de chapitre (« Pour aller plus loin »).

## Correspondance programme → chapitres

| Partie du programme PT | Chapitre du site (id) | Avant | Après |
|---|---|---|---|
| Algèbre linéaire A a) Produit d'espaces vectoriels, somme et somme directe de sous-espaces, base adaptée | `ev2a` | 🔶 (produit absent) | ⏳ |
| Algèbre linéaire A d) Hyperplans, équations, intersection de p hyperplans | `ev2a` | 🔶 | ⏳ |
| Algèbre linéaire A b) Sous-espaces stables, endomorphisme induit, matrices par blocs | `applin2a` (+ `matrices2a` §5) | 🔶 ⚠️ (dual, polynômes d'endomorphisme) | ⏳ |
| Algèbre linéaire A c) Trace d'une matrice, d'un endomorphisme | `matrices2a` §3 (+ `applin2a`) | ✅ | ✅ encadré « Au programme » ajouté le 2026-11-13 |
| Projecteurs et symétries (1ʳᵉ année) et leur réduction (C c) | `projsym` | 🔶 | ⏳ |
| Algèbre linéaire B Déterminants (matrice, propriétés, famille de vecteurs, endomorphisme) | `det2a` | 🔶 ⚠️ (comatrice, Cramer, formes multilinéaires) | ⏳ |
| Algèbre linéaire C a) b) Éléments propres, polynôme caractéristique, multiplicité | `elempropres` | 🔶 | ⏳ |
| Algèbre linéaire C c) d) Diagonalisation, trigonalisation | `reduction` | 🔶 | ⏳ |
| Préhilbertiens A Produit scalaire, Cauchy-Schwarz, orthogonalité, Gram-Schmidt, projection orthogonale, distance | `prehilb` | 🔶 | ⏳ |
| Préhilbertiens B a)–d) Isométries, matrices orthogonales, dimensions 2 et 3 | `isometries` | 🔶 | ⏳ |
| Préhilbertiens B e) Matrices symétriques réelles, théorème spectral | `isometries` + `conred` | ✅ (`conred`) | ⏳ |
| Fonctions vectorielles a) Limite, dérivation, Leibniz, Taylor-Young, DL | `fxvect` | 🔶 | ⏳ |
| Fonctions vectorielles b) c) Courbes paramétrées, tangente, étude locale, branches infinies, support | `courbes` | 🔶 ⚠️ (polaires) | ⏳ |
| Fonctions vectorielles d) e) Longueur, abscisse curviligne, Frenet, courbure, développée, enveloppe | `geoplane` | 🔶 ⚠️ (courbure par le déterminant) ; ❌ enveloppe, développée | ⏳ |
| Séries numériques a) b) Comparaison série-intégrale, séries alternées, convergence absolue, d'Alembert, produit de Cauchy | `series2a` (+ `suites2a`) | 🔶 ⚠️ (familles sommables) | ⏳ |
| Séries entières a)–d) | `serient` | 🔶 | ⏳ |
| Intégration a)–c) Intégrales généralisées, intégrabilité, fonctions de référence | `intgene` | 🔶 | ⏳ |
| Intégration d) Intégration terme à terme | `intgene` | ❌ | ⏳ |
| Intégration e) Intégrales à paramètre (continuité, dérivation) | `intparam` | 🔶 | ⏳ |
| Outils de 1ʳᵉ année réinvestis (relations de comparaison, développements asymptotiques, suites récurrentes) | `suites2a` | 🔶 ⚠️ (Cesàro) | ⏳ |
| Outils de 1ʳᵉ année réinvestis (sommes de Riemann, Taylor avec reste intégral, inégalités intégrales) | `integ2a` | 🔶 | ⏳ |
| Probabilités A a) b) Ensembles dénombrables, univers, tribu, événements | `tribus` | 🔶 | ⏳ |
| Probabilités A c) d) f) Probabilité, continuité monotone, conditionnement, Bayes, indépendance | `espproba` | 🔶 (continuité monotone, quasi-complet absents) | ⏳ |
| Probabilités A e) g) Lois, géométrique, Poisson, couples, indépendance, coalitions | `vadisc1` | 🔶 | ⏳ |
| Probabilités B Espérance, variance, covariance, fonctions génératrices, Markov, Bienaymé-Tchebychev, loi faible | `vadisc2` | 🔶 | ⏳ |
| Équations différentielles A Ordre 2 à coefficients continus, Cauchy linéaire, DSE, solution connue | `edo2a` | 🔶 ⚠️ (systèmes différentiels) | ⏳ |
| Fonctions de deux ou trois variables a)–g) | `fpv` | 🔶 | ⏳ |
| Courbes et surfaces A a) Courbes du plan définies par une équation cartésienne | `coniques` | ❌ | ⏳ |
| Courbes et surfaces A b) Coniques (foyer, directrice, excentricité, équations réduites, paramétrages) | `coniques` | 🔶 ⚠️ (équation polaire) | ⏳ |
| Courbes et surfaces A b) Réduction d'une équation du second degré | `conred` | ✅ | ✅ encadré « Au programme » ajouté le 2026-11-13 |
| Courbes et surfaces B Surfaces paramétrées et cartésiennes, plan tangent, réglées, révolution, courbes de l'espace | `surfaces` | ✅ (sections planes, matrices de rotation absentes) | ✅ complété le 2026-11-13 (§9 sections planes et lignes de niveau, matrices de rotation) |
| Géométrie de l'espace de 1ʳᵉ année réinvestie (produits vectoriel et mixte, droites, plans, distances) | `geo3d` | 🔶 | ⏳ |
