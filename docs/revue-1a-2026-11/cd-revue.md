# `contderiv` (prefix `cd`) — compte rendu, 2026-11-21

Audit `docs/audit-2026-11/maths-1a.md` : §2 point 6 (dérivabilité), §3 (hors-programme et doublons), §5 points 3 et 8.
Remise en ordre des trois chapitres `contderiv`, `asympt`, `dl` **sans recouvrement** : `contderiv` = limites,
continuité, dérivabilité (jusqu'à la classe \(\mathcal C^k\), Leibniz et le cas complexe) ; `asympt` = relations de
comparaison ; `dl` = développements limités. Cours réécrit en entier au format de la 1ʳᵉ année, méthodes et exercices
refaits ou complétés, cartes relues et complétées.

## Fichiers produits

| Fichier | Contenu |
|---|---|
| `cd-cours.src.html` | cours complet (92 655 car., dont ≈ 33 000 de SVG) : bloc « AU PROGRAMME · PTSI », 12 sections, 19 exemples traités, 5 figures, « Pour aller plus loin » — construit par `cd_construire.py cd` depuis `cd-cours.tpl.html` et `cd_figs.json` |
| `cd-meth.src.html` | 10 méthodes (exemple éclair vérifié chacune) + encadré des pièges |
| `cd-exos.src.html` | 11 exercices + 1 « Concours PT » en trois parties |
| `cd-cartes-corr.json` | 1 carte corrigée (réponse seule) |
| `cd-cartes-ajout.js` | 14 cartes nouvelles (27 → 41) |
| Scripts | `cd_calculs.py` (exemples du cours), `cd_calculs_exos.py` (méthodes, exercices, concours), `cd_figs.py` + `cd_svg.py` (figures ; `cd_svg.py` sert aussi à `asy` et `dl`), `cd_construire.py` (assemblage, commun aux trois chapitres), `cd_voir.py` (captures des figures), `cd_patch.py` + `cd_r*.py` (retouches), `cd_cartes_rendu.py` (rendu MathJax des cartes) ; panneaux d'origine `cd_orig_{cours,meth,exos}.html` |

## Erreurs et défauts corrigés

1. **Hors-programme présenté comme exigible** (audit §3) : le §4 « Fonctions convexes, inégalité de Jensen » était une
   section du cours (même signalée), la méthode 5 et l'EXO 05 portaient sur la convexité, l'exercice « Concours PT »
   s'intitulait « TVI et inégalité de convexité ». Convexité, Jensen, continuité uniforme et Heine sont maintenant
   regroupés dans « Pour aller plus loin · Hors programme » ; méthode et exercice de convexité retirés, concours remplacé.
   La caractérisation séquentielle de la limite (réciproque) n'était pas dans le chapitre ; elle est ajoutée en
   « Pour aller plus loin », seul le sens direct (image d'une suite, au programme) étant au §1.
2. **Carte 23** (« Définition d'un point d'inflexion ») présentée comme exigible : réponse corrigée, préfixée
   « Hors programme en PTSI », avec renvoi à la position courbe/tangente (au programme).
3. **EXO 02 d'origine** (point fixe de \(\cos\)) : la question demandait la solution « à \(10^{-3}\) près par
   dichotomie », la correction sautait de \([0{,}7 ; 0{,}8]\) à \(0{,}74\) sans dichotomie. Tableau complet des 7 étapes
   (EXO 04 désormais), nombre d'étapes justifié.
4. **EXO 03 d'origine** Q3 : l'énoncé indiquait « appliquer le TAF à \(\ln\) sur \([1, 1 + x]\) », la correction faisait
   une étude de fonction avec un argument confus pour \(x \in\, ]-1, 0[\) (« car on vient de la droite en croissant »).
   Refait proprement par les accroissements finis des deux côtés (EXO 06 Q2-Q3), fusionné avec l'ancien EXO 02 de `dl`
   (même inégalité).
5. **Ancien EXO 01 de `dl`** (repris ici en EXO 03) : « \(\arctan\sqrt x\) n'est pas dérivable en 0, car \(\sqrt x\) ne
   l'est pas » est un raisonnement faux en général ; justifié maintenant par la limite de la dérivée (\(+\infty\)).
6. **Notation** : « théorème de Weierstrass » remplacé par « théorème des bornes atteintes » (programme, audit §4).
   L'erreur de l'audit « une limite en \(a\) existe ssi \(\ell^- = \ell^+\) » était déjà corrigée dans la version en ligne ;
   gardée, avec le contre-exemple et la distinction « \(f\) définie ou non en \(a\) ».
7. **Doublons** avec `dl` §1-3 (dérivée, règles de calcul, Rolle, TAF, IAF, monotonie, convexité) : tout est
   maintenant ici, une seule fois ; `dl` y renvoie.

## Couverture du programme (« Limites et continuité », « Dérivabilité ») avant → après

| Capacité | Avant | Après |
|---|---|---|
| Limite en un point (a fini/infini, dans I ou extrémité), inégalités larges, unicité, limite = f(a) si définie, bornée au voisinage | 🔶 (définition seule) | ✅ §1 (démonstrations, deux exemples ε-η, EXO 01) |
| Limites à gauche, à droite | ✅ | ✅ §1 (recollement, contre-exemple) |
| Image d'une suite de limite a | ❌ | ✅ §1 (démonstration, \(\sin(1/x)\), EXO 01 Q4, méthode 2) |
| Opérations, inégalité large, encadrement, minoration | 🔶 (une ligne) | ✅ §2 (deux encadrements, méthode 2) |
| Théorème de la limite monotone | ❌ | ✅ §2 (idée de preuve, carte) |
| Continuité, prolongement, à gauche/droite, opérations | 🔶 | ✅ §3 (quatre exemples, méthode 3, EXO 02) |
| TVI, dichotomie, image d'un intervalle, cas strictement monotone | ✅ | ✅ §4 (démonstration par dichotomie, figure, EXO 04) |
| Bornes atteintes, image d'un segment, réciproque continue | ✅ | ✅ §5 (contre-exemples des trois hypothèses) |
| Dérivabilité, DL1, tangente, vitesse, dérivable ⇒ continue, à gauche/droite | ✅ | ✅ §6 (figure des sécantes, Euler, EXO 05) |
| Opérations, composée, réciproque, tangente à f⁻¹ | 🔶 (formules, en double avec `dl`) | ✅ §7 (démonstrations, figure exp/ln, \(\arcsin'\), EXO 03 Q5) |
| Extremum local, point critique, Rolle, égalité des AF (interprétations) | ✅ (en double) | ✅ §8 (démonstrations, figure, racines de P', EXO 07) |
| IAF, application à \(u_{n+1} = f(u_n)\), caractérisations (constante, monotone, strictement) | 🔶 | ✅ §9 (suite \(\cos\), méthodes 8-9, EXO 06, EXO 10) |
| **Théorème de la limite de la dérivée**, extension \(\pm\infty\) | ❌ | ✅ §10 (démonstration, raccord, \(e^{-1/x}\), figure \(x^2\sin(1/x)\), EXO 08, concours) |
| **Classe \(\mathcal C^k\)**, opérations, **formule de Leibniz** | ❌ | ✅ §11 (démonstration par récurrence, dérivées n-ièmes usuelles, EXO 09, méthode 10) |
| **Fonctions à valeurs complexes** (limite, dérivée, \((e^\varphi)'\), IAF ; Rolle faux) | ❌ | ✅ §12 (EXO 11) |

## Cours (12 sections)

§1 Limite d'une fonction en un point · §2 Opérations et théorèmes d'existence · §3 Continuité en un point · §4 Théorème
des valeurs intermédiaires · §5 Bornes atteintes et bijections continues · §6 Dérivabilité en un point · §7 Opérations
sur les fonctions dérivables · §8 Extremum local, Rolle, accroissements finis · §9 Inégalité des accroissements finis et
monotonie · §10 Théorème de la limite de la dérivée · §11 Classe \(\mathcal C^k\), formule de Leibniz · §12 Fonctions
à valeurs complexes · Pour aller plus loin (caractérisation séquentielle, continuité uniforme et Heine, convexité et
Jensen). Figures calculées : TVI et dichotomie pour \(x^3 + x - 1\), sécantes et tangente de \(x^2\), exp/ln et leurs
tangentes, accroissements finis pour \(x^3 - 3x\) (deux points \(c\)), \(x^2\sin(1/x)\) et sa dérivée ; vérifiées en
clair et en sombre.

## Méthodes (10)

Limite par la définition ; encadrement ou absence de limite ; continuité et prolongement ; résoudre \(f(x) = \gamma\)
(existence, unicité, dichotomie) ; dérivabilité en un point délicat ; composée, réciproque, tangente à \(f^{-1}\) ;
compter des racines avec Rolle ; inégalité par étude de fonction ou IAF ; suite \(u_{n+1} = f(u_n)\) contractante ;
dérivée \(n\)-ième. Les quatre méthodes justes d'origine sont reprises ; la méthode « convexité » est retirée.

## Exercices (12)

01 limites (définition, encadrement, absence de limite) — nouveau ; 02 = ancien 01 ; 03 = ancien EXO 01 de `dl`
+ Q5 réciproque ; 04 = ancien 02 corrigé ; 05 = ancien 04 + Q4 (\(\mathcal C^1\) non \(\mathcal C^2\)) ; 06 = ancien 03
+ ancien EXO 02 de `dl`, refait ; 07 Rolle (racines de \(P'\), \(P''\), fonction auxiliaire) — nouveau ; 08 limite de la
dérivée (raccord réglable, \(x^2\ln|x|\)) — nouveau ; 09 Leibniz (dont dérivées de \(\arctan\) en 0) — nouveau ;
10 = ancien 06 + Q4 ; 11 fonctions complexes — nouveau ; Concours PT « Une fonction de classe \(\mathcal C^\infty\) très
plate en 0 » (\(e^{-1/x}\) : continuité, \(\mathcal C^1\), toutes les dérivées, fonction bosse). Ancien EXO 05 (convexité,
hors programme) retiré.

## Cartes

Corrigée : carte 23 (réponse). Ajoutées (14) : limite de la dérivée (2 cartes + réciproque fausse), classe \(\mathcal C^k\),
Leibniz, \(\sin^{(n)}\) et \(\cos^{(n)}\), exemple \(\mathcal C^1\) non \(\mathcal C^2\), image d'une suite, limite
monotone, prolongement par continuité, \((e^\varphi)'\), Rolle faux dans \(\mathbb C\), stricte monotonie, tangente à
\(f^{-1}\). Les cartes de convexité 13-17 et 19 (déjà préfixées « Hors programme (pour aller plus loin) ») sont gardées
telles quelles.

## Notations

\(\mathcal C^k\) (comme `integrales` réécrit et `integ2a`), inégalités larges dans les définitions, « théorème des bornes
atteintes », \(\operatorname{ch}\), \(\operatorname{sh}\), \(\arctan\), \(\arcsin\), \(e^x\), \(\tau_a\) pour le taux
d'accroissement, \(\lfloor x\rfloor\) pour la partie entière.

## Doutes et points d'intégration

- **Ordre des chapitres** : `CHAP_GROUPS` range `contderiv, dl, asympt`. `dl` utilise les notations \(o\), \(\sim\) de
  `asympt` ; je recommande l'ordre `contderiv, asympt, dl` (voir `dl-revue.md`).
- La formule de Leibniz est aussi au programme dans la section « Polynômes » : le chapitre `polynomes` peut renvoyer
  au §11.
- L'EXO 02 (Q3) utilise un développement limité de \(\sin\) (outil du second semestre) : c'est signalé dans l'énoncé.
- Les chapitres renvoient à `dl` par « le chapitre des développements limités », formule valable que `dl` soit renommé
  ou non.
