# Artemis Kalshi Event Contract Strategy

**Track:** Kalshi Prediction Markets
**Competition:** Artemis Quant Competition 2026
**Submission Date:** June 1, 2026

---

## Strategy Overview

This project presents a systematic trading strategy for Kalshi event contracts focused on crypto price milestone markets. The strategy uses a simple mean-reversion fair value model to identify mispricings between the model probability and live Kalshi market prices. Trades are executed only when the absolute edge exceeds a 5% threshold after applying liquidity filters.

The fair value model applies a base probability of `0.50` with a fixed `±0.12` adjustment based on whether the Kalshi price is above or below `0.50`. This creates a conservative mean-reversion bias. The model is intentionally simple due to the unavailability of live crypto Kalshi markets during development.

The core idea is to treat Kalshi prices as noisy observations of true event probabilities and exploit temporary deviations through disciplined mean reversion. The approach prioritizes robustness over complexity and avoids overfitting to historical patterns that may not persist in prediction markets.

---

## Fair Value Model

The fair value calculation is defined as:

* Base probability = `0.50`
* Adjustment = `+0.12` when Kalshi price > `0.50`
* Adjustment = `-0.12` when Kalshi price < `0.50`

Edge is computed as the absolute difference between the model probability and the Kalshi market price.

Positions are only taken when:

* Edge exceeds `5%`
* Liquidity filters are satisfied

This conservative bias prevents aggressive betting on extreme deviations and helps manage risk in thin markets.

---

## Repository Structure

```text
artemis-kalshi-crypto-strategy/
├── src/
│   ├── strategy.py          # Signal generation and edge calculation
│   ├── fair_value.py        # Fair probability model with documentation
│   ├── market_data.py       # Kalshi Trade API v2 data fetch
│   ├── backtest.py          # Multi-market backtest and results
│   └── market_scanner.py      # Open market discovery and filtering
│
├── reports/
│   └── research_report.pdf
│
├── slides/
│   └── pitch_deck.pdf
│
├── data/
│   └── kalshi_sample_markets.csv
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

No additional dependencies are required beyond the Python `requests` package.

---

## How to Run

### Run strategy on a single market

```bash
python src/strategy.py MARKET_TICKER
```

Example:

```bash
python src/strategy.py KXMVESPORTSMULTIGAMEEXTENDED-S20269601D2B45CD-FF122287453
```

### Run the backtest

```bash
python src/backtest.py
```

### Discover open Kalshi markets

```bash
python src/market_scanner.py
```

---

## Backtest Results

The backtest runs across multiple sample markets using historical Kalshi price data.

Results are generated in:

```text
src/backtest.py
```

Detailed metrics and analysis are available in:

```text
reports/research_report.pdf
```

The current implementation demonstrates modest but consistent edge capture due to the static nature of the fair value model.

---

## Deliverables

* Research Report: `reports/research_report.pdf`
* Reproducible Code: this GitHub repository
* Pitch Deck: `slides/pitch_deck.pdf`

---

## Limitations

The current fair value model is intentionally simple and remains uncalibrated.

Current limitations include:

* No external macroeconomic or volatility data inputs
* Static adjustment parameter
* Limited historical market coverage
* No live execution framework
* No dynamic risk management layer

The absence of live crypto Kalshi markets during development constrained model validation and calibration.

---

## Future Improvements

Potential future enhancements include:

* Incorporating macroeconomic releases and volatility indicators
* Dynamic parameter calibration
* Position sizing and drawdown controls
* Live market streaming support
* Multi-factor probabilistic forecasting models
* Automated execution infrastructure

---

## License

MIT License
