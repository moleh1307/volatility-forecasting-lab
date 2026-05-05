# Milestone 3 Summary: Robustness And Uncertainty Diagnostics

## Purpose

Milestone 3 adds robustness diagnostics around the existing volatility-forecasting
baselines before introducing any new model families.

The milestone asks whether model-comparison patterns are stable across rolling
time windows and whether pairwise forecast-error differences are large relative
to block-bootstrap uncertainty.

## What Changed

- Added `docs/robustness-uncertainty-protocol.md`.
- Added validation-slice forecast-error panel construction.
- Added rolling-window model ranking diagnostics.
- Added block-bootstrap pairwise error-difference diagnostics.
- Kept the model set fixed: lagged absolute return, expanding mean absolute
  return, HAR-style statistical baseline, and the first scikit-learn ML baseline.

## Diagnostic Outputs

- `artifacts/reports/rolling_window_model_ranking.md`
- `artifacts/reports/bootstrap_error_differences.md`

The generated CSV diagnostics remain ignored by git and can be regenerated with:

```bash
uv run python scripts/run_baseline_evaluation.py
```

## Rolling-Window Findings

The rolling-window diagnostic produced 5,120 ranking rows.

Across 252-trading-day windows stepped by 21 trading days:

| Horizon | Metric | Main Pattern |
| --- | --- | --- |
| next_day | MAE | `hist_gradient_boosting` has the most rolling-window wins, but rankings vary by ticker and window. |
| next_day | RMSE | `hist_gradient_boosting` has the most wins, while HAR remains competitive. |
| next_week | MAE | `hist_gradient_boosting` has the most wins, with HAR also winning many windows. |
| next_week | RMSE | `hist_gradient_boosting` has the most wins, but best-model identity still changes over time. |

Every horizon/ticker/metric group shows best-model changes across rolling windows.
This is stability evidence against a simple one-model-wins narrative.

## Bootstrap Findings

The block-bootstrap diagnostic produced 60 rows:

- 2 horizons;
- 5 tickers;
- 2 metrics;
- 3 pairwise model comparisons.

Key patterns:

- `hist_gradient_boosting` versus `expanding_mean_abs_return`: bootstrap evidence
  is consistently negative across all tickers, horizons, and metrics, meaning the
  ML baseline has lower forecast error than the expanding-mean baseline in this
  diagnostic.
- `har_daily_weekly_monthly` versus `expanding_mean_abs_return`: HAR is generally
  stronger than the expanding-mean baseline, especially for RMSE and next-week
  metrics.
- `hist_gradient_boosting` versus `har_daily_weekly_monthly`: evidence is mixed.
  Most intervals cross zero, especially for RMSE and next-week comparisons.

## Interpretation

Milestone 3 strengthens the repo because it moves beyond full-slice error tables.
The results now show both ranking instability and uncertainty around pairwise
differences.

The ML baseline remains useful as a nonlinear diagnostic comparison. The strongest
evidence is that both ML and HAR improve on the expanding-mean baseline under the
current validation design. Evidence for ML versus HAR is conditional and mixed,
not a robust model-superiority result.

## Claim Boundary

Supported:

- The repo now includes reproducible robustness diagnostics.
- Rolling-window rankings show that model rankings vary over time.
- Bootstrap intervals show stronger evidence versus the expanding-mean baseline
  than versus HAR.
- ML is a useful diagnostic comparison row under the current methodology.

Not supported:

- A trading system, allocation strategy, alpha signal, or investment claim.
- A broad claim that ML beats HAR.
- A claim that any model is universally best across horizons, tickers, metrics,
  and time windows.
- A claim that forecast-error improvements imply economic value.

## Next Step

Run a Milestone 3 release-readiness check before deciding whether to tag a
`v0.3.0-milestone-3` release.
