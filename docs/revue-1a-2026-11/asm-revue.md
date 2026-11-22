# Revue du chapitre `assemblage` (prefix `asm`) — lot 7, point 4 de l'audit (2026-11-22)

Fichiers : `asm-cours.src.html` (construit par `asm_construire.py` depuis `asm-cours.tpl.html` et `asm_figs.json`),
`asm-meth.src.html`, `asm-exos.src.html`, `asm-cartes-corr.json` (1 carte), `asm-cartes-ajout.js`.
Scripts : `asm_svg.py` (copie de `moul_svg.py`), `asm_figs.py` (6 figures calculées), `asm_calculs.py`,
`asm_calculs_meth.py`, `asm_calculs_exos.py` (tous les nombres), `asm_voir.py` (aperçu clair et sombre, `asm_voir/`),
`asm_cartes_rendu.js`, `asm_deborde.js`. Anciens panneaux : `asm_orig_{cours,meth,exos}.html`.

## Programme (si.txt)

- G2, **S3** : « Évaluer la capacité d'un procédé à réaliser une pièce métallique » : **assemblage par soudage**, domaines
  d'application, **règles de conception**, critères de choix des procédés.
- F3, **S4** : « Concevoir et dimensionner une liaison mécanique » : exigence technique **assemblage** (traitée en 2ᵉ année
  dans `conception`, §2-§4).
- Notions de 1ʳᵉ année réutilisées : frottement de Coulomb (`statique`, S2), nature des ajustements (`cotation`, S2).

Rien n'est exigible en PTSI : bloc « Au programme · PTSI » explicite et encadré **« Vu en avance (2ᵉ année) »** en tête.
Le doublon signalé par l'audit (ancien §4 ↔ `conception` §3-§4) est résolu : le §11 ne garde que le principe de
l'adhérence, les règles courantes et un exemple, avec renvoi à `conception` (mêmes notations : \(T_{max} = f\,n_f\,n\,F_0\),
\(\sigma = F_v/A_s \le R_e/s\)).

| Capacité | Avant | Après |
|---|---|---|
| Familles, démontable/permanent, modes de transmission | §1 (une liste) | §1 (tableau obstacle / adhérence / continuité / adhésion, exemple du treillis), M1, EXO 01, 03 |
| Soudage : principe, énergie | §2 (définitions) | §2 (figure du MAG, soudabilité, brasage, \(E = \eta U I/v\), section fondue estimée), M2, EXO 04 |
| Procédés de soudage et domaines | 3 lignes | §3 (tableau de 7 procédés, point de soudure \(Q = RI^2t\)) |
| ZAT, phénomènes thermiques | une phrase | §4 (figure calculée des températures maximales, ZAT 4,5 / 2,2 / 6,0 mm, préchauffage, recuit de détente), EXO 02 |
| Déformations, contraintes résiduelles | une phrase | §5 (\(\sigma = E\alpha\Delta T\), formes de déformation, remèdes), M6, EXO 07, concours C |
| Joints et préparation des bords | **absents** | §6 (figure à l'échelle V / X / bords droits, métal déposé et temps), M3, M4, EXO 05 |
| Dimensionner un cordon | **absent** | §7 (gorge, figure, méthode simplifiée, plat sur gousset), M5, EXO 06, concours B |
| Règles de conception d'un ensemble soudé | **absentes** | §8 (accessibilité, peu de cordons, zones sollicitées, épaisseurs, symétrie, usinage après soudage), M7 |
| Rivetage, sertissage, clinchage | 1 ligne | §9 (figure, cisaillement et matage, pince et pas), M8, EXO 08 |
| Collage | 2 lignes | §10 (familles, cisaillement contre pelage/clivage, figure calculée de Volkersen, deux exemples), M9, EXO 09 |
| Assemblages démontables, frettage | §3-§4, recouvrant `conception` | §11 resserré + renvoi (vis en traction, adhérence, frettage), M10, EXO 10, 11, concours D |
| Critères de choix, environnement | une règle | §12 (tableau, exemple points / rivets / colle, fin de vie), M1, concours D |

## Erreurs et imprécisions corrigées

1. **Carte 13** (rivetage) : « sans apport de chaleur excessive » (imprécis : les gros rivets d'acier se posent à chaud ;
   l'essentiel est qu'aucune pièce ne fond) → réponse corrigée (obstacle, pas de fusion ni de ZAT, cisaillement et
   matage) ; question inchangée.
2. Ancien concours « frettage » (devenu EXO 11) : « sans risque pour l'acier » précisé (assez bas pour ne pas altérer une
   denture trempée et revenue) ; refroidissement de l'arbre et combinaison mentionnés.
