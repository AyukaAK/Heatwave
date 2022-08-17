#!/usr/bin/env python
# coding: utf-8

# In[10]:


import camelot


# In[11]:


import pandas as pd


# In[12]:


tables = camelot.read_pdf("monthlyannualtemp.pdf", flavor="stream", pages="1-4")
tables


# In[13]:


tables[2].df


# In[16]:


df = pd.concat([
    tables[0].df,
    tables[1].df,
    tables[2].df,
    tables[3].df,
], ignore_index=True)
df


# In[17]:


#Change the columns
df = df.rename(columns={
    0: 'YEAR',
    1: 'JAN',
    2: 'FEB',
    3: 'MAR',
    4: 'APR',
    5: 'MAY',
    6: 'JUN',
    7: 'JUL',
    8: 'AUG',
    9: 'SEP',
    10: 'OCT',
    11: 'NOV',
    12: 'DEC',
    13: 'ANNUAL'
})
df = df[df['YEAR'] != 'YEAR']
df


# In[18]:


#drop any rows that have unnecessary values in the rebounds columns
df = df[df.MAR != "Average Monthly & Annual Temperatures at Central Park"]


# In[19]:


df = df[df.JUN != "Last Updated: 5/9/21"]


# In[20]:


df


# In[21]:


df.to_csv('Central_Park.csv', index=False)


# In[ ]:




