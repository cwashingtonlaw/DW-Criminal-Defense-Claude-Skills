# Discovery Triage Report — Template

After classifying **every file**, generate the **Discovery Triage Report** with the following structure.

### Report Header
- Case Name
- Case Number / Docket Number
- Attorney Name
- Report Generation Date & Time
- Total Files Processed
- Total Files Classified vs Unclassified

### Section 1: File Classification Summary

| File Name | Extension | Evidence Type | Assigned Auditor(s) | Priority |
|-----------|-----------|----------------|-------------------|----------|
| [filename] | .pdf | Police Report | dw-crime-scene-auditor-crim, dw-suppression-motion-crim | HIGH |
| [filename] | .mp4 | Body Cam Video | dw-video-evidence-auditor-crim | HIGH |
| (all files listed) | | | | |

**Legend:**
- ⭐ = Constitutional concern flagged
- 🔒 = Brady/Giglio exposure flagged
- ⚠️ = Chain of custody issue flagged
- 📋 = Administrative (low priority)

### Section 2: Recommended Processing Order

Based on discovery priority and workflow logic, list auditor skills in recommended execution order:

**Priority 1 — Constitutional Issues (Must Run First):**
1. `dw-suppression-motion-crim` — Search warrant audit, seizure/interrogation analysis
2. Files: [list]
3. Estimated runtime: [estimate based on file count]

**Priority 2 — Forensic Audits (Parallel Execution):**
1. `dw-mobile-forensic-auditor-crim` — Phone extractions audit
2. Files: [list]
3. Estimated runtime: [estimate]

[Repeat for each forensic/evidence auditor needed]

**Priority 3 — Witness & Procedural Audits:**
1. `dw-eyewitness-identification-auditor-crim` — Photo array procedures
2. Files: [list]
3. Estimated runtime: [estimate]

[Repeat for witness-related auditors]

**Priority 4 — Brady/Giglio Final Sweep (Always Last):**
1. `dw-brady-giglio-auditor-crim` — Comprehensive discovery compliance audit across all files
2. Files: [all discovery files]
3. Estimated runtime: [estimate]

**Priority 5 — Compliance Update (Final Step):**
1. `dw-discovery-compliance-monitor-crim` — Update discovery ledger with processed files and findings
2. Estimated runtime: [estimate]

### Section 3: Classified Files by Auditor

Group all classified files by their assigned auditor skill:

```
## dw-crime-scene-auditor-crim
- 010 - Incident Report.pdf (Police Report)
- 042 - Lab DNA Report.pdf (DNA Lab Report)
- Estimated files: 3
- Estimated auditor workload: 2–3 hours

## dw-video-evidence-auditor-crim
- 025 - Body Camera Footage/ (folder with 4 video files)
- 031 - Surveillance Video.mp4
- Estimated files: 5
- Estimated auditor workload: 2–3 hours

## dw-mobile-forensic-auditor-crim
- 015 - Cellebrite Extraction Report.pdf
- Estimated files: 1
- Estimated auditor workload: 1–2 hours

[Continue for each auditor]
```

### Section 4: Unclassified Files Requiring Manual Review

| File Name | Size | Upload Date | Reason for Non-Classification |
|-----------|------|-------------|-------------------------------|
| MiscDoc_001.docx | 145 KB | [date] | Content unclear; appears to be administrative routing slip |
| IMG_8374.jpg | 3.2 MB | [date] | Image appears to be crime scene photo but lacks context/metadata |

**Recommendation:** Attorney review to determine proper classification or discard.

### Section 5: Workflow Execution Plan

**Option A — Full Automated Orchestration (Recommended)**
- I will execute all auditor skills in the recommended order
- Each auditor will process assigned files and generate findings
- Final Brady/Giglio sweep will cross-reference all auditor outputs
- Estimated total workflow time: [sum of all estimates]

**Option B — Attorney-Selected Subset**
- You choose which auditors to run now (e.g., Priority 1–2)
- Defer others to later sessions
- I will execute selected skills only

**Option C — Manual Selection**
- You review the triage report and tell me which specific auditors to invoke
- I will route specific files to those auditors

**Which option do you prefer?**
