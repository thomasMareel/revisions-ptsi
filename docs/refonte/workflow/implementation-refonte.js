export const meta = {
  name: 'implementation-refonte',
  description: "Implémente le nouveau design « Cahier de prépa » dans le site : socle, deux lignes de travail parallèles, fusion, relecture adversariale en boucle",
  phases: [
    { title: 'Socle', detail: 'polices, jetons, MathJax 1,07, data-mat, CSS rangé en régions, composants de base' },
    { title: 'Lignes', detail: 'A : coquille puis page chapitre ; B : contenu/simulateurs puis révision/fenêtres' },
    { title: 'Fusion', detail: 'fusion des deux lignes, batterie complète, documentation' },
    { title: 'Relecture', detail: '4 angles de relecture adversariale + corrections, jusqu\'à épuisement (3 tours max)' },
    { title: 'Vérification finale', detail: 'batterie complète, visuel --strict, planche avant/après' },
  ],
}

const REPO = '/home/user/revisions-ptsi'
const S = '/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad'
const F = S + '/refonte/design/final'
const I = S + '/refonte/impl'
const BASE = 'claude/repo-analysis-vjplbu'

const ENV = `
CONTEXTE : refonte graphique COMPLÈTE du site de révisions PTSI→PT (${REPO}, index.html unique ≈ 76 500 lignes avec CSS/JS inline, GitHub Pages, PWA 100 % hors-ligne). Conventions dans le CLAUDE.md injecté : RESPECTE-LES (ancres grep, jamais lire index.html en entier, couche de commande cachée .chap-btn/.tab + navigateTo à ne jamais casser, Store et pas localStorage, état des flashcards flash:/flashids: INTOUCHABLE, aucune couleur codée en dur, sombre = :root[data-theme="dark"], polices et ressources locales uniquement, etc.).
L'utilisateur (étudiant, site public) trouve le site actuel « visuellement médiocre » et veut du changement à tous les étages. Le système de design FINAL a été conçu et validé : TOUT est dans ${F}/ :
- SPEC.md : spécification complète (lis les parties qui concernent ta tâche EN ENTIER, et §1, §6, §9 dans tous les cas) ;
- tokens.css (jetons définitifs, anciens noms de variables conservés), composants.css (CSS de RÉFÉRENCE déjà écrit sur les classes existantes du site, sections numérotées), polices/ (14 woff2 + polices.css) ;
- maquettes/*.html et captures/*.png : la CIBLE visuelle (01 chapitre ordinateur, 02/02b chapitre téléphone, 03a/b/c navigation, 04a/b carte, 05 Aujourd'hui, 06a/b sombre, 07a/b thème, 08a/b/c exercices et simulateur, 09 spécimen) ; outils/ (scripts de contrôle : contrastes-dom.js, cibles.js, capture.js, mesures.js…).
DÉCISIONS IMPÉRATIVES DE L'UTILISATEUR : aucune barre fixe en bas sur téléphone ; pas de sommaire en puces sur téléphone ; le site s'ouvre sur le dernier chapitre consulté et « Aujourd'hui » ne s'ouvre JAMAIS seul (entrée manuelle) ; thème Clair/Sombre/Auto (mécanisme déjà publié : window.__setTheme/__themePref, data-theme="dark" effectif, data-theme-pref) ; pas d'anneau de % dans la navigation (il reste dans le Bilan).
OUTILS : Playwright global (NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers ; JAMAIS npm install ni playwright install) ; toujours FONTCONFIG_FILE=${S}/ptspe/fonts-sans-lm.conf pour Chromium et les tests. Tests : node tests/run.js [--suite=site,mobile,interactions,pwa,regressions,visuel] [--rapide] [--strict] [--chapitres=…] --sortie=<dossier dans ${S}> (lancés depuis la racine de TA copie, ils servent cette copie ; > 10 min → arrière-plan avec sortie dans un fichier). Validateurs : python3 tools/validate.py ; TMPDIR=${S} python3 tools/check_js.py. Couverture CSS (classes utilisées sans règle / règles mortes) : python3 ${I}/couverture.py index.html. Pour REGARDER une capture, ouvre le PNG avec l'outil Read : compare TOUJOURS le rendu réel du site aux captures cibles.
RÈGLES DE TRAVAIL : tout en français (commentaires, commits) ; code dans le style du code voisin ; JS défensif et idempotent (une exception dans le grand script coupe tout ce qui suit) ; ne dégrade pas la vitesse de chargement sur téléphone (déjà lente : pas de calcul lourd au chargement, travail paresseux) ; garde les IDs utilisés par le JS et les tests, ou mets à jour les tests EN CONSERVANT ce qu'ils vérifient (ne jamais affaiblir ni supprimer une vérification pour la faire passer) ; ne modifie pas CACHE_VERSION (bump unique à la publication) mais tiens PRECACHE de sw.js à jour ; aucun git push. Commite souvent sur ta branche (commits de travail permis) ; fin de CHAQUE message de commit, après une ligne vide :
Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01UP4LBNtK8zfhs8M8oE2kQm
REPRISE APRÈS REDÉMARRAGE (le conteneur peut redémarrer) : tiens un journal de progression ${I}/<ta-tâche>.md (fait / reste à faire) ; au début, si ta branche a déjà des commits de ta tâche ou si ce journal existe, REPRENDS là où c'en était.
`

