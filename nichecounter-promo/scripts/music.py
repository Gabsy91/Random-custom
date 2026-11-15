"""Original music bed for the Niche Counter promo, synthesised from scratch with numpy (no samples).

120 BPM (beat 0.5 s, bar 2 s), D minor -> F major. 25.0 s, 48 kHz stereo WAV.
  0.0-3.0   hook: Dm9 swell, sub hit on frame 0, tick on the price strike
  3.0-8.0   tension: near silence, clock ticks, low drone, riser into 8.0
  8.0       drop: soft kick, sub bass, FM electric-piano chords Bb-F-C-Dm | Bb-F-C-F, shaker
  12.0-16.0 build: sparse plucked arpeggio, impact on 14.0 (best price lands)
  22.0-25.0 outro: drums out, final F chord rings, fade to silence at 25.0

Usage: python3 scripts/music.py  -> assets/audio/music.wav
Pads/keys are low-passed (~1.3 kHz) to leave the 1-4 kHz voice band clear.
"""
import os
import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve

SR = 48000
DUR = 25.0
BPM = 120
BEAT = 60 / BPM
N = int(SR * DUR)
rng = np.random.default_rng(20261115)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def t_(d):
    return np.arange(int(d * SR)) / SR


def hz(note):  # MIDI -> Hz
    return 440.0 * 2 ** ((note - 69) / 12)


def lp(x, fc, order=2):
    return sosfilt(butter(order, fc, "low", fs=SR, output="sos"), x)


def hp(x, fc, order=2):
    return sosfilt(butter(order, fc, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def adsr(n, a, d, s, r, sustain_len=None):
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    sl = max(0, n - a - d - r) if sustain_len is None else int(sustain_len * SR)
    env = np.concatenate([np.linspace(0, 1, a, endpoint=False), np.linspace(1, s, d, endpoint=False),
                          np.full(sl, s), np.linspace(s, 0, r)])
    return np.pad(env, (0, max(0, n - len(env))))[:n]


class Bus:
    def __init__(self):
        self.L = np.zeros(N + SR * 4)
        self.R = np.zeros(N + SR * 4)

    def add(self, x, start, gain=1.0, pan=0.0):
        i = int(start * SR)
        if i >= len(self.L):
            return
        x = x[: len(self.L) - i]
        gl, gr = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
        self.L[i:i + len(x)] += x * gain * gl * 1.4142
        self.R[i:i + len(x)] += x * gain * gr * 1.4142

    def stereo(self):
        return np.stack([self.L[:N], self.R[:N]], 1)


# ---------------------------------------------------------------- instruments
def ep_note(note, dur, vel=1.0):
    """FM electric piano (Rhodes-like): carrier 1:1 modulator with decaying index + tine at 14x."""
    n = int((dur + 1.2) * SR)
    t = np.arange(n) / SR
    f = hz(note)
    idx = 1.6 * np.exp(-t * 6) + 0.25
    mod = np.sin(2 * np.pi * f * t) * idx
    body = np.sin(2 * np.pi * f * t + mod)
    tine = np.sin(2 * np.pi * f * 14 * t) * np.exp(-t * 40) * 0.08
    env = adsr(n, 0.004, 0.6, 0.55, 1.0, sustain_len=max(0.0, dur - 0.6))
    trem = 1 + 0.06 * np.sin(2 * np.pi * 4.5 * t)
    return (body + tine) * env * trem * vel * 0.18


def pad_note(note, dur, attack=0.6, release=1.2):
    n = int((dur + release) * SR)
    t = np.arange(n) / SR
    f = hz(note)
    x = np.zeros(n)
    for det in (-0.07, 0.0, 0.06):  # 3 detuned saws (band-limited-ish via additive)
        ff = f * 2 ** (det / 12)
        for k in range(1, 9):
            x += np.sin(2 * np.pi * ff * k * t + k) / k
    x = lp(x, 1100)
    return x * adsr(n, attack, 0.3, 0.8, release, sustain_len=max(0.0, dur - attack - 0.3)) * 0.035


def sub_note(note, dur):
    n = int((dur + 0.15) * SR)
    t = np.arange(n) / SR
    f = hz(note)
    x = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(4 * np.pi * f * t)
    return np.tanh(1.4 * x) * adsr(n, 0.008, 0.2, 0.75, 0.12, sustain_len=max(0.0, dur - 0.2)) * 0.32


def kick(vel=1.0):
    t = t_(0.45)
    f = 45 + 95 * np.exp(-t * 32)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-t * 7.5)
    click = hp(rng.standard_normal(len(t)), 2500) * np.exp(-t * 300) * 0.05
    return (np.tanh(1.6 * x) + click) * 0.55 * vel


def shaker(vel=1.0):
    t = t_(0.09)
    x = hp(rng.standard_normal(len(t)), 7000, 4) * np.exp(-t * 55)
    return x * 0.05 * vel


def tick(freq=5200, vel=1.0):
    t = t_(0.05)
    x = bp(rng.standard_normal(len(t)), freq * 0.8, freq * 1.25) * np.exp(-t * 140)
    x += np.sin(2 * np.pi * freq * 0.5 * t) * np.exp(-t * 200) * 0.3
    return x * 0.12 * vel


def pluck(note, vel=1.0):
    t = t_(0.7)
    f = hz(note)
    x = (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t + 0.5)) * np.exp(-t * 9)
    return lp(x, 3000) * 0.07 * vel


def noise_riser(dur, f0=300, f1=6000):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = rng.standard_normal(n)
    out = np.zeros(n)
    seg = int(0.02 * SR)
    for i in range(0, n, seg):  # stepped band-pass sweep
        p = i / n
        fc = f0 * (f1 / f0) ** p
        out[i:i + seg] = bp(x[max(0, i - 2048):i + seg], fc * 0.7, min(fc * 1.4, SR / 2 - 100))[-len(out[i:i + seg]):]
    return out * (t / dur) ** 2.2 * 0.09


def impact():
    t = t_(1.6)
    f = 38 + 60 * np.exp(-t * 18)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 3.2)
    air = lp(rng.standard_normal(len(t)), 2500) * np.exp(-t * 9) * 0.25
    return np.tanh(1.3 * (boom + air)) * 0.45


def reverb_ir(dur=2.4, decay=3.0):
    t = t_(dur)
    l = rng.standard_normal(len(t)) * np.exp(-t * decay)
    r = rng.standard_normal(len(t)) * np.exp(-t * decay)
    l, r = lp(l, 5000), lp(r, 5000)
    return l / np.abs(l).sum() * 40, r / np.abs(r).sum() * 40


# ---------------------------------------------------------------- arrangement
keys, pads, bass, drums, fx = Bus(), Bus(), Bus(), Bus(), Bus()

# Chord voicings (MIDI). D minor world -> F major lift
Dm9 = [50, 53, 57, 60, 64]          # D3 F3 A3 C4 E4
Bb = [46, 53, 57, 62, 65]           # Bb2 F3 A3 D4 F4 (Bbmaj7 colour)
F = [41, 53, 57, 60, 64]            # F2 F3 A3 C4 E4 (Fmaj7)
C = [48, 52, 55, 62, 64]            # C3 E3 G3 D4 E4 (Cadd9)
Dm = [50, 53, 57, 60, 65]
roots = {"Dm9": 38, "Bb": 34, "F": 41, "C": 36, "Dm": 38}

# --- 0.0-2.5 hook
for nt in Dm9:
    pads.add(pad_note(nt, 3.0, attack=0.25, release=1.4), 0.0, 1.0, pan=(nt - 57) / 20)
bass.add(sub_note(38, 1.9), 0.0, 0.8)
drums.add(kick(0.9), 0.0)
fx.add(tick(6000, 1.6), 1.40, pan=0.2)                      # the strike line
keys.add(ep_note(69, 0.6, 0.8), 1.76, pan=0.15)            # 157 € lands
keys.add(ep_note(74, 0.8, 0.6), 1.76, pan=-0.15)

# --- 2.5-8.0 tension: low drone + clock ticks, riser into the drop
drone = pad_note(38, 4.9, attack=0.8, release=0.4) * 1.4
pads.add(lp(drone, 400), 3.0)
for i, tt in enumerate(np.arange(3.5, 8.0, BEAT / 2)):
    fx.add(tick(4800 if i % 2 else 3600, 0.55 if i % 2 else 0.8), tt, pan=0.25 if i % 2 else -0.25)
