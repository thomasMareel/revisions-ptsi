# Revue du chapitre `cotation` (prefix `cota`) — « Cotation & tolérances », SI 1ʳᵉ année

Réécriture complète sur la spécification géométrique des produits (GPS) du programme 2021 (A5, semestre S2),
d'après l'audit `docs/audit-2026-11/si-1a.md` (§2 point 2, §5 point 3). Rédaction et exemples originaux ; tous les
nombres vérifiés en Python (`cota_calculs.py`, `cota_calculs_meth.py`, `cota_calculs_exos.py`).

## Fichiers produits (dans AN1)

| Fichier | Contenu |
|---|---|
| `cota-cours.src.html` | cours : bloc « AU PROGRAMME · PTSI », 12 sections §1–§12, « POUR ALLER PLUS LOIN », 16 figures calculées, 16 exemples traités (≈ 130 000 car., dont ≈ 75 000 de SVG) |
| `cota-meth.src.html` | 10 méthodes (étapes, exemple éclair chiffré) et 4 pièges |
| `cota-exos.src.html` | 11 exercices + 1 « Concours PT » en 5 parties, 4 figures de pièces inventées |
| `cota-cartes-corr.json` | 6 cartes corrigées (réponse seule, question inchangée) |
| `cota-cartes-ajout.js` | 15 cartes ajoutées, à la fin (24 → 39) |
| scripts | `cota_svg.py` (primitives : symboles GPS dessinés, cadres, références, cotes encadrées, hachures), `cota_figs.py` → `cota_figs.json`, `cota_construire.py` (gabarits `cota-cours.tpl.html`, `cota-exos.tpl.html` → `.src.html`), `cota_voir.py` (aperçu clair/sombre), `cota_deborde.js`, `cota_choix_rectitude.py`, calculs ci-dessus ; copies des anciens panneaux `cota_*_orig.html`, `cota_cartes_actuelles.json` |

Contrôles passés : `verif_src.py` sans erreur ni « attention » sur les trois fichiers ; `apercu_src.py` à 390 et 1440 px :
`merr`, `brut`, `larges` vides, aucune erreur JS, aucun débordement de page ; captures regardées (figures en clair et
en sombre via `cota_voir.py`) ; `corriger_cartes.py … --essai` (6 réponses corrigées) et `ajouter_cartes.py … --essai`
(24 → 39) sans erreur.

## Erreurs et défauts corrigés

1. **Programme** : l'ancien chapitre suivait l'ancien programme (ISO 286, chaîne de cotes, rugosité) et ne traitait
   aucun attendu GPS 2021 (principes, modèles, opérations, taille / zone / gabarit, enveloppe, références et liaisons,
   fiche GPS). Tout est désormais traité ; ISO 286, chaîne de cotes et maximum de matière sont en « Pour aller plus
   loin », la rugosité y est signalée comme vue en 2ᵉ année.
2. **Nature d'un ajustement** (cours §2 ancien, cartes 7 et 10) : inégalités strictes (« jeu mini > 0 », « jeu maxi
   < 0 ») qui laissaient sans nature un ajustement de jeu minimal nul (glissant juste, cas réel des bagues de
   roulement en logement H). Corrigé en \(J_{\min} \geq 0\) / \(J_{\max} \leq 0\) (cours §6, cartes 7 et 10).
3. **Carte 9** : « jeu mini négatif → il y a serrage » ; c'est seulement un serrage *possible* (incertain, ou serré si
   le jeu maxi est aussi négatif). Réponse corrigée.
4. **Carte 23** : « la bague tournante » sans dire « par rapport à la direction de la charge » (règle de la charge
   tournante, chapitre `conception` §6). Réponse précisée.
5. **Cartes 16 et 17** (Ra) : hors programme de PTSI non signalé ; réponse préfixée « Hors programme en PTSI (vu en
   2ᵉ année) : ».
