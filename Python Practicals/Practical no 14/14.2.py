'''14.2Write a Pandas program to print a concise summary of
the dataset.'''
import pandas as pd

# Load your dataset
df = pd.read_csv('data.csv')  # or pd.read_excel for Excel files

# Print a concise summary of the DataFrame
df.info()
'''
output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  169 non-null    int64  
 1   Pulse     169 non-null    int64  
 2   Maxpulse  169 non-null    int64  
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
'''
