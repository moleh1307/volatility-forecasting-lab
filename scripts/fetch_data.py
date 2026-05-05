from volatility_forecasting_lab.config import load_config
from volatility_forecasting_lab.data import fetch_adjusted_prices


def main() -> None:
    config = load_config()
    prices = fetch_adjusted_prices(config)
    print(
        f"Fetched {len(prices)} rows for {len(prices.columns)} tickers: "
        f"{prices.index.min().date()} to {prices.index.max().date()}"
    )


if __name__ == "__main__":
    main()
