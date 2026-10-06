#!/usr/bin/env python
# coding: utf-8

# # What is Pandas?
# 
# ### Definition
# 
# Pandas is a Python library used to work with data.
# 
# It helps us to create, read, organize, analyze, and manipulate data in a simple way.
# 
# Pandas mainly works with two important data structures:
# 
# - Series
# - DataFrame
# 
# ### Example
# 
# We can use Pandas to store student information such as:
# 
# Name, Age, Mark
# 
# Pandas makes it easier to work with this type of tabular data.
# 
# ### Real-World Example
# 
# A school can use Pandas to analyze student marks, attendance, and other student information.
# 
# ### Business Example
# 
# A company can use Pandas to analyze customer data, sales data, employee information, and financial records.
# 
# ### AI/ML Example
# 
# Pandas is widely used in AI/ML projects for loading datasets, cleaning data, selecting columns, handling missing values, and preparing data before training a machine learning model.
# 
# ### Code Explanation
# 
# `import pandas as pd` imports the Pandas library.
# 
# `pd.DataFrame()` creates a DataFrame using the given data.
# 
# The DataFrame stores the student information in rows and columns.
# 
# ### Output Explanation
# 
# The output displays the student information as a table with Name, Age, and Mark columns.

# In[1]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

print(students)


# # Why Pandas?
# 
# ### Definition
# 
# Pandas is useful because it makes working with structured and tabular data easier.
# 
# Instead of handling data manually, Pandas helps us easily:
# - Store data in rows and columns
# - Read data from files
# - Filter required data
# - Clean data
# - Find missing values
# - Calculate values
# - Analyze data
# 
# ### Simple Example
# 
# Suppose we have student marks:
# 
# | Name | Mark |
# |------|------|
# | Preethi | 85 |
# | Rahul | 78 |
# | Anu | 92 |
# 
# Using Pandas, we can easily find students who scored more than 80.
# 
# ### Real-World Example
# 
# In a school, Pandas can be used to manage student details, marks, attendance, and results.
# 
# ### Business Example
# 
# A company can use Pandas to work with customer data, sales data, employee data, and financial reports.
# 
# For example, a company can find customers whose purchase amount is greater than ₹10,000.
# 
# ### AI/ML Example
# 
# In AI/ML, Pandas is commonly used before training a model.
# 
# We can use Pandas to:
# - Load the dataset
# - Check the data
# - Select required columns
# - Filter rows
# - Handle missing values
# - Prepare data for machine learning
# 
# ### Code Explanation
# 
# `import pandas as pd` imports the Pandas library.
# 
# `pd.DataFrame()` creates a table with rows and columns.
# 
# `students["Mark"] > 80` checks which students scored more than 80.
# 
# `students[students["Mark"] > 80]` filters and gives only those students.
# 
# ### Output Explanation
# 
# The output contains only the students whose marks are greater than 80.

# In[2]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Mark": [85, 78, 92]
})

high_marks = students[students["Mark"] > 80]

print(high_marks)


# # Series
# 
# ### Definition
# 
# A Series is a one-dimensional data structure in Pandas.
# 
# It stores data in a single column with an index for each value.
# 
# ### Simple Example
# 
# For example, student marks can be stored as a Series:
# 
# 85, 78, 92
# 
# Each value will have an index like 0, 1, 2.
# 
# ### Real-World Example
# 
# A school can use a Series to store only the marks of students.
# 
# ### Business Example
# 
# A company can use a Series to store the sales amount of different days.
# 
# ### AI/ML Example
# 
# In AI/ML, a Series can represent one feature or one column from a dataset, such as Age, Salary, or Marks.
# 
# ### Code Explanation
# 
# `import pandas as pd` imports Pandas.
# 
# `pd.Series()` creates a Pandas Series.
# 
# The values inside the list are stored in one column.
# 
# `print(marks)` displays the Series along with its index.
# 
# ### Output Explanation
# 
# The output shows the marks in one column.
# 
# The numbers on the left, 0, 1, and 2, are the indexes of the values.

# In[3]:


import pandas as pd

marks = pd.Series([85, 78, 92])

print(marks)


