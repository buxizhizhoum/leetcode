#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.dfs(nums)
        cache = [-1 for _ in nums]
        # return self.dfs_cache(nums, cache, 0)
        return self.dp(nums)

    def dfs(self, nums):
        """
        time limit exceeded
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        res = -1
        for i in range(len(nums)):
            # if i + 2 <= len(nums) - 1:
                res = max(res, nums[i] + self.dfs(nums[i+2:]))
            # else:
            #     res = max(res, nums[i])
        return res

    def dfs_1(self, nums, index):
        # todo: attention the difference between dfs and dfs_1
        if index >= len(nums):
            return 0

        res = -1
        for i in range(index, len(nums)):
            res = max(res, nums[i] + self.dfs_1(nums, i+2))
        return res

    def dfs_cache(self, nums, cache, index):
        # cache the result of nums[index:], index is the key
        if index < len(cache) and cache[index] != -1:
            return cache[index]

        if index >= len(nums):
            return 0
        if index == len(nums) - 1:
            return nums[index]

        res = -1
        for i in range(index, len(nums)):
            res = max(res, nums[i] + self.dfs_cache(nums, cache, i+2))
            # todo: attention it is index not i
            cache[index] = res
        return res

    @staticmethod
    def dp(nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        cache = [-1 for _ in nums]

        cache[-1] = nums[-1]
        cache[-2] = max(nums[-2:])

        for i in range(len(nums) - 3, -1, -1):
            cache[i] = nums[i] + max(cache[i+2:])

        return max(cache)





if __name__ == "__main__":
    test_nums = [1, 2, 3, 1]
    test_nums = [2, 7, 9, 3, 1]
    # test_nums = [1, 2]
    test_nums = [0]
    test_nums = [1,3,1]
    test_nums = [4,1,2,7,5,3,1]
    print(Solution().rob(test_nums))
    print(Solution().dfs_1(test_nums, 0))




