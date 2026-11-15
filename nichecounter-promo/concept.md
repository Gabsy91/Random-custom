# Niche Counter — 25 s vertical promo · Concept (v1, for approval)

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

## 2. Narrative structure (120 BPM → beat = 0.5 s, bar = 2 s)

| Time | Beat | Job |
|---|---|---|
| 0.0–2.0 | **Hook** (1 bar) | "260 €" fills the screen on frame 0; red strike; "157 €" slams under it. Works muted. |
| 2.0–8.0 | **Pain** (3 bars) | The old way: price tags and tabs multiply, a cursor hesitates. "Lequel est le bon ?" / "À qui faire confiance ?" Music almost silent, ticking. |
| 8.0–12.0 | **Reveal + search** (drop) | Tabs collapse into one search bar → match cut to the real site on a phone. Tap, type "Renaissance". |
| 12.0–16.0 | **Compare + payoff** | 4 real seller cards, "Prix croissant" tapped, cards re-sort, price counter rolls 178 → 157, best card lit, "−40 %". |
| 16.0–19.5 | **Trust** | Zoom through best card into the real product page; the protection block lights: "Fonds bloqués jusqu'à votre confirmation de réception". |
| 19.5–25.0 | **Recap + CTA** | World flips to cream: "Tous les parfums. Tous les vendeurs. Le meilleur prix." → logo mark draws itself → "nichecounter.fr" held from 22.2 s (2.8 s). |

## 3. French voice-over script (target timings — re-timed on real audio in phase 3)

Voice: warm, low-mid, calm, confident, premium (no "YouTube ad" energy). ~65 words.

| # | Time (s) | Line | Words |
|---|---|---|---|
| L1 | 0.10–2.10 | Deux cent soixante euros… ou cent cinquante-sept ? | 8 |
| L2 | 2.40–7.60 | Même parfum. Encore faut-il trouver le bon vendeur… et pouvoir lui faire confiance. | 14 |
| L3 | 8.10–11.70 | Sur Niche Counter, tapez son nom : tous les vendeurs, côte à côte. | 12 |
| L4 | 12.10–15.50 | Le meilleur prix passe en tête : moins quarante pour cent. | 10 |
| L5 | 16.10–19.10 | Et votre argent reste bloqué jusqu'à la réception. | 9 |
| L6 | 19.60–22.60 | Tous les parfums. Tous les vendeurs. Le meilleur prix. | 9 |
| L7 | 23.00–24.50 | nichecounter point F R. | 3 |

On-screen text never repeats the VO word for word except the brand tagline (L6), which is the site's own headline.

## 4. Storyboard (shot by shot)

Safe zone used: all words and the CTA inside **y 250–1330 px**, **x 80–900 px** (clear of TikTok/Reels top bar, caption/handle zone and right action rail). Below 1330 px: only the phone body, texture, decoration. Min text 48 px body, 96–360 px key words.

**S1 · Hook · 0.00–2.00** — World: warm type world (ground `#14120F` with a 2 % grain and a very soft warm floor gradient to `#262219`).
- Frame 0 (thumbnail): "260 €" Cormorant 600, ~330 px, ink, y≈560; above it "Xerjoff Renaissance · 100 ml" Hanken 52 px muted, y≈330; under it "en boutique" 56 px muted.
- 0.70 s: rose `#D4636F` strike line draws across "260 €" in 0.25 s (registry `strikethrough-replace`); 260 € dims to 35 %.
- 0.95 s: "157 €" (Cormorant 700, ~360 px, ink) drops in from 40 px above with a spring (damping 0.6), label "même parfum" 56 px; "−40 %" rose pill pops at 1.25 s (`spring-pop`).
- Transition → S2 (2.00, on the bar): match cut — the "157 €" pill detaches and multiplies into a cascade of price tags.

