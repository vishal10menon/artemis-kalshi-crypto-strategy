import sys

from market_data import get_kalshi_probability


def calculate_edge(fair_probability: float, kalshi_probability: float) -> float:
    """
    Calculate the pricing edge between estimated fair probability and Kalshi price.

    Example:
        fair_probability = 0.62
        kalshi_probability = 0.54
        edge = 0.08
    """
    return fair_probability - kalshi_probability


def generate_signal(
    fair_probability: float,
    kalshi_probability: float,
    threshold: float = 0.05,
) -> str:
    """
    Generate a trade signal based on the gap between fair value and market price.

    Returns:
        BUY_YES: fair value is meaningfully above Kalshi price
        BUY_NO: fair value is meaningfully below Kalshi price
        HOLD: no clear edge
    """
    edge = calculate_edge(fair_probability, kalshi_probability)

    if edge > threshold:
        return "BUY_YES"

    if edge < -threshold:
        return "BUY_NO"

    return "HOLD"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python src/strategy.py <KALSHI_MARKET_TICKER>")

    ticker = sys.argv[1]

    # Temporary placeholder until we connect the real crypto/fair-value model.
    fair_probability = 0.62

    kalshi_probability = get_kalshi_probability(ticker)
    signal = generate_signal(fair_probability, kalshi_probability)
    edge = calculate_edge(fair_probability, kalshi_probability)

    print("Ticker:", ticker)
    print("Fair probability:", fair_probability)
    print("Kalshi probability:", kalshi_probability)
    print("Edge:", edge)
    print("Signal:", signal)

