---
name: dw-local-transcription-crim
description: >-
  Court-reporter and working transcripts of criminal discovery media, produced entirely on firm
  hardware, with speaker diarization, cross-recording speaker identification, and a media-
  integrity audit. ALWAYS invoke for "transcribe locally," "court reporter transcript,"
  "transcript with speaker labels," "who is speaking on this recording," "identify the detective,"
  "diarize," "which officer asked that," "audit the media," "is the export complete," "the file
  won't open," "8 MB," "cloud-only file," or any request to transcribe interviews, interrogations,
  jail calls, 911 calls, CAC interviews, or body-worn camera where audio must NOT leave attorney
  hardware. Produces a court-reporter .docx with numbered lines and page:line citation, per-item
  working transcripts, a master media index, and a media-integrity report. Do NOT use for vendor-
  routed transcription (dw-transcript-router-crim) or substantive analysis of the resulting
  transcript (dw-jail-call-analyzer-crim, dw-confession-interrogation-auditor-crim).
---

# D&W Local Transcription and Speaker Identification

Transcribes criminal discovery media **on the firm's own machine**. No audio is uploaded to Rev,
JusticeText, case.dev, or any cloud ASR. For a co-defendant's custodial statement or a child forensic
interview under a protective order, that is not a preference — it is the correct handling posture, and
it is a sentence you can say on the record.

This skill exists because vendor platforms return a transcript. They do not tell you that the export
you were given is twenty-eight minutes shorter than the camera original, that the detective may have
misstated the appointed-counsel prong, or that a second officer took over the questioning at minute
fifty-four. **Finding those things is the work.** The transcript is the byproduct.

---

## STEP 0 — HARD STOPS, IN ORDER

**0.1 Court gate.** If the matter is in a project or case folder with a court gate, satisfy it before
anything else. State the court and parish back before drafting, researching, or transcribing.

**0.2 File intake.** Ask: *"Are you uploading any additional audio or video files? I'll start only
after you confirm."* Wait for an explicit answer. Re-running a batch because two more files arrived
is expensive.

