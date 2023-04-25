#!C:\Python\python.exe
import cgi, cgitb, sys, random, time
cgitb.enable()
random.seed()
form = cgi.FieldStorage()

print("Content-type: text/html")
print()

print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'><title>Aufgaben</title></head>")
print("<body>")
print("<p><b>Kopfrechnen</b></p>")

if not "name" in form:
        print("<p>Kein Name, kein Spiel</p>")
        print("<a href='http://localhost/Python310/spiel_server.htm'>Zurück</a>")
        print("</body>")
        print("</html>")
        sys.exit(0)

print("<form action='spiel_server_b.cgi'>")
print(f"<p>Hallo <b>{form['name'].value}</b>, Ihre Aufgaben</p>")
print("<input name='name' type='hidden' value='" + form["name"].value + "'>")

startzeit = time.time()
print(f"<input name='startzeit' type='hidden' value='{startzeit}'>")

print("<table border='0'>")
for aufgabe in range(5):
        a = random.randint(10,30)
        b = random.randint(10,30)
        c = a + b

        print("<tr>")
        print(f"<td> {aufgabe+1}. </td>")
        print(f"<td> {a} </td>")
        print("<td> + </td>")
        print(f"<td> {b} </td>")
        print("<td> = </td>")
        print(f"<td><input name='ein{aufgabe}' size='12'></td>")
        print("</tr>")

        print(f"<input name='erg{aufgabe}' type='hidden' value='{c}'>")

print("</table>")
print("<p><input type='submit' value='Fertig'></p>")
print("</form>")
print("</body>")
print("</html>")
