# Chapitre `logique` (prefix `log`) — « Logique, ensembles, applications » — compte rendu

Rédigé le 2026-11-22 (point 4 de l'audit, lot 6 ; `docs/audit-2026-11/maths-1a.md` lignes 12, 13, 15, 72, 113).
Chapitre existant de 1ʳᵉ année, partie « Logique et calculs » des maths, juste avant `calculs` (lot 4).

## Fichiers
- `log-cours.src.html` (≈ 81 000 car., dont ≈ 29 000 de figures) : construit par `log_construire.py` à partir de
  `log-cours.tpl.html` et `log_figs.json` (`log_figs.py`, outil `log_svg.py`, copie de `calc_svg.py`) ; retouches
  `log_retouches1.py` à `log_retouches5.py` (formules passées en bloc, déjà appliquées).
- `log-meth.src.html` (10 méthodes), `log-exos.src.html` (11 exercices + 1 « Concours PT »).
- `log-cartes-corr.json` (1 carte), `log-cartes-ajout.js` (15 cartes : 25 → 40).
- Contrôles : `log_calculs.py` (21 286 vérifications, sympy et énumérations exhaustives sur toutes les parties d'un
  ensemble à 4 éléments, toutes justes), `log_cartes_rendu.py` (74 formules des cartes rendues, 0 erreur MathJax),
  `log_voir.py` (captures des figures, clair et sombre), `log_deborde5.js` (recherche d'un débordement à 390 px).
- `verif_src.py` : aucune erreur ni « attention » ; `apercu_src.py` à 390 et 1440 px : `merr`, `brut`, `larges` vides,
  aucune erreur JS, largeur de page 390 au téléphone ; `corriger_cartes.py --essai`, `ajouter_cartes.py --essai` sans erreur.

## Erreurs trouvées et corrigées
- Cours d'origine : relations d'équivalence et d'ordre exposées dans le §2 (hors programme : le programme de PTSI exclut
  « toute étude systématique de la logique, de la théorie des ensembles » ; seules la relation d'ordre de ℝ et la
  congruence modulo 2π y figurent) → déplacées en fin de chapitre (« Pour aller plus loin »).
- EXO 01 Q3 : la proposition à nier n'avait pas de quantificateur sur \(x\) (« ∀ε, ∃η, |x − a| < η ⇒ … ») → « ∀x ∈ I »
  ajouté, et la correction le commente.
- EXO 02 : « gcd(p, q) = 1 » (notation anglaise) → fraction irréductible ; les implications « p² pair ⇒ p pair » et
  « 3 | p² ⇒ 3 | p » étaient affirmées sans justification → renvoi au §4 (contraposée, disjonction des cas).
- EXO 06 Q2 : l'initialisation affirmait « F₁ = 1 = φ¹ » (faux : 1 < 1,618) → inégalité, et version plus fine
  \(F_n \le \varphi^{n-1}\) signalée. Q3 (PGCD de deux termes consécutifs) doublait l'exercice « Concours PT » de
  `calculs` → remplacée par l'identité de Cassini (avec renvoi).
- Concours d'origine : A1 (Σk³ par récurrence) doublait `calculs` EXO 03 → retiré ; B1-B2 (homographie
  \(x \mapsto \frac{x+1}{x-1}\) involutive) repris et généralisés dans la partie A du nouveau concours.
- Carte 4 : coquille « irrationnalité » (réponse seule corrigée).

## Couverture du programme (avant → après)
| Capacité du programme de PTSI | Avant | Après |
|---|---|---|
| Connecteurs, tables de vérité, De Morgan logique | §1 (bref) | §1 (table complète, formule, démonstration), EXO 01, cartes |
| Implication, contraposition, équivalence, négation | §1 | §2, méth. 1-3, EXO 01 |
| Condition nécessaire, condition suffisante | absent | §2 (exemples x = 2 / x² = 4, multiple de 6 / pair), §5, carte |
| Quantificateurs, ordre, négation, pas d'abréviation | §1 | §3 (traductions, contre-exemple n² + n + 41), méth. 1, EXO 07 |
| Direct, contraposition, absurde, disjonction des cas | §1 (liste) | §4 (3 exemples), méth. 2, 4, 5, EXO 02 |
| Analyse-synthèse | absent | §5 (√(x + 2) = x, décomposition paire-impaire démontrée), méth. 6, EXO 08 |
| Récurrence simple, double, forte | §4 (énoncés) | §6 (Bernoulli, 2ⁿ − 1, récurrence forte), méth. 7, EXO 03, 06, concours C3 |
| Ensemble, inclusion, double inclusion, 𝒫(E) | partiel, 𝒫(E) absent | §7 (𝒫({a, b, c}), ∈ / ⊂), EXO 05 Q4, carte |
| Réunion, intersection, différence, complémentaire, produit cartésien | §2 | §8 + figure de Venn (démonstration de De Morgan), EXO 05 |
| Recouvrement disjoint, partition | absent | §8 + figure, EXO 05 Q5, concours B2, carte |
| Application, graphe, ℱ(E, F) = Fᴱ, famille | absent | §9 |
| Indicatrice | absent | §9 (règles, démonstration, tableau, lien avec les cardinaux), méth. 10, EXO 11 |
| Restriction, prolongement, composition | composition seule | §9, carte |
| Image directe, image réciproque | 1 ligne | §10 + figure calculée, propriétés démontrées, méth. 9, EXO 09 |
| Injection, surjection, bijection, réciproque, composées, (g∘f)⁻¹ | §3 | §11 + figure sagittale, démonstrations, méth. 8, EXO 04, 10, concours A |
| Compatibilité des deux sens de f⁻¹ | absent | §11 |

