#!/usr/bin/env python
# coding: utf-8

# # loc
# 
# ### Definition
# 
# `loc` is used to select rows and columns from a Pandas DataFrame using labels or column names.
# 
# ### Simple Example
# 
# If we want to select the details of one student using the row label, we can use `loc`.
# 
# ### Real-World Example
# 
# In a student dataset, we can use `loc` to select a particular student's details.
# 
# ### Business Example
# 
# A company can use `loc` to select the details of a particular employee.
# 
# ### AI/ML Example
# 
# In machine learning, `loc` can be used to select specific rows or columns before preparing data for a model.
# 
# ### Code Explanation
# 
# First, we create a DataFrame with student details.
# 
# `students.loc[0]` selects the row with label `0`.
# 
# `students.loc[0, "Name"]` selects the Name from row `0`.
# 
# ### Output Explanation
# 
# The first statement displays the complete details of the first student.
# 
# The second statement displays only the name of the first student.

# In[1]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "Age": [24, 23, 25, 22],
    "Mark": [85, 78, 92, 81]
})

print("First student's details:")
print(students.loc[0])

print("\nFirst student's name:")
print(students.loc[0, "Name"])


# # iloc
# 
# ### Definition
# 
# `iloc` is used to select rows and columns from a Pandas DataFrame using their position number.
# 
# ### Simple Example
# 
# If we want to select the first row, we use position `0`.
# 
# ### Real-World Example
# 
# In a student dataset, `iloc` can be used to select the first student or first few students.
# 
# ### Business Example
# 
# A company can use `iloc` to select specific rows or columns from employee data based on their position.
# 
# ### AI/ML Example
# 
# In AI/ML, `iloc` can be used to select specific rows and columns from a dataset before training a model.
# 
# ### Code Explanation
# 
# `students.iloc[0]` selects the first row.
# 
# `students.iloc[0, 1]` selects the value from the first row and second column.
# 
# `students.iloc[0:2]` selects the first two rows.
# 
# ### Output Explanation
# 
# The output shows the selected rows or values based on their position.

# In[2]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "Age": [24, 23, 25, 22],
    "Mark": [85, 78, 92, 81]
})

print("First row:")
print(students.iloc[0])

print("\nFirst row, second column:")
print(students.iloc[0, 1])

print("\nFirst two rows:")
print(students.iloc[0:2])


# # Boolean Indexing
# 
# ### Definition
# 
# Boolean Indexing is used to select rows from a DataFrame based on a condition.
# 
# The condition gives `True` or `False` for each row.
# 
# ### Simple Example
# 
# If we want to select students whose marks are greater than 80, we can use Boolean Indexing.
# 
# ### Real-World Example
# 
# We can select employees whose salary is greater than ₹50,000.
# 
# ### Business Example
# 
# A company can find customers whose purchase amount is greater than ₹10,000.
# 
# ### AI/ML Example
# 
# In AI/ML, Boolean Indexing can be used to select only the required records from a dataset.
# 
# ### Code Explanation
# 
# `students["Mark"] > 80` checks each student's mark.
# 
# Rows where the condition is `True` are selected.
# 
# ### Output Explanation
# 
# Only students with marks greater than 80 will be displayed.

# In[3]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "Age": [24, 23, 25, 22],
    "Mark": [85, 78, 92, 81]
})

high_mark_students = students[students["Mark"] > 80]

print("Students with marks greater than 80:")
print(high_mark_students)


# # Filtering Rows
# 
# ### Definition
# 
# Filtering Rows means selecting only the rows that match a specific condition.
# 
# ### Simple Example
# 
# If we want to see only students who are 24 years old, we can filter the rows using the Age column.
# 
# ### Real-World Example
# 
# A shopping website can filter customers based on their age or purchase amount.
# 
# ### Business Example
# 
# A company can filter employees who belong to a particular department.
# 
# ### AI/ML Example
# 
# In AI/ML, filtering can be used to select useful records from a dataset before analysis or model training.
# 
# ### Code Explanation
# 
# `students["Age"] == 24` checks which students are 24 years old.
# 
# The matching rows are stored in `filtered_students`.
# 
# ### Output Explanation
# 
# The output displays only the students whose age is 24.

# In[4]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "Age": [24, 23, 25, 24],
    "Mark": [85, 78, 92, 81]
})

filtered_students = students[students["Age"] == 24]

