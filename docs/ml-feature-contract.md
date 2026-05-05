# ML Feature Contract

## Purpose

Define the first leakage-safe feature matrix for Milestone 2 ML volatility-forecasting comparisons.

This feature layer does not train a model and does not produce performance evidence.

## Shape

`ml_feature_matrix(returns)` returns a DataFrame indexed by date with two-level columns:

```text
(ticker, feature_name)
```

This keeps ticker-specific features explicit for future per-ticker model training.

## Initial Features

Each row is timestamped at date `t` and uses information available through `t` only:

- `signed_return_1d`
- `abs_return_1d`
- `vol_1d`
- `vol_mean_5d`
- `vol_mean_22d`
- `vol_std_5d`
- `vol_std_22d`
- `signed_return_mean_5d`
- `signed_return_mean_22d`

`vol_*` features use annualized absolute daily log returns as transparent volatility proxies.

## Leakage Boundary

Features must not use:

- `return_{t+1}`;
- any return inside the forward target window;
- target values;
- random row shuffles;
- information from other horizons' future labels.

The target construction remains separate from the feature matrix.

## Next Use

`VFL-009` should consume this matrix for the first scikit-learn ML baseline. Model training must still enforce the horizon-specific label-availability rule from `docs/validation-protocol.md`.
