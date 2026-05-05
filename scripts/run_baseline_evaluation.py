from pathlib import Path

from volatility_forecasting_lab.config import load_config
from volatility_forecasting_lab.data import load_adjusted_prices
from volatility_forecasting_lab.evaluation import evaluate_forecasts, validation_slice
from volatility_forecasting_lab.features import (
    daily_log_returns,
    expanding_mean_vol_forecast,
    lagged_abs_return_forecast,
    next_day_realized_volatility,
)


def main() -> None:
    config = load_config()
    prices = load_adjusted_prices()
    returns = daily_log_returns(prices)
    target = next_day_realized_volatility(returns, config.annualization_days)

    forecasts = {
        "lagged_abs_return": lagged_abs_return_forecast(returns, config.annualization_days),
        "expanding_mean_abs_return": expanding_mean_vol_forecast(
            returns,
            annualization_days=config.annualization_days,
        ),
    }
    metrics = evaluate_forecasts(
        validation_slice(target, config.validation_start),
        {
            name: validation_slice(frame, config.validation_start)
            for name, frame in forecasts.items()
        },
    )

    output_dir = Path("artifacts/reports")
    output_dir.mkdir(parents=True, exist_ok=True)
    metrics.to_csv(output_dir / "baseline_next_day_metrics.csv", index=False)
    (output_dir / "baseline_next_day_report.md").write_text(
        _render_report(metrics, config.validation_start)
    )
    print(f"Wrote {len(metrics)} metric rows to {output_dir / 'baseline_next_day_metrics.csv'}")


def _render_report(metrics, validation_start: str) -> str:
    return "\n".join(
        [
            "# Baseline Next-Day Volatility Forecast Evaluation",
            "",
            f"Validation slice starts at `{validation_start}`.",
            "",
            "This report compares simple baseline forecasts for next-day annualized realized "
            "volatility. It is a methodology scaffold, not an investment or trading result.",
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
                "- Metrics describe forecast errors only; they are not trading, "
                "allocation, or alpha metrics."
            ),
        ]
    )


if __name__ == "__main__":
    main()
