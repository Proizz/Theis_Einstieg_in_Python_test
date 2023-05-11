inch = 2.54
print(f"{'Inch':>5}{'cm':>8}")
for xi in range (15, 41, 5):
    xcm = xi * inch
    print(f"{xi:>5.1f} {xcm:>7.1f}")
