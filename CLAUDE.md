# CLAUDE.md — Conventions du projet « Révisions PTSI »

Notes destinées à Claude pour les sessions futures. Objectif du projet : rendre maintenable un fichier de révisions PTSI et l'héberger sur GitHub Pages, **sans casser l'existant**.

## Règles de collaboration

- **Tout en français** (réponses, commentaires, contenu).
- **Ne rien casser** de ce qui marche (design + fonctionnalités). Pas de refonte non demandée.
- **Modifications du HTML autorisées sans confirmation préalable** (accord donné par l'utilisateur le 2026-09-26) : agir directement, puis expliquer ce qui a été fait.
- L'utilisateur est étudiant en prépa, débutant en dev. Privilégier des explications claires et des changements incrémentaux.
- **Mise en ligne systématique (consigne de l'utilisateur du 2026-10-05)** : **chaque tâche terminée est publiée sur `main` sans demander la permission**, petits correctifs comme gros changements. Avant de pousser : `validate.py`, `check_js.py`, suites de tests concernées (batterie complète pour un gros changement), bump de `CACHE_VERSION` si un asset change ; pour un gros changement, créer d'abord un point de retour (branche `sauvegarde-avant-…` sur l'état actuel de `main`). Ensuite : vérifier que le run Actions est `completed success`, et dire à l'utilisateur ce qui est en ligne. Ne jamais pousser un travail inachevé ou dont les tests échouent.
- **Contenus de 2ᵉ année (PT spé)** : rédigés à partir des manuels privés du dépôt `thomasMareel/cours-pt-spe` (release v1), qui ne servent qu'à cerner le programme et les notations. **Rédaction originale obligatoire** (site public, droit d'auteur) : ne jamais recopier ni paraphraser de près leurs phrases, énoncés, corrigés, exemples chiffrés, schémas ou plans ; exercices inventés.

## Architecture

- **Un seul fichier servi : `index.html`** (≈ 76 450 lignes, ≈ 6,3 Mo). HTML + CSS + JS tout inline : 15 blocs `<script>` : 4 petits avant (config MathJax, `__icon`, Lorentz, `cstCards`), **un grand script applicatif unique** (de `const Store = (function` au tiroir, puis `data-domain` et la recherche améliorée), puis 10 petits modules. Une exception non rattrapée dans le grand script coupe tout ce qui suit (decks, navigation, quiz, tiroir) : code de chargement défensif (`if(!el) return;`).
- **Ne jamais lire `index.html` en entier** ni se fier à des numéros de ligne : chercher par **ancre grep** (`grep -n 'const CHAPTERS = \['`, puis `sed -n 'A,Bp'`). Titres de blocs CSS : `/* =====`.
- `fichier de départ/` = original intact, **non versionné** (voir `.gitignore`).
- Aucun build. Édition directe du fichier. Autour : `sw.js` + `manifest.webmanifest` (PWA), `vendor/`, `tools/`, `tests/` + `package.json` (tests navigateur), `docs/audit-2026-09.md` (audit de référence : carte du fichier, anomalies, pistes).

### Pilotage data-driven

Le tableau **`CHAPTERS`** (`grep -n 'const CHAPTERS = \['`) est la source de vérité : navigation, redraw des simulateurs, recherche, quiz, tiroir en dérivent. **160 chapitres** : physique 50, maths 48, SI 36, info 8, anglais 18 (dont 52 de 2ᵉ année). Chaque entrée (11 champs) :

```js
{ id:'rlc', prefix:'rlc', name:'Circuit RLC série',
  matiere:'physique', sub:'ondes', subLabel:'Ondes & signaux', domain:'ondes',
  matiereLabel:'Électrocinétique',
  panels:['cours','meth','simu','flash','exos'], drawFn:'drawSim',
  mobLabel:'Circuit RLC série' }
```

- `matiere` ∈ `physique` | `maths` | `si` | `info` | `anglais`. Les chapitres `physique/maths/info/anglais` vivent dans le grand `<main>` ; `si` a son propre `<main id="si-content">` (masqué au départ).
- **Ajouter une matière** = l'ajouter aux énumérations en dur : boutons `.mob-mat-btn` du tiroir (HTML), zone `.mat-content[data-mat-content="X"]`, `buildSidebars` (`['physique',…]`), `buildChapData` + `const MATS` (tiroir), `const MAT_TAGS` (tiroir **et** Aujourd'hui), `colorsMap` et cases `qc-<matière>` du quiz (HTML + listes JS : `grep -n 'qc-physique'`), `perMat` + `matLabel` du **Bilan**, CSS `.flash-mat-*`, `.mt-*`, `.mob-mat-btn.active[data-mat]`, `.quiz-chapter-badge.*`, `.chap-title-banner.mat-*`, variable `--<matière>` si couleur propre.
- **Anglais** : matière de langue, cartes en **texte brut**. `makeFlash` détecte `CHAPTERS_BY_PREFIX[prefix].matiere === 'anglais'` (`isPlainDeck`) et rend `card.q`/`card.a` en HTML brut sans `flashPretty` (sinon « I », « / » seraient mathématisés) ; idem quiz (`item.meta.mat === 'anglais'`). Réponses avec `<strong>`/`<em>`/`<br>` possibles. Panels typiques : `['cours','flash']`. **Lecture audio (TTS)** : `window.__TTS` (Web Speech API, défini AVANT les decks car `makeFlash` teste `__TTS.ok`) — bouton 🔊 sur les flashcards anglaises et dans le quiz (`#quiz-tts-btn`) ; lit la face visible (voix en-GB/fr-FR, gloses françaises retirées), stoppée au flip/changement/fermeture. Les decks **info**, eux, passent par `flashPretty` (anomalie connue).
- `drawFn` : fonction du simulateur (27 chapitres), ou `null`. Le simulateur SVG de Lorentz (`lorDraw`, `lor-simu`) n'est **pas** déclaré dans `CHAPTERS`.
- `CHAPTERS_BY_ID` / `CHAPTERS_BY_PREFIX` sont dérivés automatiquement (après le tri).
- `validateChaptersCoherence()` (IIFE) alerte dans la console au chargement, mais ne compare que les ids de chapitre (`CHAPTERS` ↔ `div.chapter`).

### Ordre d'apprentissage (réorganisation centralisée)

Juste après `CHAPTERS`, l'IIFE `reorderChapters` déclare **`CHAP_GROUPS`** (`grep -n 'const CHAP_GROUPS'`) = `[ [subCode, subLabel, [ids…]] , … ]` (25 groupes, dont `['ia', 'Intelligence artificielle', ['ia']]` en SI, après Capteurs) : **source unique** de l'ordre pédagogique, des **sous-domaines** (`c.sub`) et de leurs **libellés** (`c.subLabel`), qu'il réécrit en réordonnant `CHAPTERS` en place. `subCode` à `null` = pas de code de sous-domaine (maths ; le `subLabel` groupe quand même le tiroir). Un `id` absent est rejeté en fin de liste. **Pour changer l'ordre ou le sous-domaine : éditer `CHAP_GROUPS`**. ⚠️ `matiereLabel` (tag) et `domain` (couleurs via `data-domain`) ne sont **pas** réécrits : les tenir à la main en cohérence (ex. `lorentz` porte encore le tag « Mécanique » dans le groupe Électromagnétisme). Tags ajoutés avec la PT spé : « Électronique » (ali, oscelec, signum, groupe Ondes & signaux), « Résistance des matériaux » et « Conception » (SI Mécanique), « Intelligence artificielle » (ia) ; le chapitre SI `ia` a `domain:'info'` (pas de couleur `--dom-*` dédiée : couleurs par défaut). Le code `'meca'` sert en physique ET en SI.

**2ᵉ année** : dans la même IIFE, `window.__YEAR2A = new Set([...])` (52 ids : maths 28, physique 13, SI 11 ; les 26 chapitres de PT spé ajoutés le 2026-10-04 sont listés en fin de `CHAPTERS`, de `__YEAR2A` et des decks, sous un commentaire « PT spé (2ᵉ année) ») pilote le badge « 2ᵉ année » du bandeau (« 2A » dans le tag des `.chap-btn`), le `data-year` des `.chap-btn`, le filtre 1ʳᵉ/2ᵉ année du tiroir (clé `year`) et le surtitre de la page de garde imprimée (`printChapter` : « PT · 2ᵉ année », sans la pastille « 2A » dans la matière). Règle en dur (`buildChapData`, `syncSidebar`) : **anglais** et `constantes` sont visibles les deux années. Juste après `__YEAR2A`, la même règle est exposée : `window.__chapYear(c)` (0 = les deux années, sinon 1 ou 2), `window.__currentYear()` (clé `year`, 1 par défaut) et `window.__inYear(c, y)`. Elles filtrent par année **préc./suiv.** (`goRelChapter`/`updateNavButtons`, touches n/p, Alt+←/→ : année du chapitre actif, ou année courante pour anglais/constantes). Le **Bilan** et le **quiz** (`buildDeck`) passent par `window.__inRevision(c, y)` : en 1ʳᵉ année, 1ʳᵉ année seulement ; en 2ᵉ année, **les deux années** (les concours portent sur tout le programme). Les « Révisions du jour » (`dueDeck`) restent toutes années.

### Navigation : barres invisibles = couche de commande

Les `.mat-content` du HTML ne contiennent que des conteneurs vides `.subdomain-bar` / `.chapter-bar` (en maths, la div **est** `.chapter-bar mat-content` ; la zone SI précède `main#si-content`). `buildSidebars` les remplit de `.sub-btn` / `.chap-btn` depuis `CHAPTERS` (tag = `matiereLabel`, libellé = `mobLabel`), **avant** l'attachement des handlers. Ces barres sont **invisibles à toutes les largeurs** (`display:none !important`) : `.chap-btn`/`.tab` forment une **couche de commande cachée**, cliquée par `navigateTo`, le tiroir, le routage et préc./suiv. La seule navigation visible est le **tiroir `#mob-drawer`**, sur mobile (☰) comme sur desktop (« Chapitres » `#nav-toggle-btn`). **Seul le handler `.chap-btn`** (`grep -n 'CHAPTER SWITCHING'`) bascule entre le `<main>` principal et `#si-content`.

→ Naviguer **toujours** via `navigateTo('chap-<id>','<prefix>-<onglet>', cb)` ou un clic sur `.chap-btn`/`.tab`, jamais en posant `.active` à la main. Ne pas supprimer ces barres, et **ne pas ajouter de `.chap-btn` dans le HTML** (effacés par `buildSidebars`).

**Ajouter un chapitre = 5 endroits** (gabarit : `GABARIT-CHAPITRE.md`) : (1) entrée `CHAPTERS` ; (2) id dans `CHAP_GROUPS` ; (3) id dans `__YEAR2A` si 2ᵉ année ; (4) bloc DOM `chap-<id>` dans le bon `<main>` ; (5) `const <prefix>Cards` + `makeFlash(...)` **après** les constantes `FLASH_*` (`grep -n 'const FLASH_FR2'` ; avant, TDZ → plantage).

### Routage par URL (deep-link + bouton précédent)

L'IIFE `urlRouting` synchronise `location.hash` (`#chapId/onglet`, ex. `#rlc/cours`) avec le chapitre/onglet actif, par **délégation** (clics sur `.chap-btn`/`.tab`/`.sub-btn`/`.mob-chap-item`/boutons matière, puis `syncHash`). `pushState` au changement de chapitre (le bouton « précédent » revient au chapitre précédent), `replaceState` au simple changement d'onglet. Au chargement (restauration à +120 ms), un `#hash` a priorité sur `lastPos` (`window.__navFromHash`). `popstate` rejoue la navigation.

## Conventions de nommage des IDs (IMPORTANT)

- Le `<div>` du chapitre : `id="chap-<id>"` (ex. `chap-rlc`).
- **`id` ≠ `prefix`** pour **141 chapitres sur 160** : le `prefix` sert aux panels et aux flashcards.
  Ex. chapitre `id:'ondes'` → panels `ond-` ; `id:'rlc'` → panels `rlc-`. **Construire un id de panneau avec `CHAPTERS_BY_ID[id].prefix`**, jamais `id+'-cours'`.
- Panels : `<section class="panel" id="<prefix>-<panel>">` avec `<panel>` ∈ `cours` | `meth` | `simu` | `flash` | `exos`.
- Onglets : `<button class="tab" data-panel="<prefix>-<panel>">`.
- Bouton de commande (généré, invisible) : `<button class="chap-btn" data-chap="<id>">`.

## Structure d'un chapitre (DOM)

```html
<div class="chapter" id="chap-<id>">
  <nav class="tabs">
    <button class="tab active" data-panel="<prefix>-cours"><span class="num">01</span>Cours</button>
    <button class="tab" data-panel="<prefix>-meth">…Méthodes</button>
    <!-- simu seulement si drawFn défini -->
    <button class="tab" data-panel="<prefix>-flash">…Flashcards</button>
    <button class="tab" data-panel="<prefix>-exos">…Exercices</button>
  </nav>
  <section class="panel active" id="<prefix>-cours"> … </section>
  <section class="panel" id="<prefix>-meth"> … </section>
  …
</div>
```

Classes de contenu : `.course-section`, `.sec-num` (ex. « §1 · LES BASES »), `.intro`, `.formula` (formules MathJax `$$…$$`), `.def-box`, `.prop-box`, `.method-box`, `.notice`, `.reveal` (bloc dépliable au clic). Exercices : `.exo` **dans** `.exo-wrapper` (exo « CONCOURS PT » compris, sans `</div>` en plus). Bandeau `.chap-title-banner.mat-<matiere>` injecté par `injectChapterTitleBanners`.

**Deux `.chapter.active` dans le HTML source** : `chap-rlc` et `chap-ingsys` (un par `<main>`), jusqu'au 1ᵉʳ clic `.chap-btn` (restauration à +120 ms s'il y a un `#hash` ou un `lastPos` ; sinon, à la 1ʳᵉ visite, jusqu'à la 1ʳᵉ navigation). Pour le chapitre **visible**, filtrer par `offsetParent` (cf. `function activeChapter` du formulaire).

## Formules : deux conventions distinctes

- **Cours / méthodes** : LaTeX via MathJax. Inline `\( … \)`, bloc `$$ … $$` (**pas** `\[ … \]`). Pas de « < » collé à une lettre dans une formule (lu comme une balise : `\lt`, contrôlé par `validate.py`). Pas de macro d'extension absente (`\cancel`, `\ce`, `physics`…). Éviter les longues formules en ligne (débordement mobile) : `$$` dans `.formula`.
- **Flashcards** : **par défaut** en **caractères Unicode** (ex. `ω₀`, `√(LC)`, `e^(iθ)`, `ω_k`, `≤`, `∫`, `z̄`, `ü`). À l'affichage, `makeFlash` applique `flashPretty()` qui **repère les fragments mathématiques, les convertit en LaTeX (`flashConvertMath()` : `^(…)`, `_(…)`, `√(…)`, `{…}`, `cos`, `z̄`, `ü`, `²`/`ₙ`…) et les enrobe dans `\( … \)`** ; MathJax (appelé dans `show()`) les rend **dans la police du cours**. Le texte français reste hors maths. Une carte écrite directement en `\( … \)` est **admise** et laissée intacte (536 cartes : decks cst, cine, stat, slci, et 459 cartes des 26 decks de PT spé) ; dès qu'un champ contient `\(`, `flashPretty` le laisse **entier** à MathJax : y écrire alors toutes les formules en `\( … \)` — dans la chaîne JS, doubler l'antislash (`\\(`). ⚠️ Séparation maths/texte **heuristique** : une carte mêlant phrase et formule peut demander une réécriture directe en `\( … \)`.

## Flashcards

```js
const <prefix>Cards = [
  {q:"Question ?", a:"Réponse."},
  {q:"Loi d'Ohm ?", a:"U = R·I", cat:'form'},   // cat facultatif
  …
];
const <prefix>Flash = makeFlash(<prefix>Cards, '<prefix>',
  '<prefix>-flash-content', '<prefix>-flash-prog', '<prefix>-stats');
```

- 160 decks, 3 749 cartes. `makeFlash` (`grep -n 'function makeFlash'`) gère flip 3D / notation (à revoir / hésitant / acquis) / progression / Leitner ; il range le deck dans `window.FLASH_REGISTRY[prefix]` et l'instance dans `window.FLASH_INSTANCES[prefix]` (`flip, rate, prev, next, resetProgress, getProgress, reload`).
- Champ facultatif **`cat:'form'|'val'`** (851 cartes) : filtre « Formules / Grandeurs usuelles » du quiz.
- **État et identifiants de cartes** (`grep -n 'ÉTAT DES FLASHCARDS'`) : `flash:<prefix>` reste un tableau d'états `{h,o,e,last,box,due}` **aligné par position** (Bilan, `srsCountDue`, quiz, badge le lisent par index) ; `flashids:<prefix>` mémorise l'identifiant de chaque position, `flashCardIds(cards)` = `'Q|R'` (empreintes FNV-1a de la question et de la réponse). `flashLoadState(prefix, cards)` **réaligne l'état par identifiant** ; `flashSaveState(prefix, cards, state)` écrit toujours les deux clés ensemble. **Migration au chargement** : chaque `makeFlash` réécrit l'état si l'ordre ou les identifiants ont changé (état « hérité » sans identifiants : conservé par position). `rate()`/`getProgress()` relisent le Store, et `quizRate` appelle `FLASH_INSTANCES[prefix].reload()` : quiz et onglet Flashcards ne s'écrasent plus.
- **Règle d'édition des decks** (règle exacte : en-tête de `flashLoadState`). **Sans perte** : ajouter/retirer/réordonner des cartes ; **toute retouche de texte** (question et/ou réponse, remplacement global compris) à longueur et ordre inchangés (repli par rang : jamais pire que l'ancien appariement par position), **sauf** pour une question présente en double dans le paquet (n'en retoucher qu'une copie par mise à jour) et une réponse passée d'une carte à une autre dont les questions sont aussi retouchées ; question reformulée, réponse inchangée, gardant son rang depuis sa voisine reconnue précédente **ou** suivante (même si cette voisine a été déplacée), ou entourée d'autant de cartes retirées que de cartes ajoutées. **Carte remise à zéro** : question retouchée hors de ces cas (réponse aussi changée alors que des cartes sont ajoutées/retirées entre ses voisines — sauf autant d'ajouts que de retraits, voir la contrepartie —, carte retouchée **et** déplacée, rang changé des deux côtés), ou ambiguïté (deux candidates de même réponse). **Contrepartie** : entre deux voisines reconnues, autant de cartes nouvelles/retouchées que de cartes disparues → celles dont la réponse ne désigne pas une seule entrée prennent l'entrée de même rang : une carte ajoutée (ou retouchée et déplacée) à la place d'une disparue hérite de son état, et une carte à question **et** réponse retouchées côtoyant un retrait + un ajout peut recevoir l'état de la carte retirée (et la carte ajoutée, le sien). Prévenir l'utilisateur. `flagged` : réaligné par question **et** réponse, puis question seule ; question introuvable : garde son index, orpheline (`i:-1`, listée mais ne marque aucune carte) si cet index est pris par un autre signalement.

## Stockage

Objet `Store` (`grep -n 'const Store = (function'`) : wrapper `localStorage` avec **fallback en mémoire** (`memBackend`) ; si une écriture échoue en cours de session (quota), la valeur part en mémoire et `get` la relit en priorité. API : `get/set`, `getJSON/setJSON`, `available()` (pas de `remove`). Utiliser `Store`, jamais `localStorage` directement — seule exception : la Sauvegarde.

Clés : `flash:<prefix>` (progression par chapitre), `flashids:<prefix>` (identifiants de cartes), `theme`, `lastPos` (dernier chapitre/panneau vu), `year` (1 ou 2, tiroir), `recents` (8 derniers chapitres, MRU, par `syncSidebar`), `pinned` (épinglés ★, 8 au plus), `drawerCollapsed` (sous-domaines repliés, clé `mat|subLabel`), `todayAtLaunch` (`'0'` = pas d'écran « Aujourd'hui » au lancement), `flagged` (cartes signalées `{p,i,q,a,t}`), `quizConfig` (dernier réglage du quiz `{mats,mode,nb,type}`), `readScale` (taille du texte A−/A+, index 0-2 → `--read-scale`). Toute nouvelle clé est exportée par la Sauvegarde : l'ajouter ici, et **ne pas la faire commencer par `flash:`** (préfixe qui compte les chapitres avec progression ; d'où le nom `flashids:`).

