#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = self.recursion(nums)
        return self.remove_duplicates(res)

    def recursion(self, nums):
        res = []
        answer = []
        return self._recursion(nums, res, answer)

    def _recursion(self, nums, res, answer):
        if len(nums) == 0:
            res.append(answer)
            return res

        for i in range(len(nums)):
            self._recursion(nums[:i] + nums[i+1:], res, [nums[i]] + answer)

        return res

    def remove_duplicates(self, data):
        res = set(map(tuple, data))
        return list(map(list, res))


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permuteUnique(nums))






