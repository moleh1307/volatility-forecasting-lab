# Target Definitions

## Initial Target

Milestone 1 starts with next-day realized volatility:

```text
target_t = abs(log_return_{t+1}) * sqrt(252)
```

Forecasts available at date `t` may use information known through date `t`, but not the next-day return.

The implementation routes this through the generic forward realized-volatility target with `horizon = 1`.

## Planned Extension

The target pipeline is horizon-aware so next-week realized volatility can be added without changing the validation contract.

For horizon `h`, the planned target definition is:

```text
target_t,h = sqrt((252 / h) * sum_{i=1..h}(log_return_{t+i}^2))
```

A later next-week report should still define:

- whether the five-trading-day window is overlapping or non-overlapping;
- why the sum-of-squares realized-volatility target is the chosen definition;
- how missing market holidays are handled;
- how the horizon affects validation rows and report labels.

## Claim Boundary

These targets are forecast-error targets only. They are not trading returns, allocation returns, alpha signals, or investment performance metrics.
