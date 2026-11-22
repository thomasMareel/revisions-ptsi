# Revue du chapitre `thermo3` (prefix `th3`) — « 2e principe thermo » — 2026-11-22

Objet (point 4 de l'audit, lot 8 ; `docs/audit-2026-11/physique-1a.md` l. 49, 82, 104, 113, 155 ; `audit-2026-11.md` §5
points 7 et 8) : cours de 10 000 signes sans figure, §4 « identités thermodynamiques » (1.2 de PT) et §5 « formules à
connaître par cœur » alors qu'en PTSI l'expression de S est fournie, 5 méthodes, 6 exercices + 1 « Concours PT » de
2 questions, 26 cartes ; chevauchements avec `thermo1`/`thermo2` (lois de Joule, causes d'irréversibilité, thermostat).
Programme : PTSI 2021, partie 3.4 « Deuxième principe. Bilans d'entropie » (`ptsi.txt` l. 1583-1606).

## Décisions
- **Expression de S fournie** : le cours la présente comme donnée par l'énoncé (§4 : gaz parfait sous trois formes,
  phase condensée, thermostat ; extensivité), conformément à l'en-tête de la partie 3.4. Les **identités
  thermodynamiques** passent en « Pour aller plus loin » (2ᵉ année, renvoi `thermodiff` §2), avec la façon d'en tirer
  les expressions fournies ; les quatre cartes 10-13 étaient déjà préfixées « Hors programme en PTSI ».
- **Loi de Laplace** (au programme de 3.4) : conditions détaillées une à une, démonstration par \(\Delta S=0\) à partir de
  la forme \((P,V)\) de l'entropie ; la démonstration par le premier principe reste dans `thermo2` §5 (renvoi).
- **Chevauchements** : définitions des transformations, thermostat, causes d'irréversibilité et détente de Joule-Gay-Lussac
  renvoyées à `thermo2` §1 et §6 ; ici, chaque cause est **chiffrée** par un bilan (§6). Changement d'état : la relation
  \(\Delta h_{12}=T\Delta s_{12}\) est citée et utilisée (§10), le détail reste dans `changement` §9-§10. Machines : §11 se
  limite à l'inégalité de Clausius et au moteur monotherme, renvoi à `machines` §2, §4, §5.
- **Notations** du site : \(S_{\text{éch}}=\sum_iQ_i/T_i\), \(S_{\text{créée}}\), transferts reçus par le système,
  \(T\) en kelvins, \(C_V\), \(C_P\), \(\gamma\), \(\Delta h_{12}\) ; \(T_C\), \(T_F\), \(e_{PAC}\) comme `machines` dans l'EXO 06.

## Fichiers produits (dans `AN1/`)
- `th3-cours.src.html` (63 ko ; 32 900 signes de texte contre 10 000) — assemblé par `th3_construire.py` depuis
  `th3-cours.tpl.html` et `th3_figs.json` ;
- `th3-meth.src.html` (10 méthodes, 3 pièges) ; `th3-exos.src.html` (11 exercices + « Concours PT ») ;
- `th3-cartes-corr.json` (2 réponses corrigées) ; `th3-cartes-ajout.js` (14 cartes) ;
- scripts : `th3_figs.py` (6 figures), `th3_calculs.py` (cours), `th3_calculs_exos.py` (méthodes, exercices, concours ;
  sympy pour la compression brutale), `th3_construire.py`, `th3_voir.py`, `th3_deborde.js`, `th3_cartes_rendu.js` ;
  copies `th3_orig_{cours,meth,exos}.html`.

## Erreurs trouvées et corrigées
| Où | Problème | Correction |
|---|---|---|
| Ancien EXO 04 (compression adiabatique brutale) | énoncé impossible : volume divisé par 4 sous \(P_{\text{ext}}=P_f\) « donnée par Laplace » ; le corrigé suppose en fait \(P_{\text{ext}}\) égale à la pression finale du gaz, et une erreur de signe (\(-\tfrac12T_f=-750\)) donne 600 K ; l'équation correcte \(\tfrac52(T_f-T_i)=3T_f\) donne \(T_f\lt0\) | exercice réécrit : même pression finale (10 bar) par les deux chemins ; \(T_f=T_i[1+(\gamma-1)P_f/P_i]/\gamma\) démontré (vérifié par sympy) ; \(S_{\text{créée}}=17{,}9\) J/K ; Q4 : rapport des volumes borné par \(\gamma/(\gamma-1)=3{,}5\), d'où l'impossibilité de l'ancien énoncé ; même limite expliquée au cours, §9 |
| Ancien EXO 03 (mélange) | \(T_f=328{,}9\) K au lieu de 329,0 K (avec 353 et 293 K), d'où \(S_{\text{créée}}=7{,}8\) J/K au lieu de 8,6 | corrigé (8,6 J/K) ; Q4 ajoutée sur la sensibilité du résultat à \(T_f\) |
| Ancien EXO 05 (deux thermostats) | corrigé inachevé : \(W\), \(Q_1\), \(Q_2\) jamais déterminés, conclusion vague | exercice réécrit avec \(Q_1\) et \(W\) donnés : \(Q_2\), \(S_{\text{créée}}=3{,}67\) J/K, puis travail maximal 2,1 kJ imposé par \(S_{\text{créée}}\geq0\) |
| Ancien EXO 06 (pompe à chaleur) | notation « COP », exercice de machines sans deuxième principe ; « COP clim = COP − 1 » aux mêmes températures en été | notations \(e_{PAC}\), \(T_C\), \(T_F\) de `machines` ; entropie créée par seconde, \(W=W_{\min}+T_FS_{\text{créée}}\) ; climatiseur entre 25 °C et 35 °C |
| Ancien §4-§5 | identités « valables pour tout système » et formules « à connaître par cœur » | expressions fournies (§4) ; identités hors programme, en fin de chapitre, avec leur domaine (système fermé, composition fixée) |
| Carte 22 | démarche : « calculer ΔS par l'identité thermo » | « avec l'expression fournie » (réponse seule) |
| Carte 11 | identité « valable pour tout système » | système fermé de composition fixée, états d'équilibre voisins (réponse seule, reste « Hors programme ») |
| Ancien §2 | « Si ΔS < 0 … » (phrase tronquée par un « < » brut) | réécrit ; aucun « < » brut |

