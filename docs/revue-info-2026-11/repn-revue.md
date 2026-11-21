# `pyrepr` (prefix `repn`) — « Représentation des nombres » — compte rendu

Chapitre existant, 1ʳᵉ année, partie 2.2 du programme d'informatique commune 2021 (2ᵉ semestre). Rédaction entièrement
originale : exemples, exercices et données inventés ; les faits historiques cités (Ariane 501 en 1996, Patriot en 1991,
compteurs 32 bits et « an 2038 ») sont des faits publics, sans emprunt de texte.

## Fichiers produits (dans `INFO/`)
- `repn-cours.src.html` (≈ 83 000 car.) : bloc « AU PROGRAMME · INFORMATIQUE » + 9 sections + « Pour aller plus loin » ;
  12 exemples traités, 4 figures SVG calculées (mot de 8 bits et ses poids ; roue des mots de 4 bits en complément à deux ;
  flottants d'un format jouet sur une droite ; alignement des mantisses : absorption et cancellation), tableaux calculés
  (divisions successives, tailles de mots, mots signés, factorielles, développement binaire de 0,375 et 0,1, valeurs
  exactes de 0,1 + 0,2, cancellation, somme des \(1/k^2\) dans les deux ordres), additions posées en binaire (blocs à
  chasse fixe, retenue sortante séparée par un trait vertical : 107 + 54, 200 + 100, 45 + (−73), (−20) + (−30), 100 + 50).
- `repn-meth.src.html` : 9 méthodes (étapes, exemple éclair) + pièges.
- `repn-exos.src.html` : 10 exercices (3 ★, 4 ★★, 2 ★★★, 1 « Concours PT » en 4 parties).
- `repn-cartes-corr.json` (10 réponses retouchées, **aucune question modifiée**), `repn-cartes-ajout.js` (12 cartes, 4 `cat:'form'`).
- Sources et tests : `INFO/tests/repn/` — `code_repn.py`, `code_repn_meth.py`, `code_repn_exos.py` (tous les blocs de code),
  `test_repn.py` (un test par bloc, consoles vérifiées par `doctest`, valeurs citées dans les textes), `figs_repn.py`,
  `svg.py`, `tables_repn_exos.py`, gabarits `*.tpl.html`, `build_repn.py` (tests puis assemblage : le code affiché est le
  code testé), `cartes_repn.py` (cartes, avec vérification des valeurs). Outils copiés de `tests/pyb/` (`outils.py`,
  `lire_cartes.py`). Reconstruction : `python3 INFO/tests/repn/build_repn.py`. 64 blocs, 43 tests.

## Cours (avant : 4 sections, ≈ 3 300 car. de HTML)
1. Bits, mots, entiers naturels : écriture en base 2, poids, \(2^n\) valeurs de 0 à \(2^n - 1\), nombre de bits
   \(\lfloor \log_2 n \rfloor + 1\) (fonction `nb_bits`, variant), tailles usuelles ; hexadécimal en simple remarque.
2. Changer de base (en précisant que ce n'est « pas un objectif de formation ») : Horner, divisions successives (77),
   `binaire` / `valeur` (liste, poids faible en tête) avec variant et invariant, `chaine_binaire` / `valeur_chaine`,
   `bin` et `int(…, 2)` signalés hors annexe.
3. Entiers de taille fixe : addition posée, dépassement = calcul modulo \(2^n\), compteur de 49,7 jours, an 2038, Ariane 5.
4. Complément à deux : définition (\(x + 2^n\) pour \(x \lt 0\)), formule de la valeur, « inverser + 1 » (démonstration
   dépliable), roue de 4 bits, additions, retenue sortante ≠ dépassement, règle des signes, fonctions `code_c2`,
   `valeur_c2`, `mot`, `somme_c2` (n'utilisent `%` qu'avec des opérandes positifs, comme le veut l'annexe).
5. Entiers multi-précision de Python : exactitude, \(21!\) sur 64 bits, coût dépendant de la taille (difficulté signalée
   par le programme, renvoi à l'exponentiation rapide de `pydicho`), débordement silencieux des tableaux `numpy`.
6. Réels, décimaux, dyadiques, flottants : critère « dénominateur puissance de 2 », développement binaire par doublements
   (0,375 fini, 0,1 périodique), `bits_fraction` en calcul exact, valeur rangée pour `0.1`, Patriot.
7. Mantisse et exposant : définition générale (format à \(p\) bits), zéro codé à part, décompositions (13,25, −6,5, 0,1),
   `decomposer`, ordres de grandeur des `float` (53 bits, \(2^{-52}\), \(1{,}8 \times 10^{308}\)) donnés « pour fixer les
   idées », espacement des flottants, entiers au-delà de \(2^{53}\).
8. Précision des calculs : erreur relative ≤ \(2^{-53}\), 0,1 + 0,2 expliqué (somme exacte à mi-chemin de deux flottants),
   non-associativité, accumulation, absorption (\(10^{16} + 1\), ordre de sommation), cancellation (\((1 - \cos x)/x^2\)
   et sa réécriture).
9. Comparer des flottants : tolérances absolue et relative (`proche`), échecs d'une tolérance absolue fixe, boucles pilotées
   par un compteur entier, renvois (variant flottant de `pyanalyse` §3, jeux de tests, centimes du chapitre glouton).
Hors programme regroupé : IEEE-754, dénormalisés, infinis/NaN (une ligne, `OverflowError`), modes d'arrondi, `fsum`,
`fractions`, `decimal`, Karatsuba.

## Couverture du programme 2.2 (avant → après)
| Notion | Avant | Après |
|---|---|---|
| Entiers positifs sur mots de taille fixe | 2 lignes | §1, §3, M3, M6, EXO 01-03 |
| Entiers signés, complément à deux | 1 phrase | §4, M4-M6, EXO 04-05, Concours A-C |
| Entiers multi-précision, difficulté de la complexité | 1 phrase | §5, EXO 09, Concours D3 |
| Réels, décimaux, flottants ; non-représentabilité | absent | §6, M7, EXO 07-08 |
| Flottants sur mots de taille fixe, mantisse, exposant, zéro | 1 phrase | §7, M7, EXO 07 |
| Précision des calculs, comparaisons | 2 phrases | §8, §9, M8-M9, EXO 06, 08, Concours D |

## Méthodes et exercices
- Méthodes : les 2 anciennes gardées (M1, M2, enrichies : Horner, `chiffres(n, b)` en Python) ; l'ancien encadré « Pièges
  classiques » devient l'encadré final, complété ; 7 nouvelles (étendue d'un mot, coder et décoder en complément à deux,
  addition et dépassement, décomposition d'un réel, erreurs d'arrondi, comparaisons et boucles).
- Exercices gardés : anciens EXO 01 (+ Q2, Q3), 02 (+ Q2), 03 « Égalité de flottants » devenu EXO 06 (+ Q3, Q4), ancien
  « CONCOURS » conservé mot pour mot comme parties A et B du nouvel exercice « Concours PT » (accéléromètre : décodage de mots
  de 16 bits, accumulateur qui déborde, horloge flottante, moyenne calculée en entiers). Seules retouches de forme dans
  l'ancien texte : deux formules en ligne coupées en deux (débordaient à 390 px).
- Nouveaux : compteurs et an 2038, complément à deux sur 8 bits (dont un dépassement), programmation de l'opposé
  (`inverser`, `plus_un`, `oppose`), mantisse et format jouet, pertes de précision (horloge, second degré, \(\sqrt{x+1} -
  \sqrt x\)), entiers de 64 bits simulés (`produit64`, \(n!\) faux et parfois positif).

## Cartes
- Corrigées (réponse seule, question identique : progression conservée) : 1, 2, 3, 4, 6, 7, 8, 9, 10, 11 — formules en
  `\( … \)`, code en accents graves, compléments (complément à deux défini, coût des entiers multi-précision, tolérance
  relative). Aucune carte n'était fausse ; la carte 10 écrivait le code `abs(x − y)` avec un signe moins typographique
  (corrigé dans la réponse). Cartes 0 et 5 inchangées (ni code ni formule).
- **Questions non retouchées volontairement** : les questions des cartes 3 (`2^4`…), 9 (`0.1 + 0.2`), 10 (`==`) et 11
  (`bin(13)`) contiennent du code ou des formules non marqués ; pour ne pas changer question et réponse d'une même carte,
  seule la réponse a été marquée. Elles restent lisibles en texte brut.
- Ajoutées (12) : intervalle du complément à deux (form), opposé, valeur d'un mot (form), dépassement modulo \(2^n\),
  détection du dépassement, coût des grands entiers, forme d'un flottant (form), précision d'un `float` (form), 0,1 non
  représentable, absorption, cancellation, entiers exacts jusqu'à \(2^{53}\).

## Contrôles
`verif_src` sans erreur ni « attention » ; `apercu_src` à 390 et 1440 px sur les trois onglets : `merr`, `brut`, `larges`
vides, aucune erreur JS, pas de débordement de page ; figures regardées en capture (390 px) ; `corriger_cartes.py --essai`
(10) et `ajouter_cartes.py --essai` (12 → 24) sans erreur ; `verif_cartes.js` sans remarque.

## Doutes
- Le programme dit que la conversion de base « n'est pas un objectif de formation » : le §2 reste présent (mention explicite),
  car les sujets demandent souvent d'écrire ces fonctions et il sert à lire les mots binaires.
- Les valeurs du format double précision (52 bits, exposants de −1022 à 1023) sont données « pour fixer les idées » sans
  être présentées comme exigibles ; la mention de la règle « au pair » pour 0,1 + 0,2 est cantonnée au hors-programme.
- `abs`, `bin`, `int(…, 2)`, le littéral `0b…`, `math`, `fractions`, `numpy` sont hors annexe : signalés là où ils servent.
- Les références au chapitre « Recherche séquentielle, dictionnaires et dichotomie » (exponentiation rapide, racine
  entière) et « Algorithmes gloutons » supposent l'intégration de ces nouveaux chapitres en même temps.
