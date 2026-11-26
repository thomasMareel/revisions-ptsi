# Revue `mcc` — « Machine à courant continu » (point 7 de l'audit, 2026-11-26)

Livrables (AN1/) : `mcc-cours.src.html` (gabarit `mcc-cours.tpl.html` + `mcc_figs.json`, assemblés par
`mcc_construire.py`), `mcc-meth.src.html` (gabarit `mcc-meth.tpl.html`), `mcc-exos.src.html` (gabarit
`mcc-exos.tpl.html`), `mcc-cartes-corr.json`, `mcc-cartes-ajout.js`. Scripts : `mcc_figs.py` (figures calculées,
scipy `solve_ivp` pour les réponses temporelles), `mcc_calculs.py` (exemples du cours), `mcc_calculs_meth.py`,
`mcc_calculs_exos.py` (anciens et nouveaux exercices), `mcc_exo11_euler.py` (code de l'exercice 11, exécuté),
`mcc_cartes.py`, `mcc_voir.py`, `mcc_cartes_rendu.js`. Panneaux `-simu` et `-flash` non touchés (pas de `-video`).

Contrôles passés : `verif_src.py` sur les trois panneaux (aucune erreur ni « attention ») ; `apercu_src.py` à 390 et
1440 px pour cours, méthodes et exercices : `merr`, `brut`, `larges` vides, aucune erreur JS ; figures regardées en
clair et en sombre (`mcc_voir.py`) et dans la page (captures 1440) ; `corriger_cartes.py --essai` (3 réponses) et
`ajouter_cartes.py --essai` (33 → 46 cartes) ; rendu MathJax des cartes nouvelles et corrigées sans erreur.

## Programme : ce qui est en PTSI et ce qui est en PT

Vérifié dans `si.txt` : la ligne « Modéliser un convertisseur électromécanique » (modèle électromécanique de la MCC,
modèles des machines synchrone et asynchrone, bilan des puissances) est au **semestre S4** ; « Commande des machines
en couple et en vitesse » aussi (S4) ; rendement en régime permanent, inertie et masse équivalentes, ondulation dans
les convertisseurs : **S3**. En 1ʳᵉ année (S1-S2) : chaînes fonctionnelles, fonctions alimenter / moduler / convertir
(A3, S1), grandeurs d'effort et de flux (D1, S2), modèle de connaissance par fonction de transfert et schéma-blocs
(B2, S1), réponse temporelle (C2, S1), modèle de comportement et choix des entrées pour l'identifier (B2, D2, S2),
convertisseurs statiques et réversibilité (B2, S2). En physique de PTSI (1.7.5) : moteur à courant continu à entrefer
plan analysé à partir des rails de Laplace, équations électrique et mécanique, bilan énergétique, exemples
d'utilisation. Le bloc « AU PROGRAMME · PTSI » le dit tel quel, avec un paragraphe « Vu en avance (2ᵉ année) » sur le
modèle S4 (comme `energsi`, `assemblage`) : ses équations sont celles de la physique de PTSI et la MCC est l'exemple
type des modèles d'ordre 1 et 2 ; `machalt` (2ᵉ année) en fait le rappel au §9. Hors programme (fin de cours) :
formule d'Arnold, excitation et défluxage, réaction d'induit, commutation (« la physique des convertisseurs
électromécaniques n'est pas au programme »).

## Erreurs et défauts corrigés

| Où | Avant | Après |
|---|---|---|
| Cours §3 | formule d'Arnold au cœur du modèle, \(K\) = constante d'Arnold et \(k_E = k_T = K\Phi\) | \(E = K\Omega\), \(C_{em} = KI\) (notation de `machalt`, `ingsys`, `multiphy`, `induction`) ; égalité des constantes démontrée par \(P_L + ei = 0\) (renvoi `induction` §8) ; Arnold en « Pour aller plus loin » |
| Cours §1, §5 | \(C_m\) pour le couple **utile** (ailleurs \(C_m = Ki\)) ; « \(P_f = C_{frot}\Omega\) » puis « \(P_f\) désigne \(P_c\) » | \(C_u\) couple utile, \(P_c\) pertes collectives, couple de pertes \(C_p = C_{em} - C_u\) |
| Cours §2 | « règle des 3 doigts » sans la main ; \(e = -\mathrm d\phi/\mathrm dt\) sans convention ; f.c.é.m. non nommée | main droite ; convention générateur comme `induction` ; force contre-électromotrice \(E\) en convention récepteur |
| Figure de l'induit | flèche de \(U\) à deux pointes, \(E\) sans flèche, légende « \(E = k\Omega\) » | figure redessinée : \(u\), \(i\), \(Ri\), \(L\,\mathrm di/\mathrm dt\), \(e = K\Omega\) en convention récepteur |
| Cours §4 | une seule ligne de Laplace trop large (défilait à 1440 px) | trois formules |
| Méthode 6 | premier ordre sans condition sur \(\tau_e\) | critère \(\tau_m \gg \tau_e\) ; \(\omega_0\), \(\xi\), dépassement si \(\tau_m \lt 4\tau_e\) |
| Exercice 05 (HP) | \(E = K\Phi\,\Omega\) avec \(K\) d'Arnold | \(K = K_n\Phi/\Phi_n\) ; calculs inchangés (vérifiés) |
| Exercice 06 | \(V_0\), gain \(K_0\), \(k\) | \(U_0\), \(K_s\), \(K\) ; renvoi au critère \(\tau_m \lt 4\tau_e\) du cours |
| Carte 6 (Arnold) | non signalée hors programme ; « (p/2πa) » ambigu ; « = K·Φ·Ω » | réponse préfixée « Hors programme en PTSI : », écrite en \( \) |
| Carte 7 | « k_E = K·Φ » (contredit la nouvelle notation) | \(E = K\Omega\), \(K\) notée aussi \(k\) ou \(k_E\) |
| Carte 24 | « 5 à 10 fois » le courant nominal (l'exercice 03 donne près de 15 fois) ; « redresseur commandé » (hors programme, cf. `cvs`) ; rendu `flashPretty` cassé (« R : I_dem ») | « souvent 5 à 20 fois » ; rampe du rapport cyclique ou boucle de courant ; réponse en \( \) |

Tous les calculs des anciens exercices (01 à 06, Concours) ont été refaits : aucun résultat faux (`mcc_calculs_exos.py`).

## Couverture avant → après

| Capacité | Avant | Après |
|---|---|---|
| Chaîne de puissance, convertir / moduler, effort et flux (A3 S1, D1 S2) | absent | §1 (visseuse chiffrée), §8 ; exo 07 ; carte |
| Principe : Laplace, Faraday, rails, conversion parfaite (physique 1.7.5) | §2 qualitatif | §2 + exemple « d'où vient \(K\) » (100 conducteurs → \(K = 0{,}060\)) ; démonstration \(K_E = K_T\) au §3 |
| Équations électrique et mécanique, conventions (physique 1.7.5) | §3 | §3 + point de fonctionnement chiffré du moteur de référence |
| Schéma-blocs, fonction de transfert (B2 S1) | §4 (liste) | §4 figure du schéma-blocs ; §6 réduction, forme canonique, démonstration |
| Quatre quadrants, réversibilité de l'alimentation (B2 S2) | §4 | §4 figure calculée (réseau de droites, quadrants), exemple de la charge retenue (Q4) ; §8 tableau quadrants → hacheur ; exo 10 |
| Bilan énergétique, rendement | §5 | §5 + figure \(\eta(I)\), maximum pour \(RI^2 = P_c\), ordres de grandeur |
| Réponse à un échelon, ordre 1 ou 2 (C2 S1, B2 S2) | une ligne au §4 | §6 : \(\tau_e\), \(\tau_m\), \(\omega_0\), \(\xi\), critère \(\tau_m \geq 4\tau_e\), figure calculée ordre 1 / ordre 2, énergie du démarrage ; exo 11 (Euler) |
| Point de fonctionnement avec une charge | méthode 3 | §7 : charges usuelles, stabilité, figure, ventilateur, charge ramenée (renvoi `energsi`) ; exo 09 |
| Association hacheur-MCC (B2 S2) | exo 06 seulement | §8 : \(\alpha U_0 = K\Omega + R\langle i\rangle\), choix du hacheur, ondulation (renvoi `hacheurs` §5), démarrage en rampe (figure) ; méthodes 9, 10 ; exos 09, 10 |
| Identifier un modèle, choisir entrées et sorties (B2, D2 S2) | absent | §9 : tableau des essais, exemple complet ; méthode 8 ; exo 08 (courbe relevée) |
| Documentation, ordres de grandeur, exemples d'utilisation | méthode 7 | §10 : conversions, fiche vérifiée, point de service, tableau d'ordres de grandeur, utilisations |
| Hors programme (Arnold, excitation, défluxage) | Arnold au §3 | « Pour aller plus loin » ; exo 05 signalé |

## Ce qui a été ajouté

- **Cours** : bloc « AU PROGRAMME · PTSI » ; §1 à §5 gardés (même numérotation, mêmes titres), complétés d'un exemple
  chiffré chacun ; nouvelles sections **§6** réponse à un échelon (ordre 1 ou 2), **§7** point de fonctionnement avec
  une charge, **§8** alimentation par un hacheur, **§9** identification par essais, **§10** documentation, ordres de
  grandeur et utilisations ; « Pour aller plus loin · hors programme ». 13 exemples traités, tous calculés avec un
  même **moteur de référence** (24 V, \(R = 1{,}2\ \Omega\), \(L = 1{,}5\ \text{mH}\), \(K = 0{,}060\),
  \(J = 4\times10^{-5}\)) quand c'est possible. 8 figures, dont 6 calculées (coupe de la machine, induit,
  schéma-blocs, caractéristiques et quadrants, rendement, réponse indicielle ordre 1/2, démarrage en rampe,
  points de fonctionnement).
- **Méthodes** : 7 → 10 (8 identifier par essais, 9 régler la vitesse par un hacheur, 10 limiter le courant de
  démarrage) ; les 7 anciennes gardées, alignées (\(K\), \(C_u\)), méthode 6 complétée.
- **Exercices** : 7 → 12 (EXO 07 fauteuil roulant, chaîne de puissance ★ ; EXO 08 identification par trois essais
  avec courbe relevée de 330 unités de large ★★ ; EXO 09 ventilateur d'habitacle, hacheur contre résistance série
  ★★ ; EXO 10 monte-charge, quadrants et convertisseur réversible en tension ★★ ; EXO 11 micromoteur du deuxième
  ordre et Euler ★★★, code exécuté). Les 6 anciens et le Concours PT gardés (numéros inchangés : le cours renvoie à
  l'exercice 04 et à l'exercice 05).
- **Cartes** : 3 réponses corrigées (6, 7, 24) ; 13 ajoutées à la fin (fonction convertir, \(\tau_e\)/\(\tau_m\),
  critère sans dépassement, rendement maximal, relation hacheur, hacheur réversible en courant, convertisseur du
  treuil, mesure de \(R\) et \(K\), inertie par la réponse indicielle, démarrage en rampe, énergie du démarrage
  direct, conversions de catalogue, ordres de grandeur).

## Notations

\(u, i, e\) variables, \(U, I, E\) en régime permanent ; \(E = K\Omega\), \(C_{em} = KI\) (comme le rappel de
`machalt` §9) ; \(C_r\), \(C_u\), \(J\), \(f\) ; \(\tau_e = L/R\), \(\tau_m = RJ/K^2\), gain statique \(K_s\) ;
\(\omega_0\), \(\xi\), \(t_{r5\%}\) (comme `sys1`, `sys2`) ; plan \((C_{em}, \Omega)\), couple en abscisse ; source du
hacheur \(U_0\), rapport cyclique \(\alpha\), \(f_d\).

## Doutes et suites à donner

- **\(K\) ou \(k\)** : le cours, les méthodes, les exercices et les cartes nouvelles écrivent \(K\) (demande de la
  coordination, notation de `machalt`, `ingsys`, `multiphy`, `induction`). Restent en \(k\) : le simulateur (curseur
  « k (V·s/rad) »), les 30 premières cartes du deck, `cvs` (§3, §8 : \(k\), \(E_m\)) et `sys1` (§1, où \(K\) est le
  gain statique). Le cours le signale dans ses notations. À aligner plus tard si l'on veut (`cvs` surtout).
- **Source du hacheur** : \(U_0\) ici (car \(E\) est la f.é.m.), \(E\) dans `cvs` et le simulateur de `hacheurs` (où la
  f.é.m. devient \(E_m\)). Le §8 le dit.
- Le §8 et l'exercice 09 renvoient à « Les hacheurs », §2 à §5 (§5 = ondulation du courant) : numérotation vérifiée
  dans la réécriture de `hacheurs` (`hach-revue.md`).
- Table des ordres de grandeur (§10) : valeurs typiques, volontairement larges (aucune fiche de marque recopiée ; la
  fiche du §10 est inventée et cohérente).
