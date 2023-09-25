import random


class Game:
    def __init__(self):
        random.seed()
        self.solved = 0
        self.number_of_task = -1
        while self.number_of_task < 1 or self.number_of_task > 10:
            try:
                print("How many tasks?")
                self.number_of_task = int(input())
            except:
                continue

    def play(self):
        for i in range(self.number_of_task):
            t = Task(i + 1, self.number_of_task)
            print(t)
            self.solved += t.answer()

    def __str__(self):
        return f"Solved: {self.solved} of {self.number_of_task}."


class Task:
    def __init__(self, i, number_of_task):
        self.nr = i
        self.numbers_of_task = number_of_task

    def __str__(self):
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
        self.result = c
        return f"Task {self.nr} of {self.numbers_of_task} is: {a} {op} {b}"

    def answer(self):
        try:
            if self.result == int(input()):
                print(f"{self.nr}: ***Well Done***")
                return 1
            else:
                raise
        except:
            print(f"{self.nr}: ***Wrong***")
            return 0


if __name__ == '__main__':
    s = Game()
    s.play()
    print(s)
