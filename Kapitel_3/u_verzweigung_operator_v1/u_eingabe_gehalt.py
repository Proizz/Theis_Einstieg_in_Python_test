
salary = float(input("Insert your salary: "))
married = input("Are you married?(y/n)")


if salary > 4000 and married == "n":
    tax = 0.26
elif salary <= 4000 and married == "y":
    tax = 0.18
else:
    tax = 0.22
print(f"Your tax is: {salary * tax}")
