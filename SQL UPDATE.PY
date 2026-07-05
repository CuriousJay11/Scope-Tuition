import sqlite3
conn = sqlite3.connect("updateclause.db")
print("Database Connected")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,name TEXT,marks INTEGER)""")
print("Table is Created")

#Primary key - Column that uniquely identity of each row in a table

cursor.execute("""INSERT INTO students
               (name,marks) VALUES(?,?)""",
               ("Rahul",85)
               )

conn.commit()
print("Before Updation")
cursor.execute("SELECT * FROM STUDENTS")
for row in cursor.fetchall():
   print(row)

# Update Data
cursor.execute("UPDATE students SET marks = 95 WHERE name = 'Rahul'")
conn.commit()

print("After updation")

# Show Data
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

# Close DB
conn.close()