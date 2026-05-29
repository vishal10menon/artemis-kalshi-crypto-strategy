# Artemis Kalshi Event Contract Strategy

**Track:** Kalshi Prediction Markets  
**Competition:** Artemis Quant Competition 2026  
**Deadline:** June 1, 2026

## Strategy Overview

This project implements a systematic trading strategy for Kalshi event contracts. The core idea is a simple mean-reversion fair value model that compares an estimated probability against live Kalshi market prices. Positions are taken only when the gap between the model and the market exceeds a 5% threshold after basic liquidity filters.

The current implementation uses a placeholder fair value model (constant 0.62) because live crypto-related Kalshi markets were unavailable during development. The pipeline is designed to work with any Kalshi event contract.

## Repository Structure
