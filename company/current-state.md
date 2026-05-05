# Current State

## Capsule

- Objective: Build the reproducible foundation for Volatility Forecasting Lab.
- Latest status: Milestone 3 started with a robustness and uncertainty diagnostics plan.
- Operating mode: build.
- Current milestone: Milestone 3 - robustness and uncertainty diagnostics.
- Canonical workspace/repo: `/Users/melihkarakose/Projects/Active/volatility-forecasting-lab`; `https://github.com/moleh1307/volatility-forecasting-lab`
- Current canonical artifact/output: `artifacts/reports/baseline_next_day_report.md`; `artifacts/reports/baseline_next_week_report.md`; `artifacts/reports/subperiod_model_comparison.md`.
- Current active workflow: `uv sync`, `uv run pytest`, `uv run ruff check .`, `uv run python scripts/fetch_data.py`, `uv run python scripts/run_baseline_evaluation.py`.
- Known caveats: Milestone 2 evidence remains diagnostic and mixed; no new model family should be added before robustness diagnostics.
- Next action: Execute `VFL-015 - Design Robustness And Uncertainty Protocol`.
- Blockers: none.

## Capability Surface

- Available: filesystem, shell, local git, Python/uv if installed, network access for public no-key market data.
- Required now: local package install, tests, lint, yfinance data fetch, baseline evaluation.
- Missing / uncertain: exact block-bootstrap and rolling-window settings need protocol definition.
- Risk boundary: confirmation needed before future release tags, credentials, paid data, or any strategic change toward trading/allocation.
- Approval lane: autonomous for local repo setup, local tests, free project dependencies, public-data fetches, local git commits, approved public repo push, approved MIT license addition, and approved `v0.2.0-milestone-2` tag creation.
- Verification path: completed `uv run pytest`, `uv run ruff check .`, `uv run python scripts/fetch_data.py`, `uv run python scripts/run_baseline_evaluation.py`, manifest inspection, generated next-day and next-week report inspection, target/leakage review, public-readiness review, HAR label-availability test, GitHub repo creation check, and remote `main` verification.
