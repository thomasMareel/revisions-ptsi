# Audit SI de 1ʳᵉ année (PTSI) : couverture du programme 2021 (S1, S2)

Lecture seule, le 2026-11-14. 28 chapitres (`mat == "si"`, `an == 1` de `mesures.json`). Programme : `pdf-pt/prog/si.txt`
(colonne « Semestre »). Lus en entier : ingsys, cine, statique, dynsolide, energsi, cvs, cotation, trsurf, cnd, addfab,
assemblage, deform (§1-4), moulage (extraits), et leurs méthodes et cartes pour les principaux. Survolés : chapitres
récemment réécrits (sequentiel, reseaux, transm, capteurs, usinage, trtherm, groupe Automatique), mcc, hacheurs.
Référence 2ᵉ année : `docs/programme-pt/sciences-industrielles.md` et les cours `chaines`, `dyn2a`, `energ2a`, `chfonc`, `ppm`.

## 1. Tableau de couverture (S1 et S2)

| Bloc du programme (sem.) | Chapitre(s) et § du site | Statut | Remarque |
|---|---|---|---|
| A1 Besoin, exigences, critères et niveaux (S1) | ingsys §1, §2 (req) | 🔶 | Critère, niveau, flexibilité : oui. Vocabulaire APTE (fonction principale, de service, contrainte) plutôt qu'« exigences » ; aucun diagramme des exigences dessiné. |
| A1 Impact environnemental, cycle de vie (S1) | aucun en 1A (chfonc §10, ppm §5 : 2A) | ❌ | Aucune ligne d'ACV en 1ʳᵉ année. |
| A2 Frontière d'étude, milieu extérieur, flux et codage (S2) | ingsys §1 (un paragraphe), statique §2 (isolement), reseaux §4, §6, capteurs §5 (Gray) | 🔶 | Codage réparti (NRZ, hexadécimal, Gray) ; frontière et flux en deux phrases. |
| A3 Architecture fonctionnelle et structurelle, bdd, ibd (S1, lecture) | ingsys §2 | 🔶 | Quatre lignes par diagramme, **aucune figure SysML** (seul le stm est dessiné, dans sequentiel). |
| A3 Chaînes fonctionnelles ; liens entre chaînes, systèmes asservis et séquentiels (S1) | ingsys §3, schblocs §5, capteurs §1 | 🔶 | Terminologie de l'ancien programme : « chaîne d'énergie », « Distribuer » (programme 2021 et 2A : chaîne de puissance, **moduler**). Asservi et séquentiel confondus (voir §4). |
| A3 Capteurs, nature du signal, carte programmable (S2) | capteurs §1-§9 | ✅ | Carte de commande surtout en 2A (chfonc §9). |
| A3 Réseaux : topologie, canal, multiplexage, trame, adressage (S2) | reseaux §1-§8 | ✅ | — |
| A3/B2 Diagramme d'états, chronogramme (S2) | sequentiel §2-§7 | ✅ | — |
| A3 Structure d'un système asservi, poursuite, régulation (S1) | schblocs §1-§4 | ✅ | — |
| A5 Spécification GPS (principes, modèles, opérations, taille, zone, gabarit, enveloppe, fiche GPS) (S2) | cotation §3 (familles de tolérances, une phrase « GPS ») | ❌ | Chapitre écrit sur l'ancien programme (ISO 286, chaîne de cotes). « Skin model » n'existe que dans ppm (2A). |
| B2 SLCI, Laplace, fonction de transfert, signaux canoniques (S1) | slci §1-§5 | ✅ | — |
| B2 Modèles de comportement (1ᵉʳ, 2ᵉ ordre, intégrateur, retard), Bode (S2) | sys1, sys2, bode | ✅ | Cartes de sys2 non alignées (voir §4). |
| B2 Schéma-blocs : élaboration, réduction, FTBO, FTBF (S1) | schblocs §2-§5 | ✅ | — |
| B2 Liaisons : ddl, classes d'équivalence, géométrie des contacts, 11 liaisons normalisées, repères, **symboles**, graphe de liaisons, schéma cinématique (S1) | cine §4, §6 | 🔶 | 7 liaisons sur 11 (ni sphère-cylindre, ni cylindre-plan, ni sphère-plan, ni sphérique à doigt), aucun symbole, aucun schéma, pas de classes d'équivalence. Complet seulement dans **chaines §1 (2A, masqué en mode 1ʳᵉ année)**. |
| B2 Cinématique du solide : torseur, composition, contact ponctuel (roulement, glissement) (S1) | cine §3, §5, §6 | ✅/🔶 | Torseur, BABAR, composition, RSG : oui. Vitesse de glissement et rotations de roulement/pivotement à peine. Un tiers du chapitre est de la cinématique du point de physique (Frenet, cylindrique). |
| B2 Modéliser une action mécanique : local/global, densités, Coulomb et visqueux, résistance au roulement et au pivotement, torseur transmissible, glisseur et couple (S2) | statique §1, §3, §4 | 🔶 | Coulomb, cône, arc-boutement : bien. **Absents** : modèle local (pression) et passage au global, frottement visqueux, résistance au roulement/pivotement (seulement energ2a, 2A), glisseur/couple, torseurs transmissibles en 3D (liaisons données en 2D seulement). |
| B2 Simplifier un mécanisme : liaisons en série et en parallèle, liaisons équivalentes, limites du modèle plan (S2) | aucun en 1A (chaines §4-§5, 2A) | ❌ | — |
| B2 Mobilité, hyperstatisme, rendre isostatique (S2) | statique §3, cine §6 | 🔶 | Une demi-page, formules contradictoires avec chaines §5 (voir §4). |
| B2 Convertisseurs statiques : interrupteurs 2 ou 3 segments, cellule de commutation, synthèse hacheur / onduleur / redresseur, réversibilité (S2) | cvs §2-§4, hacheurs §1-§4 | 🔶 | Interrupteurs et règles d'association des sources : oui. Cellule de commutation non formalisée, **synthèse de l'onduleur et du redresseur absente en 1A** (triphase §7-§9, 2A), **aucune figure** dans cvs. |
| B3, C1, C2 Performances : stabilité, marges, précision, valeur finale, rapidité (S2) | stabilite, precision | ✅ | Hors-programme non signalé dans les cartes et un exercice (voir §3). |
| C2 Réponse temporelle (S1) et fréquentielle (S2) | sys1, sys2, bode | ✅ | — |
| C1 Loi entrée-sortie géométrique par fermeture (S1) | cine §6 (méthode en 4 lignes) | 🔶 | Exemple traité et rigueur dans chaines §2 (2A) seulement. |
| C2 Relations géométriques et cinématiques, transmetteurs (S2) | transm §1-§9, cine §6 | ✅ | — |
| C2 PFS, actions réciproques, référentiel galiléen (S2) | statique §2, §4 | ✅ | — |
| C1 Kirchhoff, superposition (S1) | chapitres d'électricité de physique | ✅ | Hors SI, suffisant. |
| D3 Erreurs de mesure : résolution, justesse, fidélité, linéarité… (S2) | capteurs §3, §8 | ✅ | — |
| G2 Pièce plastique : injection, additifs ; pièce composite (S2) | addfab §2 (additifs) | 🔶/❌ | Injection plastique et composites : seulement ppm §6 (2A). Aucune règle de conception pour la fabrication additive. |
| B2 Modeleur 3D (S2), D1-D2, E1-E2 | — | — | Pratiques de TP, pas de cours attendu. |

