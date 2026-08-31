# dw-local-transcription-crim

Local, on-premises transcription and speaker identification for criminal discovery media.

Start at `SKILL.md`.

```
SKILL.md                                    workflow, hard stops, non-negotiables
references/
  pipeline-setup.md                         install, HF gating, MPS, failure table
  speaker-identification-protocol.md        SPEAKER_00 -> DET. RANDOLPH, with worked example
  media-integrity-audit.md                  the 8 MB ceiling, truncated exports, runtime checks
  front-matter-spec.md                      everything before the transcript body
  cleanup-and-flagging-rules.md             what to correct, what NEVER to correct
  louisiana-audio-conventions.md            Iowa/Lacassine/Hebert and the rest
  tiering-and-scope.md                      working vs court-reporter; how to size the job
assets/
  annotation-catalog.md                     the 12 annotation types, with language
  body_src_EXAMPLE.txt                      Q./A. source markup for the paginator
scripts/
  probe_media.py                            inventory + probe (run first, always)
  batch_transcribe.py                       extract, transcribe, diarize; resumable
  identify_speakers.py                      openings | anchor | compare
  prep_transcript.py                        paginate to 25-line court-reporter pages
  build_transcript_docx.js                  render the .docx (node; requires `docx`)
  gen_working_transcripts.py                per-item transcripts + master index
```

Typical run:

```bash
python scripts/probe_media.py "$CASE_ROOT"
HFTOK='hf_...' python scripts/batch_transcribe.py
python scripts/identify_speakers.py openings
python scripts/identify_speakers.py anchor "#38 Interview"      # confirm with attorney
python scripts/gen_working_transcripts.py --index-to "$CASE_ROOT/02 - Pretrial Notebook/03 - Case Analysis & Notes"
# then hand-author body_src.txt for the items getting court-reporter treatment
python scripts/prep_transcript.py body_src.txt pages.json
node scripts/build_transcript_docx.js pages.json transcript.docx
```

Requires: ffmpeg, python3 venv (mlx-whisper, pyannote.audio>=4, soundfile, numpy, torch,
python-docx), node with `docx`, and a HuggingFace read token with three pyannote repos granted.
