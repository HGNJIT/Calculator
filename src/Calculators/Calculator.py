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

    # Send the received values to the addition function withing the Add class
    def add(self, a, b):
        self.result = addition(int(a), int(b))
        return self.result

    # Send the received values to the division function withing the Divide class
    def divide(self, a, b):
        self.result = round(division(int(b), int(a)))
        return self.result

    # Send the received values to the multiplication function withing the Multiply class
    def multiply(self, a, b):
        self.result = multiplication(int(b), int(a))
        return self.result

    # Send the received values to the squaring function withing the Square class
    def square(self, a):
        self.result = square(int(a))
        return self.result

    # Send the received values to the SquareRoot function withing the Square class
    def sqrt(self, a):
        self.result = round(square_root(float(a)))
        return self.result

    # Send the received values to the Subtraction function withing the Subtract class
    def subtract(self, a, b):
        self.result = subtraction(int(a), int(b))
        return self.result
