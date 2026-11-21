# Revue du chapitre `moulage` (prefix `moul`) — lot 5, point 4 de l'audit (2026-11-21)

Fichiers : `moul-cours.src.html` (construit par `moul_construire.py` depuis `moul-cours.tpl.html` et `moul_figs.json`),
`moul-meth.src.html`, `moul-exos.src.html` (assemblé par `moul_assembler_exos.py`), `moul-cartes-corr.json`,
`moul-cartes-ajout.js`. Scripts : `moul_svg.py` (aides SVG, aussi utilisées par `fad`), `moul_figs.py` (9 figures
calculées), `moul_calculs.py`, `moul_calculs_meth.py`, `moul_calculs_exos.py` (tous les nombres du cours, des méthodes
et des corrigés), `moul_voir.py` (aperçu des figures, clair et sombre), `moul_cartes_rendu.js`, `moul_deborde.js`.
Anciens panneaux : `moul_orig_{cours,meth,exos}.html`.

## Renommage proposé (à décider)

Le chapitre couvre maintenant la fonderie, l'injection des thermoplastiques et la mise en forme des composites : je propose
**« Moulage : fonderie, injection plastique et composites »** (mobLabel « Moulage, injection, composites »). Les renvois
écrits dans `fad-cours.src.html` emploient déjà ce titre (intro du bloc programme) ou « Moulage ». Si le titre reste
« Moulage (fonderie) », remplacer dans `fad-cours.src.html` le libellé du lien de l'intro. Le cours `ppm` §1 cite encore les
anciens titres « Moulage (fonderie) » et « Frittage & fabrication additive » : à retoucher à l'intégration.

## Programme (si.txt, G2)

- S2 : « Évaluer la capacité d'un procédé à réaliser une **pièce plastique** » (injection plastique et procédés additifs ;
  domaines d'application ; règles de conception) et « une **pièce composite** » (mise en forme des matériaux composites et
  procédés additifs ; domaines ; règles de conception). « Procédés additifs » = fabrication additive (chapitre `addfab`),
  pas les additifs des polymères.
- S3 : pièce métallique (moulage, déformation, découpage, procédés additifs, soudage, traitements thermiques) et critères
  de choix des procédés. La fonderie est donc une **anticipation** de la 2ᵉ année : signalée par un encadré en tête du §2
  (valable pour §2 à §4), par le bloc « Au programme » et par le titre des exercices 05 et 11 et de la méthode 5.
- Commentaire du programme : « L'analyse des procédés se limite à une approche qualitative ». Les calculs (force de
  fermeture, temps de refroidissement, loi des mélanges, coût) sont présentés comme ordres de grandeur ; la relation
  complète du temps de refroidissement, la règle du module (Chvorinov) et la rigidité transverse sont dites non exigibles.

| Capacité | Avant | Après |
|---|---|---|
| Pièce plastique : injection (presse, moule, cycle) | absente en 1A (seulement `ppm` §6, 2A) | §5 polymères, §6 presse et moule, §7 cycle ; M6-M8 ; EXO 04, 06, 07, 08 ; concours A |
| Pièce plastique : règles de conception | absentes | §8 (épaisseurs, nervures, congés, dépouilles, bossages, contre-dépouilles, seuil, lignes de soudure, défauts) ; figure des nervures calculée ; M6 ; EXO 08 |
| Pièce composite : constituants, loi des mélanges | absente en 1A | §9 ; M9 ; EXO 09 ; concours B |
| Pièce composite : mise en forme (drapage, contact, infusion, RTM, autoclave, enroulement, pultrusion, SMC) | absente | §10 (tableau, figure) ; EXO 10 |
| Pièce composite : règles de conception | absentes | §11 (orientation, symétrie, arrêts de plis, rayons, perçages, délaminage) ; exemple de l'angle d'enroulement 54,7° |
| Fondements communs (empreinte, plan de joint, dépouille, noyau, retrait) | dispersés dans la fonderie | §1 (avec phénomènes physiques et retrait chiffré) ; M2, M3 |
| Fonderie (S3, anticipée) | §1-§4, sans encadré, figure fausse | §2-§4 signalés « 2ᵉ année vue en avance », figure refaite, défauts, module et masselotte ; M4, M5 ; EXO 05, 11 |
| Critères de choix et coût (S3) | une phrase | §12 (tableau, \(C_u\), \(N^*\), figure, environnement) ; M1, M10 ; concours C |

## Erreurs trouvées et corrigées

1. **Figure du moule en sable** : le noyau flottait au milieu de l'empreinte, sans **portées** (un noyau doit être tenu dans
   le sable du moule) ; libellés de 8,5 et 9 px (sous le minimum de 12 px) ; et tous les contours dessinés en
   `class="fl-soft sk-ink"` étaient **invisibles** : l'opacité de `.fl-soft` (0,06) s'applique aussi au trait. Figure refaite
   (portées, chenal et attaque sur le plan de joint, masselotte sur la semelle, évent), remplissage et contour séparés.
   Même défaut d'opacité dans l'ancienne figure de dépouille : refaite.
2. **Rugosité du sable** : cours et carte 9 « \(R_a\) ≈ 6 à 25 µm », chapitre `ppm` « 12,5 à 50 µm » ; harmonisé sur `ppm`
   (cours §2, §3 et carte 9, réponse seule).
3. **Moulage en coquille** « réservé aux métaux à bas point de fusion (Al, Zn) » : la coquille sert surtout aux alliages
   d'aluminium, de magnésium et de cuivre ; le zinc se moule surtout sous pression. Cours §3 et carte 10 (réponse seule)
   alignés.
