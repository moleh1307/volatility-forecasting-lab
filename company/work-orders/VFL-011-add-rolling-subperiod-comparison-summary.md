# VFL-011 - Add Rolling Subperiod Comparison Summary

## Status

Done

## Objective

Add a rolling or subperiod comparison summary to check whether Milestone 2 model behavior is stable across time.

## Scope

- Summarize model rankings by ticker, horizon, and subperiod.
- Keep MAE and RMSE separate.
- Avoid model-superiority wording.
- Prefer compact CSV and Markdown outputs under `artifacts/reports/` and `docs/`.

## Acceptance Criteria

- Summary is reproducible from existing report/forecast outputs or clearly adds needed forecast-output artifacts.
- Report states whether model behavior is stable or mixed.
- Tests/lint/report commands pass.

## Closeout Evidence

- Added calendar-year subperiod metrics via `evaluate_forecasts_by_period`.
- `scripts/run_baseline_evaluation.py` now writes `artifacts/reports/subperiod_model_comparison.csv` and tracked Markdown report.
- Added `docs/subperiod-stability-review.md`.
- Verified tests, lint, report regeneration, and claim-boundary scan.
