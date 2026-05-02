---
name: dw-pi-video-generator
category: ops
description: >
  Generate personal injury video scripts and trigger HeyGen avatar video creation for Daniels & Washington.
  ALWAYS invoke for "PI video," "personal injury video," "make a video about," "video script,"
  "generate a video," "TikTok script," "Reels script," "Shorts script," "social media video,"
  "content for social media," "video idea," "what should I post about," "next video topic,"
  "run the video pipeline," "create a video about [PI topic]," or any request to produce
  short-form video content for the firm's personal injury practice.
  Produces 60-second scripts with platform-specific captions for TikTok, Instagram, YouTube, and Facebook.
  Can trigger HeyGen MCP to generate the actual avatar video if the HeyGen MCP server is connected.
  Do NOT use for criminal defense content. Do NOT use for long-form video or CLE presentations.
---

# PI Video Generator — Daniels & Washington

Generate 60-second personal injury video scripts optimized for AI avatar delivery (HeyGen) and
multi-platform social posting (TikTok, Instagram Reels, YouTube Shorts, Facebook).

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any video assets, scripts, client photos, case fact sheets, or PI imagery, do not start scripting yet.**

Your only response must be:

> *"Before I begin — are you uploading any additional video assets, scripts, client photos, case fact sheets, or PI imagery? I'll start the script and caption generation only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads, including b-roll references and brand-style guides sent mid-session, and to batch-mode runs where the attorney is feeding multiple topics at once.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before generating any script or caption, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — final published video content is firm marketing (public-facing), not work product, but pre-publication script drafts kept in the case/marketing folder are internal until approved; mark drafts accordingly.
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths. PI marketing content is not anchored to a single criminal defense case; this skill writes to the firm's marketing folder rather than `{{CASE_ROOT}}`. Where a single client case is the source for a video (e.g., a specific verdict or a redacted client story), the source-fact citations anchor to that `{{CASE_ROOT}}`.

Do not proceed to Step 1 until these protocols are loaded. Output paths for this skill follow the Marketing-Content formula (see "Output Paths" section below) — they are NOT under a per-case `{{CASE_ROOT}}` because PI marketing scripts are firm-wide content, but any case-derived facts in a script must trace back to that case's `{{CASE_ROOT}}`.

---

## Source Citation Mandate

Every factual or legal claim made in a PI video script must trace back to a specific source. The firm's name and reputation ride on every avatar video — a misstated prescriptive period, an outdated rule on direct action, or a fabricated statistic creates LSBA advertising-rule exposure and erodes consumer trust.

**Citation format (in script comments / production notes, not in the on-screen narration):** Cite the statute, code article, dataset, or firm document. Examples:
- `(La. C.C. art. 3492 — one-year prescription, personal injury)`
- `(La. R.S. 22:1269 — direct action statute)`
- `(LA Highway Safety Research Group, 2024 Annual Report, p. 12)`
- `(Firm intake data, Q1 2026 — prepared by [staff], on file with marketing)`
- `(Firm verdict — [Case Name, Year], settlement [REDACTED])`

**Multiple-source rule:** When a legal claim has both a statutory and a case-law foundation, cite both — `(La. C.C. art. 2315 + Pierre v. Allstate, 2023 La.)`.

**Unsourced assertions:** If a claim cannot be sourced to statute, code, regulation, peer-reviewed data, or firm-verified records, mark it `[UNSOURCED — VERIFY]` in the production notes and exclude from the script until resolved. Do NOT generate scripts containing unsourced legal claims about Louisiana law — the compliance check in Step 4 must catch these.

**Where sourcing applies:** Every legal claim in the body (prescription, comparative fault, direct action, insurance coverage, liability standards), every statistic cited, and any reference to firm performance. Generic safety advice ("buckle up") and pure pathos ("we know it's a hard time") do not require citation.

---

## When to Use This Skill

**Use this skill whenever anyone asks:**
- "Make a PI video about [topic]"
- "Write a video script about car accidents"
- "What should I post about today?"
- "Generate a video for social media"
- "TikTok script about insurance tactics"
- "Next video topic"
- "Run the video pipeline"
- "Create a video about [any PI topic]"
- "Give me 5 video ideas"
- "Batch me a week of scripts"

This skill handles **ideation, scripting, and (optionally) video generation** for the firm's
automated PI content pipeline.

---

## Workflow

### Step 1: Determine the Topic

If the attorney specifies a topic, use it. If not, suggest from these categories:

**Read `references/topic-list.md`** for the full 35-topic rotation list organized by category.

When suggesting topics, consider:
- What's timely (hurricane season → property damage, summer → motorcycle accidents)
- What hasn't been covered recently
- What drives consultations (car accidents and insurance tactics perform best)

### Step 2: Generate the Script

Every script follows the **Hook → Body → CTA** structure:

**HOOK (0:00–0:03):** One bold question or surprising fact. Must stop the scroll.
- "Did you know Louisiana just changed a MAJOR injury law?"
- "The insurance company is NOT on your side — here's proof."
- "You have ONE YEAR to file your injury claim in Louisiana."

**BODY (0:03–0:50):** Two to three educational points in short, conversational sentences.
- Address the viewer directly ("you," "your")
- Use Louisiana-specific language (parishes, prescriptive periods)
- Plain language — 8th-grade reading level
- Each point builds: (1) the problem, (2) what the law says, (3) what to do

