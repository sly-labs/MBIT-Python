# Define custom exception class
class NegativeNumberError(Exception):
    """Exception raised when a negative number is encountered."""

    def __init__(self, number, message="Negative numbers are not allowed"):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.number}"


# Function that raises NegativeNumberError if the number is negative
def check_positive(number):
    """
    Checks if a number is positive.

    Args:
        number: A numeric value (int or float)

    Raises:
        NegativeNumberError: If the number is less than zero

    Returns:
        bool: True if the number is positive or zero
    """
    if number < 0:
        raise NegativeNumberError(number)
    return True


# Demonstration using try-except block
if __name__ == "__main__":
    test_numbers = [10, 0, -5, 3.14, -100, 42]

    print("Testing check_positive function:\n")

    for num in test_numbers:
        try:
            check_positive(num)
            print(f"✓ {num} is valid (positive or zero)")
        except NegativeNumberError as e:
            print(f"✗ {e}")  # Uses the custom error message from __str__