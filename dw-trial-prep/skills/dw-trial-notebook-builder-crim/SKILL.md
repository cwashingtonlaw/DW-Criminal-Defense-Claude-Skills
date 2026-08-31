---
name: dw-trial-notebook-builder-crim
category: trial-prep
description: >
  Assemble the final trial notebook from all upstream deliverables. ALWAYS invoke for
  "build the trial notebook," "assemble trial notebook," "trial notebook," "trial binder,"
  "trial prep package," "ready for trial," "pull together the trial file," "notebook builder,"
  or "what do we have for trial." Scans the case folder and Case Brain for all Phase 2-4
  deliverables, organizes them into the Trial Notebook folder structure, generates a master
  index with file:// links, produces a Trial Readiness Gap Report showing what's missing,
  and includes attorney checklists (Day of Trial, Exhibit Authentication, Witness Schedule).
  The capstone skill that ties every other D&W skill together into a courtroom-ready package.
  Do NOT use for individual deliverables — use the dedicated skill (dw-cross-exam-architect-crim,
  dw-jury-instructions-builder-crim, etc.). Do NOT use for case status checks — use dw-case-dashboard-crim.
---

# Trial Notebook Builder
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

This skill is the capstone of the D&W criminal defense workflow. It collects every
deliverable produced by upstream skills across Phases 2, 3, and 4, verifies they exist and
are filed correctly in the Trial Notebook folder structure, identifies gaps, and produces a
**Master Trial Index** — a single document with `file://` links to every item in the
notebook — plus attorney-facing checklists for courtroom use.

The Trial Notebook Builder does not *create* the underlying deliverables. It *assembles*
them. If a cross-examination outline is missing, this skill tells you to run
`dw-cross-exam-architect-crim`. If jury instructions haven't been drafted, it points you to
`dw-jury-instructions-builder-crim`. Its job is to give the attorney a clear, organized picture of
what's ready, what's missing, and what to do about the gaps — then produce the courtroom-ready
package from everything that exists.

```
Phase 2 outputs ─┐
Phase 3 outputs ─┤── Trial Notebook Builder ──► Organized folder + Master Index + Gap Report + Checklists
Phase 4 outputs ─┘
```

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

This skill consumes **finished deliverables** (jury charges, witness materials, exhibit lists, motions, case analysis reports) — not raw discovery. Before scanning the case folder or generating any index, confirm that no further deliverables are inbound.

**If the user has uploaded or referenced any trial notebook deliverables (jury charges, witness materials, exhibit lists, motions, case analysis reports) or pretrial notebook contents, do not start the assembly yet.**

Your only response must be:

> *"Before I begin assembling the trial notebook — are you uploading any additional trial notebook deliverables (jury charges, witness materials, exhibit lists, motions, case analysis reports) or pretrial notebook contents? I'll start the scan and Master Index build only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop is especially important for this skill because the Master Index and Gap Report are point-in-time snapshots — adding deliverables mid-build produces a stale index.

Once the user confirms, proceed to Step 0.5.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before scanning the case folder or producing the Master Index, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to the Trial Readiness Gap Report, Master Trial Index, and the three attorney checklists (all internal deliverables).
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `{{CASE_ROOT}}`).

Do not proceed to Step 1 until these protocols are loaded. The Master Index, Gap Report, and Checklists are internal work product. Trial Notebook Builder writes directly into the trial notebook itself — its outputs anchor on `{{CASE_ROOT}}/01 - Trial Notebook/` (Master Index, Gap Report, and Checklists save to `{{CASE_ROOT}}/` at the case root, alongside `Case Tables.xlsx`). See the "Output Paths" section near the bottom of this skill for the full path table.

---

## Source Citation Mandate

Every "FOUND," "MISSING," or "PARTIAL" entry in the Inventory Table, every gap callout in the Gap Report, and every link in the Master Trial Index must trace back to a specific source — either a verified file path on disk or a Case Brain entry. The Master Index is the attorney's single courtroom entry point; a fabricated or stale link here is worse than no link at all.

