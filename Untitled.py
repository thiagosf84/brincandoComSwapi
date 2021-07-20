#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
import json


# In[11]:


url = 'http://swapi.dev/api/people'
df_final = ""
for d in range(1,10):
    pg = f'{url}?pg={d}'
    res = requests.get(pg)
    res = json.loads(res.content)
    df = pd.DataFrame.from_dict(res['results'])
    if d == 1:
        df_final = df
    else:
        df_final.append(df)


# In[14]:


df.drop(['homeworld', 'films', 'species', 'vehicles','starships', 'created', 'edited', 'url'], axis = 1, inplace = True)


# In[17]:


df.head(10)

