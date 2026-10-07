#!/usr/bin/env python
# coding: utf-8

# # CSV Files
# 
# ### Definition
# 
# CSV stands for Comma-Separated Values.
# 
# A CSV file stores data in rows and columns, where each value is separated by a comma.
# 
# CSV files are commonly used to store and share tabular data.
# 
# ### Simple Example
# 
# A CSV file can contain student data like:
# 
# Name,Age,Mark
# Preethi,24,85
# Rahul,23,78
# Anu,25,92
# 
# ### Real-World Example
# 
# A school can store student details such as name, age, marks, and attendance in a CSV file.
# 
# ### Business Example
# 
# A company can store customer or sales records in CSV files and use them for analysis.
# 
# ### AI/ML Example
# 
# Many datasets used in AI/ML projects are available as CSV files.
# 
# Pandas can read the CSV file into a DataFrame, after which we can clean, analyze, and prepare the data for machine learning.
# 
# ### Code Explanation
# 
# `pd.read_csv()` reads a CSV file and converts it into a Pandas DataFrame.
# 
# Here, we first create a small CSV file for practice.
# 
# Then we use `pd.read_csv()` to read the file.
# 
# ### Output Explanation
# 
# The output displays the records from the CSV file as a Pandas DataFrame.

# In[1]:


import pandas as pd

data = """Name,Age,Mark
Preethi,24,85
Rahul,23,78
Anu,25,92"""

with open("students.csv", "w") as file:
    file.write(data)

students = pd.read_csv("students.csv")

print(students)


# # Excel Files
# 
# ### Definition
# 
# An Excel file is a spreadsheet file used to store data in rows and columns.
# 
# Pandas can read data from Excel files and also write DataFrame data into Excel files.
# 
# Excel files usually have the `.xlsx` extension.
# 
# ### Simple Example
# 
# A student Excel file can contain:
# 
# | Name | Age | Mark |
# |------|-----|------|
# | Preethi | 24 | 85 |
# | Rahul | 23 | 78 |
# | Anu | 25 | 92 |
# 
# ### Real-World Example
# 
# A school can maintain student marks, attendance, and other records in Excel files.
# 
# ### Business Example
# 
# Companies commonly use Excel files for sales reports, employee records, customer information, and financial data.
# 
# ### AI/ML Example
# 
# In an AI/ML project, data may initially be provided in an Excel file. Pandas can read the Excel file into a DataFrame so that we can clean and prepare the data for machine learning.
# 
# ### Code Explanation
# 
# `pd.DataFrame()` creates a DataFrame.
# 
# `to_excel()` saves the DataFrame into an Excel file.
# 
# `read_excel()` reads the Excel file and converts it back into a DataFrame.
# 
# `index=False` prevents the DataFrame index from being saved as an extra column.
# 
# ### Output Explanation
# 
# The output displays the data that was saved into and then read from the Excel file.

# In[2]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

students.to_excel("students.xlsx", index=False)

data = pd.read_excel("students.xlsx")

print(data)


# # JSON Files
# 
# ### Definition
# 
# JSON stands for JavaScript Object Notation.
# 
# A JSON file is a common format used to store and exchange structured data.
# 
# JSON stores data using key-value pairs.
# 
# ### Simple Example
# 
# A student record in JSON can look like:
# 
# {
#     "Name": "Preethi",
#     "Age": 24,
#     "Mark": 85
# }
# 
# ### Real-World Example
# 
# Applications can use JSON files to store user details, application settings, and other structured information.
# 
# ### Business Example
# 
# A company may receive customer or product information from an application in JSON format.
# 
# ### AI/ML Example
# 
# In AI/ML projects, JSON data can come from APIs or applications. Pandas can read JSON data into a DataFrame so that we can analyze and prepare it for further processing.
# 
# ### Code Explanation
# 
# `pd.DataFrame()` creates a DataFrame.
# 
# `to_json()` saves the DataFrame as a JSON file.
# 
# `read_json()` reads the JSON file and converts it back into a DataFrame.
# 
# ### Output Explanation
# 
# The output displays the student records that were saved and then read from the JSON file.

