# Revue : `denombrmt` « Dénombrement et combinatoire » (prefix `denom`), 1ʳᵉ année — 2026-11-21

Restructuration des probabilités de 1ʳᵉ année (audit `docs/audit-2026-11/maths-1a.md` §2 point 8, §3 « Doublons »,
§5 point 5) : ce chapitre porte désormais **le dénombrement seul**. Le vocabulaire des probabilités est dans `proba`,
les variables aléatoires dans `va` ; le §9 ne fait qu'appliquer le dénombrement à la probabilité uniforme, avec renvoi.

## Fichiers produits
- `denom-cours.src.html` (≈ 56 000 car., bloc « AU PROGRAMME · PTSI », 9 sections, 13 exemples traités, 6 figures
  calculées, « Pour aller plus loin »), `denom-cours.tpl.html` + `denom_figs.py` / `denom_figs.json` + `denom_construire.py`.
- `denom-meth.src.html` (10 méthodes, exemple éclair chiffré chacune, 3 pièges).
- `denom-exos.src.html` (11 exercices + 1 « Concours PT » en 3 parties).
- `denom-cartes-corr.json` (15 cartes retouchées, une seule face chacune), `denom-cartes-ajout.js` (15 cartes ajoutées en fin).
- Contrôles : `denom_calculs.py` (118 vérifications, toutes justes, dont des énumérations exhaustives), `denom_cartes.py`,
  `prb_cartes_rendu.py` (rendu MathJax des cartes des trois chapitres : 67 champs, 0 erreur), `prb_voir.py` (aperçu des
  figures), `prb_scinder.py`, `prb_longues.py`, `prb_mjlarge.js`, `prb_blocs.js`, `prb_deborde.js` (formules trop larges au téléphone).
- Anciens panneaux conservés : `denom_old-{cours,meth,exos}.html`.

## Erreurs et défauts corrigés
- **Hors-programme présenté comme exigible** : loi hypergéométrique (§4 et EXO 05 de l'ancien cours, cartes 12-14 sans
  mention) → « Pour aller plus loin » ; l'exercice devient un calcul par dénombrement (exigible), le nom de la loi signalé
  hors programme ; cartes 12-14 préfixées « Hors programme (pour aller plus loin) : ». Formule du crible : déjà signalée
  (carte 20), reprise en fin de cours.
- **Doublon avec `proba`** : le dénombrement de `proba` §1 est supprimé de `proba` ; tout est ici (cardinaux, listes,
  combinaisons, Pascal, binôme).
- **Manques du programme comblés** : cardinal d'une partie et cas d'égalité ; « injective ⟺ surjective ⟺ bijective » entre
  ensembles de même cardinal (avec démonstration) ; principe des tiroirs ; cardinal d'une différence et du complémentaire ;
  nombre d'applications \(|F|^{|E|}\) ; \(|\mathcal P(E)| = 2^n\) démontré ; injections ; convention \(\binom nk = 0\) ;
  **démonstrations combinatoires de Pascal et du binôme** (exigées), formule du capitaine.
- EXO 04 ancien « Inclusion-exclusion — problème des anniversaires » : titre faux (aucune inclusion-exclusion) ; estimation
  \(\ln P \approx -n^2/730\) remplacée par \(-n(n-1)/730\), qui donne exactement 23 (\(\sqrt{2\,025} = 45\)).
- EXO 06 ancien (Vandermonde) Q3 : « par symétrie et unimodalité » sans preuve → démonstration par le rapport
  \(\binom n{k+1}/\binom nk = (n-k)/(k+1)\).
- Ancien « Concours PT » (3 questions courtes) : ses questions sont reprises dans EXO 02 (délégués, trois filles) et EXO 08
  (SUCCES) ; nouveau sujet original en trois parties (chemins dans un quadrillage).
- Méthode 1 ancienne : tableau incluant les multiensembles \(\binom{n+k-1}{k}\) sans mention → hors programme, en fin de cours.
- Notation \(C(n,k)\) des cartes → \(\binom nk\) (notation du programme et du site).

