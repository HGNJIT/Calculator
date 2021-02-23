from Calculators.Add.Add import addition
from Calculators.Divide.Divide import division
from Calculators.Multiply.Multiply import multiplication
from Calculators.Square.Square import square
from Calculators.SquareRoot.SquareRoot import square_root
from Calculators.Subtract.Subtract import subtraction


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(int(a), int(b))
        return self.result

    def divide(self, a, b):
        self.result = round(division(int(b), int(a)))
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(int(b), int(a))
        return self.result

    def square(self, a):
        self.result = square(int(a))
        return self.result

    def sqrt(self, a):
        self.result = round(square_root(float(a)))
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(int(a), int(b))
        return self.result
