# Classification Engine — Per-Evidence-Type Routing Rules

Classify files by **filename keywords**, **file extension**, **content patterns**, and **folder structure**. Use all three methods in combination.

---

#### A. Police Reports & Incident Reports

**Keywords:** report, incident, narrative, police, officer statement, supplemental, investigation, summary, offense, complaint, booking

**Extensions:** .pdf, .docx

**Content indicators:** Witness statements, officer observations, scene description, narrative of events, case number, victim name, suspect name, charges

**Auditor Route:** `dw-crime-scene-auditor` + `dw-suppression-motion` (constitutional scan for 4th Amendment seizure/search issues)

**Priority:** HIGH

---

#### B. Cell Phone Extractions (Cellebrite/UFED/GrayKey)

**Keywords:** cellebrite, ufed, graykey, mobile extraction, phone dump, forensic extraction, ios extract, android extract, logical extraction, physical extraction, secure enclave

**Extensions:** .pdf (extraction report), .txt, .xml, .bin, .img (raw forensic dumps)

**Content indicators:** Device model (iPhone, Samsung, Google Pixel), extraction method (logical/physical), UFED report header, Cellebrite case report, deleted data sections, file listings, application data

**Auditor Route:** `dw-mobile-forensic-auditor` → `dw-forensic-dump-analyzer` (for detailed deleted data / file system analysis)

**Secondary Route:** `dw-cell-site-geolocation-auditor` (if location data extracted)

**Priority:** HIGH

---

#### C. Video Evidence (Body Cam, Dash Cam, Surveillance)

**Keywords:** video, body cam, bwc, bodycam, dash cam, dashcam, surveillance, cctv, interview room, cell video, civilian video, officer footage, activation

**Extensions:** .mp4, .avi, .mov, .mkv, .wmv, .flv, .m4v, .3gp, .dav, .264, .sec (video files) + .pdf (activation reports, video logs)

**Content indicators:** Timestamp data, camera ID, activation times, duration, frame rate, resolution, audio presence, metadata fields

**Auditor Route:** `dw-video-evidence-auditor`

**Secondary Route:** `dw-suppression-motion` (if video shows constitutional violations)

**Priority:** HIGH

---

#### D. Audio Recordings (Interrogations, Jail Calls, Interviews)

**Keywords:** audio, recording, interview, interrogation, confession, call, jail call, phone call, wiretap, oral statement, conversation, transcript

**Extensions:** .wav, .mp3, .aac, .flac, .m4a, .wma (audio files) + .pdf, .docx (transcripts)

**Content indicators:** Timestamp, interviewer/suspect names, duration, recording quality notes, Miranda warning mention, admission language

**Auditor Route:** `dw-transcript-router` (parish-based dispatch to `dw-transcript-pipeline-calcasieu` or `dw-transcript-pipeline-rev`) → `dw-confession-interrogation-auditor` (for interrogation analysis and suppression issues)

**Priority:** HIGH

---

#### E. Photo Arrays & Eyewitness Identification Materials

**Keywords:** photo array, lineup, identification, six-pack, photographic lineup, identification procedures, witness id, suggestive procedures, rdp, filler photos

**Extensions:** .pdf, .jpg, .jpeg, .png (array images or array documentation), .docx

**Content indicators:** Suspect photo + filler photos, array sequence, witness instructions, witness response sheet, identification confirmation, date of procedure, witness name

**Auditor Route:** `dw-eyewitness-identification-auditor`

**Priority:** HIGH

---

#### F. Lab Reports (DNA, Toxicology, Firearms, Trace Evidence)

**Keywords:** lab, laboratory, dna, toxicology, firearms, ballistics, serology, trace evidence, drug analysis, blood alcohol, thc, cocaine, methamphetamine, analysis, results, report

**Extensions:** .pdf, .docx

**Content indicators:** Lab name, case number, evidence item numbers, testing methodology, results tables, analyst name, accreditation info, quality control notes, comparison results (DNA match/exclusion, ballistics match)

**Auditor Route:** `dw-crime-scene-auditor` (for lab methodology audit) + `dw-chain-of-custody-auditor` (for evidence handling from collection through lab)

