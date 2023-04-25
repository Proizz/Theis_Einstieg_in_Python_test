import sqlite3
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM personen WHERE name LIKE 'm%'")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

cursor.execute("SELECT * FROM personen WHERE name LIKE '%i%'")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

cursor.execute("SELECT * FROM personen WHERE name LIKE 'M__er'")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

connection.close()
