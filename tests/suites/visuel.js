'use strict';
/* ============================================================
   Suite « visuel » — mesures visuelles automatiques
   ============================================================
   Sert de garde-fou à la refonte graphique : sur une douzaine d'ÉCRANS (voir
   ECRANS), en thème CLAIR puis SOMBRE (bascule par le bouton du thème, comme
   un utilisateur), sur ordinateur 1440×900 et sur téléphone 390×844 :
   1) CONTRASTE réel du texte : couleur calculée de chaque nœud texte visible
      (et de chaque formule MathJax, prise en bloc, et de chaque texte généré
      par le CSS : ::before / ::after à content:"…", comme les étiquettes
      DÉFINITION / PROPRIÉTÉ / MÉTHODE des encadrés, sélecteur « div.def-box::before »)
      contre son fond effectif,
      obtenu en remontant les ancêtres et en composant les fonds
      semi-transparents (opacité des ancêtres comprise). Seuil 4,5:1, ou 3:1
      pour un grand texte (≥ 24 px, ou ≥ 18,66 px en gras). Un fond en image
      ou en dégradé n'est pas évalué : il est listé à part (« fonds non
      évalués »). Le quadrillage de la page (lignes de 1 px sur body) est
      négligé : le texte est évalué contre la couleur de fond ; de même une
      petite icône non répétée (≤ 48 px, posée à côté du texte). Textes des
      commandes désactivées exclus (exemption WCAG 1.4.3), ainsi que les
      éléments « masqués visuellement » (boîte visible de 1 px au plus).
   2) TAILLE du texte rendu : aucune police < 12 px (une formule MathJax compte
      pour sa taille de base : exposants et indices internes exclus ; un texte
      SVG compte pour sa taille multipliée par l'échelle du viewBox ; un texte
      généré par le CSS, pour la taille de son pseudo-élément).
   3) DÉBORDEMENT horizontal : document.scrollingElement.scrollWidth plus large
      que la fenêtre, et éléments visibles qui dépassent à droite (le plus haut
      élément qui dépasse ; un élément rogné par un ancêtre à défilement ou
      overflow:hidden n'est pas compté).
   4) CIBLES TACTILES (téléphone seulement) : boutons, liens, champs, éléments
      role=button/menuitem/tab… visibles et cliquables. Deux mesures :
      - « cible24 » (WCAG 2.5.8, niveau AA) : une cible de moins de 24 px de
        côté échoue, sauf si le disque de 24 px de diamètre centré sur elle ne
        touche aucune autre cible ni le disque d'une autre petite cible
        (exception d'espacement de la règle) ;
      - « cible44 » (WCAG 2.5.5, confort au doigt) : toute cible de moins de
        44 px de côté, signalée à part.
      Exemptés : liens dans une phrase (display:inline entourés de texte),
      commandes désactivées, cibles imbriquées dans un bouton/lien/label.
   Chaque mesure produit des constats { ecran, theme, appareil, selecteur,
   valeur, seuil } (regroupés par sélecteur lisible dans un écran : pire
   valeur, nombre d'occurrences, exemples).

   Ce qui échoue AUJOURD'HUI est listé dans TOLERES (ci-dessous) : la suite
   n'échoue que pour un constat NOUVEAU (ou aggravé au-delà de MARGES), et
   avertit (« ! ») quand une entrée tolérée n'est plus constatée. Option
   --strict : listes ignorées, tout constat fait échouer (pendant la refonte).
   Toujours écrits dans le dossier de sortie : visuel.json (détail complet),
   visuel.md (récapitulatif lisible + proposition de liste TOLERES) et une
   capture par écran (visuel-<appareil>-<thème>-<écran>.png).

   Déterminisme : Math.random est remplacé par un générateur à graine (ordre
   des flashcards, tirage du quiz), un état de flashcards est semé dans le
   Store (Bilan, Aujourd'hui, badge), les écrans sont visités dans un ordre
   fixe et les fenêtres refermées entre deux écrans. */
const fs = require('fs');
const path = require('path');
const { pause, attendreApp, naviguer, choisirTheme, etatMathJax } = require('../lib/outils');

/* ---------- Anomalies TOLÉRÉES (site aux commits b3632ad et 1d2a766, Chromium 141) ----------
   Une ligne = [mesure, écrans, thèmes, appareils, { sélecteur: pire valeur tolérée, … }]
   - mesure : contraste | taille | debordement | cible24 | cible44 ;
   - écrans : noms d'ECRANS séparés par des espaces, alias 'chapitres' (les 8
     écrans de chapitre) / 'fenetres' (tiroir, recherche, quiz, Bilan…), ou '*' ;
   - thèmes : 'clair', 'sombre' ou '*' ; appareils : 'ordi', 'tel' ou '*' ;
   - pire valeur : rapport de contraste, taille (px), bord droit (px) ou côté de
     la cible (px). Un constat toléré fait quand même échouer s'il s'aggrave au
     delà de MARGES (nouvelle couleur moins lisible, élément plus large…).
   Quand un sélecteur n'est plus constaté, la suite avertit (« ! ») : le retirer.
   Régénérer : la section « Proposition de liste TOLERES » de visuel.md donne
   la liste correspondant aux constats du dernier lancement (à relire avant de
   la recopier ici). */
