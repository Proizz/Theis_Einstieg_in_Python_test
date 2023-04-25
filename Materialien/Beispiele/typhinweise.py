a:int = 42
b:float = 42.5
c:str = "Hallo"
d:bool = True
print("Variablen:", a, b, c, d)

def mittelwert(x:float, y:float) -> float:
    ergebnis = (x+y) / 2
    return ergebnis

print("Mittelwert:", mittelwert(3.4, 9.4))
