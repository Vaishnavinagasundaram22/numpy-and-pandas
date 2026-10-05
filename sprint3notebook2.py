#!/usr/bin/env python
# coding: utf-8

# # Mean in NumPy
# 
# ### Definition
# 
# Mean means the average value of a set of numbers.
# 
# In NumPy, `np.mean()` is used to calculate the average of the values in an array.
# 
# ### Formula
# 
# Mean = Sum of all values / Number of values
# 
# ### Real-World Example
# 
# A teacher has marks of five students:
# 
# 60, 70, 80, 90, 100
# 
# The mean mark is:
# 
# (60 + 70 + 80 + 90 + 100) / 5 = 80
# 
# ### Business Example
# 
# A company can use mean to find the average sales, average salary, or average customer spending.
# 
# ### AI/ML Example
# 
# Mean is commonly used in data analysis and preprocessing to understand the central value of numerical data.
# 
# ### Code Explanation
# 
# `np.mean(marks)` calculates the average of all the values in the `marks` array.
# 
# ### Output Explanation
# 
# The average of the five marks is 80.0.

# In[1]:


import numpy as np

marks = np.array([60, 70, 80, 90, 100])

average = np.mean(marks)

print("Marks:", marks)
print("Mean:", average)


# # Median
# 
# ### Definition
# 
# Median is the middle value of a set of numbers after arranging the values in ascending order.
# 
# In NumPy, we use `np.median()` to find the median value.
# 
# ### Example
# 
# Values: 10, 20, 30, 40, 50
# 
# The middle value is 30.
# 
# So, Median = 30
# 
# If there are even number of values, the average of the two middle values is taken.
# 
# Example: 10, 20, 30, 40
# 
# Middle values are 20 and 30.
# 
# Median = (20 + 30) / 2 = 25
# 
# ### Real-World Example
# 
# Suppose five students scored:
# 
# 60, 70, 75, 80, 90
# 
# The middle score is 75, so the median mark is 75.
# 
# ### Business Example
# 
# A company can use median to find the typical customer spending amount.
# 
# Median is useful when some customers spend a very large amount and may affect the average.
# 
# ### AI/ML Example
# 
# In AI/ML, median can be used while understanding data and handling outliers.
# 
# For example, if most salaries are normal but one salary is extremely high, median can give a better idea of the typical salary.
# 
# ### Code Explanation
# 
# `np.array()` creates a NumPy array.
# 
# `np.median(values)` finds the middle value of the array.
# 
# `print()` displays the values and median.
# 
# ### Output Explanation
# 
# The output shows the given values and their median value.

# In[2]:


import numpy as np

values = np.array([60, 70, 75, 80, 90])

median_value = np.median(values)

print("Values:", values)
print("Median:", median_value)


# # Variance
# 
# ### Definition
# 
# Variance tells us how much the values in a dataset are spread out from the mean.
# 
# In NumPy, we use `np.var()` to calculate variance.
# 
# ### Example
# 
# Values: 10, 20, 30
# 
# Mean = 20
# 
# The values are different from the mean, so there is some variation in the data.
# 
# ### Real-World Example
# 
# Suppose the marks of students are:
# 
# 60, 70, 80, 90, 100
# 
# Variance helps us understand how much the marks are spread around the average mark.
# 
# ### Business Example
# 
# A company can use variance to understand how much monthly sales change from the average sales.
# 
# Low variance means the sales values are closer to the average.
# 
# High variance means the sales values are more spread out.
# 
# ### AI/ML Example
# 
# In AI/ML, variance helps us understand the spread of data.
# 
# It is also related to feature analysis and is useful when understanding how much a feature varies across different observations.
# 
# ### Code Explanation
# 
# `np.array()` creates a NumPy array.
# 
# `np.var(values)` calculates the variance of the values.
# 
# `print()` displays the values and variance.
# 
# ### Output Explanation
# 
# The output shows the given values and the calculated variance.

# In[3]:


import numpy as np

values = np.array([60, 70, 80, 90, 100])

variance = np.var(values)

print("Values:", values)
print("Variance:", variance)


