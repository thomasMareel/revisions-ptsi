# Programme officiel de physique-chimie PT (2021) ↔ chapitres du site

Inventaire tenu pendant la réécriture des cours de 2ᵉ année (demande de l'utilisateur du 2026-11-13 :
« retravaille la partie cours de tous les chapitres de deuxième année […] assure-toi que tout le
programme est bien retranscrit »).

- **Source du programme** : programme de physique-chimie de la classe de PT, annexe de l'arrêté du
  13 juillet 2021 (BO n° 31 du 26 août 2021), copie hébergée par l'UPSTI
  (`upsti.fr/static/public/espace-etudiants/programmes/2021/PT/PT_PhysiqueChimie.pdf`).
  Le programme de PTSI (même arrêté) sert à délimiter ce qui est acquis en 1ʳᵉ année.
- **Manuel de référence** (dépôt privé `cours-pt-spe`, release v1, PDF de 823 pages scannées, 22 chapitres) :
  utilisé seulement pour vérifier la couverture et les notations. Rédaction du site **originale**.
- Légende des états : ✅ couvert au niveau attendu · 🔶 couvert mais à approfondir · ❌ absent.
  La colonne « après » est remplie au fil de la réécriture.

## Constat de départ (2026-11-13)

- Les 13 chapitres de physique de 2ᵉ année (hors thermochimie) font environ 30 000 signes de cours
  chacun : le contenu est juste mais il manque des démonstrations, des exemples traités, des ordres
  de grandeur et des figures. Plusieurs contiennent des notions **hors programme 2021** (formulation
  locale de la mécanique des fluides, couche limite, plasma, ARQS électrique…), héritées de
  l'ancien programme de PT.
- Des parties entières du programme de PT n'ont **pas de chapitre de 2ᵉ année** : statique des
  fluides (1.1), thermodynamique différentielle et diagrammes des fluides réels (1.2, 1.3),
  magnétostatique (4.2), cinétique électrochimique, électrolyse et corrosion (6.2 à 6.4). Certaines
  existent sous forme d'un chapitre court rangé en 1ʳᵉ année (`fluides`, `emag`, `changement`,
  `estat`), d'avant la réforme de 2021 (le programme de PTSI 2021 ne contient ni électrostatique,
  ni statique des fluides, ni théorème d'Ampère, ni diagrammes (T, s), (h, s), (log P, h)).
- **Choix retenu** : les chapitres courts de 1ʳᵉ année restent en place (aucune progression perdue) ;
  quatre chapitres de 2ᵉ année sont créés pour couvrir le programme de PT en entier.

## Correspondance programme → chapitres

