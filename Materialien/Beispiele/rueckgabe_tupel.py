import math
def kreis(radius):
    flaeche = math.pi * radius * radius
    umfang = 2 * math.pi * radius
    return flaeche, umfang

f, u = kreis(3)
print(f"Fläche: {round(f,3)}, Umfang: {round(u,3)}")
x = kreis(3)
print(f"Fläche: {round(f,3)}, Umfang: {round(u,3)}")
