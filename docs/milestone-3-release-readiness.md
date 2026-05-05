# Milestone 3 Release Readiness

## Scope

This check reviews whether Milestone 3 is ready for a public release/tag decision.
It does not create a release tag.

Candidate tag:

```text
v0.3.0-milestone-3
```

## Release Surface

Milestone 3 adds robustness and uncertainty diagnostics around the existing
forecasting baselines:

- `docs/robustness-uncertainty-protocol.md`
- `docs/milestone-3-summary.md`
- `artifacts/reports/rolling_window_model_ranking.md`
- `artifacts/reports/bootstrap_error_differences.md`

The diagnostics are reproducible with:

```bash
uv run python scripts/run_baseline_evaluation.py
```

## Verification

Completed checks:

- `uv run pytest`: passed, 15 tests.
- `uv run ruff check .`: passed.
- `uv run python scripts/run_baseline_evaluation.py`: passed.
- Required Milestone 3 files exist and are non-empty.
- Claim-boundary scan found only negative/boundary statements.
- Local `main` matches `origin/main` at `a5e1098` before this readiness note.
- GitHub repository is public: `https://github.com/moleh1307/volatility-forecasting-lab`.
- GitHub default branch is `main`.
- GitHub license is recognized as MIT.
- Existing release tag: `v0.2.0-milestone-2`.
- No `v0.3.0-milestone-3` tag exists yet.

## Evidence Summary

Milestone 3 is release-ready as a methodology milestone.

Supported release framing:

- The repo now includes rolling-window ranking diagnostics.
- The repo now includes block-bootstrap pairwise error-difference diagnostics.
- Model-comparison evidence is more robustly documented than in Milestone 2.
- Evidence remains mixed and conditional, especially for ML versus HAR.

Unsupported release framing:

- No trading system, allocation strategy, alpha, investment, or economic-value
  claim is supported.
- No broad claim that ML beats HAR is supported.
- No claim that any model is universally best is supported.

## Decision Needed

Choose one:

1. Create annotated tag `v0.3.0-milestone-3`.
2. Continue locally without a release tag.
3. Pause after Milestone 3 readiness.

Do not create the tag without explicit approval.
