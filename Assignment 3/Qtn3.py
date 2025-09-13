def get_valid_number():
    """
    Prompts the user to enter a valid number until a valid input is provided.
    Handles ValueError exceptions for invalid inputs.
    """
    while True:
        try:
            user_input = input("Please enter a number: ")
            number = float(user_input)  # Using float to accept both integers and decimals
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid number (e.g., 42, -3.14, or 0.5).")

# Main program
if __name__ == "__main__":
    print("=== Number Input Validator ===")
    valid_number = get_valid_number()
    print(f"Thank you! You entered: {valid_number}")