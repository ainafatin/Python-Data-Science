# Area (Polymorphism)
                                                    
# Create a base Class Shape and derive the CalAreaSquare, CalAreaRectangle, CalAreaTriangle, CalAreaCircle classes.

# Use the following method in base class Shape:
# Method Name            Description
# area()                 Display the input parmaters

# Calculate area of square in all the derived classes:
# Method Name            Description
# area()                 Find the area of the Square, Rectangle, Triganle and Circle, in their respective derived classes.

# Note: The area of triangle=0.5*base*height
# pi value will be considered as 3.14

# Sample Input and Output Format 1:
# Select an Option
# 1.Square
# 2.Rectangle
# 3.Triangle
# 4.Circle
# 4
# Enter the radius
# 2
# Radius of Circle : 2
# Area of Circle : 12.57

class Shape:

    def __init__(self):
        pass

class CalAreaSquare(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        print(f"Length of Square : {self.length}")
        return self.length ** 2

class CalAreaRectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Length of Rectangle : {self.length}")
        print(f"Breadth of Rectangle : {self.breadth}")
        return self.length * self.breadth

class CalAreaTriangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Base of Triangle : {self.base}")
        print(f"Height of Triangle : {self.height}")
        return 0.5 * self.base * self.height

class CalAreaCircle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Radius of Circle : {self.radius}")
        return 3.14 * (self.radius ** 2)
    
print("Select an Option\n1.Square\n2.Rectangle\n3.Triangle\n4.Circle")
choice = int(input())

if choice == 1:
    length = int(input("Enter the length\n"))
    square = CalAreaSquare(length)
    print(f"Area of Square : {square.area()}")
elif choice == 2:
    length = int(input("Enter the length\n"))
    breadth = int(input("Enter the breadth\n"))
    rectangle = CalAreaRectangle(length, breadth)
    print(f"Area of Rectangle : {rectangle.area()}")
elif choice == 3:
    base = int(input("Enter the base\n"))
    height = int(input("Enter the height\n"))
    triangle = CalAreaTriangle(base, height)
    print(f"Area of Triangle : {triangle.area():.2f}")
elif choice == 4:
    radius = int(input("Enter the radius\n"))
    circle = CalAreaCircle(radius)
    print(f"Area of Circle : {circle.area():.2f}")   