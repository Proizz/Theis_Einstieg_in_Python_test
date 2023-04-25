import fractions

z = 12
n = 28
print(f"Bruch: {z}/{n}")

b1 = fractions.Fraction(z, n)
print("Fraction-Objekt:", b1)
print(f"Zähler: {b1.numerator}, Nenner: {b1.denominator}")
print("Wert:", b1.numerator / b1.denominator)
print()

x = 2.375
print("Zahl:", x)
b2 = fractions.Fraction(x)
print("Fraction-Objekt:", b2)
