# dw-skills Plugin Packaging Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Repackage the 69 `dw-*` criminal-defense skills into a single machine-local Claude Code marketplace exposing 8 functional plugins + `dw-core`, with `dw-core` as the single source of truth (no duplication).

**Architecture:** Approach B from `docs/superpowers/specs/2026-05-29-plugin-packaging-design.md`. Nine plugin directories at repo root, each with `.claude-plugin/plugin.json` + `skills/`; a root `.claude-plugin/marketplace.json` lists all nine with **local** `source` paths (referenced in place, so cross-plugin `../` file refs resolve). The flat `skills/` dir is retained for 6 non-dw skills (symlink stays valid). `bin/` tooling is updated to discover skills across the plugin layout.

**Tech Stack:** Claude Code plugins/marketplaces (JSON manifests), Python 3 maintenance scripts (`bin/lint-skills.py`, `bin/regen-skill-index.py`, `bin/add-category-frontmatter.py`), git.

**Branch:** `plugin-packaging` (already created; spec already committed there).

**Hard rule:** Do NOT proceed past Task 7's lint gate if `bin/lint-skills.py` reports any error. Stop and fix.

---

## File Structure

**Created:**
- `.claude-plugin/marketplace.json` — marketplace manifest, 9 plugins.
- `dw-core/.claude-plugin/plugin.json` + 8 more (`dw-intake-discovery`, `dw-evidence-audit`, `dw-offense-specialists`, `dw-pleadings`, `dw-trial-prep`, `dw-transcription`, `dw-disposition`, `dw-ops`).

**Moved (via `git mv`):** 69 `skills/dw-*/` → `<plugin>/skills/dw-*/` per the grouping table below.

**Modified:**
- 6 SKILL.md files — repoint 8 `../dw-shared-protocols/...` references.
- `bin/lint-skills.py` — add `discover_skills()` helper; use it for discovery + single-skill lookup + `all_skill_names`.
- `bin/regen-skill-index.py` — reuse `discover_skills()`; namespace skill names in rendered tables.
- `bin/add-category-frontmatter.py` — discover via plugin layout.
- `CLAUDE.md`, `README.md` — note namespaced invocation + plugin layout.
- Memory `dw-skills-maintenance-state` — mark plugin packaging done.

**Deleted:** 4 empty `skills/iron-gavel-*` cruft dirs.

### Grouping table (source of truth for moves)

| Plugin | Skills |
|---|---|
| `dw-core` | dw-case-brain, dw-case-dashboard, dw-criminal-defense, dw-data-contracts, dw-shared-protocols, dw-skill-index |
| `dw-intake-discovery` | dw-client-intake-interview, dw-brady-giglio-auditor, dw-discovery-compliance-monitor, dw-discovery-orchestrator |
| `dw-evidence-audit` | dw-cell-site-geolocation-auditor, dw-chain-of-custody-auditor, dw-child-forensic-interview-auditor, dw-confession-interrogation-auditor, dw-crime-lab-auditor, dw-crime-scene-auditor, dw-dna-forensic-biology-auditor, dw-expert-witness-evaluator, dw-eyewitness-identification-auditor, dw-forensic-dump-analyzer, dw-jail-call-analyzer, dw-mobile-forensic-auditor, dw-social-media-auditor, dw-sqlite-recovery, dw-video-evidence-auditor, dw-witness-statement-analyzer |
| `dw-offense-specialists` | dw-drug-offense-specialist, dw-dwi-specialist, dw-firearms-specialist, dw-sex-offense-specialist, dw-violent-crime-specialist |
| `dw-pleadings` | dw-404b-opposition, dw-bond-and-release-motion, dw-pretrial-motion-library, dw-suppression-motion |
| `dw-trial-prep` | dw-adversarial-stress-test, dw-appellate-error-monitor, dw-cross-exam-architect, dw-defense-investigator-tasking, dw-direct-exam-architect, dw-exhibit-manager, dw-issue-code-tracker, dw-jury-focus-group, dw-jury-instructions-builder, dw-theory-to-workplan, dw-timeline-builder, dw-trial-day-assistant, dw-trial-narrative-builder, dw-trial-notebook-builder, dw-voir-dire-assistant, dw-witness-threat-matrix, dw-neutral-inventory, dw-theory-deconstructor |
| `dw-transcription` | dw-dmar-synthesizer, dw-transcript-pipeline-calcasieu, dw-transcript-pipeline-rev, dw-transcript-router |
| `dw-disposition` | dw-appellate-brief-builder, dw-case-disposition, dw-habitual-offender-auditor, dw-plea-negotiation-analyzer, dw-post-conviction-relief, dw-sentencing-mitigation-specialist |
| `dw-ops` | dw-billing-narrative-generator, dw-case-law-researcher, dw-client-communication-drafter, dw-court-jail-tracker, dw-evidence-placeholder, dw-image-filename-stamp |

