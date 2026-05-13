import sys

from market_data import get_kalshi_probability


def calculate_edge(fair_probability: float, kalshi_probability: float) -> float:
    """
    Calculate the pricing edge between estimated fair probability and Kalshi price.
    """
    return fair_probability - kalshi_probability


def generate_signal(
    fair_probability: float,
    kalshi_probability: float,
    threshold: float = 0.05,
) -> str:
    """
    Generate a trade signal based on the gap between fair value and market price.
    """
    edge = calculate_edge(fair_probability, kalshi_probability)

    if edge > threshold:
        return "BUY_YES"

    if edge < -threshold:
        return "BUY_NO"

    return "HOLD"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(
            "Usage: python src/strategy.py <KALSHI_MARKET_TICKER> <FAIR_PROBABILITY>"
        )

    ticker = sys.argv[1]
    fair_probability = float(sys.argv[2])

    kalshi_probability = get_kalshi_probability(ticker)
    signal = generate_signal(fair_probability, kalshi_probability)
    edge = calculate_edge(fair_probability, kalshi_probability)

    print("Ticker:", ticker)
    print("Fair probability:", fair_probability)
    print("Kalshi probability:", kalshi_probability)
    print("Edge:", edge)
    print("Signal:", signal)
