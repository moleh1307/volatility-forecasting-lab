# Target Definitions

## Initial Target

Milestone 1 starts with next-day realized volatility:

```text
target_t = abs(log_return_{t+1}) * sqrt(252)
```

Forecasts available at date `t` may use information known through date `t`, but not the next-day return.

The implementation routes this through the generic forward realized-volatility target with `horizon = 1`.

## Next-Week Target

The next-week target uses an overlapping five-trading-day forward window.

For horizon `h`, the planned target definition is:

```text
target_t,h = sqrt((252 / h) * sum_{i=1..h}(log_return_{t+i}^2))
```

For next-week reports, `h = 5`.

This means each forecast timestamp `t` is scored against the next five available trading-day returns. The final five rows do not have complete forward windows and are excluded from metric calculations by the non-null evaluation mask.

## Claim Boundary

These targets are forecast-error targets only. They are not trading returns, allocation returns, alpha signals, or investment performance metrics.
