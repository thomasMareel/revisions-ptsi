# Gabarit — Ajouter un nouveau chapitre

Ce fichier est un **modèle à copier-coller** dans `index.html`. Il n'est pas utilisé par le site, c'est juste une aide-mémoire.

## Principe : 4 morceaux à ajouter

Pour ajouter un chapitre, il faut toucher **4 endroits** dans `index.html` :

| # | Quoi | Où le coller |
|---|------|--------------|
| A | Le **bouton de navigation** | dans la bonne `<div class="chapter-bar …">` (selon la matière) |
| B | Le **bloc du chapitre** (onglets + panneaux) | dans le bon `<main>` (physique/maths, ou `#si-content` pour la SI) |
| C | L'**entrée dans le tableau `CHAPTERS`** | dans le tableau `const CHAPTERS = [ … ]` (vers la ligne ~24985) |
| D | Les **flashcards** | dans la zone des `const …Cards = [ … ]` + `makeFlash(...)` (vers la ligne ~25940) |

## Convention de nommage (à choisir avant de commencer)

- **`id`** du chapitre : un identifiant unique, ex. `magnetisme`. Le bloc devient `id="chap-magnetisme"`, le bouton `data-chap="magnetisme"`.
- **`prefix`** : un préfixe court pour les panneaux et flashcards, ex. `mag`. Les panneaux deviennent `mag-cours`, `mag-meth`, `mag-flash`, `mag-exos`.
- ⚠️ `id` et `prefix` peuvent être différents — choisis-les uniques (vérifie qu'aucun autre chapitre ne les utilise déjà).

Dans les gabarits ci-dessous, remplace **`monid`** par ton id et **`mon`** par ton prefix.

---

## A. Bouton de navigation

À coller dans la `.chapter-bar` de la bonne matière (cherche `class="chapter-bar mat-content" data-mat-content="…"`) :

```html
<button class="chap-btn" data-chap="monid">
  <span class="matiere">Sous-domaine</span>Nom du chapitre
</button>
```

> Pour la physique, les boutons ont en plus `sub-content` + `data-sub-content="…"` pour le filtrage par sous-domaine. Copie le format d'un bouton physique voisin si besoin.

---

## B. Bloc du chapitre

À coller dans le `<main>` correspondant (juste avant la fin `</main>`, ou entre deux chapitres existants).
Ce gabarit est la **version sans simulateur** (le cas le plus courant). Pour ajouter un simulateur, voir la note en bas.

```html
<!-- ====================== CHAPITRE : Nom du chapitre ====================== -->
<div class="chapter" id="chap-monid">

<nav class="tabs">
  <button class="tab active" data-panel="mon-cours"><span class="num">01</span>Cours</button>
  <button class="tab" data-panel="mon-meth"><span class="num">02</span>Méthodes</button>
  <button class="tab" data-panel="mon-flash"><span class="num">03</span>Flashcards</button>
  <button class="tab" data-panel="mon-exos"><span class="num">04</span>Exercices</button>
</nav>

<!-- ---------- COURS ---------- -->
<section class="panel active" id="mon-cours">
  <div class="course-section">
    <div class="sec-num">§1 · TITRE DE SECTION</div>
    <h2>Titre principal</h2>
    <div class="intro">Phrase d'introduction de la section.</div>

    <h3>Sous-titre</h3>
    <p>Paragraphe de cours. Math en ligne : \(a^2 + b^2 = c^2\).</p>
    <div class="formula">$$E = mc^2$$</div>

    <div class="def-box"><strong>Définition.</strong> Texte de la définition.</div>
    <div class="prop-box"><strong>Propriété.</strong> Texte de la propriété.</div>

    <div class="reveal" onclick="this.classList.toggle('open')">
      <span class="label">Application</span>
      <span class="prompt">Énoncé court de l'application</span>
      <div class="content"><p>Réponse révélée au clic.</p></div>
    </div>
  </div>
</section>

<!-- ---------- MÉTHODES ---------- -->
<section class="panel" id="mon-meth">
  <div class="course-section">
    <div class="sec-num">MÉTHODES · NOM</div>
    <h2>Stratégies pour les exercices</h2>
    <div class="method-box">
      <strong>Méthode 1 — Titre de la méthode</strong>
      <ol style="margin-top:0.4rem">
        <li><span class="step">Étape 1.</span> Première étape.</li>
        <li><span class="step">Étape 2.</span> Deuxième étape.</li>
      </ol>
    </div>
  </div>
</section>

<!-- ---------- FLASHCARDS (ne pas modifier, sauf le prefix) ---------- -->
<section class="panel" id="mon-flash">
<div class="flash-wrapper">
  <div class="flash-progress" id="mon-flash-prog">Carte 1 / —</div>
  <div class="flash-card" onclick="flashFlip('mon')">
    <div class="flash-side" id="mon-flash-content"><span class="tag">Question</span><div>Chargement…</div></div>
    <div class="flash-hint">Touche pour révéler · Espace / ← → pour naviguer</div>
  </div>
  <div class="flash-controls">
    <button class="hard" onclick="flashRate('mon', 0)">À revoir</button>
    <button class="ok" onclick="flashRate('mon', 1)">Hésitant</button>
    <button class="easy" onclick="flashRate('mon', 2)">Acquis</button>
  </div>
  <div class="flash-stats-wrap">
    <span id="mon-stats">—</span>
    <div style="margin-top:0.8rem"><button class="flash-reset" onclick="flashReset('mon')">↺ Réinitialiser ma progression</button></div>
  </div>
</div>
</section>

<!-- ---------- EXERCICES ---------- -->
<section class="panel" id="mon-exos">
<div class="exo-wrapper">
  <div class="exo">
    <span class="num">EXO 01</span><span class="diff">★ ☆ ☆</span>
    <h3>Titre de l'exercice</h3>
    <div class="statement">Énoncé de l'exercice. Math : \(x \in \mathbb{R}\).</div>
    <div class="q"><strong>Q1.</strong> Première question.</div>
    <button class="toggle-sol" onclick="toggleSol(this)">Voir la solution</button>
    <div class="solution">
      <h4>Correction</h4>
      <p><strong>Q1.</strong> Réponse.</p>
    </div>
  </div>
</div>
</section>

</div>
<!-- ====================== FIN CHAPITRE ====================== -->
```

---

## C. Entrée dans le tableau `CHAPTERS`

À coller dans `const CHAPTERS = [ … ]` (vers la ligne ~24985), parmi les chapitres de la même matière :

```js
{ id:'monid', prefix:'mon', name:'Nom complet du chapitre',
  matiere:'physique', sub:'ondes', subLabel:'Ondes & signaux', domain:'ondes',
  matiereLabel:'Sous-titre affiché', panels:['cours','meth','flash','exos'], drawFn:null,
  mobLabel:'Nom court (mobile)' },
```

- `matiere` : `'physique'`, `'maths'` ou `'si'`.
- `sub` / `subLabel` / `domain` : copie ceux d'un chapitre voisin de la même zone (mets `sub:null` en maths).
- `drawFn:null` car pas de simulateur.

---

## D. Flashcards

À coller dans la zone des cartes (vers la ligne ~25940), avec les autres `const …Cards` :

```js
const monCards = [
  {q:"Première question ?", a:"Première réponse."},
  {q:"Deuxième question ?", a:"Deuxième réponse."}
];
const monFlash = makeFlash(monCards, 'mon', 'mon-flash-content', 'mon-flash-prog', 'mon-stats');
```

> ⚠️ **Les flashcards utilisent des caractères Unicode**, PAS de LaTeX. Écris `ω₀`, `√(LC)`, `½`, `→`, `x²` — et non `\(\omega_0\)`.

---

## Vérification après ajout

1. Ouvre `index.html` dans le navigateur.
2. Ouvre la **console** (F12) : la fonction `validateChaptersCoherence()` y signale toute incohérence entre le tableau `CHAPTERS` et le DOM (id manquant, etc.).
3. Vérifie que le bouton apparaît, que les 4 onglets fonctionnent, que les formules se rendent et que les flashcards défilent.

## Ajouter un simulateur (optionnel, avancé)

1. Ajoute un onglet `<button class="tab" data-panel="mon-simu">…Simulateur</button>` et un `<section class="panel" id="mon-simu">` avec un `<canvas id="mon-canvas">`.
2. Dans l'entrée `CHAPTERS`, mets `panels:['cours','meth','simu','flash','exos']` et `drawFn:'drawMon'`.
3. Écris une fonction globale `function drawMon(){ … }` qui dessine sur le canvas (inspire-toi de `drawInt`, `drawSim`, etc.).
