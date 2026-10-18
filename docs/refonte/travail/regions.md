# Régions du grand `<style>` d'index.html — propriétaires et références

État au commit du SOCLE (branche `wip/refonte`). Le grand `<style>` (en tête d'`index.html`)
est découpé en neuf régions balisées, dans cet ordre (= ordre de la cascade) :

```
/* ===== RÉGION X ===== */
/* description + propriétaire */
…règles…
/* ===== FIN RÉGION X ===== */
```

Trouver une région : `grep -n 'RÉGION' index.html`. Remplacer tout le contenu d'une région
(en gardant ses balises) : `python3 scratchpad/refonte/impl/socle/remplacer_region.py index.html X fichier.css`.

## Règles du jeu (pour travailler en parallèle sans conflit git)

1. **On n'écrit que dans sa région.** Une règle va dans la région de son **sujet** (la composante la
   plus à droite du sélecteur) : `.today-chap-btn .mob-filter-tag` → REVISION, `.chapter[data-domain] h3`
   → CONTENU, `:root[data-theme="dark"] X` → région de X. Les blocs `@media` sont dupliqués par région
   (chaque région a ses propres `@media (max-width:767px)`, `(min-width:768px)`…).
2. **JETONS et BASE sont figés** (socle). Besoin d'un jeton de plus : propriété personnalisée locale
   dans sa région (ex. `.quiz-modal{ --q-pad: … }`) ou demande au socle. Ne jamais redéfinir un jeton
   global ailleurs.
3. L'ordre des régions fixe la cascade : une région plus bas l'emporte à spécificité égale. Le
   rangement initial a été contrôlé : **aucune** inversion de cascade entre deux règles applicables au
   même élément (6 158 couples réordonnés testés sur le DOM réel, 40 états), styles calculés identiques
   avant/après. Si une ligne a besoin de battre une règle d'une région située plus bas, elle le fait par
   la spécificité, pas en déplaçant des règles chez le voisin.
4. Thème sombre des composants : **uniquement** `:root[data-theme="dark"] …`. Le seul
   `@media (prefers-color-scheme: dark)` autorisé est le filet de sécurité des jetons (région JETONS).
5. Aucune couleur codée en dur (sauf mini-vues du sélecteur de thème, SPEC §4.6) ; nouveaux noms de
   jetons uniquement (`--line-2`, `--sunk`… ; jamais `--border`/`--surface`, alias de compatibilité).
6. Une règle en liste à cheval sur deux régions a été **scindée** (même déclarations, une règle par
   région) : ex. `.tab` (PAGE) / `.mat-btn, .chap-btn` (COQUILLE) ; `.quiz-modal, .dash-modal,
   .today-modal` (REVISION) / `.search-modal, .backup-modal, .formula-modal` (FENETRES) ;
   `@media(max-width:767px){ header, .subdomain-bar, .chapter-bar, #back-to-top }` (COQUILLE) /
   `.toc, .toc-wrapper > .toc` (PAGE).
7. Keyframes : `modalIn` (partagé REVISION + FENETRES) est en BASE ; `panelIn*`, `chapterIn`,
   `fadeIn` en PAGE ; `coursTargetFlash*` en CONTENU ; `mjxIn`, `ttsPulse` en REVISION.

## Lignes de travail (SPEC §9) → régions possédées

| Ligne (SPEC §9) | Régions |
|---|---|
| 1. Socle (fait) | JETONS, BASE |
| 2. Contenu | CONTENU, SIMU |
| 3. Coquille | COQUILLE, PAGE |
| 4. Révision | REVISION |
| 5. Thème et fenêtres | FENETRES, IMPRESSION (+ sous-bloc « Sélecteur de thème » de COQUILLE, voir ci-dessous) |

**Sélecteur de thème** : la consigne le range dans COQUILLE. Si les lignes 3 et 5 tournent en
parallèle, la ligne 5 ajoute ses règles (popover `#theme-btn`, segmenté de la feuille ⋯) dans un
sous-bloc délimité `/* --- Sélecteur de thème (ligne 5) --- */ … /* --- fin sélecteur de thème --- */`
placé **à la fin** de la région COQUILLE, juste avant sa balise de fin, et la ligne 3 n'y touche pas.

