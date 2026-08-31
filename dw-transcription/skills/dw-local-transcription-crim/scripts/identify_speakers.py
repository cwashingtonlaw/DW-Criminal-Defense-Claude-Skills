#!/usr/bin/env python3
"""Step 4: put names on SPEAKER_00.

    python identify_speakers.py openings [workdir]
        Print the first 75 s of every interview. Find one naming exactly ONE
        officer -> that is your anchor. Have the attorney confirm the voice.

    python identify_speakers.py anchor  <anchor_substr> [workdir]
        Set the anchor's dominant voice as a named voiceprint and score it
        against every diarized recording.

    python identify_speakers.py compare <fileA_substr> <labelA> <fileB_substr> [workdir]
        Direct pairwise cosine -- use to solve the second officer by elimination.

Same speaker >= 0.75. Different <= 0.35. Observed: +0.860..+0.913 same,
+0.113..+0.239 different. If everything lands mid-range, the anchor is wrong.
"""
import os, sys, json, collections
import numpy as np

def load_all(H):
    B = os.path.join(H, "batch")
    man = {}
    for l in open(os.path.join(H, "batch_manifest.jsonl")):
        x = json.loads(l); man[x["id"]] = x
    return B, man

def item_of(p):
    parts = p.split("/")
    return next((q for q in reversed(parts[:-1]) if q.startswith("#")), parts[-2])

def vecs(B, fid):
    e = np.load(f"{B}/{fid}.emb.npy")
    turns = json.load(open(f"{B}/{fid}.turns.json"))
    labs = sorted({t["spk"] for t in turns})
    talk = collections.Counter()
    for t in turns: talk[t["spk"]] += t["end"] - t["start"]
    return ({l: e[k] / (np.linalg.norm(e[k]) + 1e-9) for k, l in enumerate(labs) if k < len(e)}, talk)

def find(man, sub):
    return [i for i, m in man.items() if sub in m["path"] and m.get("status") == "OK"]

def cmd_openings(H):
    B, man = load_all(H)
    seen = {}
    for fid, m in man.items():
        if not m.get("iv") or m.get("status") != "OK": continue
        f = f"{B}/{fid}.json"
        if not os.path.exists(f): continue
        d = json.load(open(f))
        txt = " ".join(s["text"] for s in d["segments"] if s["start"] < 75).strip()
        if len(txt) < 40: continue
        it = item_of(m["path"])
        if it not in seen or len(txt) > len(seen[it]): seen[it] = txt
    for it in sorted(seen):
        print(f"\n### {it}\n    {seen[it][:400]}")
    print("\nLook for 'in the room is myself, ...' naming EXACTLY ONE officer.")

def cmd_anchor(H, sub):
    B, man = load_all(H)
    ids = [i for i in find(man, sub) if os.path.exists(f"{B}/{i}.emb.npy")]
    if not ids: sys.exit(f"no diarized recording matching {sub!r}")
    v, talk = vecs(B, ids[0])
    lab = talk.most_common()[0][0]
    print(f"anchor file : {os.path.basename(man[ids[0]]['path'])}")
    print(f"anchor voice: {lab} ({talk[lab]/60:.1f} min dominant)")
    print("!! CONFIRM WITH THE ATTORNEY -- in an interview the WITNESS usually talks more\n")
    A = v[lab]
    for fid, m in sorted(man.items(), key=lambda kv: kv[1]["path"]):
        if not os.path.exists(f"{B}/{fid}.emb.npy"): continue
        d, tk = vecs(B, fid)
        best = max(d.items(), key=lambda kv: float(A @ kv[1]))
        s = float(A @ best[1])
        if s >= 0.5:
            print(f"  {s:+.3f}  {best[0]:11s} {tk[best[0]]/60:5.1f}m  "
                  f"{item_of(m['path'])[:34]:36s} {os.path.basename(m['path'])[:42]}")

def cmd_compare(H, subA, labA, subB):
    B, man = load_all(H)
    a = [i for i in find(man, subA) if os.path.exists(f"{B}/{i}.emb.npy")][0]
    va, _ = vecs(B, a); A = va[labA]
    for fid in [i for i in find(man, subB) if os.path.exists(f"{B}/{i}.emb.npy")]:
        d, tk = vecs(B, fid)
        print(os.path.basename(man[fid]["path"])[:60])
        for k, v in d.items():
            print(f"   {k:11s} {float(A @ v):+.3f}   ({tk[k]/60:.1f} min)")

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "openings": cmd_openings(os.path.expanduser(sys.argv[2] if len(sys.argv) > 2 else "~/dw-asr"))
    elif mode == "anchor": cmd_anchor(os.path.expanduser(sys.argv[3] if len(sys.argv) > 3 else "~/dw-asr"), sys.argv[2])
    elif mode == "compare": cmd_compare(os.path.expanduser(sys.argv[5] if len(sys.argv) > 5 else "~/dw-asr"), sys.argv[2], sys.argv[3], sys.argv[4])
    else: sys.exit(__doc__)
