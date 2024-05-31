'''5.3Create Shape parent class and Rect is the child class. In parent class,
we have one function to display which displays the length and breadth of the
rectangle. And in the child class, we have defined the function areal to find
the area of the rectangle and print the output.'''
class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def display(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)


class Rect(Shape):
    def R_area(self):
        area = self.length * self.breadth
        print("Area of Rectangle:", area)


class Tri(Shape):
    def T_area(self):
        area = 0.5 * self.length * self.breadth
        print("Area of Triangle:", area)


# Creating objects and calling functions
rect = Rect(5, 10)
print("Rectangle:")
rect.display()
rect.R_area()

print("\nTriangle:")
tri = Tri(6, 12)
tri.display()
tri.T_area()

