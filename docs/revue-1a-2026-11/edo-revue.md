# `edo` (prefix `edo`) — compte rendu, 2026-11-22

Point 4 de l'audit (lot 7), `docs/audit-2026-11/maths-1a.md` (ligne « Équations différentielles linéaires » : « cadre réel
seulement (K ∈ ℝ), alors que le programme prend a, b, f complexes » ; notation de l'amortissement). Cours réécrit en entier au
format de la 1ʳᵉ année, méthodes et exercices complétés, cartes relues, corrigées et complétées.

## Fichiers produits

| Fichier | Contenu |
|---|---|
| `edo-cours.src.html` | cours complet (≈ 106 000 car., dont ≈ 57 000 de SVG ; 11 sections + « Pour aller plus loin », 14 exemples, 5 figures) — construit par `edo_construire.py` depuis `edo-cours.tpl.html` et `edo_figs.json` |
| `edo-meth.src.html` | 10 méthodes + 2 encadrés « Piège » + pièges récapitulés |
| `edo-exos.src.html` | 11 exercices + 1 « Concours PT » (EXO 01-06 conservés, passés en variable \(t\) ; 07-11 nouveaux ; concours remplacé) |
| `edo-cartes-corr.json` | 6 cartes corrigées (réponse seule) |
| `edo-cartes-ajout.js` | 13 cartes nouvelles (40 → 53) |
| Scripts | `edo_calculs.py` (42 contrôles sympy/scipy du cours, dont le critère de stabilité par balayage), `edo_calculs_exos.py` (49 contrôles : méthodes, exercices, concours), `edo_figs.py`, `edo_construire.py` ; rendu des cartes par `prim_cartes_rendu.py` (0 erreur) ; copies des panneaux d'origine `edo_orig_{cours,meth,exos}.html` |

## Erreurs et défauts corrigés

