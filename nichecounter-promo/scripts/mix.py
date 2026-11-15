"""Sound effects (synthesised) + final mix for the Niche Counter promo.

Inputs : assets/voice/L1..L7.wav (Kokoro), assets/audio/music.wav (scripts/music.py)
Outputs: assets/audio/vo.wav     VO placed on the 25 s timeline, -16 LUFS integrated
         assets/audio/sfx.wav    sound-effect stem (all synthesised, no samples)
         assets/audio/mix.wav    final stereo mix, 48 kHz, ducked music, true peak <= -1 dBTP
Usage  : python3 scripts/mix.py
"""
import json, os
import numpy as np
import soundfile as sf
import pyloudnorm as pyln
from scipy.signal import butter, sosfilt, resample_poly

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SR, DUR = 48000, 25.0
N = int(SR * DUR)
rng = np.random.default_rng(7)

# VO placement (film seconds) — the animation is timed to these
VO_AT = {"L1": 0.06, "L2": 3.25, "L3": 8.20, "L4": 12.20, "L5": 16.05, "L6": 19.60, "L7": 23.20}
# SFX cues (film seconds): every sound has a cause on screen
CUES = (
    [("whoosh", 2.74, 0.7, 0.22), ("whoosh2", 7.40, 0.8, 0.45), ("tap", 8.92, 1.0, 0.0), ("enter", 10.38, 1.0, 0.0),
     ("whoosh", 11.76, 0.6, 0.5), ("tap", 12.40, 1.0, 0.0), ("swish", 12.52, 0.5, 0.35), ("pop", 13.97, 0.9, 0.0),
     ("whoosh2", 15.18, 0.9, 0.5), ("swish", 16.47, 0.6, 0.5), ("pop", 17.09, 0.6, 0.0), ("whoosh", 19.28, 0.7, 0.4),
     ("pop", 22.30, 0.55, 0.0), ("pop", 13.06, 0.45, 0.0)]
    + [("key", 9.55 + i * 0.058, 0.55 + 0.25 * ((i * 7) % 3) / 2, 0.0) for i in range(11)]
)


def lp(x, fc, o=2):
    return sosfilt(butter(o, fc, "low", fs=SR, output="sos"), x)


def hp(x, fc, o=2):
    return sosfilt(butter(o, fc, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, o=2):
    return sosfilt(butter(o, [lo, hi], "band", fs=SR, output="sos"), x)


def t_(d):
    return np.arange(int(d * SR)) / SR


def s_tap():
    t = t_(0.06)
    body = np.sin(2 * np.pi * 1800 * t * (1 - t * 4)) * np.exp(-t * 160)
    tick = hp(rng.standard_normal(len(t)), 3000) * np.exp(-t * 400) * 0.4
    return (body * 0.5 + tick) * 0.35


def s_key():
    t = t_(0.045)
    x = bp(rng.standard_normal(len(t)), 2500, 6500) * np.exp(-t * 260)
    return x * 0.22


def s_enter():
    return np.concatenate([s_key() * 1.3, np.zeros(int(0.012 * SR))]) + 0


def s_whoosh(d=0.45, f0=400, f1=3500):
    n = int(d * SR)
    t = np.arange(n) / SR
    x = rng.standard_normal(n)
    out = np.zeros(n)
    seg = 512
    for i in range(0, n, seg):
        p = i / n
        fc = f0 * (f1 / f0) ** (np.sin(np.pi * p))
        y = bp(x[max(0, i - 2048):i + seg], max(80, fc * 0.6), min(fc * 1.6, SR / 2 - 200))
        out[i:i + seg] = y[-len(out[i:i + seg]):]
    env = np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2
    return out * env * 0.35


def s_whoosh2():
    return s_whoosh(0.6, 250, 2800) * 1.1


def s_swish():
    return s_whoosh(0.3, 900, 5000) * 0.7


def s_pop():
    t = t_(0.14)
    f = 520 * np.exp(-t * 18) + 180
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 34)
    return x * 0.3


GEN = {"tap": s_tap, "key": s_key, "enter": s_enter, "whoosh": s_whoosh, "whoosh2": s_whoosh2, "swish": s_swish, "pop": s_pop}


