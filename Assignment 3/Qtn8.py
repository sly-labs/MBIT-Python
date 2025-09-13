import random


def generate_random_integers(count, min_val, max_val):
    """
    Generate a list of random integers within a specified range.

    Parameters:
        count (int): Number of random integers to generate
        min_val (int): Minimum value (inclusive)
        max_val (int): Maximum value (inclusive)

    Returns:
        list: List of random integers
    """
    return [random.randint(min_val, max_val) for _ in range(count)]


def calculate_average(numbers):
    """
    Calculate the arithmetic average of a list of numbers.

    Parameters:
        numbers (list): List of numeric values

    Returns:
        float: The average of the numbers
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def main():
    """Main function to orchestrate the program flow."""
    # Parameters
    COUNT = 10
    MIN_VAL = 1
    MAX_VAL = 100

    # Generate random integers
    random_numbers = generate_random_integers(COUNT, MIN_VAL, MAX_VAL)

    # Calculate average
    average = calculate_average(random_numbers)

    # Print results
    print(f"Generated {COUNT} random integers between {MIN_VAL} and {MAX_VAL}:")
    print(random_numbers)
    print(f"\nAverage of these numbers: {average:.2f}")


# Run the program
if __name__ == "__main__":
    main()