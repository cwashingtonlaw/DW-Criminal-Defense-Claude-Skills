# House Style

Letterhead, captions, address blocks, signatures, and boilerplate strings the skill must render consistently. This file is jurisdiction-agnostic; firm-specific values are filled in from the `firm-info` cache on first run.

---

## 1. Firm Letterhead

Centered at the top of page 1 of every output. Single-spaced. Slightly larger font (typically 14pt for the firm name, 11pt for the rest).

```
[FIRM NAME, LLC]
ATTORNEYS at LAW
[Street Address]
[City], [ST] [Zip]
Tel: ([###])[###]-[####]  [Attorney 1 Name]
Tel: ([###])[###]-[####]  [Attorney 2 Name]
Fax: ([###])[###]-[####]
```

If the firm has a logo and the attorney prefers it on the letterhead, place it centered above the firm name and adjust spacing.

---

## 2. Date Line

Format: `Full Month Day, Year` — e.g., `July 30, 2025`.

Two blank lines below the letterhead. Left-aligned.

---

## 3. Addressee Block(s)

Format:
```
[Name], [Esq. / J.D. / title]
[Firm / Organization Name]
[Street Address]
[City], [ST] [Zip]
Ph: ([###])[###]-[####]
Fax: ([###])[###]-[####]
Email: [address]
```

### Single addressee (most demand letters)
One block left-aligned below the date.

### Dual addressee (mediation papers, or demands cc'd to a mediator)
Two side-by-side blocks (use a 2-column table with invisible borders) — or stacked, with a `cc:` line.

### Ordering rules
- `mode = demand` → defense counsel first; mediator (if any) second or in a `cc:` line at the end
- `mode = mediation_paper` → mediator first; defense counsel second

### Adjuster vs. defense counsel
Pre-suit demands go to the claims adjuster; post-suit demands and mediation papers go to defense counsel. For pre-suit, the addressee block uses the adjuster's name, the carrier name, and the claim number.

---

## 4. RE: Caption Block

Two blank lines below the addressee block(s). Bold the `RE:` label.

**Pre-suit demand (no docket):**
```
RE:   Our Client:    [Plaintiff Name]
      Your Insured:  [Defendant Name]
      Date of Loss:  [MM/DD/YYYY]
      Claim No.:     [####]
      Our File No.:  [####]
```

**Post-suit demand or mediation paper:**
```
RE:   [Plaintiff Name] v. [Defendant Name] et al
      Case No. [####], Div. [Letter]
      [##] JDC, [Parish] Parish (or USDC, [W/E/M]DLA, [Division] Division)
      Our File No.:  [####]
      [PDDS / MAPS / etc.] Matter No.: [####]
```

**Mediation paper add-ons** (when known):
```
      MEDIATION DATE:   [MM/DD/YYYY]
      TIME:             [##:## AM/PM]
      LOCATION:         [in-person address OR "Zoom — link forthcoming"]
```

---

## 5. Confidentiality Marking (mediation papers only — optional)

Some mediators expect or appreciate this. If marked, place it bold and centered above the document-type banner:
```
PERSONAL AND CONFIDENTIAL
MEDIATION CONFIDENTIAL — La. R.S. 9:4112 et seq.
```

---

## 6. Document-Type Banner

Bold, ALL CAPS, centered, on its own line. Two blank lines below the RE block. One blank line below the banner.

Choose from:
- `SETTLEMENT DEMAND LETTER`
- `SETTLEMENT OFFER`
- `MEDIATION POSITION PAPER`

---

## 7. Salutation (optional)

Some demand letters skip the salutation and go straight from the banner to the body. If used, format:
- Defense counsel: `Dear [Mr./Ms.] [Last Name]:`
- Adjuster: `Dear [Mr./Ms.] [Last Name]:`
- Mediator: `Dear Mr./Ms./[Honorific] [Last Name]:` (use "Honorable" for retired judge mediators)

Skip the salutation entirely for `mediation_paper` mode — the banner takes its place.

---

## 8. Section-Label Conventions

The skill picks ONE labeling system per document and uses it throughout.

### Letter style — `mode = demand`
```
A. FACTS
B. MEDICAL TREATMENT
   a. Injuries
   b. Treatment
   c. Impact on ADLs
C. SPECIAL DAMAGES
D. GENERAL DAMAGES
   1. SOFT TISSUE
   2. CERVICAL AND LUMBAR
   3. TRAUMATIC BRAIN INJURY
E. JUDICIAL INTEREST
F. DEMAND
```

### Roman-numeral style — `mode = mediation_paper`
```
I.   INTRODUCTION
II.  LIABILITY
     A. FACTS
     B. LAW
III. DAMAGES
     1. TREATMENT
     2. PERMANENCY
     3. PAST AND FUTURE ECONOMIC LOSS
     4. LIFE EXPECTANCY
IV.  JURY VERDICT RESEARCH AND/OR SETTLEMENT DEMAND
V.   JUDICIAL INTEREST
VI.  DEMAND
```

### "Section #:" style — `mode = hybrid`
```
Section 1: Liability
Section 2: Summary of Injuries
Section 3: Special Damages
Section 4: General Damages
Section 5: Judicial Interest
Section 6: Conclusion / Demand
```

### Formatting
- Top-level section labels: bold, ALL CAPS, 14pt, left-aligned
- Sub-headings (A./B./C. or 1./2./3.): bold, Title Case or ALL CAPS, 12pt, left-aligned, indented 0.25" from the body margin
- One blank line above each section label; no blank line between the label and the first paragraph of that section

---

## 9. Signature Block

Format:
```
Sincerely,



[handwritten signature image — if available]

[ATTORNEY NAME, ALL CAPS]
```

