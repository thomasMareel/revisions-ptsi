#!/bin/sh
# Lance cap.js sur la copie de travail de la ligne B. Usage : sh cap.sh <dossier-sortie> <spec>…
export NODE_PATH=/opt/node22/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
export FONTCONFIG_FILE=/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/ptspe/fonts-sans-lm.conf
D=/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/ligneB
SORTIE="$D/$1"
shift
exec node "$D/cap.js" /home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-3 "$SORTIE" "$@"