---

## Task 1: Pre-flight verification

**Files:** none (read-only checks).

- [ ] **Step 1: Confirm branch + clean tree**

Run:
```bash
cd ~/Documents/GitHub/dw-skills
git branch --show-current   # expect: plugin-packaging
git status -s               # expect: empty (spec already committed)
```
Expected: branch is `plugin-packaging`, no uncommitted changes.

- [ ] **Step 2: Snapshot the baseline skill count**

Run:
```bash
ls -d skills/dw-*/ | wc -l   # expect: 69
bin/lint-skills.py --quiet   # expect: 0 errors (baseline green)
```
Expected: 69 dw-* skills; lint passes. Record both — they are the invariants the migration must preserve.

---

## Task 2: Create the migration helper script

A throwaway script encodes the grouping table once and is reused for the move and for verification. This keeps the 69→9 mapping DRY and auditable.

**Files:**
- Create: `bin/_packaging_map.py`

- [ ] **Step 1: Write the mapping module**

```python
# bin/_packaging_map.py — single source of truth for the plugin grouping.
# Throwaway: delete after the move lands (Task 8). Keys are plugin dir names;
# values are the dw-* skill dir names that belong in <plugin>/skills/.
PLUGINS = {
    "dw-core": [
        "dw-case-brain", "dw-case-dashboard", "dw-criminal-defense",
        "dw-data-contracts", "dw-shared-protocols", "dw-skill-index",
    ],
    "dw-intake-discovery": [
        "dw-client-intake-interview", "dw-brady-giglio-auditor",
        "dw-discovery-compliance-monitor", "dw-discovery-orchestrator",
    ],
    "dw-evidence-audit": [
        "dw-cell-site-geolocation-auditor", "dw-chain-of-custody-auditor",
        "dw-child-forensic-interview-auditor", "dw-confession-interrogation-auditor",
        "dw-crime-lab-auditor", "dw-crime-scene-auditor",
        "dw-dna-forensic-biology-auditor", "dw-expert-witness-evaluator",
        "dw-eyewitness-identification-auditor", "dw-forensic-dump-analyzer",
        "dw-jail-call-analyzer", "dw-mobile-forensic-auditor",
        "dw-social-media-auditor", "dw-sqlite-recovery",
        "dw-video-evidence-auditor", "dw-witness-statement-analyzer",
    ],
    "dw-offense-specialists": [
        "dw-drug-offense-specialist", "dw-dwi-specialist",
        "dw-firearms-specialist", "dw-sex-offense-specialist",
        "dw-violent-crime-specialist",
    ],
    "dw-pleadings": [
        "dw-404b-opposition", "dw-bond-and-release-motion",
        "dw-pretrial-motion-library", "dw-suppression-motion",
    ],
    "dw-trial-prep": [
        "dw-adversarial-stress-test", "dw-appellate-error-monitor",
        "dw-cross-exam-architect", "dw-defense-investigator-tasking",
        "dw-direct-exam-architect", "dw-exhibit-manager",
        "dw-issue-code-tracker", "dw-jury-focus-group",
        "dw-jury-instructions-builder", "dw-theory-to-workplan",
        "dw-timeline-builder", "dw-trial-day-assistant",
        "dw-trial-narrative-builder", "dw-trial-notebook-builder",
        "dw-voir-dire-assistant", "dw-witness-threat-matrix",
        "dw-neutral-inventory", "dw-theory-deconstructor",
    ],
    "dw-transcription": [
        "dw-dmar-synthesizer", "dw-transcript-pipeline-calcasieu",
        "dw-transcript-pipeline-rev", "dw-transcript-router",
    ],
    "dw-disposition": [
        "dw-appellate-brief-builder", "dw-case-disposition",
        "dw-habitual-offender-auditor", "dw-plea-negotiation-analyzer",
        "dw-post-conviction-relief", "dw-sentencing-mitigation-specialist",
    ],
    "dw-ops": [
        "dw-billing-narrative-generator", "dw-case-law-researcher",
        "dw-client-communication-drafter", "dw-court-jail-tracker",
        "dw-evidence-placeholder", "dw-image-filename-stamp",
    ],
}

DESCRIPTIONS = {
    "dw-core": "Foundation: session persistence, shared protocols, data contracts, master orchestrator, case dashboard, and skill index. Every other dw plugin depends on this.",
    "dw-intake-discovery": "Client intake interview plus discovery orchestration, compliance monitoring, and Brady/Giglio audit.",
    "dw-evidence-audit": "Methodology and reliability audits across all evidence types: forensics, interrogations, eyewitness ID, cell-site, video, social media, lab, DNA, chain of custody.",
    "dw-offense-specialists": "Element-by-element defense theory for drug, DWI, firearms, sex, and violent-crime charges.",
    "dw-pleadings": "Motion drafting: suppression, 404(b) opposition, bond/release, and the pretrial motion library.",
    "dw-trial-prep": "Trial preparation: cross/direct exam, voir dire, jury instructions, exhibits, timelines, trial-day assistant, error preservation, theory tools, and investigator tasking.",
    "dw-transcription": "Media transcription routing and DMAR pipelines (Calcasieu + Rev) plus cross-case DMAR synthesis.",
    "dw-disposition": "Sentencing, habitual-offender audit, plea analysis, appeal, post-conviction relief, and case disposition.",
    "dw-ops": "Operational utilities: billing narratives, case-law research, client communications, court/jail tracker, evidence placeholders, image stamping.",
}

if __name__ == "__main__":
    total = sum(len(v) for v in PLUGINS.values())
    assert total == 69, f"expected 69 skills, got {total}"
    print(f"{len(PLUGINS)} plugins, {total} skills — map OK")
```

