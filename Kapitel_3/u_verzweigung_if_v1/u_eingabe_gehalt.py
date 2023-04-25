
salary = float(input("Insert your salary: "))
if salary > 2500:
    tax = 0.22
else:
    tax = 0.18
print(f"Your tax is: {salary * tax}")