# # Standard Deviation
# 
# ### Definition
# 
# Standard deviation tells us how much the values in a dataset are spread out from the mean.
# 
# In NumPy, we use `np.std()` to calculate standard deviation.
# 
# ### Simple Explanation
# 
# If the values are close to the mean, the standard deviation will be small.
# 
# If the values are far from the mean, the standard deviation will be large.
# 
# ### Example
# 
# Values: 10, 20, 30, 40, 50
# 
# Mean = 30
# 
# The standard deviation tells us how far these values are generally spread around 30.
# 
# ### Real-World Example
# 
# Suppose the marks of students are:
# 
# 70, 72, 71, 73, 74
# 
# The marks are close to each other, so the standard deviation is small.
# 
# ### Business Example
# 
# A company can use standard deviation to understand how much monthly sales vary from the average sales.
# 
# ### AI/ML Example
# 
# In AI/ML, standard deviation is used to understand the spread of a feature.
# 
# It is also commonly used in data preprocessing, especially in standardization.
# 
# ### Code Explanation
# 
# `np.array()` creates a NumPy array.
# 
# `np.std(values)` calculates the standard deviation.
# 
# `print()` displays the values and standard deviation.
# 
# ### Output Explanation
# 
# The output shows the given values and the calculated standard deviation.

# In[4]:


import numpy as np

values = np.array([10, 20, 30, 40, 50])

standard_deviation = np.std(values)

print("Values:", values)
print("Standard Deviation:", standard_deviation)


# # Minimum
# 
# ### Definition
# 
# Minimum means the smallest value present in a dataset.
# 
# In NumPy, we use `np.min()` to find the smallest value in an array.
# 
# ### Example
# 
# Values: 10, 25, 5, 40, 15
# 
# The smallest value is 5.
# 
# So, Minimum = 5
# 
# ### Real-World Example
# 
# Suppose the temperatures recorded during a week are:
# 
# 32, 35, 31, 34, 30
# 
# The minimum temperature is 30.
# 
# ### Business Example
# 
# A company can use minimum to find the lowest sales amount, lowest price, or lowest customer order value.
# 
# ### AI/ML Example
# 
# In AI/ML, minimum is used during data analysis to understand the smallest value of a feature.
# 
# For example, we can find the minimum age, salary, or number of purchases in a dataset.
# 
# ### Code Explanation
# 
# `np.array()` creates a NumPy array.
# 
# `np.min(values)` finds the smallest value in the array.
# 
# `print()` displays the values and minimum value.
# 
# ### Output Explanation
# 
# The output shows the given values and the smallest value, which is 5.

# In[5]:


import numpy as np

values = np.array([10, 25, 5, 40, 15])

minimum = np.min(values)

print("Values:", values)
print("Minimum:", minimum)


# # Maximum
# 
# ### Definition
# 
# Maximum means the largest value present in a dataset.
# 
# In NumPy, we use `np.max()` to find the largest value in an array.
# 
# ### Example
# 
# Values: 10, 25, 5, 40, 15
# 
# The largest value is 40.
# 
# So, Maximum = 40
# 
# ### Real-World Example
# 
# Suppose the temperatures recorded during a week are:
# 
# 32, 35, 31, 34, 30
# 
# The maximum temperature is 35.
# 
# ### Business Example
# 
# A company can use maximum to find the highest sales amount, highest price, or highest customer order value.
# 
# ### AI/ML Example
# 
# In AI/ML, maximum is used during data analysis to understand the largest value of a feature.
# 
# For example, we can find the maximum age, salary, or number of purchases in a dataset.
# 
# ### Code Explanation
# 
# `np.array()` creates a NumPy array.
# 
# `np.max(values)` finds the largest value in the array.
# 
# `print()` displays the values and maximum value.
# 
# ### Output Explanation
# 
# The output shows the given values and the largest value, which is 40.

# In[6]:


import numpy as np

values = np.array([10, 25, 5, 40, 15])

maximum = np.max(values)

print("Values:", values)
print("Maximum:", maximum)


# # Argmin
# 
# ### Definition
# 
# `argmin` is used to find the index position of the smallest value in an array.
# 
# In NumPy, we use `np.argmin()`.
# 
# ### Example
# 
# Values: 10, 25, 5, 40, 15
# 
# The smallest value is 5.
# 
# Its index position is 2.
# 
# Remember, Python indexing starts from 0.
# 
# So, `argmin = 2`.
# 
# ### Real-World Example
# 
# Suppose we have the prices of five products:
# 
# 100, 250, 80, 150, 200
# 
# The lowest price is 80, and its index position is 2.
# 
# ### Business Example
# 
# A company can use `argmin()` to find the position of the product with the lowest price or the month with the lowest sales.
# 
# ### AI/ML Example
# 
# In AI/ML, `argmin()` can be used to find the position of the smallest value in an array, such as the feature with the lowest value or the location of a minimum error.
# 
# ### Code Explanation
# 
# `np.array()` creates a NumPy array.
# 
# `np.argmin(values)` returns the index position of the smallest value.
# 
# `print()` displays the values and the index.
# 
# ### Output Explanation
# 
# The smallest value is 5, and it is present at index position 2.

# In[7]:


import numpy as np

values = np.array([10, 25, 5, 40, 15])

minimum_index = np.argmin(values)