**Tiroir « nouvelle génération »** : `#mob-filter` (filtre instantané TOUTES matières, accents ignorés, Entrée = 1ᵉʳ résultat, année ignorée volontairement) ; sections ★ Épinglés / ⌚ Récents en tête (hors filtre) ; sous-domaines repliables (`.mob-sub-toggle`) ; rangée `.mob-chap-row` = bouton chapitre + bouton épingle (frères, pas imbriqués). Module : `buildDrawerList`/`makeChapRow`/`CHAP_ITEM_BY_ID`. L'**anneau SVG de % acquis** (`ringSVG` → `window.__ringSVG`) n'est PAS dans le tiroir (retiré à la demande) : il est rendu dans les lignes par chapitre du **Bilan**.

**Écran « Aujourd'hui »** (`#today-overlay`, module en fin de body) : affiché au lancement (+250 ms) sauf deep-link `#hash` ou préférence désactivée ; cartes dues (`srsCountDue` → `quizStartDue`), « Reprendre » (`lastPos`), 3 récents, accès rapides ; rouvrable par « Aujourd'hui » (menu **Plus** `#today-btn`, menu ⋯ mobile `#mob-today-btn`) ou `window.todayOpen()`. Inclus dans la liste `IDS` du module focus (`grep -n 'var IDS = \['`).

