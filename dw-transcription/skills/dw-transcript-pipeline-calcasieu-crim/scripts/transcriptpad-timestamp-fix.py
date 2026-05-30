#!/usr/bin/env python3
"""
TranscriptPad Timestamp Fix Script

Parses JusticeText .txt transcript exports, extracts [MM:SS] or [HH:MM:SS] timestamps,
converts to milliseconds for ZTIMECODEMS, and reformats text as ':SS - Speaker - Content'
matching TranscriptPad's expected format.

USAGE:
  1. Update EVIDENCE_PATH to the client's evidence folder
  2. Update CASE_PATHS with both .tracase locations (evidence folder + iCloud)
  3. Update TRANSCRIPT_FILES mapping: transcript Z_PK -> source .txt file path
  4. Close TranscriptPad
  5. Run: python3 /tmp/fix_timestamps.py
  6. Reopen TranscriptPad and verify

WHAT THIS SCRIPT DOES:
  - For each transcript ID in TRANSCRIPT_FILES:
    1. Reads the corresponding .txt file
    2. Skips the JusticeText header (everything before the === separator)
    3. Extracts [MM:SS] Speaker: blocks using regex
    4. Converts timestamps to milliseconds
    5. Formats text as '  :SS - Speaker - Content'
    6. Deletes existing ZTRATRANSCRIPTLINE rows for that transcript
    7. Inserts new rows with proper ZTIMECODEMS and formatted ZTEXT
    8. Updates Z_PRIMARYKEY max for entity type 9
TIMESTAMP RENDERING:
  TranscriptPad splits timestamp display between two areas:
  - Left margin (blue column): Shows MM: derived from ZTIMECODEMS
  - Text body start: Shows :SS from the ZTEXT prefix
  Combined: "02:" in margin + ":06 - Speaker - text" = 02:06 full timestamp
"""

import sqlite3
import re
import os
import sys

# ============================================================================
# CONFIGURATION -- Update these for each case
# ============================================================================

# Base evidence folder path
EVIDENCE_PATH = "/path/to/client/evidence/folder"

# Both .tracase locations to update (evidence folder copy + iCloud copy)
CASE_PATHS = [
    os.path.join(EVIDENCE_PATH, "ClientName.tracase"),
    os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/LIT SUITE/TranscriptPad/ClientName.tracase"),
]

# Transcript Z_PK -> source .txt file path
# Get transcript PKs from: SELECT Z_PK, ZTITLE FROM ZTRATRANSCRIPT;
TRANSCRIPT_FILES = {
    # 1: os.path.join(EVIDENCE_PATH, "transcript1.txt"),
    # 2: os.path.join(EVIDENCE_PATH, "subfolder/transcript2.txt"),
}
# ============================================================================
# PARSING FUNCTIONS
# ============================================================================

def parse_timestamp(ts_str):
    """Convert [HH:MM:SS] or [MM:SS] string to milliseconds."""
    parts = ts_str.split(':')
    if len(parts) == 3:
        h, m, s = int(parts[0]), int(parts[1]), int(parts[2])
    elif len(parts) == 2:
        h = 0
        m, s = int(parts[0]), int(parts[1])
    else:
        return 0
    return (h * 3600 + m * 60 + s) * 1000


