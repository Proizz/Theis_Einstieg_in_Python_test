import random
random.seed()

summe = 0
while summe < 30:
    zzahl = random.randint(1,8)
    summe = summe + zzahl
    print(f"Zahl: {zzahl}, Zwischensumme: {summe}")
