#!/usr/bin/env python
# coding: utf-8

# In[1]:


import camelot


# In[2]:


import pandas as pd


# In[4]:


tables = camelot.read_pdf("Demographics_by_NTA.pdf", flavor="stream", pages="2-8")
tables


# In[5]:


tables[0].df


# In[10]:


df = pd.concat([
    tables[0].df,
    tables[1].df,
    tables[2].df,
    tables[3].df,
    tables[4].df,
    tables[5].df,
    tables[6].df,
    tables[7].df,
    tables[8].df,
    tables[9].df
], ignore_index=True)
df


# In[14]:


#Change the columns
df = df.rename(columns={
    0: 'Neighborhood_Name',
    1: 'NTA_Code',
    2: 'Boro_Name',
    3: 'Boro_CD',
    4: 'Total_pop',
    5: 'Num_65_over',
    6: 'Per_65_over',
    7: 'Per_65_over_poverty',
    8: 'Per_Hispanic_Latino',
    9: 'Per_White',
    10: 'Per_Black',
    11: 'Per_Asian',
    12: 'Per_Other'
})
df = df[df['Neighborhood_Name'] != 'Neighborhood_Name']
df


# In[15]:


#drop any rows that have unnecessary values in the rebounds columns
df = df[df.Total_pop != "Total"]


# In[16]:


df = df[df.Boro_Name != "Boro"]


# In[17]:


df = df[df.NTA_Code != "NTA Code"]


# In[19]:


df = df[df.Boro_Name != "Name"]
df = df[df.Total_pop != "n"]
df = df[df.Num_65_over != "years"]


# In[23]:


df = df[df.Per_Hispanic_Latino != "Latino"]
df = df[df.Per_Asian != "% Race/Ethnicity,"]


# In[24]:


df


# In[25]:


df.to_csv('Demographic.csv', index=False)


# In[ ]:




