import unittest
import HW4

class Test(unittest.TestCase):
    ##cube tests
    def test_cubeVolume(self):
        side = 27
        result = HW4.cubeVolume(side)
        self.assertEqual(result, 19683)

    def test_cubeVolumeNeg(self):
        side = -5
        result = HW4.cubeVolume(side)
        self.assertEqual(result, 0)

    def test_cubeVolumeString(self):
        side = "dog"
        result = HW4.cubeVolume(side)
        self.assertEqual(result, 0)


        ##average of a list tests
    def test_averageOfList(self):
        list = [10, 10, 10]
        result = HW4.findAvg(list)
        self.assertEqual(result, 10)

    def test_averageEmptyList(self):
        list = []
        result = HW4.findAvg(list)
        self.assertEqual(result, 0)

    def test_averageOfList(self):
        list = [50,50,100,100]
        result = HW4.findAvg(list)
        self.assertEqual(result, 75)


         ##make full name from first and last tests
    def test_makeFullName(self):
        first = "John"
        last = "Smith"
        result = HW4.makeFullName(first,last)
        self.assertEqual(result, 'John Smith')

    def test_makeFullNameZeroes(self):
        first = 0
        last = 0
        result = HW4.makeFullName(first,last)
        self.assertEqual(result, "0 0")

    def test_makeFullNameEmptyStrings(self):
        first = ""
        last = ""
        self.assertEqual(result, " ")


