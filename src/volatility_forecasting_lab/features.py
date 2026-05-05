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
