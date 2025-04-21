import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(2, 2), 4)
        self.assertEqual(calculator.addition(-2, 2), 0)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(4, 2), 2)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(2, 2), 4)

    def test_division(self):
        self.assertEqual(calculator.division(2, 2), 1)

        with self.assertRaises(ValueError):
            calculator.division(2, 0)

    def test_power(self):
        self.assertEqual(calculator.power(1, 2), 1)

        with self.assertRaises(ValueError):
            calculator.power(2, -2)

    def test_sqroot(self):
        self.assertEqual(calculator.sqroot(4), 2)

        with self.assertRaises(ValueError):
            calculator.sqroot(-2)


if __name__ == "__main__":
    unittest.main()