## Couverture du programme (avant → après)
| Capacité (programme PTSI, « Dénombrement » + rappels du S1) | Avant | Après |
|---|---|---|
| Cardinal, \(|A|\), Card(A) ; partie, cas d'égalité | partiel (§1, sans cas d'égalité) | §1, carte |
| Applications entre ensembles de même cardinal (inj. ⟺ surj. ⟺ bij.) | absent | §1 (démo), méth. 10, EXO 04, carte |
| Union disjointe ou quelconque, complémentaire, différence, produit | partiel | §2, figure, méth. 2-4, cartes |
| Nombre d'applications ; nombre de parties | \(2^n\) cité | §3 (démos), EXO 03, cartes |
| p-listes d'éléments distincts, injections, permutations | oui (sans injections) | §4, arbre, EXO 03, cartes |
| p-combinaisons, \(\binom np\), convention | oui (sans convention) | §5, chemins, cartes |
| Démonstration combinatoire de Pascal et du binôme | absent | §6, §7 (démos), cartes |
| Factorielle, binôme dans ℝ (rappels S1) | oui | §4, §7 |
| Application aux probabilités uniformes | §4 | §9 (renvoi au chapitre `proba`) |
| Hors programme : crible, multiensembles, hypergéométrique | présentés comme cours | « Pour aller plus loin » |

## Contenu
- **Sections** : §1 ensembles finis et cardinal (tiroirs) ; §2 réunion, complémentaire, produit ; §3 applications, listes,
  parties ; §4 listes d'éléments distincts et permutations ; §5 coefficients binomiaux (chemins) ; §6 Pascal et triangle,
  formule du capitaine ; §7 binôme et sommes ; §8 raisonner pour dénombrer (tableau des modèles, anagrammes, poker,
  double comptage) ; §9 probabilité uniforme (tirage simultané / successif, anniversaires). Figures : Venn (multiples de 6
  et 10), arbre des 2-listes, chemin 5 × 3, triangle de Pascal, bâtons de \(\binom{10}{k}\), courbe des anniversaires.
- **Méthodes** : choisir le modèle ; principe multiplicatif ; cas disjoints ; complémentaire ; contrainte de composition ;
  corriger un sur-comptage ; double comptage ; binôme ; probabilité uniforme ; cardinaux et tiroirs.
- **Exercices** : 01 comptages directs (gardé + Q4) ; 02 coefficients binomiaux (gardé + délégués) ; 03 applications,
  injections, surjections ; 04 tiroirs ; 05 poker (gardé + full, double comptage) ; 06 anniversaires (corrigé) ; 07 lot de
  pièces (ancien « hypergéométrique », recentré) ; 08 anagrammes ; 09 sommes binomiales ; 10 Vandermonde (gardé, Q3
  démontrée) ; 11 mots sans « 11 » (Fibonacci, \(\binom{n-k+1}{k}\)) ; Concours : chemins (Pascal, crosse de hockey,
  \(\sum k^2\), chemin aléatoire, \(\sum \binom nk^2\)).
- **Cartes** : 15 corrigées (réponse seule, sauf cartes 7 et 8 : question seule, réponse inchangée, pour remplacer C(n,k)) ;
  15 ajoutées (cardinal d'une partie, même cardinal, tiroirs, différence, applications, parties, injections, convention,
  capitaine, chemins, SUCCES, preuve du binôme, parties paires, tableau des modèles, double comptage de « au moins un as »).
  Le paquet passe de 25 à 40 cartes. Les cartes sur l'espace équiprobable (11, 21) restent dans ce paquet, comme demandé.

## Notations
\(|A|\), \(\operatorname{Card}(A)\), \(\binom np\) (« p parmi n »), \(n!/(n-p)!\) écrit en toutes lettres (la notation
\(A_n^p\), hors programme, est seulement citée), \(\mathcal P(E)\), \(\mathbf 1_A\). Probabilité uniforme \(P(A) = |A|/|\Omega|\).

## Doutes
- Les cartes 0, 15, 23 gardent la notation \(A_n^k\) (correcte, mais absente du programme) : non retouchées, car justes.
- La question 3 garde « C(n,0) et C(n,n) » (une seule face retouchée : la réponse dit \(\binom n0 = \binom nn = 1\)).
- Quelques formules en bloc défilent encore au téléphone dans les encadrés étroits (comportement prévu par le site).
