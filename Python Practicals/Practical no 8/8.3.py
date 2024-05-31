'''8.3Write a python programme to raise a user defined exception if
age is less than 18'''
# Define a custom exception
class UnderageException(Exception):
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise UnderageException("Age is less than 18.")
    else:
        print("Age is 18 or above.")

# Example usage
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except UnderageException as e:
    print(f"An error occurred: {e}")
except ValueError:
    print("Please enter a valid integer for age.")
