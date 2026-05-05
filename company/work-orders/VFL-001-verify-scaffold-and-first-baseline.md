# VFL-001 - Verify Scaffold And First Baseline

## Status

Done

## Objective

Verify the local scaffold and run the first public-data baseline workflow for milestone 1.

## Scope

- Install/sync the local Python environment.
- Run tests and lint.
- Fetch v0 yfinance market data.
- Build next-day realized-volatility targets.
- Generate simple baseline forecasts and an honest evaluation report.

## Acceptance Criteria

- `uv run pytest` passes.
- `uv run ruff check .` passes, or any lint failures are fixed or explicitly recorded.
- Raw data cache and source manifest are generated locally and ignored by git.
- Baseline evaluation report exists under `artifacts/reports/`.
- Report wording avoids trading, allocation, and performance claims.

## Capability Surface

- Available: filesystem, shell, local git, Python/uv, network access for no-key public data.
- Required: package sync, test runner, linter, yfinance fetch.
- Approval lane: autonomous.
- Verification path: tests, lint, generated manifest/report inspection.

## Claim Boundary

This work may produce baseline error metrics. It must not claim model superiority, investment usefulness, alpha, or trading performance.

## Closeout Evidence

- `uv sync` completed.
- `uv run pytest` passed 4 tests.
- `uv run ruff check .` passed.
- `uv run python scripts/fetch_data.py` fetched 4,108 rows for 5 tickers from 2010-01-04 to 2026-05-04.
- `uv run python scripts/run_baseline_evaluation.py` wrote 10 metric rows and `artifacts/reports/baseline_next_day_report.md`.
- `data/raw/manifest.yml` records yfinance source caveats and cache bounds.
