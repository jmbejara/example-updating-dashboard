import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import sklearn.decomposition
import statsmodels.multivariate.pca

import plotly.io as pio
import plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go

import config
import load_fred

DATA_DIR = config.DATA_DIR


def transform_series(df):
    """
    Some series are not stationary, so we transform them to make them stationary.
    """
    dfn = pd.DataFrame().reindex_like(df)
    # 'High Yield Index OAS': Leave as is
    dfn["High Yield Index OAS"] = df["High Yield Index OAS"]
    dfn["10Y-2Y Spread"] = df["10Y-2Y Spread"]
    dfn["VIX"] = df["VIX"]
    dfn["CP - Treasury Spread, 3m"] = df["90-Day AA Fin CP"] - df["10-Year Treasury"]
    # dfn['NASDAQ/GDP'] = df['NASDAQ']/(df['GDP'].ffill())
    dfn["NASDAQ Ret (transformed)"] = (
        df["NASDAQ"].pct_change().rolling(90, min_periods=1).mean()
        - df["NASDAQ"].pct_change().mean()
    )
    dfn["10-Year Treasury (transformed)"] = (
        df["10-Year Treasury"]
        - df["10-Year Treasury"].rolling(90, min_periods=1).mean()
    )
    # 'VIX': Leave as is
    # Drop columns that are completely NaN
    dfn = dfn.dropna(axis=1, how="all")
    dfn = dfn.ffill()
    dfn = dfn.dropna()
    dfn = (dfn - dfn.mean()) / dfn.std()
    return dfn


def pca(dfn, module="scikitlearn"):
    if module == "statsmodels":
        _pc1, _loadings, projection, rsquare, _, _, _ = (
            statsmodels.multivariate.pca.pca(
                dfn,
                ncomp=1,
                standardize=True,
                demean=True,
                normalize=True,
                gls=False,
                weights=None,
                method="svd",
            )
        )
        _loadings = _loadings["comp_0"]
        loadings = np.std(_pc1) * _loadings
        pc1 = _pc1 / np.std(_pc1)
        pc1 = pc1.rename(columns={"comp_0": "PC1"})["PC1"]

    elif module == "scikitlearn":
        pca = sklearn.decomposition.PCA(n_components=1)
        _pc1 = pd.Series(pca.fit_transform(dfn)[:, 0], index=dfn.index, name="PC1")
        _loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
        _loadings = pd.Series(_loadings[:, 0], index=dfn.columns)

        loadings = np.std(_pc1) * _loadings
        pc1 = _pc1 / np.std(_pc1)
        pc1.name = "PC1"
    else:
        raise ValueError

    loadings.name = "loadings"

    return pc1, loadings


def stacked_plot(df, filename=None):
    """
    df=category_contributions
    # category_contributions.sum(axis=1).plot()
    TODO: Needs to be fixed to calculate contributions
    """

    df_pos = df[df >= 0]
    df_neg = df[df < 0]

    alpha = 0.3
    linewidth = 0.5

    ax = df_pos.plot.area(alpha=alpha, linewidth=linewidth, legend=False)
    pc1 = df.sum(axis=1)
    pc1.name = "pc1"
    pc1.plot(color="Black", label="pc1", linewidth=1)

    plt.legend()

    ax.set_prop_cycle(None)
    df_neg.plot.area(
        alpha=alpha, ax=ax, linewidth=linewidth, legend=False, ylim=(-3, 3)
    )
    # recompute the ax.dataLim
    ax.relim()
    # update ax.viewLim using the new dataLim
    ax.autoscale()
    # ax.set_ylabel('Standard Deviations')
    # ax.set_ylim(-3,4)
    # ax.set_ylim(-30,30)

    if not (filename is None):
        filename = Path(filename)
        figure = plt.gcf()  # get current figure
        figure.set_size_inches(8, 6)
        plt.savefig(filename, dpi=300)


def pc1_line_plot(pc1):
    """
    Single plot with range slider and selectors
    """
    # fig = px.line(pc1, title="Principal Component 1")
    # fig.show()

    trace = go.Scatter(x=pc1.index, y=pc1, name="PC1")

    data = [trace]
    layout = dict(
        title="First Principal Component (PC1)",
        xaxis=dict(
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            rangeslider=dict(visible=True),
            type="date",
        ),
    )

    fig = go.FigureWidget(data=data, layout=layout)
    fig.show()


def plot_unnormalized_series(df):

    series_names = [
        "High Yield Index OAS",
        "NASDAQ",
        "90-Day AA Fin CP",
        "3-Month T-Bill",
        "10-Year Treasury",
        "10Y-2Y Spread",
        "VIX",
    ]

    # Assume dfn is your dataframe and has the series_names as columns
    column = series_names[0]  # Start with the first series
    df_nona = df.dropna()
    trace = go.Scatter(x=df_nona.index, y=df_nona[column], name=column)

    data = [trace]
    layout = dict(
        title="Raw Economic Series",
        autosize=True,
        xaxis=dict(
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            rangeslider=dict(visible=True),
            type="date",
        ),
        updatemenus=[
            dict(
                type="buttons",
                direction="down",
                buttons=[
                    dict(
                        args=["y", [df_nona[name].values]], label=name, method="restyle"
                    )
                    for name in series_names
                ],
            )
        ],
    )

    fig = go.FigureWidget(data=data, layout=layout)
    fig.show()


def plot_normalized_series(dfn):
    series_names = [
        "High Yield Index OAS",
        "10Y-2Y Spread",
        "VIX",
        "CP - Treasury Spread, 3m",
        "NASDAQ Ret (transformed)",
        "10-Year Treasury (transformed)",
    ]

    # Assume dfn is your dataframe and has the series_names as columns
    column = series_names[0]  # Start with the first series
    df_nona = dfn.dropna()
    trace = go.Scatter(x=df_nona.index, y=df_nona[column], name=column)

    data = [trace]
    layout = dict(
        title="Transformed and Normalized Series",
        autosize=True,
        xaxis=dict(
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            rangeslider=dict(visible=True),
            type="date",
        ),
        updatemenus=[
            dict(
                type="buttons",
                direction="down",
                buttons=[
                    dict(
                        args=["y", [df_nona[name].values]], label=name, method="restyle"
                    )
                    for name in series_names
                ],
            )
        ],
    )

    fig = go.FigureWidget(data=data, layout=layout)
    fig.show()


def _demo():
    df = load_fred.load_fred(data_dir=DATA_DIR)
    dfn = transform_series(df)

    ## Visualize Principal Component 1
    pc1, loadings = pca(dfn, module="scikitlearn")
    pc1.plot()

    # Simple version
    fig = px.line(pc1)
    fig.show()

    # Using slider and quick views
    pc1_line_plot(pc1)

    ## Visualize normalized and raw series
    dfn.plot(subplots=True, figsize=(10, 10))

    fig = px.line(dfn, facet_col="variable", facet_col_wrap=1)
    fig.update_yaxes(matches=None)
    fig.show()

    plot_unnormalized_series(df)
    plot_normalized_series(dfn)

    # Other Charts that Need Work
    stacked_plot(dfn)
    stacked_plot(dfn.iloc[-90:])

    # Stacked Bar Chart
    today = pd.Timestamp.today().normalize()
    month_ago = today - pd.DateOffset(months=1)
    dfn_long = (
        dfn.loc[month_ago:today]
        .stack()
        .reset_index()
        .rename(columns={0: "value", "level_1": "variable"})
    )

    fig = px.bar(dfn_long, x="DATE", y="value", color="variable", title="Long-Form Input")
    fig.show()
