# Artemis Kalshi Fed Decision Calibration Strategy

## Strategy thesis
Kalshi Fed decision markets may lag changes in institutional rate expectations during high-volatility macro weeks, especially around CPI, NFP, and FOMC events.

## Market universe
Kalshi Fed rate decision contracts.

## Fair value model
Use CME FedWatch probabilities, FRED macro data, and event-date features to estimate fair probabilities for Kalshi outcomes.

## Signal
Enter when model-implied fair probability differs from Kalshi mid-price by more than a threshold after spread and liquidity filters.

## Risk management
Position sizing based on confidence, liquidity, spread width, and event correlation.

## Deliverables
- Research report
- Reproducible code
- Pitch deck
