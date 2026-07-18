# Filed Pleading Boilerplate — Convenience Index

One-stop reference for consuming skills that produce **filed pleadings** (motions, oppositions, memoranda, sentencing memoranda, proposed orders, notices of hearing). Walks through the complete boilerplate workflow in the order it must be applied.

This file is a convenience index — it does NOT replace the underlying component references. Read each component file as you reach it.

## What counts as a filed pleading

Anything served on opposing counsel or filed with the court:
- Motions (suppression, in limine, to compel, for continuance, etc.)
- Oppositions (404(b) opposition, opposition to motion to revoke bond, etc.)
- Memoranda in support / in opposition
- Sentencing memoranda
- Proposed orders
- Notices of hearing
- Certificates of service
- Habitual offender opposition pleadings
- Bond and pretrial release motions
- Post-conviction relief applications

NOT a filed pleading (use `attorney-work-product-marking.md` + `output-path-formula.md` instead):
- Internal audit reports
- Cross-examination outlines
- Discovery ledgers / triage reports
- Investigation tasking documents
- Voir dire dashboards / strike sheets
- Plea analysis memos
- Case Brain / running case notes

## Step-by-step boilerplate workflow

### Step 1 — Resolve required variables from Case Brain

Confirm all of the following are resolved from `dw-case-brain-crim` (v3.3+) BEFORE drafting:

- `{{CASE_ROOT}}` — absolute case folder path
- `{{DEFENDANT_NAME}}` — last, first, middle as filed
- `{{DOCKET}}` or `{{CASE_NUMBER}}` — docket/case number
- `{{PARISH}}` — parish name
- `{{COURT}}` — judicial district or court name
- `{{DIVISION}}` or `{{SECTION}}` — division letter (state) / section letter (Orleans)
- `{{JUDGE_NAME}}` — assigned judge
- `{{ADA_NAME}}` — assigned ADA / AUSA
- `{{ADA_EMAIL}}` — service email
- `{{HEARING_DATE}}`, `{{HEARING_TIME}}` — if applicable
- `{{CLIENT_NICKNAME}}` — short folder name for path formula

If any required variable is missing, **prompt the attorney before drafting**. Never insert placeholders into a final pleading.

### Step 2 — Apply the correct caption

Select caption file by jurisdiction:

| Court | Caption reference |
|---|---|
| 14th JDC (Calcasieu) | `caption-criminal-14thJDC.md` |
| 12th JDC (Avoyelles) | `caption-criminal-12thJDC-avoyelles.md` |
| Orleans Criminal District Court | `caption-criminal-orleans-CDC.md` |
| 19th JDC (East Baton Rouge) | `caption-criminal-19thJDC-EBR.md` |
| Federal — Western District of LA | `caption-criminal-federal-WDLA.md` |
| Other Louisiana parish | `caption-criminal-fill-in.md` (prompts attorney for parish/court values) |

### Step 3 — DO NOT apply work product marking

Filed pleadings receive **NO** work product marking. The standard "ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL" header must NOT appear on anything served or filed. See `attorney-work-product-marking.md` Section "No marking" for the rule.

This is the single most common drafting error. Verify before saving.

### Step 4 — Apply Louisiana citation style

Read `louisiana-citation-style.md`. Key points:
- La. C.Cr.P. Art. ___ (criminal procedure)
- La. C.E. Art. ___ (evidence)
- La. R.S. ___:___ (revised statutes)
- *State v. [Defendant]*, ___ So.3d ___ (La. ___) — italicize case names
- 5th Circuit and Louisiana Supreme Court decisions take precedence in 14th JDC

### Step 5 — Append signature block

Read `signature-block.md`. The standard D&W block is firm-wide; do not improvise.

### Step 6 — Append Certificate of Service

Read `certificate-of-service.md`. Use the State-court version for parish courts and the federal version for WDLA filings (both are in the same file).

### Step 7 — Append Notice of Hearing (if motion is set for hearing)

Read `notice-of-hearing.md`. Skip for pleadings that do not need hearing (e.g., proposed orders submitted ex parte, certain post-conviction filings).

### Step 8 — Append Proposed Order (if relief is sought)

Read `proposed-order.md`. Most motions require a proposed order; oppositions typically do not.

### Step 9 — Apply 14th JDC filing conventions (if filing in Calcasieu)

Read `filing-conventions-14thJDC.md`. Covers Calcasieu-specific page/margin/font requirements, e-filing rules, courtesy copy expectations.

For other parishes, consult the relevant local rules — D&W has not yet built per-parish convention references for every jurisdiction.

### Step 10 — Resolve output path

Read `output-path-formula.md`. Filed pleadings save to:

`{{CASE_ROOT}}/01 - Trial Notebook/[appropriate motion subfolder]/`

NOT to the Cowork Analysis folder (that's for internal work product).

The exact subfolder depends on the pleading type — pretrial motions, sentencing pleadings, post-conviction filings each have their own home in the trial notebook structure. Consult the firm's folder convention or the consuming skill's specific output guidance.

### Step 11 — Save filed and (optionally) draft versions

If the skill is producing both an attorney review draft AND a filed version:
- Filed version: NO work product marking, saved with `_FILED` or no suffix
- Draft version: WITH work product marking, saved with `_DRAFT_INTERNAL` suffix

See `attorney-work-product-marking.md` Section "Filed-vs-internal disambiguation".

## Quick consumer checklist

For a consuming skill, the loaded references are typically:

1. `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` (this file — orchestration)
2. The correct caption file for the jurisdiction
3. `signature-block.md`
4. `certificate-of-service.md`
5. `notice-of-hearing.md` (if applicable)
6. `proposed-order.md` (if applicable)
7. `louisiana-citation-style.md`
8. `filing-conventions-14thJDC.md` (if Calcasieu)
9. `output-path-formula.md`

The consuming skill's STEP 0.5 should reference this orchestrator file plus the jurisdiction-specific components it knows it will need.

## Common drafting errors to avoid

- **Work product marking on a filed pleading** — never. Filed = clean.
- **Wrong caption** — Orleans uses Section letters (A, B, C…), state JDCs use Division letters. Federal uses different formatting entirely.
- **Missing certificate of service** — every filed pleading requires one.
- **Hard-coded paths** — always anchor on `{{CASE_ROOT}}` from Case Brain. Never `/home/claude`, `/tmp`, `~/Downloads`, or absolute paths from the prompt without confirmation.
- **Stale citation format** — Louisiana citation style differs from federal Bluebook in places. Use the LA reference, not generic Bluebook.
- **Forgetting the proposed order** — most motions need one, even if the skill's main deliverable is the motion itself. Produce both.
