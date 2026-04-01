#!/usr/bin/env bash
# DW Skills Git → Claude Sync
# Pulls latest from GitHub, then rsyncs skills into ~/.claude/skills/
# Runs every 5 minutes via com.dw.skill-git-pull launchd agent
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_SRC="$REPO_DIR/skills"
SKILLS_DST="$HOME/.claude/skills"
LOG_PREFIX="$(date '+%Y-%m-%d %H:%M:%S')"

cd "$REPO_DIR"

# --- Step 1: Git pull ---
BRANCH=$(git branch --show-current 2>/dev/null || echo "main")
git fetch origin "$BRANCH" --quiet 2>/dev/null || { echo "$LOG_PREFIX FETCH FAILED"; exit 0; }

LOCAL=$(git rev-parse HEAD 2>/dev/null)
REMOTE=$(git rev-parse "origin/$BRANCH" 2>/dev/null)

PULLED=false
if [ "$LOCAL" != "$REMOTE" ]; then
    if git diff --quiet && git diff --cached --quiet; then
        git pull --ff-only origin "$BRANCH" --quiet 2>/dev/null && {
            PULLED=true
            echo "$LOG_PREFIX GIT-PULL: updated to $(git rev-parse --short HEAD)"
        } || echo "$LOG_PREFIX GIT-PULL: ff-only failed, skipping"
    else
        echo "$LOG_PREFIX GIT-PULL: skipped — uncommitted local changes"
    fi
fi

# --- Step 2: Rsync skills into ~/.claude/skills/ ---
# Only copies skills that exist in the repo; does NOT delete other skills in dest
if [ -d "$SKILLS_SRC" ]; then
    mkdir -p "$SKILLS_DST"
    # Sync each skill folder individually (no --delete on parent dir)
    for skill_dir in "$SKILLS_SRC"/*/; do
        skill_name=$(basename "$skill_dir")
        rsync -a --delete "$skill_dir" "$SKILLS_DST/$skill_name/"
    done
    if [ "$PULLED" = true ]; then
        echo "$LOG_PREFIX RSYNC: synced $(ls -d "$SKILLS_SRC"/*/ | wc -l | tr -d ' ') skills to $SKILLS_DST"
    fi
else
    echo "$LOG_PREFIX RSYNC: skills directory not found at $SKILLS_SRC"
fi
