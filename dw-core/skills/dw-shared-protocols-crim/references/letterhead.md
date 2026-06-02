# Firm Letterhead

Canonical letterhead for all Daniels & Washington document-producing skills. Whenever a skill drafts a document that leaves the firm on firm letterhead — client and family letters, jail mail, records and preservation requests, demand/spoliation letters, engagement correspondence, and (per firm preference) filed pleadings — apply this letterhead. This is the single source of truth; do not hand-type the firm block or improvise a `[Firm Letterhead]` placeholder. When the firm's address, phone, partners, or branding change, edit this file once and every consuming skill picks it up.

> **Authority note (firm-identity discrepancy):** This letterhead reflects the firm's current branded stationery — **Daniels & Washington Law Firm, LLC, 38167 Post Office Road, Prairieville, LA 70769**. The filed-pleading `signature-block.md` and `dw-firm-style-guide.md` still carry an older **Lake Charles, LA 70601** address and the single-attorney line "Christopher J. Washington #31354." These are infrastructure files; the attorney should reconcile them deliberately (offices may legitimately differ between letterhead and a court signature block). Until reconciled, treat **this file** as authoritative for letterhead and `signature-block.md` as authoritative for the filed-pleading signature.

---

## 1. The letterhead block (exact text)

```
                    [D&W CREST LOGO]
                                                                  (see assets/dw-letterhead-logo.png)

                    DANIELS & WASHINGTON LAW FIRM, LLC
                    38167 Post Office Road  ·  Prairieville, LA 70769
                    Ph: 225-383-3800   ·   Fax: (225) 208-1567

   Partner:                                          Partner:
   CHRISTOPHER WASHINGTON                            HARRY DANIELS III
   Attorney at Law                                   Attorney at Law
   Direct #: (225) 304-6907                          Direct #: (225) 346-6280
   E-Mail: cjw@danielswashington.com                 E-Mail: hdiii@danielswashington.com
```

- **Typeface:** Century Schoolbook (regular for the contact block; bold for the firm name and partner names). The bundled font files ship inside `assets/dw-letterhead.docx`.
- **Motto:** the crest carries the banner **FIAT JUSTITIA RUAT CÆLUM** ("Let justice be done though the heavens fall"). It lives in the logo art — do not retype it as a text line.
- **Logo placement:** crest centered (or top-left, per the bundled template) above the firm name.
- **Two-partner layout:** Christopher Washington (left column) and Harry Daniels III (right column) beneath the centered address/phone line.

## 2. Markdown / plain-text rendering (for skill drafts)

Cowork produces drafts in markdown or plain text; the attorney assembles the signed final on the actual stationery (`assets/dw-letterhead.docx`). In a draft, render the letterhead as a compact header so the attorney can see placement and verify the contact details, then drop in the real artwork at assembly:

```
**DANIELS & WASHINGTON LAW FIRM, LLC**
38167 Post Office Road · Prairieville, LA 70769 · Ph: 225-383-3800 · Fax: (225) 208-1567
Christopher Washington, Attorney at Law (Direct 225-304-6907, cjw@danielswashington.com)
Harry Daniels III, Attorney at Law (Direct 225-346-6280, hdiii@danielswashington.com)

— FIAT JUSTITIA RUAT CÆLUM —
________________________________________________________________________________
```

Place this block at the top of the first page only. Subsequent pages are plain (no repeated letterhead) unless the attorney requests a running header.

## 3. When to apply letterhead

| Document | Letterhead? | Notes |
|---|---|---|
| Client letter, jail mail, family letter | **Yes** | First page only. Privilege marking line (per `dw-firm-style-guide.md` §6) sits below the letterhead. |
| Records request, evidence-preservation / spoliation / litigation-hold letter | **Yes** | Replaces any `[Firm Letterhead]` placeholder in the source template. |
| Engagement / representation letter | **Yes** | Final signed engagement letter is on letterhead; Cowork drafts the body. |
| Demand / opposing-counsel correspondence | **Yes** | First page only. |
| Filed motion, opposition, memo, sentencing memo, proposed order | **Firm preference — see below** | The **court caption is the controlling header** for any filed pleading. By firm convention letterhead may appear above the caption; the caption, signature block (`signature-block.md`), and certificate of service are never replaced by letterhead. Do **not** apply privilege/work-product marking to filed pleadings. |
| Internal work product (Case Brain, audits, matrices, cross outlines) | **No** | Internal deliverables use work-product marking, not letterhead. |

> **Letterhead vs. caption (important):** A filed pleading's identity comes from its caption, not letterhead. Placing letterhead on a court filing is a firm style choice, not a legal requirement; some clerks/judges prefer captions alone. When in doubt on a filed pleading, lead with the caption and confirm letterhead placement with the attorney.

## 4. Variables (if a consuming skill prefers tokens)

Most skills should inline the block in §1/§2 verbatim. If a skill instead resolves firm fields from config, these are the canonical current values — keep them in sync with this file:

- `{{FIRM_NAME}}` = Daniels & Washington Law Firm, LLC
- `{{FIRM_ADDRESS_LINE_1}}` = 38167 Post Office Road
- `{{FIRM_ADDRESS_LINE_2}}` = Prairieville, LA 70769
- `{{FIRM_PHONE}}` = 225-383-3800
- `{{FIRM_FAX}}` = (225) 208-1567
- `{{PARTNER_1}}` = Christopher Washington — Direct (225) 304-6907 — cjw@danielswashington.com
- `{{PARTNER_2}}` = Harry Daniels III — Direct (225) 346-6280 — hdiii@danielswashington.com
- `{{FIRM_MOTTO}}` = FIAT JUSTITIA RUAT CÆLUM

## 5. Bundled assets

- `assets/dw-letterhead-logo.png` — the D&W crest (434×392 PNG, transparent background) for embedding in DOCX/PDF finals.
- `assets/dw-letterhead.docx` — the firm's editable letterhead stationery (logo in header, Century Schoolbook fonts embedded). **This is the file the attorney assembles signed correspondence on.**
- `assets/dw-letterhead.pdf` — flattened reference copy for visual confirmation of the canonical layout.

## 6. Guardrails

- Never fabricate or guess firm contact details — use the values in this file exactly.
- Cowork drafts the letter body and shows letterhead placement; the **attorney produces the signed final on `dw-letterhead.docx`**. A markdown draft is never the sent document.
- Do not place letterhead and attorney-work-product marking on the same outward-facing letter — letterhead is for documents that leave the firm; work-product marking is for internal deliverables.
- If the address/phone/partners on the bundled `.docx` ever diverge from §1, the `.docx` controls and this file must be updated to match.
