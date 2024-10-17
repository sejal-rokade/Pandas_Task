# DataFrame: employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | employee_id | int    |
# | name        | object |
# | department  | object |
# | salary      | int    |
# +-------------+--------+
# Write a solution to display the first 3 rows of this DataFrame.


# Example 1:

# Input:
# DataFrame employees
# +-------------+-----------+-----------------------+--------+
# | employee_id | name      | department            | salary |
# +-------------+-----------+-----------------------+--------+
# | 3           | Bob       | Operations            | 48675  |
# | 90          | Alice     | Sales                 | 11096  |
# | 9           | Tatiana   | Engineering           | 33805  |
# | 60          | Annabelle | InformationTechnology | 37678  |
# | 49          | Jonathan  | HumanResources        | 23793  |
# | 43          | Khaled    | Administration        | 40454  |
# +-------------+-----------+-----------------------+--------+
# Output:
# +-------------+---------+-------------+--------+
# | employee_id | name    | department  | salary |
# +-------------+---------+-------------+--------+
# | 3           | Bob     | Operations  | 48675  |
# | 90          | Alice   | Sales       | 11096  |
# | 9           | Tatiana | Engineering | 33805  |
# +-------------+---------+-------------+--------+
# Explanation: 
# Only the first 3 rows are displayed.




import pandas as pd
employees=[
    {'employee_id':3,
     'name':'Bob',
     'department':'operations',
     'salary':48675
},
    {'employee_id':90,
     'name':'Alice',
     'department':'sales',
     'salary':11096
},
    {'employee_id':9,
     'name':'Tatiana',
     'department':'Engineering',
     'salary':33805
},
    {'employee_id':60,
     'name':'Annabelle',
     'department':'Information Technology',
     'salary':37678
},
 {'employee_id':49,
     'name':'Jonathan',
     'department':'Human Resources',
     'salary':23793
},
 {'employee_id':43,
     'name':'Khaled',
     'department':'Administration',
     'salary':40454
},
]

userdf=pd.DataFrame(employees)
result=userdf.iloc[0:3]
print(result)



