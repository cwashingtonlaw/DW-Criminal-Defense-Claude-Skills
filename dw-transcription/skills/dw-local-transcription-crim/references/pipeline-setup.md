# Pipeline Setup

One-time setup on the machine that holds the files. Everything runs locally.

---

## Where this can and cannot run

**Runs on:** the firm workstation holding the discovery media. Apple Silicon strongly preferred — the
MPS speedup is a 9× difference on diarization.

**Does NOT run in a cloud sandbox.** Anthropic's egress proxy returns **HTTP 403** for
`huggingface.co`, `hf-mirror.com`, and `openaipublic.azureedge.net`. No ASR or diarization model can be
downloaded there. Don't spend twenty minutes rediscovering this.

**Does NOT run through a remote-device bridge mount.** Sustained sequential reads of multi-gigabyte
files through a re-exported filesystem fail (`Resource deadlock avoided`, `Operation timed out`) where
the same read succeeds natively. Extract on the machine that owns the disk.

---

## Install

```bash
# FFmpeg
brew install ffmpeg

# Isolated environment — do not install into system Python
mkdir -p ~/dw-asr && cd ~/dw-asr
python3 -m venv venv
./venv/bin/pip install --upgrade pip
./venv/bin/pip install mlx-whisper soundfile numpy "pyannote.audio>=4.0"
```

Verify:

```bash
./venv/bin/python -c "import mlx_whisper, pyannote.audio, soundfile, torch; \
print('whisper+pyannote ok', pyannote.audio.__version__, torch.__version__)"
which ffmpeg ffprobe
```

---

## HuggingFace access

pyannote models are gated. Free account, instant approval, no review queue.

1. Create an account at **huggingface.co** and verify the email.
2. Accept terms on **all three** — a click each:
   - `huggingface.co/pyannote/segmentation-3.0`
   - `huggingface.co/pyannote/speaker-diarization-3.1`
   - `huggingface.co/pyannote/speaker-diarization-community-1`
3. **Settings → Access Tokens → Create new token → type `Read`.** Not Write, not Fine-grained.
4. Copy it at creation — shown once.

**Why all three.** `speaker-diarization-3.1` declares `segmentation-3.0` and
`wespeaker-voxceleb-resnet34-LM` in its config, but **pyannote.audio 4.x redirects the 3.1 alias to
`speaker-diarization-community-1`** and pulls embedding assets from it. Granting only the two named in
the 3.1 config fails at runtime with `GatedRepoError` on `community-1/plda/xvec_transform.npz`.

**Do not try to dodge this by pinning pyannote 3.3.2.** It won't import against torch ≥2.13 —
`pyannote/audio/core/io.py` uses removed torchaudio backend APIs. Grant the third repo.

Pass the token by environment variable. Never write it to a script:

```bash
HFTOK='hf_...' ./venv/bin/python diarize.py
```

Tell the attorney to delete the token when the run is finished.

---

## Device selection

**Always try MPS first.** Measured on an Apple M4 Pro, 24 GB, 63 minutes of audio:

| Device | Time | Realtime factor |
|---|---|---|
| **MPS** | ~3 min | **~21×** |
| CPU | 27+ min | ~2.3× |

Same output. Roughly 9× the throughput. This is the difference between diarizing a whole case and
diarizing one interview.

```python
import torch
pipe.to(torch.device("mps"))   # fall back to "cpu" only if MPS raises
```

Whisper large-v3 via MLX runs ~5–7× realtime; the end-to-end batch including Drive fetch, extraction,
transcription and diarization measured **9.7× realtime** across 36.6 hours of audio.

---

## Persist raw output immediately

pyannote 4.x returns a `DiarizeOutput` dataclass, **not** the `Annotation` that 3.x returned.
`.itertracks()` does not exist on it. Fields:

- `.speaker_diarization` → `Annotation` (may contain overlapping turns)
- `.exclusive_speaker_diarization` → `Annotation`, **no overlap — use this for transcript mapping**
- `.speaker_embeddings` → `np.ndarray`, ordered by `sorted(annotation.labels())`
- `.serialize()` → plain dict

**Pickle the result before touching it.** An attribute error in a formatting line has already
destroyed a 27-minute run once:

```python
out = pipe(audio_path)
pickle.dump(out, open("raw.pkl", "wb"))     # first, always
turns = [...]                                # then format
```

---

## Disk and storage

16 kHz mono FLAC is ~30 MB per hour. 36 hours of audio is ~1.1 GB. Keep FLACs for interview-class
items (needed to re-run diarization); delete them for the rest after ASR.

**Keep working files out of evidence folders.** Write to `~/dw-asr/`, not into the discovery tree —
derivative files in an evidence directory contaminate the inventory and sync to the shared drive.

---

## Fast checks when something fails

| Symptom | Cause | Fix |
|---|---|---|
| `403` fetching a model | Cloud sandbox, or ungranted repo | Run locally; grant all three repos |
| `GatedRepoError` on `community-1` | Third repo not granted | Grant it |
| `ModuleNotFoundError: pkg_resources` | setuptools ≥81 | `pip install "setuptools<81"` |
| `Operation timed out` at exactly 8 MB | Google Drive retrieval fault | "Available offline"; see media-integrity-audit.md |
| `moov atom not found` | MP4 tail never arrived | Same as above |
| `Resource deadlock avoided` | Reading through a bridge mount | Read natively |
| `'DiarizeOutput' has no attribute 'itertracks'` | pyannote 4.x API | `.exclusive_speaker_diarization.itertracks()` |
| Diarization at 0% CPU | Matched the wrapper shell, not Python | `pgrep -fl`, check the real PID |
