import sqlite3

conn = sqlite3.connect("Sales.db")
print("Database Connected")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Items (
    id INTEGER PRIMARY KEY,
    CustomerOrder TEXT,
    Quantity INTERGER,
    Bill INTEGER,
    ProductDetails TEXT
)
""")
print("Table is Created")

cursor.execute("DELETE FROM Items")

Patients = [
    ("LED Strip", 2 , 998, "RGB 3M Light Strips"),
    ("Mouse Pad", 1 , 1200, "Minecraft Themed Bees Mouse Pad"),
    ("Neon Signs", 4 , 1359,"Decor for Birthday,Gaming,Living, Aesthetic"),
    ("Extension Cord", 2 , 499, "6 Port 1M Extesnion Cord")
]

cursor.executemany("""
INSERT INTO Items (CustomerOrder, Quantity, Bill, ProductDetails)
VALUES (?, ?,?, ? )
""", Patients)

conn.commit()

cursor.execute("SELECT * FROM Items ORDER BY Bill DESC")
data = cursor.fetchall()
print(data)
for row in data :
    print(row)

cursor.execute("UPDATE Items SET Quantity = 3 WHERE CustomerOrder = 'Neon Signs'")
conn.commit()
