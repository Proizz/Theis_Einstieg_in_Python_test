"""
mental arithmetic game

1. Player has to solve up to 10 simple math problems with 2 numbers.
2. In the Beginning he can choose how many tasks he wants to solve.
3. Tasks contain all 4 basic arithmetic operations, which will be randomized.
4. The range of the numbers in Tasks depends on the arithmetic operation. (Multiplication with smaller numbers)
5. The player has maximum 3 tries per Task.
6. The number of solved tasks is tracked and reported at the end.

"""

import random


def task():
    operation = random.randint(1, 4)
    a = 0
    b = 0
    op = 0
    c = 0
    match operation:
        case 1:
            # Addition
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            op = "+"
            c = a + b
        case 2:
            # Subtraction
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            op = "-"
            c = a - b
        case 3:
            # Multiplication
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            op = "*"
            c = a * b
        case 4:
            # Division
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            op = "/"
            a = c * b

    print(f"The task is: {a} {op} {b}")
    return c


def ask_number_of_task():
    o_num_task = - 1
    while not 0 < o_num_task <= 10:
        try:
            o_num_task = int(input("How many tasks?(max. 10) "))
        except ValueError:
            print("Unexpected entry. Please try again.")
            continue
    return o_num_task


def comment(inp_user, i_solution):
    if inp_user == i_solution:
        print(f"{inp_user} is right!")
    else:
        print(f"{inp_user} is wrong")


def report_solved_task(i_solved, i_no_tasks):
    if i_solved > 1:
        print(f"You solved {i_solved} tasks out of {i_no_tasks}")
    else:
        print(f"You solved {i_solved} of task out of {i_no_tasks}")


if __name__ == '__main__':
    random.seed()
    solved = 0
    num_tasks = ask_number_of_task()
    for i in range(num_tasks):
        solution = task()
        for j in range(3):
            try:
                user_inp = int(input("Input your solution:"))
            except ValueError:
                print("Unexpected entry. Please try again.")
                continue
            comment(user_inp, solution)
            if user_inp == solution:
                solved = solved + 1
                break
        print(f"The solution is: {solution}")
    report_solved_task(solved, num_tasks)
    print("Github")