**Priority:** HIGH

---

#### G. Medical Records

**Keywords:** medical, hospital, healthcare, emergency room, er, physician, nurse, medical exam, treatment, diagnosis, injury, medical history, sane exam, sane kit

**Extensions:** .pdf, .docx

**Content indicators:** Provider name, patient ID, admission date, diagnoses, injuries, medications, treatment notes, discharge summary, consent forms

**Auditor Route:** `medical-chronology` (to build medical timeline and injury assessment)

**Priority:** MEDIUM

---

#### H. Witness Statements

**Keywords:** statement, witness, sworn statement, affidavit, statement of, interview notes, narrative witness statement, witness signed

**Extensions:** .pdf, .docx

**Content indicators:** Witness name, signature, date, statement of what witness saw/heard, reference to time/location, cross-reference to police report

**Auditor Route:** `dw-witness-statement-analyzer` → `dw-cross-exam-architect` + `dw-brady-giglio-auditor`

**Processing Note:** Run dw-witness-statement-analyzer first to produce Witness Analysis Cards (key facts, inconsistencies, credibility indicators), which then feed into dw-cross-exam-architect for cross-examination outline building.

**Priority:** MEDIUM

---

#### I. Cell Tower Location Records (CSLI / Cell Site Location Info)

**Keywords:** cell site, csli, cell location, tower, location records, cellular location, ping records, triangulation, location data, cdma location, lte location

**Extensions:** .pdf, .csv, .xlsx, .docx

**Content indicators:** Carrier name (AT&T, Verizon, T-Mobile, Sprint), phone number, date range, tower ID, latitude/longitude, distance from cell site, signal strength, sectors

**Auditor Route:** `dw-cell-site-geolocation-auditor`

**Secondary Route:** `dw-brady-giglio-auditor` (to flag if location data contradicts prosecution timeline)

**Priority:** HIGH

---

#### J. Social Media Printouts

**Keywords:** facebook, twitter, instagram, snapchat, tiktok, social media, screenshot, post, message, dm, direct message, social network, web page print

**Extensions:** .pdf, .jpg, .jpeg, .png, .docx

**Content indicators:** Username, profile name, timestamp, message text, hashtags, likes/shares, user ID, platform name, URL

**Auditor Route:** `dw-social-media-auditor`

**Secondary Route:** `dw-brady-giglio-auditor` (if social media shows inconsistency with prosecution narrative)

**Priority:** MEDIUM

---

#### K. Search Warrants & Affidavits

**Keywords:** search warrant, warrant affidavit, probable cause affidavit, affidavit, warrant application, judicial authorization, warrant return, items seized

**Extensions:** .pdf, .docx

**Content indicators:** Judge name, affiant name, probable cause statement, items to be searched, specific items to seize, return of warrant, items actually seized vs authorized

**Auditor Route:** `dw-suppression-motion` (warrant audit mode: probable cause adequacy, particularity, execution compliance)

**Priority:** HIGH

---

#### L. Forensic Interview Recordings (Child Abuse Cases)

**Keywords:** forensic interview, child advocacy center, cac, child interview, forensic interviewer, abuse disclosure, cac video

**Extensions:** .mp4, .mov, .avi (video) + .pdf, .docx (interview report/transcript)

**Content indicators:** Child name, age, interviewer name, facility name, time/date, allegation type, disclosure language, leading questions flag

**Auditor Route:** `dw-child-forensic-interview-auditor` (for interview methodology and suggestiveness analysis)

**Priority:** HIGH

---

#### M. Expert Reports & Curricula Vitae

**Keywords:** expert, report, cv, curriculum vitae, affidavit, expert analysis, opinion, expert witness, qualification, credentials, expert declaration

**Extensions:** .pdf, .docx

**Content indicators:** Expert name, qualifications, prior testimony, opinion statement, basis for opinion, method/methodology, expert credentials section, case references

**Auditor Route:** `dw-expert-witness-evaluator` (to assess expert reliability, bias, and cross-examination vulnerabilities)

**Priority:** MEDIUM