**Citation format:**
- Inventory entries: `(Found at: {{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/[filename], modified [YYYY-MM-DD])`
- Gap entries: `(Expected at: {{CASE_ROOT}}/[expected path]; not present in folder scan or Case Brain COMPANION SKILL OUTPUTS)`
- Case Brain entries: `(Case Brain — COMPANION SKILL OUTPUTS, entry dated [YYYY-MM-DD])`
- Case Tables entries: `(Case Tables.xlsx — [Sheet name], Row [N])`

**Multiple-source rule:** When the folder scan and the Case Brain disagree (deliverable in folder but not in Brain, or vice versa), surface both in the Case Brain Sync Issues section of the Gap Report — never silently pick one.

**Unsourced assertions:** If a "FOUND" status cannot be tied to an actually-readable file on disk, mark it `[UNSOURCED — VERIFY]` and downgrade to PARTIAL/MISSING for the Gap Report. Verify every `file://` link target exists before adding it to the Master Index — a dead link is worse than a flagged gap.

**Where sourcing applies:** All inventory rows, all Gap Report entries, all Master Index links, and any "Cross Prepared?" or "Status" entry in the Witness Schedule and Exhibit Authentication checklists. Boilerplate checklist items (e.g., "Arrive early") do not require citation.

---

## STEP 0.6 — LOAD CASE CONTEXT

The Trial Notebook Builder requires case context to function. It needs to know where the
case folder is and what the case brain says about deliverables already produced.

**0A** identify the case folder (mounted in the workspace or named by the attorney; ask if neither) · **0B** load the Case Brain (client, docket, phase, charges, lead attorney, trial date, `COMPANION SKILL OUTPUTS`, `gdrive_path`, theory; if no Brain, warn and fall back to a folder-only scan) · **0C** confirm scope with the attorney.

Read `references/case-context-load.md` now for the exact prompts and extraction list. Proceed after confirmation.

---

## STEP 1 — SCAN & INVENTORY

Systematically scan the case folder to find every deliverable. The scan covers both the
Trial Notebook and Pretrial Notebook because some deliverables (motions, discovery analysis)
live in the Pretrial Notebook but feed into trial preparation.

**1A** Trial Notebook folder scan (9-tab structure; adapt to naming variations, flag non-standard organization) · **1B** Pretrial Notebook scan · **1C** `Case Tables.xlsx` sheet audit · **1D** cross-reference against Case Brain `COMPANION SKILL OUTPUTS` (flag mismatches both directions) · **1E** Inventory Table (FOUND / MISSING / PARTIAL).

Read `references/scan-and-inventory.md` now for the scan tables, status checks, and Inventory Table format; use `references/deliverable-map.md` so nothing is missed.

---

## STEP 2 — TRIAL READINESS GAP REPORT

This is the most important output for cases that aren't fully trial-ready yet. The Gap Report
tells the attorney exactly what's missing and how to fill each gap.

### Gap Report Structure

Generate `Trial Readiness Gap Report — [Client Name] [Date].docx` at the case root. Five sections: Executive Summary with readiness score (READY / NEAR-READY / SIGNIFICANT GAPS / NOT TRIAL-READY) · Critical Gaps (what, why it matters, which skill + trigger phrase, time to produce) · Non-Critical Gaps · Folder Organization Issues · Case Brain Sync Issues.

Read `references/gap-report-structure.md` now for score definitions and the critical / non-critical deliverable lists; trigger phrases come from `references/skill-routing-table.md`.

---

## STEP 2.5 — ISSUE LEDGER GAP REPORT (Front Matter)

A second, complementary gap analysis driven by the Issue Code Ledger maintained by `dw-issue-code-tracker-crim` (taxonomy v2.0): Step 2 asks what *deliverables* are missing; this step asks what *legal issues* are still Open. It becomes the first analytical document the attorney reads.

**Generate this BEFORE finalizing the rest of the trial notebook** so the attorney can
close any open issues before locking down witness order, exhibits, and motions.

