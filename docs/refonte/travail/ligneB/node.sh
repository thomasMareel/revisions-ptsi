#!/bin/sh
# Lance un script node de la ligne B avec l'environnement Playwright. Usage : sh node.sh <script.js> [args…]
export NODE_PATH=/opt/node22/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
export FONTCONFIG_FILE=/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/ptspe/fonts-sans-lm.conf
D=/tmp/claude-0/-home-user-revisions-ptsi/e8c533fd-bbf8-5240-a985-2147eaadf7cb/scratchpad/refonte/impl/ligneB
S="$1"
shift
exec node "$D/$S" /home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-3 "$@"
