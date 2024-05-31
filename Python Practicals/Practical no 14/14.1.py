'''14.1Write a Pandas program to add summation to a row of the
given excel file.'''

import pandas as pd

# Read the Excel file
df = pd.read_excel('Book2.xlsx')

# Calculate the sum of "Production" and "Labor_Hours"
# Use a list of column names to select multiple columns
sum_row = df[['Production', 'Labor_Hours']].sum()

# Create a DataFrame with the sum
# Use 'sum_row' to create a new DataFrame and transpose it with .T
df_sum = pd.DataFrame([sum_row])

# Reindex the columns of the new DataFrame to match the original DataFrame
df_sum = df_sum.reindex(columns=df.columns)

# Display the corrected DataFrame
print(df_sum)
