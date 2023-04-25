import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print(f"The task is: {a} + {b}")
print("Input the solution: ")
z = int(input())

if z == c:
    print(f"{z} is right!")
elif 100 < z or z < 0:
    print(f"{z} is very wrong!")
elif c-1 <= z <= c+1:
    print(f"{z} is close!")
else:
    print(f"{z} is wrong")


print(f"The solution is: {c}")
