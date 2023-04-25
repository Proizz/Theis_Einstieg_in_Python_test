import sqlite3
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM personen ORDER BY gehalt DESC")
for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[3])
print()

cursor.execute("SELECT * FROM personen ORDER BY name, vorname")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

connection.close()
