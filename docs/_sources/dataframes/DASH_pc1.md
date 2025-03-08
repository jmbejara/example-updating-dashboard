# Dataframe: `DASH_pc1` - Principal Component 1

This dataframe contains the principal component 1 of the normalized series.



## Dataframe Specs

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
| Data available up to (min)     | 2025-03-07 00:00:00                                                             |
| Data available up to (max)     | 2025-03-07 00:00:00                                                             |
| Download Data as Parquet       | [Parquet](../download_dataframe/DASH_pc1.parquet)            |
| Download Data as Excel         | [Excel](../download_dataframe/DASH_pc1.xlsx)                 |
| Linked Charts                  |   [DASH_pc1_line_plot](../charts/DASH_pc1_line_plot.md)<br>   |

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
