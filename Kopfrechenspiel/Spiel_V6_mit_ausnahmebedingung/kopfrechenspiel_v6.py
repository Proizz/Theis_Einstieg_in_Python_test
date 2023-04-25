import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print(f"The task is: {a} + {b}")
z = c + 1
tries = 0
while z != c:
    tries = tries + 1
    try:
        z = int(input("Input your solution:"))
    except ValueError:
        print("Unexpected entry. Please try again.")
        continue

    if z == c:
        print(f"{z} is right!")
    else:
        print(f"{z} is wrong")



print(f"The solution is: {c}")
if tries > 1:
    print(f"You needed {tries} tries.")
else:
    print(f"You needed {tries} try.")
