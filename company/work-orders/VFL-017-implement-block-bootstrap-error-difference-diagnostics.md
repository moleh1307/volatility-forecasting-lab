# VFL-017 - Implement Block-Bootstrap Error-Difference Diagnostics

## Owner Role

Research Engineer

## Status

Active

## Lifecycle State

Active

## Risk Lane

Normal

## Objective

Implement the block-bootstrap pairwise error-difference diagnostic defined in
`docs/robustness-uncertainty-protocol.md`.

## Scope

- Use validation-slice forecast-error panels for existing model forecasts.
- Compute pairwise MAE and RMSE differences using the protocol convention:
  `metric(model_a) - metric(model_b)`.
- Resample contiguous validation-date blocks with fixed seed and configurable
  block length/resample count.
- Generate a CSV diagnostic output and tracked Markdown summary.
- Add focused tests for block generation, reproducibility, and difference sign.

## Acceptance Criteria

- Bootstrap CSV and Markdown report are reproducible from a tracked CLI.
- Outputs include observed differences, percentile interval bounds, share
  negative, block length, and resample count.
- Interpretation language remains diagnostic and non-investment-oriented.
- `uv run pytest`, `uv run ruff check .`, and report regeneration pass.

## Canonical Artifact

- Planned: `artifacts/reports/bootstrap_error_differences.csv`
- Planned: `artifacts/reports/bootstrap_error_differences.md`

## Verification Evidence

Pending.

## Closeout State

Not started.
