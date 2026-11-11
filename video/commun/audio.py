"""Voix du cours (Voxtral 3, voix Camille par défaut) : synthèse par phrase avec cache, contrôle
(transcription, débit, pauses), régénération des phrases douteuses, assemblage exact par scène, timeline.json.

À lancer DEPUIS le dossier du chapitre (qui contient segments.py) :
    python3 ../../commun/audio.py        (ajouter -v pour voir toutes les phrases)

Clé Mistral : jamais dans le dépôt (voir mistral_client.py et video/MISE-EN-PLACE.md)."""
import os, sys, json, base64, subprocess, re, unicodedata, hashlib, time
import numpy as np, soundfile as sf
from concurrent.futures import ThreadPoolExecutor
from mistral_client import client
sys.path.insert(0, os.getcwd())
from segments import SCENES
c = client()
INFO = json.load(open("chapitre.json", encoding="utf-8")) if os.path.exists("chapitre.json") else {}
VOICE = INFO.get("voix", "voice_3141")   # voice_3141 = Camille, voix prédéfinie de Mistral
# Dynamisme (demande de Thomas, 2026-11-11, à partir du chapitre 4) : « expressivite » = paramètre
# expressiveness de Voxtral (guidage, ≥ 1 ; 3 donne ≈ 30 % d'intonation en plus, mesuré) et « tempo »
# (1,0 : plus de ralentissement). Absents de chapitre.json : réglage d'origine (chapitres 1 à 3).
EXPR = INFO.get("expressivite")
TEMPO = float(INFO.get("tempo", 0.95))
MODEL, SR, FPS, LEAD = "voxtral-mini-tts-3", 24000, 30, 0.8
os.makedirs("audio", exist_ok=True)

def run(cmd): subprocess.run(cmd, check=True, capture_output=True)
def norm(s):
    s = unicodedata.normalize("NFD", s.lower()); s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    NB = set("zero un une deux trois quatre cinq six sept huit neuf dix vingt trente quarante cinquante soixante cent virgule moins plus puissance fois egale egal kelvins kelvin volt volts degres ksi standard standards nuits".split())
    return [w for w in re.sub(r"[^a-z ]", " ", s).split() if len(w) > 3 and w not in NB]
import difflib
def proche(w, B): return w in B or bool(difflib.get_close_matches(w, B, n=1, cutoff=0.72))
def api(f, *a, **k):
    for i in range(5):
        try: return f(*a, **k)
        except Exception as e:
            if i == 4: raise
            time.sleep(2 + 3*i)

def mesure(mp3):
    """durée de parole, plus long silence interne, sur l'audio brut"""
    wav = mp3[:-4] + "_m.wav"
    run(["ffmpeg","-v","error","-y","-i",mp3,"-ac","1","-ar","16000",wav])
    y, sr = sf.read(wav); os.remove(wav)
    hop = 160; n = len(y)//hop
    rms = np.sqrt(np.mean(y[:n*hop].reshape(n, hop)**2, axis=1) + 1e-12); db = 20*np.log10(rms)
    voix = db > -42
    idx = np.where(voix)[0]
    if len(idx) == 0: return 0, 9
    seg = voix[idx[0]:idx[-1]+1]; best = cur = 0
    for v in seg:
        cur = 0 if v else cur + 1; best = max(best, cur)
    return (idx[-1]-idx[0]+1)*hop/sr, best*hop/sr

def synth(sid, dit, essai):
    h = hashlib.md5((dit + f"|{essai}" + (f"|e{EXPR}" if EXPR else "")).encode()).hexdigest()[:10]
    mp3 = f"audio/{sid}_{h}.mp3"
    if not os.path.exists(mp3):
        k = {"expressiveness": float(EXPR)} if EXPR else {}
        r = api(c.audio.speech.complete, model=MODEL, input=dit, voice_id=VOICE, response_format="mp3", **k)
        open(mp3, "wb").write(base64.b64decode(r.audio_data))
    js = mp3[:-4] + ".json"
    if not os.path.exists(js):
        tr = api(c.audio.transcriptions.complete, model="voxtral-mini-latest", file={"content": open(mp3,"rb"), "file_name": "a.mp3"}, language="fr").text
        d, sil = mesure(mp3)
        json.dump({"tr": tr, "parole": d, "silence": sil}, open(js, "w"), ensure_ascii=False)
    m = json.load(open(js))
    a, b = norm(dit), list(set(norm(m["tr"])))
    m["ratio"] = sum(proche(w, b) for w in a) / max(1, len(a))
    m["extra"] = [w for w in b if not proche(w, a)]
    m["debit"] = len(re.sub(r"[^\w]", "", dit)) / max(0.1, m["parole"])
    m["mp3"] = mp3
    m["ksi_ko"] = dit.lower().count("ksi") > len(re.findall(r"\b(ksi|xi|csi|ksy|ξ)\b", m["tr"].lower()))
    tk = re.findall(r"[^\W\d_]+", dit); m["formule"] = sum(len(w) <= 2 and w.lower() not in "à a y un le la de du en et il on ne se ce au ou si sa" .split() for w in tk) / max(1, len(tk)) > 0.22
    return m

