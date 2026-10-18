#!/bin/sh
# Comme cap.sh, mais sur l'index.html d'origine (wip/refonte) servi depuis ligneB/orig.
export NODE_PATH=/opt/node22/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
export FONTCONFIG_FILE=/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/ptspe/fonts-sans-lm.conf
D=/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/ligneB
SORTIE="$D/$1"
shift
exec node "$D/cap.js" "$D/orig" "$SORTIE" "$@"