**Sommaire** : le `.toc` (construit en JS, scroll-spy IntersectionObserver ; le rappel retrouve les items par la `Map` `tocItemsById`, construite une fois — un `querySelectorAll` sur tout le document par section coûtait ≈ 3 s au chargement à 160 chapitres) n'est affiché qu'en **desktop ≥ 1100 px** (sidebar sticky). En mobile il est masqué (`display:none !important`) — une version « chips horizontales » a été essayée puis **retirée à la demande de l'utilisateur** (jugée envahissante) : ne pas la réintroduire sans accord.

**Répétition espacée (Leitner)** : `box` = boîte, `due` = timestamp de prochaine révision. `srsSchedule(state, level)` (global, avant `makeFlash`) les met à jour à chaque notation (`SRS_INTERVALS` = [0,1,3,7,16,35,75] jours), dans `makeFlash.rate` **et** `quizRate`. `srsIsDue(s)`/`srsCountDue()` comptent les cartes dues. **Boutons** : desktop, `#study-btn` « Réviser » ouvre un menu (`#quiz-btn` Quiz, `#drill-btn` Calcul mental, `#revise-btn` Révisions du jour) ; mobile, `#mob-revise-btn` lance directement. `#revise-btn`/`#mob-revise-btn` → `window.quizStartDue()` : quiz limité aux cartes dues de **toutes** les matières (`dueDeck()`). 3 badges (`#rev-badge`, `#rev-badge-study`, `#rev-badge-mob`) : `window.__updateReviseBadge`.