6. **Figures** : libellés de 8,5 à 9 px (sous le minimum de 12 px du site) ; toutes redessinées.
7. **Exercice « Concours PT »** : sans aucune spécification GPS, partie B sur la chaîne de cotes (hors programme).
   Remplacé par un concours GPS complet ; son contenu juste (bague de roulement serrée, choix de la rectification)
   est repris dans l'EXO 03 (Q3 à Q5). Remarque : l'erreur citée par l'audit (alésage de bague « +0,010/0 ») était
   déjà corrigée dans la version en ligne (0/−0,010).
8. **Débordement au téléphone** : deux corrigés anciens (EXO 02 et chaîne de cotes) avaient des formules en ligne de
   380 à 420 px (page de 475 px à 390) ; reformulés.

## Couverture du programme (A5, S2) avant → après

| Capacité / connaissance | Avant | Après |
|---|---|---|
| Justifier le besoin fonctionnel d'une spécification | une phrase (§4, hors programme) | §1, §12 (démarche, passage de vis), méthodes 3 et 10, EXO 03, 09, 10, concours A, C2, D |
| Principes : indépendance, pièce rigide, élément, dualité, invocation, responsabilité | ✗ | §2 (arbre cintré, incertitude), §7, EXO 04, 06, 08, cartes |
| Modèles nominal, extrait, skin model | ✗ | §3, carte |
| Opérations : partition, collection, filtrage, extraction, construction, association | ✗ | §3 (rectitude minimax / moindres carrés), méthode 5, carte |
| Spécification = condition unilimite sur une caractéristique dimensionnelle | ✗ | §4, carte |
| Spécification par taille | cote tolérancée (§1) | §5 (élément de taille, tailles locales, maximum de matière, cote ± ambiguë), méthode 1, EXO 01 |
| Nature des ajustements (glissant, incertain, serré) | §2 (inégalités strictes) | §6 (corrigé, choix selon la fonction), méthodes 2 et 3, EXO 02, 03, 10, concours A |
| Spécification par gabarit : exigence de l'enveloppe | ✗ | §7 (gabarit, forme admise, arbre trilobé, garantie du montage), méthode 4, EXO 04, concours A3 |
| Spécification par zone : cadre, élément tolérancé, zone, références | liste des familles (§3) | §8 (anatomie du cadre, intégral / dérivé, symboles dessinés), méthode 6, EXO 05 |
| Forme et orientation | noms seulement | §9 (zones, hiérarchie, marbre, angle t/L), EXO 05, 06 |
| Position et battement | noms seulement | §10 (localisation, zone circulaire / carrée, coaxialité, symétrie, battement et excentration), méthode 8, EXO 07, 08, concours E |
| Lien liaison ↔ système de références | ✗ | §11 (association, simple / commune / système, degrés de liberté, tableau liaison → référence), méthode 7, EXO 09, concours B |
| Fiche GPS | ✗ | §12 (rubriques, exemple rempli), méthode 9, concours C1 |
| Ajustements normalisés (non exigibles), modificateurs autres que Ⓔ, chaîne de cotes | présentés en cours | « Pour aller plus loin » ; EXO 11 titré hors programme |

## Contenu

- **Cours** : §1 Spécifier une pièce · §2 Principes · §3 Modèles et opérations · §4 Ce qu'est une spécification ·
  §5 Taille · §6 Ajustements · §7 Exigence de l'enveloppe · §8 Cadre de tolérance · §9 Forme et orientation ·
  §10 Position et battement · §11 Références et liaisons · §12 Fiche GPS et écriture · Pour aller plus loin (ISO 286,
  Ⓜ, chaîne de cotes, états de surface). Figures : défauts d'une pièce, arbre cintré (indépendance), extraction et
  association (profil, minimax, moindres carrés), cote tolérancée, trois ajustements, forme admise avec Ⓔ, arbre
  trilobé, anatomie du cadre, flèche intégral / dérivé, 14 symboles dessinés, zone de forme / zone d'orientation,
  localisation (cylindre contre carré), battement (lecture sur un tour), références d'un couvercle et d'un moyeu,
  palier de la fiche GPS, chaîne de cotes.
