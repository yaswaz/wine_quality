#!/usr/bin/env python
# coding: utf-8

# # Plotting with Matplotlib
# Use Matplotlib to create bar charts that visualize the conclusions you made with groupby and query.

# In[3]:


# Import necessary packages and load `winequality_edited.csv`
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('winequality_edited.csv')
df.head()


# ### #1: Do wines with higher alcoholic content receive better ratings?
# Create a bar chart with one bar for low alcohol and one bar for high alcohol wine samples. This first one is filled out for you.

# In[4]:


# Use query to select each group and get its mean quality
median = df['alcohol'].median()
low = df.query('alcohol < {}'.format(median))
high = df.query('alcohol >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()


# In[5]:


# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating');


# ### #2: Do sweeter wines receive higher ratings?
# Create a bar chart with one bar for low residual sugar and one bar for high residual sugar wine samples.

# In[6]:


# Use query to select each group and get its mean quality
median = df['residual_sugar'].median()
low_sugar = df.query('residual_sugar < 3.0')
high_sugar = df.query('residual_sugar >= 3.0')

low_mean = low_sugar['quality'].mean()
high_mean = high_sugar['quality'].mean()


# In[7]:


# Create a bar chart with proper labels
# Create a bar chart with proper labels
locations = [1, 2]
heights = [low_mean, high_mean]
labels = ['low_sugar', 'high_sugar']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Sweetness')
plt.xlabel('Residual Sugar Content')
plt.ylabel('Average Quality Rating');


# ### #3: What level of acidity receives the highest average rating?
# Create a bar chart with a bar for each of the four acidity levels.

# In[8]:


# Use groupby to get the mean quality for each acidity level
df.describe().pH

bin_edges = [2.72, 3.11, 3.21, 3.32, 4.01]
bin_names =['high', 'mod_high', 'moderate', 'low']
df['acidity_levels'] = pd.cut(df['pH'], bin_edges, labels=bin_names)
acidity_level_means = df.groupby('acidity_levels').mean().quality
print(acidity_level_means)


# In[9]:


# Create a bar chart with proper labels
locations = [4, 3, 2, 1]
heights = acidity_level_means
labels = ['low', 'moderate', 'mod_high', 'high']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Acidity Levels')
plt.xlabel('Acidity Levels')
plt.ylabel('Average Quality Rating');


# ### Bonus: Create a line plot for the data in #3
# You can use pyplot's [plot](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot) function for this.

# In[10]:


# Create a bar chart with proper labels

locations = [4, 3, 2, 1]
heights = acidity_level_means
labels = ['low', 'moderate', 'mod_high', 'high']
plt.plot(locations, heights)
plt.title('Average Quality Ratings by Acidity Levels')
plt.xlabel('Acidity Levels')
plt.ylabel('Average Quality Rating');


# Compare this with the bar chart. How might showing this visual instead of the bar chart affect someone's conclusion about this data?



# ### Create arrays for red bar heights white bar heights
# Remember, there's a bar for each combination of color and quality rating. Each bar's height is based on the proportion of samples of that color with that quality rating.
# 1. Red bar proportions = counts for each quality rating / total # of red samples
# 2. White bar proportions = counts for each quality rating / total # of white samples

# In[11]:


# get counts for each rating and color
color_counts = wine_df.groupby(['color', 'quality']).count()['pH']
color_counts


# In[12]:


# get total counts for each color
color_totals = wine_df.groupby('color').count()['pH']
color_totals


# In[13]:


# get proportions by dividing red rating counts by total # of red samples
red_proportions = color_counts['red'] / color_totals['red']
red_proportions


# In[14]:


# get proportions by dividing white rating counts by total # of white samples
white_proportions = color_counts['white'] / color_totals['white']
white_proportions


# ### Plot proportions on a bar chart
# Set the x coordinate location for each rating group and and width of each bar.

# In[15]:


ind = np.arange(len(red_proportions))  # the x locations for the groups
width = 0.35       # the width of the bars


# Now let’s create the plot.

# In[16]:


# plot bars
red_bars = plt.bar(ind, red_proportions, width, color='r', alpha=.7, label='Red Wine')
white_bars = plt.bar(ind + width, white_proportions, width, color='w', alpha=.7, label='White Wine')

# title and labels
plt.ylabel('Proportion')
plt.xlabel('Quality')
plt.title('Proportion by Wine Color and Quality')
locations = ind + width / 2  # xtick locations
labels = ['3', '4', '5', '6', '7', '8', '9']  # xtick labels
plt.xticks(locations, labels)

# legend
plt.legend()


# Oh, that didn't work because we're missing a red wine value for a the 9 rating. Even though this number is a 0, we need it for our plot. Run the last two cells after running the cell below.

# In[17]:


red_proportions['9'] = 0
red_proportions