const TOLERES = [
  // — Contraste du texte —
  ['contraste', 'aujourdhui', '*', '*', { 'span.due-sub': 2.57 }],
  ['contraste', 'aujourdhui', 'sombre', '*', { '#today-due-btn span': 2.99, 'span.due-count': 2.99 }],
  ['contraste', 'bilan', 'clair', '*', { '#dash-close-btn': 4.09 }],
  ['contraste', 'bilan', 'sombre', '*', { '#dash-revise-btn': 2.99 }],
  ['contraste', 'chapitres', '*', '*', { 'span.num': 4.01 }],
  ['contraste', 'chapitres', 'sombre', 'ordi', { '#rev-badge': 2.99 }],
  ['contraste', 'chapitres', 'sombre', 'tel', { '#rev-badge-mob': 2.99 }],
  ['contraste', 'quiz', '*', 'ordi', { 'button.quiz-btn-reread kbd': 3.25, 'button.quiz-rate-btn.rate-acq kbd': 2.39, 'button.quiz-rate-btn.rate-hes kbd': 1.96, 'button.quiz-rate-btn.rate-rev kbd': 2.46 }],
  ['contraste', 'quiz', 'clair', '*', { '#quiz-progress-text': 4.28, 'button.quiz-close': 3.68 }],
  ['contraste', 'recherche', '*', '*', { 'span.sr-snippet mark': 2.11 }],
  ['contraste', 'recherche', 'clair', '*', { 'span.sr-badge.sr-b-meth': 4.17 }],
  ['contraste', 'rlc-cours maxwell-cours', 'sombre', '*', { 'div.notice': 1.99, 'div.notice em': 1.99, 'div.notice mjx-container': 1.99 }],
  ['contraste', 'rlc-flash anglais-flash', '*', '*', { 'button.flash-reset': 1.9, 'div.flash-stats-wrap span#*-stats': 2.96, 'span.ic-lbl': 2.34 }],
  ['contraste', 'rlc-flash anglais-flash', 'clair', '*', { 'button.ok': 2.61, 'div.flash-progress': 3.68 }],
  ['contraste', 'rlc-simu', 'clair', '*', { 'span.lbl': 3.54 }],
  ['contraste', 'tiroir', '*', '*', { 'button.mob-mat-btn': 3.18 }],
  ['contraste', 'tiroir', 'clair', '*', { '#mob-drawer-close': 4.09 }],
  // — Taille du texte (px) —
  ['taille', 'aujourdhui', '*', '*', { '#today-date': 10.56, 'span.due-sub': 11.52, 'span.mob-filter-tag': 10.24, 'span.today-label': 10.24 }],
  ['taille', 'bilan', '*', '*', { 'div.m-name': 9.6, 'div.m-sub': 11.52, 'span.c-mat': 9.92, 'span.c-revoir': 11.52, 'span.dash-section-label': 9.92 }],
  ['taille', 'chapitres', '*', '*', { 'span.cpg-dir': 10.24, 'span.num': 11.2 }],
  ['taille', 'chapitres', '*', 'ordi', { '#rev-badge': 9.92, '#search-btn kbd': 9.6, '#theme-label': 11.2, 'div.eyebrow': 11.2, 'span.ctb-sub': 10.88, 'span.hdr-btn-label': 11.2 }],
  ['taille', 'chapitres', '*', 'tel', { '#rev-badge-mob': 9.92, 'button.tab': 11.52 }],
  ['taille', 'maxwell-cours', '*', 'ordi', { 'span.yr2a': 8.92 }],
  ['taille', 'maxwell-cours', '*', 'tel', { 'text.lab-accent': 11.92, 'text.lab-accent2': 11.92, 'text.lab-it': 11.92, 'text.lab-muted': 10.54 }],
  ['taille', 'menu-plus', '*', 'ordi', { '#backup-btn': 11.52, '#flag-btn': 11.52, '#formula-btn': 11.52, '#print-btn': 11.52, '#today-btn': 11.52, 'button.hdr-more-item': 11.52, 'span.read-size-val': 11.2 }],
  ['taille', 'quiz', '*', '*', { '#qs-acquis': 11.2, '#qs-hes': 11.2, '#qs-rev': 11.2, '#qs-skip': 11.2, '#quiz-chapter-badge': 10.4, '#quiz-goto-btn': 11.2, '#quiz-progress-text': 11.52, 'span.ic-lbl': 11.2, 'span.quiz-card-tag': 10.4, 'span.quiz-score-item.score-acquis': 11.2, 'span.quiz-score-item.score-hes': 11.2, 'span.quiz-score-item.score-rev': 11.2, 'span.quiz-score-item.score-skip': 11.2 }],
  ['taille', 'quiz', '*', 'ordi', { 'button.quiz-btn-reread kbd': 10.4, 'button.quiz-rate-btn.rate-acq kbd': 10.4, 'button.quiz-rate-btn.rate-hes kbd': 10.4, 'button.quiz-rate-btn.rate-rev kbd': 10.4 }],
  ['taille', 'quiz', '*', 'tel', { 'button.quiz-rate-btn.rate-acq': 11.52, 'button.quiz-rate-btn.rate-hes': 11.52, 'button.quiz-rate-btn.rate-rev': 11.52 }],
  ['taille', 'recherche', '*', '*', { 'div.search-group-label': 9.6, 'div.search-hint-bar span': 10.4, 'div.sr-suggest': 11.2, 'div.sr-suggest a': 11.2, 'span.sr-badge.sr-b-cours': 9.92, 'span.sr-badge.sr-b-def': 9.92, 'span.sr-badge.sr-b-exo': 9.92, 'span.sr-badge.sr-b-flash': 9.92, 'span.sr-badge.sr-b-meth': 9.92, 'span.sr-meta': 10.88 }],
  ['taille', 'rlc-cours maxwell-cours', '*', '*', { 'span.label': 11.2 }],
  ['taille', 'rlc-cours maxwell-cours slci-cours', '*', '*', { 'div.def-box::before': 9.92, 'div.prop-box::before': 9.92 }],
  ['taille', 'rlc-cours maxwell-cours slci-cours', '*', 'ordi', { 'span.toc-title': 11.52 }],
  ['taille', 'rlc-exos', '*', '*', { 'p.exo-part': 11.52, 'span.diff': 11.2 }],
  ['taille', 'rlc-flash anglais-flash', '*', '*', { 'button.flash-reset': 10.88, 'div.flash-hint': 11.2, 'span.tag': 11.2 }],
  ['taille', 'rlc-meth', '*', '*', { 'div.method-box::before': 9.92, 'span.step': 11.2 }],
  ['taille', 'rlc-simu', '*', '*', { 'span.lbl': 11.2 }],
  ['taille', 'tiroir', '*', '*', { 'button.mob-mat-btn': 10.88, 'button.mob-subdomain-label.mob-sub-toggle': 10.24, 'span.mob-filter-tag.mt-anglais': 10.24, 'span.mob-filter-tag.mt-si': 10.24, 'span.mob-subdomain-label.mob-drawer-section': 10.24, 'span.sub-chev': 9.6, 'span.sub-count': 10.56 }],
  // — Débordement horizontal (bord droit, px) —
  ['debordement', 'rlc-cours', '*', 'tel', { '#mob-header': 415, 'div.course-section li mjx-container': 414, 'page (scrollWidth)': 415 }],
  // — Cibles tactiles < 44 px (côté, px) —
  ['cible44', 'anglais-flash', '*', 'tel', { 'button.flash-tts-btn': 40 }],
  ['cible44', 'aujourdhui', '*', 'tel', { '#today-close': 15 }],
  ['cible44', 'bilan', '*', 'tel', { '#dash-close-btn': 15, 'button.dash-chap': 38.2 }],
  ['cible44', 'quiz', '*', 'tel', { '#quiz-flag-btn': 28.7, '#quiz-goto-btn': 28.7, 'button.quiz-btn-reread': 34, 'button.quiz-close': 25.8 }],
  ['cible44', 'rlc-exos', '*', 'tel', { 'button.toggle-sol': 34 }],
  ['cible44', 'rlc-flash anglais-flash', '*', 'tel', { 'button.flash-course-link': 32, 'button.flash-flag-btn': 28.2, 'button.flash-reset': 27.2 }],
  ['cible44', 'rlc-simu', '*', 'tel', { '#C': 16, '#L': 16, '#R': 16 }],
  ['cible44', 'tiroir', '*', 'tel', { '#mob-drawer-close': 27.4, '#mob-filter': 40, 'button.mob-subdomain-label.mob-sub-toggle': 40 }],
];

/* Tolérance sur la valeur d'un constat toléré (instabilités de rendu, polices) */
const MARGES = { contraste: 0.05, taille: 0.3, debordement: 12, cible24: 2, cible44: 2 };
/* Sens de chaque mesure : 'min' = plus petit est pire (contraste, tailles) ; 'max' = plus grand est pire */
const SENS = { contraste: 'min', taille: 'min', debordement: 'max', cible24: 'min', cible44: 'min' };
const LIBELLES = {
  contraste: 'contraste du texte ≥ 4,5:1 (3:1 si grand texte)',
  taille: 'taille du texte ≥ 12 px',
  debordement: 'aucun débordement horizontal',
  cible24: 'cibles tactiles ≥ 24 px ou assez espacées (WCAG 2.5.8)',
  cible44: 'cibles tactiles ≥ 44 px (confort au doigt, WCAG 2.5.5)',
};

const APPAREILS = [
  { nom: 'ordi', mobile: false, largeur: 1440, hauteur: 900 },
  { nom: 'tel', mobile: true, largeur: 390, hauteur: 844 },
];
const THEMES = ['clair', 'sombre'];

/* ---------- Écrans mesurés ----------
   chap/onglet : chapitre affiché (navigateTo) ; racine : zone mesurée (body
   par défaut ; une fenêtre ouverte est mesurée seule, sans la page derrière,
   ouverte au-dessus de rlc/meth, qui ne déborde pas à 390 px : sinon la page
   élargit la zone d'affichage du téléphone et toutes les fenêtres avec elle) ;
   preparer(page, app) : action qui ouvre l'écran, renvoie la liste des
   problèmes (vide = écran prêt). */
const ECRANS = [
  { nom: 'rlc-cours', chap: 'rlc', onglet: 'cours' },
  { nom: 'rlc-meth', chap: 'rlc', onglet: 'meth' },
  { nom: 'rlc-simu', chap: 'rlc', onglet: 'simu' },
  { nom: 'rlc-flash', chap: 'rlc', onglet: 'flash' },
  { nom: 'rlc-exos', chap: 'rlc', onglet: 'exos', preparer: deplierSolution },
  { nom: 'maxwell-cours', chap: 'maxwell', onglet: 'cours' },   // 2ᵉ année
  { nom: 'slci-cours', chap: 'slci', onglet: 'cours' },         // SI (<main id="si-content">)
  { nom: 'anglais-flash', chap: 'anglais', onglet: 'flash' },   // 1er chapitre d'anglais de CHAPTERS
  { nom: 'tiroir', chap: 'rlc', onglet: 'meth', racine: '#mob-drawer', preparer: ouvrirTiroir },
  { nom: 'recherche', chap: 'rlc', onglet: 'meth', racine: '#search-overlay', preparer: ouvrirRecherche },
  { nom: 'quiz', chap: 'rlc', onglet: 'meth', racine: '#quiz-overlay', preparer: ouvrirQuiz },
  { nom: 'bilan', chap: 'rlc', onglet: 'meth', racine: '#dash-overlay', preparer: ouvrirBilan },
  { nom: 'aujourdhui', chap: 'rlc', onglet: 'meth', racine: '#today-overlay', preparer: ouvrirAujourdhui },
  { nom: 'menu-plus', chap: 'rlc', onglet: 'meth', racine: '#more-menu', ordinateurSeul: true, preparer: ouvrirMenuPlus },
  // Coquille de la refonte : menu Réviser, sélecteur de thème, feuille ⋯ du téléphone, Sommaire de la matière
  { nom: 'menu-reviser', chap: 'rlc', onglet: 'meth', racine: '#study-menu', ordinateurSeul: true, preparer: ouvrirMenuReviser },
  { nom: 'theme', chap: 'rlc', onglet: 'meth', racine: '#theme-pop', ordinateurSeul: true, preparer: ouvrirSelecteurTheme },
  { nom: 'feuille-plus', chap: 'rlc', onglet: 'meth', racine: '#mob-more-menu', telephoneSeul: true, preparer: ouvrirFeuillePlus },
  { nom: 'sommaire', chap: 'rlc', onglet: 'meth', preparer: ouvrirSommaire },
];

