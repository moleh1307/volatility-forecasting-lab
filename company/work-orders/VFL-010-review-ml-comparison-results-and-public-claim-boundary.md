# VFL-010 - Review ML Comparison Results And Public Claim Boundary

## Status

Done

## Objective

Review the first ML comparison results and public wording before treating Milestone 2 as coherent.

## Scope

- Inspect next-day and next-week report tables with the ML baseline rows.
- Compare ML behavior against simple and HAR baselines without claiming robust superiority.
- Add a short review note under `docs/`.
- Confirm README/report wording preserves the forecasting-methodology boundary.

## Acceptance Criteria

- Review states what the ML row does and does not show.
- Any suspicious result or caveat is documented.
- Claim-boundary scan passes.
- Tests, lint, and report regeneration pass.

## Closeout Evidence

- Added `docs/ml-comparison-review.md`.
- Review documents that ML improves MAE versus HAR in 5/5 next-day tickers and 4/5 next-week tickers, but improves RMSE in only 1/5 tickers for each horizon.
- README and docs preserve the no model-superiority claim boundary.
- Verified tests, lint, report regeneration, and claim-boundary scan.
