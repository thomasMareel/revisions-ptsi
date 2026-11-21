# Revue du chapitre `changement` — « Corps pur diphasé et changements d'état » (1ʳᵉ année, prefix `ce`)

Revue du 2026-11-21, d'après `CONSIGNES-1A.md` (et `em/CONSIGNES-EM.md`, `em/CONSIGNES-EM-1A.md`,
`revue/CONSIGNES-REVUE.md`, `maths/CONSIGNES.md`). Programme : PTSI 2021, parties 3.1 (corps pur diphasé), 3.3
(enthalpies de transition de phase) et 3.4 (\(\Delta h_{12} = T\Delta s_{12}\)) de le programme officiel de PTSI
(l. 1502-1513, 1574-1580, 1603-1606) ; 2ᵉ année : `phys.txt` partie 1.3 (l. 618-655). Motif : audit
`docs/audit-2026-11/physique-1a.md` §2 point 2 et §5 point 3 (le site renvoyait à tort en 2ᵉ année le diagramme (P, v),
le titre par la règle des moments et \(\Delta s = \Delta h/T\)). Rédaction originale ; toutes les valeurs recalculées.

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `ce-cours.src.html` | cours réécrit en entier : bloc « AU PROGRAMME · PTSI », 10 sections §1-§10, deux sections « POUR ALLER PLUS LOIN » (2ᵉ année ; hors programme), 19 exemples traités chiffrés, 7 figures (6 calculées + 1 schéma), ≈ 80 ko |
| `ce-meth.src.html` | 10 méthodes (étapes, exemple éclair chiffré, pièges) |
| `ce-exos.src.html` | 12 exercices (11 + « Concours PT » en 4 parties), un seul `.exo-wrapper` |
| `ce-cartes-corr.json` | 1 réponse corrigée (question inchangée) |
| `ce-cartes-ajout.js` | 15 cartes ajoutées en fin de deck (25 → 40) |
| `ce-cours.tpl.html` + `ce_construire.py` | gabarit du cours (`@@FIG:nom@@`) et assemblage |
| `ce_figs.py` → `ce_figs.json` | figures calculées (CoolProp 8 : IAPWS-95 pour l'eau, Span-Wagner pour CO₂ ; sublimation : IAPWS R14-08 et Span-Wagner 1996, vérifiées à 1 atm) ; aussi les 3 figures de `thermo1` |
| `ce_calculs.py`, `ce_calculs_meth.py`, `ce_calculs_exos.py` | vérification de tous les nombres du cours, des méthodes et des exercices |
| `ce_cartes.py` | génère les fichiers de cartes (et ceux de `thermo1`) |
| `ce_voir.py` | aperçu PNG des figures, clair et sombre |

Contrôles passés : `verif_src.py` (aucune erreur ni « attention ») ; `apercu_src.py` à 390 et 1440 px pour les trois
panneaux : `merr`, `brut`, `larges` vides, `scrollW` = largeur, aucune erreur JS ; captures du cours (1440) et des 7 figures
(clair et sombre, `ce_voir.py`) regardées ; `corriger_cartes.py --essai` (1 corrigée) et `ajouter_cartes.py --essai`
(25 → 40) sans erreur.

## Erreurs trouvées dans l'existant (et corrigées)

1. **Encadré d'en-tête** : « Le diagramme (P, v) et cette relation [\(\Delta h_{12} = T\Delta s_{12}\)] ne sont pas encore
   développés ici » — capacités exigibles en PTSI absentes du cours ; le titre n'était défini que par une phrase, sans
   règle des moments ni diagramme (P, v). Tout est maintenant traité (§4-§6, §9-§10) ; les seuls renvois « vu en 2ᵉ
   année » concernent ce qui l'est vraiment (potentiel chimique, diagrammes (T, s), (h, s), (log P, h), tables).
2. **§2 de l'ancien cours** intitulé « Enthalpie de changement d'état — équation de Clausius-Clapeyron » : la relation de
   Clausius-Clapeyron (hors des deux programmes) occupait la moitié d'une section du programme ; déplacée en
   « Pour aller plus loin · hors programme ».
3. **Ancien exo 03** (titre, chaudière) : le chauffage n'était pas dit **isobare** (nécessaire pour \(Q = \Delta H\) et pour
   parler de vapeur surchauffée) ; \(c_{\text{vapeur}} = 2\) remplacé par \(c_p \approx 2{,}2\ \text{kJ·K}^{-1}\text{·kg}^{-1}\)
   (CoolProp : 2,22 entre 150 et 200 °C sous 4,76 bar), d'où \(Q_2 = 110\ \text{kJ}\) et \(Q = 1\,589\ \text{kJ}\) ; « un
   chaudière » ; question d'entropie ajoutée (Q4).
