import sqlite3
conn = sqlite3.connect("schools.db")
print("Database Connected")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,name TEXT,marks INTEGER)""")
print("Table is Created")

cursor.execute("DELETE FROM students")

Students = [("Alex",85),("Steve",90),("Kai",100),("Connor",95)]

cursor.executemany("""INSERT INTO students
               (name,marks) VALUES(?,?)""",
               Students
               )

conn.commit()
#   Count FUNCTION

cursor.execute("SELECT COUNT (*) FROM Students")
print("Total Students")
print(cursor.fetchone()[0])

#Average FUNCTION

cursor.execute("SELECT AVG (marks) FROM Students")
print("Avg Students")
print(cursor.fetchone()[0])


cursor.execute("SELECT MAX(marks) FROM Students")
print("Highest marks:")
print(cursor.fetchone()[0])

# MIN fn
cursor.execute("SELECT MIN(marks) FROM Students")
print("Lowest marks:")
print(cursor.fetchone()[0])

# SUM fn
cursor.execute("SELECT SUM(marks) FROM Students")
print("Total marks:")
print(cursor.fetchone()[0])

conn.close()