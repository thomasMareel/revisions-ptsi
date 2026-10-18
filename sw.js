/* Service worker — Révisions PTSI
   Met en cache toute la coquille de l'app pour un fonctionnement hors-ligne.
   IMPORTANT : à chaque modification d'un asset mis en cache (index.html, polices,
   MathJax…), incrémenter CACHE_VERSION pour forcer le rafraîchissement chez les
   utilisateurs déjà installés. */
const CACHE_VERSION = 'ptsi-cache-v88';

const PRECACHE = [
  './',
  'index.html',
  'manifest.webmanifest',
  'icons/icon-192.png',
  'icons/icon-512.png',
  'icons/apple-touch-icon.png',
  'vendor/fonts/polices.css',
  'vendor/fonts/jetbrains-mono-greek-wght-normal.woff2',
  'vendor/fonts/jetbrains-mono-latin-ext-wght-normal.woff2',
  'vendor/fonts/jetbrains-mono-latin-wght-normal.woff2',
  'vendor/fonts/source-sans-3-greek-wght-normal.woff2',
  'vendor/fonts/source-sans-3-latin-ext-wght-normal.woff2',
  'vendor/fonts/source-sans-3-latin-wght-normal.woff2',
  'vendor/fonts/source-sans-3-symboles-wght-normal.woff2',
  'vendor/fonts/source-serif-4-greek-opsz-normal.woff2',
  'vendor/fonts/source-serif-4-greek-wght-italic.woff2',
  'vendor/fonts/source-serif-4-latin-ext-opsz-normal.woff2',
  'vendor/fonts/source-serif-4-latin-ext-wght-italic.woff2',
  'vendor/fonts/source-serif-4-latin-opsz-normal.woff2',
  'vendor/fonts/source-serif-4-latin-wght-italic.woff2',
  'vendor/fonts/source-serif-4-symboles-opsz-normal.woff2',
  'vendor/mathjax/tex-mml-chtml.js',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_AMS-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Calligraphic-Bold.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Calligraphic-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Fraktur-Bold.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Fraktur-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Main-Bold.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Main-Italic.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Main-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Math-BoldItalic.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Math-Italic.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Math-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_SansSerif-Bold.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_SansSerif-Italic.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_SansSerif-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Script-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Size1-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Size2-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Size3-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Size4-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Typewriter-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Vector-Bold.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Vector-Regular.woff',
  'vendor/mathjax/output/chtml/fonts/woff-v2/MathJax_Zero.woff'
];

self.addEventListener('install', event => {
  // Pas de skipWaiting() automatique : le nouveau SW reste « en attente » jusqu'à
  // ce que l'utilisateur clique « Recharger » (bannière de mise à jour côté page),
  // qui envoie le message SKIP_WAITING ci-dessous. (Au tout premier install, sans
  // SW préexistant, l'activation est immédiate de toute façon.)
  event.waitUntil(
    caches.open(CACHE_VERSION).then(cache => cache.addAll(PRECACHE))
  );
});

// La page demande l'activation immédiate de la nouvelle version.
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'SKIP_WAITING') self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE_VERSION).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return; // laisser passer toute requête externe

  const isNav = req.mode === 'navigate' ||
                (req.headers.get('accept') || '').includes('text/html');

  if (isNav) {
    // HTML : « cache d'abord puis revalidation » (stale-while-revalidate).
    // Lancement INSTANTANÉ depuis le cache (crucial en PWA), tout en récupérant
    // la nouvelle version en arrière-plan ; la bannière de mise à jour (pilotée
    // par le bump de CACHE_VERSION + skipWaiting) invite à recharger quand prêt.
    event.respondWith(
      caches.open(CACHE_VERSION).then(cache =>
        cache.match('index.html').then(cached => {
          const network = fetch(req)
            .then(res => { if (res && res.ok) cache.put('index.html', res.clone()); return res; })
            .catch(() => cached || cache.match('./'));
          return cached || network;   // cache si présent (instantané), sinon réseau (1er chargement)
        })
      )
    );
    return;
  }

  // Assets : cache d'abord, puis réseau (et on met en cache au passage)
  event.respondWith(
    caches.match(req).then(cached => cached || fetch(req).then(res => {
      if (res && res.ok) {
        const copy = res.clone();
        caches.open(CACHE_VERSION).then(c => c.put(req, copy));
      }
      return res;
    }))
  );
});
