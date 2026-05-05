# Target Definitions

## Initial Target

Milestone 1 starts with next-day realized volatility:

```text
target_t = abs(log_return_{t+1}) * sqrt(252)
```

Forecasts available at date `t` may use information known through date `t`, but not the next-day return.

## Planned Extension

The target pipeline should remain horizon-aware so next-week realized volatility can be added without changing the validation contract. A later next-week target should define:

- whether the five-trading-day window is overlapping or non-overlapping;
- whether the target is sum-of-squares realized volatility or average absolute return;
- how missing market holidays are handled;
- how the horizon affects validation rows and report labels.

## Claim Boundary

These targets are forecast-error targets only. They are not trading returns, allocation returns, alpha signals, or investment performance metrics.
