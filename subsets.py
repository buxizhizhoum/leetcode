#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        answer = []
        self.find_subsets(res, answer, nums)
        res.append([])
        return res

    def find_subsets(self, res, answer, nums):
        # this is to find all combinations,
        # so res.append(answer) not executed at here
        if len(nums) == 0:
            return

        for i in range(len(nums)):
            current_num = nums[i]

            res.append(answer + [current_num])
            self.find_subsets(res, answer + [current_num], nums[i+1:])


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    print(Solution().subsets(test_nums))
