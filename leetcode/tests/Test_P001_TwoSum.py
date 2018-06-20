import unittest

from leetcode.src.P001_TwoSum import TwoSum


class TestTwoSum(unittest.TestCase):

    def test1(self):
        ts = TwoSum()
        self.assertEqual(ts.two_sum([1, 2, 3, 4, 5], 8), [2, 4])

    def test2(self):
        ts = TwoSum()
        self.assertEqual(ts.two_sum([1, 2, 3, 4, 5], 13), None)

    def test3(self):
        ts = TwoSum()
        self.assertEqual(ts.two_sum([1], 2), False)


if __name__ == '__main__':
    unittest.main()
