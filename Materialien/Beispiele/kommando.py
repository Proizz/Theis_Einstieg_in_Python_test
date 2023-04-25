import sys
print("Parameter:", sys.argv)
print("Anzahl:", len(sys.argv))

summe = 0
for i in sys.argv[1:]:
    try:
        summe += float(i)
    except:
        print(f"Fehler bei Parameter {i}")
print("Summe:", summe)
