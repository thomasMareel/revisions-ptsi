"""Assemble le chapitre : recale chaque scène à l'image près, concatène, écrit les sous-titres,
le MP4 final (sous-titres désactivables + chapitres) et la fiche YouTube.
À lancer DEPUIS le dossier du chapitre, après audio.py et rendu.sh :  python3 ../../commun/assemble.py"""
import json, subprocess, re, os
tl = json.load(open("timeline.json")); FPS = 30
INFO = json.load(open("chapitre.json", encoding="utf-8")); NOM = INFO["fichier"]
def run(c): subprocess.run(c, check=True, capture_output=True)
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
os.makedirs("out", exist_ok=True); lst = []
for s in tl["ordre"]:
    src, e = f"media_{s}/{s}.mp4", tl["scenes"][s]["duree"]; d = dur(src); dst = f"out/{s}.mp4"
    manque = round((e - d) * FPS)
    if manque != 0:   # recale la scène à sa durée exacte (image finale = tableau vide)
        run(["ffmpeg","-v","error","-y","-i",src,"-vf",f"tpad=stop_mode=clone:stop_duration={max(manque,0)/FPS}","-frames:v",str(round(e*FPS)),
             "-c:v","libx264","-crf","17","-preset","medium","-pix_fmt","yuv420p","-r","30",dst+".tmp.mp4"]); os.replace(dst+".tmp.mp4", dst)
    else: run(["cp", src, dst])
    lst.append(f"file '{s}.mp4'\n")
open("out/liste.txt","w").write("".join(lst))
run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i","out/liste.txt","-c","copy","out/video_tmp.mp4"]); os.replace("out/video_tmp.mp4","out/video.mp4")
print("vidéo", dur("out/video.mp4"), "audio", dur("narration.wav"), "timeline", tl["duree"])

# --- sous-titres
NBSP = " "
def equilibre(m, maxi=42):
    m = re.sub(r" ([:;?!])", NBSP + r"\1", m)
    if len(m) <= maxi: return m.replace(NBSP, " ")
    mots = m.split(" "); best = None
    for i in range(1, len(mots)):
        a, b = " ".join(mots[:i]), " ".join(mots[i:])
        if len(a) <= maxi and len(b) <= maxi and (best is None or abs(len(a)-len(b)) < best[0]): best = (abs(len(a)-len(b)), a, b)
    if best is None:
        c = [(max(len(" ".join(mots[:i])), len(" ".join(mots[i:]))), i) for i in range(1, len(mots))]
        i = min(c)[1]; best = (0, " ".join(mots[:i]), " ".join(mots[i:]))
    return (best[1] + "\n" + best[2]).replace(NBSP, " ")
def decoupe(txt, maxi=80):
    out, cur = [], ""
    for bout in re.split(r"(?<=[.:?!,])\s+", txt):
        if cur and len(cur) + 1 + len(bout) > maxi: out.append(cur); cur = bout
        else: cur = (cur + " " + bout).strip()
    if cur: out.append(cur)
    res = []
    for o in out:                      # sécurité : morceau encore trop long
        while len(o) > 84:
            k = o.rfind(" ", 0, 80); res.append(o[:k]); o = o[k+1:]
        res.append(o)
    return res
cues, chap = [], []
for s in tl["ordre"]:
    sc = tl["scenes"][s]; chap.append({"t": sc["t0"], "titre": sc["titre"]})
    for p in sc["phrases"]:
        ms = decoupe(p["ecrit"]); tot = sum(len(m) for m in ms); t = sc["t0"] + p["debut"]
        for m in ms:
            d = (p["fin"] - p["debut"]) * len(m) / tot; cues.append([round(t,3), round(t+d,3), equilibre(m)]); t += d
def hms(t, sep):
    ms = int(round(t*1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"
with open("out/soustitres_fr.srt","w",encoding="utf-8") as f:
    for i,(a,b,x) in enumerate(cues,1): f.write(f"{i}\n{hms(a,',')} --> {hms(b,',')}\n{x}\n\n")
print(len(cues), "sous-titres ; plus longue ligne :", max(len(l) for c in cues for l in c[2].split("\n")))
# --- MP4 complet (sous-titres désactivables + chapitres) et fiche pour YouTube
titre = f"{INFO['cours']} — Chapitre {INFO['numero']} : {INFO['titre']}"
meta = ";FFMETADATA1\ntitle=" + titre + "\n"
for i, c in enumerate(chap):
    fin = chap[i+1]["t"] if i+1 < len(chap) else tl["duree"]
    meta += f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={int(c['t']*1000)}\nEND={int(fin*1000)}\ntitle={c['titre']}\n"
open("out/meta.txt","w",encoding="utf-8").write(meta)
os.replace("out/soustitres_fr.srt", f"out/{NOM}.srt")
run(["ffmpeg","-v","error","-y","-i","out/video.mp4","-i","narration.wav","-i",f"out/{NOM}.srt","-i","out/meta.txt","-map","0:v","-map","1:a","-map","2:s","-map_metadata","3",
     "-c:v","copy","-c:a","aac","-b:a","160k","-c:s","mov_text","-metadata:s:a:0","language=fra","-metadata:s:s:0","language=fra","-metadata:s:s:0","title=Français",
     "-disposition:s:0","default","-movflags","+faststart","out/tmp_full.mp4"]); os.replace("out/tmp_full.mp4",f"out/{NOM}.mp4")
print(f"{NOM}.mp4", round(os.path.getsize(f"out/{NOM}.mp4")/1e6,1), "Mo", round(dur(f"out/{NOM}.mp4"),2), "s")
# Fiche YouTube : titre, description, chapitres (le premier doit être à 0:00 ; YouTube en veut au moins 3 de 10 s ou plus)
def mmss(t): t = int(t); return f"{t//60}:{t%60:02d}"
lignes = [titre, "", INFO.get("description", f"Cours de {INFO['cours'].lower()} — programme de PT."), "",
          "Chapitres :"] + [f"{mmss(c['t'])} {c['titre']}" for c in chap] + ["",
          "Narration : voix de synthèse (Voxtral, Mistral AI). Tableau animé avec Manim.",
          "Sous-titres français disponibles (bouton CC)."]
open("out/youtube.txt","w",encoding="utf-8").write("\n".join(lignes) + "\n")
print("fiche YouTube : out/youtube.txt")
