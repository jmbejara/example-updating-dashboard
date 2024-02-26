#!/usr/bin/env python
# coding: utf-8

# # PCA Index Interactive Visualization Examples

# In[ ]:


import plotly.express as px

import config
import load_fred
import pca_index

DATA_DIR = config.DATA_DIR


# In[ ]:


df = load_fred.load_fred(data_dir=DATA_DIR)
dfn = pca_index.transform_series(df)


# In[ ]:


## Visualize Principal Component 1
pc1, loadings = pca_index.pca(dfn, module="scikitlearn")
pc1.plot();


# In[ ]:


# Simple version
fig = px.line(pc1)
fig.show()


# In[ ]:


# Using slider and quick views
pca_index.pc1_line_plot(pc1)


# In[ ]:


## Visualize normalized and raw series
dfn.plot(subplots=True, figsize=(10, 10));


# In[ ]:


fig = px.line(dfn, facet_col="variable", facet_col_wrap=1)
fig.update_yaxes(matches=None)
fig.show()


# In[ ]:


pca_index.plot_unnormalized_series(df)


# In[ ]:


pca_index.plot_normalized_series(dfn)


# In[ ]:




