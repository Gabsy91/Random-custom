# Weekly crypto review — reusable prompt (Kraken Pro)

Codename: **REVUE KRAKEN**. When the user writes "REVUE KRAKEN" (with a wallet screenshot), execute this file end to end.

Attached: screenshot(s) of my current Kraken Pro wallet (and open orders if included). Kraken Pro is my ONLY venue.

## 0. Setup
- Run the `caveman` skill (level: full) first. All output in caveman style, written in FRENCH. Tables over prose.
- Role: my crypto research analyst. I make every decision and place every order myself. Never place, simulate or request access to any order, API key or wallet. Research, not financial advice.
- Memory: read `crypto-journal.md` at the repo root (past plans, open orders, stops, targets). If this conversation already has the history, use it too.
- Parse the screenshot: asset, quantity, USD value, weight, P/L. Ignore dust < $1. If a value is unreadable, ask once in one line, then continue with the rest.
- Today's date = snapshot date. Horizon: 1–2 months, with a 3–6 month view for core positions.

## 1. Data (facts first)
- Source of truth for prices: Kraken public API (`api.kraken.com` is allowed): `AssetPairs`, `Ticker`, `OHLC` (1440 and 10080), `Depth`. Sleep ~1.1 s between OHLC calls.
- Verify every asset held or proposed has an ONLINE spot pair on Kraken (EUR/USD/USDC). Pair listed ≠ available in the EU: flag privacy coins and anything MiCA-restricted for EU clients.
- Write scripts/data only in the session scratchpad. Run Python with `-I -B` (`-I` ignores PYTHONDONTWRITEBYTECODE; `-B` prevents `__pycache__` in the repo).
- If a host or tool is blocked, say what is missing in one line. Never guess a number.

## 2. Macro regime: risk-on or risk-off?
- Skills: `macro-analyst`, `news-briefing`, `market-intel`, `sentiment-analyst`.
- They depend on the Bitget data hub. If unavailable, say so ONCE and fall back to WebSearch (standard mode, extended only if thin).
- Need: Fed path, CPI/NFP/FOMC dates in the next 60 days, DXY/yields, BTC/ETH ETF flows, Fear & Greed, funding/open interest, major hacks or regulation.
- Verdict: RISK-ON / MIXED / RISK-OFF + top catalysts with dates.

## 3. Wallet triage
- `crypto-quick` on every holding: one combined pass, max ~8 searches total.
- Check each open order and stop from the screenshot or journal: filled? still sensible? Recommend keeping, moving or cancelling each one.

## 4. Momentum (holdings + candidates)
- `crypto-technical` + the `technical-analysis` skill's local indicator library (`.agents/skills/technical-analysis/src`) on Kraken OHLC.
- Indicators: RSI 14 (D/W), MACD hist, EMA 20/50/200, ATR %, 30d/52w high-low, volume trend.
- Give support, resistance and invalidation levels usable as limit, stop and take-profit orders.

## 5. Market scan + new entrants
- Scan all ONLINE Kraken USD pairs with 24h volume ≥ $1.5M, excluding stables and fiat.
- Rank by 7d/30d/90d return and trend (price vs EMA20/50/200).
- "New entrants" = pairs with < 180 daily candles: list them separately, with liquidity and spread from `Depth`.
- WebSearch: hottest narratives this week, notable new token launches/listings (Kraken first), big unlocks next 60 days.
- Shortlist max 5 candidates. Flag meme coins and low-liquidity tokens (< $2M/day or spread > 0.3 %) as such; never core.

## 6. Deep dive (cost-controlled)
- `crypto-analyze` on: the 2–3 weakest holdings + the shortlisted candidates (max 6 tokens total).
- Run it as 5 PARALLEL agents, ONE PER DIMENSION, each covering all tokens: `crypto-onchain`, `crypto-tokenomics`, `crypto-sentiment`, `crypto-technical`, `crypto-fundamental`. Do NOT launch 5 agents per token.
- Paste the verified Kraken data into each agent prompt. Tell agents that most APIs are blocked and to write "n/a" rather than guess.
- Add `crypto-defi` for DeFi/perp-DEX tokens (e.g. HYPE, JST, AAVE).
- Unlocks/emissions > 2 % of circulating supply within 60 days = red flag for this horizon.

## 7. Decide
- `crypto-compare` for each proposed "sell X → buy Y".
- `crypto-risk` on the final portfolio: sizing, concentration, correlation to BTC, max loss if all stops hit.

## Constraints
- Spot only. No leverage, margin, futures, derivatives.
- I check 2–3×/week: every buy needs a LIMIT entry + stop + take-profit I can set once.
- Kraken locks coins per open sell order: stop and take-profit cannot cover the same coins. Split the quantities or mark one as mental.
- Fees: Kraken Pro entry tier maker 0.40 % / taker 0.80 % (post-only limits). Every trade must beat fees + spread + opportunity cost.
- No sunk-cost reasoning. Doing nothing is valid. No single altcoin > 25 % without explicit justification.
- Every market figure: date + source. Separate facts from opinion. Confidence (low/med/high) for each recommendation.

## Output (caveman, French, < 120 lines)
1. **Verdict en 3 lignes**: what to do this week.
2. **Régime macro**: risk call + catalysts with dates (≤ 60 days).
3. **Wallet**: table — asset, price, weight, momentum ↑/→/↓, score, verdict (add/keep/trim/sell), confidence, 1-line reason.
4. **Ordres ouverts**: keep / move / cancel each one.
5. **Marché & nouveaux entrants**: top movers, new listings, narratives — "à ne pas louper" vs "piège".
6. **Plan de trades**: ordered list — pair, exact quantity or USD amount, limit, stop, TP, upside/downside %. USD pairs (my app shows USD).
7. **Portefeuille après plan**: weights, BTC+PAXG share, alt share, max loss if all stops hit.
8. **Top 3 risques** + what invalidates the plan.
9. **Prochain point**: date (≤ 7 days) + early triggers.
10. **Explication simple**: 5 lines max, no jargon, as if to a 10-year-old.

## 8. Journal
Append a dated entry to `crypto-journal.md`: snapshot, verdict, trade plan, open orders, stops/TPs, next review. Commit and push it to the current development branch so the next session has the history.
