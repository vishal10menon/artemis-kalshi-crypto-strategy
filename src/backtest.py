from market_data import get_kalshi_probability

markets = [
    ("KXMVESPORTSMULTIGAMEEXTENDED-S20269601D2B45CD-FF122287453", 0.62),
    ("KXMVESPORTSMULTIGAMEEXTENDED-S202659668525F4C-031CC73E6FB", 0.48),
    ("KXMVESPORTSMULTIGAMEEXTENDED-S2026BFBA0F21C23-921685113D6", 0.71),
]

results = []

for ticker, fair in markets:
    try:
        kalshi = get_kalshi_probability(ticker)
        edge = fair - kalshi

        if edge > 0.05:
            signal = "BUY_YES"
        elif edge < -0.05:
            signal = "BUY_NO"
        else:
            signal = "HOLD"

        results.append({
            "ticker": ticker,
            "fair": fair,
            "kalshi": kalshi,
            "edge": round(edge, 3),
            "signal": signal,
        })
    except Exception as e:
        results.append({"ticker": ticker, "error": str(e)})

for r in results:
    print(r)
