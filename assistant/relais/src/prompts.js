/* Prompts de l'assistant (versionnés : à relire comme du contenu pédagogique).
   Structure de la requête, dans l'ordre du cache de prompt :
   system[0] = REGLES_ECRIT (fixe), system[1] = fiche du chapitre (fixe pendant la
   conversation), puis l'historique, puis le dernier message (contexte volatil + question).
   Rien de variable (date, heure, identifiant) dans les deux blocs système : le cache serait perdu. */

export const REGLES_ECRIT = `Tu es l'assistant de révision intégré à un site de cours de classe préparatoire scientifique (PTSI en 1re année, PT en 2e année, programmes officiels de 2021). Un élève lit une page du site et te pose une question ; tu reçois le chapitre affiché et l'endroit précis où il se trouve.

Règles :
1. Appuie-toi d'abord sur le chapitre fourni : mêmes notations, mêmes conventions de signe et d'orientation, même vocabulaire que le site. Renvoie à une section par son numéro (« §3 ») quand c'est utile.
2. Reste au niveau et dans le programme de PTSI-PT. Si la question sort du programme, dis-le en une phrase, puis réponds brièvement.
3. Méthode avant résultat : quelle loi ou quel théorème, pourquoi, sous quelles hypothèses ; puis le calcul ; puis une vérification (unités, signe, ordre de grandeur, cas limite).
4. Exercice dont la solution n'a pas été ouverte par l'élève : commence par un indice ou la méthode, et ne donne la solution complète que s'il la demande.
5. Formules en LaTeX : \\( … \\) dans le texte, $$ … $$ en bloc ; jamais \\[ … \\]. Pas de titres ni de tableaux ; des paragraphes courts, des listes à tirets si besoin, du **gras** avec parcimonie.
6. Français, ton direct et bienveillant, tutoiement. Réponses courtes (en général moins de 200 mots), sauf si l'élève demande plus.
7. Si tu n'es pas sûr, dis-le. N'invente ni valeur numérique, ni référence, ni contenu du site.`;

const ONGLETS = { cours: 'Cours', video: 'Vidéos', meth: 'Méthodes', simu: 'Simulateur', flash: 'Cartes', exos: 'Exercices' };

const nettoyer = (t, n) => String(t == null ? '' : t).replace(/\u0000/g, '').slice(0, n);

/* Bloc système n° 2 : le chapitre. Mêmes octets à chaque tour (condition du cache). */
export function blocChapitre(chapitre, texte) {
  const c = chapitre || {};
  const annee = c.annee === 2 ? '2e année (PT)' : c.annee === 1 ? '1re année (PTSI)' : 'les deux années';
  return `Chapitre affiché sur le site : « ${nettoyer(c.nom, 200)} » (${nettoyer(c.matiere, 40)} › ${nettoyer(c.partie, 120)}, ${annee}).
Voici son contenu tel qu'il est sur le site (formules en TeX ; « [Solution (non ouverte par l'élève)] » marque une correction que l'élève n'a pas encore dépliée) :
<chapitre>
${nettoyer(texte, 230000)}
</chapitre>`;
}

/* Message de l'élève : contexte volatil (où il est, ce qu'il a sélectionné…) + question.
   Déterministe : l'historique renvoyé par le site est reconstruit à l'identique. */
export function messageUtilisateur(x, question) {
  x = x || {};
  const L = [];
  if (x.onglet) {
    let l = 'Onglet : ' + (ONGLETS[x.onglet] || nettoyer(x.onglet, 20));
    if (x.section) l += ' ; section : ' + (x.section.num ? nettoyer(x.section.num, 10) + ' ' : '') + '« ' + nettoyer(x.section.titre, 200) + ' »';
    if (x.methode) l += ' ; méthode : « ' + nettoyer(x.methode.titre, 200) + ' »';
    L.push(l);
  } else if (x.page) L.push('Page : ' + nettoyer(x.page, 20));
  if (x.exercice) {
    const e = x.exercice;
    L.push('Exercice affiché : ' + nettoyer(e.num, 20) + ' « ' + nettoyer(e.titre, 200) + ' »'
      + (e.concours ? ' (type concours)' : '') + (e.solutionOuverte ? ' — solution ouverte' : ' — solution non ouverte'));
    if (e.enonce) L.push('Énoncé (début) : ' + nettoyer(e.enonce, 1500));
  }
  if (x.carte) {
    const k = x.carte;
    L.push('Carte affichée (' + (k.face === 'verso' ? 'réponse visible' : 'réponse cachée') + ') : « ' + nettoyer(k.question, 600) + ' »'
      + (k.face === 'verso' && k.reponse ? ' — réponse : « ' + nettoyer(k.reponse, 800) + ' »' : ''));
  }
  if (x.simulateur) {
    const s = x.simulateur;
    const r = Object.entries(s.reglages || {}).slice(0, 12).map(([a, b]) => nettoyer(a, 60) + ' = ' + nettoyer(b, 40)).join(' ; ');
    const m = Object.entries(s.mesures || {}).slice(0, 12).map(([a, b]) => nettoyer(a, 60) + ' = ' + nettoyer(b, 60)).join(' ; ');
    L.push('Simulateur : ' + nettoyer(s.titre, 120) + (s.mode ? ' (mode ' + nettoyer(s.mode, 60) + ')' : '') + (r ? ' ; réglages : ' + r : '') + (m ? ' ; mesures : ' + m : ''));
  }
  if (x.video) {
    const v = x.video;
    let l = 'Vidéo en cours : « ' + nettoyer(v.titre, 200) + ' », à ' + nettoyer(v.temps, 10) + (v.estime ? ' (environ)' : '');
    if (v.partie) l += ', partie « ' + nettoyer(v.partie, 120) + ' »';
    L.push(l);
    if (v.phrase && v.phrase.ecrit) L.push('Phrase dite à cet instant : « ' + nettoyer(v.phrase.ecrit, 600) + ' »');
  }
  if (x.selection && x.selection.texte) L.push('Passage sélectionné par l\'élève' + (x.selection.section ? ' (' + nettoyer(x.selection.section, 10) + ')' : '') + ' :\n« ' + nettoyer(x.selection.texte, 4000) + ' »');
  const q = nettoyer(question, 4000).trim();
  return (L.length ? '<contexte>\n' + L.join('\n') + '\n</contexte>\n\n' : '') + q;
}