| Partie du programme PT | Chapitre du site (id) | Avant | Après |
|---|---|---|---|
| 1.1 Statique des fluides (forces de pression, RFSF, atmosphère isotherme, résultante, Archimède) | **nouveau** `fluidstat` | ❌ (seulement `fluides`, 1ʳᵉ année, court) | |
| 1.2 Principes sous forme différentielle, G potentiel thermodynamique, identités thermodynamiques, potentiel chimique | **nouveau** `thermodiff` (+ `thermochimie` §2 côté chimie) | 🔶 côté chimie seulement | |
| 1.3 Diagrammes d'état des fluides réels : phases, équilibre par μ, enthalpie/entropie de changement d'état, titre, règle des moments, diagrammes (P,v), (T,s), (h,s), (log P,h), tables | **nouveau** `thermodiff` | ❌ (`changement` 1ʳᵉ année, court ; `thermoouv` §6) | |
| 1.4 Écoulement stationnaire en conduite : grandeurs eulériennes, lignes et tubes de courant, débits, conservation, laminaire/turbulent, Reynolds | `ecoulement` | 🔶 + hors programme (dérivée particulaire, tourbillon, potentiel) | |
| 1.5 Énergétique en conduite : viscosité, cisaillement, conditions aux limites, Bernoulli, pertes de charge (abaques), bilans de puissance, pompe, travail indiqué, 1ᵉʳ et 2ᵈ principes en écoulement, plusieurs entrées-sorties | `ecoulreel` (+ `thermoouv`) | 🔶 + hors programme (couche limite, traînée) | |
| 1.6 Thermodynamique industrielle : compresseur, turbine, rendement isentropique, mélangeur, séparateur, échangeur, détendeur, tuyère, cycles moteurs et récepteurs, améliorations | `thermoouv` | 🔶 | |
| 1.7 Conduction thermique 1D cartésienne : flux, loi de Fourier, bilan, équation de la diffusion, temps caractéristique, différences finies, résistance thermique, loi de Newton | `diffth` | 🔶 | |
| 2.1 Stabilité des systèmes linéaires d'ordre 1 et 2 | `ali` | 🔶 (dans la rétroaction) | |
| 2.2 Rétroaction et ALI : modèle du 1ᵉʳ ordre, saturations, vitesse de balayage, produit gain-bande, montages, impédances, comparateurs simple et à hystérésis | `ali` | 🔶 | |
| 2.3 Oscillateurs quasi-sinusoïdaux et de relaxation | `oscelec` | 🔶 | |
| 2.4 Électronique numérique : échantillonnage, Nyquist-Shannon, repliement, analyse spectrale numérique, filtrage numérique | `signum` | 🔶 | |
| 3.1 Modèle scalaire, chemin optique, Malus, lentilles, trains d'onde et largeur spectrale, détecteurs | `interf` | 🔶 | |
| 3.2 Superposition : incohérence, Fresnel, contraste, N ondes, réseau | `interf` (+ `dispinterf` §3) | 🔶 | |
| 3.3 Trous d'Young : ordre, interfrange, non-localisation, brouillage spatial et spectral | `dispinterf` | 🔶 | |
| 3.4 Michelson : lame d'air, coin d'air, localisation, lumière blanche, doublet, cohérence | `dispinterf` | 🔶 | |
| 4.1 Électrostatique (Coulomb → condensateur plan, lignes et équipotentielles, énergie potentielle, gravitation) | `estat2a` | 🔶 || ✅ réécrit le 2026-11-13 |
| 4.2 Magnétostatique : densité de courant, symétries, théorème d'Ampère, fil épais, solénoïde infini, lignes de champ | **nouveau** `magnetostat` | ❌ (`emag` 1ʳᵉ année, court) || ✅ réécrit le 2026-11-13 |
| 4.3 Maxwell : conservation de la charge, formes locale et intégrale, équations de propagation, ARQS magnétique, statique, Poisson et Laplace | `maxwell` | 🔶 || ✅ réécrit le 2026-11-13 |
| 4.4 Énergie : force et puissance volumiques, loi d'Ohm locale, effet Joule, Poynting, bilans | `maxwell` | 🔶 || ✅ réécrit le 2026-11-13 |
| 4.5 Propagation : d'Alembert, OPP, OPPM, spectre, polarisation rectiligne, polariseurs, énergie | `oemvide` | 🔶 || ✅ réécrit le 2026-11-13 |
| 4.5 Propagation : milieu ohmique et effet de peau, réflexion sur un conducteur parfait, onde stationnaire, cavité, guide entre deux plans | `oemcond` | 🔶 + hors programme (plasma, Drude) || ✅ réécrit le 2026-11-13 |
| 5.1 et 5.2 Thermochimie | `thermochimie` | ✅ (réécrit le 2026-11-11) | |
| 6.1 Thermodynamique de l'oxydoréduction | `thermochimie` §9 | ✅ | |
| 6.2 Courbes courant-potentiel | **nouveau** `electrochimie` | ❌ | |
| 6.3 Piles, accumulateurs, électrolyse (bilans, rendement faradique) | `thermochimie` §10 + **nouveau** `electrochimie` | 🔶 (piles seulement) | |
| 6.4 Corrosion, protection, passivation | **nouveau** `electrochimie` | ❌ | |