**S2 · Pain · 2.00–8.00** — World: "the old way", desaturated and cooler (`#17171A`), slightly busy.
- Code-built generic browser tabs and price tags (no real competitor names or logos: "Vendeur ?", "178 € ?", "171 €…", "Rupture", "Avis ?") stack and scroll upward, overlapping, 3 layers with parallax (front fast with motion blur, back slow and blurred).
- A small cursor hops between tags, hesitates (registry `agent-cursor`/`dart-cursor`, trimmed to the arrow only).
- Text (Hanken 600, 88 px, ink, centred block y≈420): "Lequel est le bon ?" 2.50–4.90 → "À qui faire confiance ?" 5.00–7.60 (word-by-word mask reveal, `kinetic-center-build`).
- Music: near silence, clock-like ticking hats.
- Transition → S3 (7.50–8.00): all tags fly into the centre and fuse into **one rounded search bar** (object morph), which becomes the real search bar of the site at 8.00 (drop).

**S3 · Reveal + search · 8.00–12.00** — World: product world, phone on brand ground.
- 8.00: real home screen of nichecounter.fr (processed screenshot: bottom nav removed, status bar clean) in a minimal phone frame, 880 px wide, top at y≈430, bottom bleeding past the frame edge; soft shadow 0 40 80 rgba(0,0,0,.55). Phone rises 120 px with ease-out (expo, 0.6 s). The site's own hero "Tous les parfums. Tous les vendeurs. Le meilleur prix." is visible on the phone.
- Caption above phone (y≈290): "Tapez son nom." Hanken 600, 76 px, 8.40–11.80.
- 8.70: finger tap on the search bar (`gesture-tap`), camera pushes in 1.35× to the bar (0.5 s, motion blur, `cursor-zoom-follow` logic).
- 9.10–10.30: "Renaissance" types letter by letter in the rebuilt search field (same font/size/colours as the site), caret blinking on timeline time; soft key ticks.
- 10.60: Enter → the real results page slides up into the phone ("Résultats pour « Renaissance » · 4 annonces"); camera pulls back to 1.0.
- Transition → S4 (12.00): push into the results grid.

**S4 · Compare + payoff · 12.00–16.00**
- The 4 real result cards (cropped individually from the site) fill the frame as a 2×2 grid at ~1.9× real size, initially in a mixed order (178, 164, 157, 171) — Text: "4 vendeurs, un classement." 12.10–13.50 (y≈290).
- 12.60: tap on the real "Prix croissant" chip → cards slide and re-sort (FLIP motion, 0.55 s, spring) into 157 / 164 / 171 / 178.
- 13.20–14.40: big price counter above the grid rolls 178 → 157 € (`number-wheel`), lands on a beat (14.0) with a 0-ms hit.
- 13.60: best card lifts (scale 1.06, rose 4 px outline, others dim to 45 %); "Le meilleur prix, en tête" 13.60–15.90; "−40 %" pill spring-pops at 14.50.
- Transition → S5 (15.70–16.00): zoom through the best card (`zoom-through-transition`) into its product page.

**S5 · Trust · 16.00–19.50**
- Real product page (processed screenshot): "Renaissance · 157 € ~~260 €~~ −40 % · Soit 103 € de moins qu'en boutique", held 0.8 s at 1.7×, the "103 €" underlined in rose (`inline-highlight`) at 16.30.
- 16.90: smooth scroll (ease in-out, with slight motion blur) down to the seller card ("Flacon Club ★ 4.6 · 88 ventes") and the protection block.
- 17.40: the protection block (real element crop) lifts forward at 2×; the line "Fonds bloqués jusqu'à votre confirmation de réception" gets a rose highlight; lock icon pulses once.
- Text (y≈290): "Argent bloqué" / "jusqu'à réception." 16.40–19.30 (the site debits at order and releases funds to the seller only after you confirm reception, so "payé à la réception" would be false).
- Transition → S6 (19.50): radial mask wipe in cream `#FAF6EF` opening from the lock icon (`transitions-radial`).

