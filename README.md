# Volatility Forecasting Lab

Reproducible volatility-forecasting research lab using free public market data.

The project starts conservatively: build trustworthy data, target, baseline, and validation machinery before adding ML models.

## Current Status

| Area | Status |
| --- | --- |
| Data pipeline | V0 `yfinance` adjusted-close cache and source manifest |
| Market panel | SPY, QQQ, IWM, GLD, TLT |
| Targets | Next-day and next-week realized volatility |
| Validation | Time-ordered validation slice from 2020-01-01 |
| Baselines | Lagged absolute return, expanding mean absolute return, HAR-style statistical baseline |
| ML models | First modest scikit-learn baseline added |
| GitHub publication | Public repository on GitHub |
| License | MIT |

## Scope

- V0 panel: SPY, QQQ, IWM, GLD, TLT
- Data: free/no-key public market data via `yfinance`
- Initial targets: next-day and next-week realized volatility
- Milestone 1: data pipeline, target construction, baseline forecasts, validation protocol, honest evaluation report

## Non-Goals

- No trading system
- No allocation strategy
- No live execution
- No investment recommendation
- No performance claims
- No claim that ML beats econometric baselines

## Quickstart

```bash
uv sync
uv run pytest
uv run ruff check .
uv run python scripts/fetch_data.py
uv run python scripts/run_baseline_evaluation.py
```

Generated data caches live under `data/` and are ignored by git. Generated reports live under `artifacts/reports/`.

## Outputs And Docs

- Next-day baseline report: [`artifacts/reports/baseline_next_day_report.md`](artifacts/reports/baseline_next_day_report.md)
- Next-week baseline report: [`artifacts/reports/baseline_next_week_report.md`](artifacts/reports/baseline_next_week_report.md)
- Rolling-window ranking report: [`artifacts/reports/rolling_window_model_ranking.md`](artifacts/reports/rolling_window_model_ranking.md)
- Block-bootstrap error-difference report: [`artifacts/reports/bootstrap_error_differences.md`](artifacts/reports/bootstrap_error_differences.md)
- Target definitions: [`docs/target-definitions.md`](docs/target-definitions.md)
- Validation protocol: [`docs/validation-protocol.md`](docs/validation-protocol.md)
- Target/leakage review: [`docs/target-leakage-review.md`](docs/target-leakage-review.md)
- Documentation index: [`docs/index.md`](docs/index.md)
- Milestone 2 plan: [`docs/milestone-2-plan.md`](docs/milestone-2-plan.md)
- Milestone 2 summary: [`docs/milestone-2-summary.md`](docs/milestone-2-summary.md)
- Milestone 2 release readiness: [`docs/milestone-2-release-readiness.md`](docs/milestone-2-release-readiness.md)
- Milestone 3 plan: [`docs/milestone-3-plan.md`](docs/milestone-3-plan.md)
- Milestone 3 summary: [`docs/milestone-3-summary.md`](docs/milestone-3-summary.md)
- Milestone 3 release readiness: [`docs/milestone-3-release-readiness.md`](docs/milestone-3-release-readiness.md)
- Robustness and uncertainty protocol: [`docs/robustness-uncertainty-protocol.md`](docs/robustness-uncertainty-protocol.md)
- ML comparison review: [`docs/ml-comparison-review.md`](docs/ml-comparison-review.md)
- Subperiod stability review: [`docs/subperiod-stability-review.md`](docs/subperiod-stability-review.md)

## Repository Layout

```text
configs/        Project configuration
data/           Local data cache and tracked source manifest
docs/           Methodology and review notes
scripts/        Reproducible CLI entry points
src/            Python package code
tests/          Target/evaluation tests
artifacts/      Generated research reports
company/        JarvisOS project state and work orders
```

## Interpretation Boundary

The current reports compare forecast errors for baseline methods within a fixed horizon, target definition, ticker, and validation slice. Lower error is better for that diagnostic only. It does not imply a useful trading signal, model superiority, alpha, or investment performance.

The first ML baseline is included for diagnostic comparison. Current results should be read as mixed forecast-error evidence, not as proof that ML is superior to econometric/statistical baselines.

Milestone 2 summary: the repo now includes a first leakage-safe ML baseline. Results provide useful diagnostic contrast against statistical baselines, but the evidence is mixed across metrics and horizons.

Milestone 3 adds robustness diagnostics. The rolling-window ranking report shows time variation in best-model rankings, and the block-bootstrap report adds pairwise forecast-error uncertainty intervals. These diagnostics support a more careful comparison, not a broad winner claim.

## License

MIT License. See [`LICENSE`](LICENSE).
