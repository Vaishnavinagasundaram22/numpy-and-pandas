#!/usr/bin/env python
# coding: utf-8

# # Random Numbers
# 
# ### Definition
# 
# Random numbers are numbers generated in an unpredictable or random way.
# 
# In NumPy, we use the `np.random` module to generate random numbers.
# 
# ### Example
# 
# For example, we can generate random numbers such as:
# 
# 25, 67, 12, 89, 45
# 
# Every time we run the program, different numbers may be generated.
# 
# ### Real-World Example
# 
# In a game, random numbers can be used to randomly select a reward or generate an opponent's position.
# 
# ### Business Example
# 
# A company can use random numbers to select customers for a survey or create sample data for testing.
# 
# ### AI/ML Example
# 
# In AI/ML, random numbers are commonly used for creating sample data, initializing model values, and testing algorithms.
# 
# ### Code Explanation
# 
# `np.random.rand(5)` generates 5 random decimal numbers between 0 and 1.
# 
# `print()` displays the generated random numbers.
# 
# ### Output Explanation
# 
# The output will contain 5 random decimal numbers between 0 and 1.

# In[1]:


import numpy as np

random_numbers = np.random.rand(5)

print("Random Numbers:", random_numbers)


# # Random Seed
# 
# ### Definition
# 
# Random seed is used to make randomly generated numbers the same every time we run the program.
# 
# In NumPy, we use `np.random.seed()` to set a starting point for random number generation.
# 
# ### Example
# 
# If we use the same seed value every time, NumPy will generate the same random numbers.
# 
# For example, `np.random.seed(10)` will give the same sequence of random numbers whenever the code is run.
# 
# ### Real-World Example
# 
# Suppose we are testing a game that uses random values. Using the same seed helps us reproduce the same situation again for testing.
# 
# ### Business Example
# 
# A company can use a random seed while creating sample data so that the same test data can be reproduced later.
# 
# ### AI/ML Example
# 
# In AI/ML, random seed is useful when splitting data, initializing values, or creating random samples.
# 
# It helps us get reproducible results while testing and comparing models.
# 
# ### Code Explanation
# 
# `np.random.seed(10)` sets the seed value to 10.
# 
# `np.random.rand(5)` generates 5 random decimal numbers.
# 
# Because the seed is fixed, running the code again will produce the same numbers.
# 
# ### Output Explanation
# 
# The same 5 random numbers will be generated every time this code is executed with the same seed.

# In[2]:


import numpy as np

np.random.seed(10)

random_numbers = np.random.rand(5)

print("Random Numbers:", random_numbers)


# # Random Integers
# 
# ### Definition
# 
# Random integers are whole numbers generated randomly within a specified range.
# 
# In NumPy, we use `np.random.randint()` to generate random integers.
# 
# ### Example
# 
# If we want to generate a random number between 1 and 10, we can use:
# 
# `np.random.randint(1, 11)`
# 
# Here, 1 is included and 11 is excluded.
# 
# So the generated number can be from 1 to 10.
# 
# ### Real-World Example
# 
# In a game, random integers can be used to generate a dice number or select a random player number.
# 
# ### Business Example
# 
# A company can use random integers to generate sample customer IDs or randomly select customers for testing.
# 
# ### AI/ML Example
# 
# In AI/ML, random integers can be used to create sample datasets, randomly select records, or generate test values.
# 
# ### Code Explanation
# 
# `np.random.randint(1, 11, 5)` generates 5 random integers from 1 to 10.
# 
# The first value `1` is the starting value.
# 
# The second value `11` is the ending value, but it is not included.
# 
# The third value `5` tells NumPy to generate 5 numbers.
# 
# ### Output Explanation
# 
# The output will contain 5 random whole numbers between 1 and 10.

# In[3]:


import numpy as np

random_numbers = np.random.randint(1, 11, 5)

print("Random Integers:", random_numbers)


# # Random Choice
# 
# ### Definition
# 
# Random choice is used to randomly select one or more values from an array.
# 
# In NumPy, we use `np.random.choice()` for random selection.
# 
# ### Example
# 
# Suppose we have:
# 
# Apple, Banana, Orange, Mango
# 
# Using `np.random.choice()`, we can randomly select one fruit from these values.
# 
# ### Real-World Example
# 
# In a game, random choice can be used to randomly select a player, reward, or question.
# 
# ### Business Example
# 
# A company can randomly select customers from a customer list for a survey.
# 
# ### AI/ML Example
# 
# In AI/ML, random choice can be used to randomly select samples from a dataset for testing or experimentation.
# 
# ### Code Explanation
# 
# `fruits` contains the available choices.
# 
# `np.random.choice(fruits)` randomly selects one value from the array.
# 
# `print()` displays the selected value.
# 
# ### Output Explanation
# 
# The output will show one randomly selected fruit from the given array.

