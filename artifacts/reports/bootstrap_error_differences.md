# Block-Bootstrap Error Differences

This report estimates uncertainty around pairwise forecast-error differences using contiguous validation-date block resampling.

Difference convention: `metric(model_a) - metric(model_b)`. Negative values mean `model_a` had lower forecast error for that diagnostic.

Defaults: 20-trading-day blocks, 1,000 bootstrap resamples, fixed random seed, and 95% percentile intervals.

These intervals are forecast-error uncertainty diagnostics only. They are not trading, allocation, alpha, investment, or economic-value evidence.

## Summary Counts

| horizon   | metric   | model_a                  | model_b                   | mostly_negative   | interval_crosses_zero   |   ticker_count |
|:----------|:---------|:-------------------------|:--------------------------|:------------------|:------------------------|---------------:|
| next_day  | mae      | garch_1_1                | expanding_mean_abs_return | False             | False                   |              5 |
| next_day  | mae      | garch_1_1                | har_daily_weekly_monthly  | False             | False                   |              5 |
| next_day  | mae      | har_daily_weekly_monthly | expanding_mean_abs_return | False             | True                    |              3 |
| next_day  | mae      | har_daily_weekly_monthly | expanding_mean_abs_return | True              | False                   |              2 |
| next_day  | mae      | hist_gradient_boosting   | expanding_mean_abs_return | True              | False                   |              5 |
| next_day  | mae      | hist_gradient_boosting   | garch_1_1                 | True              | False                   |              5 |
| next_day  | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  | False             | True                    |              4 |
| next_day  | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  | True              | False                   |              1 |
| next_day  | rmse     | garch_1_1                | expanding_mean_abs_return | False             | False                   |              2 |
| next_day  | rmse     | garch_1_1                | expanding_mean_abs_return | False             | True                    |              3 |
| next_day  | rmse     | garch_1_1                | har_daily_weekly_monthly  | False             | False                   |              5 |
| next_day  | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return | True              | False                   |              5 |
| next_day  | rmse     | hist_gradient_boosting   | expanding_mean_abs_return | True              | False                   |              5 |
| next_day  | rmse     | hist_gradient_boosting   | garch_1_1                 | True              | False                   |              5 |
| next_day  | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  | False             | True                    |              5 |
| next_week | mae      | garch_1_1                | expanding_mean_abs_return | False             | True                    |              5 |
| next_week | mae      | garch_1_1                | har_daily_weekly_monthly  | False             | False                   |              5 |
| next_week | mae      | har_daily_weekly_monthly | expanding_mean_abs_return | True              | False                   |              5 |
| next_week | mae      | hist_gradient_boosting   | expanding_mean_abs_return | True              | False                   |              5 |
| next_week | mae      | hist_gradient_boosting   | garch_1_1                 | True              | False                   |              5 |
| next_week | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  | False             | True                    |              5 |
| next_week | rmse     | garch_1_1                | expanding_mean_abs_return | False             | True                    |              2 |
| next_week | rmse     | garch_1_1                | expanding_mean_abs_return | True              | False                   |              3 |
| next_week | rmse     | garch_1_1                | har_daily_weekly_monthly  | False             | False                   |              5 |
| next_week | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return | True              | False                   |              5 |
| next_week | rmse     | hist_gradient_boosting   | expanding_mean_abs_return | True              | False                   |              5 |
| next_week | rmse     | hist_gradient_boosting   | garch_1_1                 | True              | False                   |              5 |
| next_week | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  | False             | True                    |              5 |

## Pairwise Error Differences

