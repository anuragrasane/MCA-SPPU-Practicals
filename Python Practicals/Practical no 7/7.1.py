'''7.1Write a program to accept input from the user contains only
letters, spaces.
Any other character is not allowed, using compile function.'''
import re

# Compile a regular expression that matches only letters and spaces
pattern = re.compile(r'^[a-zA-Z\s]*$')

# Accept input from the user
user_input = input("Enter a string: ")

# Check if the input matches the pattern
if pattern.match(user_input):
    print("The input is valid.")
else:
    print("The input is not valid. It should contain only letters and spaces.")
