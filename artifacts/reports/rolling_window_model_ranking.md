# Rolling-Window Model Ranking

This report checks whether model rankings are stable across rolling validation windows. Windows use 252 trading days, step forward by 21 trading days, and require at least 126 observations per model.

Lower MAE/RMSE ranks better inside a given horizon, ticker, metric, and window. These are forecast-error diagnostics only, not trading, allocation, alpha, or investment results.

## Best-Model Counts

| horizon   | metric   | model                     |   rolling_window_wins |
|:----------|:---------|:--------------------------|----------------------:|
| next_day  | mae      | expanding_mean_abs_return |                    68 |
| next_day  | mae      | har_daily_weekly_monthly  |                    63 |
| next_day  | mae      | hist_gradient_boosting    |                   189 |
| next_day  | rmse     | expanding_mean_abs_return |                    46 |
| next_day  | rmse     | har_daily_weekly_monthly  |                   115 |
| next_day  | rmse     | hist_gradient_boosting    |                   159 |
| next_week | mae      | expanding_mean_abs_return |                    51 |
| next_week | mae      | har_daily_weekly_monthly  |                   101 |
| next_week | mae      | hist_gradient_boosting    |                   168 |
| next_week | rmse     | expanding_mean_abs_return |                    26 |
| next_week | rmse     | har_daily_weekly_monthly  |                   123 |
| next_week | rmse     | hist_gradient_boosting    |                   171 |

## Average Rank

| horizon   | metric   | model                     |   average_rank |
|:----------|:---------|:--------------------------|---------------:|
| next_day  | mae      | hist_gradient_boosting    |          1.491 |
| next_day  | mae      | har_daily_weekly_monthly  |          2.172 |
| next_day  | mae      | expanding_mean_abs_return |          2.337 |
| next_day  | mae      | lagged_abs_return         |          4.000 |
| next_day  | rmse     | hist_gradient_boosting    |          1.553 |
| next_day  | rmse     | har_daily_weekly_monthly  |          1.847 |
| next_day  | rmse     | expanding_mean_abs_return |          2.619 |
| next_day  | rmse     | lagged_abs_return         |          3.981 |
| next_week | mae      | hist_gradient_boosting    |          1.538 |
| next_week | mae      | har_daily_weekly_monthly  |          1.925 |
| next_week | mae      | expanding_mean_abs_return |          2.550 |
| next_week | mae      | lagged_abs_return         |          3.987 |
| next_week | rmse     | hist_gradient_boosting    |          1.503 |
| next_week | rmse     | har_daily_weekly_monthly  |          1.784 |
| next_week | rmse     | expanding_mean_abs_return |          2.750 |
| next_week | rmse     | lagged_abs_return         |          3.962 |

## Best-Model Instability Flags

| horizon   | ticker   | metric   |   distinct_best_models | best_model_changed   |
|:----------|:---------|:---------|-----------------------:|:---------------------|
| next_day  | GLD      | mae      |                      3 | True                 |
| next_day  | GLD      | rmse     |                      3 | True                 |
| next_day  | IWM      | mae      |                      3 | True                 |
| next_day  | IWM      | rmse     |                      3 | True                 |
| next_day  | QQQ      | mae      |                      2 | True                 |
| next_day  | QQQ      | rmse     |                      2 | True                 |
| next_day  | SPY      | mae      |                      3 | True                 |
| next_day  | SPY      | rmse     |                      2 | True                 |
| next_day  | TLT      | mae      |                      3 | True                 |
| next_day  | TLT      | rmse     |                      3 | True                 |
| next_week | GLD      | mae      |                      3 | True                 |
| next_week | GLD      | rmse     |                      3 | True                 |
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