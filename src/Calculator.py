class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = int(a) + int(b)
        return self.result

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def square(self, a):
        return a ** 2

    def sqrt(self, a):
        return a ** .5
