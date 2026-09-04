# MODULE 16: Post-Trial Motions (New Trial · PVJA · Arrest of Judgment)

Read by `dw-pretrial-motion-library-crim` at MODULE 16 before drafting any post-trial motion. This module covers the three post-verdict, pre-sentence filings: Motion for New Trial (La. C.Cr.P. arts. 851-854), Motion for Post-Verdict Judgment of Acquittal (art. 821), and Motion in Arrest of Judgment (arts. 859-861). It also maps how these motions interact with the appeal clock (art. 914).

**Bundled template:** None in this skill. The firm's new-trial exemplar is bundled with `dw-appellate-error-monitor-crim` at `assets/templates/motion_for_new_trial.docx` (see that skill's MODULE E and `dw-appellate-error-monitor-crim/references/07-post-trial-motions.md`); load it through that skill's assets when the attorney selects a bundled template at STEP 1, then port per the STEP 1.5 procedure. The Motion for Appeal and Motion to Reconsider Sentence (art. 881.1) remain the monitor's MODULE E — do not draft those here.

**DEVONthink search:**
```
devonthink:search
query: "new trial" OR "post verdict judgment of acquittal" OR "arrest of judgment"
databaseName: Law Library-Criminal
groupPath: /Motions
limit: 10
```

```
devonthink:search
query: "newly discovered evidence" OR "Art. 851" OR "Art. 821"
databaseName: Law Library-Criminal
groupPath: /Post-Trial
limit: 10
```

---

## Timing Table (verify against current code before filing — renumbering guardrail applies)

| Motion | Deadline | Source |
|--------|----------|--------|
| Motion for New Trial (general) | Must be **filed and disposed of before sentence**; court may postpone sentencing for good cause to allow preparation | Art. 853(A) |
| Motion for New Trial — new evidence (851(B)(3)) | May be filed **within one year after verdict or judgment**, even though sentence has been imposed or a prior new-trial motion was filed; if an appeal is pending, heard only on remand | Art. 853(B) |
| Motion for New Trial — trafficking-victim ground (851(B)(6)) | May be filed **within three years after verdict or judgment**, same post-sentence / remand rules | Art. 853(C) |
| Post-Verdict Judgment of Acquittal | Must be **made and disposed of before sentence** | Art. 821(A) |
| Motion in Arrest of Judgment | Must be **filed and disposed of before sentence**; court may postpone sentencing for cause | Art. 861 |
| Sentencing delay after denial | Sentence shall not be imposed until **at least 24 hours after** a motion for new trial or in arrest of judgment is overruled, unless the defendant expressly waives the delay | Art. 873 |
| Motion for Appeal | No later than **30 days** after the judgment or ruling appealed from, or **30 days from the ruling on an art. 881.1 motion to reconsider sentence** if one is filed | Art. 914(B) |

**Appeal-clock interaction:** Because timely new-trial, PVJA, and arrest-of-judgment motions must be disposed of *before sentence*, their rulings precede sentencing and the art. 914(B)(1) 30-day appeal delay then runs from the sentence/judgment; a timely art. 881.1 motion to reconsider sentence (the monitor's MODULE E) restarts the clock at 30 days from its ruling per art. 914(B)(2). Never sentence-date-compute these chains by hand — route every date through `dw-deadline-engine-crim`, and log each ruling with `dw-appellate-error-monitor-crim` so the preservation record is complete.

---

## 16.1 — Motion for New Trial (Arts. 851-854)

**Form (art. 852):** In writing, stating the grounds, tried contradictorily with the district attorney.

**Foundational rule (art. 851(A)):** The motion is based on the supposition that *injustice has been done the defendant*; unless that is shown, the motion shall be denied no matter the allegations.

**Grounds and standards (art. 851(B)):**

| Ground | Art. 851(B) | Standard / What Must Be Shown | Notes |
|--------|-------------|-------------------------------|-------|
| Verdict contrary to the law and the evidence | (1) | Weight-of-the-evidence review by the trial judge as "thirteenth juror" — distinct from *Jackson v. Virginia* sufficiency (that is the PVJA's job, § 16.2) | Denial on this ground presents nothing for appellate sufficiency review by itself — pair with a PVJA |
| Prejudicial error in a ruling on a written motion or an objection | (2) | The ruling shows prejudicial error | Renews trial objections — pull the enumerated rulings straight from the `dw-trial-day-assistant-crim` Module B objection log |
| New and material evidence | (3) | Four-part showing (below) plus art. 854 sworn allegations | One-year window per art. 853(B) |
| Newly discovered prejudicial error or defect in the proceedings | (4) | Error/defect discovered since verdict that reasonable diligence could not have discovered earlier | |
| Ends of justice | (5) | Court's discretion though defendant has no strict legal right | Ruling on this ground alone is unreviewable on appeal — still plead it |
| Trafficking-victim ground | (6) | Defendant is a victim of human trafficking / trafficking of children for sexual purposes and the offense was a direct result of the trafficking | Three-year window per art. 853(C) |

**Newly-discovered-evidence four-part test:** the defendant must show (1) the evidence was discovered after trial; (2) the failure to discover it earlier was not caused by lack of diligence; (3) the evidence is material to the issues at trial; and (4) it is of such a nature that it would probably have produced a different verdict. *State v. Prudholm*, 446 So.2d 729, 735 (La. 1984); clarified by *State v. Cavalier*, 96-3052 (La. 10/31/97), 701 So.2d 949, 951 (trial court asks whether the new material is fit for a new jury's verdict — it does not weigh the evidence as though it were the jury) `[VERIFY CITATION — confirmed via public databases; Westlaw-check currency and pin cites before filing]`.

**Art. 854 pleading requirements (ground (3) only):** allegations of fact, sworn to by the defendant or counsel, showing (1) reasonable diligence notwithstanding, the evidence was not discovered before or during trial; (2) the names of the witnesses who will testify and a concise statement of the new evidence; (3) the facts the witnesses or evidence will establish; and (4) that the witnesses or evidence are not beyond the court's process or are otherwise available. A witness's newly discovered whereabouts or residence is NOT newly discovered evidence.

---

## 16.2 — Motion for Post-Verdict Judgment of Acquittal (Art. 821)

- **Timing (821(A)):** made and disposed of before sentence.
- **Standard (821(B)):** granted only if the evidence, viewed in the light most favorable to the State, does not reasonably permit a finding of guilty — the *Jackson v. Virginia* sufficiency standard, applied to every essential element per *State v. Mussall*, 523 So.2d 1305, 1310 (La. 1988).
- **Modification option (821(C)):** if the evidence supports only a lesser included responsive offense, the court may modify the verdict and render judgment on the lesser offense in lieu of acquittal. The appellate court has the same power (821(E)).
- **State's remedy (821(D)):** if granted or modified, the State may seek supervisory review or appeal.
- **Strategy:** file the PVJA alongside (not instead of) an art. 851(B)(1) new-trial motion — the PVJA preserves constitutional sufficiency (*Jackson*); the new-trial motion invokes the trial judge's weight-of-the-evidence review. They are different standards with different reviewers; brief them separately.

---

## 16.3 — Motion in Arrest of Judgment (Arts. 859-861)

**Exclusive grounds (art. 859)** — the court shall arrest judgment only on one or more of the following:

1. The indictment is substantially defective, in that an essential averment is omitted;
2. The offense charged is not punishable under a valid statute;
3. The court is without jurisdiction of the case;
4. The tribunal that tried the case did not conform to the requirements of arts. 779, 780, and 782 (wrong jury size / judge-vs-jury composition);
5. The verdict is not responsive to the indictment, or is otherwise so defective that it will not form the basis of a valid judgment;
6. Double jeopardy, if not previously urged;
7. The prosecution was not timely instituted, if not previously urged; or
8. The prosecution was for a capital offense or an offense punishable by life imprisonment but was not instituted by grand jury indictment.

Improper venue may NOT be urged by motion in arrest of judgment. The grounds list is exclusive — a complaint that does not fit one of the eight enumerated grounds belongs in a different vehicle (new trial, PVJA, or appeal).

**Form (art. 860):** in writing, stating the ground, tried contradictorily with the district attorney. **Timing (art. 861):** filed and disposed of before sentence; the court may postpone sentencing for cause to allow preparation.

---

## Module-specific intake

- Verdict date, verdict on each count, and responsive-verdict options given to the jury
- Sentencing date (set or anticipated) — the controlling deadline for all three motions
- The trial-day objection log and issue-spotter flags (`dw-trial-day-assistant-crim` Modules B / G) — the raw material for 851(B)(2)
- Any new evidence: what it is, when and how discovered, why it was undiscoverable with diligence, witness names and availability (art. 854 checklist)
- Sufficiency targets: which essential elements the defense contends the State failed to prove, and the lesser included responsive offenses in play (art. 821(C))
- Charging-instrument defects, jury-composition irregularities (arts. 779-782), double jeopardy, or prescription issues for art. 859 grounds
- Whether an appeal is contemplated — coordinate the 881.1 / 914 sequence with `dw-appellate-error-monitor-crim` MODULE E and compute all dates through `dw-deadline-engine-crim`

## Draft-shell guidance

Per STEP 3 / `references/drafting-and-review.md`: generate a short-form Motion (2-3 pages — procedural history, grounds tracked to the statutory subsections, prayer) plus a Memorandum in Support (argument per ground, with the record citations from the objection log). Caption, signature block, certificate of service, and proposed order per `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md`; filed pleadings get NO work-product marking. When more than one post-trial motion is warranted, file them as separate pleadings (each has its own statutory footing and ruling), and calendar the art. 873 24-hour sentencing delay after any denial.

## Key authority

La. C.Cr.P. arts. 851, 852, 853, 854 (new trial); art. 821 (PVJA); arts. 859, 860, 861 (arrest of judgment); art. 873 (sentencing delay); art. 914 (appeal delays); *Jackson v. Virginia*, 443 U.S. 307 (1979); *State v. Mussall*, 523 So.2d 1305 (La. 1988); *State v. Prudholm*, 446 So.2d 729 (La. 1984) and *State v. Cavalier*, 96-3052 (La. 10/31/97), 701 So.2d 949 `[VERIFY CITATION — confirmed via public databases; Westlaw-check before filing]`.
