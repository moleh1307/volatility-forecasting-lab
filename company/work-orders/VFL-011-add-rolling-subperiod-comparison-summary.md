# VFL-011 - Add Rolling Subperiod Comparison Summary

## Status

Ready

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