- [ ] **Step 2: Verify the map sums to 69**

Run:
```bash
python3 bin/_packaging_map.py   # expect: "9 plugins, 69 skills — map OK"
```
Expected: prints OK (assertion guarantees 69).

- [ ] **Step 3: Verify the map matches what's on disk (no typo, no orphan)**

Run:
```bash
python3 - <<'PY'
from pathlib import Path
import sys; sys.path.insert(0, "bin")
from _packaging_map import PLUGINS
mapped = {s for v in PLUGINS.values() for s in v}
ondisk = {p.name for p in Path("skills").iterdir() if p.is_dir() and p.name.startswith("dw-")}
print("in map not on disk:", sorted(mapped - ondisk))
print("on disk not in map:", sorted(ondisk - mapped))
PY
```
Expected: both lists empty. If not, fix `_packaging_map.py` before continuing.

- [ ] **Step 4: Commit**

```bash
git add bin/_packaging_map.py
git commit -m "build: packaging grouping map (throwaway migration helper)"
```

---

## Task 3: Scaffold plugin manifests

**Files:**
- Create: `.claude-plugin/marketplace.json`
- Create: `<plugin>/.claude-plugin/plugin.json` × 9

- [ ] **Step 1: Generate all manifests from the map**

Run:
```bash
python3 - <<'PY'
import json, sys
from pathlib import Path
sys.path.insert(0, "bin")
from _packaging_map import PLUGINS, DESCRIPTIONS

root = Path(".")
author = {"name": "Chris Washington", "email": "cjw@danielswashington.com"}

# Per-plugin plugin.json
for plugin in PLUGINS:
    d = root / plugin / ".claude-plugin"
    d.mkdir(parents=True, exist_ok=True)
    (d / "plugin.json").write_text(json.dumps({
        "name": plugin,
        "version": "1.0.0",
        "description": DESCRIPTIONS[plugin],
        "author": author,
        "skills": "./skills",
    }, indent=2) + "\n", encoding="utf-8")

# Root marketplace.json
mp = {
    "name": "dw-criminal-defense",
    "owner": {"name": "Chris Washington", "url": "https://danielswashington.com"},
    "description": "Daniels & Washington criminal-defense toolkit — 69 skills across 8 plugins plus dw-core foundation.",
    "metadata": {"version": "1.0.0"},
    "plugins": [
        {
            "name": p,
            "source": f"./{p}",
            "description": DESCRIPTIONS[p],
            "version": "1.0.0",
            "author": author,
        } for p in PLUGINS
    ],
}
mpd = root / ".claude-plugin"
mpd.mkdir(parents=True, exist_ok=True)
(mpd / "marketplace.json").write_text(json.dumps(mp, indent=2) + "\n", encoding="utf-8")
print("manifests written")
PY
```
Expected: prints "manifests written".

