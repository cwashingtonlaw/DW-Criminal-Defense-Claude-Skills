#!/usr/bin/env bash
# Uninstall the auto-pull launchd agent
set -euo pipefail
AGENT_LABEL="com.dw.skill-git-pull"
AGENT_PLIST="$HOME/Library/LaunchAgents/${AGENT_LABEL}.plist"
if [ -f "$AGENT_PLIST" ]; then
    launchctl unload "$AGENT_PLIST" 2>/dev/null || true
    rm -f "$AGENT_PLIST"
    echo "[ok] Auto-pull agent removed."
else
    echo "[warn] No agent found at $AGENT_PLIST"
fi
