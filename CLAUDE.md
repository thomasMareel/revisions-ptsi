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

## Dépendances externes (CDN)

- **MathJax 3** : `cdn.jsdelivr.net/npm/mathjax@3/...` (l.31).
- **Google Fonts** : Fraunces, JetBrains Mono, Inter Tight (l.9).
- `printChapter()` régénère un document d'impression qui recharge ces mêmes ressources.
- Conséquence hors-ligne : formules en texte brut + police système. À héberger en local si la révision hors-ligne devient un besoin.

## Anomalies connues (à traiter avec validation utilisateur)

1. **ID dupliqué `int-meth`** (vrai bug) : utilisé par le panneau Méthodes des intégrales (`<section id="int-meth">`, ~l.17286) ET par un `<select id="int-meth">` du simulateur (~l.17425). `getElementById` ne renvoie que le premier.
2. **Commentaires de bannière obsolètes** : certains `<!-- CHAPITRE X -->` ne correspondent plus au chapitre qui suit (ex. l.~1893 « RLC » devant `chap-ondes`).
3. Deux chapitres ont `class="chapter active"` au chargement (`chap-rlc`, `chap-mcc`) — **non bug** : ils sont dans deux `<main>` séparés (physique vs SI), un seul affiché à la fois.

## Variables CSS de thème (`:root`)

`--ink`, `--paper`, `--paper-dark`, `--accent` (#c8472e), `--accent2` (#2d5f8a), `--green`, `--amber`, `--grid`, `--shadow`. Thème sombre : `:root[data-theme="dark"]` avec overrides ciblés. Bascule via `applyTheme()` (~l.31354).
