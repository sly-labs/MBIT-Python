def calculate_average(*args):
    """
    Calculate the average of a variable number of numeric arguments.

    Parameters:
    *args : variable number of numeric arguments (int or float)

    Returns:
    float or None: The average of the provided numbers. Returns None if no arguments are provided.
    """
    if not args:
        return None
    total = sum(args)
    count = len(args)
    return total / count


def get_user_numbers():
    """
    Prompts the user to enter numbers separated by spaces and returns them as a list of floats.
    Handles invalid input by asking the user to try again.
    """
    while True:
        try:
            user_input = input("Enter numbers separated by spaces: ")
            numbers = [float(x) for x in user_input.split()]
            return numbers
        except ValueError:
            print("Invalid input. Please enter numbers only, separated by spaces.")


# Get numbers from user
user_numbers = get_user_numbers()

# Calculate and display results
if user_numbers:
    average = calculate_average(*user_numbers)
    count = len(user_numbers)
    total = sum(user_numbers)

    print("\nResults:")
    print(f"Input values: {user_numbers}")
#    print(f"Count: {count}")
#    print(f"Total: {total}")
    print(f"Average: {average}")
else:
    print("No numbers were entered.")