const RES = { type: 'object', properties: {
  branche: { type: 'string' }, commits: { type: 'array', items: { type: 'string' } },
  fait: { type: 'array', items: { type: 'string' } },
  ecartsAuxMaquettes: { type: 'array', items: { type: 'string' }, description: 'différences volontaires ou restantes avec la cible, et pourquoi' },
  tests: { type: 'string', description: 'commandes lancées et résultats exacts' },
  resteAFaire: { type: 'array', items: { type: 'string' } },
}, required: ['branche', 'commits', 'fait', 'tests', 'resteAFaire'] }

const BRANCHE_DEBUT = (br, depuis) => `Tu es dans une copie isolée du dépôt (git worktree, ton répertoire courant). Commence par : si la branche ${br} existe (git rev-parse --verify ${br}), « git checkout ${br} » ; sinon « git checkout -B ${br} ${depuis} ». FIN : tout commité sur ${br}, puis « git checkout --detach » (libère la branche pour l'étape suivante).`

// ---------------------------------------------------------------- Socle
phase('Socle')
const socle = await agent(ENV + `
TÂCHE : SOCLE de la refonte (SPEC §9 point 1 + base des composants). ${BRANCHE_DEBUT('wip/refonte', BASE)}
1) POLICES (SPEC §2.1, §2.6) : copier ${F}/polices/*.woff2 + licences dans vendor/fonts/, polices.css → vendor/fonts/polices.css (chemins relatifs corrects) ; <link> du <head> ET gabarit d'impression (printChapter) vers polices.css ; remplacer TOUTES les mentions nominatives des anciennes polices (grep 'Fraunces', 'Inter Tight', 'JetBrains Mono' dans le CSS, les style="…" du contenu, les ctx.font des canvas, le gabarit d'impression) par les nouvelles (var(--font-text|ui|code) dans le CSS ; noms de familles réels dans les ctx.font : 'Source Sans 3' pour les étiquettes, 'JetBrains Mono' gardée pour le code/valeurs) ; puis supprimer les anciens fichiers de polices devenus inutiles et l'ancien fonts.css ; PRECACHE de sw.js mis à jour (la suite pwa vérifie que chaque fichier listé existe).
2) JETONS : ${F}/tokens.css en tête du grand <style>, à la place des blocs de variables :root / :root[data-theme="dark"] actuels (les anciens noms restent définis comme alias, cf. SPEC §3.6). Mets à jour le script de thème du <head> pour qu'il pose AUSSI data-theme-pref (sinon le filet de sécurité CSS « :root sans attribut + système sombre » rend sombre un utilisateur « Clair » sur un appareil sombre jusqu'au grand script) ; meta theme-color selon SPEC §3.8 ; corrige la phrase du CLAUDE.md « ne pas écrire de @media (prefers-color-scheme) » pour décrire le filet de sécurité des jetons.
3) MathJax chtml.scale 1.07 (config de la page ET du gabarit d'impression) — SPEC §2.2.
4) data-mat (SPEC §7.1) sur chaque .chapter (là où data-domain est posé), sur les rangées du tiroir et sur .chap-title-banner.
5) getCanvasColors()/__CV (SPEC §3.7) : muted/grid lus depuis les jetons ; la suite regressions (B4) doit rester verte, vérifie les 27 simulateurs en clair et en sombre.
6) RANGEMENT DU CSS EN RÉGIONS : réorganise le grand <style> en régions balisées, chacune avec un propriétaire, pour que deux lignes de travail parallèles puissent ensuite réécrire leurs régions sans conflit git :
   /* ===== RÉGION JETONS ===== */ … /* ===== FIN RÉGION JETONS ===== */, puis BASE (reset, typo de base, boutons/compteurs/badges/puces/champs = composants.css §0 et §1, que TU portes maintenant), COQUILLE (en-tête, navigation/tiroir, barre téléphone, menus, sélecteur de thème, bandeaux de mise à jour), PAGE (feuille, intercalaire .chap-title-banner, onglets .tabs, rail .toc, pied #chap-pager), CONTENU (cours, encadrés, formules, tableaux, listes, figures/SVG, exercices), SIMU (simulateurs, Lorentz compris), REVISION (flashcards, quiz, calcul mental, Aujourd'hui, Bilan, cartes signalées), FENETRES (recherche, formulaire, sauvegarde, raccourcis, toasts, autres overlays), IMPRESSION (@media print de la page).
   CHAQUE règle existante va dans EXACTEMENT UNE région selon son sélecteur (les blocs @media sont dupliqués par région) ; garde l'ordre relatif des règles à l'intérieur d'une région ; une règle qui ne sert plus (vérifie par grep/couverture qu'aucun HTML ni JS n'utilise la classe) peut être supprimée. Les petits autres blocs <style> du fichier : laisse-les en place mais note leur propriétaire dans ton journal. Le rendu peut changer à ce stade (polices, couleurs, ordre de cascade) : c'est normal, les lignes suivantes réécrivent chaque région ; mais rien ne doit être CASSÉ fonctionnellement.
7) Écris ${I}/regions.md : liste des régions avec leurs propriétaires et, pour chaque région, les sections de composants.css et de SPEC qui la concernent (pour les étapes suivantes).
CRITÈRES : validate.py et check_js.py OK ; suites site, interactions, pwa, regressions VERTES (les suites visuel et mobile peuvent signaler des écarts dus au nouveau rendu : note-les sans affaiblir leurs listes) ; 0 erreur JS ; 0 requête externe ; polices réellement chargées (document.fonts) ; formules MathJax correctes à 1,07 (regarde une capture de rlc-cours ordinateur et téléphone).`,
  { label: 'socle', phase: 'Socle', schema: RES, isolation: 'worktree' })

