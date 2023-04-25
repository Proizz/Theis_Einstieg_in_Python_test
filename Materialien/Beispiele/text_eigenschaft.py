tx = "Das"
print("Text:", tx)
print("Typ:", type(tx))
print("Anzahl der Zeichen:", len(tx))
for z in tx:
    print(z)
for i in range(len(tx)):
    print(f"{i}: {tx[i]}")

tx = 'Auch das ist eine Zeichenkette'
print(tx)

tx = """Diese Zeichenkette
        steht in
        mehreren Zeilen"""
print(tx)

tx = 'Hier sind "doppelte Hochkommata" gespeichert'
print(tx)
