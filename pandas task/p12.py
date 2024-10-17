# DataFrame df1
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

# DataFrame df2
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

# Write a solution to concatenate these two DataFrames vertically into one DataFrame.

# The result format is in the following example.

# Example 1:

# Input:
# df1
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 1          | Mason   | 8   |
# | 2          | Ava     | 6   |
# | 3          | Taylor  | 15  |
# | 4          | Georgia | 17  |
# +------------+---------+-----+
# df2
# +------------+------+-----+
# | student_id | name | age |
# +------------+------+-----+
# | 5          | Leo  | 7   |
# | 6          | Alex | 7   |
# +------------+------+-----+
# Output:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 1          | Mason   | 8   |
# | 2          | Ava     | 6   |
# | 3          | Taylor  | 15  |
# | 4          | Georgia | 17  |
# | 5          | Leo     | 7   |
# | 6          | Alex    | 7   |
# +------------+---------+-----+
# Explanation:
# The two DataFramess are stacked vertically, and their rows are combined.

import pandas as pd

df1=[
    {
        'student_id':1,
        'name':'Mason',
        'age':8
    },
    {
        'student_id':2,
        'name':'Ava',
        'age':6
    },
    {
        'student_id':3,
        'name':'Taylor',
        'age':15
    },
    {
        'student_id':4,
        'name':'Grorgia',
        'age':17
    },
]

df2=[
    {
        'student_id':5,
        'name':'Leo',
        'age':7
    },
    {
        'student_id':6,
        'name':'Alex',
        'age':7
    }, 
]

df1=pd.DataFrame(df1)
df2=pd.DataFrame(df2)
df=pd.concat([df1,df2],axis=0)            #(0 for vertically & 1 for Horizontally)
print(df)







