from __future__ import annotations

import numpy as np
import pandas as pd


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
