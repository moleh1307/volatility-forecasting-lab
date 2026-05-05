# Subperiod Model Comparison

This report checks whether model behavior is stable across calendar-year subperiods inside the validation slice.

The counts below are forecast-error diagnostics only. They are not trading, allocation, alpha, or investment results.

## Full-Slice ML Versus HAR Counts

| horizon   | metric   |   ml_better_than_har_tickers |   ticker_count |
|:----------|:---------|-----------------------------:|---------------:|
| next_day  | mae      |                            5 |              5 |
| next_day  | rmse     |                            1 |              5 |
| next_week | mae      |                            4 |              5 |
| next_week | rmse     |                            1 |              5 |

## Calendar-Year Best-Model Counts

| horizon   | metric   | best_model                |   subperiod_ticker_wins |
|:----------|:---------|:--------------------------|------------------------:|
| next_day  | mae      | expanding_mean_abs_return |                       6 |
| next_day  | mae      | har_daily_weekly_monthly  |                       8 |
| next_day  | mae      | hist_gradient_boosting    |                      21 |
| next_day  | rmse     | expanding_mean_abs_return |                       5 |
| next_day  | rmse     | har_daily_weekly_monthly  |                      13 |
| next_day  | rmse     | hist_gradient_boosting    |                      17 |
| next_week | mae      | expanding_mean_abs_return |                       5 |
| next_week | mae      | har_daily_weekly_monthly  |                      12 |
| next_week | mae      | hist_gradient_boosting    |                      18 |
| next_week | rmse     | expanding_mean_abs_return |                       3 |
| next_week | rmse     | har_daily_weekly_monthly  |                      12 |
| next_week | rmse     | hist_gradient_boosting    |                      20 |

## Interpretation

Model behavior is mixed across metrics and horizons. The ML baseline is useful as a diagnostic comparison row, but the subperiod view should not be read as evidence of robust model superiority.