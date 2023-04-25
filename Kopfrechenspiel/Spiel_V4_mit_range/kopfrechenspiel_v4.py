import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print(f"The task is: {a} + {b}")
for i in range(1,10):
    print("Input the solution: ")
    z = int(input())

    if z == c:
        print(f"{z} is right!")
        break
    else:
        print(f"{z} is wrong")


print(f"The solution is: {c}")