segs = [(s[0], x) for s in SCENES for x in s[2]]
with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(lambda sx: synth(sx[1][0], sx[1][2] or sx[1][1], 0), segs))
med = float(np.median([m["debit"] for m in res if not m["formule"]]))
def defauts(m):
    d = []
    if m["ratio"] < 0.9: d.append(f"mots {m['ratio']:.2f}")
    if len(m["extra"]) > 1 or any(len(w) > 5 for w in m["extra"]): d.append(f"ajouts {m['extra']}")
    if m.get("ksi_ko"): d.append("ksi mal transcrit")
    if not m["formule"] and abs(m["debit"]/med - 1) > 0.17: d.append(f"débit {m['debit']:.1f} (médiane {med:.1f})")
    if m["silence"] > 1.0: d.append(f"silence {m['silence']:.2f}s")
    return d
choix, rapport = {}, []
for (scene, x), m in zip(segs, res):
    sid, dit = x[0], x[2] or x[1]; best, e = m, 0
    cle = lambda q: (len(defauts(q)), abs(q["debit"]/med - 1))
    while defauts(best) and e < 6:
        e += 1; m2 = synth(sid, dit, e)
        if cle(m2) < cle(best): best = m2
    choix[sid] = best
    rapport.append((sid, e, defauts(best), best["debit"], best["silence"], best["ratio"], best["tr"]))
print(f"débit médian {med:.1f} car/s")
for r in rapport:
    flag = "  !! " + ", ".join(r[2]) if r[2] else ""
    if r[2] or "-v" in sys.argv: print(f"{r[0]:4} essais+{r[1]} débit {r[3]:4.1f} sil {r[4]:.2f} mots {r[5]:.2f}{flag}\n       {r[6]}")
print("phrases avec défaut restant :", sum(bool(r[2]) for r in rapport), "/", len(rapport), "| régénérées :", sum(r[1]>0 for r in rapport))
json.dump({r[0]: {"defauts": r[2], "tr": r[6]} for r in rapport}, open("rapport.json","w"), ensure_ascii=False, indent=1)

# --- assemblage exact par scène
timeline, pistes, T0 = {"scenes": {}, "ordre": []}, [], 0.0
for scene, titre, phrases in SCENES:
    t, items, clips = LEAD, [], []
    for sid, ecrit, dit, pause in phrases:
        wav = f"audio/{sid}.wav"
        run(["ffmpeg","-v","error","-y","-i",choix[sid]["mp3"],"-ac","1","-ar",str(SR),"-af",
             f"silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse,atempo={TEMPO*(1.0 if choix[sid]['formule'] else float(np.clip((med/choix[sid]['debit'])**0.6,0.85,1.1))):.4f}",wav])
        y, _ = sf.read(wav); d = len(y)/SR
        items.append({"id": sid, "debut": round(t,3), "fin": round(t+d,3), "ecrit": ecrit, "dit": dit or ecrit})
        clips.append((t, y)); t += d + pause
    nfr = int(np.ceil(t*FPS)); duree = nfr/FPS
    piste = np.zeros(int(round(duree*SR)))
    for t0, y in clips:
        i = int(round(t0*SR)); piste[i:i+len(y)] += y[:len(piste)-i]
    pistes.append(piste)
    timeline["scenes"][scene] = {"titre": titre, "t0": round(T0,4), "duree": duree, "phrases": items}
    timeline["ordre"].append(scene); T0 += duree
sf.write("narration_brute.wav", np.concatenate(pistes), SR)
run(["ffmpeg","-v","error","-y","-i","narration_brute.wav","-af","loudnorm=I=-16:TP=-1.5:LRA=11","-ar","48000","narration.wav"])
timeline["duree"] = round(T0,4)
json.dump(timeline, open("timeline.json","w"), ensure_ascii=False, indent=1)
print(f"durée totale {T0:.1f} s = {T0/60:.1f} min")
for s in timeline["ordre"]: print(s, timeline["scenes"][s]["t0"], timeline["scenes"][s]["duree"])