| horizon   | ticker   | metric   | model_a                  | model_b                   |   observed_difference |   ci_lower |   ci_upper |   share_negative |
|:----------|:---------|:---------|:-------------------------|:--------------------------|----------------------:|-----------:|-----------:|-----------------:|
| next_day  | GLD      | mae      | garch_1_1                | expanding_mean_abs_return |              0.004407 |   0.001767 |   0.007021 |         0.001000 |
| next_day  | GLD      | mae      | garch_1_1                | har_daily_weekly_monthly  |              0.006025 |   0.003383 |   0.008784 |         0.000000 |
| next_day  | GLD      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.001617 |  -0.004348 |   0.000836 |         0.887000 |
| next_day  | GLD      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.002366 |  -0.004597 |  -0.000355 |         0.993000 |
| next_day  | GLD      | mae      | hist_gradient_boosting   | garch_1_1                 |             -0.006773 |  -0.009302 |  -0.004378 |         1.000000 |
| next_day  | GLD      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000749 |  -0.001743 |   0.000299 |         0.909000 |
| next_day  | GLD      | rmse     | garch_1_1                | expanding_mean_abs_return |             -0.002377 |  -0.007861 |   0.002759 |         0.768000 |
| next_day  | GLD      | rmse     | garch_1_1                | har_daily_weekly_monthly  |              0.005239 |   0.002396 |   0.008263 |         0.000000 |
| next_day  | GLD      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.007616 |  -0.013166 |  -0.002510 |         0.998000 |
| next_day  | GLD      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.008167 |  -0.013223 |  -0.003027 |         1.000000 |
| next_day  | GLD      | rmse     | hist_gradient_boosting   | garch_1_1                 |             -0.005790 |  -0.008865 |  -0.003060 |         1.000000 |
| next_day  | GLD      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000551 |  -0.002099 |   0.000899 |         0.739000 |
| next_day  | IWM      | mae      | garch_1_1                | expanding_mean_abs_return |              0.009839 |   0.007146 |   0.013133 |         0.000000 |
| next_day  | IWM      | mae      | garch_1_1                | har_daily_weekly_monthly  |              0.011888 |   0.006203 |   0.018830 |         0.000000 |
| next_day  | IWM      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.002049 |  -0.007094 |   0.002305 |         0.746000 |
| next_day  | IWM      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.004592 |  -0.009776 |  -0.000174 |         0.978000 |
| next_day  | IWM      | mae      | hist_gradient_boosting   | garch_1_1                 |             -0.014431 |  -0.022209 |  -0.008803 |         1.000000 |
| next_day  | IWM      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.002543 |  -0.004558 |  -0.000516 |         0.991000 |
| next_day  | IWM      | rmse     | garch_1_1                | expanding_mean_abs_return |              0.007233 |   0.003819 |   0.010567 |         0.000000 |
| next_day  | IWM      | rmse     | garch_1_1                | har_daily_weekly_monthly  |              0.026618 |   0.008270 |   0.049197 |         0.000000 |
| next_day  | IWM      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.019386 |  -0.039295 |  -0.003263 |         1.000000 |
| next_day  | IWM      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.017762 |  -0.032832 |  -0.003162 |         0.999000 |
| next_day  | IWM      | rmse     | hist_gradient_boosting   | garch_1_1                 |             -0.024994 |  -0.044399 |  -0.008930 |         1.000000 |
| next_day  | IWM      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.001624 |  -0.003032 |   0.006903 |         0.260000 |
| next_day  | QQQ      | mae      | garch_1_1                | expanding_mean_abs_return |              0.006725 |   0.002735 |   0.010779 |         0.000000 |
| next_day  | QQQ      | mae      | garch_1_1                | har_daily_weekly_monthly  |              0.011597 |   0.006804 |   0.017375 |         0.000000 |
| next_day  | QQQ      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.004872 |  -0.009948 |  -0.001198 |         0.998000 |
| next_day  | QQQ      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.006514 |  -0.010451 |  -0.003459 |         1.000000 |
| next_day  | QQQ      | mae      | hist_gradient_boosting   | garch_1_1                 |             -0.013239 |  -0.018652 |  -0.007814 |         1.000000 |
| next_day  | QQQ      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.001642 |  -0.003959 |   0.000650 |         0.915000 |
| next_day  | QQQ      | rmse     | garch_1_1                | expanding_mean_abs_return |              0.000701 |  -0.002928 |   0.004995 |         0.383000 |
| next_day  | QQQ      | rmse     | garch_1_1                | har_daily_weekly_monthly  |              0.021273 |   0.009850 |   0.036452 |         0.000000 |
| next_day  | QQQ      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.020572 |  -0.036968 |  -0.008029 |         1.000000 |
| next_day  | QQQ      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.017407 |  -0.030009 |  -0.007220 |         1.000000 |
| next_day  | QQQ      | rmse     | hist_gradient_boosting   | garch_1_1                 |             -0.018107 |  -0.029824 |  -0.008412 |         1.000000 |
| next_day  | QQQ      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.003165 |  -0.002196 |   0.008819 |         0.169000 |
| next_day  | SPY      | mae      | garch_1_1                | expanding_mean_abs_return |              0.004504 |   0.002125 |   0.007477 |         0.000000 |
| next_day  | SPY      | mae      | garch_1_1                | har_daily_weekly_monthly  |              0.010752 |   0.005469 |   0.018042 |         0.000000 |
| next_day  | SPY      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.006248 |  -0.012472 |  -0.001563 |         0.998000 |
| next_day  | SPY      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.007891 |  -0.012447 |  -0.004610 |         1.000000 |
| next_day  | SPY      | mae      | hist_gradient_boosting   | garch_1_1                 |             -0.012395 |  -0.018177 |  -0.008162 |         1.000000 |
| next_day  | SPY      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.001643 |  -0.003687 |   0.001209 |         0.904000 |
| next_day  | SPY      | rmse     | garch_1_1                | expanding_mean_abs_return |              0.002515 |   0.000575 |   0.004769 |         0.010000 |
| next_day  | SPY      | rmse     | garch_1_1                | har_daily_weekly_monthly  |              0.026340 |   0.008885 |   0.048156 |         0.000000 |
| next_day  | SPY      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.023825 |  -0.046066 |  -0.005293 |         1.000000 |
| next_day  | SPY      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.018568 |  -0.030059 |  -0.006879 |         1.000000 |
| next_day  | SPY      | rmse     | hist_gradient_boosting   | garch_1_1                 |             -0.021083 |  -0.033816 |  -0.010312 |         1.000000 |
| next_day  | SPY      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.005257 |  -0.003186 |   0.015534 |         0.291000 |
| next_day  | TLT      | mae      | garch_1_1                | expanding_mean_abs_return |              0.007263 |   0.004179 |   0.010874 |         0.000000 |
| next_day  | TLT      | mae      | garch_1_1                | har_daily_weekly_monthly  |              0.009159 |   0.005599 |   0.012722 |         0.000000 |
| next_day  | TLT      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.001896 |  -0.004680 |   0.000286 |         0.945000 |
| next_day  | TLT      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.002524 |  -0.004449 |  -0.000821 |         1.000000 |
| next_day  | TLT      | mae      | hist_gradient_boosting   | garch_1_1                 |             -0.009787 |  -0.013051 |  -0.007056 |         1.000000 |
| next_day  | TLT      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000628 |  -0.001754 |   0.000392 |         0.886000 |
| next_day  | TLT      | rmse     | garch_1_1                | expanding_mean_abs_return |              0.002184 |  -0.001076 |   0.006471 |         0.091000 |
| next_day  | TLT      | rmse     | garch_1_1                | har_daily_weekly_monthly  |              0.010983 |   0.004227 |   0.019149 |         0.000000 |
| next_day  | TLT      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.008799 |  -0.018492 |  -0.001443 |         1.000000 |
| next_day  | TLT      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.007134 |  -0.014120 |  -0.002056 |         1.000000 |
| next_day  | TLT      | rmse     | hist_gradient_boosting   | garch_1_1                 |             -0.009318 |  -0.014418 |  -0.004769 |         1.000000 |
| next_day  | TLT      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.001664 |  -0.001159 |   0.004968 |         0.199000 |
| next_week | GLD      | mae      | garch_1_1                | expanding_mean_abs_return |             -0.003515 |  -0.007984 |   0.001041 |         0.915000 |
| next_week | GLD      | mae      | garch_1_1                | har_daily_weekly_monthly  |              0.006670 |   0.002618 |   0.011663 |         0.000000 |
| next_week | GLD      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.010185 |  -0.017728 |  -0.003826 |         0.999000 |
| next_week | GLD      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.010282 |  -0.016808 |  -0.004393 |         1.000000 |
| next_week | GLD      | mae      | hist_gradient_boosting   | garch_1_1                 |             -0.006767 |  -0.011797 |  -0.002815 |         1.000000 |
| next_week | GLD      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000097 |  -0.001748 |   0.001573 |         0.555000 |
| next_week | GLD      | rmse     | garch_1_1                | expanding_mean_abs_return |             -0.010563 |  -0.017695 |  -0.003082 |         0.999000 |
| next_week | GLD      | rmse     | garch_1_1                | har_daily_weekly_monthly  |              0.010984 |   0.004792 |   0.017838 |         0.000000 |
| next_week | GLD      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.021547 |  -0.032036 |  -0.011546 |         1.000000 |
| next_week | GLD      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.023122 |  -0.032335 |  -0.012838 |         1.000000 |
| next_week | GLD      | rmse     | hist_gradient_boosting   | garch_1_1                 |             -0.012559 |  -0.019161 |  -0.005601 |         1.000000 |
| next_week | GLD      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.001575 |  -0.004242 |   0.001573 |         0.850000 |
| next_week | IWM      | mae      | garch_1_1                | expanding_mean_abs_return |              0.003383 |  -0.002129 |   0.008833 |         0.104000 |
| next_week | IWM      | mae      | garch_1_1                | har_daily_weekly_monthly  |              0.021417 |   0.010110 |   0.035833 |         0.000000 |
| next_week | IWM      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.018034 |  -0.030874 |  -0.007254 |         1.000000 |
| next_week | IWM      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.018630 |  -0.028719 |  -0.010437 |         1.000000 |
| next_week | IWM      | mae      | hist_gradient_boosting   | garch_1_1                 |             -0.022013 |  -0.032948 |  -0.012443 |         1.000000 |
| next_week | IWM      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000596 |  -0.004572 |   0.004156 |         0.642000 |
| next_week | IWM      | rmse     | garch_1_1                | expanding_mean_abs_return |              0.002450 |  -0.003525 |   0.007128 |         0.206000 |
| next_week | IWM      | rmse     | garch_1_1                | har_daily_weekly_monthly  |              0.044347 |   0.015243 |   0.074942 |         0.000000 |
| next_week | IWM      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.041896 |  -0.069254 |  -0.016542 |         1.000000 |
| next_week | IWM      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.037406 |  -0.055389 |  -0.019473 |         1.000000 |
| next_week | IWM      | rmse     | hist_gradient_boosting   | garch_1_1                 |             -0.039856 |  -0.059371 |  -0.017310 |         1.000000 |
| next_week | IWM      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.004491 |  -0.004479 |   0.013622 |         0.255000 |
| next_week | QQQ      | mae      | garch_1_1                | expanding_mean_abs_return |             -0.001287 |  -0.007092 |   0.003914 |         0.710000 |
| next_week | QQQ      | mae      | garch_1_1                | har_daily_weekly_monthly  |              0.025105 |   0.016791 |   0.036999 |         0.000000 |
| next_week | QQQ      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.026392 |  -0.039324 |  -0.015926 |         1.000000 |
| next_week | QQQ      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.025252 |  -0.034885 |  -0.017209 |         1.000000 |
| next_week | QQQ      | mae      | hist_gradient_boosting   | garch_1_1                 |             -0.023964 |  -0.030668 |  -0.017570 |         1.000000 |
| next_week | QQQ      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.001140 |  -0.002549 |   0.005989 |         0.319000 |
| next_week | QQQ      | rmse     | garch_1_1                | expanding_mean_abs_return |             -0.006977 |  -0.011560 |  -0.002865 |         0.999000 |
| next_week | QQQ      | rmse     | garch_1_1                | har_daily_weekly_monthly  |              0.040976 |   0.022890 |   0.061149 |         0.000000 |
| next_week | QQQ      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.047953 |  -0.069433 |  -0.028586 |         1.000000 |
| next_week | QQQ      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.038901 |  -0.050771 |  -0.027267 |         1.000000 |
| next_week | QQQ      | rmse     | hist_gradient_boosting   | garch_1_1                 |             -0.031924 |  -0.041001 |  -0.022822 |         1.000000 |
| next_week | QQQ      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.009052 |  -0.001756 |   0.021001 |         0.079000 |
| next_week | SPY      | mae      | garch_1_1                | expanding_mean_abs_return |              0.002856 |  -0.000871 |   0.006604 |         0.067000 |
| next_week | SPY      | mae      | garch_1_1                | har_daily_weekly_monthly  |              0.019683 |   0.010030 |   0.033533 |         0.000000 |
| next_week | SPY      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.016827 |  -0.028725 |  -0.007548 |         1.000000 |
| next_week | SPY      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.019266 |  -0.027743 |  -0.011787 |         1.000000 |
| next_week | SPY      | mae      | hist_gradient_boosting   | garch_1_1                 |             -0.022122 |  -0.030704 |  -0.015413 |         1.000000 |
| next_week | SPY      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.002440 |  -0.006073 |   0.002996 |         0.855000 |
| next_week | SPY      | rmse     | garch_1_1                | expanding_mean_abs_return |             -0.000268 |  -0.003049 |   0.002350 |         0.567000 |
| next_week | SPY      | rmse     | garch_1_1                | har_daily_weekly_monthly  |              0.041620 |   0.015127 |   0.074406 |         0.000000 |
| next_week | SPY      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.041888 |  -0.068366 |  -0.015750 |         1.000000 |
| next_week | SPY      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.034071 |  -0.047446 |  -0.019002 |         1.000000 |
| next_week | SPY      | rmse     | hist_gradient_boosting   | garch_1_1                 |             -0.033803 |  -0.047160 |  -0.021034 |         1.000000 |
| next_week | SPY      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.007817 |  -0.006762 |   0.023480 |         0.257000 |
| next_week | TLT      | mae      | garch_1_1                | expanding_mean_abs_return |             -0.001290 |  -0.005978 |   0.003906 |         0.682000 |
| next_week | TLT      | mae      | garch_1_1                | har_daily_weekly_monthly  |              0.007468 |   0.003673 |   0.011431 |         0.000000 |
| next_week | TLT      | mae      | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.008758 |  -0.014128 |  -0.004153 |         1.000000 |
| next_week | TLT      | mae      | hist_gradient_boosting   | expanding_mean_abs_return |             -0.009181 |  -0.013398 |  -0.005076 |         1.000000 |
| next_week | TLT      | mae      | hist_gradient_boosting   | garch_1_1                 |             -0.007891 |  -0.011906 |  -0.004577 |         1.000000 |
| next_week | TLT      | mae      | hist_gradient_boosting   | har_daily_weekly_monthly  |             -0.000423 |  -0.002743 |   0.001341 |         0.654000 |
| next_week | TLT      | rmse     | garch_1_1                | expanding_mean_abs_return |             -0.005406 |  -0.009155 |  -0.000992 |         0.994000 |
| next_week | TLT      | rmse     | garch_1_1                | har_daily_weekly_monthly  |              0.011682 |   0.003155 |   0.020034 |         0.003000 |
| next_week | TLT      | rmse     | har_daily_weekly_monthly | expanding_mean_abs_return |             -0.017088 |  -0.027336 |  -0.007478 |         1.000000 |
| next_week | TLT      | rmse     | hist_gradient_boosting   | expanding_mean_abs_return |             -0.016873 |  -0.024045 |  -0.009890 |         1.000000 |
| next_week | TLT      | rmse     | hist_gradient_boosting   | garch_1_1                 |             -0.011467 |  -0.018348 |  -0.005165 |         1.000000 |
| next_week | TLT      | rmse     | hist_gradient_boosting   | har_daily_weekly_monthly  |              0.000215 |  -0.004132 |   0.003190 |         0.438000 |

## Interpretation

`share_negative` is the share of bootstrap resamples where `model_a` has lower error than `model_b`. Intervals crossing zero should be treated as weak or mixed evidence. Even intervals mostly on one side of zero remain conditional method-comparison evidence for the named horizon, ticker, metric, and validation design only.