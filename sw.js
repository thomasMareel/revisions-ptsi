/* Service worker — Révisions PTSI
   Met en cache toute la coquille de l'app pour un fonctionnement hors-ligne.
   IMPORTANT : à chaque modification d'un asset mis en cache (index.html, polices,
   MathJax…), incrémenter CACHE_VERSION pour forcer le rafraîchissement chez les
   utilisateurs déjà installés. */
const CACHE_VERSION = 'ptsi-cache-v45';

const PRECACHE = [
  './',
  'index.html',
  'manifest.webmanifest',
  'icons/icon-192.png',
  'icons/icon-512.png',
  'icons/apple-touch-icon.png',
  'vendor/fonts/fonts.css',
  'vendor/mathjax/tex-mml-chtml.js',
  'vendor/fonts/Fraunces-400-italic-latin-ext.woff2',
  'vendor/fonts/Fraunces-400-italic-latin.woff2',
  'vendor/fonts/Fraunces-400-normal-latin-ext.woff2',
  'vendor/fonts/Fraunces-400-normal-latin.woff2',
  'vendor/fonts/Fraunces-600-normal-latin-ext.woff2',
  'vendor/fonts/Fraunces-600-normal-latin.woff2',
  'vendor/fonts/Fraunces-800-normal-latin-ext.woff2',
  'vendor/fonts/Fraunces-800-normal-latin.woff2',
  'vendor/fonts/InterTight-400-normal-latin-ext.woff2',
  'vendor/fonts/InterTight-400-normal-latin.woff2',
  'vendor/fonts/InterTight-500-normal-latin-ext.woff2',
  'vendor/fonts/InterTight-500-normal-latin.woff2',
  'vendor/fonts/InterTight-600-normal-latin-ext.woff2',
  'vendor/fonts/InterTight-600-normal-latin.woff2',
  'vendor/fonts/JetBrainsMono-400-normal-latin-ext.woff2',
  'vendor/fonts/JetBrainsMono-400-normal-latin.woff2',
  'vendor/fonts/JetBrainsMono-500-normal-latin-ext.woff2',
  'vendor/fonts/JetBrainsMono-500-normal-latin.woff2',
  'vendor/fonts/JetBrainsMono-600-normal-latin-ext.woff2',
  'vendor/fonts/JetBrainsMono-600-normal-latin.woff2',
  'vendor/fonts/JetBrainsMono-700-normal-latin-ext.woff2',
  'vendor/fonts/JetBrainsMono-700-normal-latin.woff2',
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
  event.waitUntil(
    caches.open(CACHE_VERSION)
      .then(cache => cache.addAll(PRECACHE))
      .then(() => self.skipWaiting())
  );
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
    // HTML : réseau d'abord (toujours frais en ligne), cache en secours hors-ligne
    event.respondWith(
      fetch(req)
        .then(res => {
          const copy = res.clone();
          caches.open(CACHE_VERSION).then(c => c.put('index.html', copy));
          return res;
        })
        .catch(() => caches.match('index.html').then(r => r || caches.match('./')))
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
