# List of names to write to the file
names = [
    "Alice Johnson",
    "Bob Smith",
    "Carol Davis",
    "David Wilson",
    "Eve Brown"
]

# Write names to names.txt (one per line)
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
    print(f"Successfully wrote {len(names)} names to 'names.txt'.")

# Read names from names.txt and print to console
print("\nReading names from 'names.txt':")
with open("names.txt", "r") as file:
    for line in file:
        # Strip newline characters and print each name
        print(line.strip())