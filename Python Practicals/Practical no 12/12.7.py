'''12.7Write a NumPy program to capitalize the first letter, lowercase,
uppercase, swapcase, title-case of all the elements of
a given array.'''
import numpy as np

# Create a sample array
arr = np.array(['hello', 'WORLD', 'NumPy', 'is', 'awesome'])

# Capitalize the first letter of each element
capitalized_arr = np.char.capitalize(arr)
print("Capitalized array:")
print(capitalized_arr)

# Convert all elements to lowercase
lowercase_arr = np.char.lower(arr)
print("\nLowercase array:")
print(lowercase_arr)

# Convert all elements to uppercase
uppercase_arr = np.char.upper(arr)
print("\nUppercase array:")
print(uppercase_arr)

# Swap the case of all elements
swapcase_arr = np.char.swapcase(arr)
print("\nSwapcase array:")
print(swapcase_arr)

# Convert all elements to title-case
titlecase_arr = np.char.title(arr)
print("\nTitle-case array:")
print(titlecase_arr)
