#!/usr/bin/env python
# coding: utf-8

# # head()
# 
# ### Definition
# 
# `head()` is a Pandas function used to view the first few rows of a DataFrame.
# 
# By default, `head()` displays the first 5 rows.
# 
# We can also give a number inside `head()` to display that many rows.
# 
# ### Simple Example
# 
# If a DataFrame has 10 student records, `head()` will show only the first 5 records.
# 
# For example:
# 
# `students.head(3)` shows the first 3 rows.
# 
# ### Real-World Example
# 
# A school may have thousands of student records. Instead of displaying all the records, we can use `head()` to quickly see the beginning of the data.
# 
# ### Business Example
# 
# A company may have thousands of customer records. `head()` helps us quickly check whether the data has been loaded correctly.
# 
# ### AI/ML Example
# 
# When we load a dataset for an AI/ML project, we can use `head()` to quickly check the first few rows and understand what the dataset looks like.
# 
# ### Code Explanation
# 
# `pd.DataFrame()` creates the student DataFrame.
# 
# `students.head()` displays the first 5 rows.
# 
# `students.head(3)` displays only the first 3 rows.
# 
# ### Output Explanation
# 
# The first `print()` displays the first 5 student records.
# 
# The second `print()` displays only the first 3 records.

# In[1]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik", "Divya", "Arun"],
    "Age": [24, 23, 25, 22, 24, 26],
    "Mark": [85, 78, 92, 81, 88, 75]
})

print(students.head())

print("\nFirst 3 rows:")
print(students.head(3))


# # tail()
# 
# ### Definition
# 
# `tail()` is a Pandas function used to view the last few rows of a DataFrame.
# 
# By default, `tail()` displays the last 5 rows.
# 
# We can also give a number inside `tail()` to display that many rows.
# 
# ### Simple Example
# 
# If a DataFrame has 10 student records, `students.tail()` shows the last 5 records.
# 
# For example:
# 
# `students.tail(3)` shows the last 3 rows.
# 
# ### Real-World Example
# 
# A school can use `tail()` to quickly check the last few student records in a large dataset.
# 
# ### Business Example
# 
# A company can use `tail()` to check the latest records at the end of a dataset and make sure the data was loaded correctly.
# 
# ### AI/ML Example
# 
# After loading a dataset for an AI/ML project, `tail()` can be used along with `head()` to inspect both the beginning and the end of the data.
# 
# ### Code Explanation
# 
# `pd.DataFrame()` creates the DataFrame.
# 
# `students.tail()` displays the last 5 rows.
# 
# `students.tail(3)` displays only the last 3 rows.
# 
# ### Output Explanation
# 
# The first output shows the last 5 student records.
# 
# The second output shows only the last 3 records.

# In[2]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik", "Divya", "Arun"],
    "Age": [24, 23, 25, 22, 24, 26],
    "Mark": [85, 78, 92, 81, 88, 75]
})

print(students.tail())

print("\nLast 3 rows:")
print(students.tail(3))


# # sample()
# 
# ### Definition
# 
# `sample()` is a Pandas function used to randomly select rows from a DataFrame.
# 
# By default, `sample()` returns one random row.
# 
# We can give a number inside `sample()` to select multiple random rows.
# 
# ### Simple Example
# 
# If a DataFrame has 10 student records:
# 
# `students.sample(3)`
# 
# will randomly select 3 students.
# 
# ### Real-World Example
# 
# A school can use `sample()` to randomly check a few student records from a large dataset.
# 
# ### Business Example
# 
# A company can randomly select customer records for checking or quality testing.
# 
# ### AI/ML Example
# 
# In AI/ML, `sample()` can be used to randomly inspect data or select a small sample from a large dataset for quick testing.
# 
# ### Code Explanation
# 
# `students.sample()` selects one random row.
# 
# `students.sample(3)` selects three random rows.
# 
# The selected rows can be different each time because the selection is random.
# 
# ### Output Explanation
# 
# The output displays randomly selected student records from the DataFrame.

# In[3]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik", "Divya", "Arun"],
    "Age": [24, 23, 25, 22, 24, 26],
    "Mark": [85, 78, 92, 81, 88, 75]
})

print("One random row:")
print(students.sample())

print("\nThree random rows:")
print(students.sample(3))