## Détail par région

### JETONS — socle (figé)
- Contenu : `tokens.css` de la conception (polices `--font-text|ui|code`, graisses `--w-*`, échelle
  `--fs-*`, interlignes `--lh-*`, approches `--track-*`, mesure `--measure`, espacements `--sp-*`,
  rythme `--flow-*`, gabarits `--header-h`, `--bar-h`, `--tabs-h`, `--sidebar-w`, `--rail-w`,
  `--margin-col`, `--sheet-max`, `--tap`, rayons `--r-*`, mouvement `--ease`, `--dur-1/2/3`, plans
  `--z-*` ; couleurs clair, bloc sombre `:root[data-theme="dark"]` **+ sa copie** filet de sécurité
  `@media (prefers-color-scheme: dark){ :root[data-theme-pref="auto"], :root:not([data-theme-pref]):not([data-theme]) }` ;
  notation `--note-*` ; rôles `--chap`, `--chap-fond`, `--chap-vif`, `--def-*`, `--prop-*`, `--meth-*`,
  `--notice-*`, `--sol-*`, `--reveal-trait`, `--mill-*` via `[data-mat]` ; alias `--ink`, `--paper`,
  `--paper-dark`, `--muted`, `--grid`, `--border`, `--surface`, `--accent`, `--accent-deep`, `--accent2`,
  `--green`, `--amber`, `--shadow*`, `--radius-*`, `--read-scale`, `--dom-*` ; `html{font-size}` (A−/A+) ;
  `prefers-contrast: more` et `prefers-reduced-motion` sur les jetons.
- `data-mat` est posé en JS sur chaque `.chapter`, chaque `.mob-chap-row` du tiroir et chaque
  `.chap-title-banner` (les `.mob-mat-btn`/`.mat-btn` portaient déjà `data-mat`).
- composants.css : — ; SPEC : §2.1, §2.3, §3.1 à §3.8, §6.4 (`prefers-contrast`), §8.1.

### BASE — socle (figé)
- Contenu : reset (`*`, `html`, `body` sur `--desk`, sans quadrillage, `overflow-x:clip`), sélection,
  focus `--focus`, `button{font:inherit}`, `a`, `code/kbd/pre/samp`, `.ic`, `.ic-s`, `.ic-lbl`, `.sr`,
  `mjx-container`, `.desk`, barres de défilement, `@keyframes modalIn`, `.empty-state`, puis **composants
  de base** prêts à l'emploi : `.btn` (`-primary`, `-chap`, `-ghost`, `-icon`, `-lg`, `-block`),
  `.count` (`-soft`, `-quiet`), `.badge` (`-chap`, `-strong`, `-out`, `-2a`), `.dot`, `.chip`, `kbd`/`.kbd`,
  `.kbd-hint`, `.seg` (+ `.mode-switch`), `.seg-block`, `.field` (`-soft`), `.menu`, `.menu-item`,
  `.menu-sep`, `.menu-label`, `.kicker`, `.stack` (`.s0/.s1/.s2`), `.legend` ; mouvement réduit global.
- composants.css : §0, §1 (et §15 pour la partie globale) ; SPEC : §2.1, §2.5, §5.1, §6.1–§6.4.
- ⚠️ `.seg, .mode-switch` (composants §1) style déjà en partie `.mode-switch` des simulateurs : les
  anciennes règles `.mode-switch` de SIMU, plus bas, l'emportent encore pour ce qu'elles déclarent.

### COQUILLE — ligne 3 (Coquille)
- Contenu actuel : `header` (+ `.header-nav`, `.header-actions`, `.eyebrow`, `h1`, `.header-today`),
  `.hdr-btn*`, `.rev-badge`, menus `.hdr-more*`, `#more-btn`, `.read-size-ctrl` (A−/A+), `.flag-badge`,
  barre téléphone `#mob-header`, `#mob-menu-btn`, `#mob-chapter-title`, `.mob-header-actions`,
  `#mob-more-*`, tiroir `#mob-drawer*`, `#mob-year-bar`/`.mob-year-btn`, `#mob-mat-bar`/`.mob-mat-btn`,
  `#mob-filter*`, `#mob-chap-list`, `.mob-chap-row`/`.mob-chap-item`/`.mob-chap-label`/`.mob-pin`,
  `.mob-sub-toggle`, `.mob-subdomain-label`, `.mob-drawer-section`, `.mob-filter-tag` (+ `.mt-*`),
  `.mob-filter-empty`, **couche de commande cachée** `.subdomain-bar`/`.sub-btn`, `.chapter-bar`/
  `.chap-btn` (+ `.matiere`, `.yr2a`, `[data-domain]`), `.mat-btn`, `#back-to-top`, `.skip-link`, `footer`.
- À faire (SPEC) : en-tête `.hdr` 56 px (§5.12), barre latérale ≥ 1 200 px / tiroir / page Chapitres
  téléphone (§4.3, §5.13), barre téléphone `.mbar` qui s'efface (§4.2), feuille ⋯ qui monte du bas
  (§4.2), bannière de mise à jour (§5.1 ; aujourd'hui `#sw-update-banner` en style inline dans le JS),
  sélecteur de thème (§4.6, voir ci-dessus). Les barres invisibles et `.chap-btn` **ne changent pas**
  (`display:none !important` à garder). Aucune barre fixe en bas ; pas de sommaire en puces ; pas
  d'anneau de % dans la navigation.
- composants.css : §2 (coquille ordinateur : `.hdr`, `.brand`, `.app`, `.side`, `.main`), §3
  (navigation : `.nav-block`, `.mat-tabs`/`.mat-tab`, `.chips`, `.nav-part`, `.nav-item`), §9 (barre
  `.mbar` ; les onglets `.mtabs` relèvent de PAGE), §12 (sélecteur de thème), §13 (feuille ⋯), §14
  (page Chapitres), §15 (mouvement réduit de la barre et du tiroir).
- SPEC : §4.1, §4.2, §4.3, §4.5, §4.6, §5.1 (menus, bannière), §5.12, §5.13, §5.14 (bandeau),
  §6.3, §6.4 ; JS : §7.7, §7.8, §7.12.

### PAGE — ligne 3 (Coquille, partie page)
- Contenu actuel : `main`, `#si-content`, `.chapter`, `section.panel` (+ animations `panelIn*`,
  `chapterIn`, `fadeIn`), intercalaire `.chap-title-banner` (+ `.ctb-sub`, `.ctb-title`, `.mat-*`,
  `.yr2a`), onglets `nav.tabs`/`.tab`/`.tab .num`, sommaire `.toc-wrapper`/`.toc`/`.toc-title`/
  `.toc-item`/`.toc-content`, pied `#chap-pager`/`.chap-pager-btn`/`.cpg-*`.
- À faire : feuille (`--sheet`, liseré de matière, marge « § » 112 px, filet rouge), intercalaire teinté
  millimétré + fil d'Ariane + actions + méta (§4.4, §5.14 ; JS §7.4), onglets soulignés sans « 01–05 »
  + compteurs (§5.1, §7.5), rail droit sommaire + « Mes cartes » + liste d'exercices (§4.4, §7.10),
  pager en deux cartes (§4.4, §7.11), onglets collants `.mtabs` du téléphone (§4.2).
- composants.css : §4 (feuille, intercalaire, onglets), §8 (rail droit), §9 (`.mtabs`), §2 (`.rail`).
- SPEC : §4.1, §4.4, §5.14 ; JS : §7.4, §7.5, §7.10, §7.11.

### CONTENU — ligne 2 (Contenu)
- Contenu actuel : `.course-section` (+ `::before`, `.sec-num`, `h2/h3/h4`, `.intro`, `p`, listes),
  `.formula`, `mjx-container` (en ligne / en bloc), encadrés `.def-box`, `.prop-box`, `.method-box`
  (+ `.step`), `.notice`, `.reveal`, règles par domaine `.chapter[data-domain=…] …`, `.video-resources`,
  `.hors-prog`, schémas `figure.schema`/`.schema .sk-*`/`.fl-*`/`text.lab-*`/`#sk-arrow-*`, code
  `.codeblock`/`.code-inline`, exercices `.exo-wrapper`/`.exo` (+ `.num`, `.diff`, `h3`, `.statement`,
  `.q`, `.concours`), `.exo-source`, `.exo-part`, `.solution`, `.toggle-sol`, `.cine-svg-wrap`,
  `.panel h2/h3/.sec-num` (scroll-margin), `.cours-target-flash`.
- À faire : SPEC §5.2 et §5.3 ; **supprimer** les 7 définitions successives de `.def-box`/
  `.prop-box`/`.method-box` et les règles par domaine (`.chapter[data-domain=…] h3`, `.sec-num`,
  `::before`) ; scripts §7.2 (découpage `.sec-num`, `.diff`) et §7.3 (typographie française,
  `.mj-large`). Le texte courant est provisoirement en Source Sans 3 (police du `body`) tant que
  `.panel` ne prend pas `--font-text`.
- composants.css : §5 (texte de cours), §6 (exercices).
- SPEC : §2.4, §2.5, §5.2, §5.3 ; JS : §7.2, §7.3.
- Autre bloc `<style>` à elle : le `<style>` dans `#cine-exos` (`.cine-svg-wrap`, `.svg-*`).

### SIMU — ligne 2 (Contenu, simulateurs)
- Contenu actuel : `.sim-wrapper` (+ `h2`, `.lead`), `.sim-controls`, `.control` (+ `label`,
  `input[type=range|number]`, `select`, `.value`), `.regime-badge` (+ `.pseudo`, `.critique`,
  `.aperiodique`), canvas `#…-canvas` (tailles), `.sim-info` (+ `div`, `.lbl`), `.mode-switch`, bloc
  « Contraste des encadrés de simulateur en thème sombre ».
- À faire : grille à zones nommées sans toucher au DOM (§5.5), scène collante sur téléphone, curseurs
  stylés (`--p` posé par le script, §7.14), courbe principale en `--chap-vif` ; le bloc d'overrides
  sombres est **remplacé** par des règles à variables. Lorentz (`lor-*`, SVG) garde son DOM.
- composants.css : §7 (simulateur), §1 (`.mode-switch` partagé avec `.seg`, déjà en BASE).
- SPEC : §3.7, §5.5 ; JS : §7.14. `getCanvasColors()`/`__CV` lisent déjà `--text-3` (muted) et l'encre
  à 8 %/12 % (grid) : suite `regressions` B4 à jour.

### REVISION — ligne 4 (Révision)
- Contenu actuel : flashcards `.flash-wrapper`, `.flash-progress`, `.flash-card` (+ `.flipping`,
  `.flash-mat-*`, `::before`), `.flash-side` (+ `.tag`, sub/sup), `.flash-hint`, `.flash-controls`
  (`.hard`/`.ok`/`.easy`), `.flash-stats-wrap`, `[id$="-stats"]`, `.flash-reset`, `.flash-course-link`,
  `.flash-flag-btn`, `.flash-tts-btn`, `#quiz-tts-btn` ; quiz `.quiz-*`, `.rate-*`, `.score-*`,
  `.fill-acq`, `#quiz-card` ; Aujourd'hui `.today-*` ; Bilan `.dash-*`, `#dash-body`, anneau `.mob-ring`
  (+ `.ring-bg`, `.ring-fg`) ; calcul mental `#drill-*`, `.drill-*` ; cartes signalées `.flag-list`,
  `.is-flagged`.
- À faire : SPEC §5.4, §5.6, §5.7, §5.8, §5.11 (Cartes signalées, Calcul mental). Faire une
  Sauvegarde avant et vérifier l'état octet pour octet : **`flash:`/`flashids:` intouchables**.
- composants.css : §10 (cartes de révision), §11 (Aujourd'hui), §1 (`.stack`, `.legend`, `.count`).
- SPEC : §5.4, §5.6, §5.7, §5.8, §5.11 ; JS : §7.6, §7.9, §7.13.

### FENETRES — ligne 5 (Thème et fenêtres)
- Contenu actuel : recherche `.search-overlay`, `.search-modal`, `#search-input`, `.search-hint-bar`,
  `.search-results`, `.search-result` (+ `.sr-title`, `.sr-meta`, `.sr-snippet`, `mark`) ; formulaire
  `.formula-overlay`, `.formula-modal`, `.formula-head*`, `.formula-print-btn`, `.formula-close`,
  `#formula-body`, `.fsheet-*`, `.formula-empty` ; sauvegarde `.backup-*` ; raccourcis
  `#key-help-modal`, `.key-help-*`.
- À faire : gabarit commun des modales (§5.11), recherche (§5.9), formulaire (§5.10), toasts (§5.1).
- Autre bloc `<style>` à elle : `<style id="sr-badge-style">` injecté par le module « RECHERCHE
  AMÉLIORÉE » du grand script (`.sr-badge`, `.sr-b-*`, `.sr-type-row`, `.search-group-label`…).
- composants.css : §1 (`.field`, `kbd`), §13 (gabarit de feuille, pour le plein écran téléphone).
- SPEC : §4.2 (pages plein écran, retour Android), §5.1 (toasts), §5.9, §5.10, §5.11 ; JS : §7.7.

### IMPRESSION — ligne 5 (Thème et fenêtres, impression)
- Contenu actuel : `@media print` de la page (masquage de la page hors `printChapter`, impression du
  formulaire `body.printing-formula …`, `#chap-pager`).
- Le gabarit d'impression **a son propre CSS** (`const CSS = \`` dans `printChapter`) : il charge déjà
  `vendor/fonts/polices.css`, définit `--font-text|ui|code` et règle MathJax à `chtml.scale 1.07` ;
  reste à faire §5.15 (thème clair forcé, page de garde, corps 11 pt, encadrés imprimés ouverts…).
- SPEC : §5.15 ; correctif B5 (suite `regressions`) à garder vert.

## Ce que le socle a déjà fait (à ne pas refaire)
- Polices : `vendor/fonts/` = 14 woff2 + `polices.css` + licences ; `<link>` page et impression ;
  plus aucune mention de Fraunces / Inter Tight (CSS → `var(--font-*)`, SVG et `ctx.font` → noms réels
  `'Source Sans 3'`, `"Source Serif 4"`, `JetBrains Mono` gardée) ; `PRECACHE` à jour (45 entrées) ;
  `CACHE_VERSION` **non** incrémenté (bump unique à la publication).
- MathJax `chtml.scale: 1.07` (page + impression).
- Thème : script du `<head>` pose `data-theme-pref` + `data-theme="dark"` ; deux `<meta name="theme-color">`
  (#fffdf9 / #191b20) alignées par `applyTheme` sur une préférence explicite ; manifeste aux couleurs
  des jetons. Le bouton `#theme-btn` tourne toujours en cycle (le sélecteur §4.6 reste à faire).
- `data-mat` sur `.chapter`, `.mob-chap-row`, `.chap-title-banner`.

## Dette de transition laissée par le socle (suites `visuel` et `mobile`, listes NON affaiblies)
Les suites `site`, `interactions`, `pwa`, `regressions` sont vertes. `visuel` et `mobile` échouent
sur des écarts dus au nouveau rendu, à corriger par les lignes propriétaires :
- **REVISION / COQUILLE — compteurs rouges en sombre** : `#rev-badge`, `#rev-badge-mob`,
  `#dash-revise-btn`, `span.due-count`, `#today-due-btn span` (2,19:1) et `span.due-sub` (1,96:1) :
  anciennes règles `background:var(--accent); color:#fff` ; `--accent` vaut maintenant `--rouge`
  (#ff9085 en sombre). Cible : `.count` (`--rouge-plein` / `--on-rouge-plein`, 8,1:1 en sombre) et
  `.btn-chap` pour `.dash-revise-btn` (SPEC §5.1, §5.7, §5.8).
- **REVISION** : `span.ic-lbl` « Signaler cette carte » (2,21:1, couleur estompée de `.flash-flag-btn`),
  `button.quiz-btn-reread kbd` (2,71:1 : opacité de l'ancienne règle + `kbd` de BASE en `--text-2`).
- **COQUILLE / FENETRES** : `#search-btn kbd` (4,16:1) et `div.search-hint-bar kbd` (4,1:1) : même
  cause (opacité héritée des anciennes règles sur le `kbd` de BASE) ; disparaissent avec `.hdr` (champ
  « Ctrl K ») et la barre d'aide de la recherche (masquée au doigt).
- **CONTENU — débordements à 390 px** : MathJax à 1,07 élargit les formules de 7 % : `rlc-cours`
  415 → 441 px, 12 autres panneaux connus aggravés (sig-meth, cpx-meth, pol-cours, suit-meth, cd-cours,
  dl-meth, asy-meth, prim-meth, va-cours, ensi-meth, repn-cours), 3 nouveaux (lor-cours 408, asy-cours
  409, int-meth 396). Cible : `.formula{overflow-x:auto}` + `.mj-large` (SPEC §2.5, §5.2) ; ensuite
  retirer de `DEBORDEMENTS_CONNUS` les panneaux corrigés.
- 38 sélecteurs que les jetons ont rendus conformes ont été **retirés** de `TOLERES` (visuel.js).

## Après la ligne A, étape 1 (COQUILLE ET NAVIGATION, branche wip/refonte-a)
- COQUILLE réécrite : grille (§1), en-tête `.hdr` + menus (§2), navigation `#mob-drawer` (barre latérale
  ≥ 1200 px / tiroir 768–1199 / page Chapitres ≤ 767) (§3), Sommaire de la matière (§4), barre `.mbar`
  + feuille ⋯ `.bsheet` (§5), retour en haut / lien d'évitement / pied `.pied` / bannière `.maj-banniere`
  (§6), mouvement réduit (§7), sous-bloc « Sélecteur de thème » en fin de région (fait par la ligne A).
- Colonne de lecture : `<article id="app-main" role="none">` enveloppe sommaire + 2 `<main>` + pager +
  pied (jamais div/section : balises orphelines du contenu). Décalage barre latérale = `#app-main`.
- Règles de COQUILLE dont le sujet relève de PAGE, à reprendre/fusionner par l'étape 2 (spécificité
  haute exprès) : `#app-main nav.tabs{ top }` (collant sous l'en-tête 56 px / la barre du téléphone,
  `html.mbar-cachee` → top 0), `#app-main > main{ margin-top:0 !important }` au téléphone,
  `html.sommaire-ouvert #app-main > main, #chap-pager{ display:none }`.
- `.mob-filter-tag` (étiquette PHY/MATH des récents d'Aujourd'hui) gardée dans COQUILLE, version jetons.
- JS : module « NAVIGATION DES CHAPITRES » (barre du téléphone, feuille ⋯, sommaire), urlRouting
  (#sommaire/<matière>, retour Android), THÈME (popover), menus Réviser/Plus (clavier, « Dans ce
  chapitre »), taille du texte (A / A+ / A++). API pour l'étape 2 : `window.__ouvrirSommaire(mat)`
  (fil d'Ariane), `window.__togglePin(id)` / `__isPinned(id)` (bouton Épingler de l'intercalaire),
  `window.__casPhrase(texte, section)` (titres de section en casse de phrase), `window.__surSection`
  (appelé par le scroll-spy du sommaire interne).
