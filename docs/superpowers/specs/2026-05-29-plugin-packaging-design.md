# Design: dw-skills → 9-plugin local marketplace (Approach B, machine-local)

**Date:** 2026-05-29
**Status:** Approved design, pending implementation plan
**Scope:** Repackage the 69 `dw-*` criminal-defense skills in `~/Documents/GitHub/dw-skills` from a flat, symlink-loaded skill collection into a single **local** Claude Code marketplace exposing **8 functional plugins + `dw-core`**. Machine-local only — not git-publishable as-is.

---

## 1. Background & motivation

The `dw-skills` repo currently holds 69 `dw-*` skills in a flat `skills/dw-*/` tree, surfaced to Claude Code via the symlink `~/.claude/skills → ~/Documents/GitHub/dw-skills/skills`. A prior 70-skill audit proposed an "8-plugin + `dw-core`" architecture (recorded in memory `dw-skills-maintenance-state` as the big remaining structural move; the plugin-boundary analysis lives in `docs/skill-dependency-graph.md`). This spec executes that packaging.

**Why machine-local (Approach B):** The collection is tightly coupled — every skill loads `dw-shared-protocols` (Step 0.5), and the `dw-criminal-defense` orchestrator routes to specialists. Claude Code isolates **git/versioned** plugins in a copied cache (where cross-plugin `../` paths break), but references **local `source` path** plugins **in place** (verified: the user's `iron-gavel` plugin `installPath` is its repo dir). Keeping the marketplace local lets `dw-core` remain the single source of truth with no file duplication — preserving the single-source discipline established in recent maintenance work. The trade-off (accepted): the marketplace is not installable from git without migrating to a self-contained, duplicated-core model (Approach A).

---

## 2. Target architecture

### 2.1 Plugin grouping (approved)

`dw-core` is the shared foundation every other plugin depends on. The 8 functional plugins are derived from the existing `category:` frontmatter buckets, with two small categories merged to land on 8.

| Plugin | # | Skills |
|---|---|---|
| **dw-core** | 6 | dw-case-brain, dw-case-dashboard, dw-criminal-defense, dw-data-contracts, dw-shared-protocols, dw-skill-index |
| **dw-intake-discovery** | 4 | dw-client-intake-interview *(merged from `intake`)*, dw-brady-giglio-auditor, dw-discovery-compliance-monitor, dw-discovery-orchestrator |
| **dw-evidence-audit** | 16 | dw-cell-site-geolocation-auditor, dw-chain-of-custody-auditor, dw-child-forensic-interview-auditor, dw-confession-interrogation-auditor, dw-crime-lab-auditor, dw-crime-scene-auditor, dw-dna-forensic-biology-auditor, dw-expert-witness-evaluator, dw-eyewitness-identification-auditor, dw-forensic-dump-analyzer, dw-jail-call-analyzer, dw-mobile-forensic-auditor, dw-social-media-auditor, dw-sqlite-recovery, dw-video-evidence-auditor, dw-witness-statement-analyzer |
| **dw-offense-specialists** | 5 | dw-drug-offense-specialist, dw-dwi-specialist, dw-firearms-specialist, dw-sex-offense-specialist, dw-violent-crime-specialist |
| **dw-pleadings** | 4 | dw-404b-opposition, dw-bond-and-release-motion, dw-pretrial-motion-library, dw-suppression-motion |
| **dw-trial-prep** | 18 | dw-adversarial-stress-test, dw-appellate-error-monitor, dw-cross-exam-architect, dw-defense-investigator-tasking, dw-direct-exam-architect, dw-exhibit-manager, dw-issue-code-tracker, dw-jury-focus-group, dw-jury-instructions-builder, dw-theory-to-workplan, dw-timeline-builder, dw-trial-day-assistant, dw-trial-narrative-builder, dw-trial-notebook-builder, dw-voir-dire-assistant, dw-witness-threat-matrix, dw-neutral-inventory *(merged from `analysis`)*, dw-theory-deconstructor *(merged from `analysis`)* |
| **dw-transcription** | 4 | dw-dmar-synthesizer, dw-transcript-pipeline-calcasieu, dw-transcript-pipeline-rev, dw-transcript-router |
| **dw-disposition** | 6 | dw-appellate-brief-builder, dw-case-disposition, dw-habitual-offender-auditor, dw-plea-negotiation-analyzer, dw-post-conviction-relief, dw-sentencing-mitigation-specialist |
| **dw-ops** | 6 | dw-billing-narrative-generator, dw-case-law-researcher, dw-client-communication-drafter, dw-court-jail-tracker, dw-evidence-placeholder, dw-image-filename-stamp |

**Total: 69 skills across 9 plugin directories** (6+4+16+5+4+18+4+6+6 = 69).

### 2.2 Repo layout (after)

```
dw-skills/
  .claude-plugin/marketplace.json          # NEW — name: "dw-criminal-defense", 9 plugins, local source paths
  dw-core/
    .claude-plugin/plugin.json             # NEW
    skills/dw-case-brain/ … dw-skill-index/ (6)
  dw-intake-discovery/ .claude-plugin/plugin.json  skills/… (4)
  dw-evidence-audit/   .claude-plugin/plugin.json  skills/… (16)
  dw-offense-specialists/ …/skills/… (5)
  dw-pleadings/        …/skills/… (4)
  dw-trial-prep/       …/skills/… (18)
  dw-transcription/    …/skills/… (4)
  dw-disposition/      …/skills/… (6)
  dw-ops/              …/skills/… (6)
  skills/                                   # RETAINED — 6 non-dw skills only (see §5)
  bin/  docs/  CLAUDE.md  README.md
```

Each `plugin.json` carries `name`, `version` (`1.0.0`), `description`, `author` (Chris Washington / cjw@danielswashington.com). The default `skills/` directory is auto-discovered (per the `case-orchestrator@legal-workflow` precedent, an explicit `"skills"` field is optional); we set it explicitly for clarity, matching the `iron-gavel` plugin.

---

## 3. Invocation & reference changes

### 3.1 Namespaced invocation (behavioral change)
Plugin skills are **always** namespaced `plugin:skill`. Every `dw-*` skill's invocation changes:

| Before | After |
|---|---|
| `/dw-suppression-motion` | `/dw-pleadings:dw-suppression-motion` |
| `/dw-case-brain` | `/dw-core:dw-case-brain` |
| `/dw-criminal-defense` | `/dw-core:dw-criminal-defense` |

Bare `/dw-*` no longer resolves. The orchestrator's runtime routing to specialists still works: all enabled plugin skills appear in one available-skills list, so cross-plugin invocation is possible (confirmed by `gsd:`, `superpowers:`, and `dw-*` coexisting today).

### 3.2 File-path references (must be repointed)
There are **8** relative file-path references, all to `dw-shared-protocols/references/template-selection-protocol.md` (one also to `dw-shared-protocols/SKILL.md`), spread across 6 skills. After the move, the depth from a skill body to the shared file changes. Each must be recomputed **per file location**:

- A reference inside `<plugin>/skills/<skill>/SKILL.md` → `../../../dw-core/skills/dw-shared-protocols/references/template-selection-protocol.md` (3 × `../`).
- A reference inside a deeper `<plugin>/skills/<skill>/references/<file>.md` → 4 × `../`.

These resolve on disk because the local marketplace is referenced in place. **No duplication of `dw-core` content.**

### 3.3 Cross-skill *name* references (prose)
Bare-name mentions in skill bodies (e.g. "ALWAYS invoke `dw-suppression-motion`", orchestrator phase routing) are left as bare names — the model maps them to the namespaced invocable via the available-skills list. Exception: `dw-skill-index`'s **visible routing tables** are updated to display namespaced names so the index stays accurate. `skill-index-categories.yml` already encodes the buckets and is the source for those tables.

---

## 4. `bin/` tooling updates

The maintenance scripts assume a flat `skills/dw-*` glob and break after the move. Required updates:

- `bin/lint-skills.py` — scan `*/skills/dw-*/SKILL.md` (plugin dirs) instead of `skills/dw-*`; keep E4 cross-reference resolution working against the new layout.
- `bin/regen-skill-index.py` + `bin/skill-index-categories.yml` — generate routing tables (and, optionally, the per-plugin manifests) from the bucket definitions; emit namespaced skill names.
- `bin/add-category-frontmatter.py` — update path glob (category frontmatter is retained; harmless and still drives index tables).
- `bin/auto-pull.sh`, `bin/dw-skill-git.sh`, `bin/install-agent.sh` — audit for hardcoded `skills/dw-*` paths; update as needed.

`category:` frontmatter is **kept** on every skill (redundant with plugin grouping but harmless, and still feeds the index routing tables).

---

## 5. Non-dw skills & cleanup (approved)

- The 6 git-tracked non-dw skills (`file-organizer`, `frontend-design`, `medical-chronology`, `notebooklm`, `ui-ux-pro-max`, `youtube-transcript`) **stay in `skills/`**. The `~/.claude/skills → skills/` symlink is **retained**, so they keep loading unchanged. Mixed-mode (symlinked personal skills + local marketplace plugins) is fine.
- The 4 empty `iron-gavel-*` cruft dirs in `skills/` are deleted (the real Iron Gavel skills live in the separate `iron-gavel-skills` repo).

---

## 6. Migration sequence (executed in the implementation-plan phase, not here)

1. Create branch `plugin-packaging` from clean `main`.
2. Create 9 plugin dirs + `.claude-plugin/plugin.json` each + root `.claude-plugin/marketplace.json`.
3. `git mv` each `skills/dw-*` into its plugin's `skills/` (preserves history). Leave the 6 non-dw skills in `skills/`; delete the 4 iron-gavel cruft dirs.
4. Recompute and fix the 8 file-path references (§3.2), per-file depth.
5. Update `bin/` tooling (§4); regenerate `dw-skill-index` tables with namespaced names.
6. Run `bin/lint-skills.py` → must be 0 errors (E4 cross-refs resolve).
7. Register the local marketplace and enable all 9 plugins.
8. Smoke test: invoke one skill per plugin via its namespace + one orchestrator→specialist routing path; confirm `dw-shared-protocols` loads from a skill in a *different* plugin.
9. Update `CLAUDE.md`, `README.md`, and memory `dw-skills-maintenance-state` (mark plugin packaging done; note namespaced invocation).
10. Merge to `main`, push.

---

## 7. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Symlink + marketplace both surface the same skill → duplicate/conflicting | dw-* skills are physically **moved out** of `skills/`; symlink only sees the 6 non-dw + nothing dw. No overlap. |
| Marketplace not portable (git install breaks `../` shared-file refs) | Accepted & documented. Revisiting requires Approach A (duplicate `dw-core`). Recorded in this spec + memory. |
| Orchestrator bare-name routing degrades after namespacing | Runtime cross-plugin invocation verified to work; index tables updated to namespaced names; smoke test covers a routing path. |
| `git mv` of 69 dirs loses history or mis-sorts a skill | Move scripted from the §2.1 table; lint + a count check (69 skills, 9 dirs) before commit. |
| `bin/` scripts silently keep old paths | Each script updated and re-run; lint must pass against new layout. |

---

## 8. Out of scope

- Approach A (self-contained, git-publishable, duplicated `dw-core`).
- Relocating the 6 non-dw skills out of the repo.
- DMAR schema reconciliation, Westlaw statute-version verification, and the paused bloat-trims (separate open items in `dw-skills-maintenance-state`).
- Any change to skill *content/logic* beyond reference-path and index-table edits.

---

## 9. Success criteria

- 9 plugin dirs, 69 dw-* skills correctly placed per §2.1; `skills/` holds only the 6 non-dw skills.
- `bin/lint-skills.py` reports 0 errors against the new layout.
- All 9 plugins install from the local marketplace and every dw-* skill is invocable as `plugin:skill`.
- A skill in one plugin successfully loads `dw-shared-protocols` content from `dw-core`.
- `dw-criminal-defense` orchestrator routes to at least one specialist in another plugin in a live smoke test.
- Repo back to clean working tree on a merged `main`; memory updated.
