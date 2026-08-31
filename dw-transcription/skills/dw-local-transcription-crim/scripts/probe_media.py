#!/usr/bin/env python3
"""Step 1: inventory + probe every media file in a case tree.

    python probe_media.py "<CASE_ROOT>" [outdir]

Writes media_probe.jsonl: one record per file with bytes, duration, audio-stream
presence, codec. Reads container headers/trailers only, so it SUCCEEDS on files
whose payload cannot be retrieved -- that is how truncated productions surface.
Resumable: re-run to fill in gaps.
"""
import json, os, subprocess, sys, collections

EXT = {".mts",".mp4",".mov",".avi",".mkv",".wmv",".m4v",".mpg",".mpeg",".vob",
       ".wav",".mp3",".m4a",".aac",".wma",".flac",".amr",".ogg",".opus",".3gp",".dvr-ms"}
FFPROBE = os.environ.get("FFPROBE", "/opt/homebrew/bin/ffprobe")

def main():
    root = sys.argv[1]
    out_dir = os.path.expanduser(sys.argv[2] if len(sys.argv) > 2 else "~/dw-asr")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "media_probe.jsonl")

    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: done.add(json.loads(line)["path"])
            except Exception: pass

    files = []
    for dirpath, _, names in os.walk(root):
        for n in names:
            if os.path.splitext(n)[1].lower() in EXT:
                files.append(os.path.join(dirpath, n))
    print(f"{len(files)} media files found; {len(done)} already probed", flush=True)

    fh = open(out, "a")
    for i, p in enumerate(files):
        if p in done: continue
        rec = {"path": p}
        try: rec["bytes"] = os.path.getsize(p)
        except OSError: rec["bytes"] = 0
        try:
            r = subprocess.run(
                [FFPROBE, "-v", "error", "-show_entries", "format=duration",
                 "-show_entries", "stream=codec_type,codec_name,channels,sample_rate",
                 "-of", "json", p], capture_output=True, timeout=90, text=True)
            d = json.loads(r.stdout or "{}")
            rec["dur"] = float(d.get("format", {}).get("duration") or 0)
            audio = [s for s in d.get("streams", []) if s.get("codec_type") == "audio"]
            rec["has_audio"] = bool(audio)
            if audio:
                rec["acodec"] = audio[0].get("codec_name")
                rec["ch"] = audio[0].get("channels")
                rec["sr"] = audio[0].get("sample_rate")
            rec["ok"] = rec["dur"] > 0
            if r.stderr.strip(): rec["err"] = r.stderr.strip()[:200]
        except Exception as e:
            rec["ok"] = False; rec["err"] = f"{type(e).__name__}: {e}"[:200]
        fh.write(json.dumps(rec) + "\n"); fh.flush()
        if i % 25 == 0: print(f"  {i}/{len(files)}", flush=True)

    rows = [json.loads(l) for l in open(out)]
    ok  = [r for r in rows if r.get("ok")]
    aud = [r for r in ok if r.get("has_audio")]
    sil = [r for r in ok if not r.get("has_audio")]
    bad = [r for r in rows if not r.get("ok")]
    hm = lambda s: "%d h %02d m" % (s // 3600, (s % 3600) // 60)
    print(f"\nprobed {len(rows)}   readable {len(ok)}   FAILED {len(bad)}")
    print(f"  with audio  : {len(aud):4d}   {hm(sum(r['dur'] for r in aud))}   <-- transcription scope")
    print(f"  silent video: {len(sil):4d}   {hm(sum(r['dur'] for r in sil))}")
    print(f"  unreadable  : {len(bad):4d}")
    ext = collections.Counter(os.path.splitext(r["path"])[1].lower() for r in aud)
    print("  audio-bearing by type:", dict(ext))
    for r in bad[:10]:
        print("   FAIL:", os.path.basename(r["path"])[:60], "|", (r.get("err") or "")[:70])

if __name__ == "__main__":
    main()