**0.3 Load shared protocols.** Read `dw-shared-protocols-crim/SKILL.md` and load:
- `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — every deliverable from this skill is internal work
  product and carries the two-line header.
- `dw-shared-protocols-crim/references/output-path-formula.md` — paths anchor on `CASE_ROOT`.

**0.4 Confirm the deliverable tier before processing anything.** These are not the same job:

| Tier | What it is | Cost |
|---|---|---|
| **Working transcript** | Timestamped, machine speaker labels, searchable, delivered per evidence item | Automated |
| **Court-reporter transcript** | Numbered lines, page:line citation, Q./A., hand-verified proper nouns, annotations, front matter | Roughly one working session per hour of audio |

**Never silently downgrade.** A court-reporter transcript produced without the hand pass looks
finished and is not, which is worse than a working transcript that admits what it is. If the attorney
asks for court-reporter treatment across many hours, say plainly how long that takes and propose an
order. See `references/tiering-and-scope.md`.

---

## STEP 1 — INVENTORY AND PROBE BEFORE TRANSCRIBING

Run `scripts/probe_media.py`. It walks the case tree, finds every media file, and records byte size,
container duration, and whether an audio stream exists.

Do this **first, always**, for three reasons:

1. **Most video in a criminal case has no audio.** In one homicide file: 757 media files, 198 with an
   audio track. The other 548 were silent surveillance. Transcription scope was a quarter of what the
   file looked like.
2. **The case's own inventory will understate the volume.** The same file's Case Brain recorded "12
   hours" because that counted only interviews with a runtime stated in a police report. Actual
   transcribable audio was 36 hours 40 minutes.
3. **Probing reads only container headers and trailers**, so it succeeds on files whose payload cannot
   be retrieved. That is exactly how you discover a truncated production. See Step 5.

---

## STEP 2 — SET UP THE LOCAL PIPELINE

Full commands in `references/pipeline-setup.md`. Summary:

- **FFmpeg** on the machine that holds the files.
- **Python venv** with `mlx-whisper`, `pyannote.audio`, `soundfile`, `numpy`, `torch`.
- **HuggingFace read token**, with terms accepted on `pyannote/segmentation-3.0`,
  `pyannote/speaker-diarization-3.1`, and `pyannote/speaker-diarization-community-1`.
- **Run diarization on Apple MPS, not CPU.** Measured on an M4 Pro: **21× realtime on GPU versus 2.3×
  on CPU.** That 9× difference is what makes case-wide diarization practical rather than a weekend.

Two failure modes that will cost you an hour each if you don't know them:

- **A cloud sandbox cannot do this work.** Anthropic's egress proxy returns 403 for huggingface.co,
  hf-mirror.com, and openaipublic.azureedge.net. No ASR or diarization model can be fetched there.
  Everything runs on the firm machine.
- **Persist the raw pipeline output before formatting it.** pyannote v4 returns a `DiarizeOutput`
  object, not the `Annotation` that v3 returned, and `.itertracks()` does not exist on it. Pickle the
  result the instant it comes back. A formatting bug should never destroy twenty-seven minutes of
  compute — that mistake has already been made once so it does not need making again.

---

## STEP 3 — EXTRACT AND TRANSCRIBE

Run `scripts/batch_transcribe.py`. It extracts 16 kHz mono FLAC, transcribes with Whisper large-v3,
and diarizes anything matching the interview pattern.

**Settings that matter for legal accuracy, and why:**

| Setting | Value | Reason |
|---|---|---|
| `condition_on_previous_text` | **False** | Suppresses carry-over hallucination. Non-negotiable. |
| `initial_prompt` | **None** | Never seed the recognizer with names from the case file. If you prompt with "Sheltren Tucker," the model will produce "Sheltren Tucker" whether or not anyone said it. Every proper noun must be earned from the audio. |
| `word_timestamps` | True | Needed for page:line anchoring and speaker mapping. |
| `temperature` | 0.0–1.0 fallback | Standard. |
| Audio processing | **none** | No filtering, gain, or normalization. You may be asked what you did to the evidence. "Nothing" is the best answer. |

Order the queue **interviews first, longest first**, so the material that matters lands early and a
crash at hour four costs you surveillance footage instead of the client's statement. Make it
resumable — check for existing output and skip.

---

## STEP 4 — IDENTIFY THE SPEAKERS

Diarization returns `SPEAKER_00`, `SPEAKER_01`. Turning those into names is the highest-value step in
this skill, and it is done **from the recordings**, not from the attorney's memory.

Full method in `references/speaker-identification-protocol.md`. The shape of it:

1. **Find a single-officer anchor.** Recorded police interviews open with the officer naming who is
   present. Find a recording that names **exactly one** officer. Its dominant voice is that officer.
2. **Have the attorney confirm the anchor.** Ten seconds of audio. This is the one assumption in the
   chain — the dominant voice in an interview is usually the *witness*, not the questioner, so verify
   rather than assume. Everything downstream is arithmetic on embeddings and is reliable.
3. **Propagate by cosine similarity** of pyannote speaker embeddings. Same voice lands ≥0.75; different
   voices land ≤0.35. The gap is wide and unambiguous.
4. **Solve the rest by elimination.** A recording naming exactly two officers, with one already
   identified, gives you the second for free.

Worked example that produced a real identification:

> Item #38 opened *"myself, Detective Randolph"* — one officer named. Attorney confirmed the voice.
> That voiceprint matched the target interview at **+0.913** and **+0.907**. Item #139 opened
> *"Detective Randolph … Detective George Miller"* — two officers, one known. The remaining voice
> matched the unexplained second questioner in the target interview at **+0.790**, against +0.113 and
> +0.239 for the other two speakers present. **The second examiner was Det. George Miller.**

**Discipline on how far to push it.** Block-level attribution — who is examining across a span — is
reliable. Line-level attribution is not: Whisper word timestamps drift against diarization boundaries
and flip mid-sentence. Mark examiner changes with `BY DET. ___:` in court-reporter convention and
**stop there**. Roughly 15% of lines will be genuinely uncertain; say so rather than guessing.

**Before asserting a third speaker exists, rule out a recording artifact.** Measure RMS, peak, and
spectral centroid per segment. If they match across a file boundary, a new cluster is a new person. If
they don't, it's a gain change and the cluster is noise. In the worked example the four segments
matched within 0.9 dB, which is what made "a third voice enters at minute 54" a finding rather than a
guess.

---

## STEP 5 — AUDIT MEDIA INTEGRITY

**Do this on every case. It is the highest-yield thing in this skill.**

Compare **probed container duration** against **extracted audio duration** for every file. Anything
short is either a retrieval failure or a truncated production, and both matter.

Three patterns worth knowing, all drawn from a single homicide file — details in
`references/media-integrity-audit.md`:

**The 8 MB ceiling.** Files that read exactly 8,388,608 bytes and then fail with "Operation timed out"
are a Google Drive retrieval fault, not corruption. `stat` reports the full size, so Drive knows what
it should be serving. In one case this hit **7.6 hours across seven evidence items**, including both
jailhouse-informant interviews and a threat witness. Try "Available offline," then a browser download.
If the bytes still won't come, the defense does not possess that evidence and that is a written demand.

**The truncated export.** One item's 2026 export ran 1:03:13 against native originals of 1:31:08 — the
first segment byte-identical to the original, and **27 minutes 54 seconds cut out of the back half.**
Found by arithmetic on durations, nothing more.

**The stated-runtime check.** Interviews announce their start and end times on the record. Total the
media and compare. In the same item the detective said 1:23 p.m. and closed at 3:03 p.m. — 100
minutes — against 63 minutes of media. That gap is what sent us looking.

Report every gap in minutes, name the item, and say plainly whether you can tell a retrieval failure
from a production failure. Usually you can't from the workstation, and saying so is the honest answer.

---

## STEP 6 — BUILD THE DELIVERABLES

**Working transcripts** — `scripts/gen_working_transcripts.py`, one per evidence item, written into
the item's own folder. Work-product header, every source file, timestamps, machine speaker labels,
and a coverage-gap warning naming how much is missing.

**Master media index** — same script, `--index-to <dir>`. Every item with recorded runtime, transcribed
runtime, voice count, and coverage status. Zero-audio items in bold.

**Court-reporter transcript** — `scripts/prep_transcript.py` then `scripts/build_transcript_docx.js`.
25 numbered lines per page, Courier New, page:line citable, `Q.`/`A.` with `BY DET. ___:` examiner
markers, runtime markers inline.

Front matter is specified in `references/front-matter-spec.md` and is **not optional**. Minimum:
caption, appearances with examiner blocks, designation convention, source-media table with per-file
duration and status, methodology and limitations, annotations, tags, keyword frequency, topic index,
and a runtime→page:line concordance.

Every deliverable opens with the same two disclaimers: **this is not a certified court reporter's
transcript**, and **it contains PII spoken on the recording** — Social Security numbers, dates of
birth, minors' names — so redact before filing or service per La. R.S. 46:1844(W).

---

## STEP 7 — CLEAN THE ASR, AND KNOW WHAT NEVER TO CLEAN

Rules in `references/cleanup-and-flagging-rules.md`. The one that matters most:

**Never silently correct anything inside a rights advisement.** If Whisper renders *"we won't be able
to appoint or represent you,"* leave it, flag it, re-decode it under different settings, and report
whether the passages agree. Do not tidy it into the standard form. A misadvisement is a suppression
issue and correcting it erases the issue.

And state the counter-argument in the same annotation. In the worked example two independent decodes
both produced a negation — but the same recognizer rendered *"right to remain silent"* as *"right to
remain **solid**"* on both passes, so a consistent machine negation is **not** proof the detective
negated the right. Give the attorney the reason to listen and the reason it might be nothing.

Louisiana specifics — *Iowa* pronounced "eye-oh-way," Lacassine, Calcasieu, Atchafalaya, Opelousas,
and the parish and street names Whisper reliably mangles — are in
`references/louisiana-audio-conventions.md`.

---

## Outputs

| File | Location |
|---|---|
| `WORKING TRANSCRIPT — <item> (<date>).docx` | the evidence item's own folder |
| `MASTER MEDIA TRANSCRIPTION INDEX (<date>).docx` | `{{CASE_ROOT}}/02 - Pretrial Notebook/03 - Case Analysis & Notes/` |
| `Transcript - <item> (COURT REPORTER).docx` | the evidence item's own folder |
| `Media Integrity Audit (<date>).md` | `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` |

Feeds `dw-confession-interrogation-auditor-crim`, `dw-jail-call-analyzer-crim`,
`dw-child-forensic-interview-auditor-crim`, `dw-cross-exam-architect-crim`,
`dw-discovery-compliance-monitor-crim`, and `dw-case-brain-crim`.

**This skill does not produce a DMAR.** If the Defense Media Analysis Report is wanted, run
`dw-dmar-synthesizer-crim` over these transcripts.

### Source Citation Mandate

Every factual claim in the media-integrity report, the master media index, and any speaker-identification finding must trace back to a specific recording, item number, and timestamp (e.g., `(Item 14 — BWC Ofc. Doe, 00:12:41–00:13:05)`), or to the discovery inventory entry it was probed from. Transcripts are machine output that nobody has verified against the recording; the citation is what lets the attorney go check. Never assert a speaker identity, a coverage gap, or a rights-advisement discrepancy without the item + timestamp it was derived from.

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **tiering-and-scope.md** — STEP 0/1: which items get court-reporter vs working-transcript treatment
- **pipeline-setup.md** — STEP 2: on-device ASR + diarization environment setup on firm hardware
- **speaker-identification-protocol.md** — STEP 4: block-level, cross-recording speaker identification rules
- **media-integrity-audit.md** — STEP 5: export-completeness and file-integrity audit procedure
- **cleanup-and-flagging-rules.md** — STEP 7: what may be cleaned in ASR output and what must only be flagged
- **front-matter-spec.md** — STEP 6: front-matter and page:line citation spec for the court-reporter .docx
- **louisiana-audio-conventions.md** — Louisiana-specific conventions (agency names, rights advisement phrasing, juvenile-initials rule)

---

## Non-negotiables

1. No audio leaves attorney hardware.
2. No `initial_prompt`. No name seeding. Ever.
3. No audio processing — no filtering, gain, or normalization.
4. Never correct a rights advisement. Flag, re-decode, report both.
5. Block-level speaker attribution only. Never line-level.
6. Every deliverable states that nothing was human-verified against the recording.
7. Report coverage gaps in minutes, by item, on the first page.
8. Juvenile witnesses by initials in anything leaving the office — La. R.S. 46:1844(W).
