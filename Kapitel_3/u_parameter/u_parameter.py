def steuer(salary):
    tax = 0.22
    if salary < 2500:
        tax = 0.18
    print(f"Your salary is {salary} €")
    print(f"Your tax is {tax*100} % which comes to {tax * salary} €")
    print(f"Your final salary is {salary - tax * salary} €")


lsalary = (1800, 2200, 2500, 2900)
for salary in lsalary:
    steuer(salary)
