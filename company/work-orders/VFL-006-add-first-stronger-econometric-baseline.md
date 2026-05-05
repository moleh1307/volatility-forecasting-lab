# VFL-006 - Add First Stronger Econometric Volatility Baseline

## Status

Done

## Objective

Add the first stronger econometric-style volatility baseline without introducing ML or trading claims.

## Candidate Scope

- Prefer a transparent HAR-style realized-volatility baseline if it fits the current data frequency and target definitions.
- Consider GARCH only if dependency stability and runtime remain reasonable.
- Keep next-day and next-week evaluations separate.

## Acceptance Criteria

- Baseline forecast uses only information available through timestamp `t`.
- Tests cover forecast alignment.
- Reports label the model as an econometric/statistical baseline, not an optimized strategy.
- Claim boundary remains forecasting-methodology only.

## Closeout Evidence

- Added HAR-style daily/weekly/monthly realized-volatility baseline.
- Training at timestamp `t` only uses labels whose full forward target window is observable by `t`.
- Added test covering delayed label availability for five-day targets.
- Regenerated next-day and next-week reports with HAR baseline rows.
- Verified tests, lint, report existence, and claim-boundary wording.