Three blank lines between the comma-after-Sincerely and the typed name to leave room for the handwritten signature. If a signature image is on file, insert it inline; otherwise leave the gap for manual signing.

The firm letterhead already has the address, phone, and email — so no contact info is repeated below the signature. Bar number is included only if firm convention requires it; otherwise omit.

---

## 10. PS Line (optional)

Below the signature block, on its own line, left-aligned, italic (or plain — firm preference):

- Demand letter going to a mediation: `PS: Please note that plaintiff is agreeable to trying to mediate this matter in good faith.`
- Pre-suit demand: `PS: Please let me know if you are in need of any of the records referenced herein.`

---

## 11. Attachment List (optional)

If exhibits are attached, list them at the end of the document with sequential numbers:

```
Attachments:
   Exhibit 1 — Medical Chronology
   Exhibit 2 — Medical Expense Worksheet
   Exhibit 3 — Police/Crash Report (LSP Report No. ####)
   Exhibit 4 — Scene Photographs (4 images)
   Exhibit 5 — Deposition of [Defendant Name], [Date]
   Exhibit 6 — W-2 history of [Plaintiff Name] (Tax Years [Y1]–[Y6])
   Exhibit 7 — [Surgeon] Operative Report dated [Date]
   ...
```

Every exhibit cited in the text body must appear in this list, and the exhibit number in the body must match the number in the list.

---

## 12. Recurring Boilerplate Strings (verbatim)

These are tested phrasings — render them exactly.

**Sole-fault statement** (liability closing):
> Based on information and belief, the defendant, [DEFENDANT NAME], was solely responsible for causing the wreck/accident giving rise to this [suit/claim]. Based on information and belief, the defendant, [DEFENDANT NAME], has no good faith legal or factual basis for alleging fault or comparative fault on behalf of the plaintiff.

**Special damages opening:**
> Enclosed is the medical expense worksheet detailing the past medical bills incurred secondary to [Client]'s treatment necessitated by the subject [crash/collision/incident]. The total amount for [Client]'s past medical expenses is $[X].

**General damages lead-in:**
> A review of Louisiana law shows that similarly situated persons to [Client] have recovered the following amounts:

**General damages closing (per bucket):**
> Considering the foregoing case[s], as well as the injuries and treatment received and needed by [Client], a compromise of $[X] would adequately compensate [Client] for [body region] injur[y/ies] (past and future).

**Demand closing (single-step):**
> In the interest of seeking an amicable resolution to this matter we will resolve [Client]'s case today for a total of $[X] inclusive of all costs and fees.

**Demand closing (two-step — mediation papers):**
> If [Client] is forced to trial in this matter, we would seek a judgment of $[TRIAL ANCHOR]. Nevertheless, in the interest of seeking an amicable resolution to this matter we will resolve [Client]'s case today for a total of $[TODAY NUMBER] inclusive of all costs and fees.

**Response deadline:**
> **PLEASE RESPOND WITHIN [15/30] DAYS INDICATING YOUR ACCEPTANCE, REJECTION, OR COUNTER OF THIS REASONABLE SETTLEMENT COMPROMISE.**

**Per-se negligence closer (LAW subsection):**
> [Defendant]'s violation of [statute] constitutes negligence per se under Louisiana law. There is no factual or legal basis for any allocation of comparative fault to [Plaintiff].

**Policy-limits posture statement (when applicable):**
> The defendants ignored the opportunity to resolve this claim for the policy limits in [date]. We will never agree to resolve this claim for the policy limits. If the defendants are not prepared to resolve this claim for significantly more than the policy limits there is no need to attempt mediation.

---

## 13. Plaintiff-Name Rendering

Pick a convention once per document and apply it consistently:

| Section | Firm corpus convention | Alternative |
|---------|------------------------|-------------|
| RE: caption | **ALL CAPS** (STACY BOUDREAUX v. STATE FARM) — verified in Boudreaux 2016, Antoine 2017, Monroe 2023 | Title Case — used in some newer drafts but not the historical default |
| FACTS section first mention | ALL CAPS on first mention ("On [date], STACY BOUDREAUX was..."), then Title Case ("Mr. Boudreaux") thereafter | Title Case throughout — when the attorney prefers a less-formal register |
| Subsequent references | "Mr./Mrs./Ms. [Last Name]" — based on attorney preference and plaintiff age | "[First Name]" — only for child plaintiffs |
| Pronouns | Consistent he/him/his or she/her/hers throughout, **matched to the plaintiff's gender** | They/them if attorney specifies |
| Damages buckets | Always full reference style | — |

Never mix conventions within the same document.

---

## 14. Currency Formatting

- Always use `$1,000,000.00` style — comma thousand-separators, two-decimal cents.
- For round-thousand amounts, drop the cents only if the attorney prefers; default is two-decimal.
- Never use shorthand like "$1M" or "$1.5K" in a formal demand.
- Render judicial-interest math with at least two decimals throughout to keep the table arithmetic checkable.

---

## 15. Common Typo Allowlist (always auto-fix)

| Wrong | Right |
|-------|-------|
| Priarieville | Prairieville |
| Sherriff's | Sheriff's |
| INJUIES | INJURIES |
| the crashed | the crash |
| 11/02/05 (in case cite when it should be a year) | 2005 (or correct year) |
| Cir 11/02/05 | La. App. 3 Cir. 2005 (or correct circuit/year from the cite) |
| "Mrs." vs "Ms." inconsistency | Pick one per plaintiff and stay consistent |
| "judgement" | "judgment" |
| "alot" | "a lot" |
| Trailing double spaces | Single space |

The skill should run a silent find-and-replace pass for the firm-history typos before output.
