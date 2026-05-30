# Daniels & Washington — Criminal Defense Claude Skills

This repository is the canonical source of truth for the Daniels & Washington (D&W) Louisiana criminal defense skill collection used by Claude Cowork. Every skill in `skills/dw-*/` follows a standardized pattern; the pattern is enforced by the linter at `bin/lint-skills.py`.

When working in this repo, follow the conventions below. They exist because they have been established across ~60 skills and ~150 reference files; deviations create maintenance burden and lawyer-facing inconsistency.

> **Plugin layout (as of May 2026):** Skills now live in 9 plugins — `dw-core` (foundation) plus 8 functional plugins (`dw-intake-discovery`, `dw-evidence-audit`, `dw-offense-specialists`, `dw-pleadings`, `dw-trial-prep`, `dw-transcription`, `dw-disposition`, `dw-ops`) — installed as a machine-local marketplace named `dw-criminal-defense`. Invoke skills namespaced: `/dw-pleadings:dw-suppression-motion-crim`, `/dw-core:dw-case-brain-crim`, etc. Cross-skill references in prose still use bare `dw-*` names; the model resolves them via the available-skills list.

---

## Repository layout

```
.
├── CLAUDE.md                    ← You are here
├── README.md
├── .claude/
│   └── settings.json            ← Project-level Claude settings (Stop hook for the linter)
├── bin/
│   ├── lint-skills.py           ← Skill-pattern linter (run before every commit)
│   ├── dw-skill-git.sh          ← Daily git sync between repo, ~/.claude/skills, and Cowork
│   ├── auto-pull.sh             ← Background auto-pull
│   └── install-agent.sh         ← LaunchAgent installer for auto-pull
├── docs/
│   ├── DW_Criminal_Defense_Cowork Project_Instructions_1.md
│   ├── DW_Skills_Operations_Guide_v1.2.docx
│   └── Updated_Skill_Map_March_2026.docx     ← Canonical skill map (refresh on net additions/removals)
└── skills/
    ├── dw-criminal-defense-crim/     ← Master 3-phase orchestrator (the entry point)
    ├── dw-skill-index-crim/          ← Lookup table for all skills (the routing manual)
    ├── dw-shared-protocols-crim/     ← Library of shared references other skills load (work-product marking, output-path formula, captions, DEVONthink template-selection-protocol, etc.)
    ├── dw-data-contracts-crim/       ← Cross-skill input/output schemas
    └── dw-*/                    ← All other D&W skills follow the standard pattern
```

The `skills/` directory is the canonical install point — Claude Code reads from here. The duplicate top-level `dw-trial-notebook-builder-crim/` directory is a known stale artifact from an older upload pipeline; treat `skills/dw-trial-notebook-builder-crim/` as authoritative.

---

## Onboarding — first-time setup

Use this section if you are new to the D&W skill collection (joining the firm, setting up a new machine, or onboarding a new attorney).

### 1. Clone the repository

```
git clone <repo-url> ~/Documents/GitHub/dw-skills
cd ~/Documents/GitHub/dw-skills
```

The actual remote URL is internal to D&W — see your team lead or the firm operations document.

### 2. Link skills into Claude Code's skill directory

Claude Code (CLI, Web, IDE) reads skills from `~/.claude/skills/`. The `bin/dw-skill-git.sh` script keeps the repo's `skills/` and `~/.claude/skills/` in sync:

```
bin/dw-skill-git.sh status        # show sync state
bin/dw-skill-git.sh sync          # one-shot sync
```

### 3. (Optional) Install the auto-pull background agent

Keeps the local repo current with `origin/main` automatically (macOS only — installs a LaunchAgent):

```
bin/install-agent.sh
```

Confirm it's running: `launchctl list | grep com.dw.skill-git-pull`. To uninstall: `bin/uninstall-agent.sh`.

### 4. Verify the linter and hooks

```
bin/lint-skills.py              # should report 0 errors, 0 warnings
jq -e '.hooks.Stop[0].hooks[0].command' .claude/settings.json   # should print the linter command and exit 0
```

The Stop hook will block your session from ending if the linter finds errors. The SessionStart hook prints a one-line linter banner each session start. See the **Hooks** section below for details.

### 5. Open a Claude Code session in this repo

The session-start banner will confirm the linter is healthy. Try a discoverability test:

