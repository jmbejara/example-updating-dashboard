#!/usr/bin/env python
# coding: utf-8

# # PCA Index Dashboard

# In[ ]:


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


# In[ ]:


def transform_series(df):
    """
    Some series are not stationary, so we transform them to make them stationary.
    """
    dfn = pd.DataFrame().reindex_like(df)
    # 'High Yield Index OAS': Leave as is
    dfn['High Yield Index OAS'] = df['High Yield Index OAS']
    dfn['CP - Treasury Spread, 3m'] = df['90-Day AA Fin CP'] - df['10-Year Treasury']
    # dfn['NASDAQ/GDP'] = df['NASDAQ']/df['GDP']
    dfn['NASDAQ Ret (dev)'] = (df['NASDAQ'].pct_change() - df['NASDAQ'].pct_change().mean()).rolling(90).mean()
    dfn['10-Year Treasury (dev)'] = df['10-Year Treasury'] - df['10-Year Treasury'].rolling(250).mean()
    # 'VIX': Leave as is
    dfn['VIX'] = df['VIX']
    dfn['10Y-2Y Spread'] = df['10Y-2Y Spread']
    # Drop columns that are completely NaN
    dfn = dfn.dropna(axis=1, how='all')
    return dfn

df = load_fred.load_fred(data_dir=DATA_DIR)
df['GDP'] = df['GDP'].ffill()
df = df.dropna()
dfn = transform_series(df)


# In[ ]:


dfn.plot(subplots=True, figsize=(10, 10))


# In[ ]:


# Create the same plot as dfn.plot(subplots=True, figsize=(10, 10)), but with plotly
fig = px.line(dfn, facet_col="variable", facet_col_wrap=1)
fig.update_yaxes(matches=None)
fig.show()


# In[ ]:


import plotly.graph_objs as go 

trace = go.Scatter(x=list(dfn['10Y-2Y Spread'].index),
                   y=list(dfn['10Y-2Y Spread']))

data = [trace]
layout = dict(
    title='Time series with range slider and selectors',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)

fig = go.FigureWidget(data=data, layout=layout)
fig.show()


# In[ ]:


import plotly.graph_objs as go

# Sample data series names
series_names = ['High Yield Index OAS', '10Y-2Y Spread', 'VIX', 'CP - Treasury Spread, 3m', 'NASDAQ Ret (dev)', '10-Year Treasury (dev)']

# Assume dfn is your dataframe and has the series_names as columns
column = series_names[0]  # Start with the first series
dfn_nona = dfn.dropna()
trace = go.Scatter(x=dfn_nona.index, y=dfn_nona[column], name=column)

data = [trace]
layout = dict(
    title='Time series with range slider and selectors',
    autosize=True,  # Change to False to use custom size
    # width=1800,      # Adjust width as needed
    # height=800,      # Adjust height as needed
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(visible=True),
        type='date'
    ),
    updatemenus=[dict(
        type="buttons",
        direction="down",
        buttons=[dict(
            args=["y", [dfn_nona[name].values]],
            label=name,
            method="restyle"
        ) for name in series_names]
    )]
)

fig = go.FigureWidget(data=data, layout=layout)
fig.show()


# In[ ]:




