---
date: 2025-03-08 04:01:43
tags: FRED
category: Macroeconomics, Financial Economics
---

# Chart: Principal Component 1 Line Plot
Line plot of principal component 1.

## Chart
```{raw} html
<iframe src="../_static/DASH_pc1_line_plot.html" height="500px" width="100%"></iframe>
```
[Full Screen Chart](../download_chart/DASH_pc1_line_plot.html)
This chart shows the principal component 1 of the normalized series.



| Chart Name             | Principal Component 1 Line Plot                                             |
|------------------------|------------------------------------------------------------|
| Chart ID               | pc1_line_plot                                               |
| Topic Tags             | Macroeconomics, Financial Economics                                |
| Data Series Start Date | 1993-01-02                                 |
| Data Frequency         | Daily                                         |
| Observation Period     | Weekday                                     |
| Lag in Data Release    | One day                                    |
| Data Release Date(s)   | Weekday                                     |
| Seasonal Adjustment    | None                                    |
| Units                  | Index                                                  |
| Data Series            |                                             |
| HTML Chart             | [HTML](../download_chart/DASH_pc1_line_plot.html)    |

## Data

| Dataframe Name                 | Principal Component 1                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [DASH_pc1](../dataframes/DASH_pc1.md)                       |
| Data Sources                   | FRED                                        |
| Data Providers                 | FRED                                      |
| Links to Providers             | NA                             |
| Topic Tags                     | Macroeconomics, Financial Economics                                          |
| Type of Data Access            | Public                                              |
| Data License                   | No                                                     |
| License Expiration Date        |                                           |
| Contact Provider Before Use?   | No                                         |
| Provider Contact Information   |                                             |
| Restrictions on Use of Data    | No                                               |
| How is data pulled?            | Pandas DataReader                                                    |
| Data available up to (min)     |                                                              |
| Data available up to (max)     |                                                              |
| Download Data as Parquet       | [Parquet](../download_dataframe/DASH_pc1.parquet)            |
| Download Data as Excel         | [Excel](../download_dataframe/DASH_pc1.xlsx)                 |
| Linked Charts                  |   [DASH_pc1_line_plot](../charts/DASH_pc1_line_plot.md)<br>   |

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