"""Onglet « Vidéos » du chapitre rdm (résistance des matériaux) : à lancer quand les vidéos ont leur youtube.json.
Usage (depuis la racine du dépôt) : python3 video/rdm/integrer_videos.py
Les trois vidéos vont dans le même chapitre du site, dans l'ordre ch1, ch2, ch3 ; aperçus media/videos/rdm-N.webp."""
import json, os, re
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
CID, PFX = 'rdm', 'rdm'
src = open(f'{R}/index.html', encoding='utf-8').read()
nums = [n for n in (1, 2, 3) if os.path.exists(f'{R}/video/rdm/ch{n}/youtube.json')]
if not nums:
    raise SystemExit('aucune vidéo envoyée (pas de youtube.json)')

def un(a, b):
    global src
    assert src.count(a) == 1, (src.count(a), a[:80]); src = src.replace(a, b)

def js(s): return s.replace('\\', '\\\\').replace("'", "\\'")

# 1. CHAPTERS : 'video' après 'cours'
i = src.index("{ id:'%s'" % CID); j = src.index('}', src.index('panels:', i))
ent = src[i:j]
if "'video'" not in ent:
    ent2 = ent.replace("panels:['cours',", "panels:['cours','video',", 1)
    assert ent2 != ent
    src = src[:i] + ent2 + src[j:]
# 2. Onglet et panneau
tab_cours = f'<button class="tab active" data-panel="{PFX}-cours"><span class="num">01</span>Cours</button>'
if f'data-panel="{PFX}-video"' not in src:
    un(tab_cours, tab_cours + f'\n  <button class="tab" data-panel="{PFX}-video"><span class="num">02</span>Vidéos</button>')
    k = src.index(f'id="{PFX}-cours"'); k = src.rindex('<section', 0, k); e = src.index('</section>', k) + len('</section>')
    panneau = (f'\n<section class="panel" id="{PFX}-video">\n'
               f'  <div class="vid-liste" data-videos="{CID}"><p class="vid-attente">Les vidéos du cours au tableau, à lancer une par une.</p></div>\n'
               '</section>')
    src = src[:e] + panneau + src[e:]
# 3. Table window.__VIDEOS
if re.search(r'\n    %s: \[\n' % CID, src):
    raise SystemExit(f'{CID} déjà dans la table : à mettre à jour à la main')
lignes = []
for n in nums:
    d = f'{R}/video/rdm/ch{n}'
    yt = json.load(open(f'{d}/youtube.json'))
    vid = yt.get('id') or yt.get('video_id') or yt['url'].rsplit('/', 1)[-1]
    info = json.load(open(f'{d}/chapitre.json')); tl = json.load(open(f'{d}/timeline.json'))
    duree = int(round(tl['duree']))
    parties = [[int(tl['scenes'][s]['t0']), tl['scenes'][s]['titre']] for s in tl['ordre']]
    parties[0][0] = 0
    p_txt = ','.join(f"[{t},'{js(ti)}']" for t, ti in parties)
    lignes.append(f"      {{ yt:'{vid}', titre:'{js(info['titre'])}', duree:{duree}, apercu:'media/videos/rdm-{n}.webp',\n"
                  f"        parties:[{p_txt}] }}")
    print(n, vid, duree, len(parties), 'parties')
entree = f"    {CID}: [\n" + ',\n'.join(lignes) + "\n    ],\n"
un('  window.__VIDEOS = {\n', '  window.__VIDEOS = {\n' + entree)
open(f'{R}/index.html', 'w', encoding='utf-8').write(src)
