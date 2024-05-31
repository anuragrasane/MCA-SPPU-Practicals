'''7.3Write a program to accept any string as input from the user to
Search particular word in given string using search function.'''
import re
'''
# Function to search for a word within a string
def search_word(input_string, word_to_search):
    # Using search function to find the word anywhere in the string
    if re.search(rf"\\b{word_to_search}\\b", input_string):
        return f"The word '{word_to_search}' was found in the string."
    else:
        return f"The word '{word_to_search}' was not found in the string."

# Accepting input from the user
user_input = input("Enter a string: ")
word = input("Enter the word to search: ")

# Calling the function and printing the result
result = search_word(user_input, word)
print(result)


def search_word(input_string, search_word):
    if search_word in input_string:
        return True
    else:
        return False
input_string = input("Enter a string: ")
search_word = input("Enter the word to search: ")
if search_word(input_string, search_word):
    print(f" '{search_word}' found in the input string.")
else:
    print(f" '{search_word}' not found in the input string.")

'''
def search_word_in_string(user_string,search_word):
    index = user_string.find(search_word)
    return index
user_string = input("Enter a String: ")
search_word = input("Enter the word to search for in the string: ")
result =search_word_in_string(user_string, search_word)
print(result)
if result != -1:
    print("'{}' found at index {} in the input string.".format(search_word, result))
else:
    print("'{}' not found in the input string.".format(search_word))
