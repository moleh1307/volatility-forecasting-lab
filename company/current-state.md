# Current State

## Capsule

- Objective: Build the reproducible foundation for Volatility Forecasting Lab.
- Latest status: Rolling-window ranking diagnostics and block-bootstrap error-difference diagnostics are implemented and generated.
- Operating mode: build.
- Current milestone: Milestone 3 - robustness and uncertainty diagnostics.
- Canonical workspace/repo: `/Users/melihkarakose/Projects/Active/volatility-forecasting-lab`; `https://github.com/moleh1307/volatility-forecasting-lab`
- Current canonical artifact/output: `docs/robustness-uncertainty-protocol.md`; `artifacts/reports/rolling_window_model_ranking.md`; `artifacts/reports/bootstrap_error_differences.md`; `artifacts/reports/baseline_next_day_report.md`; `artifacts/reports/baseline_next_week_report.md`; `artifacts/reports/subperiod_model_comparison.md`.
- Current active workflow: `uv sync`, `uv run pytest`, `uv run ruff check .`, `uv run python scripts/fetch_data.py`, `uv run python scripts/run_baseline_evaluation.py`.
- Known caveats: Bootstrap intervals are conditional forecast-error uncertainty diagnostics, not trading/allocation/economic-value evidence.
- Next action: Execute `VFL-018 - Review Milestone 3 evidence and update public summary`.
- Blockers: none.

## Capability Surface

- Available: filesystem, shell, local git, Python/uv if installed, network access for public no-key market data.
- Required now: local package install, tests, lint, yfinance data fetch, baseline evaluation.
- Missing / uncertain: Milestone 3 evidence still needs a public summary and claim-boundary review.
- Risk boundary: confirmation needed before future release tags, credentials, paid data, or any strategic change toward trading/allocation.
- Approval lane: autonomous for local repo setup, local tests, free project dependencies, public-data fetches, local git commits, approved public repo push, approved MIT license addition, and approved `v0.2.0-milestone-2` tag creation.
- Verification path: completed `uv run pytest`, `uv run ruff check .`, `uv run python scripts/fetch_data.py`, `uv run python scripts/run_baseline_evaluation.py`, manifest inspection, generated next-day and next-week report inspection, generated rolling-window ranking report inspection, generated bootstrap error-difference report inspection, target/leakage review, public-readiness review, HAR label-availability test, GitHub repo creation check, and remote `main` verification.
