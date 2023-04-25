import random

random.seed()


def task():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f"The task is: {a} + {b}")
    return a + b


def comment(iuser, solution):
    if iuser == solution:
        print(f"{iuser} is right!")
    else:
        print(f"{iuser} is wrong")


c = task()
z = c + 1
tries = 0
while z != c:
    tries = tries + 1
    try:
        z = int(input("Input your solution:"))
    except ValueError:
        print("Unexpected entry. Please try again.")
        continue
    comment(z, c)

print(f"The solution is: {c}")
if tries > 1:
    print(f"You needed {tries} tries.")
else:
    print(f"You needed {tries} try.")
