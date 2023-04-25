#!C:\Python\python.exe
import cgi, cgitb, time, glob, pickle
cgitb.enable()

def hs_lesen():
    global hs_liste
    if not glob.glob("highscore.bin"):
        hs_liste = []
        return
    d = open("highscore.bin", "rb")
    hs_liste = pickle.load(d)
    d.close()

def hs_anzeigen():
    print("<table>")
    print("<tr><td>Platz</td><td>&nbsp;Name&nbsp;</td>"
          "<td align='right'>Zeit</td></tr>")
    for i in range(len(hs_liste)):
        print("<tr>")
        print(f"<td align='right'>{i+1}</td>")
        print(f"<td> {hs_liste[i][0]} </td>")
        print(f"<td align='right'>{hs_liste[i][1]:.2f} sec</td>")
        print("</tr>")
        if i >= 9:
            break
    print("</table>")

def hs_schreiben():
    d = open("highscore.bin","wb")
    pickle.dump(hs_liste,d)
    d.close()

def hs_hinzu(name, zeit):
    gefunden = False
    for i in range(len(hs_liste)):
        if zeit < hs_liste[i][1]:
            hs_liste.insert(i, [name, zeit])
            gefunden = True
            break
    if not gefunden:
        hs_liste.append([name, zeit])

# Programm
form = cgi.FieldStorage()
differenz = round(time.time() - float(form["startzeit"].value), 2)

print("Content-type: text/html")
print()

print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'><title>Auswertung</title></head>")
print("<body>")
print("<p><b>Kopfrechnen</b></p>")

print(f"<p>Hallo <b>{form['name'].value}</b>, Ihr Ergebnis</p>")

richtig = 0
for aufgabe in range(5):
    if f"ein{aufgabe}" in form:
        if form[f"ein{aufgabe}"].value == form[f"erg{aufgabe}"].value:
            richtig += 1

print(f"<p>{richtig} von 5 in {differenz:.2f} Sekunden", end = "")

if richtig == 5:
    print(", Highscore</p>")
    hs_lesen()
    hs_hinzu(form["name"].value, differenz)
    hs_schreiben()
    hs_anzeigen()
else:
    print(", leider kein Highscore</p>")

print("<p><a href='http://localhost/Python310/spiel_server.htm'>Zum Start</a></p>")

print("</body>")
print("</html>")
