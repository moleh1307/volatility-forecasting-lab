# Volatility Forecasting Lab

Reproducible volatility-forecasting research lab using free public market data.

The project starts conservatively: build trustworthy data, target, baseline, and validation machinery before adding ML models.

## Scope

- V0 panel: SPY, QQQ, IWM, GLD, TLT
- Data: free/no-key public market data via `yfinance`
- Initial targets: next-day realized volatility, with horizon-aware design for next-week targets
- Milestone 1: data pipeline, target construction, baseline forecasts, validation protocol, honest evaluation report

## Non-Goals

- No trading system
- No allocation strategy
- No live execution
- No investment recommendation
- No performance claims
- No claim that ML beats econometric baselines

## Quickstart

```bash
uv sync
uv run pytest
uv run ruff check .
uv run python scripts/fetch_data.py
uv run python scripts/run_baseline_evaluation.py
```

Generated data caches live under `data/` and are ignored by git. Generated reports live under `artifacts/reports/`.

## Current Status

Local-first research repo scaffold. Public GitHub push is intentionally deferred until milestone 1 has a credible baseline report and clean README.
