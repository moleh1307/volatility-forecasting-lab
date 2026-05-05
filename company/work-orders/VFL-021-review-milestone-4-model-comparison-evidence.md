# VFL-021 - Review Milestone 4 Model-Comparison Evidence

## Owner Role

Research Lead

## Status

Done

## Lifecycle State

Done

## Risk Lane

Normal

## Objective

Review whether the GARCH baseline changes the project's econometric-versus-ML
interpretation.

## Scope

- Compare GARCH, HAR, ML, and simple baselines across horizons and metrics.
- Inspect rolling-window and bootstrap diagnostics after adding GARCH.
- Update public summary language if needed.
- Preserve no-trading/no-model-superiority claim boundary.

## Acceptance Criteria

- Add a Milestone 4 comparison review under `docs/`.
- State supported and unsupported claims explicitly.
- `uv run pytest`, `uv run ruff check .`, and report regeneration pass.

## Canonical Artifact

- Planned: `docs/milestone-4-comparison-review.md`

## Verification Evidence

- Added `docs/milestone-4-comparison-review.md`.
- Review found GARCH lower than HAR in 0/10 full-slice MAE comparisons and 0/10 RMSE comparisons.
- Review found GARCH lower than ML in 0/10 full-slice MAE comparisons and 0/10 RMSE comparisons.
- Review found GARCH lower than expanding mean in 3/10 MAE comparisons and 5/10 RMSE comparisons.
- Review preserves no-trading/no-broad-model-superiority claim boundary.

## Closeout State

Done. Next decision is whether to run Milestone 4 release readiness or continue diagnostic refinement.
