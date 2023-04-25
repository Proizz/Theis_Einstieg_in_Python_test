import os, time
tu = os.stat("formatiert.txt")
print("Anzahl Byte:", tu[6])
print("Letzter Zugriff:",
    time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(tu[7])))
print("Letzte Modifikation:",
    time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(tu[8])))
