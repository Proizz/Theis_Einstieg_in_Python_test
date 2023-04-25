print("Datum-Entry-Programm")

# input datum
day = int(input("Input Day:"))
month = int(input("Input Month: "))
year = int(input("Input Year: "))

# check max day of the month
if 0 < month <= 12:
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            max_day = 31
        case 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                max_day = 29
            else:
                max_day = 28
        case _:
            max_day = 30
    print(f"The month has {max_day} days.")
    if 0 < day <= max_day:
        print(f"The datum {day}.{month}.{year} is a correct datum.")
    else:
        print(f"The datum {day}.{month}.{year} is a wrong datum.")
else:
    print(f"The datum {day}.{month}.{year} is a wrong datum.")


