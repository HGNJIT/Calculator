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

#    def test_subtract_method_calculator(self):
#        self.assertEqual(self.calculator.subtract(4, 2), 2)

#    def test_multiply_method_calculator(self):
#        self.assertEqual(self.calculator.multiply(2, 2), 4)

#   def test_divide_method_calculator(self):
#       self.assertEqual(self.calculator.divide(8, 2), 4)

#    def test_square_method_calculator(self):
#        self.assertEqual(self.calculator.square(3), 9)

#    def test_sqrt_method_calculator(self):
#        self.assertEqual(self.calculator.sqrt(25), 5)


if __name__ == '__main__':
    unittest.main()
