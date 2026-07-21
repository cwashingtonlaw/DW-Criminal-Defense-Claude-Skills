---
name: dw-padilla-advisement-crim
description: >
  [OUTCOME]: Generates a signable, bilingual (English/Spanish) Padilla immigration-consequences
  advisement (.docx) that notifies a non-U.S.-citizen client, in writing, of the immigration
  effects of pleading guilty or being found guilty — deportability, inadmissibility, mandatory
  ICE detention, bars to relief/naturalization — with client, attorney, and interpreter
  certification/signature blocks.
  [TRIGGER]: ALWAYS invoke for "Padilla advisement," "immigration advisement," "advise the client
  of immigration consequences," "immigration consequences of a plea," "non-citizen plea warning,"
  "advise non-citizen client," or any request to warn a non-U.S.-citizen defendant about the
  immigration effects of a conviction or plea.
  [ANTI-TRIGGER]: Do NOT use for actual immigration relief analysis or removal-defense strategy
  (refer to immigration counsel); for general client status letters (use
  dw-client-communication-drafter-crim); or for the plea trial-exposure math (use
  dw-plea-negotiation-analyzer-crim).
---

# D&W Padilla Immigration-Consequences Advisement

Produces a written, signable Padilla advisement for a non-U.S.-citizen client, per
*Padilla v. Kentucky*, 559 U.S. 356 (2010). Cowork drafts; the attorney reviews, and the
attorney and interpreter sign. This skill does NOT give immigration legal advice — it warns
the client and routes the specifics to immigration counsel.

## Before you start
- Read `references/firm-context.md` (jurisdiction, formatting, quality preference).
- Check `learnings.md` and apply any rules.
- If the current directory has a `claude.md` (per-matter), read it for case context.
- **Load the case:** pull client, charges, court/division/judge, attorney, primary language, and
  any expressed wish to be deported from the **Case Brain** (`dw-case-brain-crim`) and/or
  `000 - Case Profile.docx`. Use these to pre-fill inputs; only ask for what is missing.

## Step 1 — Gather inputs
Confirm/collect (AskUserInput only for gaps not answered by the Case Brain/Profile/claude.md):
- Client full name + DOB; **non-citizen status confirmed** (do not run for U.S. citizens).
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

## Step 3 — Generate the document
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

## Step 5 — Quality review (client-facing)
Per `references/firm-context.md` quality preference (this is a client-facing document): have a
fresh reviewer confirm (a) every charge is addressed, (b) classifications match
`references/immigration-consequences-classification.md`, (c) no U.S.-citizen was processed,
(d) Spanish mirrors English, (e) signature/certification blocks are intact.

## Legal compliance guardrails (mandatory)
1. **Cite specific authority** — keep the INA/U.S.C. and *Padilla* citations exact; never invent cites.
2. **Flag uncertainty** — mark unclear immigration categorizations "[REQUIRES VERIFICATION BY
   IMMIGRATION COUNSEL]" instead of guessing.
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
