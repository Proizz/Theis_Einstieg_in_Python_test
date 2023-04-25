#!C:\Python\python.exe
import cgi, cgitb

cgitb.enable()
form = cgi.FieldStorage()

print("Content-type: text/html")
print()
print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'><title>Daten empfangen</title></head>")
print("<body>")

if "nn" in form:
    print("<p><b>Registrierte Daten:</b></p>")
    print("<p>Nachnamen:<br />")
    try:
        print(form["nn"].value)
    except:
        for element in form["nn"]:
            print(element.value, "<br />")
    print("</p>")
else:
    print("<p><b>Keine Daten gesendet</b></p>")

print("</body>")
print("</html>")