- **Méthodes** (10) : exploiter une cote ; nature d'un ajustement ; choisir la nature selon la fonction ; interpréter
  Ⓔ ; décrire par modèles et opérations ; lire un cadre ; établir un système de références ; juger une localisation
  ou un battement ; remplir une fiche GPS ; écrire une spécification à partir de la fonction.
- **Exercices** (12) : EXO 01, 02 (anciens, complétés d'une question), 03 (trois fonctions + bague de roulement), 04
  (indépendance et enveloppe), 05 (lire quatre cadres, figure), 06 (parallélisme et planéité au comparateur), 07
  (localisation de deux trous, figure), 08 (battement d'un arbre, figure), 09 (liaisons → références), 10 (spécifier un
  support de galet, ★★★), 11 (ancienne chaîne de cotes, hors programme), Concours PT « Flasque de motoréducteur »
  (A ajustement du roulement, B mise en position, C fiche GPS, D trous de fixation, E contrôle ; figure).
- **Cartes ajoutées** (15) : indépendance ; pièce rigide et dualité ; Ⓔ (cat form) ; maximum de matière ; trois
  modèles ; six opérations ; définition d'une spécification ; trois manières de spécifier ; flèche intégral / dérivé ;
  cote encadrée ; zone de localisation ; planéité / parallélisme ; référence spécifiée d'un plan ; ordre des
  références ; battement et excentration (cat form).

## Notations

Cote nominale \(N\), écarts \(ES\), \(EI\) (gardés pour toute cote, comme dans les cartes existantes), \(IT\) ;
alésage \(D\) (\(D_{\min}\), \(D_{\max}\)), arbre \(d\), jeu \(J = D - d\), \(J_{\max} = D_{\max} - d_{\min}\),
\(J_{\min} = D_{\min} - d_{\max}\), serrage maximal \(-J_{\min}\) ; tolérance géométrique \(t\) ; Ⓔ, « maximum de
matière », « élément tangent extérieur à la matière », « skin model », opérations : identiques au §10 de `ppm` (qui
renvoie à ce chapitre pour le détail). Liaisons : noms du chapitre `liaisons` (sphère-cylindre, sphère-plan, appui
plan, pivot glissant ; Tx…Rz) et seuils \(L/D \lt 0{,}8\) / \(\gt 1{,}5\), basculement \(j/L\) (comme `liaisons` et
`conception`). Les symboles GPS sont **dessinés** dans les SVG : ⌖ ⌭ ⌯ ⏥ ↗ ⌰… n'existent dans aucune police du site.

## Doutes et points d'intégration

- **Ⓔ en texte** (U+24BA) : absent des polices du site, affiché par une police système (comme dans `ppm`) ;
  correct dans Chromium, à surveiller sur d'anciens téléphones. Dans les figures, Ⓔ est dessiné.
- **Liens** : `#liaisons/cours` (chapitre créé dans ce lot, absent du dépôt actuel), `#conception/cours`,
  `#ppm/cours`. Le §11 renvoie à « Liaisons, §11 » (conditions géométriques) : à vérifier si la numérotation de
  `lia-cours` change à l'intégration.
- **Principe de responsabilité** : formulation simplifiée de l'ISO 8015:2011 (concepteur : adéquation et
  non-ambiguïté ; vérificateur : mesure et incertitude).
- **Fiche GPS** : aucun format normalisé ; rubriques choisies d'après l'usage des cours de SI, rédaction originale.
- **Passage de vis** (§12, EXO 07, 10, concours D) : modèle simple (axes parallèles, positions théoriques confondues
  à l'assemblage), présenté comme démarche et non comme formule à retenir.
- **EXO 08 Q2** : la valeur « 24,5 µm sur un tour continu » vient du modèle qui a servi à fabriquer les lectures.
- Les cartes 11 à 13 et 19 à 22 gardent leur préfixe « Hors programme (pour aller plus loin) : », exact (ISO 286 et
  chaîne de cotes ne sont au programme d'aucune des deux années).
- Après intégration : `python3 tools/replier_panneaux.py` (les panneaux sont écrits dépliés).
