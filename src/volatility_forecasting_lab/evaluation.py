from __future__ import annotations

import numpy as np
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


def block_bootstrap_error_differences(
    error_panel: pd.DataFrame,
    comparisons: list[tuple[str, str]],
    block_length: int = 20,
    resamples: int = 1000,
    random_seed: int = 0,
    interval: float = 0.95,
) -> pd.DataFrame:
    if block_length < 1:
        raise ValueError("block_length must be at least 1")
    if resamples < 1:
        raise ValueError("resamples must be at least 1")
    if not 0 < interval < 1:
        raise ValueError("interval must be between 0 and 1")

    rng = np.random.default_rng(random_seed)
    alpha = (1 - interval) / 2
    rows: list[dict[str, float | int | str]] = []
    panel = error_panel.copy()
    panel["date"] = pd.to_datetime(panel["date"])

    for (horizon, ticker), group in panel.groupby(["horizon", "ticker"]):
        for model_a, model_b in comparisons:
            paired = _paired_model_errors(group, model_a=model_a, model_b=model_b)
            if paired.empty:
                continue

            sampled_indices = _moving_block_bootstrap_indices(
                n_observations=len(paired),
                block_length=block_length,
                resamples=resamples,
                rng=rng,
            )
            for metric in ["mae", "rmse"]:
                observed_difference = _metric_difference(paired, metric=metric)
                sampled_differences = np.array(
                    [
                        _metric_difference(paired.iloc[sample], metric=metric)
                        for sample in sampled_indices
                    ],
                    dtype=float,
                )
                rows.append(
                    {
                        "horizon": horizon,
                        "ticker": ticker,
                        "metric": metric,
                        "model_a": model_a,
                        "model_b": model_b,
                        "observations": int(len(paired)),
                        "observed_difference": float(observed_difference),
                        "ci_lower": float(np.quantile(sampled_differences, alpha)),
                        "ci_upper": float(np.quantile(sampled_differences, 1 - alpha)),
                        "share_negative": float((sampled_differences < 0).mean()),
                        "block_length": int(block_length),
                        "resamples": int(resamples),
                    }
                )

    if not rows:
        return pd.DataFrame(
            columns=[
                "horizon",
                "ticker",
                "metric",
                "model_a",
                "model_b",
                "observations",
                "observed_difference",
                "ci_lower",
                "ci_upper",
                "share_negative",
                "block_length",
                "resamples",
            ]
        )

    return pd.DataFrame(rows).sort_values(
        ["horizon", "ticker", "metric", "model_a", "model_b"]
    ).reset_index(drop=True)


def _moving_block_bootstrap_indices(
    n_observations: int,
    block_length: int,
    resamples: int,
    rng: np.random.Generator,
) -> np.ndarray:
    if n_observations < 1:
        raise ValueError("n_observations must be at least 1")

    effective_block_length = min(block_length, n_observations)
    max_start = n_observations - effective_block_length
    blocks_needed = int(np.ceil(n_observations / effective_block_length))
    indices = np.empty((resamples, n_observations), dtype=int)

    for row in range(resamples):
        starts = rng.integers(0, max_start + 1, size=blocks_needed)
        sample = np.concatenate(
            [np.arange(start, start + effective_block_length) for start in starts]
        )
        indices[row] = sample[:n_observations]

    return indices


def _paired_model_errors(group: pd.DataFrame, model_a: str, model_b: str) -> pd.DataFrame:
    model_errors = group[group["model"].isin([model_a, model_b])]
    paired = model_errors.pivot(index="date", columns="model", values="error").dropna()
    if model_a not in paired.columns or model_b not in paired.columns:
        return pd.DataFrame(columns=[model_a, model_b])
    return paired[[model_a, model_b]].sort_index()


def _metric_difference(paired_errors: pd.DataFrame, metric: str) -> float:
    model_a, model_b = paired_errors.columns
    if metric == "mae":
        return float(paired_errors[model_a].abs().mean() - paired_errors[model_b].abs().mean())
    if metric == "rmse":
        model_a_rmse = float((paired_errors[model_a].pow(2).mean()) ** 0.5)
        model_b_rmse = float((paired_errors[model_b].pow(2).mean()) ** 0.5)
        return model_a_rmse - model_b_rmse
    raise ValueError(f"unsupported metric: {metric}")


def validation_slice(frame: pd.DataFrame, validation_start: str) -> pd.DataFrame:
    return frame.loc[pd.Timestamp(validation_start) :]
