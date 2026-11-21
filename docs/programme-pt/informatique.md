# Programme officiel d'informatique commune (2021, MP, PC, PSI, PT) ↔ chapitres du site

Inventaire et chantier du 2026-11-19 au 2026-11-21 (point 5 de `docs/audit-2026-11.md`).

- **Programme** : informatique commune des filières MP, PC, PSI, PT (2021), trois semestres (S1 et S2 en
  PTSI, S3 en PT) et une **annexe « Langage Python »** qui fixe limitativement ce qui est exigible ; tout ce qui
  en sort (`deque`, `float('inf')`, `sorted`, `math.sqrt`, matplotlib…) est documenté là où il sert.
- **Avant** (audit du 2026-11-14) : 8 chapitres minces (≈ 2 000 signes de cours chacun) couvrant à peu près
  la moitié du programme ; rien sur les graphes, les bases de données, les dictionnaires et la programmation
  dynamique, les algorithmes gloutons, les images, ni sur l'IA et les jeux ; cartes mises en forme comme des
  formules (`type(x)` lu comme une fonction mathématique).
- **Après** : 17 chapitres (14 de 1ʳᵉ année, 3 de 2ᵉ année) en cinq parties, chacun au format des cours
  réécrits : bloc « AU PROGRAMME · INFORMATIQUE » (notions du programme, semestre, renvoi au §), 7 à 11
  sections avec exemples déroulés, code commenté **exécuté et testé** (le code affiché est celui des tests),
  complexités justifiées, erreurs classiques, figures SVG calculées, hors-programme en fin de cours ; 8 à 9
  méthodes ; 9 à 10 exercices dont un « Concours PT » ; 22 à 29 cartes (code entre accents graves, rendu tel
  quel par `flashInfoHTML`). Comptes rendus par chapitre : `docs/revue-info-2026-11/<prefix>-revue.md`.

## Répartition des notions

| Partie (`CHAP_GROUPS`) | Chapitre (prefix) | Année | Programme | Contenu |
|---|---|---|---|---|
| Programmation | `pybases` (pyb) | 1 | S1, annexe | variables, types de base, opérateurs, comparaisons, booléens paresseux, `print`, conversions |
| | `pyctrl` (pyc) | 1 | S1 | `if/elif/else`, `for`, `while`, `break`/`return` dans une boucle, accumulateurs |
| | `pyfonc` (fonc) | 1 | S1, S2 2.1 | fonctions, appel par valeur, portée, pile d'appels, effets de bord |
| | `pytypes` (typc) | 1 | S1, annexe | chaînes, tuples, listes (copies, alias), dictionnaires en boîte noire |
| Algorithmique | `pyanalyse` (anal) | 1 | S2 2.1 | spécification, `assert`, invariant, variant, terminaison, correction, tests, complexité (chapitre de référence) |
| | `pydicho` (dich) | 1 | S1 | recherche séquentielle, maximum, comptage par dictionnaire, boucles imbriquées, dichotomie, exponentiation rapide |
| | `pyrec` (recu) | 1 | S2 2.1 | récursivité, pile d'appels, sous-listes, permutations, fractales |
| | `pytri` (tri) | 1 | S1, S2 2.1 | insertion, sélection, bulles, partition-fusion, tri rapide, comptage |
| | `pyglouton` (glou) | 1 | S1 | gloutons : monnaie, salles, activités, preuves, contre-exemples |
| | `progdyn` (pdyn) | 2 | S3 3.2 | hachage et limites des clés, programmation dynamique (5 exemples du programme) |
| Nombres et calcul numérique | `pyrepr` (repn) | 1 | S2 2.2 | entiers (taille fixe, complément à deux), flottants, précision |
| | `pynum` (numr) | 1 | S1, capacités numériques | méthodes numériques (renvois aux chapitres de physique, de maths et de SI) |
| Données : fichiers, images, bases | `pyfichiers` (fich) | 1 | S1 | modules, fichiers texte, statistiques, tracés |
| | `pyimages` (img) | 1 | S1 | matrices de pixels, transformations, convolution, contours |
| | `sql` (sql) | 2 | S3 3.1 | modèle relationnel, entités-associations, toutes les requêtes du programme |
| Graphes et intelligence artificielle | `graphes` (gra) | 1 | S2 2.3 | vocabulaire, représentations, piles et files, parcours, connexité, Dijkstra, A* |
| | `iajeux` (iaj) | 2 | S3 3.3 | k plus proches voisins, k-moyennes, jeux d'accessibilité, attracteurs, minimax |

## Règles retenues

- **Images en niveaux de gris** : classes `.px-fond`, `.px`, `.px-t`, `.px-tc` (région CONTENU) : une image est
  une donnée, 0 reste noir et 255 blanc dans les deux thèmes (jetons échangés en sombre, aucune couleur en dur).
- **Cartes existantes** : retouchées sur une seule face (question **ou** réponse), ajouts en fin de paquet ;
  migration de l'état simulée avec le vrai `flashLoadState` avant intégration : aucune progression perdue.
- Le chapitre de SI `ia` traite aussi les k plus proches voisins : `iajeux` y renvoie, avec la même convention
  de matrice de confusion (réel en ligne, prédit en colonne).
