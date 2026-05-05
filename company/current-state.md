# Current State

## Capsule

- Objective: Build the reproducible foundation for Volatility Forecasting Lab.
- Latest status: VFL-005 added separate next-day and next-week baseline reports with horizon-aware target labeling.
- Operating mode: build.
- Current milestone: Milestone 1 - data pipeline, realized-volatility targets, baseline forecasts, validation protocol, honest evaluation report.
- Canonical workspace/repo: `/Users/melihkarakose/Projects/Active/volatility-forecasting-lab`
- Current canonical artifact/output: `artifacts/reports/baseline_next_day_report.md`; `artifacts/reports/baseline_next_week_report.md`.
- Current active workflow: `uv sync`, `uv run pytest`, `uv run ruff check .`, `uv run python scripts/fetch_data.py`, `uv run python scripts/run_baseline_evaluation.py`.
- Known caveats: local repo only; no public GitHub push until baseline report and README are clean.
- Next action: User decision for `VFL-004` public GitHub push, or continue locally with `VFL-006` stronger econometric baseline.
- Blockers: none.

## Capability Surface

- Available: filesystem, shell, local git, Python/uv if installed, network access for public no-key market data.
- Required now: local package install, tests, lint, yfinance data fetch, baseline evaluation.
- Missing / uncertain: no GitHub remote yet by design; exact future ML model set intentionally deferred.
- Risk boundary: confirmation needed before public push, release tags, credentials, paid data, or any strategic change toward trading/allocation.
- Approval lane: autonomous for local repo setup, local tests, free project dependencies, public-data fetches, and local git commits; confirmation needed for public GitHub publication.
- Verification path: completed `uv run pytest`, `uv run ruff check .`, `uv run python scripts/fetch_data.py`, `uv run python scripts/run_baseline_evaluation.py`, manifest inspection, generated next-day and next-week report inspection, target/leakage review, and public-readiness review.
