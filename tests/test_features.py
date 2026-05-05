import numpy as np
import pandas as pd

from volatility_forecasting_lab.features import (
    daily_log_returns,
    forward_realized_volatility,
    har_realized_vol_forecast,
    hist_gradient_boosting_vol_forecast,
    lagged_abs_return_forecast,
    ml_feature_matrix,
    next_day_realized_volatility,
)


def test_next_day_realized_volatility_uses_future_return_as_target() -> None:
    prices = pd.DataFrame(
        {"SPY": [100.0, 101.0, 99.0]},
        index=pd.date_range("2024-01-01", periods=3),
    )
    returns = daily_log_returns(prices)

    target = next_day_realized_volatility(returns, annualization_days=252)

    expected_second_return_vol = abs(np.log(99.0 / 101.0)) * np.sqrt(252)
    assert np.isclose(target.iloc[0]["SPY"], expected_second_return_vol)
    assert np.isnan(target.iloc[-1]["SPY"])


def test_lagged_abs_return_forecast_uses_current_known_return() -> None:
    prices = pd.DataFrame({"SPY": [100.0, 101.0]}, index=pd.date_range("2024-01-01", periods=2))
    returns = daily_log_returns(prices)

    forecast = lagged_abs_return_forecast(returns, annualization_days=252)

    assert np.isclose(forecast.iloc[0]["SPY"], abs(np.log(101.0 / 100.0)) * np.sqrt(252))


def test_forward_realized_volatility_uses_future_window_only() -> None:
    returns = pd.DataFrame(
        {"SPY": [0.01, -0.02, 0.03, -0.04]},
        index=pd.date_range("2024-01-01", periods=4),
    )

    target = forward_realized_volatility(returns, horizon=2, annualization_days=252)

    expected_first = np.sqrt(((-0.02) ** 2 + 0.03**2) * 252 / 2)
    expected_second = np.sqrt((0.03**2 + (-0.04) ** 2) * 252 / 2)
    assert np.isclose(target.iloc[0]["SPY"], expected_first)
    assert np.isclose(target.iloc[1]["SPY"], expected_second)
    assert np.isnan(target.iloc[2]["SPY"])
    assert np.isnan(target.iloc[3]["SPY"])


def test_five_day_forward_realized_volatility_leaves_last_five_rows_missing() -> None:
    returns = pd.DataFrame(
        {"SPY": [0.01, -0.02, 0.03, -0.04, 0.05, -0.06, 0.07]},
        index=pd.date_range("2024-01-01", periods=7),
    )

    target = forward_realized_volatility(returns, horizon=5, annualization_days=252)

    expected_first = np.sqrt(
        ((-0.02) ** 2 + 0.03**2 + (-0.04) ** 2 + 0.05**2 + (-0.06) ** 2)
        * 252
        / 5
    )
    expected_second = np.sqrt(
        (0.03**2 + (-0.04) ** 2 + 0.05**2 + (-0.06) ** 2 + 0.07**2)
        * 252
        / 5
    )
    assert np.isclose(target.iloc[0]["SPY"], expected_first)
    assert np.isclose(target.iloc[1]["SPY"], expected_second)
    assert target.iloc[2:]["SPY"].isna().all()


def test_har_forecast_waits_until_forward_labels_are_observable() -> None:
    returns = pd.DataFrame(
        {"SPY": np.linspace(0.01, 0.08, 40)},
        index=pd.date_range("2024-01-01", periods=40),
    )

    forecast = har_realized_vol_forecast(
        returns,
        horizon=5,
        min_train_size=3,
        annualization_days=252,
    )

    assert forecast.iloc[:28]["SPY"].isna().all()
    assert np.isfinite(forecast.iloc[28]["SPY"])


def test_ml_feature_matrix_has_stable_ticker_feature_columns() -> None:
    returns = pd.DataFrame(
        {
            "SPY": np.linspace(0.01, 0.04, 30),
            "TLT": np.linspace(-0.02, 0.01, 30),
        },
        index=pd.date_range("2024-01-01", periods=30),
    )

    features = ml_feature_matrix(returns, annualization_days=252)

    assert features.columns.names == [None, None]
    assert ("SPY", "vol_mean_5d") in features.columns
    assert ("TLT", "signed_return_mean_22d") in features.columns
    assert np.isclose(features.loc[returns.index[0], ("SPY", "signed_return_1d")], 0.01)
    assert np.isnan(features.loc[returns.index[3], ("SPY", "vol_mean_5d")])
    assert np.isfinite(features.loc[returns.index[4], ("SPY", "vol_mean_5d")])


def test_ml_feature_matrix_uses_only_current_and_past_returns() -> None:
    returns = pd.DataFrame(
        {"SPY": [0.01, 0.02, 0.03, 0.04, 0.50, 0.06]},
        index=pd.date_range("2024-01-01", periods=6),
    )

    baseline_features = ml_feature_matrix(returns, annualization_days=252)
    shocked_returns = returns.copy()
    shocked_returns.iloc[5, 0] = 9.99
    shocked_features = ml_feature_matrix(shocked_returns, annualization_days=252)

    row_before_shock = returns.index[4]
    pd.testing.assert_series_equal(
        baseline_features.loc[row_before_shock],
        shocked_features.loc[row_before_shock],
        check_names=False,
    )


def test_hist_gradient_boosting_forecast_respects_label_availability() -> None:
    returns = pd.DataFrame(
        {
            "SPY": np.sin(np.linspace(0.0, 8.0, 90)) / 100,
        },
        index=pd.date_range("2024-01-01", periods=90),
    )

    forecast = hist_gradient_boosting_vol_forecast(
        returns,
        horizon=5,
        validation_start="2024-02-01",
        min_train_size=20,
        retrain_frequency=10,
        annualization_days=252,
    )

    assert forecast.loc[: "2024-01-31", "SPY"].isna().all()
    first_valid_date = forecast["SPY"].first_valid_index()
    assert first_valid_date is not None

    first_valid_position = returns.index.get_loc(first_valid_date)
    latest_known_position = first_valid_position - 5
    feature_rows = ml_feature_matrix(returns, annualization_days=252)["SPY"]
    target = forward_realized_volatility(returns, horizon=5, annualization_days=252)["SPY"]
    train_frame = (
        feature_rows.iloc[: latest_known_position + 1]
        .assign(target=target.iloc[: latest_known_position + 1])
        .dropna()
    )

    assert len(train_frame) >= 20
    assert forecast.iloc[:first_valid_position]["SPY"].isna().all()