# # info()
# 
# ### Definition
# 
# `info()` is a Pandas function used to get a quick summary of a DataFrame.
# 
# It shows the number of rows, columns, column names, data types, and non-null values.
# 
# ### Simple Example
# 
# If we have a student DataFrame, `students.info()` helps us understand what type of data each column contains.
# 
# ### Real-World Example
# 
# A company may receive a customer dataset with thousands of records. Before working with the data, `info()` can be used to check the structure of the dataset.
# 
# ### Business Example
# 
# A business can use `info()` to check whether columns like Customer Name, Age, and Sales have missing values and whether their data types are correct.
# 
# ### AI/ML Example
# 
# Before building an ML model, we need to understand the dataset. `info()` helps us check the columns, data types, and missing values.
# 
# ### Code Explanation
# 
# `students.info()` displays the basic information about the DataFrame.
# 
# It shows:
# - Number of rows
# - Column names
# - Non-null values
# - Data types
# - Memory usage
# 
# ### Output Explanation
# 
# The output gives a summary of the DataFrame structure.
# 
# For example, `int64` means the column contains integer values, and `object` usually represents text data.

# In[4]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik", "Divya", "Arun"],
    "Age": [24, 23, 25, 22, 24, 26],
    "Mark": [85, 78, 92, 81, 88, 75]
})

students.info()


# # describe()
# 
# ### Definition
# 
# `describe()` is a Pandas function used to get a statistical summary of numerical columns in a DataFrame.
# 
# It gives values like count, mean, standard deviation, minimum, maximum, and percentiles.
# 
# ### Simple Example
# 
# If we have student marks, `students.describe()` helps us understand the marks quickly.
# 
# ### Real-World Example
# 
# A school can use `describe()` to understand the overall performance of students.
# 
# ### Business Example
# 
# A company can use it to summarize values such as sales, salary, or customer age.
# 
# ### AI/ML Example
# 
# Before training an ML model, `describe()` can help us understand the numerical data and identify unusual values.
# 
# ### Code Explanation
# 
# `students.describe()` calculates a statistical summary for the numerical columns.
# 
# The output includes:
# 
# - `count` → number of values
# - `mean` → average value
# - `std` → standard deviation
# - `min` → minimum value
# - `25%` → first quartile
# - `50%` → median
# - `75%` → third quartile
# - `max` → maximum value
# 
# ### Output Explanation
# 
# The output gives a quick statistical overview of the Age and Mark columns.

# In[5]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik", "Divya", "Arun"],
    "Age": [24, 23, 25, 22, 24, 26],
    "Mark": [85, 78, 92, 81, 88, 75]
})

print(students.describe())


# # shape
# 
# ### Definition
# 
# `shape` is a Pandas property used to find the number of rows and columns in a DataFrame.
# 
# It returns the result in this format:
# 
# `(rows, columns)`
# 
# ### Simple Example
# 
# If a DataFrame has 6 rows and 3 columns:
# 
# `students.shape`
# 
# will return:
# 
# `(6, 3)`
# 
# ### Real-World Example
# 
# If we receive a large customer dataset, `shape` helps us quickly know how many records and columns are available.
# 
# ### Business Example
# 
# A company can use `shape` to check the size of a sales dataset before starting analysis.
# 
# ### AI/ML Example
# 
# Before training an ML model, we can use `shape` to understand how many data records and features are available.
# 
# ### Code Explanation
# 
# `students.shape` gives the number of rows and columns.
# 
# `students.shape[0]` gives the number of rows.
# 
# `students.shape[1]` gives the number of columns.
# 
# ### Output Explanation
# 
# The output `(6, 3)` means the DataFrame contains 6 rows and 3 columns.

# In[6]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik", "Divya", "Arun"],
    "Age": [24, 23, 25, 22, 24, 26],
    "Mark": [85, 78, 92, 81, 88, 75]
})

print("Shape:", students.shape)
print("Number of rows:", students.shape[0])
print("Number of columns:", students.shape[1])


# # columns
# 
# ### Definition
# 
# `columns` is a Pandas property used to get the names of all columns in a DataFrame.
# 
# ### Simple Example
# 
# If a DataFrame contains `Name`, `Age`, and `Mark`, then:
# 
# `students.columns`
# 
# will show these column names.
# 
# ### Real-World Example
# 
# When working with a large dataset, we can use `columns` to quickly see what information is available.
# 
# ### Business Example
# 
# A company can check the column names of a customer dataset to know whether it contains details like Customer_ID, Age, Sales, and Location.
# 
# ### AI/ML Example
# 
# In AI/ML, `columns` helps us identify the available features and decide which columns can be used for model training.
# 
# ### Code Explanation
# 
# `students.columns` displays all column names in the DataFrame.
# 
# We can also use `list(students.columns)` to convert the column names into a normal Python list.
# 
# ### Output Explanation
# 
# The output displays the names of the columns present in the DataFrame.

# In[7]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik", "Divya", "Arun"],
    "Age": [24, 23, 25, 22, 24, 26],
    "Mark": [85, 78, 92, 81, 88, 75]
})

print("Column names:")
print(students.columns)

print("\nColumn names as a list:")
print(list(students.columns))


# # dtypes
# 
# ### Definition
# 
# `dtypes` is a Pandas property used to find the data type of each column in a DataFrame.
# 
# ### Simple Example
# 
# If a DataFrame has:
# 
# - Name → text
# - Age → integer
# - Mark → integer
# 
# `students.dtypes` shows the data type of each column.
# 
# ### Real-World Example
# 
# When we receive a dataset, we can use `dtypes` to check whether each column contains the correct type of data.
# 
# ### Business Example
# 
# A company can check whether Age and Sales are stored as numbers and Customer Name is stored as text.
# 
# ### AI/ML Example
# 
# In AI/ML, checking data types is important before preprocessing and model training. Numerical columns and text columns may need different processing.
# 
# ### Code Explanation
# 
# `students.dtypes` displays the data type of every column.
# 
# `int64` represents integer values.
# 
# `object` is commonly used for text values.
# 
# ### Output Explanation
# 
# The output shows the data type for each column in the DataFrame.

# In[8]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik", "Divya", "Arun"],
    "Age": [24, 23, 25, 22, 24, 26],
    "Mark": [85, 78, 92, 81, 88, 75]
})

print(students.dtypes)


# # memory_usage()
# 
# ### Definition
# 
# `memory_usage()` is a Pandas function used to check how much memory each column of a DataFrame is using.
# 
# ### Simple Example
# 
# If we have a DataFrame with Name, Age, and Mark columns, `memory_usage()` shows the memory used by each column.
# 
# ### Real-World Example
# 
# When working with a very large dataset, checking memory usage helps us understand how much computer memory the DataFrame needs.
# 
# ### Business Example
# 
# A company working with millions of customer records can use `memory_usage()` to identify columns that are using more memory.
# 
# ### AI/ML Example
# 
# In AI/ML projects, datasets can contain a large number of rows and columns. Checking memory usage helps us optimize the dataset before model training.
# 
# ### Code Explanation
# 
# `students.memory_usage()` shows the memory used by each column.
# 
# `index=True` is used by default, so the memory used by the DataFrame index is also displayed.
# 
# `memory_usage(deep=True)` gives a more accurate memory usage for object or text columns.
# 
# ### Output Explanation
# 
# The output shows the memory usage of the index and each column in bytes.

# In[9]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik", "Divya", "Arun"],
    "Age": [24, 23, 25, 22, 24, 26],
    "Mark": [85, 78, 92, 81, 88, 75]
})

print("Memory usage:")
print(students.memory_usage())

print("\nDetailed memory usage:")
print(students.memory_usage(deep=True))


# # nunique()
# 
# ### Definition
# 
# `nunique()` is a Pandas function used to find the number of unique values in each column.
# 
# Unique means values that are different from each other.
# 
# ### Simple Example
# 
# If a column contains:
# 
# Preethi, Rahul, Preethi, Anu
# 
# there are 3 unique names:
# 
# Preethi, Rahul, Anu
# 
# So, `nunique()` returns 3.
# 
# ### Real-World Example
# 
# A company can use `nunique()` to find how many different cities or products are present in a dataset.
# 
# ### Business Example
# 
# A business can check how many different customers, products, or locations are available in its data.
# 
# ### AI/ML Example
# 
# In AI/ML, `nunique()` helps us understand categorical columns and find how many different categories are present.
# 
# ### Code Explanation
# 
# `students.nunique()` finds the number of unique values in every column.
# 
# By default, missing values are not counted.
# 
# ### Output Explanation
# 
# The output shows the number of different values present in each column.

# In[10]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Preethi", "Divya", "Rahul"],
    "Age": [24, 23, 25, 24, 24, 23],
    "Mark": [85, 78, 92, 85, 88, 78]
})

print("Number of unique values in each column:")
print(students.nunique())


# In[ ]:




