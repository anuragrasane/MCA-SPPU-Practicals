'''#7.4Write a program to demonstrate findall(), split() and sub()
function
'''
import re

# Sample text
text = "The rain in Spain falls mainly in the plain!"

# findall() function example
# Find all occurrences of 'ai' in the text
found = re.findall("ai", text)
print("findall():", found)

# split() function example
# Split the text at every 'ai'
split_text = re.split("ai", text)
print("split():", split_text)

# sub() function example
# Replace every 'ai' with 'XX'
subbed_text = re.sub("ai", "XX", text)
print("sub():", subbed_text)
