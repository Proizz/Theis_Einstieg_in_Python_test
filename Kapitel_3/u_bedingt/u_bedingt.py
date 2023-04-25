def taxcalc(salary):
    return 0.18 * salary if salary < 2500 else 0.22 * salary


lSalary = (1800, 2200, 2500, 2900)
for sal in lSalary:
    myTax = taxcalc(sal)
    print(f"Your salary is {sal} €")
    print(f"Your tax is {myTax / sal} % which comes to {myTax} €")
    print(f"Your final salary is {sal - myTax} €")
