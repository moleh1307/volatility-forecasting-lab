# Milestone 4 Plan: Stronger Econometric Baseline

## Purpose

Milestone 4 adds a stronger econometric volatility baseline before adding more ML
model families.

Milestone 3 showed that the first ML baseline is useful as a nonlinear diagnostic
row, but ML-versus-HAR evidence remains mixed. A GARCH-family baseline improves
the econometric comparison set and raises the credibility of later ML claims.

## Scope

Milestone 4 should add:

- a GARCH(1,1) daily-return volatility baseline using `arch`;
- next-day and next-week forecasts from the same validation protocol;
- regenerated baseline, rolling-window, and bootstrap diagnostics;
- a short comparison review focused on whether GARCH changes the interpretation
  of ML versus econometric baselines.

## Non-Goals

- No hyperparameter search.
- No EGARCH/GJR-GARCH model sweep in this milestone.
- No trading, allocation, alpha, or investment interpretation.
- No claim that GARCH, HAR, or ML is universally best.

## Proposed Work Orders

- `VFL-020`: Add GARCH(1,1) econometric baseline.
- `VFL-021`: Review Milestone 4 model-comparison evidence and claim boundary.

## Acceptance Gates

Milestone 4 is coherent only if:

- the GARCH baseline is reproducible from tracked scripts;
- runtime remains acceptable for the small V0 panel;
- tests cover the new baseline's basic forecast contract;
- reports keep horizons, tickers, metrics, and model names separate;
- public wording remains diagnostic and non-investment-oriented.
