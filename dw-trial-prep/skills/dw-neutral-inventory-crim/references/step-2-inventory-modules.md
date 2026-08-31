# Step 2 — Neutral Inventory Modules A–F

Read at STEP 2 (Neutral Inventory Modules) of `dw-neutral-inventory-crim/SKILL.md` — the six module field tables and rules, moved verbatim from SKILL.md.

---

### MODULE A — Document Catalog

Catalog every document in the case file. For each document, record:

| Field | Description |
|-------|-------------|
| **Doc #** | Sequential number assigned by this inventory (D-001, D-002, ...) |
| **Filename** | Exact filename as it appears in the case folder |
| **Bates Range** | Bates stamp range if available (e.g., Bates #00145-00160) |
| **Page Count** | Total pages |
| **Document Type** | Classification: Police Report, Supplemental Report, Witness Statement, Victim Statement, Lab Report, Forensic Report, Autopsy Report, Charging Document, Court Order, Plea Agreement, Search Warrant, Arrest Warrant, Affidavit, Evidence Log, Chain of Custody, Medical Record, School Record, Employment Record, Financial Record, Correspondence, Other (specify) |
| **Date of Document** | Date on the document face (not the date produced) |
| **Author / Source** | Who created or signed the document (officer name, lab analyst, witness, etc.) |
| **One-Line Factual Summary** | Single sentence describing the factual content — neutral, no strategic assessment |

**Ordering:** Catalog documents in the order they appear in the case folder structure (following the firm's standard folder convention), then by Bates number within each folder.

**Multi-part documents:** If a single production contains multiple distinct documents (e.g., a 200-page discovery dump with incident report, supplemental reports, witness statements, and lab reports), break them into separate catalog entries with individual Doc # assignments and the appropriate Bates sub-ranges.

---

### MODULE B — Media Catalog

Catalog every audio, video, and digital media file. For each item, record:

| Field | Description |
|-------|-------------|
| **Media #** | Sequential number (M-001, M-002, ...) |
| **Filename** | Exact filename |
| **Duration / Size** | Runtime for A/V; file size for data files |
| **Media Type** | Classification: Body-Worn Camera (BWC), Dash Cam, Interview Recording, Interrogation Recording, Jail Call, 911 Audio, CCTV / Surveillance, Cell Phone Video, Social Media Video, Photograph Set, Cell Phone Extraction (Cellebrite/GrayKey/UFED), CSLI Data, Cell Tower Records, Social Media Extraction, Computer Forensic Image, Other Digital (specify) |
| **Recording Date** | Date the recording was made |
| **Participants Identified** | Names and roles of all identifiable participants |
| **One-Line Content Summary** | Single sentence describing the factual content — neutral |

**Phone extractions:** For Cellebrite or similar extraction reports, note the device make/model, extraction type (full file system, logical, advanced logical), and total page count of the report. Do not catalog individual extracted items here — that is `dw-mobile-forensic-auditor-crim`'s job.

**Photograph sets:** If discovery includes a batch of photographs (scene photos, evidence photos, booking photos), catalog the set as a single Media # entry with the count and general subject matter. Individual photo analysis is downstream work.

---

### MODULE C — Physical Evidence Catalog

Catalog every piece of physical evidence referenced in discovery. For each item, record:

| Field | Description |
|-------|-------------|
| **Item #** | The evidence item number as assigned by law enforcement (e.g., Item #E-001) or, if unnumbered, a sequential P-### number |
| **Description** | Factual description of the item (e.g., ".45 caliber semi-automatic handgun, Smith & Wesson Model M&P, serial #ABC12345") |
| **Collection Location** | Where the item was collected (address, room, vehicle, person) |
| **Collection Date** | Date and time of collection |
| **Collected By** | Name and title of the person who collected the item |
| **Custodian** | Current known custodian (crime lab, evidence room, etc.) |
| **Lab Submitted** | Whether the item was submitted to a lab for analysis, and if so, which lab and what analysis was requested |
| **Lab Report Available** | Yes / No / Pending — cross-reference with Document Catalog entries |
| **Source Documents** | Which discovery documents reference this item (cite Doc # from Module A) |

**Items referenced but not produced:** If a police report references physical evidence (e.g., "officers recovered a firearm") but no evidence log, chain of custody form, or lab report for that item appears in discovery, catalog it here with all available fields and flag the gap in Module E.

---

### MODULE D — Witness Roster

List every person mentioned in any discovery document. For each person, record:

| Field | Description |
|-------|-------------|
| **Name** | Full name as it appears in discovery |
| **Role** | Classification: Victim, Eyewitness, Character Witness, Expert Witness, Law Enforcement Officer, Detective/Investigator, Lab Analyst, Medical Professional, Confidential Informant (if disclosed), Co-Defendant, Defendant, Other (specify) |
| **Documents Appeared In** | List every document (by Doc # from Module A) and media file (by Media # from Module B) in which this person is mentioned, with Bates stamps or timestamps where available |
| **Statement Exists** | Yes (cite Doc #) / No / Unknown |
| **Statement Type** | Written / Recorded / Transcribed / Grand Jury / Deposition / N/A |
| **Contact Info in File** | Whether the file contains address, phone number, or other contact information for this person (Yes / No — do not reproduce the actual contact info in the inventory) |

**De-duplication:** Watch for the same person appearing under different name spellings, nicknames, or titles across documents. Consolidate into a single entry and note all name variants.

**Unnamed persons:** If a document references an unidentified person (e.g., "an unknown male," "a confidential informant," "the caller"), create an entry with whatever identifying information is available and flag for investigation.

---

### MODULE E — Completeness Flags

Flag what appears to be missing from the discovery production. Each flag must cite the specific document that references the missing item.

| Flag Type | What to Flag | Source Citation |
|-----------|-------------|----------------|
| **Document Referenced, Not Produced** | A document mentioned in discovery that does not appear in the production (e.g., a supplemental report referenced in the incident report but not included) | Cite the document and passage that references the missing item |
| **Witness Mentioned, No Statement** | A person identified as a witness in reports who has no corresponding statement in the file | Cite the document that identifies the person as a witness |
| **Evidence Referenced, No Lab Report** | Physical evidence submitted to a lab (per evidence log or report narrative) with no corresponding lab results in discovery | Cite the evidence log entry or report passage |
| **BWC/Dash Cam Expected, Not Produced** | An encounter with law enforcement where body-worn or dash camera footage would be expected (arrest, search, traffic stop) but no corresponding media file exists | Cite the report documenting the encounter |
| **Recording Referenced, Not Produced** | An interview, interrogation, or call referenced in a report but no corresponding audio/video file in discovery | Cite the report passage referencing the recording |
| **Incomplete Production Indicators** | Bates number gaps, missing pages within a document, or other signs of incomplete production | Cite the Bates range gap or the document with missing pages |
| **Standard Discovery Not Present** | Items that would normally be produced for this charge type but are absent (e.g., autopsy report in a homicide, SANE report in a sex case, toxicology in a DWI) | Cite the charging document and the expected item |

**Important:** The completeness flags are observational, not accusatory. Do not characterize missing items as discovery violations or Brady issues — that analysis belongs to `dw-discovery-compliance-monitor-crim` and `dw-brady-giglio-auditor-crim` respectively. Simply note: "Referenced in [source] but not present in the discovery production as of [date]."

---

### MODULE F — Verification Status

After completing Modules A-E, assign a verification status to every catalog entry:

| Status | Meaning | When to Apply |
|--------|---------|---------------|
| **[VERIFIED]** | Source document has been reviewed by this skill and the catalog entry accurately reflects its contents | The document/media/evidence item was directly reviewed during this inventory |
| **[UNVERIFIED]** | Entry is based on references in other documents; the source item itself was not directly reviewed | The item is mentioned in a report, evidence log, or witness statement, but the item itself is not in the case file or was not accessible for review |
| **[PARTIAL]** | Source document was reviewed but is incomplete (missing pages, redacted sections, truncated recording) | The item was reviewed but could not be fully cataloged due to incompleteness |

Apply the status tag at the end of each catalog entry's one-line summary.

**Verification counts:** At the end of the inventory, provide a summary count:
- Total entries: ___
- [VERIFIED]: ___
- [UNVERIFIED]: ___
- [PARTIAL]: ___

A high [UNVERIFIED] count signals that the discovery production may be incomplete — this finding feeds directly into `dw-discovery-compliance-monitor-crim`.
