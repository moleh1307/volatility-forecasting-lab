import pandas as pd

from volatility_forecasting_lab.evaluation import evaluate_forecasts, validation_slice


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
