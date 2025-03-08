# Automated Dashboard Update

Last updated: {sub-ref}`today` 


## Table of Contents

```{toctree}
:maxdepth: 1
:caption: Notebooks 📖
notebooks/DASH_01_pca_index_visualizations.ipynb
notebooks/DASH_02_pca_index_dashboard.ipynb
```



```{toctree}
:maxdepth: 1
:caption: Pipeline Charts 📈
charts.md
```

```{postlist}
:format: "{title}"
```


```{toctree}
:maxdepth: 1
:caption: Pipeline Dataframes 📊
dataframes/DASH_normalized_series.md
dataframes/DASH_pc1.md
```


```{toctree}
:maxdepth: 1
:caption: Appendix 💡
myst_markdown_demos.md
apidocs/index
```


## Pipeline Specs

  | Pipeline Name                   | Automated Dashboard Update                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [DASH](./index.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Bitbucket Repo URL              | https://github.com/jmbejara/example-updating-dashboard                        |
| Pipeline Web Page               | <a href="https://github.com/jmbejara/example-updating-dashboard">https://github.com/jmbejara/example-updating-dashboard</a>      |
| Date of Last Code Update        | 2025-03-08 04:01:43           |
| Runs on Linux, Windows, Both, or Other? |Windows/Linux/MacOS|
| Linked Dataframes               |  [DASH_normalized_series](./dataframes/DASH_normalized_series.md)<br>  [DASH_pc1](./dataframes/DASH_pc1.md)<br>  |


In addition to the `requirements.txt` and `r_requirements.txt`, the pipeline code relies
on first loading modules using the following command:
```
module load anaconda3/3.11.4
```




# About this project

This example uses GitHub Actions to automatically update a dashboard. The dashboard consists of a Sphinx site that is published to GitHub Pages. The Sphinx site is generated using a custom tool called ChartBook: https://github.com/jmbejara/chartbook 



# Quick Start

To quickest way to run code in this repo is to use the following steps. First, note that you must have TexLive installed on your computer and available in your path.
You can do this by downloading and installing it from here ([windows](https://tug.org/texlive/windows.html#install) and [mac](https://tug.org/mactex/mactex-download.html) installers).
Having installed LaTeX, open a terminal and navigate to the root directory of the project and create a conda environment using the following command:
```
conda create -n blank python=3.12
conda activate blank
```
and then install the dependencies with pip
```
pip install -r requirements.txt
```
You can then navigate to the `src` directory and then run 
```
doit
```
