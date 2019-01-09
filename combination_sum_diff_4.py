#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.basic(nums, target)

    def basic(self, nums, target):
        # return self._recursion(nums, target, 0)
        # return self._recursion(nums, target)
        memo = [None for _ in range(target+1)]
        return self._recursion_memo(nums, target, memo)


    # def _recursion(self, nums, target, index):
    #     if target == 0:
    #         return 1
    #
    #     if index > len(nums) - 1:
    #         return 0
    #
    #     res = 0
    #     for i in range(len(nums)):
    #         capacity = target // nums[index]
    #         for j in range(capacity + 1):
    #             if target - j * nums[i] >= 0:
    #                 res += self._recursion(nums, target - j * nums[i], index+1)
    #                 # res += self._recursion(nums, target - j * nums[i], index)
    #
    #     return res

    def _recursion(self, nums, target):
        """
        comb[target] = sum(comb[target - nums[i]])
        :param nums:
        :param target:
        :return:
        """
        if target == 0:
            return 1

        res = 0
        for i in range(len(nums)):
            # 如果能放下就先放下这个再考虑下一次递归，下一次i又是从0开始
            # 不是先放当前的这个一直到放不下当前的为止
            # todo: recursion tree
            # 排列问题递归树右侧不会随着递归深度增加减少，组合可以在递归数开始时候
            # 在[index:]区间继续展开
            if target - nums[i] >= 0:
                res += self._recursion(nums, target - nums[i])

        return res

    def _recursion_memo(self, nums, target, memo):
        if target == 0:
            return 1

        if memo[target] is not None:
            return memo[target]

        res = 0
        for i in range(len(nums)):
            # 如果能放下就先放下这个再考虑下一次递归，下一次i又是从0开始
            # 不是先放当前的这个一直到放不下当前的为止
            # todo: recursion tree
            # 排列问题递归树右侧不会随着递归深度增加减少，组合可以在递归数开始时候
            # 在[index:]区间继续展开
            if target - nums[i] >= 0:
                res += self._recursion_memo(nums, target - nums[i], memo)

        memo[target] = res
        return res


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    test_target = 4

    test_nums = [4, 2, 1]
    test_target = 32

    print(Solution().combinationSum4(test_nums, test_target))



