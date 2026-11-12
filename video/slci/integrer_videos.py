"""Onglet « Vidéos » des chapitres d'automatique : à lancer quand les vidéos ont leur youtube.json.
Usage (depuis la racine du dépôt) : python3 video/slci/integrer_videos.py [n1 n2 ...]  (numéros des vidéos à intégrer ; défaut : toutes celles qui ont un youtube.json)"""
import json, os, re, sys
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
CH = {1: ('slci', 'slci'), 2: ('schblocs', 'sb'), 3: ('sys1', 's1'), 4: ('sys2', 's2'), 5: ('bode', 'bode'),
      6: ('stabilite', 'stab'), 7: ('precision', 'prec'), 8: ('correcteurs', 'corr')}
src = open(f'{R}/index.html', encoding='utf-8').read()
nums = [int(x) for x in sys.argv[1:]] or [n for n in CH if os.path.exists(f'{R}/video/slci/ch{n}/youtube.json')]

def un(a, b):
    global src
    assert src.count(a) == 1, (src.count(a), a[:80]); src = src.replace(a, b)

def js(s): return s.replace('\\', '\\\\').replace("'", "\\'")

for n in nums:
    cid, pfx = CH[n]
    d = f'{R}/video/slci/ch{n}'
    yt = json.load(open(f'{d}/youtube.json'))
    vid = yt.get('id') or yt.get('video_id') or yt['url'].rsplit('/', 1)[-1]
    info = json.load(open(f'{d}/chapitre.json')); tl = json.load(open(f'{d}/timeline.json'))
    duree = int(round(tl['duree']))
    parties = [[int(tl['scenes'][s]['t0']), tl['scenes'][s]['titre']] for s in tl['ordre']]
    parties[0][0] = 0
    # 1. CHAPTERS : 'video' après 'cours'
    i = src.index("{ id:'%s'" % cid); j = src.index('}', src.index('panels:', i))
    ent = src[i:j]
    if "'video'" not in ent:
        ent2 = ent.replace("panels:['cours',", "panels:['cours','video',", 1)
        assert ent2 != ent, cid
        src = src[:i] + ent2 + src[j:]
    # 2. Onglet et panneau
    tab_cours = f'<button class="tab active" data-panel="{pfx}-cours"><span class="num">01</span>Cours</button>'
    if f'data-panel="{pfx}-video"' not in src:
        un(tab_cours, tab_cours + f'\n  <button class="tab" data-panel="{pfx}-video"><span class="num">02</span>Vidéos</button>')
        k = src.index(f'id="{pfx}-cours"'); k = src.rindex('<section', 0, k); e = src.index('</section>', k) + len('</section>')
        panneau = (f'\n<section class="panel" id="{pfx}-video">\n'
                   f'  <div class="vid-liste" data-videos="{cid}"><p class="vid-attente">Les vidéos du cours au tableau, à lancer une par une.</p></div>\n'
                   '</section>')
        src = src[:e] + panneau + src[e:]
    # 3. Table window.__VIDEOS
    p_txt = ','.join(f"[{t},'{js(ti)}']" for t, ti in parties)
    entree = (f"    {cid}: [\n      {{ yt:'{vid}', titre:'{js(info['titre'])}', duree:{duree}, apercu:'media/videos/slci-{n}.webp',\n"
              f"        parties:[{p_txt}] }}\n    ],\n")
    if re.search(r'\n    %s: \[\n' % cid, src):
        raise SystemExit(f'{cid} déjà dans la table : à mettre à jour à la main')
    un('  window.__VIDEOS = {\n', '  window.__VIDEOS = {\n' + entree)
    print(n, cid, vid, duree, len(parties), 'parties')

open(f'{R}/index.html', 'w', encoding='utf-8').write(src)
