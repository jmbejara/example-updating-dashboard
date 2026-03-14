# Dataframe: `DASH:pc1` - Principal Component 1

This dataframe contains the principal component 1 of the normalized series.



## DataFrame Glimpse

```
Rows: 7717
Columns: 2
$ PC1           <f64> -0.1719744480330026
$ DATE <datetime[ns]> 2026-03-13 00:00:00


```

## Dataframe Manifest

| Dataframe Name                 | Principal Component 1                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [pc1](../dataframes/DASH/pc1.md)                                       |
| Data Sources                   | FRED                                        |
| Data Providers                 | FRED                                      |
| Links to Providers             | https://fred.stlouisfed.org/                             |
| Topic Tags                     | Macroeconomics, Financial Economics                                          |
| Type of Data Access            | Public                                  |
| How is data pulled?            | Pandas DataReader                                                    |
| Data available up to (min)     | 2026-03-13 00:00:00                                                             |
| Data available up to (max)     | 2026-03-13 00:00:00                                                             |
| Dataframe Path                 | /home/runner/work/example-updating-dashboard/example-updating-dashboard/_data/pc1.parquet                                                   |


**Linked Charts:**


- [DASH:pc1_line_plot](../../charts/DASH.pc1_line_plot.md)



## Pipeline Manifest

| Pipeline Name                   | Automated Dashboard Update                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [DASH](../index.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/jmbejara/example-updating-dashboard                        |
| Pipeline Web Page               | <a href="file:///home/runner/work/example-updating-dashboard/example-updating-dashboard/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-03-14 05:04:24           |
| OS Compatibility                |  |
| Linked Dataframes               |  [DASH:normalized_series](../dataframes/DASH/normalized_series.md)<br>  [DASH:pc1](../dataframes/DASH/pc1.md)<br>  |


