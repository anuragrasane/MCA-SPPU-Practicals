#8.1 Program to check for ZeroDivisionError Exception.
'''
import os

# Function to get the file size
def get_file_size(file_path):
    try:
        # Get the size of the file in bytes
        size = os.path.getsize(file_path)
        return f"The size of the file is: {size} bytes"
    except OSError as e:
        return f"Error: {e}"

# Replace 'yourfile.txt' with the path to your text file
file_path = 'yourfile.txt'
print(get_file_size(file_path))
'''
# Function to perform division and handle ZeroDivisionError
def perform_division(dividend, divisor):
    try:
        result = dividend / divisor
        print("Result of division: {}".format(result))
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Input for the dividend and divisor
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

# Perform the division operation
perform_division(dividend, divisor)