def place(buf, x, t, gain=1.0, pan=0.0):
    i = int(round(t * SR))
    x = x[: max(0, buf.shape[0] - i)]
    gl, gr = np.cos((pan + 1) * np.pi / 4) * 1.414, np.sin((pan + 1) * np.pi / 4) * 1.414
    buf[i:i + len(x), 0] += x * gain * gl
    buf[i:i + len(x), 1] += x * gain * gr


def true_peak_db(x):
    up = resample_poly(x, 4, 1, axis=0)
    return 20 * np.log10(np.abs(up).max() + 1e-12)


def main():
    meter = pyln.Meter(SR)
    # ---------------- VO
    vo = np.zeros((N, 2))
    spans = []
    for lid, t0 in VO_AT.items():
        x, sr = sf.read(os.path.join(ROOT, "assets/voice", f"{lid}.wav"))
        if x.ndim > 1:
            x = x.mean(1)
        x = resample_poly(x, SR, sr)
        x = hp(x, 85)
        place(vo, x, t0)
        spans.append((t0, t0 + len(x) / SR))
    vo_l = meter.integrated_loudness(vo)
    vo *= 10 ** ((-16.0 - vo_l) / 20)
    # ---------------- SFX
    sfx = np.zeros((N, 2))
    for name, t, g, pan in CUES:
        place(sfx, GEN[name](), t, g, pan)
    # ---------------- music + ducking (sidechain on the VO envelope: 80 ms attack, 300 ms release)
    mus, sr = sf.read(os.path.join(ROOT, "assets/audio/music.wav"))
    assert sr == SR and len(mus) >= N
    mus = mus[:N]
    env = np.abs(vo.mean(1))
    win = int(0.02 * SR)
    env = np.convolve(env, np.ones(win) / win, mode="same")
    active = (env > 10 ** (-45 / 20)).astype(float)
    duck_db = np.zeros(N)
    a_att, a_rel = np.exp(-1 / (0.08 * SR)), np.exp(-1 / (0.30 * SR))
    g = 0.0
    target = active * -12.0
    for i in range(N):  # one-pole smoothing towards the target gain (deterministic)
        a = a_att if target[i] < g else a_rel
        g = a * g + (1 - a) * target[i]
        duck_db[i] = g
    mus_d = mus * (10 ** (duck_db / 20))[:, None]
    # music bed level: -16 LUFS VO, music bed ~ -21 LUFS in the gaps
    m_l = meter.integrated_loudness(mus)
    mus_d *= 10 ** ((-19.5 - m_l) / 20)
    sfx_gain = 10 ** (-3 / 20)
    mix = vo + mus_d + sfx * sfx_gain
    # ---------------- gentle bus limiter to true peak <= -1 dBTP
    tp = true_peak_db(mix)
    ceiling = -1.2
    if tp > ceiling:
        # soft-knee peak limiting on samples above the threshold, then trim
        thr = 10 ** ((ceiling - 1.5) / 20)
        mag = np.abs(mix)
        over = mag > thr
        mix[over] = np.sign(mix[over]) * (thr + (1 - np.exp(-(mag[over] - thr) / 0.05)) * 0.05)
        tp = true_peak_db(mix)
        if tp > ceiling:
            mix *= 10 ** ((ceiling - tp) / 20)
    # fade the last 30 ms to digital silence (clean end), first 5 ms anti-click
    f = int(0.03 * SR)
    mix[-f:] *= np.linspace(1, 0, f)[:, None]
    mix[: int(0.005 * SR)] *= np.linspace(0, 1, int(0.005 * SR))[:, None]
    out = os.path.join(ROOT, "assets/audio")
    sf.write(os.path.join(out, "vo.wav"), vo.astype(np.float32), SR, subtype="PCM_24")
    sf.write(os.path.join(out, "sfx.wav"), (sfx * sfx_gain).astype(np.float32), SR, subtype="PCM_24")
    sf.write(os.path.join(out, "mix.wav"), mix.astype(np.float32), SR, subtype="PCM_24")
    report = {
        "vo_lufs": round(meter.integrated_loudness(vo), 2),
        "mix_lufs": round(meter.integrated_loudness(mix), 2),
        "mix_true_peak_dbtp": round(true_peak_db(mix), 2),
        "music_duck_db_under_vo": -12.0,
        "vo_spans": [(round(a, 2), round(b, 2)) for a, b in spans],
    }
    json.dump(report, open(os.path.join(out, "mix_report.json"), "w"), indent=1)
    print(json.dumps(report))


if __name__ == "__main__":
    main()
