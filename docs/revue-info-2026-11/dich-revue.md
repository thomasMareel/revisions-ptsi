# Revue — `dich` (chapitre `pydicho`, « Recherche séquentielle, dictionnaires et dichotomie », informatique, 1ʳᵉ année)

Nouveau chapitre. Fichiers : `dich-cours.src.html`, `dich-meth.src.html`, `dich-exos.src.html`, `dich-cartes.js` (24 cartes).

**Fabrication** : les panneaux sont produits par `tests/dichglou/build.py html dich` à partir des gabarits
`tests/dichglou/dich-{cours,meth,exos}.tpl.html` et du fichier de code `tests/dichglou/dich_code.py`. Chaque bloc de
code affiché y est un bloc `# >>> nom … # <<<` **exécuté** ; les lignes de démonstration « `expr   # valeur` » sont
évaluées et comparées au commentaire (82 valeurs vérifiées) ; les fonctions sont testées hors des blocs (tests au hasard
contre `list.index`, `max`, `sorted`, `bisect`, `math.isqrt`, `pow`, recherche exhaustive…). Pour modifier un panneau :
éditer le gabarit ou `dich_code.py`, puis relancer `python3 -I build.py html dich` (ne pas retoucher les `.src.html` à
la main, sinon la prochaine génération écrase la retouche). Figures : `tests/dichglou/dich_figs.py` (SVG calculés).

## Couverture du programme (avant → après)
Avant : rien de ce chapitre sur le site (audit 2026-11 §5 : « dichotomie, exponentiation rapide 🔶 (zéro d'une
fonction dans `pynum`) », dictionnaires seulement présentés dans `pytypes`). Après, thèmes S1 du programme 2021 :
- recherche séquentielle d'un élément, maximum, second maximum, manipulations élémentaires (§2, §3) ;
- dictionnaires en boîte noire : syntaxe, coût constant admis, comptage, valeur la plus fréquente, index de positions (§4) ;
- boucles imbriquées : recherche naïve d'un facteur (§5), deux valeurs les plus proches (§6), complexité quadratique,
  validation par une seconde méthode (tri + voisines) sur des tests aléatoires ;
- dichotomie dans un tableau trié (§7 : invariant, variant, borne ⌊log₂ n⌋ + 1 démontrée, erreurs d'indices) ;
- exponentiation rapide itérative (§8 : invariant r·aᵏ = xⁿ, nombre de multiplications, coût réel avec les grands entiers) ;
- coûts constant / linéaire / quadratique / logarithmique (§1, tableau d'ordres de grandeur), jeux de tests, mesure
  de l'accélération en comptant les comparaisons (§9) ;
- « Pour aller plus loin » : KMP / Boyer-Moore, module `bisect`, exponentiation rapide de matrices (Fibonacci).
Renvois (sans redite) : *Spécification, correction et complexité* (outils S2), *Algorithmes de tri* (tri à bulles,
`sorted`), *Récursivité* (versions récursives), *Méthodes numériques* (dichotomie sur une fonction),
*Représentation des nombres*, *Dictionnaires et programmation dynamique* (hachage, 2ᵉ année).

## Méthodes (9)
Recherche séquentielle avec sortie anticipée ; extremum / second extremum en un passage ; compter avec un dictionnaire ;
dénombrer des boucles imbriquées ; écrire une dichotomie sans erreur d'indice ; justifier terminaison et coût d'une
dichotomie ; exponentiation rapide à la main ; construire un jeu de tests ; choisir liste, liste triée ou dictionnaire.

## Exercices (10, dont 1 « Concours PT »)
01 ★ dernière occurrence (parcours à rebours) et nombre d'occurrences ; 02 ★ relevés de température (amplitude en un
passage, moyenne en deux passages, plus longue hausse avec invariant) ; 03 ★★ second maximum bogué à corriger + jeu de
tests + deuxième valeur distincte ; 04 ★★ anagrammes par dictionnaire (preuve, coût) ; 05 ★★ toutes les occurrences
d'un motif, occurrences disjointes (variant) ; 06 ★★ deux éléments de somme donnée (O(n²), dictionnaire O(n), deux
indices sur liste triée avec invariant) ; 07 ★★ première occurrence et comptage dans une liste triée (intervalle
semi-ouvert) ; 08 ★★★ racine carrée entière par dichotomie (milieu arrondi au-dessus, échec de `int(n ** 0.5)` pour
10¹⁶ − 1) ; 09 ★★ 7²⁰²⁶ mod 1000 par exponentiation rapide modulaire (649, 19 multiplications) ; **Concours PT** :
surveillance vibratoire d'un pont (parcours séquentiels, épisodes d'alerte, statistiques horaires par dictionnaire,
requêtes par dichotomie, précondition et jeu de tests).

## Choix
- Code limité à l'annexe Python du programme : pas de `max`, `min`, `abs`, `sum`, `enumerate`, `range` à trois
  arguments ni de `.get` ; `sorted` et `random.randint` sont documentés là où ils servent ; `ecart(a, b)` remplace `abs`.
- Échec signalé par −1 (convention de `str.find`), avec une mise en garde : `t[-1]` est accepté par Python.
- « Second maximum » défini répétitions comprises (le cas « valeurs distinctes » est l'objet de l'exercice 3).
- Durées du tableau du §1 estimées à 10⁸ opérations élémentaires par seconde (mesure faite : ≈ 24 ns par tour d'une
  boucle avec une comparaison).

## Contrôles
- `verif_src.py` sur les trois panneaux : aucune ERREUR ; une seule « attention » sur le cours : « pas de bloc
  « AU PROGRAMME · PT » », car l'outil cherche la chaîne exacte `AU PROGRAMME · PT` alors que les consignes
  d'informatique demandent « AU PROGRAMME · INFORMATIQUE » (bloc présent). À ignorer, ou adapter l'outil.
- `apercu_src.py` (copie `INFO/site/index.html`) à 390 et 1440 px pour les trois panneaux : `merr`, `brut`, `larges`
  vides, aucune erreur JS ; les trois figures tiennent dans la colonne à 390 px (ni `.lisible` ni `.defile`).
- Cartes : `node -e … dichCards.length` → 24, questions toutes distinctes, aucun HTML.

## Doutes
- Le cours est long (≈ 38 000 signes de texte, 68 000 caractères de HTML à cause de la coloration du code) : c'est
  voulu (neuf sections exigées par la répartition), mais on pourrait alléger §9 si l'utilisateur le juge redondant
  avec le futur chapitre *Spécification, correction et complexité*.
- Les lignes de code les plus longues (≈ 60 signes) défilent au téléphone dans leur bloc ; pas de débordement de page.
- Les cartes marquent le code entre accents graves, comme demandé : leur rendu dépend de l'intégration.
