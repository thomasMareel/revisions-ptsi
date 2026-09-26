# Gabarit — Ajouter un nouveau chapitre

Ce fichier est un **modèle à copier-coller** dans `index.html`. Il n'est pas utilisé par le site, c'est juste une aide-mémoire.

> 💡 **Retrouver un endroit dans `index.html`** : le fichier fait plus de 50 000 lignes et les numéros de ligne changent à chaque modification. On cherche donc un **texte repère** : dans ton éditeur, `Ctrl+F` puis le repère indiqué (par ex. `const CHAP_GROUPS`) ; dans un terminal, `grep -n "const CHAP_GROUPS" index.html`.

## Principe : 5 endroits à modifier

| # | Quoi | Où (texte repère à chercher) |
|---|------|------------------------------|
| A | L'**entrée dans le tableau `CHAPTERS`** | `const CHAPTERS = [` — parmi les chapitres de la même matière |
| B | L'**id dans `CHAP_GROUPS`** (range le chapitre dans le menu, dans l'ordre) | `const CHAP_GROUPS` — dans le bon groupe |
| C | L'**id dans `__YEAR2A`** — *seulement pour un chapitre de 2ᵉ année* | `window.__YEAR2A = new Set` |
| D | Le **bloc du chapitre** (onglets + panneaux) | le bon `<main>` : `id="si-content"` pour la SI, le `<main>` principal pour les autres matières |
| E | Les **flashcards** (`const …Cards` + `makeFlash(...)`) | juste après une ligne `Flash = makeFlash(` existante (repère : `Flash = makeFlash(`) |

⚠️ **Il n'y a PAS de bouton de navigation à écrire.** Le menu des chapitres (tiroir) et les boutons `.chap-btn` sont construits automatiquement à partir de `CHAPTERS` et `CHAP_GROUPS` ; un bouton ajouté à la main serait effacé.

## Convention de nommage (à choisir avant de commencer)

