# Artemis Kalshi Event Contract Strategy

**Track:** Kalshi Prediction Markets  
**Competition:** Artemis Quant Competition 2026  
**Submission Date:** June 1, 2026

## Strategy Overview

This project presents a systematic trading strategy for Kalshi event contracts. The strategy uses a simple mean-reversion fair value model to identify mispricings between the model probability and live Kalshi market prices. Trades are executed only when the absolute edge exceeds a 5% threshold after applying liquidity filters.

The fair value model applies a base probability of 0.50 with a fixed ±0.12 adjustment based on whether the Kalshi price is above or below 0.50. This creates a conservative mean-reversion bias. The model is intentionally simple due to the unavailability of live crypto Kalshi markets during development.

## Repository Structure

artemis-kalshi-crypto-strategy/
├── src/
│   ├── strategy.py          # Signal generation and edge calculation
│   ├── fair_value.py        # Fair probability model with documentation
│   ├── market_data.py       # Kalshi Trade API v2 data fetch
│   ├── backtest.py          # Multi-market backtest and results
│   └── find_markets.py      # Open market discovery tool
├── reports/
│   └── research_report.pdf
├── slides/
│   └── pitch_deck.pdf
├── data/
│   └── kalshi_sample_markets.csv
├── .gitignore
├── LICENSE
└── README.md

## How to Run

```bash
pip install requests

# Run strategy on a single market
python src/strategy.py KXMVESPORTSMULTIGAMEEXTENDED-S20269601D2B45CD-FF122287453

# Run full backtest
python src/backtest.py

# Discover current open Kalshi markets
python src/find_markets.py
## Deliverables

- Research Report: reports/research_report.pdf

- Reproducible Code: this GitHub repository

- Pitch Deck: slides/pitch_deck.pdf (also shared via Google Slides with lindsey@artemisanalytics.xyz)

## Limitations and Critical Evaluation
The fair value model remains a simple, uncalibrated rule. No external data sources (CME FedWatch, FRED, or macro releases) were incorporated. The backtest shows limited variation across markets due to the static nature of the current model. Edge decay is expected as market efficiency improves. Full discussion of limitations is provided in the research report.