# # DataFrame
# 
# ### Definition
# 
# A DataFrame is a two-dimensional data structure in Pandas.
# 
# It stores data in rows and columns, similar to a table in Excel.
# 
# ### Simple Example
# 
# For example, student data can have columns like Name, Age, and Mark.
# 
# | Name | Age | Mark |
# |------|-----|------|
# | Preethi | 24 | 85 |
# | Rahul | 23 | 78 |
# | Anu | 25 | 92 |
# 
# This type of table can be created using a Pandas DataFrame.
# 
# ### Real-World Example
# 
# A school can use a DataFrame to store student name, age, class, marks, and attendance.
# 
# ### Business Example
# 
# A company can store customer details such as Customer Name, Age, City, and Purchase Amount in a DataFrame.
# 
# ### AI/ML Example
# 
# In AI/ML, datasets are commonly stored and processed as DataFrames.
# 
# For example, a customer dataset can contain Age, Income, Website Visits, and Purchase columns. We can use Pandas DataFrame to inspect and prepare this data before giving it to a machine learning model.
# 
# ### Code Explanation
# 
# `import pandas as pd` imports the Pandas library.
# 
# `pd.DataFrame()` creates a DataFrame.
# 
# The data is given using column names such as Name, Age, and Mark.
# 
# Each list becomes one column in the DataFrame.
# 
# ### Output Explanation
# 
# The output displays the student information in rows and columns.
# 
# The numbers on the left are the row indexes.

# In[4]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

print(students)


# # Creating DataFrames
# 
# ### Definition
# 
# Creating a DataFrame means creating a table with rows and columns using Pandas.
# 
# We can create a DataFrame from different types of data such as dictionaries, lists, and NumPy arrays.
# 
# ### Simple Example
# 
# We can use a dictionary to create a student DataFrame.
# 
# The dictionary keys become the column names and the values become the data in each column.
# 
# ### Real-World Example
# 
# A school can create a DataFrame from student information such as Name, Age, and Mark.
# 
# ### Business Example
# 
# A company can create a DataFrame from customer information such as Customer Name, City, and Purchase Amount.
# 
# ### AI/ML Example
# 
# In AI/ML, we can create a DataFrame for testing or preparing small datasets before training a machine learning model.
# 
# ### Code Explanation
# 
# `import pandas as pd` imports Pandas.
# 
# The dictionary contains three columns: Name, Age, and Mark.
# 
# `pd.DataFrame(student_data)` converts the dictionary into a DataFrame.
# 
# `print(students)` displays the created table.
# 
# ### Output Explanation
# 
# The output shows a table with three columns and three student records.

# In[5]:


import pandas as pd

student_data = {
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
}

students = pd.DataFrame(student_data)

print(students)


# # Data Types in Pandas
# 
# ### Definition
# 
# Data types tell us what kind of data is stored in each column of a DataFrame.
# 
# For example:
# - `int64` → whole numbers
# - `float64` → decimal numbers
# - `object` / `string` → text
# - `bool` → True or False
# 
# ### Simple Example
# 
# If a DataFrame has:
# - Age → 24, 25, 26
# - Salary → 25000.50, 30000.75
# - Name → Preethi, Rahul, Anu
# 
# Pandas identifies the suitable data type for each column.
# 
# ### Real-World Example
# 
# In a student dataset, Age can be an integer, Name can be text, and Attendance can be a decimal value.
# 
# ### Business Example
# 
# In a company dataset, Employee_ID can be an integer, Employee_Name can be text, and Salary can be a decimal value.
# 
# ### AI/ML Example
# 
# Data types are important in AI/ML because machine learning models need data in suitable formats. Before training a model, we usually check the data types and convert them if required.
# 
# ### Code Explanation
# 
# `pd.DataFrame()` creates the DataFrame.
# 
# `students.dtypes` shows the data type of every column.
# 
# ### Output Explanation
# 
# The output shows the data type of each column.
# 
# For example, Name is text, while Age and Mark are whole numbers.

# In[6]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92],
    "Attendance": [95.5, 88.0, 91.5]
})

print(students.dtypes)


# # Index
# 
# ### Definition
# 
# Index is used to identify the position of each row in a Pandas DataFrame or Series.
# 
# By default, Pandas gives numbers as indexes starting from 0.
# 
# ### Simple Example
# 
# If we have three students:
# 
# Preethi → index 0  
# Rahul → index 1  
# Anu → index 2
# 
# We can use these indexes to identify and access rows.
# 
# ### Real-World Example
# 
# In a student dataset, each row can have an index to identify the position of a student's record.
# 
# ### Business Example
# 
# In a sales dataset, the index can help identify each sales record.
# 
# ### AI/ML Example
# 
# In AI/ML, indexes help us access specific rows while filtering, selecting, or processing datasets.
# 
# ### Code Explanation
# 
# `pd.DataFrame()` creates the DataFrame.
# 
# `students.index` displays the indexes of the DataFrame.
# 
# The default index starts from 0 and increases by 1 for every row.
# 
# ### Output Explanation
# 
# The output shows the starting index, ending index, and step value.
# 
# Here, the index starts at 0 and ends before 3, so the indexes are 0, 1, and 2.

# In[7]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

print(students.index)


# # Columns
# 
# ### Definition
# 
# Columns are the vertical parts of a DataFrame.
# 
# Each column usually represents one type of information, such as Name, Age, Mark, or Salary.
# 
# ### Simple Example
# 
# In a student DataFrame:
# 
# | Name | Age | Mark |
# |------|-----|------|
# | Preethi | 24 | 85 |
# | Rahul | 23 | 78 |
# | Anu | 25 | 92 |
# 
# Here, Name, Age, and Mark are the columns.
# 
# ### Real-World Example
# 
# A school student dataset can have columns such as Student Name, Age, Class, Mark, and Attendance.
# 
# ### Business Example
# 
# A company customer dataset can have columns such as Customer Name, City, Age, and Purchase Amount.
# 
# ### AI/ML Example
# 
# In AI/ML, columns are often called features when they are used as input data for a machine learning model.
# 
# For example, Age, Income, and Website Visits can be features used to predict whether a customer will purchase a product.
# 
# ### Code Explanation
# 
# `students.columns` is used to get the column names of the DataFrame.
# 
# `print(students.columns)` displays all the column names.
# 
# ### Output Explanation
# 
# The output shows the names of all columns present in the DataFrame.

# In[8]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

print(students.columns)


# # Reading Data
# 
# ### Definition
# 
# Reading data means loading data from a file into Pandas so that we can view, analyze, and work with it.
# 
# Pandas can read data from different file formats such as CSV, Excel, JSON, and more.
# 
# ### Simple Example
# 
# If we have a CSV file containing student details, Pandas can read that file and convert the data into a DataFrame.
# 
# ### Real-World Example
# 
# A school may store student details in a CSV file. We can use Pandas to read the file and analyze the student records.
# 
# ### Business Example
# 
# A company may have a sales CSV file. Pandas can read the file so that the company can analyze sales, customers, and revenue.
# 
# ### AI/ML Example
# 
# In AI/ML, datasets are often stored in files. Pandas is used to read the dataset and convert it into a DataFrame before cleaning and preparing the data for a machine learning model.
# 
# ### Code Explanation
# 
# `pd.read_csv()` is used to read a CSV file.
# 
# Here, we first create a small CSV file using Python so that the example can run without needing an external file.
# 
# Then `pd.read_csv()` reads the file and creates a DataFrame.
# 
# ### Output Explanation
# 
# The output displays the data that was read from the CSV file as a Pandas DataFrame.

# In[9]:


import pandas as pd

data = """Name,Age,Mark
Preethi,24,85
Rahul,23,78
Anu,25,92"""

with open("students.csv", "w") as file:
    file.write(data)

students = pd.read_csv("students.csv")

print(students)


# # Writing Data
# 
# ### Definition
# 
# Writing data means saving the data from a Pandas DataFrame into a file.
# 
# Pandas can save DataFrames into different file formats such as CSV, Excel, and JSON.
# 
# ### Simple Example
# 
# If we have student data in a DataFrame, we can save that data into a CSV file.
# 
# ### Real-World Example
# 
# A school can save student marks and attendance data into a CSV file for future use.
# 
# ### Business Example
# 
# A company can save customer or sales data into a file after analyzing it.
# 
# ### AI/ML Example
# 
# In AI/ML, after cleaning or preprocessing a dataset, we can save the processed data into a file and use it later for model training.
# 
# ### Code Explanation
# 
# `pd.DataFrame()` creates the DataFrame.
# 
# `students.to_csv()` saves the DataFrame as a CSV file.
# 
# `index=False` prevents Pandas from saving the DataFrame index as an extra column.
# 
# ### Output Explanation
# 
# The DataFrame is saved as `students_output.csv`.
# 
# The message confirms that the data has been written to the CSV file.

# In[10]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

students.to_csv("students_output.csv", index=False)

print("Data saved successfully!")


# In[ ]:




