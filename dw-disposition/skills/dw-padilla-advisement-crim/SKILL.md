---
name: dw-padilla-advisement-crim
category: disposition
description: >
  [OUTCOME]: Signable, written plea-consequence advisements. Flagship: bilingual (EN/ES)
  Padilla immigration advisement (.docx) — deportability, inadmissibility, ICE detention,
  bars to relief — with client/attorney/interpreter signature blocks. Companion (any
  client): full collateral-consequences advisement — registration, firearms, licensing,
  housing/benefits/aid, voting — plus a one-page plea-counseling checklist.
  [TRIGGER]: ALWAYS invoke for "Padilla advisement," "immigration consequences of a plea,"
  "non-citizen plea warning," "collateral consequences," "what else does this plea do,"
  "registration consequences," "will he lose his license/housing/gun rights," or any request
  to warn a defendant about immigration or other collateral effects of a conviction or plea.
  [ANTI-TRIGGER]: NOT for immigration relief/removal-defense strategy (refer to immigration
  counsel), client status letters (dw-client-communication-drafter-crim), or plea
  trial-exposure math (dw-plea-negotiation-analyzer-crim).
---

# D&W Padilla Immigration & Collateral-Consequences Advisement

Produces a written, signable Padilla advisement for a non-U.S.-citizen client, per
*Padilla v. Kentucky*, 559 U.S. 356 (2010). Cowork drafts; the attorney reviews, and the
attorney and interpreter sign. This skill does NOT give immigration legal advice — it warns
the client and routes the specifics to immigration counsel.

The immigration advisement remains the flagship module. The skill ALSO runs a general
collateral-consequences advisement (Step 2A) for ANY client — U.S. citizen or not — covering
sex-offender registration, firearms, occupational licensing, housing/benefits/student aid, and
voting, and produces a one-page plea-counseling checklist for the case file.

## Before you start
- Read `references/firm-context.md` (jurisdiction, formatting, quality preference).
- Check `learnings.md` and apply any rules.
- If the current directory has a `claude.md` (per-matter), read it for case context.
- **Load the case:** pull client, charges, court/division/judge, attorney, primary language, and
  any expressed wish to be deported from the **Case Brain** (`dw-case-brain-crim`) and/or
  `000 - Case Profile.docx`. Use these to pre-fill inputs; only ask for what is missing.

## Step 1 — Gather inputs
Confirm/collect (AskUserInput only for gaps not answered by the Case Brain/Profile/claude.md):
- Client full name + DOB; **citizenship/immigration status confirmed**. The immigration
  advisement (Steps 2–3) runs ONLY for confirmed non-U.S.-citizens (never generate it for a
  U.S. citizen); for a U.S.-citizen client, skip Steps 2–3 and run Step 2A only.
- Docket, court + division, judge, attorney of record.
- Charges (statute + short name), per count.
- Primary language / interpreter language. **Language mode:** `bilingual` (EN-ES, default) or `en`.
  (Languages other than Spanish require a certified translator — generate `en` and note this.)
- Has the client expressed a wish to be deported/removed? (Y/N) → controls the "wish to be
  deported" caution section.
- Sentence exposure phrase for the caution (e.g., "a long Louisiana prison sentence (Count 1
  carries mandatory life without parole)"), if the caution is included.

## Step 2 — Classify immigration consequences (per charge)
Read `references/immigration-consequences-classification.md`. For EACH charge, determine which
categories apply (aggravated felony, crime involving moral turpitude, controlled substance,
firearm, domestic-violence/child-abuse, sex-offense registration) and the governing INA cites.
Then:
- Compose the case-specific **charge-classification paragraph** (advisement point 2) in English
  and, for bilingual mode, Spanish. Preserve the statutory citations exactly.
- Set `conditional_flags` for any of: `sex_offense_registration`, `controlled_substance`,
  `firearm`, `domestic_violence`.
- **Flag uncertainty:** immigration categorization can turn on the record of conviction and the
  categorical/modified-categorical analysis. Where the result is not clearly established, say
  "[REQUIRES VERIFICATION BY IMMIGRATION COUNSEL]" in the paragraph rather than overstating.
  When the consequence is clear (e.g., an aggravated felony), state it clearly, as Padilla requires.

## Step 2A — Collateral-consequences advisement (all clients)
Run for EVERY client facing a plea or conviction — U.S. citizens included; ask counsel only if
they want it skipped. Read `references/collateral-consequences-modules.md` and work the four
modules against each charge in the plea:
- **CC-A — Sex-offender registration/notification**: La. R.S. 15:540 et seq. — registrable
  offenses, tier durations and renewal, notification, residency/presence restrictions.
- **CC-B — Firearms**: La. R.S. 14:95.1 (enumerated felonies; 10-year cleansing rule) plus the
  lifetime federal bar of 18 U.S.C. § 922(g)(1) — and the warning that state cleansing or
  expungement alone does NOT lift the federal bar.
- **CC-C — Occupational licensing**: La. R.S. 37:2950 framework, board carve-outs, CDL.
- **CC-D — Housing, benefits, student aid, voting**: public housing/Section 8 screening,
  SNAP/TANF (Louisiana opt-out), federal student aid, La. R.S. 18:102 voting suspension, jury.

Then complete the one-page checklist in `references/plea-counseling-checklist.md` (consequence
category × triggered-by-this-plea? × client-advised? × date) and save it with the advisement.
Apply the same clarity rule as Step 2: state clearly triggered consequences plainly ("will");
mark unclear ones "UNCLEAR — may result; requires verification" and route to the specialist
skill rather than guessing. When `dw-plea-negotiation-analyzer-crim` invoked this check from its
collateral-consequences gate, hand the completed checklist back for its plea memo.

## Step 3 — Generate the document
(Immigration advisement only — for a U.S.-citizen / Step 2A-only run, skip to Step 4 and deliver
the collateral-consequences advisement and completed checklist as a standalone document.)

Write a `case_params.json` (schema documented at the top of the generator) capturing Step 1–2
values, then run:

```bash
python3 scripts/generate_padilla_advisement.py \
  --params case_params.json \
  --language-file assets/advisement_language.json \
  --out "Padilla Immigration Advisement (Bilingual EN-ES) - [Client Last] - [YYYY-MM-DD].docx"
```

The fixed advisement language lives in `assets/advisement_language.json` (mirrored, human-readable,
in `references/advisement-language-en-es.md`). **Do not paraphrase** the fixed blocks — edit the
asset if the firm's standard language must change. Only the charge-classification paragraph, the
conditional points, the deportation-caution sentence, and the case-identifier fields are per-case.

If `python-docx` is unavailable: `pip install python-docx --break-system-packages`.

## Step 4 — Save, verify, deliver
- Save to the matter's client-facing folder: `[CASE_ROOT]/02 - Pretrial Notebook/Docs to Client/`
  (fall back to CASE_ROOT if that folder does not exist).
- Render to PDF and eyeball it before delivering (see the `docx` skill's soffice/pdftoppm steps).
- Deliver the .docx and note it is a **DRAFT that REQUIRES ATTORNEY REVIEW** and attorney +
  interpreter signature before use.
- If Step 2A ran, save the completed plea-counseling checklist to the same folder (same DRAFT
  caveat) and offer a copy to `dw-plea-negotiation-analyzer-crim` for the plea memo.

## Step 5 — Quality review (client-facing)
Per `references/firm-context.md` quality preference (this is a client-facing document): have a
fresh reviewer confirm (a) every charge is addressed, (b) classifications match
`references/immigration-consequences-classification.md`, (c) no U.S.-citizen received the
immigration advisement, (d) Spanish mirrors English, (e) signature/certification blocks are
intact, (f) if Step 2A ran, every checklist row is marked Y/N/UNCLEAR and dated, and the
collateral classifications match `references/collateral-consequences-modules.md`.

## Legal compliance guardrails (mandatory)
1. **Cite specific authority** — keep the INA/U.S.C. and *Padilla* citations exact; never invent cites.
2. **Flag uncertainty** — mark unclear immigration categorizations "[REQUIRES VERIFICATION BY
   IMMIGRATION COUNSEL]" instead of guessing. The same rule governs Step 2A: mark unclear
   collateral consequences "UNCLEAR — requires verification" and preserve every
   `[VERIFY CITATION]` flag from the modules reference until the attorney confirms it.
3. **Not legal research / not immigration advice** — this advisement is general information; it
   must state, and the workflow must treat it as, a warning that routes eligibility questions to
   immigration counsel.
4. **Preserve original language** — do not paraphrase the fixed advisement blocks or the client's
   charges; quote statutes as written.
5. **Attorney review required** — every output carries the attorney-work-product / DRAFT footer and
   is not valid until the attorney (and interpreter, where used) review and sign.

## After the run
Ask: "Did this meet your expectations? Anything to improve for next time?" Log useful feedback to
`learnings.md`. Offer to record the advisement in the Case Brain (`COMPANION SKILL OUTPUTS`) and
against any open plea/immigration issue.
