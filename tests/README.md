# Tests navigateur — Révisions PTSI

Cette batterie de tests **ouvre le site dans un vrai navigateur** (Chromium,
piloté par [Playwright](https://playwright.dev)) et vérifie automatiquement
qu'il fonctionne : chaque chapitre, chaque onglet, les formules, les
simulateurs, la version mobile, le quiz, la sauvegarde, le mode hors-ligne…

Elle ne modifie **jamais** `index.html` : elle le lit, le sert sur un petit
serveur local le temps du test, puis s'arrête.

> À lancer **après chaque modification importante** de `index.html`, en plus
> de `python tools/validate.py` (qui, lui, ne regarde que le code source).

---

## 1. Ce que vérifient les suites

| Suite | Ce qui est vérifié | Durée (complète / `--rapide`) |
|---|---|---|
| `site` | chargement sans erreur JavaScript ; **aucune requête externe** (site 100 % autonome) ; `CHAPTERS` cohérent avec le DOM ; **tous les chapitres × tous leurs onglets** : panneau affiché, 0 erreur MathJax, aucun `\(` `$$` resté en clair ; toutes les flashcards passées par MathJax ; **tous les simulateurs** exécutés et dessinés en thème clair **et** sombre | ≈ 6 min / ≈ 40 s |
| `mobile` | téléphone 390 px : en-tête, tiroir des chapitres, filtre, bouton thème ; **débordement horizontal** de chaque panneau (une liste de débordements *déjà connus* est tolérée) | ≈ 3 min / ≈ 15 s |
| `interactions` | lien direct `#chapitre/onglet`, boutons précédent/suivant du navigateur, boutons ‹ ›, passage vers la SI, recherche, flashcards + répétition espacée, quiz, « Réviser », Bilan, Aujourd'hui, formulaire, cartes signalées, calcul mental, impression, thème, **sauvegarde export puis import** | ≈ 30 s |
| `pwa` | `sw.js` (fichiers du précache présents), manifeste, service worker activé, cache rempli, **rechargement hors-ligne** | ≈ 10 s |
| `regressions` | un test par correctif **B1 à B4** : notes du quiz conservées par les flashcards, même localStorage plein (puis de nouveau disponible) et même quand le quiz tourne dans un autre onglet (B1) ; progression qui suit ses cartes quand un deck change (B2 : un état distinct pour **chaque** carte, contrôlé carte par carte) — carte insérée, retirée, déplacée ; question reformulée (sur place, suivie d'une insertion, après retrait de la précédente, à côté d'une carte déplacée, entre une carte retirée et une carte ajoutée) ; cas ambigu (deux entrées candidates de même réponse → carte vierge) ; question **et** réponse retouchées sur place, deck entier réécrit (état conservé) ; carte remplacée sur place (hérite de l'état de l'ancienne) ; question en double (réponses différentes ou doublon exact) —, `quizRate` sur un état ancien non migré, import d'une ancienne sauvegarde, cartes signalées (y compris sur une question en double, et signalement devenu orphelin) ; t₅% et palier du simulateur SLCI (B3) ; couleurs des simulateurs en thème sombre (B4) | ≈ 3 min |

Les durées sont indicatives (mesurées dans un conteneur Linux à 4 cœurs : batterie
complète ≈ 18 min, `--rapide` ≈ 4 min 30 s).

---

## 2. Installation (une seule fois)

Il faut **Node.js 18 ou plus récent** (version « LTS » conseillée).

### Windows

1. Installer Node.js depuis <https://nodejs.org> (bouton « LTS », options par défaut).
2. Ouvrir un terminal **dans le dossier du dépôt** : dans l'Explorateur de
   fichiers, ouvrir le dossier `revisions-ptsi`, puis clic droit dans le vide →
   « Ouvrir dans le Terminal ». (Ou, dans PowerShell : `cd "C:\chemin\vers\revisions-ptsi"`.)
3. Taper, l'une après l'autre :

   ```
   npm install
   npx playwright install chromium
   ```

   La 1re commande installe Playwright dans un dossier `node_modules/`
   (ignoré par git) ; la 2e télécharge le navigateur de test (≈ 150 Mo).

### Linux / macOS

```
cd revisions-ptsi
npm install
npx playwright install chromium
```

(Sous Linux, si Chromium refuse de démarrer faute de bibliothèques système :
`npx playwright install --with-deps chromium`.)

---

## 3. Lancer les tests

Toujours depuis le dossier du dépôt :

| Commande | Effet |
|---|---|
| `npm test` | **toute** la batterie (≈ 18 min) |
| `npm run test:rapide` | version courte : une dizaine de chapitres couvrant les 5 matières + tous les simulateurs dans un seul thème (≈ 4 min 30 s) |
| `npm run valider` | le validateur Python `tools/validate.py` (quelques secondes, sans navigateur) |

Pour passer des options, soit `node tests/run.js <options>`, soit
`npm test -- <options>` (les deux tirets sont obligatoires avec npm) :

| Option | Rôle | Exemple |
|---|---|---|
| `--rapide` | échantillon de chapitres, simulateurs en thème clair seulement | `node tests/run.js --rapide` |
| `--suite=nom[,nom]` | ne lancer que certaines suites (un nom inconnu, ou aucun nom, arrête le lancement) | `node tests/run.js --suite=site,mobile` |
| `--chapitres=id[,id]` | ne parcourir que ces chapitres (ids de `CHAPTERS` ; un prefix comme `og` ou `cpx` est accepté ; un nom inconnu arrête le lancement avec la liste des ids valides) | `node tests/run.js --suite=site --chapitres=rlc,slci` |
| `--racine=dossier` | tester un autre dossier que le dépôt (ex. une ancienne version) | `node tests/run.js --racine=../copie` |
| `--sortie=dossier` | où écrire captures et rapport (défaut `tests/sortie/`) | |
| `--visible` | ouvre une vraie fenêtre Chromium pour **voir** le test se dérouler | `node tests/run.js --suite=interactions --visible` |
| `--aide` | liste des options | |

---

## 4. Lire le résultat

Pendant le test, chaque contrôle s'affiche :

```
== Suite « site » — chargement, chapitres × onglets, MathJax, flashcards, simulateurs
     ok   CHAPTERS cohérent avec le DOM (chapitres, onglets, panneaux)
         .............x..........  (un point par chapitre, x = problème)
   ÉCHEC  chapitres × onglets : affichage, MathJax (526 panneaux)
          x cpx-meth : 1 erreur(s) MathJax (mjx-merror) : Missing close brace
     !    le panneau va-cours ne déborde plus : le retirer de DEBORDEMENTS_CONNUS
```

- `ok` : le contrôle est réussi.
- `ÉCHEC` : quelque chose ne va pas ; les lignes `x` en dessous disent **où**
  (chapitre, onglet, formule…) et **quoi**.
- `!` : simple avertissement, ne fait pas échouer (souvent : une anomalie
  connue a été corrigée, il faut mettre à jour une liste dans le test).

À la fin, un **résumé** donne `[OK]` ou `[ÉCHEC]` par suite, puis
`RÉSULTAT : TOUT EST OK` ou `RÉSULTAT : ÉCHEC`. Le programme se termine avec
le code 0 si tout passe, 1 si un test échoue, 2 si le test lui-même n'a pas
pu démarrer.

**Ctrl+C** arrête le lancement proprement : le navigateur et le serveur sont
fermés, le message « Interrompu (Ctrl+C) : aucun rapport écrit. » s'affiche,
aucun résumé ni `rapport.json` n'est produit (code 130). Les contrôles en
cours ne sont pas comptés en échec.

Dans `tests/sortie/` (ignoré par git) :
- `rapport.json` : tous les détails (chaque contrôle, chaque message, mesures) ;
- des **captures d'écran** (`site-accueil.png`, `mobile-tiroir.png`, `regressions-b3-slci-aperiodique.png`…).

---

## 5. Que faire en cas d'échec ?

1. **Lire le message** : il indique le chapitre (`rlc`), l'onglet (`rlc-cours`),
   la formule ou l'erreur JavaScript en cause.
2. **Relancer seulement ce qui échoue**, c'est bien plus rapide :
   `node tests/run.js --suite=site --chapitres=rlc`
3. **Regarder** : ajouter `--visible`, ou ouvrir les captures de `tests/sortie/`.
4. Ouvrir le site (double-clic sur `index.html`), aller sur le chapitre et
   ouvrir la console du navigateur (F12) : l'erreur y apparaît souvent.
5. Si c'est un **avertissement `!`** du type « ne déborde plus : le retirer de
   … », c'est une bonne nouvelle : supprimer la ligne indiquée dans le fichier
   de test cité.
6. Suite `regressions` en échec : un bug déjà corrigé (B1 à B4) est revenu —
   le message dit lequel. Les contrôles B2 suivent la règle d'appariement décrite
   en tête de `flashLoadState` (dans `index.html`) : si cette règle a été changée
   **volontairement**, adapter les scénarios B2a (`scenarios`), B2e et B2f.
7. Messages d'installation :
   - « Playwright est introuvable » → refaire `npm install` dans le dossier du dépôt ;
   - « Impossible de lancer Chromium » → `npx playwright install chromium`.
8. Sous Windows, si les accents s'affichent mal dans le terminal : utiliser
   « Terminal Windows » (ou taper `chcp 65001` avant de lancer les tests).

**Anomalies connues tolérées** (elles ne font pas échouer les tests, en
attendant d'être corrigées avec l'accord de l'utilisateur) :
- `tests/suites/mobile.js` → `DEBORDEMENTS_CONNUS` : 13 panneaux trop larges à 390 px (longues formules en ligne) ;
- `tests/suites/site.js` → `TEX_EN_CLAIR_CONNUS` (tableau de Routh en `\[ … \]`) et `ONGLETS_HORS_CHAPTERS_CONNUS` (simulateur de Lorentz non déclaré) ;
- suite `pwa` : le rechargement automatique à la 1re visite est signalé par un avertissement
  (l'écouteur `controllerchange` d'`index.html` recharge la page sans vérifier qu'un service
  worker contrôlait DÉJÀ la page ; or `clients.claim()` de `sw.js` déclenche cet événement dès
  la 1re visite).

---

## 6. Ajouter un test

### Un contrôle dans une suite existante

Chaque suite reçoit `ctx` (outils) et `res` (résultats). Exemple à ajouter
dans `tests/suites/interactions.js` :

```js
await etape('le bouton Bilan affiche un pourcentage', async () => {
  await page.click('#dash-btn');
  await pause(400);
  const texte = await page.evaluate(() => document.getElementById('dash-overlay').innerText);
  return [!/%/.test(texte) && 'aucun pourcentage dans le Bilan'];   // liste vide = OK
});
```

Ailleurs : `res.verifier('nom du contrôle', condition, ['message si échec'])`.

### Une nouvelle suite

1. Créer `tests/suites/<nom>.js` sur ce modèle :

   ```js
   'use strict';
   const { pause, attendreApp, naviguer } = require('../lib/outils');
   module.exports = {
     nom: '<nom>',
     description: 'ce que vérifie la suite',
     delaiMax: () => 5 * 60000,              // délai maximal (ms)
     async executer(ctx, res) {
       const { page, journal } = await ctx.nouvellePage();   // { mobile: true } pour un téléphone
       await page.goto(ctx.url('#rlc/cours'));
       await attendreApp(page);
       await naviguer(page, 'optgeo', 'flash');              // id du chapitre (pas le prefix « og ») + onglet
       const n = await page.evaluate(() => CHAPTERS.length);
       res.verifier('au moins 100 chapitres', n >= 100, n + ' chapitres seulement');
     },
   };
   ```
2. Ajouter `'<nom>'` à la liste `SUITES` en tête de `tests/run.js`.

### Outils disponibles

- `ctx.nouvellePage({ mobile, sw, largeur, hauteur })` : navigateur neuf (stockage vide),
  service workers **bloqués** par défaut (sinon le site se recharge tout seul à la 1re visite) ;
  renvoie `{ contexte, page, journal }` — `journal` collecte erreurs console, exceptions,
  requêtes externes ou en échec.
- `ctx.url('#id/onglet', { param: valeur })`, `ctx.capture(page, 'nom')`, `ctx.selectionner(chapitres)`
  (applique `--rapide` / `--chapitres`), `ctx.options`.
- `tests/lib/outils.js` : `attendreApp`, `naviguer`, `fermerOverlays`, `etatMathJax`,
  `extraireDeck` / `remplacerDeck` (lire ou modifier un deck de flashcards dans le HTML)…
- **Variante d'`index.html`** : `ctx.serveur.variantes.set('nom', (html, params) => htmlModifié)`,
  puis charger `ctx.url('#rlc/flash', { variante: 'nom' })`. Le fichier sur le disque n'est pas touché
  (exemple : `varianteB2` dans `tests/suites/regressions.js` : `{ variante: 'b2', op: 'retrait,edition', i: '5' }`
  retire la carte 5 de rlc puis reformule la suivante ; `op@k` vise l'index k ; opérations listées en tête du fichier).

### Pièges à connaître

- `CHAPTERS` (comme `CHAPTERS_BY_ID` et `CHAPTERS_BY_PREFIX`) est une constante
  globale « lexicale » : dans `page.evaluate`, écrire `CHAPTERS.length`, **pas**
  `window.CHAPTERS` (qui vaut `undefined`). `Store`, `navigateTo`, `getCanvasColors`,
  `flashPretty`… s'appellent aussi directement par leur nom.
- `applyTheme` n'est pas accessible : pour changer de thème, cliquer `#theme-btn`.
- Naviguer avec `naviguer(page, id, onglet)` (ou `location.hash = '#id/onglet'`),
  jamais en posant `.active` à la main.
- Attention `id` ≠ `prefix` : l'onglet Cours de `ondes` est `ond-cours`. Utiliser `CHAPTERS_BY_ID[id].prefix`.
- **Pas de hasard dans un contrôle** : l'ordre des flashcards est tiré au hasard (`buildOrder`), donc
  « noter 6 cartes au clic » ne note pas toujours les mêmes. Les contrôles B2 écrivent plutôt l'état de
  départ directement (`flashSaveState`, un état distinct et non vierge pour **chaque** carte) : une carte
  qui reprend l'état d'une autre, ou aucun, se voit à coup sûr.

### Vérifier qu'un test attrape vraiment le bug (mutation)

Copier le site dans un dossier temporaire **hors du dépôt**, y désactiver la règle testée dans
`index.html` (liens symboliques possibles pour `vendor/`, `icons/`, `sw.js`, `manifest.webmanifest`),
puis `node tests/run.js --racine=<copie> --suite=regressions` doit **échouer** (et passer sur le dépôt).
Chaque règle d'appariement de `flashLoadState` et le réalignement des cartes signalées ont été vérifiés
ainsi (tableau « mutant → contrôle qui l'attrape » : `docs/audit-2026-09.md`, §6).

---

## 7. Dans le conteneur Claude Code

- Playwright 1.56.1 est installé **globalement** et Chromium est dans
  `/opt/pw-browsers` (`PLAYWRIGHT_BROWSERS_PATH` déjà positionné). `tests/run.js`
  trouve le Playwright global tout seul (via `npm root -g`) : `NODE_PATH` est facultatif.
- **Ne pas lancer** `npx playwright install` ni `npm install` dans le dépôt
  (une autre version de Playwright réclamerait un Chromium absent du conteneur).
- Commandes : `node tests/run.js --rapide` (≈ 4 min 30 s), `node tests/run.js` (≈ 18 min).
  L'outil Bash coupe au bout de 10 min : lancer la batterie complète **en arrière-plan**
  en redirigeant la sortie vers un fichier temporaire hors du dépôt, puis suivre ce fichier.
- Tester le **dernier commit** (par exemple pour comparer avec l'ancienne version) :
  ```
  mkdir -p <dossier-temporaire>/orig
  git -C /home/user/revisions-ptsi archive HEAD | tar -x -C <dossier-temporaire>/orig
  node tests/run.js --racine=<dossier-temporaire>/orig --sortie=<dossier-temporaire>/sortie
  ```
  ⚠️ `git archive HEAD` extrait le dernier commit **sans** les modifications non commitées.
  Pour figer l'**état actuel** du dossier de travail (par exemple pendant qu'une autre
  session modifie `index.html`), copier plutôt `index.html` dans un dossier temporaire, avec
  des liens symboliques (ou des copies) vers `vendor/`, `icons/`, `sw.js` et
  `manifest.webmanifest`, puis utiliser `--racine` (même méthode qu'au §6, « mutation ») :
  ```
  mkdir -p <dossier-temporaire>/fige && cp /home/user/revisions-ptsi/index.html <dossier-temporaire>/fige/
  for f in vendor icons sw.js manifest.webmanifest; do ln -s /home/user/revisions-ptsi/$f <dossier-temporaire>/fige/$f; done
  node tests/run.js --racine=<dossier-temporaire>/fige --sortie=<dossier-temporaire>/sortie
  ```
- Le serveur de test est intégré à `run.js` et s'arrête avec lui : aucun
  `http-server` à lancer ni à tuer.

---

## 8. Fichiers

```
package.json          scripts npm (test, test:rapide, valider) + dépendance Playwright
tests/run.js          point d'entrée : options, serveur, lancement des suites, résumé
tests/lib/serveur.js  petit serveur statique (module http de node) + variantes d'index.html
tests/lib/outils.js   fonctions partagées (attente du site, navigation, MathJax, decks…)
tests/suites/*.js     les suites : site, mobile, interactions, pwa, regressions
tests/sortie/         captures + rapport.json du dernier lancement (ignoré par git)
```

Le dossier `tests/` et `package.json` sont publiés sur GitHub Pages avec le reste
du dépôt (sans effet sur le site) ; `tests/sortie/` et `node_modules/` ne le sont pas
(ignorés par git).
