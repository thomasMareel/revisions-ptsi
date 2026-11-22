# Revue du chapitre `mvtsolide` (prefix `msol`) — « Mouvement d'un solide » — 2026-11-22

Objet (point 4 de l'audit, lot 6 ; `docs/audit-2026-11/physique-1a.md` l. 45, 70, 106, 111, 138, 154 ; `audit-2026-11.md` §5) :
chapitre mince (4 800 signes de cours, 2 méthodes, 3 exercices, 18 cartes) ; doublon partiel avec `mcinc` §2 ; tableau de J
différent de celui de `mcinc` ; capacité numérique « non-isochronisme du pendule pesant » absente ; étude énergétique du pendule
(diminution de l'énergie mécanique) absente ; justification du moment d'une liaison pivot absente. Programme : PTSI 2021,
partie 2.7 (`pdf-pt/prog/ptsi.txt`, l. 1382-1450).

## Fichiers produits (dans `AN1/`)
- `msol-cours.src.html` (≈ 90 ko, `mcin_construire.py msol` depuis `msol-cours.tpl.html` et `msol_figs.json`) ;
- `msol-meth.src.html` (10 méthodes), `msol-exos.src.html` (11 exercices + 1 « Concours PT ») ;
- `msol-cartes-corr.json` (1 réponse précisée), `msol-cartes-ajout.js` (14 cartes) ;
- scripts : `msol_figs.py` (5 figures), `msol_calculs.py`, `msol_calculs_exos.py`, `msol_code.py` et `msol_tester_code.py`
  (**tout le code affiché est exécuté** : périodes du §7, énergie du §9, boucle de l'EXO 08), `msol_retouches*.py` ; copies des
  anciens panneaux `msol_orig_{cours,meth,exos}.html`.

## Erreurs et défauts corrigés
| Où | Problème | Correction |
|---|---|---|
| Figure du pendule pesant | libellé « m g⃗ » avec la flèche combinante U+20D7 (carré à l'écran), libellés à 10 px, figure dessinée à la main | figure recalculée, vecteurs en gras, bras de levier \(d\sin\theta\), action du pivot |
| Tableau des moments d'inertie | différent de celui de `mcinc` | un seul tableau (ici, §3), « fourni » ; `mcinc` n'en a plus |
| Liaison pivot | « exerce un moment nul » sans justification ; carte 6 « elle n'intervient pas dans le TMC » ambiguë (sa résultante n'est pas nulle) | §4 : forces de contact radiales sans frottement (figure), couple résistant avec frottement ; carte 6 précisée (réponse seule) |
| Non-isochronisme | une phrase | §7 : simulation `odeint` exécutée, tableau \(T/T_0\) jusqu'à 170°, comparaison à Borda, figure calculée |
| Diminution de l'énergie mécanique (capacité exigible) | absente | §9 : \(\mathrm dE_m/\mathrm dt=-\lambda\dot\theta^2\), simulation et figure, mesure de \(Q\) |
| Équivalence théorème du moment cinétique / énergie cinétique | absente | §8 : démonstration |

Aucune carte fausse ; les anciens exercices (tige, treuil, barre) sont gardés et complétés (EXO 04, 05, concours).

## Couverture du programme (partie 2.7) : avant → après
| Capacité exigible | Avant | Après |
|---|---|---|
| Solide / système déformable ; translation rectiligne et circulaire | encadré | §1 (figure translation circulaire / rotation, grande roue), méthode 1, EXO 01, carte |
| Rotation : trajectoire et vitesse d'un point | une ligne | §2 (disque dur, ordres de grandeur), méthode 2, EXO 01-02 |
| \(L_\Delta=J\omega\), \(J\) fourni, lien qualitatif avec la répartition des masses | formule et tableau | §3 (rayon de giration, anneau/disque, Terre \(0{,}33MR^2\)), méthode 3, EXO 03, 2 cartes |
| Couple ; liaison pivot et moment qu'elle peut produire | une phrase | §4 (poids « en G » démontré, couple \(\Gamma\), pivot parfait justifié, frottement solide ou visqueux, figure), méthode 4, 3 cartes |
| Théorème scalaire du moment cinétique | énoncé | §5 (meule, treuil couplé), méthodes 4-5, EXO 05-06, 11, carte |
| Pendule pesant : équation, intégrale première | dans un bloc dépliable | §6 (\(\omega_0\), \(\ell_{\text{eq}}=J/(md)\), intégrale première, tige, cerceau), méthodes 6-7, EXO 04, 07, concours, 2 cartes |
| Non-isochronisme (capacité numérique) | une phrase | §7 (code exécuté, tableau, figure, horloge), méthode 9, EXO 08, concours C, 2 cartes |
| Énergie cinétique, théorème de l'énergie cinétique, équivalence | formules | §8 (\(\mathcal P=\mathcal M_\Delta\omega\) démontrée, équivalence, moteur, volant de stockage), méthode 8, EXO 05, 2 cartes |
| Étude énergétique du pendule, diminution de \(E_m\) | absente | §9 (bilan, simulation, figure, mesure de \(Q\)), EXO 09, concours D, carte |
| Système déformable, travail des forces intérieures, tabouret | encadré | §10 (nullité pour un solide démontrée, tabouret, embrayage), méthode 10, EXO 10-11, carte |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 10 sections + « Pour aller plus loin ») : §1 solide, translation ; §2 rotation ;
§3 moment d'inertie ; §4 poids, couple, liaison pivot ; §5 théorème scalaire ; §6 pendule pesant ; §7 non-isochronisme ;
§8 énergie cinétique et équivalence ; §9 étude énergétique du pendule ; §10 système déformable ; hors programme : Huygens-Steiner
(déplacé de `mcinc`), roulement, gyroscope (renvoi). 13 exemples traités chiffrés, 9 notices, 2 tableaux, 4 démonstrations
dépliables, 2 programmes Python exécutés, 5 figures SVG calculées (translation circulaire et rotation ; forces de contact d'un
pivot avec et sans frottement ; pendule pesant ; \(\theta(t)\) pour 20°, 90°, 160° et \(T/T_0\) avec Borda ; pendule amorti,
angle et énergie), vues en clair et en sombre.

**Méthodes** (10) : translation ou rotation ; vitesse d'un point ; exploiter \(J\) fourni ; bilan des moments ; solides couplés ;
pendule pesant ; intégrale première ; énergie cinétique ; simuler et valider ; système déformable. 2 pièges.

**Exercices** (12) : 01 translation ou rotation (bielle) ; 02 disque compact à vitesse linéaire constante ; 03 choisir un volant
d'inertie ; 04 tige (ancien 01, complété) ; 05 treuil par les deux théorèmes (ancien 02, complété) ; 06 roue de vélo freinée
(frottement visqueux) ; 07 disque suspendu par son bord (ancien `mcin` EXO 03, \(J_A\) fourni) ; 08 mesurer \(g\) : amplitude
maximale pour 1 % (code) ; 09 balancier d'horloge (\(Q\approx700\), puissance d'entretien) ; 10 tabouret d'inertie ;
11 embrayage, disques contrarotatifs ; **Concours PT « La barre qui pivote »** (ancien concours étendu : A chute, accélération
initiale \(\tfrac32g\) de l'extrémité ; B action du pivot \(\tfrac14mg\) au lâcher, \(\tfrac52mg\) à la verticale ;
C grandes oscillations, 1,93 s contre Borda 1,89 s ; D pivot réel, énergie perdue).

**Cartes** : 18 → 32 (14 ajoutées à la fin : translation ou rotation, moment du poids, pivot réel, équation et \(\omega_0\) du
pendule pesant, \(\ell_{\text{eq}}\), puissance, équivalence des théorèmes, pendule amorti, non-isochronisme, simulation de la
période, treuil, embrayage, J de la Terre, couple) ; 1 réponse précisée. Rendu MathJax : 0 erreur.

## Contrôles
`verif_src.py` sans erreur ni attention ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges` vides, aucune erreur JS,
pas de débordement ; `corriger_cartes.py --essai` (1 réponse) et `ajouter_cartes.py --essai` (18 → 32) sans erreur ; périodes
contrôlées par l'intégrale elliptique exacte (`scipy.special.ellipk`) ; code affiché exécuté (`msol_tester_code.py`).

## Notations
\(J_\Delta\) (fourni), \(L_\Delta=J_\Delta\omega\), \(\mathcal M_\Delta\), couple \(\Gamma\) (\(\Gamma_m\), \(\Gamma_f=-\lambda\omega\),
torsion \(-K\theta\) : pas de \(C\), réservé à la constante des aires), \(d\) distance de l'axe à \(G\), \(\omega_0=\sqrt{mgd/J}\),
\(T_0\), \(\ell_{\text{eq}}\), \(Q=J\omega_0/\lambda\) et \(\tau=2Q/\omega_0\) (convention du site), \(\mathcal P_{\text{int}}\).

## Doutes
- La formule de Borda est « admise », comme dans `incertitudes` (EXO 08), auquel le §7 et l'EXO 08 renvoient.
- Le principe fondamental appliqué au centre de masse (concours, partie B) vient de `mecpt` (lot 5) ; le programme de 2.7
  exclut l'étude générale translation + rotation, mais pas le calcul de l'action d'un pivot à axe fixe.
