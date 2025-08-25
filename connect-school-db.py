import sqlite3

# Connect to the existing database or create if it doesn't exist
conn = sqlite3.connect('school.db')

# Create a cursor object
cursor = conn.cursor()

# 1. Create the table IF it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# 2. Optional: Insert a sample student to test
cursor.execute('''
INSERT INTO students (name, age)
VALUES (?, ?)
''', ("Lynn", 21))

# 3. Select and print all data from the table
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())
