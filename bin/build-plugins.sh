#!/usr/bin/env bash
# build-plugins.sh — package every D&W plugin as a .plugin file for distribution.
#
# .plugin files are the firm's distribution method. A push to origin/main updates
# the source of truth; it does NOT update any machine. Run this, then accept the
# files in Claude to actually ship the change.
#
#   bin/build-plugins.sh                 # build all plugins into ./dist
#   bin/build-plugins.sh dw-trial-prep   # build one
#   bin/build-plugins.sh --check         # report versions, build nothing
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST="$REPO_ROOT/dist"
cd "$REPO_ROOT"

plugins() { for f in */.claude-plugin/plugin.json; do dirname "$(dirname "$f")"; done; }

ver() { python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['version'])" "$1/.claude-plugin/plugin.json"; }

if [[ "${1:-}" == "--check" ]]; then
  printf "%-24s %-10s %s\n" PLUGIN VERSION SKILLS
  for p in $(plugins); do
    printf "%-24s %-10s %s\n" "$p" "$(ver "$p")" "$(ls -d "$p"/skills/*/ 2>/dev/null | wc -l | tr -d ' ')"
  done
  exit 0
fi

# Refuse to build from a dirty tree — a .plugin built from uncommitted work is
# a version number that means nothing.
if [[ -n "$(git status --porcelain)" ]]; then
  echo "ERROR: working tree is dirty. Commit first — a .plugin built from" >&2
  echo "       uncommitted changes carries a version that isn't in git." >&2
  git status --short >&2
  exit 1
fi

targets=("$@")
if [[ ${#targets[@]} -eq 0 ]]; then
  mapfile -t targets < <(plugins)
fi

mkdir -p "$DIST"
for p in "${targets[@]}"; do
  if [[ ! -f "$p/.claude-plugin/plugin.json" ]]; then
    echo "ERROR: $p is not a plugin (no .claude-plugin/plugin.json)" >&2
    exit 1
  fi
  v="$(ver "$p")"
  out="$DIST/$p.plugin"
  rm -f "$out"
  ( cd "$p" && zip -rq "$out" . -x "*.DS_Store" -x "setup/*" )
  printf "  %-24s v%-9s %8s bytes  ->  dist/%s.plugin\n" "$p" "$v" "$(wc -c < "$out" | tr -d ' ')" "$p"
done

echo
echo "Built from $(git rev-parse --short HEAD). Accept these in Claude to ship them —"
echo "nothing on any machine changes until you do."
