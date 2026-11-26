# Revue `hacheurs` (prefix `hach`) — « Les hacheurs » (point 7 de l'audit, 2026-11-26)

Livrables (AN1/) : `hach-cours.src.html` (gabarit `hach-cours.tpl.html` + `hach_figs.json`, assemblés par
`hach_construire.py`), `hach-meth.src.html`, `hach-exos.src.html`, `hach-cartes-corr.json`, `hach-cartes-ajout.js`.
Scripts : `hach_calculs.py` (régime périodique exact d'une charge R, L, E_m découpée + exemples du cours),
`hach_figs.py` (10 figures), `hach_calculs_meth.py`, `hach_calculs_exos.py` (+ `hach_calculs_exos.out`),
`hach_cartes.py`, `hach_voir.py`, `hach_cartes_rendu.js`, correctifs `hach_fix*.py`. Panneaux `-simu` et `-flash`
non touchés.

Contrôles passés : `verif_src.py` (trois panneaux, aucune erreur ni « attention ») ; `apercu_src.py` à 390 et 1440 px
pour cours, méthodes, exercices : `merr`, `brut`, `larges` vides, aucune erreur JS ; figures regardées en clair et en
sombre et dans la page (captures 390) ; `corriger_cartes.py --essai` (4 réponses) ; `ajouter_cartes.py --essai`
(25 → 38) ; rendu MathJax des cartes sans erreur.

## Programme

`si.txt`, B2 « Modéliser les convertisseurs statiques d'énergie » (**S2**) : interrupteurs parfaits, cellule de
commutation, synthèse limitée au hacheur, à l'onduleur et au redresseur, nature des grandeurs, réversibilité ;
convertisseurs à deux ou trois cellules. A3 (S1) : fonction moduler. **S3** : ondulation des grandeurs en régime
permanent et composants de filtrage (C2) ; **S4** : choix des composants de la chaîne de puissance. Le programme ne
nomme pas la MLI ; elle est présentée comme le moyen de régler \(\alpha\) et de modéliser le hacheur par un gain
(schéma-blocs, S1). Bloc « AU PROGRAMME · PTSI » écrit en conséquence, avec « Vu en avance (2ᵉ année) » pour
l'ondulation (§5) et « Hors programme » pour le hacheur élévateur seul, la conduction discontinue, le filtrage, la
commutation douce.

## Erreurs corrigées

| Où | Avant | Après |
|---|---|---|
| Cours §3 (hacheur réversible en courant) | « Phase active : T2 passant, D1 bloquée → énergie renvoyée vers la source » | **faux** : quand \(T_2\) conduit, \(u = 0\) et l'énergie s'accumule dans \(L\) ; elle revient à la source quand le courant passe par \(D_1\) (\(u = E\)). Figure calculée, notice « Erreur classique », carte nouvelle |
| Cours §3 | « quadrants 1 et 4 » sans dire le plan, avec \(\Omega\), \(C_{em}\) (contraire au plan \((C_{em}, \Omega)\) de `mcc`) | plan \((u, i)\) dit explicitement, correspondance avec Q1-Q2 du plan \((C_{em}, \Omega)\) ; tableau de correspondance au §7 |
| Cours §1 | \(0 < \alpha < 1\) (« < » brut dans le HTML), \(U_e\), \(U_s\), \(U_C\) pour la même tension | \(0 \leq \alpha \leq 1\) ; \(E\), \(u\) (notations de `cvs` et de la 2ᵉ année) |
| Figure du §1 | libellés à 9 px (minimum du site : 12 px), « t_on=αT » | figure recalculée, libellés ≥ 12 px |
| Cours §2 | « un courant résiduel circule dans K₂ » ; « condition recommandée \(f > 10/\tau_L\) » sans justification | c'est tout le courant de charge qui passe par la diode ; règle de \(f\) rattachée à l'ondulation (§5) |
| Cours §2 | « pas de freinage régénératif » sans dire ce qui se passe si la machine est entraînée | conduction discontinue puis courant nul, plus aucun couple de freinage |
| Cours §4, tableau | tableau en `array` TeX (\textbf{i_s}…), plan non dit | tableau HTML : quadrant \((u, i)\), régime, aiguillage, hachage, composants des deux phases (séquences vérifiées une à une) |
| Méthode 3 | réversible en courant = « 2 cellules », pont en H = « 4 cellules » | une cellule (deux interrupteurs à trois segments) ; pont = deux cellules (bras), quatre interrupteurs |
| Exercice 02 | inductance **pure** alimentée par un hacheur série : aucun régime permanent possible (le courant croît sans fin), \(\Delta I^- = 0\) présenté comme normal | bobine \(r\)-\(L\) : régime périodique, \(\Delta I^\pm = \pm 0{,}06\ \text{A}\), surtension de 60 kV estimée, énergie 0,18 J |
| Exercice 04 | « Phase (T₂, T₃ ON) : courant de B vers A » : le courant ne s'inverse pas à chaque phase | le courant garde son signe (inductance) ; avec \(i > 0\), ce sont \(D_2\), \(D_3\) qui conduisent quand \(T_2\), \(T_3\) sont commandés ; point de fonctionnement d'une machine, ondulation bipolaire / séquentielle |
| Exercice 05 | « \(P_{sw} = E^2/(2Rn)\) » (formule sans sens) | pertes de commutation = énergie par période × \(f\) ; conduction du transistor et de la diode calculées |
| Exercice 06 (élévateur) | non signalé ; condensateur de sortie absent de l'énoncé | « (hors programme, pour aller plus loin) » ; condensateur précisé |
| Exercices 01, 03 | écritures ambiguës « /2×10⁻³ », « < » brut, lignes trop larges au téléphone | fractions, `\lt`, formules en bloc |
| Concours PT | trois questions sur \(\langle u\rangle = \alpha E\) (★★☆) | problème original en quatre parties (chariot autonome, pont en H bipolaire) |
| Cartes 1, 5, 13, 15 | « signal carré de tension **alternatif** » (il ne l'est pas) ; « courant résiduel » ; réversible en courant = « 2 cellules » ; pont = « 4 cellules » | réponses corrigées (questions inchangées) |

Calculs refaits (`hach_calculs_exos.py`) : exercices 01 et 03 justes ; 06 juste ; anciennes valeurs reprises.

## Couverture avant → après

| Capacité | Avant | Après |
|---|---|---|
| Fonction moduler, intérêt du découpage (A3 S1) | §1 qualitatif | §1 + exemple chiffré (résistance série : 25 % ; hacheur) |
| Interrupteurs, cellule, hacheur série (B2 S2) | §2 (pas de figure, pas d'équations) | §2 : schéma, phases avec équations, relations moyennes \(\alpha E = R\langle i\rangle + E_m\), courants moyens, conservation de la puissance, chronogrammes **calculés** (u, i, i_T, i_D) |
| Réversibilité, hacheur réversible en courant | §3 (erreur sur le transfert d'énergie) | §3 corrigé : schéma, deux commandes, commande complémentaire (réversibilité naturelle), chronogramme calculé en freinage, exemple |
| Pont en H, quadrants | §4 séquentielle seulement | §4 : schéma, commande bipolaire \((2\alpha - 1)E\) avec figure, séquentielle en tableau, pont asymétrique (réversible en tension), exemple |
| Ondulation, choix de L (S3, vu en avance) | une phrase | §5 : formule démontrée, cas bipolaire, figure \(\alpha(1-\alpha)\), choix de \(L\), conduction discontinue (HP) |
| Commande MLI, gain du hacheur | définition de α | §6 : comparateur et porteuse (figure), \(\alpha = v_c/V_p\), gain \(G = E/V_p\), porteuse symétrique, commande numérique, temps morts |
| Association avec la MCC | dispersé | §7 : modèle moyen, deux plans (figure calculée), tableau régimes → quadrants → hacheur, cycle chiffré, limite de la récupération |
| Bilan de puissance, rendement | absent (sauf exercice 05) | §8 : conduction, commutation, compromis sur \(f\), exemple à 99 % |

## Ajouts

- **Cours** : bloc « AU PROGRAMME · PTSI » ; §1 à §4 gardés (mêmes numéros et titres), réécrits et corrigés ;
  nouvelles sections **§5** ondulation et inductance, **§6** commande MLI, **§7** association avec une MCC,
  **§8** bilan de puissance ; « Pour aller plus loin · hors programme ». 8 exemples chiffrés (un par section),
  10 figures (dont 5 calculées : chronogrammes série et freinage en régime périodique exact, créneaux MLI et
  bipolaire, ondulation, porteuse, plans).
- **Méthodes** : 4 → 9 (1 grandeurs moyennes, 2 phases du série, 3 qui conduit, 4 choisir la structure,
  5 pont en H séquentiel, 6 ondulation et L, 7 MLI, 8 point de fonctionnement d'une MCC, 9 bilan de puissance) +
  pièges complétés.
- **Exercices** : 7 → 11 (01, 03, 06 gardés ; 02, 04, 05 refaits ; 07 hacheur série et moteur ★, 08 freinage avec
  récupération d'une trottinette ★★, 09 commande MLI et fonction de transfert ★★, 10 pont en H séquentiel sur un
  cycle ★★ ; Concours PT en quatre parties : structure, croisière et ondulation, accélération / freinage avec bilan
  énergétique, commande et modèle).
- **Cartes** : 4 réponses corrigées (1, 5, 13, 15) ; 13 ajoutées à la fin (relation moyenne, courants moyens,
  ondulation, bipolaire, retour d'énergie en freinage, commande complémentaire, MLI, temps morts, quadrants dans les
  deux plans, ordres de grandeur, pertes, limite de la récupération, pont asymétrique).

## Notations

\(E\) source (comme `cvs`, le simulateur et la 2ᵉ année), \(u\) tension de sortie, \(i\), \(i_e\), \(i_T\), \(i_D\),
\(E_m\) f.é.m. de la machine, \(\alpha\), \(T = 1/f\), \(\langle\cdot\rangle\). Interrupteurs : K1 = \(T\), K2 = \(D\)
(série) ; \(T_1\)/\(D_1\), \(T_2\)/\(D_2\) (réversible) ; \(T_1\) à \(T_4\) (pont) — **gardés** pour que les cartes
14 à 22, qui les citent, restent justes ; la correspondance avec les bras \(K_1\), \(K_1'\), \(K_2\), \(K_2'\) de
`cvs` est donnée sous la figure du pont.

## Doutes et suites

- `cvs` (§8) écrit : « Le chapitre « Les hacheurs » note \(U_e\) la tension d'entrée (ici \(E\)) et \(T_1\) à \(T_4\)
  les transistors du pont » : la première moitié n'est plus vraie (le cours écrit \(E\) ; seules les premières
  cartes gardent \(U_e\), \(U_s\)). Phrase à mettre à jour lors d'une reprise de `cvs`.
- Les premières cartes (2, 3, 4, 6, 8…) gardent \(U_e\), \(U_s\) (justes, non modifiées) ; le bloc de notations du
  cours le signale.
- Renvois de `mcc` §8 vers « Les hacheurs » §2 à §5 : vérifiés (§5 = ondulation).
- La MLI n'est pas nommée par le programme : présentée comme principe de commande, sans exigence électronique.
