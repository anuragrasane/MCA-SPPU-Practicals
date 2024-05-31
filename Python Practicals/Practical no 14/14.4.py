'''14.4Write a Pandas program to Delete columns from DataFrame using
Pandas.drop().
'''
import pandas as pd

# Create a sample DataFrame
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']
}
df = pd.DataFrame(data)

# Drop column 'A'
df.drop(['A'], axis=1, inplace=True)

# Display the resulting DataFrame
print(df)
'''
Output
    B   C   D   E
0  B1  C1  D1  E1
1  B2  C2  D2  E2
2  B3  C3  D3  E3
3  B4  C4  D4  E4
4  B5  C5  D5  E5
'''
