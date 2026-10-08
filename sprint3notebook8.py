#!/usr/bin/env python
# coding: utf-8

# # Rename Columns
# 
# ### Definition
# 
# Renaming Columns means changing the existing column names of a Pandas DataFrame.
# 
# We use `rename()` to change column names.
# 
# ### Simple Example
# 
# If a column is named `Name`, we can change it to `Student_Name`.
# 
# ### Real-World Example
# 
# When working with data from different sources, column names may not be clear. We can rename them to make the data easier to understand.
# 
# ### Business Example
# 
# A company may rename `Sales_Amt` to `Sales_Amount` to make the column name clearer.
# 
# ### AI/ML Example
# 
# In AI/ML projects, clear column names make the dataset easier to understand and use during preprocessing and model building.
# 
# ### Code Explanation
# 
# `rename()` is used to change column names.
# 
# Here, `Name` is changed to `Student_Name` and `Mark` is changed to `Marks`.
# 
# ### Output Explanation
# 
# The DataFrame is displayed with the new column names.

# In[1]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

students = students.rename(columns={
    "Name": "Student_Name",
    "Mark": "Marks"
})

print(students)


# # Drop Rows
# 
# ### Definition
# 
# `drop()` is used to remove unwanted rows from a Pandas DataFrame.
# 
# ### Simple Example
# 
# If we want to remove the second student from the DataFrame, we can drop that row using its index.
# 
# ### Real-World Example
# 
# If a customer record is no longer needed, we can remove that row from the dataset.
# 
# ### Business Example
# 
# A company can remove incorrect or unwanted employee records from its data.
# 
# ### AI/ML Example
# 
# In AI/ML, unwanted rows can be removed during data cleaning before training a model.
# 
# ### Code Explanation
# 
# `students.drop(1)` removes the row with index `1`.
# 
# `axis=0` means we are working with rows.
# 
# ### Output Explanation
# 
# The student at index `1` is removed, and the remaining rows are displayed.

# In[2]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu", "Karthik"],
    "Age": [24, 23, 25, 22],
    "Mark": [85, 78, 92, 81]
})

students = students.drop(1)

print("After dropping row 1:")
print(students)


# # Drop Columns
# 
# ### Definition
# 
# `drop()` is used to remove unwanted columns from a Pandas DataFrame.
# 
# ### Simple Example
# 
# If we do not need the `Age` column, we can remove it from the DataFrame.
# 
# ### Real-World Example
# 
# A customer dataset may contain unnecessary columns that are not needed for analysis.
# 
# ### Business Example
# 
# A company can remove unwanted employee information before creating a report.
# 
# ### AI/ML Example
# 
# In AI/ML, unnecessary columns can be removed before model training.
# 
# ### Code Explanation
# 
# `students.drop("Age", axis=1)` removes the `Age` column.
# 
# Here, `axis=1` means we are working with columns.
# 
# ### Output Explanation
# 
# The `Age` column is removed, and the remaining columns are displayed.

# 

# In[4]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Age": [24, 23, 25],
    "Mark": [85, 78, 92]
})

students = students.drop("Age", axis=1)

print("After dropping Age column:")
print(students)


# # Insert Columns
# 
# ### Definition
# 
# Inserting Columns means adding a new column to an existing Pandas DataFrame.
# 
# We can create a new column by assigning values to a new column name.
# 
# ### Simple Example
# 
# If we have student details and want to add a `Result` column, we can insert a new column.
# 
# ### Real-World Example
# 
# A student dataset can have a new column such as `Pass_Status`.
# 
# ### Business Example
# 
# A company can add a `Bonus` column to employee salary data.
# 
# ### AI/ML Example
# 
# In AI/ML, we can add a new feature column based on existing data.
# 
# ### Code Explanation
# 
# `students["Result"] = ["Pass", "Pass", "Pass"]` creates a new `Result` column and adds values to it.
# 
# ### Output Explanation
# 
# The DataFrame now contains the newly added `Result` column.

# In[5]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Mark": [85, 78, 92]
})

students["Result"] = ["Pass", "Pass", "Pass"]

print("After inserting Result column:")
print(students)


# # assign()
# 
# ### Definition
# 
# `assign()` is used to add a new column or create a modified DataFrame in Pandas.
# 
# ### Simple Example
# 
# We can use `assign()` to add a `Result` column based on student marks.
# 
# ### Real-World Example
# 
# A company can add a new column such as `Bonus` to employee data.
# 
# ### Business Example
# 
# A business can calculate a new `Total_Sales` column from existing sales data.
# 
# ### AI/ML Example
# 
# In AI/ML, `assign()` can be used to create new features from existing columns.
# 
# ### Code Explanation
# 
# `assign(Result=...)` creates a new column called `Result`.
# 
# Here, students with marks greater than or equal to 80 are given `Pass`.
# 
# ### Output Explanation
# 
# The output contains the original columns along with the newly created `Result` column.

# In[6]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Mark": [85, 78, 92]
})

students = students.assign(
    Result=students["Mark"].apply(lambda x: "Pass" if x >= 80 else "Fail")
)

print(students)


# # apply()
# 
# ### Definition
# 
# `apply()` is used to apply a function to each value or row in a Pandas DataFrame or Series.
# 
# ### Simple Example
# 
# We can use `apply()` to increase each student's mark by 5.
# 
# ### Real-World Example
# 
# A company can use `apply()` to calculate a bonus for each employee.
# 
# ### Business Example
# 
# A business can calculate a discount for each product using `apply()`.
# 
# ### AI/ML Example
# 
# In AI/ML, `apply()` can be used for data transformation and feature creation.
# 
# ### Code Explanation
# 
# The function `add_five()` receives one mark and adds 5 to it.
# 
# `students["Mark"].apply(add_five)` applies the function to every value in the Mark column.
# 
# ### Output Explanation
# 
# Each student's mark is increased by 5.

# In[7]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "Mark": [85, 78, 92]
})

def add_five(mark):
    return mark + 5

students["Updated_Mark"] = students["Mark"].apply(add_five)

print(students)


# # map()
# 
# ### Definition
# 
# `map()` is used to apply a function or replace values in a Pandas Series.
# 
# ### Simple Example
# 
# If we have short city codes like `CHN` and `BLR`, we can use `map()` to convert them into full city names.
# 
# ### Real-World Example
# 
# A company may have short codes for departments and use `map()` to convert them into readable names.
# 
# ### Business Example
# 
# A business can convert product category codes into category names.
# 
# ### AI/ML Example
# 
# In AI/ML, `map()` can be used to convert categorical values into meaningful values during data preprocessing.
# 
# ### Code Explanation
# 
# The dictionary inside `map()` contains the old value and its new value.
# 
# `students["City"].map(city_names)` changes the city codes into full city names.
# 
# ### Output Explanation
# 
# The `City` column now contains the full city names instead of the short codes.

# In[8]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "City": ["CHN", "BLR", "CHN"]
})

city_names = {
    "CHN": "Chennai",
    "BLR": "Bangalore"
}

students["City"] = students["City"].map(city_names)

print(students)


# # replace()
# 
# ### Definition
# 
# `replace()` is used to replace existing values in a Pandas DataFrame or Series with new values.
# 
# ### Simple Example
# 
# If a city is written as `Chennai` and we want to change it to `Madras`, we can use `replace()`.
# 
# ### Real-World Example
# 
# A dataset may contain incorrect or old values that need to be replaced.
# 
# ### Business Example
# 
# A company can replace short department names such as `HR` with `Human Resources`.
# 
# ### AI/ML Example
# 
# In AI/ML, `replace()` can be used to clean and standardize values before model training.
# 
# ### Code Explanation
# 
# `replace("CHN", "Chennai")` changes every `CHN` value into `Chennai`.
# 
# ### Output Explanation
# 
# The `CHN` values in the City column are replaced with `Chennai`.

# In[10]:


import pandas as pd

students = pd.DataFrame({
    "Name": ["Preethi", "Rahul", "Anu"],
    "City": ["CHN", "BLR", "CHN"]
})

students["City"] = students["City"].replace({
    "CHN": "Chennai",
    "BLR": "Bangalore"
})

print(students)


# # Duplicate Handling
# 
# ### Definition
# 
# Duplicate Handling means finding and removing repeated rows from a Pandas DataFrame.
# 
# We use `duplicated()` to find duplicate rows and `drop_duplicates()` to remove them.
# 
# ### Simple Example
# 
# If the same student's details appear twice, we can remove the repeated row.
# 
# ### Real-World Example
# 
# A customer database may contain the same customer record more than once.
# 
# ### Business Example
# 
# A company can remove duplicate customer or sales records before preparing reports.
# 
# ### AI/ML Example
# 
# In AI/ML, duplicate data can affect analysis and model training, so duplicates can be removed during data cleaning.
# 
# ### Code Explanation
# 
# `duplicated()` checks whether a row is repeated.
# 
# `drop_duplicates()` removes the duplicate rows.
# 
# ### Output Explanation
# 
# The duplicate student record is removed, and only unique records remain.

# In[ ]:




