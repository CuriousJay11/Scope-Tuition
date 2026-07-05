import sqlite3

conn = sqlite3.connect("library.db")
print("Database Connected")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    pages INTEGER
)
""")
print("Table is Created")

cursor.execute("DELETE FROM books")

Books = [
    ("Harry Potter Order of the Pheonix", 500),
    ("The Hobbit", 310),
    ("Percy Jackson Lighting Thief", 328),
    ("The Alchemist", 208)
]

cursor.executemany("""
INSERT INTO books (title, pages)
VALUES (?, ?)
""", Books)

conn.commit()

# COUNT Function
cursor.execute("SELECT COUNT(*) FROM books")
print("Total Books:")
print(cursor.fetchone()[0])

# AVG Function
cursor.execute("SELECT AVG(pages) FROM books")
print("Average Pages:")
print(cursor.fetchone()[0])

# MAX Function
cursor.execute("SELECT MAX(pages) FROM books")
print("Maximum Pages:")
print(cursor.fetchone()[0])

# MIN Function
cursor.execute("SELECT MIN(pages) FROM books")
print("Minimum Pages:")
print(cursor.fetchone()[0])

# SUM Function
cursor.execute("SELECT SUM(pages) FROM books")
print("Total Pages:")
print(cursor.fetchone()[0])

conn.close()