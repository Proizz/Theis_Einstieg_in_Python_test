def volumen(breite, laenge, tiefe=1, farbe="schwarz"):
    print("Werte:", breite, laenge, tiefe, farbe)
    print("Volumen:", breite * laenge * tiefe, "Farbe:", farbe)

volumen(4, 6, 2, "rot")
volumen(2, 12, 7)
volumen(5, 8)
volumen(4, 7, farbe="rot")