// ---------------------------------------------------------------- Lignes
phase('Lignes')
const LIGNES = [
  { key: 'A', branche: 'wip/refonte-a', etapes: [
    { nom: 'coquille', consigne: `COQUILLE ET NAVIGATION. Régions CSS : COQUILLE (et BASE si un composant de base manque). SPEC §4.1 (grille et points de rupture), §4.2 (téléphone : barre haute .mbar qui s'efface au défilement + section courante, onglets collants, feuille ⋯ qui monte du bas, pages plein écran fermées aussi par le bouton retour Android), §4.3 (navigation des chapitres : année, filtre groupé par matière avec <mark>, épinglés/récents, intercalaires de matière avec effectif, parties repliables, rangées .nav-item, page Chapitres du téléphone avec ses 2 tuiles, SOMMAIRE DE LA MATIÈRE avec le lien profond #sommaire/<matière>), §4.5, §4.6 (popover de thème ordinateur avec 3 mini-vues + taille du texte ; segmenté dans la feuille ⋯ sur téléphone ; « actuellement : … » suivi par matchMedia), §5.12 (en-tête ordinateur : recherche visible, Aujourd'hui, Bilan, Réviser + compteur, thème, Plus), §5.13 (tiroir = barre latérale permanente ≥ 1 200 px), §5.14, §6. JS SPEC §7 points 6, 7, 8, 12. composants.css §2, §3, §9, §12, §13, §14. Cibles : captures 01 (en-tête + barre latérale), 02/02b (barre téléphone), 03a, 03b, 03c, 07a, 07b. Les menus existants (Plus, Réviser, ⋯) gardent leurs actions et leurs IDs (#today-btn passe dans l'en-tête : mets à jour les tests qui l'ouvraient par #more-btn) ; #theme-btn ouvre désormais le popover (mets à jour les tests du thème pour choisir une option du popover, en vérifiant toujours data-theme et Store).` },
    { nom: 'page', consigne: `PAGE CHAPITRE. Régions CSS : PAGE. SPEC §4.4 (intercalaire teinté et millimétré de .chap-title-banner : fil d'Ariane avec lien vers le Sommaire de la matière, titre h2.ctb-title, actions Formulaire/Imprimer/Épingler, méta année/sections/cartes/exercices/simulateur ; onglets posés sur l'intercalaire puis collants ; feuille avec marge « § » de 112 px et filet rouge ; rail droit ≥ 1 360 px : sommaire scroll-spy restylé + « Mes cartes » + liste des exercices sur l'onglet Exercices ; pied #chap-pager en deux cartes), §5.1 (onglets). JS SPEC §7 points 4, 5, 10, 11. composants.css §4 et §8. Cibles : captures 01, 06a, 08a (rail des exercices), 02 et 06b pour le téléphone (pas d'intercalaire dans la page sur téléphone). La coquille vient d'être faite par l'étape précédente sur cette même branche : construis dessus.` },
  ] },
  { key: 'B', branche: 'wip/refonte-b', etapes: [
    { nom: 'contenu', consigne: `CONTENU DU COURS, EXERCICES ET SIMULATEURS. Régions CSS : CONTENU et SIMU. SPEC §2 (application de toute l'échelle typographique au contenu : tailles par élément, interlignage, mesure 34 em, rythme vertical, micro-typographie), §5.2 (cours : .course-section, .sec-num découpé, h2/h3/h4, .intro en romain, .formula et fusion des formules consécutives, .mj-large, .def-box/.prop-box/.method-box/.notice/.reveal et « À retenir », étapes de méthode en pastilles, tableaux, listes, figures et SVG), §5.3 (exercices : .exo-wrapper/.exo, .diff en barres + mot, solutions .toggle-sol, puce Concours, filtre de difficulté), §5.5 (simulateurs : grille à zones nommées SANS toucher au DOM des 26 simulateurs canvas, courbe collante d'abord sur téléphone, --p sur les input range, courbe principale en --chap-vif ; le simulateur SVG de Lorentz doit rester lisible). Supprime les 7 définitions successives de .def-box/.prop-box/.method-box et les règles par domaine (SPEC §9.2). JS SPEC §7 points 2, 3 (typographie française et .mj-large, dans la promesse de typesetPanel et après le rendu d'une solution ou du Formulaire, jamais dans code/pre/kbd/mjx-container), 14. composants.css §5, §6, §7. Cibles : captures 01 (contenu), 08a, 08b, 08c, 09-specimen-clair/sombre. Balaye au moins 20 chapitres variés des 5 matières (dont 5 de 2ᵉ année, un d'anglais, un d'info avec du code, des chapitres à tableaux et à SVG) en clair et en sombre, ordinateur et téléphone : aucun contenu illisible, cassé ou débordant (rlc-cours ne doit plus déborder à 390 px : retire de DEBORDEMENTS_CONNUS les panneaux corrigés).` },
    { nom: 'revision', consigne: `RÉVISION ET FENÊTRES. Régions CSS : REVISION, FENETRES, IMPRESSION. SPEC §5.4 (cartes : fiche bristol avec réglure en lh retirée si formule haute, verso avec la question en rappel, boutons de notation tout en bas avec icône + échéance + touche, en-tête de fiche à badges, aide selon le pointeur, progression empilée, raccourcis 1/2/3/Espace sur TOUS les decks avec garde de saisie — dans makeFlash ET dans le quiz ; l'état flash:/flashids: n'est PAS touché : vérifie qu'il est identique octet pour octet avant/après une session de notation équivalente), §5.6 quiz, §5.7 Aujourd'hui (barres par matière, histogramme 7 jours, salutation, reprise horodatée via lastPos.t si présent), §5.8 Bilan, §5.9 recherche, §5.10 formulaire, §5.11 autres fenêtres (sauvegarde, raccourcis, cartes signalées, calcul mental, toasts, bannière de mise à jour), §5.15 impression (l'impression vient d'être réparée, test B5 de regressions : il doit rester vert ; encre noire sur blanc). JS SPEC §7 points 9 et 13. composants.css §10, §11 et le reste pour les fenêtres. Cibles : captures 04a, 04b, 05, 09. Les cartes d'anglais restent en texte brut (isPlainDeck) avec leur bouton de lecture audio. La branche contient déjà l'étape « contenu » : construis dessus.` },
  ] },
]

const lignes = await parallel(LIGNES.map(L => async () => {
  const sorties = []
  for (const [i, e] of L.etapes.entries()) {
    const r = await agent(ENV + `
TÂCHE : ligne ${L.key}, étape ${i + 1}/${L.etapes.length} — ${e.consigne}
Journal : ${I}/ligne-${L.key}-${e.nom}.md. Lis d'abord ${I}/regions.md (régions CSS et propriétaires, écrit par le socle) : ne modifie que TES régions CSS (et le HTML/JS de ton périmètre) — une autre ligne travaille en parallèle sur les autres régions et les deux branches seront fusionnées.
${BRANCHE_DEBUT(L.branche, 'wip/refonte')}
MÉTHODE : réécris tes régions en partant de composants.css (référence) et de la SPEC, en reprenant de l'ancien CSS ce qui reste nécessaire (règles propres à un simulateur, à un overlay…) mais restylé avec les jetons ; puis compare le rendu RÉEL du site (captures Playwright aux mêmes tailles que les maquettes, clair ET sombre) aux captures cibles et corrige jusqu'à une fidélité soignée (alignements, rythme, hiérarchie, rien ne déborde, cibles tactiles ≥ 44 px au téléphone, contrastes AA mesurés).
CRITÈRES : validate.py et check_js.py OK ; suites site, interactions, pwa, regressions VERTES ; suite visuel lancée en --strict : AUCUN constat sur les écrans de ton périmètre (liste les constats restants hors périmètre) ; mobile : pas de nouveau débordement ; 0 erreur JS ; aucune couleur codée en dur hors mini-vues du sélecteur de thème.`,
      { label: `ligne-${L.key}:${e.nom}`, phase: 'Lignes', schema: RES, isolation: 'worktree' })
    sorties.push({ etape: e.nom, resultat: r })
  }
  return { ligne: L.key, branche: L.branche, sorties }
}))

