# Block-Bootstrap Error Differences

This report estimates uncertainty around pairwise forecast-error differences using contiguous validation-date block resampling.

Difference convention: `metric(model_a) - metric(model_b)`. Negative values mean `model_a` had lower forecast error for that diagnostic.

Defaults: 20-trading-day blocks, 1,000 bootstrap resamples, fixed random seed, and 95% percentile intervals.

These intervals are forecast-error uncertainty diagnostics only. They are not trading, allocation, alpha, investment, or economic-value evidence.

## Summary Counts

| horizon   | metric   | model_a                  | model_b                   | mostly_negative   | interval_crosses_zero   |   ticker_count |
|:----------|:---------|:-------------------------|:--------------------------|:------------------|:------------------------|---------------:|
| next_day  | mae      | har_daily_weekly_monthly | expanding_mean_abs_return | False             | True                    |              2 |
| next_day  | mae      | har_daily_weekly_monthly | expanding_mean_abs_return | True              | False                   |              2 |
| next_day  | mae      | har_daily_weekly_monthly | expanding_mean_abs_return | True              | True                    |              1 |
| next_day  | mae      | hist_gradient_boosting   | expanding_mean_abs_return | True              | False                   |              5 |
| next_day  | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  | False             | True                    |              4 |
| next_day  | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  | True              | False                   |              1 |
| next_day  | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return | True              | False                   |              5 |
| next_day  | rmse     | hist_gradient_boosting   | expanding_mean_abs_return | True              | False                   |              5 |
| next_day  | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  | False             | True                    |              5 |
| next_week | mae      | har_daily_weekly_monthly | expanding_mean_abs_return | True              | False                   |              5 |
| next_week | mae      | hist_gradient_boosting   | expanding_mean_abs_return | True              | False                   |              5 |
| next_week | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  | False             | True                    |              5 |
| next_week | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return | True              | False                   |              5 |
| next_week | rmse     | hist_gradient_boosting   | expanding_mean_abs_return | True              | False                   |              5 |
| next_week | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  | False             | True                    |              5 |

## Pairwise Error Differences

