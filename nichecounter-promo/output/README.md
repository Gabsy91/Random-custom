# Niche Counter promo — deliverables

| File | What |
|---|---|
| `nichecounter_promo_1080x1920_60fps.mp4` | Final video: 1080×1920, 60 fps CFR, H.264 yuv420p, AAC 48 kHz stereo, 25.0 s |
| `concept.md` | Final concept, VO script with measured timings, storyboard as built |
| `assets/SOURCES.md` | Source of every image/font/audio file (no third-party images) |
| `nichecounter_vo_fr.wav` | French voice-over placed on the 25 s timeline (-16 LUFS) |

The editable project is the parent folder `nichecounter-promo/`:

- `index.html` + `compositions/{hook,pain,app,trust,endcard}.html` — HyperFrames scenes (GSAP timelines)
- `compositions/components/` — registry components installed for this film
- `scripts/capture.mjs` — re-captures the site screens · `scripts/process_assets.py` — crops/resizes them into `assets/final/`
- `scripts/vo.py` — French VO (Kokoro `ff_siwis`) · `scripts/music.py` — music synthesised in code · `scripts/mix.py` — SFX + mix (ducking, loudness, true peak)

Re-render after an edit:

```bash
python3 scripts/vo.py && python3 scripts/music.py && python3 scripts/mix.py
npx hyperframes@0.9.54 render --fps 60 --quality delivery -o output/nichecounter_promo_1080x1920_60fps.mp4
```

Python deps: `pip install numpy scipy soundfile pyloudnorm kokoro-onnx potracer pillow`.
