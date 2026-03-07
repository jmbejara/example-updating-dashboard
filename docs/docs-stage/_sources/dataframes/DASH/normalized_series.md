# Dataframe: `DASH:normalized_series` - Normalized Series

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


## DataFrame Glimpse

```
Rows: 7712
Columns: 7
$ High Yield Index OAS                    <f64> -0.8660707372316615
$ 10Y-2Y Spread                           <f64> -0.403863818177394
$ VIX                                     <f64> 0.4309523139430819
$ CP - Treasury Spread, 3m                <f64> 0.45104899190722353
$ NASDAQ Ret (transformed)                <f64> -0.6807771817142014
$ 10-Year Treasury (transformed)          <f64> -0.001079032199824804
$ DATE                           <datetime[ns]> 2026-03-06 00:00:00


```

## Dataframe Manifest

| Dataframe Name                 | Normalized Series                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [normalized_series](../dataframes/DASH/normalized_series.md)                                       |
| Data Sources                   | FRED                                        |
| Data Providers                 | FRED                                      |
| Links to Providers             | https://fred.stlouisfed.org/                             |
| Topic Tags                     | Macroeconomics, Financial Economics                                          |
| Type of Data Access            | Public                                  |
| How is data pulled?            | Pandas DataReader                                                    |
| Data available up to (min)     | 2026-03-06 00:00:00                                                             |
| Data available up to (max)     | 2026-03-06 00:00:00                                                             |
| Dataframe Path                 | /home/runner/work/example-updating-dashboard/example-updating-dashboard/_data/dfn.parquet                                                   |


**Linked Charts:**


- [DASH:unnormalized_series_chart](../../charts/DASH.unnormalized_series_chart.md)

- [DASH:normalized_series_chart](../../charts/DASH.normalized_series_chart.md)



## Pipeline Manifest

| Pipeline Name                   | Automated Dashboard Update                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [DASH](../index.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/jmbejara/example-updating-dashboard                        |
| Pipeline Web Page               | <a href="file:///home/runner/work/example-updating-dashboard/example-updating-dashboard/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-03-07 04:02:55           |
| OS Compatibility                |  |
| Linked Dataframes               |  [DASH:normalized_series](../dataframes/DASH/normalized_series.md)<br>  [DASH:pc1](../dataframes/DASH/pc1.md)<br>  |


