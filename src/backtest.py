from strategy import generate_signal, calculate_edge
import matplotlib.pyplot as plt
from market_data import get_kalshi_probability
from fair_value import get_fair_probability

markets = [
    "KXMVESPORTSMULTIGAMEEXTENDED-S20269601D2B45CD-FF122287453",
    "KXMVESPORTSMULTIGAMEEXTENDED-S202659668525F4C-031CC73E6FB",
    "KXMVESPORTSMULTIGAMEEXTENDED-S2026BFBA0F21C23-921685113D6",
]

results = []
equity = [100]

for ticker in markets:
    try:
        fair = get_fair_probability(ticker)
        kalshi = get_kalshi_probability(ticker)
        signal = generate_signal(fair, kalshi)
        edge = calculate_edge(fair, kalshi)

        # simple pseudo-PnL model (MUST be inside loop)
        if signal == 1:
            pnl = edge * 10
        elif signal == -1:
            pnl = -edge * 10
        else:
            pnl = 0

        equity.append(equity[-1] + pnl)

        results.append({
            "ticker": ticker,
            "fair": fair,
            "kalshi": kalshi,
            "edge": edge,
            "signal": signal,
        })

    except Exception as e:
        results.append({
            "ticker": ticker,
            "error": str(e),
        })

for r in results:
    print(r)

# plot equity curve AFTER loop finishes
plt.figure()
plt.plot(equity)
plt.title("Strategy Equity Curve")
plt.xlabel("Trades")
plt.ylabel("Portfolio Value")
plt.grid(True)

plt.savefig("assets/equity_curve.png")
plt.show()
