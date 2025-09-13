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