```
> what skills do we have for evidence audits?
```

Claude should consult `dw-skill-index-crim` and return the Evidence Auditing routing table. If it doesn't, the skill collection isn't loaded — re-run `bin/dw-skill-git.sh sync`.

### 6. Cowork project setup (Claude on the web)

For the Claude Cowork project (firm-wide criminal-defense workspace), the project instructions are maintained at `docs/DW_Criminal_Defense_Cowork Project_Instructions_1.md`. Paste the contents into the Cowork project's instructions field. Update both this repo and the Cowork project when project instructions change.

### 7. First skill to invoke (typical attorney workflow)

| Situation | Say this | Skill that fires |
|---|---|---|
| New client, first meeting | "intake" or "new client meeting" | `dw-client-intake-interview-crim` |
| New case, file processing | "new case" or "case intake" | `dw-criminal-defense-crim` (Phase 1) |
| Returning to existing case | "load the case" | `dw-case-brain-crim` |
| Mid-trial, in court | "log this objection" | `dw-trial-day-assistant-crim` |
| After verdict, prepping appeal | "preserve error" then later "appellate brief" | `dw-appellate-error-monitor-crim` → `dw-appellate-brief-builder-crim` |

For the full routing table, ask: *"what skills do we have"* (invokes `dw-skill-index-crim`).

### 8. Common troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Stop hook fires, session won't end | Linter found errors | Run `bin/lint-skills.py --errors-only` to see what's broken; fix and retry stop |
| SessionStart banner missing | `.claude/settings.json` wasn't present at session start | Run `/hooks` in Claude Code to reload, or restart the session |
| Skill not invoked when expected | Trigger keywords don't match user's wording | Check `dw-skill-index-crim` for the canonical trigger phrase; rephrase, or update the skill's frontmatter description |
| `bin/lint-skills.py` reports E4 (broken cross-skill ref) | Skill mentions a `dw-foo` that doesn't exist | Either fix the reference or, if intentional historical mention, add a "former" / "merged into" / "deprecated" marker on the same line so the linter recognizes it as historical |
| `bin/regen-skill-index.py --check` exits 1 | Index is stale | Run `bin/regen-skill-index.py` to apply, then commit `skills/dw-skill-index-crim/SKILL.md` |

---

## House rules — non-negotiable

These rules apply to every skill, every reference file, every commit. The linter catches structural violations; the substantive ones depend on you.

### 1. No fabricated citations — ever

Every Louisiana statute, code article, and case citation in skill files must be one you can verify. If you cannot verify it, mark it `[VERIFY CITATION]` so the attorney knows to confirm before relying on it. This applies to:

- Louisiana Code of Criminal Procedure articles (La. C.Cr.P. Art. ___)
- Louisiana Code of Evidence articles (La. C.E. Art. ___)
- Louisiana Revised Statutes (La. R.S. ___:___)
- Louisiana Children's Code articles (La. Ch.C. Art. ___)
- All case citations (state and federal)
- Louisiana Rules of Professional Conduct

**Anchor authorities** that are well-established may be cited without a flag: *Miranda*, *Daubert*, *Foret*, *Brady*, *Giglio*, *Strickland*, *Jackson v. Virginia*, *Chapman*, *Captville*, *Crawford*, *Batson*, *Miller v. Alabama*, *Montgomery v. Louisiana*, *Padilla v. Kentucky*. If in doubt, flag.

When you build new skills or reference files, sub-agents should be given this rule in their prompt (the agents have demonstrated they follow it).

### 2. The Source Citation Mandate is mandatory

Every analytical skill includes a Source Citation Mandate section near the top of its body. Every factual assertion in a skill's outputs must trace to a specific source document — discovery file, transcript page/line, BWC timestamp, lab report, etc. Format examples are in each skill's mandate section.

Unsourced claims must be marked `[UNSOURCED — VERIFY]` so the attorney knows to confirm or remove them before relying on the deliverable.

### 3. Output paths anchor on `{{CASE_ROOT}}`

All deliverable file paths follow the formula in `dw-shared-protocols-crim/references/output-path-formula.md`. The convention root for analytical outputs:

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

with sub-folders for specific phases. Two known special-case anchors:

