"""Planche de contrôle : l'image la plus chargée de chaque scène (juste avant l'effacement final),
réunies dans out/planche.jpg. À REGARDER avant d'assembler : chevauchements, textes hors cadre.
À lancer DEPUIS le dossier du chapitre :  python3 ../../commun/planche.py [S0 S3 ...]"""
import json, subprocess, sys, os
tl = json.load(open("timeline.json")); os.makedirs("out/planche", exist_ok=True)
scenes = sys.argv[1:] or tl["ordre"]; imgs = []
for s in scenes:
    t = max(0.0, tl["scenes"][s]["duree"] - 0.7); dst = f"out/planche/{s}.jpg"
    subprocess.run(["ffmpeg","-v","error","-y","-ss",f"{t:.2f}","-i",f"media_{s}/{s}.mp4","-frames:v","1","-vf",
                    f"scale=960:-1,drawtext=text='{s}':x=16:y=h-th-14:fontsize=28:fontcolor=white:box=1:boxcolor=black@0.5","-q:v","3",dst], check=True)
    imgs.append(dst)
cols = 2; rows = -(-len(imgs)//cols); args = ["ffmpeg","-v","error","-y"]
for i in imgs: args += ["-i", i]
if len(imgs) > 1:
    lay = "|".join(f"{(k%cols)*960}_{(k//cols)*540}" for k in range(len(imgs)))
    args += ["-filter_complex", f"xstack=inputs={len(imgs)}:layout={lay}:fill=black", "-q:v", "3", "out/planche.jpg"]
else: args += ["-q:v", "3", "out/planche.jpg"]
subprocess.run(args, check=True); print("out/planche.jpg :", len(imgs), "scène(s) — images seules dans out/planche/")
