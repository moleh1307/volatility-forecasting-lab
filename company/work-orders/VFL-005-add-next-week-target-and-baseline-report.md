# VFL-005 - Add Next-Week Target And Baseline Report

## Status

Done

## Objective

Add a next-week realized-volatility target and simple baseline evaluation without weakening the existing next-day validation contract.

## Scope

- Use the generic forward realized-volatility target with `horizon = 5`.
- Label overlapping five-trading-day windows explicitly.
- Generate a separate next-week baseline report.
- Keep next-day and next-week metrics separate.

## Acceptance Criteria

- Tests cover the five-day target alignment.
- Report names and docs make the horizon clear.
- Metrics compare models only within the same horizon.
- Claim boundary remains forecasting-methodology only.

## Closeout Evidence

- Extended `scripts/run_baseline_evaluation.py` to generate separate next-day and next-week reports.
- Added five-trading-day target alignment test.
- Updated README and docs to list next-day and next-week reports separately.
- Regenerated baseline reports.
- Verified tests, lint, report existence, and claim-boundary wording.