print("Values:", values)
print("Index of Minimum Value:", minimum_index)


# # Argmax
# 
# ### Definition
# 
# `argmax` is used to find the index position of the largest value in an array.
# 
# In NumPy, we use `np.argmax()`.
# 
# ### Example
# 
# Values: 10, 25, 5, 40, 15
# 
# The largest value is 40.
# 
# Its index position is 3.
# 
# So, `argmax = 3`.
# 
# ### Real-World Example
# 
# Suppose the scores of five students are:
# 
# 70, 85, 60, 95, 75
# 
# The highest score is 95, and its index position is 3.
# 
# ### Business Example
# 
# A company can use `argmax()` to find the position of the month with the highest sales.
# 
# ### AI/ML Example
# 
# In AI/ML, `argmax()` is commonly used to find the position of the highest value.
# 
# For example, when a model gives probabilities for different classes, `argmax()` can be used to find the class with the highest probability.
# 
# ### Code Explanation
# 
# `np.array()` creates a NumPy array.
# 
# `np.argmax(values)` returns the index position of the largest value.
# 
# `print()` displays the values and the index.
# 
# ### Output Explanation
# 
# The largest value is 40, and it is present at index position 3.

# In[8]:


import numpy as np

values = np.array([10, 25, 5, 40, 15])

maximum_index = np.argmax(values)

print("Values:", values)
print("Index of Maximum Value:", maximum_index)


# # Percentile
# 
# ### Definition
# 
# Percentile tells us the value below which a certain percentage of the data falls.
# 
# In NumPy, we use `np.percentile()` to calculate a percentile.
# 
# For example, the 50th percentile is the same as the median.
# 
# ### Example
# 
# Values: 10, 20, 30, 40, 50
# 
# The 50th percentile is 30.
# 
# This means 50% of the data is below or equal to 30.
# 
# ### Real-World Example
# 
# Suppose we have the marks of students.
# 
# We can use the 90th percentile to understand the score below which about 90% of the students fall.
# 
# ### Business Example
# 
# A company can use percentiles to understand customer spending.
# 
# For example, the 90th percentile of customer spending tells us the spending level below which about 90% of customers fall.
# 
# ### AI/ML Example
# 
# In AI/ML, percentiles are useful for understanding data distribution and detecting unusually high or low values.
# 
# They can also be used when setting thresholds for data preprocessing.
# 
# ### Code Explanation
# 
# `np.array()` creates a NumPy array.
# 
# `np.percentile(values, 50)` calculates the 50th percentile.
# 
# The second argument `50` means we are finding the 50th percentile.
# 
# ### Output Explanation
# 
# The output will show 30 as the 50th percentile because 30 is the middle value of the given data.

# In[9]:


import numpy as np

values = np.array([10, 20, 30, 40, 50])

percentile_50 = np.percentile(values, 50)

print("Values:", values)
print("50th Percentile:", percentile_50)


# # Dot Product
# 
# ### Definition
# 
# Dot product is a mathematical operation that multiplies the corresponding values of two arrays and then adds all the results.
# 
# In NumPy, we can use `np.dot()` to calculate the dot product.
# 
# ### Example
# 
# Array 1: [2, 3, 4]
# 
# Array 2: [5, 6, 7]
# 
# Calculation:
# 
# (2 × 5) + (3 × 6) + (4 × 7)
# 
# = 10 + 18 + 28
# 
# = 56
# 
# So, the dot product is 56.
# 
# ### Real-World Example
# 
# Suppose a shop sells 2 pens, 3 books, and 4 bags.
# 
# Their prices are 5, 6, and 7.
# 
# Dot product can calculate the total amount:
# 
# (2 × 5) + (3 × 6) + (4 × 7) = 56
# 
# ### Business Example
# 
# Dot product can be used to calculate total sales using quantities and prices.
# 
# ### AI/ML Example
# 
# In AI/ML, dot product is an important operation used in machine learning calculations.
# 
# For example, a model can multiply input features with their weights and add the results to produce a value.
# 
# ### Code Explanation
# 
# `array1` and `array2` contain the values.
# 
# `np.dot(array1, array2)` multiplies the corresponding values and adds the results.
# 
# ### Output Explanation
# 
# The output will be 56 because:
# 
# (2 × 5) + (3 × 6) + (4 × 7) = 56

# In[10]:


import numpy as np

array1 = np.array([2, 3, 4])
array2 = np.array([5, 6, 7])

dot_product = np.dot(array1, array2)

print("Array 1:", array1)
print("Array 2:", array2)
print("Dot Product:", dot_product)


