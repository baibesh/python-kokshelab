class Calculator:
    def __init__(self):
        self.history: list = []

    def add(self, a, b):
        summ = a + b
        self.history.append(f"{a} + {b} = {summ}")
        return summ

    def subtract(self, a, b):
        summ = a - b
        self.history.append(f"{a} - {b} = {summ}")
        return summ

    def multiply(self, a, b):
        summ = a * b
        self.history.append(f"{a} * {b} = {summ}")
        return summ

    def divide(self, a, b):
        if b == 0:
            return "Нельзя делить на ноль"
        summ = a / b
        self.history.append(f"{a} / {b} = {summ}")
        return summ

    def power(self, a, b):
        summ = a**b
        self.history.append(f"{a} ** {b} = {summ}")
        return summ


calc = Calculator()
print(calc.add(2, 4))
print(calc.history)
