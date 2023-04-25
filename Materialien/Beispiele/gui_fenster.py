import tkinter

def erzeugeZwei():
    global status, fensterZwei
    if status != "fenster":
        return
    status = "fensterZwei"
    fensterZwei = tkinter.Toplevel(fenster)
    fensterZwei.title("Zwei")
    lbHallo = tkinter.Label(fensterZwei, text="Hallo", width=10)
    lbHallo.grid(row=0, column=0, padx=20, pady=10)
    buEndeZwei = tkinter.Button(fensterZwei, text="Ende Zwei",
        width=10, command=endeZwei)
    buEndeZwei.grid(row=0, column=1, padx=20, pady=10)

def endeZwei():
    global status
    fensterZwei.destroy()
    status = "fenster"

def ende():
    if status == "fenster":
        fenster.destroy()

fenster = tkinter.Tk()
fenster.title("Fenster")
fenster.resizable(0, 0)
status = "fenster"

buZwei = tkinter.Button(fenster, text="Zwei", width=10, command=erzeugeZwei)
buZwei.grid(row=0, column=0, padx=20, pady=10)

buEnde = tkinter.Button(fenster, text="Ende", width=10, command=ende)
buEnde.grid(row=0, column=1, padx=20, pady=10)

fenster.mainloop()
