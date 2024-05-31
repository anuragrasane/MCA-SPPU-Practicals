#5.6Write a python program to overload + Operator.
# Define a class called Point
class Point:
    # Define a constructor with x and y parameters
    def __init__(self, x, y):
        # Assign the parameters to the instance attributes
        self.x = x
        self.y = y
    
    # Define the __add__ method to overload the + operator
    def __add__(self, other):
        # Return a new Point object with the sum of x and y coordinates
        return Point(self.x + other.x, self.y + other.y)
    
    # Define a method to print the Point object
    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Use the + operator with the Point objects
p3 = p1 + p2

# Print the result
print(p3) # Output: (4, 6)
