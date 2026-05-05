# VFL-020 - Add GARCH Econometric Baseline

## Owner Role

Research Engineer

## Status

Done

## Lifecycle State

Done

## Risk Lane

Normal

## Objective

Add a GARCH(1,1) econometric volatility baseline to strengthen the baseline set
before adding more ML models.

## Scope

- Add `arch` as a project dependency.
- Implement an annual-refit GARCH(1,1) forecast baseline.
- Generate next-day and next-week forecasts through the existing report CLI.
- Include GARCH in rolling-window and bootstrap diagnostics.
- Add focused tests for the baseline forecast contract.

## Acceptance Criteria

- Baseline reports include `garch_1_1` rows.
- Rolling-window and bootstrap diagnostics include GARCH comparisons.
- `uv run pytest`, `uv run ruff check .`, and report regeneration pass.
- Public wording remains diagnostic and non-investment-oriented.

## Canonical Artifact

- Planned: updated baseline and robustness reports.

## Verification Evidence

- Added `arch>=7.0`; resolved version is `arch==8.0.0`.
- Added `garch_vol_forecast`.
- Added focused GARCH tests.
- Baseline reports include `garch_1_1` rows.
- Rolling-window diagnostics include `garch_1_1` and now write 6,400 rows.
- Bootstrap diagnostics include GARCH comparisons and now write 120 rows.
- Report regeneration completed in about 57 seconds.
- `uv run pytest` passed with 17 tests.
- `uv run ruff check .` passed.

## Closeout State

Done. Next work order is `VFL-021 - Review Milestone 4 model-comparison evidence`.
