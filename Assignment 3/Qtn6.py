def divide_numbers(numerator, denominator):
    """
    Divides two numbers: numerator / denominator.

    Handles:
        - ZeroDivisionError: when denominator is zero
        - TypeError: when either argument is not a number (int or float)

    Parameters:
        numerator: The dividend (should be int or float)
        denominator: The divisor (should be int or float)

    Returns:
        float: The result of the division if successful.
        None: If an error occurs.
    """
    try:
        # Attempt the division
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Both numerator and denominator must be numbers (int or float).")
        return None


# Example usage and test cases
if __name__ == "__main__":
    # Test cases
    print("Testing divide_numbers function:\n")

    # Valid division
    print("1. divide_numbers(10, 2):")
    print(f"Result: {divide_numbers(10, 2)}\n")

    # Division by zero
    print("2. divide_numbers(10, 0):")
    print(f"Result: {divide_numbers(10, 0)}\n")

    # Invalid input types
    print("3. divide_numbers('10', 2):")
    print(f"Result: {divide_numbers('10', 2)}\n")

    print("4. divide_numbers(10, '2'):")
    print(f"Result: {divide_numbers(10, '2')}\n")

    print("5. divide_numbers(None, 5):")
    print(f"Result: {divide_numbers(None, 5)}\n")

    # Valid float division
    print("6. divide_numbers(7.5, 2.5):")
    print(f"Result: {divide_numbers(7.5, 2.5)}\n")