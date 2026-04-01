# D&W Skills Library

Private repository for Daniels & Washington Claude skill definitions. Syncs across Claude Code and Cowork on all machines.

## Setup (New Machine)

```bash
# 1. Clone
git clone https://github.com/Jobikinobi/dw-skills.git ~/Documents/GitHub/dw-skills

# 2. Symlink for Claude Code
ln -sfn ~/Documents/GitHub/dw-skills/skills ~/.claude/skills

# 3. Install auto-pull agent (optional)
~/Documents/GitHub/dw-skills/bin/install-agent.sh

# 4. Verify
~/Documents/GitHub/dw-skills/bin/dw-skill-git.sh status
```

## Daily Workflow

### After editing a skill on this machine
```bash
~/Documents/GitHub/dw-skills/bin/dw-skill-git.sh push "description of change"
```

### Pulling changes from the other machine
```bash
~/Documents/GitHub/dw-skills/bin/dw-skill-git.sh pull
```

The auto-pull agent checks every 5 minutes if installed.

## Commands

| Command | What it does |
|---------|-------------|
| `dw-skill-git.sh status` | Compare local skills vs repo, show drift |
| `dw-skill-git.sh push "msg"` | Stage all changes + commit + push |
| `dw-skill-git.sh pull` | Pull latest from remote |
| `dw-skill-git.sh diff` | Show what changed since last commit |
| `dw-skill-git.sh log` | Recent commit history |
| `dw-skill-git.sh link` | Set up ~/.claude/skills symlink |
| `dw-skill-git.sh export-cowork` | Generate .skill packages for Cowork import |

## Structure

```
dw-skills/
├── skills/                    ← All skill directories live here
│   ├── dw-case-brain/
│   │   └── SKILL.md
│   ├── dw-criminal-defense/
│   │   ├── SKILL.md
│   │   └── references/
│   └── ...
├── bin/                       ← Management scripts
│   ├── dw-skill-git.sh        ← Daily driver CLI
│   ├── install-agent.sh       ← Set up auto-pull launchd agent
│   └── uninstall-agent.sh     ← Remove auto-pull agent
├── .gitignore
└── README.md
```

## CONFIDENTIAL

This repository contains attorney work product and privileged workflow definitions. Do not make public.
