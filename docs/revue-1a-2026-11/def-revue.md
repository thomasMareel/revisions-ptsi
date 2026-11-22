# Revue du chapitre `deform` (prefix `def`) — lot 7, point 4 de l'audit (2026-11-22)

Fichiers : `def-cours.src.html` (construit par `def_construire.py` depuis `def-cours.tpl.html` et `def_figs.json`),
`def-meth.src.html`, `def-exos.src.html`, `def-cartes-corr.json` (vide : aucune carte fausse), `def-cartes-ajout.js`.
Scripts : `def_svg.py` (copie de `moul_svg.py`), `def_figs.py` (9 figures calculées), `def_calculs.py`,
`def_calculs_meth.py`, `def_calculs_exos.py` (tous les nombres du cours, des méthodes et des corrigés), `def_voir.py`
(aperçu des figures, clair et sombre, dans `def_voir/`), `def_cartes_rendu.js` (cartes passées dans `flashPretty` +
MathJax). Anciens panneaux : `def_orig_{cours,meth,exos}.html`.

## Programme (si.txt, G2)

« Évaluer la capacité d'un procédé à réaliser une pièce métallique » : mise en forme des bruts par **déformation
plastique**, moulage et **découpage** ; domaines d'application ; **règles de conception** ; critères de choix des procédés.
Tout est au semestre **S3** : le chapitre entier est une anticipation de la 2ᵉ année. Il est signalé par le bloc
« Au programme · PTSI » (qui le dit explicitement) et par un encadré **« Vu en avance (2ᵉ année) »** en tête. Le
commentaire du programme (« approche qualitative ») est rappelé : efforts, passes, retour élastique, flans = ordres de
grandeur non exigibles, relations fournies par un sujet.

| Capacité | Avant | Après |
|---|---|---|
| Phénomènes physiques : plasticité, écrouissage, retour élastique, volume conservé | 3 lignes, sans essai de traction | §1 (courbe de traction calculée, décharge et écrouissage), M3, M4, EXO 03, 04 |
| Rôle de la température (froid / chaud) | 2 lignes | §2 (\(T_r \approx 0{,}4\)–\(0{,}5\,T_f\), tableau, effort de refoulement 7× plus grand à froid), M2, EXO 01 |
| Forgeage, estampage, matriçage | un paragraphe | §3 (figure calculée avant/après, rôle du cordon de bavure, lopin, effort de presse), M5, EXO 05, 11 |
| Fibrage | 2 phrases | §4 (figure calculée usinée/refoulée, matière perdue 69 % contre 11 %), EXO 06 |
| Règles de conception des pièces forgées | **absentes** | §5 (plan de joint, dépouilles, congés, replis, voiles, surépaisseurs ; coût d'une dépouille), M5 |
| Laminage, filage, tréfilage | 3 lignes | §6 (figure du laminoir à l'échelle, \(\Delta e_{\max} \approx f^2R\), débit, rapport de filage, passes de tréfilage), EXO 03 |
| **Découpage** (cité par le programme) | une ligne | §7 (figure : outil, jeu, faciès ; \(F \approx p\,e\,R_g\) comme `ppm` ; imbrication), M6, EXO 07, concours C |
| Pliage | 2 lignes | §8 (figure, fibre neutre, rayon minimal, longueur développée, retour élastique calculé, effort en V), M7, M8, EXO 08, concours B |
| Emboutissage | un paragraphe + figure | §9 (figure calculée, défauts, \(D_0\), rapport \(\beta\), passes à l'échelle, effort maximal, serre-flan), M9, EXO 09, 10, concours A |
| Règles de conception des pièces en tôle | **absentes** | §10 (découpage, pliage, emboutissage, rigidifier par la forme : ×61 pour +18 % de matière) |
| Critères de choix, coût, environnement | absents | §11 (tableau, \(C_u\), \(N^*\) comme `moulage`/`ppm`, matière, énergie, fin de vie), M10, EXO 11, concours C |

## Erreurs et imprécisions corrigées

Aucune erreur de fond dans l'ancien chapitre (3 700 signes) ni dans ses 22 cartes ; il était surtout incomplet. Retouches :
1. **Anticipation S3 non signalée** (audit §1) : bloc programme et encadré « Vu en avance ».
2. Ancien EXO 03 Q2 : « bridé latéralement par sa largeur » remplacé par l'explication de l'emprise (écoulement vers la
   direction libre, frottement sur une emprise plus large que longue).
3. Ancien concours (godet Ø 50 × 30, devenu EXO 09) : ajout du contrôle du rapport d'emboutissage (\(\beta \approx 1{,}84\),
   une passe) ; C1 nuancé (une paroi d'un millimètre se moule mal en acier).
4. Ancien EXO 02 complété (Q4 rondelles, Q5 petite série de supports), EXO 01 (Q3 plomb), EXO 03 (Q3 vitesse, Q4 \(f^2R\)).

## Cours : 11 sections + bloc programme + « Pour aller plus loin »

§1 traction, écrouissage, volume · §2 froid/chaud · §3 forgeage, estampage · §4 fibrage · §5 règles des pièces forgées ·
§6 laminage, filage, tréfilage · §7 découpage · §8 pliage · §9 emboutissage · §10 règles de la tôlerie · §11 choix et coût ·
Pour aller plus loin (déformations vraies, limite du tréfilage 63 %, modèle du retour élastique, hydroformage, repoussage,
formage incrémental, superplasticité). 14 exemples chiffrés, 9 figures calculées (traction, estampage, fibrage, laminage,
découpage, pliage, retour élastique, emboutissage, passes), 99 000 caractères. Chaque section a son « Erreur classique ».

## Méthodes (10, au lieu de 2 et une liste de pièges)

1 identifier la famille · 2 froid ou chaud · 3 conservation du volume · 4 lire une courbe de traction · 5 dessiner un brut
estampé · 6 effort de découpage et règles · 7 flan d'une pièce pliée · 8 effort de pliage et retour élastique · 9 flan et
passes d'emboutissage · 10 comparer par le coût. Deux pièges (brut/pièce finie ; surface contre volume).

## Exercices (12)

EXO 01-03 anciens complétés · 04 essai de traction · 05 lopin et presse d'estampage · 06 crochet de levage (fibrage) ·
07 platine découpée (outil à suivre, règles, bavure) · 08 chape en U (flan, rayon, effort, surpliage) · 09 ancien concours
(godet) · 10 godet profond en quatre passes · 11 bielle : usiner ou estamper · **Concours PT** « corps de filtre à huile » :
A bol embouti en deux passes (flan Ø 182, \(\beta\) = 2,40), B patte pliée, C découpage, seuil 26 700 pattes, imbrication 86 %.

## Cartes (22 → 37)

Aucune corrigée. 15 ajoutées : \(T_r\), conservation du volume, retour élastique \(\sigma/E\) et écrouissage, cordon de
bavure, règles d'estampage, \(\Delta e_{\max} \approx f^2R\), filage/tréfilage, \(F \approx p\,e\,R_g\), jeu et faciès, rayon
minimal de pliage, longueur développée, compensation du retour élastique, \(D_0 = \sqrt{d^2 + 4dh}\), rapport
d'emboutissage, rigidifier par la forme. Rendu vérifié (`def_cartes_rendu.js`) : cinq réponses réécrites en `\( … \)`
pour éviter une conversion maladroite par `flashPretty` (« 3 mm. », « (10 à 30 % »).

## Notations

Celles de `rdm` et `ppm` : \(R_e\), \(R_m\), \(A\), \(E\), \(\sigma\), \(\varepsilon\) ; découpage \(F \approx p\,e\,R_g\)
(\(p\) : périmètre, comme `ppm` §7) ; coût \(C_u\), \(C_o\), \(C_v\), \(N^*\) (comme `moulage`, `ppm`) ; coefficient de
frottement \(f\) (comme `statique`). Nouvelles : contrainte d'écoulement \(\sigma_{\text{éc}}\) (et non \(\sigma_f\), que
`ppm` emploie pour la résistance de dimensionnement), \(T_r\), \(T_f\), \(K_p\), rapport d'emboutissage \(\beta = D_0/d\),
\(R_i\), \(k\), \(L_d\), \(V\) (ouverture du vé), \(K_s\) (retour élastique, hors programme).

## Doutes et propositions

- **Renommage proposé** : « Mise en forme par déformation et découpage » (le programme cite le découpage à part ; le §7 et
  les §10-§11 le traitent). mobLabel inchangé possible (« Déformation plastique »).
- Ordres de grandeur d'atelier (non issus du programme) : \(K_p\) = 5 à 8 (pièce simple avec bavure), \(F \approx 1{,}33\,R_m L e^2/V\),
  \(\beta_{\lim}\) 1,8-2,2 puis 1,2-1,3, jeu 5-10 %, dépouilles 3-7° / 5-10°, rayon de matrice 4-10 \(e\), distance trou-pli
  \(R_i + 2e\), bord minimal 4-6 \(e\) : valeurs usuelles des guides de conception, présentées comme indicatives.
- Rayon minimal : l'estimation \(R_i/e \ge (1/A - 1)/2\) est dite prudente ; la règle \(R_i \ge e\) pour l'acier doux donne
  une fibre extérieure à 33 %, un peu au-dessus de \(A\) = 30 % : le cours l'explique (la fibre d'un pli supporte plus que
  l'allongement de traction).
- La courbe de traction de la figure est calculée avec une loi d'écrouissage puissance ; la striction est une allure.
- Le cours `ppm` §7 reste la synthèse de 2ᵉ année ; il pourrait renvoyer aux §5 et §10 pour les règles de conception.
