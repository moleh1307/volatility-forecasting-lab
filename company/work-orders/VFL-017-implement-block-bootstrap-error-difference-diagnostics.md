# VFL-017 - Implement Block-Bootstrap Error-Difference Diagnostics

## Owner Role

Research Engineer

## Status

Done

## Lifecycle State

Done

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

- Added `block_bootstrap_error_differences` evaluation helper using paired
  model errors and moving contiguous date blocks.
- Added tests for difference sign convention and reproducibility.
- Updated `scripts/run_baseline_evaluation.py` to generate block-bootstrap
  diagnostics for the protocol's three pairwise comparisons.
- Generated `artifacts/reports/bootstrap_error_differences.md`.
- Generated ignored CSV diagnostic:
  - `artifacts/reports/bootstrap_error_differences.csv`
- `uv run pytest` passed with 15 tests.
- `uv run ruff check .` passed.
- `uv run python scripts/run_baseline_evaluation.py` regenerated reports and wrote 60 bootstrap rows.

## Closeout State

Done. Next work order is `VFL-018 - Review Milestone 3 evidence and update public summary`.