- [ ] **Step 2: Validate JSON + plugin count**

Run:
```bash
python3 -c "import json; d=json.load(open('.claude-plugin/marketplace.json')); print('plugins:', len(d['plugins'])); assert len(d['plugins'])==9"
for p in dw-core dw-intake-discovery dw-evidence-audit dw-offense-specialists dw-pleadings dw-trial-prep dw-transcription dw-disposition dw-ops; do python3 -c "import json; json.load(open('$p/.claude-plugin/plugin.json'))" && echo "$p ok"; done
```
Expected: `plugins: 9` and 9 `... ok` lines.

- [ ] **Step 3: Commit**

```bash
git add .claude-plugin '*/.claude-plugin/plugin.json'
git commit -m "feat: marketplace + 9 plugin manifests (skills not yet moved)"
```

---

## Task 4: Move the 69 skills into their plugins

**Files:** moves only (`git mv`).

- [ ] **Step 1: Move every skill per the map**

Run:
```bash
python3 - <<'PY'
import subprocess, sys
from pathlib import Path
sys.path.insert(0, "bin")
from _packaging_map import PLUGINS
for plugin, skills in PLUGINS.items():
    dest = Path(plugin) / "skills"
    dest.mkdir(parents=True, exist_ok=True)
    for s in skills:
        src = Path("skills") / s
        assert src.is_dir(), f"missing source: {src}"
        subprocess.run(["git", "mv", str(src), str(dest / s)], check=True)
print("moved 69 skills")
PY
```
Expected: prints "moved 69 skills", no assertion/`git mv` errors.

- [ ] **Step 2: Verify placement counts (must equal the map)**

Run:
```bash
for p in dw-core dw-intake-discovery dw-evidence-audit dw-offense-specialists dw-pleadings dw-trial-prep dw-transcription dw-disposition dw-ops; do printf "%-24s %s\n" "$p" "$(ls -d $p/skills/dw-*/ 2>/dev/null | wc -l | tr -d ' ')"; done
echo "TOTAL placed: $(ls -d */skills/dw-*/ 2>/dev/null | wc -l)"
echo "remaining dw-* in flat skills/: $(ls -d skills/dw-*/ 2>/dev/null | wc -l)"
```
Expected: counts `6 4 16 5 4 18 4 6 6`, TOTAL `69`, remaining flat `0`.

