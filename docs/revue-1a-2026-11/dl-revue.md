# `dl` (prefix `dl`) — compte rendu, 2026-11-21

Audit `docs/audit-2026-11/maths-1a.md` : §2 point 6 (formule de Taylor polynomiale), §3 « Doublons » (`contderiv` §3 et
`dl` §1-3 ; `dl` §4-6 et `asympt` §2), §5 points 3 et 8. Le chapitre « Dérivation et DL » est recentré sur les
**développements limités** : la dérivation (règles, Rolle, accroissements finis, monotonie, convexité) passe dans
`contderiv`, la définition et les règles des équivalents dans `asympt`. Cours réécrit en entier, méthodes et exercices
refaits ou complétés, cartes relues et complétées.

## Fichiers produits

| Fichier | Contenu |
|---|---|
| `dl-cours.src.html` | cours complet (66 072 car., dont ≈ 32 000 de SVG) : bloc « AU PROGRAMME · PTSI », 9 sections, 12 exemples traités, 3 figures, « Pour aller plus loin » — construit par `cd_construire.py dl` depuis `dl-cours.tpl.html` et `dl_figs.json` |
| `dl-meth.src.html` | 10 méthodes + encadré des pièges |
| `dl-exos.src.html` | 10 exercices + 1 « Concours PT » en quatre parties |
| `dl-cartes-corr.json` | 1 carte corrigée (réponse seule) |
| `dl-cartes-ajout.js` | 13 cartes nouvelles (46 → 59) |
| Scripts | `dl_calculs.py` (cours, méthodes, exercices, concours : tous les développements recalculés par `sympy.series`), `dl_figs.py` (figures, avec `cd_svg.py`), `dl_r*.py` (retouches) ; outils communs `cd_construire.py`, `cd_voir.py`, `cd_patch.py`, `cd_cartes_rendu.py` ; panneaux d'origine `dl_orig_{cours,meth,exos}.html` |

## Erreurs et défauts corrigés

1. **Doublons** : anciens §1-3 (nombre dérivé, règles, dérivées usuelles, Rolle, TAF, IAF, monotonie, convexité)
   identiques à `contderiv` §3 ; ancien §7 (définition des équivalents, équivalents usuels) identique à `asympt` §1.
   Retirés ; renvois aux deux chapitres.
