import unittest
import leapyear2 as leap

class TestLeap(unittest.TestCase):

    def test_leap2100(self):
        check = leap.checkleap(2100)
        self.assertEqual(check, False) 

    def test_leap2000(self):
        check = leap.checkleap(2000)
        self.assertEqual(check, True) 

    def test_leap2007(self):
        check = leap.checkleap(2007)
        self.assertEqual(check, False) 