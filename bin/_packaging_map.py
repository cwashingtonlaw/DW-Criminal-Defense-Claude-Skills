# bin/_packaging_map.py — single source of truth for the plugin grouping.
# Throwaway: delete after the move lands (Task 8). Keys are plugin dir names;
# values are the dw-* skill dir names that belong in <plugin>/skills/.
PLUGINS = {
    "dw-core": [
        "dw-case-brain", "dw-case-dashboard", "dw-criminal-defense",
        "dw-data-contracts", "dw-shared-protocols", "dw-skill-index",
    ],
    "dw-intake-discovery": [
        "dw-client-intake-interview", "dw-brady-giglio-auditor",
        "dw-discovery-compliance-monitor", "dw-discovery-orchestrator",
    ],
    "dw-evidence-audit": [
        "dw-cell-site-geolocation-auditor", "dw-chain-of-custody-auditor",
        "dw-child-forensic-interview-auditor", "dw-confession-interrogation-auditor",
        "dw-crime-lab-auditor", "dw-crime-scene-auditor",
        "dw-dna-forensic-biology-auditor", "dw-expert-witness-evaluator",
        "dw-eyewitness-identification-auditor", "dw-forensic-dump-analyzer",
        "dw-jail-call-analyzer", "dw-mobile-forensic-auditor",
        "dw-social-media-auditor", "dw-sqlite-recovery",
        "dw-video-evidence-auditor", "dw-witness-statement-analyzer",
    ],
    "dw-offense-specialists": [
        "dw-drug-offense-specialist", "dw-dwi-specialist",
        "dw-firearms-specialist", "dw-sex-offense-specialist",
        "dw-violent-crime-specialist",
    ],
    "dw-pleadings": [
        "dw-404b-opposition", "dw-bond-and-release-motion",
        "dw-pretrial-motion-library", "dw-suppression-motion",
    ],
    "dw-trial-prep": [
        "dw-adversarial-stress-test", "dw-appellate-error-monitor",
        "dw-cross-exam-architect", "dw-defense-investigator-tasking",
        "dw-direct-exam-architect", "dw-exhibit-manager",
        "dw-issue-code-tracker", "dw-jury-focus-group",
        "dw-jury-instructions-builder", "dw-theory-to-workplan",
        "dw-timeline-builder", "dw-trial-day-assistant",
        "dw-trial-narrative-builder", "dw-trial-notebook-builder",
        "dw-voir-dire-assistant", "dw-witness-threat-matrix",
        "dw-neutral-inventory", "dw-theory-deconstructor",
    ],
    "dw-transcription": [
        "dw-dmar-synthesizer", "dw-transcript-pipeline-calcasieu",
        "dw-transcript-pipeline-rev", "dw-transcript-router",
    ],
    "dw-disposition": [
        "dw-appellate-brief-builder", "dw-case-disposition",
        "dw-habitual-offender-auditor", "dw-plea-negotiation-analyzer",
        "dw-post-conviction-relief", "dw-sentencing-mitigation-specialist",
    ],
    "dw-ops": [
        "dw-billing-narrative-generator", "dw-case-law-researcher",
        "dw-client-communication-drafter", "dw-court-jail-tracker",
        "dw-evidence-placeholder", "dw-image-filename-stamp",
    ],
}

DESCRIPTIONS = {
    "dw-core": "Foundation: session persistence, shared protocols, data contracts, master orchestrator, case dashboard, and skill index. Every other dw plugin depends on this.",
    "dw-intake-discovery": "Client intake interview plus discovery orchestration, compliance monitoring, and Brady/Giglio audit.",
    "dw-evidence-audit": "Methodology and reliability audits across all evidence types: forensics, interrogations, eyewitness ID, cell-site, video, social media, lab, DNA, chain of custody.",
    "dw-offense-specialists": "Element-by-element defense theory for drug, DWI, firearms, sex, and violent-crime charges.",
    "dw-pleadings": "Motion drafting: suppression, 404(b) opposition, bond/release, and the pretrial motion library.",
    "dw-trial-prep": "Trial preparation: cross/direct exam, voir dire, jury instructions, exhibits, timelines, trial-day assistant, error preservation, theory tools, and investigator tasking.",
    "dw-transcription": "Media transcription routing and DMAR pipelines (Calcasieu + Rev) plus cross-case DMAR synthesis.",
    "dw-disposition": "Sentencing, habitual-offender audit, plea analysis, appeal, post-conviction relief, and case disposition.",
    "dw-ops": "Operational utilities: billing narratives, case-law research, client communications, court/jail tracker, evidence placeholders, image stamping.",
}

if __name__ == "__main__":
    total = sum(len(v) for v in PLUGINS.values())
    assert total == 69, f"expected 69 skills, got {total}"
    print(f"{len(PLUGINS)} plugins, {total} skills — map OK")
