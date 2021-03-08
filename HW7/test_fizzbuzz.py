import unittest
import fizzbuzz as fb

class TestFizz(unittest.TestCase):

    def test_fizz3(self):
        check = fb.fizzbuzz(3)
        self.assertEqual(check, "Fizz") 

    def test_fizz10(self):
        check = fb.fizzbuzz(10)
        self.assertEqual(check, "Buzz") 

    def test_fizz15(self):
        check = fb.fizzbuzz(15)
        self.assertEqual(check, "FizzBuzz")

    def test_fizz7(self):
        check = fb.fizzbuzz(7)
        self.assertEqual(check, 7)
