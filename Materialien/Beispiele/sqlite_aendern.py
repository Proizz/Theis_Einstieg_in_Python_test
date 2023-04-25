import sqlite3
def ausgabe():
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
    print()

connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
ausgabe()

sql = "UPDATE personen SET gehalt = 3780 WHERE personalnummer = 81343"
cursor.execute(sql)
connection.commit()

ausgabe()
connection.close()
