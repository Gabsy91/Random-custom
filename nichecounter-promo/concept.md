# Niche Counter — 25 s vertical promo · Concept (final, as built)

Format: 1080×1920 · 60 fps · 25.0 s · H.264 yuv420p + AAC · French VO + code-synthesised music.

---

## 0. What the live site says (checked 2026-11-15) — corrections to the brief

| Brief assumption | Live site | Consequence for the ad |
|---|---|---|
| "Marketplace + price comparator" | Marketplace. Sellers list on Niche Counter; buyers compare **the sellers on the platform** (one search → all listings, sortable "Prix croissant"). It does **not** compare external shops. Title: "Le meilleur prix du marché gris de la parfumerie de niche". | We say "tous les vendeurs, côte à côte", never "tous les sites". |
| Verified sellers | Footer: "Vendeurs vérifiés"; sellers pass "vérification d'identité en privé". | OK to show the trust row. |
| Secure Stripe payment, buyer protection | "Paiement débité à la commande · Fonds bloqués jusqu'à votre confirmation de réception · Un problème ? Ouvrez un litige, l'argent reste bloqué" (Stripe Connect). | Main trust beat. |
| Price-drop alerts | "M'alerter sur ce parfum" button + newsletter "baisses de prix". | Optional micro-moment, not in VO. |
| — | Authenticity: product page says it is "déclaré par le vendeur, Niche Counter ne le vérifie pas" (but footer says "100 % authentique"). | **No authenticity claim** in the ad. |
| — | Catalogue today: 16 listings, 104 brands listed (most "Bientôt"). | No "des milliers de parfums". Tagline "Tous les parfums." is the site's own headline, used verbatim. |

Brand: ground `#14120F`, card `#1D1A16`, ink `#F5F1E8`, muted `#9A9389`, brand rose `#D4636F` (fill `#AE3A47`), gold `#D3A551`; light theme `#FAF6EF` / rose `#9B2D3A`. Fonts: Cormorant Garamond (display) + Hanken Grotesk (UI). Logo: line-drawn bottle mark (light + dark PNGs) + Cormorant wordmark. Full notes: `assets/raw/SITE_NOTES.md`.

## 1. One-line concept

**One real perfume, one real number:** the Xerjoff Renaissance goes from 260 € to 157 € in front of you — and the film shows exactly how, inside the real Niche Counter app: search, compare sellers, best price first, money held until delivery.

Spine data (real listings, search "Renaissance", sorted "Prix croissant"): **178 € · 171 € · 164 € · 157 €** vs 260 € → best = 157 €, −40 %, "Soit 103 € de moins qu'en boutique", seller Flacon Club 4.6 ★ (53 avis).

Other storylines considered (not recommended): **B "Life before / after"** — split screen, left a phone drowning in tabs, right Niche Counter calm; collapses to one. **C "The mark is the story"** — the logo's bottle line-art draws continuously and each stroke becomes a UI element (search line, price strike, lock). Picked A: a stranger remembers a real price drop more than a style.

## 2. Narrative structure — AS BUILT (120 BPM → beat 0.5 s, bar 2 s)

| Time (s) | Beat | What happens |
|---|---|---|
| 0.00–3.00 | **Hook** | Frame 0: "XERJOFF / Renaissance · 100 ml / 260 € en boutique". 1.40 strike, 1.76 "157 €" drops in, 2.22 "−40 %" pops. Vertical whip out. |
| 3.00–8.00 | **Pain** | Anonymous listings ("Vendeur inconnu", "Paiement par virement hors plateforme", "Authentique ? sans garantie"…) drift up in 3 parallax columns, a cursor hesitates, "?" stamps pop. "Lequel est le bon ?" → "À qui faire confiance ?". 7.42: the whole field collapses into one search bar. |
| 8.00–15.75 | **Reveal → search → compare → payoff** (one continuous take) | 8.00 drop: the search bar opens into the real nichecounter.fr home on a phone. Tap, camera push, "Renaissance" typed, real results page. 11.76: the 4 real offer cards are carried out of the phone, 12.40 tap on the real "Prix croissant" chip, 12.52 cards re-sort exactly as the site does (164/157/178/171 → 157/164/171/178), best card ringed in rose, counter rolls 178 → 157 €, 13.97 "−40 %" lands on the impact. 15.20 zoom through the best card. |
| 15.75–19.80 | **Trust** | Real product page settles in, "Soit 103 € de moins qu'en boutique" underlined; scroll to the real payment-protection block, which comes forward while the page dims; "Fonds bloqués jusqu'à votre confirmation de réception" highlighted. Caption "Argent bloqué jusqu'à réception." |
| 19.30–25.00 | **Recap + CTA** | Iris opens in cream from the lock icon. Tagline per word on the VO; 22.2 logo bottle mark draws itself + wordmark; CTA capsule "nichecounter.fr →" from 22.30 to 25.00 (2.7 s), trust lines "Paiement sécurisé / Vendeurs vérifiés". One shimmer pass on the CTA at 23.3. |

