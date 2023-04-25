#!C:\Python\python.exe
import sqlite3
print("Content-type: text/html")
print()

print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'><title>Datenbank</title></head>")
print("<body>")

connection = sqlite3.connect("sqlite/firma.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM personen")

print("<table style='border:1px solid black;'>")
for name in "Name", "Vorname", "PNr.", "Gehalt", "Geburtstag":
    print(f"<td style='border:1px solid black;'>{name}</td>")
for dsatz in cursor:
    print("<tr>")
    for feld in dsatz:
        print(f"<td style='border:1px solid black;'>{feld}</td>")
    print("</tr>")
print("</table>")

connection.close()
print("</body>")
print("</html>")
