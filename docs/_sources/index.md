# Automated Dashboard Update

Last updated: {sub-ref}`today` 


## Table of Contents

```{toctree}
:maxdepth: 1
:caption: Notebooks 📖
notebooks/DASH/01_pca_index_visualizations.ipynb
notebooks/DASH/02_pca_index_dashboard.ipynb
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
dataframes/DASH/normalized_series.md
dataframes/DASH/pc1.md
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
| Git Repo URL                    | https://github.com/jmbejara/example-updating-dashboard                        |
| Pipeline Web Page               | <a href="file:///home/runner/work/example-updating-dashboard/example-updating-dashboard/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-03-07 04:02:55           |
| OS Compatibility                |  |
| Linked Dataframes               |  [DASH:normalized_series](./dataframes/DASH/normalized_series.md)<br>  [DASH:pc1](./dataframes/DASH/pc1.md)<br>  |





# About this project

This example uses GitHub Actions to automatically update a dashboard. The dashboard consists of a Sphinx site that is published to GitHub Pages. The Sphinx site is generated using a custom tool called ChartBook: https://github.com/jmbejara/chartbook

The documentation for ChartBook is available here: https://backofficedev.github.io/chartbook



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
