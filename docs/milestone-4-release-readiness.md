# Milestone 4 Release Readiness

## Scope

This check reviews whether Milestone 4 is ready for a public release/tag decision.
It does not create a release tag.

Candidate tag:

```text
v0.4.0-milestone-4
```

## Release Surface

Milestone 4 adds a GARCH(1,1) econometric volatility baseline and updates the
existing evaluation reports and robustness diagnostics.

Primary files:

- `docs/milestone-4-plan.md`
- `docs/milestone-4-comparison-review.md`
- `artifacts/reports/baseline_next_day_report.md`
- `artifacts/reports/baseline_next_week_report.md`
- `artifacts/reports/subperiod_model_comparison.md`
- `artifacts/reports/rolling_window_model_ranking.md`
- `artifacts/reports/bootstrap_error_differences.md`

The diagnostics are reproducible with:

```bash
uv run python scripts/run_baseline_evaluation.py
```

## Verification

Completed checks:

- `uv run pytest`: passed, 17 tests.
- `uv run ruff check .`: passed.
- `uv run python scripts/run_baseline_evaluation.py`: passed in about 54 seconds.
- Required Milestone 4 files exist and are non-empty.
- Claim-boundary scan found only negative/boundary statements.
- Local `main` matches `origin/main` at `492c1bc` before this readiness note.
- GitHub repository is public: `https://github.com/moleh1307/volatility-forecasting-lab`.
- GitHub default branch is `main`.
- GitHub license is recognized as MIT.
- Existing release tag: `v0.2.0-milestone-2`.
- No `v0.4.0-milestone-4` tag exists yet.

## Evidence Summary

Milestone 4 is release-ready as a methodology milestone.

Supported release framing:

- The repo now compares simple baselines, HAR, GARCH(1,1), and the first ML
  baseline under one validation protocol.
- GARCH adds a useful econometric reference point.
- Current GARCH results do not dominate HAR or ML.
- HAR remains the stronger transparent econometric benchmark in this
  implementation.

Unsupported release framing:

- No trading system, allocation strategy, alpha, investment, or economic-value
  claim is supported.
- No broad claim that ML beats econometric baselines is supported.
- No claim that GARCH, HAR, or ML is universally best is supported.

## Decision Needed

Choose one:

1. Create annotated tag `v0.4.0-milestone-4`.
2. Continue locally without a release tag.
3. Pause after Milestone 4 readiness.

Do not create the tag without explicit approval.