# # Matrix Multiplication
# 
# ### Definition
# 
# Matrix multiplication means multiplying two matrices and producing a new matrix as the result.
# 
# In NumPy, we can use `np.matmul()` or the `@` operator for matrix multiplication.
# 
# For matrix multiplication, the number of columns in the first matrix must be equal to the number of rows in the second matrix.
# 
# ### Example
# 
# Matrix A:
# 
# [1, 2]
# [3, 4]
# 
# Matrix B:
# 
# [5, 6]
# [7, 8]
# 
# The result is:
# 
# [19, 22]
# [43, 50]
# 
# ### Real-World Example
# 
# Matrix multiplication can be used in image processing, where images are represented using numerical matrices.
# 
# ### Business Example
# 
# Businesses can use matrix operations in recommendation systems and data analysis to calculate relationships between different data values.
# 
# ### AI/ML Example
# 
# Matrix multiplication is very important in AI/ML.
# 
# Neural networks use matrix multiplication to combine input values with weights and calculate outputs.
# 
# ### Code Explanation
# 
# `matrix_a` and `matrix_b` are two NumPy matrices.
# 
# `np.matmul(matrix_a, matrix_b)` performs matrix multiplication.
# 
# `print()` displays the matrices and the result.
# 
# ### Output Explanation
# 
# The result is a new matrix:
# 
# [19, 22]
# [43, 50]
# 
# This is obtained by multiplying the rows of the first matrix with the columns of the second matrix.

# In[11]:


import numpy as np

matrix_a = np.array([[1, 2],
                     [3, 4]])

matrix_b = np.array([[5, 6],
                     [7, 8]])

result = np.matmul(matrix_a, matrix_b)

print("Matrix A:")
print(matrix_a)

print("Matrix B:")
print(matrix_b)

print("Matrix Multiplication Result:")
print(result)


# # Transpose
# 
# ### Definition
# 
# Transpose is used to change the rows of a matrix into columns and the columns into rows.
# 
# In NumPy, we can use `.T` to find the transpose of an array.
# 
# ### Example
# 
# Original matrix:
# 
# [1, 2, 3]
# [4, 5, 6]
# 
# After transpose:
# 
# [1, 4]
# [2, 5]
# [3, 6]
# 
# So, the rows become columns.
# 
# ### Real-World Example
# 
# In a table of data, transpose can be used to change the arrangement of rows and columns when a different data format is needed.
# 
# ### Business Example
# 
# A company may use transpose while rearranging sales or customer data for analysis.
# 
# ### AI/ML Example
# 
# Transpose is commonly used in AI/ML mathematical operations, especially when changing the orientation of matrices during calculations.
# 
# ### Code Explanation
# 
# `np.array()` creates a 2-dimensional matrix.
# 
# `.T` changes the rows into columns and columns into rows.
# 
# `print()` displays the original matrix and its transpose.
# 
# ### Output Explanation
# 
# The original matrix has 2 rows and 3 columns.
# 
# After transpose, it has 3 rows and 2 columns.

# In[12]:


import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

transpose = matrix.T

print("Original Matrix:")
print(matrix)

print("Transpose:")
print(transpose)


# # Basic Linear Algebra Operations
# 
# ### Definition
# 
# Linear algebra is a branch of mathematics that works with vectors, matrices, and mathematical operations between them.
# 
# NumPy provides functions to perform basic linear algebra operations easily.
# 
# Some common operations are:
# 
# - Dot Product
# - Matrix Multiplication
# - Transpose
# - Matrix Inverse
# - Determinant
# 
# In this topic, we will see a simple example using matrix multiplication and determinant.
# 
# ### Real-World Example
# 
# Linear algebra is used in many areas such as image processing, computer graphics, data analysis, and recommendation systems.
# 
# ### Business Example
# 
# Businesses can use matrix operations to analyze customer data, product relationships, and recommendation systems.
# 
# ### AI/ML Example
# 
# Linear algebra is very important in AI/ML.
# 
# Machine learning models and neural networks use vectors and matrices for calculations between input data, weights, and outputs.
# 
# ### Code Explanation
# 
# `np.array()` creates a matrix.
# 
# `np.matmul()` performs matrix multiplication.
# 
# `np.linalg.det()` calculates the determinant of a matrix.
# 
# ### Output Explanation
# 
# The code displays the matrix multiplication result and the determinant of the matrix.
# 
# For the given matrix:
# 
# [1, 2]
# [3, 4]
# 
# the determinant is -2.

# In[13]:


import numpy as np

matrix_a = np.array([[1, 2],
                     [3, 4]])

matrix_b = np.array([[5, 6],
                     [7, 8]])

multiplication = np.matmul(matrix_a, matrix_b)
determinant = np.linalg.det(matrix_a)

print("Matrix Multiplication:")
print(multiplication)

print("Determinant of Matrix A:", determinant)


# In[ ]:




