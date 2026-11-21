# Revue du chapitre `addfab` (prefix `fad`) — lot 5, point 4 de l'audit (2026-11-21)

Fichiers : `fad-cours.src.html` (construit par `fad_construire.py` depuis `fad-cours.tpl.html` et `fad_figs.json`),
`fad-meth.src.html`, `fad-exos.src.html` (assemblé par `fad_assembler_exos.py`), `fad-cartes-corr.json` (vide : aucune
carte fausse), `fad-cartes-ajout.js`. Scripts : `fad_figs.py` (7 figures calculées, aides de `moul_svg.py`),
`fad_calculs.py`, `fad_calculs_meth_exos.py`, `fad_cartes_rendu.js`. Anciens panneaux : `fad_orig_{cours,meth,exos}.html`.

## Renommage proposé (à décider)

Le frittage conventionnel, hors de tout programme, passe en « Pour aller plus loin » : je propose **« Fabrication
additive »** (ou « Fabrication additive : procédés et règles de conception » ; mobLabel « Fabrication additive » au lieu
de « Frittage & impression 3D »). Les renvois du cours `moul` disent déjà « Fabrication additive ».

## Programme (si.txt, G2 ; G1)

- S2 : procédés additifs pour une **pièce plastique** et une **pièce composite**, domaines d'application, **règles de
  conception**. S3 : procédés additifs pour une **pièce métallique** (§5, encadré « 2ᵉ année vue en avance ») et critères de
  choix des procédés (§11). G1 (S4) : prototype. Analyse qualitative : les calculs sont des ordres de grandeur.

| Capacité | Avant | Après |
|---|---|---|
| Principe, chaîne numérique (STL, tranchage) | une phrase | §1 (figure facettes et couches, flèche \(\delta\)) ; M1 ; EXO 02 |
| Familles de procédés | 3 procédés cités | §2 (7 familles, tableau, figure) ; §3 dépôt de fil (débit \(Q = whv\), masse, durée, coût) ; §4 résine et poudre polymère ; M2, M3 ; EXO 03, 04 |
| Pièce composite par procédé additif | absente | §6 (fibres courtes, fibres continues, loi des mélanges) ; M9 ; EXO 09 |
| Règles de conception | **absentes** (audit) | §7 anisotropie et orientation ; §8 porte-à-faux, ponts, supports (critère \(\tan\alpha \geq 2h/w\), figure calculée) ; §9 épaisseurs, trous, jeux, précision ; §10 effet d'escalier (\(c = h\cos\alpha\), figure) ; M4-M7 ; EXO 05-07 ; concours B |
| Pièce métallique (S3) | une ligne (SLM) | §5 signalé « 2ᵉ année vue en avance » (L-PBF, DED, projection de liant, post-traitements, exemple chiffré) |
| Domaines, choix, coût | §3 générique recoupant `ppm` §7 | §11 recentré sur l'additif (domaines, limites, \(C_u\), \(N^*\), figure, environnement) avec renvois à `ppm` §7 et `moul` §12 ; M10 ; EXO 08 ; concours C |
| Frittage conventionnel (hors programme) | §1, en tête du chapitre | « Pour aller plus loin » en fin de chapitre (figure refaite, porosité chiffrée) |

## Erreurs et défauts corrigés

1. **Ordre du chapitre** : le cours commençait par le frittage conventionnel, hors programme des deux années (signalé, mais
   en §1) ; il est passé en fin de chapitre, comme le demande le format.
2. **Recoupement avec `ppm` §7** (ancien §3 « Choisir un procédé d'obtention ») : remplacé par une section propre à
   l'additif (§11) qui renvoie à `ppm` §7 et à `moul` §12 pour la comparaison générale.
3. **Aucune règle de conception** (manque n° 6 de l'audit) : §7 à §10.
4. **Figures** : mêmes défauts d'opacité que dans `moul` (contours en `fl-soft sk-ink` invisibles) ; refaites.
5. Abréviations et anglicismes des anciens exercices (« FA », « near-net-shape », « SLM ») explicités ; ancien EXO 01
   « SOUS » en capitales mis en gras.
6. Aucune carte fausse (`fad-cartes-corr.json` vide) ; les six cartes de frittage gardent leur préfixe « Hors programme
   (pour aller plus loin) : », exact puisque le frittage n'est au programme d'aucune année.

## Cours : 11 sections + bloc programme + « Pour aller plus loin »

§1 chaîne numérique · §2 sept familles · §3 dépôt de fil fondu · §4 photopolymérisation et frittage laser de poudre
polymère · §5 métal (2ᵉ année vue en avance) · §6 composites · §7 anisotropie · §8 porte-à-faux · §9 épaisseurs, trous, jeux
· §10 effet d'escalier et finition · §11 additif, moulé ou usiné · frittage conventionnel. 12 exemples chiffrés, 7 figures
calculées, 86 400 caractères.

## Méthodes (10, au lieu de 3)

1 préparer une impression · 2 choisir une famille · 3 masse, durée, coût · 4 orientation · 5 surplombs et supports ·
6 parois, trous, jeux · 7 effet d'escalier · 8 anisotropie dans un dimensionnement · 9 pièce composite imprimée ·
10 additif, moulage ou usinage. L'ancienne méthode « frittage » est couverte par la section « Pour aller plus loin » et
l'EXO 10 ; l'ancienne méthode 3 (« choisir parmi toutes les familles ») par la méthode 10 et `ppm`.

## Exercices (12)

EXO 01 ancien « additif ou soustractif » (+ Q4) · 02 facettes et couches · 03 quel procédé additif · 04 masse, durée et
coût d'un boîtier · 05 surplombs, ponts, trou horizontal · 06 orientation d'un crochet · 07 effet d'escalier · 08 imprimer
puis injecter · 09 bras renforcé de fibres continues · 10 anciens EXO 01 et 03 réunis (frittage et palier autolubrifiant,
hors programme, + Q5 chiffrée) · 11 ancien concours (synthèse de choix, 2ᵉ année vue en avance) · **Concours PT**
« équerre de caméra imprimée » (procédé et orientation, règles de conception, coût et délai). Corrigés vérifiés
(`fad_calculs_meth_exos.py`).

## Cartes (22 → 36)

14 ajoutées : chaîne numérique, flèche \(\delta\), débit \(Q = whv\), poudre sans supports, durée liée à la hauteur,
direction faible, règle des 45°, éviter les supports, effet d'escalier, ordres de grandeur du dépôt de fil, métal (2ᵉ année),
composites imprimés, domaines, coût et seuil. Rendu contrôlé (`fad_cartes_rendu.js`, aucune erreur MathJax).

## Notations

\(h\) épaisseur de couche, \(w\) largeur de cordon, \(v\) vitesse de dépôt, \(Q\) débit, \(\alpha\) inclinaison d'une
surface sur le plan des couches (90° = paroi verticale), \(\delta\) flèche de facettisation, \(c\) hauteur de marche ; coût
comme `moul` et `ppm` (\(C_u\), \(C_o\), \(C_v\), \(N^*\)) ; loi des mélanges comme `moul` §9.

## Doutes

- Valeurs de résistance du PLA (50 MPa dans le plan, 25 MPa à travers les couches) et anisotropie « souvent de moitié » :
  ordres de grandeur courants, très dépendants des réglages ; données comme « valeurs typiques » dans les énoncés.
- Le critère géométrique \(\tan\alpha \geq 2h/w\) est un modèle simple (présenté comme tel) qui retrouve la règle des 45°.
- Tableau du §9 (parois minimales, précisions, jeux) : ordres de grandeur, variables selon les machines.
