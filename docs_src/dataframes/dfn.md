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