**S6 · Recap + CTA · 19.50–25.00** — World: brand light (cream `#FAF6EF`, ink `#14120F`, rose `#9B2D3A`), same as the site's light theme.
- 19.60–22.20: tagline builds line by line, Cormorant 700, 120 px, left-aligned block at x 90: "Tous les parfums." / "Tous les vendeurs." / "Le meilleur prix." (last line in rose, like the site hero). Each line mask-wipes up on the VO word.
- 21.90–22.50: tagline slides up and shrinks out; logo mark (vectorised from `logo-mark.png`) **draws itself stroke by stroke** (`svg-stroke-trace`, 0.7 s), wordmark "Niche Counter" wipes in beside it.
- 22.20–25.00: CTA button "nichecounter.fr" (ink pill like the site's "Acheter" button, Hanken 600, 64 px) at y≈1080; under it the trust row "Paiement sécurisé · Vendeurs vérifiés · Litiges protégés" 40 px muted (only decoration-size, still above 1330). Everything holds still (no drift) to the end; last frame = clean end card.

Texture across S1–S5: grain overlay 2–3 % (`grain-overlay`), 6 % vignette. No glow, no particles, no glass cards.

## 5. Music brief (composed in code — Python + numpy, rendered to WAV)

- Mood: dark, warm, minimal "luxury boutique" electronic: muted Rhodes/FM-electric-piano chords, round sub bass, soft brushed kick, airy shaker; no lead melody fighting the voice.
- Tempo **120 BPM**, key **D minor → F major lift** at the reveal. Every cut sits on a beat (2.0, 8.0, 12.0, 16.0, 19.5, 22.0).
- Structure:
  - 0.0–2.0 Hook: low Dm9 chord swell + one soft sub hit on frame 0 and a "tick" on the strike (0.7 s).
  - 2.0–8.0 Tension: almost silent — filtered clock tick (8ths), a low drone, a rising filtered noise in the last bar (riser into 8.0).
  - **8.0 Drop / reveal**: kick (4-on-floor, soft), sub bass, chords open to Bb–F–C–Dm, shaker 16ths.
  - 12.0–16.0 Build: add a plucked arpeggio high (>4 kHz content kept light); impact hit at 14.0 when 157 € lands.
  - 16.0–19.5: same groove, chords thinner under VO.
  - 19.5–25.0 Outro: drums out at 22.0, final F-major chord on 22.0 ringing, fade 23.5–25.0, ends on silence at 25.0.
- Mix rules: pads low-passed ~1.2 kHz and EQ notch 1–4 kHz under voice; music ducked −12 dB under VO (sidechain on VO envelope, 80 ms attack / 300 ms release), back up in gaps; VO −16 LUFS integrated, master ≤ −1 dBTP.
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

## Questions before I build (please answer)

1. **Voice-over provider — blocker for phase 3.** `/media-use` uses HeyGen TTS by default. Missing right now:
   - HeyGen sign-in (`npx hyperframes auth login`; free plan includes 3 min of Voice Turbo/month) **and** the `heygen` CLI (https://developers.heygen.com/cli), **and** network access to HeyGen's API host — the "nichecounter" cloud environment this session now uses only allows nichecounter.fr + a few image hosts.
   - Alternatives the skill supports: **(b)** local Kokoro TTS via `npx hyperframes tts` (free, offline, one French voice `ff_siwis`, female, less premium); **(c)** Gemini TTS with your Google API key (good French, style-directable).
   - Which one? If HeyGen: please sign in and tell me, and I'll request the host.
2. **Perfume bottle image.** None of the Renaissance listings has a photo on the site (it shows "XR" initials). The environment allows xerjoff.com, but Xerjoff's packshots are their copyright with no reuse licence, so under your rules I would **not** use them unless you confirm you have the rights. Default: no bottle photo; the hook is typographic and the bottle motif is the brand's own logo line-art. OK?
3. **Hero product:** Xerjoff Renaissance (4 sellers, 260 → 157 €, −40 %) as recommended, or Kilian Rolling in Love (3 sellers, 250 → 145 €, −42 %)?
4. Anything to change in the script, the on-screen lines, or the cream end card?
