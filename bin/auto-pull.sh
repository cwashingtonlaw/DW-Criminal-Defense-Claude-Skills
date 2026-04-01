#!/usr/bin/env bash
set -euo pipefail
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"
BRANCH=$(git branch --show-current 2>/dev/null || echo "main")
git fetch origin "$BRANCH" --quiet 2>/dev/null || exit 0
LOCAL=$(git rev-parse HEAD 2>/dev/null)
REMOTE=$(git rev-parse "origin/$BRANCH" 2>/dev/null)
if [ "$LOCAL" != "$REMOTE" ]; then
    if git diff --quiet && git diff --cached --quiet; then
        git pull --ff-only origin "$BRANCH" --quiet 2>/dev/null && \
            echo "$(date '+%Y-%m-%d %H:%M:%S') AUTO-PULL: updated to $(git rev-parse --short HEAD)" || \
            echo "$(date '+%Y-%m-%d %H:%M:%S') AUTO-PULL: ff-only failed, skipping"
    else
        echo "$(date '+%Y-%m-%d %H:%M:%S') AUTO-PULL: skipped — uncommitted local changes"
    fi
fi
