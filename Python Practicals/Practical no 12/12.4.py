'''12.4Write a NumPy program, Find the indexes from given array where
the values are odd.'''
import numpy as np

# Example array
my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Find the indexes of odd values
odd_indexes = np.where(my_array % 2 != 0)

print("Indexes of odd values:")
print(odd_indexes)
print(type(odd_indexes))
