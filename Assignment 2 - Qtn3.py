class Shape:
    def __init__(self):
        print("Shape constructor called")
        self.name = "Shape"

    def calculate_area(self):
        # Base class method, may be overridden
        print("Area calculation not defined for generic shape.")
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        # Call the parent class constructor using super()
        super().__init__()
        self.length = length
        self.width = width
        self.name = "Rectangle"

    def calculate_area(self):
        # Override calculate_area, but we're not calling super() here
        # because Shape's version isn't useful for area calculation.
        # However, we *did* use super() in __init__ to reuse initialization logic.
        return self.length * self.width


# Example usage:
rect = Rectangle(5, 3)
print(f"Name: {rect.name}")
print(f"Area: {rect.calculate_area()}")  # Output: 15

"""
Explanation:
super().__init__() is used in Rectangle.__init__() to ensure the Shape class's initialization logic runs (e.g., setting name, printing message).
The calculate_area() method in Rectangle overrides the one in Shape and computes the correct area.
We do not call super().calculate_area() inside Rectangle.calculate_area() because the base version returns 0 and is not useful—but we could if we wanted to extend rather than replace behavior.
The key point: super() is used in the constructor (__init__), not in calculate_area(), to reuse parent initialization.
"""