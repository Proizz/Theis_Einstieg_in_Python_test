z = ["Paris","Lyon","Metz"]
print("Liste:", z)

z.insert(1,"Nantes")
print("Einsetzen:", z)

z.sort()
print("Sortieren:", z)

z.reverse()
print("Umdrehen:", z)

such = "Nantes"
if such in z:
    z.remove(such)
    print("Entfernen:", z)

z.append("Paris")
print("Am Ende hinzu:", z)
print()

such = "Paris"
print(f"Anzahl gefunden:", z.count(such))

startpos = 0
while such in z[startpos:]:
    pos = z.index("Paris", startpos)
    print("Position:", pos)
    startpos = pos + 1