4. **Ancien concours, A1** : « la coquille et la sous-pression ne se justifient que pour de très grandes séries » : la
   coquille vise les moyennes et grandes séries ; corrigé (l'exercice devient l'EXO 11).
5. **Ancien EXO 02, Q2** : « aluminium (bas point de fusion) » précisé (environ 660 °C, assez bas pour un moule en acier).
6. **Retrait** : l'ancien cours parlait de « tracer le modèle plus grand du taux de retrait » sans définir \(r\) ; défini
   au §1 par \(L_{\text{empreinte}} = (1 + r)\,L_{\text{pièce}}\), conforme à l'ancien EXO 03 et aux cartes.
7. **Formule en ligne trop large au téléphone** dans l'ancien EXO 03 (débordement de 18 px à 390 px) : passée en bloc.

## Cours : 12 sections + bloc programme + « Pour aller plus loin »

§1 principe commun (viscosités, retrait chiffré pour 5 matières) · §2 sable (figure, rendement de coulée) · §3 coquille,
basse pression, sous pression, cire perdue (tableau IT et \(R_a\), force d'une machine sous pression) · §4 point chaud,
cercles inscrits (figure calculée : L vif 1,17 e, congés e, croix 1,41 e, T décalés 1,25 e), module et masselotte, règles,
dépouille chiffrée, défauts · §5 polymères (amorphes, semi-cristallins, températures, charges, dispersion du retrait) ·
§6 presse et moule (figure), \(F_f \geq p_e S_p\) · §7 cycle (figure calculée de \(p_e(t)\)), \(t_r \propto e^2/a\),
cadence · §8 règles de conception (figure des nervures : 1,25 e contre 1,09 e), défauts · §9 composites, loi des mélanges,
stratification (figure), carbone contre acier · §10 procédés (figure, tableau), plis et résine d'une plaque RTM · §11
règles de conception des composites, angle d'enroulement · §12 choix et coût (tableau, figure, environnement).
13 exemples chiffrés, 9 figures calculées (`moul_figs.py`), 100 600 caractères.

## Méthodes (10, au lieu de 2 et une liste de pièges)

1 choisir un procédé de moulage · 2 plan de joint et démoulage · 3 empreinte et modèle (retrait, surépaisseur) ·
4 dépouille (fonderie et injection) · 5 point chaud et masselotte (fonderie, 2ᵉ année) · 6 vérifier une pièce injectée ·
7 force de fermeture · 8 effet de l'épaisseur sur le cycle · 9 stratifié · 10 coût et seuil. Les anciennes méthodes 1-2 et
les pièges sont repris dans 1, 2, 3, 5 et les notices. Exemples éclair vérifiés (`moul_calculs_meth.py`).

## Exercices (12)

EXO 01-03 anciens (02 complété d'une Q4 sur une pièce injectée ; 03 formule en bloc) · 04 thermoplastique ou
thermodurcissable · 05 dépouille et masselotte (fonderie) · 06 force de fermeture d'un plateau · 07 cycle, cadence et coût ·
08 critique d'un tracé injecté (cercles inscrits) · 09 lame de suspension composite · 10 choisir un procédé composite ·
11 ancien concours « support de palier » (fonderie, 2ᵉ année vue en avance) · **Concours PT** « capot de batterie de vélo :
injection ou composite ? » (A injection, B composite RTM, C coût, 280 €/kg gagné). Corrigés vérifiés
(`moul_calculs_exos.py`).

## Cartes (24 → 39)

- Corrigées (réponse seule, question inchangée) : 9 (rugosité et précision du sable), 10 (coquille : alliages concernés).
- Ajoutées (15) : viscosité et pression, thermoplastique/thermodurcissable, retrait amorphe/semi-cristallin, empreinte
  \((1+r)L\), cycle d'injection, \(F_f \geq p_e S_p\), \(t_r \propto e^2/a\), nervures, tiroir et ligne de soudure, fibres et
  matrice, loi des mélanges, ordres de grandeur des fibres, stratifié symétrique et équilibré, procédés composites, coût
  et seuil. Rendu contrôlé avec `flashPretty` + MathJax (`moul_cartes_rendu.js`, aucune erreur ; trois réponses écrites en
  `\( … \)` pour éviter une conversion maladroite).

## Notations

Celles de `ppm` (2ᵉ année) : \(F_f\), \(p_e\), \(S_p\), \(t_r\), \(e\), \(a\), \(V_f\), \(E_f\), \(E_m\), \(E_\parallel\),
\(\rho_c\), \(C_u\), \(C_o\), \(C_v\), \(N^*\) ; retrait linéaire \(r\) ; module de refroidissement \(M = V/S\) ; \(R_a\), IT.

## Doutes

- Ordres de grandeur de la coquille (IT 12-14, \(R_a\) 3,2-12,5 µm) et de la cire perdue (IT 10-12, \(R_a\) 1,6-3,2 µm) :
  valeurs usuelles des tableaux de procédés, absentes de `ppm` ; taux de fibres du SMC « ≈ 20 % » (en volume, avec charges
  minérales) ; taux « ≈ 30 % » au contact repris de `ppm` (souvent moins avec un mat).
- `ppm` §6 (2ᵉ année) recouvre maintenant les §5 à §11 : il pourrait devenir un rappel court renvoyant à ce chapitre.
- Le chapitre est long (12 sections) parce qu'il réunit trois familles ; une scission (fonderie / plasturgie et composites)
  est possible si l'on préfère des chapitres plus courts.