- [ ] **Step 3: Confirm only the 6 non-dw skills remain in skills/**

Run:
```bash
ls skills/ | grep -v '^iron-gavel-' | sort
```
Expected exactly: `file-organizer  frontend-design  medical-chronology  notebooklm  ui-ux-pro-max  youtube-transcript`.

- [ ] **Step 4: Delete the 4 iron-gavel cruft dirs**

Run:
```bash
rm -rf skills/iron-gavel-client-sponsor skills/iron-gavel-episode-prep skills/iron-gavel-research-outreach skills/iron-gavel-youtube-growth
git add -A skills/
ls skills/   # expect: only the 6 non-dw skills
```
Expected: `skills/` lists only the 6 non-dw skills.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "refactor: move 69 dw-* skills into 9 plugin dirs; drop iron-gavel cruft"
```

---

## Task 5: Repoint the 8 cross-plugin file references

All 8 live in a `SKILL.md` at depth `<plugin>/skills/<skill>/SKILL.md`. From there, `dw-core` is reached via `../../../dw-core/skills/dw-shared-protocols/...` (3× `../`). Every occurrence of `../dw-shared-protocols/` becomes `../../../dw-core/skills/dw-shared-protocols/`.

**Files (modify):**
- `dw-disposition/skills/dw-sentencing-mitigation-specialist/SKILL.md` (lines 8, 239)
- `dw-trial-prep/skills/dw-issue-code-tracker/SKILL.md` (line 29)
- `dw-pleadings/skills/dw-bond-and-release-motion/SKILL.md` (line 7)
- `dw-disposition/skills/dw-post-conviction-relief/SKILL.md` (lines 259, 285)
- `dw-pleadings/skills/dw-404b-opposition/SKILL.md` (line 8)
- `dw-pleadings/skills/dw-suppression-motion/SKILL.md` (line 8)

- [ ] **Step 1: Apply the uniform repoint across the 6 files**

Run:
```bash
for f in \
  dw-disposition/skills/dw-sentencing-mitigation-specialist/SKILL.md \
  dw-trial-prep/skills/dw-issue-code-tracker/SKILL.md \
  dw-pleadings/skills/dw-bond-and-release-motion/SKILL.md \
  dw-disposition/skills/dw-post-conviction-relief/SKILL.md \
  dw-pleadings/skills/dw-404b-opposition/SKILL.md \
  dw-pleadings/skills/dw-suppression-motion/SKILL.md ; do
    perl -i -pe 's{\.\./dw-shared-protocols/}{../../../dw-core/skills/dw-shared-protocols/}g' "$f"
done
echo "repointed"
```
Expected: prints "repointed".

- [ ] **Step 2: Verify no stale 2-dot refs remain and the new refs resolve on disk**

Run:
```bash
echo "stale refs left (expect 0):"; grep -rn '\.\./dw-shared-protocols' */skills/ | grep -v '\.\./\.\./\.\./dw-core/' | wc -l
echo "new refs that DO NOT resolve on disk (expect empty):"
python3 - <<'PY'
import re
from pathlib import Path
bad=[]
for md in Path(".").glob("*/skills/dw-*/SKILL.md"):
    for m in re.finditer(r'(\.\./\.\./\.\./dw-core/skills/dw-shared-protocols/[^\s`)]+)', md.read_text(encoding="utf-8")):
        target=(md.parent / m.group(1)).resolve()
        if not target.exists(): bad.append((str(md), m.group(1)))
