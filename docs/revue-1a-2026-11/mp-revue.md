# Revue du chapitre `mecpt` (prefix `mp`) — « Méca du point — Principes de la dynamique » — 2026-11-21

Objet (point 4 de l'audit, lot 5 ; `docs/audit-2026-11/physique-1a.md` l. 40, 85, 107, 120, 154 ; `audit-2026-11.md` §5) :
chapitre mince (5 300 signes de cours, 14 cartes) ; ni système de points, ni \(\vec p=m\vec v(G)\), ni conservation de la
masse ; vitesse limite en exercice seulement ; pas d'équation adimensionnée ni de simulation ; lois de Coulomb (programme de
SI) au cœur du §2 ; force de Lorentz redondante avec `lorentz`. Programme : PTSI 2021, partie 2.2
(`pdf-pt/prog/ptsi.txt`, l. 968-1017) et annexe 3 (méthode d'Euler, ordre 2 en système d'ordre 1).

## Fichiers produits (dans `AN1/`)
- `mp-cours.src.html` (79 ko ; 43 100 signes de texte avec les légendes, contre 5 300) — assemblé par `mp_construire.py`
  depuis `mp-cours.tpl.html` et `mp_figs.json` ;
- `mp-meth.src.html` (10 méthodes), `mp-exos.src.html` (11 exercices + 1 « Concours PT ») ;
- `mp-cartes-corr.json` (2 réponses corrigées), `mp-cartes-ajout.js` (15 cartes) ;
- scripts : `mp_figs.py` (5 figures, outils de `cpt_svg.py`), `mp_calculs.py` (exemples du cours), `mp_calculs_meth.py`,
  `mp_calculs_exos.py`, `mp_euler.py` (**code du §10 exécuté** : chute du parachutiste, validation sur le modèle linéaire,
  stabilité, `euler_ordre2`, balle de tennis, contrôle par `odeint`), `mp_concours.py` (volant de badminton, code de la
  partie D exécuté), `mp_tester_code.py` (exécute tout le code affiché), `mp_retouches_exos.py`, `mp_voir.py` ; copies des
  anciens panneaux `mp_orig_{cours,meth,exos}.html`.

## Erreurs trouvées et corrigées
| Où | Problème | Correction |
|---|---|---|
| §1 et carte 0 (audit, erreur n° 4) | « géocentrique galiléen pour des durées ≪ 1 jour » | **déjà corrigé** dans le dépôt (≪ 1 an, terrestre ≪ 1 jour) ; repris au §2 avec les accélérations en cause et une notice « Erreur classique » sur cette confusion, méthode 2, EXO 04, carte d'ordres de grandeur |
| Ancien §3 et carte 4 | « \(\sum\vec F=\mathrm{d}\vec p/\mathrm{d}t\) … utile avec une masse variable » : faux pour un système ouvert (fusée) | §1, §4 : la loi porte sur un **système fermé** ; notice ; EXO 11 (wagon qui se remplit) montre l'erreur ; « Pour aller plus loin » sur la fusée ; carte 4 corrigée par sa réponse |
| Ancien EXO 03 (demi-sphère), Q2 | projection radiale aux signes inversés (« poids \(+mg\cos\theta\), réaction \(-N\) » sur \(\vec e_r\) sortant), qui ne mène pas au résultat écrit | projection refaite : \(-mR\dot\theta^2=N-mg\cos\theta\), d'où \(N=mg(3\cos\theta-2)\) (EXO 09) |
| Ancien §2 | lois de Coulomb (SI) présentées dans le corps du cours | réaction \(\vec R=\vec N+\vec T\) avec \(N\geq0\) ; Coulomb en « Pour aller plus loin », renvoi à SI `statique` §10-11 ; ancien « Concours » du plan incliné gardé comme EXO 05 titré « lois de Coulomb, vues en SI » |
| Ancien §2 | force de Lorentz redonnée | une ligne du tableau des forces, renvoi au chapitre `lorentz` |
| Carte 10 | Frenet avec \(R\) (rayon de courbure) | \(\rho\), comme `cinept` (réponse seule) |

Les deux anciens « Concours PT » (plan incliné, looping) deviennent EXO 05 et EXO 10 : un seul « Concours PT » par chapitre.

