tx = "Das ist ein Satz"
print("Text:", tx)
wortliste = tx.split()
for i in range(0, len(wortliste)):
    print("Element:", i, wortliste[i])
print()

tx = "Maier;Hans;6714;3.500,00;15.03.62"
print("Text:", tx)
wortliste = tx.split(";")
for i in range(0, len(wortliste)):
    print("Element:", i, wortliste[i])
