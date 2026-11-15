"""French voice-over for the Niche Counter promo, generated locally with Kokoro-82M (voice ff_siwis).

Same engine/model as `npx hyperframes tts`, but called directly so the phonemes can be cleaned:
espeak inserts "(en)…(fr)" language-switch markers around "Counter" which Kokoro would voice.

Usage:  python3 scripts/vo.py            -> assets/voice/L1.wav … L7.wav + assets/voice/lines.json
"""
import json, os, re, sys
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
from kokoro_onnx.tokenizer import Tokenizer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.expanduser("~/.cache/hyperframes/tts")
MODEL = os.path.join(CACHE, "models", "kokoro-v1.0.onnx")
VOICES = os.path.join(CACHE, "voices", "voices-v1.0.bin")
VOICE = "ff_siwis"
SPEED = float(os.environ.get("VO_SPEED", "0.93"))

# id, text. A line may be split into segments joined by fixed pauses (seconds) for rhythm.
SEGMENTS = {
    "L1": ["Deux cent soixante euros…", 0.28, "ou cent cinquante-sept ?"],
    "L6": ["Tous les parfums.", 0.22, "Tous les vendeurs.", 0.26, "Le meilleur prix."],
}
LINES = [
    ("L1", "Deux cent soixante euros… ou cent cinquante-sept ?"),
    ("L2", "Même parfum. Encore faut-il trouver le bon vendeur… et pouvoir lui faire confiance."),
    ("L3", "Sur Niche Counter, tapez son nom : tous les vendeurs, côte à côte."),
    ("L4", "Le meilleur prix passe en tête : moins quarante pour cent."),
    ("L5", "Et votre argent reste bloqué jusqu'à la réception."),
    ("L6", "Tous les parfums. Tous les vendeurs. Le meilleur prix."),
    ("L7", "Niche Counter point F R."),
]
# "Counter" said the way a French speaker says the brand: [kaʊntœʁ]
BRAND = "nˈiʃ kˈaʊntœʁ"


def phonemes_for(tok: Tokenizer, text: str) -> str:
    p = tok.phonemize(text, "fr-fr")
    p = re.sub(r"\((en|fr)\)", "", p)                  # drop language-switch markers
    p = re.sub(r"nˈiʃ\s*kˈaʊntə", BRAND, p)              # normalise the brand name
    return re.sub(r"\s+", " ", p).strip()


def trim(x, sr, pad=0.04):
    env = np.abs(x)
    idx = np.where(env > 0.02 * env.max())[0]
    a = max(0, idx[0] - int(pad * sr)); b = min(len(x), idx[-1] + int(pad * sr))
    y = x[a:b].copy()
    f = int(0.01 * sr)
    y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
    return y


def main():
    tok = Tokenizer()
    k = Kokoro(MODEL, VOICES)
    out = {}
    sr = 24000
    for lid, text in LINES:
        parts, phs, cues = [], [], []
        for seg in SEGMENTS.get(lid, [text]):
            if isinstance(seg, float):
                parts.append(np.zeros(int(seg * sr), dtype=np.float32)); continue
            ph = phonemes_for(tok, seg); phs.append(ph)
            a, sr = k.create(ph, voice=VOICE, speed=SPEED, lang="fr-fr", is_phonemes=True)
            cues.append(round(sum(len(q) for q in parts) / sr, 3))
            parts.append(trim(np.asarray(a, dtype=np.float32), sr, pad=0.03))
        audio = np.concatenate(parts)
        ph = " | ".join(phs)
        path = os.path.join(ROOT, "assets", "voice", f"{lid}.wav")
        sf.write(path, audio, sr, subtype="PCM_24")
        out[lid] = {"text": text, "phonemes": ph, "segment_starts_s": cues, "duration_s": round(len(audio) / sr, 3), "sr": sr}
        print(lid, out[lid]["duration_s"], ph)
    json.dump(out, open(os.path.join(ROOT, "assets", "voice", "lines.json"), "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
