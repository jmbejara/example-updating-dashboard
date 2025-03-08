---
date: 2025-03-08 04:01:43
tags: FRED
category: Macroeconomics, Financial Economics
---

# Chart: Normalized Series
Line plot of normalized series.

## Chart
```{raw} html
<iframe src="../_static/DASH_normalized_series_chart.html" height="500px" width="100%"></iframe>
```
[Full Screen Chart](../download_chart/DASH_normalized_series_chart.html)
Simple line plot of normalized series.



| Chart Name             | Normalized Series                                             |
|------------------------|------------------------------------------------------------|
| Chart ID               | normalized_series_chart                                               |
| Topic Tags             | Macroeconomics, Financial Economics                                |
| Data Series Start Date | 1993-01-02                                 |
| Data Frequency         | Daily                                         |
| Observation Period     | Weekday                                     |
| Lag in Data Release    | One day                                    |
| Data Release Date(s)   | Weekday                                     |
| Seasonal Adjustment    | None                                    |
| Units                  | Index                                                  |
| Data Series            |                                             |
| HTML Chart             | [HTML](../download_chart/DASH_normalized_series_chart.html)    |

## Data

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
| Data available up to (min)     |                                                              |
| Data available up to (max)     |                                                              |
| Download Data as Parquet       | [Parquet](../download_dataframe/DASH_normalized_series.parquet)            |
| Download Data as Excel         | [Excel](../download_dataframe/DASH_normalized_series.xlsx)                 |
| Linked Charts                  |   [DASH_unnormalized_series_chart](../charts/DASH_unnormalized_series_chart.md)<br>  [DASH_normalized_series_chart](../charts/DASH_normalized_series_chart.md)<br>   |

## Pipeline

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