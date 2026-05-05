# Rolling-Window Model Ranking

This report checks whether model rankings are stable across rolling validation windows. Windows use 252 trading days, step forward by 21 trading days, and require at least 126 observations per model.

Lower MAE/RMSE ranks better inside a given horizon, ticker, metric, and window. These are forecast-error diagnostics only, not trading, allocation, alpha, or investment results.

## Best-Model Counts

| horizon   | metric   | model                     |   rolling_window_wins |
|:----------|:---------|:--------------------------|----------------------:|
| next_day  | mae      | expanding_mean_abs_return |                    61 |
| next_day  | mae      | garch_1_1                 |                    25 |
| next_day  | mae      | har_daily_weekly_monthly  |                    56 |
| next_day  | mae      | hist_gradient_boosting    |                   178 |
| next_day  | rmse     | expanding_mean_abs_return |                    45 |
| next_day  | rmse     | garch_1_1                 |                     6 |
| next_day  | rmse     | har_daily_weekly_monthly  |                   111 |
| next_day  | rmse     | hist_gradient_boosting    |                   158 |
| next_week | mae      | expanding_mean_abs_return |                    51 |
| next_week | mae      | garch_1_1                 |                     3 |
| next_week | mae      | har_daily_weekly_monthly  |                   100 |
| next_week | mae      | hist_gradient_boosting    |                   166 |
| next_week | rmse     | expanding_mean_abs_return |                    25 |
| next_week | rmse     | garch_1_1                 |                     1 |
| next_week | rmse     | har_daily_weekly_monthly  |                   123 |
| next_week | rmse     | hist_gradient_boosting    |                   171 |

## Average Rank

| horizon   | metric   | model                     |   average_rank |
|:----------|:---------|:--------------------------|---------------:|
| next_day  | mae      | hist_gradient_boosting    |          1.613 |
| next_day  | mae      | har_daily_weekly_monthly  |          2.322 |
| next_day  | mae      | expanding_mean_abs_return |          2.600 |
| next_day  | mae      | garch_1_1                 |          3.525 |
| next_day  | mae      | lagged_abs_return         |          4.941 |
| next_day  | rmse     | hist_gradient_boosting    |          1.641 |
| next_day  | rmse     | har_daily_weekly_monthly  |          1.897 |
| next_day  | rmse     | expanding_mean_abs_return |          2.944 |
| next_day  | rmse     | garch_1_1                 |          3.556 |
| next_day  | rmse     | lagged_abs_return         |          4.963 |
| next_week | mae      | hist_gradient_boosting    |          1.559 |
| next_week | mae      | har_daily_weekly_monthly  |          2.013 |
| next_week | mae      | expanding_mean_abs_return |          3.003 |
| next_week | mae      | garch_1_1                 |          3.456 |
| next_week | mae      | lagged_abs_return         |          4.969 |
| next_week | rmse     | hist_gradient_boosting    |          1.531 |
| next_week | rmse     | har_daily_weekly_monthly  |          1.844 |
| next_week | rmse     | expanding_mean_abs_return |          3.328 |
| next_week | rmse     | garch_1_1                 |          3.372 |
| next_week | rmse     | lagged_abs_return         |          4.925 |

## Best-Model Instability Flags

| horizon   | ticker   | metric   |   distinct_best_models | best_model_changed   |
|:----------|:---------|:---------|-----------------------:|:---------------------|
| next_day  | GLD      | mae      |                      3 | True                 |
| next_day  | GLD      | rmse     |                      4 | True                 |
| next_day  | IWM      | mae      |                      4 | True                 |
| next_day  | IWM      | rmse     |                      3 | True                 |
| next_day  | QQQ      | mae      |                      3 | True                 |
| next_day  | QQQ      | rmse     |                      2 | True                 |
| next_day  | SPY      | mae      |                      3 | True                 |
| next_day  | SPY      | rmse     |                      2 | True                 |
| next_day  | TLT      | mae      |                      4 | True                 |
| next_day  | TLT      | rmse     |                      4 | True                 |
| next_week | GLD      | mae      |                      4 | True                 |
| next_week | GLD      | rmse     |                      4 | True                 |
| next_week | IWM      | mae      |                      3 | True                 |
| next_week | IWM      | rmse     |                      3 | True                 |
| next_week | QQQ      | mae      |                      3 | True                 |
| next_week | QQQ      | rmse     |                      3 | True                 |
| next_week | SPY      | mae      |                      3 | True                 |
| next_week | SPY      | rmse     |                      2 | True                 |
| next_week | TLT      | mae      |                      3 | True                 |
| next_week | TLT      | rmse     |                      3 | True                 |

## Interpretation

Rolling-window rankings are intended to expose time variation in forecast-error behavior. A higher win count or lower average rank should not be compressed into a broad model-superiority claim without matching uncertainty evidence.