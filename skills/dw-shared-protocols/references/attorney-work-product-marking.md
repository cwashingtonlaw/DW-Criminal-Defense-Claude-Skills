# Attorney Work Product Marking

Standard marking applied to **internal** D&W deliverables. NEVER applied to filed pleadings, proposed orders, or anything served on opposing counsel.

## Standard marking

```
ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL
PREPARED IN ANTICIPATION OF LITIGATION
```

## Placement rules by deliverable type

**Header (top of every page, right-justified or centered, 9-10 pt):**
- Case Brain
- Cross-examination outlines and chapters
- Discovery triage reports / ledgers
- Audit reports (Brady/Giglio, chain of custody, mobile forensic, etc.)
- Witness threat matrices
- Plea analysis memos
- Investigation tasking documents
- Voir dire dashboards (export form)

**Footer (bottom of every page, centered, 9 pt):**
- Trial notebook tabs and master index
- Source exhibit catalogs

**Watermark (diagonal, gray, 30-40% opacity):**
- Documents being shared with co-counsel or expert witnesses
- Sentencing mitigation packages prior to attorney finalization

**No marking:**
- Filed pleadings (motions, oppositions, memoranda, sentencing memoranda)
- Proposed orders
- Notices of hearing
- Certificates of service
- Anything served on the State / opposing counsel
- Client copies of filed pleadings (the filed version stands alone)

## Filed-vs-internal disambiguation

When a single skill produces both an internal draft AND a filed version (e.g., proposed jury instructions reviewed internally before submission):
- Internal review draft → marking applied
- Filed version → no marking

The skill must produce two outputs in this case, with the filed version saved without the marking and named clearly (e.g., `JuryInstructions_FILED.docx` vs. `JuryInstructions_DRAFT_INTERNAL.docx`).

## Format specifics

- Font: same family as document body (typically Times New Roman); size 9-10 pt for header/footer, 36-48 pt for watermark
- Color: black for header/footer, gray (RGB 180/180/180) for watermark
- Bold optional but consistent within a document
- Two lines, no period at end
- Apply via .docx header/footer XML, not body text — survives copy/paste better and doesn't disrupt page layout
