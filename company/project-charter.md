# Project Charter: Volatility Forecasting Lab

## Purpose

Build a serious, reproducible quantitative research repo that compares econometric volatility forecasting baselines with later ML models using free public market data.

## Audience

- Primary: GitHub / quant credibility and job applications.
- Secondary: personal research depth.

## Milestone 1

Create a conservative forecasting-methodology foundation:

- public-data pipeline with cached raw data and source manifests;
- realized-volatility target construction;
- baseline forecasts;
- validation protocol;
- honest evaluation report.

Milestone 1 explicitly does not include ML unless the baseline structure is already solid.

## Scope Boundaries

- Free/no-key public data only for v0.
- Use `yfinance`, cached raw data, source manifests, and clear data caveats.
- Research methodology only.
- No trading system.
- No allocation strategy.
- No performance claims.
- No claim that ML beats econometrics unless a later validation protocol supports it.

## V0 Market Panel

- SPY
- QQQ
- IWM
- GLD
- TLT

BTC-USD is intentionally excluded from v0 to avoid mixing market microstructure and regime differences too early.

## Forecast Targets

- Primary: next-day realized volatility.
- Designed extension: next-week realized volatility.

If both targets slow milestone 1, implement next-day first while keeping the target pipeline horizon-aware.

## Stack

- Python with `uv`
- `pandas`, `numpy`
- `scikit-learn`
- `statsmodels` and/or `arch` if stable and useful
- CLI scripts, tests, docs, cached data ignored by git

## Project-Shape Inference

- Project shape: reproducible public quant research repo for volatility forecasting methodology.
- What makes success hard: volatility target definitions, horizon alignment, leakage avoidance, fair baselines, time-series validation, and restrained public claims.
- Main failure modes: lookahead bias, comparing models on inconsistent targets, data-quality caveats hidden in code, overclaimed model performance, and adding ML before baselines are trustworthy.
- Evidence/artifacts that matter: source manifests, target-definition docs, validation protocol, reproducible CLI commands, tests, generated evaluation tables, and report caveats.
- Roles/disciplines needed: Founder/Chief of Staff, Quant Researcher, Data Engineer, Research Engineer, Replication QA.
- Initial operating mode: build.
- Confidence lanes needed: methodology choices are working assumptions until tested; forecast results require verified/reviewed lanes before public wording.
- Verification/adversarial gates: target alignment tests, no-leakage review, source manifest inspection, baseline evaluation smoke tests, and report claim-boundary review before GitHub push.
- What should not be overbuilt: no trading layer, no allocation/backtest layer, no dashboard, no deep ML framework, and no broad asset universe before v0 is credible.

## Related Projects

- Similar operating style reference: [[macro-regime-portfolio-lab]]
- This project is standalone and should not become an allocation or trading project.
