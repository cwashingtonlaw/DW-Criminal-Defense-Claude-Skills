#!/usr/bin/env bash
# ============================================================================
# dw-skill-git.sh — D&W Skill Sync via Git
# Daily driver for keeping skills in sync across machines and products.
# ============================================================================
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$REPO_DIR/skills"
CODE_SKILLS="$HOME/.claude/skills"
COWORK_EXPORT_DIR="$REPO_DIR/_cowork-exports"

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; CYAN='\033[0;36m'; NC='\033[0m'
log()  { echo -e "${CYAN}[dw-skills]${NC} $1"; }
warn() { echo -e "${YELLOW}[warn]${NC} $1"; }
err()  { echo -e "${RED}[error]${NC} $1" >&2; }
ok()   { echo -e "${GREEN}[ok]${NC} $1"; }

# Discover every skill across the 9-plugin layout AND the retained flat skills/
# dir, mirroring bin/lint-skills.py discover_skills(). Plugin-housed skills win
# on a name clash. Emits one TAB-separated "<parent_dir>\t<skill_name>" line per
# skill, where <parent_dir> is the directory that directly contains the skill
# folder (so a .skill zip can be built with the skill folder as its top entry).
discover_skill_dirs() {
    local seen=" " d name parent
    for d in "$REPO_DIR"/*/skills/*/; do          # plugin-housed: <plugin>/skills/<name>/
        [ -f "${d}SKILL.md" ] || continue
        name=$(basename "$d")
        case "$seen" in *" $name "*) continue ;; esac
        seen="$seen$name "
        parent=$(dirname "${d%/}")
        printf '%s\t%s\n' "$parent" "$name"
    done
    for d in "$SKILLS_DIR"/*/; do                   # flat (retained non-plugin skills)
        [ -f "${d}SKILL.md" ] || continue
        name=$(basename "$d")
        case "$seen" in *" $name "*) continue ;; esac
        seen="$seen$name "
        printf '%s\t%s\n' "$SKILLS_DIR" "$name"
    done
}

# ── STATUS ──────────────────────────────────────────────────────────────────
cmd_status() {
    echo ""
    echo -e "${BLUE}═══════ D&W Skill Sync Status ═══════${NC}"
    echo ""
    cd "$REPO_DIR"
    local branch
    branch=$(git branch --show-current 2>/dev/null || echo "unknown")
    echo -e "  ${CYAN}Branch:${NC}  $branch"
    git fetch origin "$branch" --quiet 2>/dev/null || true
    local local_hash remote_hash
    local_hash=$(git rev-parse HEAD 2>/dev/null || echo "none")
    remote_hash=$(git rev-parse "origin/$branch" 2>/dev/null || echo "none")

    if [ "$local_hash" = "$remote_hash" ]; then
        echo -e "  ${GREEN}Sync:${NC}    Up to date with remote"
    elif git merge-base --is-ancestor "$local_hash" "$remote_hash" 2>/dev/null; then
        local behind
        behind=$(git rev-list --count HEAD.."origin/$branch" 2>/dev/null || echo "?")
        echo -e "  ${YELLOW}Sync:${NC}    $behind commit(s) behind remote — run 'pull'"
    elif git merge-base --is-ancestor "$remote_hash" "$local_hash" 2>/dev/null; then
        local ahead
        ahead=$(git rev-list --count "origin/$branch"..HEAD 2>/dev/null || echo "?")
        echo -e "  ${YELLOW}Sync:${NC}    $ahead commit(s) ahead of remote — run 'push'"
    else
        echo -e "  ${RED}Sync:${NC}    Diverged from remote — manual merge needed"
    fi

    local changes
    changes=$(git status --porcelain "$SKILLS_DIR" 2>/dev/null | wc -l | tr -d ' ')
    if [ "$changes" -gt 0 ]; then
        echo -e "  ${YELLOW}Local:${NC}   $changes uncommitted change(s)"
        git status --porcelain "$SKILLS_DIR" | head -10 | while read -r line; do
            echo "             $line"
        done
        [ "$changes" -gt 10 ] && echo "             ... and $((changes - 10)) more"
    else
        echo -e "  ${GREEN}Local:${NC}   Clean"
    fi
    local repo_count
    repo_count=$(discover_skill_dirs | wc -l | tr -d ' ')
    echo ""
    echo -e "  ${CYAN}Skills in repo:${NC}  $repo_count"

    if [ -L "$CODE_SKILLS" ]; then
        local target
        target=$(readlink "$CODE_SKILLS")
        if [ "$target" = "$SKILLS_DIR" ]; then
            echo -e "  ${GREEN}Code symlink:${NC}    ✓ ~/.claude/skills → repo"
        else
            echo -e "  ${YELLOW}Code symlink:${NC}    Points to $target (expected $SKILLS_DIR)"
        fi
    elif [ -d "$CODE_SKILLS" ]; then
        echo -e "  ${YELLOW}Code dir:${NC}        ~/.claude/skills is a regular directory (not symlinked)"
    else
        echo -e "  ${RED}Code dir:${NC}        ~/.claude/skills does not exist"
    fi

    local agent_label="com.dw.skill-git-pull"
    if launchctl list 2>/dev/null | grep -q "$agent_label"; then
        echo -e "  ${GREEN}Auto-pull:${NC}       Running"
    else
        echo -e "  ${YELLOW}Auto-pull:${NC}       Not installed (run install-agent.sh)"
    fi

    echo ""
    echo -e "  ${CYAN}Last commit:${NC}"
    git log -1 --format="    %h  %s  (%ar)" 2>/dev/null || echo "    (no commits)"
    echo ""
}
# ── PUSH ────────────────────────────────────────────────────────────────────
cmd_push() {
    local msg="${1:-update skills}"
    cd "$REPO_DIR"
    log "Staging all changes..."
    git add -A
    local changes
    changes=$(git diff --cached --stat | tail -1)
    if [ -z "$changes" ]; then
        ok "Nothing to commit."
        return
    fi
    echo "  $changes"
    git commit -m "$msg"
    log "Pushing to remote..."
    git push
    ok "Pushed: $msg"
}

# ── PULL ────────────────────────────────────────────────────────────────────
cmd_pull() {
    cd "$REPO_DIR"
    log "Pulling latest..."
    local before after
    before=$(git rev-parse HEAD)
    git pull --ff-only origin "$(git branch --show-current)" 2>/dev/null || {
        warn "Fast-forward failed. Remote has diverged."
        echo "  Run 'git pull --rebase' or resolve manually."
        return 1
    }
    after=$(git rev-parse HEAD)
    if [ "$before" = "$after" ]; then
        ok "Already up to date."
    else
        local count
        count=$(git rev-list --count "$before".."$after")
        ok "Pulled $count new commit(s)."
        git log --oneline "$before".."$after" | head -10
    fi
}

# ── DIFF ────────────────────────────────────────────────────────────────────
cmd_diff() {
    cd "$REPO_DIR"
    git diff "$SKILLS_DIR"
    git diff --cached "$SKILLS_DIR"
}

# ── LOG ─────────────────────────────────────────────────────────────────────
cmd_log() {
    cd "$REPO_DIR"
    git log --oneline --graph -20
}

# ── EXPORT-COWORK ───────────────────────────────────────────────────────────
cmd_export_cowork() {
    log "Packaging skills for Cowork import..."
    mkdir -p "$COWORK_EXPORT_DIR"
    local count=0 total=0 dw=0 parent name skilldir outfile current=" "
    # Discover across the plugin layout + flat dir (see discover_skill_dirs).
    while IFS=$'\t' read -r parent name; do
        [ -n "$name" ] || continue
        total=$((total + 1))
        current="$current$name "      # track current names for the prune pass
        case "$name" in dw-*) dw=$((dw + 1)) ;; esac
        skilldir="$parent/$name"
        outfile="$COWORK_EXPORT_DIR/${name}.skill"
        # Incremental: re-zip only when the source is newer than the package.
        if [ ! -f "$outfile" ] || [ "$(find "$skilldir" -newer "$outfile" 2>/dev/null | head -1)" ]; then
            rm -f "$outfile"   # avoid zip appending into a stale archive
            (cd "$parent" && zip -rq "$outfile" "$name/" -x "*.DS_Store")
            count=$((count + 1))
        fi
    done < <(discover_skill_dirs)
    ok "Packaged $count of $total skill(s) ($dw dw-* firm skills, $((total - dw)) other) to: $COWORK_EXPORT_DIR"
    [ "$count" -lt "$total" ] && log "$((total - count)) skill(s) already up to date — skipped."
    # Prune orphaned packages: .skill files with no matching current skill
    # (left over from renamed or retired skills). Keeps the upload set clean so
    # re-uploading the folder to Cowork doesn't create stale duplicates.
    local pruned=0 base f
    for f in "$COWORK_EXPORT_DIR"/*.skill; do
        [ -e "$f" ] || continue
        base=$(basename "$f" .skill)
        case "$current" in *" $base "*) continue ;; esac
        rm -f "$f"
        warn "pruned stale package: ${base}.skill"
        pruned=$((pruned + 1))
    done
    [ "$pruned" -gt 0 ] && log "Pruned $pruned stale package(s) for renamed/retired skills."
}

# ── LINK ────────────────────────────────────────────────────────────────────
cmd_link() {
    if [ -L "$CODE_SKILLS" ]; then
        local target
        target=$(readlink "$CODE_SKILLS")
        if [ "$target" = "$SKILLS_DIR" ]; then
            ok "Symlink already correct."
            return
        fi
        warn "Symlink exists but points to: $target"
        echo -n "  Replace with repo link? [y/N] "
        read -r answer
        [ "$answer" = "y" ] || return
        rm "$CODE_SKILLS"
    elif [ -d "$CODE_SKILLS" ]; then
        warn "~/.claude/skills/ is a regular directory."
        echo "  It will be renamed to ~/.claude/skills.bak.$(date +%s)"
        echo -n "  Proceed? [y/N] "
        read -r answer
        [ "$answer" = "y" ] || return
        mv "$CODE_SKILLS" "${CODE_SKILLS}.bak.$(date +%s)"
    fi
    mkdir -p "$(dirname "$CODE_SKILLS")"
    ln -sfn "$SKILLS_DIR" "$CODE_SKILLS"
    ok "Symlinked: ~/.claude/skills → $SKILLS_DIR"
}

# ── HELP ────────────────────────────────────────────────────────────────────
cmd_help() {
    echo ""
    echo -e "${BLUE}D&W Skill Git Manager${NC}"
    echo ""
    echo "Usage: dw-skill-git.sh <command> [args]"
    echo ""
    echo "Commands:"
    echo "  status              Show sync state, skill count, symlink check"
    echo "  push \"message\"      Stage all + commit + push to remote"
    echo "  pull                Pull latest from remote (fast-forward only)"
    echo "  diff                Show uncommitted changes"
    echo "  log                 Recent commit history"
    echo "  link                Set up ~/.claude/skills symlink to repo"
    echo "  export-cowork       Generate .skill packages for Cowork import"
    echo "  help                This message"
    echo ""
}

# ── DISPATCH ────────────────────────────────────────────────────────────────
case "${1:-help}" in
    status)         cmd_status ;;
    push)           cmd_push "${2:-update skills}" ;;
    pull)           cmd_pull ;;
    diff)           cmd_diff ;;
    log)            cmd_log ;;
    link)           cmd_link ;;
    export-cowork)  cmd_export_cowork ;;
    help|--help|-h) cmd_help ;;
    *)              err "Unknown: $1"; cmd_help; exit 1 ;;
esac
