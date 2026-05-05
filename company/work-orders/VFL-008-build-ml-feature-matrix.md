# VFL-008 - Build ML Feature Matrix

## Status

Done

## Objective

Build a leakage-safe feature matrix for the first ML volatility-forecasting comparison.

## Scope

- Add transparent lagged/rolling volatility features available at timestamp `t`.
- Keep features separate from forward target construction.
- Support both next-day and next-week target horizons.
- Add tests proving feature timestamps do not use future returns.

## Acceptance Criteria

- Feature function returns a stable schema with documented columns.
- Tests cover row alignment and no future-return usage.
- Docs explain the feature contract.
- No ML model is added in this work order unless the feature layer is already verified.

## Claim Boundary

This work creates input features for future forecasting comparisons. It does not produce or claim model performance.

## Closeout Evidence

- Added `ml_feature_matrix(returns)` with `(ticker, feature)` MultiIndex columns.
- Added tests for stable schema and no future-return usage.
- Added `docs/ml-feature-contract.md`.
- Verified tests and lint before push.
- No ML model was added in this work order.
