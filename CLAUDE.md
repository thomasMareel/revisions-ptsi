# CLAUDE.md — Conventions du projet « Révisions PTSI »

Notes destinées à Claude pour les sessions futures. Objectif du projet : rendre maintenable un fichier de révisions PTSI et l'héberger sur GitHub Pages, **sans casser l'existant**.

**Où est le détail.** Ici : règles et architecture ; au besoin, `docs/interface.md` (implémentation, texte complet des règles résumées ici) et `docs/historique-contenu.md` (chantiers de contenu). Renvois : « fichier › section ». En cas d'écart, ce fichier fait foi.

## Règles de collaboration

- **Tout en français** (réponses, commentaires, contenu).
- **Ne rien casser** de ce qui marche (design + fonctionnalités). Pas de refonte non demandée (la refonte graphique « Cahier de prépa » d'octobre 2026 a été demandée et sa conception validée : voir « Identité visuelle »).
- **Modifications du HTML autorisées sans confirmation préalable** (accord donné par l'utilisateur le 2026-09-26) : agir directement, puis expliquer ce qui a été fait.
- L'utilisateur est étudiant en prépa, débutant en dev. Privilégier des explications claires et des changements incrémentaux.
- **Mise en ligne systématique (consigne de l'utilisateur du 2026-10-05)** : **chaque tâche terminée est publiée sur `main` sans demander la permission**, petits correctifs comme gros changements. Avant de pousser : `validate.py`, `check_js.py`, suites de tests concernées (batterie complète pour un gros changement), bump de `CACHE_VERSION` si un asset change ; pour un gros changement, créer d'abord un point de retour (branche `sauvegarde-avant-…` sur l'état actuel de `main`). Ensuite : vérifier que le run Actions est `completed success`, et dire à l'utilisateur ce qui est en ligne. Ne jamais pousser un travail inachevé ou dont les tests échouent. **Exception** : ce que l'**assistant IA** du site modifie (sessions Managed Agents lancées depuis le panneau) passe par une **pull request**, jamais par un push sur `main` ; c'est Thomas qui fusionne (voir « Assistant IA »).
- **Contenus de 2ᵉ année (PT spé)** : rédigés à partir des manuels privés du dépôt `thomasMareel/cours-pt-spe` (release v1), qui ne servent qu'à cerner le programme et les notations. **Rédaction originale obligatoire** (site public, droit d'auteur) : ne jamais recopier ni paraphraser de près leurs phrases, énoncés, corrigés, exemples chiffrés, schémas ou plans ; exercices inventés.

## Cours vidéo (dossier `video/`)

- Fabrication des **cours vidéo « prof au tableau »** et sources LaTeX des cours PDF. **Mode d'emploi complet : `video/README.md`** ; mise en ligne : `video/YOUTUBE.md`.
- Voix (depuis le chapitre 4) : `"expressivite": 3.0`, `"tempo": 1.0` dans `chapitre.json`, texte sur un ton vivant.
- **Format de toutes les vidéos à venir** (2026-11-16) : cours **condensé** (≈ 25-30 %) puis **vraie résolution d'exercices** (≈ 70 %, 2 ou 3 exercices inventés), 10 à 13 min : `video/README.md` › « Format ».
- Indépendant du site (rien de `video/` n'est chargé ni mis en cache) : pas de bump de `CACHE_VERSION` pour un changement limité à `video/`.
- Session vidéo sur l'**environnement cloud dédié « revisions-ptsi »** (secret réseau Mistral, variables YouTube ; « Default » n'en a aucun). Avant tout travail vidéo : `bash video/installer.sh`.
- **Mise en place faite le 2026-11-11** (clé Mistral en secret réseau, autorisation YouTube durable `YT_REFRESH_TOKEN`, premiers envois réels réussis) ; à refaire seulement si une clé est révoquée : suivre `video/MISE-EN-PLACE.md` **pas à pas, une étape à la fois** ; ne jamais lui faire coller un secret dans la conversation. Envoi d'un chapitre : `python3 ../../commun/youtube.py envoi` depuis son dossier.
- **Aucun fichier produit n'est versionné** (audio, images, MP4, PDF : `.gitignore`) ; les vidéos vont sur **YouTube en non répertorié**, le site n'en garde que les liens ; les MP4 et SRT finis sont envoyés à l'utilisateur dans la conversation. Vidéos en ligne : `docs/historique-contenu.md` › « Cours vidéo ».
- **Clé Mistral : jamais dans le dépôt (public)**, ni dans un fichier, un commit ou une sortie affichée ; elle vient de l'environnement cloud (secret réseau `api.mistral.ai`, ou variable `MISTRAL_API_KEY`). Même règle pour les identifiants YouTube (`YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`).
- **Onglet « Vidéos »** : table **`window.__VIDEOS`** (`grep -n 'window.__VIDEOS = {'`, champ `src` = `video/<cours>/chN`), aperçus dans `media/videos/`, lecteur créé **au clic seulement**. Ajouter une vidéo : une entrée + son aperçu ; nouvel onglet : `video/README.md` › « Intégration au site » ; détail : `docs/interface.md` › « Onglet Vidéos ».

## Assistant IA (phase 0 en ligne le 2026-11-19 ; phase 1 prête, en attente de mise en service)

- Bouton « Assistant » (discussion écrite puis vocale ; modifications par Claude Managed Agents). **Plan : `docs/assistant-ia.md`** (à lire avant tout travail sur l'assistant, à tenir à jour à chaque phase).
- Phase 0 : bouton activé par `?assistant=1` (`?assistant=0` le retire), `assistant/assistant.js` chargé au premier usage. Phase 1 dormante tant que `RELAIS` est vide ; relais `assistant/relais/` (`cd assistant/relais && npm install && npm test`). Détail : `docs/interface.md` › « Assistant IA ».
- **Mise en service par Thomas : `assistant/MISE-EN-SERVICE.md`** (comptes Anthropic et Cloudflare, secrets saisis par lui seul) ; à la fin, écrire l'adresse du relais dans `RELAIS`, relancer `npm test` du relais, la suite `assistant`, publier.

Règles permanentes, pour toutes les sessions :

- **Aucune clé dans le front-end ni dans le dépôt** (Anthropic, Mistral, GitHub, YouTube, Cloudflare) : tout appel aux API passe par le **relais authentifié** (Cloudflare Worker recommandé), dont les secrets sont saisis par Thomas dans la console, jamais dans une conversation. Le jeton de l'assistant n'est jamais rangé dans `Store` ni dans une clé `localStorage` exportée par la Sauvegarde (origine `thomasmareel.github.io` partagée).
- **Rester compatible avec la collecte du contexte** (`window.__contexteAssistant()`, schéma versionné) : garder `CHAPTERS` source de vérité, `div#chap-<id>`, panneaux `<prefix>-<onglet>`, surtitres `.sec-num` « §n · … », `.exo` (`.num`, `h3`, `.statement`, `.solution`) dans `.exo-wrapper`, `.method-box`, fiche `.flash-side` (`.fc-q`, `.fc-a`, `.fp-n`), simulateurs `.sim-wrapper`, routage `#id/onglet`, `window.__surSection`, `__preparerSections`, la table `__VIDEOS` avec son champ **`src`** (dossier `video/<cours>/chN`, écrit aussi par les scripts `integrer_videos.py`), `window.__instantVideo()` et un `timeline.json` versionné par vidéo. Un nouvel onglet ou une nouvelle page se déclare au collecteur (`assistant/assistant.js`) et passe la suite de tests `assistant`.
- **Aucune requête externe avant que Thomas ouvre et utilise le panneau** (comme l'onglet Vidéos) ; hors ligne : message, aucune tentative. Code de l'assistant chargé à la demande, rien de plus au démarrage du site.
- **Modifications demandées depuis l'assistant : pull request seulement** (compte robot sans droit sur `main`, budget plafonné par session) ; les skills réutilisables (kit vidéo, PDF, modification d'un chapitre) iront dans `.claude/skills/<nom>/SKILL.md` (aucune n'existe encore), courtes et renvoyant à `CLAUDE.md` et `video/README.md`.

## Architecture

- **Démarrage : `index.html` seul** (≈ 3 Mo : coquille, CSS, scripts, paquets de cartes, chaque `div.chapter` avec ses onglets et ses panneaux). Le **contenu des onglets Cours, Méthodes et Exercices** vit dans **`chapitres/<id>.html`** (un fichier par chapitre, nommé par l'`id`), chargé à l'ouverture du chapitre ; l'index de la recherche dans `chapitres/recherche.json` ; `assistant/assistant.js` à la demande. Tout le reste inline : 20 blocs `<script>` : 5 petits, **un grand script applicatif unique** (de `const Store = (function` à l'impression), 14 modules (liste : `docs/interface.md` › « Scripts inline »).
- Une exception non rattrapée dans le grand script coupe tout ce qui suit (decks, navigation, quiz, tiroir) : code de chargement défensif (`if(!el) return;`), modules enveloppés (`try/catch`, `sur(f)`).
- **Un fichier par chapitre** (point 6 de l'audit, 2026-11-27 ; plan et mesures : `docs/chargement-chapitres.md`) : dans `index.html`, les panneaux Cours, Méthodes, Exercices sont **vides** (`<section class="panel" id="<prefix>-cours"></section>`) ; leur contenu est dans `chapitres/<id>.html`, sous la forme `<template class="pan-tpl" data-panneau="<prefix>-cours">…</template>` (un par onglet, dans l'ordre d'`index.html`). **Règle : un chapitre visible a toujours son contenu.** `window.__chargerChapitre(id)` → promesse ; le clic sur un `.chap-btn` d'un chapitre pas encore chargé est **différé** (écouteur en capture) puis rejoué ; `navigateTo` attend le chargement (`window.__demanderChapitre` : la dernière demande l'emporte) ; `window.__chapitreCharge(id)`, `window.__navigationEnCours()`. Le script du `<head>` demande d'emblée le chapitre de départ (`window.__prechargement`) et masque la colonne (`html.chap-attente`) jusqu'à son affichage. Les `<template>` chargés sont mis en place par `window.__deplierChapitre(chap)` (rappels `window.__apresDepliage`) ; `window.__racinePanneau(p)` lit un panneau encore replié. Rien de ce qui suit le clic n'a changé ; un chapitre pas encore chargé n'est ni rendu ni mesuré (`typesetPanel`, `__aFormulaire` ne mémorisent rien). Détail : `docs/interface.md` › « Un fichier par chapitre ».
- **Éditer un chapitre = éditer `chapitres/<id>.html`** (se lit en entier, par morceaux si long), puis **`node tools/chapitres.js`** (≈ 7 s, Playwright comme les tests) : il régénère le manifeste `window.__CHAPITRES` (empreinte de chaque fichier, script du `<head>`, entre deux marqueurs) et `chapitres/recherche.json` ; `validate.py` refuse des données périmées. Dans un fichier de chapitre : aucun `<script>`, `<style>` ni `<marker>`/`<symbol>` partagé (chargé tard, il ne s'appliquerait pas avant l'ouverture du chapitre), aucun `</template>` dans le contenu.
- **`index.html` ne s'ouvre plus par un double-clic** (`file://` : les chapitres ne se chargent pas, toast d'explication) : passer par le site en ligne ou `python -m http.server` dans le dossier.
- **Ne jamais lire `index.html` en entier** ni se fier à des numéros de ligne : chercher par **ancre grep** (`grep -n 'const CHAPTERS = \['`, puis `sed -n 'A,Bp'`). Régions du CSS : `grep -n 'RÉGION' index.html` ; titres de blocs : `/* =====`, `/* ---`. Le contenu d'un chapitre se cherche dans `chapitres/<id>.html` (`grep -rn … chapitres/`).
- `fichier de départ/` = original intact, **non versionné** (voir `.gitignore`).
- Aucun build : édition directe (autour : `sw.js`, `manifest.webmanifest`, `vendor/`, `tools/`, `tests/`, `docs/`).

### Pilotage data-driven

Le tableau **`CHAPTERS`** (`grep -n 'const CHAPTERS = \['`) est la source de vérité. **184 chapitres** : physique 56, maths 49, SI 43, info 17, anglais 19 (dont 62 de 2ᵉ année). Entrée à 11 champs :

```js
{ id:'rlc', prefix:'rlc', name:'Circuit RLC série',
  matiere:'physique', sub:'ondes', subLabel:'Ondes & signaux', domain:'ondes',
  matiereLabel:'Électrocinétique',
  panels:['cours','meth','simu','flash','exos'], drawFn:'drawSim',
  mobLabel:'Circuit RLC série' }
```

- `matiere` ∈ `physique` | `maths` | `si` | `info` | `anglais`. Les chapitres `physique/maths/info/anglais` vivent dans le grand `<main>` ; `si` a son propre `<main id="si-content">` (masqué au départ).
- **Ajouter une matière** = l'ajouter aux énumérations en dur : intercalaires `.mob-mat-btn.mat-tab` de la navigation (HTML), zone `.mat-content[data-mat-content="X"]`, `buildSidebars` (`['physique',…]`), `buildChapData` + `const MATS` (navigation), les **8 tables de noms** `{ physique:'Physique', … }` (`grep -n "physique:'Physique'"` : fiche de révision `FLASH_MAT_NOMS`, recherche, impression, navigation, Bilan, cartes signalées, Aujourd'hui, PAGE CHAPITRE) et la table `MATIERES` de `assistant/assistant.js`, `NOMS`/`MATS` d'Aujourd'hui, puce `qc-<matière>` (avec `data-mat`) du quiz (HTML + listes JS : `grep -n 'qc-physique'`), `perMat` du **Bilan**, jetons `[data-mat="X"]` (région JETONS, bloc clair **et** bloc sombre, **et** leur copie du filet de sécurité Auto), variable `--<matière>` (+ `-fond`, `-vif`). Les couleurs viennent toutes des jetons `data-mat` (plus de `colorsMap` ; `.flash-mat-*`, `.quiz-chapter-badge.*`, `.mt-*` ne sont plus stylés).
- **Anglais** : cartes en **texte brut** (`isPlainDeck` ; quiz : `item.meta.mat === 'anglais'`), sans `flashPretty` ; `<strong>`/`<em>`/`<br>` possibles ; panels typiques `['cours','flash']`. `window.__TTS` est défini AVANT les decks (`makeFlash` teste `__TTS.ok`) ; depuis le 2026-11-26 (point 9), il lit une face **par morceaux**, chacun avec sa voix (`__TTS.lecture(texte, autreFace)`, `detectLang(texte, autreFace)` : indices par mot, infinitifs en -er/-ir sauf `EN_ER`, citation « … », autre face de la carte) ; test `site` › « lecture audio ». Détail : `docs/interface.md` › « Cartes d'anglais et d'informatique », « Lecture audio » ; contenu : `docs/historique-contenu.md` › « Anglais ».
- **Informatique** : cartes rendues par **`flashInfoHTML`** (`isInfoDeck` ; quiz : `item.meta.mat === 'info'`) : texte tel quel, aucune mise en forme mathématique automatique ; `` `code` `` → `<code>`, formules en `\( … \)`. Toute nouvelle carte d'informatique marque ainsi son code et ses formules. Cours : bloc « AU PROGRAMME · INFORMATIQUE », code affiché exécuté et testé, annexe Python du programme limitative (`docs/historique-contenu.md` › « Informatique »).
- `drawFn` : fonction du simulateur (31 chapitres), ou `null`.
- `CHAPTERS_BY_ID` / `CHAPTERS_BY_PREFIX` sont dérivés automatiquement (après le tri).
- `validateChaptersCoherence()` (IIFE) alerte dans la console au chargement, mais ne compare que les ids de chapitre (`CHAPTERS` ↔ `div.chapter`).

### Ordre d'apprentissage (réorganisation centralisée)

- **`CHAP_GROUPS`** (`grep -n 'const CHAP_GROUPS'`, IIFE `reorderChapters` juste après `CHAPTERS`) = `[ [subCode, subLabel, [ids…]] , … ]` (30 groupes) : **source unique** de l'ordre pédagogique, des sous-domaines (`c.sub`) et de leurs libellés (`c.subLabel`) ; `CHAPTERS` est réordonné en place. `subCode` à `null` = pas de code (maths). Un `id` absent est rejeté en fin de liste. **Pour changer l'ordre ou le sous-domaine : éditer `CHAP_GROUPS`**.
- ⚠️ `matiereLabel` (tag) et `domain` (`data-domain`) ne sont **pas** réécrits : les tenir à la main en cohérence (ex. `lorentz` garde le tag « Mécanique »). Le code `'meca'` sert en physique ET en SI. Les couleurs ne dépendent plus de `domain` mais de `matiere` (`data-mat`). Groupes et tags : `docs/historique-contenu.md` › « Chapitres, groupes et tags ».
- **2ᵉ année** : `window.__YEAR2A` (62 ids) pilote badges « 2A », `data-year`, filtre d'année (clé `year`), surtitre imprimé. **Anglais**, `constantes` et `incertitudes` : visibles les deux années (règle en dur : `buildChapData`, `syncSidebar`, `__chapYear`). API : `window.__chapYear(c)` (0 = les deux années, sinon 1 ou 2), `window.__currentYear()`, `window.__inYear(c, y)` (préc./suiv. filtrés par année). Bilan et quiz : `window.__inRevision(c, y)` (1ʳᵉ année : 1ʳᵉ seule ; 2ᵉ année : les deux). Révisions du jour (`dueDeck`) : toutes années. Détail : `docs/interface.md` › « Années ».

### Rédaction des contenus

Ce qui a été fait : `docs/historique-contenu.md` › « Automatique », « Cours de 2ᵉ année », « Électromagnétisme de 1ʳᵉ année », « 1ʳᵉ année : audit », « Point 7 ». Inventaires programme ↔ chapitres : `docs/programme-pt/`.
- **2ᵉ année** : chaque cours commence par un bloc « AU PROGRAMME · PT » (sec-num sans §, `.reveal` « Programme officiel » listant les capacités exigibles du programme 2021, renvoyant aux §) ; hors-programme regroupé en fin de cours (« POUR ALLER PLUS LOIN · … »). Cartes : « Hors programme en PT (pour aller plus loin) : » en tête de la réponse, question inchangée.
- **1ʳᵉ année** : bloc « AU PROGRAMME · PTSI » ; garder les § existants (les vidéos y renvoient), nouvelles sections à la suite. Hors-programme signalé sur place : encadré « Hors programme en PTSI (vu en 2ᵉ année) » ou « (pour aller plus loin) », titre de la méthode ou de l'exercice, préfixe de la réponse d'une carte. Aperçus (`estat`, `fluides`, `fluiddyn`) : encadré « non exigible en PTSI ».
- Chapitres revus jusqu'ici : 6 à 10 méthodes, 7 à 12 exercices dont un « Concours PT ».
- **Notations communes** (harmonisées le 2026-11-15, point 3) : ξ amortissement (SI, maths), Q et τ = 2Q/ω₀ (oscillateurs en physique ; ξ = avancement en chimie), T_i/K_i (PI), « chaîne de puissance / moduler », E(X), V(X), binôme \(\binom{n}{k}\), ch, sh, A^⊤, rg, Δh₁₂ (enthalpie de changement d'état), S_éch / S_créée, K° avec c°, moments 𝓜 ; `flashPretty` rend droits rang, rg, ch, sh, Vect, Ker…
- Automatique : ξ, ω₀, ω_c0 (coupure à 0 dB de la FTBO), Mφ, M_G, écart ε. Électromagnétisme : \(\vec{\mathcal M}\), \(\vec\Gamma\), \(U_m\) (énergie magnétique), \(I_{\text{enlacé}}\), σ (conductivité).
- Dans les figures SVG, un vecteur s'écrit en **gras** (la flèche combinante U+20D7 n'existe dans aucune police du site et s'affiche en carré ; seules les cartes, converties en `\vec` par `flashPretty`, peuvent l'employer).

### Navigation : barres invisibles = couche de commande

- Les `.subdomain-bar` / `.chapter-bar` du HTML sont vides ; `buildSidebars` les remplit (`.sub-btn` / `.chap-btn`) **avant** l'attachement des handlers. Invisibles : `.chap-btn`/`.tab` = **couche de commande cachée**. Seule navigation visible : **`#mob-drawer`** (barre latérale ≥ 1200 px, tiroir, page « Chapitres » au téléphone).
- Colonne de lecture : **`<article id="app-main" role="none">`**, jamais un `<div>` ni un `<section>` (les `</div>` / `</section>` orphelins du contenu le refermeraient).
- **Seul le handler `.chap-btn`** (`grep -n 'CHAPTER SWITCHING'`) bascule entre le `<main>` principal et `#si-content`. Détail : `docs/interface.md` › « Couche de commande ».

→ Naviguer **toujours** via `navigateTo('chap-<id>','<prefix>-<onglet>', cb)` ou un clic sur `.chap-btn`/`.tab`, jamais en posant `.active` à la main. Ne pas supprimer ces barres, et **ne pas ajouter de `.chap-btn` dans le HTML** (effacés par `buildSidebars`).

**Ajouter un chapitre = 6 endroits** (gabarit : `GABARIT-CHAPITRE.md`) : (1) entrée `CHAPTERS` ; (2) id dans `CHAP_GROUPS` ; (3) id dans `__YEAR2A` si 2ᵉ année ; (4) bloc DOM `chap-<id>` dans le bon `<main>`, panneaux Cours / Méthodes / Exercices **vides** ; (5) leur contenu dans `chapitres/<id>.html` ; (6) `const <prefix>Cards` + `makeFlash(...)` **après** les constantes `FLASH_*` (`grep -n 'const FLASH_FR2'` ; avant, TDZ → plantage). Puis `node tools/chapitres.js` (voir Architecture).

### Routage par URL (deep-link + bouton précédent)

`urlRouting` synchronise `location.hash` (`#chapId/onglet`, ex. `#rlc/cours`) : `pushState` au changement de chapitre, `replaceState` au changement d'onglet ; au chargement, un `#hash` passe avant `lastPos` ; `popstate` rejoue. `#sommaire/<matière>` : Sommaire de la matière. Retour Android (liste `PAGES`) : `docs/interface.md` › « Routage et retour Android ».

## Conventions de nommage des IDs (IMPORTANT)

- Le `<div>` du chapitre : `id="chap-<id>"` (ex. `chap-rlc`).
- **`id` ≠ `prefix`** pour **163 chapitres sur 184** : le `prefix` sert aux panels et aux flashcards.
  Ex. chapitre `id:'ondes'` → panels `ond-` ; `id:'rlc'` → panels `rlc-`. **Construire un id de panneau avec `CHAPTERS_BY_ID[id].prefix`**, jamais `id+'-cours'`.
- Panels : `<section class="panel" id="<prefix>-<panel>">` avec `<panel>` ∈ `cours` | `video` | `meth` | `simu` | `flash` | `exos` (`video` : onglet « Vidéos », rempli par la table `window.__VIDEOS`, voir « Cours vidéo »).
- Onglets : `<button class="tab" data-panel="<prefix>-<panel>">`.
- Bouton de commande (généré, invisible) : `<button class="chap-btn" data-chap="<id>">`.
- Les IDs du chrome (`#search-btn`, `#study-btn`, `#theme-btn`, `#more-btn`, `#mob-*`, overlays…) sont lus par le JS **et** par les tests : les garder.

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

- Les `<span class="num">01</span>` restent, **masqués** (libellés réécrits par le module PAGE CHAPITRE). Classes de contenu : `.course-section`, `.sec-num`, `.intro`, `.formula`, `.def-box`, `.prop-box`, `.method-box` (étapes `<span class="step">`), `.notice`, `.reveal`. Exercices : `.exo` **dans** `.exo-wrapper` (exo « CONCOURS PT » `.exo.concours` compris, sans `</div>` en plus).
- **Page chapitre** (module « PAGE CHAPITRE ») : la feuille est le `.chapter` lui-même (`overflow:clip`, jamais `hidden` : les onglets collent) ; intercalaire, onglets ARIA, rail `aside#chap-rail`, pied `#chap-pager` : `docs/interface.md` › « Page chapitre ».
- **Deux `.chapter.active`** au départ (`chap-rlc`, `chap-ingsys`) : chapitre **visible** = filtrer par `offsetParent`.

### Contenu (région CONTENU + module « CONTENU », SPEC §5.2, §5.3, §7.2, §7.3)

Module paresseux et idempotent (`grep -n '===== CONTENU : enrichissements'`) ; il ne modifie jamais le texte lu par la recherche, le sommaire ou l'impression. Pour écrire du contenu :
- encadrés : intitulés **générés en CSS** (ne pas les écrire dans le HTML) ;
- `.formula` : `data-nom="…"` = nom de la formule (marge, Formulaire, recherche) ;
- notations « X_y » hors formule : préférer `\( V_m \)` (`python3 tools/validate.py --souligne` les liste) ;
- figures : SVG aux couleurs du thème (`.svg-*`, `.lab-*`) ; images en niveaux de gris : `.px-fond`, `.px`, aucune couleur en dur ;
- exercices : filtres par **`.filtre-masque`** (jamais `hidden` : l'impression garde tout) ; libellé « Voir la solution » fixe.

Détail : `docs/interface.md` › « Module CONTENU ».

### Simulateurs (région SIMU, SPEC §5.5)

DOM uniforme (`.sim-wrapper`), mis en page **sans toucher au HTML**. Nouveau simulateur (gabarit : `GABARIT-CHAPITRE.md`) : hauteur de toile par `--h` (région SIMU) ; courbe principale `__CVchap(canvas)` ; libellés **≥ 12 px** ; grandeurs `__grandeur(ctx, 'u_C / U_0', x, y)` (indice d'**un seul caractère** : `'M_f_z'`) ; nombres par `window.__nb(x, déc)` ; liseré en `outline`, pas de bordure. Détail : `docs/interface.md` › « Simulateurs ».

## Formules : deux conventions distinctes

- **Cours / méthodes** : LaTeX via MathJax. Inline `\( … \)`, bloc `$$ … $$` (**pas** `\[ … \]`). Pas de « < » collé à une lettre dans une formule (lu comme une balise : `\lt`, contrôlé par `validate.py`). Pas de macro d'extension absente (`\cancel`, `\ce`, `physics`…). Éviter les longues formules en ligne : `$$` dans `.formula` (qui défile au besoin).
- **Flashcards** : par défaut en **caractères Unicode** (`ω₀`, `√(LC)`, `e^(iθ)`, `≤`) ; `flashPretty()` repère les fragments mathématiques, les convertit en LaTeX et les enrobe dans `\( … \)`. Une carte écrite en `\( … \)` est **admise** et laissée intacte (1 287 cartes) : dès qu'un champ contient `\(`, il est laissé **entier** à MathJax, y écrire alors toutes les formules en `\( … \)` (antislash doublé dans la chaîne JS : `\\(`). ⚠️ Séparation maths/texte **heuristique** : une carte mêlant phrase et formule peut demander une réécriture directe en `\( … \)`. Restent hors des formules (2026-11-26) : ordinaux « 1er », « 2e » (`FLASH_ORDINAL`), sigles et unités en lettres « BO », « FT », « PI », « dB » (`FLASH_SIGLES`), « du », « va »… en minuscules (`FLASH_FR2_MIN`), « correcteur I », parenthèses de la phrase ; test `site` › « ordinaux, sigles ». Détail : `docs/interface.md` › « Formules des cartes ».

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

- 184 decks, 6 303 cartes. `makeFlash` (`grep -n 'function makeFlash'`) range le deck dans `window.FLASH_REGISTRY[prefix]` et l'instance dans `window.FLASH_INSTANCES[prefix]`. Champ facultatif **`cat:'form'|'val'`** (1 822 cartes). API : `docs/interface.md` › « État et registre ».
- **État et identifiants de cartes** (`grep -n 'ÉTAT DES FLASHCARDS'`) — **INTOUCHABLE** : `flash:<prefix>` reste un tableau d'états `{h,o,e,last,box,due}` **aligné par position** (Bilan, `srsCountDue`, quiz, badge, rail « Mes cartes » le lisent par index) ; `flashids:<prefix>` mémorise l'identifiant de chaque position, `flashCardIds(cards)` = `'Q|R'` (empreintes FNV-1a de la question et de la réponse). `flashLoadState(prefix, cards)` **réaligne l'état par identifiant** ; `flashSaveState(prefix, cards, state)` écrit toujours les deux clés ensemble. **Migration au chargement** : chaque `makeFlash` réécrit l'état si l'ordre ou les identifiants ont changé (état « hérité » sans identifiants : conservé par position). `rate()`/`getProgress()` relisent le Store, et `quizRate` appelle `FLASH_INSTANCES[prefix].reload()` : quiz et onglet Cartes ne s'écrasent plus. La refonte n'a rien changé à cet état (vérifié octet pour octet sur une session de notation scriptée).
- **Règle d'édition des decks** (règle exacte : en-tête de `flashLoadState`). **Sans perte** : ajouter/retirer/réordonner des cartes ; **toute retouche de texte** (question et/ou réponse, remplacement global compris) à longueur et ordre inchangés (repli par rang : jamais pire que l'ancien appariement par position), **sauf** pour une question présente en double dans le paquet (n'en retoucher qu'une copie par mise à jour) et une réponse passée d'une carte à une autre dont les questions sont aussi retouchées ; question reformulée, réponse inchangée, gardant son rang depuis sa voisine reconnue précédente **ou** suivante (même si cette voisine a été déplacée), ou entourée d'autant de cartes retirées que de cartes ajoutées. **Carte remise à zéro** : question retouchée hors de ces cas (réponse aussi changée alors que des cartes sont ajoutées/retirées entre ses voisines — sauf autant d'ajouts que de retraits, voir la contrepartie —, carte retouchée **et** déplacée, rang changé des deux côtés), ou ambiguïté (deux candidates de même réponse). **Contrepartie** : entre deux voisines reconnues, autant de cartes nouvelles/retouchées que de cartes disparues → celles dont la réponse ne désigne pas une seule entrée prennent l'entrée de même rang : une carte ajoutée (ou retouchée et déplacée) à la place d'une disparue hérite de son état, et une carte à question **et** réponse retouchées côtoyant un retrait + un ajout peut recevoir l'état de la carte retirée (et la carte ajoutée, le sien). Prévenir l'utilisateur. `flagged` : réaligné par question **et** réponse, puis question seule ; question introuvable : garde son index, orpheline (`i:-1`, listée mais ne marque aucune carte) si cet index est pris par un autre signalement.
- Fiche de révision (DOM construit au **premier affichage** du deck) et raccourcis des cartes : `docs/interface.md` › « Fiche de révision », « Raccourcis des cartes ».

## Stockage

- **`Store`** (`grep -n 'const Store = (function'`) : wrapper `localStorage` avec repli en mémoire ; `get/set`, `getJSON/setJSON`, `available()` (pas de `remove`). Toujours `Store`, jamais `localStorage` (exceptions : la Sauvegarde, le script du `<head>`).
- **Clés** (détail : `docs/interface.md` › « Stockage ») : `flash:<prefix>` (progression), `flashids:<prefix>` (identifiants de cartes), `theme` (`light` | `dark` | `auto`, absente = `auto`), `lastPos` (`{chap, panel, t, s}`), `year` (1 ou 2), `recents` (8 derniers), `pinned` (8 au plus), `drawerCollapsed` (parties repliées, `mat|subLabel`), `flagged` (`{p,i,q,a,t}`), `quizConfig` (`{mats,mode,nb,type}`), `readScale` (0-2), `yearAuto` (`'1'` = 2ᵉ année atteinte automatiquement), `navCollapsed` (`'1'` = barre latérale repliée), `assistant` (`'1'` activé, `'0'` retiré).
- Le jeton d'accès de l'assistant (phase 1) ne sera **jamais** une clé Store ni `localStorage` exportée. Toute nouvelle clé est exportée par la Sauvegarde : l'ajouter ici, et **ne pas la faire commencer par `flash:`** (préfixe qui compte les chapitres avec progression ; d'où le nom `flashids:`).
- **Leitner** : `srsSchedule(state, level)` met à jour `box` et `due` à chaque notation (`SRS_INTERVALS` = [0,1,3,7,16,35,75] jours), dans `makeFlash.rate` **et** `quizRate` ; `srsIsDue(s)`/`srsCountDue()` comptent les dues (boutons : `docs/interface.md` › « Réviser : boutons et compteurs »).
- **Sauvegarde** (`#backup-overlay`) : export de toutes les clés du `localStorage` (origine `thomasmareel.github.io` partagée) ; import en fusion, `flash:X`/`flashids:X` traités par paire (`docs/interface.md` › « Sauvegarde »).

**Écrans** : `docs/interface.md` › « Navigation des chapitres », « Barre du téléphone et feuille ⋯ », « Sommaire de la matière », « Sommaire du chapitre », « Quiz », « Bilan », « Aujourd'hui », « Fenêtres, recherche et toasts », « Défilement ».
- Navigation (`grep -n 'NAVIGATION DES CHAPITRES'`) : construite paresseusement, modifiée sur place ; tiroir modal par `aria-hidden="true"` sur `#app-main` (jamais `inert` ; `grep -n 'const ARRIERE_PLAN'`).
- Barre `#mob-header.mbar` : effacée par `translateY(-100%)`, jamais `visibility:hidden` ; `--bar-h-reel` jamais sur `<body>` ni `<html>`.
- `#sommaire-matiere`, `#today-overlay` (liste `IDS` du focus : `grep -n 'var IDS = \['`), `#quiz-overlay` (IDs d'origine gardés), `#dash-overlay`. Changement de chapitre : retour en haut (`scrollPageTop()`) ; d'onglet : `DEFIL_ONGLETS`.
- **Fenêtres** `.fen` : classe **`.open`** + fermeture par **Échap** (le retour d'Android en dépend), ids des boutons inchangés. Recherche : `grep -n 'RECHERCHE GLOBALE'`.

## Dépendances : tout en local (aucun CDN)

Le site est **100 % autonome** — aucune requête externe, fonctionne hors-ligne (vérifié par les suites `site` et `pwa`).

- **MathJax 3.2.2** local (`vendor/mathjax/tex-mml-chtml.js`, sans extensions, polices `woff-v2`), référencé dans l'en-tête ET le template d'impression. Pas de `fontPath`. **`chtml.scale: 1.07`** (page ET gabarit d'impression).
- **Typeset paresseux** : seul le panneau visible est rendu, les autres à l'ouverture de leur onglet (`typesetPanel(panel)`, idempotent). Tout panneau à formules doit être atteint par un onglet, sinon appeler `typesetPanel`. ⚠️ Pas d'attribut `data-mjx…` sur un conteneur (panneau jamais rendu).
- Dans `startup.ready()` : **re-rendu sans doublon** (`findMath` de l'entrée MathML ignore les `<math>` d'un `mjx-container`, page et gabarit d'impression) et **correctif `\text{…}` de largeur nulle** (`grep -n 'largeur nulle'`). Ne pas retirer.
- `\oiint` : macro `tex.macros.oiint` (∯), page **et** gabarit d'impression ; pas de `\unicode{…}` (extension absente).
- **Polices** : Source Serif 4, Source Sans 3, JetBrains Mono (`vendor/fonts/`, `vendor/fonts/polices.css`, page ET gabarit d'impression). Dans le CSS et les `style="…"`, **toujours** `var(--font-text)`, `var(--font-ui)`, `var(--font-code)` ; noms réels seulement dans les `ctx.font` des canvas (`"Source Sans 3"`, `"Source Serif 4"` entre guillemets, `JetBrains Mono`) et les règles visant du texte SVG. Fraunces et Inter Tight (anciennes polices) ont disparu du dépôt : ne pas les réintroduire.
- **Impression** : `printChapter()` → `window.__imprimerDocument({…})` (`grep -n 'function imprimerDocument'`), thème clair forcé, feuille CHTML recopiée (`#print-mjx-styles`, sans elle formules invisibles), Ctrl+P intercepté. Test : `regressions` › B5.
- Détail et mises à jour : `docs/interface.md` › « MathJax », « Polices », « Impression ».

## PWA (installable + hors-ligne sur mobile)

- `manifest.webmanifest` + `sw.js`, enregistré en fin de `<body>` (`grep -n 'serviceWorker.register'`), **uniquement en http/https**.
- `sw.js` précache la coquille (`PRECACHE`, 45 entrées) ; HTML en stale-while-revalidate ; **assets en cache-d'abord, jamais rafraîchis sans bump**. Chapitres (`chapitres/<id>.html?v=<empreinte>`, `recherche.json?v=…`) : cache à part **`ptsi-chapitres`**, gardé d'une version à l'autre (une mise à jour ne retélécharge que les chapitres modifiés), rempli en arrière-plan par la page (un fichier à la fois, jamais en économie de données : hors ligne complet), versions périmées retirées.
- Pas de `skipWaiting()` automatique : après un bump, bannière « Nouvelle version disponible — Recharger ».
- ⚠️ **Bump OBLIGATOIRE** : à chaque commit **publié** modifiant un asset mis en cache (index.html inclus), **incrémenter `CACHE_VERSION`** en tête de `sw.js` (`ptsi-cache-vN` → `vN+1`) **dans le même commit** : bannière, rafraîchissement des assets, purge des anciens caches, cohérence HTML/assets. (Branches de travail `wip/…` : bump unique au moment de la publication.)
- Ajout/retrait d'un fichier de `vendor/` ou `icons/` → mettre à jour `PRECACHE` (la suite `pwa` vérifie que chaque fichier listé existe).
- Tests : `serviceWorkers:'block'` hors suite `pwa`. Détail (icônes, mise à jour, 1ʳᵉ visite) : `docs/interface.md` › « PWA ».

## Déploiement (GitHub Pages)

- Servi par **GitHub Pages** depuis `main` (`https://thomasmareel.github.io/revisions-ptsi/`), workflow Actions `.github/workflows/deploy-pages.yml` à chaque push. Chaque push doit donner un run `completed success`.
- Vérifier : dans le cloud, outils GitHub MCP (`actions_list`, owner `thomasMareel`, repo `revisions-ptsi`, workflow id `283713397`) ; sous Windows, `gh run list --repo thomasMareel/revisions-ptsi --limit 5`.
- ⚠️ **Ne PAS se fier à `pages/builds/latest` ni à `pages-build-deployment`** (ancienne pipeline Jekyll figée). Le vrai état = les **runs Actions**.
- ⚠️ **`.nojekyll` à la racine : le garder, ne jamais le supprimer** (filet de sécurité si Pages repassait en « Deploy from a branch »). Détail : `docs/interface.md` › « Déploiement ».

## Outils

- `tools/validate.py` (ou `npm run valider`) : 8 contrôles (ids, IDs dupliqués, `makeFlash`, `drawFn`, « < » collé à une lettre, `\[ … \]`, contenu dans `chapitres/<id>.html` et panneaux vides dans `index.html`, données dérivées à jour), sur `index.html` **et** les fichiers de chapitre → `[OK]` ou exit ≠ 0. **Angles morts** : équilibre des balises, couverture de `CHAP_GROUPS`/`__YEAR2A`, export `window.drawX`, ids des simulateurs (suite `site`).
- `node tools/chapitres.js` (données dérivées ; `--verifier` n'écrit rien ; extraction : `tools/extraction-chapitres.js`, rejouée par la suite `site`). `tools/check_js.py` → `blocs en erreur: 0` (20 blocs) ; `node --check assistant/assistant.js` à part. Couverture CSS : `docs/refonte/travail/couverture.py index.html`.
- `tools/tag_formulas.py`, `tools/migrate_canvas_colors.py` : réécrivent `index.html` en place. **Ne pas les lancer sans raison ni accord.**
- `tools/pre-commit` + `tools/install-hooks.sh` : **non installé par défaut**, le proposer, pas d'office. Détail : `docs/interface.md` › « Outils ».

## Tests navigateur (`tests/`)

Batterie Playwright + Chromium : sert le site sur un petit serveur local et le parcourt comme un utilisateur, sans jamais modifier `index.html`. Mode d'emploi (installation Windows/Linux, options, rapport, ajout d'un test) : **`tests/README.md`**.

- `npm test` = toute la batterie (≈ 60 min dans le conteneur en novembre 2026) ; `npm run test:rapide` (≈ 8 min). `node tests/run.js --suite=…`, `--chapitres=rlc,slci`, `--strict`, `--delai-chapitres=300` (chaque chapitre chargé 300 ms plus tard : erreurs de synchronisation), `--aide`. Ne pas lancer deux suites lourdes (site, mobile, assistant : chacune garde les 742 onglets rendus dans une seule page) en même temps : essayé le 2026-11-26, le navigateur plante faute de mémoire (16 Go). Sortie 0 = OK, 1 = échec.
- Suites : `site`, `mobile`, `interactions`, `pwa`, `regressions` (B1 à B5), `assistant`, `visuel` (26 écrans, clair et sombre, ordinateur et téléphone). **La refonte vise `visuel --strict` vert** : tout nouveau style doit passer sans liste tolérée. Contenu des suites et écriture d'un test : `docs/interface.md` › « Tests ».
- **Quand les lancer** : **avant chaque commit touchant `index.html`**, en plus de `validate.py` et `check_js.py` — au minimum `npm run test:rapide` + la suite concernée ; la batterie complète avant un commit important. `regressions` doit rester verte.
- **Anomalies tolérées** : `DEBORDEMENTS_CONNUS` (`tests/suites/mobile.js`, vide), `TEX_EN_CLAIR_CONNUS` et `ONGLETS_HORS_CHAPTERS_CONNUS` (`tests/suites/site.js`), `TOLERES` (`tests/suites/visuel.js` ; après une correction voulue, recopier la proposition de `visuel.md`, à relire). Une anomalie corrigée doit être retirée de sa liste (un avertissement `!` le rappelle). Ne jamais affaiblir ni supprimer une vérification pour faire passer un test.
- **Conteneur Claude Code** : Playwright 1.56.1 global (`NODE_PATH=/opt/node22/lib/node_modules`), Chromium dans `/opt/pw-browsers` ; **ne pas lancer `npm install` ni `npx playwright install`**. Bash coupe à 10 min : batterie complète en arrière-plan, sortie dans un fichier. Polices Latin Modern installées (`/usr/share/texmf/fonts`) : lancer avec un `FONTCONFIG_FILE` qui les exclut (`docs/interface.md` › « Tests »).

## Identité visuelle : refonte « Cahier de prépa » (octobre 2026)

- **Référence** : `docs/refonte/conception/SPEC.md`, `tokens.css`, `composants.css`, maquettes.
- **Icônes** : `window.__icon(name)` (script juste après le sprite, AVANT les decks : `makeFlash` l'utilise). **Focus** : `window.__focusables(conteneur)` (jamais `[href]` seul), `window.__repliFocus(el)`, `window.__rendreFocus(op, repli)`. Focus jamais caché sous les barres collantes (`grep -n 'Focus jamais caché sous les barres'`) ; **pas de `scroll-padding-top` sur `<html>`**. Détail : `docs/interface.md` › « Identité visuelle ».
- **Ne pas faire** (SPEC §9 et décisions de l'utilisateur) :
  - poser `overflow:hidden` sur `html`, `body` ou un ancêtre des barres collantes (casse `position:sticky`) : utiliser `overflow-x:clip` ;
  - utiliser `--border` ou `--surface` (alias de compatibilité) dans du nouveau code : `--line-2`, `--sunk` ;
  - coder une couleur en dur (seule exception : les mini-vues du sélecteur de thème) ;
  - remettre une **barre fixe en bas** sur téléphone ;
  - réintroduire le **sommaire en puces** sur téléphone ;
  - **ouvrir « Aujourd'hui » au lancement** (le site s'ouvre sur le dernier chapitre consulté ; entrée manuelle seulement) ;
  - remettre un **anneau de %** dans la navigation (il reste dans le Bilan) ;
  - écrire un texte sous 13 px (12 px seulement en gras, pour les compteurs et pastilles, `--fs-count`) ou une cible de moins de 44 × 44 px au doigt ;
  - envelopper la colonne de lecture dans un `<div>`/`<section>` (voir `#app-main`) ;
  - écrire un `@media (prefers-color-scheme)` hors du filet de sécurité des jetons.
- **Points de retour** sur origin : branches `sauvegarde-avant-lot3` (`9e16255`), `sauvegarde-avant-finitions2` (`b1d2a25`), `sauvegarde-avant-pt-spe`, tag `v1.0` ; la refonte vit sur `wip/refonte` jusqu'à sa publication (point de retour `sauvegarde-avant-refonte` à créer à ce moment-là). Rollback (uniquement sur demande explicite) : `git reset --hard <branche> && git push --force origin main`.

## Anomalies connues (à traiter avec validation utilisateur)

Liste par gravité : **`docs/audit-2026-09.md`** ; audit du 2026-11-14 : **`docs/audit-2026-11.md`**. Principales restantes : aucune anomalie ouverte de cette liste (voir l'audit pour le contenu). Correctifs passés : `docs/interface.md` › « Anomalies corrigées ». Non-bug : les deux `.chapter.active` du HTML source (`chap-rlc`, `chap-ingsys`), un par `<main>`.

## CSS : régions, jetons, thème

- **Régions** (`grep -n 'RÉGION' index.html`), ordre de la cascade : JETONS, BASE, COQUILLE, PAGE, CONTENU, SIMU, REVISION, FENETRES, IMPRESSION. Chaque règle va dans **une seule** région, celle de son sujet (composante la plus à droite du sélecteur ; `:root[data-theme="dark"] X` va avec X) ; chaque région a ses propres blocs `@media`. Une région plus bas l'emporte à spécificité égale : pour battre une règle d'une région plus bas, jouer sur la spécificité, pas déplacer la règle. Aucun `<style>` hors du grand bloc. Détail : `docs/interface.md` › « CSS ».
- **Jetons** (région JETONS = `tokens.css` de la refonte) : `data-mat="<matière>"` définit l'encre `--chap`, `--chap-fond`, `--chap-vif`. Anciens noms gardés comme alias (`--ink`, `--paper`, `--accent`…) ; nouveau code : les nouveaux noms (jamais `--border`/`--surface`). Les blocs JETONS et BASE sont le socle : ne pas y redéfinir de jeton depuis une autre région (besoin local : propriété personnalisée dans sa région).
- **Thème sombre** : `:root[data-theme="dark"]` est le seul sélecteur du sombre pour les composants. Seule exception : le filet de sécurité (bloc sombre des jetons recopié **à l'identique** sous `@media (prefers-color-scheme: dark)`). Ne pas écrire d'autre `@media (prefers-color-scheme)` ; retoucher les deux copies ensemble. Préférences (clé `theme`) : Clair, Sombre, Auto (défaut) ; module THÈME : `grep -n 'function applyTheme'` (local à une IIFE). API : `window.__themePref()`, `window.__setTheme('light'|'dark'|'auto')`.
- **Couleurs des simulateurs et schémas** : variables de thème, **jamais une couleur codée en dur** ; sur fond coloré, `var(--sheet)` plutôt que `#fff` ; côté canvas, **`__CV()`**, **`__CVA('accent', 0.4)`**, **`__CVchap(canvas)`** ; une nouvelle variante de badge (région SIMU) prend ses couleurs des jetons.
