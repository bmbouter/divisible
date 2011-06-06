import unittest

from divisible import *

class TestDivisibilityFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_by_two(self):
        self.assertTrue(divisible_by_two(4))
        self.assertFalse(divisible_by_two(5))
        self.assertTrue(divisible_by_two(6548))
        self.assertFalse(divisible_by_two(23481))

    def test_by_three(self):
        self.assertTrue(divisible_by_three(9))
        self.assertFalse(divisible_by_three(11))
        self.assertTrue(divisible_by_three(36936))
        self.assertFalse(divisible_by_three(36937))

    def test_by_four(self):
        self.assertTrue(divisible_by_four(12))
        self.assertFalse(divisible_by_four(13))
        self.assertTrue(divisible_by_four(172980))
        self.assertFalse(divisible_by_four(172982))

    def test_by_five(self):
        self.assertTrue(divisible_by_five(10))
        self.assertFalse(divisible_by_five(13))
        self.assertTrue(divisible_by_five(1245))
        self.assertFalse(divisible_by_five(312))

    def test_by_six(self):
        self.assertTrue(divisible_by_six(18))
        self.assertFalse(divisible_by_six(20))
        self.assertTrue(divisible_by_six(2538))
        self.assertFalse(divisible_by_six(2534))

    def test_by_seven(self):
        self.assertTrue(divisible_by_seven(21))
        self.assertFalse(divisible_by_seven(25))
        self.assertTrue(divisible_by_seven(301))
        self.assertFalse(divisible_by_seven(305))

    def test_by_eight(self):
        self.assertTrue(divisible_by_eight(24))
        self.assertFalse(divisible_by_eight(27))
        self.assertTrue(divisible_by_eight(34840))
        self.assertFalse(divisible_by_eight(34844))

    def test_by_nine(self):
        self.assertTrue(divisible_by_nine(81))
        self.assertFalse(divisible_by_nine(85))
        self.assertTrue(divisible_by_nine(38115))
        self.assertFalse(divisible_by_nine(38117))

    def test_by_ten(self):
        self.assertTrue(divisible_by_ten(80))
        self.assertFalse(divisible_by_ten(84))
        self.assertTrue(divisible_by_ten(1230))
        self.assertFalse(divisible_by_ten(1238))

if __name__ == '__main__':
    unittest.main()
