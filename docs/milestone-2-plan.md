# Milestone 2 Plan: First ML Forecasting Comparison

## Purpose

Add the first ML volatility-forecasting comparison without weakening the baseline methodology or overstating results.

Milestone 2 should answer a narrow research question:

> On the same public-data panel, horizons, validation slice, and error metrics, do simple tree-based ML baselines behave differently from transparent statistical volatility baselines?

This is a forecasting-methodology comparison, not a trading or investment result.

## Current Baseline Anchor

Milestone 1 provides:

- V0 panel: SPY, QQQ, IWM, GLD, TLT.
- Targets: next-day and overlapping next-week realized volatility.
- Metrics: MAE, RMSE, and bias by ticker, horizon, and model.
- Baselines:
  - lagged absolute return;
  - expanding mean absolute return;
  - HAR-style daily/weekly/monthly expanding-window OLS baseline.

## Candidate ML Scope

Start with one deliberately modest ML model family:

- `RandomForestRegressor` or `HistGradientBoostingRegressor` from scikit-learn.
- Forecast each ticker/horizon separately at first.
- Use only lagged return/volatility features available at timestamp `t`.
- Keep expanding or rolling time-series training. Do not random-shuffle rows.

Do not add neural networks, deep learning frameworks, hyperparameter sweeps, dashboards, or broad asset universes in Milestone 2.

## Feature Contract

Initial ML features should be transparent and leakage-safe:

- lagged absolute return;
- rolling 5-day mean absolute return;
- rolling 22-day mean absolute return;
- rolling 5-day realized-volatility proxy;
- rolling 22-day realized-volatility proxy;
- optional recent signed return lags if documented as known at `t`.

Feature rows must be timestamped at `t` and must not use `return_{t+1}` or any part of the forward target window.

## Validation Contract

- Keep the validation start at `2020-01-01` unless a new documented protocol supersedes it.
- Compare models only within the same ticker, horizon, target definition, date range, and metric.
- For horizon `h`, model training at timestamp `t` may only use target labels whose full forward target window is observable by `t`.
- Report ML output as forecast-error diagnostics, not model superiority or useful signal evidence.

## Acceptance Gates

Before Milestone 2 can be called complete:

1. Tests cover feature/target alignment for ML features.
2. Next-day and next-week reports include ML rows without mixing horizons.
3. README and report wording preserve the claim boundary.
4. A short review note states whether ML adds useful diagnostic contrast versus baselines, without claiming robust outperformance.
5. `uv run pytest`, `uv run ruff check .`, and report regeneration pass.

## Proposed Work Orders

- `VFL-008`: Build leakage-safe feature matrix for ML comparison.
- `VFL-009`: Add first scikit-learn ML baseline with expanding/rolling training.
- `VFL-010`: Review ML comparison results and public claim boundary.
