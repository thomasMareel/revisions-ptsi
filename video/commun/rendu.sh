#!/bin/bash
# Rend les scènes données (ou toutes celles de timeline.json), 2 en parallèle.
# À lancer DEPUIS le dossier du chapitre :  bash ../../commun/rendu.sh [S0 S3 ...]
set -u
COMMUN="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="$COMMUN${PYTHONPATH:+:$PYTHONPATH}"
[ -f timeline.json ] || { echo "timeline.json absent : lancer d'abord audio.py"; exit 2; }
mkdir -p logs
S=${@:-$(python3 -c "import json; print(' '.join(json.load(open('timeline.json'))['ordre']))")}
printf "%s\n" $S | xargs -P 2 -I{} sh -c 'manim -qh --fps 30 --disable_caching --media_dir media_{} -o {}_tmp.mp4 scenes.py {} > logs/{}.log 2>&1 && mv media_{}/videos/scenes/1080p30/{}_tmp.mp4 media_{}/{}.mp4 && echo "{} ok" || echo "{} ECHEC (voir logs/{}.log)"'
grep -h "RETARD" logs/*.log 2>/dev/null | sort | uniq