# In[3]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

students.to_json("students.json", orient="records")

data = pd.read_json("students.json")

print(data)


# # Parquet Files
# 
# ### Definition
# 
# Parquet is a file format used to store structured data efficiently.
# 
# It stores data in a column-based format, so it is useful when working with large datasets.
# 
# Parquet files usually have the `.parquet` extension.
# 
# ### Simple Example
# 
# Suppose we have student data with columns such as Name, Age, and Mark.
# 
# We can save this DataFrame as a Parquet file and read it later when needed.
# 
# ### Real-World Example
# 
# Large organizations can use Parquet files to store large amounts of customer, sales, or transaction data.
# 
# ### Business Example
# 
# A company may store millions of sales records in Parquet format because it is suitable for handling large datasets efficiently.
# 
# ### AI/ML Example
# 
# In AI/ML, large datasets can be stored in Parquet files. Pandas can read the required data into a DataFrame for data analysis and model preparation.
# 
# ### Code Explanation
# 
# `to_parquet()` saves a DataFrame as a Parquet file.
# 
# `read_parquet()` reads the Parquet file and converts it into a DataFrame.
# 
# The `pyarrow` engine is used to work with the Parquet format.
# 
# ### Output Explanation
# 
# The output displays the student data that was saved into and then read from the Parquet file.

# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install --upgrade pyarrow')


# In[2]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

students.to_parquet("students.parquet", index=False)

data = pd.read_parquet("students.parquet")

print(data)


# # Pickle Files
# 
# ### Definition
# 
# Pickle is a Python format used to save Python objects into a file.
# 
# With Pandas, we can save a DataFrame as a Pickle file and load it again later.
# 
# Pickle files usually have the `.pkl` extension.
# 
# ### Simple Example
# 
# Suppose we have a student DataFrame.
# 
# We can save the DataFrame as a Pickle file and read it back whenever we need it.
# 
# ### Real-World Example
# 
# A data analyst can save a processed dataset as a Pickle file and use it later without creating the DataFrame again.
# 
# ### Business Example
# 
# A company can save processed customer or sales data as a Pickle file for later analysis.
# 
# ### AI/ML Example
# 
# In AI/ML, Pickle can be used to save processed Python objects or datasets so they can be loaded again later.
# 
# It can also be used with trained machine learning objects, although model files should only be loaded from trusted sources.
# 
# ### Code Explanation
# 
# `to_pickle()` saves the DataFrame as a Pickle file.
# 
# `read_pickle()` reads the Pickle file and loads it back into a DataFrame.
# 
# ### Output Explanation
# 
# The output displays the student data after it is loaded from the Pickle file.

# In[3]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

students.to_pickle("students.pkl")

data = pd.read_pickle("students.pkl")

print(data)


# # SQL Tables
# 
# ### Definition
# 
# SQL (Structured Query Language) is used to store and manage data in databases.
# 
# Pandas can read data from SQL tables and also write DataFrames into SQL tables.
# 
# This helps us work with database data directly in Python.
# 
# ### Simple Example
# 
# Suppose we have a student table in a database:
# 
# | Name | Age | Mark |
# |------|-----|------|
# | Preethi | 24 | 85 |
# | Rahul | 23 | 78 |
# | Anu | 25 | 92 |
# 
# Pandas can read this table into a DataFrame.
# 
# ### Real-World Example
# 
# Schools can store student information in databases and use Pandas to analyze the data.
# 
# ### Business Example
# 
# Companies store customer, employee, and sales data in SQL databases.
# 
# Pandas can read the data for reporting and analysis.
# 
# ### AI/ML Example
# 
# In AI/ML projects, datasets are often stored in databases.
# 
# Pandas can load the data from SQL tables and prepare it for machine learning.
# 
# ### Code Explanation
# 
# `sqlite3.connect()` creates a database connection.
# 
# `to_sql()` saves the DataFrame into a SQL table.
# 
# `read_sql()` reads the SQL table into a DataFrame.
# 
# ### Output Explanation
# 
# The output displays the data read from the SQL table.