**Tableau de bord** : « Bilan » (`#dash-btn`, `#mob-dash-btn`) → `#dash-overlay`, qui agrège `flash:*` (`FLASH_REGISTRY` pour le total + `Store.getJSON('flash:'+prefix)`) : % acquis global/par matière (`perMat` : physique, maths, SI seulement)/par chapitre, tri par priorité, clic → `navigateTo` vers les flashcards. `computeStats(year, seule)` suit `__inRevision` : en 1ʳᵉ année, 1ʳᵉ année seulement (+ anglais/constantes), avec une ligne de rappel pour la 2ᵉ année si elle a des cartes notées ; en 2ᵉ année, les deux années, avec une ligne « dont 2ᵉ année ». Le quiz (`buildDeck`, info « · 1ʳᵉ année » ou « · 1ʳᵉ + 2ᵉ année ») suit la même règle.

**Sauvegarde / restauration** : « Sauvegarde » dans le menu **Plus** (`#backup-btn`, mobile `#mob-backup-btn`) → `#backup-overlay`. Export = toutes les clés du `localStorage` (origine `thomasmareel.github.io` partagée) dans un JSON `{app,version,exportedAt,data}`. Import = vérifie `obj.data` (pas `obj.app`), réécrit les clés en **fusion**, traite `flash:X`/`flashids:X` par paire (ancienne sauvegarde sans `flashids:` → relue par position), puis recharge.

