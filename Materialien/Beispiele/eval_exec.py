def rechnung1(a, b):
    return a + b

def rechnung2(a, b):
    return a * b

for i in 1, 2:
    print(eval("rechnung" + f"{i}" + "(3,4)"))

for i in 1, 2:
    exec("print(rechnung" + f"{i}" + "(3,4))")
