import unittest
import fibonacci as fib

class TestFib(unittest.TestCase):
    def test_fib8(self):
        w = fib.fibonacci(8)
        self.assertEqual(w, 21)

    def test_fib3(self):
        w = fib.fibonacci(3)
        self.assertEqual(w, 2)

    def test_fib7(self):
        w = fib.fibonacci(7)
        self.assertEqual(w, 13)

def test_fib():
    assert fib.fibonacci(8) == 21

def test_fib2():
    assert fib.fibonacci(3) == 2
