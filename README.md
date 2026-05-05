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
| Baselines | Lagged absolute return and expanding mean absolute return |
| ML models | Deferred until baseline methodology is solid |
| GitHub publication | Local-first; public push deferred |

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
- Target definitions: [`docs/target-definitions.md`](docs/target-definitions.md)
- Validation protocol: [`docs/validation-protocol.md`](docs/validation-protocol.md)
- Target/leakage review: [`docs/target-leakage-review.md`](docs/target-leakage-review.md)
- Documentation index: [`docs/index.md`](docs/index.md)

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

The current reports compare forecast errors for simple baselines within a fixed horizon, target definition, ticker, and validation slice. Lower error is better for that diagnostic only. It does not imply a useful trading signal, model superiority, alpha, or investment performance.
