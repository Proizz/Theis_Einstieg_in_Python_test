def volumen(breite, laenge, tiefe, farbe):
    print("Werte:", breite, laenge, tiefe, farbe)
    print("Volumen:", breite * laenge * tiefe, "Farbe:", farbe)

volumen(4, 6, 2, "rot")
volumen(laenge=2, farbe="gelb", tiefe=7, breite=3)
volumen(5, tiefe=2, laenge=8, farbe="blau")
# volumen(3, tiefe=4, laenge=5, "schwarz")
