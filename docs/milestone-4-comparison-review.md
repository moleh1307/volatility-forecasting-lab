# Milestone 4 Comparison Review: GARCH Baseline

## Purpose

Milestone 4 adds `garch_1_1` as a stronger econometric volatility baseline. This
review checks whether that changes the project interpretation before any further
ML expansion.

## Implementation Summary

- Added `arch>=7.0` as a project dependency; current resolved version is
  `arch==8.0.0`.
- Added `garch_vol_forecast`.
- Forecasts use annual expanding-window GARCH(1,1) refits.
- Daily decimal returns are scaled to percentages for model fitting and converted
  back to annualized volatility forecasts.
- Next-day and next-week reports use the same target and validation protocol as
  existing baselines.

## Full-Slice Findings

Across 10 horizon/ticker slices:

| Comparison | MAE: GARCH Lower | RMSE: GARCH Lower |
| --- | ---: | ---: |
| GARCH vs HAR | 0 / 10 | 0 / 10 |
| GARCH vs ML | 0 / 10 | 0 / 10 |
| GARCH vs expanding mean | 3 / 10 | 5 / 10 |

The GARCH row improves the baseline set, but under the current annual-refit
specification it does not outperform HAR or the first ML baseline in full-slice
MAE/RMSE.

## Rolling-Window Findings

The rolling-window report now contains 6,400 ranking rows.

GARCH has some rolling-window wins, especially next-day MAE, but it has fewer
wins and weaker average ranks than HAR and the ML baseline:

| Horizon | Metric | GARCH Wins |
| --- | --- | ---: |
| next_day | MAE | 25 |
| next_day | RMSE | 6 |
| next_week | MAE | 3 |
| next_week | RMSE | 1 |

This suggests GARCH adds diagnostic coverage but does not change the main
ranking story.

## Bootstrap Findings

The bootstrap report now contains 120 rows.

Key patterns:

- `hist_gradient_boosting` has lower error than `garch_1_1` across all tickers,
  horizons, and metrics in the bootstrap summary.
- `garch_1_1` does not show lower error than HAR in any ticker for MAE or RMSE.
- GARCH versus expanding mean is mixed: it improves some RMSE slices, especially
  next-week RMSE, but not consistently across metrics and horizons.

## Interpretation

Adding GARCH makes the econometric baseline set more credible, but this specific
baseline does not weaken the earlier conclusion that HAR remains the stronger
transparent econometric comparator.

The ML baseline still looks useful as a nonlinear diagnostic row. However, the
ML-versus-HAR evidence remains conditional and mixed because many ML/HAR
bootstrap intervals cross zero, especially for RMSE and next-week comparisons.

## Claim Boundary

Supported:

- The repo now compares simple baselines, HAR, GARCH(1,1), and the first ML
  baseline under one validation protocol.
- GARCH adds an important econometric reference point.
- Current GARCH results do not dominate HAR or ML.
- HAR remains the stronger transparent econometric benchmark in this
  implementation.

Not supported:

- A claim that GARCH, HAR, or ML is universally best.
- A claim that ML beats econometric baselines in general.
- Any trading, allocation, alpha, investment, or economic-value interpretation.

## Next Step

Run a Milestone 4 release-readiness check only if this GARCH baseline should be
tagged publicly. Otherwise, continue with diagnostic refinement rather than adding
another model family immediately.
