from pathlib import Path

import pandas as pd

from volatility_forecasting_lab.config import load_config
from volatility_forecasting_lab.data import load_adjusted_prices
from volatility_forecasting_lab.evaluation import (
    block_bootstrap_error_differences,
    evaluate_forecasts,
    evaluate_forecasts_by_period,
    forecast_error_panel,
    rolling_window_model_ranking,
    validation_slice,
)
from volatility_forecasting_lab.features import (
    daily_log_returns,
    expanding_mean_vol_forecast,
    forward_realized_volatility,
    har_realized_vol_forecast,
    hist_gradient_boosting_vol_forecast,
    lagged_abs_return_forecast,
)

HORIZONS = {
    "next_day": {
        "window": 1,
        "label": "Next-Day",
        "description": "next-day annualized realized volatility",
    },
    "next_week": {
        "window": 5,
        "label": "Next-Week",
        "description": "overlapping five-trading-day annualized realized volatility",
    },
}

BOOTSTRAP_COMPARISONS = [
    ("hist_gradient_boosting", "har_daily_weekly_monthly"),
    ("hist_gradient_boosting", "expanding_mean_abs_return"),
    ("har_daily_weekly_monthly", "expanding_mean_abs_return"),
]


def main() -> None:
    config = load_config()
    prices = load_adjusted_prices()
    returns = daily_log_returns(prices)
    forecasts = {
        "lagged_abs_return": lagged_abs_return_forecast(returns, config.annualization_days),
        "expanding_mean_abs_return": expanding_mean_vol_forecast(
            returns,
            annualization_days=config.annualization_days,
        ),
    }

    output_dir = Path("artifacts/reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    period_metrics_by_horizon = {}
    full_metrics_by_horizon = {}
    error_panels = []

    for horizon_name, horizon_config in HORIZONS.items():
        target = forward_realized_volatility(
            returns,
            horizon=horizon_config["window"],
            annualization_days=config.annualization_days,
        )
        horizon_forecasts = {
            **{
                name: validation_slice(frame, config.validation_start)
                for name, frame in forecasts.items()
            },
            "har_daily_weekly_monthly": validation_slice(
                har_realized_vol_forecast(
                    returns,
                    horizon=horizon_config["window"],
                    annualization_days=config.annualization_days,
                ),
                config.validation_start,
            ),
            "hist_gradient_boosting": validation_slice(
                hist_gradient_boosting_vol_forecast(
                    returns,
                    horizon=horizon_config["window"],
                    validation_start=config.validation_start,
                    annualization_days=config.annualization_days,
                ),
                config.validation_start,
            ),
        }
        validation_target = validation_slice(target, config.validation_start)
        metrics = evaluate_forecasts(
            validation_target,
            horizon_forecasts,
        )
        period_metrics = evaluate_forecasts_by_period(validation_target, horizon_forecasts)
        error_panels.append(
            forecast_error_panel(
                validation_target,
                horizon_forecasts,
                horizon=horizon_name,
            )
        )
        period_metrics.insert(0, "horizon", horizon_name)
        metrics.insert(0, "horizon", horizon_name)
        period_metrics_by_horizon[horizon_name] = period_metrics
        full_metrics_by_horizon[horizon_name] = metrics
        metrics_path = output_dir / f"baseline_{horizon_name}_metrics.csv"
        report_path = output_dir / f"baseline_{horizon_name}_report.md"
        metrics.drop(columns=["horizon"]).to_csv(metrics_path, index=False)
        report_path.write_text(
            _render_report(
                metrics=metrics.drop(columns=["horizon"]),
                validation_start=config.validation_start,
                horizon_label=horizon_config["label"],
                target_description=horizon_config["description"],
                horizon_window=horizon_config["window"],
            )
        )
        print(f"Wrote {len(metrics)} metric rows to {metrics_path}")

    all_period_metrics = pd.concat(period_metrics_by_horizon.values(), ignore_index=True)
    all_period_metrics.to_csv(output_dir / "subperiod_model_comparison.csv", index=False)
    (output_dir / "subperiod_model_comparison.md").write_text(
        _render_subperiod_report(all_period_metrics, full_metrics_by_horizon)
    )
    print(
        f"Wrote {len(all_period_metrics)} rows to "
        f"{output_dir / 'subperiod_model_comparison.csv'}"
    )

    all_errors = pd.concat(error_panels, ignore_index=True)
    all_errors.to_csv(output_dir / "forecast_error_panel.csv", index=False)
    rolling_rankings = rolling_window_model_ranking(all_errors)
    rolling_rankings.to_csv(output_dir / "rolling_window_model_ranking.csv", index=False)
    (output_dir / "rolling_window_model_ranking.md").write_text(
        _render_rolling_window_report(rolling_rankings)
    )
    print(
        f"Wrote {len(rolling_rankings)} rows to "
        f"{output_dir / 'rolling_window_model_ranking.csv'}"
    )
    bootstrap_differences = block_bootstrap_error_differences(
        all_errors,
        comparisons=BOOTSTRAP_COMPARISONS,
    )
    bootstrap_differences.to_csv(output_dir / "bootstrap_error_differences.csv", index=False)
    (output_dir / "bootstrap_error_differences.md").write_text(
        _render_bootstrap_report(bootstrap_differences)
    )
    print(
        f"Wrote {len(bootstrap_differences)} rows to "
        f"{output_dir / 'bootstrap_error_differences.csv'}"
    )


def _render_report(
    metrics,
    validation_start: str,
    horizon_label: str,
    target_description: str,
    horizon_window: int,
) -> str:
    return "\n".join(
        [
            f"# Baseline {horizon_label} Volatility Forecast Evaluation",
            "",
            f"Validation slice starts at `{validation_start}`.",
            f"Target horizon: `{horizon_window}` trading day(s).",
            "",
            f"This report compares simple baseline forecasts for {target_description}. "
            "It is a methodology scaffold, not an investment or trading result.",
            "",
            "Lower MAE/RMSE indicates lower forecast error within this target, date range, "
            "and ticker only. The table should not be read across horizons or as a trading "
            "performance result.",
            "",
            metrics.to_markdown(index=False, floatfmt=".6f"),
            "",
            "## Caveats",
            "",
            "- yfinance data is a free public-data source and can be revised.",
            "- Baselines are intentionally simple and are not tuned for performance claims.",
            (
                "- The HAR-style baseline is an expanding-window OLS statistical benchmark; "
                "it is not an optimized ML model or trading strategy."
            ),
            (
                "- The histogram gradient boosting row is a modest scikit-learn ML baseline "
                "with annual expanding-window refits, not a tuned model selection result."
            ),
            (
                "- Metrics describe forecast errors only; they are not trading, "
                "allocation, or alpha metrics."
            ),
        ]
    )


def _render_subperiod_report(period_metrics, full_metrics_by_horizon) -> str:
    summary_rows = []
    for horizon, metrics in full_metrics_by_horizon.items():
        for metric in ["mae", "rmse"]:
            pivot = metrics.pivot(index="ticker", columns="model", values=metric)
            har = pivot["har_daily_weekly_monthly"]
            ml = pivot["hist_gradient_boosting"]
            summary_rows.append(
                {
                    "horizon": horizon,
                    "metric": metric,
                    "ml_better_than_har_tickers": int((ml < har).sum()),
                    "ticker_count": int(len(pivot)),
                }
            )
    summary = pd.DataFrame(summary_rows)

    rank_rows = []
    for (horizon, period, ticker), group in period_metrics.groupby(["horizon", "period", "ticker"]):
        for metric in ["mae", "rmse"]:
            best = group.sort_values([metric, "model"]).iloc[0]
            rank_rows.append(
                {
                    "horizon": horizon,
                    "period": period,
                    "ticker": ticker,
                    "metric": metric,
                    "best_model": best["model"],
                }
            )
    ranks = pd.DataFrame(rank_rows)
    win_counts = (
        ranks.groupby(["horizon", "metric", "best_model"])
        .size()
        .reset_index(name="subperiod_ticker_wins")
        .sort_values(["horizon", "metric", "best_model"])
    )

    return "\n".join(
        [
            "# Subperiod Model Comparison",
            "",
            "This report checks whether model behavior is stable across calendar-year "
            "subperiods inside the validation slice.",
            "",
            "The counts below are forecast-error diagnostics only. They are not trading, "
            "allocation, alpha, or investment results.",
            "",
            "## Full-Slice ML Versus HAR Counts",
            "",
            summary.to_markdown(index=False),
            "",
            "## Calendar-Year Best-Model Counts",
            "",
            win_counts.to_markdown(index=False),
            "",
            "## Interpretation",
            "",
            "Model behavior is mixed across metrics and horizons. The ML baseline is useful "
            "as a diagnostic comparison row, but the subperiod view should not be read as "
            "evidence of robust model superiority.",
        ]
    )


def _render_rolling_window_report(rankings) -> str:
    if rankings.empty:
        return "\n".join(
            [
                "# Rolling-Window Model Ranking",
                "",
                "No rolling-window rankings were generated. Check the configured window length, "
                "validation span, and minimum-observation threshold.",
            ]
        )

    best_models = rankings[rankings["rank"] == 1]
    best_counts = (
        best_models.groupby(["horizon", "metric", "model"])
        .size()
        .reset_index(name="rolling_window_wins")
        .sort_values(["horizon", "metric", "model"])
    )
    average_rank = (
        rankings.groupby(["horizon", "metric", "model"])["rank"]
        .mean()
        .reset_index(name="average_rank")
        .sort_values(["horizon", "metric", "average_rank", "model"])
    )
    instability = (
        best_models.groupby(["horizon", "ticker", "metric"])["model"]
        .nunique()
        .reset_index(name="distinct_best_models")
        .sort_values(["horizon", "ticker", "metric"])
    )
    instability["best_model_changed"] = instability["distinct_best_models"] > 1

    return "\n".join(
        [
            "# Rolling-Window Model Ranking",
            "",
            "This report checks whether model rankings are stable across rolling validation "
            "windows. Windows use 252 trading days, step forward by 21 trading days, and "
            "require at least 126 observations per model.",
            "",
            "Lower MAE/RMSE ranks better inside a given horizon, ticker, metric, and window. "
            "These are forecast-error diagnostics only, not trading, allocation, alpha, or "
            "investment results.",
            "",
            "## Best-Model Counts",
            "",
            best_counts.to_markdown(index=False),
            "",
            "## Average Rank",
            "",
            average_rank.to_markdown(index=False, floatfmt=".3f"),
            "",
            "## Best-Model Instability Flags",
            "",
            instability.to_markdown(index=False),
            "",
            "## Interpretation",
            "",
            "Rolling-window rankings are intended to expose time variation in forecast-error "
            "behavior. A higher win count or lower average rank should not be compressed into "
            "a broad model-superiority claim without matching uncertainty evidence.",
        ]
    )


def _render_bootstrap_report(differences) -> str:
    if differences.empty:
        return "\n".join(
            [
                "# Block-Bootstrap Error Differences",
                "",
                "No bootstrap error differences were generated. Check comparison model names "
                "and forecast-error panel coverage.",
            ]
        )

    summary = differences.copy()
    summary["interval_crosses_zero"] = (summary["ci_lower"] <= 0) & (summary["ci_upper"] >= 0)
    summary["mostly_negative"] = summary["share_negative"] >= 0.95
    summary_table = summary[
        [
            "horizon",
            "metric",
            "model_a",
            "model_b",
            "mostly_negative",
            "interval_crosses_zero",
        ]
    ]
    summary_table = (
        summary_table.groupby(
            [
                "horizon",
                "metric",
                "model_a",
                "model_b",
                "mostly_negative",
                "interval_crosses_zero",
            ]
        )
        .size()
        .reset_index(name="ticker_count")
        .sort_values(["horizon", "metric", "model_a", "model_b", "mostly_negative"])
    )

    display = differences[
        [
            "horizon",
            "ticker",
            "metric",
            "model_a",
            "model_b",
            "observed_difference",
            "ci_lower",
            "ci_upper",
            "share_negative",
        ]
    ]

    return "\n".join(
        [
            "# Block-Bootstrap Error Differences",
            "",
            "This report estimates uncertainty around pairwise forecast-error differences "
            "using contiguous validation-date block resampling.",
            "",
            "Difference convention: `metric(model_a) - metric(model_b)`. Negative values "
            "mean `model_a` had lower forecast error for that diagnostic.",
            "",
            "Defaults: 20-trading-day blocks, 1,000 bootstrap resamples, fixed random seed, "
            "and 95% percentile intervals.",
            "",
            "These intervals are forecast-error uncertainty diagnostics only. They are not "
            "trading, allocation, alpha, investment, or economic-value evidence.",
            "",
            "## Summary Counts",
            "",
            summary_table.to_markdown(index=False),
            "",
            "## Pairwise Error Differences",
            "",
            display.to_markdown(index=False, floatfmt=".6f"),
            "",
            "## Interpretation",
            "",
            "`share_negative` is the share of bootstrap resamples where `model_a` has lower "
            "error than `model_b`. Intervals crossing zero should be treated as weak or "
            "mixed evidence. Even intervals mostly on one side of zero remain conditional "
            "method-comparison evidence for the named horizon, ticker, metric, and validation "
            "design only.",
        ]
    )


if __name__ == "__main__":
    main()