for b in bad: print(b)
PY
```
Expected: `0` stale refs; the Python block prints nothing (every repointed path resolves).

- [ ] **Step 3: Commit**

```bash
git add */skills/*/SKILL.md
git commit -m "fix: repoint 8 dw-shared-protocols refs to dw-core depth"
```

---

## Task 6: Update `bin/` discovery tooling

Add one shared discovery helper in `lint-skills.py`, reuse it everywhere. It derives the plugin namespace from the layout (`<plugin>/skills/<skill>` → plugin = `parent.parent.name`).

**Files (modify):** `bin/lint-skills.py`, `bin/regen-skill-index.py`, `bin/add-category-frontmatter.py`

- [ ] **Step 1: Add `discover_skills()` to `bin/lint-skills.py`**

Insert after the `SKILLS_DIR = REPO_ROOT / "skills"` line (around line 34):

```python
def discover_skills():
    """Yield (plugin_name_or_None, skill_dir) across the plugin layout and the
    retained flat skills/ dir. plugin_name is None for flat (non-plugin) skills."""
    seen = set()
    for p in sorted(REPO_ROOT.glob("*/skills/dw-*"), key=lambda x: x.name):
        if p.is_dir() and p.name not in seen:
            seen.add(p.name)
            yield p.parent.parent.name, p
    if SKILLS_DIR.is_dir():
        for p in sorted((q for q in SKILLS_DIR.iterdir() if q.is_dir()), key=lambda x: x.name):
            if p.name not in seen:
                seen.add(p.name)
                yield None, p


def discover_skill_dirs():
    """All skill directories (plugin-housed + flat), sorted by name."""
    return [d for _, d in discover_skills()]
```

- [ ] **Step 2: Rewire the `main()` discovery in `bin/lint-skills.py`**

Replace the discovery block (the `if args.skill: ... else: all_dirs = sorted(...)` section near line 345 and the `all_skill_names` line near 357) with:

```python
    all_dirs = discover_skill_dirs()
    by_name = {d.name: d for d in all_dirs}

    if args.skill:
        if args.skill not in by_name:
            print(f"Skill not found: {args.skill}", file=sys.stderr)
            return 2
        targets = [by_name[args.skill]]
    elif args.all:
        targets = all_dirs
    else:
        targets = [d for d in all_dirs if d.name.startswith("dw-")]

    all_skill_names = set(by_name)
```

Delete the now-obsolete `if not SKILLS_DIR.is_dir(): print("skills/ not found"...) return 2` guard above it (the plugin layout no longer requires a flat `skills/`).

- [ ] **Step 3: Reuse the helper in `bin/regen-skill-index.py`**

In `load_skills()` (near line 298), replace `for d in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):` with:

```python
    for d in _lint_skills.discover_skill_dirs():
```

(`_lint_skills` is already imported at the top of the file.) Remove the `if not SKILLS_DIR.is_dir(): raise SystemExit(...)` guard just above it.

- [ ] **Step 4: Namespace skill names in the rendered index tables**

In `bin/regen-skill-index.py`, add near the top (after the `_lint_skills` import block):

```python
# Map bare skill name -> plugin namespace, derived from the on-disk layout.
PLUGIN_OF = {d.name: plugin for plugin, d in _lint_skills.discover_skills()}

def ns(skill_name: str) -> str:
    """Namespaced display name, e.g. dw-pleadings:dw-suppression-motion."""
    p = PLUGIN_OF.get(skill_name)
    return f"{p}:{skill_name}" if p else skill_name
```

Then in `render_section()`, change the two skill-cell builders:
- `shared_references` branch: `lines.append(f"| `{ns(skill_name)}` | {label} | {read_by} |")`
- normal rows: `skill_cell = f"`{ns(skill_name)}`{suffix}"` and the no-suffix branch `skill_cell = f"`{ns(skill_name)}`"`.

- [ ] **Step 5: Update `bin/add-category-frontmatter.py` discovery**

Replace its skill discovery (near line 184) `skills = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and p.name.startswith("dw-"))` with:

```python
    skills = sorted(
        (p for p in REPO_ROOT.glob("*/skills/dw-*") if p.is_dir()),
        key=lambda p: p.name,
    )