---

#### N. Prior Conviction Records

**Keywords:** prior, conviction, criminal history, record, prior conviction, sentencing, judgment, guilty plea, adjudication, habitual offender, habitual, repeat offender

**Extensions:** .pdf, .docx

**Content indicators:** Defendant name, date of conviction, charge, jurisdiction, disposition, sentence, case number

**Auditor Route:** `dw-habitual-offender-auditor` (to assess habitual offender exposure and prior conviction admissibility)

**Priority:** MEDIUM

---

#### O. Plea Agreements & Cooperation Agreements

**Keywords:** plea, plea agreement, cooperation agreement, plea deal, coop agreement, guilty plea, plea and disposition, sentencing recommendation, plea facts, plea allocution, 5k1, substantial assistance

**Extensions:** .pdf, .docx

**Content indicators:** Defendant name, charges, terms of agreement, cooperation language, immunity clause, sentencing recommendation, prosecutor signature, judge approval, factual admission

**Auditor Route:** `dw-brady-giglio-auditor` (to flag undisclosed cooperation deals and Giglio impeachment material)

**Priority:** HIGH

---

#### P. SANE Exam Reports & Sex Offense Evidence

**Keywords:** sane, sane exam, sexual assault, rape kit, sexual assault kit, forensic exam, nurse examiner, sane nurse, sexual battery, indecent behavior, molestation, sex offense, sexual abuse

**Extensions:** .pdf, .docx

**Content indicators:** SANE nurse name, exam findings, injury documentation, forensic exam collection log, DNA reference samples, toxicology, patient history, chain of custody for kit components

**Auditor Route:** `dw-sex-offense-specialist` (comprehensive sex offense analysis including SANE audit, DNA mixture interpretation, rape shield, delayed disclosure research)

**Secondary Route:** `dw-chain-of-custody-auditor` (for kit handling from collection through lab) + `dw-child-forensic-interview-auditor` (if victim is a minor and forensic interview also in discovery)

**Priority:** HIGH

---

#### Q. Raw Database Files (SQLite / WAL)

**Keywords:** database, sqlite, .db, .wal, .shm, journal, wal file, write-ahead log, freelist, deleted records

**Extensions:** .db, .sqlite, .sqlite3, .sqlitedb, -wal, -shm, -journal

**Content indicators:** Companion -wal/-shm files alongside a .db, file sizes suggesting active WAL (>0 bytes), database filenames matching known iOS/Android app databases (sms.db, ChatStorage.sqlite, msgstore.db, call_history.db)

**Auditor Route:** `dw-sqlite-recovery` (WAL sequencing analysis, deleted data recovery audit, forensic standard-of-care assessment)

**Note:** These files are typically produced alongside a phone extraction (Category B). If the extraction report is also present, route the extraction report to `dw-mobile-forensic-auditor` first, then raw database files to `dw-sqlite-recovery`. The SQLite auditor evaluates what the extraction tool missed.

**Priority:** HIGH (if case-critical databases like messaging or location are present)

---

#### R. Cross-Cutting: Timeline Assembly

**Secondary route applied to ALL timestamped evidence across categories.**

Any file classified under Categories A (Police Reports), C (Video Evidence), D (Audio Recordings), I (Cell Tower Records), or B (Phone Extractions) should ALSO be routed to `dw-timeline-builder` as a secondary auditor.

**Auditor Route (Secondary):** `dw-timeline-builder`

**Purpose:** After primary auditors process these files, dw-timeline-builder aggregates all extracted timestamps into the master case timeline with conflict detection and source reliability scoring.

**Processing Note:** Run dw-timeline-builder AFTER Priority 2 forensic audits complete, using all timestamped evidence to assemble the unified chronology. This runs parallel to Priority 3 witness audits.

---

### Unclassified Files

Files that do not match the above patterns:
- Administrative documents (cover letters, routing slips, binders)
- Miscellaneous forms with unclear content
- Encrypted or corrupted files
- Files with no discernible extension or metadata

**Handling:** Flag in Triage Report under "Manual Review Required." List filename, size, upload date, and reason for non-classification.
