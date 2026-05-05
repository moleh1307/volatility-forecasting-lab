# VFL-009 - Add First Scikit-Learn ML Baseline

## Status

Done

## Objective

Add the first modest scikit-learn ML volatility forecasting baseline using the verified feature matrix.

## Candidate Scope

- Prefer `HistGradientBoostingRegressor` or `RandomForestRegressor`.
- Train separate models by ticker and horizon.
- Use `ml_feature_matrix(returns)` as the feature source.
- Enforce the horizon-specific label-availability rule: at timestamp `t`, train only on labels whose full forward target window is observable by `t`.
- Keep next-day and next-week reports separate.

## Acceptance Criteria

- Tests cover ML training alignment.
- Reports include ML rows without cross-horizon comparisons.
- Runtime remains reasonable for routine report regeneration.
- README/report wording preserves the claim boundary.

## Closeout Evidence

- Added `hist_gradient_boosting_vol_forecast`.
- Model trains separately by ticker and horizon using `ml_feature_matrix`.
- Training at timestamp `t` only uses labels whose full forward target window is observable by `t`.
- Reports now include `hist_gradient_boosting` rows.
- Verified tests, lint, report regeneration, runtime, and claim-boundary wording.
