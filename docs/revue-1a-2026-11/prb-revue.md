# Revue : `proba` « Probabilités sur un univers fini » (prefix `prb`), 1ʳᵉ année — 2026-11-21

Restructuration (audit `docs/audit-2026-11/maths-1a.md` §2 point 8, §3, §5 point 5) : ce chapitre porte désormais
**univers fini, probabilité, conditionnement (composées, totales, Bayes), indépendance de deux événements, indépendance
mutuelle, lemme des coalitions**. Le dénombrement est dans `denombrmt`, les variables aléatoires, lois, espérance et
variance dans `va`.

## Fichiers produits
- `prb-cours.src.html` (≈ 54 000 car., bloc « AU PROGRAMME · PTSI », 10 sections, 13 exemples, 5 figures calculées,
  « Pour aller plus loin »), `prb-cours.tpl.html`, `prb_figs.py` / `prb_figs.json`, `prb_construire.py`, `prb_svg.py`
  (outils SVG communs aux trois chapitres).
- `prb-meth.src.html` (10 méthodes), `prb-exos.src.html` (11 exercices + « Concours PT » en 4 parties).
- `prb-cartes-corr.json` (5 cartes), `prb-cartes-ajout.js` (14 cartes).
- `prb_calculs.py` (107 vérifications : énumérations de l'univers des dés, des tirages, du réseau, de la majorité, sympy).
- Anciens panneaux : `prb_old-{cours,meth,exos}.html`.

## Erreurs et défauts corrigés
- **Recouvrement triple supprimé** : l'ancien §1 (dénombrement, doublon de `denombrmt`), §3 (espérance, variance) et §4
  (lois usuelles), doublons de `va`, ont quitté le cours ; les anciennes méthodes 1, 3, 4, 5 (dénombrement, lois,
  espérance, Markov) aussi ; les anciens EXO 01 (dénombrement, doublon de `denombrmt` EXO 01) et 03 (binomiale, couvert
  par `va` EXO 03) sont retirés de ce chapitre.
- **Hors-programme présenté comme exigible** : l'espace \((\Omega, \mathcal A, P)\) σ-additif (ancien §2, encadré
  « Définitions (cadre général) ») → « Pour aller plus loin » avec renvoi à `espproba` ; lois géométrique et de Poisson
  (ancien §4, méthode 3, EXO 04 et 05) → retirées (renvoi à `vadisc1`) ; les cartes 19-23 étaient déjà préfixées.
- **Ancien « Concours PT »** : doublon de l'EXO 06 (dépistage, autres valeurs) → remplacé par un sujet original en
  quatre parties (transmission d'un bit à travers des relais : arbre, récurrence arithmético-géométrique, Bayes,
  redondance et vote majoritaire).
- **Manques comblés** : vocabulaire ensembliste ↔ probabiliste et système complet ; variables aléatoires et notation
  \((X \in A)\) ; distribution de probabilités (déterminant \(P\)) ; probabilité de la différence, croissance ;
  \(P_B\) est une probabilité (démontré) ; probabilités composées pour \(n\) événements ; convention
  \(P(A \mid B)P(B) = 0\) ; passage aux contraires ; **indépendance mutuelle** (définition, contre-exemple « deux à deux
  ne suffit pas ») ; **lemme des coalitions** (version événements, idée de preuve marquée hors programme) ;
  modélisation d'expériences indépendantes.
- Cartes : 24 (Markov) et 25 (Bienaymé-Tchebychev) sans hypothèse \(a \gt 0\), \(\varepsilon \gt 0\) → complétées ;
  1 et 18 : C(n,p) → \(\binom np\) ; 26 : question réécrite en \(\binom nk\) (réponse inchangée).

