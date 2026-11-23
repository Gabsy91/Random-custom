# Revue Kraken — Partie 2 (horizon 1–2 mois) — 2026-11-23

> Recherche uniquement, pas un conseil financier. Aucun ordre passé ni simulé. Toutes les décisions restent les tiennes sur Kraken Pro.

**Sources des prix :** API publique Kraken (`Ticker`, `OHLC` daily/4h/weekly), relevée le 2026-11-23 vers 19:00 UTC. Valeurs en USD sauf mention contraire. Total recalculé : **≈ $933** (capture d'écran : $946 à 17:08).

**Skills utilisées :** `macro-analyst`, `news-briefing`, `market-intel`, `crypto-quick`, `crypto-technical`, `technical-analysis` (moteur Python du skill lancé sur les bougies Kraken), `crypto-sentiment`, `sentiment-analyst`, `crypto-analyze` (agents on-chain, tokenomics et fondamental), `crypto-tokenomics`, `crypto-compare`, `crypto-risk`.

**Données manquantes :** depuis cet environnement, seule l'API Kraken répond. Le data hub des skills Bitget, CoinGecko, Coinglass, DefiLlama, alternative.me et Binance sont bloqués. Les ratios long/short, le taker ratio et la carte des liquidations ne sont **pas disponibles**. Le funding, l'open interest et le Fear & Greed viennent de recherches web (sources citées). Les grilles de frais Kraken ne sont pas renvoyées par `AssetPairs`. Les frais utilisés ici sont ceux du palier de base connu (0,25 % maker / 0,40 % taker) : **vérifie-les dans l'app**.

---

## 1. Régime de marché : RISK-OFF 🔴 (confiance haute)

- **La Fed va remonter ses taux, pas les baisser.** Le FOMC des 8–9 déc. (décision le **9 déc., 20:00 CET**) est pricé à environ 90–99 % pour une hausse de 25 pb, depuis une fourchette de 3,75–4,00 %. Waller évoque même 50 pb. [rateprobability](https://rateprobability.com/fed), [Forbes](https://www.forbes.com/sites/simonmoore/2026/11/09/what-to-expect-from-the-feds-december-meeting/)
- **L'inflation repart.** Le CPI d'octobre (publié le 10 nov.) ressort à +0,4 % m/m, au-dessus des +0,3 % attendus. Le 10 ans est autour de 5 % et le DXY à 103 (plus haut depuis avril 2025). [CNBC](https://www.cnbc.com/2026/11/10/us-bonds-treasurys-yields.html), [Investing/Reuters](https://www.investing.com/news/economic-indicators/hot-october-inflation-report-rattles-markets-5015775)
- **Les flux sortent.** Les ETF BTC spot ont perdu -$1,79 Md sur la semaine du 16 au 20 nov. (4e semaine négative d'affilée, dont 76 % sur IBIT). Les ETF ETH ont perdu environ -$970 M sur novembre. [coinpaper](https://coinpaper.com/39252/bitcoin-et-fs-lose-1-79-billion-in-one-week-while-btc-falls-nearly-10), [coinpaper ETH](https://coinpaper.com/39123/ethereum-price-prediction-eth-drops-23-in-november-as-black-rock-etf-loses-124-m)
- **Le sentiment est en capitulation.** Le Fear & Greed est à **9–11** (peur extrême). Le BTC a touché $55,1k le 21 nov. (plus bas sur 2 ans) après $1,8 Md de liquidations. Le funding BTC est légèrement positif (+0,0035 %/8h), et les liquidations du 23 nov. ont surtout touché les shorts. [Yahoo/Motley Fool](https://finance.yahoo.com/markets/crypto/articles/crypto-market-today-nov-22-224002736.html), [OKX brief](https://www.okx.com/en-us/orbit/insight/oli-daily-brief-2026-11-23-93527886876352), [invezz](https://invezz.com/news/2026/11/22/crypto-fear-and-greed-index-slumps-to-7-can-bitcoin-ethereum-and-xrp-rebound)
- **L'or ne joue plus son rôle de couverture.** Il est au plus bas depuis 13 mois (~$3 514 le 20 nov.), plombé par les paris de hausse de taux. Sur 90 jours, la corrélation PAXG/BTC calculée sur les données Kraken est de **0,54**. [CNBC](https://www.cnbc.com/2026/11/20/gold-federal-reserve-price-dollar-metals.html)

**Catalyseurs dans les 60 prochains jours**

| Date | Événement |
|---|---|
| 4 déc. | Emploi US (NFP) de novembre |
| **6 déc.** | Unlock contributeurs HYPE (modélisé à environ 9,9 M HYPE ; le 6 nov., seuls environ 180k avaient été effectivement distribués) |
| **9 déc.** | Décision du FOMC (hausse attendue) |
| 10 déc. | CPI de novembre |
| 15 déc. | PPI de novembre |
| 25 déc. | Échéance trimestrielle des options et futures crypto |
| ~6 janv. | Unlock HYPE suivant |
| 8 janv. / 13 janv. | NFP de décembre / CPI de décembre |

Calendrier BLS : [bls.gov](https://www.bls.gov/schedule/2026/12_sched.htm)

**Lecture :** le contexte macro joue contre toi jusqu'au FOMC. Le contrepoint : la peur est extrême et le BTC se trouve sur son prix réalisé (~$53–55k). Les ventes forcées sont en grande partie passées. Mon scénario de base est un marché en range bas, entre $55k et $67k, sur 1–2 mois. Ce n'est pas le moment de prendre plus de bêta au prix du marché. Acheter seulement sur supports, avec des ordres limites.

---

## 2. Bilan de la Partie 1

**Constat à partir des soldes :** XRP et LTC ont été vendus. Le PAXG est passé de 0,07315 à 0,03628. ETH et HYPE ont été achetés, et le BTC est passé de 0,006158 à 0,007332.

| Mouvement | Toujours valable ? | Commentaire |
|---|---|---|
| Ventes XRP / LTC | ✅ Oui | Depuis le 17 nov., XRP est passé de $0,972 à $0,949 et LTC de $44,9 à $41,7. Les deux sont sous toutes leurs EMA. Bonne sortie. |
| Achat **ETH** | 🟡 Affaibli | Le catalyseur Glamsterdam est reporté sine die. Les ETF ETH ont perdu environ -$1 Md en novembre. ETH/BTC fait -2,8 % sur 30 j et son bêta au BTC est de 1,18. C'est en pratique un BTC avec plus de levier. On garde la position sans renforcer. |
| Achat **HYPE** | ✅ Oui | Meilleur fondamental du portefeuille (85/100). Les rachats représentent environ $72 M sur 30 j (99 % des frais). HYPE fait **+12 % contre BTC sur 30 j**. Risque : l'unlock du 6 déc. |

---

## 3. Verdict par position

Scores de 0 à 100. **OnC** = on-chain, **Tok** = tokenomics, **Sent** = sentiment, **Tech** = technique, **Fond** = fondamental, **Risk** = risque (plus le score est haut, plus c'est sûr). « n/a » = non noté (donnée indisponible) ; la moyenne est alors faite sur les dimensions disponibles. Les scores BTC Tok et Fond sont des estimations du synthétiseur, faute d'agent dédié.

| Actif | Poids | Momentum | RSI j / hebdo | OnC | Tok | Sent | Tech | Fond | **Composite** | Risk | Verdict | Conf. | Raison |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC | 48,2 % | ↓ | 27 / 36 | 48 | ~85 | 48 | 30 | ~85 | **59** | 78 | **Garder + achat limite** | Moy. | Survendu, au niveau du prix réalisé ; acheter seulement sur support |
| PAXG | 14,1 % | ↓ | 34 / 30 | n/a | n/a | 42 | 28 | 65 | **45** | 72 | **Alléger 50 %** | Moy.-basse | La hausse de taux pèse directement sur l'or, qui ne couvre plus le crypto |
| JST | 13,8 % | ↑ | 57 / 76 | n/a | 63 | 47 | 62 | 53 | **56** | 38 | **Garder + stop** | Moy. | Seul actif en tendance haussière, décorrélé, rachats-burn ; marché Kraken très mince |
| TRX | 8,9 % | → | 46 / 40 | n/a | 68 | 50 | 50 | 75 | **61** | 55 | **Garder** | Moy. | MACD repassé haussier aujourd'hui, faible bêta, range 0,298–0,389 |
| ETH | 7,8 % | ↓ | 32 / 36 | 54 | 77 | 47 | 29 | 76 | **57** | 70 | **Garder, ne pas renforcer** | Basse | Doublon du BTC avec bêta 1,18 ; flux ETF négatifs |
| HYPE | 6,4 % | → | 39 / 47 | 51 | 64 | 60 | 39 | 85 | **60** | 50 | **Renforcer sur repli** | Moy. | Meilleur fondamental, surperforme le BTC ; prudence autour de l'unlock du 6 déc. |
| ADA | 0,8 % | ↓ | 33 / 35 | 38 | 67 | 40 | 24 | 39 | **42** | 50 | **VENDRE** | Haute | -89 % depuis le plus haut, TVL DeFi -81 % sur 1 an, aucun revenu |

**Détail technique** (Kraken, bougies daily, EMA 20/50/200, SuperTrend(10,3), MACD) :

- **BTC** : prix sous les 3 EMA ($67,2k / $72,9k / $75,0k). SuperTrend baissier depuis 28 barres. ADX 48 (tendance forte), StochRSI 42/25 (en train de remonter). Fibo 0,786 à $62,0k, plus bas à $55,1k.
- **ETH** : prix sous les 3 EMA ($1 909 / $2 129 / $2 247). MFI à 19 (survendu). Support au plus bas de $1 536.
- **HYPE** : SuperTrend à $76,3. EMA200 à $69,2. Plus bas sur 30 j à $55,74. MFI à 45.
- **PAXG** : sous toutes les EMA. Cassure MACD il y a 10 barres. Plus bas à $3 490.
- **JST** : SuperTrend haussier depuis **83 barres**, support à $0,134. Bandes de Bollinger serrées (5,8 %), compression juste sous le plus haut sur 30 j ($0,148).
- **TRX** : range entre 0,298 et 0,389. Croisement MACD haussier aujourd'hui.

## 4. Ce qui me choque

1. **ADA (0,8 %)** : poussière inutile, à vendre tout de suite. C'est le pire score du portefeuille sur chaque dimension. Le coût est d'environ 3 centimes de frais.
2. **PAXG à 14 % n'est plus une couverture.** Dans un régime de hausse de taux, l'or et le BTC baissent ensemble (corrélation 0,54). Le rôle de « ballast » qu'il avait dans la Partie 1 ne fonctionne pas sur cet horizon.
3. **Exposition à l'écosystème TRON / Justin Sun (JST + TRX = 22,7 %).** Ces deux actifs sont peu corrélés au marché, mais ils partagent un risque de gouvernance commun. Un administrateur de Tron Inc. a vendu pour $115 M d'actions le 19 nov. ([Investing](https://investing.com/news/insider-trading-news/tron-inc-director-weike-sun-sells-1151m-in-shares-93CH-5045155)). Pas de vente forcée, mais un stop est nécessaire.
4. **JST/EUR est quasi illiquide sur Kraken** : environ €3k de volume par jour et 0,22 % de spread. Utilise **JST/USD** (environ $41k par jour).

---

## 5. Plan de trades (ordre d'exécution)

Frais pris en compte : 0,25 % maker / 0,40 % taker (palier de base, à vérifier). Rotation d'environ $146, soit **environ $0,40–0,60 de frais au total**.

| # | Action | Paire Kraken | Quantité / Montant | Limite | Stop | Take-profit | Potentiel haut / bas |
|---|---|---|---|---|---|---|---|
| 1 | **Vendre** ADA | ADA/EUR | **47,077065 ADA** (≈ $7) | marché ou ~0,1378 € | — | — | — |
| 2 | **Vendre** PAXG | PAXG/USD | **0,0181 PAXG** (≈ $66, la moitié) | $3 640 | — | — | — |
| 3 | **Acheter** BTC | XBT/USD | **$40** (≈ 0,000714 BTC) | **$56 000** | $52 000 (-7 %) | $67 500 (+20 %) | +20 % / -7 % (R:R 2,9) |
| 4 | **Acheter** HYPE | HYPE/USD | **$33** (≈ 0,564 HYPE) | **$58,50** | $53,50 (-8,5 %) | $76 (+30 %) | +30 % / -8,5 % (R:R 3,5) |

Les ordres 3 et 4 ne se déclenchent que si le marché revient tester ses supports. **S'ils ne sont pas exécutés d'ici le 7 déc., garde le cash en USDC.** C'est une réserve volontaire.

**Stops et objectifs à poser une seule fois sur les positions existantes**

| Actif | Stop (stop-limit) | Objectif / alerte | Logique |
|---|---|---|---|
| BTC (ligne principale) | alerte sur clôture journalière < $52 000 | alerte à $67 500 | Sous le prix réalisé, la thèse de plancher tombe |
| ETH | $1 480 | $2 020 | Sous le plus bas de nov. à $1 536 ; SuperTrend/Fibo 0,618 vers 2 017–2 021 |
| HYPE (tout) | $53,50 | $76 | Sous le plus bas sur 30 j de $55,74 ; SuperTrend à 76,3 |
| JST | $0,1330 (stop-limit sur JST/USD) | vendre 50 % à $0,173 | Sous le SuperTrend à 0,134 ; Fibo 0,382 sur 90 j |
| TRX | $0,2950 | $0,345 | Sous le plus bas du range à 0,298 ; Fibo 0,5 |
| PAXG (reste) | $3 450 | $3 820 | Sous le plus bas à $3 490 ; SuperTrend à 3 822 |

⚠️ Sur Kraken spot, un stop réserve tes jetons. Sauf si Kraken Pro propose un ordre OCO sur la paire (je n'ai pas pu le vérifier), tu ne peux pas placer à la fois le stop et le take-profit sur les mêmes jetons. Le plus simple : **place le stop comme ordre et le take-profit comme alerte de prix.**

---

## 6. Portefeuille après le plan

| Actif | Maintenant | Après ventes (avant achats) | Après tous les achats |
|---|---|---|---|
| BTC | 48,2 % | 48,2 % | **52,5 %** |
| PAXG | 14,1 % | 7,1 % | 7,1 % |
| JST | 13,8 % | 13,8 % | 13,8 % |
| TRX | 8,9 % | 8,9 % | 8,9 % |
| ETH | 7,8 % | 7,8 % | 7,8 % |
| HYPE | 6,4 % | 6,4 % | **10,0 %** |
| ADA | 0,8 % | 0 % | 0 % |
| USDC / cash | ~0 % | **7,8 %** | 0 % |
| **Volatilité annualisée 90 j** | 29,9 % | 28,5 % | 31,9 % |
| **Bêta au BTC** | 0,70 | ~0,65 | 0,75 |

- **BTC + PAXG** : 62,3 % aujourd'hui, 59,6 % après le plan.
- **Bloc corrélé BTC + ETH + HYPE** : 62,4 % aujourd'hui, 70,3 % après les achats. Les corrélations entre eux vont de 0,59 à 0,93. C'est voulu : les achats ne se font que plus bas.
- **Aucun altcoin au-dessus de 25 %.** Le plus gros est JST à 13,8 %.
- **Risque de mème :** aucun. **Faible liquidité :** JST seulement.

---

## 7. Top 3 des risques

1. **Une hausse de 50 pb ou un CPI de novembre chaud le 10 déc.** pousserait le BTC à casser $55k. Les achats limites seraient exécutés puis stoppés. Perte maximale du plan : environ -$6 sur les nouvelles lignes, plus la baisse des positions existantes. *Invalidation de la thèse de plancher : clôture journalière BTC < $52k.*
2. **L'unlock HYPE du 6 déc. est vraiment distribué** (environ 9,9 M HYPE, soit environ $650 M, contre 180k le 6 nov.) et les rachats ne compensent pas. *Invalidation : HYPE < $53,5.* Le refus ou le retard de la CFTC sur les perps ICE/Hyperliquid est un risque secondaire.
3. **Choc de gouvernance sur TRON / JST** (Justin Sun, rachats suspendus). Comme JST est illiquide, le stop pourrait glisser fortement. *Invalidation : JST < $0,133.*

## 8. Déclencheurs de revue

- **Date : dimanche 7 déc. 2026**, après l'unlock HYPE et avant le FOMC. Annule ou garde les ordres limites non exécutés.
- **Revoir plus tôt si :**
  - le BTC clôture sous $55 000 ou au-dessus de $67 000 ;
  - HYPE passe sous $56 ou plus de 2 M HYPE quittent les wallets de l'équipe le 6 déc. ;
  - JST passe sous $0,134 ;
  - le Fear & Greed remonte au-dessus de 40 (le marché sort de la capitulation, envisager de redéployer le cash) ;
  - la Fed annonce une hausse de 50 pb.

---

### Rejeté
- **XMR** : la paire XMR/EUR est en ligne, mais Kraken a retiré Monero pour les clients EEE en 2024, et MEXC l'a délisté le 13 nov. 2026. Ce n'est donc pas une option pour toi.
- **SOL** (composite 55) et **LINK** (composite 50) : aucun avantage sur HYPE. LINK a un overhang d'unlocks trimestriels.

*Recherche uniquement. Pas un conseil financier. Les chiffres de sources secondaires divergent parfois : les liens sont fournis pour vérification.*
