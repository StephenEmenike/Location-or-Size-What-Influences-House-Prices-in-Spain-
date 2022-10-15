#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings

import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import VimeoVideo
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

warnings.simplefilter(action="ignore", category=FutureWarning)


# In[2]:


#Load CSV data file

df1 = pd.read_csv("/Users/steve/Desktop/Analytics/rent_spain_scraping_dataset.csv")


# In[3]:


df1.head()


# In[4]:


#Drop NaN values

df1.dropna(inplace=True)


# In[5]:


df1.info()


# In[6]:


#drop Columns

df1.drop(columns=["Unnamed: 0", "titulo", "total inmuebles/comunidad"], inplace=True)
df1.head()


# In[7]:


df1.shape


# In[8]:


df1.info()


# In[9]:


#Drop rows with strings in "mertos" column and convert "metros" to float 

df1 = df1[df1["metros"].str.contains("ascen") == False]
df1["metros"] = (df1["metros"].astype(float))


# In[10]:


#Rename column names to English translation and drop old columns
df1["Neighborhood"] = (df1["comunidad autonoma"])
df1["price_usd"] = (df1["precio"])
df1["province"] = (df1["provincia"])
df1["Number_of_rooms"] = (df1["habitaciones"])
df1["Square_meters"] = (df1["metros"])
df1.drop(columns=["provincia", "habitaciones", "metros", "precio", "comunidad autonoma"], inplace=True)
df1.head()


# In[11]:


df1.info()


# In[12]:


#Save df1
df1.to_csv("/Users/steve/Desktop/Analytics/rent_spain_scraping_dataset_main_retransformed.csv", index=False)


# In[ ]:




