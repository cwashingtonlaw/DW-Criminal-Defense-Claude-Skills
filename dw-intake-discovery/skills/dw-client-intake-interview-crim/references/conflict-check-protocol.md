# Conflict Check Protocol

The single most important sequencing rule in client intake: **conflict check before privileged narrative.** This reference operationalizes Module A of the SKILL.

---

## Why Conflict Check Comes First

Three Louisiana Rules of Professional Conduct converge on intake:

- **Rule 1.7** — Conflict of Interest: Current Clients. Concurrent representation that creates a conflict requires informed consent (writing) where waivable; cannot proceed at all where not waivable.
- **Rule 1.9** — Duties to Former Clients. The firm cannot represent a new client adverse to a former client on the same or substantially related matter without informed consent (writing) of the former client.
- **Rule 1.18** — Duties to Prospective Clients. **Even if no engagement results**, the firm owes the prospective client confidentiality of information learned during the consultation. That confidentiality can in turn disqualify the firm from representing other clients on related matters where the information was significantly harmful.

The practical consequence: **the firm can disqualify itself by listening too long.** If a prospective client tells the firm substantively privileged information about a matter on which the firm represents the alleged victim, a co-defendant, or a key witness, the firm may be foreclosed both from representing the prospective client AND from continuing in the existing representation. The way to avoid the problem is to gate the conversation:

1. Identifying information first (names of all parties)
2. Run the screen
3. Substantive information only after the screen clears

---

## The Staged-Disclosure Sequence

### Stage 1 — Gateway questions only (pre-screen)

The intake attorney (or Cowork in a phone-intake context) asks ONLY:

- Client's full name and any aliases
- The general charge category and approximate date of incident
- Names of alleged victim(s) / complainant(s) — full names if known, partial if not
- Names of any co-defendants — full names if known
- Names of any specific witnesses already identified by police or by the client
- The investigating agency (so we know the case is not one the firm has already touched on the prosecution side, which is irrelevant for a private defense firm but relevant to the analysis when one of our former clients is the named officer or informant)
- The arresting officer's name if known

The attorney explicitly tells the client:

> *"Before we talk about what happened, I need to make sure our office can represent you. Hold the story for now — I just need names. Once I check our system, I'll come back and want to hear the whole thing."*

If the client begins narrating, redirect immediately. Do not let the narrative proceed.

### Stage 2 — Run the screen

The attorney (not Cowork) runs the firm's conflict-check database against every name captured in Stage 1. The database query includes:

- **Current matters** — does any current client of the firm appear on the list as adverse, witness, or co-defendant?
- **Closed matters** — has the firm represented any person on the list previously?
- **Adverse-party history** — has the firm previously been adverse to any person on the list?
- **Personnel-of-record** — has any person on the list been an officer-witness, expert, investigator, or interpreter the firm has worked with on related matters?
- **Family relationships** — does any person on the list have a known family relationship to a current or former client?

For each query result, the attorney assigns one of:

- **CLEAR** — no current or former representation; no ethical bar
- **POTENTIAL CONFLICT — WAIVABLE** — a Rule 1.7 or 1.9 issue exists but may be waived by the affected client(s) with informed written consent
- **CONFLICT — NOT WAIVABLE** — the conflict is non-consentable (e.g., directly adverse current clients in the same matter)
- **RULE 1.18 STATUS** — even if the firm declines, prospective-client duty applies; documents must be segregated from any related representation

### Stage 3 — Document the screen

The Conflict Check Record (saved in `00 - Client File/01 - Intake/`) captures, at minimum:

```
CONFLICT CHECK RECORD
Prospective Client:    [Name]
Date of Intake:        [YYYY-MM-DD HH:MM]
Screening Attorney:    [Name]

Names Screened:
  Client:              [Name and aliases]
  Alleged Victim(s):   [Names]
  Co-Defendants:       [Names]
  Identified Witnesses:[Names]
  Officers/Agents:     [Names]
  Other:               [Names]

Database Queried:      [Firm conflict database — name and version]
Date of Query:         [YYYY-MM-DD]
Query Result:          [CLEAR / POTENTIAL CONFLICT — WAIVABLE / CONFLICT — NOT WAIVABLE]

If Conflict Identified:
  Nature of Conflict:  [Rule 1.7 current adverse / Rule 1.9 former client same-or-substantially-related /
                       Rule 1.8(f) third-party payor / other]
  Waiver Required From:[Client(s) whose consent is required]
  Waiver Status:       [Pending / Obtained / Refused / Not Sought]

Decision:
  [   ] Proceed with representation (clear)
  [   ] Proceed with representation subject to waivers (waivers attached)
  [   ] Decline — document Rule 1.18 segregation
  [   ] Defer pending further investigation

Screening Attorney Signature: ________________ Date: __________
```

The Conflict Check Record is signed before any privileged narrative is invited. If the screen is positive (conflict potentially identified), the substantive interview is paused while the conflict is resolved.

### Stage 4 — Privileged narrative (only after clearance)

Only after the screen is documented as CLEAR or as cleared-with-waiver does the attorney invite the open narrative under Module C of the SKILL. The intake memo records the timing:

```
Conflict Check completed:    [YYYY-MM-DD HH:MM]
Privileged Narrative began:  [YYYY-MM-DD HH:MM]
```

This timing record is the firm's defense if a Rule 1.18 issue is raised later.

---

## Specific Conflict Scenarios in Criminal Defense

### Co-defendant representation

The firm cannot represent two defendants in the same criminal matter except in the rarest of circumstances. The interests of co-defendants in criminal cases routinely diverge — one may want to plead and cooperate; the other may want to go to trial; one may want to point at the other; severance arguments differ; sentencing exposure differs. Joint representation creates a non-waivable conflict in nearly every criminal case. Default rule: **decline joint representation of co-defendants.**

If the prospective client identifies a co-defendant the firm already represents:

- The firm cannot ethically take the new representation as long as the existing one continues
- Refer the new prospective client out (Rule 1.16, Rule 1.18 segregation)
- Document the decline in the Conflict Check Record

### Former representation of the alleged victim

If the firm has previously represented the alleged victim/complainant on any matter, run the Rule 1.9 analysis:

- Was the prior matter the same matter? — Disqualified absent informed consent.
- Was the prior matter substantially related? — Disqualified absent informed consent.
- Did the firm acquire information protected by Rule 1.6/1.9 that would be material to the new representation? — Disqualified absent informed consent.

In nearly all criminal defense scenarios, prior representation of the alleged victim disqualifies the firm from representing the defendant against that victim. The disqualification is generally not waivable in the typical adverse-victim context.

### Former representation of a witness

If a key state witness is or was a firm client:

- Was the prior matter substantially related? — Likely disqualifying.
- Would defending the new matter require cross-examining the former client on confidential information? — Disqualifying.
- Is the former representation closed and unrelated? — May proceed with screening or limited disclosure; attorney decides.

The attorney determines whether limited disclosure or screening is appropriate.

### Former representation of an officer-witness

If the named arresting or investigating officer is a current or former firm client (e.g., the firm previously represented the officer in a personal matter — divorce, DWI, civil suit), the analysis depends on whether cross-examining the officer would require using protected information. Often a screening solution is workable; sometimes not.

### Third-party payor (Rule 1.8(f))

When a family member, friend, or other third party pays the legal fee:

- The third party does not become the client
- The lawyer's duties run to the actual client (the defendant)
- The third party does not direct strategy and does not get briefings unless the client expressly authorizes
- Rule 1.8(f) requires informed consent from the client (in writing) to the arrangement
- The engagement letter must include the third-party payor disclosure (see `engagement-scope-templates.md`)

This is a waivable conflict — but it must be papered.

### Imputed firm conflicts (Rule 1.10)

A conflict held by one lawyer in the firm is generally imputed to all lawyers in the firm. Screening of an individually conflicted lawyer is permitted in some narrow circumstances; the firm's ethics counsel signs off before any screen is implemented. Cowork flags imputed-conflict scenarios for attorney review and does not unilaterally clear them.

### Prospective-client conflicts (Rule 1.18)

Rule 1.18(c) provides that a lawyer who has had discussions with a prospective client shall not represent another client with materially adverse interests in the same or substantially related matter if the lawyer received information from the prospective client that could be significantly harmful to that person. The duty under Rule 1.18 applies even where the firm declines.

The protective steps:

1. Limit the disclosure during the consultation to what is necessary to determine whether to take the representation (see Stage 1 above)
2. If the firm declines, segregate the intake notes from any related representation; mark the file `DECLINED — Rule 1.18 protection in force`
3. If a related matter later arises, ethics counsel reviews whether the prior consultation forecloses the new matter
4. Where appropriate, obtain Rule 1.18(d) screening — informed consent of both the prospective client and the affected client

---

## Database Query Mechanics

The firm's conflict database (whatever its specific software) should be queried on at least the following fields:

- Last name (with phonetic variants)
- First name
- Full DOB if available
- Last 4 SSN if available
- Last known address
- Aliases / former names

Run the query before any privileged narrative. Save the query log (timestamps, names searched, query operator) to the Conflict Check Record. Cowork captures the query parameters; the attorney runs the query and certifies the result.

If the firm has not yet implemented a digital conflict database, the attorney runs a manual file-by-file check covering at minimum the past 5 years of representations. This is slower but no less mandatory.

---

## Written Waiver Templates

When a conflict is waivable, the waiver is in writing, signed by every affected client (or former client), and filed in `00 - Client File/01 - Intake/`.

### Template — Rule 1.7 current-client waiver

```
WAIVER OF CONFLICT — RULE 1.7

I, [Affected Client Name], am a current client of Daniels & Washington
in connection with [matter description]. I have been advised that the
firm proposes to represent [New Client Name] in connection with
[new matter description]. I have been advised:

1. That this representation may create a concurrent conflict of
   interest under La. Rule of Professional Conduct 1.7;

2. Of the specific nature of the potential conflict, including
   [specific description];

3. Of the implications for my representation, including the possibility
   that the firm may be required to withdraw from representing me if
   the conflict materializes;

4. Of reasonably available alternatives, including retention of separate
   counsel for one or both representations;

5. That I have had the opportunity to consult with independent counsel
   before signing this waiver, and I have either done so or knowingly
   waived that opportunity.

After reflecting on these advisements, I consent to the firm's
representation of [New Client Name].

___________________________________     ____________________
[Affected Client Name]                  Date

Independent counsel consulted (if any): _______________________
```

### Template — Rule 1.9 former-client waiver

```
WAIVER OF CONFLICT — RULE 1.9

I, [Former Client Name], was previously represented by Daniels &
Washington in connection with [prior matter description], which
concluded on [approximate date]. I have been advised that the firm
proposes to represent [New Client Name] in connection with
[new matter description].

I have been advised:

1. That the new matter is or may be substantially related to my prior
   representation under La. Rule of Professional Conduct 1.9;

2. Of the specific information from my prior representation that is or
   may be material to the new matter, to the extent disclosure of that
   description does not itself violate the duty owed to me;

3. Of reasonably available alternatives, including the firm's
   declining the new representation;

4. That I have had the opportunity to consult with independent counsel
   before signing this waiver.

After reflecting on these advisements, I consent to the firm's
representation of [New Client Name].

___________________________________     ____________________
[Former Client Name]                    Date

Independent counsel consulted (if any): _______________________
```

### Template — Rule 1.8(f) third-party payor consent

