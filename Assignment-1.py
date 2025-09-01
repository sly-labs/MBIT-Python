#This ia a python code snippet that demonstrates the use of variables, constants & the print function.

# Variables - values that can be changed
name = "Slyvester"
age = 37
height = 1.75
is_student = True

# Constants - values that should not be changed (conventionally uppercase)
PI = 3.14159
GRAVITY = 9.8
MAX_USERS = 100

# Using the print function to display values
print("Person Information:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Is student: {is_student}")

# Using constants in calculations
radius = 5
circle_area = PI * radius ** 2
print(f"Area of circle with radius {radius}: {circle_area}")

# Demonstrating variable modification
age += 1  # Increment age by 1
print(f"Next year, {name} will be {age} years old")

# Printing multiple values
print("Constants:", PI, GRAVITY, MAX_USERS)