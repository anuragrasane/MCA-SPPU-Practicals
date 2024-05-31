'''5.9Write a python class and delete object of that class using del keywords.'''
# Define a class named Person
class Person:
    # Define a constructor with name and age parameters
    def __init__(self, name, age):
        # Assign the parameters to the instance attributes
        self.name = name
        self.age = age
    
    # Define a method to print the person details
    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object of the Person class with name "Alice" and age 20
person = Person("Alice", 20)
# Call the print_details() method
person.print_details()

# Delete the object using the del keyword
del person

# Try to call the print_details() method again
person.print_details() # This will cause an error, as the object no longer exists
