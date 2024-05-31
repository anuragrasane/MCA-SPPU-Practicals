'''6.1Write a python program for password validation using Regular Expression,
consider following condition:
• Minimum length of password: 8 characters.
• At least one alphabet must between [a-z].
• At least one alphabet should be of Upper Case [A-Z]. At least 1 number
or digit between [0-9].
• At least 1 character from [$, @, # ]. '''
# import the re module
import re

# define the password pattern
password_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$@#])[A-Za-z0-9$@#]{8,}$"

# compile the pattern into a regular expression object
password_regex = re.compile(password_pattern)

# check if the password matches the pattern
while True:
    # accept value from user
    password = input("Enter your password: ")
    if password_regex.match(password):
        print("Valid password")
        break
    else:
        print("Invalid password")
