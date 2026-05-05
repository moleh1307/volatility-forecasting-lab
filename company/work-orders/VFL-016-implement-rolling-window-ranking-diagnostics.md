# VFL-016 - Implement Rolling-Window Ranking Diagnostics

## Owner Role

Research Engineer

## Status

Done

## Lifecycle State

Done

## Risk Lane

Normal

## Objective

Implement the rolling-window ranking diagnostic defined in
`docs/robustness-uncertainty-protocol.md`.

## Scope

- Materialize or derive validation-slice forecast-error panels from existing
  forecasts and targets.
- Compute rolling MAE and RMSE ranks by horizon, ticker, model, and window.
- Generate a CSV diagnostic output and tracked Markdown summary.
- Add focused tests for rolling-window construction and ranking behavior.

## Acceptance Criteria

- Rolling-window CSV and Markdown report are reproducible from a tracked CLI.
- Outputs separate horizon, ticker, metric, model, window start, and window end.
- Interpretation language remains diagnostic and non-investment-oriented.
- `uv run pytest`, `uv run ruff check .`, and report regeneration pass.

## Canonical Artifact

- Planned: `artifacts/reports/rolling_window_model_ranking.csv`
- Planned: `artifacts/reports/rolling_window_model_ranking.md`

## Verification Evidence

- Added `forecast_error_panel` and `rolling_window_model_ranking` evaluation helpers.
- Added tests for forecast-error panel materialization and lower-error ranking order.
- Updated `scripts/run_baseline_evaluation.py` to generate rolling-window diagnostics.
- Generated `artifacts/reports/rolling_window_model_ranking.md`.
- Generated ignored CSV diagnostics:
  - `artifacts/reports/forecast_error_panel.csv`
  - `artifacts/reports/rolling_window_model_ranking.csv`
- `uv run pytest` passed with 13 tests.
- `uv run ruff check .` passed.
- `uv run python scripts/run_baseline_evaluation.py` regenerated reports and wrote 5,120 rolling-ranking rows.

## Closeout State

Done. Next work order is `VFL-017 - Implement block-bootstrap error-difference diagnostics`.
