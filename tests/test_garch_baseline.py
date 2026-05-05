import numpy as np
import pandas as pd

from volatility_forecasting_lab.features import garch_vol_forecast


def test_garch_vol_forecast_returns_positive_validation_forecasts() -> None:
    rng = np.random.default_rng(0)
    index = pd.date_range("2020-01-01", periods=90, freq="B")
    returns = pd.DataFrame(
        {"SPY": rng.normal(0, 0.01, size=len(index))},
        index=index,
    )

    forecasts = garch_vol_forecast(
        returns,
        horizon=5,
        validation_start="2020-03-02",
        min_train_size=40,
        refit_frequency=20,
    )

    validation_forecasts = forecasts.loc["2020-03-02":, "SPY"].dropna()
    assert not validation_forecasts.empty
    assert (validation_forecasts > 0).all()


def test_garch_vol_forecast_rejects_invalid_horizon() -> None:
    returns = pd.DataFrame({"SPY": [0.01, -0.02]}, index=pd.date_range("2024-01-01", periods=2))

    try:
        garch_vol_forecast(returns, horizon=0, validation_start="2024-01-01")
    except ValueError as exc:
        assert str(exc) == "horizon must be at least 1"
    else:
        raise AssertionError("expected ValueError")
