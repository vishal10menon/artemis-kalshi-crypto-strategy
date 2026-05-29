# Artemis Kalshi Event Contract Strategy

**Track:** Kalshi Prediction Markets  
**Competition:** Artemis Quant Competition 2026  
**Deadline:** June 1, 2026

## Strategy Overview

This project implements a systematic trading strategy for Kalshi event contracts. The core idea is a simple mean-reversion fair value model that compares an estimated probability against live Kalshi market prices. Positions are taken only when the gap between the model and the market exceeds a 5% threshold after basic liquidity filters.

The current implementation uses a placeholder fair value model (constant 0.62) because live crypto-related Kalshi markets were unavailable during development. The pipeline is designed to work with any Kalshi event contract.

## Repository Structure
artemis-kalshi-crypto-strategy/
├── src/
│   ├── strategy.py          # Main signal generation
│   ├── fair_value.py        # Fair probability model
│   ├── market_data.py       # Kalshi API data fetch
│   ├── backtest.py          # Multi-market backtest loop
│   └── find_markets.py      # Helper to discover open Kalshi markets
├── reports/
│   └── research_report_outline.md
├── slides/
│   └── pitch_deck_outline.md
├── data/
│   └── kalshi_sample_markets.csv   # Placeholder data
├── .gitignore
├── LICENSE
└── README.md

## How to Run

```bash
# 1. Install dependencies
pip install requests

# 2. Run the strategy on a single market
python src/strategy.py KXMVESPORTSMULTIGAMEEXTENDED-S20269601D2B45CD-FF122287453

# 3. Run the backtest across multiple markets
python src/backtest.py

# 4. Discover current open Kalshi markets
python src/find_markets.py
