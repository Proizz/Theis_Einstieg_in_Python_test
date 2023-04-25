z = ["Paris","Lyon","Reims","Nice"]
print("Liste:", z)

z[2] = "Lens"
print("Element ersetzt:", z)

z[1:3] = ["Nancy","Metz","Gap"]
print("Slice durch Liste ersetzt:", z)

del z[2:]
print("Slice entfernt:", z)

z[0] = ["Paris-Nord","Paris-Sud"]
print("Element durch Liste ersetzt:", z)
