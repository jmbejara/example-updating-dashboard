# Dataframe: `DASH_normalized_series` - Normalized Series

The `dfn` dataframe contains normalized financial series used in Principal Component Analysis (PCA). This normalization process transforms raw financial data into a standardized format suitable for statistical analysis.

## Series Included

The dataframe contains the following financial series:

```{list-table}
:header-rows: 1
:widths: 5 30 25 15

* - #
  - Column
  - Non-Null Count
  - Dtype
* - 0
  - High Yield Index OAS
  - 7442 non-null
  - float64
* - 1
  - 10Y-2Y Spread
  - 7442 non-null
  - float64
* - 2
  - VIX
  - 7442 non-null
  - float64
* - 3
  - CP - Treasury Spread, 3m
  - 7442 non-null
  - float64
* - 4
  - NASDAQ Ret (transformed)
  - 7442 non-null
  - float64
* - 5
  - 10-Year Treasury (transformed)
  - 7442 non-null
  - float64
```

## Normalization Methodology

The normalization process consists of two main steps:

### 1. Series Transformation

Some series are used directly while others undergo transformation to improve stationarity:

- **High Yield Index OAS**: Used as is
- **10Y-2Y Spread**: Used as is
- **VIX**: Used as is
- **CP - Treasury Spread, 3m**: Calculated as:
  ```python
  df["90-Day AA Fin CP"] - df["10-Year Treasury"]
  ```
- **NASDAQ Ret (transformed)**: Calculated as 90-day rolling mean of percent change minus the overall mean:
  ```python
  df["NASDAQ"].pct_change().rolling(90, min_periods=1).mean() - df["NASDAQ"].pct_change().mean()
  ```
- **10-Year Treasury (transformed)**: Calculated as the difference from its 90-day rolling mean:
  ```python
  df["10-Year Treasury"] - df["10-Year Treasury"].rolling(90, min_periods=1).mean()
  ```

### 2. Statistical Normalization

After transformation, all series undergo z-score normalization:

```python
dfn = (dfn - dfn.mean()) / dfn.std()
```

This results in each series having a mean of 0 and a standard deviation of 1, making them directly comparable regardless of their original scales.

### Pre-Processing Steps

Before normalization, the process also includes:

- Dropping columns with all NaN values
- Forward-filling remaining NaN values
- Removing rows with any NaN values after forward-filling

```python
dfn = dfn.dropna(axis=1, how="all")
dfn = dfn.ffill()
dfn = dfn.dropna()
```

This normalized dataset provides standardized inputs for the PCA analysis, allowing for the extraction of the principal components that represent the underlying market factors.


## Dataframe Specs

| Dataframe Name                 | Normalized Series                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [DASH_normalized_series](../dataframes/DASH_normalized_series.md)                       |
| Data Sources                   | FRED                                        |
| Data Providers                 | FRED                                      |
| Links to Providers             | https://fred.stlouisfed.org/                             |
| Topic Tags                     | Macroeconomics, Financial Economics                                          |
| Type of Data Access            | Public                                              |
| Data License                   | No                                                     |
| License Expiration Date        | N/A                                          |
| Contact Provider Before Use?   | No                                         |
| Provider Contact Information   |                                             |
| Restrictions on Use of Data    | No                                               |
| How is data pulled?            | Pandas DataReader                                                    |
| Data available up to (min)     | 2025-03-07 00:00:00                                                             |
| Data available up to (max)     | 2025-03-07 00:00:00                                                             |
| Download Data as Parquet       | [Parquet](../download_dataframe/DASH_normalized_series.parquet)            |
| Download Data as Excel         | [Excel](../download_dataframe/DASH_normalized_series.xlsx)                 |
| Linked Charts                  |   [DASH_unnormalized_series_chart](../charts/DASH_unnormalized_series_chart.md)<br>  [DASH_normalized_series_chart](../charts/DASH_normalized_series_chart.md)<br>   |

## Pipeline Specs

| Pipeline Name                   | Automated Dashboard Update                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [DASH](../index.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Bitbucket Repo URL              | https://github.com/jmbejara/example-updating-dashboard                        |
| Pipeline Web Page               | <a href="https://github.com/jmbejara/example-updating-dashboard">https://github.com/jmbejara/example-updating-dashboard</a>      |
| Date of Last Code Update        | 2025-03-08 04:01:43           |
| Runs on Linux, Windows, Both, or Other? |Windows/Linux/MacOS|
| Linked Dataframes               |  [DASH_normalized_series](../dataframes/DASH_normalized_series.md)<br>  [DASH_pc1](../dataframes/DASH_pc1.md)<br>  |


In addition to the `requirements.txt` and `r_requirements.txt`, the pipeline code relies
on first loading modules using the following command:
```
module load anaconda3/3.11.4
```
