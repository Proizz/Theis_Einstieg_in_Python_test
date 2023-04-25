def taxcalc(salary):
    tax = 0.22
    if salary < 2500:
        tax = 0.18
    return tax * salary


lSalary = (1800, 2200, 2500, 2900)
for sal in lSalary:
    myTax = taxcalc(sal)
    print(f"Your salary is {sal} €")
    print(f"Your tax is {myTax / sal} % which comes to {myTax} €")
    print(f"Your final salary is {sal - myTax} €")
