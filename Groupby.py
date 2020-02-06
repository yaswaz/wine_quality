#!/usr/bin/env python
# coding: utf-8

# # Drawing Conclusions Using Groupby

# Use `winequality_edited.csv`. You should've created this data file in the previous section: *Appending Data (cont.)*.

# In[1]:


# Load dataset
import pandas as pd
df = pd.read_csv('winequality_edited.csv')
df.head()


# ### Is a certain type of wine associated with higher quality?

# In[2]:


# Find the mean quality of each wine type (red and white) with groupby
df.groupby('color').mean().quality


# ### What level of acidity receives the highest average rating?

# In[3]:


# View the min, 25%, 50%, 75%, max pH values with Pandas describe
df.describe().pH


# In[4]:


# Bin edges that will be used to "cut" the data into groups
bin_edges = [2.72, 3.11, 3.21, 3.32, 4.01] # Fill in this list with five values you just found


# In[5]:


# Labels for the four acidity level groups
bin_names = ['high', 'mod_high', 'moderate', 'low'] # Name each acidity level category


# In[6]:


# Creates acidity_levels column
df['acidity_levels'] = pd.cut(df['pH'], bin_edges, labels=bin_names)

# Checks for successful creation of this column
df.head()


# In[8]:


# Find the mean quality of each acidity level with groupby
df.groupby('acidity_levels').mean().quality


# In[ ]:


# Save changes for the next section
df.to_csv('winequality_edited.csv', index=False)


# In[9]:


# Do wines with higher Alcoholic content receive higher ratings?


# In[10]:


# get the median amount of alcohol content
df.median().alcohol


# In[11]:


# select samples with alcohol content less than the median
low_alcohol = df.query('alcohol < 10.30')

# select samples with alcohol content greater than or equal to the median
high_alcohol = df.query('alcohol >= 10.30')

# ensure these queries included each sample exactly once
num_samples = df.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count()


# In[12]:


df.query('alcohol < 10.30').mean().quality


# In[13]:


# Do sweeter wines receive better ratings


# In[14]:


# get the median amount of residual sugar
df.median().residual_sugar


# In[15]:


# select samples with residual sugar less than the median
low_sugar = df.query('residual_sugar < 3.0')

# select samples with residual sugar greater than or equal to the median
high_sugar = df.query('residual_sugar >= 3.0')

# ensure these queries included each sample exactly once
num_samples == low_sugar['quality'].count() + high_sugar['quality'].count()


# In[16]:


# get mean quality rating for the low sugar and high sugar groups
low_sugar.quality.mean(), high_sugar.quality.mean