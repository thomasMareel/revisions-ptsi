# Revue et réécriture : `cinetique` (prefix `cin`), « Cinétique chimique » — 2026-11-22

Point 4 de l'audit, lot 7 (`docs/audit-2026-11/physique-1a.md` l. 55, 92, 128, 133 ; `docs/audit-2026-11.md` §5).
Programme : PTSI 2021, partie 4.1.2 « Évolution temporelle d'un système chimique » (`pdf-pt/prog/ptsi.txt`,
l. 1136-1180) et capacités expérimentales associées (l. 473-481 : suivi cinétique, simplification de la loi de vitesse,
énergie d'activation). Vérifié dans le programme de PT (`phys.txt`) : aucun mécanisme réactionnel ni catalyse ; la cinétique
y est seulement réinvestie (réacteur adiabatique en thermochimie, courbes courant-potentiel). Rédaction originale, exemples et
exercices inventés (sauf données classiques citées comme telles), toutes les valeurs recalculées.

## Fichiers (dans `AN1/`)
| Fichier | Contenu |
|---|---|
| `cin-cours.src.html` | construit par `cin_construire.py cin` depuis `cin-cours.tpl.html` + `cin_figs.json` + `cin_code/bloc1.py`, `bloc2.py`, `bloc3.py` |
| `cin-meth.src.html` | 10 méthodes au programme + méthode 11 (mécanismes) signalée hors programme, 5 pièges |
| `cin-exos.src.html` | depuis `cin-exos.tpl.html` + `cin_code/exo11.py`, `concours.py` ; 11 exercices + « Concours PT » + 2 exercices hors programme en fin |
| `cin-cartes-corr.json`, `cin-cartes-ajout.js` | 7 réponses corrigées (questions inchangées), 13 cartes ajoutées en fin (29 → 42) ; corrections générées par `cin_cartes.py` |
| `cin_donnees.py` | données communes (fil rouge du cristal violet, constantes de N₂O₅) |
| `cin_figs.py` → `cin_figs.json` | 7 figures calculées |
| `cin_calculs.py`, `cin_calculs_exos.py` | vérification de tous les nombres du cours, des méthodes et des exercices (numpy, scipy `solve_ivp`) |
| `cin_tester_code.py` | exécute chaque `<pre class="codeblock">` (sorties identiques aux commentaires : vérifié) |
| `cin_couper.py`, `cin_deborde.js`, `cin_voir.py`, `cin_cartes_rendu.js` | coupe des formules en ligne trop larges, recherche d'un débordement à 390 px, aperçu des figures (clair et sombre, `cin_voir/`), rendu MathJax des cartes |

## Erreurs et défauts trouvés (corrigés)
1. §1 : « La vitesse est toujours positive » (faux en général : elle est positive quand la réaction avance dans le sens direct) ;
   hypothèses de la définition absentes (volume constant, réaction unique sans accumulation d'intermédiaires, que le programme
   exige) ; « en PTSI on travaille souvent avec \(v = -\mathrm d[\mathrm A]/\mathrm dt\) » (vrai seulement si le coefficient de A vaut 1).
2. Audit l. 128 (« Durée de vie : t₁/₂ » à l'ordre 0) : la mention avait déjà disparu du panneau ; le nouveau cours définit
   séparément temps de demi-réaction et temps de demi-vie d'un réactif (§7, avec un exemple où ils diffèrent), comme le programme.
3. « La vitesse double tous les 10 °C » sans condition : quantifié (vrai pour \(E_a \approx 53\ \text{kJ·mol}^{-1}\) près de 25 °C, figure).
4. Mécanismes, étape cinétiquement déterminante, AEQS et catalyse présentés comme « utiles en 2ᵉ année et en PT » (§4) et
   « relevant de la 2ᵉ année » (carte 28) : ils ne sont dans aucun des deux programmes. Regroupés en « Pour aller plus loin ».
5. Méthode 5 (étape cinétiquement déterminante) et EXO 04, EXO 06 (mécanismes) non signalés hors programme : devenus méthode 11,
   EXO 12 et EXO 13, signalés ; la constante du pré-équilibre est écrite sans dimension (avec \(c^\circ\)), comme dans `equilchim`.
6. Ancien EXO 01 intitulé « décomposition radioactive » pour une réaction chimique : retitré. Ancien EXO 05 : loi \(p(t)\) donnée
   toute faite, en mmHg : refait (EXO 07, établir la relation entre la pression et l'avancement, puis tester l'ordre).
7. Cartes (réponse seule corrigée) : n° 0 (« toujours positive », hypothèses), n° 23 (signe de la pente de la tangente oublié),
   n° 24 (demi-vie confondue avec le temps de demi-réaction), n° 16, 17, 20 (mécanismes non signalés hors programme),
   n° 28 (statut au programme de PT faux). Aucune carte fausse des deux côtés.
8. Contrôle des anciens corrigés : EXO 01 à 03, 05 et concours justes (Arrhenius : 54,6 kJ·mol⁻¹, \(k(60\,°\mathrm C) = 2{,}0\times10^{-2}\),
   \(A = 7{,}6\times10^6\) recalculés) ; gardés et complétés.

## Couverture du programme (PTSI 4.1.2), avant → après
| Capacité | Avant | Après |
|---|---|---|
| Vitesses de consommation, de formation, de réaction ; les relier (réaction unique, sans accumulation) | définition seule | §1 (hypothèses, écriture de l'équation, \(\mathrm d\xi/\mathrm dt\) vers l'électrochimie), méthode 1, EXO 01, cartes |
| Vitesse à différentes dates par méthode graphique ou numérique | ❌ | §2 (tangente, différence centrée, bruit, figure), §12, méthode 2, EXO 05, EXO 11 |
| Facteurs cinétiques concentration et température | liste | §3 (trempe chiffrée, réfrigérateur, figure \(k(T)\)) |
| Lois de vitesse : sans ordre, ordre 0, 1, 2, ordre global, ordre apparent ; exprimer la loi, déterminer \(k\) | §2 | §4 (unités de \(k\), H₂ + Br₂, NO + O₂), §5, §6 (proportions stœchiométriques, piège du coefficient 2), méthode 3, EXO 02 à 04 |
| Temps de demi-vie d'un réactif, temps de demi-réaction ; ordre par les \(t_{1/2}\) | formules | §7 (définitions distinctes, \(t_{1/2} \propto [\mathrm A]_0^{1-n}\), demi-réactions successives, figure), méthode 4, EXO 06 |
| Dégénérescence de l'ordre, conditions stœchiométriques ; proposer des conditions simplificatrices | 1 paragraphe | §6, §8 (fil rouge, excès 10 ou 100, figure exacte / pseudo-ordre), méthode 7, EXO 08 |
| Établir une loi de vitesse à partir du suivi d'une grandeur physique | ❌ | §9 (absorbance, pression, conductivité), méthode 8, EXO 07, 08, 11, concours |
| Méthode différentielle ; confirmer par la méthode intégrale | §2 | §10 (vitesses initiales, figure des trois tracés, validation par les écarts normalisés, piège du \(R^2\)), méthodes 5-6, EXO 03, 05 |
| Loi d'Arrhenius ; énergie d'activation | §3 | §11 (données de N₂O₅, régression, extrapolation), méthode 9, EXO 09, 10, concours |
| Capacité numérique : exploiter des mesures par un programme | ❌ | §12 (3 programmes testés : différences centrées + `polyfit`, méthode intégrale + écarts normalisés, Arrhenius ; renvois à `pynum` §5 et `incertitudes` §5, §9, §10), méthode 10, EXO 11, concours D |
| Hors programme (mécanismes, AEQS, catalyse, ordre quelconque) | §4 signalé | fin de chapitre, avec un profil énergétique |

## Contenu
- **Cours** : « AU PROGRAMME · PTSI » + 12 sections + « Pour aller plus loin » ; 18 exemples traités, 7 figures calculées
  (tangentes, trois ordres à même \(v_0\) avec demi-réactions successives, méthode intégrale en trois tracés, droite d'Arrhenius,
  \(k(T)/k(25\,°\mathrm C)\) pour trois \(E_a\), dégénérescence exacte contre pseudo-ordre, profil énergétique), 3 programmes testés.
  Fil rouge : décoloration du cristal violet (données inventées, \(k_{\text{app}} = 0{,}119 \pm 0{,}001\ \text{min}^{-1}\) par Monte-Carlo).
  ≈ 117 000 caractères (dont ≈ 60 000 de figures).
- **Méthodes** : 10 au programme + 1 hors programme, chacune avec un exemple éclair vérifié ; 5 pièges.
- **Exercices** : 01 vitesses (oxydation de NH₃) ; 02 ordre 1 (ancien 01) ; 03 ordre 2 graphique (ancien 02, + demi-réactions
  successives) ; 04 ordre 0 (NH₃ sur tungstène, pression totale) ; 05 différences centrées et méthode différentielle ; 06 demi-réactions
  successives ; 07 suivi par la pression (peroxyde de di-tert-butyle, ancien 05 refait) ; 08 dégénérescence (S₂O₈²⁻ + I⁻,
  spectrophotométrie, proportions stœchiométriques) ; 09 Arrhenius (ancien 03) ; 10 ordre 1 et Arrhenius (ancien concours) ;
  11 capacité numérique (hydrolyse d'un chloroalcane suivie par conductimétrie, programme testé) ; **Concours PT** « Date de
  péremption d'un médicament » (4 parties : ordre par méthode intégrale, Arrhenius, extrapolation à 25 °C et 5 °C, programme) ;
  puis hors programme : 12 (ancien 04) et 13 (ancien 06).
- **Cartes** : 13 ajoutées (vitesses de consommation et de formation, hypothèses de la vitesse de réaction, réaction sans ordre,
  unité de \(k\) pour l'ordre \(n\), loi intégrée de 2 A → produits, proportions stœchiométriques, \(t_{1/2} \propto [\mathrm A]_0^{1-n}\),
  demi-réactions successives, suivi par une grandeur physique, différence centrée, intérêt de la méthode intégrale, ordres de
  grandeur de \(E_a\), Arrhenius en Python). Rendu MathJax vérifié (`cin_cartes_rendu.js`) : aucune erreur.

## Contrôles
`verif_src.py` (3 panneaux) : aucune erreur ni « attention » ; `apercu_src.py` à 390 et 1 440 px (un par un) : `merr`, `brut`, `larges`
vides, aucune erreur JS, `scrollW` = largeur ; figures regardées en clair et en sombre (`cin_voir/`) et dans la page (captures) ;
`cin_tester_code.py` sur le cours et les exercices : sorties identiques aux commentaires ; `corriger_cartes.py --essai` (7) et
`ajouter_cartes.py --essai` (29 → 42) sans erreur.

## Notations
\(\xi\) avancement (mol), \(x = \xi/V\), \(\nu_i\) algébriques (comme `equilchim`) ; \(v\), \(v_{\text{cons}}(\mathrm A)\), \(v_{\text{form}}(\mathrm P)\) ;
\(k\), \(k_{\text{app}}\), ordres partiels \(\alpha\), \(\beta\), ordre global \(n\) ; \(t_{1/2}\) ; \(E_a\), \(A\) (facteur préexponentiel), \(R\) ;
grandeur suivie \(G\), \(G_0\), \(G_\infty\). Équations : « = » pour les bilans, « → » pour les réactions totales étudiées en cinétique et
les actes élémentaires (hors programme). Lois intégrées écrites pour A → produits (coefficient 1), cas du coefficient 2 traité en piège.

## Doutes
- Données réelles citées : constantes de N₂O₅ (Daniels et Johnston, 1921 ; \(E_a = 103\ \text{kJ·mol}^{-1}\)), \(k = 0{,}11\ \text{L·mol}^{-1}\text{·s}^{-1}\)
  pour la saponification de l'éthanoate d'éthyle à 25 °C, élimination de l'alcool ≈ 0,15 g·L⁻¹·h⁻¹, conductivités ioniques
  (Na⁺ 5,01 ; HO⁻ 19,8 ; CH₃COO⁻ 4,09 mS·m²·mol⁻¹), loi de Bodenstein pour H₂ + Br₂. Les autres données (cristal violet,
  peroxodisulfate, peroxyde, chloroalcane, principe actif) sont inventées mais plausibles ; elles sont présentées comme données.
- Mécanisme de l'oxydation de NO (pré-équilibre NO + O₂ ⇄ NO₃) : un des deux mécanismes proposés dans la littérature ; présenté
  comme « un mécanisme proposé », hors programme.
- Le cours dépasse 110 000 caractères à cause des figures (≈ 60 000) : à garder en tête pour la performance (le panneau est replié).
