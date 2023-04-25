inch_to_cm = 2.54
inch = 1
while inch != 0:
    try:
        inch = float(input("Please insert length in inch: "))
    except ValueError:
        print("Wrong entry! Try again.")
        continue

    print(f"{inch} Inch is converted to {inch_to_cm * inch} cm.")
