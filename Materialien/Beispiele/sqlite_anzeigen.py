import sqlite3
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
sql = "SELECT * FROM personen"
cursor.execute(sql)

for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[2],
          dsatz[3], dsatz[4])
connection.close()
