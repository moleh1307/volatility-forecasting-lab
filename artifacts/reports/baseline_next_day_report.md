# Baseline Next-Day Volatility Forecast Evaluation

Validation slice starts at `2020-01-01`.
Target horizon: `1` trading day(s).

This report compares simple baseline forecasts for next-day annualized realized volatility. It is a methodology scaffold, not an investment or trading result.

Lower MAE/RMSE indicates lower forecast error within this target, date range, and ticker only. The table should not be read across horizons or as a trading performance result.

| model                     | ticker   |   observations |      mae |     rmse |      bias |
|:--------------------------|:---------|---------------:|---------:|---------:|----------:|
| expanding_mean_abs_return | GLD      |           1591 | 0.085858 | 0.128926 | -0.016056 |
| har_daily_weekly_monthly  | GLD      |           1591 | 0.084241 | 0.121309 | -0.005501 |
| lagged_abs_return         | GLD      |           1591 | 0.113961 | 0.166360 | -0.000129 |
| expanding_mean_abs_return | IWM      |           1591 | 0.120798 | 0.188064 | -0.034691 |
| har_daily_weekly_monthly  | IWM      |           1591 | 0.118749 | 0.168679 | -0.006792 |
| lagged_abs_return         | IWM      |           1591 | 0.157980 | 0.225749 | -0.000044 |
| expanding_mean_abs_return | QQQ      |           1591 | 0.118457 | 0.183529 | -0.036366 |
| har_daily_weekly_monthly  | QQQ      |           1591 | 0.113585 | 0.162957 | -0.008226 |
| lagged_abs_return         | QQQ      |           1591 | 0.154746 | 0.218232 |  0.000146 |
| expanding_mean_abs_return | SPY      |           1591 | 0.093745 | 0.157020 | -0.021221 |
| har_daily_weekly_monthly  | SPY      |           1591 | 0.087497 | 0.133195 | -0.004091 |
| lagged_abs_return         | SPY      |           1591 | 0.116621 | 0.175295 |  0.000056 |
| expanding_mean_abs_return | TLT      |           1591 | 0.076525 | 0.112116 | -0.014033 |
| har_daily_weekly_monthly  | TLT      |           1591 | 0.074629 | 0.103317 | -0.003794 |
| lagged_abs_return         | TLT      |           1591 | 0.098389 | 0.132703 |  0.000036 |

## Caveats

- yfinance data is a free public-data source and can be revised.
- Baselines are intentionally simple and are not tuned for performance claims.
- The HAR-style baseline is an expanding-window OLS statistical benchmark; it is not an optimized ML model or trading strategy.
- Metrics describe forecast errors only; they are not trading, allocation, or alpha metrics.