# Revue et réécriture : `equilchim` (prefix `eq`), « Équilibres chimiques » — 2026-11-22

Point 4 de l'audit, lot 6 (`docs/audit-2026-11/physique-1a.md` l. 54, 81, 113, 133, 137, 143 ; `docs/audit-2026-11.md` §5).
Programme : PTSI 2021, partie 4.1.1 « Description d'un système et de son évolution vers un état final »
(`pdf-pt/prog/ptsi.txt`, l. 1086-1133), avec la capacité numérique. Vérifié dans le programme de PT
(`phys.txt`, l. 1575-1640) : Van 't Hoff et l'optimisation d'un procédé sont de 2ᵉ année ; le « principe de Le Chatelier »
n'est dans aucun des deux programmes. Rédaction originale, exemples et exercices inventés, toutes les valeurs recalculées.

## Fichiers (dans `AN1/`)
| Fichier | Contenu |
|---|---|
| `eq-cours.src.html` | construit par `eq_construire.py eq` depuis `eq-cours.tpl.html` + `eq_figs.json` + `eq_code/bloc1.py`, `bloc2.py` (code coloré) |
| `eq-meth.src.html` | 10 méthodes au programme + méthode 11 (Van 't Hoff) signalée hors programme, 4 pièges |
| `eq-exos.src.html` | depuis `eq-exos.tpl.html` + `eq_code/exo11.py`, `exo12.py` ; 11 exercices + « Concours PT » + 3 exercices hors programme en fin |
| `eq-cartes-corr.json`, `eq-cartes-ajout.js` | 10 réponses corrigées (questions inchangées), 15 cartes ajoutées en fin (30 → 45) ; générés par `eq_cartes.py` |
| `eq_figs.py` → `eq_figs.json` | 5 figures calculées |
| `eq_calculs.py`, `eq_calculs_meth.py`, `eq_calculs_exos.py` | vérification de tous les nombres (scipy `brentq`, sympy) |
| `eq_tester_code.py` | exécute chaque `<pre class="codeblock">` d'un fichier (sorties identiques aux commentaires) |
| `eq_couper.py`, `eq_voir.py`, `eq_cartes_rendu.js`, `eq_deck.py` | coupe des formules longues, aperçu des figures, rendu MathJax des cartes, lecture d'un deck |
| `eq_orig_{cours,meth,exos}.html` | copies des anciens panneaux |

## Erreurs et défauts trouvés (corrigés)
1. **Hors-programme au cœur du chapitre** (audit) : §2 entier sur Le Chatelier et Van 't Hoff, \(\Delta_rG^\circ = -RT\ln K^\circ\) au §3,
   \(K_p = K_c(RT)^{\Delta n}\) au §1 ; méthodes 2 et 3 sur 4, exercices 02, 03, 05 et le concours B. Tout est regroupé en
   « POUR ALLER PLUS LOIN » (cours), méthode 11 et EXO 12 à 14 (signalés « hors programme en PTSI »).
2. Ancien EXO 03 (Van 't Hoff) : \(e^{13{,}05} = 4{,}69\times10^5\) faux (4,6·10⁵) : \(K^\circ(500\ \text{K}) = 46\), pas 46,9 (devenu EXO 13).
3. Ancien EXO 05 : \(RT = 24{,}5\ \text{L·bar·mol}^{-1}\) à 298 K (c'est la valeur en L·atm ; 24,8 en L·bar) ; constante \(K_p = 0{,}14\ \text{bar}\)
   dimensionnée et différente des 0,15 du concours. Réécrit en EXO 07 avec \(K^\circ = 0{,}15\) (calcul de l'état final, au programme).
4. Ancien EXO 06 (AgCl dans NH₃) : \(s = 0{,}055\) en supposant \([\mathrm{NH_3}] = 1\), alors que \(2s\) consomme 11 % de l'ammoniac ;
   exact \(s = 0{,}050\ \text{mol·L}^{-1}\), facteur 3 700 et non 4 100 ; complexation non signalée hors programme. Corrigé (EXO 14).
5. Constantes : \(K_c\), \(K_p\) dimensionnées à côté de \(K^\circ\) (audit l. 137) : seul \(K^\circ\) sans dimension, avec \(c^\circ\) et \(P^\circ\),
   comme `acidobase`, `precipitation` et `thermochimie` ; « tableau ICE » remplacé par « tableau d'avancement ».
6. Cours sans figure, sans exemple chiffré, sans la capacité numérique, sans rupture d'équilibre : voir la couverture.
7. Cartes (réponse seule corrigée) : n° 8 (« \(K^\circ \ll 1\) : quasi totale dans le sens inverse » ambigu), n° 10 (\(\Delta_rG\) présenté en PTSI),
   n° 11 (ICE), n° 15 (\(\xi\) en mol comparé à \([A]_0\) en mol·L⁻¹), n° 21 (complexation non signalée), n° 22 (H⁺ au lieu de H₃O⁺),
   n° 24 (« étapes élémentaires » pour une combinaison d'équations), n° 7 (nuance : vérifier), n° 2 et 23 (préfixe harmonisé
   « Hors programme en PTSI »). **Carte fausse des deux côtés : n° 24** (sa question parle aussi d'« étapes élémentaires ») ; seule la
   réponse est corrigée (elle explique la confusion), la question est à reformuler plus tard, seule, pour garder la progression.

## Couverture du programme (PTSI 4.1.1), avant → après
| Capacité | Avant | Après |
|---|---|---|
| Recenser les espèces physico-chimiques ; composition (\(c\), \(x_i\), \(P_i\)) | ❌ | §1 (air, solution de sel), méthode 1, EXO 01 |
| Variables intensives et extensives | ❌ | §2 (mélange de solutions), EXO 01, carte |
| Écrire l'équation d'une ou plusieurs réactions | ❌ | §3 (ajustement, \(\nu_i\), plusieurs réactions), méthode 2, EXO 02 |
| Décrire un système dans un état d'avancement quelconque | 1 phrase | §4 (tableau, réactif limitant, \(\tau\), figure), méthode 3, EXO 02 |
| Activité (gaz parfait, soluté dilué, solvant, solide), état standard | liste | §5 (tableau, eau gazeuse, four à chaux), méthode 4, EXO 03 |
| Quotient réactionnel ; constante ; identifier un équilibre | §1 | §6 (loi d'action des masses, combinaison démontrée), méthodes 4-5, EXO 03, 05 |
| Déterminer une constante d'équilibre | ❌ | §6 (mesure de pression sur N₂O₄, eau gazeuse), méthode 5, EXO 05, concours C1 |
| Prévoir le sens d'évolution spontanée | liste | §7 (figure \(\log Q_r(\xi)\), gaz à l'eau, précipité), méthode 6, EXO 06 |
| État final : équilibre chimique | §3 (ICE) | §8 (3 exemples dont le 2ᵈ degré, pression fixée), méthode 7, EXO 04, 07, concours B |
| État final : transformation totale, approximations | 1 phrase | §9 (figure \(\tau(\log K^\circ)\), Zn/Cu²⁺, NO à 2 000 K), méthode 8, EXO 08, 10 |
| Rupture d'équilibre (systèmes hétérogènes) | ❌ | §10 (figure CaCO₃, AgCl), méthode 9, EXO 08, 09, concours C3 |
| Capacité numérique : état final par programme | ❌ | §11 (`zero_dicho` de `pynum` §2, fonction `etat_final` générale avec rupture, figure), méthode 10, EXO 11, concours D |

## Contenu
- **Cours** : « AU PROGRAMME · PTSI » + 11 sections (§1 système ; §2 intensif/extensif ; §3 équation ; §4 avancement ; §5 activité ;
  §6 quotient et constante ; §7 sens d'évolution ; §8 équilibre ; §9 totale, quasi totale, peu avancée ; §10 rupture d'équilibre ;
  §11 Python) + « Pour aller plus loin » (Van 't Hoff, \(\Delta_rG^\circ\), contre-exemple chiffré au « principe de Le Chatelier »
  — ajout de N₂ qui décompose NH₃ quand \(x_{\mathrm{N_2}} \gt 1/2\) —, \(K_c\) et \(K_p\)). 20 exemples traités, 5 figures calculées
  (avancement du propane, \(\log Q_r(\xi)\) pour deux états du gaz à l'eau, \(\tau(\log K^\circ)\) à trois dilutions, rupture CaCO₃,
  dissociation de N₂O₄ en fonction de \(P\)), 2 programmes exécutés et testés. ≈ 75 000 car.
- **Méthodes** : 10 au programme + 1 hors programme (Van 't Hoff), chacune avec exemple éclair vérifié.
- **Exercices** : 01 système (air humide) ; 02 aluminothermie, combustion de l'éthanol ; 03 quotients ; 04 HI (ancien EXO 01, + retour
  depuis HI) ; 05 PCl₅, constante par mesure de pression ; 06 sens d'évolution (dont l'ancien concours A) ; 07 N₂O₄ sous pression fixée
  (ancien EXO 05 refait) ; 08 zinc et cuivre(II) : quasi totale ou rupture ; 09 calcaire en four fermé ; 10 acide acétique (ancien EXO 04,
  approximation qui échoue à la dilution) ; 11 capacité numérique (ammoniac, \(\tau\) de 1 à 300 bar) ; **Concours PT** « Produire du
  dihydrogène » (4 parties : système, équilibre à 700 et 1 000 K, captage du CO₂ par CaO avec combinaison de constantes et rupture,
  programme) ; puis hors programme : 12 Haber-Bosch (ancien 02), 13 Van 't Hoff (ancien 03, corrigé), 14 AgCl/NH₃ (ancien 06, corrigé).
- **Cartes** : 15 ajoutées (espèce physico-chimique, pression partielle, intensif/extensif, \(n_i = n_{i,0} + \nu_i\xi\), réactif limitant,
  activité d'un gaz, loi d'action des masses, état d'équilibre, déterminer \(K^\circ\), constante inverse ou multipliée, unicité de
  l'état final, rupture, trancher équilibre/totale, « \(Q_r \lt K^\circ\) ne suffit pas », programme). Les cartes à texte mêlé sont écrites
  avec au moins une formule `\\( … \\)` pour que `flashPretty` ne mathématise pas les états (g), (ℓ) ni les nombres (rendu MathJax vérifié).

## Contrôles
`verif_src.py` (3 panneaux) : aucune erreur ni « attention » ; `apercu_src.py` à 390 et 1 440 px (un par un) : `merr`, `brut`, `larges`
vides, aucune erreur JS, `scrollW` = largeur ; figures regardées en clair et en sombre (`eq_voir/`) ; `corriger_cartes.py --essai`
(10) et `ajouter_cartes.py --essai` (30 → 45) sans erreur ; `eq_cartes_rendu.js` : aucune erreur MathJax.

## Notations
\(\xi\) (avancement, mol), \(x = \xi/V\), \(\nu_i\) algébriques et \(0 = \sum\nu_i\mathrm A_i\) (comme `thc` §1), \(n_{i,0}\), \(\xi_{\max}\), \(\xi_{\min}\),
\(\tau = \xi_f/\xi_{\max}\), \(\alpha\) (taux de dissociation), \(a_i\), \(Q_r\), \(K^\circ(T)\), \(P^\circ = 1\ \text{bar}\), \(c^\circ = 1\ \text{mol·L}^{-1}\),
équations écrites avec « = » et états (g), (ℓ), (s), (aq). Code : `zero_dicho` identique à `pynum` §2.

## Doutes
- Valeurs de \(K^\circ\) arrondies et présentées comme données : gaz à l'eau 9,0 (700 K) et 1,4 (1 000 K) ; CaCO₃ 0,20 (1 073 K) et 1,0
  (1 173 K), \(1{,}0\times10^{-5}\) (700 K) ; ammoniac \(4{,}6\times10^{-5}\) (723 K) ; PCl₅ 1,80 (523 K) ; I₂ sublimation \(4{,}1\times10^{-4}\) ;
  NO \(4{,}0\times10^{-4}\) (2 000 K). Elles varient de quelques dizaines de % selon les tables.
- Zn + Cu²⁺ : \(K^\circ = 10^{37}\) (avec 0,059 V) ; `oxred` écrit « ≈ 10³⁶ » (0,06 V) : à harmoniser lors de sa reprise.
- EXO 07 Q3, EXO 11 et §11 font varier la pression : c'est un calcul d'état final (PTSI) ; la notion d'« optimisation » reste en 2ᵉ année.
- L'ordre du groupe Chimie place `cinetique` avant `equilchim`, alors que le programme commence par 4.1.1 : à rediscuter (`CHAP_GROUPS`).
