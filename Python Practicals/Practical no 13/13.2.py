'''13.2Write a Pandas program to compare the elements of the two Pandas
Series.'''
import pandas as pd

# Create two Series
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

# Compare the elements of the two Series
comparison = {
    "Greater": series1 > series2,
    "Lesser": series1 < series2,
    "Equal": series1 == series2
}

# Display the comparison results
print("Comparison of two series:")
for key, value in comparison.items():
    print(f"{key}:\n{value}\n")