def parse_transcript_file(filepath):
    """
    Parse a JusticeText .txt file into transcript lines.

    JusticeText format:
        [Header info]
        ================================================
        [MM:SS] Speaker Name:
        Text content spanning one or more lines.

        [MM:SS] Another Speaker:
        More text content.

    Returns list of dicts: {timecode_ms, speaker, text}
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip header (everything before the === separator line)
    separator_idx = content.find('=' * 10)
    if separator_idx != -1:
        content = content[content.index('\n', separator_idx) + 1:]

    # Pattern: [MM:SS] or [HH:MM:SS] followed by Speaker Name:
    # Then text content until the next timestamp block or end of file
    pattern = r'\[(\d{1,2}:\d{2}(?::\d{2})?)\]\s+(.+?):\s*\n(.*?)(?=\n\[\d{1,2}:\d{2}|\Z)'

    matches = re.findall(pattern, content, re.DOTALL)

    lines = []
    for ts_str, speaker, text in matches:
        timecode_ms = parse_timestamp(ts_str)
        # Clean up text - remove extra whitespace/newlines, collapse into single line
        clean_text = ' '.join(text.strip().split())
        if clean_text:
            # Format seconds portion for display
            total_seconds = timecode_ms // 1000
            seconds = total_seconds % 60

            # Format as ':SS - Speaker - Text' matching TranscriptPad convention
            formatted_text = f"  :{seconds:02d} - {speaker.strip()} - {clean_text}"

            lines.append({
                'timecode_ms': timecode_ms,
                'text': formatted_text,
                'speaker': speaker.strip(),
            })

    return lines
# ============================================================================
# DATABASE FUNCTIONS
# ============================================================================

def update_database(db_path, transcript_id, lines):
    """Update the TranscriptPad database with properly formatted lines."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Delete existing lines for this transcript
    cursor.execute("DELETE FROM ZTRATRANSCRIPTLINE WHERE ZPARENTTRANSCRIPT = ?", (transcript_id,))

    # Get the current max Z_PK across all transcript lines
    cursor.execute("SELECT MAX(Z_PK) FROM ZTRATRANSCRIPTLINE")
    max_pk = cursor.fetchone()[0] or 0

    # Z_ENT for TRATranscriptLine is always 9
    z_ent = 9

    # Insert new lines
    for i, line in enumerate(lines):
        pk = max_pk + i + 1
        physical_line = i + 1
        page_num = 1  # Audio/video transcripts always use page 1
        line_on_page = i + 1
        text_length = len(line['text'])
        cursor.execute("""
            INSERT INTO ZTRATRANSCRIPTLINE (
                Z_PK, Z_ENT, Z_OPT,
                ZHIGHLIGHTCOLOR, ZISCONTINUATION, ZISFOOTER, ZISHEADER,
                ZISMARKED, ZISQUESTION, ZISREDACTED,
                ZLENGTH, ZPHYSICALLINENUMBER, ZTIMECODEMS,
                ZTRANSCRIPTLINENUMBER, ZTRANSCRIPTPAGENUMBER,
                ZUNDERSCORECOLOR, ZFLAG, ZFLAGIBEGIN, ZFLAGIEND,
                ZPARENTTRANSCRIPT, ZTEXT, ZUNREDACTEDTEXT
            ) VALUES (
                ?, ?, 1,
                0, 0, 0, 0,
                0, 0, 0,
                ?, ?, ?,
                ?, ?,
                0, NULL, NULL, NULL,
                ?, ?, NULL
            )
        """, (
            pk, z_ent,
            text_length, physical_line, line['timecode_ms'],
            line_on_page, page_num,
            transcript_id, line['text']
        ))

    # Update Z_PRIMARYKEY max for TRATranscriptLine (Z_ENT=9)
    new_max = max_pk + len(lines)
    cursor.execute("UPDATE Z_PRIMARYKEY SET Z_MAX = ? WHERE Z_ENT = 9", (new_max,))

    conn.commit()
    conn.close()

    return len(lines)
# ============================================================================
# MAIN
# ============================================================================

def main():
    if not TRANSCRIPT_FILES:
        print("ERROR: No transcript files configured. Update TRANSCRIPT_FILES dict.")
        sys.exit(1)

    for transcript_id, txt_path in TRANSCRIPT_FILES.items():
        print(f"\nProcessing transcript {transcript_id}: {os.path.basename(txt_path)}")

        if not os.path.exists(txt_path):
            print(f"  WARNING: File not found: {txt_path}")
            continue

        # Parse the transcript
        lines = parse_transcript_file(txt_path)
        print(f"  Parsed {len(lines)} timestamped lines")

        if not lines:
            print(f"  WARNING: No lines parsed! Check file format.")
            continue

        # Show sample
        for sample in lines[:3]:
            print(f"    {sample['timecode_ms']}ms | {sample['text'][:80]}")

        # Update both database locations
        for case_path in CASE_PATHS:
            db_path = os.path.join(case_path, "StoreContent", "persistentStore")
            if os.path.exists(db_path):
                count = update_database(db_path, transcript_id, lines)
                print(f"  Updated {count} lines in {os.path.basename(case_path)}")
            else:
                print(f"  DB not found: {db_path}")

    print("\nDone! All transcripts updated with proper timestamps.")
    print("Open TranscriptPad and click each transcript to verify rendering.")

if __name__ == '__main__':
    main()