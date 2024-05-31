'''5.2Write a python program to illustrate a non-parameterized /
default constructor and parameterized constructor.'''
# Define a class named Student
class Student:
    # Define a default constructor
    def __init__(self):
        # Set some default values for the attributes
        self.name = "Unknown"
        self.age = 0
        self.grade = "N/A"

# Create an object of Student class
s1 = Student()

# Print the attributes of s1
print(s1.name) # Unknown
print(s1.age) # 0
print(s1.grade) # N/A

# Define a class named Student
class Student:
    # Define a parameterized constructor
    def __init__(self, name, age, grade):
        # Assign the values of the arguments to the attributes
        self.name = name
        self.age = age
        self.grade = grade

# Create an object of Student class with some arguments
s2 = Student("Alice", 18, "A")

# Print the attributes of s2
print(s2.name) # Alice
print(s2.age) # 18
print(s2.grade) # A

