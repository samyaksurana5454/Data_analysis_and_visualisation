#!/usr/bin/env python
# coding: utf-8

# In[4]:


#this will install geopy l
import geopy


# In[5]:


get_ipython().system('pip install geopy')


# In[8]:


import pandas as pd
import numpy as np
from IPython.display import display
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt



# In[7]:


get_ipython().system('pip install plotly')


# In[12]:


#importing the dataset
data = pd.read_csv("final-car-data.csv")
data = data.dropna()
display(data.head())


# In[ ]:





# In[13]:


display(data.info())
data.Make.value_counts().reset_index()


# In[14]:


#barplot of car model vs year of manufacture
plt.figure(figsize=(6,4))
g = sns.barplot(x="Model", y="Year", hue="Model",
                data=data, palette="muted",)
g.set_ylim(2014, 2024)
plt.title("Model vs year of manufacturing of the vehicle")


# In[15]:


sns.scatterplot(data=data, x="Model", y="Range (KM)", hue="EV battery( percentage remaining)", size="EV battery( percentage remaining)",
    sizes=(20, 200),)
plt.title("Charge remaining Vs distance that can be covered by different car models")


# In[16]:


plt.plot(data['Range (KM)'], data['EV battery( percentage remaining)'], color='red', marker='o')
plt.title('Range (KM) vs Ev battery remaining percentage', fontsize=14)
plt.xlabel('Range (KM)', fontsize=14)
plt.ylabel('Ev battery remaining percentage', fontsize=14)
plt.grid(False)
plt.show()


# from the line graph above it is observed that charge remaining percentage increases with the distance range.

# In[17]:


#scatterplot of vehicles Charging state
sns.relplot(
    data=data, x="Charge State", y="EV battery( percentage remaining)",
    col="Plugged In", hue="Make", style="Make",
    kind="scatter"
)


# In[18]:


#counting number of cars that are plugged in and charge
sns.catplot(data= data, x="Plugged In", y="EV battery( percentage remaining)", jitter=False)


# In[19]:


sns.stripplot(data=data, x="Odometer(distance travelled)", y="Year")


# # geogrphical mapping of the coordinates
dataset = data.toPandas()
# In[20]:


data[["Latitude(location)", "Longitude(location)"]] = data[["Latitude(location)", "Longitude(location)"]].apply(pd.to_numeric)


# In[21]:


fig = px.scatter_mapbox(data, lat = "Latitude(location)", lon = "Longitude(location)", 
                        hover_name = "Charge State", 
                        hover_data = [ "Range (KM)", "Model"],
                        color = "EV battery( percentage remaining)", 
                        zoom = 6, height = 600)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# From the map we can see cars running on low charge and yet they are not plugged in nor charging thus we can conclude that there are no enough charging points

# In[ ]:




