import unittest
from Calculator import Calculator
from CSVReader import CSVReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        reader = CSVReader('/src/Addition.csv').data
        for row in reader:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_subtract_method_calculator(self):
        reader = CSVReader('/src/Subtraction.csv').data
        for row in reader:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_multiply_method_calculator(self):
        reader = CSVReader('/src/Multiplication.csv').data
        for row in reader:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_divide_method_calculator(self):
        reader = CSVReader('/src/Division.csv').data
        for row in reader:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), round(float(row['Result']), 9))

    def test_square_method_calculator(self):
        reader = CSVReader('/src/Square.csv').data
        for row in reader:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))

    def test_sqrt_method_calculator(self):
        reader = CSVReader('/src/SquareRoot.csv').data
        for row in reader:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), round(float(row['Result']), 9))


if __name__ == '__main__':
    unittest.main()
