import unittest
import calculator

class Test(unittest.TestCase):
    def test_addition(self):
        a = 1
        b = 2
        result = calculator.add(a,b)
        self.assertEqual(result, 3)

    def test_substraction(self):
        a = 2
        b = 1
        result = calculator.subtract(a,b)
        self.assertEqual(result, 1)

    def test_multiply(self):
        a = 5
        b = 7
        result = calculator.multiply(a,b)
        self.assertEqual(result, 35)

    def test_divide(self):
        a = 8
        b = 2
        result = calculator.divide(a,b)
        self.assertEqual(result, 4)