// ---------------------------------------------------------------- Fusion
phase('Fusion')
const fusion = await agent(ENV + `
TÂCHE : FUSION des deux lignes dans wip/refonte, puis remise en cohérence. ${BRANCHE_DEBUT('wip/refonte', BASE)}
Rapports des étapes précédentes — socle : ${JSON.stringify(socle)} ; lignes : ${JSON.stringify(lignes)}
1) git merge --no-ff wip/refonte-a puis wip/refonte-b ; résous chaque conflit en gardant le travail des DEUX lignes (lis les deux côtés ; JS partagé comme __updateReviseBadge, makeFlash, tests : combine).
2) Vérifie l'ensemble : validate.py, check_js.py, BATTERIE COMPLÈTE (node tests/run.js, en arrière-plan, sortie dans un fichier) + visuel --strict ; corrige ce qui casse à la jonction des deux lignes.
3) DOCUMENTATION : mets CLAUDE.md à jour en profondeur (nouvelle coquille et navigation, régions CSS, jetons et polices, chtml.scale, nouvelles fonctions JS et nouveaux IDs, nouvelles clés Store comme navCollapsed et lastPos.t, Sommaire de la matière et #sommaire/…, barre téléphone, sélecteur de thème, cartes, règles « ne pas faire » de SPEC §9 ; retire ce qui est devenu faux, ex. « Identité visuelle (Lot 3) », polices Fraunces/Inter Tight, anomalie .notice) ; README.md (fonctionnalités) ; GABARIT-CHAPITRE.md (nouvelles classes utiles aux auteurs : data-nom des formules, À retenir, etc.) ; tests/README.md si besoin.
Renvoie l'état exact (tests, constats visuel --strict restants).`,
  { label: 'fusion', phase: 'Fusion', schema: RES, isolation: 'worktree' })

// ---------------------------------------------------------------- Relecture
phase('Relecture')
const CONSTATS = { type: 'object', properties: {
  constats: { type: 'array', items: { type: 'object', properties: {
    gravite: { type: 'string', enum: ['bloquant', 'important', 'mineur'] },
    ecran: { type: 'string' }, probleme: { type: 'string' }, preuve: { type: 'string', description: 'capture, mesure, commande' },
    correctionProposee: { type: 'string' },
  }, required: ['gravite', 'ecran', 'probleme', 'preuve'] } },
  bilan: { type: 'string' },
}, required: ['constats', 'bilan'] }

