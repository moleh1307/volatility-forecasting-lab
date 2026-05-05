from __future__ import annotations

import numpy as np
import pandas as pd


def daily_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    return np.log(prices).diff().dropna(how="all")


def next_day_realized_volatility(
    returns: pd.DataFrame,
    annualization_days: int = 252,
) -> pd.DataFrame:
    return returns.abs().shift(-1) * np.sqrt(annualization_days)


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
