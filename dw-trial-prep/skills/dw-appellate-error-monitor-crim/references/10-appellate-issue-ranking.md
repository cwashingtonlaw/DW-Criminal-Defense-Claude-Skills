# MODULE H — Appellate Issue Ranking (Reference)

This module synthesizes the findings from all prior modules into a ranked list of appellate issues, organized by likelihood of success. **The ranked-issue output produced by this module is consumed by `dw-appellate-brief-builder-crim`.** Preserve the schema below.

## Issue Ranking Tiers

**Tier 1 -- Strongest Issues (Recommend Lead Assignments of Error):**
Issues with the highest likelihood of reversal. These should be the lead assignments of error in the appellate brief.

Criteria:

- Error is clearly preserved (Module A -- green status)
- Error is structural (automatic reversal) OR error is constitutional with strong prejudice showing
- Error relates to a central, disputed issue at trial
- Existing jurisprudence supports reversal on similar facts

**Tier 2 -- Strong Supporting Issues:**
Issues with a reasonable likelihood of success. These should be included in the appellate brief as supporting assignments of error.

Criteria:

- Error is preserved
- Error is subject to harmless error analysis but the harmless error argument is weak for the State
- Error relates to an important (but not necessarily central) issue
- Some jurisprudential support exists

**Tier 3 -- Preservation Issues (Raise to Preserve):**
Issues that are unlikely to result in reversal on direct appeal but should be raised to preserve them for post-conviction or federal habeas review.

Criteria:

- Error is preserved but harmless error analysis likely favors the State
- Error raises novel legal questions without clear jurisprudential support
- Error may gain traction in future jurisprudential developments
- Raising the issue preserves it for federal habeas review (exhaustion requirement under 28 U.S.C. Sec. 2254)

**Tier 4 -- Errors Patent Only:**
Issues identified through the errors patent review (Module D) that are reviewable without objection. These do not require an assignment of error but should be flagged for the appellate court's independent review.

**Tier 5 -- Waived Issues (IAC Salvage Only):**
Issues identified as waived (Module B missed objections) that can only be raised through ineffective assistance of counsel claims in post-conviction proceedings (Module G).

## Appellate Issue Ranking Table

| Rank | Issue | Module Source | Preservation Status | Error Type | Harmless Error Risk | Reversal Likelihood | Tier |
|------|-------|--------------|-------------------|-----------|-------------------|-------------------|------|
| 1 | [Description] | [A/B/C/D/E/F/G] | [Preserved/Waived/Patent] | [Structural/Constitutional/Non-constitutional] | [N/A/High/Moderate/Low] | [HIGH/MODERATE/LOW] | [1-5] |

## Special Issue Categories

**Sufficiency of the Evidence -- *Jackson v. Virginia*, 443 U.S. 307 (1979):**
Sufficiency of the evidence is always reviewable on appeal when raised. The standard: viewing the evidence in the light most favorable to the prosecution, any rational trier of fact could have found the essential elements of the crime beyond a reasonable doubt.

- Sufficiency challenges do not require a contemporaneous objection at trial
- They do require an assignment of error on appeal
- Sufficiency challenges are rarely successful but should be raised in appropriate cases (weak identification, circumstantial evidence, missing element)

**Excessive Sentence -- La. Const. Art. I, Sec. 20:**
An excessive sentence claim requires a motion to reconsider sentence under Art. 881.1 as a prerequisite. If the motion was filed, the issue is preserved. If the motion was not filed, the issue is waived (unless the sentence is illegal -- errors patent).

Standard: A sentence is constitutionally excessive if it is grossly out of proportion to the severity of the crime or is nothing more than the purposeless and needless imposition of pain and suffering. *State v. Bonanno*, 384 So.2d 355 (La. 1980).


---

## Module H Summary — Tiers, Table Fields, Special Categories (moved verbatim from SKILL.md MODULE H)

Five tiers:
- **Tier 1 — Strongest Issues:** lead assignments of error; preserved (Module A green); structural OR constitutional with strong prejudice; central disputed issue; jurisprudence supports reversal
- **Tier 2 — Strong Supporting Issues:** preserved; subject to harmless error but State's argument is weak; important issue; some jurisprudential support
- **Tier 3 — Preservation Issues:** preserved but harmless-error analysis likely favors State; novel questions; raise to preserve for post-conviction or federal habeas (28 U.S.C. § 2254 exhaustion)
- **Tier 4 — Errors Patent Only:** identified through Module D; reviewable without objection; flag for appellate court's independent review
- **Tier 5 — Waived Issues (IAC Salvage Only):** Module B missed objections raisable only through IAC in post-conviction (Module G)

Ranking table fields: Rank, Issue, Module Source (A/B/C/D/E/F/G), Preservation Status (Preserved/Waived/Patent), Error Type (Structural/Constitutional/Non-constitutional), Harmless Error Risk (N/A/High/Moderate/Low), Reversal Likelihood (HIGH/MODERATE/LOW), Tier (1-5).

Special issue categories: **Sufficiency of the Evidence** (*Jackson v. Virginia*, 443 U.S. 307 (1979)) — reviewable when raised, no contemporaneous objection required; **Excessive Sentence** (La. Const. Art. I, Sec. 20; *State v. Bonanno*, 384 So.2d 355 (La. 1980)) — Art. 881.1 motion is the prerequisite.
