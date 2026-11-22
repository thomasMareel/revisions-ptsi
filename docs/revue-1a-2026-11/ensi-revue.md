# `energsi` (prefix `ensi`) « Énergétique des systèmes » — chapitre réécrit (SI, 1ʳᵉ année, vu en avance), 2026-11-22

Demande : point 4 de l'audit du 2026-11-14, lot 8 (`docs/audit-2026-11/si-1a.md` : anticipations de S3, doublon avec
`dynsolide`, aucune figure, carte 15, notations r/i et f/f_v). Programme : `pdf-pt/prog/si.txt`, C2 (S3) « énergie
cinétique ; inertie et masse équivalentes ; puissance d'une action mécanique extérieure ; puissance intérieure à un ensemble
de solides ; théorème de l'énergie cinétique ; rendement en régime permanent » et C1 (S3) « PFD ou TEC ». Chapitre **vu en
avance** : bloc « AU PROGRAMME · PTSI » + encadré « Vu en avance (2ᵉ année) » ; renvois à `energ2a` (3D, rendement inverse,
couple thermique), `dynsolide` (inerties, PFD), `transm` (rapports, rendement, réversibilité), `mcc`, `energie` et `mvtsolide`
(physique).

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `ensi-cours.src.html` | cours réécrit (≈ 79 000 car. de HTML, ≈ 39 000 signes de texte ; ancien : 6 600) : bloc programme, 10 sections, « Pour aller plus loin · 2ᵉ année », 13 exemples traités chiffrés, 5 figures calculées |
| `ensi-meth.src.html` | 10 méthodes + pièges (ancien : 3 méthodes) |
| `ensi-exos.src.html` | 11 exercices + 1 « Concours PT » en 5 parties (9 questions) (ancien : 6 + concours de 2 questions) |
| `ensi-cartes-corr.json` | 4 réponses corrigées (question inchangée) |
| `ensi-cartes-ajout.js` | 14 cartes ajoutées en fin de deck (25 → 39) |
| `ensi-cours.tpl.html`, `ensi_figs.py` → `ensi_figs.json` | gabarit et figures (assemblés par `dyn_construire.py`, primitives `dyn_svg.py`) |
| `ensi_calculs.py`, `ensi_calculs_exos.py`, `dyn_calculs_meth.py` (partie `ensi`) | vérification de tous les exemples, éclairs et corrigés |
| `ensi_cartes_actuelles.json`, `dyn_cartes.py`, `dyn_cartes_rendu.js` | cartes actuelles, écriture des corrections, rendu des cartes |
| `ensi_orig_{cours,meth,exos}.html` | copie des anciens panneaux |

## Erreurs et faiblesses corrigées

