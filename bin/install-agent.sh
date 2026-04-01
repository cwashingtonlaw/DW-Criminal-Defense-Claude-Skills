#!/usr/bin/env bash
# ============================================================================
# install-agent.sh — Install launchd auto-pull agent
# Checks for remote changes every 5 minutes and fast-forward pulls.
# ============================================================================
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
AGENT_LABEL="com.dw.skill-git-pull"
AGENT_PLIST="$HOME/Library/LaunchAgents/${AGENT_LABEL}.plist"
PULL_SCRIPT="$REPO_DIR/bin/auto-pull.sh"
LOG_FILE="$REPO_DIR/sync.log"

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

# Create the lightweight pull script the agent will run
cat > "$PULL_SCRIPT" << 'PULLEOF'
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
PULLEOF
chmod +x "$PULL_SCRIPT"

# Unload existing if present
launchctl unload "$AGENT_PLIST" 2>/dev/null || true

# Write the plist
mkdir -p "$(dirname "$AGENT_PLIST")"
cat > "$AGENT_PLIST" << PLISTEOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${AGENT_LABEL}</string>
    <key>ProgramArguments</key>
    <array>
        <string>${PULL_SCRIPT}</string>
    </array>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>StandardOutPath</key>
    <string>${LOG_FILE}</string>
    <key>StandardErrorPath</key>
    <string>${LOG_FILE}</string>
    <key>RunAtLoad</key>
    <true/>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin</string>
    </dict>
</dict>
</plist>
PLISTEOF

launchctl load "$AGENT_PLIST"

echo -e "${GREEN}[ok]${NC} Auto-pull agent installed."
echo "  Checks remote every 5 minutes."
echo "  Log: $LOG_FILE"
echo "  Plist: $AGENT_PLIST"
echo ""
echo -e "${YELLOW}Install this on BOTH machines.${NC}"
