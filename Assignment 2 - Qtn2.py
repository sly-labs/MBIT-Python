# A solution that demonstrates polymorphism by calculating the total area of different shapes:
from abc import ABC, abstractmethod
import math


# Abstract base class for all shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of circle: π × r²"""
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"


# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle: width × height"""
        return self.width * self.height

    def __str__(self):
        return f"Rectangle {self.width}×{self.height}"


# Square class (special case of rectangle)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square with side {self.width}"


# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """Calculate area of triangle: (base × height) / 2"""
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Triangle with base {self.base} and height {self.height}"


# Function to calculate total area using polymorphism
def calculate_total_area(shapes):
    """
    Calculate the total area of all shapes in the list.
    Uses polymorphism - calls the area() method on each shape
    regardless of its specific type.
    """
    if not shapes:
        return 0

    total_area = 0
    for shape in shapes:
        # Polymorphism: each shape's area() method is called
        # The correct implementation is automatically used based on the object type
        total_area += shape.area()

    return total_area


# Alternative implementation using sum() and generator expression
def calculate_total_area_compact(shapes):
    """Compact version using sum() and generator expression"""
    return sum(shape.area() for shape in shapes)


# Example usage
if __name__ == "__main__":
    # Create a list of different shapes
    shapes = [
        Circle(5),  # Circle with radius 5
        Rectangle(4, 6),  # Rectangle 4×6
        Square(3),  # Square with side 3
        Triangle(4, 8),  # Triangle with base 4, height 8
        Circle(2),  # Circle with radius 2
        Rectangle(5, 3)  # Rectangle 5×3
    ]

    # Calculate total area
    total = calculate_total_area(shapes)

    # Display results
    print("Shapes and their areas:")
    print("-" * 40)

    for shape in shapes:
        print(f"{shape}: {shape.area():.2f}")

    print("-" * 40)
    print(f"Total area of all shapes: {total:.2f}")

    # Verify with compact version
    total_compact = calculate_total_area_compact(shapes)
    print(f"Total area (compact version): {total_compact:.2f}")

    # Demonstrate polymorphism
    print("\n--- Polymorphism Demonstration ---")
    print("Each shape uses its own area() implementation:")
    for shape in shapes:
        print(f"{type(shape).__name__}: {shape.area():.2f}")

"""
Key Concepts Demonstrated:
Polymorphism: The calculate_total_area() function works with any object that has an area() method, regardless of its specific type.
Abstract Base Class: Shape is an abstract class that defines the interface (area method) that all concrete shapes must implement.
Method Overriding: Each shape class provides its own implementation of the area() method.
Duck Typing: Python calls the appropriate area() method based on the object's type at runtime.
Extensibility: You can easily add new shape classes (like Pentagon, Hexagon, etc.) without modifying the calculate_total_area() function.
The function demonstrates the power of polymorphism - it doesn't need to know what type of shape each object is; it just calls the area() method and trusts that each object will calculate its area correctly according to its own implementation.
"""