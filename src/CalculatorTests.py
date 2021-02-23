import unittest
from Calculators.Calculator import Calculator
from CSVReader.CSVReader import CSVReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        reader = CSVReader('/src/Data/Addition/Addition.csv').data
        print('********** Testing Addition **********')
        for row in reader:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Pass")

    def test_divide_method_calculator(self):
        reader = CSVReader('/src/Data/Division/Division.csv').data
        print('********** Testing Division **********')
        for row in reader:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), round(float(row['Result'])))
        print("Pass")

    def test_multiply_method_calculator(self):
        reader = CSVReader('/src/Data/Multiplication/Multiplication.csv').data
        print('********** Testing Multiplication **********')
        for row in reader:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Pass")

    def test_square_method_calculator(self):
        reader = CSVReader('/src/Data/Square/Square.csv').data
        print('********** Testing Squaring **********')
        for row in reader:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
        print("Pass")

    def test_sqrt_method_calculator(self):
        reader = CSVReader('/src/Data/SquareRoot/SquareRoot.csv').data
        print('********** Testing Square Root **********')
        for row in reader:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), round(float(row['Result'])))
        print("Pass")

    def test_subtract_method_calculator(self):
        reader = CSVReader('/src/Data/Subtraction/Subtraction.csv').data
        print('********** Testing Subtraction **********')
        for row in reader:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Pass")


if __name__ == '__main__':
    unittest.main()
