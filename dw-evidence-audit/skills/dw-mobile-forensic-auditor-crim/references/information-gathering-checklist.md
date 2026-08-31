# Information Gathering Checklist

Read at STEP 1 (Information Gathering Protocol) of `dw-mobile-forensic-auditor-crim/SKILL.md` — the full ranked Essential / Strategic / Contextual intake checklist (items 1-14).

### Essential (must have before auditing)
1. **Forensic Report(s):** Cellebrite UFED, MSAB XRY, Magnet AXIOM, GrayKey, or other tool output
2. **Device Identifier:** Make, model, and OS version of the target device
3. **Extraction Type Used:** Logical, Advanced Logical, Full File System (FFS), or Physical
4. **Charges:** all counts with statutory citations — severity determines extraction adequacy threshold
5. **What the State Claims the Extraction Proves:** the prosecution's theory of what the phone data establishes

### Strategic (request if not provided)
6. **Examiner Credentials:** name, agency, certifications (CCME, CCPA, EnCE, GCFE, etc.)
7. **Chain of Custody Documentation:** seizure-to-extraction timeline, storage conditions, who handled the device
8. **Warrant/Consent Scope:** what the warrant authorized vs. what was actually extracted
9. **Defense Theory:** what happened from the defense perspective — what data should or shouldn't be there
10. **Known Suppression Issues:** any pending motions regarding the device or its seizure

### Contextual (gather from uploaded files)
11. **Tool Version:** exact software version and license type used for extraction
12. **Extraction Logs/Audit Trail:** automated logs showing extraction parameters, errors, retries
13. **Hash Values:** MD5/SHA verification of extracted image vs. source device
14. **Time Zone & Clock Settings:** device time zone, NTP sync status, manual vs. automatic time
