#8.2 Program to check for ValueError Exception.
def check_for_value_error():
    input_string = input("Enter a number: ")
    try:
        # Attempt to convert the string to an integer
        number = int(input_string)
        print(f"The number is: {number}")
    except ValueError:
        # Handle the ValueError exception
        print("That's not a valid number. Please enter a valid integer.")

# Call the function
check_for_value_error()
'''
# Function to convert user input to an integer
def convert_to_integer(user_input):
    try:
        value = int(user_input)
        print("Successfully converted '{}' to an integer: {}".format(user_input, value))
    except ValueError:
        print("Error: '{}' cannot be converted to an integer.".format(user_input))

# Accept user input
user_input = input("Enter a value to convert to an integer: ")

# Convert the input to an integer
convert_to_integer(user_input)
'''
