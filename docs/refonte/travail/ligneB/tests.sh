#!/bin/sh
# Lance la batterie de tests sur la copie de la ligne B. Usage : sh tests.sh <nom-sortie> <options run.js…>
export NODE_PATH=/opt/node22/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
export FONTCONFIG_FILE=/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/ptspe/fonts-sans-lm.conf
D=/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/ligneB
N="$1"
shift
cd /home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-3 || exit 2
node tests/run.js "$@" --sortie="$D/$N" > "$D/$N.log" 2>&1
echo "fin $N code $?" >> "$D/$N.log"
