# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

# Write a solution to select the name and age of the student with student_id = 101.

# The result format is in the following example.

# Example 1:
# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 101        | Ulysses | 13  |
# | 53         | William | 10  |
# | 128        | Henry   | 6   |
# | 3          | Henry   | 11  |
# +------------+---------+-----+
# Output:
# +---------+-----+
# | name    | age | 
# +---------+-----+
# | Ulysses | 13  |
# +---------+-----+
# Explanation:
# Student Ulysses has student_id = 101, we select the name and age.




import pandas as pd
students=[
    {'student_id':101,
     'name':'ulysses',
     'age':13
},
    {'student_id':53,
     'name':'william',
     'age':10
},
    {'student_id':128,
     'name':'Henry',
     'age':6
},
    {'student_id':3,
     'name':'Henry',
     'age':11
},
]

df=pd.DataFrame(students)
result=df.loc[df['student_id']==101,['name','age']]
print(result)