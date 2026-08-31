"""Step 6a: paginate a hand-authored Q./A. source into 25-line court-reporter pages.

    python prep_transcript.py body_src.txt pages.json

Source markers:
    Q. <text>          question by the current examiner
    A. <text>          answer
    @@TS hh:mm:ss      runtime marker
    @@EX DET. NAME     examiner change -> renders "BY DET. NAME:"
    @@END              stop

Emits pages.json for build_transcript_docx.js: 25 lines/page, wrapped to 61 cols,
plus runtime->page:line concordance, keyword and name frequencies.
"""
import json, re, textwrap
from collections import Counter

import sys
SRC = sys.argv[1] if len(sys.argv)>1 else "body_src.txt"
OUT = sys.argv[2] if len(sys.argv)>2 else "pages.json"
TEXTW = 61          # chars of text per line after the 6-char number gutter
LINES_PER_PAGE = 25

raw = open(SRC).read().splitlines()

turns = []          # (kind, text)  kind in {"Q","A","TS","PAREN"}
for ln in raw:
    if not ln.strip():
        continue
    if ln.startswith("@@TS "):
        turns.append(("TS", ln[5:].strip())); continue
    if ln.startswith("@@EX "):
        turns.append(("EX", ln[5:].strip())); continue
    if ln.startswith("@@END"):
        break
    if ln.startswith("Q. "):
        turns.append(("Q", ln[3:].strip())); continue
    if ln.startswith("A. "):
        turns.append(("A", ln[3:].strip())); continue
    turns.append(("C", ln.strip()))

# ---- wrap into physical lines -------------------------------------------
phys = []           # list of (text, ts_or_None)
for kind, txt in turns:
    if kind == "TS":
        phys.append(("", None))
        phys.append((f"                    (Runtime {txt})", txt))
        phys.append(("", None))
        continue
    if kind == "EX":
        phys.append(("", None))
        phys.append((f"     BY {txt}:", None))
        phys.append(("", None))
        continue
    if kind == "C":
        wrapped = textwrap.wrap(txt, width=TEXTW - 5) or [""]
        for i, w in enumerate(wrapped):
            phys.append(("     " + w, None))
        continue
    lead = f"{kind}.   "
    wrapped = textwrap.wrap(txt, width=TEXTW - len(lead)) or [""]
    phys.append((lead + wrapped[0], None))
    for w in wrapped[1:]:
        phys.append((" " * len(lead) + w, None))

# ---- paginate ------------------------------------------------------------
pages = []
for i in range(0, len(phys), LINES_PER_PAGE):
    chunk = phys[i:i + LINES_PER_PAGE]
    while len(chunk) < LINES_PER_PAGE:
        chunk.append(("", None))
    pages.append(chunk)

# ---- runtime index: runtime -> page:line --------------------------------
tsindex = []
for pi, pg in enumerate(pages, start=1):
    for li, (t, ts) in enumerate(pg, start=1):
        if ts:
            tsindex.append({"ts": ts, "page": pi, "line": li})

# ---- keyword counts over spoken text only -------------------------------
spoken = " ".join(t for k, t in turns if k in ("Q", "A")).lower()
words = re.findall(r"[a-z']+", spoken)
KEYWORDS = ["custody","support","lawyer","police","weekend","court","phone",
            "sheriff","paperwork","daycare","facetime","facebook","guns",
            "birthday","school","married","rights","consent","escalade","dice"]
kw = []
for k in KEYWORDS:
    n = sum(1 for w in words if w.startswith(k[:6]) and k[:6] in w)
    n = len(re.findall(r"\b" + k + r"[a-z']*\b", spoken))
    if n:
        kw.append({"word": k, "n": n})
kw.sort(key=lambda d: -d["n"])

NAMES = ["Courtney","Tucker","Tuck","Terel","Kodin","Chloe","Taronda",
         "Angelica","Jelly","Iselyn","Thomas","Kimball","Jordan","Nikki",
         "Randolph","Miller","Bradley","Lacassine","Morningside","Weaver"]
spoken_cased = " ".join(t for k, t in turns if k in ("Q", "A"))
nm = []
for n in NAMES:
    c = len(re.findall(r"\b" + n + r"\b", spoken_cased))
    if c:
        nm.append({"word": n, "n": c})
nm.sort(key=lambda d: -d["n"])

out = {"pages": [[t for t, _ in pg] for pg in pages],
       "tsindex": tsindex, "keywords": kw, "names": nm,
       "npages": len(pages), "nlines": len(phys),
       "words": len(words)}
json.dump(out, open(OUT, "w"))
print("pages:", len(pages), "phys lines:", len(phys), "spoken words:", len(words))
print("keywords:", kw[:12])
print("names:", nm[:14])
print("ts entries:", len(tsindex))
