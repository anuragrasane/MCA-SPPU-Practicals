'''5.4Create one base class named Shape and two child classes namely Rect and Tri.
Both classes inherit the displayO function from the Shape class to print the
length and breadth.
In Rect class, we find the area of the rectangle while in Tri class we find the
area of the triangle using two different functions R_area and T_area.
'''
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