1. **Anticipation S3 non signalée** : bloc programme, encadré « Vu en avance ».
2. **Doublon avec `dynsolide`** (TEC, \(P = C\omega\), \(E_m\), roulement qui ne travaille pas) : ici énergie cinétique,
   puissances, TEC, inertie et couple ramenés, rendement, cycle ; les inerties et le PFD sont dans `dynsolide` (renvois
   croisés ; le cylindre sur plan incliné est traité ici par le TEC et là-bas par le PFD, avec la condition d'adhérence).
3. Ancien §4 : réducteur « \(r = \Omega_s/\Omega_e\) » contre \(i\) dans `transm` : notation \(i\) partout (signalé « \(k\) en
   2ᵉ année »). Frottement visqueux « \(f\) » → \(c\) en translation, \(f_v\) en rotation (comme `statique` et `energ2a`).
4. Ancien §3 : « liaisons avec frottement… travail négatif » sans définition de la liaison parfaite ni du rôle du mouvement
   relatif ; ancien §1 « la puissance des inter-efforts entre solides différents contribue » sans formule : §3 réécrit
   (puissance des actions mutuelles, démonstration, moteur placé entre deux pièces mobiles).
5. **EXO 02** : Q2 « Comparer \(J_m\) et \(J_c/r^2\) … \(J_c/r^2 = 0{,}08\) » : faux (\(J_c/r^2 = 50\)) ; c'est \(J_c\,i^2\). Corrigé.
6. **EXO 03** : constante de temps de l'énergie « \(\tau_E = 1/(\xi\omega_0) = 1\ \text{s}\) » alors que \(E_m \propto
   e^{-2\xi\omega_0 t}\) : \(\tau_E = 1/(2\xi\omega_0) = 0{,}5\ \text{s}\) (1 s est celle de l'amplitude). Corrigé ; \(f\) → \(c\).
7. **EXO 04** : « irrégularités de couple » → irrégularités de **vitesse** à couple constant (inertie variable).
8. Ancien « Concours PT » (2 questions, ★★) gardé en EXO 07 ; nouveau sujet concours.

## Couverture du programme (S3) : avant → après

| Capacité | Avant | Après |
|---|---|---|
| Énergie cinétique d'un solide, d'un ensemble (C2) | §2 (formule) | §1 (trois cas, König démontré, volant, chariot) |
| Puissance d'une action extérieure (C2) | §1 (force, couple) | §2 (force, couple, torseur au même point, poids, vérin \(pQ_v\), travail ; barrière levante) |
| Puissance intérieure (C2) | une phrase | §3 (actions mutuelles, liaison parfaite, sec, visqueux, roulement, actionneur interne ; VTT en descente, robot à deux bras) |
| Énergie potentielle, énergie mécanique | §5 (ressort, amortisseur) | §4 (pesanteur, ressorts, conservation ; essai de résilience au mouton-pendule, figure) |
| Théorème de l'énergie cinétique (C2) | §3 | §5 (solide, ensemble, démonstration depuis le PFD, portée ; presse à volant, treuil) |
| Inertie et masse équivalentes (C2) | §2 (une formule) | §6 (tableau des contributions, convoyeur, rotor vu de la charge, bielle-manivelle ; 2 figures calculées) |
| Couple résistant ramené, loi de mouvement (C2) | §3 | §7 (égalité de puissance, modèle équivalent, moteur à courant continu ; portail coulissant) |
| Rendement en régime permanent (C2) | §4 (définition, produit) | §8 (pourquoi le régime permanent, tableau d'ordres de grandeur, sens du flux ; monte-charge, figure du flux de puissance) |
| Couple et puissance sur un cycle | ❌ | §9 (couple avec pertes amont/aval, élévateur à vis, figure calculée ω, C, P) |
| PFD ou TEC (C1) | ❌ | §10 (tableau, cylindre sur plan incliné) |
| Comoment 3D, rendement inverse, couple thermique, adaptation d'inertie, \(J_{eq}(q)\) | ❌ | « Pour aller plus loin » (renvoi `energ2a`) |

## Contenu

**Méthodes (10).** Énergie cinétique d'un ensemble ; puissance extérieure ; puissances intérieures ; équation du mouvement par
le TEC ; forme intégrée ; inertie ramenée ; effort ramené et modèle équivalent ; rendements ; dimensionner sur un trapèze ;
TEC ou PFD ; pièges.

**Exercices (12).** 01 moteur et réducteur (★) ; 02 inertie équivalente (★★, corrigé) ; 03 oscillateur amorti (★★, corrigé) ;
04 bielle-manivelle (★★) ; 05 rendement global (★★) ; 06 démarrage du premier ordre (★★★) ; 07 treuil (★) ; **nouveaux** :
08 course de solides roulants (★★) ; 09 freinage d'une voiture, puissance intérieure et échauffement des disques (★★) ;
10 axe vertical à vis à billes, masse équivalente de 1 470 kg (★★) ; 11 convoyeur pas à pas, énergie par phase et freinage
du moteur (★★★) ; Concours PT « Monte-charge à pignon et crémaillère » (moteur embarqué = puissance intérieure, \(J_{eq}\),
montée avec pertes, descente avec \(\eta'\), effort sur la crémaillère par le PFD).

## Cartes (25 → 39)

Corrigées (réponse seule) : 2 (« RSG sans frottement » : le roulement sans glissement exige l'adhérence) ; 7 (« vite
décroissant avec r » : c'est l'inverse, \(J_c\,i^2\) croît avec \(i\) ; notation \(i\)) ; 11 (« puissance dissipée
\(= -f\dot x^2\), toujours négative » : signe ; la force a une puissance \(-f\dot x^2\), l'amortisseur dissipe \(f\dot x^2\)) ;
21 (hacheur : « pas de chute de tension continue » → \(u\,i = 0\) pour un interrupteur parfait). Carte 15 (circuit RL),
déjà corrigée auparavant, est juste mais hors sujet : gardée (pas de retrait possible). Doublons avec `dynsolide` (1, 3, 16, 19)
gardés, justes. Ajoutées (14) : König, puissance d'un torseur, actions mutuelles, moteur entre deux pièces, ressort de
torsion, contributions \(m(Ri)^2\) et \(m(pi/2\pi)^2\), effort ramené, modèle équivalent et \(\tau = J_{eq}/b\), régime
permanent, couple avec pertes amont/aval, ordres de grandeur des rendements, charge entraînante (\(\eta'\)), tension d'un câble
(PFD et non TEC). Rendu vérifié : aucune erreur MathJax.

## Contrôles

`verif_src.py` sans erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges` vides, aucune
erreur JS (cours, méthodes, exercices) ; figures en clair et en sombre (`dyn_voir/`) ; `corriger_cartes.py --essai`
(4 corrigées) et `ajouter_cartes.py --essai` (25 → 39) sans erreur.

## Doutes

- Le §9 donne la formule exacte « pertes en aval seulement » (\(J_{amont}\dot\omega + (J_{aval}\dot\omega + C_{r,eq})/\eta\)),
  reprise de `energ2a` §8 ; c'est un peu au-delà d'une introduction, mais plus juste que « tout divisé par \(\eta\) » (écart
  chiffré dans la notice).
- Ordre du groupe Mécanique : voir `dyn-revue.md` (placer `energsi` juste après `dynsolide`).
