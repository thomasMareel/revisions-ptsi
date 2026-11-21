# pyimages (prefix `img`) — « Images : matrices de pixels » (nouveau chapitre, 1ʳᵉ année) — 2026-11-19

## Fichiers produits (dans INFO/)
- `img-cours.src.html` (≈ 108 000 car., dont ≈ 62 000 de SVG) : bloc « AU PROGRAMME · INFORMATIQUE » + 8 sections §1 à §8 + « POUR ALLER PLUS LOIN · IMAGES ET MODULES » ; 8 exemples traités, 9 figures SVG calculées, 25 blocs de code.
- `img-meth.src.html` : 8 méthodes (repérer et parcourir ; créer sans alias ; transformation géométrique par antécédent ; réduire, agrandir ; convolution à la main ; reconnaître un noyau ; coût ; images RVB), 4 pièges.
- `img-exos.src.html` : 9 exercices (★ à ★★★) + 1 « Concours PT » en 4 parties (10 questions).
- `img-cartes.js` : 25 cartes (`const imgCards`), dont 12 `cat:'form'` ; code entre accents graves, formules en `\\( … \\)`, aucun HTML.

## Contenu du cours
1. Image = tableau de pixels : indices (i ligne vers le bas, j colonne), niveaux de gris 0–255, binaire, RVB ; place en mémoire ; exemple Full HD et stockage « à plat » (k = i·l + j).
2. Listes de listes : `[[v] * l for i in range(h)]`, piège `[[0] * l] * h` (figure des références), parcours O(h·l), copie superficielle / profonde ; exemple « premier pixel noir ».
3. Pixel par pixel : négatif, seuillage, écrêtage (`borner`), luminosité, passage RVB → gris (0,299 / 0,587 / 0,114), histogramme ; en place ou non.
4. Symétries, transposition, quarts de tour (tableau des 6 formules), méthode de l'antécédent ; rotation d'angle quelconque (antécédent par la rotation d'angle −θ, plus proche voisin) et figure des trous de la méthode directe.
5. Réduction (sous-échantillonnage, moyenne des blocs, exemple du damier), agrandissement, redimensionnement au plus proche voisin, coûts.
6. Convolution : noyau, formule, image produite (h − p + 1) × (l − p + 1), conventions de bord, jamais en place, coût O(h·l·p²), convolution / corrélation (bloc dépliable).
7. Flou moyenneur et gaussien, somme des coefficients égale à 1, effet sur un bord et un pixel isolé, accentuation.
8. Contours : différences, Sobel, norme du gradient, seuil, piège de l'écrêtage de g_x, exemple du bord vertical, laplacien.
Hors programme regroupé en fin : numpy (`img[i, j]`, `shape`, `uint8` modulo 256), interpolation bilinéaire, filtre médian, JPEG.

## Couverture du programme (avant → après)
Avant : rien (chapitre absent du site). Après : tout le thème « Matrices de pixels et images » du 1ᵉʳ semestre (rotation, réduction, agrandissement, convolution : flou, contours ; tableaux à deux dimensions) + copie superficielle de l'annexe + coûts dans le pire cas.

## Exercices
01 lire et compter (★) · 02 négatif en place, alias `res = img` et `img[:]` (★) · 03 piège `[[0]*3]*3`, `copy`, `append` (★★) · 04 demi-tour, quart de tour horaire, ordre des transformations, rotation = miroir ∘ transposée (★★) · 05 damier, sous-échantillonnage vs moyenne, agrandissement, tailles réelles (★★) · 06 étirement de contraste (★★) · 07 flou à bords recopiés, erreur de la version en place chiffrée (66 au lieu de 70) (★★) · 08 contours par différences simples, |gx| + |gy|, pixel isolé (★★★) · 09 recadrer (tranches), incruster, encadrer (★★) · Concours PT « Contrôle visuel de pièces découpées » : binarisation, aire en mm², centre, translation, recentrage, écart, orientation par quarts de tour, conformité, cadence (coût O(n²), réduction de l'image).

## Vérifications
- Tout le code est exécuté par `tests/imgfich/construire.py img` (le site est construit depuis les gabarits `tests/imgfich/gab/img-*.html`, le code des fonctions vient de `tests/imgfich/img_lib.py`) : 67 blocs, 0 erreur ; sorties affichées en commentaire comparées aux sorties réelles ; tests `test_img.py` (43 vérifications : involutions, 4 quarts de tour, rotation(π/2) = quart de tour, red ∘ agr = id, convolutions d'images uniformes…), rejoués sur le code du cours (`img_cours_tests.py`) et tests des corrigés (`img_exos_tests.py`, dont une pièce défectueuse refusée par `conforme`).
- Figures produites par `tests/imgfich/img_figs.py` à partir des fonctions testées (valeurs des cases calculées), aux classes `.px-*` ; captures regardées à 390 px en clair et en sombre (`tests/imgfich/caps/px390-planche.png`, `px390d-planche.png`).
- `verif_src.py` : aucune ERREUR ; une seule « attention » sur le cours, « pas de bloc AU PROGRAMME · PT » : l'outil cherche cette chaîne, alors que CONSIGNES-INFO impose « AU PROGRAMME · INFORMATIQUE » (même situation pour les autres chapitres d'informatique).
- `apercu_src.py` à 390 et 1440 px sur les trois onglets : `merr`, `brut`, `larges` vides, aucune erreur JS.
- Cartes : `node -e …` → 25 ; aucune question en double, accents graves et délimiteurs TeX équilibrés.

## Choix
- Listes de listes seulement (annexe) ; aucun module exigé. `math` (cos, sin, sqrt) documenté dans le texte ; `abs` et `round` documentés dans les énoncés qui s'en servent ; pas de comparaisons enchaînées ni d'indices négatifs.
- Convention de convolution : image produite plus petite (les autres conventions sont citées) ; l'exercice 07 utilise l'autre convention (bords recopiés) pour montrer la différence.
- Arrondi par `int(x + 0.5)` après test de signe (expliqué au §4).

## Doutes
- (Réglé le 2026-11-19 à la demande du coordinateur.) Les grilles de pixels utilisent les classes `.px-fond` (fond de chaque image, toujours présent), `.px` (case, `fill-opacity` = 1 − v/255), `text.px-t` (valeur sur une case claire) et `text.px-tc` (case foncée, v < 128) ; `fl-ink` et `lab-*` ne servent plus qu'aux éléments autour des images (axes, flèches, légendes, indices, noyau, cases de liste). 0 reste noir et 255 blanc dans les deux thèmes, ce qui a été vérifié sur les captures en clair et en sombre.
- Le cours est long (≈ 46 000 car. hors SVG) : il couvre tout le thème avec code complet ; on peut alléger le §4 (rotation d'angle quelconque) si besoin.
- Les blocs de code ont parfois des lignes de 60 à 80 caractères (commentaires) : ils défilent au téléphone, comme ailleurs sur le site.