/* Decks dont la progression est semée (Bilan, Aujourd'hui, badge « à réviser ») */
const DECKS_SEMES = ['rlc', 'mxw', 'slci', 'og', 'cpx', 'enus'];

/* ---------- Préparation des écrans (exécutées dans l'ordre d'ECRANS) ---------- */
const estOuvert = (page, sel) => page.evaluate(s => { const e = document.querySelector(s); return !!(e && e.classList.contains('open')); }, sel);
async function cliquer(page, sel) { await page.locator(sel).first().click({ timeout: 5000 }); }

async function deplierSolution(page) {
  const ok = await page.evaluate(() => {
    const b = document.querySelector('#rlc-exos .toggle-sol');
    if (!b) return false;
    const sol = b.nextElementSibling;
    if (!(sol && sol.classList.contains('shown'))) b.click();   // déjà dépliée au passage précédent (autre thème)
    if (sol) sol.scrollIntoView({ block: 'start' });
    return !!(sol && sol.classList.contains('shown'));
  });
  await pause(300);
  return ok ? [] : ['aucune solution dépliable dans rlc-exos (.toggle-sol)'];
}
async function ouvrirTiroir(page, app) {
  // À partir de 1200 px, la navigation est une barre latérale PERMANENTE (#nav-toggle-btn la
  // replie ou l'affiche) : on vérifie qu'elle est affichée ; en dessous, c'est un tiroir
  // (page « Chapitres » plein écran au téléphone) qu'on ouvre.
  const laterale = await page.evaluate(() => matchMedia('(min-width:1200px)').matches);
  if (laterale) {
    if (await page.evaluate(() => document.documentElement.classList.contains('nav-replie'))) await cliquer(page, '#nav-toggle-btn');
    await pause(300);
    const vis = await page.evaluate(() => { const d = document.getElementById('mob-drawer'); const r = d.getBoundingClientRect();
      return d.checkVisibility() && r.width > 200 && r.left >= 0 && document.querySelectorAll('#mob-chap-list .mob-chap-row').length > 0; });
    return vis ? [] : ['la barre latérale des chapitres n\'est pas affichée'];
  }
  await cliquer(page, app.mobile ? '#mob-menu-btn' : '#nav-toggle-btn');
  await pause(450);
  return (await estOuvert(page, '#mob-drawer')) ? [] : ['le tiroir ne s\'ouvre pas'];
}
async function ouvrirRecherche(page, app) {
  await cliquer(page, app.mobile ? '#mob-search-btn' : '#search-btn');
  await pause(250);
  if (!(await estOuvert(page, '#search-overlay'))) return ['la recherche ne s\'ouvre pas'];
  await page.fill('#search-input', 'fourier');
  await pause(500);
  const n = await page.evaluate(() => document.querySelectorAll('#search-results .search-result').length);
  return n ? [] : ['recherche « fourier » : aucun résultat'];
}
async function ouvrirQuiz(page, app) {
  // Même tirage à chaque lancement (graine), et physique seule : si les decks changent, la
  // carte tirée change, mais pas la matière (couleur du badge de chapitre)
  await page.evaluate(() => { window.__visuelGraine(11); Store.setJSON('quizConfig', { mats: ['physique'] }); });
  if (app.mobile) { await cliquer(page, '#mob-more-btn'); await pause(200); await cliquer(page, '#mob-quiz-btn'); }
  else { await cliquer(page, '#study-btn'); await pause(200); await cliquer(page, '#quiz-btn'); }
  await pause(400);
  if (!(await estOuvert(page, '#quiz-overlay'))) return ['le quiz ne s\'ouvre pas'];
  await cliquer(page, '#quiz-start-btn');
  await pause(400);
  await cliquer(page, '#quiz-reveal-btn');   // réponse et boutons de notation visibles
  await pause(700);                          // demi-tour de la carte
  const q = await page.evaluate(() => getComputedStyle(document.getElementById('quiz-screen-question')).display !== 'none'
    && !!document.getElementById('quiz-question-text').textContent.trim());
  return q ? [] : ['l\'écran question du quiz ne s\'affiche pas'];
}
async function ouvrirBilan(page, app) {
  if (app.mobile) { await cliquer(page, '#mob-more-btn'); await pause(200); await cliquer(page, '#mob-dash-btn'); }
  else await cliquer(page, '#dash-btn');
  await pause(500);
  return (await estOuvert(page, '#dash-overlay')) ? [] : ['le Bilan ne s\'ouvre pas'];
}
async function ouvrirAujourdhui(page) {
  await page.evaluate(() => window.todayOpen());
  await pause(400);
  return (await estOuvert(page, '#today-overlay')) ? [] : ['l\'écran Aujourd\'hui ne s\'ouvre pas (window.todayOpen)'];
}
async function ouvrirMenuPlus(page) {
  await cliquer(page, '#more-btn');
  await pause(250);
  return (await estOuvert(page, '#more-menu')) ? [] : ['le menu Plus ne s\'ouvre pas'];
}

async function ouvrirMenuReviser(page) {
  await cliquer(page, '#study-btn');
  await pause(250);
  return (await estOuvert(page, '#study-menu')) ? [] : ['le menu Réviser ne s\'ouvre pas'];
}
async function ouvrirSelecteurTheme(page) {
  await cliquer(page, '#theme-btn');
  await pause(300);
  return (await page.evaluate(() => { const p = document.getElementById('theme-pop'); return !!(p && !p.hidden); })) ? [] : ['le sélecteur de thème (#theme-pop) ne s\'ouvre pas'];
}
async function ouvrirFeuillePlus(page) {
  await cliquer(page, '#mob-more-btn');
  await pause(450);
  return (await estOuvert(page, '#mob-more-menu')) ? [] : ['la feuille ⋯ (#mob-more-menu) ne s\'ouvre pas'];
}
async function ouvrirSommaire(page) {
  // Lien profond du Sommaire de la matière (comme un favori ou le bouton précédent)
  await page.evaluate(() => { location.hash = '#sommaire/physique'; });
  await pause(500);
  return (await page.evaluate(() => { const s = document.getElementById('sommaire-matiere'); return !!(s && !s.hidden && s.querySelector('.pcard')); }))
    ? [] : ['le Sommaire de la matière (#sommaire/physique) ne s\'affiche pas'];
}

/* Referme tout ce qui peut rester ouvert entre deux écrans (Échap, puis les
   fermetures du site), et renvoie ce qui est resté ouvert. */
async function toutFermer(page) {
  await page.keyboard.press('Escape').catch(() => {});
  await pause(120);
  return page.evaluate(() => {
    const d = document.getElementById('mob-drawer');
    if (d && d.classList.contains('open')) document.getElementById('mob-drawer-close').click();
    const q = document.getElementById('quiz-overlay');
    if (q && q.classList.contains('open') && window.quizClose) window.quizClose();
    document.querySelectorAll('.dash-overlay.open').forEach(o => o.classList.remove('open'));
    const s = document.getElementById('search-overlay');
    if (s && s.classList.contains('open')) document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
    return Array.from(document.querySelectorAll('#mob-drawer.open, .quiz-overlay.open, .search-overlay.open, .dash-overlay.open, .hdr-more-menu.open, #mob-more-menu.open'))
      .map(e => '#' + e.id);
  });
}

/* Attend la fin du rendu : formules MathJax de la zone, polices */
async function attendreRendu(page, idZone) {
  if (idZone) await etatMathJax(page, idZone, 4000);
  await page.evaluate(async () => {
    try { if (window.MathJax && MathJax.startup && MathJax.startup.promise) await MathJax.startup.promise; } catch (e) { /* ignoré */ }
    await document.fonts.ready;
  });
  await pause(150);
}

/* ============================================================
   Mesure d'un écran — code exécuté DANS la page (autonome : sérialisé
   par page.evaluate). o = { racines: [sélecteurs], mobile }.
   ============================================================ */
