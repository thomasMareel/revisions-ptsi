# `primitives` (prefix `prim`) — compte rendu, 2026-11-22

Point 4 de l'audit (lot 7), `docs/audit-2026-11/maths-1a.md` (ligne « Primitives » : « bon chapitre, mais limité aux fonctions
à valeurs réelles ») et ligne « Fonctions complexes d'une variable réelle » (❌). Cours réécrit en entier au format de la
1ʳᵉ année (bloc « AU PROGRAMME · PTSI », sections §n, exemples traités chiffrés, démonstrations en `.reveal`, figures calculées),
méthodes et exercices complétés, cartes relues et complétées.

## Fichiers produits

| Fichier | Contenu |
|---|---|
| `prim-cours.src.html` | cours complet (≈ 99 000 car., dont ≈ 53 000 de SVG ; 10 sections + « Pour aller plus loin », 20 exemples, 5 figures) — construit par `prim_construire.py` depuis `prim-cours.tpl.html` et `prim_figs.json` |
| `prim-meth.src.html` | 10 méthodes + 2 encadrés « Piège » + pièges récapitulés |
| `prim-exos.src.html` | 11 exercices + 1 « Concours PT » (EXO 01-06 conservés et retouchés, 07-12 nouveaux, concours remplacé) |
| `prim-cartes-corr.json` | `[]` : aucune carte fausse |
| `prim-cartes-ajout.js` | 14 cartes nouvelles (25 → 39) |
| Scripts | `prim_calculs.py` (77 contrôles sympy des exemples du cours), `prim_calculs_exos.py` (88 contrôles : méthodes, exercices, concours), `prim_figs.py` (figures, outil commun `int_svg.py`), `prim_construire.py`, `prim_cartes_rendu.py` (rendu MathJax des cartes, 0 erreur) ; copies des panneaux d'origine `prim_orig_{cours,meth,exos}.html` |

## Erreurs et défauts corrigés

1. **Manques au regard du programme** (section « Primitives et équations différentielles linéaires », S1) : primitives d'une
   fonction **à valeurs complexes** et de \(\mathrm e^{\lambda x}\), \(\lambda \in \mathbb C\) (absentes, sauf une astuce en
   méthode 5) ; **lien intégrale-primitive** et notation \(\int^x f(t)\,\mathrm dt\) (absents) ; **intégration par parties et
   changement de variable** (renvoyés au chapitre « Intégrales » alors que le programme les place ici, au S1) ; primitives de
   \(\frac{1}{ax^2+bx+c}\) (seulement dans les méthodes) ; application de la **décomposition en éléments simples** (absente du
   cours). Tous comblés (§2, §5, §7 à §10).
2. **Tableau des primitives usuelles** : \(a^x\) donné pour \(a \gt 0\) sans exclure \(a = 1\) (division par \(\ln a = 0\)) ;
   corrigé. Ajouts : \(\frac{1}{x^n}\), \(\ln\), \(\tan\), domaines précisés.
3. **Méthodes** : titre faux de la méthode 3 (« Décomposer un polynôme par un trinôme… » pour \(\frac{1}{ax^2+bx+c}\)) et titre
   peu clair de la méthode 5 (« Bouger les exponentielles dans les trigonométries ») ; méthodes réécrites (10, avec exemples
   éclairs vérifiés).
4. **EXO 05** : notations de l'intégration par parties inversées par rapport au cours et au chapitre « Intégrales » (\(u\) dérivé,
   \(v'\) primitivé) ; alignées (on primitive \(u'\), on dérive \(v\)), et passage par les complexes ajouté en Q2.
5. **EXO 06 (Wallis)** : Q3 demandait de « montrer » des formules à doubles factorielles, la correction se contentait de les
   vérifier sur un exemple. Formules réécrites avec des factorielles, récurrence rédigée, Q4 ajoutée (\(nW_nW_{n-1} = \frac\pi2\)).
