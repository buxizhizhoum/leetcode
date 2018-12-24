#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.ans(nums, target)

    def ans(self, nums, target):
        res = set()
        cache = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                tmp_sum = nums[i] + nums[j]
                if cache.get(tmp_sum) is None:
                    cache[tmp_sum] = [(i, j)]
                else:
                    cache[tmp_sum].append((i, j))

        for k in range(len(nums)):
            for l in range(k+1, len(nums)):
                tmp_rest = target - (nums[k] + nums[l])
                res_items = cache.get(tmp_rest)
                if res_items is not None:
                    for item in res_items:
                        # if element not used before
                        if k not in item and l not in item:
                            # add result item to set
                            res.add(tuple(sorted([nums[item[0]], nums[item[1]], nums[k], nums[l]])))

        return [list(item) for item in res]


if __name__ == "__main__":
    test_nums = [1, 0, -1, 0, -2, 2]
    test_target = 0
    print(Solution().fourSum(test_nums, test_target))

