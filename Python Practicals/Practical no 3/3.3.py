'''3.3 Write a Python program
function that interchanges the firstand last characters of a
given string (accept input from the user).'''
text = input('Enter a string: ')
newtext = text[-1]+text[1:-1]+text[0]
print("Interchanged string:", newtext)

'''def interchange_first_and_last(input_string):
    if len(input_string) < 2:
        print("The input string should have at least 2 characters.")
    else:
        first_char = input_string[0]
        last_char = input_string[-1]
        middle_chars = input_string[1:-1]
        result = last_char + middle_chars + first_char
        print("Interchanged string:", result)

# Accept input from the user
user_input = input("Enter a string: ")
interchange_first_and_last(user_input)'''

