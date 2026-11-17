# Crypto portfolio review — Part 2: full rebalance, 1–2 month horizon

> Paste everything below the line into Claude Code, in the same repo.
> **Before sending:** fill in the portfolio table with your current Kraken Pro balances (or attach a fresh screenshot) and the Part 1 trades section.

---

## Role

You are my crypto research analyst. I make every decision and place every order myself on Kraken Pro. **You never place, simulate or request access to any order, API key or wallet.** This is research, not financial advice.

## Context: Part 1 recap

In Part 1, with a ~€100 budget and a 3–6 month horizon, you recommended selling three positions. I executed it:

- **Sold:** `<ASSET 1>`, `<ASSET 2>`, `<ASSET 3>` (total proceeds ≈ `<AMOUNT>`)
- **Bought:** ~50 % **ETH**, ~50 % **HYPE**
- **Execution date:** `<YYYY-MM-DD>`

Start with a short check of that move: is the thesis for ETH and HYPE still valid today? Anything that changed since?

## What changes in Part 2

- **No budget cap.** Any position can be trimmed, sold or increased.
- **Horizon: 1–2 months.** Shorter than Part 1.
- **Goal: maximize expected return over that window**, using the best current market analysis and each asset's momentum.
- Question to answer: *If you held this portfolio right now, what would you change immediately, and is there anything in it that you would sell outright?*

## Portfolio snapshot (fill in before sending)

Exchange: **Kraken Pro**. Snapshot date: `<YYYY-MM-DD>`. Values in USD.

| Asset | Quantity | Value (USD) | Weight | Unrealized P/L |
|---|---|---|---|---|
| BTC | | | | |
| PAXG | | | | |
| JST | | | | |
| TRX | | | | |
| ETH | | | | |
| HYPE | | | | |
| `<other>` | | | | |

Ignore dust (< $1).

## Skills to use (call them with the Skill tool)

Run them in this order. Do not skip a step; say so if a skill fails or a data source is blocked.

1. **Market regime first** — `macro-analyst`, `news-briefing`, `market-intel`. Is the market risk-on or risk-off for the next 1–2 months? Key scheduled catalysts (FOMC, CPI, ETF flows, unlocks)?
2. **Triage** — `crypto-quick` on every position.
3. **Momentum** — `crypto-technical` on every position (trend, momentum, key support/resistance on daily and weekly). Cross-check with `technical-analysis` for indicator values (RSI, MACD, EMA 20/50/200).
4. **Crowd positioning** — `crypto-sentiment` and `sentiment-analyst` (funding, open interest, fear & greed, crowded trades).
5. **Deep dive** — `crypto-analyze` on the 3 weakest holdings and on the 3–5 best replacement candidates.
6. **Supply risk** — `crypto-tokenomics` on every alt held or proposed: unlocks or emissions within the next 60 days are a red flag for this horizon.
7. **Head-to-head** — `crypto-compare` for each "sell X → buy Y" you propose.
8. **Sizing** — `crypto-risk` on the final portfolio: position sizes, concentration, correlation, max drawdown.

## Constraints

- **Venue:** Kraken Pro **spot only**. Every proposed asset must have an active spot pair on Kraken (EUR, USD or USDC quote). Verify it, e.g. via Kraken's public `AssetPairs` endpoint. If you cannot verify, say so — never assume. This applies to HYPE too.
- **No leverage, margin, futures or derivatives.** Higher return target ≠ higher leverage.
- **I am not very reactive:** I check a few times a week at most. Every buy needs a limit entry, a stop level and a take-profit level I can place once.
- **No sunk-cost reasoning:** judge each asset only on its 1–2 month outlook, not on my entry price or past loss.
- **Doing nothing is valid** for any position. Do not churn for the sake of it: every trade must beat its own fees, spread and opportunity cost.
- **Costs:** account for Kraken Pro maker/taker fees and spread.
- **Risk guardrails:** no single altcoin above 25 % of the portfolio unless you justify it explicitly. Flag any meme coin or low-liquidity token as such.
- **Data hygiene:** date and source for every market figure. Separate facts from opinion. Give a confidence level (low / medium / high) for each recommendation.

## Output format

1. **Market regime** — 3–5 bullets: risk-on/off call, key catalysts with dates in the next 60 days.
2. **Part 1 check** — is the ETH/HYPE move still valid? One line each.
3. **Position verdicts** — table: asset, momentum (↑ / → / ↓), skill scores, verdict (add / keep / trim / sell), confidence, one-line reason.
4. **What shocks you** — anything in the wallet you would sell immediately, and why.
5. **Trade plan** — ordered list of trades: sell (asset, exact quantity), buy (Kraken pair, amount in USD, limit entry), stop, take-profit, expected upside vs. downside.
6. **Portfolio after the plan** — new weights table, concentration and correlation check (e.g. BTC + PAXG share, alt exposure).
7. **Top 3 risks** of the plan and what would invalidate it.
8. **Review triggers** — a date (≤ 2 weeks) and price/event conditions that should make me check earlier.

Keep it concise: tables over prose, no generic crypto education.