```

- [ ] **Step 6: Sanity-check discovery finds all 69**

Run:
```bash
python3 - <<'PY'
import sys; sys.path.insert(0, "bin")
import importlib.util
spec = importlib.util.spec_from_file_location("lint_skills", "bin/lint-skills.py")
m = importlib.util.module_from_spec(spec); sys.modules["lint_skills"]=m; spec.loader.exec_module(m)
dw = [d for d in m.discover_skill_dirs() if d.name.startswith("dw-")]
print("dw skills discovered:", len(dw))            # expect 69
print("sample namespace:", dict((p,d.name) for p,d in m.discover_skills() if d.name=="dw-suppression-motion"))
PY
```
Expected: `dw skills discovered: 69`; sample shows `{'dw-pleadings': 'dw-suppression-motion'}`.

- [ ] **Step 7: Commit**

```bash
git add bin/lint-skills.py bin/regen-skill-index.py bin/add-category-frontmatter.py
git commit -m "build: bin tooling discovers skills across plugin layout"
```

---

## Task 7: Regenerate index + lint gate

**Files (modify):** `dw-core/skills/dw-skill-index/SKILL.md` (regenerated).

- [ ] **Step 1: Regenerate the index tables**

Run:
```bash
bin/regen-skill-index.py
git diff --stat dw-core/skills/dw-skill-index/SKILL.md
```
Expected: the index SKILL.md updates; diff shows skill cells now namespaced (e.g. `dw-pleadings:dw-suppression-motion`).

- [ ] **Step 2: Lint gate (MUST be 0 errors)**

Run:
```bash
bin/lint-skills.py
echo "exit: $?"
```
Expected: `exit: 0`, no `E#` errors. If any error: STOP, diagnose (likely a missed ref repoint or a discovery edge case), fix, re-run. Do not proceed on red.

- [ ] **Step 3: Confirm E4 cross-references still resolve**

Run:
```bash
bin/lint-skills.py 2>&1 | grep -i "E4" | wc -l   # expect 0
```
Expected: `0` — every `dw-*` mention still resolves against the discovered name set.

- [ ] **Step 4: Commit**

```bash
git add dw-core/skills/dw-skill-index/SKILL.md
git commit -m "docs: regenerate skill index with namespaced names"
```

---

## Task 8: Install the marketplace + smoke test

**Files:** none (registration + live checks). This is the step that switches daily use from the symlink to the marketplace.

- [ ] **Step 1: Remove the throwaway helper**

```bash
git rm bin/_packaging_map.py
git commit -m "chore: drop throwaway packaging map"
```

- [ ] **Step 2: Add the local marketplace and enable all 9 plugins**

In the Claude Code session, run:
```
/plugin marketplace add ~/Documents/GitHub/dw-skills
```
Then enable each plugin (or via `/plugin` UI): `dw-core`, `dw-intake-discovery`, `dw-evidence-audit`, `dw-offense-specialists`, `dw-pleadings`, `dw-trial-prep`, `dw-transcription`, `dw-disposition`, `dw-ops`.

Expected: marketplace `dw-criminal-defense` registers; 9 plugins install with `installPath` pointing at the repo dirs (in place).

- [ ] **Step 3: Verify in-place install + namespaced availability**

Run:
```bash
python3 -c "import json; d=json.load(open('$HOME/.claude/plugins/installed_plugins.json')); ks=[k for k in d if k.endswith('@dw-criminal-defense')]; print('installed:', len(ks)); [print(' ', k, d[k][0]['installPath']) for k in sorted(ks)]"
```
Expected: `installed: 9`, each `installPath` under `~/Documents/GitHub/dw-skills/<plugin>` (in place, not cache).

- [ ] **Step 4: Smoke test — one skill per plugin + a cross-plugin load**