- **`id`** du chapitre : un identifiant unique, ex. `magnetisme`. Le bloc devient `id="chap-magnetisme"`, et le lien direct `…/index.html#magnetisme/cours`.
- **`prefix`** : un préfixe court pour les panneaux et les flashcards, ex. `mag`. Les panneaux deviennent `mag-cours`, `mag-meth`, `mag-flash`, `mag-exos`.
- ⚠️ `id` et `prefix` peuvent être différents (c'est le cas de la plupart des chapitres) — choisis-les **uniques** : vérifie qu'aucun autre chapitre ne les utilise déjà (`grep -n "id:'magnetisme'" index.html`, `grep -n "prefix:'mag'" index.html`).

Dans les gabarits ci-dessous, remplace **`monid`** par ton id et **`mon`** par ton prefix.

---

## A. Entrée dans le tableau `CHAPTERS`

À coller dans `const CHAPTERS = [ … ]`, parmi les chapitres de la même matière :

```js
{ id:'monid', prefix:'mon', name:'Nom complet du chapitre',
  matiere:'physique', sub:'ondes', subLabel:'Ondes & signaux', domain:'ondes',
  matiereLabel:'Sous-titre affiché', panels:['cours','meth','flash','exos'], drawFn:null,
  mobLabel:'Nom court (menu)' },
```

- `matiere` : `'physique'`, `'maths'`, `'si'`, `'info'` ou `'anglais'`.
- `sub` / `subLabel` : tu peux les recopier d'un voisin, mais ils sont **réécrits automatiquement** par `CHAP_GROUPS` (étape B).
- `matiereLabel` (petit tag du bouton de chapitre, repris sur la page de garde de l'impression ; le bandeau de titre, lui, affiche `subLabel`) et `domain` (couleur d'accent) **ne sont pas** réécrits : recopie-les d'un chapitre du **même groupe**.
- `panels` : la liste des onglets. Elle doit correspondre **exactement** aux onglets du bloc D.
- `drawFn:null` car pas de simulateur (voir la dernière section sinon).
- **Anglais (ou autre langue)** : `panels:['cours','flash']` en général (pas d'exercices). Les cartes sont affichées en texte brut (pas de maths) et peuvent être lues à voix haute.

---

## B. Ranger le chapitre dans `CHAP_GROUPS`

Cherche `const CHAP_GROUPS`. Chaque ligne est un groupe `[ code, 'Libellé', [ids dans l'ordre] ]`. Ajoute `'monid'` dans la liste du bon groupe, **à la position voulue** (c'est l'ordre d'affichage dans le menu) :

```js
['ondes',  'Ondes & signaux',   ['regimecontinu','premierordre','rlc', 'monid', 'signaux', …]],
```

> Si tu oublies cette étape, le chapitre existe quand même mais il est rejeté **tout en bas** de la liste.

## C. Chapitre de 2ᵉ année (sinon, passe à D)

Juste en dessous de `CHAP_GROUPS`, ajoute `'monid'` dans `window.__YEAR2A = new Set([ … ])`. Le chapitre reçoit alors le badge « 2ᵉ année » dans son bandeau de titre et n'apparaît que lorsque « 2ᵉ année » est sélectionnée dans le menu.

---

## D. Bloc du chapitre

À coller dans le bon `<main>` (entre deux chapitres existants : cherche `id="chap-` d'un voisin). Pour la **SI**, c'est dans `<main id="si-content">`.
Ce gabarit est la **version sans simulateur** (le cas le plus courant). Pour un chapitre d'anglais, garde seulement les onglets Cours et Flashcards (et renumérote : 01, 02).

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
  <!-- Exercice type concours (facultatif) : <div class="exo concours"> … </div>,
       à placer ICI, à l'intérieur de .exo-wrapper, sans </div> supplémentaire. -->
</div>
</section>

</div>
<!-- ====================== FIN CHAPITRE ====================== -->
```

**Règles pour les formules du cours** :
- en ligne `\( … \)`, en bloc `$$ … $$` (pas `\[ … \]`) ;
- jamais un `<` collé à une lettre dans une formule (`\(a<b\)` casse la page) : écrire `\(a \lt b\)` ;
- pas de commandes exotiques (`\cancel`, `\ce`…) : elles ne sont pas disponibles hors-ligne ;
- une très longue formule en ligne déborde sur téléphone : la mettre plutôt en bloc `$$ … $$` dans une `<div class="formula">`.

---

## E. Flashcards

Cherche une ligne `Flash = makeFlash(` d'un chapitre voisin et colle ton paquet **juste après** (les cartes doivent être déclarées après la définition de `makeFlash`, sinon tout le site plante) :

```js
const monCards = [
  {q:"Première question ?", a:"Première réponse."},
  {q:"Période propre ?", a:"T₀ = 2π√(LC)", cat:'form'},
  {q:"Vitesse de la lumière dans le vide ?", a:"c ≈ 3,00·10⁸ m/s", cat:'val'}
];
const monFlash = makeFlash(monCards, 'mon', 'mon-flash-content', 'mon-flash-prog', 'mon-stats');
```

- **Formules : caractères Unicode par défaut.** Écris `ω₀`, `√(LC)`, `½`, `→`, `x²`, `e^(iθ)`, `u_n` : le site les convertit tout seul en belles formules (même police que le cours). Si une carte s'affiche mal, tu peux l'écrire directement en LaTeX, avec **deux** antislashs dans le code JS : `a:"\\(\\omega_0 = \\dfrac{1}{\\sqrt{LC}}\\)"`.
- **Anglais** : texte brut, pas de maths ; tu peux utiliser `<strong>`, `<em>`, `<br>` dans les réponses.
- `cat` est **facultatif** : `'form'` (formule) ou `'val'` (grandeur usuelle) permet de filtrer ces cartes dans le Quiz.
- **Modifier un paquet plus tard** : tu peux ajouter, supprimer ou réordonner des cartes, et corriger une réponse, **sans perdre ta progression**. Tu peux aussi retoucher le texte des cartes — question, réponse ou les deux, même avec un « rechercher/remplacer » sur tout le paquet — **tant que tu ne changes ni le nombre ni l'ordre des cartes** : chaque carte garde sa progression. Deux exceptions rares : une question présente **en double** dans le paquet (même question sur deux cartes) — n'en retouche **qu'une copie par mise à jour** (d'abord la question de l'une ; plus tard la réponse de l'autre, ou la suppression d'une copie) ; et une réponse que tu **déplaces d'une carte à une autre** en retouchant aussi leurs questions — les deux cartes peuvent alors échanger leur progression.
  - Attention si tu **retouches la question** d'une carte **en même temps** que tu ajoutes, supprimes ou déplaces des cartes **tout près d'elle** (entre les mêmes cartes voisines) : sa progression peut repartir de zéro, ou même être remplacée par celle d'une carte supprimée à côté (surtout si tu as aussi changé sa réponse).
  - Une carte ajoutée **exactement à la place** d'une carte supprimée (entre les mêmes voisines) **hérite de la progression** de la carte supprimée. Pour qu'elle reparte de zéro, ajoute-la à un autre endroit du paquet.
  - Le plus sûr : faire les retouches de texte et les ajouts/suppressions dans **deux mises à jour séparées** (en ouvrant le site entre les deux, sur chaque appareil où tu révises : la progression est enregistrée dans le navigateur).

---

## Vérification après ajout

1. **Change le numéro de version** : en haut de `sw.js`, incrémente `CACHE_VERSION` (ex. `'ptsi-cache-v81'` → `'ptsi-cache-v82'`). Sans ça, l'application installée ne proposera pas la mise à jour.
2. **Lance le validateur** (quelques secondes) :
   ```
   python tools/validate.py
   ```
   Il vérifie la cohérence `CHAPTERS` ↔ page, les IDs dupliqués, les flashcards câblées, les `drawFn` et les `<` mal placés dans les formules. Il affiche `[OK]` ou la liste des erreurs.
3. **Vérifie la syntaxe JavaScript** : `python tools/check_js.py` (doit afficher `blocs en erreur: 0`).
4. **Lance les tests navigateur** (mode d'emploi : [`tests/README.md`](tests/README.md)) :
   ```
   npm run test:rapide
   node tests/run.js --suite=site --chapitres=monid
   ```
5. Ouvre `index.html` dans le navigateur, avec la **console** ouverte (F12) : aucune erreur rouge ne doit apparaître. Vérifie que le chapitre est dans le menu (au bon endroit), que les onglets fonctionnent, que les formules se rendent et que les flashcards défilent.

---

## Ajouter un simulateur (optionnel, avancé)

Un simulateur est un dessin sur un `<canvas>` piloté par des curseurs. Le plus simple est de copier un simulateur existant qui ressemble au tien (par ex. le 1ᵉʳ ordre : cherche `SYSTÈME 1er ORDRE`).

**1. Dans le bloc D** : ajoute l'onglet et le panneau (et renumérote les onglets suivants).

```html
<button class="tab" data-panel="mon-simu"><span class="num">03</span>Simulateur</button>
…
<section class="panel" id="mon-simu">
<div class="sim-wrapper">
  <h2>Simulateur — Titre</h2>
  <div class="sim-controls">
    <div class="control">
      <label>Paramètre a</label>
      <input type="range" id="mon-a" min="0" max="10" step="0.1" value="2">
      <span class="value" id="mon-a-val">2</span>
    </div>
    <div class="control">
      <label>Animer</label>
      <input type="checkbox" id="mon-anim" style="width:auto;align-self:start">
      <span class="value" id="mon-anim-val">non</span>
    </div>
  </div>
  <canvas id="mon-canvas"></canvas>
  <div class="sim-info">
    <div><span class="lbl">Résultat</span><span id="mon-info">—</span></div>
  </div>
</div>
</section>
```

**2. Dans `CHAPTERS`** : `panels:['cours','meth','simu','flash','exos']` et `drawFn:'drawMon'`.

**3. Le code** : colle ce modèle juste après le dernier simulateur (repère : `window.drawInt = drawInt;`, puis la ligne `})();` qui suit).

```js
/* ===== MON SIMULATEUR ===== */
(function(){
  const canvas = document.getElementById('mon-canvas');
  if(!canvas) return;                      // défensif : jamais d'erreur au chargement
  const ctx = canvas.getContext('2d');
  const $ = id => document.getElementById(id);
  let animId = null, t = 0;

  function render(){
    // Garde « panneau actif » : ne rien dessiner si l'onglet Simulateur est caché
    const panel = $('mon-simu'); if(panel && !panel.classList.contains('active')) return;
    const dpr = window.devicePixelRatio || 1;          // relu à chaque dessin
    const r = canvas.getBoundingClientRect();
    canvas.width = r.width * dpr; canvas.height = r.height * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const W = r.width, H = r.height, C = __CV();       // couleurs du thème (clair/sombre)
    ctx.clearRect(0, 0, W, H);
    ctx.strokeStyle = C.grid;  /* … grille … */
    ctx.strokeStyle = C.accent; ctx.lineWidth = 2;     /* … courbe … */
    ctx.fillStyle = __CVA('accent2', 0.15);            // couleur du thème avec transparence
    $('mon-info').textContent = '…';
  }

  // Boucle d'animation : s'arrête d'elle-même quand le canvas n'est plus visible
  function loop(){
    if(canvas.offsetParent === null){ animId = null; return; }
    t += 0.02; render(); animId = requestAnimationFrame(loop);
  }
  function start(){ if(animId === null) animId = requestAnimationFrame(loop); }
  function stop(){ if(animId !== null){ cancelAnimationFrame(animId); animId = null; render(); } }

  $('mon-a').addEventListener('input', () => { $('mon-a-val').textContent = $('mon-a').value; render(); });
  // Case nommée « …-anim » : décochée automatiquement si l'utilisateur préfère réduire les animations
  $('mon-anim').addEventListener('change', () => {
    $('mon-anim-val').textContent = $('mon-anim').checked ? 'oui' : 'non';
    if($('mon-anim').checked) start(); else stop();
  });

  function drawMon(){ render(); if($('mon-anim').checked) start(); }
  window.drawMon = drawMon;                // OBLIGATOIRE : le site appelle window[drawFn]
})();
```

**4. Les finitions** :
- **Couleurs** : uniquement `__CV()` (`C.ink`, `C.paper`, `C.accent`, `C.accent2`, `C.green`, `C.amber`, `C.muted`, `C.grid`) et `__CVA('nom', alpha)` — **jamais** de couleur écrite en dur (`'#c8472e'`, `rgba(…)`), sinon le simulateur devient illisible en thème sombre.
- **Redimensionnement de la fenêtre** : ajoute ta fonction au gestionnaire global (repère : `window.addEventListener('resize',()=>{drawSim();`) sur le modèle `if(typeof drawMon==='function')drawMon();`.
- **Taille du canvas** : ajoute `#mon-canvas` à la règle CSS commune des canvas (repère : `#sim-canvas, #opt-canvas`) ; pour une autre hauteur, ajoute une ligne comme `#mon-canvas{height:480px}` juste après.
- **Badge de régime** (`.regime-badge`) : une nouvelle variante doit recevoir sa couleur dans le bloc CSS « Contraste des encadrés de simulateur en thème sombre ».
- **Teste dans les deux thèmes** (bouton Thème), puis `node tests/run.js --suite=site --chapitres=monid` : la suite vérifie que le simulateur s'exécute et dessine en clair et en sombre.
