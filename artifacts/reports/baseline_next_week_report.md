# Baseline Next-Week Volatility Forecast Evaluation

Validation slice starts at `2020-01-01`.
Target horizon: `5` trading day(s).

This report compares simple baseline forecasts for overlapping five-trading-day annualized realized volatility. It is a methodology scaffold, not an investment or trading result.

Lower MAE/RMSE indicates lower forecast error within this target, date range, and ticker only. The table should not be read across horizons or as a trading performance result.

| model                     | ticker   |   observations |      mae |     rmse |      bias |
|:--------------------------|:---------|---------------:|---------:|---------:|----------:|
| expanding_mean_abs_return | GLD      |           1587 | 0.062747 | 0.101638 | -0.043926 |
| lagged_abs_return         | GLD      |           1587 | 0.098596 | 0.134628 | -0.028118 |
| expanding_mean_abs_return | IWM      |           1587 | 0.091797 | 0.155570 | -0.071149 |
| lagged_abs_return         | IWM      |           1587 | 0.135904 | 0.183389 | -0.036457 |
| expanding_mean_abs_return | QQQ      |           1587 | 0.094857 | 0.154155 | -0.072735 |
| lagged_abs_return         | QQQ      |           1587 | 0.127918 | 0.175167 | -0.036121 |
| expanding_mean_abs_return | SPY      |           1587 | 0.073870 | 0.136468 | -0.048418 |
| lagged_abs_return         | SPY      |           1587 | 0.097251 | 0.142255 | -0.026976 |
| expanding_mean_abs_return | TLT      |           1587 | 0.054997 | 0.087918 | -0.035813 |
| lagged_abs_return         | TLT      |           1587 | 0.083489 | 0.110198 | -0.021557 |

## Caveats

- yfinance data is a free public-data source and can be revised.
- Baselines are intentionally simple and are not tuned for performance claims.
- Metrics describe forecast errors only; they are not trading, allocation, or alpha metrics.