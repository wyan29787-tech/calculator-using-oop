import unittest
from calcu import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Set up test calculator instance before each test
        self.calc = Calculator()

    def test_add(self):

        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_calculate_invalid_operation(self):
        """Test that invalid operation raises ValueError"""
        with self.assertRaises(ValueError):
            self.calc.calculate(10, 5, "invalid")

    def test_calculate_case_insensitive(self):
        self.assertEqual(self.calc.calculate(10, 5, "ADD"), 15)
        self.assertEqual(self.calc.calculate(10, 5, "Subtract"), 5)


if __name__ == "__main__":
    unittest.main()
