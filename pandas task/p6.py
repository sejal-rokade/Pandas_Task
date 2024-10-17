# DataFrame customers
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | customer_id | int    |
# | name        | object |
# | email       | object |
# +-------------+--------+
# There are some duplicate rows in the DataFrame based on the email column.

# Write a solution to remove these duplicate rows and keep only the first occurrence.

# The result format is in the following example.


# Example 1:
# Input:
# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 5           | Finn    | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# +-------------+---------+---------------------+
# Output:  
# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# +-------------+---------+---------------------+
# Explanation:
# Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.


import pandas as pd

customers=[
   {'customer_id':1,
    'name':'Ella',
    'email':'emily@example.com'
 },
   {'customer_id':2,
    'name':'David',
    'email':'m@example.com'
 },
   {'customer_id':3,
    'name':'Zachary',
    'email':'sarah@example.com'
 },
   {'customer_id':4,
    'name':'Alice',
    'email':'john@example.com'
 },
   {'customer_id':5,
    'name':'Finn',
    'email':'john@example.com'
 },
   {'customer_id':6,
    'name':'Violet',
    'email':'Alice@example.com'
 },
 ]
df=pd.DataFrame(customers)
df.drop_duplicates(subset='email',keep='first',inplace=True)
print(df)
    