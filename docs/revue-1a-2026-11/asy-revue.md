# `asympt` (prefix `asy`) — compte rendu, 2026-11-21

Audit `docs/audit-2026-11/maths-1a.md` : §3 « Doublons » (`dl` §4-6 et `asympt` §2), §4 « Erreurs repérées »
(`asympt`), §5 points 3 et 8. Le chapitre est recentré sur les **relations de comparaison** (\(o\), \(O\), \(\sim\)) pour
les fonctions et les suites ; les développements limités (définition, usuels, opérations, applications) sont tous dans
`dl`, qui y renvoie. Cours réécrit en entier, méthodes et exercices refaits ou complétés, cartes relues et complétées.

## Fichiers produits

| Fichier | Contenu |
|---|---|
| `asy-cours.src.html` | cours complet (64 521 car., dont ≈ 34 000 de SVG) : bloc « AU PROGRAMME · PTSI », 8 sections, 11 exemples traités, 4 figures, « Pour aller plus loin » — construit par `cd_construire.py asy` depuis `asy-cours.tpl.html` et `asy_figs.json` |
| `asy-meth.src.html` | 9 méthodes + encadré des pièges |
| `asy-exos.src.html` | 10 exercices + 1 « Concours PT » en quatre parties |
| `asy-cartes-corr.json` | 1 carte corrigée (réponse seule) |
| `asy-cartes-ajout.js` | 13 cartes nouvelles (25 → 38) |
| Scripts | `asy_calculs.py` (cours), `asy_calculs_exos.py` (méthodes, exercices, concours), `asy_figs.py` (figures, avec `cd_svg.py`), `asy_r*.py` (retouches) ; outils communs `cd_construire.py`, `cd_voir.py`, `cd_patch.py`, `cd_cartes_rendu.py` ; panneaux d'origine `asy_orig_{cours,meth,exos}.html` |

## Erreurs et défauts corrigés

1. **Doublons** avec `dl` : l'ancien §2 (définition des DL, unicité, DL usuels, opérations) et l'ancien §4 (limites,
   tangentes, branches infinies par DL) répétaient `dl` §4-7 ; ils sont retirés (renvois au chapitre des
   développements limités). Les erreurs relevées par l'audit dans ces passages (« \(a_k = f^{(k)}(a)/k!\) » sans
   hypothèse, « dériver terme à terme », méthode 2 et carte 20 sur \(e^{\sin x}\)) avaient déjà été corrigées dans la
   version en ligne : je l'ai vérifié (sympy) ; elles disparaissent de toute façon de ce chapitre.
2. **Règle fausse sur la composition** (ancien §1) : « \(\varphi(f) \sim \varphi(g)\) seulement dans des cas
   particuliers (puissances, non pour \(\ln\)) ». Remplacée par les énoncés exacts (§4, §5) : puissance **constante**
   permise ; \(\ln f \sim \ln g\) si la limite de \(g\) est différente de 1 (démonstration) ; \(e^f \sim e^g \iff f - g \to 0\).
   Même correction pour l'ancien piège « sauf si \(f/g \to 1\) ET \(g \to +\infty\) » (incomplet : vrai aussi si \(g \to 0\)).
3. **Ancien EXO 01 Q3** : calcul incohérent « \(n\sin(1/n) = \frac{\sin h}{h}\times n\times h = 1\times n\times\frac1n = 1\cdot\frac{\sin h}{h}\) ». Réécrit.
4. **Ancien EXO 03 Q2** : \(\sqrt{1 + \sin x} = 1 + \frac x2 - \frac{x^2}{8} - \frac{x^3}{12} + o(x^3)\) est **faux** ; le
   terme \(\frac{u^3}{16}\) avait été oublié : le bon coefficient est \(-\frac{1}{48}\) (sympy). Corrigé et déplacé dans
   `dl` (EXO 05), avec l'explication de l'erreur.
5. **Ancien EXO 04 Q2** : phrase contradictoire (« la courbe traverse l'asymptote en \(x = -1\) … il n'y a pas de
   traversée »). Réécrit et déplacé dans `dl` (EXO 08 Q3).
6. **Ancien EXO 06** : Q1 justifiait la décroissance de \(I_n\) par « \(I_{n+1} \lt \frac{1}{n+2} \lt I_n\) », **faux** dès
   \(n \ge 3\) (on a \(I_n \le \frac{1}{2n} \lt \frac{1}{n+2}\)) ; Q2 utilisait « \(I_{n+1} \sim I_n\) » sans justification ;
   Q3 demandait « un équivalent de \(J_n\) » (trivialement \(\ln 2\)). Refait (EXO 09) : décroissance par
   \(x^{n+1} \le x^n\), encadrement \(\frac{1}{2(n+1)} \le I_n \le \frac{1}{2n}\), équivalent de \(J_n - \ln 2\).
7. **Ancien EXO 02** : Q1 et Q2 identiques à l'EXO 04 de `dl` (limites par DL) ; remplacé par des limites par
   équivalents (EXO 04), le DL étant réservé à `dl`.
8. **Carte 22** (« Plus \(n\) est grand, meilleure est l'approximation ») : faux pour \(h\) fixé (polynômes de Taylor de
   \(\ln(1 + x)\) en \(x = 1{,}5\)). Réponse corrigée : information locale, renvoi à Taylor-Lagrange.
9. Ancien §3 « Utilisation pour les séries » (critères de Riemann) : hors du sujet du chapitre, renvoyé à « Séries
   numériques » ; Stirling reste hors programme (fin de chapitre).

## Couverture du programme (« Analyse asymptotique », a et c) avant → après

| Capacité | Avant | Après |
|---|---|---|
| \(o\), \(O\), \(\sim\) en \(a \in \mathbb R\) ou \(\pm\infty\), par le quotient, \(g\) non nulle localement | ✅ | ✅ §1 (figure, deux exemples) |
| Liens entre les relations ; deux formes \(f/g \to 1\) et \(f = g + o(g)\) | 🔶 (une forme) | ✅ §1 (démonstration, formule nommée) |
| Étude en \(a \ne 0\) par \(f(a + h)\) | ❌ | ✅ §1 et méthode 1 |
| Croissances comparées en \(+\infty\) et en 0 traduites par \(o\) | 🔶 (en \(+\infty\)) | ✅ §2 (démonstration, figure, EXO 02) |
| Règles de manipulation de \(o\) et \(O\) | ❌ | ✅ §3 (EXO 03 vrai/faux) |
| Règles des équivalents (produit, quotient, puissance, changement de variable) | ✅ | ✅ §4 (équivalents usuels démontrés) |
| Pièges : somme, composée, \(\ln\), \(\exp\), puissance variable | 🔶 (imprécis) | ✅ §5 (cas sûrs démontrés, EXO 05, EXO 08) |
| Propriétés conservées (signe, limite) | 🔶 | ✅ §6 (démonstration) |
| Équivalent par encadrement | ❌ | ✅ §6 (démonstration, figure, EXO 06, EXO 09) |
| Calculs d'équivalents et de limites | ✅ (par DL, en double) | ✅ §7 (démarche équivalents → exponentielle → DL) |
| Cas des suites ; vitesse de convergence | 🔶 | ✅ §8 (croissances comparées des suites, figure des vitesses, EXO 07, concours) |

## Cours (8 sections)

§1 Négligeable, dominée, équivalente · §2 Croissances comparées · §3 Calculer avec \(o\) et \(O\) · §4 Calculer avec des
équivalents · §5 Sommes et composées : les pièges · §6 Propriétés conservées, équivalent par encadrement · §7 Lever une
forme indéterminée · §8 Le cas des suites (dont vitesse de convergence) · Pour aller plus loin (Stirling, développements
asymptotiques, sommation des relations de comparaison). Figures calculées : \(\sin x\) et \(x\) puis leur rapport ;
\((\ln x)^3/x\) en abscisse logarithmique ; \(x + \sin x\) encadrée et son rapport à \(x\) ; erreurs de quatre suites
(lente, géométrique, Newton) en échelle logarithmique.

## Méthodes (9)

Se ramener en 0 et choisir la relation ; croissances comparées ; équivalent d'un produit ou d'un quotient ; équivalent
d'une somme ; puissance variable, logarithme, exponentielle ; limite par équivalents ; équivalent par encadrement ;
étude d'une suite (équivalent, vitesse) ; équivalent d'un polynôme ou d'une fraction rationnelle. Les quatre méthodes
justes d'origine sont reprises (celle des asymptotes passe dans `dl`).

## Exercices (11)

01 = ancien 01 corrigé ; 02 croissances comparées — nouveau ; 03 vrai/faux sur \(o\), \(O\), \(\sim\) — nouveau ; 04 limites
par équivalents (reprend l'ancienne Q3 de l'EXO 02) ; 05 sommes (prépondérance ou compensation) — nouveau ;
06 encadrement, avec un cas où il échoue (somme de Riemann, \(\pi/4\)) — nouveau ; 07 = ancien 05 ; 08 logarithmes et
exponentielles d'équivalents — nouveau ; 09 = ancien 06 refait ; 10 polynômes, fractions rationnelles, points \(a \ne 0\)
— nouveau ; Concours PT « Une suite définie implicitement : \(x^n + x = 1\) » (existence, monotonie, limite,
\(1 - x_n \sim \frac{\ln n}{n}\), contrôle numérique et lenteur expliquée par le terme \(\ln\ln n\)).
Anciens EXO 03 et 04 déplacés dans `dl` (développements limités, asymptotes).

## Cartes

Corrigée : carte 22 (réponse). Ajoutées (13) : définition de \(O\), deux formes de l'équivalence, croissances comparées
en \(+\infty\) et en \(0^+\), règles sur \(o(x^p)\), encadrement, propriétés conservées, \(e^f \sim e^g\), puissance d'un
équivalent, équivalent d'un polynôme, étude en \(a \ne 0\), \(f(x) \sim f'(0)x\), vitesses de convergence. Les cartes
de DL du paquet (9-16, 20, 23) sont gardées (jamais de retrait ni de déplacement) : elles restent justes.

## Notations

\(f(x) = o(g(x))\) « quand \(x \to a\) », \(f \underset{a}{\sim} g\) dans les formules, \(u_n = o(v_n)\) comme
`suites2a` ; jamais \(f \sim 0\) ; \(\operatorname{ch}\), \(\operatorname{sh}\) ; croissances comparées des suites
\((\ln n)^\beta \ll n^\alpha \ll q^n \ll n! \ll n^n\) comme `suites2a`.

## Doutes

- Les comparaisons \(q^n = o(n!)\) et \(n! = o(n^n)\) ne sont pas écrites dans le programme de PTSI ; elles sont données
  avec une démonstration de deux lignes (§8), comme dans `suites2a`.
- La vitesse de convergence (lente, géométrique, quadratique) est traitée brièvement (le programme dit « revenir sur la
  problématique ») ; `suites2a` §6 l'approfondit.
- Ordre recommandé dans `CHAP_GROUPS` : `contderiv, asympt, dl` (voir `dl-revue.md`).
