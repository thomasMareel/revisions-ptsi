# Chapitre `sql` (prefix `sql`) — « Bases de données et SQL » : compte rendu (2026-11-19)

Nouveau chapitre de 2ᵉ année (programme d'informatique commune 2021, partie 3.1, semestre 3).

## Fichiers produits (dans `INFO/`)
- `sql-cours.src.html` (≈ 94 000 car.) : bloc « AU PROGRAMME · INFORMATIQUE » + 10 sections §1 à §10 + « POUR ALLER PLUS LOIN · HORS PROGRAMME » ; 10 exemples traités, 6 figures SVG, 40 blocs de code SQL.
- `sql-meth.src.html` : 9 méthodes (étapes, exemple éclair exécuté, pièges).
- `sql-exos.src.html` : 9 exercices (★ à ★★★) + 1 exercice « Concours PT » en quatre parties (15 questions).
- `sql-cartes.js` : 25 cartes (`const sqlCards`), code entre accents graves, formules en `\\( … \\)`, une carte `cat:'form'`.
- Sources et contrôles : `INFO/tests/sql/` (voir « Fabrication »).

**Les trois `.src.html` sont générés** : on édite les gabarits `INFO/tests/sql/{cours,meth,exos}.tpl.html`, puis
`python3 INFO/tests/sql/build.py`. Chaque requête SQL des gabarits est exécutée (sqlite3) ; le résultat affiché sous une
requête est celui du logiciel, recopié par le script ; `build.log` donne toutes les requêtes et toutes leurs lignes.

## Couverture du programme (3.1) : avant → après
Avant : rien (audit 2026-11, point 4 : « S3 : bases de données, SQL ❌ »). Après : tout 3.1.

| Notion du programme | Où |
|---|---|
| Vocabulaire : table/relation, attribut/colonne, domaine, schéma, enregistrement/ligne, types | §1 (figure « anatomie »), EXO 01 |
| Clé primaire (y compris à plusieurs attributs) | §2, M1, EXO 01, Concours Q1 |
| Entités, associations 1-1, 1-∗, ∗-∗, séparation d'une ∗-∗ en deux 1-∗, clé étrangère, diagrammes informels | §3 (deux figures), M1-M2, EXO 03, Concours Q2-Q3 |
| SELECT … WHERE, projection, AS, opérateurs + - * /, = <> < <= > >=, AND OR NOT | §4, M3, EXO 01-02 |
| DISTINCT, LIMIT, OFFSET, ORDER BY | §5, EXO 02 |
| UNION, INTERSECT, EXCEPT, produit cartésien | §6, M8, EXO 05, Concours Q7, Q14 |
| JOIN … ON (équi-jointures), autojointure | §7 (figure), M4, EXO 04, Concours Q8, Q11 |
| MIN, MAX, SUM, AVG, COUNT, GROUP BY | §8 (figure), M5, EXO 06, Concours Q8-Q12 |
| HAVING, différence WHERE / HAVING | §9 (figure de l'ordre d'évaluation, tableau comparatif, trois requêtes voisines), M6, EXO 07 |
| Requêtes imbriquées | §10, M7, EXO 08-09, Concours Q13-Q15 |
| Hors programme (NULL, CREATE/DROP/INSERT, transactions, index, jointures externes, SQL depuis Python) | encadré du bloc « Au programme » et section finale, sans exigence |

## Choix
- **Base fil rouge inventée** : service de vélos en libre-service, 5 tables reliées (Station 6 lignes, Abonne 7, Velo 6,
  Trajet 16, Favori 12). Données cohérentes et contrôlées par `bases.py` (un vélo repart de la station où il a été rendu,
  distances symétriques, vitesses plausibles). Pensée pour les cas utiles : abonnée sans trajet (Chloé : EXCEPT, groupes
  absents, jointure externe hors programme), vélo jamais utilisé (16), trajet en boucle (autojointure), aller-retour dans
  la journée, ex æquo de durées (LIMIT), clé à deux attributs (Favori), association ∗-∗ cachée dans Trajet.
- **Clés étrangères de Trajet nommées `abonne`, `velo`, `depart`, `arrivee`** (et non `id_abonne`…) : on voit qu'une
  clé étrangère n'a pas à porter le nom de la clé référencée, et la table Trajet tient dans la colonne de lecture à
  l'ordinateur (vérifié à 800, 1024, 1200 et 1440 px ; au téléphone, elle défile comme tout tableau large).
- **Bases propres aux exercices** (pour le transfert) : relevés météo (EXO 01), orchestre (EXO 03, jeu d'essai non montré,
  requêtes exécutées quand même), centrale photovoltaïque (EXO 06), parc éolien (Concours, jeu d'essai complet dans un
  bloc dépliable de l'énoncé pour que les résultats du corrigé soient vérifiables). Données inventées ; énergies entières
  (stockées en flottants) pour éviter toute égalité de flottants douteuse.
- **SQL du programme seulement** : pas de NULL, pas de CREATE/DROP dans ce qui est exigé, équi-jointures (les conditions
  non égalitaires `<`, `<>` sont toujours dans WHERE, ce que le cours explique), agrégats SQL99, pas de requête corrélée,
  alias systématique des tables dérivées (`AS c`, exigé par la norme), colonnes affichées d'une requête groupée toujours
  regroupées ou agrégées.
- **Dates** en chaînes 'AAAA-MM-JJ' (ordre alphabétique = ordre chronologique), comme le suggère le programme.
- **Division** : le programme « passe outre » ; le cours signale que 7 / 2 vaut 3 dans certains logiciels et ne divise
  que par des flottants (distance, energie).
- **Collations** : évitées. Aucun tri n'est montré sur des chaînes où la casse ou les accents changeraient l'ordre
  (sqlite classe 'VAE' avant 'classique') : le tri de la grille formule × type porte sur la formule seule.
- **Rendu** : code SQL en `<pre class="codeblock">` (mots-clés `<span class="kw">`, chaînes `str`, commentaires `cmt`) ;
  tableaux de tables et de résultats dans `<figure><div><table style="width:auto;margin-inline:auto;white-space:nowrap">`
  + `<figcaption>` (« Table Trajet : 16 enregistrements. », « Résultat : 3 lignes. ») : aucune classe nouvelle ; clés
  primaires soulignées par `<u>` dans les en-têtes. Flottants affichés arrondis au centième (dit au §1).
- **Figures SVG** (`tests/sql/figs.py`, classes du site seulement, contrôlées en clair et en sombre, 390 et 1440 px) :
  anatomie d'une table, diagramme entité-association de la base, séparation d'une ∗-∗, principe de la jointure,
  regroupement GROUP BY, ordre logique d'évaluation (WHERE avant les groupes, HAVING après).

## Contrôles faits (un par un)
- `build.py` : 130 requêtes exécutées (cours 49, méthodes 13, exercices 68), dont 4 requêtes fausses dont l'échec est
  vérifié (agrégat dans WHERE, `MAX(COUNT(*))`, colonne ambiguë) ; 8 contrôles d'équivalence (ex. NOT IN ≡ EXCEPT,
  JOIN ≡ produit + WHERE, les deux requêtes de l'EXO 07 Q6, les deux solutions « toutes » de l'EXO 09).
- `verif_src.py` sur les trois fichiers : aucune ERREUR. Une seule « attention » sur le cours : « pas de bloc AU
  PROGRAMME · PT » — l'outil cherche la chaîne « AU PROGRAMME · PT » alors que CONSIGNES-INFO impose « AU PROGRAMME ·
  INFORMATIQUE » (même avertissement sur `dich` et `img`) ; faux positif.
- `apercu_src.py` (copie `INFO/site/index.html`) à 390 et 1440 px, cours, méthodes, exercices : `merr`, `brut`,
  `larges` vides, aucune erreur JS. Captures des figures regardées (clair/sombre) ; `--captures` pleine page impossible
  (page de 50 000 px : Chromium plante), remplacé par des captures d'éléments (`tests/sql/figcap.js`).
- Cartes : `node -e … sqlCards.length` → 25 ; `tests/sql/cartes_verif.js` (pas de HTML, accents graves et délimiteurs
  appariés, questions distinctes) ; `tests/sql/cartes_sql.py` exécute les requêtes complètes citées par les cartes.

## Doutes, points à trancher par l'intégrateur
- `IN` / `NOT IN` ne figurent pas dans la liste du programme : présentés au §10 comme usuels mais non exigibles, avec
  l'équivalent sans `IN` (EXCEPT, jointure) à chaque fois.
- Taille : le cours dépasse la fourchette de 25 000-45 000 car. (tableaux, SVG et coloration du code) ; le texte seul
  est dans la fourchette. Les autres chapitres d'informatique de ce chantier sont du même ordre (69 000, 108 000).
- Le chapitre `sql` est placé dans le groupe « Programmation » par `chapitres.py` ; un sous-groupe « Bases de données »
  serait peut-être plus parlant dans la navigation (décision d'intégration).
- Cartes d'informatique : le marquage en accents graves suppose le nouveau rendu « texte tel quel » annoncé par les
  consignes ; avec le rendu actuel (flashPretty), il faudrait vérifier l'affichage des requêtes.
