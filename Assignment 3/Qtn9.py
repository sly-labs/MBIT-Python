import re


def extract_emails(text):
    """
    I. Extract all email addresses from the given text.
    Uses a regex pattern to match standard email formats.
    """
    # Pattern: local-part@domain
    # Local part: letters, digits, dots, underscores, hyphens, plus signs
    # Domain: letters, digits, hyphens, dots; TLD: 2+ letters
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails


def validate_date(date_string):
    """
    II. Validate a date in the format "YYYY-MM-DD".
    Checks for valid year (4 digits), month (01-12), day (01-31).
    """
    # Pattern: YYYY-MM-DD with strict digit grouping
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'

    if not re.match(date_pattern, date_string):
        return False

    # Additional validation for realistic dates (optional but robust)
    year, month, day = map(int, date_string.split('-'))

    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False

    # Simple checks for months with 30 days and February
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        # Simplified: assume leap years are divisible by 4 (not perfect, but good enough for basic use)
        if (year % 4 == 0 and day > 29) or (year % 4 != 0 and day > 28):
            return False

    return True


def replace_word(text, old_word, new_word):
    """
    III. Replace all occurrences of a word with another word in a string.
    Uses word boundaries (\b) to ensure only whole words are replaced.
    """
    # \b ensures we match whole words only, not substrings
    pattern = r'\b' + re.escape(old_word) + r'\b'
    replaced_text = re.sub(pattern, new_word, text)
    return replaced_text


def split_by_non_alphanumeric(text):
    """
    IV. Split a string by all non-alphanumeric characters.
    Returns a list of alphanumeric substrings only.
    """
    # Split on any character that is NOT a letter or digit
    parts = re.split(r'[^a-zA-Z0-9]', text)
    # Filter out empty strings
    return [part for part in parts if part]


# Main program demonstrating all four features
if __name__ == "__main__":
    print("=" * 60)
    print("REGULAR EXPRESSIONS DEMONSTRATION")
    print("=" * 60)

    # I. Extract email addresses
    print("\nI. Extracting Email Addresses:")
    sample_text = """
    Contact us at support@example.com or sales@company.org.
    You can also reach out to admin@test-site.net or invalid-email@.
    Another valid one: user.name+tag@domain.co.uk
    """
    emails = extract_emails(sample_text)
    print("Text:", sample_text.strip())
    print("Extracted emails:", emails)

    # II. Validate date in YYYY-MM-DD format
    print("\nII. Validating Date Format (YYYY-MM-DD):")
    test_dates = ["2023-12-25", "2024-02-29", "2023/12/25", "23-12-25", "2023-13-01", "2023-02-30"]
    for date in test_dates:
        is_valid = validate_date(date)
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"{date} -> {status}")

    # III. Replace word with another word
    print("\nIII. Replacing Words:")
    original_text = "The cat sat on the mat. The cat was very happy. Cats love fish."
    old = "cat"
    new = "dog"
    modified_text = replace_word(original_text, old, new)
    print(f"Original: {original_text}")
    print(f"Replaced '{old}' with '{new}': {modified_text}")

    # IV. Split string by non-alphanumeric characters
    print("\nIV. Splitting by Non-Alphanumeric Characters:")
    mixed_string = "Hello, world! How are you? I'm fine. 123abc-def_789"
    split_parts = split_by_non_alphanumeric(mixed_string)
    print(f"Original: {mixed_string}")
    print(f"Split result: {split_parts}")

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)