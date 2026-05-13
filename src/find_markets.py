import requests

KALSHI_BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"


def find_markets():
    url = f"{KALSHI_BASE_URL}/markets"

    cursor = None
    matches = []
    sample_markets = []
    total_checked = 0

    keywords = [
        "bitcoin",
        "btc",
        "kxbtc",
        "ethereum",
        "ether",
        "kxeth",
        "crypto",
        "solana",
        "sol",
    ]

    for _ in range(10):
        params = {
            "status": "open",
            "limit": 100,
        }

        if cursor:
            params["cursor"] = cursor

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        markets = data.get("markets", [])
        cursor = data.get("cursor")

        for market in markets:
            total_checked += 1

            ticker = market.get("ticker", "")
            event_ticker = market.get("event_ticker", "")
            title = market.get("title", "")
            subtitle = market.get("subtitle", "")

            text = f"{ticker} {event_ticker} {title} {subtitle}".lower()

            if len(sample_markets) < 20:
                sample_markets.append((ticker, title, subtitle))

            if any(word in text for word in keywords):
                matches.append((ticker, event_ticker, title, subtitle))

        if not cursor:
            break

    print(f"Checked {total_checked} markets.")
    print()

    if matches:
        print("Crypto-related matches:")
        print()

        for ticker, event_ticker, title, subtitle in matches:
            print("Ticker:", ticker)
            print("Event:", event_ticker)
            print("Title:", title)
            print("Subtitle:", subtitle)
            print()
    else:
        print("No crypto matches found.")
        print()
        print("Here are sample open markets so we can inspect what Kalshi is returning:")
        print()

        for ticker, title, subtitle in sample_markets:
            print("Ticker:", ticker)
            print("Title:", title)
            print("Subtitle:", subtitle)
            print()


if __name__ == "__main__":
    find_markets()