## Couverture du programme : avant → après
| Capacité exigible (2.2) | Avant | Après |
|---|---|---|
| Conservation de la masse d'un système fermé | absent | §1 (définition, notice), §4, EXO 11, carte |
| \(\vec p\) d'un système ; \(\vec p=m\vec v(G)\) pour deux points | \(\vec p=m\vec v\) d'un point | §1 (démonstration, wagons, Terre-Lune), §4 (théorème du centre de masse démontré, patineurs), méthode 4, EXO 01, 2 cartes |
| Principe d'inertie ; mouvement relatif de deux référentiels galiléens | liste des référentiels | §2 (translation rectiligne uniforme, train qui roule puis freine, tableau des accélérations, pendule de Foucault), méthode 2, EXO 04, 2 cartes |
| Bilan des forces sur un ou plusieurs systèmes, schéma ; troisième loi | énoncé | §3 (tableau des forces, livre sur la table, figure des deux blocs), §4 (deux blocs, ascenseur), §6 (Atwood), méthode 1, EXO 02, carte |
| Équations du mouvement d'un point ou du centre de masse | énoncé + méthode | §4 (méthode, trois exemples), méthodes 3, 5, tous les exercices |
| Gravitation, champ de pesanteur uniforme, chute sans frottement | \(\vec P=m\vec g\) | §5 (loi de Newton, \(g_0=GM_T/R_T^2\), validité, ISS), §7 (plongeon, contrôle du frottement), carte |
| Frottement fluide : modèles, résistance de l'air sur une chute | deux formules | §8 (Reynolds, Stokes, \(\beta=\tfrac12\rho C_xS\), tableau des fluides, brouillard et tennis, mesure), méthode 7, EXO 06 (mesure de viscosité), 2 cartes |
| Exploiter l'équation sans la résoudre : ordres de grandeur, vitesse limite, simulation ; équation adimensionnée | absent (vitesse limite en exercice) | §9 (vitesses limites, \(\tau=v_{\text{lim}}/g\), équations adimensionnées, figure calculée, tableau, parachutiste), méthode 8, EXO 07, concours B-C, 3 cartes |
| Méthode d'Euler (annexe 3) | absent | §10 (même fonction `euler` que `pynum` et `premierordre`, validation, stabilité, `euler_ordre2`, vecteur d'état numpy pour un mouvement plan, figure calculée), méthode 9, EXO 07 Q4, concours D, carte |
| Tension d'un fil ; pendule simple, analogie avec l'oscillateur harmonique | absent du cours (méthode et exercice) | §6 (fil idéal, poulie, Atwood), §11 (mise en équation, tension, approximation linéaire et validité, intégrale première, exemple chiffré), méthode 10, EXO 08, carte ; renvoi à `oscill` pour les oscillations |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 11 sections + « Pour aller plus loin ») : §1 Système, masse, quantité de
mouvement ; §2 Référentiels galiléens ; §3 Forces et troisième loi ; §4 Principe fondamental ; §5 Gravitation et poids ;
§6 Réaction, tension, ressort ; §7 Champ de pesanteur uniforme ; §8 Frottement fluide ; §9 Vitesse limite et équation
adimensionnée ; §10 Méthode d'Euler ; §11 Pendule simple ; hors programme : Coulomb (SI), systèmes ouverts, référentiels non
galiléens. 17 exemples traités chiffrés, 11 notices, 5 tableaux, 2 démonstrations dépliables, 2 programmes Python testés,
5 figures SVG calculées (deux blocs et troisième loi ; plan incliné ; pendule ; vitesse adimensionnée linéaire et
quadratique ; trajectoire d'une balle de tennis avec et sans frottement, calculée par Euler), vérifiées en clair et en sombre.

**Méthodes** (10) : bilan des forces ; référentiel galiléen ; projeter le principe fondamental ; quantité de mouvement ;
force de contact inconnue ; ressort ; modèle de frottement et vitesse limite ; adimensionner ; Euler ; pendule. L'ancien
« algorithme en 4 réflexes » et les pièges sont repris (méthodes 1, 3 et notices).

**Exercices** (12) : 01 barque (centre de masse fixe) ; 02 attelages d'un train ; 03 frottement linéaire (ancien 01) ;
04 référentiel galiléen ? ; 05 plan incliné avec Coulomb (ancien concours) ; 06 mesure de la viscosité de la glycérine
(Stokes, Archimède fourni, Reynolds, régression) ; 07 parachutiste (adimensionnement, tableau de simulation, Euler à la main,
ouverture de la voile) ; 08 pendule (ancien 02, tension ajoutée) ; 09 demi-sphère (ancien 03, **corrigé**) ; 10 looping (ancien
concours) ; 11 wagon qui se remplit de sable (système fermé) ; **Concours PT « Le volant de badminton »** (A sans frottement :
94 m ; B \(\beta\), \(C_x\approx0{,}53\), Reynolds, équation adimensionnée ; C début du vol par séparation des variables,
« mur » de 7 m ; D simulation : 9,31 m, chute finale à 83°, contrôle du pas ; angle optimal 24°).

**Cartes** : 14 → 29 (15 ajoutées à la fin : conservation de la masse, \(\vec p=m\vec v(G)\), centre de masse, référentiels
galiléens entre eux, ordres de grandeur des accélérations, poids et réaction, gravitation, réaction, tension, vitesse limite,
équation adimensionnée, Reynolds, vitesses limites usuelles, Euler, pendule). Rendu MathJax : 0 erreur.

## Contrôles
`verif_src.py` sans erreur ni attention sur les trois panneaux ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`,
`larges` vides, aucune erreur JS ; `corriger_cartes.py --essai` (2 réponses) et `ajouter_cartes.py --essai` (14 → 29) sans
erreur ; tout le code affiché exécuté (`mp_tester_code.py`).

## Notations
\(\vec P=m\vec g\) ; \(\vec R=\vec N+\vec T\) (réaction) ; \(\vec T\) tension d'un fil ; \(-k(\ell-\ell_0)\vec u\) ;
\(-\alpha\vec v\) et \(-\beta\|\vec v\|\vec v\) (comme les anciennes cartes 6-7), \(\beta=\tfrac12\rho C_xS\) ; \(v_{\text{lim}}\),
\(\tau=v_{\text{lim}}/g\), \(u\), \(s\) ; \(\omega_0=\sqrt{g/\ell}\), \(T_0\) ; fonction `euler(F, t0, y0, h, n)` identique à
`pynum` et `premierordre`.

## Doutes, remarques pour l'intégration
- **Titre** : « Méca du point — Principes de la dynamique » ; le cours et `cinept` l'appellent « Principes de la dynamique ».
  Proposition : « Principes de la dynamique : lois de Newton » (mobLabel inchangé).
- **Ordre du groupe Mécanique** : `oscill` (pendule simple, §4) vient après `mecpt`, qui établit maintenant l'équation du
  pendule (§11) ; `oscill` §4 peut renvoyer au §11 au lieu de refaire la mise en équation.
- La poussée d'Archimède (2ᵉ année) est donnée par l'énoncé de l'EXO 06 et citée dans la méthode 7.
- Les lois de Coulomb restent présentes (fin de cours, EXO 05, carte 8), signalées « vues en SI ».
