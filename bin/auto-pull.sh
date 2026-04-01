#!/usr/bin/env bash
# DW Skills Git ↔ Claude Sync
# Two-way sync: push local changes (if COMMIT_MSG exists), pull remote, rsync to ~/.claude/skills/
# Runs every 5 minutes via com.dw.skill-git-pull launchd agent
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_SRC="$REPO_DIR/skills"
SKILLS_DST="$HOME/.claude/skills"
COMMIT_MSG_FILE="$REPO_DIR/COMMIT_MSG"
LOG_PREFIX="$(date '+%Y-%m-%d %H:%M:%S')"

cd "$REPO_DIR"
BRANCH=$(git branch --show-current 2>/dev/null || echo "main")

# --- Helper: macOS notification on failure ---
notify_failure() {
    local title="$1"
    local msg="$2"
    osascript -e "display notification \"$msg\" with title \"DW Skill Sync\" subtitle \"$title\" sound name \"Basso\"" 2>/dev/null || true
    echo "$LOG_PREFIX ⚠️  NOTIFICATION: $title — $msg"
}

# --- Step 1: Reverse-sync ~/.claude/skills/ → repo (capture Claude edits) ---
if [ -d "$SKILLS_DST" ] && [ -d "$SKILLS_SRC" ]; then
    for skill_dir in "$SKILLS_SRC"/*/; do
        skill_name=$(basename "$skill_dir")
        if [ -d "$SKILLS_DST/$skill_name" ]; then
            rsync -a --delete "$SKILLS_DST/$skill_name/" "$SKILLS_SRC/$skill_name/"
        fi
    done
fi

# --- Step 2: Auto-push if COMMIT_MSG file exists ---
if [ -f "$COMMIT_MSG_FILE" ]; then
    MSG=$(cat "$COMMIT_MSG_FILE")
    if [ -z "$MSG" ]; then
        MSG="auto-sync: skill updates from $(hostname -s)"
    fi
    git add -A
    if ! git diff --cached --quiet; then
        git commit -m "$MSG" --quiet && \
            git push origin "$BRANCH" --quiet 2>/dev/null && \
            echo "$LOG_PREFIX PUSH: committed and pushed — $MSG" || {
                notify_failure "Push Failed" "Could not push skill changes to GitHub. Check SSH keys or network."
                echo "$LOG_PREFIX PUSH: failed"
            }
    else
        echo "$LOG_PREFIX PUSH: COMMIT_MSG found but no changes to commit"
    fi
    rm -f "$COMMIT_MSG_FILE"
else
    # Still check for uncommitted changes and warn (but don't push)
    git add -A --dry-run 2>/dev/null | grep -q . && \
        echo "$LOG_PREFIX INFO: local changes detected — drop a COMMIT_MSG file to push"
fi

# --- Step 3: Git pull ---
git fetch origin "$BRANCH" --quiet 2>/dev/null || {
    notify_failure "Fetch Failed" "Cannot reach GitHub. Check network or credentials."
    echo "$LOG_PREFIX FETCH FAILED"
    exit 0
}

LOCAL=$(git rev-parse HEAD 2>/dev/null)
REMOTE=$(git rev-parse "origin/$BRANCH" 2>/dev/null)

PULLED=false
if [ "$LOCAL" != "$REMOTE" ]; then
    if git diff --quiet && git diff --cached --quiet; then
        git pull --ff-only origin "$BRANCH" --quiet 2>/dev/null && {
            PULLED=true
            echo "$LOG_PREFIX GIT-PULL: updated to $(git rev-parse --short HEAD)"
        } || {
            notify_failure "Merge Conflict" "Fast-forward pull failed. You have a conflict that needs manual resolution."
            echo "$LOG_PREFIX GIT-PULL: ff-only failed — CONFLICT DETECTED"
        }
    else
        echo "$LOG_PREFIX GIT-PULL: skipped — uncommitted local changes"
    fi
fi

# --- Step 4: Rsync skills into ~/.claude/skills/ ---
if [ -d "$SKILLS_SRC" ]; then
    mkdir -p "$SKILLS_DST"
    for skill_dir in "$SKILLS_SRC"/*/; do
        skill_name=$(basename "$skill_dir")
        rsync -a --delete "$skill_dir" "$SKILLS_DST/$skill_name/"
    done
    if [ "$PULLED" = true ]; then
        echo "$LOG_PREFIX RSYNC: synced $(ls -d "$SKILLS_SRC"/*/ | wc -l | tr -d ' ') skills to $SKILLS_DST"
    fi
fi
