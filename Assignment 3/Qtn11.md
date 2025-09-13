What is an API? How to make a GET request using the requests library
✅ What is an API?
An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. In web development, an HTTP API typically exposes endpoints (URLs) that return data (often in JSON or XML format) when requested.

For example:

A weather app might use a weather service’s API to get current temperature data.
A mobile app might use a social media API to fetch user posts.
Common types:

REST APIs: Use standard HTTP methods like GET, POST, PUT, DELETE.
GraphQL APIs: Allow clients to request exactly the data they need.
✅ Making a GET Request with requests
The requests library is the most popular Python library for making HTTP requests.

Step-by-step: Make a GET request
import requests

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Send a GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)

    # Parse the JSON response
    data = response.json()

    # Print the result
    print("Title:", data['title'])
    print("Body:", data['body'])

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


2. Connecting to a SQLite Database Using Python
SQLite is a lightweight, serverless, file-based relational database engine. Python has built-in support via the sqlite3 module — no external installation needed.

✅ Purpose of Connecting to SQLite
To store, retrieve, update, or delete structured data (like user info, logs, settings) in a persistent, SQL-compatible way — ideal for small to medium applications.

🔧 Step-by-Step: Connect and Interact with SQLite
import sqlite3

# Step 1: Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('example.db')

try:
    # Step 2: Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Step 3: Create a table (if it doesn't exist)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE
        )
    ''')
    print("Table 'users' created or already exists.")

    # Step 4: Insert sample data
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                   ("Alice", "alice@example.com"))
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                   ("Bob", "bob@example.com"))
    conn.commit()  # Save changes to the database
    print("Sample data inserted.")

    # Step 5: Query data
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    print("\nUsers in database:")
    for row in rows:
        print(row)

    # Step 6: Update data (optional)
    cursor.execute("UPDATE users SET email = ? WHERE name = ?",
                   ("alice.new@example.com", "Alice"))
    conn.commit()
    print("\nUser email updated.")

    # Step 7: Query again to verify
    cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
    updated_row = cursor.fetchone()
    print("Updated user:", updated_row)

finally:
    # Step 8: Close the connection
    conn.close()
    print("\nDatabase connection closed.")