const ANGLES = [
  { key: 'ordinateur', lentille: "FIDÉLITÉ ET QUALITÉ VISUELLE SUR ORDINATEUR (1440×900 et 1280×800, puis 1100 et 900 px de large), clair ET sombre : compare le site réel aux captures cibles 01, 03a, 06a, 07a, 08a, 08b, 09 (rends les mêmes écrans avec Playwright et regarde-les côte à côte) ; puis balaie au moins 25 chapitres × onglets variés (5 matières, 1ʳᵉ/2ᵉ année) à la recherche de tout ce qui est laid, incohérent, mal aligné, illisible, cassé, non stylé (composant resté à l'ancien style), formule mal intégrée, encadré raté, tableau ou SVG cassé." },
  { key: 'telephone', lentille: "FIDÉLITÉ ET QUALITÉ VISUELLE SUR TÉLÉPHONE (390×844 et 360×780, contexte mobile tactile), clair ET sombre : compare aux captures cibles 02, 02b, 03b, 03c, 04a, 04b, 05, 06b, 07b, 08c ; vérifie la barre haute qui s'efface au défilement et revient avec la section, les onglets collants, la page Chapitres, la feuille ⋯, le quiz, les cartes, l'absence de barre en bas, l'absence de débordement horizontal (mesure-le sur 30 panneaux variés, solutions dépliées comprises), les cibles tactiles ≥ 44 px." },
  { key: 'fonctionnel', lentille: "FONCTIONNEL ET RÉGRESSIONS : batterie complète des tests (node tests/run.js, en arrière-plan) ; puis à la main dans Chromium : navigation (tiroir/barre latérale, préc./suiv., liens profonds #id/onglet et #sommaire/…, bouton précédent, retour Android qui ferme les pages plein écran), ouverture sur le dernier chapitre consulté et Aujourd'hui jamais automatique, recherche, flashcards (notation, raccourcis avec garde de saisie, SRS : l'état flash:/flashids: d'un deck doit évoluer EXACTEMENT comme sur la version publiée d'origin/main pour une même suite de notations — compare les deux versions), quiz, révisions du jour, Bilan, Formulaire, impression (formules dessinées), sauvegarde export/import, thème Clair/Sombre/Auto (popover, feuille ⋯, suivi du système), année 1/2, taille du texte A−/A+, anglais (texte brut + audio), simulateurs (les 27 + Lorentz, en clair et en sombre) ; erreurs JS ; vitesse : temps jusqu'à interactif et ouverture d'un gros chapitre sur téléphone émulé (CPU ×4) comparés à origin/main (pas de régression notable)." },
  { key: 'accessibilite', lentille: "ACCESSIBILITÉ ET RIGUEUR DU CODE : suite visuel en --strict (aucun constat ne doit rester) ; navigation au clavier complète (focus visible partout, ordre logique, Échap ferme, pièges de focus dans les modales), rôles ARIA (radio du thème, aria-current, aria-expanded), mouvement réduit, taille du texte A+ sans casse ; contrastes des icônes et contrôles (3:1) ; grep des couleurs codées en dur dans le nouveau CSS/JS ; couverture CSS (python3 ${I}/couverture.py : classes utilisées sans règle = composants oubliés ; règles mortes) ; JS idempotent et défensif ; conformité aux conventions du CLAUDE.md et à jour de la documentation." },
]

