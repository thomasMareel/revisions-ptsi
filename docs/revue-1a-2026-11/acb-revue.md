# Revue et réécriture : `acidobase` (prefix `acb`), « Réactions acido-basiques » — 2026-11-21

Point 4 de l'audit (`docs/audit-2026-11/physique-1a.md` §2 point 4, §3, §5 points 6 et 7). Programme : PTSI 2021, partie 4.4.1
(réactions acido-basiques), partie 4.1.1 (avancement, état final, capacité numérique) et partie expérimentale 8 (titrages).

## Fichiers
- `acb-cours.src.html` (construit par `acb_construire.py` depuis `acb-cours.tpl.html` + `acb_figs.json`), `acb-meth.src.html`,
  `acb-exos.src.html` (depuis `acb-exos.tpl.html`), `acb-cartes-corr.json` (5 cartes), `acb-cartes-ajout.js` (15 cartes).
- Scripts : `acb_chimie.py` (pH exact par électroneutralité et dichotomie, titrages simulés, partagé avec `pre`),
  `acb_calculs.py` (cours), `acb_calculs_meth.py`, `acb_calculs_exos.py`, `acb_figs.py` (9 figures), `acb_tester_code.py`
  (exécute chaque bloc `<pre class="codeblock">` d'un fichier), `acb_cartes_rendu.js`, `acb_voir.py`, `acb_deborde.js`.
- Copies des anciens panneaux : `acb_orig_{cours,meth,exos}.html`.

## Erreurs et défauts corrigés
1. **Hors-programme présenté comme exigible** (audit §3) : la méthode 1 « Calculer le pH d'une solution » appliquait les formules de pH
   que le cours disait non exigibles. Elle est remplacée par la méthode 5 « Déterminer l'état final et le pH par la réaction
   prépondérante » ; toutes les formules de pH sont regroupées en « POUR ALLER PLUS LOIN · FORMULES DE pH (HORS PROGRAMME) », avec
   leur domaine de validité et trois contre-exemples chiffrés (HCl 10⁻⁸ : 6,98 et non 8 ; acide acétique 10⁻⁵ : 5,16 et non 4,9).
2. Ancien EXO 01 (pH par formule) et ancien EXO 02 (formule de l'acide faible) : gardés (justes), mais corrigés par la réaction
   prépondérante avec vérification des hypothèses ; l'ancien « Concours PT » (titrage, pH à l'équivalence par la formule de la base
   faible) devient l'EXO 09, rédigé par la RP.
3. « Pour un titrage fort/fort, pH = 7 à l'équivalence ; n_acide = n_base » : la relation d'équivalence est maintenant écrite avec les
   coefficients stœchiométriques (piège H₂SO₄, méthode 8, carte 10 corrigée).
4. « pH = pKa à la demi-équivalence » donné sans condition (cours, méthode 3, carte 12) : nuancé (faux pour un acide trop dissocié,
   chiffré dans l'exercice concours : 2,30 au lieu de 2,1 pour H₃PO₄).
5. Diagramme de distribution d'origine dessiné à main levée (courbes de Bézier, libellés à 10 px) : remplacé par des courbes calculées.
6. Constantes : \(K_e\), \(K_a\) écrites avec \(c^\circ\) partout (comme \(K^\circ\) d'`equilchim` et de `thc`) ; « mol/L » → mol·L⁻¹ ;
   OH⁻ → HO⁻ ; équations de réaction écrites avec « = » (comme `thc`).

## Couverture du programme, avant → après
| Capacité (PTSI 2021) | Avant | Après |
|---|---|---|
| Caractère acido-basique d'une réaction | une phrase | §1 (+ exemple, méthode 1, EXO 01) |
| Ke, pH, influence de T | §1 sans T | §2 (tableau pKe(T), ordres de grandeur, piège de la dilution) |
| Ka, force, acides et bases usuels du programme | liste dans une notice | §3 (tableau des 8 espèces du programme, nivellement), EXO 01 |
| Diagrammes de prédominance et de distribution | §2 (schémas) | §4 (3 figures calculées, règle des 1 et 2 unités), méthode 2, EXO 03 |
| Combinaison linéaire des constantes | ❌ | §5 (démonstration, échelle des pKa), méthode 3, EXO 04, concours D1 |
| Espèces incompatibles, écrire la réaction selon le milieu et les observations | ❌ | §6 (2 exemples), méthode 4, EXO 04, EXO 07 |
| État final : équilibre ou transformation totale | ❌ | §7 (méthode de la RP, 3 exemples), méthodes 5 et 6, EXO 05, 06 |
| Capacité numérique « état final » | ❌ | §8 (code testé, dichotomie + `brentq`), méthode 7, EXO 08, concours C3 |
| Titrages directs/indirects, simples/successifs/simultanés, suivi pH-métrique | 4 lignes | §9 (2 figures simulées), méthode 8, EXO 09, 11, concours |
| Indicateurs colorés, équivalence et virage | une phrase | §10 (tableau, choix), méthode 9, EXO 09, concours B4 |
| Suivi conductimétrique | ❌ | §10 (figure simulée, Kohlrausch), méthode 10, EXO 10 |
| Solutions tampons (notion utile en TP) | une phrase | §11 (figure, préparation) |

## Contenu
- **Cours** : bloc « AU PROGRAMME · PTSI » + 11 sections (§1 couples ; §2 eau et pH ; §3 constante d'acidité ; §4 prédominance et
  distribution ; §5 constante d'une réaction acido-basique ; §6 prévoir et écrire la réaction ; §7 réaction prépondérante ;
  §8 capacité numérique ; §9 titrages pH-métriques ; §10 indicateurs et conductimétrie ; §11 tampons) + « Pour aller plus loin ».
  16 exemples traités chiffrés, 8 figures calculées (échelle des pKa, prédominance superposée, distributions acétique et
  phosphorique, titrages HCl/CH₃COOH avec zones de virage, conductimétrie, titrage successif, pouvoir tampon). ≈ 87 000 car.
- **Méthodes** : 10 (reconnaître, lire un diagramme, combiner des constantes, prévoir les incompatibilités, RP, totale ou équilibre,
  programmer, exploiter un titrage, choisir un indicateur, exploiter une conductimétrie), chacune avec exemple éclair vérifié, 4 pièges.
- **Exercices** : 12 (dont 3 anciens repris) : EXO 01 couples et espèces usuelles ; 02 acide fort/base forte (+ dilution extrême,
  37 °C) ; 03 distribution des phosphates ; 04 combinaisons et incompatibilités ; 05 acide acétique par la RP ; 06 trois mélanges ;
  07 vinaigre et bicarbonate (rôle du dégagement gazeux) ; 08 capacité numérique ; 09 titrage d'un acide faible ;
  10 titrage conductimétrique ; 11 titrage indirect (coquille d'œuf) ; **Concours PT** « Un détartrant à l'acide phosphorique »
  (4 parties : espèces, titrage successif simulé et indicateurs, RP et programme Python, action sur le tartre par combinaison avec Ks).
- **Cartes** : 5 réponses corrigées (7, 8, 9 : préfixe « Hors programme en PTSI », origine RP et domaine de validité ; 10 : relation
  d'équivalence ; 12 : condition de « pH = pKa ») ; 15 ajoutées (combinaison, K° acide-base, incompatibilité, RP, seuil « totale »,
  milieu, fractions, règle des unités, capacité numérique, types de titrages, indicateur, conductimétrie, neutralité à 37 °C, pKa de
  l'eau, ordres de grandeur). Questions inchangées. `corriger_cartes.py … --essai` : 5 corrigées ; `ajouter_cartes.py … --essai` : 20 → 35.

## Vérifications
- Tous les nombres recalculés : `python3 acb_calculs.py`, `acb_calculs_meth.py`, `acb_calculs_exos.py` (pH exacts par
  électroneutralité comparés aux résultats de la RP) ; codes Python exécutés par `acb_tester_code.py` (sorties identiques aux
  commentaires).
- `verif_src.py` : aucune erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges` vides, aucune erreur JS
  (trois formules en ligne des exercices coupées pour tenir à 390 px) ; figures regardées en clair et en sombre (`acb_voir/`).

## Notations
ξ (avancement), x (avancement volumique), \(K^\circ\), \(K_a\), \(K_e\) avec \(c^\circ = 1\ \text{mol·L}^{-1}\), [X] en mol·L⁻¹,
\(h = 10^{-\text{pH}}\), α (fraction d'une forme), HO⁻, « RP » pour réaction prépondérante, \(V_E\) (équivalence), λ (conductivités
molaires ioniques, mS·m²·mol⁻¹). pKa usuels : 2,0 ; 2,1/7,2/12,4 ; 3,2 ; 3,8 ; 4,8 ; 6,4/10,3 ; 7,5 ; 9,2.

## Doutes
- Le programme dit les titrages « étudiés exclusivement en travaux pratiques » ; leurs capacités (partie 8) restent exigibles, d'où
  §9-§10. La loi de Kohlrausch n'est pas nommée dans le programme : présentée comme « fournie dans les énoncés ».
- Le mot « tampon » n'est pas dans le programme de PTSI ; §11 le présente comme une conséquence des §4 et §7 (utile en TP).
- Les valeurs de pKe(T) et des zones de virage varient légèrement selon les tables (à une ou deux décimales près).
- Le lien vers « Équilibres chimiques » (`#equilchim/cours`) suppose que ce chapitre traite l'avancement et \(Q_r\) (c'est le cas) ;
  la capacité numérique y est seulement renvoyée, pas dupliquée.
