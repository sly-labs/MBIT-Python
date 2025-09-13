'''This function:
Uses a while True loop to repeatedly prompt the user for input
Attempts to convert the input to an integer using int()
If conversion fails (raises ValueError), catches the exception and prints an error message, then loops again
When a valid integer is entered, breaks out of the loop
Classifies the number as "Positive", "Negative", or "Zero" based on its value
Returns the appropriate string
The function handles invalid inputs gracefully by continuing to prompt until a valid integer is provided.
'''

def classify_number():
    while True:
        try:
            user_input = input("Enter an integer: ")
            number = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


# Example usage (optional - for testing):
if __name__ == "__main__":
    result = classify_number()
    print(result)