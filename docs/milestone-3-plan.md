# Milestone 3 Plan: Robustness And Uncertainty Diagnostics

## Purpose

Milestone 3 should test whether the Milestone 2 model-comparison patterns are stable enough to trust as research diagnostics.

The goal is not to add more model families first. The goal is to understand uncertainty, ranking stability, and sensitivity around the existing baselines.

## Starting Point

Milestone 2 found:

- ML provides useful nonlinear diagnostic contrast.
- ML often improves MAE versus HAR.
- ML does not consistently improve RMSE versus HAR.
- Subperiod behavior is mixed across horizons, metrics, tickers, and baselines.

## Research Question

How stable are model rankings and forecast-error differences across time, tickers, horizons, and resampled validation blocks?

## Scope

Milestone 3 should add:

- rolling-window model-rank summaries;
- block-bootstrap confidence intervals for forecast-error differences;
- concise stability review notes;
- clear public claim boundaries.

## Non-Goals

- No new model family until robustness diagnostics are in place.
- No hyperparameter sweep.
- No trading, allocation, alpha, or investment interpretation.
- No "best model" claim without stability evidence.

## Proposed Work Orders

- `VFL-015`: Design robustness and uncertainty protocol.
- `VFL-016`: Implement rolling-window ranking diagnostics.
- `VFL-017`: Implement block-bootstrap error-difference diagnostics.
- `VFL-018`: Review Milestone 3 evidence and update public summary.

## Acceptance Gates

Milestone 3 is coherent only if:

- diagnostics are reproducible from tracked scripts;
- outputs separate horizon, ticker, model, and metric;
- uncertainty language is explicit;
- public wording remains diagnostic and non-investment-oriented.
