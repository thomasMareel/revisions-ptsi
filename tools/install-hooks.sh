#!/bin/sh
# Installe les hooks git du projet (à lancer une fois après un clone).
# Usage : sh tools/install-hooks.sh
DIR="$(git rev-parse --git-dir)/hooks"
cp tools/pre-commit "$DIR/pre-commit"
chmod +x "$DIR/pre-commit"
echo "Hook pre-commit installé dans $DIR/pre-commit"
