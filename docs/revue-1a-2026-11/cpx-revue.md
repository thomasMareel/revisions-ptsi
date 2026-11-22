# Chapitre `complexes` (prefix `cpx`) — « Nombres complexes » — compte rendu

Rédigé le 2026-11-22 (point 4 de l'audit, lot 8 ; `docs/audit-2026-11/maths-1a.md` ligne « Nombres complexes (a à h) »,
§3 « Plus bref », §4 coquilles). Le cours d'origine (≈ 16 600 car., 5 sections, aucun encadré « Au programme ») est
**réécrit en entier** au format de la 1ʳᵉ année ; méthodes refaites (10), exercices complétés (11 + Concours) ; cartes
relues, 2 corrigées, 14 ajoutées. L'onglet Simulateur (`drawCplx`, plan complexe) n'est pas touché ; le cours y renvoie.

## Fichiers
- `cpx-cours.src.html` (≈ 78 000 car. dont ≈ 26 000 de figures) : `cpx_construire.py` assemble `cpx-cours.tpl.html` et
  `cpx_figs.json` (`cpx_figs.py`, outil `cpx_svg.py` = copie de `calc_svg.py` + arcs et cercles). Retouche : `cpx_retouches1.py`.
- `cpx-meth.src.html` (10 méthodes), `cpx-exos.src.html` (11 exercices + « Concours PT » ; EXO 01-05 d'origine gardés,
  EXO 06 adapté, nouveaux rédigés dans `cpx_exos_nouveaux.html` puis assemblés), `cpx-cartes-corr.json` (2 cartes),
  `cpx-cartes-ajout.js` (14 cartes, 42 → 56).
- Contrôles : `cpx_calculs.py` (67 vérifications du cours), `cpx_calculs_meth.py` (23), `cpx_calculs_exos.py` (43, anciens
  exercices compris) : toutes justes. `cpx_cartes_rendu.py` (formules des cartes : 0 erreur MathJax), `cpx_larges.js`,
  `cpx_deborde*.js` (formules trop larges au téléphone), `cpx_voir.py` (figures en clair et en sombre).
  Copies des panneaux d'origine : `cpx_orig_cours.html`, `cpx_orig_meth.html`, `cpx_orig_exos.html`.
- `verif_src.py` : aucune erreur ni « attention » sur les trois fichiers ; `apercu_src.py` à 390 et 1440 px : `merr`,
  `brut`, `larges` vides, aucune erreur JS, pas de débordement de page (les figures à deux panneaux défilent au
  téléphone, comme ailleurs sur le site).

