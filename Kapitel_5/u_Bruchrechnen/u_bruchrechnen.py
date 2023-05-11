import random
import fractions


def ask_difficulty():
    # Ask for difficulty of the task and make sure it's a correct input.
    while True:
        try:
            diff = int(input("Your choice:1=Easy, 2=Medium, 3=Hard, 0=End "))
            if 0 <= diff <= 3:
                return diff
            else:
                raise
        except ValueError:
            print("Something with your input went wrong. Try again!")


def easy():
    # The task is to calculate a whole number
    # Calculating a whole number by multiply a random result with random nominator, to get a denominator
    n = random.randint(-10, 10)
    res = random.randint(-10, 10)
    z = n * res
    print(f"Calculate whole Number of: {z}/{n}")
    input()
    print(f"The result is: {res}")


def medium():
    # The task is to reduce a fraction
    z = 1
    n = 1
    # Calculate a nominator and denominator by randomly multiply with 3 factors with different probabilities
    probs = 2, 2, 2, 2, 3, 3, 3, 5, 5, 7
    for i in range(3):
        z *= random.choice(probs)
        n *= random.choice(probs)
    # Use fractions modul to simply reduce the fraction
    res = fractions.Fraction(z, n)
    print(f"Reduce the fraction:{z}/{n}")
    input()
    print(f"The result is: {res} ")


def hard():
    # The task is to solve a term with two fractions with a random operator.
    negs = -1, 1
    l_frac = []
    for i in range(2):
        n = random.randint(1, 10) * random.choice(negs)
        z = random.randint(1, 10) * random.choice(negs)
        l_frac.append(fractions.Fraction(z, n))

    ops = "/", "+", "-", "*"
    op = random.choice(ops)

    print(f"Calculate {l_frac[0].numerator}/{l_frac[0].denominator} {op} {l_frac[1].numerator}/{l_frac[1].denominator}")
    input()
    # Using the eval() function to create a legal term for python to calculate.
    res = fractions.Fraction(eval(f"({l_frac[0]}){op}({l_frac[1]})")).limit_denominator(100)
    print(f"The result is: {res} ")


if __name__ == "__main__":
    # Fractions training Main Routine
    while True:
        match ask_difficulty():
            case 0:
                # End the trainer.
                break
            case 1:
                easy()
            case 2:
                medium()
            case 3:
                hard()
