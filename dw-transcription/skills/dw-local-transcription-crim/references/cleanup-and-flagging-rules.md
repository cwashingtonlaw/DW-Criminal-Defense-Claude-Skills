# ASR Cleanup and Flagging Rules

What to correct, what to leave alone, and how to mark uncertainty.

Governing principle: **the transcript must never be more confident than the evidence.** Every
correction narrows what a reader can second-guess. Make corrections that are certain, mark the rest,
and correct nothing where the error itself is the legal issue.

---

## Correct silently — errors unambiguous from context

- **Spelled words the speaker is spelling.** Whisper renders `B-R-O-W-N` as `D-R-O-W-N` when the
  speaker has just said his name is Brown. Correct it.
- **Homophone slips with one possible reading.** "You have the right to remain **solid**" → *silent*.
  But see the exception below — inside a rights advisement this becomes a flag, not a fix.
- **Local place names.** See `louisiana-audio-conventions.md`.
- **Obvious sentence-level garble where the intended word is forced by syntax** — "tried to fight it
  with our lawyer" → "without a lawyer."

Document the practice in Methodology. Never list corrections individually — that is noise.

---

## Mark, don't correct

| Situation | Marker |
|---|---|
| Speech present, unresolvable | `[INAUDIBLE]` |
| Proper noun by sound, spelling unverified | `Kodin [PHONETIC]` |
| Rendered as recognized, legally significant | `[SIC -- SEE ANNOTATION n]` |
| Editorial word supplied | `we'll get you out of here. You good with [that]?` |
| Non-verbal on the recording | `[Complies.]` `[No audible response.]` |

Every `[PHONETIC]` proper noun also goes in an annotation listing unverified names collectively. That
list is investigative work product in itself — it is where "Iselyn Malva" turned out to be **Malvo**,
spelled on the record M-A-L-V-O, and "Taronda Malboro" turned out to be **Tarhonda Malbrough**.

---

## NEVER correct — the rights advisement

**Absolute rule. Do not tidy any part of a Miranda advisement into its standard form.**

A misadvisement is a suppression issue. Correcting it erases the issue silently, and nobody
downstream will ever know to look.

When ASR produces something non-standard inside an advisement:

1. **Leave it as rendered.** Mark `[SIC -- SEE ANNOTATION n]`.
2. **Re-decode the passage** under different settings — greedy, temperature 0, separately windowed.
3. **Report whether the two passes agree**, quoting both verbatim.
4. **State the counter-argument in the same annotation.**
5. **Tell the attorney to listen**, and say what turns on it.

Worked example:

> Pass 1: *"If you cannot afford a lawyer, we won't be able to appoint or represent you for any
> questions if you wish."*
> Pass 2: *"if you cannot afford a lawyer we won't be appointed to represent you point question if
> you wish."*
> Standard: *"one will be appointed to represent you before any questioning if you wish."*
>
> Both passes produce a **negation**. **But** "one will be appointed" and "we won't be appointed" are
> acoustically close under fast speech, and this recognizer demonstrably mishears this recording — it
> rendered "right to remain silent" as "right to remain **solid**" on both passes. A consistent
> machine negation is **not** proof the officer negated the right. It is a reason to put on headphones.
> If he said it, the waiver is materially defective. If he didn't, this dies here at zero cost.

The same discipline resolves things in the State's favor, and you keep those too. In the same
advisement, pass 1 rendered the continuing-right prong as an interrogative — *"Are you deciding to
exercise these rights and stop answering...?"* — which would have read as an invocation followed by
continued questioning. Pass 2 resolved it to the standard declarative. The transcript reflects pass 2,
and the annotation is kept and marked **RESOLVED — NO ISSUE**, so the reader knows it was examined.

Extend the rule to any recited legal text: consent-to-search forms, *Padilla* advisements, waiver
language, plea colloquies.

---

## Structuring turns

Whisper segments are transcription units, not speaker turns. Merge them into Q./A. turns by content.
In a Q&A interview the semantic structure is unambiguous and **content-based turn assignment is more
accurate than machine diarization at line level.**

- One `Q.` per question or connected run of questions from the examiner.
- One `A.` per answer.
- Interruptions: trailing ` --` on the interrupted turn, leading `-- ` on the resumption.
- Long single-speaker passages stay one turn; the paginator wraps them.
- Insert `(Runtime hh:mm:ss)` markers at topic shifts, roughly every 1–3 minutes.

---

## PII

Transcribe it. Do not redact in the working document — a redacted transcript that diverges from the
recording is worse than useless on cross.

Instead: warn on the caption page, list what is present, and annotate the specific runtime where a
Social Security number or minor's identifier is spoken so redaction before filing is mechanical.

Juvenile witnesses: **initials only** in anything leaving the office, matching how the State's own
filings handle them under La. R.S. 46:1844(W). Full names may stay in the internal working copy if
the folder structure already uses them, but flag that the folder names themselves are a disclosure
risk.

---

## What the hand pass actually costs

For 63 minutes of audio — about 11,200 spoken words — the hand pass is the dominant cost of a
court-reporter transcript. Budget roughly **one working session per hour of audio**, and say so before
committing to a set. Six hours of audio is six sessions, not one long one.

If asked for court-reporter treatment at a volume that can't be done properly, say so and propose an
order. **Do not produce numbered-line documents with unverified machine text** — they look finished
and are not, and that is worse than a working transcript that admits what it is.
