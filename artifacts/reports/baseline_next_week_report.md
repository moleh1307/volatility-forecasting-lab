# Baseline Next-Week Volatility Forecast Evaluation

Validation slice starts at `2020-01-01`.
Target horizon: `5` trading day(s).

This report compares simple baseline forecasts for overlapping five-trading-day annualized realized volatility. It is a methodology scaffold, not an investment or trading result.

Lower MAE/RMSE indicates lower forecast error within this target, date range, and ticker only. The table should not be read across horizons or as a trading performance result.

| model                     | ticker   |   observations |      mae |     rmse |      bias |
|:--------------------------|:---------|---------------:|---------:|---------:|----------:|
| expanding_mean_abs_return | GLD      |           1587 | 0.062747 | 0.101638 | -0.043926 |
| har_daily_weekly_monthly  | GLD      |           1587 | 0.052562 | 0.080092 | -0.006326 |
| hist_gradient_boosting    | GLD      |           1587 | 0.052465 | 0.078517 | -0.009146 |
| lagged_abs_return         | GLD      |           1587 | 0.098596 | 0.134628 | -0.028118 |
| expanding_mean_abs_return | IWM      |           1587 | 0.091797 | 0.155570 | -0.071149 |
| har_daily_weekly_monthly  | IWM      |           1587 | 0.073763 | 0.113673 | -0.009864 |
| hist_gradient_boosting    | IWM      |           1587 | 0.073167 | 0.118164 | -0.024712 |
| lagged_abs_return         | IWM      |           1587 | 0.135904 | 0.183389 | -0.036457 |
| expanding_mean_abs_return | QQQ      |           1587 | 0.094857 | 0.154155 | -0.072735 |
| har_daily_weekly_monthly  | QQQ      |           1587 | 0.068465 | 0.106201 | -0.012115 |
| hist_gradient_boosting    | QQQ      |           1587 | 0.069606 | 0.115253 | -0.031090 |
| lagged_abs_return         | QQQ      |           1587 | 0.127918 | 0.175167 | -0.036121 |
| expanding_mean_abs_return | SPY      |           1587 | 0.073870 | 0.136468 | -0.048418 |
| har_daily_weekly_monthly  | SPY      |           1587 | 0.057044 | 0.094580 | -0.006056 |
| hist_gradient_boosting    | SPY      |           1587 | 0.054604 | 0.102397 | -0.019126 |
| lagged_abs_return         | SPY      |           1587 | 0.097251 | 0.142255 | -0.026976 |
| expanding_mean_abs_return | TLT      |           1587 | 0.054997 | 0.087918 | -0.035813 |
| har_daily_weekly_monthly  | TLT      |           1587 | 0.046240 | 0.070830 | -0.004364 |
| hist_gradient_boosting    | TLT      |           1587 | 0.045817 | 0.071045 | -0.008666 |
| lagged_abs_return         | TLT      |           1587 | 0.083489 | 0.110198 | -0.021557 |

## Caveats

- yfinance data is a free public-data source and can be revised.
- Baselines are intentionally simple and are not tuned for performance claims.
- The HAR-style baseline is an expanding-window OLS statistical benchmark; it is not an optimized ML model or trading strategy.
- The histogram gradient boosting row is a modest scikit-learn ML baseline with annual expanding-window refits, not a tuned model selection result.
- Metrics describe forecast errors only; they are not trading, allocation, or alpha metrics.