6. **« Concours PT »** : trois questions immédiates, dont A1 identique à l'EXO 02 Q1. Remplacé par un vrai problème en cinq
   parties (« Autour de \(1/(1+x^3)\) » : décomposition à forme fournie, primitive ln + arctan, \(I = \frac{\ln 2}{3} + \frac{\pi}{3\sqrt3}\),
   encadrement de contrôle, \(J = \frac16 + \frac23 I\) par dérivation, limite \(\frac{2\pi}{3\sqrt3}\)).
7. Harmonisations : `\mathrm{d}x` (comme `integrales`, `integ2a`), `\mathrm{e}`, valeurs absolues des logarithmes justifiées,
   intervalles précisés dans les énoncés.

Les exercices EXO 01 à 06 d'origine sont justes (recalculés en sympy) et conservés.

## Couverture du programme avant → après

| Capacité (programme PTSI, S1) | Avant | Après |
|---|---|---|
| Primitives sur un intervalle, ensemble des primitives, unicité à valeur imposée | ✅ (sans exemple) | ✅ §1 (démonstration, figure de la famille, figure des deux branches de \(1/x\), méthode 1, cartes 0-2) |
| Lien intégrale-primitive (rappel), notation \(\int^x f\), calcul d'intégrales | 🔶 (notation seule) | ✅ §2 (vitesse → distance avec figure, charge d'un condensateur, piège \(\int_{-1}^1 x^{-2}\)), méthode 10, carte |
| Primitives usuelles : exp, ln, puissances, trigonométriques, hyperboliques, \(\frac{1}{1+x^2}\), \(\frac{1}{\sqrt{1-x^2}}\) | ✅ | ✅ §3 (tableau complété, \(\ln\) et \(\tan\)), EXO 01, cartes |
| Reconnaître les dérivées de fonctions composées | ✅ | ✅ §4 (principe démontré, tableau, 8 exemples), méthode 2, EXO 02 |
| Fonctions à valeurs complexes ; \(\mathrm e^{\lambda x}\), \(\lambda \in \mathbb C\) ; \(\mathrm e^{ax}\cos bx\), \(\mathrm e^{ax}\sin bx\) | ❌ (astuce en méthode) | ✅ §5 (définition, formules démontrées, \(x\,\mathrm e^{ix}\)), méthode 3, EXO 05 Q2, EXO 07, EXO 12 Q3 |
| Puissances et produits trigonométriques (linéarisation) | 🔶 (méthode) | ✅ §6 (Euler, règle des exposants impairs, valeur efficace, orthogonalité, figure), méthode 4, EXO 03, EXO 08 |
| Primitives de \(\frac{1}{ax^2+bx+c}\) | 🔶 (méthode) | ✅ §7 (trois cas démontrés, numérateur affine, figure), méthodes 5-6, EXO 04, EXO 09 |
| Fractions rationnelles (éléments simples, pôles simples ; forme fournie sinon) | ❌ | ✅ §8, méthode 7, EXO 10, concours |
| Intégration par parties, changement de variable | 🔶 (renvoi) | ✅ §9, §10 (primitives de \(\ln\), \(\arctan\), \(\sqrt{1-x^2}\) ; retour à \(x\)), méthodes 8-9, EXO 05, 06, 11 |

## Cours

AU PROGRAMME · PTSI · §1 Primitives sur un intervalle · §2 Intégrales et primitives · §3 Primitives usuelles et linéarité ·
§4 Reconnaître la dérivée d'une composée · §5 Fonctions à valeurs complexes et \(\mathrm e^{\lambda x}\) · §6 Puissances et produits
de fonctions trigonométriques · §7 Primitives de \(1/(ax^2+bx+c)\) · §8 Fractions rationnelles · §9 Intégration par parties ·
§10 Changement de variable · Pour aller plus loin (\(t = \tan\frac x2\), \(\frac{1}{\sqrt{x^2 \pm 1}}\), pôles multiples, primitives
non élémentaires et théorème de Liouville). Figures calculées : famille \(x^3 - 2x^2 + x + c\) et tangentes parallèles ; deux
branches d'une primitive de \(1/x\) ; vitesse \(20(1-\mathrm e^{-t/5})\) et distance ; \(\cos^2\), sa moyenne, sa primitive ;
\(1/(x^2+2x+5)\) et sa primitive arctangente. Vérifiées en clair et en sombre, à 390 et 1440 px.

