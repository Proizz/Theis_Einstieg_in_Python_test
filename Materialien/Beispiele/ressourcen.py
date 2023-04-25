x = 42
y = 56
print(f"x:{x}, y:{y}, identisch:{x is y}")

y = 42
print(f"x:{x}, y:{y}, identisch:{x is y}")

del y
print("x:", x)

del x
try:
    print("x:", x)
except:
    print("Fehler")    
