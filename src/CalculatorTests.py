import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 4)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
