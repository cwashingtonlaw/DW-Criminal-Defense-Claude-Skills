# Module F — Privilege / Suppression Exceptions

Read this file at MODULE F — it holds F.1 baseline doctrine, F.2 genuine exceptions, F.3 *Lanza* analysis, and F.4 output format.

### F.1 Baseline Doctrine

The default rule is that recorded jail calls are admissible: inmates have no reasonable expectation of privacy in non-attorney calls under the *Hudson v. Palmer* line of authority and the federal jail-call doctrine running through *Lanza* and its progeny. Every facility posts notice that calls are recorded; recipients accept a recorded prompt; consent under one-party-consent statutes is satisfied by either the inmate or the recipient acknowledging the recording. **Do not waste motion practice attacking jail-call admissibility on privacy grounds in the typical case.**

### F.2 Genuine Exceptions

The narrow circumstances in which suppression or limitation is realistic:

- **Attorney-client breach.** If the call was to a registered attorney line and the facility recorded it anyway, the recording must be quarantined, the prosecutor must certify non-review, and the recording is suppressed. Confirm by checking whether the dialed number was registered as privileged in the vendor system. If counsel's number was not registered, that is a defense-side failure to preserve privilege, not a State-side violation — note it for internal process improvement.
- **Third-party-presence waiver issues.** When an attorney call includes a third party on the line (a family member, an investigator who is not retained as a privileged agent, a co-defendant), privilege may be waived as to communications in the third party's presence. Audit any flagged attorney-line call for third-party voices.
- **Claimed privileged content on a non-attorney call.** Sometimes a client repeats what their lawyer told them on a call to a family member. The substantive content of attorney advice may retain *some* privilege protection, but the disclosure itself usually waives it. Flag for the assigned attorney; do not assume suppression.
- **Recording-statute violations** in the rare jurisdictions where a call leg crosses state lines into a two-party-consent jurisdiction with a non-consenting recipient. Almost never wins; flag only if the facts squarely present it.
- **Selective production** — if the State produced only a curated subset of calls (e.g., only the calls that hurt) and the defense can show non-production of helpful calls, that is a *Brady* problem, not a suppression problem. Cross-feed to `dw-brady-giglio-auditor-crim`.

### F.3 *Lanza* Analysis

For any call where the client makes incriminating statements with the apparent assumption of privacy, the *Lanza* doctrine controls: privacy expectations in jail are minimal, and the recording of routine inmate calls does not constitute an unreasonable search. State the doctrine, note that it forecloses the privacy challenge, and move on. Do not file a suppression motion based solely on a privacy theory; it will lose and will preview the defense's audit thinking to the State.

### F.4 Output

For each privilege/suppression flag, document:
- The call ID and timestamp
- The doctrinal basis (attorney-client, third-party waiver, recording statute, *Brady* selective production)
- The realistic prospect (HIGH / MODERATE / LOW / DOA)
- The recommended motion vehicle (motion to suppress, motion in limine, *Brady* motion, or "do not move")