| horizon   | ticker   | metric   | model_a                  | model_b                   |   observed_difference |   ci_lower |   ci_upper |   share_negative |
|:----------|:---------|:---------|:-------------------------|:--------------------------|----------------------:|-----------:|-----------:|-----------------:|
| next_day  | GLD      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.001617 |  -0.004099 |   0.000696 |         0.898000 |
| next_day  | GLD      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.002366 |  -0.004338 |  -0.000217 |         0.987000 |
| next_day  | GLD      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000749 |  -0.001743 |   0.000299 |         0.909000 |
| next_day  | GLD      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.007616 |  -0.012753 |  -0.002561 |         1.000000 |
| next_day  | GLD      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.008167 |  -0.013208 |  -0.002736 |         1.000000 |
| next_day  | GLD      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000551 |  -0.002099 |   0.000899 |         0.739000 |
| next_day  | IWM      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.002049 |  -0.007668 |   0.002379 |         0.741000 |
| next_day  | IWM      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.004592 |  -0.010296 |  -0.000169 |         0.982000 |
| next_day  | IWM      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.002543 |  -0.004756 |  -0.000644 |         0.995000 |
| next_day  | IWM      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.019386 |  -0.039726 |  -0.002981 |         1.000000 |
| next_day  | IWM      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.017762 |  -0.033971 |  -0.002609 |         0.996000 |
| next_day  | IWM      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.001624 |  -0.003419 |   0.006800 |         0.326000 |
| next_day  | QQQ      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.004872 |  -0.010118 |  -0.000868 |         0.995000 |
| next_day  | QQQ      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.006514 |  -0.010457 |  -0.003274 |         1.000000 |
| next_day  | QQQ      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.001642 |  -0.003952 |   0.000912 |         0.894000 |
| next_day  | QQQ      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.020572 |  -0.038144 |  -0.007528 |         1.000000 |
| next_day  | QQQ      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.017407 |  -0.030007 |  -0.007278 |         1.000000 |
| next_day  | QQQ      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.003165 |  -0.002153 |   0.009630 |         0.154000 |
| next_day  | SPY      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.006248 |  -0.012839 |  -0.001479 |         0.997000 |
| next_day  | SPY      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.007891 |  -0.012068 |  -0.004393 |         1.000000 |
| next_day  | SPY      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.001643 |  -0.003630 |   0.001038 |         0.917000 |
| next_day  | SPY      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.023825 |  -0.046127 |  -0.005492 |         1.000000 |
| next_day  | SPY      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.018568 |  -0.030878 |  -0.007103 |         1.000000 |
| next_day  | SPY      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.005257 |  -0.003166 |   0.015316 |         0.295000 |
| next_day  | TLT      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.001896 |  -0.004268 |   0.000261 |         0.956000 |
| next_day  | TLT      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.002524 |  -0.004474 |  -0.000811 |         0.999000 |
| next_day  | TLT      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000628 |  -0.001660 |   0.000328 |         0.881000 |
| next_day  | TLT      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.008799 |  -0.017837 |  -0.001609 |         0.997000 |
| next_day  | TLT      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.007134 |  -0.014268 |  -0.002096 |         1.000000 |
| next_day  | TLT      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.001664 |  -0.000964 |   0.004741 |         0.151000 |
| next_week | GLD      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.010185 |  -0.016925 |  -0.004133 |         1.000000 |
| next_week | GLD      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.010282 |  -0.016135 |  -0.004619 |         1.000000 |
| next_week | GLD      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000097 |  -0.001648 |   0.001614 |         0.519000 |
| next_week | GLD      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.021547 |  -0.031010 |  -0.011325 |         1.000000 |
| next_week | GLD      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.023122 |  -0.032716 |  -0.013090 |         1.000000 |
| next_week | GLD      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.001575 |  -0.004114 |   0.001469 |         0.833000 |
| next_week | IWM      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.018034 |  -0.030442 |  -0.007976 |         1.000000 |
| next_week | IWM      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.018630 |  -0.029090 |  -0.010335 |         1.000000 |
| next_week | IWM      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000596 |  -0.004604 |   0.003974 |         0.651000 |
| next_week | IWM      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.041896 |  -0.067640 |  -0.016904 |         1.000000 |
| next_week | IWM      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.037406 |  -0.055658 |  -0.019143 |         1.000000 |
| next_week | IWM      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.004491 |  -0.004488 |   0.013533 |         0.251000 |
| next_week | QQQ      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.026392 |  -0.039410 |  -0.015845 |         1.000000 |
| next_week | QQQ      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.025252 |  -0.034829 |  -0.017916 |         1.000000 |
| next_week | QQQ      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.001140 |  -0.002639 |   0.006509 |         0.297000 |
| next_week | QQQ      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.047953 |  -0.069740 |  -0.027685 |         1.000000 |
| next_week | QQQ      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.038901 |  -0.050990 |  -0.028152 |         1.000000 |
| next_week | QQQ      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.009052 |  -0.001967 |   0.020919 |         0.085000 |
| next_week | SPY      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.016827 |  -0.029950 |  -0.007462 |         1.000000 |
| next_week | SPY      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.019266 |  -0.027440 |  -0.011938 |         1.000000 |
| next_week | SPY      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.002440 |  -0.006328 |   0.003472 |         0.834000 |
| next_week | SPY      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.041888 |  -0.071545 |  -0.014940 |         1.000000 |
| next_week | SPY      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.034071 |  -0.047567 |  -0.019627 |         1.000000 |
| next_week | SPY      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.007817 |  -0.007236 |   0.024108 |         0.306000 |
| next_week | TLT      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.008758 |  -0.014067 |  -0.004296 |         1.000000 |
| next_week | TLT      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.009181 |  -0.013913 |  -0.005072 |         1.000000 |
| next_week | TLT      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000423 |  -0.002818 |   0.001327 |         0.687000 |
| next_week | TLT      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.017088 |  -0.027397 |  -0.008569 |         1.000000 |
| next_week | TLT      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.016873 |  -0.024532 |  -0.010209 |         1.000000 |
| next_week | TLT      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.000215 |  -0.004547 |   0.003387 |         0.453000 |

## Interpretation

`share_negative` is the share of bootstrap resamples where `model_a` has lower error than `model_b`. Intervals crossing zero should be treated as weak or mixed evidence. Even intervals mostly on one side of zero remain conditional method-comparison evidence for the named horizon, ticker, metric, and validation design only.