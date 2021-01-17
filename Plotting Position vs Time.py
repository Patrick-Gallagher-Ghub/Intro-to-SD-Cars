#!/usr/bin/env python
# coding: utf-8

# # Plotting Position vs Time
# In this notebook you will plot a position vs time graph of the data you just saw.
# 
# First, I will demonstrate such a plot by following these steps:
# 
# 1. Importing `pyplot`, Python's most popular plotting library.
# 2. Storing data to be plotted in variables named `X` and `Y`
# 3. Creating a scatter plot of this data using pyplot's `scatter()` function.
# 4. Adding a line connecting two data points using pyplot's `plot()` function.
# 4. Adding axis labels and a title to the graph.

# In[ ]:


# Step 1.
#  we import pyplot as plt so we can refer to the pyplot
#  succinctly. This is a standard convention for this library.

from matplotlib import pyplot as plt


# Initially, I only told you the mileage at 2:00 and 3:00. The data looked like this.
# 
# | Time | Odometer <br>(miles) |
# |:----:|:--------------------------------:|
# | 2:00 |                30                |
# | 3:00 |                80                |
# 
# I'd like to make a scatter plot of this data and I want my **horizontal** axis to show time and my **vertical** axis to show mileage.
# 
# In this notebook (and those that follow), we are going to use a capital `X` to store horizontal axis data and a capital `Y` to store vertical axis data. In this case:

# In[2]:


# Step 2.
#  get the data into variables called X and Y. This naming pattern
#  is a convention. You could use any variables you like.

X = [2,3]
Y = [30,80]


# In[3]:


# Step 3.
#  create a scatter plot using plt.scatter. Note that you NEED
#  to call plt.show() to actually see the plot. Forgetting to  
#  call plt.show() is a common source of problems for people 
#  new to this library

plt.scatter(X,Y)
plt.show()


# This isn't a very exciting scatter plot since it only has two data points. Let's add a line connecting these data points as well.

# In[4]:


# Step 4.
#  add lines connecting adjacent points

plt.scatter(X,Y)
plt.plot(X,Y)
plt.show()


# Let's add a title and labels to the X and Y axes 

# In[5]:


plt.scatter(X,Y)
plt.plot(X,Y)
plt.title("Position vs. Time on a Roadtrip")
plt.xlabel("Time (in hours)")
plt.ylabel("Odometer Reading (in miles)")
plt.show()


# ## Twenty minute resolution
# When looking at the odometer every *20* minutes, the data looks like this:
# 
# | Time | Odometer <br>(miles) |
# |:----:|:--------------------------------:|
# | 2:00 |                30                |
# | 2:20 |                40                |
# | 2:40 |                68                |
# | 3:00 |                80                |
# 
# But a better way to think about it for plotting is like this (note the difference in how time is represented):
# 
# | Time | Odometer <br>(miles) |
# |:----:|:--------------------------------:|
# | 2.000 |                30                |
# | 2.333 |                40                |
# | 2.667 |                68                |
# | 3.000 |                80                |
# 
# ### EXERCISE 1 - Make a position vs time graph of the data shown above with lines connecting adjacent dots.
# 
# Reproduce the demonstration from before using the data shown above.

# In[12]:


# TODO - your code for exercise 1 here
from matplotlib import pyplot as plt

X = [2,2.333,2.667,3]
Y = [30,40,68,80]

plt.scatter(X,Y)
plt.show(X,Y)

plt.scatter(X,Y)
plt.plot(X,Y)
plt.title("Position vs. Time on a Roadtrip")
plt.xlabel("Time (in hours)")
plt.ylabel("Odometer Reading (in miles)")
plt.show()


# #### Exercise 1 - Solution Check (full solution code at end of notebook)
# You'll know you're correct when you've generated a plot that looks something like the following:
# 
# ![](https://d17h27t6h515a5.cloudfront.net/topher/2017/December/5a2ee74f_vmc-l1-20-min-plot/vmc-l1-20-min-plot.png)
# 

# ### EXERCISE 2 - Reflect
# Look at the graph above and think about the following questions (we will talk about them more in the video that follows) 
# 
# 1. How can you tell which of these time intervals had the highest average speed (without looking at the actual data?)
# 
# 2. If the car stopped from 3:00 - 4:00 and you were to plot that data, what would the **slope** of that line look like? 

# In[15]:


# 

#

#

#  SOLUTION CODE BELOW

#

#

#

# Exercise 1 - Solution

X = [
    2.000,
    2.333,
    2.667,
    3.000
]

Y = [
    30,
    40,
    68,
    80
]

plt.scatter(X,Y)
plt.plot(X,Y)
plt.title("Position vs. Time on a Roadtrip")
plt.xlabel("Time (in hours)")
plt.ylabel("Odometer Reading (in miles)")
plt.show()


# In[ ]:




