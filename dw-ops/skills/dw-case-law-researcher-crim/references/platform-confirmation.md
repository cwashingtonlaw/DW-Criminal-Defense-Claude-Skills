# Platform Confirmation Prompt

Read at SKILL.md Standalone Research Workflow — Step 1; holds the required platform-menu prompt, the tailoring rule, and the service-layer exception when another D&W skill calls this researcher.

**REQUIRED — Platform Confirmation**: Because this skill spans multiple research platforms with different speeds, costs, and coverage, always present the available sources and ask the attorney which ones to use before running any searches. Present them like this:

> **Which platforms should I search?**
> 1. **case.dev** — case law & statutes, API-based, fast
> 2. **CourtListener** — 9M+ opinions, semantic search, citation verification, free
> 3. **DEVONthink** — firm library, prior work product, templates
> 4. **Consensus** — academic/empirical research (200M+ papers)
> 5. **Westlaw / Fastcase / OpenCase** — premium databases, requires browser login
>
> I'd recommend [1, 2, 3] for this issue. Want me to run all of those, or a different combination?

Tailor the recommendation to the request — e.g., suggest Consensus only when empirical research is relevant, suggest Westlaw only when KeyCite/Shepard's validation is needed. But always let the attorney confirm before executing.

**Exception — called by another skill**: When invoked as a service layer by another D&W skill (e.g., `dw-suppression-motion-crim` calls for authority), use the calling skill's platform preferences if specified. If not specified, default to case.dev + CourtListener + DEVONthink (Tiers 1A + 1B + 2) without asking, since the attorney already initiated the parent workflow. The attorney can always say "also run Westlaw" or "skip DEVONthink" to override.