## Couverture du programme (3.4) : avant → après
| Capacité | Avant | Après |
|---|---|---|
| Interpréter qualitativement l'entropie par la formule de Boltzmann fournie | §3 (6 molécules) | §3 (Ω multiplié par \(2^N\) dans une détente, cohérence avec \(nR\ln2\), deux figures calculées : détente à l'échelle moléculaire, distribution binomiale pour N = 20, 200, 2 000), EXO 09, carte |
| Définir un système fermé et établir un bilan entropique | §1-§2 | §2 (énoncé, statuts, figure système-sources), §5 (méthode en 4 étapes, exemple, contrôle par l'ensemble isolé), méthodes 1-4, tous les exercices, cartes |
| Relier la création d'entropie à ses causes | liste | §6 (contact avec un thermostat : \(C(x-1-\ln x)\), figure calculée ; chute de masse ; effet Joule ; détente), §7 (contact de deux corps, N thermostats, figure), §9 (travail perdu \(T_0S_{\text{créée}}\)), méthodes 6-8, EXO 02, 03, 07, 08, 11, cartes |
| Analyser une évolution adiabatique | remarque | §5 (encadré : \(\Delta S=S_{\text{créée}}\geq0\), système isolé), §9 (compression brutale, figure en (P, V) calculée), EXO 04, 08, 09, carte |
| Utiliser l'expression fournie de l'entropie ; extensivité | « par cœur » | §4 (trois formes du gaz parfait, phase condensée, thermostat, extensivité, exemples, piège des °C), méthode 2, cartes |
| Loi de Laplace et ses conditions | une vérification | §8 (énoncé, démonstration par ΔS = 0, conditions une à une, Diesel), méthode 5, EXO 04, concours A-C, 2 cartes |
| \(\Delta h_{12}=T\Delta s_{12}\) | absent | §10 (relation, valeurs de l'eau, glaçon dans une pièce), méthode 9, EXO 10, carte |
| (Vers 3.5) bilans sur un cycle | carte 25 | §11 (Clausius, pas de moteur monotherme, \(W=T_0S_{\text{créée}}\), exemple), méthode 10, EXO 06, concours D, carte |

## Contenu
**Cours** (« AU PROGRAMME · PTSI » + 11 sections + « Pour aller plus loin ») : §1 Le sens des transformations ; §2 Le
deuxième principe ; §3 Interprétation statistique ; §4 Entropie des systèmes usuels ; §5 Bilan d'entropie (méthode, cas
adiabatique) ; §6 Causes d'irréversibilité ; §7 Contact thermique et mélange ; §8 Loi de Laplace ; §9 Détentes et
compressions d'un gaz parfait ; §10 Entropie et changement d'état ; §11 Cycles ; hors programme : identités
thermodynamiques, entropie de mélange, troisième principe. 11 exemples traités chiffrés, 11 notices, 1 démonstration
dépliable, 6 figures calculées, vérifiées en clair et en sombre.

**Méthodes** (10) : système et sources ; ΔS par l'expression fournie ; \(S_{\text{éch}}\) ; bilan et conclusion ; Laplace ;
contact thermique ; dissipation ; détente ou compression ; changement d'état ; cycle (Clausius). Les 4 anciennes méthodes et
les pièges sont repris (sans « identité thermodynamique »).

**Exercices** (11 + concours) : 01 phase condensée (ancien, Q4 thermostat à 80 °C) ; 02 détente isotherme (ancien, Q4
travail perdu) ; 03 mélange (corrigé) ; 04 compression adiabatique (réécrit) ; 05 deux thermostats (réécrit) ; 06 pompe à
chaleur (réécrit) ; 07 freinage et chute ; 08 résistance chauffante ; 09 Joule-Gay-Lussac et Boltzmann ; 10 glaçon dans un
verre (\(S_{\text{créée}}=1{,}9\) J/K) ; 11 chauffage en N étapes ; **Concours PT « Stocker de l'énergie dans de l'air
comprimé »** (A compression de Laplace, 558 K et 9,5 bar ; B stockage isochore, \(S_{\text{créée}}=216\) J/K ; C détente,
154 K, rendement \(5^{-0{,}4}=0{,}53\) ; D cycle monotherme, \(W=T_0S_{\text{créée}}=104\) kJ vérifié ; stockage de la
chaleur). L'ancien « Concours PT » (contact de deux masses égales) est couvert par le cours §7 et l'EXO 03.

**Cartes** : 2 réponses corrigées (questions inchangées : 11, 22) ; 14 ajoutées à la fin (logarithme de Boltzmann,
\(C(x-1-\ln x)\), contact de deux corps, dissipation, Joule-Gay-Lussac, Laplace et conditions, forme \((P,V)\) de S,
Diesel, compression brutale, évolution adiabatique, \(\Delta s_{12}\) de l'eau, Clausius et monotherme, N thermostats,
travail perdu). Deck : 26 → 40. Rendu MathJax contrôlé (`th3_cartes_rendu.js`) : aucune erreur ; une question réécrite en
TeX pour éviter un découpage fautif par `flashPretty`.

## Contrôles
`verif_src.py` (3 fichiers) : aucune erreur ni « attention ». `apercu_src.py` à 390 et 1440 px pour les trois panneaux :
`merr`, `brut`, `larges` vides, `scrollW` égal à la largeur, aucune erreur JS (deux formules en ligne non détectées par
`larges` mais qui élargissaient la page à 390 px ont été repérées par `th3_deborde.js` et coupées). Cartes :
`corriger_cartes.py th3 … --essai` (2) et `ajouter_cartes.py th3 … --essai` (26 → 40) sans erreur. Tous les nombres
recalculés (`th3_calculs.py`, `th3_calculs_exos.py`).

## Doutes et points pour l'intégration
- **Titre** : « 2e principe thermo » est un libellé court ; proposition « Deuxième principe : bilans d'entropie »
  (mobLabel « 2e principe » inchangé).
- Cartes 15 à 20 (« Quelle est la formule de ΔS pour… ») : justes ; en PTSI ces expressions sont fournies, mais les
  connaître reste utile ; non modifiées.
- `thermo2` §1 garde sa liste des causes d'irréversibilité (renvoi ici pour les bilans) ; `thermo2` §5 garde la démonstration
  de Laplace par le premier principe : pas de doublon gênant, deux points de vue.
- Le concours donne des ordres de grandeur d'installations réelles (« environ 70 % » visés pour le stockage adiabatique) :
  fourchette usuelle, non tirée d'une source unique.