**2.5A** read `Case Tables.xlsx` → `Issue Codes` (if absent, one-page placeholder; continue) · **2.5B** save to `{CASE_ROOT}/01 - Trial Notebook/00-Trial-Readiness-Gap-Report.docx` · **2.5C** `docx` skill, work-product marked: header, status counts + readiness %, per-code Open issues with recommended action, Addressed, N/A, sign-off · **2.5D** STALE = Open and `Last Updated` > 30 days · **2.5E** `Linked Skill` is a recommendation only — never auto-invoke.

Read `references/issue-ledger-gap-report.md` now for the placeholder language, header, per-code structure, recommended-action rules, and sign-off block.

---

## STEP 3 — ORGANIZE THE TRIAL NOTEBOOK

With the inventory complete, organize the Trial Notebook folder:

**3A** move/copy misplaced files to the correct tab — **ask before moving anything ambiguous** · **3B** create missing standard tab folders/subfolders (`00-` front matter, `99-` appendix) · **3C** naming audit (`[3-digit prefix] - [Document Name].ext`); rename suggestion table only, never auto-rename.

Read `references/organize-notebook.md` now for the placement map and full folder tree.

---

## STEP 4 — GENERATE THE MASTER TRIAL INDEX

The Master Trial Index is the attorney's single entry point to the entire trial file. It is
a `.docx` document with `file://` links to every deliverable, organized by Trial Notebook tab.

### Index Document Structure

`MASTER TRIAL INDEX — [Client Last Name] [Date].docx`, saved at the case root. Cover section → Front Matter link to the Step 2.5 Gap Report ("READ FIRST") → one section per tab (deliverable table + gap callouts) → Pretrial cross-references, Case Tables link, Case Brain link, `99 —` Issue Code Ledger Appendix link. `file://` links use the host path from `gdrive_path` with `dw-case-brain-crim` URL encoding; **verify every link target exists** — flag, never link to a dead path.

Read `references/master-index-structure.md` now for the cover block, table format, post-tab sections, and encoding rules.

---

## STEP 5 — ATTORNEY CHECKLISTS

Generate three courtroom-ready checklists and save them to the case root alongside the
Master Index.

**5A** Day of Trial Checklist — logistics, not strategy · **5B** Exhibit Authentication Checklist — auto-populated from the Evidence Table; Objection Planned left for the attorney · **5C** Witness Schedule Worksheet — pre-filled from the Witness List and Tab 3 cross outlines; Contact Info and Subpoena Status left for staff.

Read `references/attorney-checklists.md` now for file names, every checklist item, table columns, and pre-fill rules.

---

## STEP 5.5 — ISSUE LEDGER APPENDIX (Back Appendix)

Point-in-time snapshot of the Issue Code Ledger as a back-of-notebook appendix — the attorney's preserved record of the ledger's state at assembly.

**Run this LAST**, after every other Trial Notebook output is produced, so the snapshot
reflects every status update made during this build session.

**5.5A** read `Case Tables.xlsx` → `Issue Codes` (placeholder if absent; continue) · **5.5B** save to `{CASE_ROOT}/01 - Trial Notebook/99-Issue-Code-Ledger-Appendix/[YYYY-MM-DD]_Issue-Ledger-Snapshot.docx` · **5.5C** `docx` skill, work-product marked: header, full ledger table (every row, sorted by Code), then the Case Brain `Issue Ledger Audit Trail` · **5.5D** Step 2.5 is *analytical*; this appendix is *archival*.

Read `references/issue-ledger-appendix.md` now for the header block, table columns, and audit-trail instructions.

---

## STEP 6 — UPDATE THE CASE BRAIN

Log every new deliverable in `COMPANION SKILL OUTPUTS`, update `CURRENT STATUS` with the readiness assessment, add a `SESSION LOG` entry (date, score, gap counts, deliverables cataloged), and set `NEXT STEPS` to the top 3 gaps.

Read `references/case-brain-update-and-results-summary.md` now for the exact update checklist.

---

## STEP 7 — PRESENT RESULTS TO ATTORNEY

Display the results summary block (readiness, trial date, deliverables found, gap counts, generated files, top 3 gaps with trigger phrases), then provide `file://` (or Cowork `computer://`) links to each generated file.

Read `references/case-brain-update-and-results-summary.md` now for the exact summary format.

---

## Guardrails

- **This skill assembles; it does not create.** Never draft a cross-examination, jury
  instruction, motion, or other substantive legal document. If something is missing, tell
  the attorney which skill to run — don't try to fill the gap yourself.
- **Never delete or overwrite existing files.** The Trial Notebook may contain attorney work
  product that was manually placed. Move files only when clearly misplaced, and always ask
  first if ambiguous.
- **Never skip the Case Brain update.** The Case Brain is the living record — every run of
  this skill must be logged.
- **Verify links before including them.** A dead `file://` link in the Master Index is worse
  than no link. Confirm every file exists at the path before linking.
- **Respect the attorney's organization.** If the folder structure deviates from the standard
  but appears intentional (e.g., custom tabs for a complex multi-defendant case), note it
  but don't "fix" it.
- **Phase awareness.** If the case is still in Phase 1, this skill is premature. Warn the
  attorney and suggest running Phase 2 analysis first. If in Phase 2, proceed but expect
  many gaps — the Gap Report becomes the primary deliverable.
- **Always read `references/deliverable-map.md`** before scanning. It contains the complete
  list of upstream deliverables, their expected locations, and the skill that produces each one.

---

## Integration with D&W Skill Ecosystem

This skill sits downstream of every other D&W skill. Here's the routing table for filling gaps:

Read `references/skill-routing-table.md` now for the full Missing Deliverable → Skill → Trigger Phrase table.

---

## Output Paths

Apply the output-path formula from `dw-shared-protocols-crim/references/output-path-formula.md` (anchored on `{{CASE_ROOT}}`). Trial Notebook Builder is unique in the D&W skill ecosystem because it writes directly into the trial notebook itself — its outputs anchor on `{{CASE_ROOT}}/01 - Trial Notebook/` and the case root.

Master Trial Index, both Gap Reports, and the three checklists save to `{{CASE_ROOT}}/` (Master Index alongside `Case Tables.xlsx`; Step 2.5 and 5.5 outputs inside `01 - Trial Notebook/`); folder edits stay within the 9-tab structure. All generated documents carry attorney work-product marking; existing notebook files are never re-marked.

Read `references/output-paths.md` now for the full deliverable-by-deliverable path table and marking rules.

---

## Changelog

Version history (v1.0 April 2026 → v1.1 April 2026 → v1.1 May 2026, including the Step 2.5 / 5.5 issue-ledger integration) lives in `references/changelog.md`.

---

*Read `references/deliverable-map.md` for the complete deliverable checklist with expected
locations, producing skills, and criticality ratings.*

---

## Quick References

Each step names the files it needs. All live in `references/`:

- **deliverable-map.md** — Guardrails + Step 1E; every deliverable scanned for, by tab, with location, producing skill, phase, and criticality
- **case-context-load.md** — Step 0.6; case-folder prompts, Case Brain extraction list, scope confirmation
- **scan-and-inventory.md** — Step 1; folder-scan tables, Case Tables audit, Brain cross-reference, Inventory Table format
- **gap-report-structure.md** — Step 2; five-section Gap Report, readiness scores, critical / non-critical deliverable lists
- **issue-ledger-gap-report.md** — Step 2.5; front-matter Issue Ledger Gap Report structure, stale logic, routing discipline
- **organize-notebook.md** — Step 3; file placement map, 9-tab folder tree, naming audit
- **master-index-structure.md** — Step 4; Master Trial Index layout and file:// link construction
- **attorney-checklists.md** — Step 5; Day of Trial, Exhibit Authentication, Witness Schedule checklists
- **issue-ledger-appendix.md** — Step 5.5; back-appendix ledger snapshot structure and audit trail
- **case-brain-update-and-results-summary.md** — Steps 6–7; Case Brain update checklist and results summary block
- **skill-routing-table.md** — Step 2 + Integration; Missing Deliverable → Skill → Trigger Phrase table
- **output-paths.md** — Output Paths section; full deliverable path table and marking rules
- **changelog.md** — version history (v1.0 → v1.1); not needed during a build