## Couverture du programme (avant → après)
| Capacité (programme PTSI, Probabilités A a, b, c, e) | Avant | Après |
|---|---|---|
| Vocabulaire ensembliste, événement élémentaire, incompatibles, système complet | partiel | §1, tableau, carte |
| Variable aléatoire, notations \((X \in A)\) | absent | §1 (renvoi à `va`) |
| Probabilité sur un univers fini, \((\Omega, P)\), distribution de probabilités | cadre σ-additif présenté comme exigible | §2 (démo), carte |
| Probabilité uniforme | oui | §2 (renvoi à `denombrmt`) |
| Réunion, différence, contraire, croissance | partiel | §3 (démo), méth. 2, EXO 01, carte |
| Probabilité conditionnelle, \(P_B\) probabilité | définition seule | §4 (démo), méth. 3, cartes |
| Probabilités composées (n événements) | 2 événements | §5 (démo), arbre, méth. 4, carte |
| Probabilités totales (convention) | oui (sans convention) | §6 (démo), arbre, méth. 5, carte |
| Bayes | oui | §7, figure en effectifs, méth. 6, EXO 04, 05, 07, 08, carte |
| Indépendance de deux événements, contraires | définition seule | §8 (démo), méth. 7, EXO 01-02, carte |
| Indépendance mutuelle ; deux à deux ≠ mutuelle | absent | §9 (démo), tableau, méth. 8, EXO 06, cartes |
| Lemme des coalitions ; n expériences indépendantes | absent | §10, figure, méth. 9, EXO 07, 11, Concours D, cartes |
| Hors programme : crible, σ-additivité, univers infinis | présentés comme cours | « Pour aller plus loin » |

## Contenu
- **Sections** : §1 univers, événements (tableau des 36 issues de deux dés) ; §2 probabilité, distribution, uniforme (dé
  truqué) ; §3 règles de calcul (chevalier de Méré) ; §4 conditionnelles ; §5 composées (arbre de l'urne) ; §6 totales
  (arbre des trois machines) ; §7 Bayes (dépistage, arbre en effectifs) ; §8 indépendance de deux événements (\(S = 7\)
  contre \(S = 8\)) ; §9 indépendance mutuelle (deux pièces, fiabilité) ; §10 lemme des coalitions (montage série-parallèle,
  premier 6 au 3ᵉ lancer).
- **Méthodes** : modéliser ; traduire « au moins / exactement » ; conditionnelle ; composées ; totales ; Bayes ;
  indépendance de deux événements ; indépendance mutuelle ; fiabilité et coalitions ; suites d'épreuves
  (\(p_{n+1} = ap_n + b\)).
- **Exercices** : 01 règles de calcul ; 02 dé truqué ; 03 tirages sans remise (gardé + Q4) ; 04 deux urnes et un dé
  (indépendance conditionnelle ≠ indépendance) ; 05 dépistage (gardé + Q3, Q4 second test) ; 06 deux à deux sans
  mutuelle ; 07 deux architectures redondantes ; 08 pièce truquée cachée ; 09 match en manches ; 10 beau temps / mauvais
  temps (chaîne à deux états) ; 11 coalitions et contraires ; Concours : transmission par relais.
- **Cartes** : 27 → 41. Ajouts : système complet, distribution, différence et croissance, \(P_B\), composées pour
  \(n\) événements, convention, contraires, indépendance mutuelle, contre-exemple, coalitions, fiabilité, somme de deux
  dés non uniforme, « au moins un succès », dépistage. Les cartes sur le dénombrement (0-3) et sur les lois et l'espérance
  (12-26) restent dans ce paquet, comme demandé ; leurs notations sont celles du site (E(X), V(X)).

## Notations
\(P(A \mid B) = P_B(A)\), \(\overline A\), \(\varnothing\), système complet \((B_1, \dots, B_n)\), \((X \in A)\) ; identiques à
`espproba` (2ᵉ année). Les notations 𝔼[X] et Var signalées par l'audit avaient déjà disparu du site ; restait C(n,p).

## Doutes
- Le programme énonce le lemme des coalitions pour des **variables** ; la consigne le place dans ce chapitre. Choix : version
  événements ici (§10), version variables dans `va` §5, avec renvois croisés. À arbitrer si l'on préfère un seul endroit.
- La carte 10 (« Equiv » au lieu de « Équivaut ») a été laissée telle quelle : elle est juste.
