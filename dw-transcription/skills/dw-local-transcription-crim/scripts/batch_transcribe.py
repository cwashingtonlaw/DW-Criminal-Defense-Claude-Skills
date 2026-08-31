#!/usr/bin/env python3
"""Step 3: extract, transcribe, diarize. Resumable.

    HFTOK='hf_...' python batch_transcribe.py [workdir]

Reads media_probe.jsonl. Queues interview-class files FIRST, longest first, so a
crash at hour four costs surveillance footage rather than the client's statement.

Records extracted_dur against probed dur on every file -- that comparison IS the
media-integrity audit (see references/media-integrity-audit.md).
"""
import os, re, json, time, hashlib, subprocess, sys

H = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else "~/dw-asr")
B = os.path.join(H, "batch"); os.makedirs(B, exist_ok=True)
FFMPEG = os.environ.get("FFMPEG", "/opt/homebrew/bin/ffmpeg")
MODEL  = "mlx-community/whisper-large-v3-mlx"
DIAR   = "pyannote/speaker-diarization-community-1"
MIN_DUR = 10.0

INTERVIEW = re.compile(
    r"interview|interrogat|statement|\bcac\b|jail|call|911|mirand|confession|debrief", re.I)

rows = [json.loads(l) for l in open(os.path.join(H, "media_probe.jsonl"))]
queue = [r for r in rows if r.get("ok") and r.get("has_audio") and r["dur"] >= MIN_DUR]
for r in queue:
    r["id"] = hashlib.sha1(r["path"].encode()).hexdigest()[:12]
    r["iv"] = bool(INTERVIEW.search(r["path"]))
queue.sort(key=lambda r: (not r["iv"], -r["dur"]))
print(f"queue: {len(queue)} files, {sum(r['dur'] for r in queue)/3600:.1f} h; "
      f"interview-class {sum(1 for r in queue if r['iv'])}", flush=True)

import torch, numpy as np, soundfile as sf, mlx_whisper
from pyannote.audio import Pipeline

_pipe = None
def pipe():
    """Lazy-load; prefer MPS (~21x realtime vs ~2.3x on CPU)."""
    global _pipe
    if _pipe is None:
        _pipe = Pipeline.from_pretrained(DIAR, token=os.environ["HFTOK"])
        for dev in ("mps", "cpu"):
            try: _pipe.to(torch.device(dev)); print(f"  diarization device: {dev}", flush=True); break
            except Exception: continue
    return _pipe

man = open(os.path.join(H, "batch_manifest.jsonl"), "a")
for i, r in enumerate(queue):
    fid, path, dur = r["id"], r["path"], r["dur"]
    if os.path.exists(f"{B}/{fid}.json"): continue          # resume
    t0 = time.time(); rec = {"id": fid, "path": path, "dur": dur, "iv": r["iv"]}
    flac = f"{B}/{fid}.flac"
    try:
        if not os.path.exists(flac):
            # 16 kHz mono FLAC. NO filtering, gain, or normalization -- you may be
            # asked what you did to the evidence; "nothing" is the best answer.
            cp = subprocess.run([FFMPEG, "-y", "-v", "error", "-i", path, "-vn",
                                 "-ac", "1", "-ar", "16000", "-c:a", "flac", flac],
                                capture_output=True, timeout=1800, text=True)
            if cp.returncode or not os.path.exists(flac) or os.path.getsize(flac) < 5000:
                rec.update(status="EXTRACT_FAIL", err=(cp.stderr or "")[:200])
                man.write(json.dumps(rec) + "\n"); man.flush()
                print(f"[{i+1}/{len(queue)}] EXTRACT_FAIL {os.path.basename(path)[:50]}", flush=True)
                continue
        audio, sr = sf.read(flac, dtype="float32")
        got = len(audio) / sr
        rec["extracted_dur"] = round(got, 1)
        rec["short"] = got < dur * 0.9                       # <-- integrity flag
        w = mlx_whisper.transcribe(
            audio, path_or_hf_repo=MODEL, language="en",
            word_timestamps=True,
            condition_on_previous_text=False,                # suppress carry-over hallucination
            temperature=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
            compression_ratio_threshold=2.4, logprob_threshold=-1.0,
            no_speech_threshold=0.6, verbose=None)           # NO initial_prompt: never seed names
        json.dump(w, open(f"{B}/{fid}.json", "w"))
        rec["segs"] = len(w["segments"])
        if r["iv"] and got >= 30:
            try:
                out = pipe()(flac)
                import pickle; pickle.dump(out, open(f"{B}/{fid}.diar.pkl", "wb"))  # persist FIRST
                ann = out.exclusive_speaker_diarization      # no overlap -> use for mapping
                turns = [{"start": round(s.start, 3), "end": round(s.end, 3), "spk": l}
                         for s, _, l in ann.itertracks(yield_label=True)]
                json.dump(turns, open(f"{B}/{fid}.turns.json", "w"))
                if out.speaker_embeddings is not None:
                    np.save(f"{B}/{fid}.emb.npy", out.speaker_embeddings)
                rec["speakers"] = len({t["spk"] for t in turns})
            except Exception as e:
                rec["diar_err"] = f"{type(e).__name__}: {e}"[:150]
        if not r["iv"]:
            try: os.remove(flac)                              # keep FLAC only for interviews
            except OSError: pass
        rec.update(status="OK", secs=round(time.time() - t0))
    except Exception as e:
        rec.update(status="ERROR", err=f"{type(e).__name__}: {e}"[:200])
    man.write(json.dumps(rec) + "\n"); man.flush()
    print(f"[{i+1}/{len(queue)}] {rec['status']} {dur/60:.1f}m "
          f"spk={rec.get('speakers','-')} {os.path.basename(path)[:46]}", flush=True)
print("BATCH_DONE", flush=True)