# In[4]:


import pandas as pd
import sqlite3

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

connection = sqlite3.connect("students.db")

students.to_sql("student_table", connection, if_exists="replace", index=False)

data = pd.read_sql("SELECT * FROM student_table", connection)

print(data)

connection.close()


# # Reading Multiple Files
# 
# ### Definition
# 
# Reading multiple files means loading data from more than one file into Pandas.
# 
# This is useful when data is stored in separate files but we want to combine and analyze it together.
# 
# ### Simple Example
# 
# Suppose we have two CSV files:
# 
# - January sales
# - February sales
# 
# We can read both files and combine their data into one DataFrame.
# 
# ### Real-World Example
# 
# A school may have separate CSV files for different classes. We can read all the files and combine the student records.
# 
# ### Business Example
# 
# A company may store monthly sales data in separate files. We can read all monthly files and combine them for yearly analysis.
# 
# ### AI/ML Example
# 
# In AI/ML, data may be divided into multiple files. We can read the files and combine them into one dataset before cleaning and model training.
# 
# ### Code Explanation
# 
# `pd.read_csv()` reads a CSV file.
# 
# `pd.concat()` combines multiple DataFrames.
# 
# The `files` list contains the names of the CSV files.
# 
# The loop reads each file and stores the DataFrame in the `dataframes` list.
# 
# ### Output Explanation
# 
# The output contains the records from both CSV files combined into one DataFrame.

# In[5]:


import pandas as pd

january = pd.DataFrame({
    "Name": ["Preethi", "Rahul"],
    "Sales": [5000, 7000]
})

february = pd.DataFrame({
    "Name": ["Anu", "Karthik"],
    "Sales": [6000, 8000]
})

january.to_csv("january.csv", index=False)
february.to_csv("february.csv", index=False)

files = ["january.csv", "february.csv"]

dataframes = []

for file in files:
    dataframes.append(pd.read_csv(file))

all_sales = pd.concat(dataframes, ignore_index=True)

print(all_sales)


# # File Path Handling
# 
# ### Definition
# 
# File path handling means specifying the location of a file so that Python can read or write the file correctly.
# 
# A file path can be:
# - Relative path → file location based on the current folder
# - Absolute path → complete location of the file
# 
# ### Simple Example
# 
# If `students.csv` is in the same folder as our notebook, we can simply use:
# 
# "students.csv"
# 
# If the file is inside a folder called `data`, we can use:
# 
# "data/students.csv"
# 
# ### Real-World Example
# 
# A company may keep its datasets inside separate folders such as:
# 
# data/
#     sales.csv
#     customers.csv
# 
# We need the correct file path to read these files.
# 
# ### Business Example
# 
# A business project may have separate folders for sales data, customer data, and employee data. File paths help Python find the required files.
# 
# ### AI/ML Example
# 
# In AI/ML projects, datasets are often stored inside folders such as `data`, `train`, and `test`.
# 
# Correct file path handling helps us load the required dataset without errors.
# 
# ### Code Explanation
# 
# `import os` imports Python's operating system module.
# 
# `os.path.join()` creates a file path using folder and file names.
# 
# `pd.read_csv()` reads the CSV file from the given path.
# 
# ### Output Explanation
# 
# The output displays the student data read from the `data` folder.
# 
# Using `os.path.join()` helps create the path correctly for the operating system.

# In[6]:


import pandas as pd
import os

os.makedirs("data", exist_ok=True)

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

students.to_csv("data/students.csv", index=False)

file_path = os.path.join("data", "students.csv")

data = pd.read_csv(file_path)

print(data)


# In[ ]:




