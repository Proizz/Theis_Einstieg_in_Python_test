#!C:\Python\python.exe
import cgi, cgitb

cgitb.enable()
form = cgi.FieldStorage()
if "nn" in form:
    nn = form["nn"].value
if "vn" in form:
    vn = form["vn"].value

print("Content-type: text/html")
print()

print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'><title>Daten empfangen</title></head>")
print("<body>")

print("<p><b>Registrierte Daten:</b></p>")
print("<p>Nachname:", nn, "</p>")
print("<p>Vorname:", vn, "</p>")

print("</body>")
print("</html>")