## 3. French voice-over — FINAL (Kokoro `ff_siwis`, speed 0.93, measured)

| # | Starts at (s) | Ends (s) | Line |
|---|---|---|---|
| L1 | 0.06 | 3.15 | Deux cent soixante euros… ou cent cinquante-sept ? |
| L2 | 3.25 | 7.93 | Même parfum. Encore faut-il trouver le bon vendeur… et pouvoir lui faire confiance. |
| L3 | 8.20 | 11.86 | Sur Niche Counter, tapez son nom : tous les vendeurs, côte à côte. |
| L4 | 12.20 | 15.11 | Le meilleur prix passe en tête : moins quarante pour cent. |
| L5 | 16.05 | 18.90 | Et votre argent reste bloqué jusqu'à la réception. |
| L6 | 19.60 | 23.02 | Tous les parfums. Tous les vendeurs. Le meilleur prix. |
| L7 | 23.20 | 24.82 | Niche Counter point F R. |

65 words, 20.8 s of speech. "Niche Counter" is pronounced [niʃ kaʊntœʁ] (phonemes forced in `scripts/vo.py`).

## 4. Storyboard — AS BUILT

Safe band (intersection of TikTok, Reels and Shorts overlays, checked by `hyperframes check`): every word between **y 288–1248**, **x 120–888** (x ≤ 780 below y 840). Below 1248 px: only UI bleed and texture.

