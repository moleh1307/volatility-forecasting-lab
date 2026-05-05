# VFL-002 - Review Target Construction And Leakage Risks

## Status

Active

## Objective

Review the next-day realized-volatility target construction and baseline alignment before treating the first report as public-ready.

## Scope

- Audit whether forecasts at date `t` only use information available through date `t`.
- Confirm target labels and report wording match the actual horizon.
- Check whether validation rows and observations are aligned consistently across tickers and models.
- Identify the minimum changes needed before adding next-week targets or ML benchmarks.

## Acceptance Criteria

- Leakage risks are documented or ruled out.
- Any code defects found in target/forecast alignment are fixed.
- A concise review note is added under `docs/` or the work order closeout.
- Task board is re-ranked after the review.

## Claim Boundary

The review can promote the scaffold as ready for further methodology work, but not as evidence of useful model performance.
