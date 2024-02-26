import pandas as pd
import pandas_datareader
import config
from pathlib import Path

DATA_DIR = Path(config.DATA_DIR)

fred_series_long_names = {
    "BAMLH0A0HYM2": "ICE BofA US High Yield Index Option-Adjusted Spread",
    "NASDAQCOM": "NASDAQ Composite Index",
    "RIFSPPFAAD90NB": "90-Day AA Financial Commercial Paper Interest Rate",
    "DTB3": " 3-Month Treasury Bill Secondary Market Rate, Discount Basis",
    "DGS10": "Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity",
    "T10Y2Y": "10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity",
    "VIXCLS": "CBOE Volatility Index: VIX",
    # "GDP": "Gross Domestic Product",
}

fred_series_short_names = {
    "BAMLH0A0HYM2": "High Yield Index OAS",
    "NASDAQCOM": "NASDAQ",
    "RIFSPPFAAD90NB": "90-Day AA Fin CP",
    "DTB3": "3-Month T-Bill",
    "DGS10": "10-Year Treasury",
    "T10Y2Y": "10Y-2Y Spread",
    "VIXCLS": "VIX",
    # "GDP": "GDP",
}


def load_fred(data_dir=DATA_DIR, convert_names=True):
    file_path = Path(data_dir) / "pulled" / "fred.csv"
    df = pd.read_csv(file_path, parse_dates=["DATE"])
    df = df.set_index("DATE")
    # df = pd.read_parquet(file_path)
    if convert_names:
        df = convert_columns_name(df, length="short")
    return df


def pull_fred(
    start_date="1913-01-01",
    end_date="2023-10-01",
):
    df = pandas_datareader.get_data_fred(
        fred_series_short_names.keys(), start=start_date, end=end_date
    )
    return df


def convert_columns_name(df, length="short"):
    if length == "long":
        df = df.rename(columns=fred_series_long_names)
    else:
        df = df.rename(columns=fred_series_short_names)
    return df


if __name__ == "__main__":
    # Pull and save cache of fred data
    today = pd.to_datetime("today")
    df = pull_fred(
        start_date="1913-01-01",
        end_date=today,
    )
    dirpath = DATA_DIR / "pulled"
    dirpath.mkdir(exist_ok=True)
    df.to_csv(dirpath / "fred.csv")
