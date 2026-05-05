# Validation Protocol

## Purpose

Define a conservative evaluation boundary before ML models are introduced.

## Current Protocol

- Data source: cached `yfinance` adjusted close data for SPY, QQQ, IWM, GLD, and TLT.
- Training/evaluation style: time-ordered validation only.
- Current validation slice: rows from `2020-01-01` onward.
- Initial targets: next-day annualized realized volatility and overlapping next-week annualized realized volatility.
- Initial metrics: MAE, RMSE, and bias by ticker.
- Initial baselines:
  - lagged absolute return;
  - expanding mean absolute return.

## Rules

- Do not random-shuffle time-series rows.
- Do not tune baselines or ML models on the validation slice and then report it as independent evidence.
- Keep target labels explicit about horizon.
- Compare models only on the same ticker, horizon, target definition, date range, and metric.
- Treat current metrics as forecast-error diagnostics, not performance claims.

## Before Public Push

Run a claim-boundary review of README and generated reports to confirm there are no trading, allocation, alpha, or model-superiority claims.