**CTA (0:50–1:00):** Always end with:
> "If you've been injured, call Daniels and Washington, Champions for Justice,
> right here in Lake Charles, Louisiana. Your consultation is free, and you
> don't pay unless we win."

**Target length:** 150–170 words (reads naturally at speaking pace in ~60 seconds).

### Step 3: Generate Platform-Specific Captions

For each script, produce ALL of these:

| Platform | Caption Style | Hashtags |
|----------|--------------|----------|
| **TikTok** | Short, punchy, 1-2 sentences + hashtags | 4-6: #lawtok #personalinjurylawyer #lakecharles #louisiana + 2 topic-specific |
| **Instagram** | Longer, educational paragraph + hashtags | 10-15: mix of broad PI + Louisiana + topic-specific |
| **YouTube** | Title (include #Shorts) + description | Title: "[Topic] #Shorts" / Description: 2-3 sentences + firm info |
| **Facebook** | Conversational, 2-3 sentences + hashtags | 2-3 hashtags only |

### Step 4: Apply Compliance Checks

**Read `references/compliance-rules.md`** before finalizing any script.

Every script and caption MUST pass these checks:
- [ ] No promised results or guaranteed outcomes
- [ ] Uses "may," "could," "might" for potential outcomes
- [ ] Includes attorney full name + "Lake Charles, Louisiana"
- [ ] Instagram and Facebook captions include the full disclaimer
- [ ] No comparisons to other firms
- [ ] No client testimonials without proper disclaimers

**Required disclaimer (Instagram & Facebook captions only):**
> This is educational information, not legal advice. No attorney-client relationship
> is created by viewing this content. Results may vary. This video uses AI-generated
> presentation technology. Content reviewed and approved by [Attorney Name], licensed
> in Louisiana.

### Step 5: Output Format

Present the deliverable in this exact structure:

```
📹 VIDEO: [Title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎬 SCRIPT (60 seconds, ~[X] words)
[Full script text]

📱 TIKTOK CAPTION
[Caption with hashtags]

📸 INSTAGRAM CAPTION
[Caption with hashtags and disclaimer]

▶️ YOUTUBE
Title: [Title #Shorts]
Description: [Description]

📘 FACEBOOK CAPTION
[Caption with hashtags and disclaimer]
```

### Step 6 (Optional): Trigger HeyGen Video Generation

If the HeyGen MCP server is connected (check for `create_video_agent` or `create_avatar_video` tools),
offer to generate the video immediately:

> "Want me to send this to HeyGen to create the avatar video now?"

If yes, use the HeyGen MCP `create_avatar_video` tool with:
- avatar_id: [the firm's custom avatar]
- voice_id: [the firm's cloned voice]
- input_text: [the script from Step 2]

Then monitor status with `get_video` and provide the download URL when ready.

If HeyGen MCP is NOT connected, inform the attorney:
> "The HeyGen MCP server isn't connected in this session. The script is ready —
> your Make.com pipeline will pick it up automatically, or you can paste it into
> HeyGen's dashboard manually."

---

## Batch Mode

When asked for multiple scripts (e.g., "give me a week of scripts" or "batch 5 videos"):

1. Select topics from `references/topic-list.md`, varying categories for content diversity
2. Generate each script with full captions
3. Present as a numbered list
4. If requested, output as a single document (use docx skill)

---

## Ad-Hoc vs. Pipeline

This skill serves **two purposes**:

1. **Ad-hoc generation** — Attorney asks Claude directly for a script. Claude generates it
   on the spot. Attorney can then paste into HeyGen manually or trigger via MCP.

2. **Pipeline support** — The Make.com automated pipeline calls the Claude API with the
   same system prompt and topic. The pipeline handles everything automatically.

Both paths use identical script structure and compliance rules. This skill ensures
consistency whether the attorney is working interactively or the pipeline is running
unattended.

---

## Output Paths

PI marketing content is firm-wide and is not anchored to a per-criminal-case `{{CASE_ROOT}}`. Apply the output-path formula from `dw-shared-protocols/references/output-path-formula.md` against the firm's marketing folder root:

```
{{FIRM_MARKETING_ROOT}}/PI Video Pipeline/Scripts/[YYYY-MM-DD] - [Topic Slug] - Script.docx
{{FIRM_MARKETING_ROOT}}/PI Video Pipeline/Captions/[YYYY-MM-DD] - [Topic Slug] - Captions.md
```

If a script is sourced from a specific client case (e.g., a verdict story with consent), the production notes must include a citation line that points back to that case's `{{CASE_ROOT}}` — for example: `Source case: {{CASE_ROOT}} (verdict file at 08 - Verdict_Sentencing/...)`. Apply attorney work-product marking per `dw-shared-protocols/references/attorney-work-product-marking.md` to script drafts until the attorney approves them for publication; published captions and on-air scripts get NO marking.

If `{{FIRM_MARKETING_ROOT}}` is not set, fall back to the active session's outputs directory and tell the attorney where the file landed.

---

## What This Skill Does NOT Do

- Criminal defense content (use dw-criminal-defense)
- Long-form video or CLE presentations (use pptx skill)
- Opus Clip clipping or repurposing (separate workflow)
- Post directly to social media (Make.com pipeline handles this)
- File LSBA advertising compliance paperwork (manual process)
