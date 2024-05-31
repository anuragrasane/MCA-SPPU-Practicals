'''12.3Write a NumPy program to create a structured array from
given student name, height, class and their data types. Now sort
the array on height.'''
import numpy as np

# Define student data types
dt = np.dtype([('name', 'U20'), ('height', float), ('class', int)])

# Create a structured array
students = np.array([('Alice', 165.5, 10),
                     ('Bob', 172.0, 9),
                     ('Charlie', 158.2, 11)],
                    dtype=dt)

# Sort the array by height
sorted_students = np.sort(students, order='height')

print("Structured array of students:")
print(sorted_students)