fx.add(noise_riser(1.5), 6.5, 1.0)
for nt in (62, 65):  # quiet hesitation notes
    keys.add(ep_note(nt, 0.4, 0.35), 4.0 + (nt - 62) * 0.5, pan=-0.3)
keys.add(ep_note(64, 0.4, 0.3), 6.0, pan=0.3)

# --- 8.0-22.0 groove
prog = [("Bb", Bb), ("F", F), ("C", C), ("Dm", Dm), ("Bb", Bb), ("F", F), ("C", C)]
for b, (name, ch) in enumerate(prog):
    t0 = 8.0 + b * 2.0
    for k, nt in enumerate(ch[1:]):
        keys.add(ep_note(nt, 1.85, 0.75), t0 + k * 0.012, pan=(nt - 60) / 18)   # light strum
    # push chord on the "and" of beat 3
    for nt in ch[2:]:
        keys.add(ep_note(nt + 12 if nt < 60 else nt, 0.3, 0.25), t0 + 1.25, pan=0.35)
    pads.add(pad_note(ch[0] + 12, 2.0, attack=0.4, release=0.6), t0, 0.7)
    r = roots[name]
    for beat in range(4):
        bass.add(sub_note(r if beat != 3 else r + 12 if b % 2 else r, 0.42), t0 + beat * BEAT, 0.9)
    for beat in range(4):
        drums.add(kick(1.0 if beat in (0, 2) else 0.8), t0 + beat * BEAT)
    for s in range(16):
        sw = 0.018 if s % 2 else 0.0
        drums.add(shaker(1.0 if s % 4 == 2 else 0.55), t0 + s * BEAT / 4 + sw, pan=0.3)

# arpeggio 12.0-16.0 (sparse 8ths, octave 5)
arp_notes = {12.0: [72, 76, 79, 74], 14.0: [74, 77, 81, 77]}
for t0, ns in arp_notes.items():
    for i in range(8):
        keys.add(pluck(ns[i % 4], 0.8 if i % 2 == 0 else 0.5), t0 + i * BEAT / 2, pan=-0.4 + 0.1 * i)
fx.add(impact(), 14.0, 0.9)
fx.add(noise_riser(1.0, 500, 7000) * 0.6, 13.0)

# --- 22.0-25.0 outro: final F chord rings, drums out
for nt in [41, 53, 57, 60, 64, 69]:
    keys.add(ep_note(nt, 2.4, 0.8), 22.0 + (nt % 5) * 0.01, pan=(nt - 57) / 20)
    pads.add(pad_note(nt, 2.4, attack=0.3, release=0.7), 22.0, 0.8)
bass.add(sub_note(29 + 12, 2.0), 22.0, 0.9)
drums.add(kick(0.9), 22.0)

# ---------------------------------------------------------------- mix
irl, irr = reverb_ir()


def verb(bus, send):
    s = bus.stereo()
    wl = fftconvolve(s[:, 0], irl)[:N] * send
    wr = fftconvolve(s[:, 1], irr)[:N] * send
    return s + np.stack([wl, wr], 1)


mix = (verb(keys, 0.35) * 1.0 + verb(pads, 0.45) * 0.9 + bass.stereo() * 0.9
       + verb(drums, 0.08) * 0.8 + verb(fx, 0.25) * 0.9)
# keep the voice band soft: gentle 1-4 kHz dip on the whole bed
band = np.stack([bp(mix[:, c], 1000, 4000) for c in range(2)], 1)
mix = mix - 0.45 * band
# fade-in 0.03 s (no click, frame-0 hit stays), fade-out 23.6 -> 25.0
t = np.arange(N) / SR
fade = np.clip(t / 0.03, 0, 1) * np.clip((DUR - t) / 1.4, 0, 1) ** 1.5
mix *= fade[:, None]
mix = np.tanh(mix * 1.1) / 1.1
mix *= 0.89 / np.abs(mix).max()
os.makedirs(os.path.join(ROOT, "assets", "audio"), exist_ok=True)
out = os.path.join(ROOT, "assets", "audio", "music.wav")
sf.write(out, mix.astype(np.float32), SR, subtype="PCM_24")
print("wrote", out, mix.shape[0] / SR, "s")