3. Ancien §4 en doublon de `conception` §3-§4 : remplacé par le §11, court, avec renvoi.
4. Anticipation S3/S4 non signalée : bloc programme et encadré.
5. Anciens EXO 01-03 complétés (Q4-Q5 rivets et pare-brise collé ; Q3 préchauffage ; Q3 aluminium-acier).

## Cours : 12 sections + bloc programme + « Pour aller plus loin »

§1 familles · §2 principe et énergie · §3 procédés · §4 ZAT · §5 déformations et contraintes résiduelles · §6 joints et
préparations · §7 dimensionner un cordon · §8 concevoir un ensemble soudé · §9 rivetage · §10 collage · §11 démontables et
frettage · §12 choix · Pour aller plus loin (relation d'Adams, carbone équivalent, modèle de Volkersen, friction-malaxage,
méthode directionnelle). 12 exemples chiffrés, 6 figures calculées (MAG, températures maximales et ZAT, préparations à
l'échelle, gorge et cordons latéraux, rivetage, cisaillement dans un joint collé), 71 000 caractères.

## Méthodes (10, au lieu de 2 et des pièges)

1 choisir un mode d'assemblage · 2 énergie de soudage · 3 joint et préparation · 4 métal déposé et temps (section \(a^2\)
d'un cordon d'angle) · 5 cordons d'angle · 6 limiter les déformations · 7 critiquer un ensemble soudé · 8 rivetage ·
9 joint collé · 10 adhérence (vis, frettage). L'ancienne méthode 2 (frettage) est reprise dans la 10.

## Exercices (12)

EXO 01-03 anciens complétés · 04 énergie de soudage (la plus grande puissance n'est pas la plus grande énergie) · 05 V ou X
sur 16 mm · 06 plat sur gousset (cordons latéraux, puis frontal) · 07 contraintes résiduelles d'un bâti (acier, aluminium) ·
08 éclisse rivetée (le matage dimensionne) · 09 collage à recouvrement · 10 console vissée · 11 ancien concours (frettage) ·
**Concours PT** « potence de palan » : A soudage colonne-platine (énergie, épaisseurs, métal déposé), B tenue des cordons
(limite \(a \le 0{,}7\,e\) qui impose goussets ou tube plus fort), C déformations, D version en kit boulonnée et choix.

## Cartes (22 → 37)

Corrigée : 13 (réponse seule). Ajoutées (15) : énergie de soudage, brasage, MIG/MAG/TIG, soudage par points, préchauffage,
contraintes résiduelles, remèdes aux déformations, préparations selon l'épaisseur, X contre V, gorge, méthode
simplifiée, règles de la mécanosoudure, rivetage (cisaillement et matage), collage, vis en traction et adhérence. Rendu
vérifié (`asm_cartes_rendu.js`, aucune erreur MathJax) : les réponses chiffrées sont écrites en `\( … \)` pour que
`flashPretty` ne mathématise pas « X », « V » ou « 3 mm ».

## Notations

Comme `conception` et `rdm` : \(F_0\), \(f\), \(n_f\), \(n\), \(T_{max}\), \(A_s\), \(R_e\), \(s\), \(R_{pe}\), \(\tau\),
\(\tau_{adm}\), \(p_{adm}\) ; nouvelles : énergie de soudage \(E = \eta U I/v\) (J/mm), gorge \(a\), côté \(z\), longueur
de cordon \(\ell\), plans de cisaillement \(m\), précharge \(F_0\), serrage \(\delta\), jeu de montage \(j\).

## Doutes et propositions

- **Renommage proposé** : « Assemblages : soudage, rivetage, collage, vissage » (mobLabel « Assemblages ») ; le titre
  actuel « Assemblage & soudage » reste juste. `conception` §1 cite « Assemblage & soudage » : à aligner si l'on renomme.
- Valeurs indicatives (non issues du programme) : \(\tau_{adm}\) des cordons 150-200 MPa, de colle 5-10 MPa (valeur de
  calcul), rendement thermique 0,6-0,8, taux de dépôt 2-5 kg/h, préparations selon l'épaisseur, pince 1,5-2 \(d\), pas 3 \(d\).
- La figure de la ZAT repose sur la relation d'Adams (tôle mince, propriétés constantes) : largeurs indicatives ; la figure
  du collage sur le modèle élastique de Volkersen, qui exagère la saturation pour une colle ductile (dit dans le cours).
- Concours B : \(W_g = \frac43 a b^2\) (anneau de gorge assimilé à un tube mince de côté \(b\)) est fourni par l'énoncé ;
  D : modèle simplifié de la traction des vis (bras de levier 200 mm, effet de levier des platines ignoré, signalé).
- Ce chapitre et `deform` relèvent entièrement de la 2ᵉ année : on pourrait les marquer « 2ᵉ année vue en avance » dans la
  navigation (comme les encadrés le font dans le cours).