- `{{FIRM_MARKETING_ROOT}}` — used by PI marketing skills (now in the sibling `DW-PI-Marketing-Claude-Skills` repo) for marketing-folder outputs; case-derived facts still cite `{{CASE_ROOT}}` if those skills consume case data
- `~/.dw-tracker/` — local tracker artifacts (`dw-court-jail-tracker-crim`)

### 4. Every deliverable carries attorney work-product marking

Per `dw-shared-protocols-crim/references/attorney-work-product-marking.md`. Every analytical or motion deliverable header includes the marking. The shared-protocols load step is Step 0.5 in every standard skill.

### 5. Don't modify shared infrastructure casually

The following skills are infrastructure that downstream skills depend on. Changes ripple. Discuss before touching:

- `dw-shared-protocols-crim/` — the protocol library; many skills load from here (includes the DEVONthink template-selection-protocol, formerly the standalone `dw-template-selector`)
- `dw-data-contracts-crim/` — cross-skill schemas
- `dw-skill-index-crim/` — lookup; needs updating only when adding/retiring skills (use the linter to verify references resolve)
- `dw-criminal-defense-crim/` — the master orchestrator (currently v5.4); changes here affect Cowork's workflow

### 6. Cowork drafts; attorney approves

Every output is a draft for attorney review. Skills must never represent themselves to the attorney as final or filed; the attorney verifies facts, confirms legal arguments, signs, and files. This is an inviolable rule of D&W's Cowork practice.

---

## The Standard Skill Pattern

Every `skills/dw-*/SKILL.md` follows this structure. The linter (`bin/lint-skills.py`) checks for these sections; skills that legitimately diverge are exempted in the linter's `EXEMPT` table at the top of the script.

```
---
name: dw-<skill-name>             ← Must match the directory name
description: >
  ALWAYS invoke for "<trigger 1>," "<trigger 2>," ...
  Do NOT use for <X> — use <other-skill>.
---

# Skill Name
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

[1-2 paragraph skill purpose statement]

## STEP 0 — FILE INTAKE HARD STOP (Always First)
[Hard-stop language that prevents premature analysis when uploads are in flight]

## STEP 0.5 — LOAD SHARED PROTOCOLS
[Reads dw-shared-protocols-crim/SKILL.md + work-product marking + output-path formula]

### Source Citation Mandate
[Every factual assertion traces to a source; format and unsourced rules]

## STEP 1 — Information Gathering Protocol
[Essential / Strategic / Contextual ranked checklist]

## STEP 2 / 3 / ... — Analytical Modules (lettered: MODULE A, MODULE B, ...)
[The substantive work; references to references/<file>.md as needed]

## STEP N — Output Format
[What the deliverable looks like, where it saves, how it integrates with downstream skills]

## Guardrails
[Skill-specific safety rules]

## Quick References
[List of files in references/ subdirectory with brief descriptions]
```

References for a skill live in `skills/dw-<name>/references/`. Each reference is a focused topic document; the SKILL.md points to it via `Read \`references/<file>.md\``.

### Skills exempted from parts of the standard pattern

These skills legitimately diverge — see `EXEMPT` table in `bin/lint-skills.py` for the full list:

- `dw-skill-index-crim` — lookup/index only, no file output
- `dw-shared-protocols-crim` — by design a library other skills load files from (includes the template-selection-protocol)
- `dw-data-contracts-crim` — schema definitions
- `dw-criminal-defense-crim` — master orchestrator; downstream skills enforce hard stops + citations
- `dw-case-brain-crim` — session persistence to internal `brain.md`, no attorney deliverables
- `dw-evidence-placeholder-crim`, `dw-image-filename-stamp-crim` — utility skills

---

## Cross-skill integration patterns

Several skills feed each other in well-defined chains. Preserve these contracts.

