'''13.1Write a Pandas program to add, subtract, multiple and
divide two Pandas Series.'''
import pandas as pd

# Create two Series
series1 = pd.Series([10,20,30,40,50])
series2 = pd.Series([1,2,3,4,5])

# Add the two Series
addition = series1 + series2

# Subtract the second Series from the first
subtraction = series1 - series2

# Multiply the two Series
multiplication = series1 * series2

# Divide the first Series by the second
division = series1 / series2

# Display the results
print("Addition:")
print(addition)
print("\nSubtraction:")
print(subtraction)
print("\nMultiplication:")
print(multiplication)
print("\nDivision:")
print(division)
'''
output:
Addition of two series:
0    11
1    22
2    33
3    44
4    55
dtype: int64

Subtraction of two series:
0     9
1    18
2    27
3    36
4    45
dtype: int64

Multiplication of two series:
0     10
1     40
2     90
3    160
4    250
dtype: int64

Division of two series:
0    10.0
1    10.0
2    10.0
3    10.0
4    10.0
dtype: float64
'''
