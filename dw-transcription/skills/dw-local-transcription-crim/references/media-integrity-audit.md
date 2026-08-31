# Media Integrity Audit

Run on every case. This is the highest-yield part of the skill, and it costs almost nothing once the
probe data exists.

The question: **does the media the defense possesses account for the recording that was made?**

Three independent checks. Run all three — they fail in different ways.

---

## Check 1 — Stated runtime vs. media runtime

Recorded interviews announce their start on the record and are closed on the record:

> "Okay, today's date is August 20th, 2024. It is **1:23 p.m.** …"
> "… go ahead and conclude it at **3:03 p.m.**"

That is 100 minutes. Total the media for that item and compare.

Worked example: **1:40:00 announced, 1:03:13 of media.** A 37-minute discrepancy. Recorder pauses
explain some of it — but not that much, and the gap is what justified looking further.

Grep the first and last 90 seconds of every interview transcript for time announcements. Cheap, and it
finds gaps nothing else will.

---

## Check 2 — Native originals vs. produced export

Camera systems write segmented files (`00000.MTS`, `00001.MTS`). A later export carries a different
naming pattern, often with an export timestamp in the filename.

**When both are present, probe both and compare durations.**

Worked example:

| File | Duration |
|---|---|
| `00000.MTS` | 30:19.80 |
| `00001.MTS` | 30:23.79 |
| `00002.MTS` | 30:24.29 |
| **Native originals** | **1:31:07.9** |
| 2026 export (4 files) | 1:03:13.5 |
| **Difference** | **0:27:54.4** |

Three findings fell out, all arithmetic:

1. **Export segment 1 was byte-identical to `00000.MTS`** — same size, same duration to the
   microsecond. The first half hour passed through untouched.
2. **The cut was entirely in the back half.** Export segments 2–4 totalled 32:53.7 against originals
   of 1:00:48.1 for the same span.
3. **The originals accounted for the interview.** 91:08 against 100 minutes announced, leaving 8:52 of
   ordinary recorder pauses across two file boundaries.

So the camera captured it and the export did not. Demand the natives, and the provenance of the export
— who made it, when, with what tool, on what selection criteria.

**Container metadata reads succeed on files whose payload cannot be retrieved**, because ffprobe needs
only headers and trailers. That is how these durations were obtained from files that would not open.

---

## Check 3 — Probed duration vs. extracted audio duration

The batch records both. Anything where extracted < 90% of probed is flagged automatically.

### The 8 MB ceiling

Files that yield **exactly 8,388,608 bytes** and then fail with `Operation timed out` are a **Google
Drive retrieval fault**, not corruption:

- Identical byte boundary across unrelated files and folders. Real truncation is not that tidy.
- `stat` reports full size — Drive knows what it should serve.
- `cp`, `dd`, and ffmpeg all fail at the same offset. Not a tool problem.
- At AVCHD bitrates 8 MB is ~7 seconds, so a 30-minute file transcribes as 7 seconds of audio.

`moov atom not found` on MP4 is the same fault wearing a different hat — the index sits at the end of
the file and the tail never arrived.

Worked example: **7.6 hours across seven evidence items**, including both jailhouse-informant
interviews, a threat witness, and both interviews of the co-defendant.

**Remedy, in order:** "Available offline" in Finder, which uses Drive's own retry queue rather than
the on-demand read path; then a browser download from drive.google.com; then, if the bytes still will
not come, **the defense does not possess that evidence** and that is a written demand, not an IT
ticket.

### Also correct the case inventory

The same probe corrects the record in both directions. In the worked example three items the Case
Brain listed as **empty folders** — the CAC juvenile interviews — held 82, 65 and 20 minutes of audio
that transcribed successfully. Another item listed as empty held a real file Drive would not serve.

Reconcile the probe against the case's own media inventory every time. Both kinds of error are common
and both change what the attorney does next.

---

## Reporting

Per item: files, probed runtime, extracted runtime, count truncated, coverage status
(`COMPLETE` / `PARTIAL n%` / `NO AUDIO RECOVERED`). Zero-audio items in bold.

Then, in prose:

1. **Total unrecoverable audio in hours**, and which items.
2. **Which of those items matter** — name the witness and why. "Twenty minutes missing" lands
   differently as "the twenty-minute interview of the informant who admits eavesdropping on the
   client's call with his attorney."
3. **Whether you can distinguish retrieval failure from production failure.** From a workstation you
   usually cannot, and saying so is the honest answer. Give the evidence either way — a uniform 8 MB
   boundary points hard at retrieval; a clean 28-minute excision from the back half of an export
   points hard at production.
4. **The next physical step**, not a conclusion. "Available offline, then re-run."

Put the gap on the first page of every affected transcript. A coverage warning in an appendix is a
coverage warning nobody reads.