| Producer | Consumer | What flows |
|---|---|---|
| `dw-trial-day-assistant-crim` Module B (objection log) | `dw-appellate-error-monitor-crim` Modules A/B | Objection log schema is field-for-field aligned (additive `Day`/`Time` fields only) |
| `dw-trial-day-assistant-crim` Module C (witness scorecard) | `dw-cross-exam-architect-crim` | Per-witness scorecard rolls into next-day cross prep |
| `dw-appellate-error-monitor-crim` ranked-issue output (Module H) | `dw-appellate-brief-builder-crim` Step 1 | Ranked appellate issues feed brief drafting; routes back if missing |
| `dw-jail-call-analyzer-crim` tampering risk findings | `dw-witness-threat-matrix-crim` (Refresh Mode) | Cross-feed for witness-contact monitoring |
| `dw-client-intake-interview-crim` charge-type dispatcher | All five charge-type specialists | Charge identification routes to the right specialist (drug, DWI, sex, firearms, violent) |
| `dw-criminal-defense-crim` Phase 2 Step 1C | All evidence auditors | Evidence-type routing |
| `dw-criminal-defense-crim` Phase 2 Step 1D | All charge-type specialists | Charge-type routing |
| `dw-criminal-defense-crim` Phase 3 Step 11 | `dw-trial-day-assistant-crim` | Trial-day live support routing |
| `dw-confession-interrogation-auditor-crim` Step 4 | `dw-suppression-motion-crim` | Audit findings → Art. 703 motion |

When you change an upstream skill's output, check the consumer skills for breakage.

---

## Commands

| Task | Command |
|---|---|
| Lint all D&W skills (errors only) | `bin/lint-skills.py --errors-only` |
| Lint with warnings | `bin/lint-skills.py` |
| Lint a single skill | `bin/lint-skills.py --skill dw-foo` |
| Lint with warnings as errors | `bin/lint-skills.py --strict` |
| Lint including 3rd-party utility skills | `bin/lint-skills.py --all` |
| Sync skills to ~/.claude/skills | `bin/dw-skill-git.sh sync` |
| Check sync status | `bin/dw-skill-git.sh status` |
| Background auto-pull | `bin/auto-pull.sh` |
| Regenerate `dw-skill-index-crim/SKILL.md` from frontmatter | `bin/regen-skill-index.py` |
| Check whether the skill index is up to date | `bin/regen-skill-index.py --check` |
| Add `category:` frontmatter to all skills | `bin/add-category-frontmatter.py` |
| Package each skill as a `.skill` zip for Cowork import | `bin/dw-skill-git.sh export-cowork` |

### Cowork export packaging

`bin/dw-skill-git.sh export-cowork` packages each `skills/dw-*/` directory into a single `.skill` zip and writes them to `_cowork-exports/` (gitignored — generated artifact, not version-controlled). The packaging is incremental: only skills whose contents are newer than their existing `.skill` file are re-zipped.

The `.skill` files are consumed by the Cowork project on Claude.ai when uploading skills via the project's settings UI. Workflow:

1. Run `bin/dw-skill-git.sh export-cowork` after committing skill changes
2. Open the Cowork project on Claude.ai → Settings → Skills
3. Upload the affected `.skill` files

The directory `_cowork-exports/` is gitignored (see `.gitignore`); never commit `.skill` files.

---

## Hooks

Project-level Claude Code hooks live in `.claude/settings.json`. They activate automatically when a Claude Code session starts in this repo.

| Event | What it does | Blocks? |
|---|---|---|
| **SessionStart** | Runs `bin/lint-skills.py` and shows a one-line linter summary banner ("D&W Skill Linter: 62 skill(s) checked — 0 error(s), 0 warning(s).") so issues surface at session start, not at session end. | No — informational only |
| **Stop** | Runs `bin/lint-skills.py --errors-only`. If errors are present, blocks the Stop event with a `{"decision": "block", "reason": ...}` JSON payload — the model must fix the errors before the session can stop. Warnings do not block. | Yes — on errors only |

