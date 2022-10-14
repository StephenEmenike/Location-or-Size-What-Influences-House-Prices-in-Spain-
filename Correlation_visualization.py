#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


# In[28]:


df = pd.read_csv("/Users/steve/Desktop/Analytics/rent_spain_scraping_dataset_main_transformed.csv")


# In[29]:


df.info()


# In[30]:


df["province"].value_counts().head(10)


# In[31]:


#Summary statistics for price_usd and Square_meters
df[["Square_meters", "price_usd"]].describe()


# In[32]:


#Plot a Histogram of Square_meters 
plt.hist(df['Square_meters'])
plt.xlabel("Area[sq meters]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Sizes");


# In[33]:


#Horizontal boxplot of Square_meters
plt.boxplot(df["Square_meters"], vert=False)
plt.xlabel("Area[sq meters]")
plt.title("Distribution of Home Sites");


# In[57]:


#Histogram of price_usd 
plt.hist(df["price_usd"])
plt.xlabel("Price [USD]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Prices");


# In[58]:


plt.boxplot(df["price_usd"], vert=False)
plt.xlabel("Price USD")
plt.title("Distribution of Home Prices");


# In[36]:


#Create a series of mean_rental_price_by_province
mean_rental_price_by_province = df.groupby("province")["price_usd"].mean().sort_values(ascending=False)
mean_rental_price_by_province


# In[42]:


#Bar Chart of mean_rental_price_by_province
mean_rental_price_by_province.plot(
    kind="bar",
    xlabel="Province",
    ylabel="Price [USD]",
    title="Mean Rental Price by State"
);


# In[43]:


# Create a new column in df called "price_per_m2"
df["price_per_m2"] = df["price_usd"] / df["Square_meters"]
df.head()


# In[44]:


#Bar chart of "Mean Rental Price per M^2 by province"
(
    df
    .groupby("province")
    ["price_per_m2"].mean()
    .sort_values(ascending=False)
    .plot(
        kind="bar",
        xlabel="Province",
        ylabel="Mean Rental Price per M^2[USD]",
        title="Mean Rental Price per M^2 by Province"
    )
);


# In[45]:


#Scatter plot of rental price "price_usd" as a function of apartment size "Square_meters"


# In[47]:


plt.scatter(x=df["Square_meters"], y=df["price_usd"])
plt.xlabel("Area[sq meters]")
plt.ylabel("Price [USD]")
plt.title("Price vs Area");


# In[50]:


#calculate the Pearson correlation coefficient for "Square_meters" and "price_usd"

p_correlation = df["Square_meters"].corr(df["price_usd"])
print(p_correlation)


# In[51]:


#Create a new DataFrame named df_madrid. It should include all the houses from df that are in the state of Madrid.

df_madrid = df[df["province"] == "Madrid"]
df_madrid.head()


# In[52]:


#Create a scatter plot that shows price vs area in madrid

plt.scatter(x=df_madrid["Square_meters"], y=df_madrid["price_usd"])
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]")
plt.title("Madrid: Price Vs Area");


# In[54]:


#Calculate the Pearson correlation coefficient for "Square_meters" and "price_usd" in madrid

p_correlation = df_madrid["Square_meters"].corr(df_madrid["price_usd"])
print(p_correlation)


# In[55]:


# Subset `df` to include only observations from `"Barcelona"`
df_barcelona = df[df["province"] == "Barcelona"]

# Create a scatter plot price vs area
plt.scatter(x=df_barcelona["Square_meters"], y=df_barcelona["price_usd"])
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]")
plt.title("Barcelona: Price Vs Area");

p_correlation = df_barcelona["Square_meters"].corr(df_barcelona["price_usd"])
print(p_correlation)


# In[ ]:




