import unittest

from leetcode.src.P002_AddTwoNumbers import AddTwoNumbers


class TestTwoSum(unittest.TestCase):

    def test1(self):
        atn = AddTwoNumbers()
        self.assertEqual(ts.two_sum([1, 2, 3, 4, 5], 8), [2, 4])

    def test2(self):
        atn = AddTwoNumbers()
        self.assertEqual(ts.two_sum([1, 2, 3, 4, 5], 13), None)

    def test3(self):
        atn = AddTwoNumbers()
        self.assertEqual(ts.two_sum([1], 2), False)


if __name__ == '__main__':
    unittest.main()
