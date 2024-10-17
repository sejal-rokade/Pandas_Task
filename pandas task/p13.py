# DataFrame weather
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | city        | object |
# | month       | object |
# | temperature | int    |
# +-------------+--------+
# Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.

# The result format is in the following example.

# Example 1:
# Input:
# +--------------+----------+-------------+
# | city         | month    | temperature |
# +--------------+----------+-------------+
# | Jacksonville | January  | 13          |
# | Jacksonville | February | 23          |
# | Jacksonville | March    | 38          |
# | Jacksonville | April    | 5           |
# | Jacksonville | May      | 34          |
# | ElPaso       | January  | 20          |
# | ElPaso       | February | 6           |
# | ElPaso       | March    | 26          |
# | ElPaso       | April    | 2           |
# | ElPaso       | May      | 43          |
# +--------------+----------+-------------+
# Output:
# +----------+--------+--------------+
# | month    | ElPaso | Jacksonville |
# +----------+--------+--------------+
# | April    | 2      | 5            |
# | February | 6      | 23           |
# | January  | 20     | 13           |
# | March    | 26     | 38           |
# | May      | 43     | 34           |
# +----------+--------+--------------+
# Explanation:
# The table is pivoted, each column represents a city, and each row represents a specific month.

import pandas as pd

weather=[
    {'city':'Jacksonville',
     'month':'January',
    ' Temperature':'13'
    },
    {'city':'Jacksonville',
     'month':'February',
    ' Temperature':'23'
    },
    {'city':'Jacksonville',
     'month':'March',
    ' Temperature':'38'
    },
    {'city':'Jacksonville',
     'month':'April',
    ' Temperature':'5'
    },
    {'city':'Jacksonville',
     'month':'May',
    ' Temperature':'34'
    },
    {'city':' ElPaso',
     'month':'January',
    ' Temperature':'20'
    },
    {'city':' ElPaso',
     'month':'February',
    ' Temperature':'6'
    },
    {'city':' ElPaso',
     'month':'March',
    ' Temperature':'26'
    },
    {'city':' ElPaso',
     'month':'April',
    ' Temperature':'2'
    },
    {'city':' ElPaso',
     'month':'May',
    ' Temperature':'43'
    }
]

df=pd.DataFrame(weather)
result=df.pivot(index='month',columns='city',values='Temperature')
print(result)