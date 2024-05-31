'''14.3Write a Pandas program to detect missing values of a given
DataFrame. Display True or False.'''
import pandas as pd

# Load your dataset
df = pd.read_csv('nba.csv')  # or pd.read_excel for Excel files

# Detect missing values and display True or False
missing_values = df.isnull()
print(missing_values)
'''
output
      Name   Team  Number  Position    Age  Height  Weight  College  Salary
0    False  False   False     False  False   False   False    False   False
1    False  False   False     False  False   False   False    False   False
2    False  False   False     False  False   False   False    False    True
3    False  False   False     False  False   False   False    False   False
4    False  False   False     False  False   False   False     True   False
..     ...    ...     ...       ...    ...     ...     ...      ...     ...
452  False  False   False     False  False   False   False    False   False
453  False  False   False     False  False   False   False    False   False
454  False  False   False     False  False   False   False     True   False
455  False  False   False     False  False   False   False     True   False
456  False  False   False     False  False   False   False    False   False

[457 rows x 9 columns]
'''
