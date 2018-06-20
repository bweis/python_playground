class TwoSum:
    def two_sum(self, nums, target):
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        Example:

        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].

        :param nums: List of integers
        :param target: Integer to sum to
        :return:
            If successful, list of two indices whose values sum to target
            If no solution, None
            If invalid nums arg, False
        """
        if len(nums) <= 1:
            return False
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [dic[n], i]
            else:
                dic[target - n] = i
