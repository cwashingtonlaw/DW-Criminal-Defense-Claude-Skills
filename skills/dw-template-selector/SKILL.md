---
name: dw-template-selector
description: >
  Shared template selection protocol for all Daniels & Washington pleading-drafting skills.
  This skill is NOT triggered directly by user prompts — it is read as a reference protocol
  by other D&W skills before they draft legal pleadings. It standardizes how DEVONthink
  search results are presented, ranked, and selected so the attorney always chooses the
  template before drafting begins. If you are a pleading skill and your SKILL.md says to
  read this protocol, read it now and follow it before proceeding to draft.
---

# Daniels & Washington — Template Selection Protocol
**Version 1.1 | Internal Reference Protocol — Not a Direct-Trigger Skill**
**Attorney Work Product | Confidential**

---

## Purpose

This protocol governs how all D&W pleading-drafting skills search DEVONthink for firm templates and prior filings, present results to the attorney, and obtain template selection before any drafting begins.

**The Template-First Drafting Rule is firm policy.** No pleading skill drafts from scratch until DEVONthink has been searched and the attorney has been given the opportunity to select a template. This rule applies even when the attorney says "just draft it" — run the search first, present results, then draft.

---

## Step 1 — Run DEVONthink Template Search

Search `Law Library-Criminal` using motion-type-specific keywords. Every pleading skill defines its own search terms — use those. The standard search pattern is:

```
devonthink:search
query: "[motion-type-specific keywords]"
databaseName: Law Library-Criminal
groupPath: /Motions/[Relevant Subfolder]
limit: 15
```

Also run a broader tag-based search:
```
devonthink:search
query: tag:template OR tag:motion OR "[motion type]"
databaseName: Law Library-Criminal
limit: 10
```

**Also check the LA Criminal Trial Practice Formulary** if it is in DEVONthink — it is a primary template source for standard motion types.

---

## Step 2 — Rank and Present Results

After the search, present results to the attorney using the following ranked format. Do not skip this step even if only one result is found.

### Ranking Priority (highest to lowest)

| Rank | Type | Why It Ranks Here |
|------|------|-------------------|
| 1 | Firm template (tagged `template`) | Built for reuse — exact structure and language the firm uses |
| 2 | Prior approved filing (won or unchallenged) | Tested in court — real-world validated |
| 3 | Prior draft filing | Familiar format — may need updated authority |
| 4 | LA Criminal Trial Practice Formulary entry | Authoritative Louisiana-specific starting point |
| 5 | Reference article / CLE material | Useful for argument structure but not a draft template |

### Presentation Format

Present results as a numbered selection list:

---

**📂 DEVONthink Template Search Results — [Motion Type]**

Found **[N]** result(s) in `Law Library-Criminal`:

| # | Document | Type | Date | Notes |
|---|----------|------|------|-------|
| 1 | [Document name] | Firm Template | [Date] | [Brief note — e.g., "Used in State v. Jones, suppression granted"] |
| 2 | [Document name] | Prior Filing | [Date] | [Brief note] |
| 3 | [Document name] | Formulary | — | [Brief note] |

**→ Which template should I use as the base? Enter a number, or type "none" to draft from scratch.**

---

If no results are found:

---

**📂 DEVONthink Template Search Results — [Motion Type]**

No templates or prior filings found in `Law Library-Criminal` for this motion type.

**→ Drafting from scratch using this skill's structure. After attorney approval, offer to save the final version as a new firm template.**

---

## Step 3 — Load Selected Template

Once the attorney selects a template:

1. **Retrieve the full document** from DEVONthink using `devonthink:get_record_content` or `devonthink:get_record_by_identifier`
2. **Confirm the document loaded** — display the title and page/word count
3. **Identify reusable structure** — note which sections (caption, argument headings, citations, conclusion) will carry forward
4. **Proceed to the calling skill's drafting workflow** — update the template with case-specific facts, current authority, and client details

If the attorney selects "none," proceed directly to the calling skill's from-scratch drafting workflow.

---

## Step 4 — Post-Draft Template Save Offer

After the attorney approves a final draft (especially one drafted from scratch or substantially revised), offer to save it as a firm template:

> "Would you like me to save this motion as a firm template in DEVONthink? I'll tag it `template` and `[motion type]` and place it in `/Motions/[subfolder]` so it appears in future searches."

If yes, use `devonthink:create_record` to save the approved `.docx` or markdown version with appropriate tags.

---

## Integration Rules for Calling Skills

When another D&W skill reads this protocol, it must:

1. **Run the DEVONthink search before asking the attorney any intake questions** — the template search is Step 1, not Step 3.
2. **Block drafting until template selection is complete** — present the selection list and wait for attorney input.
3. **Preserve the selected template's structure and language** — only replace case-specific facts, dates, parties, and citations.
4. **Flag deviations** — if the current case requires an argument not in the template, note it as an addition rather than silently inserting it.
5. **Never present a blank draft** — even "draft from scratch" must follow the calling skill's defined structure, not a blank page.

---

## Skill Ecosystem

This protocol is read by the following D&W pleading skills:

| Skill | Motion Type |
|-------|-------------|
| `dw-suppression-motion` | Suppression / Fourth and Fifth Amendment |
| `dw-pretrial-motion-library` | Speedy trial, bill of particulars, continuance, compel, severance, venue, recusal, quash, competency, reveal the deal |
| `dw-bond-and-release-motion` | Bond reduction / pretrial release / PR bond |
| `dw-404b-opposition` | Opposition to Prieur / 404(b) notice |
| `dw-sentencing-mitigation-specialist` | Sentencing memorandum / mitigation |
| `dw-video-evidence-auditor` | Video evidence audit report (template selection for report output) |

**When any of the above skills loads this file, it should treat this protocol as mandatory — not optional guidance.**

---

## DEVONthink Tool Reference

| Tool | Use |
|------|-----|
| `devonthink:search` | Run keyword and tag searches |
| `devonthink:get_record_by_identifier` | Load selected template by UUID |
| `devonthink:get_record_content` | Extract full text of selected template |
| `devonthink:create_record` | Save approved draft as new firm template |
| `devonthink:add_tags` | Tag saved templates with `template` + motion type |
| `devonthink:list_group_content` | Browse `/Motions/` folder structure |
