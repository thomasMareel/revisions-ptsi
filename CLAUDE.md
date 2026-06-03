# CLAUDE.md — Conventions du projet « Révisions PTSI »

Notes destinées à Claude pour les sessions futures. Objectif du projet : rendre maintenable un fichier de révisions PTSI et l'héberger sur GitHub Pages, **sans casser l'existant**.

## Règles de collaboration

- **Tout en français** (réponses, commentaires, contenu).
- **Ne rien casser** de ce qui marche (design + fonctionnalités). Pas de refonte non demandée.
- **Demander confirmation avant toute modification du HTML.**
- L'utilisateur est étudiant en prépa, débutant en dev. Privilégier des explications claires et des changements incrémentaux.

## Architecture

- **Un seul fichier servi : `index.html`** (~33 000 lignes, 2,1 Mo). HTML + CSS + JS tout inline.
- `cours_ptsi-42.html` à la racine = **backup** d'origine (le temps du travail).
- `fichier de départ/` = original intact, **non versionné** (voir `.gitignore`).
- Aucun build. Édition directe du fichier.

### Pilotage data-driven

Le tableau **`CHAPTERS`** (JS, vers la ligne ~24985) est la source de vérité : navigation, redraw des simulateurs, recherche en dérivent. Chaque entrée :

```js
{ id:'rlc', prefix:'rlc', name:'Circuit RLC série',
  matiere:'physique', sub:'ondes', subLabel:'Ondes & signaux', domain:'ondes',
  matiereLabel:'Électrocinétique',
  panels:['cours','meth','simu','flash','exos'], drawFn:'drawSim',
  mobLabel:'Circuit RLC série' }
```

- `matiere` ∈ `physique` | `maths` | `si` | `info` | `anglais`. **Ajouter une matière** = l'ajouter aux énumérations en dur : boutons `mob-mat-btn` (HTML), `.mat-content[data-mat-content="X"]` (zone sidebar), `buildSidebars` (`['physique',…]`), `buildChapData`/`MATS` du tiroir, `matLabel` (recherche). Les chapitres `physique/maths/info/anglais` vivent dans le grand `<main>` ; `si` a son propre `<main id="si-content">`.
- **Anglais** : matière de langue, donc cartes en **texte brut** (pas de maths). `makeFlash` détecte `CHAPTERS_BY_PREFIX[prefix].matiere === 'anglais'` (`isPlainDeck`) et rend `card.q`/`card.a` en HTML brut sans `flashPretty` (sinon « I », « / » seraient mathématisés) ; idem côté quiz (`item.meta.mat === 'anglais'`). Les réponses peuvent contenir `<strong>`/`<em>`/`<br>`. Panels typiques : `['cours','flash']` (pas d'exos).
- `drawFn` : nom de la fonction Canvas du simulateur, ou `null` si pas de simu.
- `CHAPTERS_BY_ID` / `CHAPTERS_BY_PREFIX` sont dérivés automatiquement.
- `validateChaptersCoherence()` (~l.25256) alerte dans la console si DOM ≠ `CHAPTERS` au chargement.

### Ordre d'apprentissage (réorganisation centralisée)

Juste après la définition de `CHAPTERS` (IIFE `reorderChapters`), le tableau **`CHAP_GROUPS`** = `[ [subCode, subLabel, [ids…]] , … ]` est la **source unique** de l'ordre des chapitres (ordre pédagogique conventionnel), des **sous-domaines** (`c.sub`) et de leurs **libellés** (`c.subLabel`). Il réordonne `CHAPTERS` en place et réécrit `c.sub`/`c.subLabel`. Un `subCode` à `null` = matière « à plat » (sans sous-domaines, ex. maths). Cela pilote **tout** : sidebars desktop (générées par l'IIFE `buildSidebars` à partir de `CHAPTERS` — plus de HTML de boutons à maintenir), tiroir mobile (`buildChapData`, groupé par `subLabel`), navigation précédent/suivant, tableau de bord. **Pour changer l'ordre, le sous-domaine ou le libellé d'un chapitre : éditer uniquement `CHAP_GROUPS`.** Un `id` absent est rejeté en fin de liste.

Les `.mat-content` du HTML ne contiennent plus que des conteneurs vides `<div class="subdomain-bar"></div><div class="chapter-bar"></div>` ; `buildSidebars` les remplit (tag `.matiere` = `matiereLabel`, libellé = `mobLabel`). Elle tourne **avant** l'attachement des handlers de clic.

### Routage par URL (deep-link + bouton précédent)

L'IIFE `urlRouting` synchronise `location.hash` (`#chapId/onglet`, ex. `#rlc/cours`) avec le chapitre/onglet actif, par **délégation** (écoute les clics sur `.chap-btn`/`.tab`/`.sub-btn`/`.mob-chap-item`/boutons matière, puis `syncHash`). `pushState` au changement de chapitre (le bouton « précédent » revient au chapitre précédent), `replaceState` au simple changement d'onglet. Au chargement, un `#hash` a priorité sur `lastPos` (`window.__navFromHash`). `popstate` rejoue la navigation.

## Conventions de nommage des IDs (IMPORTANT)

- Le `<div>` du chapitre : `id="chap-<id>"` (ex. `chap-rlc`).
- **`id` ≠ `prefix`** : le `prefix` sert aux panels et aux flashcards, et peut différer de l'`id`.
  Ex. chapitre `id:'ondes'` → panels préfixés `ond-` ; chapitre `id:'rlc'` → panels `rlc-`.
- Panels : `<section class="panel" id="<prefix>-<panel>">` avec `<panel>` ∈ `cours` | `meth` | `simu` | `flash` | `exos`.
- Onglets : `<button class="tab" data-panel="<prefix>-<panel>">`.
- Bouton de navigation : `<button class="chap-btn" data-chap="<id>">`.

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

Classes de contenu : `.course-section`, `.sec-num` (ex. « §1 · LES BASES »), `.intro`, `.formula` (formules MathJax `$$…$$`), `.def-box`, `.prop-box`, `.method-box`, `.notice`, `.reveal` (bloc dépliable au clic).

## Formules : deux conventions distinctes

- **Cours / méthodes** : LaTeX via MathJax. Inline `\( … \)`, bloc `$$ … $$`.
- **Flashcards** : contenu écrit en **caractères Unicode** (ex. `ω₀`, `√(LC)`, `e^(iθ)`, `ω_k`, `≤`, `∫`, `z̄`, `ü`). À l'affichage, `makeFlash` applique `flashPretty()` qui **repère les fragments mathématiques, les convertit en LaTeX et les enrobe dans `\( … \)`** ; MathJax (déjà appelé dans `show()`) les rend alors **dans la même police que le cours**. Le texte français reste hors maths. Le helper `flashConvertMath()` fait la conversion Unicode→LaTeX (exposants `^(…)`/`^x`, indices `_(…)`/`_x`, `√(…)`→`\sqrt{}`, accolades d'ensembles `{…}`→`\{…\}`, fonctions `cos`→`\cos`, accents `z̄`→`\bar{z}`, `u̇`→`\dot{u}`, `ü`→`\ddot{u}`, exposants/indices Unicode `²`/`ₙ`…). Une carte déjà écrite en LaTeX `\( … \)` est laissée intacte. ⚠️ La séparation maths/texte est **heuristique** : quelques cartes mêlant phrase et formule peuvent demander un affinage manuel (réécriture directe en `\( … \)` dans la carte).

## Flashcards

```js
const <prefix>Cards = [
  {q:"Question ?", a:"Réponse."},
  …
];
const <prefix>Flash = makeFlash(<prefix>Cards, '<prefix>',
  '<prefix>-flash-content', '<prefix>-flash-prog', '<prefix>-stats');
```

`makeFlash` (~l.25998) gère flip / notation (à revoir / hésitant / acquis) / progression, persistée via l'objet `Store`.

## Stockage

Objet `Store` (~l.24912) : wrapper `localStorage` avec **fallback en mémoire** si indisponible. API : `get/set`, `getJSON/setJSON`, `available()`. Utiliser `Store`, jamais `localStorage` directement.

Clés utilisées : `flash:<prefix>` (progression par chapitre), `theme` (clair/sombre), `lastPos` (dernier chapitre/panneau vu), `year` (1 ou 2 — sélecteur d'année du tiroir).

**Répétition espacée (Leitner)** : l'état d'une carte est `{h,o,e,last,box,due}` — `box` = boîte de Leitner, `due` = timestamp de prochaine révision. `srsSchedule(state, level)` (global, ~avant `makeFlash`) met à jour `box`/`due` à chaque notation (intervalles `SRS_INTERVALS` = [0,1,3,7,16,35,75] jours) ; appelé dans `makeFlash.rate` **et** `quizRate`. `srsIsDue(s)`/`srsCountDue()` comptent les cartes dues. Bouton **« ↻ Réviser »** (en-tête + mobile, badge = nb de cartes dues via `window.__updateReviseBadge`) → `window.quizStartDue()` lance une session quiz limitée aux cartes dues de **toutes** les matières (`dueDeck()` dans le module quiz).

**Tableau de bord** : bouton « Bilan » → overlay `#dash-overlay` qui agrège `flash:*` (via `FLASH_REGISTRY` pour le total de cartes + `Store.getJSON('flash:'+prefix)` pour les états) : % acquis global/par matière/par chapitre, tri par priorité, clic → `navigateTo` vers les flashcards du chapitre.

**Sauvegarde / restauration** : bouton « Sauvegarde » dans l'en-tête (et mobile) → fenêtre `#backup-overlay`. Export = télécharge toutes les clés du `localStorage` dans un JSON `{app,version,exportedAt,data}`. Import = relit le JSON (vérifie `obj.data`), réécrit les clés, recharge la page. Protège la progression et permet le transfert entre appareils.

## Dépendances : tout en local (aucun CDN)

Le site est **100 % autonome** — aucune requête externe, fonctionne hors-ligne.

- **MathJax 3.2.2** : `vendor/mathjax/tex-mml-chtml.js` + polices CHTML dans `vendor/mathjax/output/chtml/fonts/woff-v2/`. Référencé dans l'en-tête ET dans le template d'impression. Ne pas spécifier de `fontPath` dans la config MathJax : le chemin par défaut (relatif au script) trouve les polices.
- **Typeset paresseux par panneau** : pour accélérer le premier affichage, on ne typesette que le **panneau visible** (au démarrage, au changement de chapitre via `chap-btn`/`sub-btn`). Les autres panneaux sont rendus à l'ouverture de leur onglet. Helper `typesetPanel(panel)` (idempotent : ne fait rien si le panneau contient déjà des `mjx-container`). En ajoutant un panneau qui contient des formules, s'assurer qu'il est bien atteint par un onglet (sinon ajouter un appel à `typesetPanel`).
- **Polices** : Fraunces, Inter Tight, JetBrains Mono dans `vendor/fonts/` (woff2 latin + latin-ext), déclarées dans `vendor/fonts/fonts.css`. Référencé via `<link rel="stylesheet" href="vendor/fonts/fonts.css">`.
- **Template d'impression** (`printChapter()`) : le document généré est écrit dans un iframe (`about:blank`), donc une balise `<base href="${location.href}">` est injectée pour que les chemins relatifs `vendor/...` résolvent correctement.
- Pour mettre à jour MathJax : `npm pack mathjax@3`, extraire, recopier `es5/tex-mml-chtml.js` + `es5/output/chtml/fonts/woff-v2/`. Pour les polices : refetch du CSS Google avec un User-Agent Chrome, filtrer les subsets latin/latin-ext.

## PWA (installable + hors-ligne sur mobile)

- `manifest.webmanifest` (nom, icônes `icons/`, `display:standalone`, `theme_color`) + `sw.js` (service worker). Enregistré dans `index.html` en fin de `<body>`, **uniquement en http/https** (pas en `file://`).
- `sw.js` : précache toute la coquille (index.html, fonts.css, MathJax + toutes les polices, icônes) ; HTML en *cache-d'abord puis revalidation* (**stale-while-revalidate** : lancement instantané depuis le cache, mise à jour récupérée en arrière-plan), assets en *cache-d'abord*.
- **Mise à jour & notification** : le SV ne fait plus de `skipWaiting()` automatique ; à chaque bump de `CACHE_VERSION`, le nouveau SV reste « en attente » et une **bannière « Nouvelle version disponible — Recharger »** (code dans `index.html`) propose d'appliquer la MAJ (clic → `postMessage(SKIP_WAITING)` → activation → `controllerchange` → reload). Re-vérification au retour sur l'app (`visibilitychange`).
- ⚠️ **À chaque modification d'un asset mis en cache** (index.html inclus), **incrémenter `CACHE_VERSION`** en tête de `sw.js` (`ptsi-cache-v1` → `v2`…) : c'est ce bump qui déclenche la bannière de mise à jour chez les utilisateurs « installés ». Comme le HTML est désormais servi cache-d'abord, **sans bump l'utilisateur garde l'ancienne version** (le bump est donc obligatoire, plus seulement « propre »).
- Si on ajoute/retire des polices, mettre à jour la liste `PRECACHE` de `sw.js`.
- Le service worker ne s'active pas en ouverture locale `file://` (normal) ; le hors-ligne local reste assuré par les assets embarqués.

## Déploiement (GitHub Pages)

- Servi par **GitHub Pages** depuis `main` (dossier `/`). URL : `https://thomasmareel.github.io/revisions-ptsi/`.
- ⚠️ **`.nojekyll` à la racine est OBLIGATOIRE — ne jamais le supprimer.** Sans lui, GitHub lance **Jekyll**, dont le parseur **Liquid** bute sur le LaTeX (`{{…}}`), les gabarits JS `${…}` et la taille de `index.html` → le build **échoue** (« Page build failed ») et le site reste **figé au dernier build réussi** (les commits suivants ne se voient pas, alors que `git push` a réussi). `.nojekyll` fait servir les fichiers tels quels.
- **Le déploiement passe désormais par GitHub Actions** (workflow « Déploiement GitHub Pages (statique) »), pas par l'ancienne pipeline Jekyll. **Diagnostic** : `gh run list --repo thomasMareel/revisions-ptsi --limit 5` → chaque push doit afficher `completed success`. Le binaire `gh` est à `C:\Program Files\GitHub CLI\gh.exe`.
  - ⚠️ **Ne PAS se fier à `gh api …/pages/builds/latest`** : cette API reflète l'ancienne pipeline Jekyll (restée bloquée sur un build `errored` de mai 2026, commit `47fa649`, antérieur au passage à Actions). Elle affiche donc un vieux commit en `built` et induit en erreur — le vrai état de déploiement est celui des **runs Actions** ci-dessus.

## Outils

- `tools/validate.py` (Python stdlib, aucune dépendance) : vérifie cohérence `CHAPTERS` ↔ DOM, IDs HTML dupliqués, flashcards câblées (`makeFlash` par chapitre listant `flash`), `drawFn` existants. `python tools/validate.py` → `[OK]` / liste d'erreurs + exit ≠ 0. **À lancer avant chaque commit touchant `index.html`.**
- `tools/pre-commit` + `tools/install-hooks.sh` : hook git qui lance `validate.py` automatiquement avant chaque commit (bloque si erreur). Installer une fois avec `sh tools/install-hooks.sh`. Contourner ponctuellement avec `git commit --no-verify`. (Le dossier `.git/hooks/` n'est pas versionné, d'où l'installeur.)

## Anomalies connues (à traiter avec validation utilisateur)

1. ~~**ID dupliqué `int-meth`**~~ — **CORRIGÉ** : le `<select>` du simulateur des intégrales a été renommé `int-meth-sel` (le panneau garde `int-meth`). Avant, `getElementById('int-meth')` renvoyait la `<section>`, donc le choix de méthode d'intégration était ignoré.
2. **Commentaires de bannière obsolètes** : certains `<!-- CHAPITRE X -->` ne correspondent plus au chapitre qui suit (ex. l.~1893 « RLC » devant `chap-ondes`).
3. Deux chapitres ont `class="chapter active"` au chargement (`chap-rlc`, `chap-mcc`) — **non bug** : ils sont dans deux `<main>` séparés (physique vs SI), un seul affiché à la fois.

## Variables CSS de thème (`:root`)

`--ink`, `--paper`, `--paper-dark`, `--accent` (#c8472e), `--accent2` (#2d5f8a), `--green`, `--amber`, `--grid`, `--shadow`. Thème sombre : `:root[data-theme="dark"]` avec overrides ciblés. Bascule via `applyTheme()` (~l.31354).

**Couleurs dans les simulateurs/schémas** : toujours utiliser les variables de thème (ou `getCanvasColors()` côté canvas), **jamais une couleur codée en dur** — sinon le contraste casse en mode sombre. Les encadrés communs des simulateurs (`.sim-controls`, `.sim-info`, `.regime-badge` et ses variantes `.pseudo/.critique/.aperiodique`) ont un bloc d'overrides sombre **unique** (chercher « Contraste des encadrés de simulateur en thème sombre » dans le `<style>`) : il s'applique à tous les simulateurs existants et futurs. Toute nouvelle variante de badge doit y recevoir une couleur issue des variables.
