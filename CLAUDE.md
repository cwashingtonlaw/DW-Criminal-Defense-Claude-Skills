# Daniels & Washington — Criminal Defense Claude Skills

This repository is the canonical source of truth for the Daniels & Washington (D&W) Louisiana criminal defense skill collection used by Claude Cowork. Every skill in `skills/dw-*/` follows a standardized pattern; the pattern is enforced by the linter at `bin/lint-skills.py`.

When working in this repo, follow the conventions below. They exist because they have been established across ~60 skills and ~150 reference files; deviations create maintenance burden and lawyer-facing inconsistency.

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
    ├── dw-criminal-defense/     ← Master 3-phase orchestrator (the entry point)
    ├── dw-skill-index/          ← Lookup table for all skills (the routing manual)
    ├── dw-shared-protocols/     ← Library of shared references other skills load (work-product marking, output-path formula, captions, etc.)
    ├── dw-template-selector/    ← DEVONthink template-search protocol read by motion-drafting skills
    ├── dw-data-contracts/       ← Cross-skill input/output schemas
    └── dw-*/                    ← All other D&W skills follow the standard pattern
```

The `skills/` directory is the canonical install point — Claude Code reads from here. The duplicate top-level `dw-trial-notebook-builder/` directory is a known stale artifact from an older upload pipeline; treat `skills/dw-trial-notebook-builder/` as authoritative.

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

All deliverable file paths follow the formula in `dw-shared-protocols/references/output-path-formula.md`. The convention root for analytical outputs:

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

with sub-folders for specific phases. Two known special-case anchors:

- `{{FIRM_MARKETING_ROOT}}` — used by `dw-pi-video-generator` for marketing-folder outputs (case-derived facts in the same skill still cite `{{CASE_ROOT}}`)
- `~/.dw-tracker/` — local tracker artifacts (`dw-court-jail-tracker`)

### 4. Every deliverable carries attorney work-product marking

Per `dw-shared-protocols/references/attorney-work-product-marking.md`. Every analytical or motion deliverable header includes the marking. The shared-protocols load step is Step 0.5 in every standard skill.

### 5. Don't modify shared infrastructure casually

The following skills are infrastructure that downstream skills depend on. Changes ripple. Discuss before touching:

- `dw-shared-protocols/` — the protocol library; many skills load from here
- `dw-template-selector/` — the DEVONthink template-search protocol
- `dw-data-contracts/` — cross-skill schemas
- `dw-skill-index/` — lookup; needs updating only when adding/retiring skills (use the linter to verify references resolve)
- `dw-criminal-defense/` — the master orchestrator (currently v5.4); changes here affect Cowork's workflow

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
[Reads dw-shared-protocols/SKILL.md + work-product marking + output-path formula]

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

- `dw-skill-index` — lookup/index only, no file output
- `dw-template-selector` — shared protocol, not directly user-invoked
- `dw-shared-protocols` — by design a library other skills load files from
- `dw-data-contracts` — schema definitions
- `dw-criminal-defense` — master orchestrator; downstream skills enforce hard stops + citations
- `dw-case-brain` — session persistence to internal `brain.md`, no attorney deliverables
- `dw-evidence-placeholder`, `dw-image-filename-stamp` — utility skills

---

## Cross-skill integration patterns

Several skills feed each other in well-defined chains. Preserve these contracts.

| Producer | Consumer | What flows |
|---|---|---|
| `dw-trial-day-assistant` Module B (objection log) | `dw-appellate-error-monitor` Modules A/B | Objection log schema is field-for-field aligned (additive `Day`/`Time` fields only) |
| `dw-trial-day-assistant` Module C (witness scorecard) | `dw-cross-exam-architect` | Per-witness scorecard rolls into next-day cross prep |
| `dw-appellate-error-monitor` ranked-issue output (Module H) | `dw-appellate-brief-builder` Step 1 | Ranked appellate issues feed brief drafting; routes back if missing |
| `dw-jail-call-analyzer` tampering risk findings | `dw-witness-threat-matrix` (Refresh Mode) | Cross-feed for witness-contact monitoring |
| `dw-client-intake-interview` charge-type dispatcher | All five charge-type specialists | Charge identification routes to the right specialist (drug, DWI, sex, firearms, violent) |
| `dw-criminal-defense` Phase 2 Step 1C | All evidence auditors | Evidence-type routing |
| `dw-criminal-defense` Phase 2 Step 1D | All charge-type specialists | Charge-type routing |
| `dw-criminal-defense` Phase 3 Step 11 | `dw-trial-day-assistant` | Trial-day live support routing |
| `dw-confession-interrogation-auditor` Step 4 | `dw-suppression-motion` | Audit findings → Art. 703 motion |

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
| Regenerate `dw-skill-index/SKILL.md` from frontmatter | `bin/regen-skill-index.py` |
| Check whether the skill index is up to date | `bin/regen-skill-index.py --check` |

---

## Hooks

Project-level Claude Code hooks live in `.claude/settings.json`. They activate automatically when a Claude Code session starts in this repo.

| Event | What it does | Blocks? |
|---|---|---|
| **SessionStart** | Runs `bin/lint-skills.py` and shows a one-line linter summary banner ("D&W Skill Linter: 62 skill(s) checked — 0 error(s), 0 warning(s).") so issues surface at session start, not at session end. | No — informational only |
| **Stop** | Runs `bin/lint-skills.py --errors-only`. If errors are present, blocks the Stop event with a `{"decision": "block", "reason": ...}` JSON payload — the model must fix the errors before the session can stop. Warnings do not block. | Yes — on errors only |

To temporarily disable the hooks: rename `.claude/settings.json` to `.claude/settings.json.disabled` (don't commit the rename). To remove permanently: delete the relevant `"Stop"` or `"SessionStart"` block from the `"hooks"` object.

To verify the hook config is valid: `jq -e '.hooks.Stop[0].hooks[0].command' .claude/settings.json` (should print the command and exit 0).

---

## Working in this repo with sub-agents

When you spawn sub-agents (general-purpose, Plan, Explore) to build or modify skills:

1. **Brief them on the standard pattern** — point them at `dw-suppression-motion`, `dw-violent-crime-specialist`, or `dw-expert-witness-evaluator` as model skills to mirror.
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

- White-collar and juvenile charge types surfaced from `dw-client-intake-interview`'s question banks as future specialist-skill candidates (Tier-2).
- Consider building `bin/regen-skill-index.py` to auto-generate `dw-skill-index/SKILL.md` from a scan of `skills/dw-*/SKILL.md` frontmatter, eliminating the hand-wired routing tables.
- Three Louisiana errors-patent appellate citations from the original brief-builder build (`State v. Price`, `State v. Haynes`, `State v. Shannon`) could not be located in publicly available case databases. They have been replaced with the canonical errors-patent authorities (`State v. Oliveaux`, 312 So.2d 337 (La. 1975) + La. C.Cr.P. Art. 920(2)) — but if the original Price/Haynes/Shannon citations turn out to be real and useful, the attorney can add them back via Westlaw lookup.
- "Mere words insufficient to constitute aggression" doctrine in `dw-violent-crime-specialist` is described without case attribution; the attorney should add the controlling Louisiana case before filing any deliverable that relies on it.

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
