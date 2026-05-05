from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor


def daily_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    return np.log(prices).diff().dropna(how="all")


def next_day_realized_volatility(
    returns: pd.DataFrame,
    annualization_days: int = 252,
) -> pd.DataFrame:
    return forward_realized_volatility(returns, horizon=1, annualization_days=annualization_days)


def forward_realized_volatility(
    returns: pd.DataFrame,
    horizon: int,
    annualization_days: int = 252,
) -> pd.DataFrame:
    if horizon < 1:
        raise ValueError("horizon must be at least 1")

    future_squared_returns = returns.pow(2).shift(-1)
    realized_variance = (
        future_squared_returns.iloc[::-1]
        .rolling(window=horizon, min_periods=horizon)
        .sum()
        .iloc[::-1]
    )
    return np.sqrt(realized_variance * annualization_days / horizon)


def lagged_abs_return_forecast(
    returns: pd.DataFrame,
    annualization_days: int = 252,
) -> pd.DataFrame:
    return returns.abs() * np.sqrt(annualization_days)


def expanding_mean_vol_forecast(
    returns: pd.DataFrame,
    min_periods: int = 60,
    annualization_days: int = 252,
) -> pd.DataFrame:
    return returns.abs().expanding(min_periods=min_periods).mean() * np.sqrt(annualization_days)


def ml_feature_matrix(
    returns: pd.DataFrame,
    annualization_days: int = 252,
) -> pd.DataFrame:
    daily_vol = returns.abs() * np.sqrt(annualization_days)
    feature_blocks = {
        "signed_return_1d": returns,
        "abs_return_1d": returns.abs(),
        "vol_1d": daily_vol,
        "vol_mean_5d": daily_vol.rolling(window=5, min_periods=5).mean(),
        "vol_mean_22d": daily_vol.rolling(window=22, min_periods=22).mean(),
        "vol_std_5d": daily_vol.rolling(window=5, min_periods=5).std(),
        "vol_std_22d": daily_vol.rolling(window=22, min_periods=22).std(),
        "signed_return_mean_5d": returns.rolling(window=5, min_periods=5).mean(),
        "signed_return_mean_22d": returns.rolling(window=22, min_periods=22).mean(),
    }
    features = pd.concat(feature_blocks, axis=1)
    features = features.swaplevel(0, 1, axis=1)
    return features.sort_index(axis=1)


def hist_gradient_boosting_vol_forecast(
    returns: pd.DataFrame,
    horizon: int,
    validation_start: str,
    min_train_size: int = 756,
    retrain_frequency: int = 252,
    annualization_days: int = 252,
) -> pd.DataFrame:
    if horizon < 1:
        raise ValueError("horizon must be at least 1")

    target = forward_realized_volatility(
        returns,
        horizon=horizon,
        annualization_days=annualization_days,
    )
    features = ml_feature_matrix(returns, annualization_days=annualization_days)
    forecasts = pd.DataFrame(index=returns.index, columns=returns.columns, dtype=float)
    validation_start_ts = pd.Timestamp(validation_start)

    for ticker in returns.columns:
        ticker_features = features[ticker]
        target_series = target[ticker]
        model: HistGradientBoostingRegressor | None = None
        last_train_position: int | None = None

        for row_position, row_date in enumerate(returns.index):
            if row_date < validation_start_ts:
                continue

            latest_known_target_position = row_position - horizon
            if latest_known_target_position < 0:
                continue

            current_features = ticker_features.iloc[[row_position]].dropna()
            if current_features.empty:
                continue

            should_retrain = (
                model is None
                or last_train_position is None
                or latest_known_target_position - last_train_position >= retrain_frequency
            )
            if should_retrain:
                train_features = ticker_features.iloc[: latest_known_target_position + 1]
                train_target = target_series.iloc[: latest_known_target_position + 1]
                train_frame = train_features.assign(target=train_target).dropna()
                if len(train_frame) < min_train_size:
                    continue

                model = HistGradientBoostingRegressor(
                    max_iter=30,
                    learning_rate=0.05,
                    max_leaf_nodes=7,
                    l2_regularization=0.01,
                    random_state=0,
                )
                model.fit(train_frame[ticker_features.columns], train_frame["target"])
                last_train_position = latest_known_target_position

            if model is not None:
                forecasts.at[row_date, ticker] = float(model.predict(current_features)[0])

    return forecasts


def har_realized_vol_forecast(
    returns: pd.DataFrame,
    horizon: int,
    min_train_size: int = 252,
    annualization_days: int = 252,
) -> pd.DataFrame:
    if horizon < 1:
        raise ValueError("horizon must be at least 1")

    target = forward_realized_volatility(
        returns,
        horizon=horizon,
        annualization_days=annualization_days,
    )
    daily_vol = returns.abs() * np.sqrt(annualization_days)
    forecasts = pd.DataFrame(index=returns.index, columns=returns.columns, dtype=float)

    for ticker in returns.columns:
        features = pd.DataFrame(
            {
                "daily": daily_vol[ticker],
                "weekly": daily_vol[ticker].rolling(window=5, min_periods=5).mean(),
                "monthly": daily_vol[ticker].rolling(window=22, min_periods=22).mean(),
            },
            index=returns.index,
        )
        target_series = target[ticker]
        design = features.assign(intercept=1.0)[["intercept", "daily", "weekly", "monthly"]]
        xtx = np.zeros((4, 4), dtype=float)
        xty = np.zeros(4, dtype=float)
        train_count = 0
        next_train_position = 0

        for row_position, row_date in enumerate(returns.index):
            latest_known_target_position = row_position - horizon
            if latest_known_target_position < 0:
                continue

            while next_train_position <= latest_known_target_position:
                x_train = design.iloc[next_train_position].to_numpy(dtype=float)
                y_train = target_series.iloc[next_train_position]
                if np.isfinite(x_train).all() and np.isfinite(y_train):
                    xtx += np.outer(x_train, x_train)
                    xty += x_train * float(y_train)
                    train_count += 1
                next_train_position += 1

            x_current = design.loc[row_date].to_numpy(dtype=float)
            if train_count < min_train_size or not np.isfinite(x_current).all():
                continue

            beta = np.linalg.pinv(xtx) @ xty
            forecasts.at[row_date, ticker] = float(x_current @ beta)

    return forecasts
