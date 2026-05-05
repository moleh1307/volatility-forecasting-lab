import pandas as pd

from volatility_forecasting_lab.evaluation import (
    evaluate_forecasts,
    evaluate_forecasts_by_period,
    forecast_error_panel,
    rolling_window_model_ranking,
    validation_slice,
)


def test_evaluate_forecasts_returns_mae_rmse_bias() -> None:
    target = pd.DataFrame({"SPY": [0.1, 0.2, 0.3]}, index=pd.date_range("2024-01-01", periods=3))
    forecast = pd.DataFrame({"SPY": [0.2, 0.2, 0.2]}, index=target.index)

    metrics = evaluate_forecasts(target, {"flat": forecast})

    row = metrics.iloc[0]
    assert row["model"] == "flat"
    assert row["ticker"] == "SPY"
    assert row["observations"] == 3
    assert abs(row["mae"] - (0.1 + 0.0 + 0.1) / 3) < 1e-12
    assert abs(row["bias"]) < 1e-12


def test_validation_slice_filters_from_start_date() -> None:
    frame = pd.DataFrame({"SPY": [1, 2, 3]}, index=pd.date_range("2024-01-01", periods=3))

    sliced = validation_slice(frame, "2024-01-02")

    assert list(sliced["SPY"]) == [2, 3]


def test_evaluate_forecasts_by_period_keeps_metrics_separate() -> None:
    target = pd.DataFrame(
        {"SPY": [0.1, 0.2, 0.3, 0.4]},
        index=pd.to_datetime(["2023-12-29", "2023-12-30", "2024-01-02", "2024-01-03"]),
    )
    forecast = pd.DataFrame({"SPY": [0.2, 0.2, 0.5, 0.5]}, index=target.index)

    metrics = evaluate_forecasts_by_period(target, {"flat": forecast}, period="YE")

    assert list(metrics["period"]) == ["2023-12-31", "2024-12-31"]
    assert list(metrics["observations"]) == [2, 2]
    assert abs(metrics.iloc[0]["mae"] - 0.05) < 1e-12
    assert abs(metrics.iloc[1]["mae"] - 0.15) < 1e-12


def test_forecast_error_panel_materializes_long_errors() -> None:
    target = pd.DataFrame({"SPY": [0.1, 0.2]}, index=pd.date_range("2024-01-01", periods=2))
    forecast = pd.DataFrame({"SPY": [0.2, 0.1]}, index=target.index)

    panel = forecast_error_panel(target, {"flat": forecast}, horizon="next_day")

    assert list(panel.columns) == [
        "date",
        "horizon",
        "ticker",
        "model",
        "target",
        "forecast",
        "error",
        "abs_error",
        "squared_error",
    ]
    assert list(panel["horizon"]) == ["next_day", "next_day"]
    assert list(panel["model"]) == ["flat", "flat"]
    assert list(panel["error"].round(10)) == [0.1, -0.1]


def test_rolling_window_model_ranking_orders_lower_error_first() -> None:
    dates = pd.date_range("2024-01-01", periods=4)
    target = pd.DataFrame({"SPY": [1.0, 1.0, 1.0, 1.0]}, index=dates)
    forecasts = {
        "better": pd.DataFrame({"SPY": [1.0, 1.1, 1.0, 1.1]}, index=dates),
        "worse": pd.DataFrame({"SPY": [1.5, 1.5, 1.5, 1.5]}, index=dates),
    }
    panel = forecast_error_panel(target, forecasts, horizon="next_day")

    rankings = rolling_window_model_ranking(
        panel,
        window_size=3,
        step_size=1,
        min_observations=3,
    )

    mae_rankings = rankings[
        (rankings["metric"] == "mae")
        & (rankings["window_start"] == "2024-01-01")
    ].sort_values("rank")
    assert list(mae_rankings["model"]) == ["better", "worse"]
    assert list(mae_rankings["rank"]) == [1, 2]
