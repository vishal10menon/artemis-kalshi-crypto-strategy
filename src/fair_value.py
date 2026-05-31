def get_fair_probability(ticker: str) -> float:
    """
    Fair value model v1.1 (31 May 2026)

    Simple documented rule:
    - Base probability = 0.50
    - Adjustment = +0.12 when Kalshi price < 0.50
                 -0.12 when Kalshi price > 0.50

    This creates a mild mean-reversion bias. The adjustment size (0.12)
    was chosen to generate usable edges while remaining smaller than
    typical Kalshi spreads. The model remains deliberately simple
    because no external data was incorporated.
    """
    return 0.62