To temporarily disable the hooks: rename `.claude/settings.json` to `.claude/settings.json.disabled` (don't commit the rename). To remove permanently: delete the relevant `"Stop"` or `"SessionStart"` block from the `"hooks"` object.

### Testing hooks locally

The hooks fire automatically when Claude Code starts a session in this repo (or when triggered by Stop). To verify they work without a full session round-trip, pipe-test the commands directly:

**Validate hook JSON shape:**
```
jq -e '.hooks.Stop[0].hooks[0].command' .claude/settings.json
jq -e '.hooks.SessionStart[0].hooks[0].command' .claude/settings.json
```
Each should print the command string and exit 0. Invalid JSON in `.claude/settings.json` silently disables ALL settings from that file — fix any pre-existing malformation if `jq -e` exits non-zero.

**Pipe-test the SessionStart hook (clean path, expected behavior):**
```
echo '{"session_id":"test"}' | bash -c 'summary=$(bin/lint-skills.py 2>&1 | tail -1); jq -nc --arg s "$summary" "{systemMessage: (\"D&W Skill Linter: \" + \$s)}"'
```
Expected output: a single JSON line like `{"systemMessage":"D&W Skill Linter: 62 skill(s) checked — 0 error(s), 0 warning(s)."}`.

**Pipe-test the Stop hook (clean path):**
```
echo '{"session_id":"test"}' | bash -c 'output=$(bin/lint-skills.py --errors-only 2>&1) || jq -nc --arg out "$output" "{decision: \"block\", reason: (\"Skill-pattern linter found errors. Fix before stopping:\\n\\n\" + \$out)}"'
```
Expected output (clean): silent (no output, exit 0). The hook only emits JSON when there are errors.

**Pipe-test the Stop hook (error path):**
1. Introduce a temporary error: `echo "broken-ref to references/totally-missing-file.md" >> skills/dw-jail-call-analyzer-crim/SKILL.md`
2. Run the same pipe-test command above
3. Expected output: a JSON line `{"decision":"block","reason":"Skill-pattern linter found errors. Fix before stopping:\n\n\n=== dw-jail-call-analyzer-crim ...\n  ERROR E3: Referenced file does not exist on disk — references/totally-missing-file.md\n\n62 skill(s) checked — 1 error(s), 0 warning(s)."}`
4. Revert: `git checkout skills/dw-jail-call-analyzer-crim/SKILL.md`

**Common gotcha — settings watcher:** Claude Code's settings watcher only watches directories that had a `.claude/settings.json` at session start. If you ADD `.claude/settings.json` mid-session, the hooks won't fire in that session. Run `/hooks` to reload, or restart the session.

---

## Working in this repo with sub-agents

When you spawn sub-agents (general-purpose, Plan, Explore) to build or modify skills:

1. **Brief them on the standard pattern** — point them at `dw-suppression-motion-crim`, `dw-violent-crime-specialist-crim`, or `dw-expert-witness-evaluator-crim` as model skills to mirror.
2. **Tell them not to commit or push** — sub-agents working on the same branch can race. Have them create files; the parent does the consolidated commit.
3. **Tell them to NOT modify infrastructure skills** unless the task explicitly requires it.
4. **Tell them to flag uncertain citations** with `[VERIFY CITATION]`.
5. **Tell them to run the linter** on their work before reporting back.
6. **Match their depth to existing skills** — agents will either underbuild (thin SKILL.md) or overbuild (verbose where existing skills are tight); the model-skills pointer keeps them calibrated.

---

## Branch and commit conventions

- Develop on feature branches; the user typically specifies the branch name when spawning a session
- Commit style: descriptive subject line, body explains the *why*, multi-section bodies for cross-skill changes
- Use HEREDOC for commit messages (preserves formatting)
- Prefer many small commits in feature work; one consolidated commit at the end of a multi-skill build pass
- Do NOT push to a branch other than the one specified at session start without explicit permission

---

## When pushing changes

The Stop hook will block stopping if linter errors are present. When you push:

1. `git status -sb` and `git diff --stat` first
2. Stage specific files (not `git add .`) when feasible
3. Commit with HEREDOC + descriptive body
4. `git push -u origin <branch>` (the branch is specified per session)
5. Confirm push succeeded
6. Do NOT create a pull request unless the user explicitly asks

---

## Known follow-up items (not blocking, worth knowing)

- White-collar and juvenile charge types surfaced from `dw-client-intake-interview-crim`'s question banks as future specialist-skill candidates (Tier-2).
- Consider building `bin/regen-skill-index.py` to auto-generate `dw-skill-index-crim/SKILL.md` from a scan of `skills/dw-*/SKILL.md` frontmatter, eliminating the hand-wired routing tables.
- Three Louisiana errors-patent appellate citations from the original brief-builder build (`State v. Price`, `State v. Haynes`, `State v. Shannon`) could not be located in publicly available case databases. They have been replaced with the canonical errors-patent authorities (`State v. Oliveaux`, 312 So.2d 337 (La. 1975) + La. C.Cr.P. Art. 920(2)) — but if the original Price/Haynes/Shannon citations turn out to be real and useful, the attorney can add them back via Westlaw lookup.
- "Mere words insufficient to constitute aggression" doctrine in `dw-violent-crime-specialist-crim` is described without case attribution; the attorney should add the controlling Louisiana case before filing any deliverable that relies on it.

## Citation verification pass (May 2026)

A May 2026 verification pass resolved every substantive `[VERIFY CITATION]` flag across the new May 2026 skills. The remaining `[VERIFY CITATION]` markers in the skill files are explanatory/instructional — they document the marker for future agents, rather than flagging unverified citations.

Verified Louisiana cases now used unflagged across the collection:

| Case | Citation | Used For |
|---|---|---|
| *State v. Hunt* | 2009-1589 (La. 12/1/09), 25 So.3d 746, 751 | De novo / deferential review on motion to suppress (legal vs. factual) |
| *State v. Magee* | 2011-0574 (La. 9/28/12), 103 So.3d 285 | Abuse of discretion across evidentiary rulings (death-penalty case, 17 assignments) |
| *State v. Mosby* | 595 So.2d 1135, 1138-39 (La. 1992) | Primary anchor for evidentiary-ruling abuse-of-discretion review |
| *State v. Mussall* | 523 So.2d 1305, 1310 (La. 1988) | Jackson methodology applied to all essential elements |
| *State v. Cook* | 95-2784 (La. 5/31/96), 674 So.2d 957, 958 | Sentencing within statutory range — abuse of discretion |
| *State v. Johnson* | 94-1379 (La. 11/27/95), 664 So.2d 94, 102 | Harmless error (paired with *Sullivan v. Louisiana* "surely unattributable") |
| *State v. Johnson* | 97-1906 (La. 3/4/98), 709 So.2d 672, 676 | Narrowing *Dorthey* — mandatory minimums presumed constitutional |
| *State v. Williams* | 2000-1725 (La. 11/28/01), 800 So.2d 790, 798-99 | La. R.S. 15:301.1 self-activation framework |
| *Stobart v. State Through DOTD* | 617 So.2d 880, 882-83 (La. 1993) | Manifest-error / clearly-wrong (civil case applied criminally) |
| *State v. Oliveaux* | 312 So.2d 337 (La. 1975) | Errors-patent doctrine (with La. C.Cr.P. Art. 920(2)) |
| *State v. Taylor* | 2001-1638 (La. 1/14/03), 838 So.2d 729, 741 | 404(B) abuse-of-discretion |
| *State v. Strickland* | 94-0025 (La. 11/1/96), 683 So.2d 218, 229 | Continuance abuse of discretion |
| *State v. Brooks* | 541 So.2d 801 (La. 1989) | Severance abuse of discretion |
| *State v. Williams* | 601 So.2d 1374, 1375 (La. 1992) | Recusal abuse of discretion |
| *State v. Marse* | 365 So.2d 1319, 1323-24 (La. 1978) | Refusal to give requested jury charge |
| *State v. Manning* | 2003-1982 (La. 10/19/04), 885 So.2d 1044, 1077 | Mistrial denial abuse of discretion |
| *State v. Hatton* | 2007-2377 (La. 7/1/08), 985 So.2d 709, 718-19 | Motion to quash bill of information de novo |
| *State v. Tompkins* | 403 So.2d 644 (La. 1981) | Sudden-passion / heat-of-blood mitigation framework |
| *State v. Anthony* | 427 So.2d 1155 (La. 1983) | Felony-murder "in the perpetration" termination |
| *State v. Kalathakis* | 563 So.2d 228 (La. 1990) | Felony-murder termination (companion to Anthony) |
| *State v. Smith* | 327 So.2d 355 (La. 1976) | Inflammatory-photograph admissibility |
| *State v. Manieri* | 378 So.2d 931 (La. 1979) | Inflammatory-photograph admissibility (companion) |
| *State v. Lee* | 331 So.2d 455 (La. 1976) | Victim-character admissibility under La. C.E. Art. 404(A)(2)(a) |
| *State v. Shelton* | 621 So.2d 769 (La. 1993) | Three-part burden-shifting framework for challenging predicate guilty plea (habitual offender) |

Sources verified via Justia, FindLaw, vLex, CourtListener, Casetext, Google Scholar, Louisiana Supreme Court, and Louisiana circuit websites. **Attorneys should still Westlaw-check for currency before filing** — published case databases reflect cases as decided, not subsequent treatment.