4. **Ancien exo 02** (Clausius-Clapeyron, hors programme) : \(M\Delta h_{\text{vap}} = 42{,}2\) et non 42,3 kJ·mol⁻¹
   (8,314 × ln 2 / 1,364·10⁻⁴ = 42 238) ; \(P(80\ °\text{C}) = 0{,}468\) bar ; comparaison à la table ajoutée.
5. **Ancien exo 04** (règle des phases, hors programme) : variance notée \(v\), comme le volume massique du chapitre →
   \(\mathcal V\).
6. **Ancien exo 06** : la valeur 108,9 J·K⁻¹·mol⁻¹ présentée comme « la règle de Trouton » → comparaison à la règle
   (hors programme) ; Q3 (enthalpie libre) signalée « 2ᵉ année ».
7. **Ancien « Concours PT »** (3 questions de calorimétrie, quasi doublon de l'exo 01) : gardé en exo 07, complété d'une
   partie C (bilan d'entropie) ; nouveau sujet « Concours PT » en 4 parties.
8. **Carte n° 19** (« Enthalpie de vaporisation : comment la mesurer ? ») : seule réponse donnée, hors programme
   (Clausius-Clapeyron) → méthode électrique à deux puissances (programme : « mettre en œuvre un protocole de mesure
   d'une grandeur énergétique »), Clausius-Clapeyron cité comme hors programme.
9. Imprécisions de l'ancien cours supprimées : « l'eau bout à ~70 °C en altitude » (Everest seulement ; remplacé par le
   mont Blanc, 84 °C, calculé), figure (P, T) purement schématique (remplacée par deux diagrammes calculés).

Les autres cartes ont été relues : justes (les cartes hors programme 5, 7, 8, 9, 11, 12, 19 sont déjà préfixées).

## Couverture du programme, avant → après

| Capacité (PTSI) | Avant | Après |
|---|---|---|
| Corps pur diphasé, palier sous P fixée | phrase (§4) | §1 (courbe d'échauffement calculée, exemple chiffré), méthode 1 |
| Analyser un diagramme (P, T) expérimental, positionner les phases | §1 + schéma | §2 : diagrammes calculés de l'eau et de CO₂, tableau triple/critique, 2 exemples ; méthode 1 ; exo 01 |
| Jeu de variables d'état d'un corps pur diphasé | absent | §3 (encadré + exemple « même (P, T), états différents ») ; méthode 2 ; carte |
| Diagramme de Clapeyron (P, v), positionner les phases | absent | §4 : diagramme calculé, allure des isothermes, table \(v_L\), \(v_V\) ; méthode 3 ; exos 03, Concours |
| Composition d'un mélange en un point du diagramme (P, v) | définition de x seule | §5 (règle des moments, démonstration, figure calculée, exemple) ; §6 (compression isotherme, chauffage isochore, figure calculée) ; méthodes 4-5 ; exos 03, Concours B-C |
| Travail des forces de pression dans un diagramme de Clapeyron | absent | §7 (aire sous le palier, \(\Delta u_{\text{vap}}\)) ; carte |
| Enthalpies de fusion, vaporisation, sublimation ; bilans avec transition | §2, §4 (notation L) | §7 (\(\Delta h_{12}\), tableau, variation avec T) ; §8 (chemin fictif, 4 exemples) ; méthodes 6-7 ; exos 02, 04-07 |
| Protocole de mesure (enthalpie de fusion…) | absent | §8 (méthode des mélanges, sensibilité) ; méthode 10 ; exo 09 ; carte 19 corrigée |
| \(\Delta h_{12}(T) = T\Delta s_{12}(T)\) | renvoyé en 2ᵉ année | §9 (justification, valeurs, contrôle sur table) ; méthode 8 ; exos 04, 08 ; cartes |
| Bilan d'entropie avec transition | absent | §10 (3 exemples : glaçon dans une pièce, eau-glace, vapeur injectée) ; méthode 9 ; exos 05-07 |

Hors programme regroupé en fin de cours : Clausius-Clapeyron, variance, retards (surfusion, surchauffe), Trouton ;
« vu en 2ᵉ année » : tables, diagrammes (T, s), (h, s), (log P, h), potentiel chimique, applications (centrale, réfrigérateur).

## Contenu ajouté

- **Sections** : §1 phases et changements d'état ; §2 diagramme (P, T) ; §3 équilibre liquide-vapeur, \(P_{\text{sat}}\),
  variables d'état ; §4 diagramme de Clapeyron ; §5 titre et règle des moments ; §6 transformations dans (P, v) ;
  §7 enthalpie de changement d'état ; §8 bilans d'enthalpie (calorimétrie, mesure) ; §9 entropie de changement d'état ;
  §10 bilans d'entropie ; deux « Pour aller plus loin ».
- **Figures** (classes du site, aucune couleur en dur) : six changements d'état (schéma) ; courbe d'échauffement de 1 kg
  d'eau ; (P, T) de l'eau (log P, 1 Pa-1 000 bar) ; (P, T) de CO₂ ; Clapeyron de l'eau (v logarithmique, 6 isothermes) ;
  règle des moments sur l'isotherme 300 °C (échelles linéaires) ; tubes scellés chauffés (fraction volumique de liquide).
- **Méthodes** (10) : lire (P, T) ; état physique d'un corps pur ; tracer les isothermes ; titre par la règle des moments ;
  suivre une transformation ; \(\Delta H\) avec changement d'état ; bilan calorimétrique ; \(\Delta S\) avec changement
  d'état ; bilan d'entropie ; mesurer une enthalpie de changement d'état.
- **Exercices** (12) : 01 diagrammes (P, T) eau/CO₂ (nouveau) ; 02 fonte de glace (ancien 01) ; 03 cylindre à 300 °C,
  titre, compression isotherme, échec du gaz parfait près de la saturation (nouveau) ; 04 vaporisation isobare (ancien 03
  corrigé + Q4) ; 05 lait chauffé à la vapeur, entropie créée (nouveau) ; 06 surfusion (ancien 05 + Q4 entropie) ;
  07 glaçons et entropie (ancien concours + partie C) ; 08 entropie de vaporisation (ancien 06) ; 09 mesure de
  \(\Delta h_{\text{vap}}\) par deux puissances (nouveau) ; 10 Clausius-Clapeyron (ancien 02, hors programme) ;
  11 règle des phases (ancien 04, hors programme) ; Concours PT « Bouteille de propane » (pression, composition,
  chauffage isochore et risque d'éclatement, soutirage et refroidissement, entropie).
- **Cartes** (+15) : diagramme de Clapeyron, allure des isothermes, \(v\) d'un mélange, règle des moments,
  \(\Delta s_{12} = \Delta h_{12}/T\), \(\Delta s_{\text{vap}}\) de l'eau, variables d'état, point critique de l'eau,
  \(v_L\)/\(v_V\) à 100 °C, récipient rigide chauffé, \(\Delta h_{\text{sub}}\), \(\Delta h_{\text{vap}}(T)\), méthode du bilan
  calorimétrique, travail de vaporisation, entropie créée par un glaçon.

## Notations

\(\Delta h_{12}\) (et \(\Delta h_{\text{fus}}\), \(\Delta h_{\text{vap}}\), \(\Delta h_{\text{sub}}\)), \(\Delta s_{12}\),
titre \(x\), volume massique \(v\), \(v_L\), \(v_V\), \(v_c\), \(P_{\text{sat}}(T)\), \(T_{\text{sat}}(P)\),
\(S_{\text{éch}}\), \(S_{\text{créée}}\) (comme `thermo3`), pression \(P\) majuscule (comme `thermo1-3`), \(r = R/M\).
Divergence signalée : `thermodiff` (2ᵉ année) écrit \(\Delta_{1\to2}h\), \(p\) minuscule, \(\delta S_e\)/\(\delta S_c\) ;
à harmoniser un jour sur les notations du site (\(\Delta h_{12}\), \(S_{\text{éch}}\), \(S_{\text{créée}}\)).

## Doutes

- La « règle des moments » est nommée dans le programme de PT (1.3) ; en PTSI, la capacité est « déterminer la
  composition d'un mélange diphasé en un point d'un diagramme (P, v) » : la règle y est l'outil naturel, présentée ici
  comme exigible en PTSI, son extension à \(h\) et \(s\) étant signalée « 2ᵉ année ».
- Données non calculées par CoolProp, citées comme ordres de grandeur : \(c_{\text{glace}} = 2{,}1\), \(\Delta h_{\text{fus}}\)
  (334 kJ·kg⁻¹), métaux (fusion de Al, Fe ; Hg, Fe au tableau du §1), masse volumique de la glace (917 kg·m⁻³).
- Le propane commercial est un mélange ; l'exercice concours le traite en corps pur (annoncé dans l'énoncé). La bouteille
  et ses données sont inventées (12,5 kg dans 30,0 L ; pleine de liquide vers 65 °C).
- Patinage (§2) : l'explication par le frottement et la couche quasi liquide de surface est l'état actuel des
  connaissances ; formulée prudemment.
