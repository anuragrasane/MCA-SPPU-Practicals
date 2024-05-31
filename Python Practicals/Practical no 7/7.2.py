'''7.2Write a program to accept any string as input from the user to
match particular word in giver string using match function.'''
import re

# Function to match a word at the beginning of a string
def match_word(input_string, word_to_match):
    ''' Using match function to check if the word is at the beginning
    of the string'''
    if re.match(rf"\b{word_to_match}\b", input_string):
        return f"The word '{word_to_match}' is at the beginning of the string."
    else:
        return f"The word '{word_to_match}' is not at the beginning of the string."

# Accepting input from the user
user_input = input("Enter a string: ")
word = input("Enter the word to match: ")

# Calling the function and printing the result
result = match_word(user_input, word)
print(result)
            