| Scene file | Film time | Visual | Assets | Motion | Out-transition | On-screen text |
|---|---|---|---|---|---|---|
| `compositions/hook.html` | 0–3.0 | type world, warm floor gradient | code | strike `scaleX` 0.24 s power2.out; 157 € expo.out drop with 12→0 px blur; pill back.out | vertical whip (y −300, blur 14, power3.in) | XERJOFF · Renaissance · 100 ml · 260 € · en boutique · 157 € · même parfum · −40 % |
| `compositions/pain.html` | 3.0–8.0 | cool grey "old way" world | code | 3 parallax columns (constant speed), per-word blur titles, hesitating cursor, "?" springs | field collapses + pill morph (scaleX 0.14→1, power3.out), ground floods to #14120F | Lequel est le bon ? · À qui faire confiance ? |
| `compositions/app.html` | 8.0–15.75 | brand ground, phone (code frame) with real screens | home_screen, results_default, card_*, chip_* | clip-path reveal from the bar; camera push 1.25× power2.inOut; tap (gesture-tap mechanics); typed text; carry-out power3.inOut; FLIP re-sort with lift; counter wheel power3.out | zoom through the best card (×3.6, power3.in) + dip | Sur Niche Counter, tapez son nom. · Tous les vendeurs, côte à côte. · Meilleur prix 157 € −40 % |
| `compositions/trust.html` | 15.75–19.8 | real product page | product_strip, protection | page arrives 1.07→1 with blur; scroll with motion blur; block forward, page dims 97 % | iris (circle clip) from the lock icon | Argent bloqué jusqu'à réception. |
| `compositions/endcard.html` | 19.3–25.0 | cream brand world (site's light theme) | logo-mark.svg (traced) | per-word blur-in; stroke-dashoffset draw + fill; wordmark clip wipe; CTA back.out; one shimmer | — (holds) | Tous les parfums. Tous les vendeurs. Le meilleur prix. · Niche Counter · nichecounter.fr → · Paiement sécurisé · Vendeurs vérifiés |

Global: 7 % film grain stepped every 2 frames (seeded), registry `vignette` on the dark scenes, render-time motion blur (`data-motion-blur="on"`).

Registry items used (installed in `compositions/components/`, adapted inline): `strikethrough-replace`, `number-wheel`, `gesture-tap`, `svg-stroke-trace`, `grain-overlay`, `zoom-through-transition`, `spring-pop`, `kinetic-center-build`, `inline-highlight`, `device-frame-stage`, `vignette`, `shimmer-sweep`.

## 5. Music brief (composed in code — Python + numpy, rendered to WAV)

- Mood: dark, warm, minimal "luxury boutique" electronic: muted Rhodes/FM-electric-piano chords, round sub bass, soft brushed kick, airy shaker; no lead melody fighting the voice.
- Tempo **120 BPM**, key **D minor → F major lift** at the reveal. Main cuts on beats/bars: 3.0, 8.0 (drop), 14.0 (impact), 22.0 (final chord); code: `scripts/music.py`.
- Structure:
  - 0.0–3.0 Hook: low Dm9 chord swell + one soft sub hit on frame 0, a tick on the strike (1.40 s), two electric-piano notes when 157 € lands (1.76 s).
  - 3.0–8.0 Tension: almost silent — filtered clock tick (8ths), a low drone, a rising filtered noise in the last bar (riser into 8.0).
  - **8.0 Drop / reveal**: kick (4-on-floor, soft), sub bass, chords open to Bb–F–C–Dm, shaker 16ths.
  - 12.0–16.0 Build: add a plucked arpeggio high (>4 kHz content kept light); impact hit at 14.0 when 157 € lands.
  - 16.0–19.5: same groove, chords thinner under VO.
  - 19.5–25.0 Outro: drums out at 22.0, final F-major chord on 22.0 ringing, fade 23.5–25.0, ends on silence at 25.0.
- Mix (as built, `scripts/mix.py`): whole bed dipped −5 dB in 1–4 kHz, pads low-passed ~1.1 kHz; music ducked −12 dB under the VO (sidechain on the VO envelope, 80 ms attack / 300 ms release) and back up in gaps; VO −16.0 LUFS integrated; final mix −16.0 LUFS, true peak −1.35 dBTP.
- Sound effects (also synthesised in code, few and exact): tap clicks on 8.70 and 12.60, soft key ticks while typing, two different whooshes on 7.5 and 15.7, impact on 14.0. No downloaded samples.

## 6. Assets plan

| Asset | Source | Processing |
|---|---|---|
| Home screen, results page, product page, seller + protection blocks, 4 result cards, search bar, chips | Real screenshots nichecounter.fr, 390×844 @3x (`assets/raw/`) | Crop, remove fixed bottom nav, clean status area, resize to 1080 px wide (or needed size), rounded corners 36 px, soft shadow |
| Logo mark (light/dark) | nichecounter.fr `/logo-mark.png`, `/logo-mark-dark.png` | Vectorise to SVG (potrace) for stroke draw; PNG fallback |
| Fonts | Site's own Cormorant Garamond + Hanken Grotesk woff2 (OFL) | `assets/fonts/` |
| Tabs/price tags (pain), phone frame, badges, counter | Built in code | — |
| Perfume bottle photo | **None by default** (see question 2) | — |

`assets/SOURCES.md` will log every file's URL.

---

## Decisions taken at the checkpoint

1. Voice-over: local Kokoro TTS, French voice `ff_siwis` (chosen by the client; HeyGen needed a sign-in, its CLI and network access not available here). The WAV can be swapped and the film re-mixed with `python3 scripts/mix.py`.
2. No bottle photo (Xerjoff packshots have no reuse licence). The bottle motif is the brand's own logo line-art.
3. Hero product: Xerjoff Renaissance.