## Erreurs et hors-programme corrigés
- **Similitudes** (méthode 7 d'origine, EXO 06 « hors programme ») : la méthode « géométrie » ne garde que translations,
  homothéties, rotations (de centre quelconque, par \(\omega + e^{i\alpha}(z - \omega)\)) et conjugaison ; l'étude générale
  de \(z \mapsto az + b\) passe en « Pour aller plus loin · hors programme ». L'EXO 06 est **adapté** au programme :
  même application, décrite comme composée d'une rotation et d'une homothétie de même centre (outils du programme),
  avec une remarque renvoyant au hors-programme.
- **Carte 6** (inégalité triangulaire) : « colinéaires positivement (mêmes argument) » — coquille, et faux si l'un des
  deux est nul (pas d'argument). Réponse corrigée : \(z' = 0\) ou \(z = \lambda z'\), \(\lambda \ge 0\).
- **Carte 41** (similitude) : réponse préfixée « Hors programme en PTSI (pour aller plus loin) : » (convention de la
  1ʳᵉ année) et complétée par \(f(z) - \omega = a(z - \omega)\). Seules les réponses changent ; aucune carte fausse des
  deux côtés.
- Coquille de l'audit « C'est l'algèbrement clos » : absente du nouveau texte ; d'Alembert-Gauss est renvoyé à
  `polynomes` §9 (où il est au programme, démonstration hors programme).
- Cours d'origine : « argument = arctan(b/a) si a > 0 … » et pièges épars repris en encadrés « Erreur classique » ;
  « argument principal » donné comme simple convention (absent du programme).
- Le cours d'origine plaçait la trigonométrie (linéarisation, angle moitié) sans renvoi à `fonctions` §8, ne donnait pas
  la factorisation de \(P(z)\) par \(z - a\), ni la brève extension de \(\sum x^k\), \(a^n - b^n\) et du binôme, ni
  \(\cos p \pm \cos q\), ni la démonstration des sommes \(\sum\cos(kt)\) : ajoutés.

## Couverture du programme (avant → après)
| Capacité du programme de PTSI (« Nombres complexes ») | Avant | Après |
|---|---|---|
| a) Re, Im, opérations ; brève extension de Σxᵏ, aⁿ − bⁿ, binôme ; affixe d'un point, d'un vecteur | §1 (sans l'extension) | §1 + figure, méth. 1, EXO 01, cartes |
| b) Conjugaison, image du conjugué ; module, \|z\|² = z z̄, produit, quotient ; \|z − z₀\|, cercles et disques ; inégalité triangulaire et cas d'égalité | §1 (cas d'égalité approximatif) | §2 + figure, démonstration du cas d'égalité, méth. 1, EXO 11 Q4, carte 6 corrigée |
| c) 𝕌, e^{it}, exponentielle d'une somme, Euler, angle moitié (1 ± e^{it}, e^{ip} ± e^{iq}, retrouver cos p ± cos q, sin p ± sin q), linéarisation, Σcos(kt), Σsin(kt), Moivre, cos(nt) et sin(nt) | §2, §4 (sans cos p ± cos q, Σ en exercice seulement) | §3 (figure), §5 (figure, 4 factorisations), §6 (figure, linéarisation, Moivre, sommes démontrées) ; méth. 3-6 ; EXO 04, 05, 07, 08 ; Concours B ; cartes |
| d) Forme trigonométrique, arguments d'un produit, d'un quotient ; a cos t + b sin t = A cos(t − φ) | §2, §4 | §4 + figure (produit = rotation + dilatation), méth. 2 et 7 |
| e) Factorisation de P(z) par z − a ; racines carrées sous forme algébrique ; second degré, somme et produit | §3 (sans la factorisation) | §7 (démonstrations), méth. 8, EXO 02, 09 Q2, cartes |
| f) Racines n-ièmes de l'unité (𝕌ₙ), d'un complexe ; représentation | §3 | §8 + figure, méth. 9, EXO 03, 09, Concours A |
| g) e^z, module et arguments, e^{z + z'}, e^z = e^{z'} ⟺ z − z' ∈ 2iπℤ | §2 (définition seule) | §9 + figure, méth. 9, EXO 10, cartes |
| h) Module et argument de (c − a)/(b − a), alignement, orthogonalité ; z ↦ az, z ↦ z + b ; conjugaison ; similitudes hors programme | §5 | §10 + figure, méth. 10, EXO 06, 11 ; similitudes en fin de cours |

## Cours (10 sections, 9 figures calculées)
Bloc « AU PROGRAMME · PTSI » ; §1 Forme algébrique et plan complexe (figure : affixe d'un vecteur, parallélogramme) ;
§2 Conjugué et module (figure : conjugué, disque ; démonstration de l'inégalité triangulaire et de son cas d'égalité ;
impédance 30 + 40j) ; §3 Nombres de module 1, \(e^{i\theta}\) (figure : cercle trigonométrique ; Euler, Moivre ;
\(\cos\frac{7\pi}{12}\) par un produit ; signal sinusoïdal) ; §4 Forme trigonométrique et arguments (figure : produit
= rotation + dilatation ; \(a\cos t + b\sin t\)) ; §5 Angle moitié (figure : losange, diagonales \(1 \pm e^{i\theta}\) ;
battements 440/444 Hz) ; §6 Linéariser, Moivre, sommes (figure : ligne brisée \(\sum e^{ikt}\) inscrite dans un cercle,
construction de Fresnel) ; §7 Racines carrées et second degré ; §8 Racines \(n\)-ièmes (figure : \(\mathbb U_6\),
racines cubiques de \(8i\)) ; §9 Exponentielle complexe (figure : images de droites par \(\exp\) ; oscillation amortie) ;
§10 Interprétation géométrique (figure : quotient d'affixes, trois transformations) ; Pour aller plus loin
(similitudes directes, construction de \(\mathbb C\), absence d'ordre). Un exemple traité chiffré et une « Erreur
classique » par section ; 9 démonstrations dépliables. La trigonométrie de base n'est pas refaite : renvoi à `fonctions`
§8-§9 ; sommes et binôme : renvoi à `calculs` §3, §5 ; produit scalaire et mixte : `geometrie` §10 ; d'Alembert-Gauss
et Horner : `polynomes` §4, §9 ; équation caractéristique : `edo` §7 ; dérivée de \(e^{\lambda t}\) : `fonctions` §12 ;
impédances : `filtres`.

## Méthodes (10)
Forme algébrique et conjugué (reconnaître un réel ou un imaginaire pur par \(\overline Z = \pm Z\)) ; forme
trigonométrique pour produits, quotients, puissances ; angle moitié ; linéariser ; Moivre ; \(\sum\cos(kt)\) ;
\(a\cos t + b\sin t\) ; second degré ; \(z^n = Z\) et \(e^z = Z\) ; géométrie. Chacune avec un exemple éclair vérifié ;
trois encadrés « Piège ». Les 7 méthodes d'origine sont reprises (reformulées), sans les similitudes.

## Exercices (12)
EXO 01 à 05 d'origine gardés (justes ; formules trop larges passées en bloc). EXO 06 adapté (voir plus haut). Nouveaux :
07 Moivre, \(\cos\frac\pi{10}\) et \(\sin\frac\pi{10} = \frac{\sqrt5 - 1}{4}\) ; 08 angle moitié (forme trigonométrique de
\(1 + e^{i\theta}\) selon \(\theta\), quotient imaginaire pur, \(\sin x + \sin 2x + \sin 3x = 0\)) ; 09 \(z^4 = -8 - 8i\sqrt3\),
\(z^6 + 7z^3 - 8 = 0\) ; 10 exponentielle complexe et oscillation amortie ; 11 triangle équilatéral
(\(a + jb + j^2c = 0\)) et cercle de diamètre donné. Concours PT étoffé (2 → 9 questions) : parties A et B d'origine
gardées et complétées (A2 général, B2-B3 sommes de \(\cos^k\theta_k\)), partie C nouvelle sur les **courants triphasés**
(courant de neutre nul, puissance constante \(3RI^2 = 6\,600\) W, harmoniques de rang 3). Figure de l'exercice concours :
`style` en dur remplacés par des classes du site.

## Cartes
Corrections (réponses seules) : cartes 6 et 41. Ajouts (14, à la fin, formules en `\\( … \\)`) : \(e^{ip} - e^{iq}\),
\(\cos p + \cos q\), \(\sin p - \sin q\), module et argument de \(1 + e^{it}\), \(\sum\cos(kt)\), \(\cos 3t\), factorisation
par \(z - a\), racines conjuguées si \(\Delta \lt 0\), somme et produit, module et argument de \(e^z\), \(e^z = e^{z'}\),
quotient \(\frac{c - a}{b - a}\), rotation de centre \(\Omega\), réel / imaginaire pur par le conjugué.
`corriger_cartes.py --essai` : 2 réponses corrigées ; `ajouter_cartes.py --essai` : 42 → 56.

## Notations
\(\operatorname{Re}\), \(\operatorname{Im}\) (comme `fonctions` §12 et `geometrie` §10 ; le cours d'origine écrivait
\(\mathrm{Re}\)), \(\overline z\), \(\arg\), \(\mathbb U\), \(\mathbb U_n\), \(j = e^{2i\pi/3}\), \(a \equiv b\ [2\pi]\) (comme
`fonctions`), \(\delta\) racine carrée de \(\Delta\), affixes en minuscules \(a, b, c, \omega\). Les anciennes cartes
gardent leur écriture Unicode.

## Renvois à mettre à jour par l'intégrateur (numéros de § changés)
- `polynomes` §6 : « (chapitre « Nombres complexes », §3) » pour la somme et le produit des racines d'un trinôme → **§7**.
- `polynomes` §9 : « … racines \(n\)-ièmes de l'unité … deux à deux distinctes (chapitre « Nombres complexes », §3) » → **§8**.
- `primitives` (prim-cours) : « linéarisation (chapitre « Nombres complexes », §4) » → **§6**.
- `geometrie` §10 et `calculs` : renvois sans numéro, toujours justes.

## Doutes
- La transformation \(a\cos t + b\sin t\) est aussi dans `fonctions` (méthode 4, EXO 06) : les deux présentations
  concordent (\(\cos\varphi = a/A\), \(\sin\varphi = b/A\)).
- L'« argument principal » dans \(]-\pi, \pi]\) est cité comme convention d'usage (absent du programme de PTSI).
- Le Concours mentionne le triphasé (2ᵉ année de SI, `triphase`) : c'est une application, sans prérequis d'électrotechnique.
