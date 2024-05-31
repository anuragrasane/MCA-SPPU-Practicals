'''13.4Write a Pandas program to create and display a DataFrame
from a specified dictionary data which has the index labels.'''
import pandas as pd

# Define a dictionary
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

# Define the index labels
index_labels = ['a', 'b', 'c', 'd']

# Create a DataFrame using the dictionary and the index labels
df = pd.DataFrame(data, index=index_labels)

# Display the DataFrame
print(df)
