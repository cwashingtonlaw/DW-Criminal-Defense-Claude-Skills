# Classification Flowchart (Quick Reference)

Walk this decision tree top-to-bottom for each discovery file. The first match wins for primary routing; secondary routing rules in `classification-engine.md` may add additional auditors.

1. **Does file contain or reference forensic interview of a child (CAC, child advocacy)?**
   - Yes → `dw-child-forensic-interview-auditor-crim`
   - No → Continue

2. **Does file contain video (body cam, dash cam, surveillance, interview room)?**
   - Yes → `dw-video-evidence-auditor-crim`
   - No → Continue

3. **Does file contain audio (interrogation, jail call, interview, 911)?**
   - Yes → `dw-transcript-router-crim` (transcription via parish-based dispatch) → then route transcript:
     - Interrogation/confession → `dw-confession-interrogation-auditor-crim`
     - Jail calls → `dw-jail-call-analyzer-crim`
     - Other audio → `dw-cross-exam-architect-crim`
   - No → Continue

4. **Does filename mention phone, Cellebrite, UFED, GrayKey?**
   - Yes → `dw-mobile-forensic-auditor-crim` → `dw-forensic-dump-analyzer-crim`
   - No → Continue

5. **Is the file a raw database (.db, .sqlite, -wal, -shm)?**
   - Yes → `dw-sqlite-recovery-crim`
   - No → Continue

6. **Does filename mention report, incident, police, crime scene?**
   - Yes → `dw-crime-scene-auditor-crim`
   - No → Continue

7. **Does filename mention lab, DNA, toxicology, firearms?**
   - Yes → `dw-crime-scene-auditor-crim` + `dw-chain-of-custody-auditor-crim`
   - No → Continue

8. **Does filename mention SANE, rape kit, sexual assault exam?**
   - Yes → `dw-sex-offense-specialist-crim` + `dw-chain-of-custody-auditor-crim`
   - No → Continue

9. **Does filename mention photo array, lineup, identification, six-pack?**
   - Yes → `dw-eyewitness-identification-auditor-crim`
   - No → Continue

10. **Does filename mention cell site, csli, tower, location?**
    - Yes → `dw-cell-site-geolocation-auditor-crim`
    - No → Continue

11. **Does filename mention search warrant, affidavit, warrant?**
    - Yes → `dw-suppression-motion-crim`
    - No → Continue

12. **Does filename mention plea, cooperation, agreement, deal?**
    - Yes → `dw-brady-giglio-auditor-crim`
    - No → Continue

13. **Does filename mention expert, cv, opinion, qualifications?**
    - Yes → `dw-expert-witness-evaluator-crim`
    - No → Continue

14. **Does filename mention prior, conviction, habitual, record?**
    - Yes → `dw-habitual-offender-auditor-crim`
    - No → Continue

15. **Does filename mention medical, hospital, healthcare?**
    - Yes → `medical-chronology`
    - No → Continue

16. **Does filename mention statement, witness, affidavit?**
    - Yes → `dw-witness-statement-analyzer-crim` → `dw-cross-exam-architect-crim` + `dw-brady-giglio-auditor-crim`
    - No → Continue

17. **Does file contain timestamps, times, dates, or temporal references?**
    - Yes → Also route to `dw-timeline-builder-crim` (secondary, in addition to primary auditor)
    - No → Continue

18. **Does filename mention social media, facebook, twitter, instagram?**
    - Yes → `dw-social-media-auditor-crim`
    - No → Continue

19. **If none match:** Flag as "Unclassified — Manual Review Required"