Hors programme regroupé en fin de cours : relations binaires, d'équivalence (classes = partition) et d'ordre (total,
partiel). Une carte HP, préfixée « Hors programme en PTSI : ».

## Sections du cours
Bloc « AU PROGRAMME · PTSI » ; §1 Propositions et connecteurs ; §2 Implication, contraposée, équivalence (CN, CS) ;
§3 Quantificateurs ; §4 Modes de raisonnement ; §5 Analyse-synthèse ; §6 Récurrence ; §7 Ensembles, parties, 𝒫(E) ;
§8 Opérations, produit cartésien, partitions ; §9 Applications (graphe, familles, indicatrices, restriction,
prolongement, composition) ; §10 Image directe, image réciproque ; §11 Injections, surjections, bijections ;
Pour aller plus loin. 16 exemples traités (au moins un par section, tous contrôlés), 9 blocs dépliables, une « erreur
classique » par section. Figures calculées (classes du site, vues en clair et en sombre) : Venn de De Morgan, partition
de {1, …, 12} par les restes modulo 3 et contre-exemple, images directe et réciproque par x ↦ x², quatre diagrammes
sagittaux. Le chapitre contient désormais des formules en bloc à retenir (`data-nom`) : De Morgan (logique et
ensembles), contraposée, négation des quantificateurs, distributivité, parties paire et impaire, indicatrices, image
réciproque, réciproque d'une composée.

## Méthodes (10, contre 3 listes sans exemple)
Nier ; démontrer une implication ; équivalence et égalité d'ensembles ; absurde ; disjonction des cas ;
analyse-synthèse ; rédiger une récurrence ; injectivité, surjectivité, bijectivité ; images directe et réciproque ;
indicatrices. Chacune avec un exemple éclair chiffré et vérifié, 5 pièges.

## Exercices (12)
01-06 d'origine corrigés (01 enrichi : quantificateur ; 03 : Q3 sur le rôle de l'initialisation ; 05 : Q4 𝒫(E), Q5
partitions ; 06 : Cassini) ; 07 quantificateurs vrai/faux ; 08 analyse-synthèse (équation fonctionnelle
f(x) + 2f(−x) = x² + x, décomposition paire-impaire, f(x)f(y) − f(xy) = x + y) ; 09 images directes et réciproques
(défauts d'injectivité et de surjectivité) ; 10 composées et injectivité/surjectivité (n ↦ 2n, n ↦ ⌊n/2⌋) ;
11 indicatrices et différence symétrique (associativité, simplification, cardinal) ; Concours PT « Involutions d'un
ensemble » (A : bijectivité, exemples, homographie \(f_a\) ; B : partition en orbites, parité de |E| − |Fix f| ;
C : \(I_n = I_{n-1} + (n-1)I_{n-2}\), \(I_n \ge \sqrt{n!}\) par récurrence double, fonction Python ; vérifié par
énumération exhaustive jusqu'à n = 8).

## Cartes
Corrigée (réponse seule) : 4. Ajoutées (15) : CN/CS, négation de l'implication, De Morgan logique, analyse-synthèse,
récurrence double, 𝒫(E), partition, indicatrices, restriction/prolongement, images directe et réciproque,
f(A ∩ A'), composées d'injections/surjections, (g∘f)⁻¹, méthode de bijectivité, relation d'équivalence (HP).

## Notations
non, et, ou (¬, ∧, ∨ cités) ; \(\overline A\), \(E \setminus A\), \(A^c\) ; \(\mathcal P(E)\) ; \(\mathbf 1_A\) et
\(|A|\) comme `denombrmt` ; \(f_{|A}\), \(\mathcal F(E, F)\), \(F^E\), \(\mathrm{id}_E\) ; \(\operatorname{pgcd}\)
(renvoi à `calculs`).

## Renvois
`calculs` (sommes, arithmétique, ordre de ℝ), `denombrmt` (|𝒫(E)| = 2ⁿ, cardinaux, finis de même cardinal),
`fonctions` (ch, sh, congruence modulo 2π), `contderiv` (prolongement par continuité), `proba` (système complet).

## Doutes
- Le programme parle de « recouvrement disjoint » sans le définir ; j'ai pris la définition usuelle (parties deux à
  deux disjointes de réunion E, éventuellement vides), la partition exigeant en plus des parties non vides.
- Le titre du chapitre est gardé tel quel.