print("Students whose age is 24:")
print(filtered_students)


# # query()
# 
# ### Definition
# 
# `query()` is used to filter rows in a Pandas DataFrame by writing a condition in a simple way.
# 
# ### Simple Example
# 
# If we want to select students whose marks are greater than 80, we can use `query()`.
# 
# ### Real-World Example
# 
# A company can use `query()` to find employees whose salary is above a particular amount.
# 
# ### Business Example
# 
# A business can find customers whose purchase amount is greater than ₹10,000.
# 
# ### AI/ML Example
# 
# In AI/ML, `query()` can be used to filter the required data before analysis or model training.
# 
# ### Code Explanation
# 
# `students.query("Mark > 80")` checks the Mark column and selects rows where the mark is greater than 80.
# 
# ### Output Explanation
# 
# Only students whose marks are greater than 80 will be displayed.

# In[5]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "Age": [24, 23, 25, 22],
    "Mark": [85, 78, 92, 81]
})

filtered_students = students.query("Mark > 80")

print("Students with marks greater than 80:")
print(filtered_students)


# # isin()
# 
# ### Definition
# 
# `isin()` is used to check whether values in a column belong to a given list of values.
# 
# ### Simple Example
# 
# If we want to select students from Chennai or Mumbai, we can use `isin()`.
# 
# ### Real-World Example
# 
# A shopping website can select customers from a list of selected cities.
# 
# ### Business Example
# 
# A company can filter sales data for selected branches.
# 
# ### AI/ML Example
# 
# In AI/ML, `isin()` can be used to select records belonging to specific categories or groups.
# 
# ### Code Explanation
# 
# `students["City"].isin(["Chennai", "Mumbai"])` checks whether each student's city is Chennai or Mumbai.
# 
# The matching rows are selected from the DataFrame.
# 
# ### Output Explanation
# 
# Only students from Chennai and Mumbai will be displayed.

# In[6]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "City": ["Chennai", "Mumbai", "Delhi", "Chennai"],
    "Mark": [85, 78, 92, 81]
})

selected_students = students[
    students["City"].isin(["Chennai", "Mumbai"])
]

print("Students from Chennai or Mumbai:")
print(selected_students)


# # between()
# 
# ### Definition
# 
# `between()` is used to select rows where a column value is within a given range.
# 
# ### Simple Example
# 
# If we want to select students whose marks are between 80 and 90, we can use `between()`.
# 
# ### Real-World Example
# 
# A company can find employees whose salary is between ₹30,000 and ₹50,000.
# 
# ### Business Example
# 
# A business can find products whose price is between ₹500 and ₹1,000.
# 
# ### AI/ML Example
# 
# In AI/ML, `between()` can be used to select data within a required numerical range before analysis.
# 
# ### Code Explanation
# 
# `students["Mark"].between(80, 90)` checks whether each mark is between 80 and 90.
# 
# The matching rows are selected from the DataFrame.
# 
# ### Output Explanation
# 
# Only students whose marks are between 80 and 90 will be displayed.

# In[7]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "Age": [24, 23, 25, 22],
    "Mark": [85, 78, 92, 81]
})

selected_students = students[
    students["Mark"].between(80, 90)
]

print("Students with marks between 80 and 90:")
print(selected_students)


# # Sorting Data
# 
# ### Definition
# 
# Sorting Data means arranging the rows in a DataFrame based on a column value.
# 
# Pandas provides `sort_values()` to sort data.
# 
# ### Simple Example
# 
# We can arrange students from the highest mark to the lowest mark.
# 
# ### Real-World Example
# 
# An online shopping website can arrange products from lowest price to highest price.
# 
# ### Business Example
# 
# A company can arrange employees based on salary from highest to lowest.
# 
# ### AI/ML Example
# 
# In AI/ML, sorting can help us understand and analyze data in a particular order.
# 
# ### Code Explanation
# 
# `sort_values("Mark")` sorts the data based on the Mark column.
# 
# `ascending=False` arranges the marks from highest to lowest.
# 
# ### Output Explanation
# 
# The students are displayed from the highest mark to the lowest mark.

# In[8]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "Age": [24, 23, 25, 22],
    "Mark": [85, 78, 92, 81]
})

sorted_students = students.sort_values(
    by="Mark",
    ascending=False
)

print("Students sorted by marks:")
print(sorted_students)


# In[ ]:




