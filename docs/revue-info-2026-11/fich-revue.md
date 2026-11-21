# pyfichiers (prefix `fich`) — « Modules, fichiers et statistiques » (nouveau chapitre, 1ʳᵉ année) — 2026-11-19

## Fichiers produits (dans INFO/)
- `fich-cours.src.html` (≈ 60 000 car.) : bloc « AU PROGRAMME · INFORMATIQUE » + 8 sections §1 à §8 + « POUR ALLER PLUS LOIN · RACCOURCIS ET MODULES » ; 7 exemples traités, 5 figures SVG calculées, 41 blocs de code, 2 tableaux de documentation (fichiers ; matplotlib.pyplot).
- `fich-meth.src.html` : 8 méthodes (importer ; lire un fichier de données ; écrire des résultats ; moyenne, variance, écart type ; médiane et quartiles ; effectifs d'un histogramme ; tracer avec la documentation ; tester une lecture de fichier), 2 pièges.
- `fich-exos.src.html` : 9 exercices (★ à ★★★) + 1 « Concours PT » en 3 parties (8 questions).
- `fich-cartes.js` : 23 cartes (`const fichCards`), dont 5 `cat:'form'` ; code entre accents graves, formules en `\\( … \\)`, aucun HTML.

## Contenu du cours
1. Modules : `import m`, `import m as a`, `from m import f, g`, `NameError` sans préfixe, conflits de noms, `math` et `random` (documentés), simulation de lancers, module personnel `outils.py`.
2. Lecture : définition d'un fichier texte, tableau de documentation de l'annexe (`open` r/w/a, `read`, `readline`, `readlines`, `write`, `close`, `split`), curseur de lecture (figure), boucle `while ligne != ''`.
3. Découpage et conversion : `split(sep)` / `split()`, `int`, `float` (tolèrent les blancs), `sans_retour` (sans `strip`, hors annexe), lecture d'un fichier commenté avec ligne vide, `lire_colonnes`, pièges des chaînes non converties et de la virgule décimale.
4. Écriture : `write` + `str` + `'\n'` + `close`, mode `'a'` (journal), `ecrire_colonnes`, test aller-retour.
5. Moyenne, variance, écart type (formules, code, figure de dispersion), König-Huygens et sa perte de précision (variance de [10⁸ + 1, 10⁸ + 2, 10⁸ + 3] calculée nulle), coût, remarque sur la division par n − 1 des incertitudes de type A.
6. Médiane et quartiles (convention de rang ⌈n/4⌉, `sorted` documenté), boîte à moustaches (figure), coût du tri, exemple « bilan d'un devoir » (lecture avec absents, statistiques, fichier de sortie, robustesse de la médiane).
7. Effectifs par classes en un parcours (O(n + k)), histogramme (figure) et histogramme texte, piège des bornes flottantes (0,3 rangé dans la classe 2).
8. Graphiques avec `matplotlib.pyplot` documenté (`plot`, `'o'`, `bar`, `hist`, légendes, `show`, `savefig`) : courbe de charge d'un condensateur lue dans un fichier (figure : mesures + modèle), histogramme à classes imposées, abscisses régulières sans cumul d'arrondis.
Hors programme regroupé en fin : `with`, `for ligne in f`, `strip`, modules `csv`, numpy, `statistics`, encodages.

## Couverture du programme (avant → après)
Avant : rien (aucun chapitre du site ne traitait modules, fichiers ni statistiques). Après : thème « Utilisation de modules, de bibliothèques » du 1ᵉʳ semestre (lecture d'un fichier de données simples, calculs statistiques, représentation graphique) et lignes « Importation de modules » et « Manipulation de fichiers texte » de l'annexe Python, documentation rappelée comme l'exige le programme.

## Exercices
01 cinq imports à interpréter + `distance` (★) · 02 curseur `readline`/`read`, `split()` vs `split('\n')` (★) · 03 lire un fichier de notes, meilleure note, moyenne (★) · 04 variance à deux passages / König-Huygens, démonstration, variance −128 sur des valeurs voisines de 10⁹, piège O(n²) (★★) · 05 médiane par tri par insertion d'une copie, quartiles, valeurs aberrantes (règle 1,5 × écart interquartile) (★★) · 06 somme de deux dés simulée, écart aux probabilités, fichier de résultats (★★) · 07 moyenne glissante O(n·p) puis O(n), lecture et écriture (★★) · 08 journal en mode `'a'`, dernière ligne, intérêt de `close` (★★) · 09 relevés météo avec `NA`, moyennes mensuelles par dictionnaire, rapport ordonné (★★★) · Concours PT « Exploiter un essai de traction » : lecture d'un fichier commenté, contrainte et déformation, R_m, module d'Young par moindres carrés (≈ 69 900 MPa), R_p0,2 (252 MPa), compte rendu écrit, tracé documenté, complexité.

## Vérifications
- Tout le code est exécuté par `tests/imgfich/construire.py fich` (gabarits `tests/imgfich/gab/fich-*.html`, fonctions de `tests/imgfich/fich_lib.py`) : 83 blocs, 0 erreur ; les blocs « erreur montrée au lecteur » (`NameError`, `ValueError`, `TypeError`) vérifient que l'erreur se produit bien ; les fichiers affichés dans le texte sont exactement ceux que lit le code (balise `FILE`) ; matplotlib exécuté en mode Agg.
- `test_fich.py` (34 vérifications, comparaison au module `statistics`), rejoué sur le code du cours (`fich_cours_tests.py`, avec les contenus exacts des fichiers écrits) ; tests des corrigés (`fich_exos_tests.py`, dont les 5 programmes de l'exercice 01 exécutés chacun dans un espace de noms neuf).
- `verif_src.py` : aucune ERREUR ; une seule « attention » sur le cours, « pas de bloc AU PROGRAMME · PT » (le surtitre imposé par CONSIGNES-INFO est « AU PROGRAMME · INFORMATIQUE »).
- `apercu_src.py` à 390 et 1440 px sur les trois onglets : `merr`, `brut`, `larges` vides, aucune erreur JS. Figures capturées et regardées à 390 px.
- Cartes : `node -e …` → 23 ; aucune question en double, accents graves et délimiteurs TeX équilibrés.

## Choix
- Seules les fonctions de l'annexe sont exigées ; tout le reste est documenté à l'endroit où il sert : `math`, `random` (`randint`, `random`), `sorted`, `abs`, `matplotlib.pyplot`. Pas de `strip` (hors annexe) : fonction `sans_retour` écrite avec les seuls indices positifs ; pas de `with`, pas d'exceptions.
- Variance « de population » (division par n), comme en mathématiques ; la division par n − 1 des incertitudes de physique est signalée.
- Quartiles : convention du lycée (plus petite valeur de rang ≥ n/4), annoncée comme une convention.

## Doutes
- Le comptage par dictionnaire n'est pas refait (renvoi au chapitre `pydicho`, d'après la répartition des notions).
- La sortie de l'exemple de simulation (§1, exercice 06) dépend du hasard : le texte donne un ordre de grandeur, jamais une valeur exacte.
- Données réelles approximatives dans l'exercice 02 (populations arrondies de Paris, Lille, Brest) ; toutes les autres données sont inventées.
