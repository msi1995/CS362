import unittest
import fizzbuzz as fb

class TestFizz(unittest.TestCase):

    def fizz3(self):
        check = fb.fizzbuzz(3)
        self.assertEqual(check, "Fizz") 

