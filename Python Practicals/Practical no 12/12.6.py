'''12.6Write a NumPy program to concatenate element-wise two arrays of
string.'''
import numpy as np

# Create two arrays of strings
arr1 = np.array(["Hello", "World"])
arr2 = np.array(["!", "Python"])

# Concatenate element-wise
result = np.core.defchararray.add(arr1, arr2)

print(result)
