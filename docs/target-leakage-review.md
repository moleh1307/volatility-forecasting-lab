# Target And Leakage Review

## Scope

This review covers the milestone 1 next-day realized-volatility target, baseline forecast alignment, validation rows, and claim boundary.

## Result

Status: working-assumption promoted to reviewed scaffold.

The current next-day setup is coherent enough for milestone 1 continuation. It is not evidence of useful model performance.

## Alignment Review

- Forecast timestamp: date `t`.
- Information allowed at `t`: prices and returns through date `t`.
- Next-day target: `abs(log_return_{t+1}) * sqrt(252)`.
- `lagged_abs_return` forecast uses `abs(log_return_t) * sqrt(252)`.
- `expanding_mean_abs_return` uses expanding historical absolute returns through `t`.
- The final cached return date has no next-day target and is excluded by the non-null metric mask.

## Verification Snapshot

- Cached prices: 4,108 rows, 5 tickers, 2010-01-04 to 2026-05-04.
- Return matrix: 4,107 rows, 2010-01-05 to 2026-05-04.
- Next-day target matrix: 4,107 rows, 2010-01-05 to 2026-05-04.
- Non-null validation target rows: 2020-01-02 to 2026-05-01.
- Baseline report observations: 1,591 per ticker/model.
- Tests and lint passed after adding a generic forward realized-volatility target.

## Risks And Caveats

- The validation start row on 2020-01-02 uses the return ending on 2020-01-02 as a forecast input and the next trading-day return as target. This is acceptable for an end-of-day forecast framing but should remain explicit.
- Current baselines are simple diagnostics, not optimized econometric models.
- `yfinance` adjusted prices can be revised; the tracked manifest records source bounds, while raw prices remain ignored.
- Next-week targets should use the same horizon-aware target function and should label overlapping windows clearly.

## Minimum Next Changes

1. Add next-week target/report only after keeping next-day report labels stable.
2. Add a stronger econometric baseline, likely GARCH-family or HAR-style, only after the no-leakage target contract is preserved in tests.
3. Before public GitHub push, review README/report wording again for model-superiority, trading, allocation, and performance-claim drift.