1. **Cadre réel seulement** : le programme prend \(a\), \(b\), \(f\) réels **ou complexes**. Ajouts : solutions complexes de
   l'homogène d'ordre 1 (\(K \in \mathbb C\), exemple \(y' - i\omega y = 0\)), §6 entier sur l'ordre 2 à coefficients complexes
   (avec une démonstration du théorème par abaissement de l'ordre, sans algèbre linéaire), passage des solutions complexes aux
   solutions réelles démontré (§7), second membre \(A\,\mathrm e^{\lambda t}\) avec \((A, \lambda) \in \mathbb C^2\), EXO 10
   (particule chargée : équation \(W' = -i\omega W\)).
2. **Notations** : l'ancien cours écrivait \(a y'' + b y' + c y\), contraire au programme (\(y'' + a y' + b y = f\)) et au chapitre
   de 2ᵉ année `edo2a` ; aligné, avec la variable \(t\) comme `edo2a` et la physique. L'oscillateur était écrit avec le \(\xi\) des
   sciences de l'ingénieur ; la correspondance est maintenant donnée une fois, avec les deux notations (\(Q\), \(\omega_0\) en
   physique, \(\xi = \frac{1}{2Q}\) en SI), le cours restant en \(a\), \(b\).
3. **Hors-programme présenté comme exigible** : le second membre \(P(x)\,\mathrm e^{\alpha x}\) (le programme ne demande que
   polynôme, \(A\,\mathrm e^{\lambda x}\), \(B\cos\omega x\), \(B\sin\omega x\)) : passé en « Pour aller plus loin », carte 20 préfixée.
   L'ancienne méthode 1 affirmait qu'une équation non linéaire se ramène « en pratique » au linéaire par changement de variable :
   retiré.
4. **EXO 04 Q1** : la correction utilisait \(c\) à la fois pour le coefficient de \(y\) et pour une inconnue (« \(c = 2 \neq 0\), donc
   on cherche \(y_p = ax^2 + bx + c\) ») ; inconnues renommées \(\alpha\), \(\beta\), \(\gamma\).
5. **« Concours PT »** : deux questions immédiates (ordre 1 constant, ordre 2 homogène). Remplacé par un problème en quatre parties
   sur \(y'' + 2\alpha y' + y = f\) (régimes, stabilité, réponse à un échelon et dépassement de 16,3 %, régime forcé et condition
   de résonance \(\alpha \lt \frac{1}{\sqrt2}\), résonance sans amortissement, correspondance \(Q = \frac{1}{2\alpha}\), \(\xi = \alpha\)).
6. **Cartes fausses ou ambiguës** (réponses corrigées, questions inchangées) :
   - 20 (\(P(x)e^{\alpha x}\)) : préfixe « Hors programme en PTSI (pour aller plus loin) » ;
   - 21 (Cauchy, ordre 2) : « une seule solution sur \(\mathbb R\) » sans hypothèse sur \(f\) → \(f\) continue sur un intervalle \(I\), solution sur \(I\) ;
   - 24, 25 (régimes, pseudo-pulsation) : \(\xi\) seul → correspondance avec \(Q\) de la physique ;
   - 32 : « résonance d'amplitude » confondue avec le cas résonant des mathématiques (\(\lambda\) racine) → les deux sens distingués ;
   - 39 : « \(y_p = A/(\omega_0^2 - \omega^2)\cos(\omega x)\) » avec un \(A\) non défini (l'équation a pour second membre \(\cos\omega x\)) → \(\frac{\cos(\omega x)}{\omega_0^2 - \omega^2}\), et le cas \(\omega = \omega_0\).

Les exercices EXO 01 à 06 d'origine sont justes (recalculés en sympy) et conservés.

## Couverture du programme avant → après

| Capacité (programme PTSI, S1) | Avant | Après |
|---|---|---|
| Ordre 1 \(y' + a(t)y = b(t)\), \(a\), \(b\) réels ou complexes, équation homogène | 🔶 (réel) | ✅ §1 (vocabulaire, forme résolue, exemples de physique), méthode 1 |
| Ensemble des solutions de l'homogène ; cas \(a\) constant | ✅ (sans démonstration) | ✅ §2 (démonstration, constante de temps, cas complexe), méthode 2, EXO 01, 06 |
| Principe de superposition ; structure \(y_p + y_h\) | ✅ | ✅ §3 (démonstration, passage aux complexes justifié), méthode 8, EXO 09 |
| Variation de la constante | ✅ | ✅ §4 (démonstration, deux exemples dont un non devinable, maison en régime sinusoïdal), méthodes 3-4, EXO 02, 07, 08 |
| Existence et unicité, problème de Cauchy (ordre 1) | ✅ (énoncé) | ✅ §5 (démonstration, courbes intégrales qui ne se croisent pas, charge RC, contre-exemple d'équation non résolue), méthode 9 |
| Ordre 2 à coefficients constants, solutions de l'homogène (cas complexe) | ❌ | ✅ §6 (démonstration), méthode 5, carte |
| Solutions réelles si \(a\), \(b\) réels | ✅ | ✅ §7 (démonstration, figure des trois régimes, amplitude-phase, correspondance \(Q\) / \(\xi\)), EXO 03, concours A |
| Solution particulière : polynôme, \(A\,\mathrm e^{\lambda t}\) (\(\mathbb C\)), \(B\cos\omega t\), \(B\sin\omega t\) | ✅ (réel, plus \(P e^{\alpha x}\) hors programme) | ✅ §8 (formules justifiées, résonance avec figure), méthodes 6-7, EXO 04, 05, 09, concours C, D |
| Existence et unicité, problème de Cauchy (ordre 2, démonstration hors programme) | ✅ | ✅ §9 (méthode, réponse à un échelon avec figure, amplitude-phase), méthode 9, EXO 05, 09 |
| Exemples des autres disciplines (bandeau de la section) | 🔶 (RC) | ✅ §1, §4, §5, §7, §10 (stabilité, régimes transitoire et permanent, RLC), EXO 06, 08, 10, concours |
| Méthode d'Euler (bandeau de la section « Dérivabilité » ; capacité de physique) | ❌ | ✅ §11 (figure, renvois `pynum` §6-7 et `premierordre` §9), EXO 11 |

## Cours

AU PROGRAMME · PTSI · §1 Équations différentielles linéaires · §2 Premier ordre : l'équation homogène · §3 Structure des solutions et
principe de superposition · §4 Premier ordre : solution particulière · §5 Problème de Cauchy à l'ordre 1 · §6 Second ordre :
solutions complexes · §7 Second ordre : solutions réelles · §8 Second ordre : solution particulière · §9 Problème de Cauchy à
l'ordre 2 · §10 Stabilité, régimes transitoire et permanent · §11 La méthode d'Euler · Pour aller plus loin (\(P(t)e^{\lambda t}\),
coefficients variables et wronskien en 2ᵉ année, variables séparables, non linéaire et explosion de \(y' = y^2\)). Figures calculées :
courbes intégrales de \(y' + y = t\) ; trois régimes de \(y'' + ay' + y = 0\) ; résonance \(t\sin(2t)/4\) contre régime amorti borné ;
réponse à un échelon de \(y'' + 2y' + 5y = 5\) (dépassement de 21 %, bande ±5 %) ; Euler pour \(y' + 2ty = 1\) (solution sans
primitive usuelle). Vérifiées en clair et en sombre, à 390 et 1440 px.

## Méthodes (10)

Reconnaître l'équation et la mettre sous forme résolue ; homogène d'ordre 1 ; solution particulière d'ordre 1 à coefficient
constant ; variation de la constante ; homogène d'ordre 2 ; second membre polynôme ou exponentiel ; second membre sinusoïdal
(complexes, résonance) ; superposition ; problème de Cauchy ; lire une équation de physique (\(\omega_0\), \(Q\), \(\xi\), stabilité,
durée du transitoire).

## Exercices (12)

EXO 01-06 conservés (variable \(t\), notations du cours) ; nouveaux : 07 deux équations à coefficients variables (\(\tan\), \(\frac{\sin t}{t}\),
seule solution bornée en 0), 08 circuit RC en régime sinusoïdal (amplitude 0,30 E, retard 72°, transitoire < 1 % après 3,4 τ),
09 superposition et résonance, 10 particule chargée dans un champ magnétique (équation complexe, rayon \(\frac{mv_0}{qB}\) ≈ 10 cm
pour un proton), 11 méthode d'Euler (erreur d'ordre 1, condition \(h \lt 2\)) ; Concours « Un oscillateur amorti : régimes,
dépassement, résonance ».

## Cartes

Corrigées (6, réponse seule) : 20, 21, 24, 25, 32, 39 (voir ci-dessus). Ajoutées (13) : problème de Cauchy à coefficients
constants, \(B\,\mathrm e^{\lambda t}\) à l'ordre 1, passage aux complexes, solutions complexes à l'ordre 2, \(A\,\mathrm e^{\lambda t}\)
selon la multiplicité, régime sinusoïdal forcé et amplitude, forme amplitude-phase, critère de stabilité, correspondance \(Q\) / \(\xi\),
méthode d'Euler, durée du transitoire (`cat:'val'`), variables séparables (capacité de physique, non exigible en maths),
variation des constantes à l'ordre 2 (« Hors programme en PTSI »).

## Notations

Celles du programme et de `edo2a` : \(y' + a(t)\,y = b(t)\), \(y'' + a\,y' + b\,y = f(t)\), \(\mathbb K = \mathbb R\) ou \(\mathbb C\),
\(A\) primitive de \(a\), solutions homogènes \(K\,\mathrm e^{-A(t)}\), équation caractéristique \(r^2 + ar + b = 0\), racines
\(\alpha \pm i\beta\), constantes \(\lambda\), \(\mu\) ; \(\chi(r) = r^2 + ar + b\) seulement dans une justification et la méthode 6.
Correspondance avec la physique (\(\omega_0\), \(Q\), \(\tau\), notations de `oscill` et `premierordre`) et les SI (\(\xi\)) donnée
une fois (§7), puis en méthode 10 et au concours. Frottement noté \(h\) (et non \(\alpha\), réservé ici à la partie réelle des racines).

## Doutes

- **Variable** : le cours, les exercices et les cartes nouvelles utilisent \(t\) (comme `edo2a` et la physique) ; les 40 cartes
  d'origine gardent \(x\) et l'ancienne écriture \(ay'' + by' + cy\) (justes, donc non modifiées pour préserver la progression).
  On pourrait les harmoniser plus tard par des retouches de texte à rang inchangé (sans perte de progression).
- Le **critère de stabilité** et les régimes transitoire / permanent ne figurent pas dans la section de mathématiques, mais dans les
  outils mathématiques de physique (« prévoir le caractère borné… ») : présentés comme exemples issus des autres disciplines,
  comme le demande le bandeau du programme.
- La **méthode d'Euler** n'est pas une capacité exigible de mathématiques (suggestion du programme) ; elle l'est en physique et en
  informatique : section courte, avec renvois.
- L'audit parlait d'un « ζ » dans `edo` §3 : le site écrivait en fait \(\xi\) ; la remarque reste valable (notation des SI dans un
  contexte de physique) et elle est traitée.
