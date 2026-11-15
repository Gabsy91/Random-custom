# Asset sources

No external (third-party) images are used. No AI-generated image or video is used.
Every visual is either built in code (HTML/CSS/SVG in `compositions/`) or a processed screenshot / file from nichecounter.fr.

| File | Source | Licence / basis | Processing |
|---|---|---|---|
| `final/home_screen.png` | Screenshot, https://nichecounter.fr/ (390×844 @3x, 2026-11-15) | Client's own site | Fixed bottom tab bar hidden, resized to 1080 px wide |
| `final/results_default.png` | Screenshot, https://nichecounter.fr/?q=Renaissance | Client's own site | idem |
| `final/results_sorted.png` | Screenshot, https://nichecounter.fr/?q=Renaissance&tri=price-asc | Client's own site | idem (kept for reference) |
| `final/card_157/164/171/178.png` | Element crops of the 4 result cards on the search page above | Client's own site | Tight crop at 3x |
| `final/chip_asc_off.png`, `chip_asc_on.png` | Crops of the "Prix croissant" sort chip (both states) | Client's own site | Tight crop, pill-shaped clip in the composition |
| `final/product_strip.png` | Screenshot, https://nichecounter.fr/annonce/ac95cac8-d942-46e0-bd5e-012f6491cbbe | Client's own site | Crop from brand line to payment-protection block, 1080 px wide |
| `final/protection.png` | Element crop of the payment-protection block (same page) | Client's own site | Tight crop at 3x |
| `final/logo-mark.png`, `logo-mark-dark.png`, `icon.png` | https://nichecounter.fr/logo-mark.png, /logo-mark-dark.png, /icon.png | Client's own brand files | Copied; `logo-mark.svg` traced from `logo-mark-dark.png` (potracer) for the stroke-draw |
| `fonts/CormorantGaramond-latin-var.woff2` | https://nichecounter.fr/_next/static/immutable/media/01e4147cff8141ee-s.p.0v7knm2wof07y.woff2 | Cormorant Garamond, SIL Open Font License 1.1 | Self-hosted as served by the site |
| `fonts/HankenGrotesk-latin-var.woff2` | https://nichecounter.fr/_next/static/immutable/media/c47649aa31f9e140-s.p.2rlmbw0a3_pri.woff2 | Hanken Grotesk, SIL Open Font License 1.1 | idem |
| `voice/L1–L7.wav` | Generated locally with Kokoro-82M (voice `ff_siwis`) via `scripts/vo.py` | Kokoro model: Apache-2.0 | Trimmed, placed and normalised in `scripts/mix.py` |
| `audio/music.wav`, `audio/sfx.wav` | Synthesised from scratch in `scripts/music.py`, `scripts/mix.py` (numpy/scipy) | Original | — |

Raw captures (unprocessed) are kept in `raw/` for reference only; nothing from `raw/` is shown in the video.
The home screen shows the site's own hero photograph as published on nichecounter.fr.
