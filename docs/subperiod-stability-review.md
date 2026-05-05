# Subperiod Stability Review

## Scope

Review calendar-year subperiod behavior after adding the first ML baseline.

## Result

Status: reviewed diagnostic stability check.

The subperiod view strengthens the case that the ML baseline is useful as a comparison row, but it still does not justify robust model-superiority language.

## Evidence

Generated report:

- `artifacts/reports/subperiod_model_comparison.md`

Full-slice ML versus HAR counts:

- Next-day MAE: ML lower than HAR for 5 of 5 tickers.
- Next-day RMSE: ML lower than HAR for 1 of 5 tickers.
- Next-week MAE: ML lower than HAR for 4 of 5 tickers.
- Next-week RMSE: ML lower than HAR for 1 of 5 tickers.

Calendar-year best-model counts show the ML baseline often ranks first in subperiod/ticker cells, but the ranking is not uniform across horizons, metrics, or baseline types.

## Interpretation

The current Milestone 2 evidence is coherent as a forecasting-methodology comparison:

- ML provides useful nonlinear diagnostic contrast.
- HAR remains a strong transparent benchmark.
- MAE and RMSE tell different stories.
- Subperiod behavior is not stable enough for broad claims.

## Claim Boundary

Acceptable:

- "The first ML baseline is useful for diagnostic comparison."
- "Subperiod results are mixed across metrics and horizons."
- "More validation is needed before stronger model claims."

Avoid:

- ML outperforms.
- ML is superior.
- Robust ML advantage.
- Any trading, allocation, alpha, signal, or investment interpretation.
