#!/usr/bin/env python3
"""Ligne A : remplace le module THÈME, la taille du texte, les menus de l'en-tête ;
compteurs de la feuille ⋯ et de la tuile ; bannière de mise à jour en classes ;
crochet du scroll-spy pour la barre du téléphone.
Usage : python3 etape_js2.py index.html <dossier des fragments>"""
import sys, os
p, d = sys.argv[1:3]
s = open(p, encoding='utf-8').read()
def lire(n):
    return open(os.path.join(d, n), encoding='utf-8').read().rstrip('\n')

def remplacer(debut, fin, neuf, inclure_fin=True):
    global s
    assert s.count(debut) == 1, debut[:50]
    i = s.index(debut)
    j = s.index(fin, i)
    j = j + len(fin) if inclure_fin else j
    s = s[:i] + neuf + s[j:]

# 1) module THÈME (commentaire d'en-tête compris)
remplacer("/* Préférence (clé 'theme') : 'light' | 'dark' | 'auto' (défaut, et ancienne",
          "  window.__setTheme = setTheme;\n})();", lire('theme.js'))

# 2) taille du texte
remplacer("/* S3 — Réglage de la taille du texte (A− / A+), persistant. */", "\n})();\n</script>", '''/* S3 — Taille du texte (clé readScale : index 0-2 → --read-scale 1 / 1,1 / 1,2), choisie
   par les segmentés A / A+ / A++ du popover Thème (ordinateur) et de la feuille ⋯ (téléphone). */
(function(){
  const LEVELS = [1, 1.1, 1.2];
  let i = parseInt(Store.get('readScale') || '0', 10);
  if(!(i >= 0 && i < LEVELS.length)) i = 0;
  function apply(){
    document.documentElement.style.setProperty('--read-scale', LEVELS[i]);
    document.querySelectorAll('[data-read-set]').forEach(b =>
      b.setAttribute('aria-checked', parseInt(b.getAttribute('data-read-set'), 10) === i ? 'true' : 'false'));
  }
  apply();
  document.querySelectorAll('[data-read-set]').forEach(b => b.addEventListener('click', e => {
    e.stopPropagation();                 // ne ferme ni le popover ni la feuille ⋯
    i = Math.max(0, Math.min(LEVELS.length - 1, parseInt(b.getAttribute('data-read-set'), 10) || 0));
    Store.set('readScale', String(i));
    apply();
  }));
})();
</script>''')

# 3) menus déroulants de l'en-tête
remplacer("/* Menu « ⋯ Plus » de l'en-tête */", "  document.addEventListener('keydown', e => { if(e.key === 'Escape') close(); });\n})();\n</script>",
          lire('menus.js') + '\n</script>', True)

# 4) compteurs : feuille ⋯ et tuile Aujourd'hui ; ligne du jour supprimée (plus d'en-tête haut)
ancien_badge = s[s.index("  function updateBadge(){\n    if(typeof srsCountDue !== 'function') return;"):s.index("  window.__updateHeaderToday = updateHeaderToday;\n")+len("  window.__updateHeaderToday = updateHeaderToday;\n")]
s = s.replace(ancien_badge, '''  function updateBadge(){
    if(typeof srsCountDue !== 'function') return;
    const n = srsCountDue();
    ['rev-badge','rev-badge-mob','rev-badge-study','rev-badge-sheet','rev-badge-tile'].forEach(id=>{
      const el=document.getElementById(id); if(!el) return;
      if(n>0){ el.textContent = n>99 ? '99+' : String(n); el.hidden=false; }
      else el.hidden=true;
    });
    const t = document.getElementById('study-btn');
    if(t) t.setAttribute('aria-label', n > 0 ? 'Réviser : ' + n + ' carte' + (n > 1 ? 's' : '') + ' due' + (n > 1 ? 's' : '') : 'Réviser');
    const m = document.getElementById('mob-revise-btn');
    if(m) m.setAttribute('aria-label', n > 0 ? 'Réviser : ' + n + ' carte' + (n > 1 ? 's' : '') + ' due' + (n > 1 ? 's' : '') : 'Réviser : révisions du jour');
    if(window.__majNavCompteurs) window.__majNavCompteurs();   // compteurs des rangées de la navigation
  }
  window.__updateReviseBadge = updateBadge;
''')

# 5) bannière de mise à jour : classes de la région COQUILLE au lieu de styles en ligne
remplacer("      const bar = document.createElement('div');\n      bar.id = 'sw-update-banner';",
          "      bar.appendChild(msg); bar.appendChild(btn); bar.appendChild(close);", '''      const bar = document.createElement('div');
      bar.id = 'sw-update-banner';
      bar.className = 'maj-banniere';
      bar.setAttribute('role', 'status');
      const msg = document.createElement('span');
      msg.innerHTML = (window.__icon ? window.__icon('refresh') : '') + ' Nouvelle version disponible';
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'maj-recharger';
      btn.textContent = 'Recharger';
      btn.addEventListener('click', () => {
        btn.disabled = true; btn.textContent = '…';
        if (reg.waiting) reg.waiting.postMessage({ type: 'SKIP_WAITING' });
        else location.reload();
      });
      const close = document.createElement('button');
      close.type = 'button';
      close.className = 'maj-ignorer';
      close.innerHTML = window.__icon ? window.__icon('x') : '×';
      close.setAttribute('aria-label', 'Ignorer');
      close.addEventListener('click', () => bar.remove());
      bar.appendChild(msg); bar.appendChild(btn); bar.appendChild(close);''')

# 6) scroll-spy du sommaire interne → section courante (barre du téléphone, lastPos.s)
a = "        a.classList.toggle('active', entry.isIntersecting);\n      });\n"
assert s.count(a) == 1
s = s.replace(a, a + "      if(entry.isIntersecting && window.__surSection) window.__surSection(entry.target);\n")
open(p, 'w', encoding='utf-8').write(s)
print('JS de la coquille remplacé')
