# Current State

## Capsule

- Objective: Build the reproducible foundation for Volatility Forecasting Lab.
- Latest status: VFL-008 added a leakage-safe ML feature matrix and documented the feature contract.
- Operating mode: build.
- Current milestone: Milestone 2 planning - first leakage-safe ML forecasting comparison.
- Canonical workspace/repo: `/Users/melihkarakose/Projects/Active/volatility-forecasting-lab`; `https://github.com/moleh1307/volatility-forecasting-lab`
- Current canonical artifact/output: `artifacts/reports/baseline_next_day_report.md`; `artifacts/reports/baseline_next_week_report.md`.
- Current active workflow: `uv sync`, `uv run pytest`, `uv run ruff check .`, `uv run python scripts/fetch_data.py`, `uv run python scripts/run_baseline_evaluation.py`.
- Known caveats: no release tag has been created; future ML model set intentionally deferred.
- Next action: Execute `VFL-009 - Add First Scikit-Learn ML Baseline`.
- Blockers: none.

## Capability Surface

- Available: filesystem, shell, local git, Python/uv if installed, network access for public no-key market data.
- Required now: local package install, tests, lint, yfinance data fetch, baseline evaluation.
- Missing / uncertain: exact first ML estimator choice is deferred to `VFL-009`.
- Risk boundary: confirmation needed before release tags, credentials, paid data, or any strategic change toward trading/allocation.
- Approval lane: autonomous for local repo setup, local tests, free project dependencies, public-data fetches, local git commits, approved public repo push, and approved MIT license addition; confirmation needed for release tags.
- Verification path: completed `uv run pytest`, `uv run ruff check .`, `uv run python scripts/fetch_data.py`, `uv run python scripts/run_baseline_evaluation.py`, manifest inspection, generated next-day and next-week report inspection, target/leakage review, public-readiness review, HAR label-availability test, GitHub repo creation check, and remote `main` verification.