**Anticipations de S3/S4 placées en 1A** (légitime, à signaler dans un encadré) : moulage, deform, assemblage (soudage), trtherm,
usinage (S3, « pièce métallique », finition), dynsolide et energsi (S3), mcc (S4). 22 chapitres sur 28 n'ont pas d'encadré
« Au programme » ; usinage et trtherm en ont un intitulé « PT » alors qu'ils sont rangés en 1ʳᵉ année.

## 2. Manques importants (par fréquence aux concours PT)

1. **Modélisation des mécanismes en 1ʳᵉ année** (S1-S2) : 11 liaisons normalisées avec symboles, torseurs cinématiques **et**
   transmissibles en 3D, classes d'équivalence, graphe de liaisons, schéma cinématique, liaisons équivalentes, mobilité et
   hyperstatisme cohérents. Présent au bon niveau dans `chaines` (2A), donc invisible pour un élève réglé en 1ʳᵉ année, et
   traité en 1A dans cine §4/§6 et statique §3 de façon incomplète et fautive. Tombe dans presque tous les sujets.
2. **Spécification GPS** (A5, S2) : `cotation` ne traite aucun des attendus (principes d'indépendance et de l'enveloppe,
   modèles nominal / extrait / skin model, opérations, taille / zone / gabarit, références et liaison, nature d'ajustement).
   Fréquent dans les épreuves de conception et d'industrialisation de la Banque PT.
3. **Actions mécaniques** (S2) : modèle local (pression de contact uniforme ou linéaire, passage au torseur), frottement
   visqueux, résistance au roulement et au pivotement, glisseur et couple, torseurs transmissibles 3D des liaisons.
4. **Analyse système** (S1) : lecture de diagrammes SysML dessinés (uc, req, bdd, ibd), exigences quantifiées, ACV et impact
   environnemental, chaîne de puissance au vocabulaire 2021, distinction asservi / séquentiel. `ingsys` : 4 200 signes,
   2 méthodes, 4 exercices, 10 cartes : le chapitre le plus mince au regard de son poids (début de chaque sujet).
5. **Convertisseurs** (S2) : cellule de commutation, démarche de synthèse (nature des sources → interrupteurs), onduleur et
   redresseur, schémas (cvs n'a aucune figure).
6. **Pièces plastiques et composites** (S2) : injection, mise en forme des composites, règles de conception (renvoi à ppm §6
   ou court chapitre de 1A). Règles de conception absentes aussi de deform, assemblage (soudage) et addfab.
7. Contact ponctuel (vitesse de glissement, roulement, pivotement) et fermeture géométrique traitée sur un exemple (cine §6).

## 3. Hors-programme présenté comme exigible, doublons

**Hors programme non signalé**
- `statique` : principe des travaux virtuels (cours §4, méthode 4, cartes 20-21, un exercice) ; absent du programme.
- `trsurf` (revêtements, corrosion, grenaillage) et `cnd` (ressuage, ultrasons, radiographie) : **entièrement hors du
  programme 2021** (G2 ne cite que les traitements thermiques surfaciques et le contrôle géométrique, S3), sans mention.
- `cotation` : chaîne de cotes (§4, méthode 3, 3 exercices, 2 cartes) et notation ISO « H7/g6 » ; le programme dit
  « ajustements normalisés non exigibles, seule la nature (glissant, incertain, serré) ».
- `precision` : PD, PID et Ziegler-Nichols (exercice 06 « Réglage PID complet », cartes 9, 10, 12, 13, 23), non signalés,
  et d'ailleurs du réglage de correcteur (S3-S4). `stabilite` : cartes Nyquist (9, 14), Routh (10, 24, 26), lieu des pôles
  (15) sans l'en-tête « Hors programme en PT (pour aller plus loin) : » (le cours et l'exercice 04 sont, eux, signalés).
- Culture plutôt que programme : frittage conventionnel (addfab §1), gradateur (cvs §1), Frenet et Coriolis (cine §1, §5).

**Doublons**
- `dynsolide` ↔ `energsi` : TEC, P = Cω, conservation de Em, RSG qui ne travaille pas, écrits deux fois (cours et cartes
  dyn 13, 14, 26, 27 ≈ ensi 3, 16, 1, 19). Les deux sont des versions planes et courtes (7 300 et 5 300 signes) de `dyn2a`
  et `energ2a` (2A, 37 000 et 44 000 signes), alors que le programme place toute la dynamique et l'énergétique en S3.
- cine §6 et statique §3 ↔ chaines §1, §5 : même notion, résultats contradictoires (voir §4).
- ingsys §3 ↔ schblocs §5 ↔ chfonc §1 : chaîne fonctionnelle trois fois, deux vocabulaires.
- assemblage §4 ↔ conception §3-§4 (2A) ; addfab §3 ↔ ppm §7 ; cotation §1-§3 ↔ ppm (IT, Ra) ; cartes de correcteurs de
  precision ↔ correcteurs (2A).

## 4. Qualité

**Chapitres les plus minces** (cours, signes) : trsurf 2 600, cnd 2 700, assemblage 3 400, addfab 3 400, deform 3 700,
cotation 3 900, ingsys 4 200, energsi 5 300, moulage 6 100 ; 3 méthodes et 4 exercices pour les sept chapitres de
fabrication, 2 méthodes pour ingsys. cvs : aucune figure ; dynsolide et energsi : aucune figure.

**Erreurs repérées**
- cine §4 : « **Glissière-rotule** (hélicoïdale) » : ce nom n'existe pas ; c'est la liaison hélicoïdale (glissière hélicoïdale).
- cine §6 : « Un **schéma cinématique** représente les solides comme des nœuds et les liaisons comme des arêtes » : c'est la
  définition du graphe des liaisons.
- cine §6 et carte 23 : « m = 3(n−1) − Σ(3 − DDL_i) » : cette formule donne m − h ; fausse dès qu'il y a hyperstatisme et
  incohérente avec chaines §5 (h_plan = m − I_c + 3γ).
- statique §3, méthode 3, cartes 10 et 23 : « h = inconnues − équations … **Si h < 0 : mécanisme** », puis trois lignes
  plus bas « h = m + n_inconnues − n_équations ». Contradictoire, et chaines §5 rappelle que h ≥ 0 toujours (h < 0 signale
  une mobilité oubliée). Carte 23 : « liaison isostatique / hyperstatique » (c'est le mécanisme qui l'est).
- statique §3, tableau 2D : appui plan « 3 inconnues X, Y, M_z … X le frottement » : une liaison parfaite de normale y n'a
  en plan que Y et M_z ; « Appui ponctuel : DDL = 1 » (5 en 3D, 2 en plan ; 1 est le nombre d'inconnues).
- statique §5 : équilibre « indifférent : si G est **au niveau du** pivot » (il faut : sur l'axe ; la carte 19 est juste).
- energsi, carte 15 : charge d'un circuit RL « moitié dans L, moitié dans R, quelle que soit R » : c'est le résultat de la
  charge d'un **condensateur** ; pour RL sous tension constante, R dissipe sans fin. Carte hors sujet de surcroît.
- sys2, carte 13 : « z ≈ 0,69 minimise t_r5% **sans dépassement** » : à ξ = 0,69 le dépassement vaut 5 % (le cours §2 le dit).
- ingsys exo 01 Q3 et §3 : le fin de course d'un portail est présenté comme « la boucle de retour de l'asservissement » ;
  c'est un système séquentiel (tout ou rien). Le programme demande justement de distinguer asservi et séquentiel (S1).
- ingsys carte 2 cite le diagramme de séquence (sd), absent du cours. cotation, exercice « Concours PT » : titre
  « spécification GPS » sans aucune spécification GPS ; alésage de bague de roulement ∅25 +0,010/0 (en réalité, écart négatif).

**Notations incohérentes**
- Amortissement : **z** dans les cartes de sys2 (une vingtaine) et stabilite (16), **ξ** dans les cours de 1A et en 2A.
- Chaîne « d'énergie / distribuer » (ingsys, cartes de schblocs) contre « de puissance / moduler » (cours de schblocs, 2A,
  programme).
- Cinématique : v(B ∈ S/R), torseur {V(S/R)}_A, « DDL » (cine) contre V(B, j/i), {𝒱(j/i)}, n_c, I_c (chaines) ; statique :
  {T(Σ₁ → S)}, « h = inconnues − équations » contre {𝒯(i → j)}, I_s, E_s, h = m + I_s − 6(n − 1) (chaines).
- Moment d'inertie J_Δ (dynsolide) contre I_Δ (dyn2a) ; rapport de transmission r (energsi) contre i (transm) ; f désigne le
  coefficient de Coulomb (statique) et le frottement visqueux (energsi ; f_v en 2A) ; retard noté L (carte 18 de stabilite).

## 5. Recommandations (par priorité)

1. **Corriger tout de suite les erreurs du §4** (cine §4, §6, carte 23 ; statique §3, §5, méthode 3, cartes 10 et 23 ;
   cartes energsi 15 et sys2 13 ; ingsys exo 01) et passer les cartes de sys2 et stabilite de z à ξ (retouches de texte :
   sans perte de progression selon la règle de `flashLoadState`). **Petite.**
2. **Donner à la 1ʳᵉ année la modélisation des mécanismes** : soit un chapitre 1A « Liaisons, graphe et schéma
   cinématique » (11 liaisons avec symboles et torseurs cinématiques et transmissibles 3D, classes d'équivalence, graphe,
   schéma, liaisons équivalentes, mobilité et hyperstatisme), soit rendre `chaines` visible les deux années ; aligner cine
   et statique sur ses notations. **Grande.**
3. **Réécrire `cotation` sur la GPS 2021** (principes, modèles, opérations, taille / zone / gabarit, enveloppe, références
   et liaisons, nature d'ajustement), chaîne de cotes et ISO 286 en « Pour aller plus loin ». **Moyenne.**
4. **Réécrire `ingsys`** : figures SysML à lire et compléter (uc, req, bdd, ibd), exigences quantifiées, ACV, frontière et
   flux, chaîne de puissance (alimenter, moduler…), asservi contre séquentiel ; viser 6 méthodes, 7 exercices, 25 cartes. **Moyenne.**
5. **Compléter `statique`** : modèle local et passage au global (pression), frottement visqueux, résistance au roulement et
   au pivotement, glisseur et couple, torseurs transmissibles 3D, conditions de la modélisation plane ; PTV en « Pour aller
   plus loin ». **Moyenne.**
6. **Fabrication** : encadré « Au programme » (semestre S2 ou S3) dans chaque chapitre ; trsurf et cnd marqués hors programme
   (ou repliés dans trtherm et ppm) ; règles de conception pour deform, soudage et fabrication additive ; injection
   plastique et composites (S2) en 1A ou renvoi explicite à ppm §6. **Moyenne.**
7. **Convertisseurs** : cellule de commutation, démarche de synthèse, onduleur monophasé et redresseur (S2), schémas dans
   cvs. **Moyenne.**
8. **dynsolide et energsi** : les présenter comme introductions de S3 avec renvoi à dyn2a et energ2a, dédoublonner leurs
   cartes, harmoniser J/I, r/i, f/f_v ; signaler le hors-programme de precision (PID, Ziegler-Nichols) et des cartes de
   stabilite au format convenu. **Petite.**
