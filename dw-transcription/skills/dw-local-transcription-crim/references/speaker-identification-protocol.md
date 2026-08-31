# Speaker Identification Protocol

Turning `SPEAKER_00` into `DET. RANDOLPH`. This is done from the recordings, not from memory.

---

## Why unsupervised clustering alone fails

A first attempt used Resemblyzer d-vector embeddings clustered over Whisper's ASR segments. Best
silhouette across 2–5 clusters was **0.348**, and inspection showed cluster boundaries straddling
speaker turns. It was rejected.

Two distinct causes, worth separating:

1. **Wrong segmentation unit.** Whisper segments are *transcription* units. They routinely span a
   question and the first word of its answer. Clustering them mixes speakers by construction.
   pyannote segments on speech activity instead and handles overlap.
2. **Wrong problem.** Clustering tells you *how many* voices there are and *where* each one speaks.
   It cannot tell you *who they are*. Names come from the recordings' own content.

Use pyannote for (1). Use the anchoring protocol below for (2).

---

## The anchoring protocol

### Step 1 — Find a single-officer anchor

Recorded police interviews open with an announcement:

> "Today's date is August 19th, 2024, it is 6:20 PM with the Lake Charles Police Department, 830
> Enterprise Boulevard … in the room is myself, Detective Randolph. And can you state your name?"

Grep the first 75 seconds of every interview transcript for `in the room is myself` / `this is
Detective` / `my name is`. You are looking for a recording that names **exactly one** officer. Its
dominant diarization cluster is that officer's voiceprint.

### Step 2 — Have the attorney confirm the anchor

**Do not skip this.** It is the only assumption in the chain, and it is a real one: in a police
interview the *witness* usually talks more than the questioner, so "dominant voice = officer" can
invert. Ten seconds of audio settles it.

State the risk plainly when you ask: *"If #38's dominant voice is Robert Davis rather than Randolph,
the whole chain inverts."*

### Step 3 — Propagate by cosine similarity

L2-normalize pyannote speaker embeddings and take the dot product.

| Similarity | Reading |
|---|---|
| **≥ 0.75** | Same speaker |
| 0.50 – 0.75 | Probable — report the number, don't assert |
| **≤ 0.35** | Different speaker |

Observed in practice: same speaker across recordings **+0.860 to +0.913**; different speakers in the
same room **+0.113 to +0.239**. The gap is wide. If everything lands in the middle, something is wrong
with the anchor.

### Step 4 — Solve the rest by elimination

A recording that names exactly two officers, with one already identified, hands you the second.

**Worked example, end to end:**

| Step | Evidence | Result |
|---|---|---|
| Anchor | Item #38 opens naming only "Detective Randolph"; attorney confirms the voice | Randolph voiceprint |
| Propagate | Target interview seg 1 **+0.913**, seg 4 **+0.907**; Item #139 **+0.860** | Randolph placed in three recordings |
| Eliminate | Item #139 opens naming *exactly two* — "Detective Randolph … Detective George Miller" | Remaining officer voice = Miller |
| Confirm | Miller voiceprint vs. target seg 4: **+0.790**, against +0.113 and +0.239 for the other two | **Second examiner = Det. George Miller** |

Also validates itself: the same clustering matched the interviewee across both of his own interviews,
and matched two CAC staff across all three child interviews — exactly the people who should recur.

---

## Ruling out artifacts before claiming a new speaker

A cluster appearing only in one file is suspicious. It might be a person entering the room, or a gain
change at a file boundary. **Measure before deciding.**

Per segment, compute RMS, peak, dBFS, and spectral centroid. If they match, a new cluster is a new
person.

Observed in the worked example:

| Segment | RMS | dBFS | Centroid |
|---|---|---|---|
| seg1 | 0.0879 | −21.12 | 1422 Hz |
| seg2 | 0.0795 | −21.99 | 1396 Hz |
| seg3 | 0.0867 | −21.24 | 1324 Hz |
| seg4 | 0.0861 | −21.30 | 1342 Hz |

Within 0.9 dB and 100 Hz. No gain change. The third voice appearing only in seg4 was therefore a
person, and the content agreed — seg4 opened on a register absent from the previous 54 minutes:
*"This is a broad statement and it is a direct question, but would you have any reason to kill her?"*

A corroborating content shift is not proof, but its **absence** should make you doubt the cluster.

---

## How far to push attribution

**Block level — reliable. Use it.** Merge runs of one speaker, bridging gaps under ~90 seconds, and
emit court-reporter examiner markers:

```
BY DET. MILLER:      00:54:10 – 00:57:47
BY DET. RANDOLPH:    00:58:09 – 01:03:00
```

**Line level — do not.** Whisper word timestamps drift against diarization boundaries; assignment
flips mid-sentence and merges a question with its answer. Word-level mapping was tried and was *worse*
than segment-level. Expect ~15% of lines genuinely uncertain.

Say this in the transcript's designation convention:

> Derived from speaker-embedding analysis at the block level, which is reliable; individual line-level
> attribution within a block was NOT attempted and should not be inferred.

---

## Cross-case reuse

Save speaker embeddings for every diarized interview. Detectives recur across a case and across cases.
Once anchored, the same voiceprint identifies them anywhere in the file automatically — and a
voiceprint library across matters means the anchor step only has to happen once per officer.

Store as `<id>.emb.npy` next to `<id>.turns.json`, ordered by `sorted(annotation.labels())`.
