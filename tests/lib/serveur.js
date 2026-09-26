'use strict';
/* ============================================================
   Petit serveur statique intégré (module http de node, aucune dépendance)
   ============================================================
   - Sert les fichiers de la racine du site avec les bons types MIME.
   - Choisit tout seul un port libre (port 0) et n'écoute que sur 127.0.0.1.
   - Peut servir une VARIANTE transformée d'index.html pour certains tests :
       /?variante=<nom>&param=valeur…  → la fonction enregistrée sous <nom>
       reçoit (html, paramètres de l'URL) et renvoie le HTML modifié.
     Le fichier index.html sur le disque n'est JAMAIS modifié.
   - /__tests__/vide.html : page vide de la même origine, pratique pour
     pré-remplir le localStorage avant de charger le vrai site. */
const http = require('http');
const fs = require('fs');
const path = require('path');

const TYPES_MIME = {
  '.html': 'text/html; charset=utf-8',
  '.htm': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.webmanifest': 'application/manifest+json; charset=utf-8',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.otf': 'font/otf',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.txt': 'text/plain; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
};

const PAGE_VIDE = '<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>vide</title></head><body></body></html>';

/* Démarre le serveur. Renvoie { url, port, variantes, requetes, fermer() }.
   `variantes` est une Map nom → fonction(html, params) → html. */
function demarrerServeur(racine) {
  const racineAbs = path.resolve(racine);
  const variantes = new Map();
  const sockets = new Set();
  const stats = { requetes: 0, erreurs404: [] };

  const serveur = http.createServer((req, res) => {
    stats.requetes++;
    let url;
    try { url = new URL(req.url, 'http://127.0.0.1'); }
    catch (e) { res.writeHead(400); res.end('URL invalide'); return; }
    if (req.method !== 'GET' && req.method !== 'HEAD') {
      res.writeHead(405, { Allow: 'GET, HEAD' }); res.end(); return;
    }
    const envoyer = (code, type, corps) => {
      res.writeHead(code, {
        'Content-Type': type,
        'Content-Length': Buffer.byteLength(corps),
        // Pas de cache HTTP : chaque chargement relit le disque (ou la variante demandée)
        'Cache-Control': 'no-store',
      });
      res.end(req.method === 'HEAD' ? undefined : corps);
    };

    // Page vide de même origine (pré-remplissage du localStorage)
    if (url.pathname === '/__tests__/vide.html') { envoyer(200, TYPES_MIME['.html'], PAGE_VIDE); return; }

    let chemin;
    try { chemin = decodeURIComponent(url.pathname); }
    catch (e) { envoyer(400, TYPES_MIME['.txt'], 'Chemin invalide'); return; }
    if (chemin.endsWith('/')) chemin += 'index.html';
    const fichier = path.resolve(racineAbs, '.' + chemin);
    // Sécurité : on ne sert rien en dehors de la racine
    if (fichier !== racineAbs && !fichier.startsWith(racineAbs + path.sep)) {
      envoyer(403, TYPES_MIME['.txt'], 'Interdit'); return;
    }
    fs.readFile(fichier, (err, contenu) => {
      if (err) {
        stats.erreurs404.push(chemin);
        envoyer(404, TYPES_MIME['.txt'], 'Introuvable : ' + chemin);
        return;
      }
      const ext = path.extname(fichier).toLowerCase();
      const type = TYPES_MIME[ext] || 'application/octet-stream';
      // Variante transformée d'index.html (hook de transformation)
      const nomVariante = url.searchParams.get('variante');
      if (nomVariante && path.basename(fichier) === 'index.html') {
        const transformer = variantes.get(nomVariante);
        if (!transformer) { envoyer(500, TYPES_MIME['.txt'], 'Variante inconnue : ' + nomVariante); return; }
        let html;
        try { html = transformer(contenu.toString('utf8'), url.searchParams); }
        catch (e) { envoyer(500, TYPES_MIME['.txt'], 'Échec de la variante ' + nomVariante + ' : ' + e.message); return; }
        envoyer(200, type, html);
        return;
      }
      envoyer(200, type, contenu);
    });
  });

  // On garde la trace des connexions (keep-alive) pour pouvoir fermer proprement
  serveur.on('connection', s => { sockets.add(s); s.on('close', () => sockets.delete(s)); });

  return new Promise((resolve, reject) => {
    serveur.once('error', reject);
    serveur.listen(0, '127.0.0.1', () => {
      const port = serveur.address().port;
      resolve({
        url: 'http://127.0.0.1:' + port + '/',
        port,
        variantes,
        stats,
        fermer() {
          return new Promise(r => {
            sockets.forEach(s => s.destroy());
            serveur.close(() => r());
          });
        },
      });
    });
  });
}

module.exports = { demarrerServeur, TYPES_MIME };
