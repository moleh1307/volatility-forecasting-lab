# Milestone 2 Summary: First ML Diagnostic Comparison

## Purpose

Milestone 2 adds the first leakage-safe ML baseline to the volatility forecasting lab and compares it against transparent statistical baselines.

This is a forecasting-methodology milestone. It is not a trading, allocation, alpha, or investment result.

## What Was Added

- Leakage-safe ML feature matrix with current/past-only return and volatility features.
- First scikit-learn ML baseline: `HistGradientBoostingRegressor`.
- Separate next-day and next-week forecast-error reports.
- Calendar-year subperiod comparison.
- Review notes for ML comparison and subperiod stability.

## Validation Setup

- Market panel: SPY, QQQ, IWM, GLD, TLT.
- Targets:
  - next-day annualized realized volatility;
  - overlapping next-week annualized realized volatility.
- Validation slice: starts at `2020-01-01`.
- Metrics: MAE, RMSE, and bias.
- ML training rule: at timestamp `t`, training only uses target labels whose full forward target window is observable by `t`.

## Result Snapshot

Against the HAR-style OLS baseline:

- Next-day MAE: ML lower than HAR for 5 of 5 tickers.
- Next-day RMSE: ML lower than HAR for 1 of 5 tickers.
- Next-week MAE: ML lower than HAR for 4 of 5 tickers.
- Next-week RMSE: ML lower than HAR for 1 of 5 tickers.

Calendar-year subperiod counts show that the ML row often ranks first in subperiod/ticker cells, but not uniformly across horizons, metrics, or baseline types.

## Interpretation

Milestone 2 is coherent as a diagnostic comparison:

- The ML baseline adds useful nonlinear contrast.
- HAR remains a strong transparent benchmark.
- MAE and RMSE tell different stories.
- Current results are mixed and should not be read as robust ML superiority.

## Claim Boundary

Do not claim:

- ML beats econometric baselines.
- ML is superior.
- Robust ML advantage.
- Trading signal, allocation result, alpha, investment performance, or live strategy relevance.

Acceptable summary:

> The repo now includes a first leakage-safe ML baseline. Results provide useful diagnostic contrast against statistical baselines, but the evidence is mixed across metrics and horizons.

## Canonical Outputs

- `artifacts/reports/baseline_next_day_report.md`
- `artifacts/reports/baseline_next_week_report.md`
- `artifacts/reports/subperiod_model_comparison.md`
- `docs/ml-comparison-review.md`
- `docs/subperiod-stability-review.md`
