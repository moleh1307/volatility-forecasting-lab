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


def forecast_error_panel(
    target: pd.DataFrame,
    forecasts: dict[str, pd.DataFrame],
    horizon: str,
) -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    for model_name, forecast in forecasts.items():
        aligned_target, aligned_forecast = target.align(forecast, join="inner")
        mask = aligned_target.notna() & aligned_forecast.notna()

        for ticker in aligned_target.columns:
            ticker_frame = pd.DataFrame(
                {
                    "date": aligned_target.index,
                    "horizon": horizon,
                    "ticker": ticker,
                    "model": model_name,
                    "target": aligned_target[ticker],
                    "forecast": aligned_forecast[ticker],
                }
            )
            ticker_frame = ticker_frame.loc[mask[ticker].to_numpy()].copy()
            if ticker_frame.empty:
                continue
            ticker_frame["error"] = ticker_frame["forecast"] - ticker_frame["target"]
            ticker_frame["abs_error"] = ticker_frame["error"].abs()
            ticker_frame["squared_error"] = ticker_frame["error"].pow(2)
            rows.append(ticker_frame)

    if not rows:
        return pd.DataFrame(
            columns=[
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
        )

    return (
        pd.concat(rows, ignore_index=True)
        .sort_values(["horizon", "ticker", "date", "model"])
        .reset_index(drop=True)
    )


def rolling_window_model_ranking(
    error_panel: pd.DataFrame,
    window_size: int = 252,
    step_size: int = 21,
    min_observations: int = 126,
) -> pd.DataFrame:
    if window_size < 1:
        raise ValueError("window_size must be at least 1")
    if step_size < 1:
        raise ValueError("step_size must be at least 1")
    if min_observations < 1:
        raise ValueError("min_observations must be at least 1")

    rows: list[dict[str, float | int | str]] = []
    panel = error_panel.copy()
    panel["date"] = pd.to_datetime(panel["date"])

    for (horizon, ticker), group in panel.groupby(["horizon", "ticker"]):
        dates = pd.Index(sorted(group["date"].unique()))
        if len(dates) < window_size:
            continue

        for start_position in range(0, len(dates) - window_size + 1, step_size):
            window_dates = dates[start_position : start_position + window_size]
            window_start = pd.Timestamp(window_dates[0])
            window_end = pd.Timestamp(window_dates[-1])
            window = group[group["date"].between(window_start, window_end)]

            for model_name, model_window in window.groupby("model"):
                observations = len(model_window)
                if observations < min_observations:
                    continue
                rows.extend(
                    [
                        {
                            "horizon": horizon,
                            "ticker": ticker,
                            "metric": "mae",
                            "window_start": str(window_start.date()),
                            "window_end": str(window_end.date()),
                            "model": model_name,
                            "observations": int(observations),
                            "value": float(model_window["abs_error"].mean()),
                        },
                        {
                            "horizon": horizon,
                            "ticker": ticker,
                            "metric": "rmse",
                            "window_start": str(window_start.date()),
                            "window_end": str(window_end.date()),
                            "model": model_name,
                            "observations": int(observations),
                            "value": float(model_window["squared_error"].mean() ** 0.5),
                        },
                    ]
                )

    if not rows:
        return pd.DataFrame(
            columns=[
                "horizon",
                "ticker",
                "metric",
                "window_start",
                "window_end",
                "model",
                "observations",
                "value",
                "rank",
            ]
        )

    rankings = pd.DataFrame(rows)
    rankings["rank"] = (
        rankings.sort_values(["value", "model"])
        .groupby(["horizon", "ticker", "metric", "window_start", "window_end"])
        .cumcount()
        + 1
    )
    return rankings.sort_values(
        ["horizon", "ticker", "metric", "window_start", "rank", "model"]
    ).reset_index(drop=True)


def validation_slice(frame: pd.DataFrame, validation_start: str) -> pd.DataFrame:
    return frame.loc[pd.Timestamp(validation_start) :]
