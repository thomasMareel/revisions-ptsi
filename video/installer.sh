#!/bin/bash
# Installe ce qu'il faut pour produire les cours vidéo (Manim, ffmpeg, voix Mistral) et les PDF (LaTeX).
# Sans danger à relancer : ce qui est déjà présent n'est pas réinstallé.  Usage :  bash video/installer.sh
set -u
manque() { ! command -v "$1" >/dev/null 2>&1; }
sty() { ! kpsewhich "$1" >/dev/null 2>&1; }
APT=""
if manque pdflatex || manque kpsewhich; then
  APT="$APT texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-science texlive-pictures texlive-lang-french"
else
  { sty standalone.cls || sty preview.sty || sty tcolorbox.sty || sty titlesec.sty; } && APT="$APT texlive-latex-extra"
  sty mathpazo.sty && APT="$APT texlive-fonts-recommended"
  { sty mhchem.sty || sty siunitx.sty; } && APT="$APT texlive-science"
  sty pgfplots.sty && APT="$APT texlive-pictures"
  sty french.ldf && sty frenchb.ldf && APT="$APT texlive-lang-french"
fi
manque dvisvgm && APT="$APT dvisvgm"
manque ffmpeg && APT="$APT ffmpeg"
pkg-config --exists pangocairo 2>/dev/null || APT="$APT libpango1.0-dev libcairo2-dev pkg-config build-essential python3-dev"
if [ -n "$APT" ]; then
  echo "Installation système :$APT"
  SUDO=""; [ "$(id -u)" -ne 0 ] && SUDO="sudo"
  $SUDO apt-get update -qq && DEBIAN_FRONTEND=noninteractive $SUDO apt-get install -y -qq --no-install-recommends $APT || echo "!! apt a échoué (réseau ?)"
fi
PIP=""
python3 -c "import manim" 2>/dev/null || PIP="$PIP manim==0.22.1"
python3 -c "from mistralai.client import Mistral" 2>/dev/null || PIP="$PIP mistralai==3.7.0"
python3 -c "import soundfile" 2>/dev/null || PIP="$PIP soundfile"
python3 -c "import numpy, scipy" 2>/dev/null || PIP="$PIP numpy scipy"
if [ -n "$PIP" ]; then
  echo "Installation Python :$PIP"
  PIP_BREAK_SYSTEM_PACKAGES=1 python3 -m pip install -q $PIP || echo "!! pip a échoué"
fi

echo; echo "== Contrôle =="
ok=1
for c in pdflatex dvisvgm ffmpeg manim; do
  if manque $c; then echo "ABSENT  $c"; ok=0; else echo "ok      $c"; fi
done
for f in standalone.cls preview.sty mathpazo.sty tcolorbox.sty pgfplots.sty mhchem.sty siunitx.sty; do
  if sty $f; then echo "ABSENT  $f (LaTeX)"; ok=0; fi
done
python3 -c "import manim, soundfile, numpy; from mistralai.client import Mistral; print('ok      Python : manim', manim.__version__)" || ok=0
# Accès à la voix : 200 = clé acceptée ; 401 = service joignable mais aucune clé ; autre = bloqué par le réseau
H=(); [ -n "${MISTRAL_API_KEY:-}" ] && H=(-H "Authorization: Bearer $MISTRAL_API_KEY")
code=$(curl -sS -o /dev/null -w "%{http_code}" --max-time 20 "${H[@]}" https://api.mistral.ai/v1/models 2>/dev/null || echo 000)
case "$code" in
  200) echo "ok      voix Mistral (clé acceptée)";;
  401) echo "!!      voix Mistral : joignable, mais pas de clé (ajouter le secret réseau api.mistral.ai, voir video/README.md)"; ok=0;;
  *)   echo "!!      voix Mistral : injoignable (code $code) — vérifier l'accès réseau de l'environnement"; ok=0;;
esac
[ $ok -eq 1 ] && echo "Tout est prêt." || echo "Installation incomplète : voir les lignes ABSENT / !! ci-dessus."
exit $((1-ok))
