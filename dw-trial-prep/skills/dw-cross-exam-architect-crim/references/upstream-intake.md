# Upstream Intake — What to Load Before Drafting

**Applied at Step 0.58. The firm's other skills have already done much of this work. Not loading their output means re-deriving it by hand, worse, and inconsistently.**

`dw-data-contracts-crim` names `dw-cross-exam-architect-crim` as a **consumer** of the DMAR contract and the Auditor Report contract. This file implements that consumption. Check for each input below before drafting; load what exists; note what is missing.

---

## 1. Intake Checklist

Run in this order. Each row says where it comes from, what to pull, and what to do if it is absent.

| # | Input | Producer skill | What to pull | If absent |
|---|---|---|---|---|
| 1 | **Witness Analysis Card** | `dw-witness-statement-analyzer-crim` | Key facts, internal inconsistencies, vagueness flags, credibility indicators, defense utility | Recommend running it first |
| 2 | **Defense Media Analysis Report (DMAR)** | `dw-transcript-pipeline-calcasieu-crim` (JusticeText) / `dw-transcript-pipeline-rev-crim` (Rev) | §9 Cross-Examination Seeds; §10 Report-vs-Recording Matrix; §4 Inconsistency Matrix; §7 Key Event Timeline | Recommend `dw-transcript-router-crim` if media discovery exists and is untranscribed |
| 3 | **Auditor Reports** | `dw-crime-lab-auditor-crim`, `dw-mobile-forensic-auditor-crim`, `dw-video-evidence-auditor-crim`, `dw-chain-of-custody-auditor-crim`, `dw-eyewitness-identification-auditor-crim`, `dw-confession-interrogation-auditor-crim`, and the other `dw-evidence-audit` skills | §6 Key Findings for Cross-Examination — each carries a finding, a source reference, and a suggested line of questioning | Recommend the auditor matching the evidence type |
| 4 | **Brady/Giglio audit** | `dw-brady-giglio-auditor-crim` | Disclosure gaps, cooperator benefits, officer credibility material | **Mandatory** before any cooperating-witness or officer-credibility cross |
| 5 | **Prior sworn testimony** | See §3 below | Every prior sworn statement by this witness in this case | Flag in Discovery Gap Report |
| 6 | **Prior cross history** | See `witness-history-lookup.md` | Whether the firm has crossed this witness before | Note as unchecked |
| 7 | **Case theory** | `dw-theory-deconstructor-crim`, `dw-trial-narrative-builder-crim` | The case theme that becomes the chapter spine | Ask the attorney (Step 1, essential item 3) |
| 7b | **Theory stress test** | `dw-adversarial-stress-test-crim` | Identified theory vulnerabilities and the State's best rebuttal — the cross must not open a door the theory cannot survive. Check each chapter against these at Step 8.5 | Skip; note that the outline is untested against the theory |
| 8 | **Consolidated DMAR** | `dw-dmar-synthesizer-crim` | Cross-case witness comparison — only when co-defendants, joined cases, or overlapping witnesses exist | Skip unless multi-case |

**Report what you loaded.** In the Step 2 Pre-Draft Confirmation, list which inputs were found and which were absent. The attorney needs to know whether the outline rests on analyzed evidence or on raw documents.

---

## 2. Mapping DMAR Output Into Chapters

The DMAR is the richest single input and maps almost directly onto the outline.

**§10 Report-vs-Recording Matrix (Barone 6-Category)** is built for cross. Each category maps to a chapter type:

| DMAR category | Chapter it feeds | Cross angle |
|---|---|---|
| 1. Narrative Match | Inconsistencies chapter | Direct contradiction — report vs. what the recording shows |
| 2. Omissions | Omissions chapter | What the officer chose not to document; establish the duty first, then the absence |
| 3. Additions | Inconsistencies chapter | Facts in the report that the recording does not support |
| 4. Timing Discrepancies | Scene/report conditions, or a Miranda-delay chapter | Timeline manipulation can conceal a constitutional violation |
| 5. Quote Accuracy | Prior inconsistent statements chapter | Especially critical where a confession is paraphrased |
| 6. Procedural Compliance | SOP violations chapter | Procedures claimed in the report that the recording contradicts |

Each matrix entry already carries a report citation (document, page, paragraph), a recording citation (file, timestamp range), and a severity rating (CRITICAL / SIGNIFICANT / MINOR). **Use the severity to drive chapter order** — CRITICAL findings belong in the chapters you are certain to reach.

**§9 Cross-Examination Seeds** are pre-identified contradictions with source references. Convert each seed into a short-question sequence rather than a single question. A seed is a destination; the sequence is the route.

**Source Register rule:** every DMAR-derived citation must still be entered in the Source Register and carry its `(N)` prefix. Cite the underlying document and recording, not the DMAR itself — the DMAR is analysis, not evidence, and is not something you can put in front of a witness.

---

## 3. Prior Sworn Testimony — The Highest-Value Vein

**Prior sworn testimony in this same case is usually the strongest impeachment material available**, because the witness testified under oath before the defense knew enough to test the account, and before the State had finished shaping it.

### Sources to check, in order of value

1. **Motion to suppress hearing transcript** — the officer's most detailed sworn account of the stop, search, or statement, given early. La. C.Cr.P. art. 703 hearings often produce testimony that later conflicts with trial testimony once the defense theory is known.
2. **Preliminary examination transcript**
3. **Grand jury testimony**, where available and disclosed
4. **Bond or detention hearing testimony**
5. **Prior trial testimony** — mistrial, severed co-defendant, or retrial
6. **Testimony in a related civil matter** — protective order proceedings, a §1983 suit against the officer, a custody case
7. **Deposition** — rare in Louisiana criminal practice; only where testimony was actually perpetuated

### Getting transcripts

If a hearing occurred and no transcript is in the file, that is a Discovery Gap Report item **and** an action item — order it. A hearing transcript that arrives the week of trial is worth less than one that arrives during outline drafting.

For recorded proceedings not yet transcribed, route through **`dw-transcript-router-crim`**: Calcasieu cases go to the JusticeText pipeline, all other parishes to Rev. Both produce a DMAR whose §4 Inconsistency Matrix will do part of the comparison work automatically.

### Working the transcript

- Extract every assertion the witness made under oath, with page and line.
- Compare against: the report, the recording, later statements, and the expected trial testimony.
- Cite in the standard format: `(N) Suppression Hearing Transcript, p. 34, ll. 5-18`.
- Prior **sworn** inconsistency is materially stronger than an unsworn one — the witness swore to it. Say so in the Step 5 report so the attorney can make that point to the jury.
- **La. C.E. art. 613:** foundation is required before offering **extrinsic** proof of the statement — fairly direct the witness to it and give an opportunity to admit. It is **not** required before simply asking. Do not telegraph.

### The transcript-availability trap

If the witness testified at a hearing and the defense never ordered the transcript, the impeachment does not exist in usable form no matter how good the memory of it is. Flag any hearing testimony with no transcript as:

`[TRANSCRIPT NOT IN FILE — impeachment unusable until ordered; ACTION REQUIRED]`