```
INFORMED CONSENT TO THIRD-PARTY PAYMENT — RULE 1.8(f)

I, [Client Name], understand that [Third Party Name] is paying the
legal fees for my representation by Daniels & Washington in
[matter description].

I have been advised:

1. That [Third Party] is not my lawyer's client; I am.

2. That my lawyer's duty of loyalty and confidentiality runs to me
   alone. [Third Party] does not direct strategy, receive privileged
   information, or make decisions about my case unless I expressly
   authorize specific disclosures.

3. That [Third Party]'s payment does not give [Third Party] any
   right to interfere with my lawyer's independent professional
   judgment.

4. That if a conflict arises between [Third Party]'s interests and my
   own, my lawyer must place my interests first or withdraw.

5. That I may revoke this consent at any time, and that doing so does
   not by itself end the representation.

I consent to the third-party payment arrangement and to the limited
disclosures (if any) listed below:

[List specific disclosures the client authorizes, if any]

___________________________________     ____________________
[Client Name]                           Date
```

All waivers are in writing and signed before the engagement letter is countersigned by the firm.

---

## Decline Protocol — When a Conflict Forecloses Representation

When the screen returns a non-waivable conflict, the firm declines:

1. Inform the prospective client orally that the firm cannot take the matter; do **not** disclose the reason if doing so would reveal protected information about a current or former client
2. Send a written non-engagement letter (template below) confirming the decline, setting a date by which the prospective client should secure other counsel, and confirming Rule 1.18 protection of intake-disclosed information
3. Segregate the intake notes (mark the file `DECLINED — Rule 1.18 protection in force` and store separately from active matters)
4. Suggest at least two referral options or refer to the parish bar lawyer-referral service
5. Track any pending court dates and warn the prospective client of imminent deadlines so they can secure counsel in time

### Non-engagement letter template

```
[FIRM LETTERHEAD — apply per dw-shared-protocols-crim/references/letterhead.md]
[Date]

[Prospective Client Name]
[Address]

Re:  Non-Engagement — [Matter Description]

Dear [Mr./Ms. Name]:

Thank you for considering Daniels & Washington for representation
in the above matter. After review, we have determined that we are
unable to undertake the representation. We wish you the best in
securing other counsel.

Critical deadlines you should be aware of:

[List any imminent deadlines — court date, response deadline,
statute of limitations]

We recommend you consult new counsel immediately. The [Parish] Bar
Association lawyer-referral service can be reached at
[phone/website]. Other firms that handle this type of matter
include [referrals].

We hold the information you shared with us in confidence pursuant
to La. Rule of Professional Conduct 1.18 and will not use that
information in any other matter.

This letter is not legal advice on the merits of your case.

Sincerely,

[Attorney Name]
[Bar Number]
[Firm Name]
```

The non-engagement letter is sent the same day the decline decision is made.

---

## Cowork's Role in the Conflict Check

Cowork **prepares**, the **attorney executes**:

- Cowork captures and organizes the names that go into the screen
- Cowork drafts the Conflict Check Record document with the names pre-populated
- The attorney runs the actual query against the firm conflict database
- The attorney signs the result line
- Cowork drafts any waiver letter or non-engagement letter using the templates above
- The attorney reviews and signs

Cowork never "clears" a conflict and never represents to the client that no conflict exists. That determination is the attorney's.

---

## Authorities

| Authority | Subject |
|---|---|
| La. Rules of Professional Conduct 1.6 | Confidentiality of Information |
| La. Rules of Professional Conduct 1.7 | Conflict of Interest: Current Clients |
| La. Rules of Professional Conduct 1.8(f) | Third-party payor consent |
| La. Rules of Professional Conduct 1.9 | Duties to Former Clients |
| La. Rules of Professional Conduct 1.10 | Imputation of Conflicts |
| La. Rules of Professional Conduct 1.16 | Declining or Terminating Representation |
| La. Rules of Professional Conduct 1.18 | Duties to Prospective Clients |

Cite by rule number. Mark any quoted text `[VERIFY CURRENT TEXT]`.

---

*The conflict check is the firm's first ethical act in any new matter. Run it before listening to a single substantive fact.*
