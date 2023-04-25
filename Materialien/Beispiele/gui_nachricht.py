import tkinter, tkinter.messagebox as mb

def info():
    mb.showinfo("Box","Info")

def warning():
    mb.showwarning("Box","Warnung")

def error():
    mb.showerror("Box","Fehler")

def yesno():
    antwort = mb.askyesno("Box","Ja oder Nein")
    lbAusgabe["text"] = "Ja" if antwort == 1 else "Nein"

def okcancel():
    antwort = mb.askokcancel("Box","OK oder Abbrechen")
    lbAusgabe["text"] = "OK" if antwort == 1 else "Abbrechen"

def retrycancel():
    antwort = mb.askretrycancel("Box","Wiederholen oder Abbrechen")
    lbAusgabe["text"] = "Wiederholen" if antwort == 1 else "Abbrechen"

def frage():
    msg_box = mb.Message(fenster, type=mb.ABORTRETRYIGNORE,
        icon=mb.QUESTION, title="Box",
        message="Abbrechen, Wiederholen oder Ignorieren")
    antwort = msg_box.show()
    if antwort == "abort":
        lbAusgabe["text"] = "Abbrechen"
    elif antwort == "retry":
        lbAusgabe["text"] = "Wiederholen"
    else:
        lbAusgabe["text"] = "Ignorieren"

def ende():
    fenster.destroy()

fenster = tkinter.Tk()

buInfo = tkinter.Button(fenster, text="Info", width=20, command=info)
buInfo.grid(row=0, column=0, padx=5, pady=5)

buWarning = tkinter.Button(fenster, text="Warnung", width=20, command=warning)
buWarning.grid(row=0, column=1, padx=5, pady=5)

buError = tkinter.Button(fenster, text="Fehler", width=20, command=error)
buError.grid(row=0, column=2, padx=5, pady=5)

buYesNo = tkinter.Button(fenster, text="Ja/Nein", width=20, command=yesno)
buYesNo.grid(row=1, column=0, padx=5, pady=5)

buOkCancel = tkinter.Button(fenster, text="OK/Abbrechen",
    width=20, command=okcancel)
buOkCancel.grid(row=1, column=1, padx=5, pady=5)

buRetryCancel = tkinter.Button(fenster, text="Wiederholen/Abbrechen",
   width=20, command=retrycancel)
buRetryCancel.grid(row=1, column=2, padx=5, pady=5)

buFrage = tkinter.Button(fenster, text="Allgemeine Frage",
    width=20, command=frage)
buFrage.grid(row=2, column=0, padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", width=20, command=ende)
buEnde.grid(row=2, column=2, padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster, text="(leer)")
lbAusgabe.grid(row=3, column=1, padx=5, pady=5)

fenster.mainloop()
