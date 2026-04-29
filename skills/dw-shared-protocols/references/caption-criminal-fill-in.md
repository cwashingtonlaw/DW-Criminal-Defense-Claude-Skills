# Caption — Fill-in Template (Unspecified Court)

Use this template when the case is in a Louisiana parish or court not yet covered by a dedicated caption file. The consuming skill MUST prompt the attorney for each variable before applying — never insert placeholder text into a final deliverable.

## Required prompts to attorney

Before drafting, the consuming skill must elicit:

1. **Court name** — full official name (e.g., "15TH JUDICIAL DISTRICT COURT", "JUVENILE COURT FOR THE PARISH OF JEFFERSON", "31ST JUDICIAL DISTRICT COURT")
2. **Parish** — full parish name (e.g., "PARISH OF LAFAYETTE")
3. **Docket/Case label** — does this court use "DOCKET NO." or "CASE NO." or another label?
4. **Section vs. Division** — does this court use "DIVISION" or "SECTION"?
5. **Section/Division designation** — letter, number, or roman numeral?
6. **Judge name** — assigned judge
7. **Defendant name** — as filed
8. **Docket/case number** — as assigned
9. **Any local caption peculiarities** — e.g., line for magistrate, special designation lines

## Suggested elicitation prompt

> I don't have a dedicated caption template for this court yet. To draft cleanly, I need:
>
> 1. Full court name (e.g., "15TH JUDICIAL DISTRICT COURT")?
> 2. Parish (e.g., "PARISH OF LAFAYETTE")?
> 3. Does this court use DOCKET NO. or CASE NO.?
> 4. Does it use DIVISION or SECTION?
> 5. Division/Section designation (letter/number/roman)?
> 6. Assigned judge?
> 7. Any local caption quirks I should know?
>
> If you can paste a sample caption from a recent filing in this court, that's the fastest route.

## Template (after elicitation)

```
STATE OF LOUISIANA              *    {{COURT_NAME}}
                                *
VERSUS                          *    {{PARISH_LINE}}
                                *
{{DEFENDANT_NAME}}              *    STATE OF LOUISIANA
                                *
{{DOCKET_LABEL}} {{NUMBER}}     *    {{DIVISION_OR_SECTION_LABEL}} "{{DESIGNATION}}"
                                *
                                *    JUDGE {{JUDGE_NAME}}
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

## Post-use action

After successfully using this fill-in template for a new court, the agent should:
1. Save the resolved caption to a draft file
2. Recommend that a permanent `caption-criminal-{{COURT_SLUG}}.md` reference be created and added to the manifest in `dw-shared-protocols/SKILL.md`
3. Do NOT auto-create the permanent reference file — surface the recommendation to the attorney for review.