## Méthodes (10)

Choisir la technique ; reconnaître \(u'g(u)\) et ajuster la constante ; passer en complexes ; \(\sin^m\cos^n\) et produits ;
\(\frac{1}{ax^2+bx+c}\) ; \(\frac{px+q}{ax^2+bx+c}\) ; fraction rationnelle ; intégration par parties ; changement de variable ;
calculer une intégrale et contrôler (signe, encadrement, rectangles).

## Exercices (12)

EXO 01-06 conservés (05 et 06 retouchés) ; nouveaux : 07 primitives à valeurs complexes (\(\mathrm e^{(2-i)x}\), \(\int_0^{2\pi} x\,\mathrm e^{inx}\),
coefficients de Fourier), 08 puissances de sinus et cosinus (\(\sin^4\), \(\cos^5\), moyenne 3/8, lien avec Wallis), 09 trinômes
(trois cas, \(\int_0^1 \frac{\mathrm dx}{x^2+x+1} = \frac{\pi}{3\sqrt3}\)), 10 fractions rationnelles (trois pôles simples, partie entière,
pôle double et facteur irréductible à forme fournie), 11 par parties ou par changement de variable, 12 trois primitives en
physique (accélération en \(\cos^2\), puissance moyenne, charge d'un courant amorti oscillant) ; Concours « Autour de \(1/(1+x^3)\) ».

## Cartes

Aucune carte fausse (les 25 relues). Ajoutées (14) : \(\int_{x_0}^x f\), \(\mathrm e^{\lambda x}\) complexe, \(\mathrm e^{ax}\cos bx\),
\(\frac{1}{x^2+k^2}\), \(\Delta = 0\), \(\frac{px+q}{ax^2+bx+c}\), \(\ln\), \(\arctan\), ch/sh/\(1+\tan^2\), formule de l'intégration par
parties, changement de variable, \(\sin^m\cos^n\) à exposant impair, fractions rationnelles, moyenne de \(\cos^2\) et valeur efficace.
Toutes en `\\( … \\)`, rendues sans erreur par MathJax.

## Notations

Celles du chapitre « Intégrales » réécrit (lot 2) : `\mathrm{d}t`, intégration par parties « on primitive \(u'\), on dérive \(v\) » ;
\(\int^x f(t)\,\mathrm dt\) (programme) ; \(\operatorname{ch}\), \(\operatorname{sh}\) ; \(\Delta = b^2 - 4ac\) ; \(k\) pour \(\frac{1}{x^2+k^2}\).

## Doutes

- **Recouvrement avec « Intégrales »** (§7 à §9 et §11 de ce chapitre réécrit) : le programme place l'intégration par parties, le
  changement de variable et les primitives complexes au S1 (ici) et l'intégrale au S2. Le présent cours les traite du point de vue
  des **primitives** (retour à \(x\), intervalles) avec des exemples différents de ceux d'« Intégrales » ; ce dernier pourrait renvoyer
  ici (« chapitre Primitives, §9-§10 ») plutôt que de redonner les formules.
- La règle « exposant impair » et la formule \(\frac{2}{\sqrt{-\Delta}}\arctan\frac{2ax+b}{\sqrt{-\Delta}}\) sont présentées comme des
  résultats à savoir refaire (le programme demande de « savoir calculer » ces primitives, pas d'apprendre la formule).
- Les décompositions à pôle double ou à facteur irréductible sont toujours données avec leur forme (conforme au programme).
