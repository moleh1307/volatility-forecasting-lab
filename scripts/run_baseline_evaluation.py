from pathlib import Path

import pandas as pd

from volatility_forecasting_lab.config import load_config
from volatility_forecasting_lab.data import load_adjusted_prices
from volatility_forecasting_lab.evaluation import (
    evaluate_forecasts,
    evaluate_forecasts_by_period,
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


if __name__ == "__main__":
    main()
