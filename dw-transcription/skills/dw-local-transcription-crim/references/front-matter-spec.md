# Transcript Front Matter Specification

What precedes the transcript body. Not optional. A reader who opens page 1 must learn, before reading
a word of testimony, what this document is, what it is not, what is missing, and what to check.

Order below is the order it appears.

---

## 1. Caption page

```
14th JUDICIAL DISTRICT COURT
PARISH OF CALCASIEU
STATE OF LOUISIANA

STATE OF LOUISIANA
VERSUS
<CLIENT NAME>
DOCKET NO. <number>, DIVISION <div>
────────────────────────────────────
TRANSCRIPT OF RECORDED INTERVIEW
<INTERVIEWEE NAME>
Taken <date>, at <time>
<agency and location, as stated on the recording>
<report number> — <offense description>
────────────────────────────────────
Evidence Item #__ · Prepared for the defense of <client>
<attorney>, <office>
Transcript prepared <date>
```

Court and parish come from the case gate. Date, time, location and report number come **from the
recording's own opening announcement**, not from the folder name or a police report — those disagree
often enough to matter.

## 2. The two standing disclaimers

Verbatim, on the caption page, italic:

> **THIS IS NOT A CERTIFIED COURT REPORTER'S TRANSCRIPT.** It is a defense-prepared working transcript
> of a recorded law-enforcement interview, produced by machine speech recognition with attorney-directed
> review. It has no independent evidentiary standing and must be verified against the source recording
> before use in any filing, examination, or stipulation.

> **THIS DOCUMENT CONTAINS PERSONALLY IDENTIFIABLE INFORMATION** spoken on the recording, including a
> Social Security number, dates of birth, telephone numbers, a home address, and the names of minor
> children. Handle accordingly. If any portion is filed or served, redact per La. R.S. 46:1844(W) and
> any protective order in the matter.

Adjust the PII list to what the recording actually contains. Do not include a category that isn't there.

## 3. Appearances / persons present

Two-column table. One row per person, plus an **Examiners** row giving the block-level examination map:

> DET. RANDOLPH conducts the examination from 00:00:04 to 00:54:10 and again from 00:58:09 to the
> close. DET. MILLER conducts it from 00:54:10 to 00:57:47. Identified by cross-recording voiceprint
> analysis and confirmed by the attorney — see Annotation 2.

Rows: Interviewee (with DOB and posture — charged? co-defendant? in custody?), each officer with how
they were identified and at what runtime, Examiners, Others present, Counsel present.

Anyone not named on the record gets `[ATTORNEY TO VERIFY against the video.]`

## 4. Designation convention

Two-column table defining every marker used:

| Marker | Meaning |
|---|---|
| `BY DET. ___:` | Change of examiner. Every `Q.` following is by that officer until the next marker. Block-level; line-level attribution was not attempted and should not be inferred. |
| `Q.` | Question by the examiner named in the most recent marker. |
| `A.` | Answer by the interviewee. |
| `[INAUDIBLE]` | Speech present but unresolvable. |
| `[PHONETIC]` | Proper noun rendered by sound; spelling unverified. |
| `[SIC]` | As spoken or as recognized; see cross-referenced annotation. |
| `[ ]` | Editorial insertion supplying an obviously elided word. **NOT on the recording.** |
| `(Runtime hh:mm:ss)` | Elapsed time from the start of segment 1. State whether continuity across segments is assumed. |

If speakers could not be separated at all, say so here and use `Q.`/`A.` with an express warning not to
attribute any line to a named officer.

## 5. Source media table

One row per file: filename, bytes, duration, status. Status is one of `TRANSCRIBED — Segment N`,
`DUPLICATE of Segment N`, or `NOT TRANSCRIBED — <reason>`.

Below it: total transcribed runtime, and the container format and audio codec.

**Every file in the folder appears here, including the ones you could not read.** A source table that
lists only what worked is how a coverage gap disappears.

## 6. Methodology and limitations

Numbered. Must state:

1. Extraction — tool, target format, and **that no filtering, gain, or normalization was applied**.
2. ASR — model, that it ran **locally on attorney hardware**, `condition_on_previous_text` disabled,
   temperature fallback, and **that no initial prompt or name list was supplied**, so no proper noun
   was suggested to the recognizer.
3. Diarization — what was tried, what was rejected and on what measurement, what was used, on what
   device. Include rejected approaches: a reader deciding how much to trust the labels needs to know
   an earlier method scored 0.348 and was thrown out.
4. Speaker identification — the full anchor chain with cosine figures, so the reasoning is auditable
   rather than asserted.
5. Cleanup rules — what was corrected, what was deliberately left alone.
6. **That nothing has been verified against the recording by a human listener.**

## 7. Annotations table

The heart of the document. Columns: `#`, `Runtime`, `Issue`. See `assets/annotation-catalog.md` for
the twelve recurring types.

Rules:

- **Ranked by consequence, not chronology.** A coverage gap and a defective Miranda advisement go
  first.
- **Every annotation names the action.** "LISTEN TO THIS PASSAGE." "Obtain the executed form."
  "Demand the native files." Not "this is notable."
- **State the counter-argument in the same annotation.** If an ASR artifact could explain the finding,
  say so there, not in a footnote. An annotation that only argues one way will get quoted in a motion
  and then embarrassed at the hearing.
- **Keep annotations that were checked and cleared.** Marking one RESOLVED tells the reader it was
  examined rather than missed — and stops the next person re-doing the work.

## 8. Tags

One line of pipe-separated descriptors: posture, content type, agency, audio characteristics, PII
warning. Machine-greppable across a case.

## 9. Keywords

Spoken-word frequency over `Q.` and `A.` text only — never front matter. Two lists: subject-matter
terms, and named parties and places. Counts included.

## 10. Topic index

`Runtime → Topic`, one row per substantive shift. This is what makes a 67-page transcript navigable.
Write topics as what a reader is *looking for* — "SATURDAY NIGHT — the Left Right Center party;
Tucker's arrival and departure" — not "Discussion of weekend activities."

## 11. Runtime → page:line concordance

Every runtime marker mapped to its page and line. This is what lets an attorney cite the video and the
transcript in the same sentence.

---

## Page numbering

Front matter in lower-case roman (i, ii, iii). Transcript body restarts at **1** so page:line citation
means the transcript body, unambiguously.

## Headers and footers

Header, every page, centered, 9 pt bold, two lines:

```
ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL
PREPARED IN ANTICIPATION OF LITIGATION
```

Footer: section label, interviewee, date, report number, page number.
