'''6.2Python program to check if the string is a valid E-mail address or not
using regex.'''
# import the re module
import re

# define the email pattern
email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# compile the pattern into a regular expression object
email_regex = re.compile(email_pattern)

# check if the email matches the pattern
while True:
    # accept value from user
    email = input("Enter your email address: ")
    if email_regex.match(email):
        print("Valid email address")
        break
    else:
        print("Invalid email address")
