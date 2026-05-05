# ML Comparison Review

## Scope

Review the first Milestone 2 ML comparison after adding the `hist_gradient_boosting` baseline to the next-day and next-week reports.

## Result

Status: reviewed diagnostic comparison.

The ML baseline adds useful diagnostic contrast, but it does not justify a model-superiority claim.

## What The ML Row Is

- Model: `HistGradientBoostingRegressor`.
- Training: separate model by ticker and horizon.
- Refitting: annual expanding-window refits.
- Features: leakage-safe current/past return and volatility features from `ml_feature_matrix`.
- Guardrail: at timestamp `t`, training only uses labels whose full forward target window is observable by `t`.

## Result Pattern

Against the HAR-style OLS baseline:

- Next-day horizon:
  - ML has lower MAE for 5 of 5 tickers.
  - ML has lower RMSE for 1 of 5 tickers.
- Next-week horizon:
  - ML has lower MAE for 4 of 5 tickers.
  - ML has lower RMSE for 1 of 5 tickers.

This pattern suggests the ML baseline may reduce typical absolute error in several slices, but it does not consistently reduce larger-error penalties versus HAR.

## Caveats

- The ML model is deliberately modest and not tuned.
- The validation slice has already been inspected during methodology development, so this is a diagnostic comparison, not fresh holdout evidence.
- No uncertainty intervals, rolling subperiod review, or statistical test has been added yet.
- The comparison is by ticker and horizon only; it is not a portfolio, trading, allocation, alpha, or investment result.

## Public Claim Boundary

Acceptable wording:

- "Milestone 2 adds a first leakage-safe ML baseline for diagnostic comparison."
- "The ML row provides useful contrast against transparent statistical baselines."
- "Results are mixed across metrics and should not be read as robust ML superiority."

Avoid wording:

- ML beats econometric baselines.
- ML outperforms.
- Alpha, signal, strategy, or investment performance.
- Any claim that the current results are robust or tradeable.

## Next Methodology Work

Useful next work should be review-oriented before adding more model families:

1. Review subperiod stability before adding more model families.
2. Consider a simpler linear/scikit-learn baseline only if it clarifies whether nonlinear ML is adding anything beyond HAR.
3. Add uncertainty or ranking-stability diagnostics before stronger public claims.
