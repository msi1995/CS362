import unittest
import leapyear2 as leap

class TestLeap(unittest.TestCase):

    def test_leap2100(self):
        check = leap.checkleap(2100)
        self.assertEqual(check, False) 