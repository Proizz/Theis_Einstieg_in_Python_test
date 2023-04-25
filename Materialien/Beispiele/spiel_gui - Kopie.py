import time, random, glob, sqlite3, tkinter, tkinter.messagebox as mb

def auswertung():
    if status != "fenster":
        return

    differenz = time.time() - startzeit
    richtig = 0
    for i in range(5):
        try:
            if int(eingabeListe[i].get()) == ergebnisListe[i]:
                richtig += 1
        except:
            pass

    if richtig < 5:
        mb.showinfo("Kein Highscore", "Leider kein Highscore")
        fenster.destroy()
        return
    
    if not glob.glob("spiel_gui_highscore.db"):
        con = sqlite3.connect("spiel_gui_highscore.db")
        cursor = con.cursor()
        sql = "CREATE TABLE daten(name TEXT, zeit REAL)"
        cursor.execute(sql)
        con.close()

    con = sqlite3.connect("spiel_gui_highscore.db")
    cursor = con.cursor()
    sql = f"INSERT INTO daten VALUES(?,{differenz})"
    cursor.execute(sql, (lbName["text"], ))
    con.commit()
    con.close()

    con = sqlite3.connect("spiel_gui_highscore.db")
    cursor = con.cursor()
    sql = "SELECT * FROM daten ORDER BY zeit LIMIT 10"
    cursor.execute(sql)

    ausgabe = ""
    i = 1
    for dsatz in cursor:
        ausgabe += f"{i}. {dsatz[0]} {round(dsatz[1],2)} sec.\n"
        i += 1
    mb.showinfo("Highscore", ausgabe)
    con.close()
    fenster.destroy()

def start():
    global startzeit, status
    lbName["text"] = enName.get()
    startzeit = time.time()
    status = "fenster"
    fensterNeu.destroy()

# Programm
fenster = tkinter.Tk()
fenster.title("Kopfrechnen")
fenster.resizable(0, 0)

lbName = tkinter.Label(fenster, text="(Spielername)")
lbName.grid(row=0, column=0, columnspan=6, pady=10)

eingabeListe = []
ergebnisListe = []
for i in range(5):
    a = random.randint(10,30)
    b = random.randint(10,30)
    ergebnisListe.append(a + b)

    tkinter.Label(fenster, text=f"Aufgabe {i+1}:").grid(
        row=i+1, column=0, padx=10, pady=5)
    tkinter.Label(fenster, text=a).grid(row=i+1, column=1, pady=5)
    tkinter.Label(fenster, text="+").grid(row=i+1, column=2, pady=5)
    tkinter.Label(fenster, text=b).grid(row=i+1, column=3, pady=5)
    tkinter.Label(fenster, text="=").grid(row=i+1, column=4, pady=5)

    enErgebnis = tkinter.Entry(fenster)
    enErgebnis.grid(row=i+1, column=5, padx=10, pady=5)
    eingabeListe.append(enErgebnis)

buAuswertung = tkinter.Button(fenster, text="Fertig", width=10, command=auswertung)
buAuswertung.grid(row=6, column=0, columnspan=6, pady=10)

# Neues Fenster
fensterNeu = tkinter.Toplevel(fenster)
fensterNeu.title("Ihr Name:")

lbNameNeu = tkinter.Label(fensterNeu, text="Ihr Name:")
lbNameNeu.grid(row=0, column=0, pady=10)

enName = tkinter.Entry(fensterNeu)
enName.grid(row=1, column=0, padx=10, pady=10)

buStart = tkinter.Button(fensterNeu, text="Start", width=10, command=start)
buStart.grid(row=2, column=0, padx=10, pady=10)

status="fensterNeu"

# Starten
fenster.mainloop()