2. **Hors programme présenté comme exigible** : la convexité (ancien §3) est retirée ; seul le lien « \(f''\) et
   position par rapport à la tangente » est mentionné en fin de chapitre. \(\tan\) n'est exigible qu'à l'ordre 3
   (l'ancien formulaire donnait l'ordre 5 comme usuel) : l'ordre 5 passe en « Pour aller plus loin » et en exercice
   (EXO 10, par \(\tan' = 1 + \tan^2\)) ; \(\arcsin\) est signalé non exigible.
3. **Ancienne méthode 4** (\(\frac{1}{1 + e^x}\) à l'ordre 2) : chaîne d'égalités fausse
   (« \(1 - \frac x2 + \frac{x^2}{4} - \frac{x^2}{4} + \frac{x^2}{4} + o(x^2) = \frac12 - \frac x4 + 0\cdot x^2\) » : signes faux
   et facteur \(\frac12\) apparu au milieu). Refait à l'ordre 3 (méthode 4 : \(\frac12 - \frac x4 + \frac{x^3}{48}\)), avec le
   contrôle par la parité.
4. **Ancienne méthode 1** : « pour un produit ou une composition, tous les DL intermédiaires doivent être à
   l'ordre \(n\) » — trop d'ordre pour un produit, pas assez pour un quotient dont on factorise \(x^p\). Remplacé par la
   règle du programme (factorisation par le terme prépondérant, méthode 1 et §5).
5. **Ancien piège** « \(x \sim x\) et \(\sin x - x\) n'a pas pour équivalent 0 » (illisible) et **carte 38**
   (« \(x \sim x\) mais \(\sin(x) - x\) n'est pas équivalent à 0 ») : corrigés (\(\sin x \sim x\), \(-x \sim -x\),
   \(\sin x - x \sim -\frac{x^3}{6}\) ; on n'écrit jamais \(f \sim 0\)) ; carte 38 corrigée par sa réponse.
6. **Ancien « Concours PT »** : ses deux parties reprenaient l'exemple du cours (\(\frac{x - \sin x}{x^3}\)) et celui de la
   méthode 2 (\(e^x\cos x\)). Remplacé par un vrai problème (\(x\arctan x\)).
7. Repris d'`asympt` et **corrigé** : \(\sqrt{1 + \sin x}\) à l'ordre 3 (coefficient de \(x^3\) : \(-\frac{1}{48}\), et non
   \(-\frac{1}{12}\)) ; asymptote de \(\frac{x^2 + 3x + 1}{x + 1}\) (phrase contradictoire réécrite).
8. **Manques comblés** : formule de Taylor polynomiale (§1), démonstrations de l'unicité, de la parité, de Taylor-Young
   et de la primitivation, signe au voisinage, troncature, développement en \(a \ne 0\) et en \(\pm\infty\), position
   courbe/tangente (pair/impair), conditions nécessaire et suffisante d'extremum à l'ordre 2, position par rapport à
   une asymptote (et le piège \(\sqrt{x^2} = |x|\) en \(-\infty\)), dérivation d'un développement (contre-exemple
   \(x^3\sin(1/x)\)).

## Couverture du programme (« Analyse asymptotique » b, et « Polynômes » d) avant → après

| Capacité | Avant | Après |
|---|---|---|
| Formule de Taylor polynomiale | ❌ (absente de toute la 1ʳᵉ année) | ✅ §1 (démonstration, exemple, EXO 02 Q1, carte) |
| DL à l'ordre n, unicité, troncature, se ramener en 0 | 🔶 (sans démonstration) | ✅ §2 (démonstrations, carte) |
| Signe de f au voisinage de a | ❌ | ✅ §2 |
| DL d'une fonction paire, impaire | 🔶 (« astuce ») | ✅ §2 (démonstration, EXO 10 Q2) |
| Caractérisation de la dérivabilité par DL1 | ✅ (en double) | ✅ §2 (renvoi `contderiv` §6) |
| Opérations : combinaison linéaire, produit, quotient, factorisation par le terme prépondérant | 🔶 | ✅ §5 (méthodes 1, 3, 4, EXO 04) |
| Composée sur des exemples | ✅ | ✅ §6 (\(e^{\sin x}\), méthode 5, EXO 05) |
| Primitivation | 🔶 (énoncé) | ✅ §6 (démonstration, \(\arctan\), \(\arcsin\), EXO 06) |
| Formule de Taylor-Young | ✅ (énoncé) | ✅ §3 (démonstration, trois exemples en \(a \ne 0\), local/global) |
| DL usuels à tout ordre ; \(\tan\) à l'ordre 3 | ✅ (avec \(\tan\) à l'ordre 5 comme usuel) | ✅ §4 (origine de chacun, contrôles numériques, ordres de la physique) |
| Équivalents et limites | ✅ | ✅ §7 (dont suites et \((1 + \frac1n)^n\), EXO 03, EXO 09) |
| Position courbe/tangente | 🔶 (une phrase) | ✅ §8 (règle pair/impair, figure à trois cas, EXO 07) |
| CN et CS à l'ordre 2 pour un extremum local | 🔶 (méthode seule) | ✅ §8 (démonstration, cas \(f''(a) = 0\)) |
| Détermination d'asymptotes | ✅ | ✅ §9 (position, \(-\infty\), figure, EXO 08, concours) |

## Cours (9 sections)

§1 Approcher une fonction par un polynôme (Taylor polynomiale) · §2 Développement limité : définition, unicité,
troncature · §3 Formule de Taylor-Young · §4 Les développements limités usuels · §5 Somme, produit, quotient · §6 Composée,
primitivation · §7 Application : limites et équivalents · §8 Application : tangente, position, extremum · §9 Application :
asymptotes · Pour aller plus loin (\(\tan\) à l'ordre 5, \(\arcsin\), branches paraboliques, développements
asymptotiques, convexité). Figures calculées : polynômes de Taylor de \(\exp\) (ordres 1-3) et de \(\cos\) (ordres 2-6) ;
trois positions courbe/tangente (\(\ln(1 + x + x^2)\), \(\sin\), \(2\cos x + x^2\)) ; \(x\exp(1/x)\) et son asymptote
\(y = x + 1\).

## Méthodes (10)

Choisir l'ordre ; développer en \(a \ne 0\) ou en \(\pm\infty\) ; produit ; quotient ; composée ; primitivation ; limite
ou équivalent ; tangente et position ; extremum local ; asymptote et position. Les sept méthodes d'origine sont reprises
(la méthode 4 corrigée, la méthode 1 précisée).

## Exercices (11)

01 = ancien 03 ; 02 Taylor polynomiale et développements en \(a \ne 0\) — nouveau ; 03 = ancien 04 ; 04 produits et
quotients — nouveau ; 05 composées (ancien 05 + ancien EXO 03 d'`asympt` corrigé + \(e^{\cos x}\)) ; 06 primitivation
— nouveau ; 07 tangente, position, extremum — nouveau ; 08 asymptotes (ancien 06 + ancien EXO 04 d'`asympt`, et
\(-\infty\)) ; 09 suites et DL — nouveau ; 10 unicité, parité, dérivation (\(x^3\sin(1/x)\), \(\tan\) à l'ordre 5) —
nouveau ; Concours PT « Étude locale et asymptotique de \(x\arctan x\) » (DL en 0, \(\arctan x + \arctan\frac1x\),
asymptotes et position, équation \(f(x) = 1\), suite \(n\arctan n - \frac{n\pi}{2}\)). L'ancien EXO 01 (calculs de
dérivées) et l'ancien EXO 02 (encadrement de \(\ln(1 + x)\)) sont passés dans `contderiv` (EXO 03, EXO 06).

## Cartes

Corrigée : carte 38 (réponse). Ajoutées (13) : Taylor polynomiale, DL à l'ordre 0, troncature, premier terme non nul,
réciproque de Taylor-Young fausse, dérivation d'un DL, ordre dans un quotient, \(\ln(\cos x)\), position
courbe/tangente, conditions d'ordre 2, asymptote et position, \((1 + \frac1n)^n\), Taylor-Young ou Taylor-Lagrange.
Les cartes 0-17 (dérivation) et 37-42 (équivalents) restent dans ce paquet, justes, conformément à la règle (ni retrait
ni déplacement) ; leur contenu est désormais enseigné dans `contderiv` et `asympt`.

## Notations

\(o(x^n)\), \(\mathcal C^n\), \(\operatorname{ch}\), \(\operatorname{sh}\), \(\arctan\), \(e^x\) ; développement en \(a\)
écrit avec \(h\) (\(f(a + h)\)), en \(\pm\infty\) avec \(t = \frac1x\) ; « développement limité » écrit en toutes lettres
dans les titres, « DL » seulement dans les noms de formules.

## Doutes et points d'intégration

- **Renommer le chapitre** : « Dérivation et DL » ne correspond plus au contenu. Proposition : `name:'Développements
  limités'`, `mobLabel:'Développements limités'` (entrée `CHAPTERS`). Le cours réécrit de `integrales`
  (`AN1/int-cours.src.html`, intro du §10) cite « chapitre « Dérivation et DL » » : à mettre à jour si le nom change. Mes
  trois chapitres écrivent « le chapitre des développements limités », valable dans les deux cas.
- **Ordre** : `CHAP_GROUPS` range `contderiv, dl, asympt` ; `dl` s'appuie sur les notations d'`asympt` (son intro le
  dit). Je recommande `contderiv, asympt, dl`.
- La formule de Taylor polynomiale relève de la section « Polynômes » du programme : elle ouvre ici le chapitre comme
  modèle de Taylor-Young ; si `polynomes` l'ajoute aussi, le recouvrement est d'un paragraphe.
- `dl` ne demande que \(\tan\) à l'ordre 3 ; la carte 24 d'origine donne aussi l'ordre 5 (juste, gardée).
