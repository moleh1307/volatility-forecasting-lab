from pathlib import Path

from volatility_forecasting_lab.config import load_config
from volatility_forecasting_lab.data import load_adjusted_prices
from volatility_forecasting_lab.evaluation import evaluate_forecasts, validation_slice
from volatility_forecasting_lab.features import (
    daily_log_returns,
    expanding_mean_vol_forecast,
    forward_realized_volatility,
    har_realized_vol_forecast,
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

    for horizon_name, horizon_config in HORIZONS.items():
        target = forward_realized_volatility(
            returns,
            horizon=horizon_config["window"],
            annualization_days=config.annualization_days,
        )
        metrics = evaluate_forecasts(
            validation_slice(target, config.validation_start),
            {
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
            },
        )
        metrics_path = output_dir / f"baseline_{horizon_name}_metrics.csv"
        report_path = output_dir / f"baseline_{horizon_name}_report.md"
        metrics.to_csv(metrics_path, index=False)
        report_path.write_text(
            _render_report(
                metrics=metrics,
                validation_start=config.validation_start,
                horizon_label=horizon_config["label"],
                target_description=horizon_config["description"],
                horizon_window=horizon_config["window"],
            )
        )
        print(f"Wrote {len(metrics)} metric rows to {metrics_path}")


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
                "- Metrics describe forecast errors only; they are not trading, "
                "allocation, or alpha metrics."
            ),
        ]
    )


if __name__ == "__main__":
    main()