const tours = []
for (let tour = 1; tour <= 3; tour++) {
  const revues = await parallel(ANGLES.map(a => () => agent(ENV + `
TÂCHE : RELECTURE ADVERSARIALE, tour ${tour}, angle : ${a.lentille}
La refonte est sur la branche wip/refonte. Extrais-la en LECTURE SEULE dans ta propre copie : cd ${REPO} && git worktree add --detach ${S}/relecture-${a.key}-${tour} wip/refonte (réutilise le dossier s'il existe déjà, après « git -C <dossier> checkout --detach wip/refonte »), travaille dans ce dossier, NE MODIFIE RIEN dans le dépôt, puis supprime la copie à la fin (git worktree remove --force).
Cherche activement les défauts ; chaque constat doit être PROUVÉ (capture regardée, mesure, commande reproductible) et accompagné d'une correction proposée précise. Gravité : bloquant (cassé, illisible, perte de données, test rouge, décision de l'utilisateur non respectée), important (écart net à la cible, incohérence visible, accessibilité), mineur (finition). ${tour > 1 ? 'Tours précédents (constats et corrections) : ' + JSON.stringify(tours) + ' — vérifie aussi que les corrections annoncées sont réelles et n\'ont rien cassé.' : ''}`,
    { label: `relecture-${tour}:${a.key}`, phase: 'Relecture', schema: CONSTATS })))
  const constats = revues.filter(Boolean).flatMap((r, i) => r.constats.map(c => ({ ...c, angle: ANGLES[i] ? ANGLES[i].key : '?' })))
  const aCorriger = constats.filter(c => c.gravite !== 'mineur' || tour < 3)
  log(`Tour ${tour} : ${constats.length} constats (${constats.filter(c => c.gravite === 'bloquant').length} bloquants, ${constats.filter(c => c.gravite === 'important').length} importants)`)
  if (!aCorriger.length) { tours.push({ tour, constats, correction: null }); break }
  const correction = await agent(ENV + `
TÂCHE : CORRIGER les constats du tour ${tour} de relecture sur la branche wip/refonte. ${BRANCHE_DEBUT('wip/refonte', BASE)}
Constats (gravité, écran, problème, preuve, correction proposée) : ${JSON.stringify(aCorriger)}
Traite-les TOUS, des bloquants aux mineurs : vérifie d'abord chaque constat (un constat faux est écarté avec la preuve), corrige la cause (pas le symptôme), regarde le rendu après correction. Puis validate.py, check_js.py, batterie complète (arrière-plan) + visuel --strict. Renvoie pour chaque constat : corrigé / écarté (pourquoi).`,
    { label: `correction-${tour}`, phase: 'Relecture', schema: { type: 'object', properties: {
      traitement: { type: 'array', items: { type: 'object', properties: { probleme: { type: 'string' }, statut: { type: 'string', enum: ['corrige', 'ecarte', 'partiel'] }, detail: { type: 'string' } }, required: ['probleme', 'statut', 'detail'] } },
      commits: { type: 'array', items: { type: 'string' } }, tests: { type: 'string' },
    }, required: ['traitement', 'commits', 'tests'] }, isolation: 'worktree' })
  tours.push({ tour, constats, correction })
}

// ---------------------------------------------------------------- Vérification finale
phase('Vérification finale')
const finale = await agent(ENV + `
TÂCHE : VÉRIFICATION FINALE avant publication de la refonte (branche wip/refonte), en lecture seule sauf correction triviale indispensable (alors commitée sur wip/refonte). Extrais la branche : cd ${REPO} && git worktree add --detach ${S}/verif-finale wip/refonte (réutilise s'il existe), travaille dedans, supprime-la à la fin.
1) python3 tools/validate.py ; TMPDIR=${S} python3 tools/check_js.py ; BATTERIE COMPLÈTE node tests/run.js (arrière-plan, sortie dans un fichier) ; node tests/run.js --suite=visuel --strict. Tout doit être vert ; sinon dis exactement ce qui échoue.
2) PLANCHE AVANT/APRÈS pour l'utilisateur : capture les mêmes écrans sur origin/main (copie détachée dans ${S}/avant) et sur wip/refonte — chapitre rlc cours ordinateur clair et sombre, rlc cours téléphone, navigation téléphone (page Chapitres), une flashcard au téléphone, Aujourd'hui au téléphone, exercices + simulateur ordinateur, maxwell (2ᵉ année) — et assemble ${S}/refonte/planche-avant-apres/ : PNG par paire + une page planche.html autonome (images en relatif) ; regarde le résultat.
3) Résumé en français, pour un étudiant débutant, de ce qui change pour lui (sans jargon), et liste des points connus restants.
Historique de la relecture : ${JSON.stringify(tours.map(t => ({ tour: t.tour, nb: t.constats.length, correction: t.correction && t.correction.traitement })))}`,
  { label: 'verification-finale', phase: 'Vérification finale', schema: { type: 'object', properties: {
    toutVert: { type: 'boolean' }, tests: { type: 'string' }, planche: { type: 'string' },
    resumeUtilisateur: { type: 'string' }, pointsRestants: { type: 'array', items: { type: 'string' } },
  }, required: ['toutVert', 'tests', 'planche', 'resumeUtilisateur', 'pointsRestants'] } })

return { socle, lignes, fusion, tours: tours.map(t => ({ tour: t.tour, nbConstats: t.constats.length, constats: t.constats, correction: t.correction })), finale }