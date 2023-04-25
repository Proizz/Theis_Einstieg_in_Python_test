import sqlite3
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

eingabe = input("Bitte den gesuchten Namen eingeben: ")
sql = "SELECT * FROM personen WHERE name LIKE ?"
cursor.execute(sql, (eingabe,))
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

eingabe = input("Bitte den gesuchten Namensteil eingeben: ")
sql = "SELECT * FROM personen WHERE name LIKE ?"
eingabe = '%' + eingabe + '%'
cursor.execute(sql, (eingabe,))
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

connection.close()