In session, confirm these are invocable by namespace (spot-check, not all 69): `/dw-core:dw-case-brain`, `/dw-pleadings:dw-suppression-motion`, `/dw-evidence-audit:dw-mobile-forensic-auditor`, `/dw-disposition:dw-sentencing-mitigation-specialist`. Then invoke `/dw-pleadings:dw-suppression-motion` and confirm it can still read `dw-core`'s `template-selection-protocol.md` (cross-plugin file load resolves) and that `/dw-core:dw-criminal-defense` orchestrator routing references a specialist in another plugin without error.

Expected: all spot-checked skills resolve; the cross-plugin file read succeeds.

- [ ] **Step 5: Decide on the `~/.claude/skills` symlink**

The symlink now surfaces only the 6 non-dw skills (dw-* moved out). Leave it as-is (keeps those 6 loading). Confirm no dw-* double-loads:
```bash
ls ~/.claude/skills | grep '^dw-' | wc -l   # expect 0
```
Expected: `0` (no dw-* visible via the symlink path → no duplicate-load conflict with the plugins).

---

## Task 9: Docs + memory + merge

**Files (modify):** `CLAUDE.md`, `README.md`, `docs/skill-dependency-graph.md`, memory `dw-skills-maintenance-state`.

- [ ] **Step 1: Update repo docs**

In `README.md` and `CLAUDE.md`, add a short "Plugin layout" note: skills now live in 9 plugins under a local marketplace; invoke as `plugin:skill` (e.g. `/dw-pleadings:dw-suppression-motion`); `dw-core` is the shared foundation; the flat `skills/` holds only non-dw personal skills. In `docs/skill-dependency-graph.md`, update the "Cross-category dependency boundaries" note to say the packaging is now implemented (Approach B, machine-local).

- [ ] **Step 2: Commit docs**

```bash
git add README.md CLAUDE.md docs/skill-dependency-graph.md
git commit -m "docs: reflect 9-plugin marketplace layout + namespaced invocation"
```

- [ ] **Step 3: Update the maintenance memory**

Edit `~/.claude/projects/-Users-greatelephant82/memory/project_dw_skills_maintenance.md`: move "Plugin packaging (8-plugin + dw-core)" from Open to Done with date 2026-05-29 and a one-line note (Approach B, machine-local, namespaced invocation, branch `plugin-packaging`). Update the MEMORY.md index line if its hook changed.

- [ ] **Step 4: Merge to main**

```bash
cd ~/Documents/GitHub/dw-skills
bin/lint-skills.py --quiet   # final green check, expect 0 errors
git checkout main
git merge --no-ff plugin-packaging -m "feat: package dw-skills into 9-plugin local marketplace (Approach B)"
git push
git checkout main
```
Expected: clean fast-forward-free merge, lint green, pushed.

- [ ] **Step 5: Final verification**

Run:
```bash
git status -s          # expect clean
ls -d */skills/dw-*/ | wc -l   # expect 69
bin/lint-skills.py --quiet     # expect 0 errors
```
Expected: clean tree, 69 skills in plugin layout, lint green.

---

## Self-Review notes (spec coverage)

- Spec §2.1 grouping → Task 2 map + Task 4 move (counts asserted = 69, per-plugin verified).
- Spec §2.2 layout → Task 3 manifests + Task 4 placement.
- Spec §3.1 namespacing → Task 6 Step 4 (index display) + Task 8 Step 4 (live invocation).
- Spec §3.2 file refs → Task 5 (repoint + on-disk resolution check).
- Spec §3.3 prose refs / index tables → Task 6 Step 4 + Task 7.
- Spec §4 tooling → Task 6 (lint, regen, add-category).
- Spec §5 non-dw + cruft → Task 4 Steps 3-4 + Task 8 Step 5.
- Spec §6 migration sequence → Tasks 1-9 (branch already created).
- Spec §7 risks → symlink overlap (Task 8 Step 5), git-mv integrity (Task 4 Step 2), tooling (Task 6 Step 6), lint gate (Task 7 Step 2).
- Spec §9 success criteria → Task 9 Step 5 + Task 8 Step 3-4.