## Dépendances : tout en local (aucun CDN)

Le site est **100 % autonome** — aucune requête externe, fonctionne hors-ligne (vérifié par les suites `site` et `pwa`).

- **MathJax 3.2.2** : `vendor/mathjax/tex-mml-chtml.js` (composant combiné, sans extensions) + polices CHTML dans `vendor/mathjax/output/chtml/fonts/woff-v2/`. Référencé dans l'en-tête ET dans le template d'impression. Ne pas spécifier de `fontPath` (le chemin par défaut, relatif au script, trouve les polices).
- **Typeset paresseux par panneau** : on ne typesette que le **panneau visible** (démarrage, changement de chapitre via `chap-btn`/`sub-btn`) ; les autres à l'ouverture de leur onglet. Helper `typesetPanel(panel)` (idempotent : rien si le panneau contient déjà des `mjx-container` ou si son rendu est lancé — `WeakSet` `window.__typesetLances`, partagé avec `typesetActive` de la config MathJax). Tout panneau à formules doit être atteint par un onglet, sinon appeler `typesetPanel`. ⚠️ Pas d'attribut `data-mjx…` sur un conteneur : MathJax ignore les éléments qui en portent un (panneau jamais rendu).
- **Re-rendu sans doublon** (dans `startup.ready()`) : le site n'a aucun MathML source, mais l'entrée MathML de `tex-mml-chtml` retrouvait le `<math>` d'accessibilité (`mjx-assistive-mml`) de chaque formule déjà rendue : tout second `typesetPromise` d'un même bloc (lien profond, « Voir la solution », Formulaire) imbriquait un `mjx-container` par formule. `findMath` de l'entrée MathML ignore donc les `<math>` situés dans un `mjx-container` (même filtre dans la config MathJax du template d'impression, qui re-rend les formules recopiées). Ne pas retirer.
- **Correctif `\text{…}` de largeur nulle** (dans `startup.ready()` de la config MathJax, `grep -n 'largeur nulle'`) : avec `mtextInheritFont`, MathJax mesure chaque `\text{…}` dans la page, à l'endroit de la formule, et garde la largeur en cache par texte ; mesuré dans un bloc masqué (solution repliée…), il valait 0 px (texte qui chevauche la suite une fois la solution dépliée, et 0 réutilisé ensuite pour le même texte dans tous les chapitres). `measureTextNode` est enveloppé : une mesure nulle d'un texte non vide est refaite hors écran (hôte en `white-space:pre`), dans la police de la formule — **espaces compris** : `\ ` donne un mtext U+00A0 que `/\S/` ne reconnaît pas ; seul le texte vide est laissé à 0 (sinon un espace mesuré replié restait à 0 px pour toute la session, « R = 20Ω »). Ne pas retirer.
- **Polices** : Fraunces, Inter Tight, JetBrains Mono dans `vendor/fonts/` (woff2 latin + latin-ext ; 22 fichiers, 8 binaires distincts), déclarées dans `vendor/fonts/fonts.css` (`<link rel="stylesheet" href="vendor/fonts/fonts.css">`).
- **Template d'impression** (`printChapter()`) : document écrit dans un iframe caché `#print-iframe` (`about:blank`), d'où une balise `<base href="${location.href}">` injectée pour résoudre les chemins `vendor/...`.
- Mettre à jour MathJax : `npm pack mathjax@3`, recopier `es5/tex-mml-chtml.js` + `es5/output/chtml/fonts/woff-v2/`. Polices : refetch du CSS Google avec un User-Agent Chrome, subsets latin/latin-ext.

## PWA (installable + hors-ligne sur mobile)

- `manifest.webmanifest` (nom, icônes `icons/`, `display:standalone`, `theme_color`) + `sw.js`. Enregistré en fin de `<body>` (`grep -n 'serviceWorker.register'`), **uniquement en http/https** (pas en `file://`, où le hors-ligne reste assuré par les assets embarqués).
- `sw.js` précache la coquille (`PRECACHE`, 53 entrées). **HTML en stale-while-revalidate** : le SW sert le `index.html` en cache, récupère le réseau en arrière-plan et **réécrit `'index.html'` dans le cache courant** → nouvelle page au lancement **suivant**, même sans bump, mais sans bannière. **Assets en cache-d'abord** : jamais rafraîchis sans bump.
- **Mise à jour** : pas de `skipWaiting()` automatique ; après un bump de `CACHE_VERSION`, le nouveau SW attend et une **bannière « Nouvelle version disponible — Recharger »** (dans `index.html`) propose la MAJ (clic → `postMessage(SKIP_WAITING)` → activation : purge de tous les autres caches de l'origine + `clients.claim()` → `controllerchange` → reload). Re-vérification au retour sur l'app (`visibilitychange`, au plus 1×/min).
- ⚠️ **Bump OBLIGATOIRE** : à chaque commit modifiant un asset mis en cache (index.html inclus), **incrémenter `CACHE_VERSION`** en tête de `sw.js` (`ptsi-cache-vN` → `vN+1`) **dans le même commit** : bannière, rafraîchissement des assets, purge des anciens caches, cohérence HTML/assets.
- Ajout/retrait d'un fichier de `vendor/` ou `icons/` → mettre à jour `PRECACHE` (la suite `pwa` vérifie que chaque fichier listé existe).
- **Anomalie connue** : **rechargement automatique à la 1ʳᵉ visite** (`clients.claim()` déclenche `controllerchange`, qui recharge sans vérifier qu'un SW contrôlait déjà la page). D'où, dans les tests, `serviceWorkers:'block'`.

## Déploiement (GitHub Pages)

- Servi par **GitHub Pages** depuis `main`. URL : `https://thomasmareel.github.io/revisions-ptsi/`.
- **Déploiement par GitHub Actions** : workflow « Déploiement GitHub Pages (statique) » (`.github/workflows/deploy-pages.yml`, à chaque push sur `main`), qui publie le dépôt tel quel (`tests/`, `docs/` compris, sans effet sur le site). Chaque push doit donner un run `completed success`.
  - **Dans le cloud (Claude Code web)** : pas de `gh` ; outils GitHub MCP (`actions_list`, owner `thomasMareel`, repo `revisions-ptsi`, workflow id `283713397`).
  - **Sur le poste Windows de l'utilisateur** : `gh run list --repo thomasMareel/revisions-ptsi --limit 5` (`C:\Program Files\GitHub CLI\gh.exe`).
  - ⚠️ **Ne PAS se fier à `pages/builds/latest` ni à `pages-build-deployment`** (id 282516546) : ancienne pipeline Jekyll figée sur un build `errored` de mai 2026 (commit `47fa649`). Le vrai état = les **runs Actions**.
- ⚠️ **`.nojekyll` à la racine : le garder, ne jamais le supprimer.** Avec la source Actions, Jekyll ne tourne plus ; mais si Pages repassait en « Deploy from a branch », son parseur **Liquid** buterait sur le LaTeX (`{{…}}`), les `${…}` et la taille de `index.html` → build en échec, site **figé au dernier build réussi**. C'est le filet de sécurité.

## Outils

- `tools/validate.py` (stdlib) : 5 contrôles — ids `CHAPTERS` ↔ `div.chapter`, IDs HTML dupliqués, `makeFlash` pour chaque chapitre listant `flash`, `drawFn` existants, « < » collé à une lettre dans une formule. `python3 tools/validate.py` (ou `npm run valider`) → `[OK]` ou erreurs + exit ≠ 0 (l'info « MathJax-script ×2 » est bénigne). **Angles morts** : équilibre des balises, couverture de `CHAP_GROUPS`/`__YEAR2A`, export `window.drawX`, ids des simulateurs (panels ↔ onglets ↔ sections : couvert par la suite `site`).
- `tools/check_js.py` : `node --check` sur chaque bloc `<script>` inline (depuis la racine du dépôt) → `blocs en erreur: 0`.
- `tools/tag_formulas.py` et `tools/migrate_canvas_colors.py` : migrations déjà appliquées **qui réécrivent `index.html` en place**. **Ne pas les lancer sans raison ni accord** (`tag_formulas` étiquetterait des cartes d'anglais en `cat:'form'`).
- `tools/pre-commit` + `tools/install-hooks.sh` : hook git lançant `validate.py` avant chaque commit. **Non installé par défaut** : le proposer (`sh tools/install-hooks.sh`), pas d'office. Limites : il cherche `python` puis `py` (pas `python3`) et laisse passer si Python est introuvable. Contournement : `git commit --no-verify`.

## Tests navigateur (`tests/`)

Batterie Playwright + Chromium : sert le site sur un petit serveur local et le parcourt comme un utilisateur, sans jamais modifier `index.html`. Mode d'emploi (installation Windows/Linux, options, rapport, ajout d'un test) : **`tests/README.md`**.

- `npm test` = toute la batterie (≈ 18 min) ; `npm run test:rapide` = une dizaine de chapitres (5 matières) + tous les simulateurs en clair (≈ 4 min 30 s). Options de `node tests/run.js` : `--suite=site,mobile,interactions,pwa,regressions`, `--chapitres=rlc,slci`, `--racine=`, `--sortie=`, `--visible`, `--aide`. Sortie 0 = OK, 1 = échec, 2 = non démarré, 130 = interrompu par Ctrl+C (aucun rapport écrit). Captures + `rapport.json` dans `tests/sortie/` (ignoré).
- Suites : **site** (0 erreur JS, 0 requête externe, `CHAPTERS` ↔ DOM avec onglets/panneaux, chapitres × onglets avec MathJax, flashcards, simulateurs en clair et sombre) ; **mobile** (390 px) ; **interactions** (routage, navigation, recherche, flashcards + SRS, quiz, Bilan, Aujourd'hui, formulaire, impression, thème, export/import…) ; **pwa** ; **regressions** (un test par correctif B1 à B4 ; chaque règle d'appariement B2 et chaque volet des correctifs B1/B3 sont couverts, preuve par mutation : audit §6).
- **Quand les lancer** : **avant chaque commit touchant `index.html`**, en plus de `validate.py` et `check_js.py` — au minimum `npm run test:rapide` + la suite concernée ; la batterie complète avant un commit important. `regressions` doit rester verte.
- **Anomalies tolérées** : `DEBORDEMENTS_CONNUS` (`tests/suites/mobile.js`), `TEX_EN_CLAIR_CONNUS` et `ONGLETS_HORS_CHAPTERS_CONNUS` (`tests/suites/site.js`), avertissement de rechargement de 1ʳᵉ visite (`pwa`). Une anomalie corrigée doit être retirée de sa liste (un avertissement `!` le rappelle).
- **Conteneur Claude Code** : Playwright 1.56.1 global, Chromium dans `/opt/pw-browsers` ; **ne pas lancer `npm install` ni `npx playwright install`**. L'outil Bash coupe à 10 min : batterie complète en arrière-plan, sortie dans un fichier. Si les polices Latin Modern sont installées dans le conteneur (`fonts-lmodern`, `/usr/share/texmf/fonts`), `rlc-cours` mesure 439 px au lieu de 415 et la suite `mobile` échoue (même résultat sur l'`index.html` d'avant la PT spé) : lancer alors les tests avec un `FONTCONFIG_FILE` qui les exclut (`<selectfont><rejectfont><glob>/usr/share/texmf/fonts/*</glob></rejectfont></selectfont>`).
- **Écrire un test** : service workers bloqués par défaut ; `CHAPTERS` et `CHAPTERS_BY_ID/PREFIX` sont des `const` globales **lexicales** (`CHAPTERS.length` ; `window.CHAPTERS` vaut `undefined`), `Store`, `navigateTo`, `getCanvasColors`, `flashPretty` s'appellent aussi par leur nom ; `applyTheme` inaccessible (cliquer `#theme-btn`) ; naviguer par `location.hash = '#<id>/<onglet>'` puis attendre ≥ 300 ms.

## Identité visuelle (Lot 3)

- **Icônes SVG maison** : sprite de **18** `<symbol id="i-…">` (menu, search, refresh, theme, dots, calendar, bolt, calc, chart, function, download, printer, flag, volume, book, keyboard, check, inbox) + 4 `<marker>` `sk-arrow-*` des schémas, en tête de `<body>`, trait `currentColor` (classe `.ic`). **`window.__icon(name)`** (petit script juste après le sprite, donc AVANT les decks, car `makeFlash` l'utilise) renvoie `<svg class="ic"><use href="#i-name"></use></svg>`. Tout le **chrome** utilise ces icônes ; les boutons à libellé variable gardent l'icône et mettent à jour un `<span class="ic-lbl">`. Volontairement **non migrés** : les 160 boutons « ↺ Réinitialiser » et les boutons secondaires d'overlays (Copier/Télécharger).
- **En-tête desktop** : `.header-nav` (« Chapitres ») + `.header-actions` (Rechercher, menu Réviser, Bilan, Thème, menu **Plus** `#more-menu` : Aujourd'hui, Sauvegarde, Raccourcis, Formulaire, Imprimer, Cartes signalées, taille du texte). **Mobile** : `#mob-header` (☰, recherche, Réviser, thème, menu ⋯ sans Imprimer ni Raccourcis).
- **Flip 3D des flashcards** : demi-tour mono-face dans `makeFlash.flip` (rotateY 0→90°, échange de face, retour), `perspective` sur `.flash-wrapper`, garde `window.__reduceMotion`.
- **Rails de couleur par matière** : `border-left` sur `.chap-title-banner.mat-<matiere>`.
- **Points de retour** sur origin : branches `sauvegarde-avant-lot3` (`9e16255`) et `sauvegarde-avant-finitions2` (`b1d2a25`), tag `v1.0`. Rollback (uniquement sur demande explicite) : `git reset --hard <branche> && git push --force origin main`.

## Anomalies connues (à traiter avec validation utilisateur)

Liste complète par gravité, avec ancres et pistes : **`docs/audit-2026-09.md`**. Corrigés le 2026-09-26 (suite `regressions`) : B1 quiz → flashcards, B2 état indexé par position, B3 formule SLCI apériodique, B4 `getCanvasColors` en sombre. Principales restantes :

1. **SLCI, Bode 1ᵉʳ ordre** (`function drawSlciB1`) : asymptote HF à −40 dB/déc, l'info affiche −20.
2. **`.notice` illisible en sombre** (texte `#7a5a0e`, ≈ 2:1, 332 encadrés dont 161 dans les chapitres de PT spé ; un override `:root[data-theme="dark"] .notice` les corrigerait tous). Le bouton « Voir la solution » (`.toggle-sol`, autrefois noir sur fond sombre) a reçu `color:var(--ink)`.
3. **Simulateur de Lorentz** (`function lorDraw`) : faux dans 3 modes sur 4, absent de `CHAPTERS.panels`.
4. **Clavier** : raccourcis des flashcards sur 18 decks/160, sans garde de saisie ; raccourcis globaux actifs derrière le quiz.
5. **Quiz** : mode « Ciblé » incluant les cartes jamais vues ; `quizGotoChapter` (carte précédente, `id` au lieu du `prefix`).
6. **Rechargement automatique à la 1ʳᵉ visite** (voir PWA).
7. **Débordement horizontal à 390 px** sur 13 panneaux, dont `rlc-cours` (chapitre par défaut). Angle mort de la suite `mobile` (mesure à l'état replié) : solutions dépliées débordant aussi dans `rlc-exos`, `mth-exos` (machines), `mcc-exos`, `slci-exos`, `reduction-exos` (aucun des 26 chapitres de PT spé).
8. **73 exos « CONCOURS PT » hors `.exo-wrapper`** (63 chapitres, `</div>` orphelin).
9. **`--border` / `--surface` n'existent pas** (97 usages).
10. **Simulateur Suites** (`steps` fractionnaire).

Corrigé le 2026-10-05 (signalé par l'utilisateur) : tout changement de chapitre — tiroir, préc./suiv., `navigateTo`, retour du navigateur — remonte en haut de page via `scrollPageTop()` (handler `.chap-btn`, et `navigateTo` sans rappel) ; un changement d'onglet garde le défilement ; une navigation avec rappel (recherche, Bilan…) défile ensuite vers sa cible.

Non-bug : les deux `.chapter.active` du HTML source (`chap-rlc`, `chap-ingsys`), un par `<main>`.

## Variables CSS de thème (`:root`)

`--ink`, `--paper`, `--paper-dark`, `--accent` (#c8472e), `--accent-deep`, `--accent2` (#2d5f8a), `--green`, `--amber`, `--grid`, `--muted`, `--shadow`, `--shadow-1/2`, `--radius-s/m/l`, `--anglais`, `--read-scale`, `--dom-*` (couleurs par domaine, via `data-domain` posé en JS sur chaque `.chapter`). ⚠️ **`--border` et `--surface` n'existent pas** (utilisées 97 fois) : ne pas les employer (`--grid`, `--muted`, `--paper-dark`). Thème sombre : `:root[data-theme="dark"]` avec overrides ciblés. `applyTheme()` (`grep -n 'function applyTheme'`) est **locale** à une IIFE : c'est le handler de `#theme-btn` (relayé par `#mob-theme-btn`) qui applique le thème, le mémorise (`theme`) et redessine le chapitre actif. Le thème n'est posé qu'à cet endroit du grand script (flash clair au chargement, connu).

**Couleurs dans les simulateurs/schémas** : toujours les variables de thème (ou `getCanvasColors()` côté canvas), **jamais une couleur codée en dur** — sinon le contraste casse en sombre. Sur fond accent, `var(--paper)` plutôt que `#fff`. `getCanvasColors()` détecte le sombre par `data-theme="dark"` sur `<html>` (correctif B4). Côté canvas, préférer **`__CV()`** (cache de `getCanvasColors()` invalidé par un MutationObserver au changement de thème — sûr dans les boucles rAF) et **`__CVA('accent', 0.4)`** pour une couleur avec alpha (au lieu d'un `rgba(...)` en dur). Le dessin a été migré (reste : quelques rgba de la palette claire, les hex de Lorentz). Les encadrés communs (`.sim-controls`, `.sim-info`, `.regime-badge` et `.pseudo/.critique/.aperiodique`) ont un bloc d'overrides sombre **unique** (« Contraste des encadrés de simulateur en thème sombre » dans le `<style>`), valable pour tous les simulateurs : toute nouvelle variante de badge y reçoit une couleur issue des variables. Nouveau simulateur : voir `GABARIT-CHAPITRE.md`.
