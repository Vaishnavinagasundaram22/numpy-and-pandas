#!/usr/bin/env python
# coding: utf-8

# # groupby()
# 
# ### Definition
# 
# `groupby()` is used to group rows that have the same value in a particular column.
# 
# After grouping, we can perform calculations such as sum, mean, count, etc.
# 
# ### Simple Example
# 
# If we have students from different cities, we can group the students based on their city.
# 
# ### Real-World Example
# 
# A company can group employees based on their department.
# 
# ### Business Example
# 
# A business can group sales based on different cities or branches and calculate the total sales.
# 
# ### AI/ML Example
# 
# In AI/ML, `groupby()` can be used to understand patterns and summarize data based on different categories.
# 
# ### Code Explanation
# 
# `students.groupby("City")` groups the students based on the City column.
# 
# `["Mark"].mean()` calculates the average mark for each city.
# 
# ### Output Explanation
# 
# The output shows the average mark for each city.

# In[1]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "City": ["Chennai", "Mumbai", "Chennai", "Mumbai"],
    "Mark": [85, 78, 92, 82]
})

average_marks = students.groupby("City")["Mark"].mean()

print("Average mark by city:")
print(average_marks)


# # agg()
# 
# ### Definition
# 
# `agg()` means aggregation. It is used to perform multiple calculations on grouped data.
# 
# We can calculate values such as `sum`, `mean`, `min`, and `max`.
# 
# ### Simple Example
# 
# For each city, we can find the total marks and average marks of students.
# 
# ### Real-World Example
# 
# A company can calculate the total and average sales for each branch.
# 
# ### Business Example
# 
# A business can find the total, average, minimum, and maximum sales for each city.
# 
# ### AI/ML Example
# 
# In AI/ML, `agg()` can be used to summarize data and understand different groups before building a model.
# 
# ### Code Explanation
# 
# First, `groupby("City")` groups the students by city.
# 
# Then, `agg()` calculates the total and average marks for each city.
# 
# ### Output Explanation
# 
# The output shows the total marks and average marks for each city.

# In[2]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "City": ["Chennai", "Mumbai", "Chennai", "Mumbai"],
    "Mark": [85, 78, 92, 82]
})

result = students.groupby("City")["Mark"].agg(
    ["sum", "mean"]
)

print("Total and average marks by city:")
print(result)


# # transform()
# 
# ### Definition
# 
# `transform()` is used to perform a calculation on grouped data and return the result with the same number of rows as the original DataFrame.
# 
# ### Simple Example
# 
# We can calculate the average mark of each city and add that average to every student from that city.
# 
# ### Real-World Example
# 
# A company can calculate the average salary of each department and show the department average beside every employee.
# 
# ### Business Example
# 
# A business can compare each employee's sales with the average sales of their branch.
# 
# ### AI/ML Example
# 
# In AI/ML, `transform()` can be useful for creating new features based on group-level information.
# 
# ### Code Explanation
# 
# `groupby("City")["Mark"].transform("mean")` calculates the average mark for each city.
# 
# The result is stored in a new `City_Average` column.
# 
# ### Output Explanation
# 
# Each student gets the average mark of their city in the `City_Average` column.

# In[3]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "City": ["Chennai", "Mumbai", "Chennai", "Mumbai"],
    "Mark": [85, 78, 92, 82]
})

students["City_Average"] = students.groupby("City")["Mark"].transform("mean")

print(students)


# # filter()
# 
# ### Definition
# 
# `filter()` is used with grouped data to keep only the groups that satisfy a given condition.
# 
# ### Simple Example
# 
# We can keep only the cities where the average student mark is greater than 80.
# 
# ### Real-World Example
# 
# A company can keep only departments whose average salary is above a certain amount.
# 
# ### Business Example
# 
# A business can find branches whose total sales are greater than ₹10,000.
# 
# ### AI/ML Example
# 
# In AI/ML, `filter()` can be used to keep only useful groups for further analysis.
# 
# ### Code Explanation
# 
# First, `groupby("City")` groups the students by city.
# 
# Then, `filter()` keeps only the groups whose average mark is greater than 80.
# 
# ### Output Explanation
# 
# Only cities with an average mark greater than 80 are displayed.

# In[4]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "City": ["Chennai", "Mumbai", "Chennai", "Mumbai"],
    "Mark": [85, 78, 92, 72]
})

result = students.groupby("City").filter(
    lambda group: group["Mark"].mean() > 80
)

print("Cities with average mark greater than 80:")
print(result)


# # Pivot Tables
# 
# ### Definition
# 
# A Pivot Table is used to summarize and organize data based on different categories.
# 
# In Pandas, we use `pivot_table()` to create a Pivot Table.
# 
# ### Simple Example
# 
# We can find the average marks of students based on their city.
# 
# ### Real-World Example
# 
# A company can use a Pivot Table to summarize sales based on city and product.
# 
# ### Business Example
# 
# A business can compare the total sales of different products in different cities.
# 
# ### AI/ML Example
# 
# In AI/ML, Pivot Tables can help summarize data and understand patterns between different categories.
# 
# ### Code Explanation
# 
# `index="City"` groups the data by city.
# 
# `values="Mark"` tells Pandas which value to calculate.
# 
# `aggfunc="mean"` calculates the average mark for each city.
# 
# ### Output Explanation
# 
# The output shows the average marks for each city.

# In[5]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "City": ["Chennai", "Mumbai", "Chennai", "Mumbai"],
    "Mark": [85, 78, 92, 82]
})

pivot = pd.pivot_table(
    students,
    index="City",
    values="Mark",
    aggfunc="mean"
)

print("Average marks by city:")
print(pivot)


# # Crosstab
# 
# ### Definition
# 
# `crosstab()` is used to create a frequency table that shows how often values occur between two or more categories.
# 
# ### Simple Example
# 
# We can use `crosstab()` to count how many students belong to each city and result category.
# 
# ### Real-World Example
# 
# A company can count employees based on department and job type.
# 
# ### Business Example
# 
# A business can count customers based on city and purchase status.
# 
# ### AI/ML Example
# 
# In AI/ML, a crosstab can help understand the relationship between categorical variables.
# 
# ### Code Explanation
# 
# `pd.crosstab()` creates a table using the `City` and `Result` columns.
# 
# `City` is shown as rows and `Result` is shown as columns.
# 
# The values in the table represent the number of students in each category.
# 
# ### Output Explanation
# 
# The output shows how many students from each city have each result.

# In[6]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik", "Divya"],
    "City": ["Chennai", "Mumbai", "Chennai", "Mumbai", "Chennai"],
    "Result": ["Pass", "Pass", "Pass", "Fail", "Fail"]
})

result = pd.crosstab(
    students["City"],
    students["Result"]
)

print("Students by city and result:")
print(result)


# In[ ]:




