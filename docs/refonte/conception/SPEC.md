# Système de design final — « Cahier de prépa »

*Spécification d'implémentation pour `index.html` (Révisions PTSI → PT). 18 octobre 2026.*

Ce document est la **cible** de la refonte du look. Il fixe, élément par élément, ce qu'il faut construire. Il s'appuie sur :

- `tokens.css` : les jetons définitifs (couleurs clair / sombre / Auto, typographie, espacements). Ce fichier est **généré** par `outils/gen-tokens.py` à partir de `outils/palette.py`.
- `polices/polices.css` et les 14 fichiers `.woff2` du dossier `polices/` : les polices locales.
- `composants.css` : le CSS de référence des composants. Il est écrit sur les classes **existantes** du site, et ses sections renvoient aux numéros de ce document.
- `maquettes/*.html` et `captures/*.png` : la cible visuelle, écrans 1 à 9.
- `controles/` : les résultats chiffrés des contrôles (contrastes des jetons, contrastes des maquettes rendues, cibles tactiles, captures).

Base : la proposition **P1 « Livre de science »**, choisie par les deux jurys. On y greffe ce que **P3 « Poly & fiches »** et **P2 « Interface nette »** font mieux. Le §1 donne chaque arbitrage, avec les désaccords entre jurys et la façon dont ils sont tranchés.

---

## Sommaire

1. Arbitrages
2. Typographie
3. Couleurs et thèmes
4. Mise en page et comportements
5. Composants
6. États, accessibilité, mouvement
7. JavaScript : ajouts et retouches ciblés
8. Contrôles chiffrés
9. Ordre de mise en œuvre et points de vigilance

---

## 1. Arbitrages

**Règle générale.** Chaque élément a été rejugé sur quatre critères : lisibilité, esthétique, praticité, cohérence. On garde l'existant seulement s'il reste le meilleur choix. C'est le cas de JetBrains Mono, du papier millimétré (déplacé hors du texte) et du bleu de la physique.

### 1.1 Désaccords entre les deux jurys, et décision

| Élément | Jury esthétique | Jury usage | Décision et raison |
|---|---|---|---|
| **Police du code** | Source Code Pro, avec un `@font-face` « JetBrains Mono » qui pointe vers ses fichiers | Garder JetBrains Mono, ligatures coupées | **JetBrains Mono, ligatures coupées** (`font-variant-ligatures:none`). L'argument d'harmonie ne tient plus une fois la taille réglée. Dans une phrase, à 0,84 em, la hauteur d'x de JetBrains (0,55 × 0,84 = 0,46 em) égale celle du serif (0,475 em). Sa grande hauteur d'x rend aussi plus lisibles les petites étiquettes des canvas (12 px), et 88 `ctx.font` et 109 styles inline la nomment déjà. Une police déclarée sous le nom d'une autre serait un piège pour la maintenance. Le fichier variable (2 sous-ensembles utiles, 55 Ko) remplace les 8 fichiers en double d'aujourd'hui. |
| **Couleurs sémantiques** | 3 : rouge, ambre, vert (sans orange) | 4 : rouge, orange, ambre, vert | **3 couleurs.** Dans P1, rouge et orange sont trop proches (ΔOKLab 5,8) : « À revoir » et « Hésitant » se confondent alors qu'ils sont côte à côte. « Hésitant » et la `.notice` « À noter » partagent l'ambre, mais ne sont jamais montrés ensemble et disent la même chose : « pas encore sûr, attention ». Écart final rouge/ambre : 11,0 en clair, 10,4 en sombre. |
| **SI et vert « acquis »** | Écart SI/Info de 8,4 déjà presque maximal | Décaler la SI vers h 185–190 (écart SI/vert de 6,6, trop faible) | **Palette réoptimisée d'un bloc** (`outils/palette-recherche.py`, puis réglage à la main). La SI reste à h 177. C'est le vert « acquis » qui bouge : h 139, plus jaune et plus sombre. L'info passe à h 229. Résultat en clair : SI/vert 9,1, SI/info 9,6, physique/info 9,2, maths/rouge 10,0, **écart minimal 9,1** (P1 : 5,8). En sombre : minimum 8,3. Les deux exigences sont satisfaites. |
| **Onglets de matière** | Onglets de P2 avec filet de couleur, « plus gais que des points, plus légers que des aplats » | Intercalaires larges et colorés de P3, avec effectif (« SI » ne mesurait que 22 px) | **Fusion.** 5 intercalaires de largeur proportionnelle au nom. Chacun porte un filet vif de 3 px en haut (4 px quand il est actif), son nom et son effectif. Fond « creux » au repos, teinte de la matière quand il est actif. Hauteur ≥ 52 px (56 au doigt), « SI » ≥ 36 px de large. Pas d'aplat saturé. |
| **Tête de chapitre** | Intercalaire teinté et millimétré (P2), en clair comme en sombre | Ordinateur seulement, en option ; pas sur téléphone (le cours y commencerait à 243 px) | **Ordinateur et tablette : intercalaire teinté, avec papier millimétré en fondu. Téléphone : pas d'intercalaire dans la page.** Le titre est dans la barre collante, qui porte un liseré de 3 px dans l'encre de la matière. Le cours commence à 124 px (mesuré), comme chez A. |
| **Barre haute du téléphone** | Elle s'efface au défilement (P2) | Elle reste, et affiche la section courante (C) | **Hybride.** Quand on descend, la barre glisse hors de l'écran et seuls les onglets restent (44 px de chrome). Au moindre geste vers le haut, elle revient, avec « Chapitre · onglet » en surtitre et la **section courante** en titre (« §2 Mise en équation »). En haut de page, elle affiche matière · partie · année et le titre complet. On gagne ainsi le maximum de place pendant la lecture, et on se repère d'un petit geste. |
| **Page « Chapitres » du téléphone** | Lignes riches de P2 (Aujourd'hui avec ses 37 cartes et ≈ 12 min, Bilan avec son %) | Tuiles de A, plus intercalaires de C, puces de 40 à 44 px | **2 tuiles riches sur une seule rangée.** Elles informent comme les lignes de P2 tout en restant compactes comme A. Viennent ensuite l'année et le filtre, côte à côte, puis les Épinglés et les Récents réunis dans une seule rangée de puces de 44 px, puis les intercalaires. |
| **Carte de révision** | Fiche bristol de P3 | Carte de A sans réglure (fragile avec les formules et A−/A+), notation tout en bas (B) | **Bristol sécurisé, notation en bas.** La réglure est calée sur l'unité `lh`, donc elle suit A−/A+. Elle disparaît automatiquement si la question contient une fraction ou une formule en bloc (`:has()`), et n'est jamais tracée sous la réponse. La notation est tout en bas, à la place même d'« Afficher la réponse ». Précédente et Passer sont juste au-dessus. Au verso, la question reste affichée en rappel. |
| **Aujourd'hui** | Contenu de P2 (dont la progression par matière) | Base A ; barres chiffrées de C ; pas de progression par matière (doublon du Bilan) | **Usage.** On garde les barres chiffrées des cartes dues par matière, Reprendre avec l'heure (P2), les 7 prochains jours, les récents et les accès rapides. La progression par matière reste dans le Bilan. Le surtitre amical « Bonjour ! On révise ? » (esthétique) est adopté. |
| **Simulateur** | Disposition de P2 : réglages à droite, grand canvas | Restyler sans déplacer le DOM | **Les deux à la fois.** Le DOM des 26 simulateurs canvas est uniforme (`.sim-wrapper > h2, .lead, .mode-switch?, .regime-badge?, .sim-controls, canvas, .sim-info`, vérifié). Une grille CSS à zones nommées donne la disposition de P2 **sans toucher au HTML**. Sur téléphone : la courbe d'abord (collante), puis les réglages. |
| **Plancher typographique** | 13 px | 13 px pour le texte, 12 px pour les pastilles | **13 px** pour tout texte ; **12 px seulement en gras**, pour les compteurs et les pastilles (`--fs-count`). |

### 1.2 Points d'accord, repris tels quels

- Source Serif 4 pour le texte et les titres, avec la taille optique.
- MathJax à `chtml.scale` 1,07, y compris dans le gabarit d'impression.
- Source Sans 3 pour l'interface.
- Chapô en romain.
- Mesure de 34 em.
- Neutres et sombre « encre de nuit » de P1.
- `--dom-*` alias de la matière.
- `.notice` à l'encre normale.
- Onglets soulignés sans « 01–05 ».
- En-tête collant de 56 px avec recherche visible.
- Sommaire de la matière (P1), complété des noms complets, de l'icône du simulateur et d'un bloc « Reprendre » (C).
- Étapes de méthode en pastilles (P3).
- Intitulé « À retenir » sur `.prop-box` (P3).
- Pastille « Afficher ▾ » sur `.reveal`.
- Formules consécutives fusionnées (`:has`, P2), et `.mj-large` (P3).
- Nom de formule : en marge sur ordinateur, au-dessus sur téléphone.
- Liste des exercices dans le rail ; cartes « chapitre précédent / suivant ».
- Sélecteur de thème de P3, avec segmenté en **bas** de la feuille ⋯.
- Marque : carré « § ».
- Filet rouge de marge, discret, sur ordinateur.

### 1.3 Écarté

- Chapô et énoncés en italique (P3) : les variables s'y perdent.
- Surligneur systématique sur les gras (P3).
- Aplats saturés des intercalaires (P3).
- Colonne de 85–90 signes (P2).
- Exposants `<sup>` de 8 px (P2).
- Bloc Auto de P2 : il inverserait la préférence « Clair » avec le JS publié.
- Pastille de marque à 5 bandes (P1).
- Orange sémantique (P1).
- Vert SI identique au vert « acquis » (P3).
- Fraunces et Inter Tight (police actuelle).

### 1.4 Deux ajouts qu'aucune proposition ne traitait

1. **Sous-ensembles « symboles ».** Les fichiers npm `@fontsource-variable` n'ont ni les indices et exposants Unicode, ni les flèches, ni ≈ ≤ ≥ √. Or le texte en contient environ **1 300** hors formules (H₂O, SO₄²⁻, Fe³⁺, ω₀), plus **1 600** « → » et environ **400** ≈ ≤ ≥ ≠. Sans correctif, ils tombent sur une police système. Deux petits fichiers (18,7 Ko et 7,1 Ko) sont construits avec fontTools à partir des paquets npm **officiels** d'Adobe (script reproductible). Ils servent aussi « ʳ ᵉ ˢ ᵈ ᵒ », ce qui évite qu'un simple « 1ʳᵉ année » fasse télécharger tout le latin-ext.
2. **Taille optique sur le romain seulement.** L'italique sert surtout à la taille du texte, où l'axe n'apporte rien : sans lui, on économise 177 Ko. Le gain visuel de l'axe sur les titres de 32 à 44 px a été vérifié côte à côte (`etude/opsz.png`) : les titres sont plus fins, plus serrés et plus élégants.

---

## 2. Typographie

### 2.1 Familles et rôles

| Rôle | Police | Pile CSS (jeton) | Usage |
|---|---|---|---|
| Lire | **Source Serif 4** (variable : graisse 200–900, taille optique 8–60 sur le romain) | `--font-text` : `'Source Serif 4','Symboles TeX','Source Sans 3',Georgia,serif` | Cours, méthodes, énoncés, corrections, questions et réponses des cartes, titres de chapitre et de section, grands nombres. |
| Agir | **Source Sans 3** (variable : graisse 200–900, romain seulement) | `--font-ui` : `'Source Sans 3','Symboles TeX',system-ui,…` | En-tête, onglets, boutons, navigation, badges, compteurs, surtitres, tableaux du contenu, simulateurs (libellés, valeurs), menus, quiz (interface). **Jamais d'italique.** |
| Code | **JetBrains Mono** (variable : graisse 100–800) | `--font-code` | `<pre>`, `<code>`, `<kbd>`, étiquettes des canvas. Ligatures coupées. Plus jamais pour un libellé en capitales. |
| Formules | TeX de MathJax 3.2.2 (inchangé) | — | `\( \)` et `$$ $$`. |
| Symboles de la prose | « Symboles TeX » (fontes MathJax Main et AMS, limitées par `unicode-range`) | 2ᵉ position des piles | ⟹ ⟺ ↔ ⇒ ∈ ∀ ∃ ∧ ⟨ ⟩ ↺ ★… prennent le dessin des formules (0 octet de plus). |

**Pourquoi ce trio.** Source Serif 4 a une hauteur d'x de 0,475 em. Avec MathJax à l'échelle 1,07, la hauteur d'x des formules vaut 1,022 fois celle du texte et l'encre est égale (mesures des jurys, au pixel). Le texte et les formules font donc un seul gris. Source Sans 3 a la même hauteur d'x (0,478), si bien qu'un badge posé dans une phrase s'aligne. Les deux polices ont le grec (environ 3 000 lettres hors formules) et ʳᵉ.

**Remplacements nominatifs à faire dans `index.html` :**
- `'Fraunces'` (28 mentions dans le CSS et les styles inline) → `var(--font-text)` ;
- `'Inter Tight'` (23 mentions) → `var(--font-ui)`. Dans les SVG inline, où les variables ne sont pas toujours lues, écrire `'Source Sans 3', sans-serif` ;
- `'JetBrains Mono'` : rien à changer.

### 2.2 Réglage MathJax

Dans la configuration du `<head>` **et** dans celle du gabarit d'impression (`printChapter`) :

```js
chtml: { scale: 1.07, minScale: 0.5, matchFontHeight: false, mtextInheritFont: true }
```

Ne rien changer d'autre. Le correctif « largeur nulle » et le filtre `findMath` restent tels quels. Avec `mtextInheritFont`, les `\text{…}` prennent Source Serif 4.

### 2.3 Échelle (13 jetons fluides, en rem pour suivre A−/A+)

Les valeurs vont de 390 px (téléphone) à 1 280 px (ordinateur) par `clamp()`, et sont multipliées par `--read-scale` (1 / 1,1 / 1,2).

| Jeton | Téléphone → ordinateur | Police, graisse | Interligne | Emplois |
|---|---|---|---|---|
| `--fs-display` | 40 → 56 px | serif 600, approche −0,03 em | 1 | « 37 cartes », % du Bilan |
| `--fs-h1` | 29 → 44 px | serif 600, taille optique auto, approche −0,018 em, `text-wrap:balance` | 1,08 | Titre de chapitre (intercalaire), titre « Physique » du Sommaire |
| `--fs-h2` | 24 → 32 px | serif 600, approche −0,01 em | 1,15 | Titre de section `.course-section h2`, titre de simulateur |
| `--fs-h3` | 20 → 23 px | serif 600 | 1,25 | `h3` du cours, titre d'exercice |
| `--fs-card-q` | 22 → 26 px | serif 600 | 1,45 | Question au recto d'une carte |
| `--fs-lead` | 18,5 → 21,5 px | serif 400 **romain**, encre 2 | 1,5 | `.intro` (chapô) |
| `--fs-body` | 17,5 → 19 px | serif 400 ; gras **650** | 1,6 | Corps du cours, encadrés, énoncés, réponses de cartes |
| `--fs-h4` | 17,5 → 19 px | serif 600 | 1,3 | `h4`, titres des `.method-box` |
| `--fs-sol` | 16,5 → 17,5 px | serif 400 | 1,6 | `.solution` (corrections) |
| `--fs-small` | 15,5 → 16,5 px | serif 400 ou italique ; sans dans les tableaux | 1,35–1,4 | Noms de formules, légendes, tableaux |
| `--fs-ui-l` | 17 px | sans 600 | 1,3 | Grands boutons (Afficher la réponse, Commencer) |
| `--fs-ui` | 15 → 16 px | sans 400–600 | 1,3 | Onglets, menus, navigation, champs |
| `--fs-ui-s` | 14 px | sans 400–600 | 1,3 | Boutons, méta, fil d'Ariane, sommaire, puces |
| `--fs-ui-xs` | **13 px (plancher)** | sans 500–600 | 1,3 | Légendes d'interface, aides, sous-libellés |
| `--fs-kicker` | 12,5 → 13 px | sans 600–700, CAPITALES espacées de 7,5 % | 1,2 | Surtitres « §1 · LES BASES », « DÉFINITION », « CORRECTION », « EXO 01 » |
| `--fs-count` | 12 px, **en gras seulement** | sans 700, chiffres tabulaires | 1 | Compteurs, « 2A », touches de raccourci |
| `--fs-bar-title` | 17 px | serif 600 | 1,2 | Titre dans la barre du téléphone (2 lignes au plus) |

On passe de 54 tailles distinctes dans le CSS actuel (22 à l'écran, dont 49 éléments sous 12 px) à ces 17 jetons, **sans aucun texte sous 12 px**. C'est mesuré sur les 19 maquettes (`captures/rapport-captures.json`, champ `sous12` vide partout).

### 2.4 Taille par élément (téléphone 390 px / ordinateur 1 440 px)

| Élément | Téléphone | Ordinateur |
|---|---|---|
| Marque « Mes cours de *prépa* » | absente de la barre (la page Chapitres la montre) | serif 600, 19 px |
| Recherche (champ) | icône 44 px | champ de 40 px, 15–16 px, « Ctrl K » |
| Titre du chapitre | 17 px dans la barre (`.mbar-h`) | 44 px (`.chap-h1`) |
| Surtitre de barre (matière · partie · année) | 13 px, 600 | — (fil d'Ariane de 14 px dans l'intercalaire) |
| Onglets | 15 px, 44 px de haut | 16 px, 46 px de haut |
| §n de section | inline dans le surtitre (13 px, capitales) | 34 px italique dans la marge |
| h2, h3, corps, chapô | 24, 20, 17,5, 18,5 px | 32, 23, 19, 21,5 px |
| Formule en bloc | pleine largeur (gouttière −12 px) | colonne de texte |
| Nom de formule | 14 px italique, au-dessus du bloc | 16,5 px italique, dans la marge |
| Question de carte | 22 px | 26 px |
| Boutons de notation | 64 px de haut, mot 15 px, échéance 13 px | idem |
| Navigation : rangée de chapitre | 48 px, 16 px | 34 px, 16 px |
| Grand nombre (Aujourd'hui, Bilan) | 40 px | 56 px |

### 2.5 Interlignage, mesure, rythme, micro-typographie

- **Mesure.** La colonne fait `34em`, soit **646 px à 19 px**. Elle donne **68 signes par ligne en moyenne (mesuré)** sur ordinateur et **41 signes** sur téléphone (358 px), contre 64 à 89 aujourd'hui.
- **Rythme vertical** (en em, il suit le corps) :
  - 0,8 em entre paragraphes ;
  - 1,1 em avant et après un encadré ou une formule ;
  - 1,9 em avant un `h3` ;
  - 3,2 em entre deux sections, plus un filet `--line`.
- **Finitions de mise en page :**
  - `text-wrap:balance` sur les titres et `pretty` sur les paragraphes ;
  - césure automatique (`hyphens:auto`) sous 1 024 px, la page étant en `lang="fr"` ;
  - chiffres alignés (`lining-nums`), et tabulaires (`tnum`) dans l'interface, les compteurs, les tableaux et les valeurs des simulateurs.
- **Micro-typographie française** : passe JS après chaque `typesetPanel` (§7.3) :
  - espace fine insécable (U+202F) avant ; ! ? ;
  - espace insécable avant : et », et après « ;
  - une ponctuation qui suit une formule en ligne reste collée à la formule (on ne voit plus « . On » partir seul à la ligne) ;
  - une formule en ligne plus large que sa ligne reçoit `.mj-large` et défile dans la ligne (anomalie n° 7 de l'audit).
- **« 1ʳᵉ » s'écrit avec les lettres en exposant Unicode**, servies par les fichiers « symboles ». Pas de `<sup>`.

### 2.6 Fichiers de polices : liste et poids

Tous les fichiers sont dans `polices/`, à copier dans `vendor/fonts/`. Le fichier `polices.css` remplace `fonts.css` ; mettre à jour le `<link>` et le gabarit d'impression.

| Fichier | Octets | Origine |
|---|---:|---|
| source-serif-4-latin-opsz-normal.woff2 | 122 360 | npm @fontsource-variable/source-serif-4 5.3.1 |
| source-serif-4-latin-ext-opsz-normal.woff2 | 100 872 | idem |
| source-serif-4-greek-opsz-normal.woff2 | 49 336 | idem |
| source-serif-4-symboles-opsz-normal.woff2 | 18 692 | construit (outils/construire-symboles.py) depuis npm source-serif 4.5.1 (Adobe) |
| source-serif-4-latin-wght-italic.woff2 | 51 576 | npm @fontsource-variable/source-serif-4 |
| source-serif-4-latin-ext-wght-italic.woff2 | 44 420 | idem |
| source-serif-4-greek-wght-italic.woff2 | 20 556 | idem |
| source-sans-3-latin-wght-normal.woff2 | 28 872 | npm @fontsource-variable/source-sans-3 5.3.1 |
| source-sans-3-latin-ext-wght-normal.woff2 | 60 088 | idem |
| source-sans-3-greek-wght-normal.woff2 | 14 528 | idem |
| source-sans-3-symboles-wght-normal.woff2 | 7 072 | construit depuis npm source-sans 3.52.0 (Adobe) |
| jetbrains-mono-latin-wght-normal.woff2 | 40 404 | npm @fontsource-variable/jetbrains-mono 5.3.0 |
| jetbrains-mono-latin-ext-wght-normal.woff2 | 15 196 | idem |
| jetbrains-mono-greek-wght-normal.woff2 | 9 004 | idem |
| **Total : 14 fichiers** | **582 976** (569 Kio) | contre **1 036 168** octets et 22 fichiers aujourd'hui (−44 %) |

**Graisses.** Ce sont des fichiers variables : un seul fichier par sous-ensemble couvre toutes les graisses employées (400, 500, 600, 650, 700). Une graisse statique de plus coûterait plus cher qu'un fichier variable.

**Chargement.** Chaque fichier n'est téléchargé que si la page contient un caractère de sa plage (`unicode-range`). Une page de cours typique charge environ 220 à 390 Ko : serif latin, italique latin, sans latin, symboles, plus le grec ou le latin-ext si besoin. Le service worker précache les 14 fichiers.

**Mise à jour.** Les 12 fichiers fontsource se reprennent tels quels avec `npm pack`. Les 2 fichiers « symboles » se refont avec `python3 -I outils/construire-symboles.py`, puis `outils/gen-polices.py` régénère `polices.css`.

**Couverture** (`outils/couverture.py`, sur les 98 011 caractères non ASCII du site) :
- Il ne reste que 63 caractères rares non couverts (1 444 occurrences).
- 712 sont les ☆ de difficulté, remplacés par des barres (§5.3).
- La plupart des autres (⃗, ₙ, ᵢ…) se trouvent dans des cartes que `flashPretty` convertit en TeX.

**PWA.** Remplacer les 22 entrées `vendor/fonts/…` de `PRECACHE` (`sw.js`) par les 14 nouvelles plus `polices.css`, et incrémenter `CACHE_VERSION`.

---

## 3. Couleurs et thèmes

Toutes les valeurs sont dans `tokens.css`. Les rapports de contraste cités ici sont recalculés par `outils/contrastes-jetons.py` (§8).

### 3.1 Neutres

| Jeton | Clair | Sombre | Rôle |
|---|---|---|---|
| `--desk` | #f3f1ec | #111316 | Bureau (fond d'application) ; pointillé `--desk-dot` à partir de 1 100 px |
| `--sheet` | #fffdf9 | #191b20 | Feuille de lecture, barre du téléphone, cartes de partie |
| `--sunk` | #f6f3ed | #20232a | Creux : formules, champs, en-têtes de tableau, corrections, onglets de matière au repos |
| `--raise` | #ffffff | #24272e | Menus, fenêtres, boutons secondaires, segment choisi |
| `--text` | #1c1d21 (16,6:1) | #e8e6e1 (13,8:1) | Texte courant |
| `--text-2` | #44464d (9,3:1) | #c2c0ba | Chapô, méta, texte secondaire, libellés de contrôle |
| `--text-3` | #63656c (5,7:1, 5,2:1 sur le bureau) | #9fa0a6 (≥ 5,7:1) | Légendes, placeholders, icônes secondaires |
| `--line` | #e8e3da | #2b2e35 | Filets décoratifs |
| `--line-2` | #d6cfc3 | #3a3e47 | Séparateurs, bordures de tableau, piste des curseurs, « jamais vue » |
| `--field` | #8b867c (≥ 3,2:1) | #737885 (≥ 3,4:1) | Contour des champs et du segment choisi (WCAG 1.4.11) |
| `--primary` / `--on-primary` | #1c1d21 / #fffdf9 | #e8e6e1 / #16181c | Action principale en aplat d'encre (inversée en sombre) |
| `--focus` | #2f62d6 | #8fb2ff | Anneau de focus, toujours décalé de 2 px |
| `--link` | #3d5db2 | #91b2ff | Liens du contenu |
| `--hover` / `--press` | encre à 5,5 % / 10 % | blanc cassé à 6 % / 11 % | Survol, appui |
| `--scrim` | rgba(20,21,24,.42) | rgba(0,0,0,.6) | Voile sous les fenêtres et les feuilles |

### 3.2 Matières : une encre par chapitre

Chaque matière a trois jetons : l'encre (texte ≥ 4,5:1 sur la feuille, le bureau, le menu, le creux **et** sa teinte), la teinte de fond, et le vif (traits, pastilles, barres, ≥ 3:1).

| Matière | Encre clair | Teinte clair | Vif clair | Encre sombre | Teinte sombre | Vif sombre |
|---|---|---|---|---|---|---|
| Physique (cobalt h266) | #3d5db2 | #edf3ff | #547add | #91b2ff | #222a3c | #6f94ee |
| Maths (framboise h350) | #973069 | #ffedf4 | #c64d8e | #ff85c3 | #39222d | #db6ea5 |
| SI (sarcelle h177) | #027966 | #e8f6f2 | #18957f | #62cab0 | #1d2e29 | #4fab95 |
| Info (pétrole h229) | #006383 | #e8f5fb | #288cb2 | #5fc3e3 | #1c2d33 | #4ca6c1 |
| Anglais (violet h304) | #6f429d | #f5efff | #9663ce | #c89bff | #2e2539 | #ac7fe0 |

**Choix des teintes.**
- On garde le bleu de la physique et le violet de l'anglais.
- Les maths quittent la brique, qui se confondait avec le rouge d'alerte.
- La SI reste vert d'eau, mais elle est maintenant écartée du vert « acquis ».
- L'info quitte l'ocre, qui se confondait avec l'ambre.
- La matière est **toujours nommée** à côté de sa couleur. La couleur seule ne porte jamais l'information.

**Le « peps »** vient de l'encre de la matière, qui pilote :
- l'intercalaire teinté et millimétré ;
- le liseré de 4 px en haut de la feuille, et de 3 px en haut de la barre du téléphone ;
- les surtitres et le grand « §1 » de la marge ;
- le soulignement de l'onglet actif ;
- les puces de liste et les pastilles d'étape ;
- l'encadré Définition et le filet de l'encadré À retenir ;
- les numéros « Q1. » et « EXO 01 » ;
- la courbe et les curseurs des simulateurs ;
- l'intercalaire de matière actif et la rangée courante de la navigation.

Passer de la physique aux maths change toute l'ambiance (comparer `captures/09-specimen-clair.png`, rangée « Les cinq encres en situation »).

### 3.3 Sémantique (3 couleurs, toujours doublées d'une icône et d'un mot)

| Jeton | Clair (encre / teinte / vif) | Sombre | Sens |
|---|---|---|---|
| `--rouge` | #ab3a33 / #ffeeec / #d24e46 | #ff9085 / #3b2220 / #e66f64 | À revoir, cartes dues, alerte. `--rouge-plein` (compteur « 37 ») : texte blanc à 6,2:1 ; en sombre, texte nuit à 8,1:1 |
| `--ambre` | #8d5e07 / #faf1e5 / #ab7415 | #e1a857 / #33281a / #c08e46 | Hésitant, encadré « À noter », seuil (régime critique) |
| `--vert` | #2e6d18 / #ebf6e8 / #4c9436 | #81ca6d / #212e1e / #6bac59 | Acquis, correction, réussi |

Notation des cartes : `--note-0` = rouge (↺ À revoir), `--note-1` = ambre (∿ Hésitant), `--note-2` = vert (✓ Acquis), `--note-nv` = `--line-2` (jamais vue). Chaque bouton porte aussi son échéance Leitner (« aujourd'hui », « dans 3 jours »…).

### 3.4 Décor « cahier » (sans rôle de texte, donc sans seuil de contraste)

| Jeton | Clair | Sombre | Emploi |
|---|---|---|---|
| `--marge` | #e9b8ae | #5c3a36 | Filet rouge vertical de marge (ordinateur, à partir de 1 024 px) ; filet de 2 px sous l'en-tête de la fiche bristol |
| `--reglure` | #dde7f3 | #2a3240 | Réglure bleue de la fiche bristol |
| `--bristol` | #fffefb | #1d1f25 | Papier de la fiche |
| `--mill-a` / `--mill-b` | 10 % / 18 % | 12 % / 22 % | Part d'encre vive de la matière dans le papier millimétré (trait fin tous les 8 px, trait fort tous les 40 px) |
| `--desk-dot` | rgba(48,52,66,.11) | rgba(200,206,222,.075) | Pointillé du bureau, tous les 22 px |

### 3.5 Rôles dérivés (`data-mat`)

`data-mat="physique|maths|si|info|anglais"` se pose :
- sur chaque `.chapter` (ajout JS, à côté de `data-domain`) ;
- sur toute carte, ligne, puce ou badge qui représente un chapitre ou une matière.

Il définit `--chap`, `--chap-fond` et `--chap-vif`, d'où dérivent :
- `--def-*`, `--prop-*` et `--meth-pastille` ;
- `--mill-fin` et `--mill-cm` ;
- les encadrés « sans matière », définis une fois pour toutes : `--notice-*` (ambre), `--sol-*` (vert) et `--reveal-trait` (contour de champ).

Hors `data-mat`, `--chap` vaut l'encre 2 (neutre).

### 3.6 Compatibilité : les noms existants restent définis

| Nom (usages dans index.html) | Nouvelle valeur | Remarque |
|---|---|---|
| `--grid` (1 923) | `--line-2` | Ce n'est plus le quadrillage, mais le filet de tableau |
| `--ink` (317) | `--text` | Aussi `fill` et `stroke` des 155 SVG |
| `--paper-dark` (205) | `--sunk` | En-têtes de tableau |
| `--accent` (153) | `--rouge` | « Stylo rouge » des schémas et des canvas |
| `--muted` (132) | `--text-3` | |
| `--accent2` (94) | `--physique` | Bleu des schémas |
| `--border` (90), `--surface` (7) | `--line-2`, `--sunk` | **Enfin définies** : 90 bordures de tableau invisibles jusqu'ici |
| `--paper` (73) | `--sheet` | |
| `--green` (70), `--amber` (55) | `--vert`, `--ambre` | |
| `--anglais` (9) | encre de l'anglais | Défini avec les matières |
| `--radius-s/m/l`, `--shadow`, `--shadow-1/2` | `--r-s/m/l`, `--sh-1/2` | |
| `--dom-*` (8 noms) | encre de la matière du domaine | Une seule encre par chapitre |
| `--accent-deep`, `--read-scale` | `--rouge`, 1 | `--read-scale` reste piloté par A−/A+ |

Les variables lues par `getCanvasColors()` (`--ink`, `--paper`, `--accent`, `--accent2`, `--green`, `--amber`) se résolvent toutes en `#rrggbb`, format exigé par `__CVA`.

### 3.7 Canvas

- Continuer à passer par `__CV()` et `__CVA()`.
- **Retouche** dans `getCanvasColors()` : `muted` et `grid` ne sont plus des valeurs codées en dur. Lire `--text-3` et `--line`, et calculer `grid` comme `__CVA('ink', 0.08)` en clair et `0.12` en sombre, ou lire `--line` directement.
- La détection du sombre par `data-theme="dark"` ne change pas.
- La courbe principale d'un simulateur prend `--chap-vif`, par `getComputedStyle(canvas)`. Les courbes secondaires prennent `accent` / `accent2` / `green` / `amber` comme aujourd'hui.

### 3.8 Thème Clair / Sombre / Auto

Le mécanisme est **déjà publié** (commit 1d2a766) et ne change pas :
- la préférence est stockée dans la clé `theme` : `light`, `dark` ou `auto` (`auto` par défaut) ;
- `data-theme="dark"` signale le thème **effectif** sombre, et l'absence de l'attribut le thème clair ;
- `data-theme-pref` porte la préférence ;
- en mode Auto, `matchMedia` suit le système en continu ;
- `window.__setTheme(pref)` change la préférence et `window.__themePref()` la lit.

Dans `tokens.css` :
- `:root[data-theme="dark"]` porte le bloc sombre ;
- un **filet de sécurité CSS** recopie ce bloc à l'identique sous `@media (prefers-color-scheme: dark)` pour `:root[data-theme-pref="auto"]` et pour `:root` sans attribut (cas où le JS n'a pas encore tourné, ou maquettes statiques). La préférence « Clair » sur un appareil sombre n'est visée par aucun sélecteur : elle reste claire ;
- `color-scheme: light | dark` est posé, pour que les barres de défilement et les champs natifs suivent le thème.

Le bouton actuel, qui fait tourner les thèmes, devient un **sélecteur explicite** (§4.6).

**Barre du téléphone (`theme-color`).** La meta `theme-color` (aujourd'hui #c8472e) doit prendre la couleur de `--sheet` du thème effectif : deux metas avec `media="(prefers-color-scheme: …)"`, mises à jour dans `applyTheme`.

---

## 4. Mise en page et comportements

### 4.1 Grille et points de rupture

| Largeur | Disposition |
|---|---|
| **≥ 1 360 px** | En-tête de 56 px. Trois colonnes : navigation permanente de 288 px, feuille (896 px au plus), rail de 240 px (sommaire et « Mes cartes », ou liste des exercices). |
| 1 200–1 359 px | Navigation et feuille ; pas de rail (le sommaire passe dans le menu Plus, rubrique « Dans ce chapitre »). |
| 1 024–1 199 px | La navigation redevient le tiroir (☰ dans l'en-tête). La feuille garde sa marge « § » de 112 px et le filet rouge. |
| 768–1 023 px (tablette) | Tiroir. La feuille n'a plus de marge (« §1 » passe dans le surtitre, le nom de formule au-dessus du bloc), mais garde l'intercalaire. Aujourd'hui et Bilan deviennent des boutons icônes. |
| **≤ 767 px (téléphone)** | Coquille téléphone (§4.2). Ce point de rupture (767/768) est **celui du code actuel** : ses 60 règles `@media (max-width:767px)` restent valables. |

- Le **bureau** porte un pointillé de 22 px à partir de 1 100 px. Aucun quadrillage n'est plus jamais dessiné sous le texte.
- La **feuille** est unie (`--sheet`), avec un rayon de 16 px et une ombre `--sh-sheet`. Elle porte un liseré de 4 px dans l'encre vive de la matière.
- Les cinq onglets gardent **la même colonne** de texte. Le simulateur, lui, s'élargit à toute la feuille.

### 4.2 Téléphone : aucune barre fixe en bas

- **Barre haute collante `.mbar`** (56 px, fond `--sheet`, liseré de 3 px de l'encre de la matière). Elle contient, dans l'ordre :
  - ☰ (page Chapitres) ;
  - un bloc titre, sur 2 lignes ;
  - la loupe ;
  - **Réviser**, icône avec compteur rouge plein : lance directement les révisions du jour (`quizStartDue`) ;
  - ⋯ (feuille d'options).

  Ce sont 4 boutons de 44 × 44 px.
- **Bloc titre au repos** (haut de page) :
  - 1ʳᵉ ligne, 13 px, 600 : « ● **Physique** · Ondes & signaux · 1ʳᵉ ». Seule la partie s'abrège (`…`), jamais l'année ;
  - 2ᵉ ligne : le titre complet en serif 17 px, sur 2 lignes au plus. Le titre n'est plus jamais tronqué en une ligne.
- **Onglets collants `.mtabs`** juste dessous (44 px) : Cours · Méthodes · Simu · Cartes ③ · Exos. Ils tiennent dans 358 px, et le compteur de Cartes compte les cartes dues du chapitre.
- **Chrome total : 100 px.** Le surtitre du cours commence à 124 px (mesuré).
- **Au défilement** (`.mbar.cachee`, translation de 200 ms) :
  - quand on descend de plus de 8 px, au-delà de 120 px, la barre glisse hors de l'écran ; les onglets restent seuls (`.mtabs.seule`, `top:0`, ombre `--sh-1`), soit **44 px de chrome** ;
  - au moindre défilement vers le haut, la barre revient, avec en surtitre « Circuit RLC série · Cours » et en titre la **section courante** (« *§2* Mise en équation »), donnée par le scroll-spy existant (`tocItemsById`).
- **Mouvement réduit** : la barre ne glisse pas. Elle disparaît et réapparaît sans animation (§6.4).
- **Menu ⋯** : une **feuille qui monte du bas**, ouverte à la demande. C'est une modale, pas une barre. Elle contient :
  - Aujourd'hui (avec son compteur), Bilan, Quiz, Calcul mental, Formulaire du chapitre, Épingler, Cartes signalées, Sauvegarde ;
  - **en bas**, à portée du pouce : Thème (segmenté Clair / Sombre / Auto, avec « actuellement : … ») et Texte (A− / A / A+).

  Imprimer et Raccourcis restent absents sur téléphone, comme aujourd'hui.
- **Pages plein écran** (Chapitres, Aujourd'hui, recherche, quiz, Bilan) : elles s'ouvrent par-dessus la page, ont un × en haut à droite, et se ferment aussi avec le bouton retour d'Android (`history.pushState` d'un état fictif, puis `popstate`).
- **Gouttière** : 16 px. Les formules en bloc débordent dans la gouttière (−12 px de chaque côté) pour gagner de la largeur.

### 4.3 Navigation des chapitres (même structure sur ordinateur et sur la page Chapitres du téléphone)

Elle repose sur les mêmes données qu'aujourd'hui : `buildDrawerList`, `CHAP_GROUPS`, et les clés `year`, `pinned`, `recents` et `drawerCollapsed`.

1. **Année** : segmenté « 1ʳᵉ année / 2ᵉ année » (clé `year`). Sur téléphone, il se réduit à « 1ʳᵉ / 2ᵉ » et se place à gauche du filtre.
2. **Filtre** `#mob-filter`. Il cherche dans toutes les matières et les deux années, sans tenir compte des accents ; Entrée ouvre le 1ᵉʳ résultat. Les résultats sont **groupés par matière** :
   - un surtitre dans l'encre de la matière, avec l'effectif ;
   - pour chaque chapitre, son nom complet, avec la correspondance surlignée par `<mark>` en teinte de matière ;
   - un sous-libellé « partie · 1ʳᵉ/2ᵉ année » et un badge « 2ᵉ » plein pour la 2ᵉ année.

   Voir `03c`.
3. **Épinglés et Récents** :
   - sur **ordinateur**, les Épinglés en puces (★ ambre) qui passent à la ligne ; les Récents en lignes de 34 px avec leur contexte à droite (« Cours · §3 » pour le plus récent, d'après `lastPos`, sinon la partie) ;
   - sur **téléphone**, une seule rangée de puces de 44 px : ★ pour les épinglés, horloge pour les récents.

   Ces deux sections ne sont jamais filtrées.
4. **Intercalaires de matière** `.mat-tabs` / `.mat-tab` :
   - 5 onglets côte à côte ; chacun prend sa place selon la longueur de son nom ;
   - chacun porte un filet vif de 3 px en haut, son nom (14 px, 600) et son effectif selon l'année (12 px, gras) ;
   - au repos, fond `--sunk` ; l'onglet actif prend la teinte de la matière, l'encre de la matière, un filet de 4 px et du gras ;
   - un filet de 2 px dans l'encre vive de la matière active ferme la rangée ;
   - hauteur : 52 px (56 px au doigt).
5. **Parties repliables** (sous-domaines de `CHAP_GROUPS`) :
   - en-tête de 36 px (44 au doigt), avec un chevron et l'effectif ;
   - l'état replié est mémorisé dans `drawerCollapsed` (inchangé) ;
   - en 2ᵉ année, chaque partie finit par la ligne « + N chapitres de 1ʳᵉ année », qui les déplie.
6. **Rangées `.nav-item`** :
   - nom court (`mobLabel`), puis, à droite, dans cet ordre : la mention « 2A » (si on est en 1ʳᵉ année), le compteur rouge clair des cartes dues, l'épingle ;
   - l'épingle est visible au survol et au focus sur ordinateur, et toujours sur téléphone ;
   - la rangée courante prend la teinte de la matière, un rail vif de 3 px à gauche et `aria-current="page"` ;
   - hauteur : 34 px (48 sur la page Chapitres du téléphone) ;
   - pas d'anneau de % : il reste dans le Bilan, comme l'utilisateur l'a demandé.
7. **Page Chapitres du téléphone** (☰, plein écran) :
   - titre « Chapitres » en serif 26 px et × ;
   - **2 tuiles riches** : « Aujourd'hui » avec son compteur et « 37 cartes dues · ≈ 12 min », et « Bilan » avec « 34 % des cartes acquises » ;
   - la rangée Année et Filtre ;
   - les puces ;
   - les intercalaires ;
   - les parties.

   Ouvrir un chapitre demande 2 gestes. Voir `03b`.
8. **Sommaire de la matière** (nouveau, `03a`). Il s'ouvre par le nom de la matière dans le fil d'Ariane, ou par un 2ᵉ clic sur l'intercalaire actif. Il présente la matière comme la table des matières d'un livre :
   - **en-tête-intercalaire** : surtitre « Sommaire de la matière · 1ʳᵉ année », « *Physique* » en serif italique 44 px dans l'encre de la matière, méta (parties, chapitres, **cartes dues en rouge**, % acquis) et carte « Reprendre » (chapitre, onglet, section et heure) ;
   - **cartes de partie** sur 2 colonnes (en flux de colonnes CSS) :
     - titre en serif 19 px, effectif ;
     - barre de % acquis, avec les cartes dues ;
     - liste **numérotée en italique dans l'encre de la matière** des chapitres, sous leur **nom complet** (`name`) ;
     - icône ∿ pour un simulateur, compteur des cartes dues ;
   - **rappel** : « 14 chapitres de 2ᵉ année… — Voir la 2ᵉ année ».

   Il se rend dans la zone de la feuille, et son lien profond est `#sommaire/physique` (extension de `urlRouting`).

### 4.4 Page chapitre

- **Intercalaire** (ordinateur et tablette). C'est le bandeau `.chap-title-banner` actuel, enrichi par `injectChapterTitleBanners`. Fond `--chap-fond`, papier millimétré dans l'encre vive de la matière (traits de 8 et 40 px), en fondu vers le bas (masque de 0 à 100 %), filet bas `--line`. Il contient, dans la colonne de texte (alignée sur la marge de 112 px) :
  - **fil d'Ariane** (14 px) : pastille, **Physique** (lien vers le Sommaire) › Ondes & signaux (lien vers la partie dans la navigation) · tag (`matiereLabel`) ;
  - **titre** `h2.ctb-title`, stylé comme le jeton h1 : 44 px, serif 600. Il reste un `h2`, car l'unique `h1` de la page est le titre du site ;
  - **actions** alignées à droite du titre : « Formulaire » (bouton secondaire avec icône), Imprimer et Épingler (boutons icônes). Elles sortent du menu Plus ;
  - **méta** : badge d'année (1ʳᵉ en contour, 2ᵉ en aplat d'encre) · 7 sections · 26 cartes · 8 exercices · 1 simulateur ;
  - **onglets** `.tabs` posés sur le bas de l'intercalaire (§5.1). Ils deviennent collants sous l'en-tête (`top:56px`) au défilement, sur fond `--sheet` avec l'ombre `--sh-1`.
- **Feuille** : une grille marge | texte, avec une marge de **112 px** à partir de 1 024 px. La marge porte :
  - le « **§1** » en serif italique 34 px dans l'encre de la matière ;
  - le nom de la formule (attribut facultatif `data-nom`, ajouté peu à peu), en serif italique 16,5 px, encre 3, aligné à droite.

  Un **filet rouge vertical** `--marge` de 1 px court sur toute la hauteur, à 20 px du texte (`.panel-body.marge::before`). Il est décoratif et n'apparaît jamais sur téléphone.
- **Rail droit** (≥ 1 360 px, collant) :
  - **sommaire scroll-spy** (le `.toc` actuel) : « DANS CE CHAPITRE », lignes « *§n* Titre » ; la ligne active porte un rail vif de 2 px et du gras ;
  - **« Mes cartes »** : grand chiffre « 10 acquises sur 26 », barre empilée (acquises / hésitantes / à revoir / jamais vues) avec sa légende, bouton « Réviser les 3 cartes dues » teinté matière ;
  - **onglet Exercices** : le rail liste les exercices (« EXO 01 » + titre + difficulté en barres) et l'exercice visible est mis en évidence.
- **Pied de chapitre** : c'est le `#chap-pager` existant, restylé en **deux cartes** (« ‹ Chapitre précédent » + nom en serif 17 px, et l'inverse). Il apparaît en bas de chaque panneau et ses noms viennent de `goRelChapter`. Sur téléphone, les deux cartes s'empilent.

### 4.5 Lancement et accès à « Aujourd'hui »

- **Au lancement**, le site rouvre le **dernier chapitre consulté** (`lastPos`, déjà publié). Un `#hash` reste prioritaire. « Aujourd'hui » ne s'ouvre jamais seul.
- « Aujourd'hui » s'ouvre à la main :
  - sur ordinateur, par le bouton de l'**en-tête** (`#today-btn`, sorti du menu Plus) ;
  - sur téléphone, par la **tuile** de la page Chapitres ou la **1ʳᵉ ligne** de la feuille ⋯ (`#mob-today-btn`) ;
  - partout, par `window.todayOpen()`.

### 4.6 Sélecteur de thème Clair / Sombre / Auto

- **Ordinateur.** Le bouton Thème de l'en-tête (icône demi-disque, `#theme-btn`) ouvre un **popover** de 352 px, placé sous le bouton. Il contient :
  - le titre « Thème » ;
  - la phrase « **Auto** suit le réglage clair/sombre de ton appareil, en continu, même site ouvert — actuellement : **clair** » ;
  - **3 cartes à mini-vue**, en `role="radio"` : Clair, Sombre, et Auto, dont la mini-vue est coupée en diagonale entre le clair et le sombre ;
  - dessous, « Taille du texte · cours et cartes » : un segmenté A− / A / A+, qui reprend le réglage `readScale` aujourd'hui rangé dans le menu Plus.

  Le choix actif a un contour de 2 px à l'encre. Le popover se ferme avec Échap, par un clic dehors ou après un choix. Les couleurs des mini-vues sont **volontairement littérales**, pour montrer chaque thème quel que soit le thème courant.
- **Téléphone.** Le thème quitte la barre haute et passe en bas de la feuille ⋯ : segmenté Clair / Sombre / Auto (44 px), avec dessous « Auto suit le réglage de ton téléphone — actuellement : sombre ».
- Les deux appellent `window.__setTheme(pref)`. La mention « actuellement » se met à jour au changement du système (écoute du même `matchMedia`).

---

## 5. Composants

Le CSS de référence est dans `composants.css`. Pour chaque composant : sa classe réelle, son apparence, ses tailles, ses états et son comportement.

### 5.1 Base

**Boutons `.btn`.**
- Taille : 38 px de haut (44 au doigt), rayon de 10 px, Source Sans 600 à 14 px, icône de 18 px, écart de 8 px.
- Variantes :
  - par défaut, secondaire : `--raise`, contour `--line-2` ;
  - `.btn-primary` : aplat d'encre (`--primary` / `--on-primary`) ;
  - `.btn-chap` : teinte et encre de la matière ;
  - `.btn-ghost` : transparent, encre 2 ;
  - `.btn-icon` : carré ;
  - `.btn-lg` : 48 px, 17 px ;
  - `.btn-block`.
- États : survol (creux, contour `--field`), appui (descend de 1 px), focus visible (anneau `--focus`), désactivé (opacité 0,45, curseur interdit, pas de translation).
- Les boutons existants s'y rattachent :
  - `.toggle-sol` et `.flash-reset` → secondaire / discret ;
  - `.quiz-btn-primary` → primaire ;
  - `.quiz-btn-secondary` → secondaire ;
  - `.dash-revise-btn` → `.btn-chap`.

**Compteurs `.count`.**
- Pastille de 22 px, rayon plein, 12 px gras, chiffres tabulaires.
- Rouge plein pour les cartes dues globales (en-tête, barre du téléphone, onglet Cartes, Aujourd'hui).
- `.count-soft` (teinte rouge) dans les listes. `.count-quiet` (neutre) pour les simples effectifs.
- Le badge « Réviser 0 » est masqué quand rien n'est dû.

**Badges `.badge`.**
- 24 px, rayon de 6 px, 13 px 600.
- Variantes :
  - neutre ;
  - `.badge-chap` (matière, avec pastille) ;
  - `.badge-out` (contour : 1ʳᵉ année) ;
  - `.badge-2a` (aplat d'encre : 2ᵉ année) ;
  - `.badge-strong` (Concours PT).
- La pastille `.dot` mesure 9 px, dans l'encre vive (≥ 3:1).

**Puces `.chip`.** 36 px (44 au doigt), rayon plein, contour `--line-2`, 14 px 500, avec une pastille ou une icône, et la mention « 2A » en 12 px gras.

**Touches `kbd`.** JetBrains Mono 12 px, contour, bordure basse de 2 px. Les aides clavier (`.kbd-hint`) sont **masquées au doigt** (`pointer:coarse`).

**Segmenté `.seg`** (et `.mode-switch` des simulateurs).
- Fond creux, padding de 3 px, segments de 32 px (44 au doigt).
- Le segment choisi a un fond `--raise`, du gras, une ombre `--sh-1` **et un contour `--field` ≥ 3:1** : jamais seulement une ombre.
- ARIA : `aria-pressed` pour un choix d'état, `role="radio"` / `aria-checked` pour un choix exclusif.

**Champs `.field`.**
- 40 px (44 au doigt, en 16 px pour éviter le zoom iOS), rayon de 10 px, contour `--field`.
- Icône à gauche en encre 3 ; placeholder en encre 3 (5,7:1).
- Raccourci « Ctrl K » à droite, masqué au doigt.
- Focus : anneau `--focus` décalé de 2 px.

**Menus `.menu`** (Plus `#more-menu`, Réviser `#study-menu`).
- Fond `--raise`, rayon de 16 px, ombre `--sh-3`, padding de 6 px.
- Éléments `.menu-item` de 40 px (48 au doigt), en 15–16 px 500, avec une icône en encre 3 et une info à droite (`.end` : compteur, `kbd`).
- Séparateur `.menu-sep`, intitulé `.menu-label` (capitales de 12,5 px).
- Navigation au clavier ↑↓ ; Échap ferme.
- **Menu Plus**, ordinateur : Formulaire, Imprimer, Sauvegarde, Raccourcis (`?`), Cartes signalées (avec compteur), et « Dans ce chapitre » entre 1 200 et 1 359 px. Aujourd'hui et la taille du texte ont quitté ce menu (ils passent dans l'en-tête et dans le popover Thème).
- **Menu Réviser** : Révisions du jour (avec compteur), Quiz, Calcul mental.

**Surtitre `.kicker`** : capitales espacées de 12,5–13 px, en 600, encre 3. Dans l'encre de la matière pour les surtitres de section et d'exercice.

**Barre empilée `.stack`.**
- 8 px, rayon plein, segments séparés de 2 px.
- Ordre : acquis (vert vif), hésitant (ambre vif), à revoir (rouge vif), jamais vues (fond `--line-2`).
- Toujours accompagnée d'une légende chiffrée (`.legend`) ou d'un `aria-label`.

**Bannière de mise à jour** (« Nouvelle version disponible — Recharger »).
- Toast en bas au centre (ordinateur) ou en bas, pleine largeur moins 16 px (téléphone), au-dessus de tout (`--z-toast`).
- Fond `--primary`, texte `--on-primary`, bouton « Recharger » en aplat clair, rayon de 12 px, ombre `--sh-3`.
- C'est un message temporaire, pas une barre de navigation.

**Toasts**, gabarit commun, par exemple « Carte signalée » ou « Sauvegarde importée ». Même apparence que la bannière, 15 px. Ils restent 4 s (affichage instantané en mouvement réduit) et portent `role="status"`.

### 5.2 Cours

| Classe réelle | Apparence |
|---|---|
| `.panel` | Serif 17,5 → 19 px, interligne 1,6, encre `--text`, chiffres alignés, `hanging-punctuation:first`. |
| `.course-section` | Grille marge 112 px \| texte 34 em (≥ 1 024 px), sinon un bloc. Entre deux sections : 3,2 em + filet `--line` sur la largeur du texte. |
| `.sec-num` | Découpé au chargement (§7.2) en `.sec-n` « §1 » (marge : serif italique 34 px, encre de la matière) et `.sec-t` « LES BASES » (surtitre de 13 px en 700, capitales, encre de la matière). Sous 1 024 px : une seule ligne « §1 · LES BASES » en surtitre. |
| `h2` | Serif 600, 24 → 32 px, interligne 1,15, approche −0,01 em, `balance` ; 0,55 em dessous. |
| `h3` | Serif 600, 20 → 23 px, 1,9 em au-dessus (1,1 em après un h2 ou un chapô). **Plus jamais de h3 coloré par domaine.** |
| `h4` | Serif 600, 17,5 → 19 px. |
| `.intro` | Chapô : serif **romain** 18,5 → 21,5 px, encre 2, interligne 1,5. **Ni italique ni filet** (on supprime l'override `!important` actuel en sombre). |
| `p`, `strong`, `em` | Paragraphes espacés de 0,8 em, `pretty` ; gras à **650** ; vraie italique Source Serif. |
| `ul`, `ol` | Retrait de 1,35 em. Puces dans l'encre vive de la matière, numéros en sans gras dans l'encre de la matière. |
| `.formula` | Creux `--sunk`, rayon de 10 px, padding 0,85 / 1,1 em, centré, **défilement horizontal** si la formule est trop longue (`overflow-x:auto`) : la page ne déborde jamais. Pleine largeur sur téléphone. Ni rail rouge ni cadre. |
| `.formula + .formula` | **Fusion** : un seul bloc, coins intérieurs carrés, séparés par un filet pointillé `--line-2`. |
| `.formula[data-nom]` | Nom en marge (ordinateur) ou au-dessus du bloc (sous 1 024 px), en serif italique, encre 3. |
| `mjx-container` inline trop large | `.mj-large` : défile dans la ligne. |
| `.def-box` | Teinte de la matière, filet gauche de 3 px en encre vive, rayon 4 / 10 px. Intitulé **« DÉFINITION »** généré en CSS (surtitre de 13 px, 700, encre de la matière). |
| `.prop-box` | Fond `--sheet`, contour `--line-2`, filet gauche de 3 px en encre vive. Intitulé **« À RETENIR »** généré ; le `<strong>` initial prend l'encre de la matière. |
| `.method-box` | Creux neutre, rayon de 10 px. Titre (`strong` initial) en serif 600, 17,5 → 19 px. Les étapes (`li` qui contient `.step`) deviennent des **pastilles numérotées** de 1,75 em, à l'encre de la matière avec le chiffre couleur feuille (contraste ≥ 5,2:1 en clair, ≥ 7,7:1 en sombre). Le texte « Étape n. » reste là pour les lecteurs d'écran : la double numérotation disparaît à l'écran seulement. |
| `.notice` | Teinte ambre, filet ambre vif. Intitulé **« À NOTER »** généré, en ambre. **Texte à l'encre normale** : 15:1 en clair, 11,5:1 en sombre, contre 1,99:1 aujourd'hui. |
| `.reveal` | Cadre en tirets de 1,5 px (`--field`), 44 px de haut au moins, et **tout le bloc est cliquable**. `.label` en surtitre encre 3, `.prompt` en gras. Une pastille « **Afficher ▾** » de 32 px, sur fond `--raise` avec contour, sert de repère (placée sous la question sur téléphone). Ouvert : cadre plein `--line-2`, « Masquer ▴ », contenu sous un filet. |
| Tableaux | Les styles inline (`font-size:.82rem`, `border … var(--grid/--border)`) sont neutralisés par `!important`. Corps en sans 15,5 → 16,5 px, chiffres tabulaires, cellules de 0,55 / 0,8 em, filets `--line-2`. En-tête (ou rangée avec `style="background…"`) en creux, 600, filet bas de 2 px `--field`. Le conteneur défile en largeur. |
| Figures, SVG | Centrés, `max-width:100%`. Légende en serif italique de 15,5 px, encre 3. Les couleurs viennent **toujours** des variables (le contenu les emploie déjà). |
| `pre`, `code` | JetBrains Mono 0,84 em, sans ligatures. `pre` : creux, filet `--line`, rayon de 10 px, défilement horizontal, interligne 1,55. `code` en ligne : creux, rayon de 4 px. |

### 5.3 Exercices

- **Outils** (en tête de l'onglet) :
  - segmenté Tous / Facile / Moyen / Difficile, qui filtre les `.exo` par `data-niveau` ;
  - puce « Concours PT · n », qui ne garde que `.exo.concours` ;
  - « 8 exercices corrigés » en encre 3 à droite.
- **`.exo`** : une carte `--sheet`, contour `--line`, rayon de 16 px, padding 1,3 / 1,5 rem (1,1 / 1 rem sur téléphone), avec 20 px d'écart entre exercices.
  - **En-tête** : « EXO 01 » (`.num`), surtitre de 13 px en 700, encre de la matière ; puis la **difficulté** (`.diff`, enrichie par script, §7.2) : **3 barres** de hauteur croissante (pleines dans l'encre vive de la matière, vides en `--line-2`) suivies du **mot** (« Facile », « Moyen », « Difficile », 13 px 600). C'est fini les ★☆ de 10 px isolés en haut à droite.
  - **Titre `h3`** : serif 20 → 23 px.
  - **`.statement`** : énoncé en serif, au corps du texte.
  - **`.q`** : « Q1. » en **retrait suspendu** de 2,5 rem, en sans gras dans l'encre de la matière.
  - **`.exo-part`** : surtitre neutre (« PARTIE A — … »).
  - **`.exo-source`** : encart creux en sans 14 px.
- **`.toggle-sol`** : bouton secondaire « Voir la solution ▾ » / « Masquer la solution ▴ » (38 px, 44 au doigt).
- **`.solution`** : creux, filet gauche **vert vif** de 3 px, intitulé « CORRECTION » (le `h4` existant) en surtitre vert, serif 16,5 → 17,5 px.
- **`.exo.concours`** : liseré intérieur de 3 px **à l'encre** en haut ; badge « CONCOURS PT » en aplat d'encre ; source en encart creux.
- **Rail** (≥ 1 360 px) : liste des exercices et rappel « Mes cartes » (§4.4).
- L'anomalie connue des 73 exos « Concours PT » hors `.exo-wrapper` n'empêche pas ce style : il ne dépend que de `.exo`.

### 5.4 Cartes de révision (onglet Cartes, quiz, révisions du jour)

Le gabarit est commun. Le DOM réel de `makeFlash` se compose de :
- `.flash-wrapper` ;
- `.flash-progress` ;
- `.flash-card`, qui contient `.flash-side` (avec `.tag` et le contenu) et `.flash-hint` ;
- `.flash-controls`, avec `.hard`, `.ok` et `.easy` ;
- `.flash-stats-wrap` ;
- les boutons ajoutés par le JS : `.flash-course-link`, `.flash-flag-btn` et `.flash-tts-btn`.

Le quiz (`.quiz-card`, `.quiz-rate-btn`, `#quiz-reveal-btn`) prend les **mêmes** styles.

**Progression `.flash-progress`.** « Carte 12 / 26 », puis une barre empilée de 4 px (acquises / hésitantes / à revoir), puis « 3 dues ».

**Fiche bristol `.flash-card`.**
- Fond `--bristol`, rayon de 16 px, ombre `--sh-2`, contour `--line`.
- **Hauteur fixe** entre recto et verso : elle remplit l'espace disponible. Sur téléphone : `100dvh` − chrome − commandes.
- **En-tête `.fc-head`** : badge matière, badge type (« Formule » si `cat:'form'`, « Grandeur » si `'val'`, rien sinon), badge « Dernière note : à revoir » (contour, avec une pastille de la couleur de la note) ; à droite, 🔊 pour l'anglais.
- **Filet rouge** `--marge` de 2 px sous l'en-tête.
- **Recto.**
  - Surtitre « QUESTION ».
  - Question en **serif 600, 22 → 26 px**, interligne 1,45, avec la **réglure bleue** `--reglure` calée sur `1lh`, qui remplit la fiche.
  - La réglure est **supprimée automatiquement** si la question contient une fraction ou une formule en bloc (`:has(mjx-mfrac, mjx-container[display="true"])`). Elle suit A−/A+, puisqu'elle est en unité `lh`.
  - Pied : « ⏱ Formule la réponse de tête, puis touche la carte. » (au doigt) ou « … puis Espace » (à la souris).
- **Verso.**
  - La **question reste en rappel** (serif 17 px, encre 2, sans réglure).
  - Séparateur « RÉPONSE » (surtitre vert, entre deux filets).
  - Réponse en serif, au corps du texte. Une formule en bloc y prend le style `.formula`.
  - Pied : « 📖 Voir dans le cours · §3 » (lien, 44 px de haut) et « ⚑ Signaler » à droite.
- **Cartes d'anglais** : texte brut, sans `flashPretty`, et 🔊 dans l'en-tête. La lecture TTS est inchangée.

**Commandes**, de haut en bas, sous la fiche :
1. Ligne « ‹ Précédente » à gauche, « Passer » à droite (boutons discrets de 44 px). Au verso aussi, « Passer » garde le même mot.
2. **Tout en bas, à l'endroit même du pouce** :
   - au recto, « ⟲ Afficher la réponse » (bouton primaire de 64 px, pleine largeur) ;
   - au verso, **3 boutons de notation** de 64 px : `.hard` « ↺ À revoir », `.ok` « ∿ Hésitant », `.easy` « ✓ Acquis ». Chacun porte en dessous l'**échéance Leitner** calculée par `srsSchedule` (« aujourd'hui », « dans 3 jours », « dans 7 jours ») et, à la souris seulement, sa touche 1 / 2 / 3.
   - Les boutons de notation sont teintés de la couleur de leur note (texte ≥ 5:1, contour à 40 % du vif). Contraste : **5,0 à 5,7:1 en clair, 6,7 à 7,2:1 en sombre**, contre 2,6 à 3,6:1 aujourd'hui.

**Flip.**
- C'est le demi-tour mono-face actuel (`makeFlash.flip`). Il est gardé, dans la limite de `--dur-3` (320 ms) ;
- en mouvement réduit, l'échange est instantané (`window.__reduceMotion`) ;
- la carte entière reste cliquable, en `role="button"` avec un `aria-label`.

**Sous la carte.** `.flash-stats-wrap` (14 px, encre 2) et « ↺ Réinitialiser » en lien discret. Les 160 boutons « ↺ Réinitialiser » gardent leur caractère ↺, servi par la police « Symboles TeX ».

### 5.5 Simulateurs (26 canvas, DOM inchangé)

- **Grille `.sim-wrapper`**, sur ordinateur (colonnes `1fr` et 19 rem) :

  ```
  "titre    titre"
  "lead     lead"
  "badge    mode"
  "scene    reglages"
  "info     reglages"
  ```

  Une zone dont l'élément n'existe pas reste vide : certains simulateurs n'ont ni `.mode-switch` ni badge.
- **`h2`** : serif 24 → 32 px. **`.lead`** : serif, encre 2, sur la mesure du texte.
- **`.mode-switch`** : segmenté pleine largeur. Ses libellés peuvent passer sur 2 lignes.
- **`.regime-badge`** : pastille et mot. Ce sont des informations, **pas des notations**, d'où ces couleurs :
  - `.pseudo` : teinte et encre de la matière ;
  - `.critique` : ambre (le seuil) ;
  - `.aperiodique` : neutre, avec un contour ;
  - jamais de rouge ni de vert, qui sont réservés à la notation.
- **`canvas`** (scène) : fond `--sheet`, contour `--line`, rayon de 16 px, dessiné à la résolution de l'écran (`devicePixelRatio`). Les couleurs viennent de `__CV()`, la courbe principale de `--chap-vif`. Les étiquettes sont en JetBrains Mono 12 px, encre 2 ; les grandeurs en serif italique (*u*꜀/*U*₀).
- **`.sim-controls`** : panneau `--sheet` à contour, avec l'intitulé « PARAMÈTRES » généré. Chaque `.control` comprend :
  - un `label` en sans 14 px, encre 2, **sans capitales forcées** (« mH » reste « mH », « µF » ne devient plus « ΜF ») ;
  - un `.value` en pastille creuse, en 600 tabulaire ;
  - un `input[type=range]` stylé : piste de 4 px, partie remplie dans l'encre vive de la matière (variable `--p` mise à jour par le script), poignée de 18 px avec contour vif, 44 px de haut au doigt.
- **Bouton « ↺ Valeurs par défaut »** : bouton discret, en bas du panneau.
- **`.sim-info`** : tuiles en creux. Libellé en sans 13 px, encre 3 (« Pulsation propre ω₀ ») ; valeur en **serif 600 de 20 px, chiffres tabulaires** (« 1 414 rad/s »).
- **Téléphone** (≤ 767 px) : une colonne, dans l'ordre titre, lead, badge, **scène collante** (`top: 100px`, sous la barre et les onglets, avec une ombre), tuiles sur 2 colonnes, mode, réglages. On voit ainsi la courbe en bougeant un curseur.
- **Lorentz** (simulateur SVG hors `CHAPTERS`) : il garde son DOM, prend les couleurs de thème, et sa correction reste un chantier à part (anomalie n° 3).
- Les overrides sombres uniques des encadrés de simulateur (bloc « Contraste des encadrés… ») sont **remplacés** par ces règles, qui passent par les variables.

### 5.6 Quiz (`#quiz-overlay`)

- **Cadre** : plein écran sur téléphone. Sur ordinateur, une modale de 40 rem centrée, avec le voile `--scrim`, un rayon de 22 px et l'ombre `--sh-3`. En-tête `.quiz-header-bar` : titre serif 20 px, ×.
- **Configuration** `#quiz-screen-config` :
  - matières (`qc-<matière>`) en **puces à cocher** avec pastille de matière ;
  - mode, nombre de cartes et type (Formules / Grandeurs usuelles) en **segmentés** ;
  - info « · 1ʳᵉ année » ou « · 1ʳᵉ + 2ᵉ année » en encre 2 ;
  - bouton primaire « Commencer » de 48 px.
- **Question** : la fiche bristol (§5.4), avec en plus `#quiz-chapter-badge` (matière et chapitre) dans l'en-tête de la fiche, la barre de progression `.quiz-progress-bar` (4 px, encre vive de la matière de la carte) et `#quiz-goto-btn` (« Voir dans le cours ») dans le pied.
- **Notation** `.quiz-rate-btn` : identique à `.flash-controls`, tout en bas. 🔊 (`#quiz-tts-btn`) pour l'anglais.
- **Résultats** : score en serif display (« 18/24 »), une ligne par note (`.quiz-result-row`) avec une barre de la couleur de la note, puis les boutons Recommencer (secondaire) et Fermer.
- **Anglais** : texte brut (règle `item.meta.mat === 'anglais'` inchangée).

### 5.7 Aujourd'hui (`#today-overlay`, `05`)

- **Cadre** : plein écran sur téléphone, avec le bureau en fond. Sur ordinateur, une modale de 44 rem, ou un panneau de 32 rem à droite.
- **En-tête** :
  - date en surtitre (`#today-date`, « SAMEDI 18 OCTOBRE ») ;
  - titre « Aujourd'hui » en serif 32 px ;
  - sous-titre amical « Bonjour ! On révise ? » (sans 15 px, encre 2) ;
  - ×.
- **Carte « Révisions du jour »** (`.tcard`) :
  - **« 37 »** en serif display, suivi de « cartes à revoir » en serif 18 px ;
  - « ≈ 12 min · répétition espacée », en comptant environ 20 s par carte ;
  - **barres chiffrées par matière** (pastille, nom, barre dans l'encre vive, nombre tabulaire), calculées par `dueDeck()` ;
  - « ▷ Commencer la révision » (primaire, 48 px) ;
  - Quiz et Calcul mental (secondaires, côte à côte).
- **Carte « Reprendre »** :
  - à droite, l'heure : « hier, 21 h 40 », grâce au champ `t` ajouté à `lastPos` (§7.6) ;
  - vignette « *§3* » en teinte de matière, titre du chapitre en serif 17 px, « Physique · Cours · Régime libre » ;
  - sous un filet, les 2 récents suivants (lignes de 44 px, avec « matière · partie » à droite : la clé `recents` ne retient que des ids de chapitre, l'onglet n'est connu que pour « Reprendre » ; décision de la relecture, tour 1, plutôt qu'une nouvelle clé).
- **Carte « 7 prochains jours »** : histogramme de 7 barres (aujourd'hui en rouge vif, les autres en `--line-2`), avec la valeur au-dessus et le jour dessous. Il est calculé à partir des dates `due` déjà stockées : **aucune nouvelle clé**.
- **Accès rapides** : 4 tuiles creuses de 64 px (Bilan, Formulaire, Signalées, Sauvegarde).
- **« Tout est à jour »** (`.today-uptodate`) : grand ✓ vert vif, « Rien à revoir aujourd'hui », et la date de la prochaine échéance.

### 5.8 Bilan (`#dash-overlay`)

- **Cadre** : comme Aujourd'hui (plein écran sur téléphone, modale de 48 rem sur ordinateur).
- **Global** (`.dash-global`) : « 34 % » en **serif display** (`.dash-big`), « des cartes acquises », barre empilée avec sa légende.
  - En 1ʳᵉ année, une ligne de rappel pour la 2ᵉ année, si elle a des cartes notées.
  - En 2ᵉ année, la ligne « dont 2ᵉ année ».
- **Par matière** (`.dash-mat`, physique, maths, SI) : pastille, nom en sans 600, % en serif 600 de 20 px (`.m-pct`), barre de 8 px dans l'encre vive de la matière.
- **Par chapitre** (`.dash-chap`) :
  - tri par priorité ;
  - l'**anneau** `__ringSVG` dans l'encre vive de la matière (piste `--line-2`), le nom, « 3 à revoir » en rouge ;
  - clic → `navigateTo` vers les Cartes ;
  - lignes de 48 px.
- **Bouton** « Réviser » (`.dash-revise-btn`) en `.btn-chap`.
- **Surtitres** `.dash-section-label` : capitales de 13 px.

### 5.9 Recherche (`#search-overlay`)

- **Cadre** :
  - ordinateur : une modale de 40 rem, à 12 vh du haut ;
  - téléphone : plein écran, avec un **× visible** en haut à droite (correctif de l'audit).
- **Champ** `#search-input` : 48 px, sans 17 px, icône loupe ; « Échap » affiché à la souris seulement.
- **Résultats** `.search-result` :
  - groupés par nature (Chapitres, Sections, Formules, Cartes), avec un surtitre de 13 px ;
  - chaque ligne de 48 px porte la pastille de la matière, un titre de 15–16 px avec la correspondance en `<mark>` (teinte de la matière), et la provenance en encre 3 (« Physique · RLC · §3 ») ;
  - la ligne active (↑↓) est en `--hover`, avec un rail de 2 px dans l'encre vive.
- **`.search-hint-bar`** (↑↓ ↵ Échap) : masquée au doigt.

### 5.10 Formulaire (`#formula-overlay`)

- **Cadre** : modale de 48 rem ; plein écran sur téléphone.
- **En-tête** `.formula-head` : titre « Formulaire » en serif 24 px avec le nom du chapitre en encre 2, boutons Imprimer (`.formula-print-btn`, secondaire) et ×.
- **Corps** :
  - les sections du chapitre en surtitres de matière (« §1 · LES BASES ») ;
  - chaque formule en `.formula`, avec son nom au-dessus (le `data-nom`, quand il existe) ;
  - les formules consécutives fusionnées.
- **Vide** `.formula-empty` : texte en encre 2, centré.

### 5.11 Autres fenêtres

Elles partagent le gabarit des modales : `--raise`, rayon de 22 px, `--sh-3`, en-tête titre + ×, plein écran sur téléphone, Échap et retour Android pour fermer, focus piégé, retour du focus au bouton d'origine.

- **Sauvegarde** (`#backup-overlay`) : explication en sans 15 px, « Exporter » (primaire), « Importer » (secondaire, avec `input[type=file]` caché).
- **Cartes signalées** (`#flag-overlay`) : liste de cartes (question en serif 16 px, matière et chapitre en encre 3). « Copier » et « Télécharger » en boutons secondaires (non migrés vers les icônes, comme aujourd'hui).
- **Calcul mental** (`#drill-overlay`) : la question en serif 32 px ; le champ `#drill-input` de 56 px, chiffres tabulaires 24 px, `inputmode="decimal"` ; le retour juste / faux en vert ou rouge **avec ✓ / ↺ et un mot**.
- **Raccourcis** (`.key-help-box`) : tableau de 2 colonnes, `kbd` à gauche, action à droite ; se ferme avec Échap.

### 5.12 En-tête ordinateur (`.hdr`, remplace `header` / `.header-nav` / `.header-actions`)

- Hauteur de 56 px, **collant**, fond `--sheet` à 92 % avec flou, filet bas `--line`.
- Contenu, de gauche à droite :
  1. bouton de la navigation (`#nav-toggle-btn`) : il replie ou affiche la barre latérale à partir de 1 200 px, et ouvre le tiroir en dessous ;
  2. marque : **carré « § »** (28 px, aplat d'encre, « § » en serif italique couleur feuille) et « Mes cours de *prépa* » en serif 600 de 19 px, « prépa » en italique 500 ;
  3. **champ de recherche visible** : 26 rem au plus, creux, « Ctrl K ». Le clic ou le raccourci ouvre la recherche (§5.9) ;
  4. espace ;
  5. **Aujourd'hui** et **Bilan** (boutons discrets avec icône, qui passent en icônes seules sous 1 100 px) ;
  6. « **Réviser** 37 ▾ » (primaire, ouvre `#study-menu`) ;
  7. séparateur ;
  8. **Thème** (icône, ouvre le popover du §4.6) ;
  9. **Plus** ⋯.

### 5.13 Tiroir et barre latérale (`#mob-drawer`)

- **De 1 200 px en haut** : `#mob-drawer` devient la barre latérale permanente de 288 px, collante sous l'en-tête, sur fond bureau, avec un filet droit `--line`. `#mob-drawer-overlay` est masqué.
- **Sous 1 200 px** : tiroir de 320 px qui glisse depuis la gauche (`--dur-3`), avec le voile.
- **Sous 768 px** : page plein écran « Chapitres » (§4.3).
- Les rangées `.mob-chap-row`, `.mob-chap-item` et `.mob-pin` se restylent en `.nav-item`, les boutons `.mob-mat-btn` en `.mat-tab`, et `.mob-year-btn` en segmenté.
- L'état replié de la barre latérale sur ordinateur est mémorisé dans une **nouvelle clé** `navCollapsed`. Elle est à documenter dans CLAUDE.md, ne commence pas par `flash:`, et est exportée par la Sauvegarde.
- Les barres de commande invisibles (`.subdomain-bar`, `.chapter-bar`, `.chap-btn`) **ne changent pas** : elles restent la couche de commande.

### 5.14 Bandeaux

- **`.chap-title-banner`** devient l'**intercalaire** (§4.4). Ses classes `.mat-<matière>` sont remplacées par `data-mat`, et `.ctb-sub` et `.yr2a` par le fil d'Ariane et le badge d'année.
- **Bandeau d'impression** : voir §5.15.
- **`.matiere-bar`** (déjà masquée en sombre) : supprimée.

### 5.15 Impression (`printChapter()`, gabarit dans `#print-iframe`)

Le correctif B5 (formules dessinées, exercices non découpés) est gardé. On ajoute :
- `<link rel="stylesheet" href="vendor/fonts/polices.css">` à la place de `fonts.css` ;
- `chtml.scale: 1.07` dans la configuration MathJax du gabarit ;
- le **thème clair forcé** : pas de `data-theme`, `color-scheme: light`, jetons du bloc clair, sans le filet de sécurité Auto, avec `print-color-adjust: exact` seulement pour les teintes des encadrés.

**Page de garde.**
- Surtitre « PT · 2ᵉ année » ou « PTSI · 1ʳᵉ année », dans l'encre de la matière.
- Titre en serif 600, 28 pt.
- Matière en sans 11 pt.

**Corps.**
- Serif 11 pt, interligne 1,45, mesure pleine page, marges de 18 mm.
- h2 : 16 pt ; h3 : 13 pt.
- `.formula` : fond `--sunk`, ou filet gris clair si l'imprimante ne rend pas les fonds.

**Sans papier millimétré, filet de marge, ombres ni intercalaire teinté.** L'intercalaire est remplacé par un filet de 2 pt dans l'encre de la matière.

**Encadrés.** Ils gardent leurs intitulés générés (DÉFINITION, À RETENIR, À NOTER, CORRECTION). Les `.reveal` et les solutions sont **imprimés ouverts**.

**Coupures.** `break-inside: avoid` sur `.formula`, les encadrés et `.exo` (il l'est déjà par B5) ; `break-after: avoid` sur h2 et h3.

---

## 6. États, accessibilité, mouvement

### 6.1 États

| État | Règle |
|---|---|
| Survol | Fond `--hover` (éléments discrets) ou `--sunk` + contour `--field` (boutons secondaires) ; `--primary-hover` pour le primaire. Pas de survol qui change la taille. |
| Focus visible | `outline: 2px solid var(--focus)` décalé de **2 px** (il touche toujours le fond, jamais le bouton : ≥ 3:1 sur feuille, bureau, creux et menu, dans les deux thèmes). Jamais retiré. Champs : même anneau. Rangées de navigation : l'anneau englobe la rangée. |
| Actif / choisi | Onglet : encre + 600 + soulignement vif de 3 px. Segment : fond haut + contour `--field`. Rangée courante : teinte de la matière + rail + `aria-current`. Intercalaire : teinte + filet de 4 px + gras. Carte de thème : contour de 2 px à l'encre. |
| Appui | Descente de 1 px (boutons) ; `--press` (éléments discrets). |
| Désactivé | Opacité 0,45, `cursor:not-allowed`, `aria-disabled="true"`. Pas d'autre changement de couleur : le contraste n'est pas exigé pour un élément inactif. |
| Sélection de texte | `--selection` (bleu à 16 % / 15 %). Texte 3 sélectionné : ≥ 4,55:1. |
| Chargement | Panneaux non encore rendus par MathJax : rien n'est masqué (le TeX brut reste masqué, comme le prévoit le lot 0 du plan). |

### 6.2 Contrastes

Tous les textes sont ≥ 4,5:1 (≥ 3:1 au-dessus de 24 px, ou de 18,7 px en gras). Les éléments graphiques porteurs de sens (pastilles, filets d'onglet actif, contours de champ, barres, focus) sont ≥ 3:1. Les chiffres sont au §8.

### 6.3 Cibles, lecture d'écran, clavier

- Au doigt (`pointer:coarse`), **toute cible fait ≥ 44 × 44 px** : boutons, segments, puces, rangées, onglets, menus, curseurs, liens isolés (« Voir dans le cours »). C'est mesuré : 0 exception sur les 10 maquettes téléphone (§8).
- La couleur n'est **jamais le seul repère**. Les notations ont une icône et un mot, la difficulté des barres et un mot, les matières leur nom, les cartes dues un compteur chiffré.
- ARIA :
  - onglets en `role="tablist"` / `tab` / `aria-selected` ;
  - intercalaires en `tab` ;
  - segmentés en `aria-pressed` ou en `radiogroup` ;
  - popover Thème en `role="dialog"`, cartes en `radio` ;
  - feuilles et fenêtres en `role="dialog"`, avec `aria-label`, focus piégé et retour du focus ;
  - barres empilées et histogrammes en `role="img"` + `aria-label` chiffré.
- Clavier :
  - les raccourcis globaux restent ;
  - les raccourcis des cartes (1 / 2 / 3, Espace, ← →) sont **étendus aux 160 decks**, avec une **garde de saisie** : inactifs quand le focus est dans un champ, et derrière une fenêtre ouverte (anomalie n° 4 de l'audit) ;
  - Échap ferme tout panneau ouvert.

### 6.4 Mouvement réduit

`prefers-reduced-motion: reduce` :
- `--dur-1/2/3` passent à 0 ;
- toutes les transitions et animations sont coupées, `scroll-behavior` repasse à `auto` ;
- la barre du téléphone se masque **sans glisser** ;
- le retournement des cartes est instantané (`window.__reduceMotion`, déjà en place) ;
- les feuilles et le tiroir apparaissent sans glissement.

`prefers-contrast: more` : l'encre 3 prend la valeur de l'encre 2, et les filets prennent la valeur `--field`.

---

## 7. JavaScript : ajouts et retouches ciblés

Le contenu des 160 chapitres n'est pas réécrit. Chaque ajout ci-dessous est **idempotent** : un marqueur `data-…` évite tout second passage. Il est **défensif** (`if(!el) return;`), pour qu'une erreur ne coupe pas le grand script.

1. **`data-mat`** sur chaque `.chapter`, posé à côté de `data-domain` depuis `CHAPTERS_BY_ID[id].matiere`. Le poser aussi sur les rangées du tiroir et sur `.chap-title-banner`.
2. **Découpage de `.sec-num`** en `<span class="sec-n">§1</span><span class="sr"> · </span><span class="sec-t">LES BASES</span>`. Le `.sr` garde un `textContent` lisible (« §1 · LES BASES ») pour le sommaire, la recherche et les lecteurs d'écran.
   **Enrichissement de `.diff`** : on compte les ★ (n) et on écrit `data-niveau="n"`, puis les barres et le mot (Facile, Moyen, Difficile), avec un `title`. Les étoiles disparaissent.
3. **Typographie française et `.mj-large`** (§2.5) : à lancer dans la promesse de `typesetPanel` (et après le rendu d'une solution ou du Formulaire), sur le seul panneau concerné. Ne pas toucher `code`, `pre`, `kbd` ni `mjx-container`.
4. **Intercalaire** : `injectChapterTitleBanners` écrit :
   - le fil d'Ariane (matière en lien vers le Sommaire, `subLabel`, `matiereLabel`) ;
   - le titre (`h2.ctb-title`) ;
   - les actions (Formulaire → `#formula-btn` existant, Imprimer → `printChapter`, Épingler → la bascule de `pinned`) ;
   - la méta (année via `__YEAR2A`, nombre de `.course-section`, de cartes (`FLASH_REGISTRY[prefix].length`), de `.exo`, de simulateur).
5. **Onglets** : les « 01–05 » sont masqués en CSS. On ajoute un `.cnt` et un `.count` (cartes dues du deck, via `srsIsDue`) sur Cartes, un `.cnt` sur Exercices et sur Méthodes. Mise à jour par `window.__updateReviseBadge`.
6. **`lastPos.t`** : un horodatage ajouté au JSON existant (même clé, rétrocompatible) pour « Reprendre · hier, 21 h 40 ».
7. **Sélecteur de thème** (§4.6) :
   - popover sur `#theme-btn` à la place du clic cyclique ;
   - segmenté dans la feuille ⋯ ;
   - `window.__setTheme(pref)` ;
   - « actuellement » mis à jour par `matchMedia` ;
   - la meta `theme-color` suit `--sheet`.

   `#mob-theme-btn` quitte la barre haute.
8. **Barre du téléphone** (§4.2) :
   - surtitre et titre depuis `CHAPTERS` (matière, `subLabel`, année) ;
   - masquage au défilement (un seul écouteur `scroll` passif, `requestAnimationFrame`, seuil de 8 px, actif au-delà de 120 px) ;
   - libellé de section depuis le scroll-spy existant ;
   - bouton Réviser → `quizStartDue()`.
9. **Cartes** (§5.4), dans `makeFlash` et l'équivalent du quiz :
   - le verso affiche la question en rappel ;
   - les boutons de notation reçoivent leur icône, leur échéance (dérivée de `SRS_INTERVALS` et de la boîte courante) et leur touche ;
   - en-tête de la fiche (badges) ;
   - aide selon le pointeur ;
   - progression empilée ;
   - raccourcis 1 / 2 / 3 / Espace sur tous les decks, avec la garde de saisie.

   **L'état des cartes (`flash:` et `flashids:`) n'est pas touché.**
10. **Rail** : « Mes cartes » (via `FLASH_INSTANCES[prefix].getProgress()`), et liste des exercices sur l'onglet Exercices (lien vers l'`.exo`, avec l'exercice visible suivi par IntersectionObserver). Le filtre de difficulté et la puce Concours masquent ou affichent les `.exo`.
11. **Pied de chapitre** : `#chap-pager` restylé ; ses noms existent déjà (`#prev-chap-name`, `#next-chap-name`).
12. **Navigation** :
    - filtre groupé par matière, avec `<mark>` et l'année ;
    - rangée « + N chapitres de 1ʳᵉ année » en 2ᵉ année ;
    - puces Épinglés et Récents ;
    - intercalaires avec effectif ;
    - clé `navCollapsed` ;
    - **Sommaire de la matière** (`#sommaire/<matière>`, extension de `urlRouting`).
13. **Aujourd'hui** : barres par matière, histogramme sur 7 jours (dates `due`), salutation, heure de reprise.
14. **Simulateurs** :
    - `--p` sur chaque `input[type=range]`, mis à jour à `input` ;
    - `getCanvasColors()` lit `--text-3` et `--line` au lieu des valeurs codées en dur `muted` et `grid` ;
    - courbe principale en `--chap-vif`.
15. **Polices et MathJax** :
    - nouveau `polices.css` (dans le `<head>` et dans l'impression) ;
    - `chtml.scale: 1.07` (aux deux endroits) ;
    - mentions nominatives remplacées (§2.1) ;
    - `PRECACHE` et `CACHE_VERSION` mis à jour.

---

## 8. Contrôles chiffrés

Tous les contrôles se relancent avec les scripts de `outils/` (Playwright et Chromium du conteneur, `FONTCONFIG_FILE` sans les polices Latin Modern).

### 8.1 Jetons : `outils/contrastes-jetons.py` → `controles/contrastes-jetons.json`

- **Bloc « Auto + système sombre » identique au bloc sombre : oui.**
- **Clair : 129/129 paires conformes. Sombre : 129/129.**
- Les paires couvrent :
  - les 3 encres sur les 5 fonds et sur le survol ;
  - le bouton principal, au repos et survolé ;
  - le compteur plein ;
  - les liens ;
  - le contour de champ sur les 4 fonds ;
  - l'anneau de focus sur les 4 fonds ;
  - le texte sélectionné ;
  - pour chaque matière, l'encre sur la feuille, le bureau, le menu, le creux et sa teinte ; le texte et les encres 2 et 3 sur sa teinte ; le vif sur la feuille, la teinte, le bureau et le menu ;
  - pour chaque couleur sémantique, l'encre sur la feuille, la carte, le creux et sa teinte ; le texte sur sa teinte ; le vif ;
  - les 6 variables historiques du contenu sur `--paper` et `--paper-dark`.
- Marges les plus faibles :

  | Thème | Texte (seuil 4,5:1) | Éléments graphiques (seuil 3:1) |
  |---|---|---|
  | Clair | 4,55:1 (encre 3 sur la sélection) | 3,21:1 (contour de champ sur le bureau) |
  | Sombre | 4,94:1 (encre 3 sur la sélection) | 3,38:1 (contour de champ sur un menu) |

- **Écarts OKLab entre encres** (×100) :
  - clair, minimum **9,1** : SI/vert 9,1, physique/info 9,2, SI/info 9,6, physique/anglais 9,6, maths/rouge 10,0, rouge/ambre 11,0 ;
  - sombre, minimum **8,3**.
  - Pour comparaison, P1 : 5,8 (rouge/orange). P3 : 1,2 (SI/vert).

### 8.2 Maquettes rendues : `outils/contrastes-dom.js` → `controles/contrastes-maquettes.json`

- **19 maquettes × 2 thèmes : 14 412 mesures, 0 échec.**
- Chaque élément visible portant du texte, chaque glyphe de formule MathJax, chaque icône et chaque pastille de matière est mesuré contre son fond réel, transparences composées.
- Mesure la plus faible :
  - en clair, la pastille SI (graphique) à **3,30:1** (seuil 3), et en texte, « onde » surligné à **4,81:1** ;
  - en sombre, le point séparateur de la méta à **5,5:1**.
- La `.notice` est à 15:1 en clair et 11,5:1 en sombre (aujourd'hui : 1,99:1 en sombre). Les boutons de notation sont entre 5,0 et 5,7:1 en clair et entre 6,7 et 7,2:1 en sombre (aujourd'hui : 2,6 à 3,6:1).

### 8.3 Cibles tactiles : `outils/cibles.js` → `controles/cibles-tactiles.json`

- **10 maquettes téléphone, 0 cible sous 44 × 44 px** (et donc aucune sous 24 px).
- Exception WCAG « inline » : les liens dans une phrase.

### 8.4 Captures : `outils/capture.js` → `captures/rapport-captures.json`

Sur les 19 captures :
- **0 débordement horizontal** ;
- **0 texte sous 12 px** ;
- 0 erreur JS ;
- **0 requête externe** ;
- polices réellement chargées : Source Serif 4 (romain et italique), Source Sans 3, JetBrains Mono, Symboles TeX, plus les fontes MathJax.

### 8.5 Mesures typographiques : `outils/mesures.js`

| Mesure | Ordinateur | Téléphone |
|---|---|---|
| Corps | 19 px, interligne 30,4 px | 17,5 px, interligne 28 px |
| Colonne | 646 px, **68 signes par ligne** en moyenne | 358 px, **41 signes par ligne** |
| Titre du chapitre | 44 px | 17 px (barre) |
| Début du texte | — | **124 px** sous le haut de l'écran |

### 8.6 Couverture des glyphes : `outils/couverture.py`

- Les caractères non ASCII du site sont presque tous couverts par les polices retenues, Symboles TeX compris.
- Il reste 63 caractères rares (1 444 occurrences), dont 712 ☆ qui seront remplacés par les barres de difficulté.

---

## 9. Ordre de mise en œuvre et points de vigilance

1. **Socle** :
   - polices (`vendor/fonts`), `PRECACHE` et `CACHE_VERSION` ;
   - `tokens.css` en tête du `<style>`, en remplacement des `:root` actuels ;
   - `chtml.scale` ;
   - `data-mat`.

   Vérifier `getCanvasColors` en clair et en sombre (suite `regressions`, B4).
2. **Contenu** : §5.2 et §5.3. On supprime les 7 définitions successives de `.def-box`, `.prop-box` et `.method-box`, et les règles par domaine (`.chapter[data-domain=…] h3`). On ajoute les scripts §7.2 et §7.3.
3. **Coquille** : en-tête, barre latérale et tiroir, intercalaire, rail, pied, barre du téléphone. Les barres de commande invisibles restent intactes.
4. **Révision** : cartes, quiz, Aujourd'hui, Bilan. Faire une **Sauvegarde** avant, et vérifier que l'état est identique octet pour octet.
5. **Thème et fenêtres** : sélecteur, recherche, formulaire, modales, impression.

**Tests à surveiller :**
- la suite `visuel` du dépôt (contraste, taille du texte, débordements, cibles tactiles), qui doit passer en `--strict` sur les nouveaux styles ;
- `DEBORDEMENTS_CONNUS` (suite `mobile`) : `rlc-cours` ne doit plus déborder (formules en défilement) ; retirer de la liste les panneaux corrigés ;
- `TEX_EN_CLAIR_CONNUS` ;
- les suites `site` et `interactions`, parce que les sélecteurs des onglets et des cartes ne changent pas ;
- `regressions` doit rester verte.

**Ne pas faire :**
- poser `overflow:hidden` sur `html`, `body` ou `.phone` : cela casse les barres collantes. Utiliser `overflow-x:clip` ;
- utiliser `--border` ou `--surface` pour du nouveau code : ce sont des alias de compatibilité. Utiliser `--line-2` et `--sunk` ;
- coder une couleur en dur, sauf dans les mini-vues du sélecteur de thème ;
- remettre une barre fixe en bas sur téléphone ;
- réintroduire le sommaire en puces sur téléphone ;
- ouvrir « Aujourd'hui » au lancement.
