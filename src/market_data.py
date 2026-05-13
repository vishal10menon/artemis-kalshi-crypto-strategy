import requests

KALSHI_BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"


def get_kalshi_probability(ticker: str) -> float:
    print(f"Fetching market: {ticker}")

    url = f"{KALSHI_BASE_URL}/markets/{ticker}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    market = data["market"]

    price_fields = [
        "yes_ask",
        "last_price",
        "yes_bid",
        "yes_ask_dollars",
        "last_price_dollars",
        "yes_bid_dollars",
    ]

    for field in price_fields:
        value = market.get(field)

        if value is None:
            continue

        value = float(value)

        if value > 1:
            return value / 100

        return value

    raise ValueError(f"No usable price found for market: {ticker}")


