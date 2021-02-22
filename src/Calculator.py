class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = int(a) + int(b)
        return self.result

    def subtract(self, a, b):
        self.result = int(b) - int(a)
        return self.result

    def multiply(self, a, b):
        self.result = int(a) * int(b)
        return self.result

    def divide(self, a, b):
        self.result = round(float(b) / float(a), 9)
        return self.result

    def square(self, a):
        self.result = int(a) ** 2
        return self.result

    def sqrt(self, a):
        self.result = round(float(a) ** .5, 9)
        return self.result
