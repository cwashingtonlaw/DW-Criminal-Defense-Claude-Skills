# Evidence Type Classification & Authentication Triage

## Evidence Reliability Hierarchy (Least → Most Reliable)

Classify every piece of social media evidence and flag authentication weaknesses based on its type.

| Level | Evidence Type | What It Provides | Authentication Weaknesses |
|-------|--------------|------------------|--------------------------|
| 1 | **Civilian Screenshot** | Image of what someone claims they saw on a screen at a point in time | No metadata linking to the platform; trivially fabricable with inspect element, Photoshop, or fake conversation generators; no chain of custody; no timestamp verification; no proof the account belongs to the defendant |
| 2 | **Law Enforcement Screenshot** | Same as civilian but with officer testimony re: when/how captured | Still no platform-verified metadata; officer may lack technical training; screenshot may not capture full context (scrolling, thread, profile verification); no hash verification |
| 3 | **Screen Recording** | Video of a device displaying social media content | Better than static screenshot (harder to fabricate seamlessly), but still no platform verification; recording software metadata may be absent; can be edited |
| 4 | **Cellebrite/Forensic Extraction of App Data** | App databases, cached content, SQLite records from device | Tied to specific device but subject to all mobile forensic limitations (see dw-mobile-forensic-auditor-crim); app may cache content from other users; deleted content recovery is extraction-type dependent |
| 5 | **Platform-Produced Records (Subpoena/Warrant Response)** | Account data, content, metadata, IP logs, timestamps directly from the platform's servers | Most reliable source — but still requires: proper legal process, records custodian certification, completeness verification, and understanding of what the platform does and does not retain |

## Authentication Adequacy Test

Apply this decision matrix:

**If the prosecution relies primarily on Level 1–2 evidence (screenshots) in a serious case:**
> ⚠ **AUTHENTICATION FLAG — CRITICAL:** The State's social media evidence consists of [screenshots / printouts] with no platform-verified metadata, no records custodian certification, and no forensic verification that the content existed on the platform as depicted. Screenshots are trivially fabricable — any person with basic computer skills can alter displayed content using browser developer tools, image editing software, or fake conversation generator websites. Under La. C.E. Art. 901, the proponent must produce evidence sufficient to support a finding that the matter is what its proponent claims. A screenshot alone, without corroborating platform records or forensic verification, fails this threshold. Flag for: (1) authentication challenge under Art. 901, (2) demand for platform-produced records, (3) cross-examination of the witness who captured the screenshot.

**If the prosecution has platform-produced records but no records custodian affidavit:**
> ⚠ **AUTHENTICATION FLAG — FOUNDATION GAP:** Platform records were produced but no records custodian affidavit or certification accompanies the production. Without custodial authentication, the records are hearsay without a recognized exception. The business records exception (La. C.E. Art. 803(6)) requires testimony or certification from a qualified custodian. Demand: records custodian affidavit or live testimony from a platform representative.

**If the prosecution relies on a Cellebrite extraction of social media app data:**
> ⚠ **AUTHENTICATION FLAG — EXTRACTION LIMITATION:** Social media content recovered from a forensic device extraction reflects cached/stored app data on the defendant's device — it does not independently verify that the defendant authored the content, that the content was not altered before caching, or that the account belongs to the defendant. Cross-reference with the dw-mobile-forensic-auditor-crim skill for extraction methodology challenges. Additionally flag: was the app data from the active app or from a cached/deleted state?
