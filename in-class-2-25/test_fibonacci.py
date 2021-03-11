import unittest
import fibonacci as fib

class TestFib(unittest.TestCase):
    def test_fib8(self):
        check = fib.fibonacci(8)
        self.assertEqual(check, 21)

    def test_fib3(self):
        check = fib.fibonacci(3)
        self.assertEqual(check, 2)

    def test_fib7(self):
        check = fib.fibonacci(7)
        self.assertEqual(check, 13)

def test_fib():
    assert fib.fibonacci(8) == 21

def test_fib2():
    assert fib.fibonacci(3) == 2
