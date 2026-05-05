from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pandas as pd
import yfinance as yf

from volatility_forecasting_lab.config import ProjectConfig, write_yaml


def fetch_adjusted_prices(
    config: ProjectConfig,
    output_path: str | Path = "data/raw/adjusted_close.csv",
    manifest_path: str | Path = "data/raw/manifest.yml",
) -> pd.DataFrame:
    prices = yf.download(
        tickers=config.tickers,
        start=config.start_date,
        auto_adjust=True,
        progress=False,
        group_by="column",
    )
    adjusted_close = _extract_close(prices, config.tickers)
    adjusted_close = adjusted_close.dropna(how="all")

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    adjusted_close.to_csv(output, index_label="date")

    write_yaml(
        manifest_path,
        {
            "source": "yfinance",
            "retrieved_at_utc": datetime.now(UTC).isoformat(),
            "tickers": config.tickers,
            "start_date": config.start_date,
            "rows": int(len(adjusted_close)),
            "columns": list(adjusted_close.columns),
            "min_date": str(adjusted_close.index.min().date()),
            "max_date": str(adjusted_close.index.max().date()),
            "caveats": [
                (
                    "yfinance is a free public-data interface and may revise "
                    "historical adjusted prices."
                ),
                (
                    "This cache is for research methodology, not production "
                    "trading or investment advice."
                ),
            ],
        },
    )
    return adjusted_close


def load_adjusted_prices(path: str | Path = "data/raw/adjusted_close.csv") -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["date"], index_col="date")


def _extract_close(downloaded: pd.DataFrame, tickers: list[str]) -> pd.DataFrame:
    if isinstance(downloaded.columns, pd.MultiIndex):
        if "Close" in downloaded.columns.get_level_values(0):
            close = downloaded["Close"]
        elif "Adj Close" in downloaded.columns.get_level_values(0):
            close = downloaded["Adj Close"]
        else:
            raise ValueError(
                "Downloaded yfinance data does not contain Close or Adj Close columns."
            )
    else:
        close = downloaded[["Close"]].copy()
        close.columns = tickers
    return close.reindex(columns=tickers)
