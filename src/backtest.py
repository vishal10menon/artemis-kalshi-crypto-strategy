print("BACKTEST STARTED")
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

        print(f"DEBUG: {ticker} | signal={signal} | edge={edge}")

        if signal == "BUY_YES":
            pnl = abs(edge) * 10
        elif signal == "BUY_NO":
            pnl = -abs(edge) * 10
        else:
            pnl = 0

        equity.append(equity[-1] + pnl)

        results.append({
            "ticker": ticker,
            "fair": fair,
            "kalshi": kalshi,
            "edge": edge,
            "signal": signal,
            "pnl": pnl
        })

    except Exception as e:
        print(f"ERROR on {ticker}: {e}")
        results.append({
            "ticker": ticker,
            "error": str(e),
        })

print("\nFINAL RESULTS:")
for r in results:
    print(r)

# Plot equity curve (ONLY ONCE)
plt.figure(figsize=(8, 4))
plt.plot(equity, marker="o")
plt.title("Strategy Equity Curve")
plt.xlabel("Trades")
plt.ylabel("Portfolio Value")
plt.grid(True)

plt.savefig("equity_curve.png")
plt.show()
