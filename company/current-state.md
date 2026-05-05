# Current State

## Capsule

- Objective: Build the reproducible foundation for Volatility Forecasting Lab.
- Latest status: Milestone 3 evidence reviewed and public summary added.
- Operating mode: build.
- Current milestone: Milestone 3 - robustness and uncertainty diagnostics.
- Canonical workspace/repo: `/Users/melihkarakose/Projects/Active/volatility-forecasting-lab`; `https://github.com/moleh1307/volatility-forecasting-lab`
- Current canonical artifact/output: `docs/milestone-3-summary.md`; `docs/robustness-uncertainty-protocol.md`; `artifacts/reports/rolling_window_model_ranking.md`; `artifacts/reports/bootstrap_error_differences.md`; `artifacts/reports/baseline_next_day_report.md`; `artifacts/reports/baseline_next_week_report.md`; `artifacts/reports/subperiod_model_comparison.md`.
- Current active workflow: `uv sync`, `uv run pytest`, `uv run ruff check .`, `uv run python scripts/fetch_data.py`, `uv run python scripts/run_baseline_evaluation.py`.
- Known caveats: Milestone 3 supports robustness diagnostics and mixed conditional evidence; no trading/allocation/economic-value or broad model-superiority claim is supported.
- Next action: Execute `VFL-019 - Milestone 3 release readiness check`.
- Blockers: none.

## Capability Surface

- Available: filesystem, shell, local git, Python/uv if installed, network access for public no-key market data.
- Required now: local package install, tests, lint, yfinance data fetch, baseline evaluation.
- Missing / uncertain: Milestone 3 release readiness has not been checked; no `v0.3.0-milestone-3` tag has been approved or created.
- Risk boundary: confirmation needed before future release tags, credentials, paid data, or any strategic change toward trading/allocation.
- Approval lane: autonomous for local repo setup, local tests, free project dependencies, public-data fetches, local git commits, approved public repo push, approved MIT license addition, and approved `v0.2.0-milestone-2` tag creation.
- Verification path: completed `uv run pytest`, `uv run ruff check .`, `uv run python scripts/fetch_data.py`, `uv run python scripts/run_baseline_evaluation.py`, manifest inspection, generated next-day and next-week report inspection, generated rolling-window ranking report inspection, generated bootstrap error-difference report inspection, target/leakage review, public-readiness review, HAR label-availability test, GitHub repo creation check, and remote `main` verification.