# In[4]:


import numpy as np

fruits = np.array(["Apple", "Banana", "Orange", "Mango"])

selected_fruit = np.random.choice(fruits)

print("Selected Fruit:", selected_fruit)


# # Shuffle
# 
# ### Definition
# 
# Shuffle is used to randomly change the order of elements in an array.
# 
# In NumPy, we use `np.random.shuffle()` to shuffle the values.
# 
# ### Example
# 
# Original values:
# 
# [10, 20, 30, 40, 50]
# 
# After shuffling, the order may become:
# 
# [30, 10, 50, 20, 40]
# 
# The values remain the same, but their order changes.
# 
# ### Real-World Example
# 
# In a game, we can shuffle a list of players before deciding the playing order.
# 
# ### Business Example
# 
# A company can shuffle customer records before selecting a random sample for a survey.
# 
# ### AI/ML Example
# 
# In AI/ML, shuffling data is useful before training a model so that the data is not always in the same order.
# 
# ### Code Explanation
# 
# `np.array()` creates an array.
# 
# `np.random.shuffle(values)` randomly changes the order of the values.
# 
# The shuffle operation changes the original array.
# 
# ### Output Explanation
# 
# The output will show the same values in a different random order.

# In[6]:


import numpy as np

values = np.array([10, 20, 30, 40, 50])

print("Before Shuffle:", values)

np.random.shuffle(values)

print("After Shuffle:", values)


# # Permutation
# 
# ### Definition
# 
# Permutation is used to create a randomly rearranged copy of an array.
# 
# In NumPy, we use `np.random.permutation()`.
# 
# The main difference between `shuffle()` and `permutation()` is that `shuffle()` changes the original array, while `permutation()` returns a new rearranged array.
# 
# ### Example
# 
# Original values:
# 
# [10, 20, 30, 40, 50]
# 
# A permutation may be:
# 
# [30, 50, 10, 40, 20]
# 
# All the original values are present, but their order is changed.
# 
# ### Real-World Example
# 
# In a game, permutation can be used to create a random playing order without changing the original player list.
# 
# ### Business Example
# 
# A company can create a random order of customer records for testing or sampling.
# 
# ### AI/ML Example
# 
# In AI/ML, permutation can be used to randomly rearrange data before analysis or model testing.
# 
# ### Code Explanation
# 
# `np.array()` creates the original array.
# 
# `np.random.permutation(values)` creates a randomly rearranged copy of the array.
# 
# The original array remains unchanged.
# 
# ### Output Explanation
# 
# The original array stays the same, while the permutation contains the same values in a different random order.

# In[7]:


import numpy as np

values = np.array([10, 20, 30, 40, 50])

permuted_values = np.random.permutation(values)

print("Original Values:", values)
print("Permuted Values:", permuted_values)


# # Random Distributions
# 
# ### Definition
# 
# A random distribution describes how randomly generated values are spread or distributed.
# 
# NumPy provides different random distribution functions to generate data that follows a particular pattern.
# 
# One commonly used distribution is the Normal Distribution.
# 
# ### Example
# 
# A normal distribution is a distribution where most values are around the average, and fewer values appear far away from the average.
# 
# For example, people's heights may roughly follow a normal distribution.
# 
# ### Real-World Example
# 
# Heights, test scores, and measurement errors can often be represented using a normal distribution.
# 
# ### Business Example
# 
# A company can use a normal distribution to create sample customer data or analyze values such as delivery times and product measurements.
# 
# ### AI/ML Example
# 
# Random distributions are useful in AI/ML for creating sample data, simulations, testing algorithms, and understanding data patterns.
# 
# ### Code Explanation
# 
# `np.random.normal(50, 10, 10)` generates 10 random values using a normal distribution.
# 
# `50` is the mean.
# 
# `10` is the standard deviation.
# 
# The last `10` tells NumPy to generate 10 values.
# 
# ### Output Explanation
# 
# The output will contain 10 random values that are generally distributed around the mean value 50.

# In[8]:


import numpy as np

random_values = np.random.normal(50, 10, 10)

print("Random Values:", random_values)


# In[ ]:




