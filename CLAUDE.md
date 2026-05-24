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

- `matiere` ∈ `physique` | `maths` | `si`.
- `drawFn` : nom de la fonction Canvas du simulateur, ou `null` si pas de simu.
- `CHAPTERS_BY_ID` / `CHAPTERS_BY_PREFIX` sont dérivés automatiquement.
- `validateChaptersCoherence()` (~l.25256) alerte dans la console si DOM ≠ `CHAPTERS` au chargement.

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
- **Flashcards** : **caractères Unicode**, PAS de LaTeX (ex. `ω₀`, `√(LC)`, `½`, `→`, `²`). MathJax ne retypeset pas les cartes.

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

Clés utilisées : `flash:<prefix>` (progression par chapitre), `theme` (clair/sombre), `lastPos` (dernier chapitre/panneau vu).

**Sauvegarde / restauration** : bouton « Sauvegarde » dans l'en-tête (et mobile) → fenêtre `#backup-overlay`. Export = télécharge toutes les clés du `localStorage` dans un JSON `{app,version,exportedAt,data}`. Import = relit le JSON (vérifie `obj.data`), réécrit les clés, recharge la page. Protège la progression et permet le transfert entre appareils.

## Dépendances : tout en local (aucun CDN)

Le site est **100 % autonome** — aucune requête externe, fonctionne hors-ligne.

- **MathJax 3.2.2** : `vendor/mathjax/tex-mml-chtml.js` + polices CHTML dans `vendor/mathjax/output/chtml/fonts/woff-v2/`. Référencé dans l'en-tête ET dans le template d'impression. Ne pas spécifier de `fontPath` dans la config MathJax : le chemin par défaut (relatif au script) trouve les polices.
- **Polices** : Fraunces, Inter Tight, JetBrains Mono dans `vendor/fonts/` (woff2 latin + latin-ext), déclarées dans `vendor/fonts/fonts.css`. Référencé via `<link rel="stylesheet" href="vendor/fonts/fonts.css">`.
- **Template d'impression** (`printChapter()`) : le document généré est écrit dans un iframe (`about:blank`), donc une balise `<base href="${location.href}">` est injectée pour que les chemins relatifs `vendor/...` résolvent correctement.
- Pour mettre à jour MathJax : `npm pack mathjax@3`, extraire, recopier `es5/tex-mml-chtml.js` + `es5/output/chtml/fonts/woff-v2/`. Pour les polices : refetch du CSS Google avec un User-Agent Chrome, filtrer les subsets latin/latin-ext.

## PWA (installable + hors-ligne sur mobile)

- `manifest.webmanifest` (nom, icônes `icons/`, `display:standalone`, `theme_color`) + `sw.js` (service worker). Enregistré dans `index.html` en fin de `<body>`, **uniquement en http/https** (pas en `file://`).
- `sw.js` : précache toute la coquille (index.html, fonts.css, MathJax + toutes les polices, icônes) ; HTML en *réseau-d'abord* (frais en ligne, cache hors-ligne), assets en *cache-d'abord*.
- ⚠️ **À chaque modification d'un asset mis en cache** (index.html inclus), **incrémenter `CACHE_VERSION`** en tête de `sw.js` (`ptsi-cache-v1` → `v2`…), sinon les utilisateurs déjà « installés » gardent l'ancienne version en cache. Le HTML étant en réseau-d'abord, il se rafraîchit seul en ligne ; mais bumper la version reste la garantie propre.
- Si on ajoute/retire des polices, mettre à jour la liste `PRECACHE` de `sw.js`.
- Le service worker ne s'active pas en ouverture locale `file://` (normal) ; le hors-ligne local reste assuré par les assets embarqués.

## Outils

- `tools/validate.py` (Python stdlib, aucune dépendance) : vérifie cohérence `CHAPTERS` ↔ DOM, IDs HTML dupliqués, flashcards câblées (`makeFlash` par chapitre listant `flash`), `drawFn` existants. `python tools/validate.py` → `[OK]` / liste d'erreurs + exit ≠ 0. **À lancer avant chaque commit touchant `index.html`.**

## Anomalies connues (à traiter avec validation utilisateur)

1. ~~**ID dupliqué `int-meth`**~~ — **CORRIGÉ** : le `<select>` du simulateur des intégrales a été renommé `int-meth-sel` (le panneau garde `int-meth`). Avant, `getElementById('int-meth')` renvoyait la `<section>`, donc le choix de méthode d'intégration était ignoré.
2. **Commentaires de bannière obsolètes** : certains `<!-- CHAPITRE X -->` ne correspondent plus au chapitre qui suit (ex. l.~1893 « RLC » devant `chap-ondes`).
3. Deux chapitres ont `class="chapter active"` au chargement (`chap-rlc`, `chap-mcc`) — **non bug** : ils sont dans deux `<main>` séparés (physique vs SI), un seul affiché à la fois.

## Variables CSS de thème (`:root`)

`--ink`, `--paper`, `--paper-dark`, `--accent` (#c8472e), `--accent2` (#2d5f8a), `--green`, `--amber`, `--grid`, `--shadow`. Thème sombre : `:root[data-theme="dark"]` avec overrides ciblés. Bascule via `applyTheme()` (~l.31354).
