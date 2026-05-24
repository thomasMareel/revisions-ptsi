# CLAUDE.md — Conventions du projet revisions-ptsi

Ce fichier est lu par Claude Code au démarrage de chaque session.  
Il documente les conventions internes du projet pour maintenir la cohérence.

## Fichiers du projet

| Fichier | Rôle |
|---|---|
| `index.html` | Fichier principal servi par GitHub Pages |
| `cours_ptsi-42.html` | Backup (copie de travail, ne pas supprimer) |
| `README.md` | Documentation publique du projet |
| `CLAUDE.md` | Ce fichier — conventions internes |

## Architecture du fichier HTML

Tout est dans `index.html` (fichier monolithique, ~30 600 lignes) :

```
<head>          → CSS inline (~1638 lignes) + config MathJax
<body>
  <header>      → Titre + boutons (recherche, quiz, thème, impression)
  nav mobile    → #mob-header + #mob-drawer (≤767px)
  .matiere-bar  → Physique | Maths | SI  [desktop uniquement]
  .mat-content[data-mat-content="physique"]
  .mat-content[data-mat-content="maths"]
  .mat-content[data-mat-content="si"]
  <main>        → Chapitres Physique + Maths
  <main id="si-content"> → Chapitres SI
  #quiz-overlay → Modal quiz global
  #search-overlay → Overlay recherche
  <script>      → Tout le JS (~5738 lignes)
```

## Registre central des chapitres

Le tableau `CHAPTERS` (ligne ~24970) est **la source de vérité**.  
Chaque entrée doit correspondre à un `<div id="chap-{id}">` dans le DOM.  
Un script de validation (`validateChaptersCoherence`) tourne au boot et avertit en console si un chapitre est déclaré mais absent du DOM, ou présent sans déclaration.

## Convention de nommage des IDs

| Élément | Convention | Exemple |
|---|---|---|
| Div chapitre | `chap-{id}` | `chap-rlc` |
| Panel cours | `{prefix}-cours` | `rlc-cours` |
| Panel méthodes | `{prefix}-meth` | `rlc-meth` |
| Panel simulateur | `{prefix}-simu` | `rlc-simu` |
| Panel flashcards | `{prefix}-flash` | `rlc-flash` |
| Panel exercices | `{prefix}-exos` | `rlc-exos` |
| Canvas simulateur | `{prefix}-canvas` | `rlc-canvas` |
| Bouton navigation | `data-chap="{id}"` | `data-chap="rlc"` |

**Règle** : l'`id` est le nom court du chapitre (3-10 caractères, minuscules, tirets).  
Le `prefix` est encore plus court (2-6 caractères) et sert à préfixer tous les IDs internes.

## Structure standard d'un chapitre

```html
<!-- ========================================================== -->
<!-- ============== CHAPITRE {NOM EN MAJUSCULES} ============== -->
<!-- ========================================================== -->
<div class="chapter" id="chap-{id}">

<nav class="tabs">
  <button class="tab active" data-panel="{prefix}-cours"><span class="num">01</span>Cours</button>
  <button class="tab" data-panel="{prefix}-meth"><span class="num">02</span>Méthodes</button>
  <!-- Si simulateur : -->
  <button class="tab" data-panel="{prefix}-simu"><span class="num">03</span>Simulateur</button>
  <button class="tab" data-panel="{prefix}-flash"><span class="num">04</span>Flashcards</button>
  <button class="tab" data-panel="{prefix}-exos"><span class="num">05</span>Exercices</button>
</nav>

<!-- ============ {ID} : COURS ============ -->
<section class="panel active" id="{prefix}-cours">
  <div class="course-section">
    <div class="sec-num">§1 · TITRE DE SECTION EN MAJUSCULES</div>
    <h2>Titre lisible de la section</h2>
    <div class="intro">Texte d'introduction de 2-3 phrases.</div>
    <h3>Sous-section</h3>
    <div class="def-box">Définition ou formule clé.</div>
    <div class="prop-box">Propriété ou théorème.</div>
    <div class="notice">Mise en garde ou remarque importante.</div>
  </div>
  <!-- Répéter .course-section pour chaque grande section -->
</section>

<!-- ============ {ID} : MÉTHODES ============ -->
<section class="panel" id="{prefix}-meth">
  <div class="course-section">
    <div class="sec-num">MÉTHODES</div>
    <h2>Méthodes et savoir-faire</h2>
    <div class="method-box">
      <strong>Méthode : Titre</strong><br>
      Étapes de la méthode.
    </div>
  </div>
</section>

<!-- ============ {ID} : FLASHCARDS ============ -->
<section class="panel" id="{prefix}-flash">
  <div id="{prefix}-flash-content"><!-- injecté par makeFlash --></div>
  <div id="{prefix}-flash-prog"></div>
  <div id="{prefix}-flash-stats"></div>
</section>
<script>
makeFlash([
  { q: "Question ?", a: "Réponse." },
  { q: "Question 2 ?", a: "Réponse 2." }
], '{prefix}', '{prefix}-flash-content', '{prefix}-flash-prog', '{prefix}-flash-stats');
</script>

<!-- ============ {ID} : EXERCICES ============ -->
<section class="panel" id="{prefix}-exos">
  <div class="exo">
    <h3>Exercice 1 — Titre</h3>
    <p>Énoncé.</p>
    <button class="sol-btn" onclick="toggleSol(this)">Voir la solution</button>
    <div class="sol">Solution détaillée.</div>
  </div>
</section>

</div><!-- fin chap-{id} -->
```

## Déclaration CHAPTERS (ligne ~24970)

```js
{ id:'{id}',       prefix:'{prefix}',  name:'Nom complet du chapitre',
  matiere:'{physique|maths|si}',
  sub:'{ondes|meca|thermo|chimie|null}',   // null pour maths et si
  subLabel:'Sous-domaine affiché',
  domain:'{ondes|meca|thermo|chimie|maths|elec|auto}',  // pour la couleur
  matiereLabel:'Intitulé matière',
  panels:['cours','meth','flash','exos'],  // ajouter 'simu' si nécessaire
  drawFn:null,    // nom de la fonction JS de dessin canvas, ou null
  mobLabel:'Nom court mobile' }
```

## Bouton de navigation à ajouter

**Pour Physique** (dans `.mat-content[data-mat-content="physique"] .chapter-bar`) :
```html
<button class="chap-btn sub-content" data-chap="{id}" data-sub-content="{ondes|meca|thermo|chimie}" style="display:none">
  <span class="matiere">{Sous-domaine}</span>
  {Nom du chapitre}
</button>
```

**Pour Maths** (dans `.mat-content[data-mat-content="maths"] .chapter-bar`) :
```html
<button class="chap-btn" data-chap="{id}">
  {Nom du chapitre}
</button>
```

**Pour SI** (dans `.mat-content[data-mat-content="si"] .chapter-bar`) :
```html
<button class="chap-btn sub-content" data-chap="{id}" data-sub-content="{elec|meca-si}" style="display:none">
  <span class="matiere">{Sous-domaine}</span>
  {Nom du chapitre}
</button>
```

## Classes CSS des encadrés

| Classe | Usage |
|---|---|
| `.def-box` | Définition formelle, formule clé |
| `.prop-box` | Propriété, théorème, résultat important |
| `.method-box` | Méthode de résolution, algorithme |
| `.notice` | Mise en garde, piège à éviter |
| `.course-section` | Bloc de section (avec bordure colorée selon le domaine) |
| `.sec-num` | Numéro de section (§1 · NOM) |
| `.formula` | Formule display isolée (scroll horizontal sur mobile) |
| `.exo` | Bloc d'exercice |
| `.sol-btn` | Bouton "Voir la solution" |
| `.sol` | Contenu de la solution (masqué par défaut) |

## Variables CSS thème

```css
var(--ink)          /* Texte principal */
var(--paper)        /* Fond de page */
var(--paper-dark)   /* Fond encadrés / barres */
var(--accent)       /* Rouge — actions, actif */
var(--accent2)      /* Bleu — liens, secondaire */
var(--green)        /* Vert — méthodes */
var(--amber)        /* Orange — notices */
```

## Simulateurs canvas

Les chapitres avec simulateur ont :
- Un `<canvas>` dans `{prefix}-simu`
- Une fonction `draw{Xxx}()` exposée sur `window`
- Le champ `drawFn:'draw{Xxx}'` dans `CHAPTERS`
- Un `ResizeObserver` ou listener pour redessiner au resize

La fonction `redrawChapter(chapId)` appelle automatiquement la `drawFn` depuis le registre.

## Dépendances CDN (à connaître)

- **MathJax v3** : `cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js`  
  → Formules LaTeX. Délimiteurs : `\(…\)` (inline) et `$$…$$` (display).  
  → Rendu à la demande : `MathJax.typesetPromise([element])`.
- **Google Fonts** : Fraunces (titres), Inter Tight (corps), JetBrains Mono (code/UI).

## Incohérences connues (à corriger un jour)

- `chap-fluides` : `data-sub-content="meca"` dans le nav HTML mais `sub:'thermo'` dans CHAPTERS → invisible sous l'onglet Thermodynamique
- SI nav : `transm`, `dynsolide`, `energsi`, `slci` apparaissent en double dans les boutons de navigation
- SI : `mcc`, `cvs`, `hacheurs` ont `data-sub-content="meca"` au lieu de `"elec"`
