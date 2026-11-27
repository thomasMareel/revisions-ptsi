#!/usr/bin/env node
/* Données dérivées des chapitres (docs/chargement-chapitres.md, §4). Le contenu des onglets Cours,
   Méthodes et Exercices vit dans chapitres/<id>.html ; cet outil en tire :
     - le manifeste window.__CHAPITRES, écrit dans le script du <head> d'index.html entre les
       marqueurs « CHAPITRES : DÉBUT » et « CHAPITRES : FIN » : v = empreinte de chaque fichier de
       chapitre (son adresse la porte : chapitres/<id>.html?v=…, une mise à jour ne sert jamais
       l'ancien), recherche = empreinte de chapitres/recherche.json ;
     - chapitres/recherche.json : entrées de la recherche (sections, définitions et propriétés,
       méthodes, formules, exercices) par chapitre, avec le repère de leur élément.
   Le contenu est lu par Chromium (même analyseur HTML que le site) et l'extraction est celle de
   tools/extraction-chapitres.js.

   Usage (depuis la racine du dépôt) :
     node tools/chapitres.js              régénère le manifeste et l'index (idempotent)
     node tools/chapitres.js --verifier   n'écrit rien ; code 1 si quelque chose est à régénérer
   À lancer après toute modification d'un fichier de chapitre (validate.py refuse des données
   périmées). Playwright : comme pour les tests (tests/README.md). */
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { execSync } = require('child_process');

const RACINE = path.resolve(__dirname, '..');
const INDEX = path.join(RACINE, 'index.html');
const DOSSIER = path.join(RACINE, 'chapitres');
const RECHERCHE = path.join(DOSSIER, 'recherche.json');
const DEBUT = '/* CHAPITRES : DÉBUT — généré par tools/chapitres.js, ne pas modifier à la main */';
const FIN = '/* CHAPITRES : FIN */';
const ANCRE = '<script>\n/* Thème posé AVANT le premier affichage';

function chargerPlaywright() {
  try { return require('playwright'); } catch (e) { /* essai suivant */ }
  let g = null;
  try { g = execSync('npm root -g', { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'], timeout: 30000 }).trim(); } catch (e) { /* npm introuvable */ }
  for (const nom of ['playwright', '@playwright/test']) {
    const p = g && path.join(g, nom);
    if (p && fs.existsSync(p)) { try { return require(p); } catch (e) { /* essai suivant */ } }
  }
  console.error('Playwright est introuvable (voir tests/README.md : npm install, puis npx playwright install chromium).');
  process.exit(2);
}

/* Empreinte d'un texte : fins de ligne normalisées (Windows et Linux donnent la même), 8 caractères.
   validate.py calcule la même (empreinte()). */
const empreinte = t => crypto.createHash('sha1').update(t.replace(/\r\n/g, '\n'), 'utf8').digest('hex').slice(0, 8);
/* index.html sans son manifeste */
function sansManifeste(html) {
  const a = html.indexOf(DEBUT), b = html.indexOf(FIN);
  return a >= 0 && b > a ? html.slice(0, a) + html.slice(b + FIN.length + 1) : html;
}
/* Empreinte de l'ensemble des chapitres (source de recherche.json) : validate.py fait le même calcul */
const empreinteEnsemble = v => empreinte(Object.keys(v).sort().map(id => id + ':' + v[id]).join('\n'));

async function extraire(textes) {
  const { chromium } = chargerPlaywright();
  const nav = await chromium.launch();
  try {
    const page = await nav.newPage();
    await page.setContent('<!doctype html><html><body></body></html>');
    await page.addScriptTag({ content: fs.readFileSync(path.join(__dirname, 'extraction-chapitres.js'), 'utf8') });
    return await page.evaluate(textes => {
      const res = {};
      for (const id of Object.keys(textes)) {
        const t = document.createElement('template');
        t.innerHTML = textes[id];          // comme le site (window.__chargerChapitre)
        const panneaux = Array.from(t.content.querySelectorAll('template.pan-tpl[data-panneau]'),
          p => ({ id: p.getAttribute('data-panneau'), racine: p.content }));
        res[id] = extraireChapitre(panneaux);
      }
      return res;
    }, textes);
  } finally { await nav.close(); }
}

(async () => {
  const verifier = process.argv.includes('--verifier');
  const html = fs.readFileSync(INDEX, 'utf8');
  const textes = {}, v = {};
  for (const f of fs.readdirSync(DOSSIER).filter(f => /^[a-z0-9]+\.html$/.test(f)).sort()) {
    const id = f.slice(0, -5);
    textes[id] = fs.readFileSync(path.join(DOSSIER, f), 'utf8');
    v[id] = empreinte(textes[id]);
  }
  const res = await extraire(textes);
  const chapitres = {};
  for (const id of Object.keys(res)) chapitres[id] = res[id];
  const recherche = JSON.stringify({ source: empreinteEnsemble(v), chapitres }) + '\n';
  const manifeste = { recherche: empreinte(recherche), v };
  const source = sansManifeste(html);
  const i = source.indexOf(ANCRE);
  if (i < 0) { console.error('ancre du script du <head> introuvable dans index.html'); process.exit(2); }
  const k = i + '<script>\n'.length;
  const nouveau = source.slice(0, k) + DEBUT + '\nwindow.__CHAPITRES = ' + JSON.stringify(manifeste) + ';\n' + FIN + '\n' + source.slice(k);
  const ancienne = fs.existsSync(RECHERCHE) ? fs.readFileSync(RECHERCHE, 'utf8') : null;
  const aJour = nouveau === html && ancienne === recherche;
  const n = Object.values(chapitres).reduce((a, x) => a + x.length, 0);
  if (verifier) {
    console.log(aJour ? '[OK] données dérivées à jour' : '[À FAIRE] données dérivées périmées : node tools/chapitres.js');
    process.exit(aJour ? 0 : 1);
  }
  if (ancienne !== recherche) fs.writeFileSync(RECHERCHE, recherche);
  if (nouveau !== html) fs.writeFileSync(INDEX, nouveau);
  console.log((aJour ? 'déjà à jour' : 'écrit') + ' : ' + Object.keys(v).length + ' chapitres, ' + n + ' entrées de recherche ('
    + (recherche.length / 1e6).toFixed(1) + ' Mo, chapitres/recherche.json)');
})().catch(e => { console.error(e); process.exit(2); });
