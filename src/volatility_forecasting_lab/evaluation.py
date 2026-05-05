from __future__ import annotations

import pandas as pd


def evaluate_forecasts(target: pd.DataFrame, forecasts: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows: list[dict[str, float | str | int]] = []
    for model_name, forecast in forecasts.items():
        aligned_target, aligned_forecast = target.align(forecast, join="inner")
        mask = aligned_target.notna() & aligned_forecast.notna()
        errors = aligned_forecast[mask] - aligned_target[mask]
        for ticker in aligned_target.columns:
            series = errors[ticker].dropna()
            if series.empty:
                continue
            rows.append(
                {
                    "model": model_name,
                    "ticker": ticker,
                    "observations": int(series.shape[0]),
                    "mae": float(series.abs().mean()),
                    "rmse": float((series.pow(2).mean()) ** 0.5),
                    "bias": float(series.mean()),
                }
            )
    return pd.DataFrame(rows).sort_values(["ticker", "model"]).reset_index(drop=True)


def evaluate_forecasts_by_period(
    target: pd.DataFrame,
    forecasts: dict[str, pd.DataFrame],
    period: str = "YE",
) -> pd.DataFrame:
    rows: list[dict[str, float | str | int]] = []
    for model_name, forecast in forecasts.items():
        aligned_target, aligned_forecast = target.align(forecast, join="inner")
        mask = aligned_target.notna() & aligned_forecast.notna()
        errors = aligned_forecast[mask] - aligned_target[mask]

        for ticker in aligned_target.columns:
            ticker_errors = errors[ticker].dropna()
            if ticker_errors.empty:
                continue

            for period_end, series in ticker_errors.groupby(pd.Grouper(freq=period)):
                if series.empty:
                    continue
                rows.append(
                    {
                        "period": str(period_end.date()),
                        "model": model_name,
                        "ticker": ticker,
                        "observations": int(series.shape[0]),
                        "mae": float(series.abs().mean()),
                        "rmse": float((series.pow(2).mean()) ** 0.5),
                        "bias": float(series.mean()),
                    }
                )

    return (
        pd.DataFrame(rows)
        .sort_values(["period", "ticker", "model"])
        .reset_index(drop=True)
    )


def validation_slice(frame: pd.DataFrame, validation_start: str) -> pd.DataFrame:
    return frame.loc[pd.Timestamp(validation_start) :]
