# Immediate-Action Triage (D.1–D.7)

Read at SKILL.md MODULE D — Immediate-Action Triage; holds the full D.1–D.7 capture lists, routing, and client instructions.

**The highest-value module in this skill.** The first 24-72 hours after retention determine whether evidence survives, whether the client says something on a jail call that destroys the defense, whether social media posts are still recoverable, and whether the bond posture is locked or fluid. Cowork produces the immediate-action checklist and routes each line item to the right downstream skill.

### D.1 — Bond posture

Capture:
- Current custody status (in custody, out on bond, summoned, warrant pending, threatened)
- Current bond amount and type, if set (cash, surety, cash-only, ROR, no-bond)
- Existing conditions of release (no-contact, GPS, curfew, travel)
- Date and parish of arrest
- Charges at booking (which may differ from charges later filed)
- Client financial capacity to post current bond
- Time since arrest (Art. 701 / Art. 230.1 timer awareness)

**Route:** Pass the bond facts directly to `dw-bond-and-release-motion-crim`. If the client is in custody and has not had a bail hearing or has an excessive bond, this is urgent — the bond motion should be drafted within 48 hours of retention.

### D.2 — Evidence preservation letters

The state's evidence has a half-life. Body-worn camera footage may be auto-purged on 90- or 180-day cycles. Business surveillance is typically overwritten on a 30/60/90-day rolling window depending on chain. Social-media platform records require a § 2703(f) preservation request to lock them before they can be subpoenaed. Cowork drafts preservation letters from `references/evidence-preservation-letters.md`:

- **Law enforcement preservation letter** — body-worn camera, dashcam, in-car video, station-house video, 911 audio, CAD logs, dispatch recordings, all officer notes/reports/CAD reports related to the matter
- **Business surveillance preservation letter** — to identified businesses (gas stations, convenience stores, ATM, parking garages, restaurants, hotels, residential complexes) with retention-window urgency
- **Social media preservation request under Stored Communications Act 18 U.S.C. § 2703(f)** — requires the platform to preserve account records for 90 days (extendable). This is preservation only — content is obtained later by subpoena or warrant.
- **Witness preservation contact** — letter or call (attorney decides the medium) to known third-party witnesses requesting they preserve photos, videos, texts, social posts, and contact information

**Route:** All preservation letters go to attorney for signature and outbound mailing/service. Copies filed in `00 - Client File/01 - Intake/Preservation Letters/`.

### D.3 — Social media lockdown

Use `references/social-media-lockdown-checklist.md`. Platform-by-platform:

- **Lock down — never delete.** Deletion is potential spoliation of evidence and can support an obstruction or evidence-tampering charge. Lock privacy settings, change passwords, enable two-factor — but **do not delete posts, photos, messages, or accounts.**
- **Deactivate vs. delete distinction.** Deactivation hides; deletion may be irreversible and may erase evidence. The skill defaults to deactivate-not-delete and flags any deletion request for attorney decision.
- **Take inventory.** Cowork captures every platform (Facebook, Instagram, Twitter/X, TikTok, Snapchat, dating apps, messaging apps, gaming chat, livestream archives) and notes what's locked, what's preserved, and what's still open.
- **Family-account hygiene.** Family members tagging the client in posts, posting about the case, or speculating publicly all create evidence problems. The client signs a separate request to family asking them not to post about the case. Cowork drafts that letter.

The lockdown worksheet is signed by the client (so the firm has a record the client agreed to the lockdown protocol and was warned not to delete).

### D.4 — Jail call hygiene warning

If the client is in custody, **every jail call is recorded and discoverable.** Many jurisdictions also record visitation. Calls to the attorney are theoretically privileged but in practice can be intercepted or improperly disclosed; calls to anyone else are unprotected.

Cowork produces the jail-call-hygiene client letter (templates from `dw-jail-call-analyzer-crim`) covering:

- Do not discuss the facts of the case with anyone other than the attorney
- Do not discuss the case with family members on jail phones — assume the prosecutor is listening
- Do not have anyone three-way the attorney into a jail call (this often breaks privilege under the local jail's terms of use)
- Do not write letters about the case to anyone except the attorney
- Do not have cellmates relay messages
- Visitation conversations are typically recorded — assume so
- If the attorney is not yet on the visitation list, inform the client to sit silent on calls about the case until the attorney visits

**Route:** Letter is sent to the client at the jail. If the client is out on bond, replace the jail-call section with a general "do not discuss the case with anyone other than your attorney" letter.

### D.5 — No-contact considerations

- If a no-contact order is in place (with alleged victim, witnesses, co-defendants), capture it, instruct the client on its scope, and flag any social media or family-channel risk
- If no order is in place but an alleged victim is present in the client's life (domestic situation, shared workplace, shared children), the attorney decides whether a self-imposed no-contact protocol is wise
- Co-defendant contact carries Rule 1.7 implications for the firm AND can support charges of obstruction or witness tampering — instruct the client not to communicate with co-defendants directly. All inter-defense communication goes attorney-to-attorney.

### D.6 — Surrender vs. warrant posture

If a warrant is pending and the client is not yet arrested:
- Capture the warrant details (issuing parish, date issued, charge listed)
- Decide whether to negotiate a surrender (typically lower booking trauma, often better bond posture) versus waiting for arrest
- Coordinate with the issuing agency on a controlled surrender date and time
- If surrender is the plan, prepare the bond motion in advance so it can be filed at first appearance

### D.7 — Devices and digital footprint

- **Do not delete anything.** Deletion of texts, photos, location history, app data, or accounts during a pending investigation is potential obstruction and is itself often discoverable through forensic recovery
- **Preserve passwords.** The client provides every device password to the firm in writing (sealed, kept in the case file). Without passwords, defense forensic examiners cannot work, and the client may face contempt or an adverse inference if compelled to produce data
- **Identify what is in police custody.** Phones, computers, vehicles, residence (post-search) — capture what was seized, when, on what authority (warrant? consent? search-incident?)
- **Identify what is still in client/family custody.** Cloud backups, secondary devices, family devices that synced with client accounts, vehicle infotainment, smart speakers, home camera DVRs. Lock these down for investigator review.
- **Cloud accounts.** Apple, Google, Microsoft, Dropbox, encrypted-messaging archives — preserve, do not modify