function mesurerEcran(o) {
  const t0 = performance.now();
  const W = document.documentElement.clientWidth;
  const sx = window.scrollX, sy = window.scrollY;
  const racines = o.racines.map(s => document.querySelector(s)).filter(Boolean);
  const prefixes = new Set(typeof CHAPTERS !== 'undefined' ? CHAPTERS.map(c => c.prefix) : []);
  const stats = { textes: 0, formules: 0, generes: 0, champs: 0, elements: 0, cibles: 0, inactifs: 0, ciblesEnLigne: 0 };
  const constats = new Map(), nonEvalues = new Map();

  /* ---- Sélecteur lisible : classes (hors classes d'état), id stable, ou balise
     précédée de l'ancêtre le plus proche qui porte une classe / un id ---- */
  const ETAT = /^(active|open|shown|flipped|flipping|show|sel|selected|current|visible|done|on|is-[\w-]+|has-[\w-]+)$/;
  const classes = e => Array.from(e.classList || []).filter(c => !ETAT.test(c));
  function idLisible(e) {
    const id = e.id;
    if (!id || /\d{4,}/.test(id)) return null;   // pas d'id, ou id généré
    const i = id.indexOf('-');
    if (i > 0 && prefixes.has(id.slice(0, i))) return '#*' + id.slice(i);   // id propre à un chapitre : rlc-stats → #*-stats
    return '#' + id;
  }
  function etiquette(e) {
    const tag = e.tagName.toLowerCase(), cl = classes(e).slice(0, 2);
    if (cl.length) return tag + cl.map(c => '.' + c).join('');
    const id = idLisible(e);
    return id ? tag + id : tag;
  }
  function decrire(e) {
    // formule : située par son contenant (div.notice mjx-container, div.course-section p mjx-container…)
    if (e.tagName === 'MJX-CONTAINER' && e.parentElement) return decrire(e.parentElement) + ' mjx-container';
    const id = idLisible(e);
    if (id && id[1] !== '*') return id;
    if (classes(e).length) return etiquette(e);
    let a = e.parentElement, k = 0;
    while (a && a !== document.body && k < 5 && !idLisible(a) && !classes(a).length) { a = a.parentElement; k++; }
    if (!a || a === document.body || a === document.documentElement) return etiquette(e);
    const ida = idLisible(a);
    return (ida && ida[1] !== '*' ? ida : etiquette(a)) + ' ' + etiquette(e);
  }

  /* ---- Constats regroupés par (mesure, sélecteur, seuil) : pire valeur + exemples ---- */
  function constater(mesure, selecteur, valeur, seuil, exemple, pireEstMin) {
    const cle = mesure + '|' + selecteur + '|' + seuil;
    let c = constats.get(cle);
    if (!c) { c = { mesure, selecteur, valeur, seuil, n: 0, exemples: [] }; constats.set(cle, c); }
    c.n++;
    if (pireEstMin ? valeur < c.valeur : valeur > c.valeur) c.valeur = valeur;
    if (c.exemples.length < 4) c.exemples.push(exemple);
    else if (pireEstMin ? valeur <= c.exemples[0].valeur : valeur >= c.exemples[0].valeur) c.exemples[3] = exemple;
    c.exemples.sort((a, b) => (pireEstMin ? a.valeur - b.valeur : b.valeur - a.valeur));
  }
  const extrait = s => String(s || '').replace(/\s+/g, ' ').trim().slice(0, 50);

  /* ---- Styles, rectangles (mis en cache : la page ne bouge pas pendant la mesure) ---- */
  const cacheS = new Map(), cacheR = new Map();
  const cs = e => { let s = cacheS.get(e); if (!s) { s = getComputedStyle(e); cacheS.set(e, s); } return s; };
  const rect = e => { let r = cacheR.get(e); if (!r) { r = e.getBoundingClientRect(); cacheR.set(e, r); } return r; };

  /* ---- Couleurs : rgb()/rgba() lus directement, toute autre syntaxe (oklch,
     color-mix…) convertie par un canvas de 1 pixel ---- */
  const cv = document.createElement('canvas'); cv.width = cv.height = 1;
  const c2 = cv.getContext('2d', { willReadFrequently: true });
  const cacheC = new Map();
  function couleur(s) {
    if (!s) return null;
    let r = cacheC.get(s);
    if (r !== undefined) return r;
    const m = /^rgba?\(([^)]+)\)$/.exec(s);
    if (m) { const v = m[1].split(/[\s,/]+/).filter(Boolean).map(parseFloat); r = { r: v[0], g: v[1], b: v[2], a: v.length > 3 ? v[3] : 1 }; }
    else if (s === 'transparent') r = { r: 0, g: 0, b: 0, a: 0 };
    else {
      c2.clearRect(0, 0, 1, 1); c2.fillStyle = 'rgba(0,0,0,0)'; c2.fillStyle = s; c2.fillRect(0, 0, 1, 1);
      const d = c2.getImageData(0, 0, 1, 1).data;
      r = { r: d[0], g: d[1], b: d[2], a: d[3] / 255 };
    }
    cacheC.set(s, r);
    return r;
  }
  /* Composition « source par-dessus destination » (couleurs non prémultipliées) */
  const VIDE = { r: 0, g: 0, b: 0, a: 0 }, BLANC = { r: 255, g: 255, b: 255, a: 1 };
  function sur(s, d) {
    const a = s.a + d.a * (1 - s.a);
    if (a <= 0) return VIDE;
    const k = d.a * (1 - s.a);
    return { r: (s.r * s.a + d.r * k) / a, g: (s.g * s.a + d.g * k) / a, b: (s.b * s.a + d.b * k) / a, a };
  }
  const lin = x => { x /= 255; return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4); };
  const lum = c => 0.2126 * lin(c.r) + 0.7152 * lin(c.g) + 0.0722 * lin(c.b);
  const rapport = (a, b) => { const la = lum(a), lb = lum(b); return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05); };
  const txt = c => 'rgb(' + Math.round(c.r) + ', ' + Math.round(c.g) + ', ' + Math.round(c.b) + ')';

  /* Quadrillage de la page : linear-gradient(<couleur> 1px, transparent 1px), en
     lignes de 1 à 2 px : négligeable pour la lisibilité (évalué contre la couleur de fond). */
  const COUCHE_FINE = /^linear-gradient\((?:[\d.]+deg,\s*|to [a-z ]+,\s*)?(?:rgba?\([^)]*\)|[a-z]+)\s+[0-2](?:\.\d+)?px,\s*(?:transparent|rgba\(0, 0, 0, 0\))\s+[0-2](?:\.\d+)?px\)$/;
  const motifFin = img => img.split(/,\s*(?=linear-gradient)/).every(c => COUCHE_FINE.test(c.trim()));
  /* Petite icône non répétée (≤ 48 px : pictogramme des étiquettes DÉFINITION…,
     posé à côté du texte grâce à un retrait) : ne passe pas derrière le texte. */
  const icone = s => /^url\([^)]*\)$/.test(s.backgroundImage) && s.backgroundRepeat === 'no-repeat'
    && /^[\d.]+px [\d.]+px$/.test(s.backgroundSize) && s.backgroundSize.split(' ').every(v => parseFloat(v) <= 48);
  const fondIgnore = s => motifFin(s.backgroundImage) || icone(s);

  /* Couleurs finales d'un texte et de son fond, en peignant la chaîne des
     ancêtres comme le navigateur : chaque ancêtre peint son fond, puis ses
     descendants par-dessus, et son opacité s'applique au groupe entier (fond
     ET texte, sur ce qui est peint derrière lui). Un texte généré (ps : style
     du ::before / ::after) peint d'abord le fond du pseudo-élément.
     → { texte, fond } ou { nonEvalue, source } si une image / un dégradé
     transparaît derrière le texte. */
  function couleursFinales(el, fg, ps, suffixe) {
    let gTexte = fg, gFond = VIDE, couvert = false;
    const peindre = s => {   // une couche : fond de s sous ce qui est déjà peint, puis son opacité → type de fond non évaluable, ou null
      const img = s.backgroundImage, op = parseFloat(s.opacity);
      if (!couvert && img && img !== 'none' && !fondIgnore(s)) return /url\(/.test(img) ? 'image' : 'dégradé';
      const c = couleur(s.backgroundColor) || VIDE;
      gTexte = sur(gTexte, c);
      gFond = sur(gFond, c);
      if (op < 1) { gTexte = Object.assign({}, gTexte, { a: gTexte.a * op }); gFond = Object.assign({}, gFond, { a: gFond.a * op }); }
      // couvert : un fond opaque sans opacité < 1 depuis → les couches plus bas ne transparaissent plus
      couvert = op >= 1 && (couvert || c.a >= 0.999);
      return null;
    };
    if (ps) { const t = peindre(ps); if (t) return { nonEvalue: t, source: decrire(el) + suffixe }; }
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      const t = peindre(cs(e));
      if (t) return { nonEvalue: t, source: decrire(e) };
    }
    return { texte: sur(gTexte, BLANC), fond: sur(gFond, BLANC) };   // toile du navigateur
  }

  /* Opacité cumulée des ancêtres */
  const cacheO = new Map();
  function opacite(e) {
    if (!e || e.nodeType !== 1) return 1;
    let v = cacheO.get(e);
    if (v === undefined) { v = (parseFloat(cs(e).opacity) || 0) * opacite(e.parentElement); cacheO.set(e, v); }
    return v;
  }
  /* Zone de rognage des ancêtres : avecDefilement=false → overflow hidden/clip
     seulement (le texte d'une zone défilante reste atteignable) ; true → aussi
     auto/scroll (pour les débordements : une table dans une zone défilante ne
     fait pas déborder la page). html/body ne rognent pas. */
  const INF = { l: -1e9, t: -1e9, r: 1e9, b: 1e9 };
  function fabriqueRognage(re) {
    const cache = new Map();
    const f = e => {
      if (!e || e.nodeType !== 1 || e === document.body || e === document.documentElement) return INF;
      let v = cache.get(e);
      if (v) return v;
      const s = cs(e);
      v = s.position === 'fixed' ? INF : f(e.parentElement);
      const ox = re.test(s.overflowX), oy = re.test(s.overflowY);
      if (ox || oy) {
        const r = rect(e);
        v = { l: ox ? Math.max(v.l, r.left) : v.l, r: ox ? Math.min(v.r, r.right) : v.r,
          t: oy ? Math.max(v.t, r.top) : v.t, b: oy ? Math.min(v.b, r.bottom) : v.b };
      }
      cache.set(e, v);
      return v;
    };
    return f;
  }
  const rognage = fabriqueRognage(/^(hidden|clip)$/);
  const rognageDefil = fabriqueRognage(/^(hidden|clip|auto|scroll)$/);
  const intersecte = (r, k) => Math.min(r.right, k.r) - Math.max(r.left, k.l) > 1 && Math.min(r.bottom, k.b) - Math.max(r.top, k.t) > 1;
  /* Face cachée d'une carte retournée (backface-visibility:hidden tournée vers l'arrière) */
  const cacheD = new Map();
  function deDos(e) {
    if (!e || e.nodeType !== 1 || e === document.body) return false;
    let v = cacheD.get(e);
    if (v !== undefined) return v;
    v = deDos(e.parentElement);
    if (!v && cs(e).backfaceVisibility === 'hidden') {
      const mat = x => (cs(x).transform && cs(x).transform !== 'none' ? new DOMMatrix(cs(x).transform) : new DOMMatrix());
      let m = mat(e);
      for (let p = e.parentElement; p && cs(p).transformStyle === 'preserve-3d'; p = p.parentElement) m = mat(p).multiply(m);
      v = m.m33 < 0;
    }
    cacheD.set(e, v);
    return v;
  }
  /* Élément réellement visible : rendu, visibility, opacité, face, rognage, dans la page.
     Une boîte (ou une partie visible) de 1 px au plus ne compte pas : motif « masqué
     visuellement » (1 × 1 px + overflow:hidden + clip), lu par les lecteurs d'écran seulement. */
  function visible(e, r) {
    const s = cs(e);
    if (s.visibility !== 'visible' || opacite(e) < 0.05 || deDos(e)) return false;
    if (r.width <= 1 || r.height <= 1) return false;
    if (r.right + sx <= 0 || r.bottom + sy <= 0) return false;   // hors de la page (lien d'évitement…)
    return intersecte(r, rognage(e));
  }

  /* ---- Parcours des zones mesurées (sous-arbres non rendus écartés d'emblée) ---- */
  const EXCLUS = new Set(['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE', 'CANVAS', 'SELECT', 'TEXTAREA', 'IFRAME', 'MJX-ASSISTIVE-MML']);
  const textes = [], formules = [], elements = [];
  for (const racine of racines) {
    if (!racine.checkVisibility()) continue;
    elements.push(racine);
    const w = document.createTreeWalker(racine, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, {
      acceptNode(n) {
        if (n.nodeType === 3) return /\S/.test(n.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
        if (EXCLUS.has(n.tagName.toUpperCase())) return NodeFilter.FILTER_REJECT;
        // non rendu → sous-arbre écarté ; sauf display:contents (pas de boîte, mais des enfants rendus)
        if (!n.checkVisibility()) return cs(n).display === 'contents' ? NodeFilter.FILTER_SKIP : NodeFilter.FILTER_REJECT;
        elements.push(n);
        if (n.tagName === 'MJX-CONTAINER') { formules.push(n); return NodeFilter.FILTER_REJECT; }
        return NodeFilter.FILTER_SKIP;
      },
    });
    while (w.nextNode()) textes.push(w.currentNode);
  }
  stats.elements = elements.length;

  /* ---- 1) et 2) Contraste et taille de chaque texte / formule / champ ---- */
  const rg = document.createRange();
  /* Taille rendue (px CSS) ; un texte SVG est mis à l'échelle par le viewBox (getScreenCTM) ;
     ps : style du pseudo-élément pour un texte généré */
  function mesurerTaille(el, sel, texte, ps) {
    let taille = parseFloat((ps || cs(el)).fontSize);
    const m = el instanceof SVGElement && el.getScreenCTM ? el.getScreenCTM() : null;
    if (m) taille *= Math.sqrt(Math.abs(m.a * m.d - m.b * m.c));
    taille = Math.round(taille * 100) / 100;
    if (taille < 12) constater('taille', sel, taille, 12, { valeur: taille, texte: extrait(texte) }, true);
    return taille;
  }
  /* suffixe : '::placeholder', '::before'… ajouté au sélecteur ; ps : style du ::before / ::after
     d'un texte généré (taille, graisse et fond lus sur le pseudo-élément) */
  function mesurerTexte(el, r, couleurTexte, texte, suffixe, ps) {
    const s = ps || cs(el);
    const sel = decrire(el) + (suffixe || '');
    const taille = mesurerTaille(el, sel, texte, ps), gras = parseInt(s.fontWeight, 10) >= 700;
    if (el.closest(':disabled, [aria-disabled="true"]')) { stats.inactifs++; return; }
    const fg = couleur(couleurTexte);
    if (!fg || fg.a === 0) return;   // texte transparent (dégradé détouré…) : rien à mesurer
    const f = couleursFinales(el, fg, ps, suffixe);
    if (f.nonEvalue) {
      const cle = sel + '|' + f.source;
      const ne = nonEvalues.get(cle) || { selecteur: sel, fond: f.source, type: f.nonEvalue, n: 0, texte: extrait(texte) };
      ne.n++;
      nonEvalues.set(cle, ne);
      return;
    }
    const ratio = Math.round(rapport(f.texte, f.fond) * 100) / 100;
    const seuil = (taille >= 24 || (taille >= 18.66 && gras)) ? 3 : 4.5;
    if (ratio < seuil) {
      constater('contraste', sel, ratio, seuil, { valeur: ratio, texte: extrait(texte), couleur: txt(f.texte), fond: txt(f.fond),
        taille: Math.round(taille * 10) / 10, gras }, true);
    }
  }
  for (const t of textes) {
    const el = t.parentElement;
    if (!el) continue;
    rg.selectNodeContents(t);
    const r = rg.getBoundingClientRect();
    if (!visible(el, r)) continue;
    stats.textes++;
    const s = cs(el);
    const svg = el instanceof SVGElement;
    // texte SVG : couleur = remplissage ; un fond fait de formes SVG n'est pas évalué
    if (svg) {
      if (!s.fill || s.fill === 'none' || /url\(/.test(s.fill)) continue;
      const doc = el.ownerSVGElement, rr = r;
      const formes = doc ? Array.from(doc.querySelectorAll('rect,circle,ellipse,polygon,path')).filter(fm => {
        const fs = cs(fm);
        if (!fs.fill || fs.fill === 'none' || parseFloat(fs.fillOpacity) === 0) return false;
        if (!(fm.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING)) return false;   // peinte après le texte
        const b = rect(fm);
        return b.left < rr.right && b.right > rr.left && b.top < rr.bottom && b.bottom > rr.top;
      }) : [];
      if (formes.length) {
        const sel = decrire(el), cle = sel + '|svg';
        const ne = nonEvalues.get(cle) || { selecteur: sel, fond: decrire(formes[formes.length - 1]), type: 'formes SVG', n: 0, texte: extrait(t.nodeValue) };
        ne.n++;
        nonEvalues.set(cle, ne);
        mesurerTaille(el, sel, t.nodeValue);
        continue;
      }
      mesurerTexte(el, r, s.fill, t.nodeValue);
      continue;
    }
    mesurerTexte(el, r, s.webkitTextFillColor || s.color, t.nodeValue);
  }
  for (const m of formules) {
    const r = rect(m);
    if (!visible(m, r)) continue;
    stats.formules++;
    mesurerTexte(m, r, cs(m).color, '[formule] ' + (m.textContent || ''));
  }
  // Textes générés par le CSS : ::before / ::after à contenu textuel (content:"DÉFINITION"…),
  // mesurés sur leur propre style (hors glyphes MathJax, rendus eux aussi par des ::before)
  const genere = c => (c && c !== 'none' && c !== 'normal' ? (c.match(/"(?:[^"\\]|\\.)*"/g) || []).map(x => x.slice(1, -1).replace(/\\(.)/g, '$1')).join('') : '');
  for (const e of elements) {
    if (e.tagName.startsWith('MJX-')) continue;
    for (const pseudo of ['::before', '::after']) {
      const ps = getComputedStyle(e, pseudo), t = genere(ps.content);
      if (!/\S/.test(t) || ps.display === 'none' || ps.visibility !== 'visible' || parseFloat(ps.opacity) < 0.05) continue;
      const r = rect(e);
      if (!visible(e, r)) continue;
      stats.generes++;
      mesurerTexte(e, r, ps.webkitTextFillColor || ps.color, t, pseudo, ps);
    }
  }
  // Champs de saisie : valeur tapée, sinon texte indicatif (placeholder)
  for (const racine of racines) {
    racine.querySelectorAll('input:not([type]), input[type="text"], input[type="search"], input[type="number"], input[type="email"], textarea').forEach(inp => {
      if (!inp.checkVisibility()) return;
      const r = rect(inp);
      if (!visible(inp, r)) return;
      stats.champs++;
      if (inp.value) mesurerTexte(inp, r, cs(inp).color, inp.value);
      else if (inp.placeholder) mesurerTexte(inp, r, getComputedStyle(inp, '::placeholder').color, inp.placeholder, '::placeholder');
    });
  }

  /* ---- 3) Débordement horizontal ---- */
  const sw = document.scrollingElement.scrollWidth;
  if (sw > W + 1) constater('debordement', 'page (scrollWidth)', sw, W, { valeur: sw, texte: 'scrollWidth ' + sw + ' > ' + W }, false);
  const dansRacine = e => racines.some(r => r.contains(e));
  for (const e of elements) {
    if (e === document.body || e === document.documentElement) continue;
    const r = rect(e);
    if (r.right <= W + 1 || r.width < 1 || r.height < 1) continue;
    const s = cs(e);
    if (s.position === 'fixed' && r.left >= W) continue;   // panneau fermé, rangé hors écran
    if (s.visibility !== 'visible' || opacite(e) < 0.05 || deDos(e)) continue;
    if (rognageDefil(e.parentElement).r <= W + 1) continue;   // rogné par un ancêtre (zone défilante, overflow:hidden)
    const p = e.parentElement;
    if (p && p !== document.body && dansRacine(p) && rect(p).right > W + 1 && rognageDefil(p.parentElement).r > W + 1) continue;   // le parent dépasse : c'est lui le coupable
    let texte = (e.textContent || '').trim();
    const mc = e.closest('mjx-container');
    if (mc && window.MathJax && MathJax.startup && MathJax.startup.document) {
      try { const it = MathJax.startup.document.getMathItemsWithin(mc.parentElement).find(x => x.typesetRoot === mc); if (it) texte = 'formule ' + it.math; } catch (x) { /* ignoré */ }
    }
    constater('debordement', decrire(e), Math.round(r.right), W, { valeur: Math.round(r.right), texte: extrait(texte), largeur: Math.round(r.width) }, false);
  }

  /* ---- 4) Cibles tactiles (téléphone) ---- */
  if (o.mobile) {
    const CIBLE = 'a[href],button,input:not([type="hidden"]),select,textarea,summary,label,[role="button"],[role="link"],[role="menuitem"],[role="tab"],[role="checkbox"],[role="radio"],[role="switch"],[role="option"],[onclick],[tabindex]:not([tabindex="-1"])';
    const CONTENANT = 'a[href],button,label,summary,[role="button"],[role="link"],[role="menuitem"],[role="tab"]';
    const cibles = [];
    // cible = élément interactif par nature, ou bloc cliquable par script (curseur « main » : .reveal,
    // flashcard…) dont le parent n'a pas ce curseur (le curseur s'hérite : on garde le plus extérieur)
    const main = e => cs(e).cursor === 'pointer';
    for (const e of elements) {
      if (!e.matches(CIBLE) && !(main(e) && !(e.parentElement && main(e.parentElement)))) continue;
      if (e.tagName === 'LABEL' && !e.htmlFor && !e.querySelector('input,select,textarea')) continue;   // simple étiquette
      if (e.matches(':disabled, [aria-disabled="true"]')) continue;
      const s = cs(e);
      if (s.pointerEvents === 'none') continue;
      const r = rect(e);
      if (!visible(e, r)) continue;
      const parent = e.parentElement && e.parentElement.closest(CONTENANT);
      if (parent && dansRacine(parent)) continue;   // cible imbriquée : c'est le contenant qu'on touche
      if (s.display === 'inline' && e.parentElement && Array.from(e.parentElement.childNodes)
        .some(n => n !== e && n.nodeType === 3 && /\S/.test(n.nodeValue))) { stats.ciblesEnLigne++; continue; }   // lien dans une phrase (exempté)
      cibles.push({ e, r, cx: r.left + r.width / 2, cy: r.top + r.height / 2, cote: Math.min(r.width, r.height) });
    }
    stats.cibles = cibles.length;
    const distRect = (x, y, r) => Math.hypot(Math.max(r.left - x, 0, x - r.right), Math.max(r.top - y, 0, y - r.bottom));
    for (const c of cibles) {
      const cote = Math.round(c.cote * 10) / 10;
      const dims = Math.round(c.r.width) + '×' + Math.round(c.r.height);
      const lib = extrait(c.e.getAttribute('aria-label') || c.e.textContent || c.e.value || c.e.placeholder || '');
      if (c.cote < 44) constater('cible44', decrire(c.e), cote, 44, { valeur: cote, texte: lib, dims }, true);
      if (c.cote >= 24) continue;
      // Exception d'espacement (2.5.8) : disque de 24 px centré sur la cible
      const petite = x => x.cote < 24;
      const voisin = cibles.find(x => x !== c && !x.e.contains(c.e) && !c.e.contains(x.e)
        && (distRect(c.cx, c.cy, x.r) < 12 || (petite(x) && Math.hypot(x.cx - c.cx, x.cy - c.cy) < 24)));
      if (voisin) constater('cible24', decrire(c.e), cote, 24, { valeur: cote, texte: lib, dims, voisin: decrire(voisin.e) }, true);
    }
  }

  return {
    W, scrollWidth: sw, stats, dureeMs: Math.round(performance.now() - t0),
    constats: Array.from(constats.values()),
    nonEvalues: Array.from(nonEvalues.values()),
  };
}

/* ---------- Listes tolérées ---------- */
/* Champ « écrans » de TOLERES : '*', noms d'ECRANS, alias 'chapitres' / 'fenetres' */
const ALIAS = {
  chapitres: ECRANS.filter(e => !e.racine).map(e => e.nom),
  fenetres: ECRANS.filter(e => e.racine).map(e => e.nom),
};
const enListe = (champ, val) => champ === '*' || champ.split(/\s+/).some(m => m === val || (ALIAS[m] || []).includes(val));
const couvre = (t, c) => t[0] === c.mesure && Object.prototype.hasOwnProperty.call(t[4], c.selecteur)
  && enListe(t[1], c.ecran) && enListe(t[2], c.theme) && enListe(t[3], c.appareil);
/* Statut d'un constat : 'nouveau', 'aggrave' (couvert par TOLERES mais pire que
   la valeur tolérée) ou 'tolere' ; `ligne` = indice de la ligne qui le couvre */
function classer(c, toleres) {
  const lignes = toleres.map((t, i) => i).filter(i => couvre(toleres[i], c));
  if (!lignes.length) return { statut: 'nouveau' };
  const marge = MARGES[c.mesure] || 0;
  const ok = lignes.filter(i => {
    const pire = toleres[i][4][c.selecteur];
    return SENS[c.mesure] === 'min' ? c.valeur >= pire - marge : c.valeur <= pire + marge;
  });
  return ok.length ? { statut: 'tolere', ligne: ok[0] } : { statut: 'aggrave', ligne: lignes[0] };
}
/* Proposition de liste TOLERES couvrant tous les constats : pour chaque
   (mesure, sélecteur), écrans / thèmes / appareils où il échoue et pire valeur ;
   puis une ligne par (mesure, écrans, thèmes, appareils). */
function proposerToleres(constats, ecransParAppareil) {
  const parSel = new Map();
  for (const c of constats) {
    const cle = c.mesure + '\u0000' + c.selecteur;
    const g = parSel.get(cle) || { mesure: c.mesure, selecteur: c.selecteur, ecrans: new Set(), themes: new Set(), appareils: new Set(), pire: c.valeur };
    g.ecrans.add(c.ecran); g.themes.add(c.theme); g.appareils.add(c.appareil);
    if (SENS[c.mesure] === 'min' ? c.valeur < g.pire : c.valeur > g.pire) g.pire = c.valeur;
    parSel.set(cle, g);
  }
  const champEcrans = g => {
    const possibles = new Set([].concat(...Array.from(g.appareils).map(a => ecransParAppareil[a] || [])));
    if (Array.from(possibles).every(e => g.ecrans.has(e))) return '*';
    const reste = new Set(g.ecrans), mots = [];
    for (const [alias, liste] of Object.entries(ALIAS)) {
      const utiles = liste.filter(e => possibles.has(e));
      if (utiles.length > 1 && utiles.every(e => reste.has(e))) { mots.push(alias); utiles.forEach(e => reste.delete(e)); }
    }
    return mots.concat(ECRANS.map(e => e.nom).filter(n => reste.has(n))).join(' ');
  };
  const lignes = new Map();
  for (const g of parSel.values()) {
    const champs = [g.mesure, champEcrans(g),
      g.themes.size === THEMES.length ? '*' : Array.from(g.themes).join(' '),
      g.appareils.size === APPAREILS.length ? '*' : Array.from(g.appareils).join(' ')];
    const cle = champs.join('\u0000');
    const l = lignes.get(cle) || { champs, sels: [] };
    l.sels.push([g.selecteur, g.pire]);
    lignes.set(cle, l);
  }
  const ordre = Object.keys(SENS);
  const q = s => "'" + String(s).replace(/\\/g, '\\\\').replace(/'/g, "\\'") + "'";
  return Array.from(lignes.values())
    .sort((a, b) => ordre.indexOf(a.champs[0]) - ordre.indexOf(b.champs[0]) || a.champs[1].localeCompare(b.champs[1])
      || a.champs[2].localeCompare(b.champs[2]) || a.champs[3].localeCompare(b.champs[3]))
    .map(l => '  [' + l.champs.map(q).join(', ') + ', { '
      + l.sels.sort((x, y) => x[0].localeCompare(y[0])).map(([sel, v]) => q(sel) + ': ' + v).join(', ') + ' }],');
}
/* Sélecteurs de TOLERES qui ne couvrent plus aucun constat (à retirer de la liste) */
function toleresPerimes(toleres, constats) {
  const out = [];
  toleres.forEach((t, i) => {
    for (const sel of Object.keys(t[4])) {
      if (!constats.some(c => c.statut !== 'nouveau' && c.selecteur === sel && couvre(t, c))) out.push({ ligne: i, mesure: t[0], ecrans: t[1], themes: t[2], appareils: t[3], selecteur: sel });
    }
  });
  return out;
}

/* Regroupe des constats par (mesure, sélecteur) pour des messages compacts */
function regrouper(liste) {
  const g = new Map();
  for (const c of liste) {
    const cle = c.mesure + '|' + c.selecteur;
    const x = g.get(cle) || { mesure: c.mesure, selecteur: c.selecteur, seuil: c.seuil, valeur: c.valeur, lieux: new Set(), themes: new Set(), appareils: new Set(), n: 0, exemple: c.exemples[0], statuts: new Set() };
    x.lieux.add(c.ecran); x.themes.add(c.theme); x.appareils.add(c.appareil); x.n += c.n; x.statuts.add(c.statut);
    if (SENS[c.mesure] === 'min' ? c.valeur < x.valeur : c.valeur > x.valeur) { x.valeur = c.valeur; x.exemple = c.exemples[0]; x.seuil = c.seuil; }
    g.set(cle, x);
  }
  return Array.from(g.values());
}
const fmt = v => String(v).replace('.', ',');
function messageGroupe(x) {
  const ex = x.exemple || {};
  const unite = x.mesure === 'contraste' ? ':1' : ' px';
  const comp = SENS[x.mesure] === 'min' ? ' < ' : ' > ';
  return x.selecteur + ' : ' + fmt(x.valeur) + unite + comp + fmt(x.seuil) + unite
    + (x.statuts.has('aggrave') ? ' (AGGRAVÉ par rapport à TOLERES)' : '')
    + ' — ' + Array.from(x.lieux).join(', ') + ' [' + Array.from(x.themes).join('+') + ', ' + Array.from(x.appareils).join('+') + ']'
    + (ex.texte ? ' « ' + ex.texte + ' »' : '')
    + (ex.couleur ? ' ' + ex.couleur + ' sur ' + ex.fond : '')
    + (ex.dims ? ' ' + ex.dims + (ex.voisin ? ', trop près de ' + ex.voisin : '') : '')
    + (x.n > 1 ? ' (×' + x.n + ')' : '');
}

/* ---------- Récapitulatif lisible (visuel.md) ---------- */
function ecrireRecap(f, d) {
  const L = [];
  const echap = s => String(s == null ? '' : s).replace(/\|/g, '\\|').replace(/\n/g, ' ');
  L.push('# Suite « visuel » — récapitulatif', '');
  L.push('- Date : ' + d.date + (d.strict ? ' · **mode strict** (listes tolérées ignorées)' : ''));
  L.push('- Écrans mesurés : ' + d.ecrans.length + ' (' + APPAREILS.map(a => a.nom + ' ' + a.largeur + '×' + a.hauteur).join(', ') + ' ; thèmes ' + THEMES.join(', ') + ')');
  L.push('- Durée de la suite : ' + Math.round(d.dureeMs / 1000) + ' s', '');
  L.push('| Mesure | Constats (écran × sélecteur) | Nouveaux | Aggravés | Tolérés |', '|---|---|---|---|---|');
  for (const m of Object.keys(SENS)) {
    const l = d.constats.filter(c => c.mesure === m);
    L.push('| ' + LIBELLES[m] + ' | ' + l.length + ' | ' + l.filter(c => c.statut === 'nouveau').length + ' | '
      + l.filter(c => c.statut === 'aggrave').length + ' | ' + l.filter(c => c.statut === 'tolere').length + ' |');
  }
  L.push('');
  for (const m of Object.keys(SENS)) {
    const groupes = regrouper(d.constats.filter(c => c.mesure === m))
      .sort((a, b) => (SENS[m] === 'min' ? a.valeur - b.valeur : b.valeur - a.valeur));
    L.push('## ' + LIBELLES[m], '');
    if (!groupes.length) { L.push('Aucun constat.', ''); continue; }
    L.push('| Sélecteur | Pire valeur | Seuil | Écrans | Thèmes | Appareils | Occurrences | Exemple | Statut |', '|---|---|---|---|---|---|---|---|---|');
    for (const x of groupes) {
      const ex = x.exemple || {};
      const exemple = [ex.texte ? '« ' + ex.texte + ' »' : '', ex.couleur ? ex.couleur + ' sur ' + ex.fond : '', ex.dims || '', ex.voisin ? 'près de ' + ex.voisin : ''].filter(Boolean).join(' · ');
      L.push('| `' + echap(x.selecteur) + '` | ' + fmt(x.valeur) + ' | ' + fmt(x.seuil) + ' | ' + Array.from(x.lieux).join(', ') + ' | '
        + Array.from(x.themes).join(', ') + ' | ' + Array.from(x.appareils).join(', ') + ' | ' + x.n + ' | ' + echap(exemple) + ' | '
        + Array.from(x.statuts).join(', ') + ' |');
    }
    L.push('');
  }
  L.push('## Fonds non évalués (image, dégradé, formes SVG)', '');
  if (!d.nonEvalues.length) L.push('Aucun.', '');
  else {
    const g = new Map();
    for (const n of d.nonEvalues) {
      const cle = n.selecteur + '|' + n.fond;
      const x = g.get(cle) || { selecteur: n.selecteur, fond: n.fond, type: n.type, n: 0, lieux: new Set(), texte: n.texte };
      x.n += n.n; x.lieux.add(n.ecran + ' (' + n.theme + ', ' + n.appareil + ')');
      g.set(cle, x);
    }
    L.push('| Texte | Fond | Type | Occurrences | Écrans | Exemple |', '|---|---|---|---|---|---|');
    for (const x of g.values()) L.push('| `' + echap(x.selecteur) + '` | `' + echap(x.fond) + '` | ' + x.type + ' | ' + x.n + ' | ' + Array.from(x.lieux).slice(0, 6).join(', ') + (x.lieux.size > 6 ? '…' : '') + ' | ' + echap(x.texte) + ' |');
    L.push('');
  }
  L.push('## Sélecteurs de TOLERES plus constatés (à retirer)', '');
  if (!d.toleresNonConstates.length) L.push('Aucun.', '');
  else d.toleresNonConstates.forEach(t => L.push('- `' + echap(t.selecteur) + '` (' + t.mesure + ', écrans ' + t.ecrans + ', thèmes ' + t.themes + ', appareils ' + t.appareils + ')'));
  L.push('', '## Proposition de liste TOLERES (constats de ce lancement)', '',
    'À relire avant de la recopier en tête de `tests/suites/visuel.js` : une ligne par mesure et lieu (écrans, thèmes, appareils), chaque sélecteur avec sa pire valeur.', '',
    '```js', 'const TOLERES = [', ...d.propositionToleres, '];', '```', '');
  fs.writeFileSync(f, L.join('\n'));
}

module.exports = {
  nom: 'visuel',
  description: 'contraste, taille du texte, débordements, cibles tactiles (clair/sombre, ordinateur/téléphone)',
  delaiMax: () => 8 * 60000,

  async executer(ctx, res) {
    const t0 = Date.now();
    const strict = !!ctx.options.strict;
    const toleres = strict ? [] : TOLERES;
    if (strict) ctx.log('mode strict : listes tolérées ignorées');
    const tous = [], nonEvalues = [], ecransMesures = [], pbPreparation = [];
    const ecransParAppareil = {};

    for (const app of APPAREILS) {
      const { page, journal } = await ctx.nouvellePage({ mobile: app.mobile, largeur: app.largeur, hauteur: app.hauteur });
      // Hasard à graine fixe (ordre des flashcards, tirage du quiz) ; window.__visuelGraine(n) le réinitialise
      await page.addInitScript(() => {
        let graine = 1;
        Math.random = () => { graine = (graine * 16807) % 2147483647; return (graine - 1) / 2147483646; };
        window.__visuelGraine = n => { graine = n || 1; };
      });
      journal.lieu = 'chargement ' + app.nom;
      await page.goto(ctx.url('#rlc/cours'), { waitUntil: 'load', timeout: 60000 });
      await attendreApp(page);
      // État de flashcards semé : 1 carte sur 5 jamais vue, les autres acquises / hésitantes / à revoir, certaines dues
      const anglais = await page.evaluate(decks => {
        const jour = 86400000, maintenant = Date.now();
        for (const p of decks) {
          const cartes = window.FLASH_REGISTRY && FLASH_REGISTRY[p];
          if (!cartes) continue;
          const etat = cartes.map((_, i) => {
            const k = i % 5;
            if (k === 4) return { h: 0, o: 0, e: 0, last: null };
            const last = [2, 1, 0, 2][k];
            return { h: last === 0 ? 1 : 0, o: last === 1 ? 1 : 0, e: last === 2 ? 2 : 0, last, box: last === 2 ? 2 : (last === 1 ? 1 : 0),
              due: maintenant + (k === 2 || i % 7 === 0 ? -jour : 3 * jour) };
          });
          flashSaveState(p, cartes, etat);
          if (window.FLASH_INSTANCES && FLASH_INSTANCES[p] && FLASH_INSTANCES[p].reload) FLASH_INSTANCES[p].reload();
        }
        if (window.__updateReviseBadge) window.__updateReviseBadge();
        const a = CHAPTERS.find(c => c.matiere === 'anglais' && c.panels.includes('flash'));
        return a ? a.id : null;
      }, DECKS_SEMES);
      const ecrans = ECRANS.filter(e => !(e.ordinateurSeul && app.mobile) && !(e.telephoneSeul && !app.mobile));
      ecransParAppareil[app.nom] = ecrans.map(e => e.nom);
      let rang = 0;
      ctx.log(app.nom + ' ' + app.largeur + '×' + app.hauteur + ' : ' + ecrans.length + ' écrans × ' + THEMES.length + ' thèmes');

      for (const theme of THEMES) {
        journal.lieu = 'thème ' + theme + ' (' + app.nom + ')';
        await toutFermer(page);
        if (theme === 'sombre') {
          // Sélecteur de thème : popover de #theme-btn (ordinateur), feuille ⋯ (téléphone)
          await choisirTheme(page, 'dark', app.mobile).catch(e => pbPreparation.push(app.nom + ' : sélecteur de thème : ' + String(e.message).split('\n')[0]));
          await pause(150);
        }
        const th = await page.evaluate(() => ({ attr: document.documentElement.getAttribute('data-theme'), store: Store.get('theme') }));
        const attendu = theme === 'sombre' ? 'dark' : null;
        if (th.attr !== attendu || (theme === 'sombre' && th.store !== 'dark')) {
          pbPreparation.push(app.nom + ' : thème ' + theme + ' non appliqué (data-theme=' + th.attr + ', Store theme=' + th.store + ')');
        }
        // Un écran : fermer, naviguer, préparer, attendre le rendu, mesurer, capturer → liste de problèmes
        const mesurer = async ecran => {
          const restes = await toutFermer(page);
          if (restes.length) return ['fenêtre restée ouverte avant l\'écran : ' + restes.join(', ')];
          const chap = ecran.chap === 'anglais' ? anglais : ecran.chap;
          if (!chap) return ['aucun chapitre d\'anglais avec flashcards'];
          await naviguer(page, chap, ecran.onglet);
          const pid = await page.evaluate(([id, onglet]) => CHAPTERS_BY_ID[id].prefix + '-' + onglet, [chap, ecran.onglet]);
          if (ecran.onglet === 'simu') await pause(300);
          await attendreRendu(page, pid);
          const pb = ecran.preparer ? await ecran.preparer(page, app) : [];
          if (pb.length) return pb;
          await attendreRendu(page, ecran.racine ? ecran.racine.slice(1) : pid);
          const m = await page.evaluate(mesurerEcran, { racines: [ecran.racine || 'body'], mobile: app.mobile });
          const capture = await ctx.capture(page, app.nom + '-' + theme + '-' + ecran.nom, { animations: 'disabled', caret: 'hide' });
          ecransMesures.push({ ecran: ecran.nom, theme, appareil: app.nom, racine: ecran.racine || 'body', largeur: m.W, scrollWidth: m.scrollWidth,
            stats: m.stats, mesureMs: m.dureeMs, capture: capture ? path.basename(capture) : null });
          for (const c of m.constats) tous.push(Object.assign({ ecran: ecran.nom, theme, appareil: app.nom }, c));
          for (const n of m.nonEvalues) nonEvalues.push(Object.assign({ ecran: ecran.nom, theme, appareil: app.nom }, n));
          return [];
        };
        for (const ecran of ecrans) {
          const lieu = ecran.nom + ' · ' + theme + ' · ' + app.nom;
          journal.lieu = lieu;
          let pb;
          try { pb = await mesurer(ecran); } catch (e) { pb = [String(e.message).split('\n')[0]]; }
          pbPreparation.push(...pb.map(x => lieu + ' : ' + x));
          ctx.progression(rang++, ecrans.length * THEMES.length, pb.length > 0);
        }
      }
      const js = journal.erreurs.map(e => '[' + e.lieu + '] ' + e.type + ' : ' + e.texte);
      res.verifier('aucune erreur JavaScript pendant les mesures (' + app.nom + ')', !js.length, js);
      await page.context().close().catch(() => {});
    }

    /* ---------- Bilan des mesures ---------- */
    res.verifier('écrans préparés et mesurés (' + ecransMesures.length + ' écran(s) × thème × appareil)', !pbPreparation.length && ecransMesures.length > 0, pbPreparation);
    for (const c of tous) { const k = classer(c, toleres); c.statut = k.statut; }
    for (const m of Object.keys(SENS)) {
      const liste = tous.filter(c => c.mesure === m);
      const fautifs = regrouper(liste.filter(c => c.statut !== 'tolere'))
        .sort((a, b) => (SENS[m] === 'min' ? a.valeur - b.valeur : b.valeur - a.valeur));
      const nTol = liste.filter(c => c.statut === 'tolere').length;
      res.verifier(LIBELLES[m] + ' — ' + liste.length + ' constat(s)' + (strict ? '' : ', dont ' + nTol + ' toléré(s)'),
        !fautifs.length, fautifs.map(messageGroupe));
    }
    // Sélecteurs tolérés qui ne couvrent plus aucun constat : à retirer de la liste
    const toleresNonConstates = toleresPerimes(toleres, tous);
    toleresNonConstates.forEach(t => res.avertir('TOLERES : « ' + t.selecteur + ' » (' + t.mesure + ', écrans ' + t.ecrans + ', thèmes ' + t.themes
      + ', appareils ' + t.appareils + ') n\'est plus constaté — le retirer de la liste (tests/suites/visuel.js)'));
    const nbNonEvalues = new Set(nonEvalues.map(n => n.selecteur + '|' + n.fond)).size;
    if (nbNonEvalues) ctx.log(nbNonEvalues + ' sélecteur(s) de texte sur fond image / dégradé / formes SVG, contraste non évalué (voir visuel.md)');

    /* ---------- Sorties : visuel.json, visuel.md ---------- */
    const detail = {
      date: new Date().toISOString(), strict, dureeMs: Date.now() - t0,
      appareils: APPAREILS, themes: THEMES, seuils: { contraste: 4.5, contrasteGrandTexte: 3, taille: 12, cible24: 24, cible44: 44 },
      ecrans: ecransMesures, constats: tous, nonEvalues, toleresNonConstates, preparation: pbPreparation,
      propositionToleres: proposerToleres(tous, ecransParAppareil),
    };
    fs.writeFileSync(path.join(ctx.options.sortie, 'visuel.json'), JSON.stringify(detail, null, 1));
    ecrireRecap(path.join(ctx.options.sortie, 'visuel.md'), detail);
    res.info('constats', Object.fromEntries(Object.keys(SENS).map(m => [m, tous.filter(c => c.mesure === m).length])));
    res.info('nonEvalues', nonEvalues.length);
    res.info('detail', 'visuel.json + visuel.md');
    ctx.log('détail : ' + path.join(ctx.options.sortie, 'visuel.json') + ' · récapitulatif : visuel.md · durée ' + Math.round((Date.now() - t0) / 1000) + ' s');
  },
};
