import sqlite3
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

cursor.execute("SELECT name, vorname FROM personen")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

cursor.execute("SELECT * FROM personen WHERE gehalt > 3600")
for dsatz in cursor:
    print(dsatz[0], dsatz[3])
print()

cursor.execute("SELECT * FROM personen WHERE name = 'Schmitz'")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

cursor.execute("SELECT * FROM personen " \
      "WHERE gehalt >= 3600 AND gehalt <= 3650")
for dsatz in cursor:
    print(dsatz[0], dsatz[3])

connection.close()
